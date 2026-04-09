### A1-06 — PostScript como servidor web

- **Archivo seed:** `dev/postscript-web-server.md`
- **Slug propuesto:** `postscript-como-servidor-web`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-postscript-como-servidor-web.md`
- **Serie:** A1
- **Cross-links:** depende de [[A1-03]] (Forth, antecesor directo); lleva a [[A1-05]] (Clipper como servidor — el mismo absurdo en otro lenguaje)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** short (700-1000 palabras)

**Concepto:** PostScript es un lenguaje de programación Turing-completo basado en stack (esencialmente Forth con dibujos). Y sí: alguien lo usó para servir páginas web. El post es sobre por qué eso *funciona conceptualmente* y qué nos enseña sobre la diferencia entre "lenguaje de propósito general" y "lenguaje para una tarea".

**Hook:** "tu impresora corre Linux, pero antes corría un lenguaje Turing-completo y hacía cosas que ni te imaginás". Mostrar el "Hello World" web server en PostScript.

**Outline:**
1. PostScript es un lenguaje de programación, no un formato. Adobe lo diseñó así a propósito.
2. Cómo se relaciona con Forth (mismo modelo de stack, otra notación).
3. El experimento: PostScript como CGI / como servidor HTTP. Existieron, no eran broma.
4. Por qué funciona: archivos PS son texto, los intérpretes son rápidos, y el lenguaje tiene `file` y `string` operators.
5. Por qué nadie lo usaría hoy: rendimiento, ecosistema, sandboxing.
6. La lección: el lenguaje "para imprimir" es un lenguaje de propósito general porque la separación es arbitraria.

**Bibliografía:**
- [Adobe Systems Inc., *PostScript Language Reference*, 3.ª ed., Addison-Wesley 1999](https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf) — la referencia oficial.
- [Don Lancaster, *PostScript: An Introduction*](https://www.tinaja.com/post01.shtml) — tutorial clásico.
- [PostScript en Wikipedia](https://en.wikipedia.org/wiki/PostScript).
- [Anders Karlsson, *The world's smallest HTTP server in PostScript*](https://web.archive.org/web/20120607013010/http://www.bjbygg.com/postscript-http-server.html) — el post original (frágil; verificar Wayback).
- [c2 wiki — PostScript](https://wiki.c2.com/?PostScriptLanguage).
- [Real Programmers don't use PASCAL — chapter on PostScript](https://www.pbm.com/~lindahl/real.programmers.html) — clásico humorístico.
- [Brendan Zabarauskas, *PostScript implementations*](https://github.com/janert/postscript-by-example) — ejemplos modernos en GitHub.

**Imágenes:**
- _Crear_: screenshot del "Hello World" PostScript abierto en GhostScript (5 min).
- _Crear_: comparación side-by-side de un mismo programa en Forth y en PostScript (~20 min).

**Tags propuestos:** `['PostScript', 'Adobe', 'Forth', 'stack', 'historia']`

**Estado actual:** sólo título, sin notas.

