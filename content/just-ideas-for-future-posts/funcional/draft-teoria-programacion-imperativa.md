### B-06 — Teoría de la programación imperativa

- **Archivo seed:** `dev/draft-teoria-de-programacion-imperativa.md`
- **Slug propuesto:** `teoria-programacion-imperativa`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-teoria-programacion-imperativa/index.md`
- **Serie:** B (deep dive — pero el ángulo es "la teoría detrás del paradigma que nos parece el más obvio")
- **Cross-links:** depende de [[tr-19]] (Dijkstra), [[tr-18]] (Hoare); lleva a [[B-04]] (recursión vs iteración), [[C-05]] (revolución del cómputo)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** long (2500-3500 palabras)

**Concepto:** la programación imperativa parece "obvia" (asignás, secuencía, decidís, repetís) y sin embargo tiene una base teórica seria: Hoare logic, weakest preconditions de Dijkstra, separation logic. El post es una introducción honesta para alguien que escribió código imperativo toda la vida sin saber que había una teoría detrás.

**Hook:** "vos escribiste `x = x + 1` mil veces sin pensarlo. Ahora vamos a probar formalmente que ese `x = x + 1` es correcto. Y resulta que la matemática para hacerlo es más interesante que la matemática para los lenguajes funcionales."

**Outline:**
1. La pregunta tonta: ¿qué *significa* `x := x + 1`? Si pensás en términos de cuánto tiempo lleva responderla, el ejercicio recién empieza.
2. Hoare triples: `{P} S {Q}`. Pre, post, programa.
3. Las reglas de inferencia: assignment axiom, sequence rule, while rule, etc.
4. Weakest precondition de Dijkstra: la transformación inversa.
5. Loop invariants: la herramienta más infravalorada de la programación.
6. Más allá: separation logic (Reynolds, O'Hearn) — para cuando hay punteros y mutación compartida.
7. Cierre: por qué en 2026 las herramientas de verificación basadas en estas ideas (Dafny, Frama-C, Verified Software Toolchain) están más vivas que nunca.

**Bibliografía:**
- [C.A.R. Hoare, *An Axiomatic Basis for Computer Programming*, CACM 1969](https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf) — el paper fundacional.
- [Edsger Dijkstra, *A Discipline of Programming*, Prentice-Hall 1976](https://archive.org/details/disciplineofprog0000dijk) — el libro de weakest preconditions.
- [[tr-19]] — EWD archive.
- [John Reynolds, *Separation Logic: A Logic for Shared Mutable Data Structures*, LICS 2002](https://www.cs.cmu.edu/~jcr/seplogic.pdf).
- [Peter O'Hearn, *Separation Logic*, CACM 2019](https://cacm.acm.org/research/separation-logic/) — overview moderno.
- [Mike Gordon, *Mechanizing Programming Logics in Higher Order Logic*, 1989](https://www.cl.cam.ac.uk/archive/mjcg/papers/MechanizingProgrammingLogics.pdf) — bridge a verificación mecánica.
- [Dafny — programming + verification](https://dafny.org/) — herramienta moderna.
- [Frama-C](https://www.frama-c.com/) — para C verificado.
- [Verified Software Toolchain (VST) — Princeton](https://vst.cs.princeton.edu/).

**Imágenes:**
- _Crear_: diagrama SVG de un Hoare triple aplicado a un swap simple (~30 min).
- _Crear_: comparison side-by-side de un loop con/sin invariante anotado (~30 min).
- _Crear_: opcional, tabla resumen de Hoare logic, wp, separation logic (~45 min).

**Tags propuestos:** `['Hoare logic', 'Dijkstra', 'separation logic', 'verificacion', 'imperativo']`

**Estado actual:** sólo título — uno de los posts más exigentes de toda la grilla.

