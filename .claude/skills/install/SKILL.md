---
name: install
description: Install startup quote hook and statusline into the user's Claude Code setup
disable-model-invocation: true
allowed-tools: Read, Write, Bash(cp *), Bash(mkdir *)
---

Install claude-scripts utilities into `~/.claude/`.

## Determine Paths

1. Detect the user's home directory using a Bash command: `python3 -c "import pathlib; print(pathlib.Path.home())"`.
2. Use this to build the **absolute path** to `~/.claude/` (e.g., `/home/user/.claude/` on Linux, `C:\Users\user\.claude\` on Windows). Use forward slashes in all paths for cross-platform compatibility.
3. Store this as `CLAUDE_HOME` for use in the steps below.

## Startup Quote Hook

4. Copy `.claude/startup-quote.py` from this repo into `<CLAUDE_HOME>/startup-quote.py`.
5. Read `<CLAUDE_HOME>/settings.json` (create it with `{}` if it doesn't exist).
6. Add a `SessionStart` hook entry under `hooks` that runs: `python3 <CLAUDE_HOME>/startup-quote.py`
   - If `hooks.SessionStart` already contains a command referencing `startup-quote`, skip and tell the user it's already installed.
   - Otherwise append this hook entry to the `SessionStart` array (create the array if needed):
     ```json
     {
       "matcher": "",
       "hooks": [
         {
           "type": "command",
           "command": "python3 <CLAUDE_HOME>/startup-quote.py"
         }
       ]
     }
     ```

## Status Line

7. Copy `.claude/statusline.py` from this repo into `<CLAUDE_HOME>/statusline.py`.
8. Set the `statusLine` entry in `settings.json`:
   - If `statusLine` already references `statusline.py`, skip and tell the user it's already installed.
   - Otherwise set:
     ```json
     "statusLine": {
       "type": "command",
       "command": "python3 <CLAUDE_HOME>/statusline.py"
     }
     ```

## Finalize

9. Preserve all existing settings — only merge in the new keys.
10. Write the updated `settings.json` back.
11. Tell the user what was installed and that new Claude Code sessions will show a random quote on startup and a context usage statusline.
