# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal blog and website for César Ballardini, built with **Hugo** using the **Ananke** theme (git submodule). Bilingual site: Spanish (primary) and English. Hosted on GitHub Pages at `katra.ballardini.com.ar`.

## Build & Development Commands

```bash
# Local development server
hugo server -D          # with drafts
hugo server             # without drafts

# Build for production (generates /public)
hugo

# Create new content
hugo new content/es/posts/YYYY-MM-DD-slug.md
hugo new content/en/posts/YYYY-MM-DD-slug.md
```

The `/public` directory is committed to the repo — GitHub Actions deploys it directly to Pages on push to `master`.

## Architecture

- **Config**: `hugo.toml` — TOML format, defines both languages, site params, and menu structure
- **Theme**: `themes/ananke/` — git submodule from `github.com/theNewDynamic/gohugo-theme-ananke`
- **Content**: Multilingual layout under `content/{es,en}/`
  - `es/posts/` — 15 published Spanish posts (mix of legacy Jekyll and Hugo frontmatter)
  - `en/posts/` — empty (placeholder only)
  - Top-level pages: `cv.md`, `consultoria.md`/`consulting.md`, `habilidades.md`/`skills.md`
- **Drafts**: `content/just-ideas-for-future-posts/` — organized by `dev/`, `misc/`, `sysadmin/`
- **Static output**: `docs/` contains CNAME; `public/` is the full built site

## Custom Layout & CSS System

### Per-page CSS loading

Pages can load CSS files selectively via frontmatter, avoiding site-wide CSS bloat:

```toml
layout = "cv"
page_css = ["cv.css"]
```

- `layouts/partials/head-additions.html` — overrides the theme partial; reads `page_css` from frontmatter and inlines CSS from `assets/ananke/css/` into a `<style>` tag on that page only
- `layouts/_default/cv.html` — custom layout that wraps `.Content` in a `<div class="cv-page">` wrapper, omits author/date/reading-time header, and uses full width
- `assets/ananke/css/cv.css` — styles for CV, consulting, and skills pages, scoped under `.cv-page`; uses Hugo auto-generated heading IDs (e.g., `#experience`, `#education`) to scope section-specific styles

### CSS styling approach

The CV/consulting/skills pages use **pure markdown** with CSS targeting standard HTML elements:
- `h1` → name, `h2` → section headings, `h3` → experience entries
- `h3 + p` → role (bold), `h3 + p + p` → date/location (italic)
- Hugo heading IDs for section-specific rules: `#languages + ul`, `#extended-skills ~ p`, etc.
- Responsive breakpoints at 768px (tablet) and 480px (phone)
- Print styles included

### Translation pairing

Pages with different filenames across languages need `translationKey` in frontmatter:
```toml
translationKey = "consulting"   # pairs consulting.md ↔ consultoria.md
translationKey = "skills"       # pairs skills.md ↔ habilidades.md
```
Pages with the same filename (e.g., `cv.md`) auto-pair without `translationKey`.

## URL Structure

Spanish is the default language — its pages have **no `/es/` prefix**:
- Spanish CV: `/cv/`, consulting: `/consultoria/`, skills: `/habilidades/`
- English CV: `/en/cv/`, consulting: `/en/consulting/`, skills: `/en/skills/`

Internal links in Spanish content must use `/cv/`, `/habilidades/`, `/consultoria/` (not `/es/cv/`).

## Content Conventions

**New Hugo posts** use TOML frontmatter (`+++` delimiters):
```toml
+++
title = "Post Title"
date = "2026-02-22"
draft = false
description = "Meta description"
tags = ["tag1", "tag2"]
author = "César Ballardini"
+++
```

**Legacy posts** (from 2016 Jekyll era) use YAML frontmatter (`---` delimiters) with `layout: post`. Both formats coexist.

Menu pages use `menu = "main"` and `weight` for ordering.

**Tags**: avoid periods in tag values — they generate slugs ending in `.` which are invalid Windows filenames (e.g., use `Guy L Steele Jr` not `Guy L. Steele J.`).

## Deployment

Push to `master` triggers `.github/workflows/static.yml`, which uploads `./public` to GitHub Pages. Hugo must be run locally before pushing — the CI does **not** run Hugo.

## Content Guidelines

### Professional role at NewGrid

César is part of a development team at NewGrid — he does backend and frontend development but is not the sole builder. When describing the $100M savings achievement or the analysis platform, always frame it as team work (e.g., "helped build", "the platform our team builds", "trabajé en la construcción de"). Never imply he built it alone or performed the grid reconfigurations — he develops the **software** that power systems engineers use.

### Writing style for CV/consulting pages

- When listing achievements, prefer clean enumerations (commas + "and"/"y") over repetitive connectors like "from... to... to..." or "desde... hasta... hasta..."
- Keep both language versions (ES/EN) consistent in tone and structure — changes to one should be mirrored in the other

## Editor Settings

`.vscode/settings.json` configures cSpell with 150+ technical terms, line wrap at 100 chars, trim trailing whitespace, and insert final newline.
