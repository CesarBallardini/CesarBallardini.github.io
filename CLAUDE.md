# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Git rules (NEVER break)

**Do not run any git command that adds, deletes, or modifies the repository state.** This includes, but is not limited to:

- `git commit` (including `--amend`)
- `git add` / `git rm` / `git mv` / `git restore` / `git reset`
- `git push` / `git pull` / `git fetch` with side effects
- `git branch` (create/delete) / `git checkout` / `git switch`
- `git merge` / `git rebase` / `git cherry-pick` / `git revert`
- `git stash` (push/pop/apply)
- `git tag` (create/delete)
- `git clean`
- `git submodule` mutations

**Read-only git is allowed:** `git status`, `git diff`, `git log`, `git show`, `git blame`, `git ls-files`, `git config --get`.

**If the user asks for a commit, push, branch change, etc.:** draft the command or the commit message as text and let the user run it themselves. Never execute it.

## What This Is

Personal bilingual Hugo blog ("katra") by César Ballardini, published at https://katra.ballardini.com.ar/. Content is primarily in Spanish (es-AR), with an English section prepared but currently empty.

## Build & Development Commands

```bash
hugo server          # Local dev server with live reload (default: http://localhost:1313/)
hugo server -D       # Include draft posts
hugo                 # Build site to ./public/
hugo new content/es/posts/YYYY-MM-DD-slug-here/index.md   # Create a new Spanish post (page bundle)
```

No Makefile, no npm scripts, no other build tooling in the root. The theme has its own package.json but that's managed upstream.

## Deployment

GitHub Actions (`.github/workflows/static.yml`) deploys the pre-built `./public/` directory to GitHub Pages on every push to `master`. There is **no Hugo build step in CI** — the `public/` directory must be committed and up to date before pushing.

Because `public/` is committed, stale files from previous builds (old slugs, removed tags, renamed posts) do not get cleaned automatically. Build with `hugo --cleanDestinationDir` to drop orphan files, or `rm -rf public && hugo` for a fully fresh tree before committing.

**Staging caveat:** if `hugo` is re-run after `git add`-ing `public/`, the rebuild overwrites the staged files and the commit will capture the older build. Re-stage with `git add -u public/` (and add any newly-untracked files) before committing.

**Never commit a `hugo server` build.** `hugo server` rewrites `baseURL` to whatever localhost port it picked (e.g. `http://localhost:3131/`) and bakes that into every `<link rel="canonical">`, `og:url`, sitemap entry, RSS `<link>`, and internal nav href; it also injects a `/livereload.js?...port=NNNN` script into every page and emits a non-fingerprinted `public/ananke/css/main.min.css` alongside the fingerprinted asset that the HTML actually references. Any of those leaking to GitHub Pages breaks the RSS feed for subscribers and the canonical URL for search engines. Always do a fresh `hugo --cleanDestinationDir` (or `rm -rf public && hugo`) before staging `public/`, and verify with `grep -rl "localhost:" public/ | wc -l` returning `0`.

## Content Conventions

- **Post format:** all posts use **page bundles** — `content/es/posts/YYYY-MM-DD-slug/index.md` with images and assets as siblings inside the same folder. Flat `.md` files are the old format; do not create new ones.
- **Post filename pattern:** `YYYY-MM-DD-slug-in-lowercase` — Hugo extracts the date from the directory name (`[frontmatter] date = [':filename', ':default']`)
- **Spanish posts go in:** `content/es/posts/`
- **English posts go in:** `content/en/posts/`
- **Frontmatter:** YAML (`---`) for all 2025+ posts. The full house rules — frontmatter shape, tag rules (no periods, Hugo Windows limitation), footnote style (named, never numeric), internal link rules (no `/es/` prefix in Spanish URLs), image bundles vs flat files, voice — live in [`content/just-ideas-for-future-posts/near-future-posts.md`](content/just-ideas-for-future-posts/near-future-posts.md) under "Convenciones de la casa". Read that section before writing or editing a post — it reflects the actual practice in the published posts, not what `AGENTS.md` says (they conflict; the published posts win).
- **Hero banner:** every post has `featured_image: hero-filename.jpg` in frontmatter. The image lives in the post's bundle folder. Use landscape-oriented images (2.5:1 ratio or wider); portrait photos must be cropped with Pillow before use (`uv run --with Pillow python`). `featured_image_class = "cover bg-center"` is set globally in `hugo.toml`.
- **Per-page CSS:** add `page_css: ['tables.css']` to frontmatter for posts with markdown tables. The CSS lives at `assets/ananke/css/tables.css` and is loaded via the `layouts/partials/head-additions.html` partial.
- **Image attribution:** every public domain or CC-licensed image requires a named footnote with URL, author, and license. Example: `[^img_foo]: Imagen de [Title](URL) — CC BY-SA 4.0 — Author.` If the image was cropped or otherwise adapted for the blog, note that at the end of the footnote (e.g. "Recortada a 2.5:1 para hero landscape.").
- **Academic paper citations:** when a paper's canonical URL (IEEE Xplore, Springer, ACM DL) is paywalled or blocks automated fetch (IEEE returns HTTP 418), the footnote should link to a **stable DOI** (`https://doi.org/10.XXXX/...`) as the canonical reference plus a **free full-text mirror** when one exists (university course pages, archive.org, the author's Wikipedia page). Always include journal name / volume / issue / year in the footnote regardless of linkability.
- **Verify fragile URLs before publishing:** YouTube links, personal blogs, and university-course paper mirrors move or disappear. Check that each fragile URL responds before the post ships; for load-bearing sources keep a Wayback Machine backup link in the footnote.
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

1. **Ideas are kept forever, never deleted for staleness.** When an idea cools off, mark its `Estado actual:` as `en hibernación` or `concepto refinado` and leave the draft file in place. The only legitimate reason to delete a draft is that the concept has been factually superseded or the post has been published with no remaining improvements. Do not suggest deleting unwritten drafts in maintenance passes. When a post is published: delete the draft file and remove its entry from the index **only if** the draft has no pending improvements listed. If it has pending improvements (cross-links to add, possible follow-up posts, etc.), keep both the draft and the index entry.
2. **The author has lived experience in some of these topics** (Argentine public-sector IT — STG and Ministerio de Cultura Santa Fe in particular) and personal life topics in Series K. Do not invent details about institutions, projects, dates, or personal circumstances; ask the user or leave gaps in the entry. The drafts already in place reflect this — they have placeholders where verification is needed.

**When the user says "the plan" or "the editorial plan"**, they mean `content/just-ideas-for-future-posts/near-future-posts.md` and the 11 category folders alongside it.

## Architecture

- **Theme:** Ananke, included as a git submodule at `themes/ananke` (source: `github.com/theNewDynamic/gohugo-theme-ananke`)
- **Custom partial:** `layouts/partials/head-additions.html` — injects per-page CSS listed in the `page_css` frontmatter array
- **Custom partial:** `layouts/partials/site-header.html` — overrides the theme's site header. Identical to the theme copy in the *with-featured-image* branch; in the *no-featured-image* branch (used by the homepage and any post without `featured_image`), it trims the tall black banner on desktop: outer `pb6-l` → `pb2-l` (8rem → 0.5rem bottom padding), title `f-subheadline-l` → `f1-l` (5rem → 3rem), subtitle `f3-l` → `f4-l` with margins `mt3 mb4` → `mt2 mb2`. Mobile layout matches the theme default.
- **Custom CSS:** `assets/ananke/css/tables.css` — adds borders and padding to markdown tables; loaded via `page_css` frontmatter
- **Archetype:** `archetypes/default.md` uses TOML frontmatter with auto-date and title derived from filename
- **Config:** Single file `hugo.toml` — bilingual setup with Spanish (weight 1) as default, English (weight 2) secondary; `featured_image_class = "cover bg-center"`
- **Pagination:** Currently set to 3 per page (intentionally low)
- **Static assets:** `favicon/` directory has the favicon; `static/` is empty

## Submodule

After cloning, initialize the theme submodule:
```bash
git submodule update --init --recursive
```

## External Reference Sites

Sites approved for browsing when researching content for this blog:

- **[Internet Archive](https://archive.org/)** — book lookups, borrowable texts, C-SPAN recordings, historical media; also the Wayback Machine for backup copies of fragile URLs.
- **[Wikimedia Commons](https://commons.wikimedia.org/)** — images with clear licensing (CC, public domain) for blog post illustrations.
- **[llmstxt.org](https://llmstxt.org/)** — specification for the `llms.txt` file format.
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** — specification for the `AGENTS.md` file format.
- **[Science Museum Group Collection](https://collection.sciencemuseumgroup.org.uk/)** — historical engineering artifacts and images (typically CC-BY-NC-SA 4.0).
- **[Fundación Vía Libre](https://www.vialibre.org.ar/)** — Argentine digital rights foundation; primary source for local debates on software libre, colegiación profesional de informáticos, voto electrónico, políticas de IA en Latinoamérica, privacidad y propiedad intelectual.
- **[EWD archive — UT Austin](https://www.cs.utexas.edu/~EWD/)** — Edsger Dijkstra's writings (EWD manuscripts), both HTML transcriptions and PDF scans of the originals. Stable.
- **[DOI resolver](https://doi.org/)** — canonical citation URL for academic papers; use as the primary link when the publisher page is paywalled.
