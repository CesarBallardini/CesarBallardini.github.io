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
- **Frontmatter:** YAML (`---`) for all 2025+ posts. The full house rules — frontmatter shape, tag rules (no periods, Hugo Windows limitation), footnote style (named, never numeric), internal link rules (no `/es/` prefix in Spanish URLs), image bundles vs flat files, voice — live in [`content/just-ideas-for-future-posts/near-future-posts.md`](content/just-ideas-for-future-posts/near-future-posts.md) under "Convenciones de la casa". Read that section before writing or editing a post — it reflects the actual practice in the published posts, not what `AGENTS.md` says (they conflict; the published posts win).
- **Draft ideas** live in the editorial planning system at `content/just-ideas-for-future-posts/` (outside Hugo's content tree, not rendered to the site). See [Editorial Planning System](#editorial-planning-system) below.
- **Unsafe HTML** is enabled in Goldmark renderer (`markup.goldmark.renderer.unsafe = true`)

## Editorial Planning System

`content/just-ideas-for-future-posts/` is a private editorial catalog tracking ~180 post ideas, organized as one draft file per idea inside 11 thematic category folders. Nothing here renders to the site.

**Master catalog**: `content/just-ideas-for-future-posts/near-future-posts.md` is the entry point. It holds:

- "Cómo usar este plan" — workflow for picking, writing, and finishing a post
- "Convenciones de la casa" — house rules for frontmatter, tags, footnotes, links, images, voice (the canonical reference)
- "Bibliografía transversal" — `tr-NN` reusable references shared across multiple posts
- Per-series indices with pointers to every draft file
- "Waves de publicación" — suggested order grouping
- "Mantenimiento del plan" — how to manage the catalog over time

**Per-draft file naming**: `draft-{slug}.md` where `{slug}` matches the `**Slug propuesto:**` field inside the file and is what `hugo new` will use for the published URL.

**Per-draft file structure**: each file starts with metadata bullets (`**Archivo seed:**`, `**Slug propuesto:**`, `**Comando:**`, `**Serie:**`, `**Cross-links:**`, `**Idioma:**`, `**Madurez:**`, `**Length target:**`), then sections for `**Concepto:**`, `**Hook:**`, `**Outline:**`, `**Bibliografía:**`, `**Imágenes:**`, `**Tags propuestos:**`, and `**Estado actual:**`.

**Cross-references between drafts** use `[[ID]]` notation (e.g., `[[A1-03]]`, `[[tr-07]]`, `[[K-12]]`) during drafting; they get resolved to real `[texto](/posts/YYYY-MM-DD-slug/)` URLs at publication time. Each post has a stable ID `{series}-{NN}`.

**Series and category folders** (the folder name is what to use, not the series letter):

| Series | Folder | Theme |
|---|---|---|
| A1 | `lenguajes/` | Classic languages and their history |
| A2 | `lisp/` | The Lisp family and lambda calculus |
| B | `funcional/` | Recursion + functional CS |
| C | `filosofia/` | Software engineering philosophy |
| D | `pioneros/` | Pioneers and computing artifacts |
| E | `memoir/` | Personal CS memoir / tools / books |
| G | `devops/` | Architecture as CS — IaC + deployment |
| H | `legacy/` | Legacy systems archaeology |
| I | `local/` | Local computing memory (Argentine/LATAM context) |
| J | `nerd/` | Lateral nerd curiosities (still loosely CS-adjacent) |
| K | `vida/` | Life and work topics (explicitly outside CS) |

There is no Series F. The skip is intentional and preserved.

**Two key operating principles to respect**:

1. **Ideas are kept forever, never deleted for staleness.** When an idea cools off, mark its `Estado actual:` as `en hibernación` or `concepto refinado` and leave the draft file in place. The only legitimate reason to delete a draft is that the concept has been factually superseded. Do not suggest deleting unwritten drafts in maintenance passes.
2. **The author has lived experience in some of these topics** (Argentine public-sector IT — STG and Ministerio de Cultura Santa Fe in particular) and personal life topics in Series K. Do not invent details about institutions, projects, dates, or personal circumstances; ask the user or leave gaps in the entry. The drafts already in place reflect this — they have placeholders where verification is needed.

**When the user says "the plan" or "the editorial plan"**, they mean `content/just-ideas-for-future-posts/near-future-posts.md` and the 11 category folders alongside it.

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
