### A2-03 — Jim Weirich y el Y combinator (en vivo)

- **Archivo seed:** `dev/jim-weinrich-y-combinator.md` (nota: el filename tiene "weinrich", el correcto es "Weirich")
- **Slug propuesto:** `jim-weirich-y-combinator-en-vivo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-jim-weirich-y-combinator-en-vivo/index.md`
- **Serie:** A2
- **Cross-links:** depende de [[tr-14]]; lleva a [[A2-02]] (Lambda papers), [[B-01]] (listas infinitas)
- **Idioma:** es
- **Madurez:** seed-with-sources (hay vídeo)
- **Length target:** medium (1200-1600 palabras)

**Concepto:** el Y combinator (la versión de Curry, no la incubadora) es el truco más mágico del cálculo lambda: cómo escribir recursión sin nombres. Jim Weirich lo derivó en vivo en una charla, sobre Ruby, paso a paso. Si entendiste eso, entendiste lambda. Si no, este post (y el vídeo) son tu mejor camino.

**Hook:** "Imaginate escribir una función recursiva en un lenguaje que no permite nombres. ¿Imposible? Es exactamente lo que el Y combinator hace, y Jim Weirich nos lo muestra paso a paso, en una hora, en Ruby. Hagamos juntos cada paso."

**Outline:**
1. Quién fue Jim Weirich (Rake, autoría en Ruby community, sus charlas legendarias). Una breve nota in memoriam.
2. La pregunta: ¿se puede hacer recursión sin asignar nombres a funciones?
3. Lambda calculus mínimo necesario (variables, abstracción, aplicación; nada más).
4. La derivación paso a paso: factorial → factorial helper → factorial (lambda x. x x) → Y.
5. Por qué hay dos Ys (uno para call-by-value, uno para call-by-name).
6. El cierre: por qué este truco aparenta ser un juguete y termina siendo el corazón de cómo se prueban teoremas en sistemas de tipos.

**Bibliografía:**
- [Jim Weirich, *Y Not? Adventures in Functional Programming*, ScotlandRuby 2012](https://www.youtube.com/watch?v=FITJMJjASUs) — la charla canónica.
- [Mike Vanier, *The Y Combinator (Slight Return) or: How to Succeed at Recursion Without Really Recursing*](https://mvanier.livejournal.com/2897.html) — derivación escrita.
- [Jim Weirich obituary en Ruby Inside](https://web.archive.org/web/20140410112156/http://rubyinside.com/jim-weirich-1956-2014-7170.html) — frágil, in Wayback.
- [Y combinator en Wikipedia](https://en.wikipedia.org/wiki/Fixed-point_combinator).
- [Jim Weirich, *The Building Blocks of Modularity*, Ruby Conf 2011](https://www.youtube.com/watch?v=NCC2MIYFQa0) — para situar a Jim.
- [The Little Schemer (Friedman & Felleisen)](https://mitpress.mit.edu/9780262560993/the-little-schemer/), capítulos 8-9 — la derivación en libro.
- [SICP §1.3.2 — derivación de combinators](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-12.html#%_sec_1.3.2).

**Imágenes:**
- _Embed_: thumbnail del vídeo *Y Not?* en YouTube.
- _Crear_: opcional — diagrama SVG de la reducción β paso a paso (~45 min).

**Tags propuestos:** `['Y combinator', 'Jim Weirich', 'Ruby', 'lambda calculus', 'in memoriam']`

**Estado actual:** seed con notas; el vídeo es la pieza central y está estable.

