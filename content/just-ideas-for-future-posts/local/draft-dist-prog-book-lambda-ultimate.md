### I-11 — Dist-prog-book: el libro sobre programación distribuida que forkeé para leer (y la colección de Lambda the Ultimate)

- **Archivo seed:** `github.com/CesarBallardini/dist-prog-book` (fork, CSS, Feb 2021)
- **Slug propuesto:** `dist-prog-book-lambda-ultimate`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-dist-prog-book-lambda-ultimate/index.md`
- **Serie:** I — por el ángulo "material raro que colecciono para estudiar"
- **Cross-links:** lleva a [[A2-02]] (Lambda papers), [[B-06]] (teoría imperativa), [[E-08]] (libros que me marcaron)
- **Idioma:** es
- **Madurez:** fork del libro comunitario "Programming Models for Distributed Computing" (Christopher Meiklejohn et al)
- **Length target:** short-medium (1000-1500 palabras)

**Concepto:** *dist-prog-book* es un libro comunitario editable sobre modelos de programación distribuida, curado por Christopher Meiklejohn. Lo forkeé en 2021 para leer. El post es un "libro roto por dentro" — una reseña del estado del libro, de sus capítulos más fuertes (actor model, lattices y CRDTs, consenso, monitores), y una invitación a leerlo en paralelo con [[A2-02]] (los Lambda papers) para entender cómo la programación distribuida mainstream sigue tropezándose con problemas que los teóricos de lenguajes resolvieron hace 40 años.

**Hook:** "hay un libro gratis y editable en GitHub que se llama *Programming Models for Distributed Computing*. Lo hizo Christopher Meiklejohn con colaboradores. No es perfecto, no está terminado, y sin embargo es la introducción más honesta a los modelos serios de programación distribuida. El post es una reseña desde dentro del fork, con tres capítulos destacados."

**Outline:**
1. Qué es el libro, quién lo hizo, por qué importa.
2. Capítulo destacado: actor model (Hewitt, Agha).
3. Capítulo destacado: CRDTs y lattices para consistencia eventual.
4. Capítulo destacado: consenso (Paxos/Raft sin tears).
5. Lo que le falta al libro vs lo que le sobra.
6. Cierre: leanlo antes de escribir un sistema distribuido "desde cero".

**Bibliografía:**
- [dist-prog-book en GitHub](https://github.com/heathermiller/dist-prog-book) — el upstream.
- [Christopher Meiklejohn — blog](http://christophermeiklejohn.com/).
- [Lambda the Ultimate — classic papers](http://lambda-the-ultimate.org/classic/papers.html).

**Imágenes:**
- _Crear_: tabla de los capítulos y su madurez (~30 min).

**Tags propuestos:** `['distributed systems', 'CRDTs', 'actor model', 'libro', 'review']`

**Estado actual:** fork funcional + lectura parcial. Post como reseña.

