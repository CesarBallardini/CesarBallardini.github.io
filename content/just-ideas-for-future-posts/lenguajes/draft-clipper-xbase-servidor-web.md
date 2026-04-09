### A1-05 — Clipper, xBase y los servidores web que no debían existir

- **Archivo seed:** `dev/draft-clip-web-server.md` + `dev/draft-clip.md` (consolidados — el mismo tema desde dos ángulos)
- **Slug propuesto:** `clipper-xbase-servidor-web`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-clipper-xbase-servidor-web/index.md`
- **Serie:** A1 — cross con [[H-04]] (migración COBOL: la misma idea de "código viejo que sobrevive")
- **Cross-links:** lleva a [[H-03]] (FoxBase en Linux), [[E-01]] (cómo llegué al software libre)
- **Idioma:** es
- **Madurez:** seed-with-sources
- **Length target:** medium (1500-2000 palabras)

**Concepto:** Clipper y xBase fueron *enormes* en los 80 y 90, especialmente en LATAM. La pregunta: ¿qué pasaba si querías hacer un servidor web sobre Clipper en 1996? Spoiler: lo hacías, funcionaba, y todavía hay sistemas en producción así.

**Hook:** "el bingo del barrio se manejaba con Clipper, y cuando había que conectarlo a la web alguien escribió un servidor HTTP en Clipper". El post es sobre ese alguien y por qué lo que parece grotesco era en realidad bastante razonable.

**Outline:**
1. Qué es xBase: dBase, Clipper, FoxPro, FoxBase. Por qué dominó LATAM (precio, idioma, simplicidad).
2. La cadena Clipper → SuperLib → fuentes Borland C → DOS extender → GCC. La torre de hacks que hacía Clipper viable en 32-bit.
3. La idea del servidor web Clipper: por qué no era una locura (CGI estándar, fork-per-request, query a DBF directo).
4. La realidad: SuperLib y librerías ad-hoc.
5. Hoy: harbour project (Clipper open-source). Cómo migrar un Clipper a Harbour sin reescribir.
6. Cierre: por qué este tipo de "código de barrio" sobrevive a los frameworks de Silicon Valley.

**Bibliografía:**
- [Clipper (programming language) en Wikipedia](https://en.wikipedia.org/wiki/Clipper_(programming_language)).
- [Harbour Project — Clipper open source](https://harbour.github.io/) y su [GitHub](https://github.com/harbour/core).
- [xBase en Wikipedia](https://en.wikipedia.org/wiki/XBase).
- [SuperLib for Clipper](https://web.archive.org/web/19980206213700/http://www.usinfo.com/superlib/) — recuperado desde Wayback (frágil).
- [The CA-Clipper FAQ](http://www.itlnet.net/programming/program/Reference/clipfaq.htm) — colección histórica.
- [comp.lang.clipper en Google Groups](https://groups.google.com/g/comp.lang.clipper) — archivo del newsgroup.
- [DOS extender — DJGPP / Phar Lap en Wikipedia](https://en.wikipedia.org/wiki/DOS_extender).

**Imágenes:**
- _Wikimedia_: [dBase III screenshot](https://commons.wikimedia.org/wiki/File:DBase_III_Plus.png) — license: CC-BY-SA, para situar la familia.
- _Crear_: screenshot de Harbour compilando un Clipper viejo (5 min). Diagrama simple del flujo CGI con un .EXE Clipper como backend (~30 min).

**Tags propuestos:** `['Clipper', 'xBase', 'Harbour', 'dBase', 'FoxPro', 'historia']`

**Estado actual:** dos seeds con notas; consolidar es trivial.

