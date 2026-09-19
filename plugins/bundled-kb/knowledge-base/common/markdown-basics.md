---
title: Markdown Basics
description: Common Markdown syntax for headings, emphasis, lists, links, images, quotes, code, and tables.
tags: markdown, README, documentation, formatting, headings, lists, links, code blocks, tables
---

# Markdown Basics

Markdown is a plain-text format commonly used for README files, documentation, issues, and comments.

## Text and headings

```markdown
# Level 1 heading
## Level 2 heading

**bold text**
*italic text*
~~strikethrough~~
```

Separate paragraphs with a blank line.

## Lists

```markdown
- Unordered item
- Another item

1. First item
2. Second item

- [ ] Open task
- [x] Completed task
```

Indent items to create nested lists. Task lists are a common extension and may not be supported by every Markdown renderer.

## Links and images

```markdown
[Link text](https://example.com)
![Alternative text](image.png)
```

Use descriptive link text. Image alternative text should communicate the image's purpose when the image contains useful information.

## Quotes and code

```markdown
> A block quote

Use `inline code` for commands and identifiers.
```

Use fenced code blocks for multiple lines and add a language name when syntax highlighting is useful:

````markdown
```javascript
console.log("Hello, world!");
```
````

## Tables

```markdown
| Name | Value |
| --- | ---: |
| Apples | 3 |
| Oranges | 5 |
```

Tables and some other features vary between Markdown implementations. Check the renderer used by the target platform when exact formatting matters.