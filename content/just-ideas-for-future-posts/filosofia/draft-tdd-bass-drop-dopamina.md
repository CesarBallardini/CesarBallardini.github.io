### C-04 — TDD bass drop: cuando el test rojo te da dopamina

- **Archivo seed:** `dev/tdd-bass-drop-snl.md`
- **Slug propuesto:** `tdd-bass-drop-dopamina`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-tdd-bass-drop-dopamina/index.md`
- **Serie:** C
- **Cross-links:** depende de [[tr-08]] (Beck, TDD by Example); lleva a [[C-03]] (Tidy First, mismo autor), [[E-06]] (memoir: cómo enseñé TDD en clase 2020 de Paradigmas)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** short (800-1200 palabras)

**Concepto:** TDD no se vende bien explicando "calidad" o "regresión". Se vende contando que el ciclo *red → green → refactor* es un loop de recompensa pequeño y constante, como un bass drop en una canción de Saturday Night Live: cada test que pasa es una micro-descarga de dopamina. El que practica TDD no lo hace por disciplina; lo hace porque se siente bien.

**Hook:** "TDD se enseña como si fuera medicina: amargo pero te hace bien. Está mal vendido. TDD se siente como un sketch de Saturday Night Live con bass drops cada 30 segundos. Te das cuenta cuando lo practicás dos semanas y empezás a *querer* escribir el test antes que el código, no porque sos disciplinado, sino porque querés el bajo."

**Outline:**
1. El sketch de SNL del bass drop (tengo que verificar exactamente cuál es — anotación para mí mismo).
2. La analogía: red bar / green bar / commit. Cada green es un bass drop pequeño.
3. La explicación neurológica honesta — el ciclo de recompensa variable de Skinner y Csíkszentmihályi (flow). Sin pretensión de ser psicólogo.
4. Por qué esto explica la diferencia entre quien probó TDD y dejó vs quien lo adoptó: los primeros no completaron el ciclo lo suficiente como para que el cerebro lo registre como recompensa.
5. Anécdota de la clase de Paradigmas 2020 — qué pasó cuando los alumnos vieron una sesión de TDD live coding por primera vez.
6. Cierre: el truco para "engancharte" — empezá con un bug que ya tenés, escribí el test que lo reproduce, mirá la barra roja, arreglalo, mirá la barra verde. Eso es todo.

**Bibliografía:**

_(Pasada de fuentes 2026-07-15: todas las URLs de abajo fueron fetcheadas y confirmadas una por una, salvo donde se aclara lo contrario. Flag de bitrot en cada entrada.)_

- [[tr-08]] — Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley, 2002 (para los fundamentos). Hay copia en archive.org en **préstamo controlado**: [testdrivendevelo0000beck](https://archive.org/details/testdrivendevelo0000beck) — ojo, ese ejemplar es la impresión de **2003** (ISBN 0321146530), no la de 2002; misma obra. **estable**
- [Kent Beck, Mike Beedle, ... James Grenning, Robert C. Martin et al., *Manifesto for Agile Software Development*](https://agilemanifesto.org/), 2001 — contexto histórico. Verificado: los 17 firmantes están listados en el sitio y Beck, Grenning y Martin figuran entre ellos. **estable** (dominio propio del manifiesto, sin cambios desde 2001)
- [Robert C. Martin, *The Cycles of TDD*](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html), Clean Coder Blog, 17 de diciembre de 2014 — acá están las tres leyes, con esta redacción exacta: (1) *"You must write a failing test before you write any production code."* (2) *"You must not write more of a test than is sufficient to fail, or fail to compile."* (3) *"You must not write more production code than is sufficient to make the currently failing test pass."* Dato clave para el post: las tres leyes son el **nano-ciclo** (segundo a segundo), el más interno de cuatro ciclos anidados —nano / micro (red-green-refactor) / milli (específico-genérico) / primario (fronteras arquitectónicas)—. **frágil** (blog personal) → backup Wayback: [snapshot 2026-07-10](http://web.archive.org/web/20260710193742/http://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)
- [Mihály Csíkszentmihályi, *Flow: The Psychology of Optimal Experience*](https://archive.org/details/flowpsychologyof00csik), Harper & Row, Nueva York, 1990 — la base teórica del estado de flujo. Verificado en archive.org: **préstamo controlado**, no abierto. **estable**
- [*SNL Digital Short: When Will the Bass Drop?*](https://www.youtube.com/watch?v=DoUV7Q1C1SU) — canal oficial de Saturday Night Live. Título y canal verificados vía la API oEmbed de YouTube (la página de YouTube no es fetcheable directamente). **La URL que estaba antes en este draft (`BACGAfZqDBo`) daba 404 y fue reemplazada.** Fecha (17/5/2014), elenco y personaje **NO verificados por fuente primaria** — ver la marca [VERIFICAR:] en la sección «El sketch». Página oficial del clip en NBC (da timeout, no la pude confirmar): `nbc.com/saturday-night-live/video/snl-digital-short-when-will-the-bass-drop/2783137`. **frágil** (YouTube; hay snapshot Wayback del 2025-12-08 pero web.archive.org está bloqueado para verificarlo desde acá)
- [Martin Fowler, *Is TDD Dead?*](https://martinfowler.com/articles/is-tdd-dead/), 2014 — serie de **cinco conversaciones de 30 minutos por Google Hangout con Kent Beck y DHH, entre el 9 de mayo y el 4 de junio de 2014** (verificado en la página: hay video, audio y minutas de cada una). La otra cara del debate. **frágil** (sitio personal) → backup Wayback: [snapshot 2026-07-11](http://web.archive.org/web/20260711124814/https://martinfowler.com/articles/is-tdd-dead/)
- [David Heinemeier Hansson, *TDD is dead. Long live testing.*](https://dhh.dk/2014/tdd-is-dead-long-live-testing.html), 23 de abril de 2014 — la opinión disidente. Verificado: distingue testing (que defiende) de test-first (que rechaza); frase load-bearing: *"Test-first units leads to an overly complex web of intermediary objects and indirection in order to avoid doing anything that's 'slow'"*; propone tests de sistema de más alto nivel (Capybara) en lugar de diseño guiado por tests unitarios. **frágil** (blog personal) → backup Wayback: [snapshot 2026-04-27](http://web.archive.org/web/20260427155155/https://dhh.dk/2014/tdd-is-dead-long-live-testing.html)

_Nuevas — agregadas en la pasada de fuentes para la sección «La parte neurológica»:_

- C. B. Ferster y B. F. Skinner, *Schedules of Reinforcement*, Appleton-Century-Crofts, Nueva York, 1957 — **la fuente primaria de los esquemas de refuerzo que al draft le faltaba**. Copia en archive.org en préstamo controlado: [schedulesofreinf0000bfsk](https://archive.org/details/schedulesofreinf0000bfsk). **estable**
- [B. F. Skinner Foundation — *Schedules of Reinforcement*](https://www.bfskinner.org/product/schedules-of-reinforcement/) — la fundación del propio autor; confirma la reedición de 1997 del original de 1957 y aclara que, aunque la investigación se hizo con palomas, «the basic principles they discovered apply equally to the behavior of other species including human beings». Preferible a Wikipedia como cita (regla de la casa: el sitio del autor primero). **frágil** (página de producto) 
- Wolfram Schultz, Peter Dayan y P. Read Montague, *A Neural Substrate of Prediction and Reward*, **Science**, vol. 275, n.º 5306, pp. 1593-1599, 1997. DOI canónico: [10.1126/science.275.5306.1593](https://doi.org/10.1126/science.275.5306.1593) (metadatos verificados vía `api.crossref.org`, porque science.org bloquea el fetch). Mirror libre en la página del co-autor Peter Dayan (Gatsby, UCL): [sdm97.html](http://www.gatsby.ucl.ac.uk/~dayan/papers/sdm97.html) / [PDF](https://www.gatsby.ucl.ac.uk/~dayan/papers/sdm97.pdf). **Es el paper que dice que las neuronas dopaminérgicas señalan el _error de predicción_ de la recompensa, no la recompensa** — o sea, la fuente que pone en duda el mecanismo del Concepto. Léelo antes de escribir la sección neurológica. **estable** (DOI) / **frágil** (el mirror de UCL, página académica personal)

**Imágenes:**
- _Crear_: GIF animado / SVG del ciclo red→green→refactor con ondas de sonido tipo bass drop (~1 hora — el chiste visual del post).
- _Embed_: vídeo del sketch de SNL (verificar derechos / usar embed oficial de YouTube).

**Tags propuestos:** `['TDD', 'Kent Beck', 'flow', 'dopamina', 'red green refactor']`

**Estado actual:** prosa-borrador con **pasada de fuentes hecha (2026-07-15)**; sin revisar por César.

⚠️ **PREMISA EN DUDA:** el Concepto y el título dicen que cada test que pasa es «una micro-descarga de dopamina». La fuente primaria sobre dopamina va en contra de la versión literal de eso: Schultz, Dayan y Montague (*Science*, 275(5306):1593-1599, 1997) establecieron que las neuronas dopaminérgicas señalan el **error de predicción** de la recompensa, no la recompensa en sí. Una barra verde que *esperabas* —y la esperás, porque escribiste el código para que pase— es una recompensa predicha, y por ese mecanismo debería producir poca o ninguna descarga. Lo que engancharía, si algo, sería la barra verde *inesperada* o la roja que no viste venir.
Esto no hunde el post, pero sí obliga a elegir: (a) tratar la dopamina como metáfora declarada y no como mecanismo —la prosa ya va para ahí, con el párrafo «no soy psicólogo ni neurocientífico»—, y apoyar el peso argumental en **flow** (Csíkszentmihályi), que sí sostiene la tesis central: TDD fabrica la *retroalimentación inmediata* que es una de las condiciones del flujo y que el resto de la programación no da; o (b) reescribir la sección neurológica en serio alrededor del error de predicción, que además da un remate mejor —el ciclo deja de dar dopamina justo cuando lo dominás, y ahí es donde se vuelve hábito y no descarga. El Hook y el Concepto quedan intactos: la decisión es de César. La palabra «dopamina» está en el slug y en los tags, así que conviene decidir antes de publicar.

**Sourcing hecho en esta pasada:** verificadas por fetch las 7 referencias que ya estaban (Beck, Agile Manifesto, Uncle Bob, Csíkszentmihályi, SNL, Fowler, DHH) y agregadas 3 nuevas (Ferster & Skinner 1957 como fuente primaria del refuerzo; la ficha de la B. F. Skinner Foundation; Schultz/Dayan/Montague 1997 con DOI + mirror de UCL). Flags de bitrot y backups de Wayback puestos en toda la Bibliografía. **Hallazgo importante: el link de YouTube que tenía el draft (`BACGAfZqDBo`) devolvía HTTP 404 — reemplazado por `DoUV7Q1C1SU`, verificado como el video del canal oficial de SNL vía la API oEmbed.**

**Marcas `[VERIFICAR:]`: quedan 2 de 4.**
- ✅ Resueltas: las tres leyes de Uncle Bob (redacción exacta confirmada en *The Cycles of TDD*, 17/12/2014 — y el hallazgo de que son el **nano-ciclo**, escala de segundos, refuerza el argumento del post: la prosa se actualizó); y la tesis de DHH en 2014 (confirmada en su post del 23/4/2014 y en la serie de Fowler: cinco charlas, 9/5 al 4/6/2014 — la prosa ahora lo cita en vez de resumirlo de memoria).
- ⏳ Abiertas: (1) el sketch de SNL —título y canal sí verificados, pero fecha/elenco no, porque NBC.com da timeout, IMDb devuelve vacío, snlarchives.net tiene el certificado roto y web.archive.org está bloqueado; hay que mirar el video—; (2) el párrafo del refuerzo intermitente —ya tiene fuente primaria citable (Skinner), pero el argumento sigue siendo dudoso por lo mismo de la premisa; mi recomendación es borrarlo, pero es decisión de César.

Quedan **9 huecos** que necesitan a César (todos los del punto 5 del outline —la clase de Paradigmas 2020— más su propio momento de adopción y si vio el sketch de SNL): ninguna búsqueda web los toca. Nota personal previa que sigue vigente: revisar el material de la clase de Paradigmas 2020 antes de publicar.

---

## Borrador de prosa

TDD se enseña como si fuera medicina: amargo pero te hace bien. Escribí el test primero, aguantate la incomodidad, y dentro de seis meses vas a agradecerlo cuando el refactor no te explote en la cara. Es un argumento correcto y es un argumento perdedor. Nadie cambia de hábitos porque alguien le prometa una recompensa diferida a seis meses; si eso funcionara, todos haríamos ejercicio y nadie fumaría.

Está mal vendido. TDD no se siente como medicina. Se siente como un sketch de Saturday Night Live con bass drops cada treinta segundos. Y te das cuenta recién cuando lo practicás dos semanas seguidas y una mañana te descubrís *queriendo* escribir el test antes que el código —no porque seas disciplinado, sino porque querés el bajo.

### El sketch

Hay un sketch de SNL donde un DJ está frente a una multitud enorme, todo el aparato del EDM montado, las luces, la máquina de humo, y la gente esperando el bass drop. El chiste es la espera: la tensión se estira, y se estira, y se estira, y el tipo arriba del escenario no hace nada más que apretar un botón en el momento justo. Toda la ingeniería del género está al servicio de un único instante de descarga.[^snl]

> 🕳️ **HUECO — necesita a César:** ¿viste el sketch vos, o te lo mostró alguien? ¿En qué contexto te acordaste de él mientras hacías TDD —fue una asociación que hiciste en el momento o algo que venías rumiando?

[VERIFICAR: PARCIALMENTE RESUELTO. Confirmado por fetch: el sketch existe y se llama *SNL Digital Short: When Will the Bass Drop?*, publicado en el canal oficial de Saturday Night Live — verificado vía la API oEmbed de YouTube (`youtube.com/oembed`), que devuelve `title` y `author_name: "Saturday Night Live"`. **OJO: la URL que tenía este draft (`watch?v=BACGAfZqDBo`) devuelve HTTP 404 — estaba mal y ya la reemplacé** por `watch?v=DoUV7Q1C1SU`, que sí resuelve.
FALTA confirmar fecha y elenco con fuente primaria: no pude abrir ninguna. NBC.com (la página oficial del clip, `nbc.com/saturday-night-live/video/snl-digital-short-when-will-the-bass-drop/2783137`) da timeout en dos intentos; IMDb (tt3686928) devuelve página vacía al fetch; snlarchives.net falla por certificado inválido; onesnladay.com rechaza la conexión. La página de YouTube tampoco es fetcheable (devuelve sólo el footer), y web.archive.org está bloqueado para este agente.
Como CONTEXTO (no cita primaria — regla de la casa: Wikipedia no cita): el artículo de Wikipedia sobre la temporada 39 de SNL dice que el episodio 21, final de temporada, fue el 17 de mayo de 2014, con Andy Samberg de host y St. Vincent de músico invitado, y que «Lil Jon appears in the first SNL Digital Short» — pero no nombra el sketch. Encaja con todo lo demás, pero no lo doy por verificado.
ACCIÓN ANTES DE PUBLICAR: mirá el video (2 minutos) y confirmá vos fecha, elenco y el nombre del personaje DJ; el chiste del personaje parodiando a Avicii aparece en las notas de prensa pero no lo pude verificar de primera mano.]

Me interesa el sketch no por el chiste sino por lo que el chiste presupone: que todos entendemos, sin que nadie nos lo explique, que un género musical entero puede organizarse alrededor de la administración de una recompensa. Tensión, tensión, tensión, descarga. Y otra vez.

### Red bar, green bar, commit

Ahora mirá el ciclo de TDD tal como lo formuló Kent Beck: escribí un test que falle, hacelo pasar, refactorizá.[^beck] En la práctica, con un runner decente al lado del editor, eso es:

1. Escribís tres líneas que describen lo que querés que pase.
2. Corrés. **Barra roja.** Bien: el test sirve, falla por la razón correcta.
3. Escribís el código más tonto que haga pasar el test.
4. Corrés. **Barra verde.**
5. Limpiás. Corrés. Verde otra vez. Commit.

La barra verde es el bass drop. Es exactamente eso: una tensión chiquita, autoimpuesta, deliberadamente construida para durar poco, y una descarga. El paso 2 —el rojo— no es un trámite burocrático. Es la máquina de humo. Es lo que hace que el verde signifique algo. Un test que nunca lo viste fallar no te da nada, ni información ni placer, porque no hubo tensión que resolver.

Y esto es lo que la formulación estricta de las tres leyes de Uncle Bob captura y a la vez oculta.[^cleancoder] Las leyes describen la mecánica con una precisión de reglamento —no escribir código de producción antes de tener un test que falle; no escribir de un test más de lo suficiente para que falle (o no compile); no escribir más código de producción del suficiente para hacer pasar el test que está fallando— y en esa precisión suenan a penitencia. Pero leídas al revés, las tres leyes no son un código moral: son la especificación técnica de cómo mantener el ciclo lo suficientemente corto como para que el cerebro lo registre.

Y acá el propio texto de Uncle Bob me da la razón más de lo que esperaba: en *The Cycles of TDD* las tres leyes no son *el* ciclo de TDD, son el **nano-ciclo**, el de escala de segundos, el más interno de cuatro ciclos anidados (nano = las tres leyes; micro = red-green-refactor, minuto a minuto; milli = específico/genérico; y el ciclo primario, hora a hora, el de las fronteras arquitectónicas).[^cleancoder] Es decir: la unidad de medida que Uncle Bob eligió para las tres leyes es *el segundo*. No está pidiéndote que sufras. Está calibrando el intervalo entre bass drops.

### La parte neurológica, con honestidad

Acá tengo que frenar y aclarar que no soy psicólogo ni neurocientífico, y que lo que sigue es una analogía que me sirve, no una explicación validada.

Lo que sí está bien documentado es la mecánica del **flow** de Csíkszentmihályi: el estado aparece cuando la dificultad de la tarea y la habilidad de quien la ejecuta están más o menos equilibradas, cuando los objetivos son claros y —esto es lo que importa acá— cuando la retroalimentación es *inmediata*.[^flow] Esa última condición es la que casi ningún trabajo de programación cumple naturalmente. ¿Escribiste bien esta función? Bueno, lo sabrás cuando alguien la use, o en el code review del jueves, o en producción el mes que viene. La retroalimentación llega tarde, difusa y mezclada con otras diez cosas.

TDD fabrica la condición faltante. No te vuelve más hábil ni te achica el problema: te fabrica retroalimentación inmediata donde no la había. Por eso engancha. No es disciplina; es que el ciclo cumple, casi por accidente de diseño, la lista de requisitos del flow.

Se suele agregar acá la teoría del refuerzo intermitente —que una recompensa impredecible engancha más que una predecible. [VERIFICAR: SIGUE ABIERTO, y la pasada de fuentes reforzó la sospecha del draft en lugar de salvarlo. Lo que sí conseguí es la fuente primaria que faltaba: Ferster y Skinner, *Schedules of Reinforcement*, Appleton-Century-Crofts, 1957 —hay copia en archive.org (préstamo controlado) y la B. F. Skinner Foundation lo reeditó en 1997—, así que la atribución a Skinner ya es citable en serio (ver Bibliografía). Pero eso resuelve la cita, no el argumento.
El problema de fondo que anotaba el draft sigue en pie y ahora tiene respaldo: la barra verde *no* es impredecible —escribiste el código justamente para que pase—, y la literatura sobre dopamina apunta en contra. Schultz, Dayan y Montague (*Science*, 1997) establecen que las neuronas dopaminérgicas no señalan la recompensa sino el **error de predicción** de la recompensa (ver Bibliografía). Si el mecanismo es error de predicción, entonces una barra verde que esperabas debería producir *poca o ninguna* descarga —justo al revés de lo que sugiere el párrafo, y en tensión con el «micro-descarga de dopamina» del Concepto (ver la nota ⚠️ PREMISA EN DUDA en Estado actual).
Mi recomendación tras buscar: borrar el párrafo del refuerzo intermitente. La parte de flow (Csíkszentmihályi) se sostiene sola y es la que hace el trabajo. Decisión de César, no mía — por eso la marca queda.]

### Por qué el que abandona, abandona

Esto explica algo que me venía intrigando: la diferencia entre el que probó TDD dos días y dice que es una pérdida de tiempo, y el que lo adoptó y no puede programar de otra manera. Yo creía que era una diferencia de temperamento, o peor, de virtud. No creo que sea ninguna de las dos.

Es una diferencia de dosis. Los primeros días de TDD son puro costo y nada de recompensa: peleás con el runner, no sabés qué testear, escribís tests que no fallan por la razón que creías, el ciclo te sale de veinte minutos en lugar de dos. A los veinte minutos por vuelta no hay bass drop —hay una canción larguísima y aburrida. La descarga sólo aparece cuando el ciclo se acorta lo suficiente, y el ciclo sólo se acorta con práctica. El que abandona no abandona porque le falte disciplina: abandona porque salió de la sala antes de que bajara el bajo.

> 🕳️ **HUECO — necesita a César:** ¿cuánto tardaste vos en llegar a ese punto, y cómo fue? ¿Hubo un momento concreto en que el ciclo se te acortó y lo notaste?

> 🕳️ **HUECO — necesita a César:** ¿alguna vez abandonaste TDD y volviste? Si sí, ¿qué te hizo volver?

Y esto tiene una consecuencia incómoda para el debate de 2014 entre DHH, Beck y Fowler.[^dhh][^tddead] DHH argumentaba contra el TDD ortodoxo desde el resultado —el diseño que produce, el costo que impone—: su tesis, en el post del 23 de abril de 2014, es que el *test-first* como práctica de diseño empuja a «una maraña excesivamente compleja de objetos intermediarios e indirección con tal de no hacer nada que sea "lento"», y que la salida no es dejar de testear sino subir el nivel del test —pegarle a la base de datos, tests de sistema por encima— en vez de derivar el diseño de los tests unitarios. De ahí el título: *TDD is dead. Long live testing.* No estaba matando el testing; estaba matando el test-first como método de diseño.[^dhh]

Conviene notar que el debate no fue un cruce de trincheras: las cinco conversaciones que Fowler organizó con Beck y DHH entre el 9 de mayo y el 4 de junio de 2014 terminan bastante lejos del titular, en un «depende del contexto» que a nadie le sirvió para hacer bandera.[^tddead] Si mi lectura es correcta, buena parte de ese debate se dio entre gente que ya había pagado el costo de entrada y podía discutir el mérito, hablando frente a una audiencia que en su mayoría no. Para el que nunca completó el ciclo lo suficiente, «TDD is dead» no es una posición técnica: es un permiso.

> 🕳️ **HUECO — necesita a César:** ¿seguiste el debate *Is TDD Dead?* en su momento, en 2014? ¿De qué lado estabas entonces y de cuál estás ahora?

### La clase de Paradigmas, 2020

> 🕳️ **HUECO — necesita a César:** ¿en qué materia/institución exactamente fue esta clase de Paradigmas de 2020, y con qué rol estabas vos ahí?

> 🕳️ **HUECO — necesita a César:** ¿fue presencial o remota? (2020 sugiere remota, pero no lo doy por sentado.) Si fue remota, ¿qué herramienta usaste para que vieran la pantalla?

> 🕳️ **HUECO — necesita a César:** ¿qué lenguaje y qué framework de testing usaste en la sesión de live coding? ¿Y qué problema elegiste para resolver en vivo?

> 🕳️ **HUECO — necesita a César:** ¿qué pasó concretamente cuando vieron la sesión por primera vez? Una reacción concreta que recuerdes —una pregunta que te hizo alguien, un comentario en el chat, un silencio.

> 🕳️ **HUECO — necesita a César:** ¿algo te salió mal en vivo? (Si el test no pasó cuando esperabas que pasara, eso es *el* momento del post y hay que contarlo.)

> 🕳️ **HUECO — necesita a César:** ¿sabés si alguno de esos alumnos siguió usando TDD después? ¿Tenés alguna manera de saberlo?

*(La anécdota va acá y es el corazón del post: es la única evidencia de primera mano de que ver el ciclo funcionando produce un efecto distinto a que te lo expliquen. Sin esto el post es una analogía linda sin nada abajo. Escribir sólo cuando estén contestados los huecos de arriba y después de revisar el material de la clase.)*

### El truco

Si querés probar esto sin comprometerte a nada, no empieces por un proyecto nuevo ni por un kata. Empezá con un bug que ya tenés.

Agarrá uno que sepas reproducir. Escribí el test que lo reproduce —nada más que eso, el test que falla—. Corrélo. Mirá la barra roja. Ahí, en ese instante, ya ganaste algo aunque no arregles nada: ahora tenés el bug capturado, escrito, ejecutable, y no depende de que te acuerdes de los pasos. Después arreglalo. Mirá la barra verde.

Eso es todo. No hay una segunda parte. Si sentiste algo en el paso de la roja a la verde, ya sabés de qué te estoy hablando y el resto es práctica hasta que el ciclo se acorte. Si no sentiste nada, también está bien —hay gente que no escucha EDM.

Lo que no te voy a decir es que lo hagas porque te hace bien.

[^beck]: Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley, 2002. Copia en préstamo controlado en [archive.org](https://archive.org/details/testdrivendevelo0000beck) (impresión de 2003).
[^snl]: [*SNL Digital Short: When Will the Bass Drop?*](https://www.youtube.com/watch?v=DoUV7Q1C1SU) — canal oficial de Saturday Night Live. Título y canal verificados vía oEmbed; fecha e intérpretes pendientes de confirmar mirando el video (ver marca [VERIFICAR:] arriba).
[^cleancoder]: Robert C. Martin, [*The Cycles of TDD*](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html), Clean Coder Blog, 17 de diciembre de 2014 — las tres leyes como *nano-ciclo*, el más interno de los cuatro ciclos anidados.
[^flow]: Mihály Csíkszentmihályi, [*Flow: The Psychology of Optimal Experience*](https://archive.org/details/flowpsychologyof00csik), Harper & Row, 1990 (préstamo controlado en archive.org).
[^dhh]: David Heinemeier Hansson, [*TDD is dead. Long live testing.*](https://dhh.dk/2014/tdd-is-dead-long-live-testing.html), 23 de abril de 2014.
[^tddead]: Martin Fowler, [*Is TDD Dead?*](https://martinfowler.com/articles/is-tdd-dead/), 2014 — serie de cinco conversaciones con DHH y Kent Beck, del 9 de mayo al 4 de junio de 2014.
[^schultz]: Wolfram Schultz, Peter Dayan y P. Read Montague, *A Neural Substrate of Prediction and Reward*, Science, vol. 275, n.º 5306, pp. 1593-1599, 1997 — DOI [10.1126/science.275.5306.1593](https://doi.org/10.1126/science.275.5306.1593); [mirror libre](http://www.gatsby.ucl.ac.uk/~dayan/papers/sdm97.html) en la página de Dayan (Gatsby, UCL). _(Footnote lista para usar si se reescribe la sección neurológica; hoy no está referenciada en el cuerpo.)_
[^skinner]: C. B. Ferster y B. F. Skinner, *Schedules of Reinforcement*, Appleton-Century-Crofts, 1957 — [copia en archive.org](https://archive.org/details/schedulesofreinf0000bfsk) (préstamo controlado); [ficha en la B. F. Skinner Foundation](https://www.bfskinner.org/product/schedules-of-reinforcement/), que reeditó el original en 1997. _(Ídem: disponible por si el párrafo del refuerzo intermitente sobrevive.)_

