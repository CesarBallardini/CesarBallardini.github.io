### A2-04 — Sistemas expertos en BASIC (lo que salió en Byte)

- **Archivo seed:** `dev/draft-expert-system-en basic.md` (atención: filename con espacio antes de "basic")
- **Slug propuesto:** `sistemas-expertos-en-basic-byte-1981`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-sistemas-expertos-en-basic-byte-1981/index.md`
- **Serie:** A2 (Lisp lineage — el código original de Byte fue un port de un sistema en Lisp de Winston)
- **Cross-links:** depende de [[tr-05]] (Winston *LISP*), [[tr-10]] (Byte archive); lleva a [[A2-02]] (Lambda papers), [[J-03]] (MindForth como descendiente moral)
- **Idioma:** es
- **Madurez:** seed-with-sources (URLs específicas en draft-rest.md líneas 108-112)
- **Length target:** medium (1500-1800 palabras)

**Concepto:** en septiembre de 1981 *Byte Magazine* publicó "Knowledge-Based Expert Systems Come of Age" con código BASIC funcional para construir tu propio sistema experto. El código era un port directo del capítulo 18 del libro *LISP* de Patrick Winston. El post es sobre por qué eso era totalmente normal en los 80 y por qué hoy nos parece marciano.

**Hook:** "en 1981 podías comprar una revista en el quiosco que te enseñaba a hacer un sistema experto. En BASIC. Para tu IBM PC. Y funcionaba. Hoy te explican cómo hacer un wrapper de OpenAI y eso se llama AI."

**Outline:**
1. Contexto 1981: AI hype #1, expert systems en boca de todos, MYCIN, DENDRAL.
2. Byte Magazine, septiembre 1981 — el issue dedicado a expert systems. Quiénes lo escribieron (Duda, Gaschnig).
3. El código BASIC: 40-50 líneas para un motor de inferencia básico (forward chaining, IF-THEN rules).
4. El código original en Lisp (Winston cap. 18): cómo se ve el mismo motor en una página de Lisp.
5. Por qué BASIC era un objetivo razonable: era *el* lenguaje de las microcomputadoras.
6. Cierre: la lección que olvidamos — un sistema experto bien hecho de 50 líneas es más explicable que un LLM de 70B parámetros, y para muchos dominios, suficiente.

**Bibliografía:**
- [[tr-05]] — Winston & Horn, *LISP* (1981), capítulo 18 "Expert Problem Solving Using IF-THEN Rules".
- [[tr-10]] — Byte Magazine archive.
- [Byte Magazine, septiembre 1981, "Knowledge-Based Expert Systems Come of Age" (Duda & Gaschnig)](https://archive.org/details/byte-magazine-1981-09/page/n239/mode/1up) — el issue completo.
- [Código BASIC del artículo, Byte 1981-09](https://archive.org/details/byte-magazine-1981-09/page/n265/mode/1up) — los listados.
- [Byte Magazine, abril 1985, versión en Pascal y pseudocódigo](https://vintageapple.org/byte/pdf/198504_Byte_Magazine_Vol_10-04_Artificial_Intelligence.pdf) — pp. 315.
- [Edward Feigenbaum, *Expert Systems in the 1980s*](https://web.stanford.edu/dept/cs/historical/feigenbaum-expert-systems.pdf) — perspectiva histórica.
- [MYCIN en Wikipedia](https://en.wikipedia.org/wiki/Mycin) — el ejemplar canónico de expert system.
- [Patrick Winston obituary en MIT News](https://news.mit.edu/2019/professor-patrick-winston-obituary-0719) — para situar a Winston.

**Imágenes:**
- _Archive.org_: scan de las páginas relevantes del Byte 1981-09 (uso académico/educativo, atribución a Byte).
- _Crear_: comparación side-by-side del mismo motor en BASIC vs Lisp (~30 min).

**Tags propuestos:** `['expert system', 'BASIC', 'LISP', 'Patrick Winston', 'Byte', 'AI history']`

**Estado actual:** seed con URLs específicas en `draft-rest.md` lineas 108-112.

