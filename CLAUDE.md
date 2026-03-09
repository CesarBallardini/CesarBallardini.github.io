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

## Deployment

Push to `master` triggers `.github/workflows/static.yml`, which uploads `./public` to GitHub Pages. Hugo must be run locally before pushing — the CI does **not** run Hugo.

## Editor Settings

`.vscode/settings.json` configures cSpell with 150+ technical terms, line wrap at 100 chars, trim trailing whitespace, and insert final newline.
