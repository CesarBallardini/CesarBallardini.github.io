### A2-01 — SICP en castellano (y los videos del 80)

- **Archivo seed:** `dev/draft-sicp-en-castellano.md`
- **Slug propuesto:** `sicp-en-castellano-videos-del-80`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-sicp-en-castellano-videos-del-80/index.md`
- **Serie:** A2
- **Cross-links:** depende de [[tr-03]]; lleva a [[A2-02]] (Scheme papers), [[B-01]] (listas infinitas), [[E-08]] (libros que me hicieron programador)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-1800 palabras)

**Concepto:** SICP es probablemente el mejor libro de CS jamás escrito, y los vídeos de Abelson y Sussman de 1986 muestran cómo *enseñarlo*. El problema: en castellano hay poco. Este post es un mapa de qué hay disponible para alguien que no lee inglés, más mi propio side project para ayudar a cerrar la brecha.

**Hook:** "Hace 40 años, dos profesores del MIT explicaban en cámara cómo construir un evaluator de Scheme en 20 minutos. La grabación está completa en YouTube. ¿Por qué no es lectura/visionado obligatorio en toda carrera de software?"

**Outline:**
1. Qué es SICP, por qué importa, por qué no es solo "el libro de Scheme".
2. Los vídeos del MIT 6.001 (1986, en Hewlett-Packard): Abelson y Sussman explicando, en pizarra, los capítulos 1-5.
3. Las traducciones al español: la traducción "oficial" del capítulo 1 (UPV), la traducción incompleta, la versión interactiva online, el JS Self Bowl.
4. Mi side project: notas en castellano siguiendo el ritmo del libro, en GitHub. Por qué lo empecé y dónde está.
5. Cierre: qué *no* hay (un audio en castellano, una versión Racket-friendly) y a quién haría falta involucrar.

**Bibliografía:**
- [[tr-03]] — *SICP*, MIT Press 2.ª ed. 1996; texto libre bajo CC BY-SA 4.0 (confirmado 2026-07-16 en la [web oficial del MIT](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html)). — estable.
- [SICP en HTML interactivo](https://sarabander.github.io/sicp/) — edición web de Andres Raba (usuario GitHub «sarabander»), 2.ª ed., bajo CC BY-SA 4.0; nombre y licencia confirmados en el [repo](https://github.com/sarabander/sicp). La mejor versión web del libro. — estable.
- [MIT 6.001 — página del CSAIL sobre los vídeos de Abelson y Sussman](https://groups.csail.mit.edu/mac/classes/6.001/abelson-sussman-lectures/) — página de presentación; confirma «twenty video lectures … given in July 1986 for Hewlett-Packard employees, and professionally produced by Hewlett-Packard Television». — estable.
- [MIT OpenCourseWare — Video Lectures del 6.001 (Spring 2005)](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/) — aloja las 20 clases (1A–10B) de Abelson y Sussman con transcripción en PDF; el curso de 2005 lo dictaron Grimson, Szolovits y Darrell, pero los vídeos son los de 1986. — estable.
- [Internet Archive — MIT 6.001 SICP 1986](https://archive.org/details/MIT_Structure_of_Computer_Programs_1986) — las 20 clases descargables (MPEG4/OGG) con subtítulos SubRip; CC BY-NC-SA 3.0. Backup estable de los vídeos. — estable.
- [SICP — playlist en YouTube](https://www.youtube.com/playlist?list=PLE18841CABEA24090) — copia de conveniencia; no verificable por fetch (SPA), usar el OCW/Internet Archive como referencia canónica. — frágil.
- [Composing Programs (Berkeley CS61A)](https://www.composingprograms.com/) — adaptación en Python por John DeNero. — estable.
- [SICP JavaScript Edition / Comparison Edition](https://sicp.sourceacademy.org/) — adaptación a JavaScript por Martin Henz y Tobias Wrigstad (con Julie Sussman), CC BY-SA 4.0; en inglés. — estable.
- [fedehc, *SICP-ES*](https://github.com/fedehc/SICP-ES) — traducción al español de la 2.ª ed. iniciada en 2019; sólo el capítulo 1 quedó completo; repo archivado (read-only) el 2022-11-07. — estable (archivado).
- [SICP capítulo 1 traducido al castellano (UPV)](https://web.archive.org/web/20140126180939/http://www.gris.disca.upv.es/asignaturas/iped/sicp.pdf) — sólo en Wayback; traductor y año sin confirmar (PDF no fetcheable). — frágil.
- [Anarcat, *SICP study notes*](https://anarc.at/sicp/) — referencia útil. — frágil (sitio personal).
- Mi propio repo en GitHub (🕳️ necesita a César: slug exacto — ver `**Estado actual:**`).

**Imágenes:**
- _Crear_: screenshot del SICP en HTML interactivo abierto en un capítulo característico (5 min).
- _Crear_: still frame del vídeo de Abelson y Sussman en la pizarra (con atribución a MIT — uso justo / educativo).

**Tags propuestos:** `['SICP', 'Scheme', 'MIT', 'Abelson', 'Sussman', 'pedagogia']`

**Estado actual:** prosa completa escrita contra el outline de 5 puntos (~1.650 palabras, dentro del target medium). Lo que está escrito: el encuadre de qué es SICP y por qué no es «el libro de Scheme», la sección de los vídeos del 6.001, el mapa de qué hay en castellano (UPV, Sarabander, Composing Programs, anarcat) y el cierre sobre lo que falta.

Lo que quedó como hueco y bloquea la publicación:

- **El repo propio (sección 4 del outline) es casi todo huecos.** El draft dice «existe un repo personal en GitHub» pero no da slug, ni fecha de inicio, ni alcance, ni motivo. Sin eso, esa sección no se puede escribir: son 6 huecos marcados.
- **La relación de César con el libro y los vídeos** (cuándo lo leyó, en qué idioma, si llegó al capítulo 4, si usó la traducción de la UPV) — 4 huecos más.
- **Hechos de la sección de vídeos:** la fecha 1986, el rol de Hewlett-Packard, la cobertura capítulos 1-5 y el «evaluator en 20 minutos» del Hook vienen del seed, no de la bibliografía. Van marcados `[VERIFICAR:]` — hay que mirar la página del CSAIL y la playlist antes de afirmarlos.
- **«La traducción incompleta» y «el JS Self Bowl»** aparecen en el outline sin entrada en la bibliografía. Escribí alrededor de eso con `[VERIFICAR:]`; si no aparecen las fuentes, esos dos ítems se caen del post.

Pendiente además: las dos imágenes (screenshot de Sarabander + still frame de la pizarra) siguen sin crear.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 3 de 8 marcadores [VERIFICAR:], más uno parcial. Resueltos: el evaluador metacircular ocupa las clases 7A y 7B (OCW); la 2.ª ed. liberada por el MIT está bajo CC BY-SA 4.0 y permite derivados; la edición web «Sarabander» es de Andres Raba. Parcial: se confirmó una traducción incompleta al español (fedehc/*SICP-ES*, 2019, sólo capítulo 1, archivada 2022-11-07), pero «el JS Self Bowl» del seed sigue sin fuente. Sin resolver (no fetcheables / requieren mirar el vídeo): la playlist de YouTube, quién habla y el disfraz de mago en 1A, y el traductor/año/alcance de la traducción de la UPV (el PDF de la Wayback no es fetcheable). Nuevos datos verificados agregados a la bibliografía: la página del CSAIL, la galería de vídeos del OCW, el ítem descargable del Internet Archive (CC BY-NC-SA 3.0) y la *SICP JavaScript Edition* de Henz y Wrigstad. Hallazgo colateral para César, no incorporado por ser HUECO: una búsqueda devolvió el repo `github.com/CesarBallardini/sicp-spanish` («Traducción al castellano de SICP»), que podría ser el «repo propio» de la sección 4 — confirmarlo vos.

---

## Borrador de prosa

Hace cuarenta años —julio de 1986, exactamente[^csail]—, dos profesores del MIT se pararon frente a una pizarra, con una cámara encendida, y explicaron cómo construir un intérprete de Scheme. No en un cuatrimestre: en dos clases —la 7A y la 7B del listado del OpenCourseWare, que son las que arman el evaluador metacircular.[^ocwvideos] (El «en 20 minutos» del Hook es licencia retórica: lo que entra en esas dos clases es el intérprete entero, no un cronómetro.) La grabación completa está libre: el MIT OpenCourseWare la publica entera, con transcripciones,[^ocwvideos] y el Internet Archive tiene una copia descargable de las veinte clases.[^iavideos] El libro que acompaña esas clases también está libre.[^sicp] Y sin embargo, si vos estudiaste software en castellano, hay muchas chances de que nunca te lo hayan hecho leer.

Ese hueco me da vueltas hace rato, y este post es mi intento de mapearlo: qué es *Structure and Interpretation of Computer Programs*, por qué esos vídeos siguen siendo lo mejor que hay para aprender a *enseñar* programación, qué existe en castellano — que es poco — y qué estoy haciendo yo, modestamente, para que sea un poquito menos poco.

### No es «el libro de Scheme»

El primer malentendido que hay que sacarse de encima: SICP no es un libro para aprender Scheme. Scheme es el vehículo, y está elegido justamente porque se aprende en veinte minutos y después desaparece del camino. Abelson y Sussman lo dicen sin vueltas en el «Preface to the First Edition»: el material esencial de una materia de este nivel «no es la sintaxis de construcciones particulares de un lenguaje de programación, ni algoritmos ingeniosos para computar funciones particulares con eficiencia, ni siquiera el análisis matemático de algoritmos y los fundamentos de la computación, sino más bien las técnicas usadas para controlar la complejidad intelectual de sistemas de software grandes».[^prefacio] En el mismo párrafo va la frase que todo el mundo cita de memoria: «los programas deben escribirse para que los lean personas, y sólo incidentalmente para que las máquinas los ejecuten». Lo que el libro enseña es **cómo controlar la complejidad**: abstracción por procedimientos, abstracción por datos, estado y asignación, evaluación como proceso, y finalmente la construcción de máquinas que ejecutan lenguajes.

Esa progresión es lo que lo hace distinto de cualquier manual. Un libro de Java te enseña Java. SICP te enseña que un lenguaje de programación es un objeto que vos podés construir, modificar y razonar sobre él — y te lo demuestra construyendo uno adelante tuyo, con las mismas herramientas que venías usando para calcular raíces cuadradas en el capítulo 1. Cuando llegás al metacircular evaluator, la sensación no es «ah, aprendí una técnica»; es que se te corre el piso. El intérprete que estuviste usando todo el libro resulta ser un programa más, de una carilla, escrito en el lenguaje que interpreta.

Por eso lo cito en este blog cada vez que puedo, y por eso aparece en la lista de los libros que me hicieron programador ([[E-08]]). Las listas infinitas y los streams del capítulo 3 tienen su propio post ([[B-01]]), y los papers de Scheme que están debajo de todo esto, el suyo ([[A2-02]]).

> 🕳️ **HUECO — necesita a César:** ¿cuándo leíste SICP por primera vez, en qué edición y en qué idioma? ¿Fue por una materia, por recomendación de alguien, o lo encontraste solo?

> 🕳️ **HUECO — necesita a César:** ¿hasta dónde llegaste en ese momento? ¿Llegaste al capítulo 4 (el metacircular evaluator) o te quedaste antes? Si te quedaste, ¿en qué te trabaste?

### Los vídeos del 6.001

Ahora, la parte que menos gente conoce. En julio de 1986, Abelson y Sussman dictaron el 6.001 en una versión especial grabada **para empleados de Hewlett-Packard**, y producida profesionalmente por Hewlett-Packard Television. La frase del MIT es literal: «given in July 1986 for Hewlett-Packard employees, and professionally produced by Hewlett-Packard Television».[^csail] Es decir: no fue un curso patrocinado ni grabado de casualidad en instalaciones ajenas — fue un curso de capacitación corporativa, filmado por la televisión interna de HP, que terminó siendo el material didáctico de CS más reproducido de la historia.

Son exactamente veinte clases, numeradas 1A a 10B,[^ocwvideos] y sí cubren el arco completo del libro hasta el capítulo 5: arrancan en «Overview and Introduction to Lisp» y terminan en «Compilation» y «Storage Allocation and Garbage Collection», pasando por el metacircular evaluator (7A y 7B), logic programming (8A y 8B) y las register machines (9A y 9B).[^ocwvideos]

Dónde están hoy: la página del CSAIL sigue siendo la referencia de la que todos parten, pero es apenas una página de presentación — no tiene ni los vídeos ni transcripciones ni slides, sólo texto y un link.[^csail] Los vídeos y las transcripciones (un PDF por clase) están en el MIT OpenCourseWare, colgados —confusamente— de la página del 6.001 de *Spring 2005*.[^ocwvideos] Ojo con esto, porque es una trampa fácil: ese curso de 2005 lo dictaron Grimson, Szolovits y Darrell, pero los vídeos que el OCW publica ahí son los de Abelson y Sussman de 1986. El Internet Archive tiene además las veinte clases descargables.[^iavideos] Y hay copias en YouTube [VERIFICAR: el draft citaba la playlist `PLE18841CABEA24090`; WebFetch sobre YouTube devuelve el shell de la SPA y no permite confirmar ni el título, ni el dueño, ni la cantidad de vídeos. No citar esa playlist sin abrirla a mano; el Internet Archive y el OCW cubren la misma función y son estables].

Lo que hace especial a la versión del 80 no es el contenido — el contenido está en el libro. Es *la actuación*. La clase 1A abre con un profesor diciendo que el nombre de la materia es un desastre: «Computer science is a terrible name for this business. First of all, it's not a science. It might be engineering or it might be art, but we'll actually see that computer so-called science actually has a lot in common with magic».[^ocw1a] Y no es un chiste suelto: unos minutos después define proceso como «a magical spirit that sort of lives in the computer and does something», procedimiento como el «pattern of rules» que lo dirige — «procedures are the spells, if you like, that control these magical spirits that are the processes» — y remata que los hechiceros de verdad usan arcadio o sumerio, mientras que «we're going to conjure our spirits in a magical language called Lisp».[^ocw1a] Abelson explica recursión caminando alrededor de la pizarra como si el proceso de evaluación fuera algo que se puede señalar con el dedo. No hay slides con bullets. No hay «objetivos de aprendizaje». Hay dos tipos que entienden algo profundamente y que están genuinamente entusiasmados de mostrártelo.

Eso es lo que te llevás de ver los vídeos, y es la razón por la que se los recomiendo a docentes más que a estudiantes: es un curso de pedagogía disfrazado de curso de programación.

> ⚠️ **Corrección de la pasada de fuentes (2026-07-15).** El párrafo anterior decía: «Sussman entra en cámara vestido de mago, con capa y sombrero, y dice que la programación de computadoras no es magia». Leí la transcripción completa de la clase 1A que publica el OCW (18 páginas, PDF)[^ocw1a] y **dice lo contrario**: el profesor sostiene que la CS «has a lot in common with magic», y desarrolla la metáfora de los conjuros durante varios minutos. La frase «no es magia» no aparece; lo que sí aparece es «it's not a science». Reescribí el párrafo con las citas textuales.
>
> [VERIFICAR: quedan dos cosas sin resolver. (1) **Quién habla en 1A.** La transcripción del OCW rotula todo como «PROFESSOR» sin nombre, y la ficha del OCW acredita la clase a «Hal Abelson and Gerald Jay Sussman» juntos, sin desagregar. La atribución habitual del monólogo del mago es a Abelson, pero no la pude confirmar en fuente primaria — no escribir «Sussman dice» ni «Abelson dice» sin mirar el vídeo. (2) **El disfraz de mago.** Una transcripción registra habla, no vestuario, así que su silencio no prueba nada. Busqué en la página del CSAIL, en la ficha del OCW de 1A y en el ítem del Internet Archive: ninguno describe el vestuario. Si el gag existe, hay que ubicarlo mirando el vídeo y anotar el minutaje; si no aparece, el detalle se cae.]

> 🕳️ **HUECO — necesita a César:** ¿viste los vídeos completos? ¿Cuándo, y en qué formato los conseguiste la primera vez (YouTube, descarga, DVD)? Una frase sobre en qué circunstancia los mirabas le da carne a esta sección.

> 🕳️ **HUECO — necesita a César:** ¿hay una escena puntual de los vídeos que te haya quedado grabada? Si tenés una, la cito con el minutaje.

### Qué hay en castellano (spoiler: poco)

Acá viene la parte incómoda. Si no leés inglés con comodidad, tu acceso a SICP es esencialmente:

**La traducción del capítulo 1 de la UPV.** Existe un PDF con el capítulo 1 traducido al castellano, de la Universitat Politècnica de València.[^upv] Es la traducción más citada en el mundo hispanohablante y es honesta y legible. El problema es doble: llega hasta el capítulo 1 [VERIFICAR: abrir el PDF de la Wayback y confirmar el alcance real — ¿es sólo el capítulo 1 o hay más?] y el original ya no está en línea; sobrevive en la Wayback Machine. Un recurso educativo que depende de que el Internet Archive siga en pie no es una base sólida para una carrera de grado.

**Una traducción parcial más: *SICP-ES*, de fedehc.** Existe una traducción al español de la 2.ª edición, iniciada en 2019, de la que quedó completo sólo el capítulo 1; el repositorio fue archivado (read-only) en noviembre de 2022.[^fedehc] Es el mismo patrón que la UPV: alguien arranca en serio, traduce el capítulo 1 —lo más difícil, donde se fija el vocabulario— y el resto queda pendiente. [VERIFICAR: el seed mencionaba además «el JS Self Bowl» sin fuente, y no encontré ningún recurso con ese nombre. Lo más cercano y real es la *SICP JavaScript Edition* de Martin Henz y Tobias Wrigstad,[^sicpjs] pero no puedo afirmar que el seed se refiriera a eso. Confirmar con César qué era «el JS Self Bowl», o sacarlo del post.]

**Y después, inglés.** La mejor versión del libro para leer hoy es la de Andres Raba, en HTML, con tipografía cuidada, matemática bien renderizada y navegación decente.[^sarabander] Es hermosa. Está en inglés.

Hay un desvío interesante: *Composing Programs*, de John DeNero, en Berkeley, que reescribe la primera mitad de SICP en Python para el curso CS61A.[^composing] Baja muchísimo la barrera de entrada — todo el mundo lee algo de Python — pero paga un precio: sin el sustrato de Lisp, el capítulo del evaluator ya no es el mismo golpe. Igual está en inglés.

Y para el que quiere hacer los ejercicios con compañía, las notas de estudio de anarcat son un buen mapa de las trampas del camino.[^anarcat] También en inglés.

El resultado neto: un estudiante hispanohablante que quiera hacer SICP en serio necesita, primero, un nivel de inglés técnico que la carrera no le exige y a veces no le da. Eso no es un detalle de comodidad. Es un filtro.

### Mi granito de arena

> 🕳️ **HUECO — necesita a César:** esta sección entera depende de vos. El draft dice que tenés un repo en GitHub con notas de SICP en castellano, pero no tengo el slug. ¿Cuál es la URL exacta?

> 🕳️ **HUECO — necesita a César:** ¿qué es exactamente el repo? ¿Notas tuyas de lectura, traducción del texto, resoluciones de ejercicios comentadas, o una mezcla? El post necesita una frase que lo describa sin prometer de más.

> 🕳️ **HUECO — necesita a César:** ¿cuándo lo empezaste y qué te disparó empezarlo? (¿Alguien te preguntó por material en castellano? ¿Te frustraste con lo que había? ¿Era una excusa para releerlo?)

> 🕳️ **HUECO — necesita a César:** ¿hasta dónde llegó? ¿Qué capítulos están cubiertos hoy y cuáles no?

> 🕳️ **HUECO — necesita a César:** ¿en qué implementación corrés los ejercicios — MIT Scheme, Racket, Guile, otra? Y si elegiste una, ¿por qué esa?

> 🕳️ **HUECO — necesita a César:** ¿está abierto a contribuciones? ¿Querés que el post invite a mandar pull requests, o preferís que quede como un cuaderno personal público?

Lo que sí puedo escribir sin consultarte: un proyecto así no compite con nada. No es una traducción oficial, no tiene el permiso de MIT Press, no tiene un calendario. Es un cuaderno público. La apuesta es que un cuaderno público en castellano vale más que un cuaderno privado perfecto, y que si alguien busca en su idioma y encuentra *algo*, ya es mejor que encontrar nada.

### Lo que falta

Termino con la lista de lo que no existe y me gustaría que existiera:

- **El libro completo en castellano**, traducido con criterio y mantenido. Es trabajo de años y de más de una persona. La licencia lo permite: la edición liberada por el MIT está bajo Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), que autoriza obras derivadas —traducciones incluidas— con atribución y misma licencia.[^sicp]
- **Los vídeos subtitulados en castellano.** Esto sí es abordable: son subtítulos, no doblaje, y hay transcripciones en inglés de las que partir.[^videos] Una cátedra con veinte estudiantes lo hace en un cuatrimestre.
- **Una versión de los ejercicios que corra en Racket sin fricción**, para no perder gente en el paso de instalar MIT Scheme.

Ninguna de las tres necesita permiso de nadie salvo la licencia. Necesitan a alguien que las empiece.

> 🕳️ **HUECO — necesita a César:** ¿querés cerrar el post con un llamado concreto (a cátedras argentinas, a algún grupo de usuarios) o con algo más personal? Y si hay una cátedra o persona a la que le pondrías esto adelante, ¿cuál?

[^sicp]: Harold Abelson & Gerald Jay Sussman, *Structure and Interpretation of Computer Programs*, MIT Press, 2.ª ed. 1996. [Versión libre](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html), [PDF](https://web.mit.edu/6.001/6.037/sicp.pdf) y [vídeos del 6.001 (Spring 2005) en MIT OCW](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/).
[^videos]: [MIT 6.001, clases con Abelson y Sussman](https://groups.csail.mit.edu/mac/classes/6.001/abelson-sussman-lectures/) — las grabaciones canónicas, con transcripciones.
[^playlist]: [SICP — playlist completa en YouTube](https://www.youtube.com/playlist?list=PLE18841CABEA24090).
[^sarabander]: [SICP en HTML interactivo](https://sarabander.github.io/sicp/) — edición web de Andres Raba (usuario GitHub «sarabander»), 2.ª ed., bajo CC BY-SA 4.0; nombre y licencia confirmados en el [repositorio](https://github.com/sarabander/sicp).
[^composing]: [*Composing Programs*](https://www.composingprograms.com/) — adaptación de SICP a Python por John DeNero para CS61A, Berkeley.
[^upv]: [SICP, capítulo 1, traducido al castellano (UPV)](https://web.archive.org/web/20140126180939/http://www.gris.disca.upv.es/asignaturas/iped/sicp.pdf) — el original ya no está en línea; el enlace es a la Wayback Machine. [VERIFICAR: identificar quién hizo la traducción y en qué año, si el PDF lo dice.]
[^anarcat]: [Anarcat, *SICP study notes*](https://anarc.at/sicp/).
[^csail]: [MIT 6.001 — Structure and Interpretation of Computer Programs, Video Lectures](https://groups.csail.mit.edu/mac/classes/6.001/abelson-sussman-lectures/) (CSAIL). Confirma textualmente: «twenty video lectures by Hal Abelson and Gerald Jay Sussman … given in July 1986 for Hewlett-Packard employees, and professionally produced by Hewlett-Packard Television». Es una página de presentación: reenvía al MIT OpenCourseWare para ver los vídeos.
[^ocwvideos]: [Video Lectures — 6.001 SICP (Spring 2005), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/). Aloja las 20 clases (1A a 10B) de Abelson y Sussman con transcripción en PDF por clase. El curso de 2005 lo dictaron Grimson, Szolovits y Darrell, pero los vídeos publicados ahí son los de 1986; el OCW aclara que se basan en la 1.ª edición (1985) del libro.
[^iavideos]: [MIT 6.001 SICP 1986 — Internet Archive](https://archive.org/details/MIT_Structure_of_Computer_Programs_1986). Las 20 clases descargables (MPEG4 ~2,9 GB, OGG) con subtítulos SubRip; licenciadas CC BY-NC-SA 3.0 por Abelson y Sussman. Backup estable de los vídeos.
[^fedehc]: [fedehc, *SICP-ES*](https://github.com/fedehc/SICP-ES) — traducción al español de la 2.ª edición, iniciada en 2019 a partir del sitio oficial del MIT; quedó completo sólo el capítulo 1. El repositorio fue archivado (read-only) por su autor el 2022-11-07.
[^sicpjs]: [*Structure and Interpretation of Computer Programs — JavaScript Edition*](https://sicp.sourceacademy.org/) — adaptación a JavaScript por Martin Henz y Tobias Wrigstad, con Julie Sussman; texto libre en inglés bajo CC BY-SA 4.0 (código GPLv3).

