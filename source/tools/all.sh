set -e
cd /home/claude/atlas
python3 tools/build_sites.py | tail -1 | cut -c1-80
python3 tools/drive.py > /dev/null
python3 tools/padus.py
python3 tools/leads.py | cut -c1-60
python3 tools/make.py
python3 tools/export.py
mkdir -p dist/site && cp dist/Lost-and-Hidden-Atlas.html dist/site/index.html
(cd dist/site && rm -f ../lost-hidden-atlas-website.zip && zip -q ../lost-hidden-atlas-website.zip index.html)
node -e "const fs=require('fs'); new Function(fs.readFileSync('src/app.js','utf8')); console.log('syntax ok')"
ls -la dist | tail -6
