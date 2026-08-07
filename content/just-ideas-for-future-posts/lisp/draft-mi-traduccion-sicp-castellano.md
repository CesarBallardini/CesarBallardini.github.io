### A2-06 — Mi propia traducción de SICP al castellano: el proyecto que casi termina

- **Archivo seed (repo POC):** [github.com/CesarBallardini/sicp-spanish](https://github.com/CesarBallardini/sicp-spanish) — TeX, 10 stars, último push 2022-10-19
- **Slug propuesto:** `mi-traduccion-sicp-castellano`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mi-traduccion-sicp-castellano/index.md`
- **Serie:** A2 — complementa [[A2-01]] (donde se cita la traducción de FedeHC); también E (memoir personal)
- **Cross-links:** depende de [[tr-03]] (SICP) y [[A2-01]]; lleva a [[A2-07]] (DrRacket + Jupyter), [[E-12]] (el patrón Vagrant+Ansible)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César) — el toolchain de build (HTML5/ePub/PDF desde `sicp.texi` dentro de una VM Virtualbox) funciona; la traducción avanza incrementalmente desde el capítulo 2 (porque el capítulo 1 ya está cubierto por la traducción de FedeHC).
- **Length target:** medium (1800-2500 palabras)

**Concepto:** SICP (*Structure and Interpretation of Computer Programs*, Abelson & Sussman) es uno de los libros más importantes de la historia de la enseñanza de CS. Tiene traducciones al español, pero la mayoría son parciales, abandonadas o difíciles de mantener. En 2018-2022 me senté a empezar mi propia traducción, partiendo del *texinfo* fuente original del MIT, con un toolchain dentro de una VM (Virtualbox + Ansible) que produce HTML5, ePub y PDF en un solo build. Empecé por el capítulo 2 porque el capítulo 1 ya estaba cubierto por la versión de FedeHC. Después la realidad pateó la pelota y la traducción quedó parcial. El post es la historia honesta de por qué intenté, qué aprendí, y por qué creo que vale la pena que alguien la termine algún día.

**Hook:** "SICP es uno de los libros más importantes de CS. La traducción al español es un patchwork de proyectos abandonados. En 2018 dije: lo hago yo. Armé el toolchain, monté la VM, empecé por el capítulo 2 (el 1 ya estaba traducido por FedeHC), avancé varias secciones... y la realidad me pasó por encima. Quedó parcial. El post es por qué intenté, por qué la pedagogía de SICP merece esfuerzo, y qué le diría a la próxima persona que se anime."

**Outline:**
1. SICP en 30 segundos (cross con [[A2-01]] y [[tr-03]]).
2. El paisaje de las traducciones al español: FedeHC, Andres Raba (PDF moderno), traducciones parciales en blogs, los videos doblados.
3. Por qué decidí empezar de nuevo: tener el `texinfo` fuente como input, no PDF. Habilita ePub, HTML5, PDF, traducciones parciales que se pueden mejorar incrementalmente.
4. La VM: Virtualbox + Ansible + texinfo + texlive + Calibre. El `Vagrantfile` y por qué eligí build dentro de VM en vez de en mi máquina anfitriona.
5. La estrategia de "empezar por el capítulo 2": evitar duplicar trabajo y entrar directo al material técnico más jugoso (data abstraction, generic operations, message passing).
6. Lo que hice y lo que no: las secciones traducidas, las que quedaron a medio, los términos técnicos que me trabaron (¿"closure"?, ¿"thunk"?, ¿"tail call"?).
7. Por qué se frenó: no es una sola razón. Trabajo, otras prioridades, y honestamente — la traducción es un trabajo de horas y no de inspiración.
8. Lo que aprendí del proceso: traducir es leer 4 veces; el toolchain es lo de menos; lo difícil es la consistencia terminológica.
9. Cierre: si alguien quiere continuarla, el repo está abierto. Y si soy yo quien la continúa algún día, ya sé en qué orden hacerlo.

**Bibliografía:** *(pasada de sourcing 2026-07-15 — todas las URLs de abajo fueron fetcheadas y verificadas salvo donde se aclara lo contrario; flag de bitrot al final de cada una)*

*El libro*

- Abelson, Harold; Gerald Jay Sussman; Julie Sussman. *Structure and Interpretation of Computer Programs*. **2da ed.**, Cambridge, MA: MIT Press, 1996. ISBN 978-0-262-01153-2. Texto completo oficial, [MIT Press](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html) — **CC BY-SA 4.0** (dato load-bearing: es lo que hace legal la traducción). — *estable*
- Ídem, **1ra ed.**, MIT Press / McGraw-Hill, 1985, ISBN 0-262-01077-1, 578 pp. — [archive.org](https://archive.org/details/structureinterpr00abel), préstamo digital controlado; el ejemplar digitalizado es la 8va impresión. — *estable*

*El curso*

- [6.001 — MIT OpenCourseWare, Spring 2005](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/pages/syllabus/) — el syllabus con la cita exacta del libro de texto. Confirma número de curso y edición. — *estable*
- [Evan B. '10, «The End of an Era», MIT Admissions, 8-ene-2008](https://mitadmissions.org/blogs/entry/the_end_of_an_era_1/) — otoño 2007 fue el último dictado de 6.001; reemplazado por 6.00/6.01/6.02. — *estable* (dominio institucional MIT)
- [6.037 — SICP en el IAP, MIT (2019)](https://web.mit.edu/6.001/6.037/) — el curso que sigue usando SICP. — *estable*

*El linaje del texinfo (la cadena de la que sale `sicp.texi`)*

- [Neil Van Dyke, *SICP in Texinfo Format*](https://www.neilvandyke.org/sicp-texi/) — Unofficial Texinfo Format `2.neilvandyke4` (10-ene-2007); conversión original de Lytha Ayth desde el HTML del MIT Press. Sitio del autor. — *frágil* → [backup Wayback 3-jun-2026](http://web.archive.org/web/20260603112726/https://www.neilvandyke.org/sicp-texi/)
- [Andres Raba, *sicp-pdf*](https://github.com/sarabander/sicp-pdf) — UTF `2.andresraba5`, texinfo→LaTeX, XeTeX. CC BY-SA 4.0 el contenido, GPLv3 los scripts. — *frágil* (GitHub personal)
- [Andres Raba, *sicp* — HTML5 + ePub3](https://github.com/sarabander/sicp) — base de mi build; raíz `sicp-pocket.texi`. — *frágil* (GitHub personal)
- [PDF de Raba mirroreado en el sitio de 6.037](https://web.mit.edu/6.001/6.037/sicp.pdf) — 883 pp. **No es una edición del MIT Press pese al dominio**: la portada dice «Unofficial Texinfo Format 2.andresraba5.6». — *estable*

*Traducciones al español*

- [SICP-ES — FedeHC](https://github.com/FedeHC/SICP-ES) — 2da edición, CC BY-SA 4.0, capítulo 1 traducido (sep-2019), archivado 7-nov-2022. — *frágil* (GitHub personal)
- Repo del POC propio: [CesarBallardini/sicp-spanish](https://github.com/CesarBallardini/sicp-spanish). — *frágil*

*El debate MIT → Python*

- Dan Weinreb, [«Why Did M.I.T. Switch from Scheme to Python?»](http://web.archive.org/web/20120106165325/http://danweinreb.org/blog/why-did-mit-switch-from-scheme-to-python), 10-may-2009 — **la fuente principal**: Sussman en la International Lisp Conference 2009 + confirmación del Prof. Jacob White (diseñador de la currícula). `danweinreb.org` está muerto; se cita por Wayback. — *estable* (vía Wayback; el original ya no existe)
- Chas Emerick, [«Why MIT now uses python instead of scheme…»](https://cemerick.com/2009/03/24/why-mit-now-uses-python-instead-of-scheme-for-its-undergraduate-cs-program/), 24-mar-2009 — notas de la misma charla. — *frágil* → [backup Wayback 8-nov-2020](http://web.archive.org/web/20201108162611/https://cemerick.com/2009/03/24/why-mit-now-uses-python-instead-of-scheme-for-its-undergraduate-cs-program/)
- ~~[Stuart Halloway, *Why MIT now uses Python instead of Scheme…*](https://news.ycombinator.com/item?id=602307)~~ — **entrada errónea, corregida.** El ítem 602307 de HN no es de Stuart Halloway ni se titula así: es «Why Did M.I.T. Switch from Scheme to Python?», subido por `l0stman` el 10-may-2009, y apunta al posteo de **Dan Weinreb** que está arriba (verificado vía [la API de HN](https://hn.algolia.com/api/v1/items/602307); `news.ycombinator.com` devolvió HTTP 429 en tres intentos). Se reemplaza por las dos fuentes de arriba, que son las de primera mano.

*Herramientas*

- [iRacket](https://github.com/rmculpepper/iracket) — kernel de Racket para Jupyter, BSD-3-Clause; original de Theo Giannakopoulos (PPAML), mantenido por Ryan Culpepper (cross [[A2-07]]). — *frágil* (GitHub personal)
- [[tr-03]] — SICP referencia transversal.

**Imágenes:**
- _Crear_: screenshot del HTML5 generado por mi build, mostrando el capítulo 2 en castellano (~15 min).
- _Crear_: side-by-side de un párrafo en inglés vs su traducción en castellano (~10 min).
- _Crear_: captura del repo en GitHub mostrando la estructura de directorios (~5 min).

**Tags propuestos:** `['SICP', 'traduccion', 'castellano', 'texinfo', 'Vagrant', 'Abelson', 'Sussman', 'pedagogia']`

**Estado actual:**

⚠️ **PREMISA EN DUDA (sourcing 2026-07-15):** el Concepto dice que el proyecto parte «del *texinfo* fuente original del MIT». **Ese texinfo no existe.** El MIT Press publicó SICP en HTML; el `sicp.texi` es el *Unofficial Texinfo Format*, una conversión comunitaria hecha desde ese HTML por Lytha Ayth (2001 o antes), mantenida por Neil Van Dyke (`2.neilvandyke4`, 10-ene-2007) y continuada por Andres Raba (`2.andresraba5.x`). Verificado en tres fuentes independientes: el README de sarabander/sicp («It comes from the lineage of Unofficial Texinfo Format that was converted from the original HTML version at The MIT Press»), el sitio de Neil Van Dyke, y la portada del propio PDF («Unofficial Texinfo Format 2.andresraba5.6 (February 2, 2016), based on 2.neilvandyke4 (January 10, 2007)»). No toqué el Concepto ni el Hook. La decisión técnica del proyecto no cambia —el input estructurado existe y es lo que habilita el multiformato y la traducción incremental—; lo que cambia es a quién se le atribuye: no al MIT, sino a tres personas que lo hicieron a mano en quince años. Hay una nota de corrección marcada en la sección «Por qué decidí empezar de nuevo».

⚠️ **Segunda tensión, menor:** la respuesta del post a la objeción «el MIT dejó SICP» («envejeció como asignación de tiempo institucional») no queda contradicha, pero sí incompleta: Weinreb documenta que quienes querían sacar SICP de la base del primer año, desde 1995, eran Abelson y Sussman mismos. Hay una nota marcada en la sección «Lo que aprendí» y un hueco para que César decida cómo contestarla.

**Sourcing hecho (2026-07-15):** se agregaron 11 referencias nuevas, todas fetcheadas y verificadas, con flag de bitrot y backup de Wayback en las frágiles load-bearing. Hallazgos que cambian el draft: (1) la entrada de bibliografía «Stuart Halloway / HN 602307» estaba **mal atribuida** — el ítem es «Why Did M.I.T. Switch from Scheme to Python?», subido por `l0stman`, y apunta al blog de **Dan Weinreb**; reemplazada por Weinreb (vía Wayback, el dominio murió) + Emerick, que son las fuentes de primera mano de la charla de Sussman. (2) El PDF de `web.mit.edu/6.001/6.037/sicp.pdf` que el draft citaba como «sitio del MIT (2da edición)» es en realidad el PDF de Raba mirroreado por la cátedra. (3) Dato nuevo y útil: el MIT Press distribuye SICP bajo **CC BY-SA 4.0**, que es lo que hace legal el proyecto — ahora está en la prosa. Resueltos 3 de los 5 `[VERIFICAR:]` (número de curso 6.001 y años; ediciones 1985/1996 con ISBNs; el debate MIT→Python). Quedan 2, ambos irreducibles por búsqueda web: el alcance fino de la traducción de FedeHC (ejercicios/notas al pie — hay que abrir los archivos del repo) y el inventario del capítulo 2 en el repo propio de César. Los 15 huecos 🕳️ siguen intactos.

**Estado del POC:** **partial-poc** en GitHub (10 stars, build funciona, traducción parcial). El post es 90% memoir y 10% técnico, así que sale rápido.

Hay un borrador de prosa completo abajo (~2.200 palabras, dentro del target medium), escrito sobre el outline de 9 puntos sin modificarlo. Como el post es memoir sobre un proyecto propio, el borrador está construido como andamio: el encuadre técnico, las transiciones y el argumento pedagógico están escritos; **todo recuerdo, decisión y opinión de César quedó como hueco marcado** (15 huecos `🕳️`, casi todos de una o dos frases de respuesta). Los datos que la bibliografía del draft no respaldaba —fechas de edición de SICP, el número del curso del MIT, el alcance real de la traducción de FedeHC, qué secciones quedaron efectivamente traducidas, qué decía exactamente el debate de MIT/Python— quedaron con marcadores `[VERIFICAR:]` inline (5 en total; la ficha anterior decía 7, el conteo real era 5) en vez de afirmarse. La pasada de sourcing del 2026-07-15 resolvió 3 y dejó 2, más dos notas de corrección visibles en la prosa. Pendiente: contestar los huecos, resolver los 2 `[VERIFICAR:]` que quedan contra el repo propio y el de FedeHC, decidir qué hacer con la corrección del «texinfo original del MIT» (afecta al Concepto), y recién ahí pasar a `hugo new`. Las tres imágenes siguen sin crear.

---

## Borrador de prosa

SICP es, para mucha gente que hace software, el libro. No el libro que te enseña un lenguaje: el libro que te enseña a mirar. Y la traducción al español es un patchwork de proyectos que empezaron con toda la energía del mundo y se apagaron en algún capítulo intermedio. En 2018 me miré al espejo y dije: bueno, lo hago yo.

Armé el toolchain, monté la VM, empecé por el capítulo 2 —el 1 ya lo había traducido FedeHC— y avancé varias secciones. Después la realidad me pasó por encima y quedó parcial. El repo está ahí, público, con el build funcionando.[^repo] Este post es la historia honesta de por qué lo intenté, por qué creo que la pedagogía de SICP merece el esfuerzo, y qué le diría a la próxima persona que se anime.

### SICP en 30 segundos

*Structure and Interpretation of Computer Programs*, de Harold Abelson y Gerald Jay Sussman con Julie Sussman, fue el libro de texto de **6.001**, el curso introductorio de computación del MIT.[^ocw6001] La materia se apoyó en SICP desde 1985[^weinreb] y se dictó por última vez en el semestre de otoño de 2007: la nueva currícula de Course VI (EECS) no le dejó lugar y la reemplazó por 6.00, 6.01 y 6.02.[^end_of_era] El libro igual no se fue del MIT: sobrevive en 6.037, la versión que se dicta en el IAP.[^mit_6037] Usa Scheme, pero no es un libro sobre Scheme: usa Scheme porque el lenguaje se aprende en una tarde y entonces deja de estorbar. Lo que enseña es otra cosa —abstracción de datos, abstracción procedural, estado, evaluación, cómo se construye un intérprete— y lo enseña haciéndote construir las herramientas en lugar de contártelas.

Si querés el desarrollo largo de por qué este libro importa, está en [[A2-01]] y en la referencia transversal [[tr-03]]. Acá me alcanza con una cosa: SICP es de los pocos textos técnicos donde el orden de los capítulos *es* el argumento. No se puede saltear. Y eso, spoiler, después me complicó la vida.

Hay dos ediciones. La primera es de 1985, publicada por MIT Press junto con McGraw-Hill (ISBN 0-262-01077-1).[^sicp_1ed] La segunda —la que se cita siempre, la que pide el syllabus de 6.001 y la que uso yo— es de 1996 (MIT Press, ISBN 978-0-262-01153-2).[^ocw6001] Y hay un detalle que para este post no es decorativo: el MIT Press publica el texto completo de la segunda edición bajo licencia **Creative Commons Attribution-ShareAlike 4.0**.[^mit_fulltext] Traducir SICP no es un favor que haya que pedirle a nadie: la licencia ya te dio permiso.

> 🕳️ **HUECO — necesita a César:** ¿Cuándo y cómo llegaste vos a SICP por primera vez? ¿Fue en la facultad, por cuenta propia, alguien te lo recomendó? Una o dos frases.

> 🕳️ **HUECO — necesita a César:** ¿Cuál fue *el momento* de SICP para vos —la página o el ejercicio donde dijiste «ah, esto es otra cosa»? Sirve para anclar el post en algo concreto en vez de en el prestigio del libro.

### El paisaje de las traducciones al español

Cuando uno se pone a buscar SICP en castellano, lo que encuentra no es una traducción: son varias, incompletas, en distintos formatos y en distintos estados de abandono.

La referencia principal es **SICP-ES, de FedeHC**.[^fedehc] Es un trabajo serio y es el que uso como punto de partida para no duplicar esfuerzo: apunta a la segunda edición, está publicado bajo CC BY-SA 4.0, y llegó a tener **el capítulo 1 completo** —anunciado en septiembre de 2019, con la sección 1.1 revisada a fondo para julio de 2020— antes de quedar archivado en modo sólo-lectura el 7 de noviembre de 2022.[^fedehc] El README no se anda con vueltas sobre el motivo: el trabajo «me llevará seguramente muchos meses, tal vez incluso años». Es exactamente la misma pared contra la que me di yo, y la cuento más abajo. [VERIFICAR: si el capítulo 1 de FedeHC incluye los ejercicios y las notas al pie o sólo el cuerpo del texto — el README menciona haber revisado «el código fuente de los ejemplos» y las notas al pie, pero no declara el alcance; hay que abrir los archivos del repo, con el README no alcanza]

Después están los proyectos que no son traducciones pero cambian el paisaje igual. **Andres Raba** rehizo SICP en un PDF moderno, con la tipografía corregida y las figuras rearmadas,[^raba_pdf] y además publicó una edición HTML5 + ePub3.[^raba_html] Están en inglés, pero son importantes acá por una razón de la que hablo enseguida: son fuentes *estructurados*, no papel escaneado.

Y después está la larga cola: traducciones parciales en blogs, capítulos sueltos en PDF, videos doblados o subtitulados. Cosas hechas con buena voluntad que resuelven el problema de una persona y no el de la comunidad, porque no se pueden continuar. Vos no podés agarrar el capítulo 3 traducido en un blog y mandar un pull request.

> 🕳️ **HUECO — necesita a César:** ¿Qué traducciones parciales concretas te cruzaste cuando buscaste? Con que recuerdes una o dos y en qué estado estaban alcanza — si no las recordás con precisión, decilo y lo dejo genérico.

> 🕳️ **HUECO — necesita a César:** ¿Llegaste a hablar con FedeHC o con alguien de los otros proyectos, o fue todo asincrónico vía repos?

### Por qué decidí empezar de nuevo

Esta es la parte técnica del post y es más corta de lo que parece.

Casi todas las traducciones parten del PDF o del HTML publicado. Es lo natural: es lo que uno encuentra. Y es también la razón por la que se mueren. Cuando tu input es un PDF, tu output es un PDF, y cada mejora posterior es una edición manual sobre un formato que no fue diseñado para editarse.

Yo quería partir del **texinfo** original. `sicp.texi` no es el libro renderizado: es el libro *antes* de decidir en qué formato sale. Y de ahí, con un solo build, salen las tres cosas que quiero:

- **HTML5**, para leer en el navegador y para que Google lo encuentre.
- **ePub**, para el lector de libros.
- **PDF**, para imprimir o para quien lo quiera así.

Pero el beneficio real no es el multiformato. Es que **una traducción parcial se vuelve un objeto legítimo**. Con el fuente estructurado, el capítulo 2 traducido y el 3 en inglés conviven en el mismo build sin romper nada: los índices funcionan, los links cruzados funcionan, la numeración de ejercicios funciona. La traducción deja de ser un evento —«sale cuando esté completa»— y pasa a ser un proceso incremental que cualquiera puede empujar un poco. Que es exactamente lo que necesita un proyecto que depende de tiempo libre.

La base de mi build es la edición HTML5 + ePub3 de Raba.[^raba_html]

> ⚠️ **CORRECCIÓN de sourcing (2026-07-15):** el `sicp.texi` **no es «el texinfo original del MIT»** — el Concepto del draft y esta sección lo dan a entender, y no es exacto. El MIT Press publicó el libro en HTML, no en texinfo. Lo que existe es el **Unofficial Texinfo Format (UTF)**: una conversión comunitaria hecha desde ese HTML por Lytha Ayth (2001 o antes), mantenida después por Neil Van Dyke —versión `2.neilvandyke4`, 10 de enero de 2007—[^utf_nvd] y continuada por Andres Raba como `2.andresraba5.x`, que la pasó a LaTeX/XeTeX.[^raba_pdf] La portada del PDF que circula lo dice textualmente: «Unofficial Texinfo Format 2.andresraba5.6 (February 2, 2016), based on 2.neilvandyke4 (January 10, 2007)».[^raba_mit_mirror] Esto no debilita el argumento de la sección — lo mejora: el input estructurado del que parte todo el proyecto existe *porque* tres personas lo construyeron a mano durante quince años. Vale la pena decirlo así en el post y nombrarlos.

### La VM: por qué no compilo esto en mi máquina

El toolchain para producir esos tres formatos no es liviano: texinfo, TeX Live y Calibre, cada uno con su cadena de dependencias.

Elegí meter todo eso adentro de una VM de VirtualBox, provisionada con Ansible y levantada con un `Vagrantfile`, en vez de instalarlo en la máquina anfitriona. Las razones:

1. **No quiero TeX Live tatuado en mi laptop.** Es un montón de disco y de paquetes para un proyecto al que le dedico ratos.
2. **El build tiene que ser reproducible por otro.** Si alguien clona el repo, `vagrant up` y ya. No hay una lista de veinte `apt install` en un README que se desactualiza.
3. **Reproducible por mí en tres años.** Que es —anticipo el final— exactamente lo que terminó pasando.
4. **El provisioning es documentación ejecutable.** El playbook de Ansible *es* la lista de dependencias, y no puede mentir, porque si miente el build falla.

Este mismo patrón Vagrant + Ansible lo uso en otros proyectos y lo desarrollo aparte en [[E-12]]; acá es la aplicación de esa idea a un problema de libros en lugar de a uno de infraestructura.

Como complemento —no como parte del build— usé **iRacket**, el kernel de Racket para Jupyter,[^iracket] para poder correr el código del libro en notebooks mientras traducía. Eso lo cuento en detalle en [[A2-07]].

> 🕳️ **HUECO — necesita a César:** ¿Qué te rompió el build cuando lo armaste? Un problema concreto (una versión de texinfo, un font de TeX, Calibre en headless) le da carne a esta sección; si fue todo liso, decilo y lo digo así.

> 🕳️ **HUECO — necesita a César:** ¿Cuánto tarda un build completo de los tres formatos en la VM? Aunque sea un orden de magnitud: ¿un minuto?, ¿diez?

### La estrategia de empezar por el capítulo 2

Acá está la decisión de la que estoy más conforme y la que más me costó explicar cuando la contaba.

Traducir un libro empezando por el capítulo 2 suena a locura. Pero el capítulo 1 ya estaba cubierto por FedeHC, y duplicar ese trabajo era regalarle meses al ego. Si el objetivo es que exista SICP en castellano —y no que exista *mi* SICP en castellano— el único movimiento razonable es agarrar por donde no hay nadie.

Y hay un bonus: el capítulo 2 es donde el libro se pone realmente interesante. Abstracción de datos, operaciones genéricas, message passing. El capítulo 1 es hermoso pero es el que más se parece a lo que ya sabés; el 2 es donde SICP empieza a hacer lo suyo.

> 🕳️ **HUECO — necesita a César:** ¿La decisión de arrancar por el 2 fue así de deliberada desde el principio, o arrancaste por el 1, viste que ya estaba hecho y te corriste? La versión honesta es mejor post que la versión ordenada.

### Lo que hice y lo que no

[VERIFICAR: qué secciones del capítulo 2 quedaron efectivamente traducidas y cuáles a medias — la pasada de sourcing web NO audita esto a propósito: es el repo propio de César (`CesarBallardini/sicp-spanish`, último push 2022-10-19 según la ficha del draft). Hay que abrirlo y hacer el inventario a mano, o preguntarle a él. Ninguna búsqueda lo responde.]

> 🕳️ **HUECO — necesita a César:** ¿Hasta dónde llegaste realmente? Aunque sea aproximado: ¿qué secciones del capítulo 2 están completas, cuáles a medio camino, y tocaste algo del 3?

> 🕳️ **HUECO — necesita a César:** ¿Traducías también los ejercicios y las notas al pie, o primero el cuerpo del texto y después el resto?

Lo que sí puedo contar sin abrir el repo es dónde me trababa, porque me trababa siempre en el mismo lugar: **los términos que no tienen traducción buena**.

*Closure* es el caso testigo. SICP usa la palabra en su sentido matemático —una operación es cerrada sobre un conjunto si combinar elementos te devuelve otro elemento del mismo conjunto— y el lector de hoy la conoce del sentido de la programación funcional, que es otro. «Clausura» arrastra el problema y suma el ruido judicial. *Thunk*: no existe en castellano y cualquier perífrasis explica el mecanismo pero pierde el sustantivo, y necesitás el sustantivo porque después decís «el thunk» quince veces. *Tail call*: «llamada en cola» se entiende, pero suena a traducción y no a idioma.

Y la trampa: cada una de estas decisiones parece chica y ninguna lo es, porque una vez que elegiste tenés que sostenerla trescientas páginas. Cambiar de opinión en el capítulo 3 te obliga a volver al 2.

> 🕳️ **HUECO — necesita a César:** ¿Qué resolviste finalmente con «closure»? ¿Dejaste el término en inglés en itálicas, tradujiste, pusiste nota del traductor? Es el detalle más jugoso de toda esta sección.

> 🕳️ **HUECO — necesita a César:** ¿Llevabas un glosario en algún lado —archivo, planilla, cabeza— o ibas decidiendo sobre la marcha?

### Por qué se frenó

No hay una sola razón, y las historias de proyectos abandonados que tienen una sola razón suelen estar editadas.

> 🕳️ **HUECO — necesita a César:** ¿Qué pasó, concretamente, alrededor de 2022? ¿Trabajo, otro proyecto que te comió el tiempo libre, algo personal? Con el titular alcanza, no hace falta el detalle.

Pero sí hay algo que puedo decir y que es la lección más transferible del post: **traducir es un trabajo de horas, no de inspiración.** No hay un día en que se te ocurre el capítulo 2. Hay cuarenta noches de párrafo a párrafo. Y los proyectos que dependen de horas y no de inspiración son exactamente los que pierden contra la vida, porque la vida no te saca las ganas: te saca las noches.

> 🕳️ **HUECO — necesita a César:** ¿Sentiste culpa cuando lo dejaste, o fue una decisión tranquila? El post gana si esto es honesto.

### Lo que aprendí

**Traducir es leer cuatro veces.** Una para entender, otra para escribir, otra para que suene a castellano y no a calco, y otra para que concuerde con lo que decidiste doscientas páginas antes. Nunca leí SICP tan bien como cuando lo estaba traduciendo, y ese es probablemente el beneficio real que me llevé.

**El toolchain es lo de menos.** Yo entré a este proyecto por la puerta de la infraestructura, que es mi puerta: VM, Ansible, build reproducible, tres formatos de salida. Todo eso funcionó y funciona todavía. Y no era el problema. El problema era el párrafo.

**Lo difícil es la consistencia terminológica.** No la primera decisión: la número doscientos, cuando ya no te acordás de la número tres. Si volviera a empezar, lo primero que haría no es levantar la VM: es escribir el glosario. Antes de traducir una línea.

Y hay un debate que conviene contar bien, porque casi siempre se cuenta mal: por qué el MIT dejó de usar Scheme y SICP en el curso introductorio y pasó a Python.

La fuente de primera mano es un posteo de **Dan Weinreb** del 10 de mayo de 2009.[^weinreb] Weinreb escuchó una charla improvisada de Gerry Sussman en la International Lisp Conference y después —para tener una segunda opinión— llamó al profesor Jacob White, uno de los diseñadores de la nueva currícula, que le confirmó la versión. Del posteo salen dos cosas, y las dos son incómodas para algún bando. La primera: **cambiar de lenguaje no fue un objetivo, fue una consecuencia.** La materia nueva es de robots, el software del robot venía en Python, fin de la historia; en palabras de Weinreb, «Changing programming languages was absolutely not a goal of the curriculum change». La segunda, la que casi nunca se cita: **Abelson y Sussman venían proponiendo desde 1995** cambiar radicalmente la currícula de primer año y no basarla en SICP.

Chas Emerick, que estuvo en la misma charla, anotó el razonamiento de Sussman:[^emerick] el ingeniero de hoy recibe una biblioteca enorme con un manual de trescientas páginas lleno de errores, y un robot cuyo comportamiento exacto no puede caracterizar —¿qué pasa cuando patina una rueda?—, así que su trabajo es hacer experimentos para averiguar cómo funciona todo. En 1980 el juego era componer piezas bien definidas hasta llegar a algo bien definido. Ya no. Sobre por qué Python y no otro, Sussman no fingió doctrina: «Why did they choose python? Who knows, it's probably because python has a good standard library for interacting with the robot».[^emerick]

Menciono ese debate porque es la objeción que siempre aparece: si el propio MIT se corrió de SICP, ¿para qué traducirlo? Mi respuesta corta es que el libro no envejeció como currícula, envejeció como *asignación de tiempo institucional*, que no es lo mismo. Las ideas del capítulo 2 no caducaron. Solo dejaron de caber en un cuatrimestre.

> ⚠️ **Nota de sourcing:** ojo con la respuesta de arriba, porque las fuentes la dejan a medio sostener. Que el cambio no fue una guerra de lenguajes: confirmado, Weinreb es explícito.[^weinreb] Pero «asignación de tiempo institucional» sugiere que a SICP le sacaron el lugar desde afuera, y Weinreb dice otra cosa: los que querían sacar SICP de la base del primer año, desde 1995, eran **Abelson y Sussman mismos**. La postura sigue siendo defendible —SICP como libro no es lo mismo que SICP como currícula de una carrera de ingeniería del MIT, y Sussman habla de formar ingenieros, no de si el libro vale— pero el post gana si cita ese dato y lo contesta, en vez de esquivarlo. Si no, la objeción vuelve en el primer comentario. La respuesta la tiene que dar César (ver el hueco de acá abajo).

> 🕳️ **HUECO — necesita a César:** ¿Cuál es tu postura sobre el «MIT dejó SICP»? Es la objeción obvia al proyecto y conviene que la respuesta sea tuya y no mía.

### Cierre

El repo está abierto.[^repo] El build anda: `vagrant up`, y a los pocos minutos tenés HTML5, ePub y PDF. El capítulo 1 está cubierto por FedeHC. El 2 está empezado. Si alguien quiere continuarlo, no tiene que pelearse con el toolchain, que es donde mueren la mayoría de estos intentos: tiene que sentarse a traducir, que es donde tiene que morir el esfuerzo.

Y si algún día lo continúo yo, ya sé el orden: primero el glosario, después la VM, después el párrafo. Al revés de como lo hice.

> 🕳️ **HUECO — necesita a César:** ¿Querés cerrar con una invitación explícita —«mandame un mail / abrí un issue»— o preferís dejarlo como está, sin pedir nada?

[^repo]: [CesarBallardini/sicp-spanish](https://github.com/CesarBallardini/sicp-spanish) — el repositorio del proyecto, con el `Vagrantfile`, el provisioning y los fuentes en texinfo.
[^ocw6001]: [6.001 *Structure and Interpretation of Computer Programs*, Spring 2005 — MIT OpenCourseWare](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/pages/syllabus/) — el [syllabus](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/pages/syllabus/) declara el libro de texto obligatorio: «Abelson, Harold, Gerald Jay Sussman, and Julie Sussman. *Structure and Interpretation of Computer Programs*. 2nd ed. Cambridge, MA: MIT Press, 1996. ISBN: 9780262011532». Dictado por Eric Grimson, Peter Szolovits y Trevor Darrell.
[^end_of_era]: [Evan B. '10, «The End of an Era» — MIT Admissions, 8 de enero de 2008](https://mitadmissions.org/blogs/entry/the_end_of_an_era_1/) — blog institucional del MIT: «this is the last term that [6.001] was offered» (otoño 2007); «it's being replaced by 6.00, 6.01, and 6.02 in the new curriculum».
[^mit_6037]: [6.037 — *Structure and Interpretation of Computer Programs*, IAP 2019 (MIT)](https://web.mit.edu/6.001/6.037/) — la materia de IAP que sigue usando SICP después del retiro de 6.001.
[^sicp_1ed]: [Abelson, Harold; Gerald Jay Sussman; Julie Sussman. *Structure and Interpretation of Computer Programs*. 1ra ed. Cambridge, MA: MIT Press / New York: McGraw-Hill, 1985. ISBN 0-262-01077-1](https://archive.org/details/structureinterpr00abel) — 578 pp. En archive.org sólo en préstamo digital controlado (el ejemplar digitalizado es la 8va impresión).
[^mit_fulltext]: [*Structure and Interpretation of Computer Programs*, 2da edición — texto completo, MIT Press](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html) — la edición electrónica oficial: «licensed under a Creative Commons Attribution-ShareAlike 4.0 International License by the MIT Press».
[^fedehc]: [SICP-ES — traducción de FedeHC](https://github.com/FedeHC/SICP-ES) — traducción al español de la 2da edición, CC BY-SA 4.0. Capítulo 1 traducido (anuncio de septiembre de 2019; sección 1.1 revisada para julio de 2020). Repositorio archivado en modo sólo-lectura el 7 de noviembre de 2022.
[^raba_pdf]: [Andres Raba, *SICP modern PDF edition*](https://github.com/sarabander/sicp-pdf) — revisión `2.andresraba5`: conversión del texinfo a LaTeX, compilada con XeTeX (Unicode + OpenType, fuentes Inconsolata LGC y Linux Libertine, figuras SVG→PDF vía Inkscape). `sicp.texi`, `sicp.pdf` y los diagramas bajo CC BY-SA 4.0; los scripts bajo GPLv3.
[^raba_html]: [SICP — edición HTML5 + ePub3](https://github.com/sarabander/sicp) — la base de mi build. README: «This is a new HTML5 and EPUB3 version of *Structure and Interpretation of Computer Programs*… It comes from the lineage of Unofficial Texinfo Format that was converted from the original HTML version at The MIT Press». Fuente raíz: `sicp-pocket.texi`. Contenido CC BY-SA 4.0, scripts GPLv3.
[^utf_nvd]: [Neil Van Dyke, *SICP in Texinfo Format* (Unofficial Texinfo Format)](https://www.neilvandyke.org/sicp-texi/) — versión `2.neilvandyke4`, 10 de enero de 2007; conversión original de Lytha Ayth (2001 o antes) desde el HTML del MIT Press, con las figuras redibujadas en ASCII art. ([backup Wayback, 3 de junio de 2026](http://web.archive.org/web/20260603112726/https://www.neilvandyke.org/sicp-texi/)).
[^raba_mit_mirror]: [SICP PDF alojado en el sitio de 6.037 (MIT)](https://web.mit.edu/6.001/6.037/sicp.pdf) — 883 páginas. **Ojo:** pese a estar en un dominio del MIT, no es una edición del MIT Press: la portada dice «Unofficial Texinfo Format 2.andresraba5.6 / second edition» y la página de créditos «Unofficial Texinfo Format 2.andresraba5.6 (February 2, 2016), based on 2.neilvandyke4 (January 10, 2007)», ©1996 MIT, CC BY-SA 4.0. Es el PDF de Raba mirroreado por la cátedra.
[^iracket]: [iRacket — Racket kernel for Jupyter](https://github.com/rmculpepper/iracket) — kernel de Jupyter para Racket, licencia BSD-3-Clause. Versión original de Theo Giannakopoulos (BAE Systems) para el programa PPAML; mantenido por Ryan Culpepper. Instalación: `raco pkg install iracket` + `raco iracket install`; requiere Racket, Jupyter y ZeroMQ.
[^weinreb]: Dan Weinreb, [«Why Did M.I.T. Switch from Scheme to Python?»](http://web.archive.org/web/20120106165325/http://danweinreb.org/blog/why-did-mit-switch-from-scheme-to-python), *Dan Weinreb's blog*, 10 de mayo de 2009. Relato de primera mano: charla improvisada de Gerry Sussman en la International Lisp Conference 2009, confirmada por el Prof. Jacob White, uno de los diseñadores de la nueva currícula. El dominio `danweinreb.org` está muerto (expirado, sin certificado válido) — este link es la copia de Wayback, que es la única forma de citarlo hoy.
[^emerick]: Chas Emerick, [«Why MIT now uses python instead of scheme for its undergraduate CS program»](https://cemerick.com/2009/03/24/why-mit-now-uses-python-instead-of-scheme-for-its-undergraduate-cs-program/), 24 de marzo de 2009 ([backup Wayback, 8 de noviembre de 2020](http://web.archive.org/web/20201108162611/https://cemerick.com/2009/03/24/why-mit-now-uses-python-instead-of-scheme-for-its-undergraduate-cs-program/)). Notas del autor sobre la misma charla improvisada de Sussman en la International Lisp Conference.

