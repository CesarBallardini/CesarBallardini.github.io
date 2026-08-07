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

Personal bilingual Hugo blog ("katra") by César Ballardini, published at https://katra.ballardini.com.ar/. Content is primarily in Spanish (es-AR); the English section has a small number of translated posts (not a 1:1 mirror of the Spanish content).

## Build & Development Commands

```bash
hugo server          # Local dev server with live reload (default: http://localhost:1313/)
hugo server -D       # Include draft posts
hugo                 # Build site to ./public/
hugo new content/es/posts/YYYY-MM-DD-slug-here/index.md   # Create a new Spanish post (page bundle)
```

No Makefile, no npm scripts, no other build tooling in the root. The theme has its own package.json but that's managed upstream.

**Local build artifacts**: `resources/_gen/` (Hugo's derived-asset cache — minified/fingerprinted CSS, processed images) is gitignored; safe to delete and let Hugo regenerate it. `.hugo_build.lock` is also gitignored. `public/` is the one build artifact that **is** committed (see Deployment below) — clean it with `hugo --cleanDestinationDir`, never delete it outright.

## Deployment

GitHub Actions (`.github/workflows/static.yml`) deploys the pre-built `./public/` directory to GitHub Pages on every push to `master`. There is **no Hugo build step in CI** — the `public/` directory must be committed and up to date before pushing.

Because `public/` is committed, stale files from previous builds (old slugs, removed tags, renamed posts) do not get cleaned automatically. Build with `hugo --cleanDestinationDir` to drop orphan files, or `rm -rf public && hugo` for a fully fresh tree before committing.

**Staging caveat:** if `hugo` is re-run after `git add`-ing `public/`, the rebuild overwrites the staged files and the commit will capture the older build. Re-stage with `git add -u public/` (and add any newly-untracked files) before committing.

**Future-dated posts vanish without a word.** Hugo excludes content dated later than "now" unless `--buildFuture` is passed. Because the date comes from the bundle directory name and there is **no build step in CI**, a post dated tomorrow is simply absent from `public/` — no warning, no error, and the deploy succeeds. Run `hugo list future` before building: if it lists something you meant to publish, either build with `hugo --cleanDestinationDir --buildFuture` or rename the bundle to an earlier date. The flag is self-correcting — once the date arrives, a plain rebuild produces the same tree — but a bundle renamed to a future date after `public/` was built is the way a post silently disappears from the live site.

### Publishing a post — the command sequence (César runs these; Claude never does)

Claude is forbidden from running any of this (see "Git rules" above). It drafts the commands; César executes them. Order matters: **build first, stage second, never rebuild after staging.**

```bash
# 1. What is Hugo about to silently drop?  Empty output = nothing future-dated.
hugo list future

# 2. Build.  Add --buildFuture ONLY if step 1 listed something you want published now.
hugo --cleanDestinationDir --buildFuture

# 3. Verify the build is not a `hugo server` artifact.  Both must be clean:
grep -rl "livereload" public/ | wc -l    # must be 0
grep -rl "localhost:" public/ | wc -l    # must be 1 — the 2016 Jekyll post mentions localhost:4000

# 4. Stage the content, then public/.  Adjust the content paths to the post at hand.
git add content/es/posts/YYYY-MM-DD-slug/
git add content/just-ideas-for-future-posts/
git add -u public/ && git add public/

# 5. Confirm nothing unrelated snuck in, then commit and push.
git status --short
git commit
git push origin master
```

**Traps this sequence exists to avoid**, each of which has bitten before:

- **Re-running `hugo` after `git add public/`** silently commits the *previous* build. If you must rebuild, re-run step 4.
- **`git add -u public/` alone misses new files** (a new post's directory is untracked, not modified). That is why step 4 has both `add -u` and a plain `add`.
- **`git add -A` from the repo root** sweeps in every unrelated modified draft in `content/just-ideas-for-future-posts/`. Stage explicit paths and read `git status --short` before committing.
- **A future-dated bundle** is absent from `public/` with no warning and the deploy still succeeds. That is what step 1 is for.

**Never commit a `hugo server` build.** `hugo server` rewrites `baseURL` to whatever localhost port it picked (e.g. `http://localhost:3131/`) and bakes that into every `<link rel="canonical">`, `og:url`, sitemap entry, RSS `<link>`, and internal nav href; it also injects a `/livereload.js?...port=NNNN` script into every page and emits a non-fingerprinted `public/ananke/css/main.min.css` alongside the fingerprinted asset that the HTML actually references. Any of those leaking to GitHub Pages breaks the RSS feed for subscribers and the canonical URL for search engines. Always do a fresh `hugo --cleanDestinationDir` (or `rm -rf public && hugo`) before staging `public/`, and verify with `grep -rl "localhost:" public/ | wc -l` returning `0`.

## Pre-publish checks

Run these against a build before committing a post. Each one has caught a real defect that reads as fine in the source — Hugo reports none of them as errors, because none of them are.

- **`hugo list future`** — a future-dated bundle is missing from the site with no warning. See Deployment above.
- **Internal links, resolved against the built tree.** Walk `public/**/*.html`, extract every `href="/..."`, and check the path exists as a file or a directory with an `index.html`. The recurring mistake is writing the *dated* bundle name into a link (`/posts/2026-08-03-slug/`) when the permalink strips the date, or leaving a `.md` extension on the target; both 404 silently and neither is visible in the markdown.
- **Footnotes: definitions versus references.** Collect `id="fn:N"` and `href="#fn:N"` from the rendered HTML and compare the sets both ways. A footnote defined but never referenced is dead weight; one referenced but never defined renders as literal `[^name]` text in the middle of a paragraph. Also grep the output for a stray `[^` — if the count is not zero, a definition line got merged into its neighbour and stopped being a definition. **This is how an image's licence attribution goes missing**, which for CC BY-SA is a licence violation and not a typo.
- **External URLs.** Check each one responds; see "Verify fragile URLs" below. Links into this repository on GitHub will 404 until the commit is pushed — expected, not a failure.
- **`grep -rl "localhost:" public/`** — see Deployment above. Note that a legitimate hit exists: a 2016 post about Jekyll mentions `localhost:4000` in its prose.

## Content Conventions

- **Post format:** all posts use **page bundles** — `content/es/posts/YYYY-MM-DD-slug/index.md` with images and assets as siblings inside the same folder. Flat `.md` files are the old format; do not create new ones.
- **Post filename pattern:** `YYYY-MM-DD-slug-in-lowercase` — Hugo extracts the date from the directory name (`[frontmatter] date = [':filename', ':default']`). Renaming the directory therefore changes the post's date but **not** its URL; it does change any hard-coded GitHub links that point at the bundle path, so grep for the old directory name after a rename.
- **What a page bundle publishes:** every *non-page* resource in the bundle directory is copied to the output — images, PDFs, SVGs, `.py`, `.txt`, and subdirectories with them. But `.md` files other than `index.md` are treated as **page** resources and are **not** copied, so they exist in the repository and not on the site. Link to those on GitHub, or rename them to `.txt` if they have to be downloadable from the post. Confirm what actually shipped with `find public/posts/<slug> -type f` after a build.
- **Spanish posts go in:** `content/es/posts/`
- **English posts go in:** `content/en/posts/`
- **Frontmatter:** YAML (`---`) for all 2025+ posts. The full house rules — frontmatter shape, tag rules (no periods, Hugo Windows limitation), footnote style (named, never numeric), internal link rules (no `/es/` prefix in Spanish URLs), image bundles vs flat files, voice — live in [`content/just-ideas-for-future-posts/near-future-posts.md`](content/just-ideas-for-future-posts/near-future-posts.md) under "Convenciones de la casa". Read that section before writing or editing a post — it reflects the actual practice in the published posts, not what `AGENTS.md` says (they conflict; the published posts win).
- **Hero banner:** every post has `featured_image: hero-filename.jpg` in frontmatter. The image lives in the post's bundle folder. Use landscape-oriented images (2.5:1 ratio or wider); portrait photos must be cropped with Pillow before use (`uv run --with Pillow python`). `featured_image_class = "cover bg-center"` is set globally in `hugo.toml`.
- **Per-page CSS:** add `page_css: ['tables.css']` to frontmatter for posts with markdown tables. The CSS lives at `assets/ananke/css/tables.css` and is loaded via the `layouts/partials/head-additions.html` partial.
- **Mermaid diagrams:** add `mermaid: true` to frontmatter to live-render ```` ```mermaid ```` fences (loaded via `layouts/partials/hooks/body-end.html`, see Architecture below). Without the flag, a mermaid fence just renders as unstyled plain code.
  - **Truncated node labels?** Add `mermaid_html_labels: true` as well. Mermaid's default `securityLevel: 'strict'` forces `htmlLabels: false`, so the library measures label width itself instead of letting the browser do it; with accents and symbols (`↔`, `á`, `í`) it under-measures and clips long labels mid-word. The flag switches that page to `securityLevel: 'antiscript'` + `htmlLabels: true` — the browser measures the real text, and `<br/>` works for manual line breaks. It is **opt-in per post on purpose**: enabling it site-wide would silently re-flow the diagrams in already-published posts. `'antiscript'` allows HTML in labels but drops `<script>`; prefer it over `'loose'`.
- **Math formulas:** write LaTeX directly — `\( ... \)` inline, `\[ ... \]` or `$$ ... $$` for display. **Rendered at build time** by `layouts/_markup/render-passthrough.html` via `transform.ToMath` (KaTeX compiled into the Hugo binary), which emits native MathML. No JavaScript, no CDN, no stylesheet, and screen-reader friendly. No frontmatter flag is needed. Requires `[markup.goldmark.extensions.passthrough]` in `hugo.toml` — without it Goldmark mangles `_`, `\` and `{}` before the math renderer sees them (`k_B` turns into italics).
- **Electronic schematics (KiCad):** the `/370-145` panel post keeps its schematics in `kicad/` inside the bundle — Python generators that emit `.kicad_sch` and a symbol library, plus the PDF and SVG exported with `kicad-cli`. They are *generated by script rather than drawn by hand* so a layout fix is a re-run, not an afternoon of dragging symbols. If you touch one, re-export and re-verify: `kicad-cli sch erc` for wiring, **plus `kicad-cli sch export netlist` whenever the change could move a component**. The two catch different things — ERC finds off-grid endpoints and wires that stop a fraction of a millimetre short of a pin, while only the netlist proves which pins actually share a net. A schematic can be drawn so cramped that it reads as a series chain and still be wired correctly, and it can look impeccable and be wired wrong; neither check alone tells you which.
- **Read-aloud audio player:** a client-side text-to-speech player (browser `speechSynthesis`, no cloud TTS, no API key) is injected on every content page **by default** — it is opt-**out**, not opt-in. To suppress it on a specific post, set `audio_player: false` in frontmatter. UI language and voice follow the page language (`.Language.Lang`). Injected via `layouts/partials/hooks/body-end.html` with CSS in `assets/ananke/css/audio-player.css` (see Architecture below).
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

**Cross-references between drafts** use `[[ID]]` notation (e.g., `[[A1-03]]`, `[[tr-07]]`, `[[K-12]]`) during drafting; they get resolved to real `[texto](/posts/slug/)` URLs at publication time. Each post has a stable ID `{series}-{NN}`.

**Internal link URLs never contain the date.** The page bundle is `content/es/posts/YYYY-MM-DD-slug/`, but Hugo strips the date prefix when building the permalink (`date = [':filename', ':default']` consumes it), so the published URL is `/posts/slug/` — e.g. the bundle `2025-03-10-soplar-humo-de-tabaco/` is served at `/posts/soplar-humo-de-tabaco/`. Writing `/posts/2025-03-10-soplar-humo-de-tabaco/` produces a 404: no alias is generated for the dated form. Verify with a build (`hugo -d /tmp/check`) and confirm the target `index.html` exists before publishing a post that cross-links.

**Expanded drafts (`## Borrador de prosa`)** — as of 2026-07-15, 66 drafts carry an extra `## Borrador de prosa` section appended after `**Estado actual:**`, holding full Spanish prose. These were generated with Claude's assistance and are marked `**Madurez:** prosa-borrador (... sin revisar por César)`. **This prose is unreviewed and is not publication-ready.** Four markers appear inside it, and each means something specific:

| Marker | Meaning | Rule |
|---|---|---|
| `🕳️ **HUECO — necesita a César:**` | A memory, opinion, anecdote or biographical fact only César can supply. | Never fill one in. No source answers it. Only César resolves these. |
| `[VERIFICAR: ...]` | A factual claim (number, date, attribution) that the draft's bibliography does not support. | Never delete without a fetched source that actually settles it. Deleting an unresolved marker silently converts "I don't know" into a false claim. |
| `⚠️ PREMISA EN DUDA:` (in `**Estado actual:**`) | Sources contradict, or fail to support, the draft's own Hook/Concepto. | The post needs its premise fixed before more prose is worth writing. Do not "fix" it by editing the Hook — it is César's. |
| `estable` / `frágil` | Bitrot risk flag on a bibliography entry. | Fragile load-bearing URLs need a Wayback backup before publishing. |

**Known-bad premises**: the 2026-07-15 sourcing pass found that several drafts rest on claims that sources contradict (e.g. C-13 names a Cutler article that does not exist; C-03 says Beck offers three options where the book has four; A1-13's chapter-order argument is falsified by the book's actual order; C-15's framing ignores that the Beck×Noda conversation was sponsored by DX). **Do not treat a draft's Concepto or Hook as established fact.** Check before building on it.

**When writing or expanding a draft, never invent**: a URL, DOI, ISBN, page number, edition year, or a fact about a real named person. Cite only what has been fetched and confirmed. An honest gap beats a plausible fabrication — this rule outranks completeness, length targets, and prose quality.

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
- **Custom partial:** `layouts/partials/site-header.html` — overrides the theme's site header. Two customizations beyond the theme copy: (1) in the *no-featured-image* branch (used by the homepage and any post without `featured_image`), it trims the tall black banner on desktop: outer `pb6-l` → `pb2-l` (8rem → 0.5rem bottom padding), title `f-subheadline-l` → `f1-l` (5rem → 3rem), subtitle `f3-l` → `f4-l` with margins `mt3 mb4` → `mt2 mb2` — mobile layout matches the theme default; (2) when the `<h1>` is showing the site title (i.e., `.Title` is unset or equals `.Site.Title` — homepage and any page without its own title), the title is wrapped in an anchor + native `title=""` tooltip pointing to the explainer post in the page's language: ES → `/posts/por-que-katra/` with tooltip "¿Por qué katra?", EN → `/en/posts/why-katra/` with tooltip "Why katra?". Built with `relLangURL` (not `relURL`) so the language prefix is correct; if a third language is added, mirror the post under that language section and extend the `cond` block. Pages with their own `.Title` (every blog post, CV, etc.) render the page title as plain text, unchanged from the theme.
- **Custom CSS:** `assets/ananke/css/tables.css` — adds borders and padding to markdown tables; loaded via `page_css` frontmatter
- **Custom CSS:** `assets/ananke/css/audio-player.css` — the read-aloud player's styles: the `.reading-now` highlight for the paragraph being spoken, the `#katra-apProgress` range-thumb styling, and small-screen positioning of the fixed panel. Not loaded via `page_css`; it is inlined by `body-end.html` (via `resources.Get` + `safeCSS`) only when the player is present.
- **Custom partial:** `layouts/partials/hooks/body-end.html` — overrides the theme's `_partials/hooks/body-end.html` hook point (theme's hook-dispatch mechanism resolves `hooks/<name>.html` by name via `templates.Exists`, so a same-named project partial shadows/adds behavior without touching the submodule). Hosts **two** independent, self-contained blocks:
  - **Mermaid** (opt-in, `mermaid: true`): injects a `<script type="module">` that imports mermaid.js from a CDN (jsdelivr), converts every `pre > code.language-mermaid` block (the markup Goldmark emits for a ```` ```mermaid ```` fence) into a `<div class="mermaid">` using `.textContent` (Chroma has no mermaid lexer so the fence renders unhighlighted, but entities are still HTML-escaped in the source — `.textContent` decodes them correctly), then calls `mermaid.initialize({ startOnLoad: true, theme: 'neutral' })`. Not loaded site-wide. When `mermaid_html_labels: true` is also set, the init call instead uses `securityLevel: 'antiscript'` + `flowchart: { htmlLabels: true, useMaxWidth: true }` to stop long labels from being clipped (see Content Conventions). The two branches are kept separate deliberately so pages that don't opt in emit byte-identical output to before the flag existed.
- **Custom render hook:** `layouts/_markup/render-passthrough.html` — converts LaTeX passthrough blocks to MathML at build time with `transform.ToMath`. Pairs with `[markup.goldmark.extensions.passthrough]` in `hugo.toml`, which protects the math delimiters from the markdown parser. Output is `output: "mathml"`, so pages ship no math JavaScript, no KaTeX CSS and no webfonts — browsers render MathML natively. Note the path: Hugo 0.146+ uses `layouts/_markup/`, not the older `layouts/_default/_markup/`.
  - **Read-aloud audio player** (opt-**out**, guarded by `{{ if and .IsPage (ne .Params.audio_player false) }}`): a fixed bottom-left panel plus a vanilla-JS controller using the browser's `speechSynthesis` API — **no cloud TTS, no CDN, no API key**. It collects the article title (`article header h1`) then `h2`–`h4`, `p`, `li`, `blockquote` inside `article .nested-copy-line-height` (skipping tag pills `ul.pa0`, `.footnotes`, and duplicated blockquote containers; stripping `sup`/anchor/footnote-ref nodes), and reads them paragraph by paragraph, highlighting the current one via `.reading-now`. UI strings, TTS locale, and voice preference come from per-language tables keyed on `.Language.Lang` (`es`/`en`). Voice selection is **locale-first** (`getBestVoice` exhausts each locale in the preference `order` — best gender/quality within it — before the next), so `es-US` is always tried before `es-ES`; on **Android** the Spanish `order` is reordered to lead with `es-US` (the only Spanish voice usually installed there is Castilian). Robustness: hides itself when `speechSynthesis` is absent or the page has no `.nested-copy-line-height` body; works around unreliable native pause on Android/Firefox by cancel-and-respeak; remembers the visitor's voice pick in `localStorage` per language. The player CSS lives in `assets/ananke/css/audio-player.css` and is inlined by this partial. When editing the player, remember `public/` is committed — rebuild with `hugo --cleanDestinationDir` so every page's rendered copy stays in sync.
- **Archetype:** `archetypes/default.md` uses TOML frontmatter with auto-date and title derived from filename
- **Config:** Single file `hugo.toml` — bilingual setup with Spanish (weight 1) as default, English (weight 2) secondary; `featured_image_class = "cover bg-center"`
- **Pagination:** Currently set to 3 per page (intentionally low)
- **Static assets:** `favicon/` directory has the favicon; `static/` is empty

## Submodule

After cloning, initialize the theme submodule:
```bash
git submodule update --init --recursive
```

The ananke repo's default/actively-maintained branch is **`main`**, not `master` (`master` is a stale branch there, last updated 2024-10-18, and checking it out is a downgrade that breaks the build — `git checkout origin/master` produced a `can't evaluate field Social in type interface {}` render error in `social-share.html`). To update the submodule to the latest fixes, use `git checkout origin/main` from inside `themes/ananke/`, then rebuild and verify `hugo --cleanDestinationDir` succeeds with no warnings before committing the new submodule pointer.

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

## Work in progress — post 2 de DCI (`2026-08-05-dci-en-python-roles-en-runtime`)

**Estado: NO publicado**, sincronizado con el repo de código y revisado al 2026-08-07.
Borrar esta sección cuando el post se publique.

### Las cuatro piezas

| Pieza | Dónde | Para qué |
| --- | --- | --- |
| El post | `content/es/posts/2026-08-05-dci-en-python-roles-en-runtime/index.md` | lo que se publica |
| El plan de la sincronización | `.../2026-08-07-plan-mejoras.md` (mismo bundle) | qué se corrigió contra el repo y por qué |
| El plan anterior | `.../2026-08-05-draft-doc.md` (mismo bundle) | histórico; no sirve para planificar |
| El repo de código | `C:/Users/cesar/cesar/github/CesarBallardini/dci-in-python` | **la fuente de verdad de todo el código y todas las salidas** |

El repo está commiteado (`1264e87`) y publicado en `github.com/CesarBallardini/dci-in-python`, **en la rama `main`** — no `master`. Los seis enlaces del post a archivos del repo usan `blob/main/`; escribir `blob/master/` da 404.

### El post hoy

Diecinueve secciones, **~7850 palabras** de cuerpo, 18 notas al pie, 6 tablas, 4 diagramas mermaid, 27 bloques de código. La estructura:

1. La transferencia, tres veces (con la objeción de Feathers como paréntesis)
2. La maquinaria — el `Context` en 25 líneas, más el cuadro «De qué está hecho, exactamente» con los recursos de Python 3.14
3. Algunos escenarios donde el modelo de objetos de Python falla — las cuatro fallas
4. Cuatro maneras de prestar un rol — los cuatro binders y su tabla
5. La pregunta que decide si esto se puede usar — persistencia y ORM
6. Un paréntesis: la librería que hay (Molenaar)
7. Cinco maneras de escribir la misma transferencia — con su tabla
8. Y en tu código, ¿cuál? — la tabla de decisión de siete filas
9. El veredicto

### Verificado el 2026-08-07

- **Build limpio**: 18 notas definidas / 18 referenciadas, cero `[^` sueltos, 6 tablas, 4 mermaid.
- **Los 30 enlaces externos dan HTTP 200**, incluidos los seis del repo en `main` y `fulloo.info/Examples/`.
- **`hugo list future` vacío.**
- **Las salidas de consola** coinciden carácter por carácter con `uv run --frozen python demo/dci_demo.py`. No hay nada que repegar salvo que se toque la demo.
- **El código simplificado del post corre**: se extrajo a un script y da la misma salida que la sección 1 de la demo.

### El hallazgo que el post tiene y el repo no

**Dos contextos con roles _distintos_ sobre el mismo objeto no dan error de MRO: ligan.** Medido el 2026-08-07 corriendo el repo. `Account@SourceAccount@DestinationAccount` se construye sin quejarse; el primer contexto que sale le arranca los métodos al segundo, y cuando el segundo sale deja el objeto como `Account@SourceAccount` **de manera permanente y fuera de todo contexto**. El lock lo cubre (verificado: cero errores, clase final `Account`, saldo correcto).

`APPROACHES.md` y `test_limits.py` sólo cubren el caso del **mismo** rol, así que hoy el post afirma algo más preciso que su propio repositorio. **Pendiente del repo**: un test que fije el caso de roles distintos, y el ajuste al documento.

### CSS

El post carga `page_css: ['tables.css', 'code.css']`. `code.css` se ajustó en esta sesión: `font-size: 0.82rem` y selector ampliado a `.code-block` además de `.highlight`, porque los fences **sin lenguaje** —todas las salidas de consola— no pasan por Chroma y quedaban al tamaño del tema. **`code.css` es compartido con el post `python-tooling-backend-desde-cero`**, así que ese post también cambia de tamaño y su `public/` va a aparecer modificado sin que se lo haya tocado.

### Lo que queda abierto

- **La cuenta de líneas.** El post muestra un mecanismo de **veinticinco** líneas y después dice tres veces **«cincuenta líneas»** refiriéndose a lo mismo. El párrafo que explicaba la diferencia (25 mostradas contra 51 en el repo, medidas con `ast`) se borró en la pasada de estilo. Es la única inconsistencia visible que queda.
- **La tabla de versiones de `roles`** está fechada el 4 de agosto de 2026. Es lo que primero envejece.
- **Los dos documentos de planificación del repo** (`2026-08-06-presentation.md`, `2026-08-06-comparative-readme.md`) están **sin commitear**. No enlazarlos desde el post.
- **La parte 1 no necesitó cambios.** Su párrafo sobre el ORM está deliberadamente hedgeado («el mecanismo canónico de DCI, el de reasignarle la clase») porque `InstanceContext` sí toma la entidad declarativa; si se edita esa sección, no perder el matiz.

### Reglas que no hay que perder de vista

- Nada de código ni de salidas escritas a mano: todo sale de correr el repo. Si una salida cambia, se re-corre `make demo` y se pega, sin traducir.
- El post y el repo tienen que contar la misma historia. Cada vez que se toque uno, revisar el otro.
- Cuando este archivo y el repo no coinciden, gana el repo.
- **En una pasada de edición, una referencia que quedó sin destino se arregla cambiando la referencia, no reponiendo el texto borrado.** Si César borró algo, borrado está.
