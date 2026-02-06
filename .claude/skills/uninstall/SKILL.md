---
name: uninstall
description: Remove startup quote hook and statusline from the user's Claude Code setup
disable-model-invocation: true
allowed-tools: Read, Write, Bash(rm *)
---

Remove claude-scripts utilities from `~/.claude/`.

## Determine Paths

1. Detect the user's home directory using a Bash command: `python3 -c "import pathlib; print(pathlib.Path.home())"`.
2. Use this to build the **absolute path** to `~/.claude/` (e.g., `/home/user/.claude/` on Linux, `C:\Users\user\.claude\` on Windows). Use forward slashes in all paths for cross-platform compatibility.
3. Store this as `CLAUDE_HOME` for use in the steps below.

## Remove

4. Read `<CLAUDE_HOME>/settings.json`.
5. Remove any `SessionStart` hook entry whose command references `startup-quote`.
   - If the `SessionStart` array becomes empty, remove the `SessionStart` key.
   - If the `hooks` object becomes empty, remove the `hooks` key.
6. Remove the `statusLine` entry if it references `statusline.py`.
7. Preserve all other settings.
8. Write the updated `settings.json` back.
9. Delete `<CLAUDE_HOME>/startup-quote.py` and `<CLAUDE_HOME>/statusline.py` if they exist.
10. Tell the user what was removed.
