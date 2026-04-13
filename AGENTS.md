# AGENTS.md

<!-- Standard: https://github.com/agentsmd/agents.md -->

Personal bilingual Hugo blog ("katra") by César Ballardini, published at https://katra.ballardini.com.ar/. Content is primarily in Spanish (es-AR), with an English section holding professional pages (CV, consulting, skills). Hosted on GitHub Pages.

## Git rules (NEVER break)

Agents working on this repo **must not run any git command that adds, deletes, or modifies repository state**. Prohibited:

- `git commit` (including `--amend`)
- `git add` / `git rm` / `git mv` / `git restore` / `git reset`
- `git push` / `git pull` / `git fetch` with side effects
- `git branch` (create/delete) / `git checkout` / `git switch`
- `git merge` / `git rebase` / `git cherry-pick` / `git revert`
- `git stash` (push/pop/apply)
- `git tag` (create/delete)
- `git clean`
- `git submodule` mutations

Read-only git is allowed: `git status`, `git diff`, `git log`, `git show`, `git blame`, `git ls-files`, `git config --get`.

When the user asks for a commit, push, branch change, etc., draft the command or commit message as text and hand it back for the user to run manually.

## Submodule setup

After cloning, initialize the Ananke theme submodule:

```bash
git submodule update --init --recursive
```

## Build and test commands

```bash
hugo server          # Local dev server with live reload (default: http://localhost:1313/)
hugo server -D       # Include draft posts
hugo                 # Build site to ./public/
hugo new content/es/posts/YYYY-MM-DD-slug-here/index.md   # Create a new Spanish post (page bundle)
```

Hugo must be run locally before pushing — the CI only uploads `/public` to GitHub Pages; there is no Hugo build step in CI.

## Deployment

Push to `master` triggers `.github/workflows/static.yml` which deploys the pre-built `./public/` directory to GitHub Pages. The `public/` directory must be committed and up to date before pushing.

Because `public/` is committed, stale files from previous builds (old slugs, removed tags, renamed posts) are not cleaned automatically. Build with `hugo --cleanDestinationDir` to drop orphans, or `rm -rf public && hugo` for a fully fresh tree before committing.

## Code style guidelines

- **Post format:** all posts use **page bundles** — `content/es/posts/YYYY-MM-DD-slug/index.md` with images and assets as siblings. Do not create flat `.md` files.
- **Post filename pattern:** `YYYY-MM-DD-slug-in-lowercase` — Hugo extracts the date from the directory name (`[frontmatter] date = [':filename', ':default']`).
- **Frontmatter:** All 2025+ posts use YAML (`---` delimiters). The archetype (`archetypes/default.md`) still emits TOML (`+++`), but the canonical practice — observed in every published post since `2025-01-27-growing-a-language.md` — is YAML. New posts must use YAML.
- The full house rules — frontmatter shape, tag rules, footnote style, link conventions, voice, image bundles — live in [`content/just-ideas-for-future-posts/near-future-posts.md`](content/just-ideas-for-future-posts/near-future-posts.md) under "Convenciones de la casa". Read that section before writing or editing a post. When this file and the published posts disagree, the published posts win.
- **Tags:** Avoid periods in tag values — they produce slugs invalid on Windows (e.g., `Guy L Steele Jr` not `Guy L. Steele Jr.`).
- **Language URLs:** Spanish is the default language; its URLs have no `/es/` prefix. English URLs use `/en/`. Internal links in Spanish content must omit the `/es/` prefix.
- **Footnotes:** Named, not numeric: `[^kay]`, `[^okasaki]`, `[^video]` — never `[^1]`. Definitions live grouped at the end of the post: `[^name]: [Texto del enlace](URL) — comentario opcional.`
- **Hero banner:** every post has `featured_image: hero-filename.jpg` in frontmatter. The image lives in the post's bundle folder. Use landscape-oriented images (2.5:1 ratio or wider); portrait photos must be cropped before use. `featured_image_class = "cover bg-center"` is set globally in `hugo.toml`.
- **Per-page CSS:** add `page_css: ['tables.css']` to frontmatter for posts with markdown tables. CSS lives in `assets/ananke/css/` and is loaded via `layouts/partials/head-additions.html`.
- **Image attribution:** every public domain or CC-licensed image requires a named footnote: `[^img_foo]: Imagen de [Title](URL) — CC BY-SA 4.0 — Author, via Wikimedia Commons.`
- **HTML in content:** Unsafe HTML is enabled (`markup.goldmark.renderer.unsafe = true`). Raw HTML blocks do not process markdown inside them — footnote refs (`[^name]`) inside HTML tags will not render as links. Keep footnote refs in markdown context.

## Content guidelines

- César is part of a development team at NewGrid — he does backend and frontend work but is not the sole builder. When describing the $100M savings or the analysis platform, frame it as team work (e.g., "helped build", "our team builds"). He develops the **software** that engineers use; he does not perform grid reconfigurations.
- Prefer clean enumerations (commas + "and"/"y") over repetitive connectors like "from... to... to..." or "desde... hasta... hasta..."
- Keep both language versions (ES/EN) consistent — changes to one should be mirrored in the other.

## Editorial planning system

`content/just-ideas-for-future-posts/` is a private editorial catalog tracking ~180 post ideas, organized as one draft file per idea inside 11 thematic category folders. Nothing here renders to the site (it sits outside Hugo's content tree).

**Master catalog**: `content/just-ideas-for-future-posts/near-future-posts.md` — the entry point. It holds the workflow guide ("Cómo usar este plan"), the canonical "Convenciones de la casa" (house rules), the bibliografía transversal table (`tr-NN` reusable references), per-series indices with pointers to every draft file, publication waves, and maintenance principles.

**Per-draft file naming**: `draft-{slug}.md` where `{slug}` matches the `**Slug propuesto:**` field inside the file and is what `hugo new` will use for the published URL.

**Per-draft file structure**: each file starts with metadata bullets (`**Archivo seed:**`, `**Slug propuesto:**`, `**Comando:**`, `**Serie:**`, `**Cross-links:**`, `**Idioma:**`, `**Madurez:**`, `**Length target:**`), then sections for `**Concepto:**`, `**Hook:**`, `**Outline:**`, `**Bibliografía:**`, `**Imágenes:**`, `**Tags propuestos:**`, and `**Estado actual:**`.

**Cross-references between drafts** use `[[ID]]` notation (e.g., `[[A1-03]]`, `[[tr-07]]`, `[[K-12]]`) during drafting; they resolve to real `[texto](/posts/YYYY-MM-DD-slug/)` URLs at publication time. Each post has a stable ID `{series}-{NN}`.

**Series and category folders** (use the folder name in commands and links, not the series letter):

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

**Two operating principles to respect:**

1. **Ideas are kept forever, never deleted for staleness.** When an idea cools off, mark its `Estado actual:` as `en hibernación` or `concepto refinado` and leave the draft file in place. The only legitimate reason to delete a draft is that the concept has been factually superseded or the post has been published with no remaining improvements. When a post is published: delete the draft file and remove its index entry **only if** the draft has no pending improvements listed. If it has pending improvements (cross-links to add, possible follow-up posts, etc.), keep both. Do not propose deleting unwritten drafts in maintenance passes.
2. **The author has lived experience in some of these topics** (Argentine public-sector IT — STG and Ministerio de Cultura Santa Fe in particular) and personal life topics in Series K. Do not invent details about institutions, projects, dates, or personal circumstances; ask or leave gaps in the entry. Existing drafts already use placeholders where verification is needed.

When the user refers to "the plan" or "the editorial plan", they mean `content/just-ideas-for-future-posts/near-future-posts.md` and the 11 category folders alongside it.

## Architecture

- **Config:** `hugo.toml` — single config file with bilingual setup: Spanish (weight 1, default), English (weight 2)
- **Theme:** Ananke, included as a git submodule at `themes/ananke/` (source: `github.com/theNewDynamic/gohugo-theme-ananke`)
- **Content:** `content/{es,en}/` — bilingual content. Pages with different filenames across languages need `translationKey` in frontmatter to pair translations
- **Editorial planning:** `content/just-ideas-for-future-posts/` — 11 category folders + master catalog, outside Hugo's content tree, not rendered
- **Custom layouts:**
  - `layouts/_default/cv.html` — wraps content in `.cv-page` div, used by CV, consulting, and skills pages
  - `layouts/partials/head-additions.html` — per-page CSS loading via `page_css` frontmatter param; inlines CSS from `assets/ananke/css/`
  - `layouts/partials/site-header.html` — overrides the theme's site header. Identical to the theme copy in the *with-featured-image* branch; in the *no-featured-image* branch (used by the homepage and any post without `featured_image`), it trims the tall black banner on desktop: outer `pb6-l` → `pb2-l` (8rem → 0.5rem bottom padding), title `f-subheadline-l` → `f1-l` (5rem → 3rem), subtitle `f3-l` → `f4-l` with margins `mt3 mb4` → `mt2 mb2`. Mobile layout matches the theme default.
- **Custom CSS:**
  - `assets/ananke/css/cv.css` — styles scoped under `.cv-page`, targeting standard HTML elements via Hugo auto-generated heading IDs
  - `assets/ananke/css/skills.css` — styles for the skills page
  - `assets/ananke/css/tables.css` — borders and padding for markdown tables; loaded per-post via `page_css` frontmatter
- **Archetype:** `archetypes/default.md` emits TOML frontmatter with auto-date and title derived from filename (but published posts use YAML — see Code style guidelines)
- **Pagination:** 3 per page (intentionally low)
- **Static assets:** `favicon/` has the favicon; `static/` is empty

## Per-page CSS pattern

Add to frontmatter to load page-specific CSS without affecting other pages:

```toml
layout = "cv"
page_css = ["cv.css"]
```

The partial `head-additions.html` reads the `page_css` list and inlines each stylesheet from `assets/ananke/css/`.
