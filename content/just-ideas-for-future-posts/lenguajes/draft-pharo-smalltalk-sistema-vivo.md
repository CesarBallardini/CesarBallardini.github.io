### A1-11 — Pharo Smalltalk: el sistema vivo donde el código y el mundo son la misma cosa

- **Archivo seed (repo POC):** ninguno propio aún; el POC pedagógico vive en [github.com/CesarBallardini/ansible-devops-workstation](https://github.com/CesarBallardini/ansible-devops-workstation) (instala Pharo) y en [github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles](https://github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles) (la solución para mirar el MOOC oficial)
- **Slug propuesto:** `pharo-smalltalk-sistema-vivo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-pharo-smalltalk-sistema-vivo/index.md`
- **Serie:** A1 — el lenguaje "raro" que faltaba en la grilla original; cruza con [[A1-01]] (Kay → Smalltalk), [[A2-03]] (Y combinator vivo en Ruby — el otro post sobre lenguajes-como-entornos), [[J-05]] (la solución Rube-Goldberg para mirar el MOOC oficial)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** Smalltalk no es "un lenguaje". Es un *sistema*: una imagen de objetos vivos que persisten entre sesiones, donde editás el código *desde adentro del sistema mientras corre*, y cualquier cambio entra en efecto inmediatamente. Pharo es la implementación moderna, libre, mantenida, viva. El post explica por qué la idea de "imagen viva" es radical, qué se siente programar así por primera vez, y por qué Alan Kay (ver [[A1-01]]) sigue insistiendo en que esto es lo más cerca que estuvimos de la "revolución que no llegó".

**Hook:** "abrís Pharo. Aparece una ventana con varios paneles. Hacés click en una clase. Aparece su código. Lo modificás. Apretás Ctrl-S. Listo, ya funciona. *No compilaste nada*. *No reiniciaste nada*. El sistema entero está vivo, todo el tiempo, mientras vos escribís. Vos no programás *un programa*; vos hablás con un mundo de objetos vivos. Si nunca tuviste esa sensación, este post es para vos."

**Outline:**
1. Smalltalk en 30 segundos: Xerox PARC, los 70, Alan Kay, Adele Goldberg, Dan Ingalls. Smalltalk-80 como punto de referencia (ver [[A1-01]]).
2. Pharo en 30 segundos: la implementación moderna, fork de Squeak (2008), liderada por Stéphane Ducasse y la INRIA de Lille.
3. La idea de imagen: por qué tu *estado del sistema* persiste como un blob, en vez de regenerarse desde fuentes. Las ventajas (productividad mágica) y las desventajas (dependencia de la imagen, dificultad de versionar).
4. Las 5 clases que hay que conocer en Pharo para empezar: `Object`, `Number`, `Collection`, `String`, `Transcript`.
5. El "do it" / "print it" / "inspect it" del workspace — el REPL pero persistente.
6. El browser de clases — por qué editás clases en una ventana de 5 paneles en vez de en un archivo.
7. Lo extraño que cuesta entender al principio: que el código de Pharo *no vive en archivos*. Vive en la imagen. Los archivos son un export, no la fuente de verdad.
8. Cómo conviven Pharo y git en 2026: Iceberg, Metacello, Tonel.
9. El MOOC oficial de Pharo (FUN) y mi solución para mirarlo — cross-link [[J-05]].
10. Cierre: por qué incluso si nunca vas a programar Pharo en producción, una semana usándolo te cambia la cabeza.

**Bibliografía:**
- [Pharo — sitio oficial](https://pharo.org/).
- [*Pharo by Example* (libro libre, varias ediciones)](https://books.pharo.org/).
- [Stéphane Ducasse et al, *Deep into Pharo*, libro libre](https://books.pharo.org/deep-into-pharo/).
- [MOOC oficial de Pharo en FUN](https://www.fun-mooc.fr/en/courses/pharo-syntax-and-tools/) — el curso de Inria, gratuito.
- [Alan Kay, *The Early History of Smalltalk*, HOPL II 1993](http://worrydream.com/EarlyHistoryOfSmalltalk/).
- [Adele Goldberg & David Robson, *Smalltalk-80: The Language and its Implementation*, Addison-Wesley 1983 (el "Blue Book")](https://archive.org/details/smalltalk80imple00gold) — el libro fundacional.
- [Squeak — el ancestro libre de Pharo](https://squeak.org/).
- [Dan Ingalls, *Design Principles Behind Smalltalk*, Byte Magazine August 1981](https://www.cs.virginia.edu/~evans/cs655/readings/smalltalk.html) — el manifiesto.
- [Bret Victor, *Inventing on Principle*, CUSEC 2012](https://vimeo.com/36579366) — heredero estético de la idea de "sistema vivo".
- Cross-link [[A1-01]] para la conexión con Kay, [[J-05]] para el MOOC.

**Imágenes:**
- _Wikimedia_: foto de Alan Kay y/o Dan Ingalls — disponibles bajo CC.
- _Crear_: screenshot del Pharo browser de clases con código abierto (~15 min — esto es la imagen central del post).
- _Crear_: GIF / animación corta del "do it" en el playground (~30 min, opcional).
- _Crear_: comparación side-by-side de un pequeño programa en Pharo vs en Java/Python (~20 min).

**Tags propuestos:** `['Pharo', 'Smalltalk', 'sistema vivo', 'imagen', 'Alan Kay', 'Squeak', 'INRIA', 'lenguajes vivos']`

**Estado actual:** prosa completa escrita contra el outline de 10 puntos (≈2000 palabras, dentro del target medium). Lo que quedó cubierto: el encuadre histórico PARC/Smalltalk-80, la explicación de la imagen viva, las cinco clases de entrada, el ciclo do-it/print-it/inspect-it, el browser de clases, el problema de «el código no vive en archivos», la convivencia con git, el pase al MOOC y el cierre.

Lo que quedó como hueco (necesita a César, 8 marcadores `🕳️`): todo lo autobiográfico — el primer contacto con Pharo, la anécdota concreta del momento en que le cerró la idea de imagen, su opinión sobre Iceberg en la práctica, la motivación / el contenido / el destinatario del repo `pharo-mooc-english-audio-spanish-subtitles`, si efectivamente terminó el MOOC, el contexto de enseñanza donde usa `ansible-devops-workstation`, y la respuesta personal del cierre.

Lo que quedó marcado para verificar (6 marcadores inline): el año de Smalltalk-80, la fecha del fork de Squeak (2008) y quiénes lo iniciaron, la atribución institucional a Ducasse / Inria Lille, la genealogía Smalltalk-80 → Squeak, los nombres y roles exactos de Iceberg / Metacello / Tonel, y la formulación textual de la idea de Kay sobre «la revolución que no llegó». Nada de eso está respaldado por la bibliografía tal como está listada; hay que chequearlo en pharo.org, squeak.org, *Pharo by Example* y el Blue Book antes de publicar.

Bloqueante para publicar: los 8 huecos. Post tirado a publicar después de terminar el MOOC.

---

## Borrador de prosa

Abrís Pharo. Aparece una ventana con varios paneles. Hacés click en una clase. Aparece su código. Lo modificás. Apretás Ctrl-S. Listo, ya funciona. No compilaste nada. No reiniciaste nada. No hay un `make`, no hay un watcher, no hay un hot reload que te avisa que perdió el estado y arranca de nuevo. El sistema entero está vivo, todo el tiempo, mientras vos escribís.

Eso es lo que cuesta explicar de Smalltalk, y por eso este post existe. No vas a programar *un programa*: vas a hablar con un mundo de objetos que ya están corriendo, y que van a seguir corriendo cuando cierres los ojos. Si nunca tuviste esa sensación, seguí leyendo. Si ya la tuviste, probablemente sepas de qué hablo y no necesites que te convenza de nada.

### Smalltalk en treinta segundos

Smalltalk sale del Xerox PARC en los años setenta, del grupo de Alan Kay, con Adele Goldberg y Dan Ingalls entre los nombres centrales. La versión que quedó como punto de referencia canónico es Smalltalk-80, documentada en el libro que todo el mundo llama el *Blue Book*: Goldberg y Robson, *Smalltalk-80: The Language and its Implementation*, Addison-Wesley, 1983[^bluebook]. Si querés la historia contada por adentro y con todas las cicatrices a la vista, está *The Early History of Smalltalk* de Kay, que presentó en HOPL-II en 1993[^kay]; y si querés el manifiesto corto, el que te explica *por qué* el sistema es así y no de otra manera, es el artículo de Ingalls en Byte de agosto de 1981, escrito cuando estaba en el Learning Research Group del PARC[^ingalls].

De la parte histórica no voy a hablar mucho acá, porque ya le dediqué un post entero a Kay y a la idea que tenía en la cabeza cuando armó todo esto: [[A1-01]]. Lo que me importa hoy es lo otro. Lo que quedó vivo.

### Pharo en treinta segundos

Pharo es la implementación moderna, libre y mantenida de Smalltalk[^pharo]. El propio *Pharo by Example* lo dice con fecha y número de versión: «The Pharo project started in March 2008 as a fork of Squeak 3.9, and the first 1.0 beta version was released on July 31, 2009»[^pbe]. No fue sólo una poda técnica: parte del punto era resolver los líos de licencia de Squeak, y por eso el core de Pharo contiene únicamente código aportado bajo licencia MIT[^pbe].

Lo empezaron Stéphane Ducasse y Marcus Denker. La historia, contada por ellos mismos en el aniversario de los diez años, arranca en 2007: los dos eran mantenedores de Squeak en la Universidad de Berna, les parecía que su infraestructura estaba pesada y obsoleta, y Ducasse —que acababa de crear el equipo RMoD en Inria— invitó a Denker a rehacer las bases desde cero[^inria10]. Ducasse es director de investigación en el centro Inria Lille – Nord Europe; Denker, investigador del equipo RMoD[^inria10]. Hoy Pharo se coordina a través del consorcio Pharo, creado en 2013, y sigue recibiendo apoyo de Inria, RMOD, CNRS, UDL y Cristal, entre otros[^pharo][^inria10].

Squeak, a su vez, viene de la línea directa de Smalltalk-80: es «a re-implementation of the classic Smalltalk-80 system»[^pbe], y sus propios autores cuentan en *Back to the Future* que no arrancaron de cero sino desde la implementación de Smalltalk-80 que tenía Apple — «a gold mine of useful software» —, hasta soltarlo a la comunidad de internet en septiembre de 1996[^btf]. Si querés la genealogía completa y de primera mano, Ingalls la escribió entera en HOPL-IV: *The evolution of Smalltalk: from Smalltalk-72 through Squeak*[^hopl4]. Es decir: cuando abrís Pharo, no estás abriendo un homenaje ni una reimplementación arqueológica. Estás abriendo algo que desciende por linaje continuo de aquella cosa del PARC, y que se sigue actualizando.

La documentación de entrada es *Pharo by Example*[^pbe], libre y en varias ediciones — la vigente al escribir esto es *Pharo by Example 9*[^books]. Cuando quieras bajar un nivel — el compilador, el garbage collector, las tripas — está *Deep into Pharo*[^deep].

> 🕳️ **HUECO — necesita a César:** ¿Cuándo y cómo fue tu primer contacto con Pharo (o con Smalltalk en general)? ¿Fue por curiosidad, por el MOOC, por alguien que te lo mostró?

### La idea de imagen

Acá está el concepto único del post, y todo lo demás son consecuencias.

En casi todos los lenguajes que usás, la verdad vive en archivos de texto. Escribís fuentes, un proceso las lee, arma un mundo en memoria, corre, y cuando el proceso muere ese mundo se evapora. Volvés a arrancar y se reconstruye desde cero, desde el texto. El estado en memoria es *derivado*. Es descartable por diseño.

En Smalltalk es al revés. El sistema es un conjunto de objetos vivos en memoria — todos: tus objetos, las clases, el compilador, el editor, las ventanas abiertas, la posición del cursor — y eso se puede serializar entero a un archivo. Ese archivo es la *imagen*. Cuando la volvés a levantar, no se «reconstruye»: se despierta, exactamente donde estaba, con las ventanas donde las dejaste y el objeto que estabas inspeccionando todavía abierto.

Las clases del sistema son objetos que viven ahí adentro. El compilador es un objeto que vive ahí adentro. Cuando editás un método y lo guardás, le estás mandando un mensaje a un objeto vivo para que se modifique a sí mismo, mientras el sistema corre. No hay un «afuera» desde donde se reconstruye todo. Vos estás adentro.

La ventaja es una productividad que se siente casi ilegítima. No existe el ciclo editar-compilar-arrancar-navegar-hasta-el-estado-que-me-interesa-reproducir-el-bug. El estado que te interesa ya está ahí; lo tenés en la mano; le abrís el código y lo cambiás mientras lo mirás.

La desventaja es simétrica y es seria. Tu trabajo vive en un blob binario. Ese blob es difícil de diffear, difícil de revisar en un pull request, difícil de mergear. Y acumula mugre: cada experimento que hiciste, cada objeto huérfano, cada ventana que abriste hace tres semanas y olvidaste. La imagen es también una casa que se desordena. Buena parte de la historia técnica de Smalltalk moderno es la historia de reconciliar esa imagen viva con el mundo de los archivos versionados, y ya vamos a llegar ahí.

### Cinco clases para empezar

No necesitás aprenderte la jerarquía entera. Con cinco alcanza para el primer día:

- `Object` — la raíz. Todo hereda de acá, incluidas las clases.
- `Number` — enteros, fracciones, floats. Las fracciones son de verdad, no son floats disfrazados.
- `Collection` — la familia grande: `Array`, `OrderedCollection`, `Set`, `Dictionary`, `Bag`. Casi todo lo que hacés en Pharo es mandarle mensajes a alguna colección.
- `String` — que es una colección de caracteres, y se comporta como tal.
- `Transcript` — la consola. Es a donde le gritás cuando querés ver algo pasar.

La sintaxis entera de Smalltalk entra en una postal — y esto no es una figura mía: es como lo describe el propio Ducasse, «the instructions fit onto a postcard», contra otros lenguajes que «sometimes don't even fit onto 50 pages»[^inria10]. Mandás mensajes a objetos, y eso es todo. No hay `if` como palabra reservada; hay un mensaje `ifTrue:ifFalse:` que se le manda a un booleano. No hay `for`; hay `do:` que se le manda a una colección con un bloque. No hay operadores especiales; `+` es un mensaje. El lenguaje tiene menos reglas que casi cualquier cosa que hayas usado, y por eso la curva de aprendizaje no está en la sintaxis: está en el *sistema*.

### Do it, print it, inspect it

En el playground escribís una expresión, la seleccionás y elegís qué hacer con ella.

*Do it* la evalúa y no te muestra nada. *Print it* la evalúa y te pega el resultado ahí mismo, en el texto, como si el editor fuera una hoja de cálculo. *Inspect it* la evalúa y te abre una ventana con el objeto adentro: sus variables, sus valores, y un lugar donde podés seguir escribiendo expresiones *en el contexto de ese objeto*.

Es un REPL, sí. Pero un REPL cuyo estado no se pierde al cerrar la terminal, y donde el «resultado» no es texto impreso sino el objeto mismo, agarrable, abrible, modificable. La diferencia entre ver un `<Foo object at 0x7f...>` y tener el Foo abierto en una ventana con sus tripas a la vista es más grande de lo que parece por escrito.

> 🕳️ **HUECO — necesita a César:** ¿Te acordás del momento concreto en que la idea de imagen te hizo click? ¿Qué estabas haciendo — un inspect que te sorprendió, un cambio en caliente, un bug que arreglaste sin reiniciar? Una escena de dos o tres frases sirve.

### El browser de clases

Editás en una ventana de varios paneles: paquetes, clases, categorías de métodos, métodos, y abajo el código del método seleccionado. Al principio se siente incómodo, porque estás acostumbrado a ver un archivo con la clase entera.

Y ahí está el punto: no hay archivo. La unidad de edición en Pharo es *el método*, no el archivo. El browser no es un editor de texto con una barra lateral; es una navegación sobre objetos vivos. Cuando hacés click en una clase, no abriste un archivo: le preguntaste a un objeto-clase qué métodos tiene, y te contestó.

### Lo que más cuesta: el código no vive en archivos

Este es el punto donde se traba todo el mundo, yo incluido. Uno pasa la vida pensando que el código *es* el árbol de archivos, y que todo lo demás es una consecuencia de eso. En Pharo es al revés: el código vive en la imagen, y los archivos son un *export*. No son la fuente de verdad; son una proyección de la fuente de verdad hacia el mundo exterior, hecha para que puedas usar herramientas que no entienden de imágenes.

Cuesta soltarlo. No porque sea difícil de entender, sino porque contradice un reflejo tan viejo que ya no lo notás.

### Pharo y git en 2026

La respuesta corta es que sí, se puede, y que hoy es razonablemente normal.

La cadena de herramientas que se nombra siempre es Iceberg, Metacello y Tonel, y los tres roles están documentados:

- **Iceberg** es «the main toolset for handling VCS in Pharo», y da «tools to checkout, commit, merge and other common operations in git repositories, all directly from the image»[^iceberg]. El booklet oficial lo resume bien: en Pharo tenés una *doble* working copy — la imagen y la working copy de git — e Iceberg sincroniza las dos por detrás, de forma transparente[^booklet].
- **Metacello** es «a package management system for Smalltalk»[^metacello]: define, vía un `BaselineOf`, qué paquetes tiene el proyecto, de qué otros proyectos depende y en qué orden se cargan[^booklet].
- **Tonel** es el formato de serialización a archivos: «a file-per-class format for monticello repositories»[^tonel], y es «the preferred format for Pharo projects»[^booklet].

Una precisión sobre Tonel, porque es fácil contarlo mal: el motivo de diseño que documentan no es «que los diffs sean legibles» sino que sea *amable con el sistema de archivos y con Windows* — «It has been designed to be Windows and file system friendly»[^booklet]. Que el código se lea mejor fuera de Pharo y que haya menos archivos (uno por clase en vez de uno por método) es consecuencia, no la bandera.

> **Nota de la pasada de fuentes (2026-07-15):** el draft original decía que Tonel estaba «pensado para que los diffs sean legibles». Corregido arriba contra el booklet oficial, que da otro motivo de diseño.

[VERIFICAR: re-chequear el estado de mantenimiento de los tres al día de publicar. Al 2026-07-15: Iceberg activo (v2.4.11, 2026-07-09) y Tonel activo (v1.2.0, 2025-05-26). Metacello es ambiguo y conviene mirarlo de nuevo: el repo canónico multi-dialecto `Metacello/metacello` tiene CI y PRs recientes pero su último *release* es de 2015, y el fork `pharo-project/pharo-metacello` quedó con un release de 2015 («Version of Metacello integrated into Pharo 5.0»). No encontré una página oficial de Pharo que declare cuál es el repo vigente — preguntar en la lista o mirar qué carga la imagen de Pharo del momento.]

El modelo mental es este: seguís trabajando en la imagen viva, y el commit es un acto de exportación. La imagen sigue siendo donde vivís; git es donde publicás.

> 🕳️ **HUECO — necesita a César:** ¿Usaste Iceberg en la práctica? ¿Te resultó natural o te peleaste con él? Si tenés una opinión concreta (aunque sea «no llegué a usarlo en serio»), va acá.

### El MOOC, y mi vuelta de tuerca

Inria publica un MOOC oficial de Pharo en FUN, gratuito: se llama *Live Object Programming in Pharo*, lo dan Damien Cassou, Stéphane Ducasse y Luc Fabresse, son siete semanas y unas 40 horas[^mooc]. El sitio del curso tiene además videos, slides y ejercicios por fuera de la plataforma[^moocpharo]. Es el camino de entrada más ordenado que conozco.

Un dato que conviene tener a mano antes de contar la vuelta de tuerca: el MOOC está doblado a francés e inglés, y trae subtítulos en francés, inglés, **español** y japonés[^mooc][^moocpharo].

> 🕳️ **HUECO — necesita a César:** ¿Por qué te armaste el repo `pharo-mooc-english-audio-spanish-subtitles`? ¿Cuál era el problema exacto con el MOOC tal como venía — subtítulos que no estaban, que no se podían bajar, audio en inglés sin transcripción usable?

> 🕳️ **HUECO — necesita a César:** ¿Qué hace técnicamente ese repo, en una frase? ¿Y para quién lo armaste: para vos solo, o para gente a la que le estabas enseñando?

> 🕳️ **HUECO — necesita a César:** ¿Terminaste el MOOC? Si sí, ¿qué te llevaste? Si no, ¿dónde te quedaste y por qué?

La historia completa de esa solución medio Rube-Goldberg la conté aparte, en [[J-05]].

> 🕳️ **HUECO — necesita a César:** `ansible-devops-workstation` instala Pharo. ¿En qué contexto lo usás para enseñar — un curso, un taller, gente del trabajo? ¿Y por qué te pareció que Pharo tenía que estar en la workstation por default?

### Por qué te conviene aunque nunca lo uses en producción

Seamos honestos: lo más probable es que no escribas Pharo en producción, y no voy a fingir lo contrario.

Pero la pregunta no es esa. La pregunta es qué te pasa en la cabeza después de una semana adentro de un sistema donde la distancia entre pensar algo y verlo pasar es cero. Porque volvés a tu stack habitual, y de golpe notás cosas que antes te parecían el clima: el rebuild de cuarenta segundos, el restart para probar una línea, los `print` sembrados como migas para reconstruir un estado que el sistema tenía y tiró a la basura. Nada de eso es una ley de la naturaleza. Es una decisión, tomada por otra gente, hace mucho, y que heredaste sin votarla.

Bret Victor armó toda una charla alrededor de esta sensación — *Inventing on Principle*, en CUSEC 2012, Montreal[^victor] — y aunque no habla de Smalltalk, habla exactamente de esto: la inmediatez como principio, no como comodidad. Su formulación es que los creadores necesitan una conexión inmediata con lo que están creando: si hacés un cambio, tenés que ver el efecto *inmediatamente*. (Dato al pasar: entre los ejemplos de inventores guiados por un principio, Victor cita a Kay.)

Kay viene diciendo hace décadas que la revolución de la computación, la de verdad, todavía no pasó. La formulación es directamente el título de su charla: *The Computer Revolution Hasn't Happened Yet*, que dio en 1997 — en Stanford en junio[^kaystanford] y como keynote de OOPSLA '97[^kayoopsla]. El abstract de Stanford lo despliega: los inventos que cambian el mundo casi nunca se aceptan cuando aparecen, primero tienen que disfrazarse de «better old things»; y a 50 años de desarrollo «the computer is still masquerading as *better paper*»[^kaystanford].

[VERIFICAR: si se lo va a citar entre comillas con una frase suelta del cuerpo de la charla, sacar la cita del transcript de OOPSLA '97 que está en archive.org[^kayoopsla] y verificar la frase exacta. Busqué en ese transcript y **no** aparece una formulación en una sola línea del tipo «la revolución no llegó» dentro del cuerpo: el título es la tesis, y Kay la desarrolla a lo largo de la charla sin repetirla como eslogan. Lo seguro es atribuirle el título y el abstract de Stanford, que sí están verificados; no inventar una frase entrecomillada.] Uno puede pensar que es la nostalgia de un tipo que estuvo en el lugar correcto en el momento correcto. Instalá Pharo, pasá una semana adentro, y después decime si sigue sonando a nostalgia.

> 🕳️ **HUECO — necesita a César:** ¿Cuál es *tu* respuesta a esto? Después de tu experiencia con Pharo, ¿te cambió algo en cómo mirás las herramientas que usás todos los días, o te quedó como una curiosidad interesante y nada más? La honestidad acá vale más que el entusiasmo.

[^bluebook]: Adele Goldberg & David Robson, *Smalltalk-80: The Language and its Implementation*, Addison-Wesley, 1983 — el «Blue Book», [archive.org/details/smalltalk80imple00gold](https://archive.org/details/smalltalk80imple00gold).
[^kay]: Alan Kay, *The Early History of Smalltalk*, HOPL II, 1993 — [worrydream.com/EarlyHistoryOfSmalltalk](http://worrydream.com/EarlyHistoryOfSmalltalk/).
[^ingalls]: Dan Ingalls, *Design Principles Behind Smalltalk*, Byte Magazine, agosto 1981 — [cs.virginia.edu/~evans/cs655/readings/smalltalk.html](https://www.cs.virginia.edu/~evans/cs655/readings/smalltalk.html).
[^pharo]: [Pharo — sitio oficial](https://pharo.org/).
[^squeak]: [Squeak](https://squeak.org/) — el ancestro libre de Pharo.
[^pbe]: *Pharo by Example*, libro libre en varias ediciones — [books.pharo.org](https://books.pharo.org/).
[^deep]: Stéphane Ducasse et al, *Deep into Pharo* — [books.pharo.org/deep-into-pharo](https://books.pharo.org/deep-into-pharo/).
[^mooc]: [MOOC oficial de Pharo en FUN](https://www.fun-mooc.fr/en/courses/pharo-syntax-and-tools/) — el curso de Inria, gratuito.
[^victor]: Bret Victor, *Inventing on Principle*, CUSEC 2012 — [vimeo.com/36579366](https://vimeo.com/36579366).

