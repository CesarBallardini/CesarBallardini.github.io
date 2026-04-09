### A2-09 — Lambda the Ultimate Imperative: el paper de Steele que cambió cómo pensar imperativo

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `lambda-the-ultimate-imperative`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-lambda-the-ultimate-imperative/index.md`
- **Serie:** lisp
- **Cross-links:** [[A2-02]] (Scheme papers), [[B-03]] (recursivo a iterativo), [[B-04]] (tail recursion)
- **Idioma:** es
- **Madurez:** seed-from-cosecha (raw idea, falta desarrollar)
- **Length target:** _por definir_

**Concepto:** *Lambda: The Ultimate Imperative* (Guy L Steele, 1976) es uno de los famosos "Lambda Papers" donde Steele muestra que cualquier construcción de control imperativo (loops, gotos, exception handlers) puede expresarse como un caso particular de una llamada a procedimiento con continuaciones. El post explica el argumento del paper en términos modernos, con ejemplos en Scheme y JavaScript, y discute por qué este paper sigue siendo la base teórica de los compiladores modernos.

**Hook:** cualquier loop, cualquier goto, cualquier try/catch, es secretamente una llamada a una función. Eso lo demostró Guy Steele en 1976 en un paper de 19 páginas. El post lo explica sin matemática.

**Outline:** _por desarrollar — el concepto está, falta el orden de presentación_

**Bibliografía:**
- Guy L Steele Jr, *Lambda: The Ultimate Imperative*, MIT AI Memo 353, 1976
- [[tr-14]] Lambda the Ultimate classic papers
- github.com/scheme-and-computer-science/library.readscheme.org

**Imágenes:** _a definir_

**Tags propuestos:** `['Scheme','Steele','lambda papers','continuations','compilers','historia CS']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. La idea está identificada con concepto + hook + bibliografía mínima; el outline y la prosa quedan pendientes.
