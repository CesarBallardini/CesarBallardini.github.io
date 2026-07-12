### A2-08 — Simply Scheme: el libro con el que Berkeley enseñó a 500 programadores principiantes

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `simply-scheme-500-programadores`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-simply-scheme-500-programadores/index.md`
- **Serie:** lisp
- **Cross-links:** [[A2-01]] (SICP), [[A2-07]] (DrRacket), [[E-18]] (Little Lisper)
- **Idioma:** es
- **Madurez:** seed-from-cosecha (raw idea, falta desarrollar)
- **Length target:** _por definir_

**Concepto:** *Simply Scheme* (Brian Harvey & Matthew Wright, MIT Press 1994) es el libro que Berkeley usaba para enseñar el primer curso de CS a no-mayors de informática. Pensado como introducción suave a los conceptos de SICP. El "500" del título no es una anécdota de cantidad de alumnos — es una cita verbatim del prefacio: la caricatura que Harvey y Wright hacen de la "vista conservadora" ("500 mediocre programmers can join together...") contra la "vista radical" que ellos sostienen (expandir la mente con ideas más grandes en vez de disciplinar el trabajo de una masa). Verificado por fetch directo a `ssch0/preface.html`, `ssch0/foreword.html` y `ssch0/instructor.html` — no hay ninguna cita de "500 veces mejor" en el libro; la única mención de "500" es esta.

**Hook:** la cita textual del prefacio — "500 mediocre programmers" vs "expand their minds" — como cold open. El post arma el post entero alrededor de esa dicotomía: escalar cabezas disciplinadas vs. escalar lo que una sola mente puede sostener.

**Outline:** cold open con las dos citas → "Un curso para los que no iban a ser programadores" (CS3, alumnos no-CS) → "Un prólogo a SICP" (con la cita correcta del foreword de Abelson, no del prefacio) → "La interacción como método, no como lujo" (Dijkstra) → "Tres decisiones que construyen una mente expandida" (HOF antes que recursión, cero mutación, programación simbólica) → "Leerlo hoy" (cierre volviendo a la dicotomía 500 vs. pocos, aplicada a los cursos intro actuales).

**Bibliografía:**
- *Simply Scheme: Introducing Computer Science*, Brian Harvey & Matthew Wright, MIT Press 1994 (2nd ed 1999) — people.eecs.berkeley.edu/~bh/ss-toc2.html
- Prefacio: people.eecs.berkeley.edu/~bh/ssch0/preface.html (cita de los "500 mediocre programmers")
- Prólogo (Hal Abelson): people.eecs.berkeley.edu/~bh/ssch0/foreword.html (cita "points the way out of the trap" — ojo, esta cita es del foreword, no del prefacio; el primer borrador la atribuía mal)

**Imágenes:** ninguna (post sin imágenes, archivo plano seguiría siendo válido pero ya se creó como bundle)

**Tags propuestos:** `['libros','Scheme','pedagogia','Berkeley','Brian Harvey']`

**Estado actual:** borrador completo escrito en `content/es/posts/2026-04-16-simply-scheme-500-programadores/index.md` (2026-07-11), todavía sin `git add` ni commit. Título ajustado a "el libro que no quería 500 programadores mediocres" para reflejar la cita real. Pendiente: revisión final del usuario antes de commitear.
