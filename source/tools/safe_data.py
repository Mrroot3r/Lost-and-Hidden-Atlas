#!/usr/bin/env python3
"""A place list is data, and this proves it before anything runs it.
   python3 tools/safe_data.py [folder]      reads every data_*.py and bricks_*.py in the folder (default: this one)

Why it exists. Research sessions write these files with nobody watching, their pull requests merge by themselves, and
the build then runs each file as Python, on GitHub, with the right to publish the site. A session reads pages from all
over the web while it works, and a page can be written to talk a model into things. So the files are held to what a
place list needs and no more, and they are READ here, never run: build_sites.py and check.py call must() before they
import a single one.

What a place list may hold:
  - comments, and  from data_<name> import NAME, ...   (only names that the other list itself defines);
  - NAME = value, NAME += value, NAME[key] = value, assert, and  NAME.update(...)  on a line of its own;
  - small helpers:  def L(t,u): return [t,u]   or a lambda, made of the same things;
  - values: text, numbers, lists, tuples, dicts, sets, + - * / %, comparisons, comprehensions, f-strings, a[b];
  - calls to its own helpers and the imported ones, to  dict list tuple set str int float len sorted min max round
    range zip enumerate sum any all abs bool,  and to the methods in METHODS below.
Nothing else: no import of anything but another place list, no attribute read (x.y) except to call one of those
methods, no name that the file did not make itself, no class, loop, with, try, global, or decorator.
If a list needs more than this, the thing it needs belongs in a tool, not in the list."""
import ast,sys,os,glob,re,builtins

BUILTINS={'dict','list','tuple','set','str','int','float','len','sorted','min','max','round','range','zip','enumerate','sum','any','all','abs','bool','id','True','False','None'}      # id: N(id, name, ...) uses it as an argument's name, and the builtin is harmless
METHODS={'replace','update','join','split','strip','lstrip','rstrip','lower','upper','title','capitalize','append','extend','get','items','keys','values','copy','startswith','endswith','setdefault'}
# Python's own names (eval, open, getattr, ...). A list may not give any of them a new meaning either: a name bound inside a
# comprehension or as a helper's argument is not the name the rest of the file sees, so "bound somewhere" would prove nothing.
PYTHON=set(dir(builtins))-BUILTINS
MODULE=re.compile(r'^(data|bricks)_[a-z0-9_]+$')
EXPR=(ast.Constant,ast.Name,ast.List,ast.Tuple,ast.Dict,ast.Set,ast.BinOp,ast.UnaryOp,ast.BoolOp,ast.Compare,ast.IfExp,ast.Subscript,ast.Slice,
      ast.Starred,ast.JoinedStr,ast.FormattedValue,ast.ListComp,ast.SetComp,ast.DictComp,ast.GeneratorExp,ast.comprehension,ast.Lambda,
      ast.keyword,ast.Call,ast.Attribute,ast.arguments,ast.arg,ast.expr_context,ast.operator,ast.unaryop,ast.boolop,ast.cmpop)
TOP=(ast.ImportFrom,ast.Assign,ast.AugAssign,ast.FunctionDef,ast.Assert,ast.Expr)
INDEF=(ast.Return,ast.Assign,ast.AugAssign,ast.If,ast.Expr,ast.Assert)

def top_names(tree):
    """the names a list defines at its top level: what another list may import from it"""
    out=set()
    for n in tree.body:
        if isinstance(n,ast.FunctionDef): out.add(n.name)
        elif isinstance(n,ast.ImportFrom): out.update(a.asname or a.name for a in n.names)
        elif isinstance(n,(ast.Assign,ast.AugAssign)):
            for t in (n.targets if isinstance(n,ast.Assign) else [n.target]):
                out.update(x.id for x in ast.walk(t) if isinstance(x,ast.Name))
    return out

def check_file(path,cache=None):
    """the problems in one file, as a list of lines; empty when the file is only data"""
    cache={} if cache is None else cache; name=os.path.basename(path); folder=os.path.dirname(path); bad=[]
    def no(node,why): bad.append('%s line %d: %s'%(name,getattr(node,'lineno',0),why))
    try: tree=ast.parse(open(path,encoding='utf-8').read(),name)
    except SyntaxError as e: return ['%s line %s: not Python that can be read (%s)'%(name,e.lineno,e.msg)]
    def exports(mod):
        if mod not in cache:
            f=os.path.join(folder,mod+'.py')
            try: cache[mod]=top_names(ast.parse(open(f,encoding='utf-8').read()))
            except Exception: cache[mod]=None
        return cache[mod]
    # every name the file makes for itself, anywhere in it: a name it uses must be one of these or a plain builtin,
    # and none of them may be one of Python's own names
    bound=set()
    def bind(node,nm):
        if nm.startswith('__') or nm in PYTHON: no(node,"gives a meaning to '%s', which is one of Python's own names"%nm)
        bound.add(nm)
    for n in ast.walk(tree):
        if isinstance(n,ast.Name) and isinstance(n.ctx,(ast.Store,ast.Del)): bind(n,n.id)
        elif isinstance(n,ast.FunctionDef): bind(n,n.name)
        elif isinstance(n,ast.arg):
            bind(n,n.arg)
            if n.annotation is not None: no(n,'an annotation on the argument %s (Python runs annotations)'%n.arg)
        elif isinstance(n,ast.ImportFrom):
            for a in n.names: bind(n,a.asname or a.name)
    def expr(e):
        for n in ast.walk(e):
            if not isinstance(n,EXPR): no(n,'%s is not something a place list may hold'%type(n).__name__); continue
            if isinstance(n,ast.Name):
                if n.id.startswith('__') or (isinstance(n.ctx,ast.Load) and n.id not in bound and n.id not in BUILTINS): no(n,"the name '%s' is not made in this file and is not one of the plain builtins a list may use"%n.id)
            elif isinstance(n,ast.Attribute): pass          # judged where it is called, below
            elif isinstance(n,ast.Call):
                f=n.func
                if isinstance(f,ast.Attribute):
                    if f.attr not in METHODS: no(n,"calls .%s(), which a place list may not (allowed: %s)"%(f.attr,' '.join(sorted(METHODS))))
                elif not isinstance(f,ast.Name): no(n,'calls something that is not a plain name')
        calls={id(n.func) for n in ast.walk(e) if isinstance(n,ast.Call)}
        for n in ast.walk(e):
            if isinstance(n,ast.Attribute) and id(n) not in calls: no(n,"reads .%s: a place list may not reach into a value except to call one of the allowed methods"%n.attr)
    def target(t):
        for n in ast.walk(t):
            if isinstance(n,ast.Attribute): no(n,'assigns to an attribute (.%s)'%n.attr)
        if isinstance(t,(ast.Name,ast.Tuple,ast.List)): pass          # the names themselves were judged where they were bound, above
        elif isinstance(t,ast.Subscript): expr(t)
        else: no(t,'assigns to something that is not a name or NAME[key]')
    def stmt(n,inside):
        if isinstance(n,ast.Expr):
            if isinstance(n.value,ast.Constant) and isinstance(n.value.value,str): return          # a docstring
            if isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Attribute): expr(n.value); return      # X.update({...})
            no(n,'a bare expression that does nothing a place list needs'); return
        if isinstance(n,ast.Assign):
            for t in n.targets: target(t)
            expr(n.value); return
        if isinstance(n,ast.AugAssign): target(n.target); expr(n.value); return
        if isinstance(n,ast.Assert):
            expr(n.test)
            if n.msg is not None: expr(n.msg)
            return
        if inside and isinstance(n,ast.Return):
            if n.value is not None: expr(n.value)
            return
        if inside and isinstance(n,ast.If):
            expr(n.test)
            for x in n.body+n.orelse: stmt(x,True)
            return
        if not inside and isinstance(n,ast.ImportFrom):
            if n.level or not n.module or not MODULE.match(n.module): no(n,"imports from '%s': a place list may import only from another place list (data_<name>)"%(('.'*n.level)+(n.module or ''))); return
            have=exports(n.module)
            if have is None: no(n,"imports from %s, which is not a file in this folder that can be read"%n.module); return
            for a in n.names:
                if a.name=='*' or a.name.startswith('_') or a.name not in have: no(n,"imports '%s' from %s, which that list does not define at its top level"%(a.name,n.module))
            return
        if not inside and isinstance(n,ast.FunctionDef):
            if n.decorator_list: no(n,'a decorator on %s()'%n.name)
            if n.returns is not None or getattr(n,'type_params',None): no(n,'an annotation on %s() (Python runs annotations)'%n.name)
            for d in n.args.defaults+[d for d in n.args.kw_defaults if d is not None]: expr(d)
            for x in n.body:
                if isinstance(x,INDEF): stmt(x,True)
                else: no(x,'%s inside %s(): a helper may only assign, test with if, and return'%(type(x).__name__,n.name))
            return
        no(n,'%s is not something a place list may hold'%type(n).__name__)
    for n in tree.body: stmt(n,False)
    return bad

def check_folder(folder):
    cache={}; bad=[]; files=sorted(glob.glob(os.path.join(folder,'data_*.py'))+glob.glob(os.path.join(folder,'bricks_*.py')))
    for f in files: bad+=check_file(f,cache)
    return files,bad

def must(folder):
    """stop the program, saying why, unless every place list in the folder is only data. Call it before importing any."""
    files,bad=check_folder(folder)
    if bad:
        sys.exit('STOP: a place list holds more than data, so nothing was run (tools/safe_data.py explains the rule):\n  '+'\n  '.join(bad[:40])+('\n  ... and %d more'%(len(bad)-40) if len(bad)>40 else ''))
    return len(files)

if __name__=='__main__':
    folder=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.abspath(__file__))
    files,bad=check_folder(folder)
    for b in bad: print(b)
    print('%d place lists read, %s'%(len(files),'all of them only data' if not bad else '%d problem(s)'%len(bad)))
    sys.exit(1 if bad else 0)
