# Add places with your own Claude

The Lost & Hidden Atlas grows by research sessions. A Claude session picks a piece of ground, reads the sources, looks at
every pin on the aerial photo, writes the places up and sends them in. If you have Claude with Claude Code, yours can do
the same, on your own account, for your own town or anywhere it likes.

If you only want to tell us about one place, you do not need any of this: open the Atlas, tap "+ Add", drop a pin, write
a line, and tap "Suggest it to the Atlas".

## What you need

- A free GitHub account.
- Claude with Claude Code (on the web, in the desktop app or in a terminal), connected to that GitHub account.

## The steps

1. **Make your own copy.** On this repository's page on GitHub, press **Fork**. That gives you a copy under your own
   name. Nothing you do there can change the Atlas.
2. **Give Claude your copy.** Start a Claude Code session on your copy of the repository.
3. **Say what to do.** The one word `go` starts a session that draws its own ground at random. To aim it, say where:
   `go: Troy, New York` or `go: Bucks County, Pennsylvania`. For more control, paste the prompt from
   [PROMPTS.md](PROMPTS.md).
4. **Let it work.** A session takes an hour or two and does not need you. It follows the same rules as every other
   session: every fact from a source it opened, every pin looked at on the aerial, who owns the land and how to reach
   it legally, and nothing about getting past a fence or into a sealed building.
5. **It sends its work in.** The session finishes by opening a pull request from your copy to this repository. GitHub
   builds and checks it by itself. The owner of the Atlas then looks at it and merges it, and the places are on the map
   about a minute later.

## What to expect

- Work from a copy always waits for the owner to look at it. That can take a few days.
- The owner may change or leave out places: a pin that cannot be confirmed, land with no legal way in, a source that
  does not say what the entry says.
- Everything in this repository is public. Do not put anything private in a place entry: no names of private
  landowners, no home addresses, nothing about yourself.
- Two people's sessions can pick the same ground. The session looks at the open pull requests here before it starts,
  and the checks refuse the same place twice.

## For the Claude session reading this

You are working in a copy (a fork) of `Mrroot3r/Lost-and-Hidden-Atlas`. Do everything as `CLAUDE.md` and `PROMPTS.md`
say, with these differences:

- Push your branch to the copy you were given (`origin`), then open the pull request **into
  `Mrroot3r/Lost-and-Hidden-Atlas`, branch `main`**:
  `gh pr create --repo Mrroot3r/Lost-and-Hidden-Atlas --base main --head <copy owner>:<branch>`.
- Before anything else, bring the copy's `main` up to date with the Atlas, or you will research ground that is
  already done and your branch will not fit: `git remote add upstream https://github.com/Mrroot3r/Lost-and-Hidden-Atlas.git`,
  `git fetch upstream main`, `git push origin upstream/main:refs/heads/main`. Then run setup and work as usual.
- `tools/choose.py --claim` cannot record a claim on the Atlas from a copy. It still draws ground at random and still
  reads the Atlas's open pull requests; that is enough.
- Your pull request will not merge by itself. Say in its text what you verified and what you could not, and stop.
