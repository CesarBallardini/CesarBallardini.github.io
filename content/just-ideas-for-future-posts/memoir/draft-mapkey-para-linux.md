### E-03 — mapkey para Linux: cuando el teclado no era el que vos querías

- **Archivo seed:** `dev/draft-mapkey-para-linux.md`
- **Slug propuesto:** `mapkey-para-linux`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mapkey-para-linux/index.md`
- **Serie:** E
- **Cross-links:** lleva a [[E-01]] (FOSS journey), [[I-04]] (memoria del cómputo local — teclados raros)
- **Idioma:** es
- **Madurez:** bare-seed (archivo vacío)
- **Length target:** short (800-1200 palabras)

**Concepto:** en los 90 tempranos, los teclados latinoamericanos en Linux eran un campo minado. La distribución venía con el layout norteamericano, los acentos no funcionaban, la *ñ* era un misterio, AltGr no estaba mapeado. *mapkey* era una utilidad chiquita que permitía remapear teclas; el post cuenta cómo aprendí scancodes, qué pelée con XKB, y por qué este problema pequeño me enseñó más sobre el stack de eventos que cualquier libro.

**Hook:** "querer escribir una *ñ* en Linux en 1995 era un acto de fe. El teclado no la tenía mapeada, X11 no la conocía, y para colmo cada terminal usaba su propia tabla. *mapkey* fue mi entrada al rabbit hole de los scancodes, los keycodes, las modmaps y las layout. El post cuenta esa caída y por qué hoy no la cambiaría."

**Outline:**
1. El problema: teclado latinoamericano, distro genérica, ningún acento funciona.
2. La cadena de eventos: hardware → scancode → keycode → keysym → texto. Cinco capas. Cualquier cosa puede romperse en cualquiera.
3. *mapkey* y sus primos (`loadkeys`, `setkeycodes`, `xmodmap`). Qué hacía cada uno y por qué se pisaban.
4. La aparición de XKB y por qué fue una mejora real (más allá de lo críptico que es el formato).
5. La trampa moderna: Wayland reabre todo el debate y ahora hay tres maneras incompatibles de configurar lo mismo.
6. Cierre: qué configuro hoy en una instalación nueva, en 4 líneas. Y por qué ahora funciona.

**Bibliografía:**
- [Linux console — `loadkeys` man page](https://man7.org/linux/man-pages/man1/loadkeys.1.html).
- [`xmodmap` man page](https://www.x.org/releases/X11R7.7/doc/man/man1/xmodmap.1.xhtml).
- [The XKB Configuration Guide](https://www.x.org/releases/current/doc/xorg-docs/input/XKB-Config.html).
- [Daniel Stone, *XKB and All That*](https://www.fooishbar.org/blog/xkb-design-overview/) — explicación legible de XKB.
- [Wayland — input handling](https://wayland-book.com/seat.html).
- [Wikipedia — Keyboard layout](https://en.wikipedia.org/wiki/Keyboard_layout).

**Imágenes:**
- _Crear_: diagrama de las 5 capas (hardware → scancode → keycode → keysym → texto) (~30 min).
- _Crear_: foto de un teclado latinoamericano viejo si todavía tengo uno (~10 min).

**Tags propuestos:** `['memoir', 'Linux', 'teclado', 'XKB', 'scancodes', 'i18n']`

**Estado actual:** archivo vacío; el post existe sólo como recuerdo.

