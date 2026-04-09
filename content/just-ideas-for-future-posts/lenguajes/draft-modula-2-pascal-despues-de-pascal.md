### A1-04 — Modula-2: Pascal después de Pascal

- **Archivo seed:** `dev/draft-modula2.md`
- **Slug propuesto:** `modula-2-pascal-despues-de-pascal`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-modula-2-pascal-despues-de-pascal.md`
- **Serie:** A1
- **Cross-links:** lleva a [[A1-03]] (Forth, otro lenguaje para "una persona"), [[E-08]] (libros que me hicieron programador, donde aparece *Algorithms + Data Structures = Programs*)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** medium (1200-1500 palabras)

**Concepto:** Modula-2 es lo que Wirth hizo después de Pascal cuando se dió cuenta de que Pascal tenía problemas reales para programar en grande. Módulos de verdad, separación clara interface/implementación, coroutines. La pregunta del post: ¿por qué este lenguaje, que era objetivamente mejor que Pascal y anterior a Ada, no ganó?

**Hook:** abrir con la portada del libro de Wirth de 1982. Después: "Pascal era para enseñar; Modula-2 era para construir. Y casi nadie lo usó. ¿Por qué?".

**Outline:**
1. Nicklaus Wirth y la línea Algol → Pascal → Modula → Modula-2 → Oberon. Cada lenguaje es una autocrítica del anterior.
2. Qué agrega Modula-2: módulos con interface separada, coroutines, types low-level controlados.
3. Su uso real: el sistema operativo Lilith, la mayor parte del libro *Algorithms + Data Structures = Programs* de Wirth.
4. Por qué perdió frente a C/C++: timing, free compilers, C era "suficientemente rápido" y ya estaba en Unix.
5. Lecciones para hoy: la cantidad de cosas modernas (Go, Rust modules, etc.) que terminaron pareciéndose a Modula-2.

**Bibliografía:**
- [Niklaus Wirth, *Programming in Modula-2*, Springer-Verlag 1982 (4.ª ed. 1988)](https://archive.org/details/programminginmod0000wirt) — el libro canónico, en archive.org.
- [*Algorithms + Data Structures = Programs*, Wirth 1976](https://archive.org/details/algorithmsdatast00wirt) — el libro que la mayor parte del mundo leyó en Pascal y que Wirth reescribió en Modula-2.
- [Niklaus Wirth, *A Brief History of Software Engineering*](https://people.inf.ethz.ch/wirth/Articles/HistorySoftwareEngineering.pdf) — IEEE Annals, 2008.
- [Modula-2 en Wikipedia](https://en.wikipedia.org/wiki/Modula-2).
- [Lilith (workstation) en Wikipedia](https://en.wikipedia.org/wiki/Lilith_(computer)) — la máquina de Wirth para correr Modula-2.
- [Niklaus Wirth, *From Modula to Oberon*](https://e-collection.library.ethz.ch/eserv/eth:3210/eth-3210-01.pdf) — su autocrítica del lenguaje siguiente.
- [Computer History Museum, oral history con Wirth](https://www.computerhistory.org/collections/catalog/102746194).

**Imágenes:**
- _Wikimedia_: [Niklaus Wirth (1969)](https://commons.wikimedia.org/wiki/File:Niklaus_Wirth,_UrGU.jpg) — license: CC-BY-SA — foto canónica.
- _Wikimedia_: [Lilith workstation](https://commons.wikimedia.org/wiki/Category:Lilith_(computer)) — varias fotos disponibles.
- _Crear_: opcional — comparación side-by-side de un módulo Pascal vs Modula-2 (~30 min).

**Tags propuestos:** `['Modula-2', 'Niklaus Wirth', 'Pascal', 'Lilith', 'historia']`

**Estado actual:** sólo título.

