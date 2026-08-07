### A1-06 — PostScript como servidor web

- **Archivo seed:** `dev/postscript-web-server.md`
- **Slug propuesto:** `postscript-como-servidor-web`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-postscript-como-servidor-web.md`
- **Serie:** A1
- **Cross-links:** depende de [[A1-03]] (Forth, antecesor directo); lleva a [[A1-05]] (Clipper como servidor — el mismo absurdo en otro lenguaje)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
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

_Todas las URLs de abajo fueron fetcheadas y confirmadas en la pasada de fuentes del 2026-07-15, salvo donde se aclara lo contrario._

**El servidor (fuente primaria del post):**
- [Anders Karlsson, *PS-HTTPD* V1.6 — código fuente `ps-httpd.ps`](https://raw.githubusercontent.com/gmork2/PS-HTTPD/master/ps-httpd.ps) — **estable** (raw.githubusercontent). Cabecera verbatim: `% PS-HTTPD V1.6 / % Copyright 2000-2010 Anders Karlsson, pugo@pugo.org / % License: GNU General Public License`. Ésta es la fuente a transcribir. El repo: [gmork2/PS-HTTPD](https://github.com/gmork2/PS-HTTPD) (mirror de terceros; sólo contiene `README` y `ps-httpd.ps`) — **frágil** (es un mirror, no el sitio del autor).
- [Slashdot, *Httpd Written In Postscript? Shell?*, 2000-04-21](https://slashdot.org/story/00/04/21/1838216/httpd-written-in-postscript-shell) — **estable**. **Fuente clave**: documenta la línea de inetd con la que se lo corre: `8080 stream tcp nowait nobody /usr/bin/gs gs -dNODISPLAY -q` + el path al `.ps`. Un comentarista señala que es «trampa» porque requiere Ghostscript en vez del motor PostScript de una impresora — ese matiz vale para el post.
- [Hacker News — *PS-HTTPD is a web server written in PostScript* (2010)](https://news.ycombinator.com/item?id=1728381) — **frágil**. La URL enviada era `http://www.pugo.org/main/project_pshttpd/` (sitio del autor). Un usuario reporta haberlo corrido con `gs`.
- [Ghostscript, *Using Ghostscript* (documentación oficial)](https://ghostscript.readthedocs.io/en/latest/Use.html) — **frágil** (`/en/latest/` se mueve con cada release); backup: [snapshot Wayback 2026-07-06](http://web.archive.org/web/20260706165746/https://ghostscript.readthedocs.io/en/latest/Use.html) (la API de disponibilidad devuelve `status: 200`). Verifica dos piezas de la línea de inetd: `-q` = «Quiet startup: suppress normal startup messages, and also do the equivalent of -dQUIET», y que se le puede pedir a Ghostscript que lea PostScript de entrada estándar — textual: «These are not really switches: they tell Ghostscript to read from standard input, which is coming from a file or a pipe, with or without buffering». ⚠️ **`-dNODISPLAY` no figura en esa página** — el resto de la línea de inetd sigue apoyado sólo en el hilo de Slashdot.

**PostScript: historia y diseño (fuentes primarias / institucionales):**
- [Computer History Museum, *PostScript: A Digital Printing Press*](https://computerhistory.org/blog/postscript-a-digital-printing-press/) — **estable**. Adobe fundada en diciembre de 1982 por Chuck Geschke y John Warnock; PostScript creado hacia fines de 1984; equipo liderado por Warnock con Geschke, Doug Brotz, Bill Paxton y Ed Taft. Cita textual: «The language they created was in fact a complete programming language, named PostScript.»
- [CHM — *Warnock, John oral history part 1 of 2*, cat. 102738759](https://www.computerhistory.org/collections/catalog/102738759) — **estable**. Entrevistado por David C. Brock, 26 de abril de 2018. Warnock relata JaM, Interpress y la salida de Xerox PARC.
- [CHM, press release: liberación del código fuente de PostScript, 2022-12-01](https://computerhistory.org/press-releases/computer-history-museum-makes-adobe-postscripts-source-code-available-to-the-public-as-a-part-of-its-art-of-code-series/) — **estable**. El código liberado es una versión temprana (fines de febrero de 1984).
- [Brian Reid, *PostScript and Interpress: a comparison*, fa.laser-lovers, 1985-03-01](https://groups.google.com/g/fa.laser-lovers/c/H3us4h8S3Kk/m/-vGRDirzDV0J) — **frágil** (Google Groups). **La fuente más precisa sobre el linaje**: JaM = «John And Martin» (Warnock + Newell), con «postfix execution semantics», basado en el modelo de imagen de Evans & Sutherland; y The Design System de John Gaffney (~1975) combinaba «the execution semantics of the Burroughs machines with the evolving Evans and Sutherland imaging models». Nótese: **Burroughs, no Forth**. Ojo con la fecha: el code study de abajo lo cita como «Reid 1988», pero el posteo original es de 1985 — verificar cuál se cita antes de publicar.
- [Tekla S. Perry, *Inventing PostScript*, IEEE Spectrum, 1988-05-01](https://spectrum.ieee.org/adobe-postscript) — **frágil** (paywall blando). Design System liberado por E&S en 1977, «interactive, stack-oriented architecture»; Warnock en E&S 1971-1977; JaM con Newell en PARC en 1978; Interpress terminado en 1981; Adobe incorporada en diciembre de 1982. Menciona Forth **sólo como comparación** («as complete and flexible a programming language as Pascal or C or Forth»), no como influencia.
- [Jeffrey Starr, *PostScript 1.0 — A Code Study*, 2024-09-26](https://ztoz.blog/posts/postscript-code/) — **frágil** (blog personal). Estudio serio de los ~12.000 líneas de C liberadas por CHM. Traza el linaje Gaffney → Design System → JaM → Interpress → PostScript. **No menciona Forth ni una sola vez.**

**Referencia del lenguaje:**
- Adobe Systems Inc., *PostScript Language Reference*, 3.ª ed., Addison-Wesley Professional, 8 de marzo de 1999, ISBN 0-201-37922-8 — la referencia oficial (el «Red Book»). Ficha verificada en [InformIT](https://www.informit.com/store/postscript-language-reference-9780201379228) — **estable**. ⚠️ El PDF que Adobe publica en `https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf` **no pudo verificarse**: dos fetches dieron timeout (son ~7,5 MB). Aparece con el título correcto en resultados de búsqueda, pero no lo abrí — confirmar a mano antes de linkearlo.
- [Internet Archive — *PostScript language reference manual*, Addison-Wesley 1988, 12.ª impresión, ISBN 0-201-10174-2](https://archive.org/details/postscriptlangua00adob) — **estable**. Préstamo digital controlado. Ojo: es la **1.ª edición**, no la 3.ª que se cita arriba. [Otra copia (ed. 1985)](https://archive.org/details/postscriptlangua0000unse_c7i6) — **estable**, también préstamo controlado.
- [Internet Archive — *PostScript language reference manual*, Ed Taft, Addison-Wesley 1990, ISBN 0-201-18127-4](https://archive.org/details/postscriptlangua0000taft) — **estable**, préstamo digital controlado. Hallazgo de esta pasada: es la copia más cercana a la 3.ª edición que hay libre, pero **no es la 3.ª** (1999) — la ficha de archive.org no declara número de edición, así que no le pongo uno. Otros nombres asociados en la ficha: Jeff Walden, Paul Engstrom, Adobe Systems.
- [Don Lancaster, *Guru's Lair PostScript Library*](https://www.tinaja.com/post01.shtml) — **frágil** (sitio personal). Se autodescribe como «one of the world's foremost collections of raw PostScript-as-language demos, utilities, and applications» — el encuadre «PostScript-as-language» es exactamente la tesis del post.
- Henry McGilton y Mary Campione, *PostScript by Example*, Addison-Wesley, 1992, ISBN 0-201-63228-4 — [copia en Internet Archive](https://archive.org/details/postscriptbyexam00mcgi) — **estable**, préstamo digital controlado.

**Contexto:**
- [Ed Post, *Real Programmers Don't Use PASCAL*, Datamation vol. 29 n.º 7, julio de 1983, pp. 263-265](https://homepages.inf.ed.ac.uk/rni/papers/realprg.html) — **frágil** (página de cátedra, Univ. de Edimburgo), pero es la copia que sí abre: la de `pbm.com/~lindahl/` que estaba antes en esta bibliografía **tiene el certificado TLS vencido**. ⚠️ **No menciona PostScript en ningún lado** (ver corrección abajo).
- [Linux kernel — *USB Printer Gadget Driver*](https://www.kernel.org/doc/html/v5.7/usb/gadget_printer.html) — **estable** (kernel.org). Textual: «This driver may be used if you are writing printer firmware using Linux as the embedded OS.» Es la evidencia más concreta que encontré de que existe firmware de impresora sobre Linux — pero no sostiene «*tu* impresora corre Linux» (ver marca abajo).
- [Red Hat, press release *Red Hat's Open Source Embedded OS to Power Post-PC Printer Device from Brother*, Raleigh, 13 de marzo de 2000](https://www.redhat.com/en/about/press-releases/press-postpc) — **estable** (redhat.com). Hallazgo de esta pasada, y va **en contra** del hook: Brother eligió **eCos**, no Linux, para el firmware de sus láser «HL-2400CeN & HL-3400CN». Sirve como contrapunto honesto: el firmware de impresora es un SO embebido completo, pero no necesariamente Linux.
- [PostScript en Wikipedia](https://en.wikipedia.org/wiki/PostScript) — contexto, no cita primaria (regla de la casa). Su infobox dice «Influenced by: Mesa, Interpress, Lisp, FORTH», pero ninguna fuente primaria lo respalda; además el propio artículo se contradice al atribuir JaM a «John Gaffney and Martin Newell» (CHM y Reid dicen Warnock + Newell — «John And Martin»).

**Descartadas en esta pasada (no usar):**
- `web.archive.org/.../bjbygg.com/postscript-http-server.html` — la URL que traía el borrador. **No verificable** (la herramienta no puede fetchear `web.archive.org`) y el dominio es sospechoso: el sitio del autor es `pugo.org`, no `bjbygg.com`. El título «The world's smallest HTTP server in PostScript» tampoco aparece en ninguna búsqueda. Reemplazada por el código fuente real, arriba.
- `github.com/janert/postscript-by-example` — **HTTP 404**. Y «Brendan Zabarauskas» no tiene relación alguna con PostScript: la atribución del borrador era doblemente errónea. Lo que sí existe es el libro de McGilton y Campione, arriba.
- `wiki.c2.com/?PostScriptLanguage` — no se pudo verificar el contenido (la página sirve un loader JS sin texto). Sin confirmar, no va.
- `www.pugo.org/project/pshttpd/` — sitio del autor (sería la cita preferida por regla de la casa), pero **devuelve una página sin contenido** al fetchearla. Reintentar a mano antes de publicar; sería la mejor cita si revive.
- `www.pugo.org/main/project_pshttpd/` (la URL que se envió a HN) — reintentada en la pasada del 2026-07-15: **devuelve sólo la cadena «pugo.org», sin contenido**. La API de Wayback sí reporta snapshot con `status: 200` del 2026-06-06 (`http://web.archive.org/web/20260606205349/https://www.pugo.org/main/project_pshttpd/`), pero **no pude abrirlo** (la herramienta no fetchea `web.archive.org`), así que no lo cito. Abrilo a mano: si tiene texto, ésta es la cita preferida por regla de la casa y desplaza al mirror de GitHub.
- `download.support.xerox.com/.../IGEN_150/.../Third-Party-Software-Disclosure...pdf` — **HTTP 404**.
- `support.xerox.com/en-us/content/152832` (Third Party Software Disclosure, Xerox C235) — abre, pero el «Linux» que muestra es la **plataforma soportada por el driver**, no el firmware; el disclosure real es un ZIP que no pude abrir. No sirve para la marca del hook.
- `loc.gov/preservation/digital/formats/fdd/fdd000029.shtml` (Library of Congress, ficha del formato PostScript) — **HTTP 403** al fetchear. Sería una buena fuente institucional para «PostScript es un lenguaje»; reintentar a mano.
- `www.adobe.com/content/dam/acom/en/devnet/actionscript/articles/PLRM.pdf` — segunda URL candidata para el PLRM 3.ª ed.; **también dio timeout** (mismo problema de tamaño que la URL `/jp/`). Ninguna de las dos está verificada.

**Imágenes:**
- _Crear_: screenshot del "Hello World" PostScript abierto en GhostScript (5 min).
- _Crear_: comparación side-by-side de un mismo programa en Forth y en PostScript (~20 min).

**Tags propuestos:** `['PostScript', 'Adobe', 'Forth', 'stack', 'historia']`

**Estado actual:** prosa completa escrita contra el outline (~950 palabras, dentro del target short). Lo que quedó cerrado: el encuadre («PostScript es un lenguaje, no un formato»), la comparación con Forth a nivel modelo de stack, el argumento de por qué la separación «lenguaje de propósito general» / «lenguaje para una tarea» es arbitraria, y el cierre.

Lo que queda como hueco o pendiente de verificación:

- **Huecos de César (5):** su primer contacto con PostScript; si alguna vez escribió PS a mano; si tocó Forth antes o después; el equipamiento de impresión del sector público santafesino; y la opinión final sobre si el experimento le parece chiste o argumento.
- **Código del servidor HTTP:** hay que transcribirlo textualmente del post de Anders Karlsson en Wayback. No está escrito en el borrador a propósito — no se inventa código y se lo atribuye a alguien.
- **Datos con `[VERIFICAR:]` (6):** año/autoría de PostScript y de Adobe; el linaje Forth→JaM→PostScript; la existencia real de los operadores de red que el servidor necesita y en qué intérprete; la transcripción del código de Karlsson; la afirmación del Hook sobre impresoras corriendo Linux; y el capítulo de PostScript en *Real Programmers*. Pendiente además verificar la autoría del repo de ejemplos (ver abajo).
- **Conflicto en la bibliografía:** el ítem de ejemplos modernos figura como «Brendan Zabarauskas» pero la URL apunta a `janert/postscript-by-example`. Resolver antes de publicar.


---

## Borrador de prosa

Hay un archivo que casi todos abrimos alguna vez sin darnos cuenta de lo que era. Termina en `.ps`, lo mandás a la impresora, sale una página. Uno asume que adentro hay algo parecido a lo que hay adentro de un `.jpg`: datos, coordenadas, una descripción inerte de dónde va cada mancha de tinta. Y no. Adentro de ese archivo hay un **programa**. Un programa completo, en un lenguaje Turing-completo, que la impresora ejecuta. Vos no le mandaste una página: le mandaste código, y la página fue lo que salió de correrlo.

Una vez que aceptás eso, la pregunta se hace sola. Si es un lenguaje de programación de verdad, ¿qué le impide hacer cualquier otra cosa? La respuesta es: nada. Alguien escribió un servidor HTTP en PostScript.[^karlsson] No como performance artística — como cosa que anda.

### PostScript no es un formato, es un lenguaje

Esto no fue un accidente ni un efecto colateral. Adobe lo diseñó explícitamente como lenguaje de programación, y la referencia oficial —el PLRM— está estructurada como el manual de un lenguaje, no como la spec de un formato de archivo: tiene modelo de ejecución, tipos de datos, diccionarios, alcance, manejo de errores.[^plrm] La parte de dibujar es una biblioteca. Una biblioteca enorme y hermosa, pero una biblioteca: `moveto`, `lineto`, `show`, `showpage` son operadores como cualquier otro, apilados encima de un núcleo que no sabe nada de tinta.

Los datos: Chuck Geschke y John Warnock fundaron Adobe en diciembre de 1982, después de irse de Xerox PARC; PostScript fue el primer producto de la empresa y estuvo listo hacia fines de 1984. El equipo lo lideró Warnock, con Geschke, Doug Brotz, Bill Paxton y Ed Taft.[^chm] El Computer History Museum, que en 2022 publicó el código fuente original —una versión de fines de febrero de 1984—, lo dice sin vueltas: «The language they created was in fact a complete programming language, named PostScript».[^chm][^chm_src]

El «Hello World» deja el modelo a la vista:

```postscript
%!PS
/Helvetica findfont 24 scalefont setfont
72 700 moveto
(Hello, world) show
showpage
```

Leelo de izquierda a derecha, no como una frase sino como una secuencia de empujones. `/Helvetica` se apila. `findfont` la saca y deja el objeto font. `24` se apila. `scalefont` saca dos cosas y deja una. `setfont` la consume. No hay paréntesis de llamada, no hay argumentos con nombre: hay una pila y operadores que la comen y la alimentan.

> 🕳️ **HUECO — necesita a César:** ¿Cuál fue tu primer contacto con PostScript — impresora, Ghostscript, un `.ps` que te llegó por mail, la facultad? ¿Y te enteraste ahí de que era un lenguaje o mucho después?

> 🕳️ **HUECO — necesita a César:** ¿Alguna vez escribiste PostScript a mano (aunque sean diez líneas para probar algo), o siempre lo consumiste generado por otro programa?

### Es Forth con dibujos

Si venís de leer sobre Forth [[A1-03]], nada de esto te resultó raro. Es el mismo modelo: notación posfija, una pila de operandos, un diccionario donde las palabras se buscan por nombre, y la posibilidad de definir palabras nuevas que son indistinguibles de las primitivas. Cambian la notación y el vocabulario; el motor es el mismo.

Ahora: **el parecido es real, pero el parentesco no.** La genealogía de PostScript está documentada y Forth no aparece en ella. La línea es otra: John Gaffney, en Evans & Sutherland, escribió un intérprete de stack para el simulador del puerto de Nueva York; de ahí salió The Design System (E&S, ~1975-77), que —en palabras de Brian Reid— combinaba «the execution semantics of the Burroughs machines with the evolving Evans and Sutherland imaging models».[^reid] Warnock trabajó seis años en E&S, se llevó el modelo a Xerox PARC y en 1978 lo rehízo con Martin Newell: JaM, por «John And Martin», ya con semántica posfija.[^reid][^spectrum] JaM desembocó en Interpress (1981), e Interpress —y la frustración con Xerox— en PostScript.[^chm]

O sea que la notación posfija de PostScript no baja de Forth: baja de las máquinas de pila de Burroughs, por otra rama del mismo árbol. Son primos, no padre e hijo. Chuck Moore y John Warnock llegaron a la misma idea porque la idea estaba en el aire de la época —y en el hardware—, no porque uno copiara al otro.

> ⚠️ **Corrección de la pasada de fuentes (2026-07-15):** el borrador afirmaba que había que chequear si Forth es «el antecesor directo». Se chequeó: **no lo es, y ninguna fuente primaria lo sostiene.** El estudio serio del código fuente 1.0 liberado por CHM no menciona Forth ni una vez;[^ztoz] IEEE Spectrum lo menciona sólo como término de comparación, no como influencia;[^spectrum] Reid traza la ejecución posfija a Burroughs.[^reid] La única fuente que dice «influenced by FORTH» es el infobox de Wikipedia, sin cita — y ese mismo artículo se equivoca atribuyendo JaM a «John Gaffney and Martin Newell». Ver `Estado actual:` — esto afecta el Concepto y el cross-link a [[A1-03]].

La diferencia práctica está en el diccionario, no en el modelo. Forth te da un lenguaje desnudo y espera que lo pueble el que lo usa. PostScript te lo entrega con todo el vocabulario de tipografía y curvas de Bézier ya adentro. Eso es lo que hace que uno lo confunda con un formato: viene tan cargado hacia una tarea que la tarea tapa al lenguaje.

> 🕳️ **HUECO — necesita a César:** ¿Conociste Forth antes o después de PostScript? La transición del post cambia según cuál te explicó al otro.

### El servidor

El experimento existe: un servidor HTTP mínimo escrito enteramente en PostScript.[^karlsson] La mecánica conceptual cierra sin trucos. Los archivos `.ps` son texto plano. El lenguaje tiene operadores de archivo y de string —`file`, `readline`, `writestring`, `token`— es decir, puede leer una request, cortarla, decidir, y escribir bytes de vuelta. Y una respuesta HTTP no es más que un string bien armado.[^plrm]

Y acá hay que ser honesto con el detalle que hace toda la diferencia, porque es donde el chiste se vuelve interesante en vez de tramposo: **PS-HTTPD no abre ningún socket.** No puede: el lenguaje no tiene con qué. Lo que hace es leer de `%stdin` y escribir a `%stdout`, como cualquier filtro Unix de 1975:

```postscript
/stdin (%stdin) (r) file def
/stdout (%stdout) (w) file def
```

La red se la pone otro. Se lo corre desde `inetd`, que acepta la conexión TCP, la cablea a los descriptores estándar de un Ghostscript y deja que el programa PostScript hable HTTP por ahí:

```
8080 stream tcp nowait nobody /usr/bin/gs gs -dNODISPLAY -q ...
```

Ésa es la línea que circuló cuando Slashdot lo levantó, en abril de 2000.[^slashdot] Un comentarista de entonces marcó la objeción justa: es «trampa», porque corre sobre Ghostscript y no sobre el motor PostScript de una impresora de verdad.[^slashdot] Tiene razón, y conviene decirlo antes de que lo diga el lector. Pero fijate qué poco le concede: el parsing del request, la decisión de ruta, el manejo de MIME types, la construcción del header, el chequeo de `..`, las conexiones persistentes de HTTP/1.1 — todo eso está escrito en PostScript.[^karlsson] `inetd` sólo aporta el caño. El lenguaje hace el trabajo.

Mi detalle favorito del código es un comentario que revela lo cerca que está todo esto de salirse de control:

```postscript
% Redefine handleerror in errordict to quit on all errors.
% Otherwise it will be possible to telnet and get a postscript-prompt
```

Karlsson tuvo que romper el manejo de errores a propósito. Si no, un request malformado te dejaba caer en el prompt interactivo del intérprete — es decir, cualquiera con `telnet` conseguía un REPL de PostScript con los permisos del server. Es la mejor prueba de la tesis del post: el «formato de impresión» tenía un intérprete vivo adentro, esperando.

[VERIFICAR: transcribir el código completo del servidor desde la fuente ya localizada —`https://raw.githubusercontent.com/gmork2/PS-HTTPD/master/ps-httpd.ps`, PS-HTTPD V1.6, © 2000-2010 Anders Karlsson <pugo@pugo.org>, GPL— y elegir qué fragmentos van al post. Los snippets de arriba están verificados contra esa fuente, pero el bloque largo hay que copiarlo textual, con atribución y nota de licencia GPL. NO reconstruir de memoria. Pendiente además: decidir si se pide permiso a Karlsson o si basta con la atribución GPL.]

### Por qué nadie lo haría hoy

Por las razones aburridas, y está bien que sean aburridas. El rendimiento de un intérprete de stack diseñado para páginas no compite con nada moderno. El ecosistema no existe: no hay librerías, no hay TLS, no hay comunidad a quien preguntarle. Y el sandboxing es al revés de lo que necesitás — el lenguaje fue pensado para correr código arbitrario que le llega de afuera y dibujarlo, que es exactamente el modelo de amenaza que un servidor no quiere.

[VERIFICAR: la afirmación del hook de que «tu impresora corre Linux». **Parcialmente sostenida, no del todo.** Lo mejor que encontré es la doc del kernel sobre el *USB Printer Gadget Driver*, que dice textual: «This driver may be used if you are writing printer firmware using Linux as the embedded OS»[^kernel] — o sea, kernel.org confirma que existe firmware de impresora sobre Linux, pero no que *tu* impresora lo tenga. Dónde busqué sin resultado: HPLIP y el portal de developers de HP (es el driver del host, no el firmware de la impresora — no sirve para esto); la wiki de printer-freedom de Trisquel y el artículo de Hackaday sobre por qué no hay firmware libre de impresoras (ambos van en la dirección contraria: subrayan que el firmware es propietario y cerrado). Falta probar: los avisos de licencias open-source que los fabricantes publican por obligación de la GPL (buscar «open source software notice» + modelo, en los sitios de soporte de HP/Brother/Xerox) — ahí saldría el kernel Linux listado si está. **Si no aparece, suavizar el hook a «muchas impresoras de red hoy corren un sistema operativo completo»** — que sí es defendible con la cita del kernel. Ojo: el hook es de César, no lo reescribo yo.]

> 🕳️ **HUECO — necesita a César:** ¿Te tocó administrar impresoras PostScript en la STG o en el Ministerio de Cultura de Santa Fe? Si sí, ¿qué eran esos equipos y qué se rompía?

### La lección

Lo que me interesa de esto no es el chiste. Es que «lenguaje de propósito general» y «lenguaje para una tarea» describen mucho menos de lo que creemos. PostScript quedó del lado de los lenguajes-para-una-tarea, y esa clasificación no está en el lenguaje: está en la biblioteca que le pusieron encima, en el ejecutable donde lo empaquetaron, y en la costumbre. Adentro es tan de propósito general como cualquiera. La frontera no la trazó la teoría, la trazó el marketing.

Y una vez que ves eso en PostScript, empezás a verlo en todos lados: SQL, CSS, la hoja de cálculo, las macros de tu editor. La misma historia — un lenguaje completo disfrazado de herramienta, que espera a que a alguien se le ocurra la barbaridad correcta. En este blog eso ya pasó una vez con Clipper [[A1-05]], que es exactamente el mismo absurdo en otro idioma.

> 🕳️ **HUECO — necesita a César:** ¿Cuál es tu veredicto final: es un chiste con moraleja o un argumento serio contra la taxonomía de lenguajes? El cierre necesita tu opinión, no la mía.

Hay una tradición vieja de reírse de esto. *Real Programmers Don't Use PASCAL*, el clásico que Ed Post publicó en Datamation en julio de 1983, es el catecismo del género:[^realprog] el Programador de Verdad usa la herramienta que tiene a mano para lo que se le canta, y la taxonomía de lenguajes le importa poco. Y la broma siempre es la misma: el que escribe un programa serio en el lenguaje equivocado no está confundido. Entendió algo que el resto todavía está mirando de reojo.

> ⚠️ **Corrección de la pasada de fuentes (2026-07-15):** el borrador decía que *Real Programmers* «le dedica un pasaje al asunto» de PostScript. **Es falso, y era imposible:** el ensayo se publicó en Datamation vol. 29 n.º 7, julio de 1983, pp. 263-265 — más de un año **antes** de que PostScript saliera al mercado (1984). Fetcheé el texto completo y la palabra «PostScript» no aparece ni una vez; los lenguajes que discute son FORTRAN, PASCAL, assembler, COBOL, Ada, C, BASIC, PL/I, APL, LISP, RATFOR y MORTRAN.[^realprog] Reescribí la frase para citar el ensayo por lo que sí dice (el espíritu general), sin atribuirle un pasaje inexistente. **Si preferís sacarlo del todo, sacalo** — el párrafo cierra igual sin él.

[^plrm]: [Adobe Systems Inc., *PostScript Language Reference*, 3.ª ed., Addison-Wesley 1999](https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf).
[^karlsson]: [Anders Karlsson, *The world's smallest HTTP server in PostScript*](https://web.archive.org/web/20120607013010/http://www.bjbygg.com/postscript-http-server.html) — copia archivada en Wayback; el original ya no responde.
[^realprog]: [*Real Programmers Don't Use PASCAL*](https://www.pbm.com/~lindahl/real.programmers.html).
