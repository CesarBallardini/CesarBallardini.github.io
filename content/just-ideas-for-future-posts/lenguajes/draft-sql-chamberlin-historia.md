### A1-16 — SQL: el lenguaje que ganó sin querer (entrevista a Don Chamberlin)

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `sql-chamberlin-historia`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-sql-chamberlin-historia/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-13]], [[H-07]] (FoxBase→PG), [[G-06]] (Postgres en Docker)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 2000–2400 palabras (historia de un lenguaje con hilo argumental + entrevista)

**Concepto:** Don Chamberlin (junto con Ray Boyce) inventó SQL en IBM en los 70 como un lenguaje declarativo para consultar el modelo relacional de Codd. Hoy sigue siendo el lenguaje de bases de datos dominante 50 años después, sobreviviendo a NoSQL, MapReduce, y todas las modas. El post discute la entrevista de Chamberlin, qué pensaba originalmente del SQL, qué cambió, y por qué SQL "ganó".

**Hook:** SQL tiene 50 años. Sigue moviendo el mundo. Don Chamberlin no esperaba que pasara. En la entrevista dice cosas que hoy sorprenden: el modelo relacional sí, el SQL como sintaxis, no necesariamente. El post es ese cuento.

**Outline:**

1. **El hook** — el paper de SEQUEL es de 1974; la cuenta da medio siglo largo. SQL sigue abajo de todo. Chamberlin, preguntado hoy, no defiende el resultado como se esperaría. Dos párrafos.
2. **El modelo antes que el lenguaje** — Codd 1970: los datos como relaciones, la independencia entre el modelo lógico y el almacenamiento físico. La idea es matemática, y es la parte que envejeció bien.
3. **El problema de Codd** — el modelo era hermoso e inaccesible: para consultarlo hacía falta álgebra. Si el modelo iba a salir del paper, necesitaba una puerta de entrada.
4. **SEQUEL, 1974** — Chamberlin y Boyce. La palabra clave del título es *English*: el lenguaje se diseñó para que lo escribiera alguien que no fuera programador. Ese era el objetivo declarado.
5. **La distinción que hace Chamberlin** — modelo relacional y sintaxis SQL son dos cosas separables, y él las separa. Reivindica la primera con más entusiasmo que la segunda.
6. **Por qué ganó igual** — la hipótesis: SQL no ganó por elegante sino por estándar. La portabilidad como propiedad de red; el costo de salida de los datos; treinta años de gente formada.
7. **NoSQL y el regreso** — la ola que lo iba a reemplazar terminó reimplementándolo encima. Lo que eso demuestra y lo que no.
8. **Yo y SQL** — la parte personal: la migración FoxBase→PG ([[H-07]]), Postgres en Docker ([[G-06]]), y si alguna vez vi cumplirse la promesa del *English*.
9. **Cierre** — el lenguaje que ganó sin querer: qué se aprende de un diseño que sobrevivió a su propio autor y a sus propias razones.

**Bibliografía:** _(reforzada el 2026-07-16; todas las fuentes marcadas «verificado» fueron fetcheadas)_

Fuentes primarias:

- **Codd 1970** — E. F. Codd, «A Relational Model of Data for Large Shared Data Banks», *Communications of the ACM*, vol. 13, núm. 6 (junio 1970), pp. 377–387. DOI canónico: [10.1145/362384.362685](https://doi.org/10.1145/362384.362685) — _verificado vía api.crossref.org_, _estable_. Texto libre (mirror del curso CIS 550, UPenn, full-text verificado): <https://www.engineering.upenn.edu/~zives/03f/cis550/codd.pdf> — _frágil_ (página de curso; conviene backup Wayback antes de publicar).
- **Chamberlin & Boyce 1974** — Donald D. Chamberlin y Raymond F. Boyce, «SEQUEL: A Structured English Query Language», en *Proceedings of the 1974 ACM SIGFIDET (now SIGMOD) Workshop on Data Description, Access and Control*, Ann Arbor, Michigan, mayo 1974, pp. 249–264. DOI canónico: [10.1145/800296.811515](https://doi.org/10.1145/800296.811515) — _verificado vía Crossref_, _estable_. **Nota:** ACM DL/Crossref etiquetan mal el contenedor como «FIDET '76 / 1976»; el paper, la ficha de IBM Research y la nota al pie 16 de la oral history de CHM confirman **1974**. Texto libre (PDF alojado por IBM, full-text verificado, 16 pp.): <https://s3.us.cloud-object-storage.appdomain.cloud/res-files/2705-sequel-1974.pdf> — _frágil_ (object storage; backup Wayback recomendado).
- **Oral History of Donald Chamberlin** ([[tr-11]], CHM) — entrevistado por Paul McJones, 21 de julio de 2009, Computer History Museum, Mountain View, CA. CHM Ref. X5374.2009. [Transcripción PDF](http://archive.computerhistory.org/resources/text/Oral_History/Chamberlin_Don/102702111.05.01.acc.pdf) — _full-text verificado_, _estable_ (archivo CHM). Fuente primaria que confirma: venue y fecha del paper SEQUEL (SIGFIDET, Ann Arbor, mayo 1974, pp. 249–264); la muerte de Ray Boyce (aneurisma cerebral, junio 1974, a los 27 años); el motivo del renombre («The word "SEQUEL" turned out to be somebody's trademark. So I took all the vowels out of it and turned it into SQL» — **sin nombrar a la empresa**); que Oracle (Relational Software Inc., de Larry Ellison) fue la primera implementación comercial de SQL, ganándole a IBM por un par de años; y la adopción posterior por ANSI/ISO.

Fuentes de Chamberlin sobre la historia de SQL (pagas / con challenge — se cita el DOI canónico):

- **Chamberlin 2012** — Donald D. Chamberlin, «Early History of SQL», *IEEE Annals of the History of Computing*, vol. 34, núm. 4 (2012), pp. 78–82. DOI: [10.1109/MAHC.2012.61](https://doi.org/10.1109/MAHC.2012.61) — _verificado vía Crossref_, _estable_. Paywall en IEEE Xplore; el mirror de Project MUSE exige challenge. No se pudo verificar un mirror libre confiable (los que circulan son scribd/researchgate/studocu, no citables).
- **Chamberlin 2024** — Donald Chamberlin, «50 Years of Queries», *Communications of the ACM*, vol. 67, núm. 8 (2024), pp. 110–121. DOI: [10.1145/3649887](https://doi.org/10.1145/3649887) — _verificado vía Crossref_, _estable_. Abierto en cacm.acm.org pero devuelve 403 al fetch automatizado.

Libro de entrevistas:

- **[[tr-23]] Masterminds** — Federico Biancuzzi y Shane Warden, *Masterminds of Programming: Conversations with the Creators of Major Programming Languages*, O'Reilly, 2009. ISBN 978-0-596-51517-1. [Ejemplar en archive.org](https://archive.org/details/MastermindsOfProgramming) (préstamo; texto **no fetcheable**). Capítulo de entrevista a Don Chamberlin: la cita textual central del post (separación modelo/sintaxis) y el número de capítulo/páginas siguen **pendientes de verificar contra el ejemplar**.

**Imágenes:** _a definir_

**Tags propuestos:** `['SQL','Chamberlin','IBM','historia','bases de datos']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le construyó el outline (9 puntos) y se escribió el borrador de prosa completo (~2200 palabras) al final del archivo.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 3 de 6 marcadores `[VERIFICAR:]`. Resueltos: la ficha completa de Codd 1970 (CACM 13(6), pp. 377–387, DOI 10.1145/362384.362685 + mirror UPenn) y de Chamberlin & Boyce 1974 (SIGFIDET, pp. 249–264, DOI 10.1145/800296.811515 + PDF libre de IBM), y la cronología de estandarización/comercialización (Oracle V2 jun-1979 primero; ANSI 1986 / ISO 1987). Se sumó como fuente primaria fetcheada la *Oral History of Donald Chamberlin* (CHM, 2009), que corrobora la muerte de Boyce, el motivo del renombre y la primacía comercial de Oracle. Siguen abiertos por depender de material no fetcheable: la cita textual central sobre la separación modelo/sintaxis (Masterminds, ejemplar de préstamo), el capítulo/páginas de esa entrevista, y el nombre de la empresa de la marca «Sequel» (ninguna fuente primaria la nombra; el dato «Hawker Siddeley» sólo aparece en fuentes secundarias).

Lo que quedó **escrito y cerrado**: el encuadre histórico a baja resolución (modelo primero, lenguaje después), el argumento central del post (SQL ganó como estándar, no como diseño), la sección sobre NoSQL y el cierre. Todo eso es argumentación y encuadre, y no depende de datos que la bibliografía no tenga.

Lo que quedó como **hueco (necesita a César)** — 7 marcadores:

1. Primer encuentro con SQL: cuándo, con qué motor, y si lo aprendió antes o después del modelo relacional.
2. Si en la formación le enseñaron álgebra relacional o directamente `SELECT`.
3. La migración FoxBase→PG en el Ministerio de Cultura de Santa Fe: qué se sintió al pasar de xBase a SQL ([[H-07]]).
4. Si alguna vez vio a un no-programador escribir SQL por su cuenta (la promesa original del paper).
5. Si hoy escribe SQL a mano o va por un ORM, y por qué ([[G-06]]).
6. Si está de acuerdo con la separación modelo/sintaxis que hace Chamberlin.
7. Qué es lo que puntualmente le molesta de SQL como lenguaje.

Lo que quedó como **`[VERIFICAR:]`** — 8 marcadores. Los importantes:

- **El Hook no está respaldado por la bibliografía tal como está.** El Hook afirma que en la entrevista Chamberlin dice «el modelo relacional sí, el SQL como sintaxis, no necesariamente». Esa es la afirmación que sostiene el post entero, y no hay transcripción a mano: sólo la referencia al libro ([[tr-23]]). La prosa está escrita **de modo que el argumento se sostenga aunque el matiz de la cita cambie** — el punto 5 atribuye la distinción con marcador de verificación explícito en vez de ponerla entre comillas. **Antes de publicar hay que abrir el capítulo de Chamberlin en *Masterminds* y citar textual, o reescribir el punto 5.** Es la deuda principal del draft.
- Faltan los datos de cita completos de Codd 1970 (revista, volumen, número, páginas, DOI) y de Chamberlin & Boyce 1974 (venue, actas), más las iniciales/nombre de pila de Codd. La bibliografía del draft trae sólo título y año.
- El rol de Ray Boyce, la relación SEQUEL→SQL (cambio de nombre), System R, la primera versión comercial y la cronología del estándar ANSI **no entraron al texto como afirmaciones**: no están en la bibliografía. Donde el hilo los pedía, están marcados. Si se los quiere afirmar, hay que verificarlos y agregar fuentes primero.
- La cuenta de «50 años» del Hook: el paper de SEQUEL es de 1974, así que en 2026 son 52. El texto usa «medio siglo largo» para no comprometerse; queda a decisión de César si el Hook redondea a propósito.

Antes de publicar: resolver la cita de Chamberlin, completar los huecos, y decidir imágenes (siguen `_a definir_`).

---

## Borrador de prosa

El paper que presentó SEQUEL al mundo es de 1974. Si hacés la cuenta desde ahí, el lenguaje que hoy llamamos SQL lleva medio siglo largo en producción[^sequel]. En ese lapso vimos nacer y morir la computadora personal como categoría, la burbuja punto com, tres o cuatro paradigmas de programación vendidos como definitivos, y una cantidad de tecnologías de datos que se anunciaron explícitamente como su reemplazo. Abajo de casi todo lo que usaste hoy —el homebanking, el sistema de la obra social, el carrito del supermercado, probablemente el CMS de este blog si tuviera base de datos— hay alguien mandando cadenas de texto que empiezan con `SELECT`.

Lo raro no es que haya durado. Las cosas duran. Lo raro es lo que pasa cuando le preguntás a Don Chamberlin, uno de los dos autores de aquel paper, qué opina del asunto. Un inventor cuyo invento gobernó la industria durante cincuenta años tiene todo el derecho a la vuelta olímpica. Chamberlin, en la entrevista que le hacen para *Masterminds of Programming*, no la da[^masterminds]. Y ese es el cuento que quiero contarte.

### El modelo vino antes que el lenguaje

Primero hay que separar dos cosas que la costumbre pegoteó hasta volverlas una sola.

En 1970, Edgar Codd publica en IBM un trabajo con un título que ya dice el programa entero: *A Relational Model of Data for Large Shared Data Banks*[^codd]. La palabra importante es **modelo**. Lo que Codd propone no es un producto ni una sintaxis: es una manera de pensar los datos. Los datos como relaciones, con una teoría matemática detrás que dice qué operaciones son legítimas y qué resultados producen. Y, sobre todo, una separación tajante entre cómo se describen los datos y cómo se guardan.

Esa separación es la joya. Antes, consultar una base de datos significaba saber cómo estaba organizada por dentro: navegar punteros, seguir cadenas, conocer el orden físico de los registros. El programa tenía cableada la forma del disco. Cambiabas el almacenamiento y se rompía el código. Codd dice: no, vos declarás qué datos querés, en términos del modelo lógico, y el sistema se arregla con el resto. Hoy suena obvio. Era una idea grande.

Y es —vale adelantarlo— la parte de todo este asunto que envejeció bien. Cincuenta años después, la crítica seria a las bases relacionales casi nunca es una crítica al modelo relacional. Es una crítica a otra cosa.

### El problema que tenía Codd

El modelo relacional tenía un defecto operativo: era hermoso e inaccesible.

Para consultar una relación en los términos de Codd hacía falta manejar el aparato formal que venía con el modelo. Y acá conviene ser preciso, porque la costumbre nos hizo decir mal esta parte durante años: lo que Codd propone en el paper del 70 **no es un álgebra**. La palabra «álgebra» no aparece ni una vez en esas once páginas. Lo que propone, en la sección que titula *Some Linguistic Aspects*, es «un sublenguaje de datos universal basado en un **cálculo de predicados aplicado**», y aclara que alcanza con uno de primer orden si las relaciones están en forma normal[^codd].

Es cierto que el paper también define operaciones sobre relaciones —permutación, proyección, join, composición, restricción—, pero conviene mirar para qué las pone: están en la sección de *redundancia y consistencia*, y el propio Codd escribe que «la mayoría de los usuarios no tendrían que ocuparse directamente de estas operaciones», que son cosa de los diseñadores del sistema[^codd]. O sea: ni siquiera las operaciones que hoy llamamos algebraicas estaban pensadas como la puerta de entrada del usuario.

Eso está muy bien para un paper y para un departamento de investigación de IBM, y está muy mal para que la idea salga al mundo. Un modelo de datos que sólo pueden interrogar quienes leen cuantificadores no es un modelo de datos: es un artículo de revista.

Así que si el modelo iba a servirle a alguien, necesitaba una puerta. Alguien tenía que construir la manija.

### 1974: la palabra clave del título es «English»

Ahí entran Don Chamberlin y Ray Boyce con *SEQUEL: A Structured English Query Language*[^sequel].

Fijate en el título, porque el título es la tesis de diseño. No dice «un lenguaje algebraico de consulta». Dice **structured English**. Inglés estructurado. Y el abstract lo dice todavía más claro: SEQUEL, escriben, identifica un conjunto de operaciones simples sobre estructuras tabulares «sin recurrir a los conceptos de variables ligadas y cuantificadores», con un poder demostrablemente equivalente al del cálculo de predicados de primer orden[^sequel]. Traducido: le sacamos el cálculo de encima al usuario y le dejamos la potencia.

¿Para quién? Acá no hay que interpretar nada, porque el paper nombra a la gente con nombre y apellido de oficio. Hay una clase de usuarios, dicen, que no son especialistas en computación pero estarían dispuestos a aprender a interactuar con un lenguaje de consulta no procedural de alto nivel: «ejemplos de tales usuarios son **contadores, ingenieros, arquitectos y urbanistas**. Es para esta clase de usuarios que SEQUEL está pensado»[^sequel]. El contador. Está literalmente en el paper, en la lista, primero.

La persona que sabe qué quiere saber y no sabe —ni tiene por qué saber— qué es un producto cartesiano.

Ese es el origen de todo lo que hoy nos parece raro de SQL. `SELECT nombre FROM empleados WHERE sueldo > 1000` no está escrito así porque sea la forma más limpia de expresar una proyección con selección. Está escrito así porque se lee casi en voz alta. Las palabras reservadas largas, el orden de las cláusulas que no coincide con el orden de evaluación, la vocación de oración en vez de fórmula: todo eso son decisiones al servicio de un objetivo que hoy nadie recuerda que existió.

Y acá conviene ser honesto: esa promesa no se cumplió. Pero no hace falta que lo diga yo, porque lo dice Chamberlin, y lo dice sin anestesia:

> «Ray y yo pensábamos que estábamos desarrollando un lenguaje que usarían principalmente "usuarios casuales" para hacer consultas ad hoc […]. Esperábamos ver SQL usado directamente por analistas financieros, urbanistas y otros profesionales que necesitaban acceso a los datos pero no querían escribir programas. **Estas expectativas resultaron demasiado optimistas.** Desde el comienzo, SQL fue usado principalmente por programadores entrenados. De hecho, con los años una gran cantidad de código SQL ha sido generada por herramientas automáticas, algo que no se previó en los primeros días.»[^masterminds]

El diseño ganó el mundo; el usuario para el que fue diseñado nunca apareció. Los contadores, los urbanistas y los arquitectos del paper del 74 terminaron mirando formularios con una base SQL atrás que nunca van a ver. En otro lugar de la misma entrevista lo dice más corto todavía: «probamos ser un poquito ingenuamente optimistas en nuestros objetivos del diseño original del lenguaje»[^masterminds].

> 🕳️ **HUECO — necesita a César:** ¿alguna vez viste, en la vida real, a un no-programador escribiendo SQL por su cuenta para responderse una pregunta? ¿Quién, y funcionó?

### Un paréntesis que duele: Ray Boyce

El paper de 1974 tiene dos firmas. La segunda casi no aparece en ninguna historia de SQL, y vale la pena decir por qué.

Boyce y Chamberlin trabajaban juntos en el centro de investigación de IBM en Yorktown Heights. Los dos fueron al simposio sobre el modelo relacional que Codd organizó ahí en 1972 — Chamberlin lo llama, sin ironía, una «experiencia de conversión». Después de eso los dos se engancharon en lo que Chamberlin describe como un «juego de consultas» (*query game*), desafiándose mutuamente a diseñar lenguajes lo bastante flexibles como para expresar todo tipo de preguntas. De ese juego salió SEQUEL. En 1973 los dos se mudaron a San José para sumarse al equipo de System R, y ahí su primera tarea fue diseñar el lenguaje de consulta del prototipo[^masterminds].

Y entonces:

> «Poco después de la publicación de aquel paper inicial, Ray Boyce murió repentina y trágicamente por los efectos de un aneurisma cerebral.»[^masterminds]

El paper es de mayo de 1974. Boyce alcanzó a publicar el diseño y no llegó a ver nada de lo que vino después: ni System R terminado, ni Oracle, ni el estándar, ni los cincuenta años. La «B» de la forma normal de Boyce-Codd es de él.

### De SEQUEL a SQL

El cambio de nombre sí ocurrió, y la razón está dicha por el autor en una sola línea: «El nombre del lenguaje se acortó de SEQUEL a SQL para evitar una infracción de marca registrada»[^masterminds].

Eso es todo lo que Chamberlin dice al respecto. Circula por internet una versión más detallada, con el nombre de la empresa británica que tendría registrada la marca «Sequel»; esa parte no la pude verificar en ninguna fuente primaria y no entra al post.

[VERIFICAR: qué marca registrada y de qué empresa forzó el acortamiento SEQUEL→SQL. **El motivo está confirmado por dos fuentes de Chamberlin**: la *Oral History* de CHM (2009, fetcheada y verificada) — «The word "SEQUEL" turned out to be somebody's trademark. So I took all the vowels out of it and turned it into SQL» — y el capítulo de *Masterminds* («to avoid a trademark infringement», cap. 10, p. 227 según el draft, pendiente de verificar contra el ejemplar). **Ninguna de las dos nombra a la empresa.** Fuentes secundarias (Wikipedia, citando a Oppel, *Databases Demystified*, 2004) atribuyen la marca «Sequel» a la británica *Hawker Siddeley Dynamics Engineering Limited*; **ninguna fuente primaria fetcheada lo confirma**, así que no entra al post como afirmación. Sigue pendiente conseguir «Early History of SQL» (IEEE Annals 34(4), 2012) o «50 Years of Queries» (CACM 67(8), 2024) por una vía que permita leer el texto, por si Chamberlin ahí sí nombra la empresa.]

### Lo que dice Chamberlin

Acá está el corazón del post, y acá es donde hay que pisar con cuidado.

Cuando a Chamberlin le preguntan por SQL en *Masterminds of Programming*, lo interesante es que no trata a SQL como un bloque. Distingue. Por un lado el modelo relacional, que defiende sin reservas: la idea de Codd le parece correcta, sigue siendo correcta, y es la razón por la que todo esto funcionó. Por el otro, la sintaxis concreta que él mismo diseñó, sobre la que se muestra bastante menos ceremonioso — como quien reconoce que ese pedazo particular fue producto de un momento, de un objetivo específico, y que rehecho hoy con lo que sabemos podría no ser eso[^masterminds].

[VERIFICAR: **esta es la afirmación central del post.** Hay que abrir el capítulo de Chamberlin en *Masterminds of Programming* (tr-23, [archive.org](https://archive.org/details/MastermindsOfProgramming)) y citar textual: qué dice exactamente sobre el modelo relacional, qué dice exactamente sobre la sintaxis de SQL, y con qué grado de reserva. El párrafo de arriba es la lectura que el draft hace de la entrevista, no una cita. Si el matiz es otro, se reescribe este punto — el resto del post se sostiene igual.]

Si esa lectura se confirma, el punto es más filoso de lo que parece. Estamos tan acostumbrados a que SQL *sea* lo relacional que perdimos de vista que son capas distintas: una teoría de datos, y una manera de tipear preguntas sobre esa teoría. Podés estar de acuerdo con la primera y encontrar mediocre a la segunda. De hecho es, probablemente, la postura mayoritaria entre quienes lo piensan un rato — sólo que casi nunca la decimos así de claro, y es raro y saludable escucharla del autor.

> 🕳️ **HUECO — necesita a César:** ¿estás de acuerdo con esa separación? ¿El modelo relacional te parece bien y la sintaxis mal, las dos bien, o tenés otra postura?

> 🕳️ **HUECO — necesita a César:** si tuvieras que nombrar **una** cosa puntual de SQL como lenguaje que te resulte francamente molesta, ¿cuál es? (Una, concreta, con ejemplo si tenés.)

### Entonces, ¿por qué ganó?

Si ni el autor lo defiende como pieza de diseño, la victoria pide explicación. Mi hipótesis es que SQL no ganó por ser bueno. Ganó por ser **el mismo en todos lados**.

Un lenguaje de consulta tiene una propiedad económica que un lenguaje de programación no tiene con la misma fuerza: es la interfaz de tus datos, y los datos son lo caro. El código lo reescribís. Los datos, no. Eso significa que la sintaxis con la que interrogás la base se convierte en un contrato de larguísimo plazo — más largo que la aplicación, que el framework de moda, y en muchos casos más largo que la empresa que la escribió.

Cuando una interfaz tiene ese peso, la propiedad que importa no es la elegancia: es que sea la misma que usa todo el mundo. Un motor nuevo que hable SQL entra al mercado con toda la gente ya entrenada, todas las herramientas ya escritas, todo el conocimiento ya acumulado. Un motor nuevo con un lenguaje mejor entra al mercado solo. Ese cálculo se hizo miles de veces en cincuenta años y dio SQL siempre.

Es la misma clase de victoria del teclado QWERTY, de las pulgadas en los caños, del ancho de vía. No es que sea lo óptimo. Es que reemplazarlo cuesta más de lo que rinde, todos los años, para siempre.

Las fechas sostienen el argumento. La primera implementación comercial de SQL no fue de IBM: fue **Oracle** —la V2, lanzada en junio de 1979 por Relational Software Inc., la empresa de Larry Ellison que antes se llamaba Software Development Laboratories—, que le ganó de mano a IBM por un par de años. El propio Chamberlin lo cuenta así en su historia oral: «fue la primera implementación comercial de SQL en salir al mercado»[^estandar]. Y la sintaxis se congeló como contrato cuando se volvió norma: **ANSI adoptó SQL como estándar en 1986 e ISO en 1987**[^estandar]. Desde entonces, cada motor nuevo que quiso jugar tuvo que hablar ese mismo idioma.

### La ola que se lo iba a llevar puesto

Hace unos años esto que estoy diciendo era una opinión perdedora. Estaba NoSQL, estaba MapReduce, estaba el consenso de que el modelo relacional era una reliquia de una época en que el disco era caro y los datos, chicos.

Lo que pasó después es cómico y merece su propio post. La mayoría de esos sistemas, a medida que maduraron y se les pidió hacer cosas serias, fueron incorporando: un lenguaje de consulta declarativo, tipos, esquemas, y garantías transaccionales. Cada uno por su camino, cada uno con su nombre propio, y muchos terminaron ofreciendo directamente una capa que habla SQL encima del motor que había venido a reemplazarlo.

No quiero sacar de ahí más conclusión de la que aguanta. Esto **no** demuestra que SQL sea óptimo, ni que el modelo relacional sea la última palabra en datos. Hay problemas —grafos, series temporales, documentos anidados— donde otro modelo es genuinamente mejor, y no es una concesión decirlo. Lo que sí demuestra es más modesto y más interesante: que cuando construís un sistema de datos y lo dejás madurar bajo presión real, terminás necesitando casi todo lo que la gente de los setenta ya había descubierto que hacía falta. La rueda vuelve a salir redonda.

Y el mérito de eso, ojo, es del modelo de Codd. No de la sintaxis de Chamberlin. La distinción del punto anterior es exactamente lo que permite entender esta parte.

### Yo y SQL

> 🕳️ **HUECO — necesita a César:** ¿cuándo escribiste tu primer `SELECT`, con qué motor, y en qué contexto (facultad, laburo, curiosidad)?

> 🕳️ **HUECO — necesita a César:** en tu formación, ¿te enseñaron primero el modelo relacional (álgebra, normalización) y después SQL, o te tiraron directamente el `SELECT` y el modelo vino después —o nunca—?

Hay un momento de mi historia laboral que viene justo al caso, porque fue exactamente el salto del que habla este post: pasar de un mundo donde para consultar tenías que saber cómo estaban guardadas las cosas, a uno donde declarás qué querés. La migración de FoxBase a PostgreSQL en el Ministerio de Cultura de Santa Fe ([[H-07]]) fue eso, de un lado del abismo al otro, con datos reales adentro.

> 🕳️ **HUECO — necesita a César:** en esa migración, ¿qué se sintió pasar de xBase a SQL? Concretamente: ¿qué se volvió trivial y qué se volvió más difícil que antes?

Y del otro extremo de la línea de tiempo: hoy levantar un Postgres es un `docker compose up` ([[G-06]]), el motor está a un comando de distancia, y la pregunta ya no es si tenés base sino cómo le hablás.

> 🕳️ **HUECO — necesita a César:** hoy, en tus proyectos, ¿escribís SQL a mano o pasás por un ORM? ¿Y esa decisión fue deliberada o por inercia de la herramienta?

### El lenguaje que ganó sin querer

Me quedo con esto.

SQL es un lenguaje diseñado para un usuario que nunca llegó, con una sintaxis que su propio autor mira con distancia, montado sobre una teoría que casi nadie discute, que sobrevivió a cinco décadas de intentos de reemplazo y que probablemente nos sobreviva a todos los que estamos leyendo esto. Ganó por razones que no tienen casi nada que ver con las razones por las que se lo diseñó.

Hay una tentación de leer eso como una historia triste — la mediocridad venciendo a la elegancia, otra vez. No la leo así. La leo como el recordatorio más honesto que tenemos de qué es lo que realmente sobrevive en este oficio: no lo mejor, sino lo que resuelve un problema real lo suficientemente temprano y lo suficientemente bien como para que reemplazarlo nunca valga la pena. SEQUEL le dio a la idea de Codd una puerta por la que salir al mundo. Que la manija estuviera un poco torcida importó muchísimo menos de lo que la teoría de diseño de lenguajes hubiera predicho.

Chamberlin, medio siglo después, parece saberlo mejor que nadie.

[^masterminds]: Federico Biancuzzi y Shane Warden, *Masterminds of Programming*, O'Reilly, 2009 (ISBN 978-0-596-51517-1) — capítulo de entrevista a Don Chamberlin. [Ejemplar en archive.org](https://archive.org/details/MastermindsOfProgramming) (préstamo; texto no fetcheable). Las citas de este capítulo (muerte de Boyce, renombre SEQUEL→SQL, expectativas del diseño) están **corroboradas de forma independiente** por la *Oral History of Donald Chamberlin* (CHM, 21-jul-2009, [PDF](http://archive.computerhistory.org/resources/text/Oral_History/Chamberlin_Don/102702111.05.01.acc.pdf)), fetcheada y verificada el 2026-07-16. [VERIFICAR: número de capítulo y páginas exactas de la entrevista dentro del libro — no fue posible fetchear el ejemplar.]
[^codd]: E. F. Codd, «A Relational Model of Data for Large Shared Data Banks», *Communications of the ACM*, vol. 13, núm. 6 (junio 1970), pp. 377–387. DOI: [10.1145/362384.362685](https://doi.org/10.1145/362384.362685) (verificado vía api.crossref.org, 2026-07-16). Texto libre (mirror curso CIS 550, UPenn, full-text verificado): <https://www.engineering.upenn.edu/~zives/03f/cis550/codd.pdf> (_frágil_).
[^sequel]: Donald D. Chamberlin y Raymond F. Boyce, «SEQUEL: A Structured English Query Language», en *Proceedings of the 1974 ACM SIGFIDET (now SIGMOD) Workshop on Data Description, Access and Control*, Ann Arbor, Michigan, mayo 1974, pp. 249–264. DOI: [10.1145/800296.811515](https://doi.org/10.1145/800296.811515) (verificado vía Crossref; el contenedor aparece mal fechado como 1976 en ACM DL — es 1974). Texto libre (PDF alojado por IBM, full-text verificado): <https://s3.us.cloud-object-storage.appdomain.cloud/res-files/2705-sequel-1974.pdf> (_frágil_). La lista de usuarios previstos («accountants, engineers, architects, and urban planners») fue verificada contra este PDF.
[^estandar]: Cronología verificada el 2026-07-16. Oracle como primera implementación comercial de SQL: *Oral History of Donald Chamberlin* (CHM, 2009; ver Bibliografía) — «it was the first commercial implementation of SQL to go on the market… delivered by Larry Ellison's company». La versión y fecha (Oracle V2, junio 1979, Relational Software Inc.) y los años de estandarización (ANSI 1986, ISO 1987) provienen de [SQL — Wikipedia](https://en.wikipedia.org/wiki/SQL) (fuente secundaria; Chamberlin confirma en la historia oral la adopción por ANSI/ISO, pero sin dar el año). El detalle fino de las revisiones (SQL-89, SQL-92, etc.) queda pendiente si el post llega a necesitarlo.
