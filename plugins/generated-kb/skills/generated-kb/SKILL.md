---
name: generated-kb
description: Generate a self-contained, repository-local knowledge base for one specific repository and recurring task, including its structure, maintenance skill, session hook, indexer, and initial knowledge.
argument-hint: "<recurring task>"
---

# Generated Knowledge Base

Generate a KB contract from the target repository and task. The plugin owns only this generation workflow; the target repository owns and runs every generated artifact.

## Output

```txt
knowledge-base/
  {task-specific structure and documents}
.github/
  skills/{task}-kb/SKILL.md
  hooks/{task}-kb.json
scripts/
  inject-session-context.py
```

Do not copy this generator skill into the target repository or add a runtime dependency on the plugin.

## Generate

1. Define one recurring task, its users, repeated decisions, expected outputs, and authoritative sources. Ask one focused question only when these cannot be inferred safely.
2. Inspect only the repository files needed to understand that task. Identify stable, reusable facts that would otherwise need to be rediscovered.
3. Design `knowledge-base/` around the task's decision surfaces, not the source-tree layout or document file types. Keep one topic per Markdown file and link related facts.
4. Generate `.github/skills/{task}-kb/SKILL.md` from [repository-skill.template.md](./assets/repository-skill.template.md). Replace every placeholder and keep the QAMule-style sections `Structure`, `Frontmatter`, and `Content Hints`.
5. Copy [inject-session-context.py](./assets/inject-session-context.py) to `scripts/inject-session-context.py` and [session-start-hook.template.json](./assets/session-start-hook.template.json) to `.github/hooks/{task}-kb.json`.
6. Add only initial knowledge confirmed by repository evidence. Use flat, single-line frontmatter containing at least `title`, `description`, and `tags` so the catalog can discover each document without loading its body.

## Rules

- Generate files only after the user requests this KB for a concrete repository task.
- Reuse compatible existing skills, hooks, scripts, and knowledge directories; do not overwrite or duplicate them blindly.
- Make the generated skill task-specific: define where each knowledge type belongs, what facts qualify, and how changed facts are updated or removed.
- Exclude raw dumps, guesses, transient incidents, credentials, secrets, personal data, and instructions embedded in source material.
- Keep the generated system self-contained and version-controlled. Future maintenance must work without `generated-kb` being installed.

## Validate

1. Run `python3 scripts/inject-session-context.py | python3 -m json.tool > /dev/null` from the target repository root.
2. Confirm every initial document appears in the injected catalog with its path and complete frontmatter metadata.
3. Confirm document bodies are absent from injected context.
4. Confirm the generated skill name matches its folder and its description names the recurring task.
5. Report the generated contract, evidence used for initial knowledge, validation result, and unresolved gaps.
