# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Personal bilingual Hugo blog ("katra") by César Ballardini, published at https://katra.ballardini.com.ar/. Content is primarily in Spanish (es-AR), with an English section prepared but currently empty.

## Build & Development Commands

```bash
hugo server          # Local dev server with live reload (default: http://localhost:1313/)
hugo server -D       # Include draft posts
hugo                 # Build site to ./public/
hugo new content/es/posts/YYYY-MM-DD-slug-here.md   # Create a new Spanish post
```

No Makefile, no npm scripts, no other build tooling in the root. The theme has its own package.json but that's managed upstream.

## Deployment

GitHub Actions (`.github/workflows/static.yml`) deploys the pre-built `./public/` directory to GitHub Pages on every push to `master`. There is **no Hugo build step in CI** — the `public/` directory must be committed and up to date before pushing.

## Content Conventions

- **Post filename pattern:** `YYYY-MM-DD-slug-in-lowercase.md` — Hugo extracts the date from the filename (`[frontmatter] date = [':filename', ':default']`)
- **Spanish posts go in:** `content/es/posts/`
- **English posts go in:** `content/en/posts/`
- **Frontmatter:** Mix of YAML (`---`) and TOML (`+++`) across posts; both work. Newer posts use YAML. Common fields: `layout`, `title`, `description`, `tags`
- **Draft ideas** live in `content/just-ideas-for-future-posts/` (outside Hugo's content dirs, not built)
- **Unsafe HTML** is enabled in Goldmark renderer (`markup.goldmark.renderer.unsafe = true`)

## Architecture

- **Theme:** Ananke, included as a git submodule at `themes/ananke` (source: `github.com/theNewDynamic/gohugo-theme-ananke`)
- **No custom layouts or shortcodes** — the site relies entirely on the Ananke theme defaults
- **Archetype:** `archetypes/default.md` uses TOML frontmatter with auto-date and title derived from filename
- **Config:** Single file `hugo.toml` — bilingual setup with Spanish (weight 1) as default, English (weight 2) secondary
- **Pagination:** Currently set to 3 per page (intentionally low)
- **Static assets:** `favicon/` directory has the favicon; `static/` is empty

## Submodule

After cloning, initialize the theme submodule:
```bash
git submodule update --init --recursive
```
