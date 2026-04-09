### B-05 — Trampolines: saltar para no apilar

- **Archivo seed:** `dev/draft-trampoline.md`
- **Slug propuesto:** `trampolines-saltar-para-no-apilar`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-trampolines-saltar-para-no-apilar/index.md`
- **Serie:** B
- **Cross-links:** depende de [[B-04]]; lleva a [[A2-02]] (Lambda papers, donde aparece el truco), [[B-02]] (Okasaki, otra manera de no apilar)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** medium (1200-1500 palabras)

**Concepto:** un trampoline es la manera de simular tail call optimization en un lenguaje que no la tiene. La función recursiva no se llama a sí misma directamente; devuelve una *thunk* que el trampoline después invoca. Resultado: stack flat aunque tu lenguaje (Java, Python, JS pre-ES6 sin TCO) no coopere.

**Hook:** "Java no optimiza tail calls. Por lo tanto Java no puede hacer recursión profunda. ERROR. Java *sí* puede hacer recursión arbitrariamente profunda, sólo que tenés que enseñarle el truco. Se llama trampoline, y cabe en 10 líneas."

**Outline:**
1. El problema: lenguajes sin TCO + recursión profunda = StackOverflowError.
2. La idea del trampoline: en vez de llamarte recursivamente, devolvé una función que cuando se invoque haga el siguiente paso.
3. La implementación mínima en JavaScript / Java / Python (10 líneas cada una).
4. Ejemplo: factorial mutuo (par/impar) — el caso donde ni tail recursion clásica ayuda.
5. Conexión con CPS: el trampoline es CPS-to-trampolined-style transformation.
6. Cierre: por qué este truco aparece en intérpretes (Lua bytecode dispatcher), parsers (combinator libraries) y otros lugares "lejos" de funcional puro.

**Bibliografía:**
- [Steve Ganz, Daniel Friedman, Mitch Wand, *Trampolined Style*, ICFP 1999](https://www.cs.indiana.edu/~dyb/pubs/stack.pdf) — el paper canónico.
- [Trampoline (computing) en Wikipedia](https://en.wikipedia.org/wiki/Trampoline_(computing)).
- [Rúnar Bjarnason, *Stackless Scala With Free Monads*, Scala Days 2012](https://blog.higher-order.com/assets/trampolines.pdf).
- [Jim Duey, *Clojure trampoline tutorial*](https://web.archive.org/web/20150906131833/http://jimduey.com/perm/2010-05-08T15:04:55+00:00.html) — frágil, en Wayback.
- [Continuation-passing style en Wikipedia](https://en.wikipedia.org/wiki/Continuation-passing_style).
- [Roshan James & Amr Sabry, *Yield: Mainstream Delimited Continuations*](https://legacy.cs.indiana.edu/~rpjames/yield.pdf) — pariente conceptual moderno.

**Imágenes:**
- _Crear_: animación SVG conceptual (3-4 frames) — la diferencia entre llamada recursiva tradicional (stack crece) y trampoline (stack se mantiene plano) (~45 min).

**Tags propuestos:** `['trampoline', 'tail recursion', 'CPS', 'Java', 'Clojure']`

**Estado actual:** sólo título.

