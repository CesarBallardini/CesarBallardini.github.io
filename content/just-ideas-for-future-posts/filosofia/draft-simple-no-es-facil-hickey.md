### C-02 — Simple no es lo mismo que fácil (Rich Hickey)

- **Archivo seed:** `dev/draft-simple-o-facil.md`
- **Slug propuesto:** `simple-no-es-facil-hickey`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-simple-no-es-facil-hickey/index.md`
- **Serie:** C
- **Cross-links:** depende de [[tr-07]]; lleva a [[C-03]] (Tidy First, otro framework para hablar de cambio), [[A2-04]] (Clojure y la práctica de Hickey), [[B-02]] (Okasaki — estructuras simples pero no fáciles)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** la charla *Simple Made Easy* de Rich Hickey (Strange Loop 2011) es uno de esos textos que cambia el vocabulario con el que pensás tu trabajo. La distinción entre *simple* (sin entrelazar, sin nudos: una propiedad objetiva del diseño) y *easy* (cerca de tu mano, conocido, instalable con un comando: una propiedad subjetiva del usuario) explica por qué todo el tiempo elegimos lo "fácil" y luego pagamos en complejidad.

**Hook:** "Rich Hickey, el creador de Clojure, dio una charla en 2011 que vino a romper el vocabulario con el que hablábamos de software. Después de esa charla ya no podés decir 'esta solución es simple' sin que te corrija una vocecita interna: querés decir *fácil*. Hay una diferencia, y la diferencia importa."

**Outline:**
1. La etimología que abre la charla: *simple* viene de *simplex* (un pliegue), su opuesto es *complex* (varios pliegues entrelazados). *Easy* viene de *adjacens* — cerca de vos.
2. Por qué la confusión es sistemática: los vendedores de herramientas optimizan para easy (tutorial de 5 minutos), pero el costo de simple se paga después.
3. La lista de Hickey de cosas "simples" vs "complejas":
   - state vs values
   - methods vs functions
   - vars vs managed refs
   - inheritance, switch, matching vs polymorphism
   - syntax vs data
   - imperative loops, fold vs set functions
   - actors vs queues
   - ORM vs declarative data manipulation
   - conditionals vs rules
4. La tesis fuerte: *no podés construir cosas confiables a partir de partes complejas*. Reliability requires understanding requires simplicity.
5. La crítica que se le hace a Hickey y por qué la critica falla: "simple es subjetivo también" — no, es estructural; podés contar los entrelazamientos.
6. Aplicaciones prácticas: cómo usar este vocabulario en code review y en arquitectura. Ejemplo concreto con un caso de mi experiencia.
7. Cierre: el costo de elegir easy todo el tiempo es la deuda de complejidad que después no podés pagar.

**Bibliografía:** (verificada por fetch el 2026-07-16)
- [[tr-07]] — Rich Hickey, *Simple Made Easy*, Strange Loop 2011. Video en [InfoQ](https://www.infoq.com/presentations/Simple-Made-Easy/) (título y autor confirmados; grabada el 20-oct-2011) — **estable**. Transcripción oficial en [`matthiasn/talk-transcripts`](https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md), fuente para citar literal (todas las citas del cuerpo se cotejaron contra esta transcripción) — **estable**.
- [Rich Hickey, *Hammock Driven Development*, Clojure Conj 2010](https://www.youtube.com/watch?v=f84n5oFoZBc) — la charla compañera, sobre el modo de pensar. URL resuelve; título confirmado. YouTube — **frágil**.
- [Rich Hickey, *The Value of Values*, JaxConf 2012](https://www.youtube.com/watch?v=-6BsiVyC1kM) — URL resuelve; título «The Value of Values with Rich Hickey» confirmado, contenido no cotejado. YouTube — **frágil**.
- [Stuart Halloway, *Narcissistic Design*, Clojure/conj 2015](https://www.youtube.com/watch?v=LEZv-kQUSi4) — extiende el argumento de Hickey con humor. URL resuelve; título confirmado, contenido no cotejado. YouTube — **frágil**.
- [Fred Brooks, *No Silver Bullet — Essence and Accident in Software Engineering*](https://www.cs.unc.edu/techreports/86-020.pdf) — IEEE Computer vol. 20, n.º 4, abril 1987 (este PDF es el tech report UNC 86-020, mirror libre del ensayo). Antecedente directo: complejidad esencial vs accidental. URL resuelve (PDF binario, no extraíble por fetch) — **estable** (dominio institucional `.edu`).
- [Ben Moseley & Peter Marks, *Out of the Tar Pit*, 2006](https://curtclifton.net/papers/MoseleyMarks06a.pdf) — el otro texto canónico sobre complejidad. URL resuelve (PDF binario, no extraíble por fetch) — **frágil** (mirror en dominio personal `curtclifton.net`; conviene backup Wayback antes de publicar).

**Imágenes:**
- _Crear_: tabla SVG con dos columnas — *simple* a la izquierda, *easy* a la derecha — replicando la lista de Hickey con íconos (~1 hora).
- _Crear_: diagrama del "tejido" — un nudo de cuerdas entrelazadas (complex) vs cuerdas paralelas (simple) (~30 min).
- _Crear_: opcional, screenshot del slide "what's simple?" de la charla original (verificar uso justo / fair use).

**Tags propuestos:** `['Rich Hickey', 'Clojure', 'simple', 'complejidad', 'arquitectura']`

**Estado actual:** prosa completa escrita siguiendo el outline de 7 puntos, citando únicamente la bibliografía ya verificada del draft. Quedaron **cinco huecos** (🕳️): cuándo y cómo llegó César a la charla, el caso concreto de su experiencia que pide el punto 6 del outline, si el vocabulario «simple/fácil» le entró efectivamente en el code review, una decisión propia donde eligió *easy* a sabiendas, y su lectura de Brooks. Quedaron **diez marcas `[VERIFICAR:]`**, casi todas sobre el contenido literal de la charla (etimologías, la lista simple/complejo, la formulación de la tesis de confiabilidad, el uso de *complect*) — todo eso lo respalda la transcripción oficial que ya está en la bibliografía, pero hay que leerla y confirmar redacción y orden antes de publicar, no confiar en el recuerdo. Las otras tres marcas piden ver/leer fuentes que ya están en la bibliografía pero cuyo contenido no se chequeó (*The Value of Values*, *Out of the Tar Pit*, *Narcissistic Design*). Pendiente al publicar: resolver los `[[ID]]`, agregar `page_css: ['tables.css']` al frontmatter (el cuerpo trae una tabla markdown), armar los dos SVG (tabla simple/easy y diagrama de cuerdas) y decidir el hero. La tabla markdown del cuerpo es un placeholder del SVG previsto en **Imágenes:** — al publicar, decidir si van las dos o sólo una. El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch: InfoQ, transcripción matthiasn, y las URLs de las charlas y papers acompañantes) y se resolvieron 1 de 5 marcadores `[VERIFICAR:]`. Resuelto: la formulación de la cadena confiabilidad→entendimiento→simplicidad (cotejada contra la transcripción; se añadió la máxima literal «simplicity is a prerequisite for reliability» que Hickey suscribe y la pregunta que la ancla). Sin resolver por falta de fetch de contenido: *The Value of Values* (valor/tiempo), *Out of the Tar Pit* (estado como fuente de complejidad + cita a Brooks; el PDF resuelve pero es binario no extraíble), *Narcissistic Design* (ángulo de consejos invertidos), y la afirmación personal «la hora mejor invertida de mi carrera» (depende de César). Corrección de contenido no marcada como `[VERIFICAR:]`: la etimología de *easy* atribuía el paso francés a la palabra «aise», que la transcripción **no** nombra (Hickey sólo dice «a French word»); se quitó el término inventado. Todas las citas literales de la charla (etimologías *simple*/*complex*, «one twist... no twists», *complect*, «just means simpler», vars/managed refs, «I'm leaving your minds to do that») se cotejaron verbatim contra la transcripción y coinciden.

---

## Borrador de prosa

Hay charlas que te enseñan una técnica y hay charlas que te cambian el diccionario. *Simple Made Easy*, la que dio Rich Hickey —el creador de Clojure— en la Strange Loop de 2011, es de las segundas.[^smadeeasy] Después de verla ya no podés decir «esta solución es simple» sin que te corrija una vocecita interna: querés decir *fácil*. Hay una diferencia, y la diferencia importa.

Importa porque las dos palabras se usan como sinónimos y no lo son ni de casualidad. Una describe una propiedad del objeto que construiste; la otra describe tu distancia a ese objeto. Confundirlas es lo que te permite salir de una reunión de arquitectura convencido de que tomaste la decisión correcta cuando en realidad tomaste la decisión cómoda. Y la factura de esa confusión no llega en el sprint donde la firmaste: llega dos años después, cuando alguien —posiblemente vos— tiene que cambiar algo y descubre que no puede.

### Dos etimologías que hacen todo el trabajo

Hickey abre la charla con el diccionario, y es un movimiento más astuto de lo que parece.

*Simple* viene de las raíces *sim* y *plex*: «un pliegue, una trenza o un giro» —«one fold or one braid or twist»—. Y Hickey remata la cuenta en el acto: un solo giro, ¿qué aspecto tiene? Ninguno. «One twist, what's one twist look like? No twists, right, actually.» Su opuesto es *complex*, que significa «trenzado junto o plegado junto».[^transcripcion] Fijate en lo que eso implica: *simple* habla de **cuántas cosas están atadas entre sí**. Es una propiedad estructural del diseño. No depende de vos, ni de tu experiencia, ni de si dormiste bien. Está ahí, en el código, aunque no la mires.

*Easy*, en cambio, viene —dice Hickey— de una palabra francesa (no la nombra en la charla) y de ahí «a la palabra latina que es la raíz de *adjacent*, que significa yacer cerca, estar cerca» —«from the Latin word that is the root of *adjacent*, which means to lie near and to be nearby»—. **Lo que está al lado tuyo**, lo que tenés a mano.[^transcripcion]

Acá conviene ser más honesto que el resumen que suele circular de la charla, porque Hickey lo es: él mismo aclara que **el último paso de esa derivación es especulativo** —«the last step of this derivation is actually speculative, but I bought it because it serves this talk really well»—. Es decir: la etimología de *easy* no es un dato duro que gana la discusión, es una imagen que Hickey adopta a sabiendas porque le sirve. Vale la pena citarla con esa reserva puesta. (De paso: el opuesto, *hard*, no significa «lejos» sino «fuerte», o retorcido de tan fuerte; la simetría no es perfecta y Hickey también lo dice.)

Y eso también implica algo brutal: *easy* es **relativo al observador**. Algo es fácil porque lo tenés cerca: instalable con un comando, o ya lo conocés, o está en el idioma que hablás, o cabe en tu cabeza tal como tu cabeza está hoy. Cambiá de persona y cambia la respuesta.

Ahí está el nudo del asunto. Cuando discutimos diseño, creemos estar hablando de una propiedad del sistema y en realidad estamos hablando de nuestra propia comodidad.

### Por qué la confusión no es un accidente

Lo fácil se puede vender. Lo simple, no.

Pensá en cómo evaluás una herramienta nueva. Mirás el *quickstart*. Si en cinco minutos tenés un «hola mundo» andando, la herramienta «es buena». Ese es el mercado en el que compiten todos los frameworks: la métrica es el tiempo hasta el primer éxito. Y es una métrica honesta para lo que mide —tu distancia inicial al artefacto— pero no mide absolutamente nada de lo que te va a doler.

Porque el costo de *easy* está diferido. La herramienta que te resolvió el día uno en cinco minutos lo hizo entrelazando cosas por vos: tu modelo de datos con tu esquema de base, tu lógica con tu framework web, tu configuración con tu ambiente. Ese entrelazado es exactamente lo que te va a cobrar el día 500, cuando quieras tocar una de esas cosas sin tocar las otras y descubras que no existe «una de esas cosas»: existe el nudo.

Hickey tiene una palabra para el verbo de hacer eso: *complect*. La define así: «significa entretejer, entrelazar o trenzar» —«it means to interleave or entwine or braid»—. Y explica por qué la elige en vez de *braid* o *entwine*, que serían más comunes: porque esas no tienen la connotación de bueno/malo que él quiere. «Complect is obviously bad.»[^transcripcion] Es un verbo arcaico —él mismo lo dice, y agrega que no hay ninguna regla que prohíba volver a usarlo— y lo rescata justamente porque no tenemos otro. Nos falta la palabra para nombrar el pecado que cometemos todo el tiempo.

### La lista

El corazón de la charla es una tabla de dos columnas. A la izquierda, lo complejo; a la derecha, la contraparte **más simple**:

| Complejo (entrelaza) | Más simple |
|---|---|
| state, objects | values |
| methods | functions, namespaces |
| vars, variables | managed refs |
| inheritance, switch, matching | polymorphism a la carte |
| syntax | data |
| imperative loops, fold | set functions |
| actors | queues |
| ORM | declarative data manipulation |
| conditionals | rules |
| inconsistency | consistency |

Dos precisiones que la charla hace y que casi todas las reproducciones de esta tabla —incluida la primera versión de este borrador— se comen:

La primera es del propio Hickey, al presentarla: **la columna de la derecha significa «más simple», no «simple»**. «The simplicity column just means simpler. It doesn't mean that the things over there are purely simple.» Y agrega que no rotuló las columnas como «malo» y «bueno»: «I'm leaving your minds to do that.»[^transcripcion]

La segunda es el caso testigo de eso: sobre la fila de los *vars*, lo que Hickey dice literalmente es que **las managed refs también son complejas**, sólo que menos. «Vars are complex and variables are complex. Managed references are also complex, but they're simpler.» No es una columna de absoluciones.

Lo que hace que la lista sea incómoda —y por eso es buena— es que casi todo lo de la columna izquierda es lo que la mayoría de nosotros usa todos los días. No es una lista de malas prácticas. Es una lista de prácticas normales, respetadas, enseñadas, con el cargo de complejidad que traen anotado al lado.

Tomá `state`. El estado no es malo porque sea sucio; es complejo porque entrelaza el valor con el tiempo. Si un objeto tiene un campo mutable, ya no podés hablar del valor sin hablar de *cuándo*. Nunca más. Ese entrelazado es el tema de otra charla de Hickey, *The Value of Values*, que es la continuación natural de esta. [^values] [VERIFICAR: que *The Value of Values* efectivamente desarrolla el argumento valor/tiempo — chequear la charla, está en la bibliografía]

O tomá el ORM, que es el ejemplo perfecto de *easy* triunfando sobre *simple*: te ahorra escribir SQL el primer día y te entrelaza el modelo de objetos, el esquema relacional, la sesión, la caché y la estrategia de carga en un solo objeto que ya no sabés dónde termina.

### La tesis fuerte

Si la charla fuera sólo la tabla, sería una opinión sobre gustos. No lo es, porque tiene un argumento debajo, y el argumento es una cadena corta:

**No podés construir cosas confiables a partir de partes que no entendés. No podés entender partes que están entrelazadas. Por lo tanto: confiabilidad requiere entendimiento, y entendimiento requiere simplicidad.** La charla lo sostiene con una máxima que Hickey suscribe en pantalla —«simplicity is a prerequisite for reliability»— y con la pregunta que la ancla: «how can we possibly make things that are reliable that we don't understand?».[^transcripcion]

Esto saca la discusión del terreno estético. No es «me gusta el código limpio». Es: la complejidad tiene una consecuencia medible en la cantidad de cosas que podés afirmar sobre tu sistema sin correrlo. Y cuando no podés afirmar nada sin correrlo, lo único que te queda son los tests, que te dicen qué pasa en los casos que se te ocurrieron, no en los que no.

Hickey no inventó esta línea de pensamiento. Está en la sombra de Fred Brooks, que en *No Silver Bullet* partió la complejidad en **esencial** (la que trae el problema) y **accidental** (la que trae nuestra manera de resolverlo).[^brooks] Y está al lado de *Out of the Tar Pit*, de Moseley y Marks, que va todavía más lejos con la misma preocupación.[^tarpit] [VERIFICAR: la tesis central de *Out of the Tar Pit* sobre el estado como fuente principal de complejidad, y si los autores citan explícitamente a Brooks — el PDF está en la bibliografía]

Vale la pena marcar la diferencia, igual: Brooks argumenta que la complejidad esencial pone un piso a lo que se puede mejorar —de ahí que no haya bala de plata—. Hickey no discute ese piso: dice que estamos muy por encima de él, y por decisión propia.

> 🕳️ **HUECO — necesita a César:** ¿leíste *No Silver Bullet* antes o después de ver la charla de Hickey, y te pareció que Hickey lo contradice o que lo continúa? Una o dos frases con tu lectura.

### «Simple también es subjetivo» — la objeción que no cierra

La crítica más común a la charla es una devolución de saque: *si «fácil» es relativo al observador, «simple» también lo es; lo que a vos te parece un solo pliegue a mí me parecen tres.*

No cierra, y no cierra por una razón concreta: los entrelazamientos se pueden contar. Poné un componente sobre la mesa y preguntá cuántas cosas necesitás saber para cambiarlo. Cuántos módulos tocás si cambia el esquema. Cuántas responsabilidades hay ligadas dentro de una misma clase. Esos números no dependen de tu opinión: dependen de la topología del código. Podés discutir el conteo —qué contás como una atadura— pero estás discutiendo una medición, no un gusto.

*Easy*, en cambio, no tiene ninguna medición posible que no sea «para quién». No hay un observador de referencia.

La confusión persiste, creo, porque *simple* y *fácil* correlacionan **en el largo plazo**: lo simple termina siendo fácil de mantener. Pero al principio, casi siempre, lo simple es más difícil. Te obliga a pensar antes. Ese es exactamente el tema de la otra charla de Hickey, *Hammock Driven Development*: el trabajo de diseño es un trabajo que se hace pensando, y pensar no se ve en el gráfico de commits.[^hammock]

### Cómo se usa esto un lunes

El valor práctico de la charla es que te da un vocabulario para decir en voz alta algo que antes sólo te incomodaba.

En un code review, la pregunta deja de ser «¿te parece bien?» y pasa a ser **¿qué entrelaza esto?**. Es una pregunta técnica, contestable, sin carga personal. «Este cambio ata la validación al transporte HTTP» es una observación sobre el diseño. «No me gusta» es una pelea.

En arquitectura, sirve para desarmar el falso empate. Cuando alguien dice «esta opción es más simple», podés preguntar: ¿simple, o la conocemos? Las dos respuestas son legítimas —a veces elegís *easy* a propósito, porque el equipo lo tiene a mano y no hay tiempo— pero son decisiones distintas y hay que anotarlas distinto. Elegir *easy* sabiendo que elegís *easy* es ingeniería. Elegir *easy* creyendo que elegís *simple* es cómo se construye la deuda que después nadie sabe de dónde salió.

Stuart Halloway hizo una versión cómica y bastante cruel de este mismo punto en *Narcissistic Design*, que recomiendo como acompañamiento.[^narcissistic] [VERIFICAR: el ángulo concreto de *Narcissistic Design* — es una charla de consejos invertidos («cómo hacer software imposible de mantener»)? confirmar viéndola, está en la bibliografía]

> 🕳️ **HUECO — necesita a César:** ¿cuándo viste *Simple Made Easy* por primera vez, y qué estabas haciendo en ese momento que la charla te hizo mirar distinto?

> 🕳️ **HUECO — necesita a César:** el outline pide un caso concreto de tu experiencia. ¿Hay un sistema en el que puedas señalar el entrelazado que te costó caro —qué estaba atado con qué, y qué cambio simple se volvió imposible por eso? (Sirve de STG, de Cultura, o de cualquier otro lado; con dos o tres frases alcanza.)

> 🕳️ **HUECO — necesita a César:** ¿te entró de verdad este vocabulario en el trabajo diario, o es un marco que te gusta pero que no usás cuando estás con las manos en el código? La respuesta honesta es mejor material que la respuesta linda.

> 🕳️ **HUECO — necesita a César:** ¿hay alguna decisión tuya donde elegiste *fácil* a sabiendas, con buenos motivos, y hoy la volverías a tomar igual?

### El interés compuesto de lo cómodo

El punto que se me quedó pegado no es que haya que elegir siempre lo simple. Hay veces que no se puede y hay veces que no conviene.

El punto es que *easy* se paga en cuotas y las cuotas son crecientes. Cada vez que elegís lo adyacente sin mirar lo que entrelaza, agregás un pliegue. Los pliegues no se suman, se multiplican: cada cosa nueva atada a las otras es una posibilidad nueva de que el cambio de acá rompa aquello de allá. Y llega un punto —todos lo conocemos, tiene un olor característico— donde el sistema ya no admite ningún cambio barato. Todo cuesta lo mismo: mucho.

Ahí es donde la charla deja de ser filosofía y se vuelve muy concreta. Ese sistema al que ya no le podés cambiar nada no se hizo así de golpe. Se hizo en una sucesión larga de martes razonables en los que alguien, apurado, eligió lo que tenía a mano.

Y no se lo puede culpar, porque no tenía la palabra para nombrar lo que estaba haciendo.

Si nunca la viste, la charla dura una hora y está entera acá.[^smadeeasy] Hay una transcripción oficial si preferís leerla.[^transcripcion] Es, tranquilamente, la hora mejor invertida de mi carrera [VERIFICAR: no afirmar esto sin que César lo confirme — depende del hueco sobre cuándo la vio y qué efecto tuvo].

[^smadeeasy]: Rich Hickey, [*Simple Made Easy*](https://www.infoq.com/presentations/Simple-Made-Easy/) — Strange Loop, 2011. → [[tr-07]]
[^transcripcion]: [Transcripción oficial de *Simple Made Easy*](https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md) — repositorio `matthiasn/talk-transcripts`. Es la fuente para citar literal.
[^hammock]: Rich Hickey, [*Hammock Driven Development*](https://www.youtube.com/watch?v=f84n5oFoZBc) — Clojure Conj, 2010.
[^values]: Rich Hickey, [*The Value of Values*](https://www.youtube.com/watch?v=-6BsiVyC1kM) — JaxConf, 2012.
[^narcissistic]: Stuart Halloway, [*Narcissistic Design*](https://www.youtube.com/watch?v=LEZv-kQUSi4) — Clojure/conj, 2015.
[^brooks]: Fred Brooks, [*No Silver Bullet — Essence and Accident in Software Engineering*](https://www.cs.unc.edu/techreports/86-020.pdf), IEEE Computer, 1987.
[^tarpit]: Ben Moseley & Peter Marks, [*Out of the Tar Pit*](https://curtclifton.net/papers/MoseleyMarks06a.pdf), 2006.

