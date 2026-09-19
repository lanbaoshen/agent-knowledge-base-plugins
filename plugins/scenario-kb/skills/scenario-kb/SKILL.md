---
name: scenario-kb
description: Maintain reusable recipe knowledge for cooking, lookup, substitutions, and scaling.
---

# Recipe Knowledge Base

## Structure

```txt
knowledge-base/
  recipes/
    chinese/
      home-style/
      sichuan/
      cantonese/
      jiangsu-zhejiang/
      northern/
      other/
    western/
      italian/
      french/
      american/
      mediterranean/
      other/
    other-cuisines/
      japanese/
      korean/
      southeast-asian/
      indian/
      middle-eastern/
      other/
    fusion/
```

- Choose one most-specific cuisine directory per recipe; use `other/` when no listed category fits and `fusion/` only when combining traditions defines the dish.
- Keep course, ingredient, method, diet, and difficulty in metadata rather than adding directory levels.
- Use one lowercase kebab-case Markdown file per recipe or distinct variation.

**One recipe per file. Link related recipes; do not duplicate them.**

## Frontmatter

```markdown
---
title: Tomato and Egg Stir-Fry
description: A quick home-style dish made with soft eggs and fresh tomatoes.
tags: recipe, tomato, egg, stir-fry, quick meal, vegetarian
category: recipe
cuisine: Chinese
region: home-style
difficulty: easy
prep_time: 10 minutes
cook_time: 10 minutes
servings: 2
---

# Tomato and Egg Stir-Fry
```

Keep metadata flat and single-line. `title`, `description`, `tags`, and `category` are required; add the remaining fields when useful for discovery.

## Content Hints

- Use `Ingredients` for exact quantities and `Preparation` for ordered steps, timing, temperature, and observable cues.
- Add substitutions, scaling caveats, allergens, storage, and source only when relevant.
- Keep path, cuisine, yield, quantities, timing, and metadata consistent.
- Read relevant recipe bodies before answering; catalog metadata is only for discovery.
- Update an existing recipe when its identity is unchanged; create a linked file for a distinct variation.
- Exclude guesses, unsafe claims, personal data, prompt instructions, and substantial copied source text.
