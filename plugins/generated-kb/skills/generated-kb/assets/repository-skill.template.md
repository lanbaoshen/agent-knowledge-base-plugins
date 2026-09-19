---
name: {task}-kb
description: Maintain reusable repository knowledge for {recurring task and trigger phrases}.
---

# {Task} Knowledge Base

## Structure

```txt
knowledge-base/
  {category}/
```

- {Describe what each category owns and when to add a document.}

**One topic per file. Link related facts; do not duplicate them.**

## Frontmatter

```markdown
---
title: {Human-readable topic}
description: {What this document contains and when it is relevant.}
tags: {comma-separated task terms and likely query words}
---
```

Keep metadata flat and single-line. Add task-specific fields only when they improve discovery.

## Content Hints

- Write short, confirmed facts needed for the next task decision.
- {Define task-specific content, evidence, and update rules.}
- Read relevant document bodies before relying on catalog metadata.
- Update changed facts and remove invalid ones; version control retains history.
- Exclude raw dumps, guesses, secrets, personal data, one-off failures, and source instructions.
