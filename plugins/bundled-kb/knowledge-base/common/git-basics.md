---
title: Git Basics
description: A short reference for repositories, commits, branches, remotes, everyday commands, and safe ways to undo changes.
tags: git, version control, repository, commit, branch, merge, remote, pull request
---

# Git Basics

Git is a distributed version control system. Each clone contains the project's files and its commit history.

## Core concepts

- **Working tree:** The files currently checked out on disk.
- **Staging area:** Changes selected for the next commit.
- **Commit:** A saved snapshot with an author, timestamp, message, and parent history.
- **Branch:** A movable name that points to a commit.
- **Remote:** A named location for another copy of the repository, commonly named `origin`.

## Everyday workflow

```shell
git status                 # Show changed and untracked files
git diff                   # Show unstaged changes
git add README.md          # Stage a file
git diff --staged          # Show staged changes
git commit -m "Update README"
```

Make commit messages describe the purpose of the change. A commit should be understandable without depending on uncommitted local files.

## Branches and history

```shell
git switch -c feature-name # Create and switch to a branch
git branch                 # List local branches
git log --oneline          # Show compact history
git show COMMIT            # Inspect one commit
```

A merge combines histories. A rebase replays commits onto a different base and therefore changes their commit IDs.

## Remotes

```shell
git fetch origin           # Download remote history without integrating it
git pull                   # Fetch and integrate the current branch
git push origin HEAD       # Publish the current branch
```

Fetching is a useful first step when you want to inspect incoming changes before integrating them.

## Undoing changes

```shell
git restore FILE           # Discard unstaged changes in a file
git restore --staged FILE  # Unstage a file but keep its changes
git revert COMMIT          # Create a new commit that reverses a commit
```

Check `git status` and `git diff` before discarding work. Reverting is usually safer for shared history because it does not rewrite existing commits.