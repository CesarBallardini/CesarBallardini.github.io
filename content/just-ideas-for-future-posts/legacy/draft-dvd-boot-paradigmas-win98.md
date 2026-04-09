### H-05 — Un DVD que botea Win98 con compiladores (para la clase de Paradigmas)

- **Archivo seed:** `sysadmin/draft-dvd-boot-paradigmas.md`
- **Slug propuesto:** `dvd-boot-paradigmas-win98`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-dvd-boot-paradigmas-win98/index.md`
- **Serie:** H
- **Cross-links:** lleva a [[H-08]] (ThinStation, otro experimento de boot), [[H-09]] (UDPcast, otro DVD de instalación), [[E-01]] (FOSS journey)
- **Idioma:** es
- **Madurez:** bare-seed (1 línea: "dvd boot con win98 y los lenguajes + apuntes")
- **Length target:** medium (1200-1800 palabras)

**Concepto:** para enseñar Paradigmas de Programación en una facultad, necesitaba que cada alumno tuviera, en una máquina cualquiera, *exactamente* el mismo set de compiladores e intérpretes. Sin instalación, sin permisos, sin pelearme con el laboratorio. Solución: un DVD que booteaba Win98 (porque era el OS más liviano que aceptaba los compiladores que necesitaba) con Turbo Pascal, Turbo Prolog, gcc, miniSML, una versión chica de Smalltalk, los apuntes en HTML y un editor decente.

**Hook:** "para enseñar Paradigmas de Programación armé un DVD que boteaba Win98 con seis compiladores precargados, los apuntes del curso, y un editor. Año dos mil y pico. Cada alumno bajaba el ISO, lo grababa, lo metía en cualquier máquina del laboratorio, y tenía mi entorno *idéntico* al que yo había usado para preparar el curso. No era *cool*. Era *funcional*. Y resolvió un problema real que el laboratorio universitario no podía resolver."

**Outline:**
1. El problema: enseñar 6 paradigmas implica 6 lenguajes. Cada uno con su instalación, su versión, sus quirks. Imposible mantenerlo en máquinas compartidas.
2. Las soluciones que descarté: máquinas virtuales (demasiado pesadas para hardware del laboratorio), instalación en cuentas de usuario (sin permisos), VPS (no había wifi confiable).
3. La solución: un DVD bootable. Win98 mínimo, FAT32, todos los lenguajes copiados al disco.
4. ¿Por qué Win98 y no Linux? — honestidad: Turbo Pascal y Turbo Prolog corrían mejor ahí, los alumnos ya conocían DOS, no había problemas de drivers de teclado.
5. Los lenguajes incluidos: TP 7, Turbo Prolog, gcc (DJGPP), miniSML, Smalltalk Express, Logo, Scheme R5RS (DrScheme).
6. Los apuntes integrados — HTML simple servido por un browser local. No hacía falta internet.
7. Cómo se distribuía: imagen ISO en el FTP del campus, los alumnos la grababan en casa.
8. Lo que aprendí: la solución técnica menos elegante, si resuelve el problema, gana.
9. Cierre: ¿qué haría hoy? Una imagen Docker con todos los lenguajes. O un Codespace de GitHub. La idea sigue siendo la misma — *garantizar que el entorno es el mismo para todos*.

**Bibliografía:**
- [Turbo Pascal 7 — historia en archive.org](https://archive.org/details/Turbo_Pascal_Version_7.0_1992_Borland) — el binario sigue disponible.
- [DJGPP — DJ Delorie's GCC port to DOS](https://www.delorie.com/djgpp/).
- [DrScheme / Racket — historia](https://racket-lang.org/) — el descendiente moderno.
- [miniSML — Standard ML for educational use](https://www.smlnj.org/) — referencia.
- [Wikipedia — Live CD](https://en.wikipedia.org/wiki/Live_CD).
- [Knoppix — el live distro pionero](http://www.knoppix.org/).
- [Apuntes de Paradigmas de Programación — varias facultades argentinas](https://www.dc.uba.ar/) — referencia local frágil, citar la cátedra específica si está online.

**Imágenes:**
- _Crear_: foto del DVD físico si todavía existe (~10 min).
- _Crear_: screenshot de un boot screen recreado o el original (~20 min).
- _Crear_: tabla de los 6 lenguajes y qué paradigma enseñaba cada uno (~15 min).

**Tags propuestos:** `['legacy', 'paradigmas', 'Win98', 'DVD live', 'Turbo Pascal', 'enseñanza']`

**Estado actual:** seed de una línea; el ISO probablemente todavía exista en algún backup mío.

