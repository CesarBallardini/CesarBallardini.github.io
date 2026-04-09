### B-02 — Estructuras de datos puramente funcionales (Okasaki)

- **Archivo seed:** `dev/draft-estructuras-de-datos-funcionales.md`
- **Slug propuesto:** `okasaki-estructuras-funcionales`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-okasaki-estructuras-funcionales/index.md`
- **Serie:** B (deep dive)
- **Cross-links:** depende de [[tr-04]]; lleva a [[B-01]] (lazy eval), [[B-05]] (trampolines), [[B-06]] (teoría imperativa: contraste)
- **Idioma:** es
- **Madurez:** seed-with-sources (la tesis es la fuente)
- **Length target:** long (2500-3500 palabras)

**Concepto:** ¿se puede tener una estructura de datos eficiente sin mutación? Sí, y la tesis de Okasaki muestra exactamente cómo. Listas, queues, deques, heaps, todo *persistent* (cualquier versión vieja sigue accesible) y con costos amortizados óptimos. El truco: lazy evaluation usada con disciplina.

**Hook:** "vamos a construir una queue inmutable que es tan rápida como una mutable. Sí, eso suena imposible. Y sin embargo, hace 30 años Chris Okasaki publicó la tesis donde explica cómo. Pasemos por el truco principal: mover el costo en el tiempo, no en el espacio."

**Outline:**
1. El problema: estructuras "persistentes" (mantener todas las versiones viejas accesibles) sin pagar O(n) por operación.
2. La distinción entre eager y lazy y por qué lazy es el corazón de la solución.
3. El amortized analysis y los physicist's debits.
4. La Banker's Queue: cómo una queue persistente puede ser O(1) amortizado.
5. Heaps: pairing heaps, binomial heaps, leftist heaps.
6. Por qué importa hoy: Clojure, Scala collections, Erlang/Elixir, los sistemas reactivos.
7. Cierre: el contraste con el dogma "inmutable es siempre más lento".

**Bibliografía:**
- [[tr-04]] — Okasaki, *Purely Functional Data Structures*, CMU thesis 1996.
- Chris Okasaki, *Purely Functional Data Structures*, Cambridge University Press 1998 (la versión libro extendida).
- [Chris Okasaki, *Simple and Efficient Purely Functional Queues and Deques*, JFP 1995](https://www.cambridge.org/core/journals/journal-of-functional-programming/article/abs/simple-and-efficient-purely-functional-queues-and-deques/01C3C72D29B5BBC60D75AB17BA1CFA1F).
- [Phil Bagwell, *Ideal Hash Trees*, 2001](https://lampwww.epfl.ch/papers/idealhashtrees.pdf) — la base de las collections persistentes de Clojure.
- [Persistent data structure en Wikipedia](https://en.wikipedia.org/wiki/Persistent_data_structure).
- [Eric Lippert, *Immutability in C#, Part 1*](https://learn.microsoft.com/en-us/archive/blogs/ericlippert/immutability-in-c-part-one-kinds-of-immutability) — para audiencia .NET.
- [Rich Hickey, *Are We There Yet?*, JVM Languages Summit 2009](https://www.infoq.com/presentations/Are-We-There-Yet-Rich-Hickey/) — por qué Clojure usa Bagwell's HAMTs.
- [Edward Z. Yang, *You could have invented fractional cascading*](http://blog.ezyang.com/2012/03/you-could-have-invented-fractional-cascading/) — relacionado, didáctico.

**Imágenes:**
- _Crear_: 4-5 SVG progresivos mostrando una banker's queue después de operaciones sucesivas (1-2 horas, esto es el corazón didáctico del post).
- _Crear_: diagrama del HAMT (Hash Array Mapped Trie) (~45 min).

**Tags propuestos:** `['estructuras de datos', 'Okasaki', 'persistent', 'Clojure', 'lazy', 'amortized']`

**Estado actual:** seed-with-sources; este es uno de los posts más exigentes del plan.

