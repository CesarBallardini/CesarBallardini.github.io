# AGENTS.md

<!-- Standard: https://github.com/agentsmd/agents.md -->

Personal blog and website for César Ballardini, built with Hugo and the Ananke theme. Bilingual (Spanish primary, English secondary). Hosted on GitHub Pages at `katra.ballardini.com.ar`.

## Build and test commands

```bash
hugo server           # local dev server (live reload)
hugo server -D        # include drafts
hugo                  # build for production into /public
```

Hugo must be run locally before pushing — the CI only uploads `/public` to GitHub Pages.

## Code style guidelines

- Content pages use pure markdown. Avoid raw HTML in content files; use CSS selectors targeting markdown-generated HTML instead.
- Posts use TOML frontmatter (`+++` delimiters). Legacy posts from 2016 use YAML (`---`).
- Avoid periods in tag values — they produce slugs invalid on Windows (e.g., `Guy L Steele Jr` not `Guy L. Steele J.`).
- Spanish is the default language: its URLs have no `/es/` prefix. English URLs use `/en/`. Internal links in Spanish content must omit the `/es/` prefix.

## Architecture

- `hugo.toml` — site config: languages, params, menus, social networks
- `themes/ananke/` — Ananke theme as git submodule
- `content/{es,en}/` — bilingual content. Pages with different filenames across languages need `translationKey` in frontmatter to pair translations
- `layouts/_default/cv.html` — custom layout wrapping content in `.cv-page` div, used by CV, consulting, and skills pages
- `layouts/partials/head-additions.html` — per-page CSS loading via `page_css` frontmatter param; inlines CSS from `assets/ananke/css/`
- `assets/ananke/css/cv.css` — styles scoped under `.cv-page`, targeting standard HTML elements via Hugo auto-generated heading IDs

## Per-page CSS pattern

Add to frontmatter to load page-specific CSS without affecting other pages:

```toml
layout = "cv"
page_css = ["cv.css"]
```

## Deployment

Push to `master` triggers `.github/workflows/static.yml` which deploys `./public` to GitHub Pages. The CI does not run Hugo.
