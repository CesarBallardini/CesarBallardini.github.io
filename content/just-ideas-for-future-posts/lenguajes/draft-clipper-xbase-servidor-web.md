### A1-05 — Clipper, xBase y los servidores web que no debían existir

- **Archivo seed:** `dev/draft-clip-web-server.md` + `dev/draft-clip.md` (consolidados — el mismo tema desde dos ángulos)
- **Slug propuesto:** `clipper-xbase-servidor-web`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-clipper-xbase-servidor-web/index.md`
- **Serie:** A1 — cross con [[H-04]] (migración COBOL: la misma idea de "código viejo que sobrevive")
- **Cross-links:** lleva a [[H-03]] (FoxBase en Linux), [[E-01]] (cómo llegué al software libre)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
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

**Estado actual:** prosa completa escrita sobre el outline existente (~1.750 palabras, dentro del target medium). Lo que quedó escrito: el encuadre de xBase y por qué dominó LATAM, la torre de hacks Clipper → librerías → DOS extender, el argumento de por qué un servidor HTTP en Clipper era razonable bajo CGI, el estado actual con Harbour y el cierre sobre el «código de barrio».

Lo que quedó como hueco y bloquea la publicación:

- **El hook es autobiográfico y no está respaldado por el draft.** El post promete «el bingo del barrio se manejaba con Clipper, y cuando había que conectarlo a la web alguien escribió un servidor HTTP en Clipper». La bibliografía no sostiene esa anécdota y no hay nada en el seed que diga si César lo vivió, lo vio, o lo escuchó. Toda la apertura y el cierre dependen de que él conteste eso. Son los huecos 1 a 4.
- Huecos menores sobre su propia relación con xBase (qué producto usó, en qué contexto), sobre si hizo o vio una migración a Harbour, y sobre el cruce con [[H-03]] (FoxBase en Linux) que el draft ya declara.
- Varios `[VERIFICAR:]` sobre fechas, versiones, propietarios sucesivos de Clipper y detalles del DOS extender: son cosas que las fuentes de la bibliografía probablemente confirmen, pero no las afirmo de memoria.

Pendiente además: las dos imágenes a crear (screenshot de Harbour compilando, diagrama del flujo CGI) y chequear que el link del CA-Clipper FAQ siga vivo — es frágil y conviene dejar copia en Wayback.

---

## Borrador de prosa

Hay una categoría de software que no aparece en ninguna retrospectiva de la industria, que nunca tuvo una conferencia con luces de colores, y que sin embargo facturó la mitad de los comercios de este país durante quince años. Se llamaba Clipper.

> 🕳️ **HUECO — necesita a César:** El hook del draft dice «el bingo del barrio se manejaba con Clipper, y cuando había que conectarlo a la web alguien escribió un servidor HTTP en Clipper». ¿Esto lo viviste vos, lo viste en un cliente, o te lo contaron? Necesito saber qué tipo de frase puedo escribir: «me acuerdo de», «me contaron que», o «circulaba la historia de».

> 🕳️ **HUECO — necesita a César:** Si fue algo que viste de cerca: ¿qué era exactamente el sistema (bingo, club, comercio), en qué años, y qué hacía la parte web — consultar algo, cargar algo, publicar resultados?

Voy a contarte por qué eso, que hoy suena a chiste o a cuento de terror, en su momento era una decisión bastante razonable. No «entendible dado el contexto», que es la forma piadosa de decir que estaba mal. Razonable de verdad, con un argumento técnico atrás que todavía se sostiene.

### Qué era xBase y por qué se comió LATAM

xBase no es un lenguaje: es una familia.[^xbase] Arranca con dBase, sigue con un montón de productos que copiaron su sintaxis y su formato de archivo — Clipper, FoxBase, FoxPro — y todos comparten dos cosas: el `.DBF` como formato de tabla en disco y un dialecto de comandos que hoy leés y parece inglés de manual de electrodoméstico. `USE clientes`, `SET INDEX TO apellido`, `SEEK "GONZALEZ"`, `BROWSE`. Escribías cinco líneas y tenías un ABM funcionando.

Clipper, específicamente, era un compilador.[^clipper] Esa es la diferencia que importa. dBase interpretaba; Clipper te tomaba el mismo código fuente y te escupía un `.EXE` de DOS. Para el que vendía sistemas, eso significaba dos cosas enormes: el cliente no necesitaba comprar una licencia del entorno, y el cliente no podía leer tu código. Vendías un ejecutable y una carpeta de `.DBF`. Se instalaba copiando archivos.

Por qué dominó acá y no tanto en otros lados es una mezcla de tres factores, y ninguno es técnico del todo. El primero es el precio: no había runtime que licenciar por puesto. El segundo es que la curva de aprendizaje era casi plana para alguien que ya sabía manejar una planilla y entendía qué era un registro. El tercero, y creo que el más subestimado, es que había una comunidad hispanohablante gigantesca — libros, revistas, cursos de academia de barrio — en una época en que la documentación en inglés era una barrera real.

[VERIFICAR: si hay algún dato duro sobre penetración de Clipper/xBase en América Latina, o si esto queda como observación mía sin número. Revisar el artículo de Wikipedia de Clipper y el CA-Clipper FAQ; si no hay cifras, escribirlo explícitamente como impresión personal y no como hecho.]

> 🕳️ **HUECO — necesita a César:** ¿Vos usaste xBase profesionalmente? ¿Cuál — dBase, Clipper, FoxBase, FoxPro — en qué años y para qué tipo de sistema? Alcanza con dos frases; quiero poder decir «yo escribí X» en vez de escribir todo el post en tercera persona.

### La torre de hacks

Acá se pone bueno. Clipper era un compilador de DOS, y DOS tenía el problema que tenía: 640 KB de memoria convencional y un modelo de direccionamiento de 16 bits. Un sistema de facturación serio no entra ahí. La solución de la época fue el *DOS extender*: una capa que ponía al procesador en modo protegido, te daba acceso al resto de la RAM, y seguía dejándote llamar a los servicios de DOS como si nada hubiera pasado.[^extender]

Clipper terminó apoyado en esa torre. Abajo del todo, el DOS extender. Arriba, el runtime de Clipper. Arriba, tus fuentes `.PRG` compiladas. Y en el medio, pegando todo, las librerías de terceros — porque el Clipper de fábrica no traía casi nada de interfaz de usuario decente, y toda la industria terminó comprando o pirateando algún paquete de ventanas y menúes. SuperLib era uno de los que circulaban.[^superlib]

[VERIFICAR: la cadena exacta que el draft anota — «Clipper → SuperLib → fuentes Borland C → DOS extender → GCC». ¿De dónde sale la parte de las fuentes Borland C y GCC? ¿Es sobre Clipper original o sobre Harbour? Chequear contra el CA-Clipper FAQ y la documentación de Harbour antes de afirmar la cadena.]

[VERIFICAR: qué DOS extender usaba Clipper y en qué versión aparece. El draft menciona Phar Lap y DJGPP genéricamente vía el artículo de Wikipedia sobre DOS extenders, pero no confirma cuál usaba Clipper.]

[VERIFICAR: la historia corporativa de Clipper — quién lo creó, la sucesión de dueños hasta Computer Associates, y las fechas de las versiones (Summer '87, 5.x). Está en el artículo de Wikipedia; hay que leerlo y citar, no escribirlo de memoria.]

El punto no es la nostalgia por el hack. El punto es que esa torre funcionaba, y que la gente que la sostenía no la vivía como una torre. Vos escribías `USE clientes` y andaba. Toda la complejidad estaba abajo, empaquetada, y era problema de otro. Es exactamente la misma sensación que tenés hoy escribiendo tres líneas de un framework arriba de un contenedor arriba de un orquestador. La torre no desapareció; cambió de nombre.

### Por qué un servidor web en Clipper no era una locura

Ahora sí, la pregunta del título. Estamos en la segunda mitad de los 90, tenés un sistema Clipper en producción, funcionando, con años de reglas de negocio adentro, y alguien te pide que eso se vea desde la web.

Pensalo desde el modelo de ejecución de la época. CGI, que era *el* estándar, funcionaba así: llega un request HTTP, el servidor levanta un proceso nuevo, le pasa los parámetros por variables de entorno y por entrada estándar, el proceso escribe HTML en la salida estándar y termina. Un proceso por request. Fork, ejecutar, morir.

Ahora mirá qué es un programa Clipper: un `.EXE` que arranca, abre unos `.DBF`, hace lo suyo, imprime, y termina. Es *exactamente* la forma de un proceso CGI. No hay que reescribir el modelo mental: ya lo tenés. La lógica de negocio ya está compilada ahí adentro, ya sabe leer esas tablas, ya sabe respetar los índices. Lo único que hay que cambiar es a dónde va la salida: en vez de dibujar una pantalla de texto, escribir HTML.

Y el acceso a datos era directo. Nada de un motor de base de datos con un puerto, un usuario, un pool de conexiones. El `.DBF` es un archivo en el disco; abrís, buscás por el índice, leés el registro. Para el volumen de un comercio o un club, eso es infinitamente más rápido de poner en marcha que montar un servidor de base de datos.

Cuando lo mirás así, «servidor web en Clipper» deja de ser una aberración y pasa a ser lo más conservador que podías hacer: reusar el código que ya funcionaba y ya estaba pago, cambiándole el dispositivo de salida. La alternativa era reescribir años de reglas de negocio en un lenguaje que nadie del equipo sabía, para ganar qué exactamente.

> 🕳️ **HUECO — necesita a César:** ¿Sabés si lo que viste era un CGI en Clipper (un `.EXE` por request, detrás de Apache o similar) o un servidor HTTP propiamente dicho, escrito en Clipper, que escuchaba el socket? Son dos cosas muy distintas y el post cambia bastante según cuál sea. Si no te acordás, decímelo y escribo las dos variantes.

> 🕳️ **HUECO — necesita a César:** Si hubo alguna complicación memorable — bloqueo de archivos con varios procesos concurrentes sobre el mismo `.DBF`, índices que se corrompían, algo así — contámela. Es el tipo de detalle que hace creíble todo el resto.

### Hoy: Harbour

La historia no terminó en los 90. Existe Harbour, que es una reimplementación libre de Clipper: compila el mismo código `.PRG`, corre en Linux, en Windows, en 64 bits.[^harbour] Es software libre, con el repositorio público.[^harbour_github]

Eso significa que un sistema Clipper de 1996 tiene una ruta de migración que no es «reescribilo todo». Es «recompilalo». No siempre limpio — las llamadas a librerías de terceros que ya no existen son el problema real, no el lenguaje — pero la lógica de negocio pasa.

[VERIFICAR: hasta qué punto Harbour es compatible con Clipper 5.x, y qué es lo que típicamente rompe al migrar. Revisar la documentación del proyecto en harbour.github.io y el repositorio; no afirmar «compila sin cambios» sin fuente.]

> 🕳️ **HUECO — necesita a César:** ¿Alguna vez compilaste algo con Harbour, aunque sea de curiosidad? El draft pide un screenshot de Harbour compilando un Clipper viejo. Si tenés un fuente `.PRG` de la época a mano, eso vale oro para el post; si no, lo armo sintético y lo digo.

Esto engancha con [[H-03]], donde cuento lo de FoxBase en Linux, y con [[H-04]], que es la misma película con COBOL: código viejo que no se muere porque nunca hubo una razón económica para matarlo.

### Por qué sobrevive el código de barrio

El sistema del bingo, o del club, o del corralón, tenía una propiedad que ningún framework de moda tiene: lo entendía la persona que lo escribió, y esa persona vivía a doce cuadras. Cuando algo se rompía, venía y lo arreglaba. No había versión mayor que rompiera la API. No había deprecación. No había un blog post anunciando que la forma correcta de hacerlo ahora es otra.

Ese software sobrevive porque el costo de reemplazarlo siempre fue mayor que el costo de aguantarlo, y porque hacía exactamente lo que había que hacer y nada más. Los frameworks que iban a barrerlo se sucedieron unos a otros y se fueron muriendo entre ellos, cada uno seguro de ser el definitivo. El `.EXE` de Clipper sigue ahí, en una máquina abajo del mostrador, sacando el listado de socios.

> 🕳️ **HUECO — necesita a César:** El cierre necesita tu opinión, no la mía. ¿Qué pensás realmente de este software — lo mirás con cariño, con vergüenza ajena, con respeto profesional? ¿Y hay algún sistema xBase que sepas que siga en producción hoy?

[^xbase]: [xBase](https://en.wikipedia.org/wiki/XBase) — Wikipedia.
[^clipper]: [Clipper (programming language)](https://en.wikipedia.org/wiki/Clipper_(programming_language)) — Wikipedia. Ver también [The CA-Clipper FAQ](http://www.itlnet.net/programming/program/Reference/clipfaq.htm) y el archivo del newsgroup [comp.lang.clipper](https://groups.google.com/g/comp.lang.clipper).
[^extender]: [DOS extender](https://en.wikipedia.org/wiki/DOS_extender) — Wikipedia.
[^superlib]: [SuperLib for Clipper](https://web.archive.org/web/19980206213700/http://www.usinfo.com/superlib/) — recuperado desde el Internet Archive; el sitio original ya no existe.
[^harbour]: [Harbour Project](https://harbour.github.io/).
[^harbour_github]: [harbour/core](https://github.com/harbour/core) en GitHub.

