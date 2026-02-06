---
name: push
description: Stage, commit, and push all local changes
disable-model-invocation: true
allowed-tools: Bash(git *)
argument-hint: optional commit message
---

Stage all local changes, commit them, and push to the remote.

## Steps

1. Run `git status` and `git diff --stat` to review what will be committed.
2. If there are no changes (no untracked, modified, or staged files), tell the user there's nothing to push and stop.
3. Run `git log --oneline -5` to see recent commit message style.
4. Stage all changes with `git add -A`.
5. Commit with a concise message:
   - If the user provided a commit message as an argument, use it exactly.
   - Otherwise, write a short message summarizing the changes based on the diff.
   - Always append `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>` to the commit message.
   - Use a HEREDOC to pass the message to `git commit`.
6. Push to the current branch's upstream with `git push`. If no upstream is set, use `git push -u origin HEAD`.
7. Show the user the result (commit hash, branch, remote).
