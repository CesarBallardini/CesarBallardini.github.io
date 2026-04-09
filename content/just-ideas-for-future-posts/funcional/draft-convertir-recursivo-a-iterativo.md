### B-03 — Convertir un programa recursivo a iterativo

- **Archivo seed:** `dev/draft-convierte-un-programa-recursivo-a-iterativo.md`
- **Slug propuesto:** `convertir-recursivo-a-iterativo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-convertir-recursivo-a-iterativo/index.md`
- **Serie:** B
- **Cross-links:** lleva a [[B-04]] (la versión "elegante": recursión de cola), [[B-05]] (cuando ni eso sirve: trampolines)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** medium (1500-2000 palabras)

**Concepto:** dada una función recursiva, hay una técnica mecánica para transformarla en iterativa con una pila explícita. El post enseña la receta y muestra cuándo (y cuándo no) usarla.

**Hook:** "vamos a tomar el quicksort recursivo más típico que viste en clase de algoritmos, y lo vamos a convertir en un loop con un array. Sin recursión. Y vamos a entender por qué esa transformación es siempre posible."

**Outline:**
1. Por qué uno querría hacer esto: stack limit, lenguajes sin TCO, performance, debugging.
2. La receta general: cada llamada recursiva → push de continuación + estado.
3. Ejemplo simple: factorial recursivo → factorial con pila explícita.
4. Ejemplo no-tan-simple: traversal de árbol DFS recursivo → con pila.
5. Ejemplo donde duele: quicksort. Por qué no se ve tan elegante.
6. La conexión con CPS: convertir-a-iterativo y CPS-transform son dos caras de lo mismo.
7. Cierre: cuándo NO hacerlo (legibilidad gana al stack limit en el 95% de los casos).

**Bibliografía:**
- [[tr-03]] — SICP §1.2 (recursive vs iterative process) y §3.2 (environment model).
- [Andrew W. Appel, *Compiling with Continuations*, Cambridge University Press 1992](https://www.cs.princeton.edu/~appel/cwc/) — la referencia para CPS.
- [Olivier Danvy, *A First-Order One-Pass CPS Transformation*](http://www.brics.dk/RS/01/49/) — paper técnico.
- [Tail call en Wikipedia](https://en.wikipedia.org/wiki/Tail_call) — para enlazar con [[B-04]].
- [Stack-oriented programming en Wikipedia](https://en.wikipedia.org/wiki/Stack-oriented_programming).
- [The Quicksort algorithm — C.A.R. Hoare, 1961](https://comjnl.oxfordjournals.org/content/5/1/10.full.pdf) — el original.
- [GCC manual on `-foptimize-sibling-calls`](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html) — TCO en compiladores reales.

**Imágenes:**
- _Crear_: animación frame-by-frame (4-5 SVG) de la pila durante un factorial recursivo y su contraparte iterativa (~1 hora).
- _Crear_: side-by-side de quicksort recursivo vs con pila explícita (~30 min).

**Tags propuestos:** `['recursion', 'iteration', 'stack', 'algoritmos', 'CPS']`

**Estado actual:** sólo título.

