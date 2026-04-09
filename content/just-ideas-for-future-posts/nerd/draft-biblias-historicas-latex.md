### J-04 — Tipografiar Biblias históricas con LaTeX: Reina-Valera 1865 y Geneva 1564

- **Archivo seed (repos POC):** [github.com/CesarBallardini/rv1865](https://github.com/CesarBallardini/rv1865) (TeX, 1 star, 2015) + [github.com/CesarBallardini/geneve_1564](https://github.com/CesarBallardini/geneve_1564) (fork, TeX, 2015)
- **Slug propuesto:** `biblias-historicas-latex`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-biblias-historicas-latex/index.md`
- **Serie:** J — curiosidad nerd lateral
- **Cross-links:** lleva a [[I-02]] (digitalización en otro contexto)
- **Idioma:** es
- **Madurez:** **complete-poc** rv1865, fork de geneve_1564
- **Length target:** medium (1500-2200 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** en 2015, por una mezcla de curiosidad lingüística y nerd-LaTeX, me senté a tipografiar la **Reina-Valera 1865** (la revisión española de la Biblia previa a las revisiones de 1881 y 1909, las que circulan hoy) usando LaTeX. El motivo declarado fue: "quería una Biblia de estudio sin las críticas que se hacían a las revisiones posteriores a 1881". El motivo *real* fue probablemente la combinación de proyecto chico-pero-largo + LaTeX + texto histórico + dominio público. El proyecto hermano `geneve_1564` (fork) hace lo mismo con la **Geneva Bible 1564** (la Biblia inglesa pre-King James). El post no es sobre teología — es sobre el oficio de tipografiar texto histórico con herramientas modernas, los problemas técnicos (encoding, font selection, división por capítulos, índices, footnotes históricas) y el placer del proyecto largo de fin de semana.

**Hook:** "tengo un repo en GitHub que se llama `rv1865`. Adentro hay LaTeX. Compilás y obtenés la Biblia Reina-Valera revisión 1865, tipografiada decentemente, en PDF, ePub y HTML. ¿Por qué? La razón teológica está en el README. La razón técnica es más interesante: tipografiar texto histórico en LaTeX es un proyecto perfecto para alguien al que le gusta el detalle, las herramientas viejas y los textos en dominio público. Acá cuento cómo y por qué."

**Outline:**
1. La cosa rara primero: tengo un repo de la Biblia en LaTeX. Sí, en serio.
2. La motivación teológica (corto, sin entrar en detalles): variantes textuales y revisiones.
3. La motivación técnica (largo, lo interesante): por qué LaTeX es el mejor amigo del texto histórico.
4. Los problemas concretos:
   - **Encoding**: textos del siglo XIX tienen caracteres raros (eñes con tildes, comillas francesas, signos pre-modernos).
   - **Font selection**: cuál font usar para que se sienta histórica sin perder legibilidad.
   - **División por capítulos y versículos**: cómo modelar la estructura sin que el LaTeX se vuelva ilegible.
   - **Índices y referencias cruzadas**: la parte donde LaTeX brilla.
   - **Output múltiple**: PDF para imprimir, ePub para leer en e-reader, HTML para web.
5. El proyecto hermano `geneve_1564`: la Geneva Bible inglesa de 1564, fork de un proyecto upstream.
6. Lo que aprendí del proceso: el oficio de tipografiar texto histórico es lento, tranquilo, y tiene una recompensa estética muy específica.
7. Cierre: si querés un proyecto de fin de semana que no se termine, agarrá un texto histórico en dominio público y tipográfialo en LaTeX.

**Bibliografía:**
- Repos: [rv1865](https://github.com/CesarBallardini/rv1865), [geneve_1564](https://github.com/CesarBallardini/geneve_1564).
- [Reina-Valera 1865 — texto en archive.org](https://archive.org/) — buscar la edición específica.
- [Geneva Bible 1560/1564 — Wikipedia](https://en.wikipedia.org/wiki/Geneva_Bible).
- [LaTeX project](https://www.latex-project.org/).
- [Donald E Knuth, *The TeXbook*, Addison-Wesley 1984](https://www-cs-faculty.stanford.edu/~knuth/abcde.html) — el libro fundacional, oblicuo pero relevante.
- [The TeX Catalogue](https://ctan.org/topic/biblical) — paquetes específicos para textos bíblicos.
- [Project Gutenberg — Bibles](https://www.gutenberg.org/) — fuentes en dominio público.

**Imágenes:**
- _Crear_: screenshot del PDF compilado de rv1865 mostrando una página típica (~10 min).
- _Crear_: side-by-side de un versículo en RV 1865 vs RV 1909 (~15 min).
- _Crear_: snippet del LaTeX en una caja (~10 min).

**Tags propuestos:** `['LaTeX', 'Biblia', 'Reina Valera', 'Geneva Bible', 'tipografia', 'texto historico', 'nerd lateral']`

**Estado actual:** **POC funcional** rv1865 + fork de geneve_1564.

