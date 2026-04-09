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
- All 2025+ posts use **YAML** frontmatter (`---` delimiters). The archetype still emits TOML (`+++`), but the canonical practice — observed in every published post since `2025-01-27-growing-a-language.md` — is YAML. New posts should be YAML. The full house rules (frontmatter shape, footnote style, link style, voice, image bundles) live in [`content/just-ideas-for-future-posts/near-future-posts.md`](content/just-ideas-for-future-posts/near-future-posts.md) under "Convenciones de la casa". Read that section before writing or editing a post — when this AGENTS.md and the published posts disagree, the published posts win.
- Avoid periods in tag values — they produce slugs invalid on Windows (e.g., `Guy L Steele Jr` not `Guy L. Steele J.`).
- Spanish is the default language: its URLs have no `/es/` prefix. English URLs use `/en/`. Internal links in Spanish content must omit the `/es/` prefix.
- Footnotes are **named, not numeric**: `[^kay]`, `[^okasaki]`, `[^video]` — never `[^1]`. Definitions live grouped at the end of the post in the format `[^name]: [Texto del enlace](URL) — comentario opcional.`

## Editorial planning system

`content/just-ideas-for-future-posts/` is a private editorial catalog tracking ~180 post ideas, organized as one draft file per idea inside 11 thematic category folders. Nothing here renders to the site (it sits outside Hugo's content tree).

Master catalog: `content/just-ideas-for-future-posts/near-future-posts.md` — entry point. It holds the workflow guide ("Cómo usar este plan"), the canonical "Convenciones de la casa" (house rules), the bibliografía transversal table (`tr-NN` reusable references), per-series indices with pointers to every draft file, the publication waves, and the maintenance principles.

Per-draft file naming: `draft-{slug}.md` where `{slug}` matches the `**Slug propuesto:**` field inside the file and is what `hugo new` will use for the published URL.

Per-draft file structure: each file starts with metadata bullets (`**Archivo seed:**`, `**Slug propuesto:**`, `**Comando:**`, `**Serie:**`, `**Cross-links:**`, `**Idioma:**`, `**Madurez:**`, `**Length target:**`), then sections for `**Concepto:**`, `**Hook:**`, `**Outline:**`, `**Bibliografía:**`, `**Imágenes:**`, `**Tags propuestos:**`, and `**Estado actual:**`.

Cross-references between drafts use `[[ID]]` notation (e.g., `[[A1-03]]`, `[[tr-07]]`, `[[K-12]]`) during drafting and resolve to real `[texto](/posts/YYYY-MM-DD-slug/)` URLs at publication. Each post has a stable ID `{series}-{NN}`.

Series and category folders (use the folder name in commands and links, not the series letter):

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

Two operating principles to respect:

1. **Ideas are kept forever, never deleted for staleness.** When an idea cools off, mark its `Estado actual:` as `en hibernación` or `concepto refinado` and leave the draft file in place. The only legitimate reason to delete a draft is that the concept has been factually superseded. Do not propose deleting unwritten drafts in maintenance passes.
2. **The author has lived experience in some of these topics** (Argentine public-sector IT — STG and Ministerio de Cultura Santa Fe in particular) and personal life topics in Series K. Do not invent details about institutions, projects, dates, or personal circumstances; ask or leave gaps in the entry. Existing drafts already use placeholders where verification is needed.

When the user refers to "the plan" or "the editorial plan", they mean `content/just-ideas-for-future-posts/near-future-posts.md` and the 11 category folders alongside it.

## Architecture

- `hugo.toml` — site config: languages, params, menus, social networks
- `themes/ananke/` — Ananke theme as git submodule
- `content/{es,en}/` — bilingual content. Pages with different filenames across languages need `translationKey` in frontmatter to pair translations
- `content/just-ideas-for-future-posts/` — private editorial planning system (see section above), 11 category folders + master catalog, outside Hugo's content tree, not rendered
- `layouts/_default/cv.html` — custom layout wrapping content in `.cv-page` div, used by CV, consulting, and skills pages
- `layouts/partials/head-additions.html` — per-page CSS loading via `page_css` frontmatter param; inlines CSS from `assets/ananke/css/`
- `assets/ananke/css/cv.css` — styles scoped under `.cv-page`, targeting standard HTML elements via Hugo auto-generated heading IDs

## Per-page CSS pattern

Add to frontmatter to load page-specific CSS without affecting other pages:

```toml
layout = "cv"
page_css = ["cv.css"]
```

## Content guidelines

- César is part of a development team at NewGrid — he does backend and frontend work but is not the sole builder. When describing the $100M savings or the analysis platform, frame it as team work (e.g., "helped build", "our team builds"). He develops the **software** that engineers use; he does not perform grid reconfigurations.
- Prefer clean enumerations (commas + "and"/"y") over repetitive connectors like "from... to... to..." or "desde... hasta... hasta..."
- Keep both language versions (ES/EN) consistent — changes to one should be mirrored in the other.

## Deployment

Push to `master` triggers `.github/workflows/static.yml` which deploys `./public` to GitHub Pages. The CI does not run Hugo.
