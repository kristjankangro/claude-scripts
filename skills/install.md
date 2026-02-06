Install the startup quote hook into the user's Claude Code setup.

Steps:

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
   - Preserve all existing settings — only merge in the hook.
4. Write the updated `settings.json` back.
5. Tell the user the installation is complete and that new Claude Code sessions will show a random quote on startup.
