### A2-08 — Simply Scheme: el libro con el que Berkeley enseñó a 500 programadores principiantes

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `simply-scheme-500-programadores`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-simply-scheme-500-programadores/index.md`
- **Serie:** lisp
- **Cross-links:** [[A2-01]] (SICP), [[A2-07]] (DrRacket), [[E-18]] (Little Lisper)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1500 palabras (elegido 2026-07-15: alcanza para las dos citas del cold open, las tres decisiones de diseño y el cierre, sin volverse una reseña capítulo por capítulo)

**Concepto:** *Simply Scheme* (Brian Harvey & Matthew Wright, MIT Press 1994) es el libro que Berkeley usaba para enseñar el primer curso de CS a no-mayors de informática. Pensado como introducción suave a los conceptos de SICP. El "500" del título no es una anécdota de cantidad de alumnos — es una cita verbatim del prefacio: la caricatura que Harvey y Wright hacen de la "vista conservadora" ("500 mediocre programmers can join together...") contra la "vista radical" que ellos sostienen (expandir la mente con ideas más grandes en vez de disciplinar el trabajo de una masa). Verificado por fetch directo a `ssch0/preface.html`, `ssch0/foreword.html` y `ssch0/instructor.html` — no hay ninguna cita de "500 veces mejor" en el libro; la única mención de "500" es esta.

**Hook:** la cita textual del prefacio — "500 mediocre programmers" vs "expand their minds" — como cold open. El post arma el post entero alrededor de esa dicotomía: escalar cabezas disciplinadas vs. escalar lo que una sola mente puede sostener.

**Outline:** cold open con las dos citas → "Un curso para los que no iban a ser programadores" (CS3, alumnos no-CS) → "Un prólogo a SICP" (con la cita correcta del foreword de Abelson, no del prefacio) → "La interacción como método, no como lujo" (Dijkstra) → "Tres decisiones que construyen una mente expandida" (HOF antes que recursión, cero mutación, programación simbólica) → "Leerlo hoy" (cierre volviendo a la dicotomía 500 vs. pocos, aplicada a los cursos intro actuales).

**Bibliografía:** _(todas las URLs de abajo fetcheadas y verificadas el 2026-07-15)_

Fuente primaria — el libro:
- *Simply Scheme: Introducing Computer Science*, Brian Harvey & Matthew Wright, MIT Press 1994 (2.ª ed. 1999). Índice: [ss-toc2.html](https://people.eecs.berkeley.edu/~bh/ss-toc2.html) — **frágil** (página personal de cátedra).
- Prefacio: [ssch0/preface.html](https://people.eecs.berkeley.edu/~bh/ssch0/preface.html) — **frágil**. Cita completa de los "500 mediocre programmers", la contracita de "expand their minds", el pasaje de Dijkstra y los datos de audiencia del curso (90% de mayors de CS con experiencia previa; alumnos de business administration y arquitectura).
- Prólogo (Hal Abelson): [ssch0/foreword.html](https://people.eecs.berkeley.edu/~bh/ssch0/foreword.html) — **frágil**. Cita "points the way out of the trap" — confirmada por fetch; es del foreword, no del prefacio. Verificado además **qué es "the trap"**: el currículum intro congelado alrededor de Pascal por el examen de Advanced Placement del College Entrance Examination Board de mediados de los '80 ("beginning courses are trapped in an approach that was already ten years out of date by the time it was canonized in the mid-1980s"). Útil para el hueco donde César pone su propia versión de la trampa.
- «To the Instructor»: [ssch0/instructor.html](https://people.eecs.berkeley.edu/~bh/ssch0/instructor.html) — **frágil**. Fuente de las tres decisiones de diseño en palabras de Harvey (orden HOF→lambda→recursión, `set!` evitado por el modelo de entornos, `vector-set!` como última concesión, simbólico temprano contra "boring numeric" programs).

Copias de respaldo del libro:
- [archive.org/details/SimplyScheme](https://archive.org/details/SimplyScheme) — **estable**. 2.ª ed. (1999), abierta y descargable (PDF/EPUB/texto). Ojo: es una subida de comunidad (usuario `creallfluharty`, 2019-03-31) compilada con `pdfunite` desde las páginas del sitio de Harvey — sirve de backup del texto, pero la fuente autorizada sigue siendo el sitio de los autores.
- [archive.org/details/simplyschemeintr00harv](https://archive.org/details/simplyschemeintr00harv) — **estable**. Edición 1994, MIT Press, ISBN 0262581329 / 9780262581325. Préstamo digital controlado (`access-restricted-item: true`), no abierta.

El curso:
- Brian Harvey, [CS 3: Introduction to Symbolic Programming](https://people.eecs.berkeley.edu/~bh/cs3.html), UC Berkeley — **frágil**. Confirma sigla, título y que el curso es *dual-purpose* (no exclusivamente para no-mayors: ver la corrección en la prosa).

Dijkstra (agregado en esta pasada — antes no había ninguna fuente suya):
- Edsger W. Dijkstra, «On the Cruelty of Really Teaching Computing Science», [EWD1036](https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html), archivo EWD, UT Austin — **estable**. Fuente primaria, preferida a Wikipedia por regla de la casa.
- Peter J. Denning (ed.), «A debate on teaching computing science», *Communications of the ACM*, vol. 32, nº 12, diciembre 1989, pp. 1397-1414 — [doi:10.1145/76380.76381](https://doi.org/10.1145/76380.76381) — **estable**. Metadatos verificados vía `api.crossref.org` (ACM DL bloquea el fetch directo). Es el venue que cita Harvey; contiene el ensayo de Dijkstra más las réplicas del debate.

**Imágenes:** ninguna (post sin imágenes, archivo plano seguiría siendo válido pero ya se creó como bundle)

**Tags propuestos:** `['libros','Scheme','pedagogia','Berkeley','Brian Harvey']`

---

## Borrador de prosa

Hay un libro de texto de 1994 cuyo prefacio arranca describiendo la posición que el libro **no** sostiene. Brian Harvey y Matthew Wright la llaman la vista conservadora, y la resumen así: «Therefore, the job of computer science education is to teach people how to discipline their work in such a way that 500 mediocre programmers can join together and produce a program that correctly meets its specification.»[^preface] Es decir: si el problema del software es que los programadores promedio no rinden, la solución es organizarlos, disciplinarlos, hacer que quinientos de ellos, juntos y bien coordinados, produzcan lo que ninguno produce solo.

Enfrente ponen la suya, la vista radical, y es una sola idea: en vez de disciplinar el trabajo de una masa, hay que **expandir la mente** de cada persona. La frase completa es «to teach people how to expand their minds so that the programs *can* fit, by learning to think in a vocabulary of larger, more powerful, more flexible ideas» — darle a una sola cabeza ideas más grandes para que sostenga lo que antes necesitaba un ejército.[^preface] Todo *Simply Scheme* es la consecuencia pedagógica de haber elegido el segundo bando. Y sí: el «500» del título de este post no es una estadística ni una anécdota de matrícula. Es la caricatura que los autores hacen del bando contrario, citada de su propio prefacio.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste vos a *Simply Scheme*? ¿Lo leíste como lector adulto, lo encontraste buscando material para enseñar, o apareció de rebote mientras estudiabas SICP? Una o dos frases alcanzan para abrir el post con algo tuyo.

### Un curso para los que no iban a ser programadores

*Simply Scheme: Introducing Computer Science* lo publicó MIT Press en 1994, con una segunda edición en 1999.[^ss] No es un libro para gente que va a dedicar su vida a esto. Es el libro de **CS 3: Introduction to Symbolic Programming**, el curso introductorio de Berkeley que Harvey describe como «a dual-purpose course; it's for people who are not intending to major in computer science but want an introduction to programming, and it's also for intended CS majors with no prior programming experience».[^cs3]

<!-- CORRECCIÓN 2026-07-15 (pasada de fuentes): el borrador anterior decía que el curso estaba "destinado a alumnos que **no** eran de informática", a secas. Las fuentes no lo sostienen así: CS 3 es explícitamente *dual-purpose*. El prefacio dice "The course at Berkeley for which we wrote this book includes both categories of students" — los no-mayors y el ~10% de mayors de CS sin experiencia previa. El ángulo del post (un curso que no puede apelar al "esto lo vas a necesitar después") sigue en pie para la mitad no-CS del aula, pero hay que decirlo con esa precisión, no como si el curso excluyera a los futuros informáticos. Nota: el **Concepto** de arriba arrastra el mismo error ("el primer curso de CS a no-mayors de informática") — corregirlo es decisión de César. -->

El prefacio agrega el detalle que le da peso al ángulo: cerca del 90% de los mayors de CS de Berkeley llegaban ya sabiendo programar, y muchos de los que llenaban CS 3 venían de administración de empresas o arquitectura, cumpliendo un requisito de razonamiento cuantitativo.[^preface]

Eso me parece la decisión más interesante de todas, y conviene detenerse en ella antes de hablar de Scheme. Un curso para futuros programadores puede justificar cualquier cosa apelando al futuro: «esto lo vas a necesitar». Un curso para gente que se va a dedicar a otra cosa no tiene esa muleta. Todo lo que enseñás tiene que valer la pena **ahora**, por sí mismo, como idea. Si el material no expande la cabeza de alguien que nunca más va a escribir un programa, el material no se defiende solo.

Y ahí es donde la dicotomía del prefacio deja de ser retórica y se vuelve un criterio de diseño de curso. La vista conservadora, llevada a un curso introductorio, produce un programa de estudios de entrenamiento: sintaxis, convenciones, la disciplina necesaria para ser una pieza confiable de un equipo grande. La vista radical produce otra cosa: un curso que apuesta a que la persona salga pensando distinto, aunque no salga sabiendo desplegar nada.

> 🕳️ **HUECO — necesita a César:** ¿te tocó alguna vez dar o cursar una materia introductoria de programación para gente que no iba a ser programadora? Si sí: ¿de qué lado caía el programa, el del entrenamiento o el de las ideas?

### Un prólogo a SICP

La otra manera de leer este libro es como rampa de acceso. *Simply Scheme* está pensado como introducción suave a los conceptos de SICP: llega a los mismos lugares, pero sin dar por sentado que quien lee ya piensa como un matemático.

El prólogo lo firma Hal Abelson — uno de los autores de SICP —, y ahí está la frase que a mí me quedó dando vueltas: el libro «points the way out of the trap».[^foreword] Vale la pena marcar de dónde sale, porque es exactamente el tipo de detalle que se ensucia al citar de memoria: **la frase es del prólogo de Abelson, no del prefacio de Harvey y Wright**. Son dos textos distintos, con dos autores distintos, al principio del mismo libro.

Y conviene decir qué es «the trap», porque Abelson es concreto: no habla de una trampa metafórica sino de un currículum congelado. «One of the best ways to stifle the growth of an idea is to enshrine it in an educational curriculum», arranca, y remata que los cursos introductorios «are trapped in an approach that was already ten years out of date by the time it was canonized in the mid-1980s, when the College Entrance Examination Board adopted an advanced placement exam based on Pascal».[^foreword] La trampa es esa: el examen estandarizado que fija una respuesta vieja y la vuelve obligatoria.

> 🕳️ **HUECO — necesita a César:** ¿cuál es «the trap» para vos, en tus palabras? Abelson usa la imagen; el post gana muchísimo si vos decís qué trampa ves en los cursos que conocés. Dos frases.

Y acá va el cross-link natural: si alguna vez intentaste entrar a SICP por la puerta principal y rebotaste, [[A2-01]] cuenta esa historia. *Simply Scheme* es, literalmente, la puerta lateral que los propios habitantes de la casa dejaron abierta.

### La interacción como método, no como lujo

<!-- RESUELTO 2026-07-15 (pasada de fuentes): la atribución a Dijkstra era buena y las dos ramas del VERIFICAR se cumplen a la vez. (b) Es Harvey quien trae a Dijkstra, en `preface.html`, y lo footnotea. (a) El EWD existe: es EWD1036, "On the Cruelty of Really Teaching Computing Science". Ojo con dos detalles: el footnote de Harvey escribe el título como "Computer Science", pero Dijkstra lo tituló "Computing Science"; y el ítem de CACM dic. 1989 vol. 32 nº 12 pp. 1397-1414 no es el ensayo suelto sino "A debate on teaching computing science", editado por Peter J. Denning, que contiene el texto de Dijkstra más las réplicas. Citar el EWD del archivo de UT Austin como fuente primaria y el DOI del debate como venue. -->

Acá el que trae a Dijkstra es el propio Harvey. En el prefacio lo presenta, con cuidado, como el caso que **no** es una caricatura: «In an article that was *not* intended as a caricature, the noted computer scientist Edsger Dijkstra argues that beginning computer science students *should not be allowed to use computers,* lest they learn to debug their programs interactively instead of writing programs that can be proven correct by formal methods before testing.»[^preface] Harvey no lo inventa como espantapájaros: lo footnotea.

Y el texto de Dijkstra dice exactamente eso. En EWD1036 describe un curso donde «the programming language in question has not been implemented on campus so that students are protected from the temptation to test their programs», porque para él «the programmer's task is not just to write down a program, but that his main task is to give a formal proof that the program he proposes meets the equally formal functional specification».[^ewd1036] No es una boutade: es la vista conservadora llevada hasta el final, sostenida por alguien que la pensó en serio.

Lo que sí se puede afirmar sin muletas es el encuadre. Escribir programas en Scheme, en un intérprete, escribiendo una expresión y viendo qué contesta, no es una comodidad de la herramienta: es el método. La expresión que escribís tiene un valor, y lo podés ver. La función que definiste se puede probar sola, sin un programa alrededor. La distancia entre «tengo una idea» y «veo qué pasa» es de un enter.

Un curso que apuesta a expandir mentes necesita ese ciclo corto, porque la unidad de trabajo del alumno deja de ser el programa y pasa a ser la **idea**. Y un curso que apuesta a disciplinar trabajadores no lo necesita tanto: ahí la unidad es el entregable.

> 🕳️ **HUECO — necesita a César:** ¿cuál fue el primer entorno interactivo que te cambió la manera de pensar — un REPL de Lisp, un intérprete de BASIC, otra cosa? El punto del post es que la interactividad es método y no lujo; contalo con tu caso.

### Tres decisiones que construyen una mente expandida

<!-- RESUELTO 2026-07-15 (pasada de fuentes): confrontadas las tres contra el índice de `ss-toc2.html` y contra `instructor.html`. Las tres se sostienen, con una corrección en la de mutación (ver abajo). Índice verificado: Parte III "Functions as Data" = cap. 8 Higher-Order Functions, 9 Lambda, 10 Tic-Tac-Toe; Parte IV "Recursion" = cap. 11-16. O sea: HOF y lambda antes que recursión, confirmado por el orden real del libro. -->

**Funciones de orden superior antes que recursión.** Confirmado por el índice: la Parte III es «Functions as Data» (cap. 8 *Higher-Order Functions*, cap. 9 *Lambda*) y recién la Parte IV es «Recursion» (cap. 11 a 16).[^ss] Es contraintuitivo para cualquiera que haya dado un curso intro. La recursión es el fantasma clásico de la materia, el tema donde se cae medio curso. Ponerla después de las funciones de orden superior sugiere que Harvey y Wright no la ven como el escalón difícil que hay que subir a los golpes, sino como algo que se entiende mejor **si ya aceptaste que una función es un dato**. Primero la idea grande; después la técnica. El propio Harvey lo explica en la nota al instructor: «We believe that higher-order procedures are easier to learn, especially because we begin in Chapter 8 by applying them only to named procedures»; el `lambda` viene después, y la recursión después de eso.[^instructor]

**Casi cero mutación.** Harvey lo pone como el rasgo más raro del libro: «One of the most unusual characteristics of this book is that there is no assignment to variables in it. The reason we avoid `set!` is that the environment model of evaluation is very hard for most students.»[^instructor] Y no es ascetismo: sin asignación no hay estado, y sin estado un programa es una expresión que vale algo. Podés razonar sobre él mirándolo.

<!-- CORRECCIÓN 2026-07-15: el borrador decía "Cero mutación" a secas. El libro no es cero mutación: en el último tramo introduce `vector-set!`. Harvey: "As the last topic in the book, we do introduce a form of mutation, namely `vector-set!`. Mutation of vectors is less problematic than mutation of lists, because lists naturally share storage." El índice lo respalda: Parte VI "Sequential Programming", cap. 23 "Vectors". Lo que el libro evita es la asignación *a variables* (`set!`), no toda mutación. Título de la viñeta ajustado a "Casi cero mutación" y agregado el párrafo de abajo. -->

Con una salvedad honesta, que conviene hacer antes de que la haga un lector: el libro no es cero mutación. En el último tramo —Parte VI, «Sequential Programming», donde aparecen los vectores— Harvey introduce `vector-set!`, y explica por qué esa y no otra: «Mutation of vectors is less problematic than mutation of lists, because lists naturally share storage».[^instructor] Lo que *Simply Scheme* evita durante casi todo el recorrido es la asignación a variables, no la mutación en general. La diferencia importa: lo que se está esquivando no es el estado por prolijidad, es el modelo de entornos.

**Programación simbólica.** No sólo números: palabras, oraciones, listas de cosas que no son cuentas — el libro las tiene desde el cap. 5, «Words and Sentences».[^ss] La razón que da Harvey es de motivación pura: «The advantage of an early introduction is that students can then write interesting symbolic programs instead of boring numeric ones.»[^instructor] Para un alumno que no va a ser programador, esto es la diferencia entre «esto es una calculadora complicada» y «esto es una manera de manipular ideas».

Las tres empujan al mismo lado. Ninguna te hace más rápido escribiendo código; las tres te hacen sostener más cosa en la cabeza a la vez.

### Leerlo hoy

La dicotomía del prefacio tiene treinta y pico de años y sigue siendo la pregunta de fondo de cualquier curso introductorio que mires hoy: ¿estamos formando quinientas personas confiables que juntas hacen mucho, o estamos tratando de que cada una salga pensando más grande de lo que entró?

Un curso intro moderno, con su stack, su framework y su deploy en la primera semana, está contestando esa pregunta aunque no la formule. Y es una respuesta defendible: la industria contrata gente que sepa moverse dentro de un equipo grande. Pero conviene saber que uno la está contestando, y que Harvey y Wright, en 1994, contestaron lo contrario a propósito y escribieron el libro entero para sostenerlo.

> 🕳️ **HUECO — necesita a César:** cierre. ¿De qué lado estás vos hoy, y cambió eso con los años? El post entero está construido sobre la dicotomía; el final necesita tu voto, no un resumen.

> 🕳️ **HUECO — necesita a César:** ¿querés que el cierre enganche con [[A2-07]] (DrRacket, para quien quiera correr los ejemplos hoy) y [[E-18]] (*The Little Lisper*, la otra rampa)? Si sí, decime en qué orden los ves.

[^ss]: *Simply Scheme: Introducing Computer Science*, Brian Harvey y Matthew Wright, MIT Press, 1994 (2.ª edición, 1999). Índice completo en [people.eecs.berkeley.edu/~bh/ss-toc2.html](https://people.eecs.berkeley.edu/~bh/ss-toc2.html). Texto completo de la 2.ª edición, compilado desde el sitio de los autores, en [archive.org](https://archive.org/details/SimplyScheme).
[^preface]: Prefacio de *Simply Scheme*: [people.eecs.berkeley.edu/~bh/ssch0/preface.html](https://people.eecs.berkeley.edu/~bh/ssch0/preface.html). Es la única aparición del número 500 en el libro.
[^foreword]: Prólogo de Hal Abelson a *Simply Scheme*: [people.eecs.berkeley.edu/~bh/ssch0/foreword.html](https://people.eecs.berkeley.edu/~bh/ssch0/foreword.html).
[^instructor]: «To the Instructor», nota preliminar de *Simply Scheme*: [people.eecs.berkeley.edu/~bh/ssch0/instructor.html](https://people.eecs.berkeley.edu/~bh/ssch0/instructor.html).
[^cs3]: Página del curso de Brian Harvey, [CS 3: Introduction to Symbolic Programming](https://people.eecs.berkeley.edu/~bh/cs3.html), UC Berkeley.
[^ewd1036]: Edsger W. Dijkstra, «On the Cruelty of Really Teaching Computing Science», [EWD1036](https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html), archivo EWD de UT Austin. Publicado como parte de «A debate on teaching computing science», editado por Peter J. Denning, *Communications of the ACM*, vol. 32, nº 12, diciembre de 1989, pp. 1397-1414 — [doi:10.1145/76380.76381](https://doi.org/10.1145/76380.76381). El footnote de Harvey en el prefacio de *Simply Scheme* cita este mismo número de CACM, aunque escribe el título como «Computer Science» en vez de «Computing Science».

**Estado actual:** borrador completo escrito en `content/es/posts/2026-04-16-simply-scheme-500-programadores/index.md` (2026-07-11), todavía sin `git add` ni commit. Título ajustado a "el libro que no quería 500 programadores mediocres" para reflejar la cita real. Pendiente: revisión final del usuario antes de commitear.

Además (2026-07-15): se agregó abajo una sección **Borrador de prosa** escrita desde este draft, siguiendo el outline de arriba y usando **solamente** las tres fuentes de la Bibliografía. Ojo: esta prosa se redactó sin leer el borrador ya existente en `content/es/posts/`, así que **son dos textos paralelos, no uno la continuación del otro** — antes de tocar nada hay que decidir cuál de los dos es el bueno y descartar el otro (o fusionarlos a mano).

Qué quedó escrito: el cold open con la dicotomía del prefacio, la sección de CS3, la sección del foreword de Abelson, la sección de interacción, las tres decisiones de diseño y el cierre.

**Pasada de fuentes (2026-07-15).** Se sourcearon y verificaron por fetch todas las URLs de la Bibliografía. **Los 4 `[VERIFICAR:]` que había quedaron resueltos**, ninguno borrado sin fuente:

1. **Cita truncada de los «500»** — RESUELTO. Oración completa transcripta desde `preface.html`, más la contracita completa de «expand their minds». La premisa central del Hook y el Concepto (la dicotomía conservadora/radical, el «500» como caricatura y no como estadística) **se confirma verbatim**. El cold open se sostiene tal cual está.
2. **Dijkstra** — RESUELTO, y mejor de lo esperado: se cumplen las dos ramas del marcador. Es Harvey quien trae a Dijkstra en `preface.html` y lo footnotea, *y* el EWD existe y dice lo que el draft suponía (EWD1036, «On the Cruelty of Really Teaching Computing Science», archivo de UT Austin). Agregados a la Bibliografía el EWD (fuente primaria) y el DOI del debate de CACM donde se publicó. La sección ya no es un esqueleto: tiene cita de Harvey y cita de Dijkstra.
3. **Las tres decisiones** — RESUELTAS contra el índice real y contra `instructor.html`, ahora con las palabras de Harvey. HOF antes que recursión: confirmado por el orden del libro (Parte III cap. 8-9 vs. Parte IV cap. 11-16). Simbólico temprano: confirmado (cap. 5). **Mutación: corregido** — el libro no es «cero mutación», introduce `vector-set!` como último tema (Parte VI, cap. 23); lo que evita es la asignación *a variables* (`set!`), y por una razón concreta (el modelo de entornos). Viñeta retitulada «Casi cero mutación» + párrafo con la salvedad.
4. **«CS3»** — RESUELTO **con corrección**. Es **CS 3: Introduction to Symbolic Programming**, confirmado en la página de curso de Harvey. Pero el público **no** es sólo no-mayors: es un curso *dual-purpose* (no-mayors + mayors de CS sin experiencia previa), y el prefacio lo dice igual («includes both categories of students»). La prosa quedó corregida. **⚠️ Ojo: el Concepto de arriba arrastra el mismo error** («el primer curso de CS a no-mayors de informática») — no se tocó porque el Concepto es de César, pero conviene ajustarlo. El ángulo del post no se cae: sigue valiendo para la mitad no-CS del aula.

Bonus no pedido: se verificó **qué es «the trap»** de Abelson (el currículum intro congelado alrededor de Pascal por el examen de AP del College Entrance Examination Board, mediados de los '80). Se agregó a la prosa como contexto, sin tocar el hueco que le pide a César su propia versión de la trampa.

Pendiente / no resuelto:
- **Backups de Wayback: no se pudieron verificar desde este entorno** (`web.archive.org` está bloqueado para fetch, y la API de disponibilidad devolvió `archived_snapshots` vacío para las páginas de `~bh/`). No se escribió ninguna URL de Wayback para no inventarla. Las 5 páginas de Berkeley son **frágiles y load-bearing** — conviene guardar snapshots a mano antes de publicar. Mitigación parcial ya en su lugar: el texto completo del libro está respaldado en `archive.org/details/SimplyScheme` (verificado).
- `people.eecs.berkeley.edu/~bh/ss.pdf` existe y devuelve un PDF de 1,7 MB, pero el fetch no pudo extraer el texto — **no se cita** como «libro completo» porque no se pudo confirmar qué contiene.
- **Los 6 huecos de César siguen abiertos** — ninguna búsqueda web los responde: cómo llegó al libro, si dio o cursó una intro para no-programadores, qué es «the trap» para él, su primer entorno interactivo, de qué lado está hoy, y el orden de los cross-links del cierre.
- Sigue pendiente lo de siempre: **hay dos textos paralelos** (este borrador y el de `content/es/posts/2026-04-16-.../index.md`). Esta pasada tocó **sólo el draft del plan**. Antes de publicar hay que decidir cuál es el bueno; si gana el de `content/es/posts/`, las fuentes de acá hay que portarlas a mano (en particular las de Dijkstra y la corrección de CS 3, que el otro texto casi seguro no tiene).
