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

### Makefile

`make` (or `make help`) lists the targets. The common ones:

| Target | What it does |
| --- | --- |
| `serve`, `serve-drafts`, `serve-future` | `hugo server`, plain / with drafts and future posts / with future posts |
| `new SLUG=mi-post [IDIOMA=en]` | `hugo new` for a dated page bundle; the archetype writes the house YAML frontmatter |
| `future`, `drafts` | `hugo list future` / `hugo list drafts` |
| `build [FUTURE=1]` | `hugo --cleanDestinationDir` into `public/`, then `verify` |
| `build-one POST=<bundle>` | the single-post recipe below: committed content plus one bundle, into `public/` |
| `files POST=<bundle>` | what that bundle actually ships under `public/` |
| `verify` | `tools/check_site.py public`: internal links, footnotes on post pages, stray `[^`, livereload, `localhost:` |
| `check` | `future`, `check-site` (builds everything on disk into `.check/` and runs the same checks), `mermaid` and `spell` |
| `urls`, `mermaid`, `spell` | external URLs (`tools/check_urls.py`), diagrams against mermaid.ink (`tools/check_mermaid.py`), cspell |
| `clean` | removes `resources/_gen`, `.hugo_build.lock` and `.check/`; never `public/` |
| `publish-steps` | prints the publishing sequence; it runs nothing |

`urls`, `mermaid` and `spell` take `POST=<bundle>` or `POSTS="a.md b.md"`; without either they check the posts that `git status` shows as modified or new. **No target runs a git command that changes the repository**: the only git calls are `git ls-files` and `git archive`, both read-only. `setup` runs `git submodule update --init` and is meant for César after a clone.

`make spell` needs `make spell-install` once: cspell and the Spanish dictionary go into `.cspell/node_modules/` (gitignored), pinned by `.cspell/package-lock.json`, and `.cspell/cli.json` adds that dictionary to the repo's `cspell.json`. VS Code does not need any of this; it gets Spanish from its extension.

Machine-specific settings go in `local.mk` (gitignored), which the Makefile includes if present. On this machine it sets `NODE` and `NPM` to the full nvm paths, because `node` is not on the PATH that make sees from Git Bash.

The Makefile variable for the post language is `IDIOMA`, not `LANG`: `LANG` is the locale variable and is usually already set in the environment.

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
- **Files left staged by earlier work ride along.** A bare `git commit` takes everything in the index, not just what step 4 added. Check `git diff --cached --name-only` for paths that belong to another post, and either unstage them (`git restore --staged <paths>`, which leaves the files on disk) or commit with a pathspec (`git commit -- <bundle>/ public/`, which commits only those paths and leaves the rest staged).

### Publishing one post while others are unfinished

`hugo` renders everything under `content/`, so step 2 above publishes every bundle on disk, including a series still in progress and any uncommitted edit to an already-published post. To ship a single post, build from what is already committed plus that one bundle, straight into `public/`:

```bash
T=$(mktemp -d)
git archive HEAD | tar -x -C "$T"                    # committed content only
cp -r themes/ananke/. "$T/themes/ananke/"            # git archive leaves submodules empty
cp -r content/es/posts/YYYY-MM-DD-slug "$T/content/es/posts/"
hugo -s "$T" -d "$(pwd -W)/public" --cleanDestinationDir   # pwd -W: hugo.exe needs a Windows path
grep -rl "<slug-of-an-unfinished-post>" public/ | wc -l    # must be 0
```

Then continue from step 4, committing with a pathspec. First used 2026-09-18 to publish `sobre-estudiar-llms-y-plantar-arboles` while the four cafetera posts sat in `content/`, two of them already staged.

**What an honest single-post diff looks like:** the new post directory, any new tag directories, and real changes only in listing pages (home, `posts/page/N/`, RSS, sitemaps, the post's tags) and in the "related posts" block of a few older posts. If every page in `public/` shows as modified, check whether the only difference is `<meta name="generator" content="Hugo 0.x">` — that is a Hugo upgrade since the last build, not a content change. Compare with `git diff --cached -I 'name="generator"' --quiet -- <file>`.

**Paths under the domain that are not this repo.** `katra.ballardini.com.ar` is this user site's custom domain, so every GitHub Pages *project* site of the account is served under it: `https://katra.ballardini.com.ar/llm-for-dummies-study-plan/` is the MkDocs book from the `llm-for-dummies-study-plan` repo, `/dci-in-python/` is that repo's JupyterLite site, and `/coffee-maker-designs/` will be the cafetera series' notebooks once Pages is enabled there. The `*.github.io/<repo>/` form of those URLs answers with a 301 to the katra one, which is the correct address to link. Never create content, a section or an alias at a path named like one of those repositories — both sites would claim the same URLs, and only one of them can be served there.

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
  - **Subdirectories publish too, and that is how something private goes public.** A file dropped in `content/es/posts/<slug>/bibliografia/` is served from `https://katra.ballardini.com.ar/posts/<slug>/bibliografia/…`. There is no `_`-prefix or front-matter escape hatch for a non-`.md` resource: if it is in the bundle, it ships. Reference material that should stay off the public site belongs outside `content/` — the working copies live in `C:/Users/cesar/cesar/trabajo/utn/objetos/objetos-bibliografia/`, and full books kept next to the blog go in the repo-root `books/` folder, which is gitignored and outside Hugo's content tree. Run the `find` above before staging, and read what it lists.
- **Spanish posts go in:** `content/es/posts/`
- **English posts go in:** `content/en/posts/`
- **Frontmatter:** YAML (`---`) for all 2025+ posts. The full house rules — frontmatter shape, tag rules (no periods, Hugo Windows limitation), footnote style (named, never numeric), internal link rules (no `/es/` prefix in Spanish URLs), image bundles vs flat files, voice — live in [`content/just-ideas-for-future-posts/near-future-posts.md`](content/just-ideas-for-future-posts/near-future-posts.md) under "Convenciones de la casa". Read that section before writing or editing a post — it reflects the actual practice in the published posts, not what `AGENTS.md` says (they conflict; the published posts win).
- **Hero banner:** every post has `featured_image: hero-filename.jpg` in frontmatter. The image lives in the post's bundle folder. Use landscape-oriented images (2.5:1 ratio or wider); portrait photos must be cropped with Pillow before use (`uv run --with Pillow python`). `featured_image_class = "cover bg-center"` is set globally in `hugo.toml`.
- **Per-page CSS:** add `page_css: ['tables.css']` to frontmatter for posts with markdown tables. The CSS lives at `assets/ananke/css/tables.css` and is loaded via the `layouts/partials/head-additions.html` partial. `code.css` (smaller code type, `font-size: 0.82rem`, selector covering both `.highlight` and `.code-block` so that language-less fences — console output, which never goes through Chroma — match) is **shared by every post that lists it**. Touching it re-renders all of them, so their `public/` shows up modified in a diff without anyone having edited those posts.
- **Mermaid diagrams:** add `mermaid: true` to frontmatter to live-render ```` ```mermaid ```` fences (loaded via `layouts/partials/hooks/body-end.html`, see Architecture below). Without the flag, a mermaid fence just renders as unstyled plain code.
  - **Validate a diagram before pasting it.** `curl -s -o out.svg -w "%{http_code}" "https://mermaid.ink/svg/$(base64 -w0 < d.mmd)"` — a `400`/`404` is a syntax error you would otherwise discover on the published page. To test a diagram that depends on the HTML-label config, send the JSON form instead: base64 of `{"code": "...", "mermaid": {"theme":"neutral","securityLevel":"antiscript","flowchart":{"htmlLabels":true}}}`, which is what `mermaid_html_labels: true` produces on the site. Swap `/svg/` for `/img/…?type=png&width=2400` to eyeball the result, or to generate a hero from the diagram itself. `make mermaid` does this for every diagram of a post, with the right config. From Python, send an explicit `User-Agent`: mermaid.ink answers `403` to urllib's default one for every diagram, valid or not, which reads as eleven syntax errors that are not there. A `503` is mermaid.ink being down, not the diagram; `tools/check_mermaid.py` retries those and reports them as unvalidated.
  - **There is no actor shape in flowcharts.** Verified against mermaid 11.16: `@{ shape: actor }`, `person` and `user` are all rejected. The stick figure only exists as the `actor` keyword in `sequenceDiagram`. For a UML use case diagram, ship an `actor.svg` in the bundle and reference it from an HTML label — `bebedor["<img src='actor.svg' width='40' height='62' alt=''/><br/>Bebedor de café"]` — plus `classDef actor fill:none,stroke:none` to drop the box that would otherwise make the actor look like another use case. Requires `mermaid_html_labels: true`. Set `width`/`height` explicitly so mermaid sizes the node without waiting for the image to load. There is a working `actor.svg` (421 bytes, five strokes) in `content/es/posts/2026-10-18-cafetera-mark-iv-enunciado-del-problema/`; copy it into any bundle that needs one, since each page bundle publishes its own resources.
  - **Truncated node labels?** Add `mermaid_html_labels: true` as well. Mermaid's default `securityLevel: 'strict'` forces `htmlLabels: false`, so the library measures label width itself instead of letting the browser do it; with accents and symbols (`↔`, `á`, `í`) it under-measures and clips long labels mid-word. The flag switches that page to `securityLevel: 'antiscript'` + `htmlLabels: true` — the browser measures the real text, and `<br/>` works for manual line breaks. It is **opt-in per post on purpose**: enabling it site-wide would silently re-flow the diagrams in already-published posts. `'antiscript'` allows HTML in labels but drops `<script>`; prefer it over `'loose'`.
- **Math formulas:** write LaTeX directly — `\( ... \)` inline, `\[ ... \]` or `$$ ... $$` for display. **Rendered at build time** by `layouts/_markup/render-passthrough.html` via `transform.ToMath` (KaTeX compiled into the Hugo binary), which emits native MathML. No JavaScript, no CDN, no stylesheet, and screen-reader friendly. No frontmatter flag is needed. Requires `[markup.goldmark.extensions.passthrough]` in `hugo.toml` — without it Goldmark mangles `_`, `\` and `{}` before the math renderer sees them (`k_B` turns into italics).
- **Electronic schematics (KiCad):** the `/370-145` panel post keeps its schematics in `kicad/` inside the bundle — Python generators that emit `.kicad_sch` and a symbol library, plus the PDF and SVG exported with `kicad-cli`. They are *generated by script rather than drawn by hand* so a layout fix is a re-run, not an afternoon of dragging symbols. If you touch one, re-export and re-verify: `kicad-cli sch erc` for wiring, **plus `kicad-cli sch export netlist` whenever the change could move a component**. The two catch different things — ERC finds off-grid endpoints and wires that stop a fraction of a millimetre short of a pin, while only the netlist proves which pins actually share a net. A schematic can be drawn so cramped that it reads as a series chain and still be wired correctly, and it can look impeccable and be wired wrong; neither check alone tells you which.
- **Read-aloud audio player:** a client-side text-to-speech player (browser `speechSynthesis`, no cloud TTS, no API key) is injected on every content page **by default** — it is opt-**out**, not opt-in. To suppress it on a specific post, set `audio_player: false` in frontmatter. UI language and voice follow the page language (`.Language.Lang`). Injected via `layouts/partials/hooks/body-end.html` with CSS in `assets/ananke/css/audio-player.css` (see Architecture below).
- **Image attribution:** every public domain or CC-licensed image requires a named footnote with URL, author, and license. Example: `[^img_foo]: Imagen de [Title](URL) — CC BY-SA 4.0 — Author.` If the image was cropped or otherwise adapted for the blog, note that at the end of the footnote (e.g. "Recortada a 2.5:1 para hero landscape.").
- **Academic paper citations:** when a paper's canonical URL (IEEE Xplore, Springer, ACM DL) is paywalled or blocks automated fetch (IEEE returns HTTP 418), the footnote should link to a **stable DOI** (`https://doi.org/10.XXXX/...`) as the canonical reference plus a **free full-text mirror** when one exists (university course pages, archive.org, the author's Wikipedia page). Always include journal name / volume / issue / year in the footnote regardless of linkability.
- **Book citations and archive.org lending:** an archive.org item is only *borrowable* if its `collection` includes **`inlibrary`**. An item that is only `printdisabled` is restricted to people with a print disability and **cannot be borrowed** — linking it as if it were a loan copy misleads the reader. Check with `curl -s https://archive.org/metadata/<id>` and read `collection`. To find whether a borrowable copy exists at all, Open Library beats archive.org's own search: `https://openlibrary.org/search.json?q=<title>+<author>&fields=title,ia,ebook_access`, where `ebook_access` is one of `borrowable` / `printdisabled` / `no_ebook`. When no borrowable copy exists, cite the canonical edition without a link and add a genuinely free alternative (the author's own paper, a university mirror, Wayback) — never link an unauthorized full-text upload, which is easy to spot by identifiers like `…www.ebooks-world.ir`.
- **Verify which book a chapter is actually in.** Two books by the same author from adjacent years are easy to confuse, and a wrong attribution survives many editing passes because it *reads* right. Check the target book's table of contents before citing a chapter number. This bit once: «Heuristics and Coffee» is chapter 11 of *UML for Java Programmers* (2003), not of *Agile Software Development, PPP* (2002) — whose chapter 11 is the DIP.
- **Extracting text from a PDF:** `pypdf` is fine for a table of contents but mangles body text into letter-spaced garbage (`T h e S i n g l e`); `pdfplumber` reads it correctly. Text set in small caps extracts as run-together capitals (`ACLASSSHOULDHAVEONLYONEREASONTOCHANGE`), so search for quotes with whitespace-insensitive matching before concluding a phrase is absent.
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
- **Archetype:** `archetypes/default.md` writes the house YAML frontmatter (`title`, `description`, `tags`, `featured_image`), with the title taken from the bundle name without its date, in sentence case. No `date` and no `draft`: the date comes from the directory name. Until 2026-10-22 it was the TOML archetype from the first commit, which broke `hugo new` (`can't evaluate field params`)
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

## Work in progress — serie de la cafetera Mark IV (cuatro posts)

**Estado al 2026-10-22: los cuatro posts corregidos y verificados juntos; el repo de código verde, con notebooks, y creado vacío en GitHub.** El orden de lo que falta está en `2026-10-21-plan-coffee-maker.md`, en la raíz del repo de código. Pendientes antes de publicar: (1) `git init` + commit + push del repo, que hace César, sin lo cual los enlaces a GitHub dan 404; (2) habilitar Pages en ese repo, ver los cuatro workflows en verde y agregar a los posts los enlaces a los notebooks; (3) regenerar `public/`, que está desactualizado respecto de los cuatro posts. ~~Decidir qué se hace con los PDF de libros~~: resuelto el 2026-10-21 (ver abajo).
**Re-verificado el 2026-10-22:** el repo de código sigue verde (53 tests, `make diff` sin diferencias, `make metrics` como abajo), los once diagramas mermaid dan 200 en mermaid.ink, y el build de lo commiteado más los cuatro bundles no tiene enlaces internos rotos ni notas al pie huérfanas. Los bundles están fechados **2026-10-18 / 19 / 20 / 21**, para que no queden debajo del post del 2026-09-17; el URL no cambia porque sale del slug. Publicarlos después del 21 no exige re-fecharlos (con fechas pasadas salen igual); re-fecharlos sólo si se quiere que aparezcan como recientes, nunca a una fecha futura.
Borrar esta sección cuando la serie esté publicada.

### Las piezas

| Pieza | Dónde |
| --- | --- |
| El plan de la serie | `plan-de-la-serie.md` en la raíz de `coffee-maker-designs` (salió del bundle del post 1 el 2026-10-21), junto a `2026-10-21-plan-coffee-maker.md`, que ordena lo que falta para publicar — outline por post, inventario de hechos verificados, tabla de errata, decisiones abiertas |
| Post 1 (escrito) | `2026-10-18-cafetera-mark-iv-enunciado-del-problema/` — consigna, enunciado, API, casos de uso |
| Post 2 (escrito) | `2026-10-19-cafetera-mark-iv-particion-por-hardware/` — construye el diseño malo y lo diagnostica |
| Post 3 (escrito) | `2026-10-20-cafetera-mark-iv-particion-por-roles/` — construye el diseño por roles y encuentra el agujero con los escenarios |
| Post 4 (escrito) | `2026-10-21-cafetera-mark-iv-martin-y-weirich/` — compara los tres y cierra con OOverkill |
| Bibliografía fuente | `C:/Users/cesar/cesar/trabajo/utn/objetos/objetos-bibliografia/coffe-maker/` — **fuera de `content/`, a propósito** |
| El código | `C:/Users/cesar/cesar/github/CesarBallardini/coffee-maker-designs` — **fuera del repo del blog** |

Los slugs evitan «diseño» porque la ñ afea el URL; se eligió «partición», que además es el término de Martin (*partitioning*).

### Las tres decisiones de diseño (el eje de la serie)

El enunciado deja **tres** preguntas sin contestar, y en las tres se adoptó **la lectura de Martin**, que es la publicada y la que su código de prueba exige:

| Pregunta | Decisión |
| --- | --- |
| ¿Cómo queda la válvula al terminar el ciclo? | **Cerrada** — abierta es transitorio, el estado de aliviar presión durante la pausa |
| ¿Cuándo se apaga la luz? | Cuando vuelve la jarra **vacía** — mientras quede café, el ciclo no cerró |
| ¿La placa calienta café que la máquina no preparó? | **No** — «sólo se enciende si hay café» es condición necesaria, no suficiente |

Están documentadas en el README del repo y fijadas como escenarios en `cafetera.feature`, cuyo encabezado lleva además una **tabla de trazabilidad** que mapea cada frase del enunciado a los escenarios que la verifican — con tres tests en `tests/unit/test_trazabilidad.py` que impiden que la tabla se despegue del archivo. **La tercera no se había visto** hasta que el barrido exhaustivo la encontró; la traza de nueve pasos no la tocaba. Desde el 2026-10-21 el post 1 plantea las tres preguntas, y el post 4 cuenta como historia de entretelones que la tercera apareció después.

**Weirich contesta las tres distinto que Martin**, y el post 4 lo dice: apaga la luz al levantar la jarra (`jim-coffee.txt`, línea 83); deja la válvula **abierta** al terminar (figura 10, estado Done; figura 16, `OnOffComposite`; figura 5, `Off() { itsDevice.Open(); }`); y su placa calienta **cualquier** jarra con café (figuras 12 y 13). La luz está en su texto; la válvula y la placa, sólo en sus diagramas, y el post lo aclara así en vez de presentarlo como una decisión escrita.

### Lo verificado corriendo el código (Python 3.14.4 + uv, sólo biblioteca estándar)

- **Los tres diseños dan exactamente el mismo comportamiento observable**: idéntico en los nueve pasos de la traza y en las **2800 secuencias** de hasta cuatro eventos (7+49+343+2401). Tres particiones sin un criterio en común y ni una diferencia. Ése es el argumento central de la serie.
- **`martin/` es un port fiel de los Listings 11-14 a 11-21 y su comportamiento no se toca.** Cuando hubo que unificar el comportamiento, se adaptaron los otros dos a su lectura, no al revés. La única excepción, el 2026-10-21, fue agregar el `Pollable` del Listing 11-20 en `m4.py`: una declaración, sin cambio observable, que lo hace más fiel.
- Adaptarse costó distinto en cada uno, y eso es contenido del post 4: en Martin, **cero**; en el de hardware, tres condiciones más dentro de `poll()`; en el de roles, un rol nuevo `PausableDevice` (distingue `off` = pausa de `rest` = reposo) y un `is_active` inyectado en el `PlateController`.
- **Las pruebas encontraron dos veces lo que la traza no**: (a) el diseño por roles arrancaba el ciclo sin jarra en la placa, y lo encontró un escenario; (b) la regla de la placa se leía distinto en cada diseño, y la encontró el barrido de las 2800 secuencias. Las dos son el mejor argumento de la serie a favor de escribir pruebas además de mirar la traza.
- **El post 3 cuenta la historia como pasó, y muestra la salida de hoy.** Al escribirlo falló **un** escenario; la suite creció después hasta catorce, y con `is_ready=tank.has_water` en el cableado hoy fallan **dos** (`2 failed, 40 passed` en los de aceptación). El post dice las dos cosas; no reescribir el pasado para que coincida con la salida.
- **`pytest-bdd` 8.1.0 parsea Gherkin en castellano** (`# language: es`). Catorce escenarios × tres diseños = 42 tests BDD. Con `scenarios()` autogenerando los tests, un fixture parametrizado normal falla con *«The requested fixture has no parameter defined for test»* porque la función generada no declara el fixture en su firma: la solución es `autouse=True`. **Ojo con el `autouse`**: un test que no necesita el fixture y vive en ese directorio se corre tres veces idénticas — por eso los tests de tabla van en `tests/unit/`.
- **`gherkin-official` 29.0.0 emite un `DeprecationWarning`** (llama a `re.split()` con `maxsplit` posicional). No hay a dónde actualizar: pytest-bdd 8.1.0 —la última— lo fija en `<30.0.0` y 29.0.0 es la única 29.x. Está filtrado en `pyproject.toml` de forma acotada, con `filterwarnings = ["error", ...]` para que cualquier warning propio siga siendo un error.

### El repositorio de código

Se decidió **`coffee-maker-designs`**, rama `main`: un solo repo con el scaffold de [`localenv-python`](https://github.com/CesarBallardini/localenv-python), un núcleo compartido (`api.py`, `simulator.py`, `scenarios.py`) y un subpaquete por diseño (`by_hardware/`, `by_roles/`, `martin/`), más un test que prohíbe los imports cruzados y otro que exige que los tres sigan coincidiendo. **Está armado en `C:/Users/cesar/cesar/github/CesarBallardini/coffee-maker-designs` y corre verde** — 53 tests (42 BDD + 11 unitarios), ruff, pyright, pyrefly, bandit, pip-audit y OSV-Scanner sin hallazgos, y `make diff` muestra las tres trazas sin diferencias. **El repo de GitHub existe desde el 2026-10-22, vacío** (`gh repo create … --public`, sin `--source` ni `--push`). **Falta el `git init`, el primer commit y el push, que los hace César**; los comandos están en la Fase 2 del plan. Hasta que esté pusheado, los enlaces al repo desde los posts dan 404, que es lo esperado. El detalle y la justificación están en la §8 de `plan-de-la-serie.md`.

El 2026-10-22 se subieron en el `uv.lock` `virtualenv`, `certifi`, `urllib3` y `mako`: `pip-audit` encontraba 17 vulnerabilidades y OSV una, que venían de antes y habrían puesto en rojo `security.yml` en el primer push.

**Notebooks en el navegador.** Cinco notebooks en `notebooks/` (`01-el-problema` a `05-la-suite`), uno por post más la suite, que se publican con JupyterLite y Pyodide (CPython 3.14) desde el workflow `lite.yml` a `https://katra.ballardini.com.ar/coffee-maker-designs/`. Corren todo, en desktop, en Pyodide sobre Node (`make test-pyodide`) y en Chromium y Firefox (`make test-e2e`), y reproducen cada bloque de consola que citan los posts, incluida la salida `2 failed, 40 passed` del post 3. Los enlaces van como `notebooks/index.html?path=NN-nombre.ipynb`; JupyterLite no salta a un ancla, así que el post nombra la sección. La tabla de secciones de cada notebook y lo que costó armarlos están en la Fase 3 del plan. Dos trampas: el kernel del navegador ya trae `pygments` 2.20.0 y micropip se niega a pisarlo; y `node`/`npm` no andan en Git Bash en esta máquina (las funciones de nvm se llaman a sí mismas), así que se pasan con la ruta completa: `make test-pyodide NODE=/c/Users/cesar/.nvm/versions/node/v24.16.0/bin/node.exe NPM=…/npm`.

**Cada parte del código tiene su propio README** —los tres diseños, el núcleo compartido, `tests/` y `tools/`— explicando cómo está armada, dónde caen las tres decisiones del enunciado y qué le costó cada una. Las métricas que citan esos README están verificadas contra `make metrics`.

Dos cosas que se decidieron al armarlo y conviene no revertir sin pensarlo: (1) **no se corre `ruff format`** y hay tres reglas de lint apagadas, porque el formateo automático explota los métodos de una línea que los posts citan textualmente — está comentado en `ruff.toml`; (2) las métricas que citan los posts salen de `make metrics` (`tools/metrics.py`), no de contar a mano: **12 clases / 132 líneas** el de hardware, **25 / 261** el de roles, **8 / 158** el de Martin (7 / 155 hasta que se agregó `Pollable`), contando sólo los módulos propios de cada diseño. Si se toca un diseño, se re-corre y se actualizan los posts.

### Reglas que no hay que perder de vista

- **Los enlaces a un repo propio van con `blob/main/`, nunca `blob/master/`.** Con `master` dan 404. Ya mordió una vez en el repo de DCI.
- Nada de código ni de salidas escritas a mano: todo sale de correr el repo. Si una salida cambia, se re-corre y se pega, sin traducir.
- El post y el repo tienen que contar la misma historia. Cada vez que se toque uno, revisar el otro.
- **En una pasada de edición, una referencia que quedó sin destino se arregla cambiando la referencia, no reponiendo el texto borrado.** Si César borró algo, borrado está.
- **Tres de los cuatro `.md` de `objetos-bibliografia/coffe-maker/` son texto generado por un modelo y tienen errores de hecho**: API inventada, constantes de la API invertidas, la válvula descrita al revés, y código Smalltalk atribuido a Martin y a Weirich que ninguno de los dos escribió. Sirven para estructura; como fuente, no. La tabla completa está en la §7 del plan.
- La página OOAD de Weirich de 1999 **no sobrevive** en la web ni en el Internet Archive. La única copia es el PDF del bundle del post 1, que es una impresión de la página hecha desde Netscape sobre Solaris.
- **«Heuristics and Coffee» es el capítulo 11 de *UML for Java Programmers* (Prentice Hall, 2003), NO de *Agile Software Development, PPP*.** Los cuatro posts lo citaron mal durante días. La confusión es fácil porque los dos son de Martin, de la misma época, y **el capítulo 11 de PPP es justamente el del DIP**. Verificado contra el índice de los dos PDF. Los cinco principios SOLID están en el capítulo 6 del mismo libro de la cafetera, páginas 64 a 82.
- **En archive.org, lo que habilita el préstamo es la colección `inlibrary`, no `printdisabled`.** Un ítem sólo `printdisabled` está restringido a personas con discapacidad para la lectura impresa y **no se puede pedir prestado**. Comprobarlo con `curl -s https://archive.org/metadata/<id>` y mirar `collection`. De los tres libros de esta serie, dos son prestables (`umlforjavaprogra00mart`, `designingobjecto00mart`) y PPP **no tiene copia prestable** — para ése se cita el paper libre «Design Principles and Design Patterns» (2000) en el sitio de Martin vía Wayback, con el aviso de que enuncia cuatro de los cinco principios y no incluye el SRP.
- **Para buscar si un libro se presta, Open Library es mejor que la búsqueda de archive.org**: `https://openlibrary.org/search.json?q=...&fields=title,ia,ebook_access`. El campo `ebook_access` distingue `borrowable` de `printdisabled` de `no_ebook`.
- **Los PDF de `bibliografia/` dentro del bundle del post 1 se publican al sitio.** Dos eran libros de Pearson completos que ningún post enlaza; el 2026-10-21 se movieron a `books/` en la raíz del repo, que está en `.gitignore` y fuera de `content/`. En el bundle queda sólo el de Weirich, que los posts enlazan y que tiene argumento de preservación, porque esa página no existe en ningún otro lado.
- **Extraer texto de un PDF con letras espaciadas:** `pypdf` devuelve `T h e S i n g l e`; `pdfplumber` sale legible. Los enunciados de los principios están en versalitas, así que se extraen como mayúsculas pegadas (`ACLASSSHOULDHAVEONLYONEREASONTOCHANGE`) y hay que buscarlos con matching insensible a espacios.

## Work in progress — «Un lenguaje que sólo lee el LLM»

**Estado al 2026-10-22: escrito y verificado; falta lo que sólo puede poner César.** Borrar esta sección cuando el post esté publicado.

- **Bundle:** `content/es/posts/2026-10-21-un-lenguaje-que-solo-lee-el-llm/`, untracked. Sale de `tmp/blog-post.md` del repo `C:/Users/cesar/cesar/github/CesarBallardini/tokens-per-function-point`. **El slug no se cambia**: el README de ese repo ya enlaza a `/posts/un-lenguaje-que-solo-lee-el-llm/`.
- **Verificado el 2026-10-21** contra las fuentes externas y contra el repo; se corrigieron doce afirmaciones (las codificaciones de tiktoken, la variante byte-level de BPE, la cuenta de nombres —son seis, no cinco—, la nota de Algol 68 con DOI `10.1007/BF00265077` y el PDF de softwarepreservation, entre otras). El plan del repo de tokens repite el «cinco» en sus líneas 190 y 304: avisado, no corregido, porque no es este repo.
- **Dos 🕳️ HUECO para César**: la imagen del hero con su nota `[^img_hero]`, y el párrafo de cierre. No se llenan.
- **Dos decisiones abiertas**: el tag `mal` (se sugirió `Make a Lisp`, que dice qué es); y la fecha, que coincide con el post 4 de la cafetera (2026-10-21) — si salen juntos, el orden entre los dos lo decide Hugo.
