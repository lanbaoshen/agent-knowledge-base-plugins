---
title: JSON Basics
description: The basic data types, syntax rules, examples, and common interoperability considerations for JSON.
tags: JSON, data format, serialization, object, array, API, configuration, parsing
---

# JSON Basics

JSON, or JavaScript Object Notation, is a text format for exchanging structured data. It is language-independent even though its syntax originated from JavaScript.

## Data types

JSON supports six value types:

- Object: unordered name-value pairs inside `{}`.
- Array: ordered values inside `[]`.
- String: text inside double quotes.
- Number: an integer or decimal number.
- Boolean: `true` or `false`.
- Null: `null`.

## Example

```json
{
  "name": "Example project",
  "version": 1,
  "public": true,
  "topics": ["demo", "knowledge"],
  "homepage": null
}
```

## Syntax rules

- Property names and strings use double quotes.
- Items are separated by commas, but the final item has no trailing comma.
- Standard JSON does not support comments.
- Whitespace outside strings does not change the data.
- Escape special characters in strings, such as `\"`, `\\`, `\n`, and `\t`.

## Interoperability notes

JSON does not define a date type, so dates are normally represented as strings using an agreed format. Large or highly precise numbers may not be represented exactly by every programming language. Object property order should not be used to carry meaning.

Use a JSON parser rather than building or reading JSON with manual string operations. Validate external JSON against the application's expected structure before using its values.