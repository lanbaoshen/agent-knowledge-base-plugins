---
title: Semantic Versioning
description: The MAJOR.MINOR.PATCH version format and how pre-release labels, build metadata, compatibility, and precedence work.
tags: semantic versioning, SemVer, version, release, compatibility, major, minor, patch, prerelease
---

# Semantic Versioning

Semantic Versioning, often shortened to SemVer, expresses compatibility using a three-part version number:

```text
MAJOR.MINOR.PATCH
```

Given a defined public API, increment:

- `MAJOR` when making incompatible API changes.
- `MINOR` when adding backward-compatible functionality.
- `PATCH` when making backward-compatible bug fixes.

For example, after `2.4.1`, a compatible bug fix becomes `2.4.2`, a compatible feature becomes `2.5.0`, and a breaking change becomes `3.0.0`.

## Pre-release versions

A hyphen adds a pre-release label:

```text
2.0.0-alpha.1
2.0.0-beta.2
2.0.0-rc.1
```

A pre-release version has lower precedence than the associated normal version. For example, `2.0.0-rc.1` comes before `2.0.0`.

## Build metadata

A plus sign adds build metadata:

```text
2.0.0+20260922
2.0.0-rc.1+build.45
```

Build metadata identifies a build but does not affect version precedence.

## Initial development

Versions with major number zero, such as `0.3.0`, indicate initial development under the SemVer specification. The public API should not be considered stable, and changes may be breaking between minor versions.

Semantic Versioning describes version meaning, but each package manager defines its own syntax for version ranges and dependency resolution. A project should document its public API and release policy so users can interpret version changes correctly.
