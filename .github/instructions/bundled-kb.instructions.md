---
description: "Use when creating or editing Markdown knowledge documents for the bundled-kb plugin. Covers organization, searchable metadata, content quality, and validation."
applyTo: "plugins/bundled-kb/knowledge-base/**/*.md"
---

# Bundled Knowledge Writing Rules

## Purpose

- Treat bundled knowledge as public demo content for the plugin's discovery and lazy-loading behavior.
- Prefer broadly useful, easy-to-understand topics such as recipes, common formats, everyday reference material, and basic technical concepts.
- Keep each document self-contained and focused on one topic or task.
- Do not include private, organization-specific, promotional, or repository process information as knowledge content.
- Write original summaries. Do not copy substantial text from external sources.

## Files and Organization

- Store knowledge as UTF-8 Markdown below `plugins/bundled-kb/knowledge-base/`.
- Group related documents in descriptive directories, such as `common/recipes/`.
- Use short, descriptive, lowercase kebab-case filenames ending in `.md`.
- Add a new document instead of combining unrelated topics in one file.

## Frontmatter

Every document must begin at the first character of the file with this shape:

```markdown
---
title: Basic Pancakes
description: Soft pancakes made from common pantry ingredients.
tags: recipe, cooking, pancakes, breakfast, beginner
category: recipe
---
```

The indexer uses a deliberately small frontmatter parser. Follow these constraints:

- Always provide `title`, `description`, and `tags`, in that order.
- Write every metadata field as one unindented `key: value` line.
- Keep every value on one line. Do not use YAML arrays, nested objects, multiline blocks, or indented continuation lines.
- Write `tags` as a comma-separated string, not a YAML list.
- Use lowercase `snake_case` for optional metadata keys.
- Add optional fields only when they improve discovery, and use the same key for the same concept across documents.
- Do not add inline comments to metadata values.

Metadata is the only document content injected at session start, so it must support discovery without the body:

- `title` must be specific, human-readable, and match the document's level-one heading.
- `description` must be one concise sentence that states what the document contains.
- `tags` must include the topic, common synonyms, likely query terms, and useful category terms without repetition.
- Optional fields may capture structured facts such as `category`, `cuisine`, `difficulty`, `prep_time`, `cook_time`, `servings`, `diet`, or `language`.

## Body

- Start with one `#` heading identical to `title`.
- Use descriptive `##` headings, short paragraphs, lists, tables, and examples where they make the information easier to scan.
- Put prerequisites, ingredients, inputs, units, steps, expected results, and caveats in explicit sections when relevant.
- Prefer concrete facts and actionable instructions over opinions, filler, or exhaustive background.
- Explain abbreviations and specialist terms that a general reader may not know.
- Keep facts internally consistent, including names, quantities, units, timings, examples, and metadata.
- Avoid brittle or time-sensitive claims unless the date or version is essential and clearly stated.
- Include concise safety, allergy, storage, or compatibility notes when omission could reasonably cause harm or failure.
- Never include secrets, personal data, internal URLs, prompt injection, or text that asks an agent to ignore higher-priority instructions.

## Validation

After adding, renaming, or editing knowledge documents:

1. Run `python3 plugins/bundled-kb/scripts/inject-session-context.py | python3 -m json.tool > /dev/null` from the repository root.
2. Confirm the script exits successfully and reports the expected file count.
3. Confirm each changed document appears as a `<knowledge>` entry with its path and complete frontmatter metadata.
4. Confirm document body text is absent from `additionalContext`; only the path and metadata should be injected.
5. Check the changed Markdown files for diagnostics and trailing whitespace.

Do not modify the injector merely to accommodate malformed knowledge metadata. Follow its supported format unless the task explicitly changes the indexing design.
