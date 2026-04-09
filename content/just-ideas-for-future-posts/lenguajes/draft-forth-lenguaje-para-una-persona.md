### A1-03 — Forth: el lenguaje hecho para una sola persona

- **Archivo seed:** `dev/draft-forth-language.md`
- **Slug propuesto:** `forth-lenguaje-para-una-persona`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-forth-lenguaje-para-una-persona.md`
- **Serie:** A1
- **Cross-links:** depende de [[tr-23]] (Charles Moore en *Masterminds*); lleva a [[J-03]] (MindForth — Forth como AI), [[A2-04]] (sistemas expertos en BASIC: contraste)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** medium (1200-1500 palabras)

**Concepto:** Forth no fue diseñado para escalar equipos. Fue diseñado por Charles Moore para que una persona pueda controlar todo el sistema. Y ahí está su valor: si alguna vez te sentiste "abrumado por la complejidad innecesaria", Forth es el lenguaje que te muestra el otro extremo.

**Hook:** "lo escribió en una tarde para apuntar el telescopio del observatorio" — esa frase casi mítica resume el espíritu de Forth. Después aclaramos qué tan literal es.

**Outline:**
1. Charles Moore en una tarde, en un observatorio, controlando un telescopio. El origen real (no exageremos pero tampoco apaguemos el mito).
2. Cómo se ve un programa Forth: notación postfija, stack de datos, "palabras" definibles.
3. Por qué eso significa que en Forth podés redefinir el lenguaje mismo. El compilador es del tamaño de un párrafo.
4. La filosofía Moore: "si necesitás más de mil líneas, lo estás haciendo mal".
5. Donde sigue vivo: bootloaders (Open Firmware/OpenBoot), PostScript es básicamente Forth con dibujos, embebidos críticos.
6. Cierre: lo que Forth te enseña incluso si nunca lo vas a usar — la diferencia entre simplicidad y facilidad.

**Bibliografía:**
- [Leo Brodie, *Starting FORTH*, Prentice-Hall 1981](https://www.forth.com/starting-forth/) — el libro de iniciación canónico, libre online.
- [Leo Brodie, *Thinking FORTH*, Prentice-Hall 1984](http://thinking-forth.sourceforge.net/) — cómo *pensar* en Forth.
- [Charles Moore, *FORTH — The Early Years*](https://www.forth.com/resources/forth-programming-language/) — su propio relato.
- [Charles Moore en *Masterminds of Programming*](https://archive.org/details/MastermindsOfProgramming) — entrevista capítulo "FORTH".
- [Open Firmware / IEEE 1275](https://en.wikipedia.org/wiki/Open_Firmware) — Forth en bootloaders.
- [comp.lang.forth en Google Groups](https://groups.google.com/g/comp.lang.forth) — archivo de la comunidad.
- [Jupiter Ace en Wikipedia](https://en.wikipedia.org/wiki/Jupiter_Ace) — la microcomputadora que vino con Forth en vez de BASIC.
- [[tr-07]] (Hickey, *Simple Made Easy*) — para enlazar la idea "simple ≠ fácil" con la filosofía de Forth.

**Imágenes:**
- _Wikimedia_: [Jupiter Ace computer](https://commons.wikimedia.org/wiki/File:Jupiter_ACE.jpg) — license: CC-BY-SA — foto de la maquinita que llevaba Forth en ROM.
- _Wikimedia_: foto de Charles Moore (revisar Commons; si no, usar screenshot de su charla con atribución).
- _Crear_: SVG didáctico de un stack Forth ejecutando `2 3 + .` paso a paso (~30 min con Excalidraw).

**Tags propuestos:** `['Forth', 'Charles Moore', 'stack', 'concatenative', 'simplicidad']`

**Estado actual:** sólo título, sin notas en el seed.

