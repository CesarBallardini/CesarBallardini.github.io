# Posts del futuro cercano — plan editorial de katra

> **Última revisión:** 2026-04-14 (C-01 publicado — primer post de Serie C; W0 baja a 1 pendiente; nuevo I-14 cosechado de la edición de C-01)
> **Owner:** César — archivo editorial privado, no se renderiza al sitio.
> **Audiencia objetivo del blog:** lectores nerd / orientados a CS — algoritmos, arquitectura de software y de computadoras, prácticas de programación, lenguajes (mainstream y oscuros). La Serie K (vida y trabajo) es la sección honesta para temas laterales no-CS.
> **Tono buscado en cada post:** divertido, entretenido, **un solo concepto** por entrada.

Este documento es el **catálogo maestro** del plan editorial de [katra](https://katra.ballardini.com.ar/). Vive en `content/just-ideas-for-future-posts/`, que está fuera de los directorios de contenido de Hugo y por lo tanto **nunca se renderiza al sitio**. Es scratch privado.

A partir del 2026-04-09 el contenido detallado de cada entrada vive en su **propio archivo** bajo una de las 11 carpetas de categoría (ver [estructura del directorio](#estructura-del-directorio)). Este documento mantiene:

- las **convenciones de la casa** (cómo se escriben los posts, frontmatter, tags, estilo),
- la **bibliografía transversal** (fuentes reutilizables entre entradas),
- el **índice de las 11 series** con punteros a cada archivo individual,
- los **waves de publicación** y el **mantenimiento del plan**.

Cada entrada-archivo incluye concepto, hook, outline, bibliografía verificada, imágenes con licencia, tags, comando `hugo new` y estado actual.

---

## Tabla de contenidos

- [Cómo usar este plan](#cómo-usar-este-plan)
- [Estructura del directorio](#estructura-del-directorio)
- [Convenciones de la casa](#convenciones-de-la-casa)
- [Bibliografía transversal](#bibliografía-transversal)
- [Las 11 series](#las-11-series)
  - [Serie A1 — Lenguajes clásicos y su historia](#serie-a1--lenguajes-clásicos-y-su-historia)
  - [Serie A2 — La familia Lisp y el cálculo lambda](#serie-a2--la-familia-lisp-y-el-cálculo-lambda)
  - [Serie B — Recursión y CS funcional](#serie-b--recursión-y-cs-funcional)
  - [Serie C — Filosofía de la ingeniería de software](#serie-c--filosofía-de-la-ingeniería-de-software)
  - [Serie D — Pioneros y artefactos del cómputo](#serie-d--pioneros-y-artefactos-del-cómputo)
  - [Serie E — Memoir CS / mi camino con el código](#serie-e--memoir-cs--mi-camino-con-el-código)
  - [Serie G — Arquitectura como CS (IaC + deployment)](#serie-g--arquitectura-como-cs-iac--deployment)
  - [Serie H — Arqueología de sistemas legacy](#serie-h--arqueología-de-sistemas-legacy)
  - [Serie I — Memoria del cómputo local](#serie-i--memoria-del-cómputo-local)
  - [Serie J — Curiosidad nerd lateral](#serie-j--curiosidad-nerd-lateral)
  - [Serie K — Vida y trabajo (lateral)](#serie-k--vida-y-trabajo-lateral)
- [Apéndice histórico — `draft-rest.md` cosechado y eliminado](#apéndice-histórico--draft-restmd-cosechado-y-eliminado)
- [Waves de publicación](#waves-de-publicación)
- [Mantenimiento del plan](#mantenimiento-del-plan)

---

## Cómo usar este plan

1. **Para elegir qué escribir hoy.** Mirá la sección [Waves de publicación](#waves-de-publicación). Empezá por la wave más temprana que todavía tenga posts pendientes. Dentro de una wave, dejate llevar por la inspiración.
2. **Para sentarte a escribir un post.** Buscá su ID (e.g. `A1-03`) en el índice de la serie correspondiente, hacé click en el archivo `draft-*.md` y abrilo. Cada archivo tiene todo lo necesario: concepto, hook, outline, bibliografía con URLs verificadas, imágenes con licencia, tags y comando `hugo new` listo para copiar.
3. **Para entender cómo se conectan los posts.** Cada archivo lista `Cross-links: depende de [[X-NN]], lleva a [[Y-NN]]`. Los IDs se resuelven a links reales en el momento de publicar (find/replace simple).
4. **Cuando termines un post.** Cambiá `Estado actual:` a `publicado` dentro del archivo draft, y agregá la fecha y el slug final. Marcá los cross-links salientes con su URL real.
5. **Cuando aparezca una idea nueva.** Creala primero como `draft-*.md` en la carpeta de categoría correspondiente (ver siguiente sección), y dentro de la semana agregala a la tabla de índice de la serie en este plan.
6. **Si un post ya no te entusiasma como antes.** Marcalo como "en hibernación" o "concepto refinado" en su `Estado actual:`, pero dejá la entrada en el plan. No todas las 180 ideas se van a escribir, y eso está bien — el plan es un archivo de ideas, no una lista de tareas. La sección [Mantenimiento](#mantenimiento-del-plan) lo explica.

> **Regla de oro:** el orden es sugerencia, no ley. Si un post te tira hoy, escribilo hoy.

---

## Estructura del directorio

Desde el 2026-04-09, cada entrada-post vive en su propio archivo markdown bajo una de las 10 carpetas de categoría, con un nombre del tipo `draft-{slug-descriptivo}.md`. La carpeta refleja la serie temática; el nombre del archivo refleja el tema concreto del post, no el ID.

```
content/just-ideas-for-future-posts/
├── near-future-posts.md      ← este archivo (catálogo maestro, guías, waves, índices)
├── lenguajes/                ← Serie A1 — Lenguajes clásicos        (21 drafts)
├── lisp/                     ← Serie A2 — Familia Lisp              ( 9 drafts)
├── funcional/                ← Serie B  — Recursión y CS funcional  ( 8 drafts)
├── filosofia/                ← Serie C  — Filosofía de la SE        (16 drafts)
├── pioneros/                 ← Serie D  — Pioneros y artefactos     ( 6 drafts)
├── memoir/                   ← Serie E  — Memoir CS                 (29 drafts)
├── devops/                   ← Serie G  — IaC + deployment          (33 drafts)
├── legacy/                   ← Serie H  — Arqueología legacy        (13 drafts)
├── local/                    ← Serie I  — Memoria del cómputo local (13 drafts)
├── nerd/                     ← Serie J  — Curiosidad nerd lateral   (10 drafts)
└── vida/                     ← Serie K  — Vida y trabajo (lateral)  (23 drafts)
```

**Total**: 181 drafts repartidos en 11 categorías. El catálogo maestro vive en `near-future-posts.md` (este archivo).

**Convención de nombres de archivo draft:** `draft-{slug}.md` donde `{slug}` es el mismo slug que aparece dentro del archivo en el campo `**Slug propuesto:**` y que después se usará en el `hugo new content/es/posts/YYYY-MM-DD-{slug}/index.md`. El prefijo `draft-` marca que el archivo es un borrador de idea (no publicado), aunque sólo el contenido de `content/es/posts/` y `content/en/posts/` se renderiza al sitio.

**Nota sobre las referencias históricas a `dev/`, `sysadmin/`, `misc/`:** estas tres carpetas existían antes del refactor del 2026-04-09 como archivo de seeds cortos originales (notas de 3-10 líneas que luego se expandieron en los archivos draft completos de cada categoría). El 2026-04-09 se eliminaron del repo porque todo su contenido ya estaba absorbido en los archivos `draft-*.md` de las 10 carpetas de categoría. Los archivos draft actuales pueden mencionar esas rutas en el campo `**Archivo seed:**` como nota histórica — no son links vivos.

---

## Convenciones de la casa

Estas reglas reflejan **la práctica real** observada en los posts publicados (`2025-01-27-growing-a-language.md`, `2025-02-23-programma-101.md`, `2025-03-10-soplar-humo-de-tabaco.md`), no necesariamente lo que dice `AGENTS.md`. Cuando hay conflicto, ganan los posts.

### Frontmatter (YAML, no TOML)

`AGENTS.md` dice que los posts usan TOML (`+++`), pero **todos** los posts de 2025 usan YAML (`---`). Los nuevos siguen YAML.

```yaml
---
title: 'Título del post entre comillas simples'
description: ''
tags: ['tag1', 'tag2', 'tag3']
translationKey: 'clave-única-si-hay-versión-bilingüe'
---
```

- **No** incluir `layout`, `date`, ni `draft` — los maneja la config de Hugo o el archetype.
- `description` puede quedar vacío en posts cortos; sólo llenar si suma.
- `translationKey` sólo cuando exista (o esté planeado) un par ES/EN.

### Tags

- **Sin puntos en los valores de tags.** Es una limitación de Hugo en Windows: los puntos rompen la generación de slugs (regla de `AGENTS.md`). Por eso `'Guy L Steele Jr'` y no `'Guy L. Steele Jr.'`.
- Vocabulario libre, pero reusar lo que ya existe en posts publicados cuando aplique: `blog`, `Hugo`, `Jekyll`, `LISP`, `OOPSLA`, `arquitectura`, `arqueologia`, `problem solving`, `medicina`, `computadora personal`, `olivetti`, `programma 101`, `humo`, `rant`, `Debian`, `vagrant`, `virtualbox`, `Ruby on Rails`, `Github Pages`, `migracion`, `instalacion`.
- Para los posts nuevos del plan, los tags propuestos en cada entrada respetan esta regla.

### Footnotes (referencias)

El estilo canonizado por `growing-a-language.md` y `programma-101.md`:

- **Footnotes con nombre** — nunca numéricas: `[^kay]`, `[^okasaki]`, `[^video]`.
- Definiciones agrupadas al **final** del post.
- Formato: `[^name]: [Texto del enlace](URL) — comentario opcional.`
- Opcionalmente, una lista de viñetas "Referencias citadas en la presentación" arriba de las definiciones de footnotes (ver `growing-a-language.md`) cuando lo amerita.

### Links internos

- Las URLs en español **no llevan prefijo `/es/`** (es el idioma por defecto). Link interno correcto: `[texto](/posts/2025-02-23-programma-101/)`. Incorrecto: `/es/posts/...`.
- Las URLs en inglés sí usan `/en/`.
- Los cross-links entre posts del plan se escriben como `[[A1-03]]` durante el drafting y se resuelven a `[texto humano](/posts/YYYY-MM-DD-slug-real/)` en el momento de publicar.

### Imágenes (convención nueva)

El blog actualmente no tiene imágenes en ningún post. Esta sección fija la convención para los posts del plan que sí las van a usar.

- **Posts con imágenes**: usan **page bundle** — la carpeta `content/es/posts/YYYY-MM-DD-slug/` con `index.md` adentro y los archivos de imagen como hermanos. Comando: `hugo new content/es/posts/YYYY-MM-DD-slug/index.md`.
- **Posts sin imágenes**: archivo plano. Comando: `hugo new content/es/posts/YYYY-MM-DD-slug.md`.
- Markdown: `![alt text](archivo-en-el-bundle.jpg)` — la ruta es relativa al bundle.
- Cada imagen pública lleva una footnote de atribución: `[^img1]: Imagen de [Wikimedia Commons](URL) — Dominio público / CC-BY-SA 4.0 — autor: Fulano.`
- **Decisión a respetar**: una vez que un post se crea como bundle, no se muda a archivo plano (cambia la URL). Decidir layout antes de correr `hugo new`.

### Estilo y voz

- Conversacional, primera persona ("voy a contarte", "me llamó la atención"), español rioplatense.
- Code-switching libre con términos técnicos en inglés (`workflow`, `framework`, `deploy`, `pull request`).
- **Un concepto por post**, con el hook en los primeros dos párrafos.
- Largo según el tema, sin relleno. Posts de 600-1000 palabras (story) son tan válidos como deep-dives de 2500+.

### IDs estables para cross-links

- Cada post tiene un ID único `{serie}-{NN}` (e.g. `A1-03`, `tr-07`, `H-04`).
- Cada fuente transversal tiene un ID `tr-NN`.
- Durante el drafting, `[[ID]]` referencia otros posts/fuentes sin necesitar el slug final.
- En `hugo new`, se puede dejar en frontmatter:
  ```yaml
  plan_id: 'A1-03'
  plan_depends: ['A1-01', 'tr-07']
  plan_leads_to: ['A2-05']
  ```
  Estos campos no rompen Hugo (los ignora) y se borran antes de publicar si molestan.

---

## Bibliografía transversal

Estas son las fuentes que aparecen en múltiples posts. En vez de repetir la cita, las entradas se refieren a ellas por ID `tr-NN`. Cada fuente lleva un flag de **bitrot risk**: `estable` (archive.org, Wikipedia, ACM DL, dominios institucionales) o `frágil` (blogs personales, YouTube, páginas de facultad — verificar en Wayback Machine antes de publicar).

| ID | Fuente | Usado por | Bitrot |
| --- | --- | --- | --- |
| **tr-01** | Alan Kay, *The Computer Revolution Hasn't Happened Yet* — keynote en OOPSLA 1997. [YouTube](https://www.youtube.com/watch?v=oKg1hTOQXoY). | A1, C, D | frágil (YouTube; backup en archive.org) |
| **tr-02** | Guy L Steele Jr, *Growing a Language* — keynote en OOPSLA 1998. [Vídeo](https://www.youtube.com/watch?v=lw6TaiXzHAE), [PDF del texto](https://homepages.inf.ed.ac.uk/wadler/documents/steele-oopsla98.pdf). Ya tiene su post: `2025-01-27-growing-a-language`. | A1, A2, C | mixto |
| **tr-03** | Harold Abelson & Gerald Jay Sussman, *Structure and Interpretation of Computer Programs* (SICP), MIT Press, 2.ª ed. 1996. [Versión libre](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html), [edición online HTML](https://web.mit.edu/6.001/6.037/sicp.pdf), [vídeos del curso 6.001 en MIT OCW](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/). | A2, B, E | estable |
| **tr-04** | Chris Okasaki, *Purely Functional Data Structures*, tesis CMU CMU-CS-96-177, 1996. [PDF en CMU](https://www.cs.cmu.edu/~rwh/students/okasaki.pdf). Versión libro 1998, Cambridge University Press. | B | estable |
| **tr-05** | Patrick Henry Winston & Berthold Klaus Paul Horn, *LISP*, Addison-Wesley, 3.ª ed. 1989. [Edición de 1981 en archive.org](https://archive.org/details/lisp-1981-addison-wesley). | A2, E | estable |
| **tr-06** | Richard P Gabriel, *Lisp: Good News, Bad News, How to Win Big* + *Worse Is Better*. [Dreamsongs](https://www.dreamsongs.com/WIB.html), [Worse Is Better](https://www.dreamsongs.com/WorseIsBetter.html). | A2, C | frágil (sitio personal; backup en Wayback) |
| **tr-07** | Rich Hickey, *Simple Made Easy* — Strange Loop 2011. [Charla en InfoQ](https://www.infoq.com/presentations/Simple-Made-Easy/), [transcripción](https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md). | C | estable |
| **tr-08** | Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly, 2023. Newsletter [Software Design: Tidy First?](https://tidyfirst.substack.com/). | C | estable |
| **tr-09** | Joe Armstrong et al., *Erlang the Movie* (1990, Ericsson). [Vídeo en YouTube](https://www.youtube.com/watch?v=BXmOlCy0oBM). Más: Joe Armstrong, *Programming Erlang* (Pragmatic Bookshelf, 2.ª ed. 2013). | A1 | mixto |
| **tr-10** | *Byte Magazine* archive — colección completa en archive.org. [Folkscanomy Computer collection](https://archive.org/details/folkscanomy_computer), [vintageapple.org Byte PDFs](https://vintageapple.org/byte/). Búsquedas por número/año dan los issues citados. | A1, A2, E, I | estable |
| **tr-11** | Computer History Museum collections. [computerhistory.org](https://www.computerhistory.org/), oral histories en [chm.org/oral-histories](https://www.computerhistory.org/collections/oralhistories/). | D, A1, I | estable |
| **tr-12** | Douglas Engelbart, *The Mother of All Demos*, SRI / Fall Joint Computer Conference, 9 de diciembre 1968. [Vídeo en archive.org (90 min)](https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect), [Doug Engelbart Institute](https://dougengelbart.org/content/view/209/). | D | estable |
| **tr-13** | Ivan Sutherland, *Sketchpad: A Man-Machine Graphical Communication System*, MIT PhD thesis, 1963. [PDF en University of Cambridge](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf), [vídeo del demo](https://www.youtube.com/watch?v=mOZqRJzE8xg). | D | estable |
| **tr-14** | Philip Wadler, *Theorems for Free!* (1989) y otros clásicos en [Lambda the Ultimate — classic papers](http://lambda-the-ultimate.org/classic/papers.html). [Wadler papers](https://homepages.inf.ed.ac.uk/wadler/topics/parametricity.html). | A2, B | estable |
| **tr-15** | Eric S Raymond, *The Cathedral and the Bazaar*. [Original en catb.org](http://www.catb.org/esr/writings/cathedral-bazaar/cathedral-bazaar/). [Traducción al castellano por Sin Dominio](https://biblioweb.sindominio.net/telematica/catedral.html). También su *Jargon File* en [catb.org/jargon](http://www.catb.org/jargon/). | C, E | estable |
| **tr-16** | Ward Cunningham, *c2 wiki* (Portland Pattern Repository). [wiki.c2.com](https://wiki.c2.com/). | A1, C | estable |
| **tr-17** | Peter Van Roy & Seif Haridi, *Concepts, Techniques, and Models of Computer Programming* (CTM), MIT Press 2004. [Página del libro](https://webperso.info.ucl.ac.be/~pvr/book.html). Usa Mozart/Oz. | A1, A2, B | estable |
| **tr-18** | C A R Hoare, *Communicating Sequential Processes* (CSP), 1978. [PDF de la versión libro (1985)](http://www.usingcsp.com/cspbook.pdf). | A1, B | estable |
| **tr-19** | Edsger W Dijkstra, *EWD archive*. [E. W. Dijkstra Archive en UT Austin](https://www.cs.utexas.edu/~EWD/). | C, A1 | estable |
| **tr-20** | Donald E Knuth, *The Art of Computer Programming* (TAOCP), Addison-Wesley. [Página de Knuth](https://www-cs-faculty.stanford.edu/~knuth/taocp.html). | B | estable |
| **tr-21** | Alan Kay, *Is "Software Engineering" an Oxymoron?* — Apéndice B de *Croquet: The User Manual*, draft 0.1, octubre 2002. [PDF en Wayback Machine](http://web.archive.org/web/20030407181600/www.opencroquet.org/downloads/Croquet0.1.pdf). | C | frágil (sólo archive) |
| **tr-22** | Reddit y stackexchange threads sobre OOP de Kay (consolidados). [Reddit r/programming "Alan Kay on his original thoughts"](https://www.reddit.com/r/programming/comments/bpb5v6/alan_kay_on_his_original_thoughts_when_he_came_up/), [Software Engineering SE "What did Alan Kay really mean"](https://softwareengineering.stackexchange.com/questions/46592/so-what-did-alan-kay-really-mean-by-the-term-object-oriented). | C | mixto |
| **tr-23** | *Masterminds of Programming* (Federico Biancuzzi & Shane Warden, O'Reilly 2009) — entrevistas con creadores de lenguajes. [archive.org](https://archive.org/details/MastermindsOfProgramming). | A1, A2, E | estable |

> Cada vez que se cite uno de estos en un post, basta con `[^kay]: ver [[tr-01]] en el plan editorial` y, en publicación, expandir a la cita completa.

---

## Las 11 series

Cada entrada del plan vive en un archivo `draft-*.md` propio bajo la carpeta de categoría correspondiente. Hacé click en el nombre del archivo para abrirlo — cada uno contiene concepto, hook, outline, bibliografía, imágenes, tags y estado actual.

> **Refactor del 2026-04-09:** las entradas A1-12..A1-21, A2-08..A2-09, C-06..C-16, D-05..D-06, E-17..E-29, I-12..I-13, J-09 y toda la Serie K (K-01..K-23) son cosecha de `draft-rest.md`. Llevan `**Madurez:** seed-from-cosecha` — son ideas con concepto + bibliografía mínima pero sin outline desarrollado todavía.

---

## Serie A1 — Lenguajes clásicos y su historia

**Concepto de la serie:** una caminata guiada por lenguajes que merecen ser conocidos por algo más que su nombre. Mainstream que envejecieron raro, paradigmas marginales que nunca despegaron, herramientas que parecían cosa del pasado y sin embargo siguen apareciendo. Cada post: un lenguaje, una idea central, una historia.

- **A1-01** — [Alan Kay y la revolución del cómputo que todavía no llegó](lenguajes/draft-alan-kay-revolucion-no-llego.md)
- **A1-02** — [Erlang the Movie (y por qué deberías ver una película de un lenguaje)](lenguajes/draft-erlang-the-movie.md)
- **A1-03** — [Forth: el lenguaje hecho para una sola persona](lenguajes/draft-forth-lenguaje-para-una-persona.md)
- **A1-04** — [Modula-2: Pascal después de Pascal](lenguajes/draft-modula-2-pascal-despues-de-pascal.md)
- **A1-05** — [Clipper, xBase y los servidores web que no debían existir](lenguajes/draft-clipper-xbase-servidor-web.md)
- **A1-06** — [PostScript como servidor web](lenguajes/draft-postscript-como-servidor-web.md)
- **A1-07** — [Spectrum y MicroHobby: la cultura del 8-bit hispanohablante](lenguajes/draft-spectrum-microhobby-cultura-8-bit.md)
- **A1-08** — [Resucitando KL1 (Kernel Language 1) y el proyecto japonés de 5ta generación con `kl1c`](lenguajes/draft-kl1-icot-quinta-generacion.md)
- **A1-09** — [GnuCOBOL-lab: aprender RM/COBOL-85 desde un libro español de 1990 dentro de una VM Vagrant](lenguajes/draft-gnucobol-lab-rm-cobol-85.md)
- **A1-10** — ["Soy mi propio abuelo": modelar una humorada folklórica en Prolog](lenguajes/draft-soy-mi-propio-abuelo-prolog.md)
- **A1-11** — [Pharo Smalltalk: el sistema vivo donde el código y el mundo son la misma cosa](lenguajes/draft-pharo-smalltalk-sistema-vivo.md)
- **A1-12** — [El documento de Alan Kay sobre qué es realmente OOP (alojado en FU Berlin)](lenguajes/draft-kay-oop-doc-fu-berlin.md) 🌱 *cosecha*
- **A1-13** — [Masterminds of Programming: roster completo de las 17 entrevistas](lenguajes/draft-masterminds-roster-completo.md) 🌱 *cosecha*
- **A1-14** — [APL: el lenguaje de los símbolos griegos (Falkoff)](lenguajes/draft-apl-falkoff-iverson.md) 🌱 *cosecha*
- **A1-15** — [BASIC: el lenguaje educativo de Dartmouth (Kurtz)](lenguajes/draft-basic-kurtz-dartmouth.md) 🌱 *cosecha*
- **A1-16** — [SQL: el lenguaje que ganó sin querer (Chamberlin)](lenguajes/draft-sql-chamberlin-historia.md) 🌱 *cosecha*
- **A1-17** — [Perl: el lenguaje del lingüista (Larry Wall)](lenguajes/draft-perl-larry-wall-linguista.md) 🌱 *cosecha*
- **A1-18** — [Haskell: el lenguaje que no quería existir (Peyton Jones, Hudak, Wadler, Hughes)](lenguajes/draft-haskell-spj-hudak-wadler-hughes.md) 🌱 *cosecha*
- **A1-19** — [Lua: el lenguaje brasileño que terminó embebido en cada motor de videojuegos](lenguajes/draft-lua-roberto-ierusalimschy-brasil.md) 🌱 *cosecha*
- **A1-20** — [Java: el pragmatismo de James Gosling](lenguajes/draft-java-gosling-pragmatismo.md) 🌱 *cosecha*
- **A1-21** — [Anders Hejlsberg: el hombre detrás de Turbo Pascal, Delphi, C# y TypeScript](lenguajes/draft-hejlsberg-delphi-csharp-typescript.md) 🌱 *cosecha*

---

## Serie A2 — La familia Lisp y el cálculo lambda

**Concepto de la serie:** Lisp como hilo conductor desde Church y Steele hasta Spectrum y BASIC. La pregunta detrás de cada post: ¿qué hace que esta familia siga siendo el patrón oro contra el que medimos los demás lenguajes 60 años después? Pensada para leer en orden, pero cada post se sostiene solo.

- **A2-01** — [SICP en castellano (y los videos del 80)](lisp/draft-sicp-en-castellano-videos-del-80.md)
- **A2-02** — [Los papers de Scheme: lambda the ultimate](lisp/draft-papers-de-scheme-lambda-the-ultimate.md)
- **A2-03** — [Jim Weirich y el Y combinator (en vivo)](lisp/draft-jim-weirich-y-combinator-en-vivo.md)
- **A2-04** — [Sistemas expertos en BASIC (lo que salió en Byte)](lisp/draft-sistemas-expertos-en-basic-byte-1981.md)
- **A2-05** — [El LISP de Carlos Adaglio (Lisp en el Spectrum)](lisp/draft-lisp-de-carlos-adaglio-spectrum-c64.md)
- **A2-06** — [Mi propia traducción de SICP al castellano: el proyecto que casi termina](lisp/draft-mi-traduccion-sicp-castellano.md)
- **A2-07** — [DrRacket + Jupyter + iRacket: Scheme didáctico en el navegador con una VM](lisp/draft-scheme-en-el-navegador-iracket.md)
- **A2-08** — [Simply Scheme: el libro con el que Berkeley enseñó a 500 programadores principiantes](lisp/draft-simply-scheme-500-programadores.md) 🌱 *cosecha*
- **A2-09** — [Lambda the Ultimate Imperative: el paper de Steele que cambió cómo pensar imperativo](lisp/draft-lambda-the-ultimate-imperative.md) 🌱 *cosecha*

---

## Serie B — Recursión y CS funcional

**Concepto de la serie:** los temas que aparecen cuando uno se anima a pensar funcionalmente — listas infinitas, tail calls, trampolines, Okasaki, pruebas de teoremas a partir de tipos. Posts más "didácticos" de la grilla: tienen código y suelen ser un poco más largos.

- **B-01** — [Listas infinitas: cómo evaluar lo que no termina](funcional/draft-listas-infinitas-evaluacion-perezosa.md)
- **B-02** — [Estructuras de datos puramente funcionales (Okasaki)](funcional/draft-okasaki-estructuras-funcionales.md)
- **B-03** — [Convertir un programa recursivo a iterativo](funcional/draft-convertir-recursivo-a-iterativo.md)
- **B-04** — [Convertir recursión a recursión de cola](funcional/draft-convertir-recursion-a-tail-recursion.md)
- **B-05** — [Trampolines: saltar para no apilar](funcional/draft-trampolines-saltar-para-no-apilar.md)
- **B-06** — [Teoría de la programación imperativa](funcional/draft-teoria-programacion-imperativa.md)
- **B-07** — [htmx-course con Gleam: HTMX desde el BEAM (Erlang OTP) en un curso de 28 capítulos](funcional/draft-htmx-course-gleam-beam.md)
- **B-08** — [Warren's Abstract Machine y la arqueología de implementaciones de Prolog (micro-PROLOG, small-prolog, wambook)](funcional/draft-warren-abstract-machine-arqueologia-prolog.md)

---

## Serie C — Filosofía de la ingeniería de software

**Concepto de la serie:** los textos y charlas que cambian la manera de pensar sobre lo que hacemos. Kay, Hickey, Beck, Dijkstra. No "filosofía" en el sentido vacío sino: ¿qué es realmente esto que llamamos "ingeniería"?

- **C-01** — [¿"Ingeniería de software" es un oxímoron?](/posts/2026-04-14-ingenieria-software-oximoron/) ✅ **publicado 2026-04-14**
- **C-02** — [Simple no es lo mismo que fácil (Rich Hickey)](filosofia/draft-simple-no-es-facil-hickey.md)
- **C-03** — [Tidy First: limpiar antes de cambiar (Kent Beck)](filosofia/draft-tidy-first-kent-beck.md)
- **C-04** — [TDD bass drop: cuando el test rojo te da dopamina](filosofia/draft-tdd-bass-drop-dopamina.md)
- **C-05** — [La revolución del cómputo todavía no llegó (ángulo filosófico)](filosofia/draft-revolucion-computo-todavia-no-llego.md)
- **C-06** — [Curtis Poe sobre qué quiso decir Alan Kay con OOP](filosofia/draft-curtis-poe-on-kay-oop.md) 🌱 *cosecha*
- **C-07** — [La explicación simple de qué quiso decir Kay con OOP (consolidación de Reddit/SE)](filosofia/draft-kay-oop-explicacion-simple.md) 🌱 *cosecha*
- **C-08** — [Por qué MDA y Executable UML nunca cumplieron sus promesas](filosofia/draft-mda-uml-promesas-incumplidas.md) 🌱 *cosecha*
- **C-09** — [DCI: Data, Context, Interaction — la idea olvidada de Trygve Reenskaug](filosofia/draft-dci-data-context-interaction-reenskaug.md) 🌱 *cosecha*
- **C-10** — [James Gosling sobre la herencia: el inventor de Java prefiere no usarla](filosofia/draft-gosling-vs-herencia.md) 🌱 *cosecha*
- **C-11** — [Goodhart's Law en software: cuando la métrica se vuelve el objetivo](filosofia/draft-goodhart-law-en-software.md) 🌱 *cosecha (Beck/Noda email)*
- **C-12** — [El Bosque y el Desierto: la metáfora de Beck para hablar de calidad de vida programando](filosofia/draft-forest-and-desert-beck.md) 🌱 *cosecha (Beck/Noda)*
- **C-13** — [Anti-productivity: medí lo que te frena, no lo que producís (John Cutler)](filosofia/draft-anti-productivity-cutler-medir-lo-que-frena.md) 🌱 *cosecha (Beck/Noda)*
- **C-14** — [XP: valores, principios, prácticas — el framework tripartito de Kent Beck](filosofia/draft-xp-values-principles-practices.md) 🌱 *cosecha (Beck/Noda)*
- **C-15** — ["Vender solo el dashboard es malpractice" — Beck sobre métricas sin acompañamiento](filosofia/draft-vender-dashboards-malpractice.md) 🌱 *cosecha (Beck/Noda)*
- **C-16** — [Developer Experience vs Effectiveness: por qué Beck rechaza la palabra "experiencia"](filosofia/draft-developer-experience-vs-effectiveness.md) 🌱 *cosecha (Beck/Noda)*

---

## Serie D — Pioneros y artefactos del cómputo

**Concepto de la serie:** las personas y las máquinas que hicieron por primera vez algo que hoy damos por sentado. Engelbart, Sutherland, Turing, Olivetti. Posts cortos, biográficos, con muchísimas imágenes públicas disponibles.

- **D-01** — [Douglas Engelbart y la Madre de Todas las Demos](pioneros/draft-engelbart-mother-of-all-demos.md)
- **D-02** — [Sketchpad: Ivan Sutherland inventa todo en 1963](pioneros/draft-sketchpad-sutherland-1963.md)
- **D-03** — [La máquina de Turing: una pizarra infinita y un cabezal terco](pioneros/draft-maquina-de-turing-explicacion.md)
- **D-04** — [Olivetti Programma 101: la computadora de escritorio que llegó antes de tiempo](pioneros/draft-programma-101-revisitada.md) ✅ **publicado 2025-02-23**
- **D-05** — [Turing Awards: un recorrido por los ganadores que cambiaron el mundo](pioneros/draft-turing-awards-historia-recorrido.md) 🌱 *cosecha*
- **D-06** — [El paper de Sutherland sobre constraints (MIT 1963): el ancestro del álgebra de restricciones](pioneros/draft-sutherland-constraint-paper-1963.md) 🌱 *cosecha*

---

## Serie E — Memoir CS / mi camino con el código

**Concepto de la serie:** mi historia con el código, contada a través de las herramientas y libros que me marcaron. Posts personales pero con un takeaway técnico. Aquí también caen los del workflow de desarrollo actual (Python, Vue, Ollama).

- **E-01** — [Cómo llegué al software libre (Bingo, diskettes y un GCC para DOS)](memoir/draft-como-llegue-al-software-libre.md)
- **E-02** — [fixperm: cómo escribí un Lisp en C porque tenía que arreglar permisos en SCO Unix](memoir/draft-fixperm-lisp-en-c-sco.md)
- **E-03** — [mapkey para Linux: cuando el teclado no era el que vos querías](memoir/draft-mapkey-para-linux.md)
- **E-04** — [Mi entorno de Python en 2026: ruff, pre-commit, pyproject](memoir/draft-entorno-python-2026.md)
- **E-05** — [Mi entorno de Vue.js 3 en 2026](memoir/draft-entorno-vue-2026.md)
- **E-06** — [Uso Ollama para criticar mi código antes de commitearlo](memoir/draft-ollama-revisa-mi-codigo.md)
- **E-07** — [dbaid: la herramienta que escribí porque no encontré ninguna](memoir/draft-dbaid-herramienta-personal.md)
- **E-08** — [Los libros que me marcaron (lista anotada y honesta)](memoir/draft-libros-que-me-marcaron.md)
- **E-09** — [Masterminds of Programming: las entrevistas que cambian todo](memoir/draft-masterminds-of-programming.md)
- **E-10** — [Cómo pienso la infraestructura corporativa: la pila que tengo en la cabeza](memoir/draft-como-pienso-la-infraestructura.md)
- **E-11** — [De Jekyll a Hugo: cómo migré mi blog y por qué (con 2 anécdotas de Vagrant + Windows 11)](memoir/draft-jekyll-a-hugo-migracion-blog.md)
- **E-12** — [El patrón Vagrant + Ansible: mi método para aprender tecnologías nuevas](memoir/draft-mi-metodo-para-aprender-vagrant-ansible.md)
- **E-13** — [El día que bajé GPT-2 de OpenAI antes de que fuera famoso](memoir/draft-gpt-2-local-antes-de-ollama.md)
- **E-14** — [Estudios de clean architecture: rentomatic + clean-architecture (el libro que nunca escribí)](memoir/draft-clean-architecture-estudios.md)
- **E-15** — [free-for-dev: mi pila personal de hobby projects contra el costo cero](memoir/draft-free-for-dev-pila-personal.md)
- **E-16** — [Tres forks de IA de antes de los LLMs: simpleai, ai-app-prog, HealthyCoderApp](memoir/draft-tres-forks-ia-pre-llm.md) ⚠️ *incompletos*
- **E-17** — [De papel a calculadora a PC a ChatGPT: cómo me afectaron los cambios tecnológicos](memoir/draft-papel-calculadora-pc-chatgpt-evolucion-personal.md) 🌱 *cosecha*
- **E-18** — [The Little Lisper: el libro con el que aprendí a pensar funcionalmente](memoir/draft-little-lisper-mi-primer-lisp.md) 🌱 *cosecha*
- **E-19** — [The Little Schemer y su familia: la pedagogía socrática de Friedman/Felleisen](memoir/draft-little-schemer-y-su-familia.md) 🌱 *cosecha*
- **E-20** — [Little Patterns? El libro chiquito sobre observer y compose que estoy buscando](memoir/draft-little-patterns-observer-compose.md) 🌱 *cosecha — pendiente verificar referencia*
- **E-21** — [The Reasoned Schemer: Scheme + lógica + miniKanren](memoir/draft-little-reasoner-scheme-para-logica.md) 🌱 *cosecha*
- **E-22** — [Aprender Haskell con Erik Meijer (el de las camisetas coloridas)](memoir/draft-haskell-erik-meijer-camisetas-coloridas.md) 🌱 *cosecha*
- **E-23** — [The Art of Unix Programming — el libro de Eric S Raymond](memoir/draft-esr-art-of-unix-programming.md) 🌱 *cosecha*
- **E-24** — [How to Become a Hacker — Eric S Raymond](memoir/draft-esr-hacker-howto.md) 🌱 *cosecha*
- **E-25** — [The Jargon File / Hacker Dictionary: el diccionario que es una novela](memoir/draft-jargon-file-hacker-dictionary.md) 🌱 *cosecha*
- **E-26** — [Clean Code de Bob Martin: lo que aprendí y dónde no estoy de acuerdo](memoir/draft-clean-code-bob-martin.md) 🌱 *cosecha*
- **E-27** — [El libro de los Pragmatic Programmers sobre programar con interfaces](memoir/draft-pragmatic-programmer-interfaces.md) 🌱 *cosecha — pendiente verificar referencia*
- **E-28** — [Concatenative programming: el libro/artículo de Byte que me hizo entender Forth](memoir/draft-concatenative-programming-byte.md) 🌱 *cosecha*
- **E-29** — [Strange Loop: la conferencia que se tomó en serio "una sola idea"](memoir/draft-strange-loop-conferencia-unica.md) 🌱 *cosecha*

---

## Serie G — Arquitectura como CS (IaC + deployment)

**Concepto de la serie:** infraestructura entendida como un problema de arquitectura de software, no de "tareas de sysadmin". Roles, profiles, componentes, inventarios, golden images, contenedores. Si tenés que pelearte con Ansible o con Docker, esta serie es para vos.

- **G-01** — [Components, roles y profiles en Ansible (el patrón de Puppet bien aplicado)](devops/draft-ansible-roles-profiles-components.md) 🌟 *near-complete*
- **G-02** — [Infraestructura determinística: golden images, CVS y un Makefile](devops/draft-infraestructura-deterministica.md)
- **G-03** — [Backups con rdiff-backup + rsync (y por qué los backups no sirven, lo que sirve es el restore)](devops/draft-backups-rdiff-rsync.md)
- **G-04** — [Trac, wiki y tickets: registro de incidencias en un ministerio público](devops/draft-trac-wiki-tickets-ministerio.md)
- **G-05** — [sibrom: despliegues diarios antes de que existiera "continuous deployment"](devops/draft-sibrom-despliegues-diarios.md)
- **G-06** — [PostgreSQL en un contenedor Docker (sin perder los datos)](devops/draft-postgresql-en-docker.md)
- **G-07** — [Docker en Windows: lo que nadie te cuenta cuando elegís WSL2 vs Hyper-V](devops/draft-docker-en-windows-wsl2-hyperv.md)
- **G-08** — [`ansible-devops-workstation`: 5 años de evolución de mi estación de trabajo como código](devops/draft-ansible-devops-workstation-5-anios.md) 🌟 *flagship*
- **G-09** — [`localenv-*`: un patrón para entornos de desarrollo locales (Python, WordPress, Symfony6)](devops/draft-localenv-pattern-python-wp-symfony.md)
- **G-10** — [La trampa del `delegate_to: localhost` vs `connection: local` en Ansible cuando el controlador vive en un virtualenv](devops/draft-delegate-to-vs-connection-local-virtualenv.md)
- **G-11** — [Recreando la arquitectura DNS/IPAM de Maynooth con PowerDNS, nsedit y phpIPAM](devops/draft-dns-ipam-maynooth-powerdns.md)
- **G-12** — [Proxmox VE como laboratorio: del nodo único al cluster hiperconvergido con Ceph](devops/draft-proxmox-ve-lab-ceph.md)
- **G-13** — [LXD homelab: cluster con FAN overlay y SDN](devops/draft-lxd-homelab-fan-sdn.md)
- **G-14** — [Tu propio registry Docker en casa: Harbor bajo Vagrant](devops/draft-harbor-registry-casero.md)
- **G-15** — [OCFS2 cluster filesystem casero: sobre NBD y sobre disco compartido VirtualBox](devops/draft-ocfs2-cluster-filesystem-casero.md)
- **G-16** — [Backups MySQL con LVM snapshot y ventana de bloqueo de microsegundos](devops/draft-mysql-backup-lvm-snapshot-microsegundos.md)
- **G-17** — [Recetas Partman/Preseed con Packer: testear instalaciones automatizadas Debian](devops/draft-partman-preseed-packer.md)
- **G-18** — [GUI apps en Docker: pgModeler + el problema del display + x11docker](devops/draft-gui-apps-en-docker-x11docker.md)
- **G-19** — [Apps GUI legadas en VMs: Enterprise Architect Lite y Visual Paradigm sobre Wine + Vagrant](devops/draft-apps-gui-legadas-vms-wine.md)
- **G-20** — [eCryptfs en 2026: por qué ya no, y cómo migrar tu HOME cifrado a LUKS](devops/draft-ecryptfs-deprecado-migrar-luks.md)
- **G-21** — [DMOJ online judge para la materia Paradigmas de Programación: Docker Compose + CSV import + sandbox](devops/draft-dmoj-online-judge-paradigmas.md)
- **G-22** — [k8s-homelab: el cluster Kubernetes que armé y por qué sigo usando LXD para casi todo](devops/draft-k8s-homelab-vs-lxd-proxmox.md)
- **G-23** — [OpenGrok bajo Tomcat con Ansible: indexar código fuente de proyectos legacy](devops/draft-opengrok-ansible-legacy-code-search.md)
- **G-24** — [Cuttlefish: mi propio servidor SMTP transaccional autohospedado](devops/draft-cuttlefish-smtp-autohosted.md)
- **G-25** — [Mailserver completo en Docker: el servidor de mail full-featured self-hosted](devops/draft-mailserver-docker-full-featured.md)
- **G-26** — [LetsEncrypt con Cloudflare DNS vía Ansible (el role mínimo que tenía que existir)](devops/draft-letsencrypt-cloudflare-ansible-role.md)
- **G-27** — [Digital Rebar Provision: PXE y orquestación de boot para provisioning masivo](devops/draft-digital-rebar-provision-pxe-boot.md) ⚠️ *incompleto*
- **G-28** — [Bareos: el backup server enterprise en mi homelab (fork + role)](devops/draft-bareos-backup-server-homelab.md)
- **G-29** — [OCS Inventory Agent: inventario automático de hosts con Ansible](devops/draft-ocs-inventory-agent-ansible.md)
- **G-30** — [Packer + OpenVPN: construir AMIs reproducibles para bastión VPN](devops/draft-packer-openvpn-ami-reproducible.md) ⚠️ *viejo 2016*
- **G-31** — [Windows dev box setup scripts: automatizar la laptop corporativa con PowerShell + Chocolatey](devops/draft-windows-dev-box-powershell-chocolatey.md)
- **G-32** — [infrastructure-development: el repo meta sobre cómo se bootea una práctica de infra](devops/draft-bootstrap-infrastructure-development-practice.md) ⚠️ *incompleto*
- **G-33** — [La bandada de roles Ansible que forkeé para estudiar](devops/draft-forks-ansible-roles-bandada.md)

---

## Serie H — Arqueología de sistemas legacy

**Concepto de la serie:** correr software viejo en máquinas nuevas, y por qué eso es (a veces) la mejor opción. SCO Unix, FoxBase, RM COBOL, Linux ABI. Los posts cruzan fuertemente entre sí — leídos en orden cuentan una historia continua de migración legacy. La parábola del diámetro de los cohetes vive acá porque es la mejor metáfora del legacy que existe.

- **H-01** — [Linux ABI: cómo correr FoxPro para SCO Unix en un kernel actual](legacy/draft-linux-abi-foxpro-sco-unix.md)
- **H-02** — [RM/COBOL bajo SCO Unix migrado a GNU/Linux: el binario que sobrevivió 25 años](legacy/draft-rm-cobol-sco-gnu-linux.md)
- **H-03** — [FoxBase para SCO migrado a GNU/Linux](legacy/draft-foxbase-sco-gnu-linux.md)
- **H-04** — [Migrar COBOL de mainframe a GnuCOBOL en GNU/Linux](legacy/draft-cobol-mainframe-a-gnucobol.md)
- **H-05** — [Un DVD que botea Win98 con compiladores (para la clase de Paradigmas)](legacy/draft-dvd-boot-paradigmas-win98.md)
- **H-06** — [La parábola del diámetro de los cohetes (la mejor metáfora del legacy que existe)](legacy/draft-parabola-diametro-cohetes.md)
- **H-07** — [Migración FoxBase → PostgreSQL en un ministerio (la otra mitad de G-04)](legacy/draft-foxbase-postgresql-ministerio.md)
- **H-08** — [ThinStation: clientes delgados con soporte sólo del lado del servidor](legacy/draft-thinstation-clientes-delgados.md)
- **H-09** — [UDPcast: instalar 40 escritorios al mismo tiempo con multicast](legacy/draft-udpcast-instalacion-masiva.md)
- **H-10** — [IBM MVS 3.8j sobre Hercules: corriendo un mainframe IBM en mi notebook](legacy/draft-mvs-3-8-hercules-mainframe-laptop.md)
- **H-11** — [Linux Ubuntu para s390x sobre Hercules: instalando arquitectura IBM Z emulada en mi laptop](legacy/draft-linux-s390x-hercules.md)
- **H-12** — [Hercules `prtspool`: imprimir desde MVS 3.8 a PDF](legacy/draft-hercules-prtspool-imprimir-mvs-pdf.md)
- **H-13** — [Apache + PHP 5.6 + Symfony 1.4 y 3.4: correr una app PHP legacy en Docker](legacy/draft-apache-php56-symfony-legacy-docker.md)

---

## Serie I — Memoria del cómputo local

**Concepto de la serie:** la memoria del cómputo en estas latitudes — el LUGLi, las revistas de quiosco, el Spectrum y su reverberación argentina, las distros caseras para reparticiones públicas. Lo que quedaba afuera de la historia oficial.

- **I-01** — [Historia del LUGLi (Linux Users Group Litoral)](local/draft-historia-del-lugli.md)
- **I-02** — [Revistas de quiosco: digitalizar lo que el archivo oficial nunca tuvo](local/draft-revistas-quiosco-digitalizacion.md)
- **I-03** — [Spectrum y MicroHobby: lo que aprendí de un teclado de goma](local/draft-spectrum-microhobby-aprendizaje.md)
- **I-04** — [MerLinux: la distro de Debian que armé para el Ministerio de Cultura de Santa Fe (con la trilogía bash → Puppet → Ansible)](local/draft-merlinux-mincultura-santa-fe.md)
- **I-05** — [Salir de la STG: memoir de un técnico que renunció a un cargo público provincial](local/draft-salir-de-la-stg-santa-fe.md)
- **I-06** — [IPC en C: el recorrido honesto por los cinco mecanismos clásicos de Unix](local/draft-ipc-en-c-cinco-mecanismos-unix.md)
- **I-07** — [SuperLib y Clipper: rescate de las herramientas de la PyME argentina de los 90](local/draft-superlib-clipper-pyme-argentina.md)
- **I-08** — [Linberry: rescate del intento argentino de un BlackBerry Desktop Manager para Linux](local/draft-linberry-blackberry-desktop-linux.md)
- **I-09** — [ZinjaI: el IDE C++ argentino que muchos usamos en la facultad](local/draft-zinjai-ide-cpp-argentino.md)
- **I-10** — [Huayra GNU/Linux: la distro argentina del Conectar Igualdad](local/draft-huayra-gnu-linux-conectar-igualdad.md)
- **I-11** — [Dist-prog-book: el libro sobre programación distribuida que forkeé para leer (y la colección de Lambda the Ultimate)](local/draft-dist-prog-book-lambda-ultimate.md)
- **I-12** — [archive.org como acervo de CS: folkscanomy_computer y Byte Magazine](local/draft-archive-org-folkscanomy-acervo-cs.md) 🌱 *cosecha*
- **I-13** — [Papers académicos viejos en ACM Digital Library y Springer: cómo cazarlos](local/draft-jlc-acm-papers-historia.md) 🌱 *cosecha*
- **I-14** — [Contra la colegiación obligatoria de los informáticos (caso Santa Fe 2007)](local/draft-contra-la-colegiacion-de-informaticos.md) 🆕 *cosechado de [[C-01]] el 2026-04-14*

---

## Serie J — Curiosidad nerd lateral

**Concepto de la serie:** la sección honesta. No es CS, no se pretende. Son cosas que un nerd disfruta y que merecen estar en algún lado.

> _Nota de serie:_ los posts de la serie J llevan al inicio una etiqueta visible **"⚠️ Curiosidad nerd lateral — esto no es ciencia de la computación"** para que el lector pueda saltearlos si no le interesa el contenido.

- **J-01** — [Construir un láser de nitrógeno (en homenaje a *The Amateur Scientist*)](nerd/draft-laser-nitrogeno-amateur-scientist.md)
- **J-02** — [Escaneo 3D de un motor de cohete del Smithsonian: cómo se digitalizó un objeto histórico para reconstruirlo](nerd/draft-escaneo-3d-motor-cohete-smithsonian.md)
- **J-03** — [MindForth y MentiFex: Arthur T. Murray, el pionero solitario que escribió una IA en Forth durante 30 años](nerd/draft-mindforth-mentifex-arthur-murray.md)
- **J-04** — [Tipografiar Biblias históricas con LaTeX: Reina-Valera 1865 y Geneva 1564](nerd/draft-biblias-historicas-latex.md)
- **J-05** — [Pharo MOOC con audio inglés y subtítulos en español: la solución Rube Goldberg con nginx en Docker](nerd/draft-pharo-mooc-rube-goldberg-subtitulos.md)
- **J-06** — [Automagica: generar un libro listo para imprenta con LaTeX (y tres Biblias antiguas)](nerd/draft-automagica-libros-latex-imprenta.md)
- **J-07** — [Relevamiento de departamentos: el script Python que imprimía una etiqueta por unidad](nerd/draft-relevamiento-deptos-etiquetas.md) ⚠️ *viejo 2016*
- **J-08** — [IBM MVS, Hercules y los jobs JCL que escribí para sentir cómo era 1970](nerd/draft-mvs-hercules-jcl-sentir-1970.md)
- **J-09** — ["Look both ways before crossing a one-way street" — la paradoja de Doug Linder](nerd/draft-doug-linder-cruzar-calle-una-via.md) 🌱 *cosecha*

---

## Serie K — Vida y trabajo (lateral)

**Concepto de la serie:** la sección honesta del plan editorial donde viven temas que un nerd quiere escribir aunque no sean estrictamente CS — vida personal, carrera, familia, finanzas, salud, etapas de la vida. La mayoría de estas entradas vienen de la cosecha de `draft-rest.md` (Bucket 2, "brainstorm de temas de vida"). Cada post lleva el aviso **"⚠️ Lateral — fuera del eje principal del blog"** para que el lector pueda saltearlo sin sentirse defraudado.

> _Nota de serie:_ esta es la 11ª serie del plan, agregada el 2026-04-09 cuando se cosechó el bucket 2 de `draft-rest.md`. Mientras la serie J es "curiosidad nerd lateral pero igual sobre temas técnicos/científicos" (láseres, cohetes, MentiFex), la serie K es "vida lateral en general" — sin pretensión de cubrir CS. La distinción importa para el lector: J puede gustarle a un nerd; K puede gustarle a alguien que conoce a César pero no quiere leer sobre código.

- **K-01** — [Sector público vs privado en IT: las diferencias que importan](vida/draft-sector-publico-vs-privado-it.md) 🌱
- **K-02** — [Cambios tecnológicos: por qué aceptarlos y cómo no quedarse atrás](vida/draft-cambios-tecnologicos-aceptar-evolucion.md) 🌱
- **K-03** — [Tener un título universitario en IT: pros, contras y la verdad](vida/draft-titulo-en-it-pros-y-contras.md) 🌱
- **K-04** — [Estudiar de grande: sentimientos, dificultades y por qué vale la pena](vida/draft-estudiar-de-grande-experiencia.md) 🌱
- **K-05** — [Armas: creación, manipulación, cuidados, normas, preparación](vida/draft-armas-creacion-manipulacion-cuidados.md) 🌱
- **K-06** — [Desarrollo personal: cómo desarrollar, mejorar, aprender, dónde aprender](vida/draft-desarrollo-personal-aprender-mejorar.md) 🌱
- **K-07** — [Matrimonio: economía, tiempos, discusiones, perdón](vida/draft-matrimonio-economia-tiempos-discusiones-perdon.md) 🌱
- **K-08** — [Paternidad: cómo se vivencian los hijos, qué podría haber mejorado, consejos a padres primerizos](vida/draft-paternidad-vivencias-mejoras-consejos.md) 🌱
- **K-09** — [Jubilación: qué depara el futuro, cómo enfrentarse a eso, cómo eludirlo](vida/draft-jubilacion-futuro-enfrentar-eludir.md) 🌱
- **K-10** — [Religión: iniciación, respeto a los demás, importancia en la vida propia](vida/draft-religion-iniciacion-respeto-importancia.md) 🌱
- **K-11** — [Mascotas (perros): cuidados, educación, querer](vida/draft-mascotas-canes-cuidados-educacion-querer.md) 🌱
- **K-12** — [Finanzas personales: cómo administrarse, cómo proyectar, qué priorizar](vida/draft-finanzas-administrar-proyectar-priorizar.md) 🌱
- **K-13** — [IA: trabajos actuales, qué estudiar, qué va a cambiar, cómo afrontarlo](vida/draft-ia-trabajos-actuales-futuro-afrontar.md) 🌱
- **K-14** — [Tecnologías en auge: ¿qué estudiar?, ¿qué no?, ¿COBOL? ¿.NET? ¿PHP?](vida/draft-tecnologias-en-auge-cobol-net-php.md) 🌱
- **K-15** — [Relaciones laborales: jefes, colegas, relaciones entre pares](vida/draft-relaciones-laborales-jefes-colegas-pares.md) 🌱
- **K-16** — [Idioma (inglés): importancia, desempeño, consejos de aprendizaje](vida/draft-idioma-importancia-aprendizaje-consejos.md) 🌱
- **K-17** — [Generaciones: las diferencias entre la mía, la tuya y la de Julián](vida/draft-generaciones-diferencias-julian-virtudes-defectos.md) 🌱
- **K-18** — [Toma de decisiones: qué evaluar, cómo contemplar el panorama, puntos críticos](vida/draft-toma-de-decisiones-evaluar-panorama-criticos.md) 🌱
- **K-19** — [Estilo de vida: alimentación, deporte, estudio, viajes, ociosidad](vida/draft-estilo-de-vida-alimentacion-deporte-estudio-viajes.md) 🌱
- **K-20** — [Etapa militar: qué pasó, cómo pasó, qué viviste, cómo se disfruta/sufre](vida/draft-etapa-militar-vivencias.md) 🌱
- **K-21** — [Rabbit Gus (placeholder, significado a clarificar)](vida/draft-rabbit-gus-significado-pendiente.md) ⚠️ *placeholder*
- **K-22** — [Fuentes pendientes de cosechar: gmail label projects-blog, posts en X, videos de Paradigmas](vida/draft-fuentes-pendientes-cosechar-gmail-x-videos.md) 📋 *meta-TODO*
- **K-23** — [Citas interesantes: colección anotada para usar en posts](vida/draft-citas-interesantes-coleccion.md) 🌱

---

## Apéndice histórico — `draft-rest.md` cosechado y eliminado

`draft-rest.md` (~233 líneas) era un mega-archivo de capturas con seis buckets de contenido. **El 2026-04-09 fue cosechado completo y eliminado del repo**: cada idea/concepto se extrajo a un archivo `draft-*.md` propio dentro de la categoría correspondiente. Este apéndice queda como **trazabilidad histórica** del cosecha — qué bucket produjo qué entradas — para que en el futuro sepas de dónde vino cada idea con `**Madurez:** seed-from-cosecha`.

| Bucket | Qué contenía | Drafts producidos |
| --- | --- | --- |
| 1 | Citas y links sobre OOP de Alan Kay (Reddit, SE.SE, Curtis Poe, FU Berlin) | [[A1-12]] (FU Berlin doc), [[C-06]] (Curtis Poe), [[C-07]] (consolidación Reddit/SE) |
| 2 | Brainstorm de temas de vida (matrimonio, paternidad, jubilación, religión, mascotas, finanzas, IA, etc.) | **Toda la Serie K**: [[K-01]] a [[K-23]] (23 drafts), más [[E-17]] (papel→pc→chatgpt) que fue al memoir CS |
| 3 | Lista de libros leídos (Little Lisper, Little Schemer, Hacker Howto, ESR, Clean Code, etc.) | [[E-18]] a [[E-29]] (12 drafts en memoir/) |
| 4 | Roster de *Masterminds of Programming* (17 entrevistas) | [[A1-13]] (roster) + [[A1-14]]..[[A1-21]] (8 entradas individuales destacadas: APL, BASIC, SQL, Perl, Haskell, Lua, Java, Hejlsberg). Refs archive.org → [[I-12]] (folkscanomy) e [[I-13]] (papers académicos viejos) |
| 5 | Refs técnicas transversales (CTM/Mozart, CSP, hexagonal, Lambda the Ultimate, expert system BASIC, DCI, MDA rant, Turing awards) | [[A2-08]] (Simply Scheme), [[A2-09]] (Lambda the Ultimate Imperative), [[D-05]] (Turing Awards), [[D-06]] (Sutherland constraints), [[C-08]] (MDA rant), [[C-09]] (DCI), [[C-10]] (Gosling vs herencia). Las refs ya absorbidas en `tr-NN` se quedaron donde estaban. |
| 6 | Transcripción del email *Tidy First / Developer Productivity Metrics* (Kent Beck × Abi Noda) | [[C-11]] (Goodhart), [[C-12]] (Forest/Desert), [[C-13]] (anti-productivity Cutler), [[C-14]] (XP values/principles/practices), [[C-15]] (vender dashboards malpractice), [[C-16]] (DX vs effectiveness). Cita de cierre Doug Linder → [[J-09]]. |

**Total cosechado**: 64 nuevos drafts distribuidos en 9 categorías (incluyendo la nueva [vida/](vida/) — Serie K).

**Cierre del ciclo**:
- `draft-rest.md` — **eliminado del repo el 2026-04-09**. Trazabilidad de cada idea → la columna "Drafts producidos" en la tabla de arriba.
- `ipc.c` — placeholder físico vacío que vivía en la raíz como recordatorio de [[I-06]] — **eliminado del repo el 2026-04-09**. La idea sigue en `local/draft-ipc-en-c-cinco-mecanismos-unix.md` (entrada I-06).

**Lección operativa**: el patrón "mega-archivo de capturas → cosecha en lotes → archivos de categoría → eliminar el mega-archivo" funcionó. Cuando vuelva a aparecer un `draft-rest.md` v2 con capturas acumuladas, repetir el mismo flujo: clasificar por buckets, extraer cada idea como draft individual, eliminar el fuente.

`draft-rest.md` (~233 líneas) **no es un post**. Es un mega-archivo de capturas con seis tipos de contenido distintos. En vez de tratarlo como una entrada del plan, lo procesamos como un pipeline de cosecha:

| Bucket | Líneas (aprox) | Qué contiene | Destino |
| --- | --- | --- | --- |
| 1 | 8-21 | Citas y links sobre OOP de Alan Kay (Reddit, SE.SE, Curtis Poe, etc.) | Cosechar a la bibliografía de [[A1-01]] / [[C-05]] (post de Kay), después borrar de `draft-rest.md` |
| 2 | 25-46 | Brainstorm de temas de vida (matrimonio, paternidad, jubilación, religión, mascotas) | **Out of scope** para katra. Mover a un cuaderno personal o eliminar. |
| 3 | 54-65 | Lista de libros leídos (Little Lisper, Little Schemer, Hacker Howto, ESR Unix, Clean Code, etc.) | **Genera un post nuevo: [[E-08]]** "Los libros que me hicieron programador". |
| 4 | 70-87 | Roster de *Masterminds of Programming* (APL, BASIC, Forth, ML, SQL, AWK, PostScript, C++, Eiffel, Objective-C, Perl, Haskell, Python, Lua, Java, UML, Delphi/C#) | **Genera un post nuevo: [[E-09]]** "Masterminds of Programming: lectura selectiva". |
| 5 | 91-120 | Refs técnicas transversales (CTM/Mozart, CSP, hexagonal arch, Lambda the Ultimate, expert system in BASIC, DCI) | Alimenta la [Bibliografía transversal](#bibliografía-transversal) (entries `tr-NN`). Ya están extraídas. |
| 6 | 131-233 | Transcripción del artículo *Tidy First / Developer Productivity Metrics* (Kent Beck × Abi Noda) | Cosechar a la bibliografía de [[C-03]] (Tidy First). Una vez integrado, borrar de `draft-rest.md`. |

**Acción al terminar:** una vez que las 6 cosechas se ejecutaron, `draft-rest.md` queda vacío y se elimina del repositorio.

---

## Waves de publicación

> **Importante:** el orden es sugerencia para combatir la fatiga de decisión, no una secuencia estricta. Si un post te tira hoy, escribilo hoy. La fecha de la próxima revisión de waves está al inicio del documento (`Última revisión:`).

| Wave | Tema | Posts | Notas |
| --- | --- | --- | --- |
| **W0** | Cosecha rápida (ya tienen prosa real) | 1 pendiente | ~~[[C-01]]~~ publicado 2026-04-14; [[G-01]] (Ansible roles/profiles, ~318 líneas) pendiente |
| **W1** | Crowd pleasers (biografías de bajo esfuerzo, imágenes públicas abundantes) | 5 | [[D-01]] Engelbart, [[D-03]] Turing, [[D-02]] Sketchpad, [[A1-01]] Kay, [[A2-03]] Y combinator (Weirich) |
| **W2** | Lanzamiento de cada serie (un post-piloto por serie para crear los anchors de cross-link) | ~9 | El post más fácil de cada serie. Una vez escritos, todas las series tienen al menos un destino para los `[[ID]]`. |
| **W3** | Round-robin de completitud | ~30 | Completar series rotando: la que va más atrás tiene prioridad. Mantiene visibilidad de las 10 series sin agotar al lector. |
| **W4** | Deep dives difíciles | ~6 | [[B-02]] Okasaki, [[B-06]] teoría imperativa, [[H-04]] migración COBOL, [[B-05]] trampolines, [[B-08]] WAM. Necesitan código, diagramas y pedagogía cuidadosa. Se escriben cuando hay momentum acumulado. |
| **W5** | Bloque concentrado de Serie H | ~6-9 | Toda la Serie H se escribe en un sprint corto, porque los posts se cruzan mucho entre sí y es más eficiente trabajarlos juntos. |

---

## Mantenimiento del plan

- **Re-leer mensual** para ver dónde está cada wave; **revisión profunda trimestral** (mover posts entre waves, marcar como "en hibernación" los que ya no entusiasman *sin borrarlos*, agregar los nuevos `draft-*.md` de cada categoría al índice correspondiente de este plan).
- Cuando aparezca una idea nueva, crear directamente el archivo `draft-{slug}.md` en la carpeta de categoría que corresponda (ver [estructura del directorio](#estructura-del-directorio)). Dentro de la semana, agregarla al índice de la serie en este archivo con su ID `{serie}-{NN}`.
- **Las ideas se conservan, no se descartan**: algunas de las 180 ideas nunca se van a escribir, y eso está bien — la idea sigue siendo valiosa aunque no encuentre tiempo para convertirse en post. El plan es un archivo de ideas, no una lista de tareas pendientes con vencimiento. Nada se borra por "no haberse escrito a tiempo". Si una entrada cambia de relevancia, marcala dentro de su archivo draft (estado "en hibernación", "concepto refinado", "ya no me entusiasma pero la dejo por las dudas") en vez de eliminarla. La única razón para borrar un archivo draft es que el concepto haya quedado *factualmente* superado.
- **Registrar el estado** después de publicar: cambiar `Estado actual:` dentro del archivo draft a `publicado YYYY-MM-DD - <slug-final>`, y resolver los `[[ID]]` salientes a links reales.
- **Owner**: César. Archivo privado, no se comparte (ni siquiera al sitio público).
- **Conflicto pendiente**: `AGENTS.md` dice TOML para frontmatter, pero todos los posts usan YAML. Próxima edición de `AGENTS.md`: corregir.
