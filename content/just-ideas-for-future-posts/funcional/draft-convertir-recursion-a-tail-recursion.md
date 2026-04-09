### B-04 — Convertir recursión a recursión de cola

- **Archivo seed:** `dev/draft-convierte-programa-recursivo-a-recursivo-de-cola.md`
- **Slug propuesto:** `convertir-recursion-a-tail-recursion`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-convertir-recursion-a-tail-recursion/index.md`
- **Serie:** B
- **Cross-links:** depende de [[B-03]]; lleva a [[B-05]] (trampolines, cuando el lenguaje no optimiza tail calls)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** medium (1200-1600 palabras)

**Concepto:** si tu lenguaje optimiza tail calls (Scheme, ML, Haskell, Erlang, Clojure con `recur`), podés escribir loops como funciones recursivas elegantes. La transformación es mecánica: agregar un acumulador.

**Hook:** "el factorial recursivo que aprendiste en la primera clase de programación tiene un problema escondido: si lo corrés con n=100000, te explota la pila. La buena noticia es que se arregla con un cambio de una línea, y el resultado es más limpio. Mostremos."

**Outline:**
1. Recap: qué es una llamada en posición de cola.
2. Por qué los compiladores que optimizan tail calls pueden reemplazar una llamada por un jump.
3. La transformación con acumulador, paso a paso, con factorial.
4. Ejemplo más interesante: `length` de una lista, `map` de una lista (mostrar el truco del "reverse al final").
5. Ejemplo donde no funciona: `tree-sum` (traversal binario — no podés acumular en tail position porque tenés dos hijos).
6. Cierre: qué hacés cuando tu lenguaje *no* optimiza tail calls. Pista: ver [[B-05]].

**Bibliografía:**
- [[tr-03]] — SICP §1.2 (donde se explica el processus iterativo).
- [Steele, *Debunking the "Expensive Procedure Call" Myth*, 1977](https://dspace.mit.edu/handle/1721.1/5753) — el paper que justifica la optimización.
- [R7RS — Scheme spec, sección sobre tail calls](https://small.r7rs.org/attachment/r7rs.pdf).
- [Clojure `recur` — official docs](https://clojure.org/reference/special_forms#recur).
- [Tail call en Wikipedia](https://en.wikipedia.org/wiki/Tail_call).
- [Guido van Rossum, *Tail Recursion Elimination*](https://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html) — el famoso post de por qué Python no la hace.
- [Rust RFC 81 — guaranteed tail call](https://github.com/rust-lang/rfcs/issues/2691) — debate moderno.

**Imágenes:**
- _Crear_: 3 SVG mostrando las stack frames del factorial recursivo (crece) vs tail-recursivo + TCO (no crece) (~30 min).

**Tags propuestos:** `['tail recursion', 'TCO', 'Scheme', 'Clojure', 'compiladores']`

**Estado actual:** sólo título.

