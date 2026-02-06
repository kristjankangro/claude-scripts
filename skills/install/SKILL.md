---
name: install
description: Install startup quote hook and statusline into the user's Claude Code setup
disable-model-invocation: true
allowed-tools: Read, Write, Bash(cp *), Bash(mkdir *)
---

Install claude-scripts utilities into `~/.claude/`.

## Startup Quote Hook

1. Copy `startup-quote.py` from this repo into `~/.claude/startup-quote.py`.
2. Read `~/.claude/settings.json` (create it with `{}` if it doesn't exist).
3. Add a `SessionStart` hook entry under `hooks` that runs: `python3 ~/.claude/startup-quote.py`
   - If `hooks.SessionStart` already contains a command referencing `startup-quote`, skip and tell the user it's already installed.
   - Otherwise append this hook entry to the `SessionStart` array (create the array if needed):
     ```json
     {
       "matcher": "",
       "hooks": [
         {
           "type": "command",
           "command": "python3 ~/.claude/startup-quote.py"
         }
       ]
     }
     ```

## Status Line

4. Copy `statusline.py` from this repo into `~/.claude/statusline.py`.
5. Set the `statusLine` entry in `settings.json`:
   - If `statusLine` already references `statusline.py`, skip and tell the user it's already installed.
   - Otherwise set:
     ```json
     "statusLine": {
       "type": "command",
       "command": "python3 ~/.claude/statusline.py"
     }
     ```

## Finalize

6. Preserve all existing settings — only merge in the new keys.
7. Write the updated `settings.json` back.
8. Tell the user what was installed and that new Claude Code sessions will show a random quote on startup and a context usage statusline.
