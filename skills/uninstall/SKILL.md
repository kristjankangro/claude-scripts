---
name: uninstall
description: Remove startup quote hook and statusline from the user's Claude Code setup
disable-model-invocation: true
allowed-tools: Read, Write, Bash(rm *)
---

Remove claude-scripts utilities from `~/.claude/`.

1. Read `~/.claude/settings.json`.
2. Remove any `SessionStart` hook entry whose command references `startup-quote`.
   - If the `SessionStart` array becomes empty, remove the `SessionStart` key.
   - If the `hooks` object becomes empty, remove the `hooks` key.
3. Remove the `statusLine` entry if it references `statusline.py`.
4. Preserve all other settings.
5. Write the updated `settings.json` back.
6. Delete `~/.claude/startup-quote.py` and `~/.claude/statusline.py` if they exist.
7. Tell the user what was removed.
