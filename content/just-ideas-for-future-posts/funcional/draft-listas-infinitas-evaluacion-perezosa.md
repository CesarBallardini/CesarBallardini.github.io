### B-01 — Listas infinitas: cómo evaluar lo que no termina

- **Archivo seed:** `dev/draft-listas-infinitas.md`
- **Slug propuesto:** `listas-infinitas-evaluacion-perezosa`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-listas-infinitas-evaluacion-perezosa/index.md`
- **Serie:** B
- **Cross-links:** depende de [[tr-03]]; lleva a [[B-02]] (Okasaki), [[B-05]] (trampolines), [[A2-01]] (SICP §3.5)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** medium (1500-2000 palabras)

**Concepto:** evaluación perezosa permite definir estructuras de datos que no terminan (los primos, los Fibonacci, las primeras N páginas de un crawler). Lo "raro" no es la lista infinita: es la *evaluación estricta* que damos por defecto. El post enseña a pensar en términos de "valores que se van computando cuando los pedís".

**Hook:** "definí los números primos como una lista. Toda la lista. Todos los primos. Y después pedí los primeros 10. Si esto te suena imposible, te falta una idea de Computer Science del año 1976."

**Outline:**
1. La intuición: una lista infinita es plausible si nadie te obliga a calcularla entera.
2. Streams en SICP §3.5: cómo definir `cons-stream` y `force` con poco más que clausuras.
3. El sieve de Eratóstenes en Haskell de 2 líneas (y por qué la versión "obvia" no es eficiente — el detalle del primer paper de Melissa O'Neill).
4. Aplicaciones reales: paginación lazy, parsers, reactive streams.
5. La trampa: leak de memoria si retenés referencias al inicio de un stream infinito (el problema del "head clinger").
6. Cierre: por qué esto cambia cómo ves loops y for-each.

**Bibliografía:**
- [[tr-03]] — SICP §3.5 "Streams".
- [[tr-14]] — Wadler, *Theorems for Free!* (uso de streams como ejemplo).
- [Melissa O'Neill, *The Genuine Sieve of Eratosthenes*](https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf), JFP 2009 — el paper sobre por qué el sieve "Haskell de 2 líneas" no es realmente el sieve.
- [Simon Peyton Jones, *The Implementation of Functional Programming Languages*, 1987](https://www.microsoft.com/en-us/research/wp-content/uploads/1987/01/slpj-book-1987.pdf) — referencia clásica de lazy eval.
- [Haskell Wiki — Lazy evaluation](https://wiki.haskell.org/Lazy_evaluation).
- [Stream (computer science) en Wikipedia](https://en.wikipedia.org/wiki/Stream_(computing)).
- [Phil Bagwell, *Ideal Hash Trees*, 2001](https://lampwww.epfl.ch/papers/idealhashtrees.pdf) — relacionado: estructuras lazy persistentes.

**Imágenes:**
- _Crear_: SVG didáctico — un stream representado como `[1 | <thunk>]` y cómo se va expandiendo cuando lo pedís (~30 min, Excalidraw).
- _Crear_: gráfico simple del sieve mostrando los números tachados (~20 min).

**Tags propuestos:** `['lazy evaluation', 'streams', 'Haskell', 'Scheme', 'SICP']`

**Estado actual:** sólo título.

