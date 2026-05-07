---
name: commit
description: Standardized commit workflow with code review integration. Stages changes, runs code-reviewer sub-agent, and commits with a descriptive message. Skips cleanly when working directory has no changes.
user_invocable: true
---

# Commit Workflow

A disciplined commit workflow that integrates code review before every commit.

## Steps

1. **Check for changes** - Run `git status` to see if there are staged or unstaged changes
2. **Exit if clean** - If no changes exist, stop immediately without triggering any review hooks
3. **Run code review** - Invoke the `code-reviewer` sub-agent (via Agent tool with
   `subagent_type: "everything-claude-code:code-reviewer"`) to review all pending changes
4. **Address issues** - If the review finds CRITICAL or HIGH severity issues, fix them before proceeding. MEDIUM issues
   should be fixed when possible
5. **Stage changes** - Use `git add` with specific file paths (never `git add -A` or `git add .`)
6. **Commit** - Write a descriptive commit message following conventional commits format: `<type>: <description>`
7. **Verify** - Run `git status` after commit to confirm clean state

## Rules

- Never use `git add -A` or `git add .` - always specify files explicitly
- Never skip code review for non-trivial changes
- Never force push or use `--no-verify`
- Never commit files that may contain secrets (.env, credentials.json, etc.)
- If the working tree is clean at step 1, exit immediately without any further action
