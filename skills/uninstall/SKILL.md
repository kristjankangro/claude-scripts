---
name: uninstall
description: Remove the startup quote hook from the user's Claude Code setup
disable-model-invocation: true
allowed-tools: Read, Write, Bash(rm *)
---

Remove the startup quote hook from `~/.claude/`.

1. Read `~/.claude/settings.json`.
2. Remove any `SessionStart` hook entry whose command references `startup-quote`.
   - If the `SessionStart` array becomes empty, remove the `SessionStart` key.
   - If the `hooks` object becomes empty, remove the `hooks` key.
   - Preserve all other settings.
3. Write the updated `settings.json` back.
4. Delete `~/.claude/startup-quote.py` if it exists.
5. Tell the user the startup quote hook has been removed.
