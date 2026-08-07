### A1-15 — BASIC: el lenguaje educativo de Dartmouth (entrevista a Thomas E Kurtz)

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `basic-kurtz-dartmouth`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-basic-kurtz-dartmouth/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-13]], [[A2-04]] (sistemas expertos en BASIC), [[A2-05]] (Lisp en Spectrum)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** BASIC fue diseñado en 1964 por Kemeny y Kurtz en Dartmouth como un lenguaje *educativo* para que cualquier estudiante pudiera aprender a programar. Veinte años después estaba en cada microcomputadora del planeta. El post discute la entrevista a Kurtz, qué pasó con BASIC entre Dartmouth y los Spectrum/Commodore, y por qué la idea original (un lenguaje accesible para todos) se mantuvo viva pero se distorsionó.

**Hook:** BASIC se inventó en 1964 para enseñar a estudiantes de humanidades a programar. Veinte años después se usaba en cada computadora hogareña del mundo. Acá está la historia de cómo eso pasó, contada por uno de sus inventores.

**Outline:**

1. **Hook — dos lenguajes con el mismo nombre.** El BASIC de Dartmouth y el BASIC del Spectrum comparten sigla y poco más. La historia de cómo uno se convirtió en el otro.
2. **El problema no era el lenguaje: era el acceso.** Kemeny y Kurtz no querían un lenguaje fácil, querían que un estudiante de humanidades no le tuviera miedo a la computadora del campus.
3. **La mitad olvidada del invento: el time-sharing.** BASIC no se inventó solo; se inventó junto con el sistema que lo hacía usable. Sin la sala de terminales, el lenguaje no significa nada.
4. **Qué decisiones de diseño salen de «el usuario es un principiante».** Números de línea, mensajes de error legibles, arranque inmediato, ausencia de ritual.
5. **La entrevista a Kurtz en *Masterminds*.** El punto de entrada del post: cómo cuenta él lo que quisieron hacer, y qué dice del resultado.
6. **Dartmouth lo dio gratis — y ahí empieza la distorsión.** La decisión de no cobrar por el lenguaje es lo que lo hizo universal y lo que lo hizo incontrolable.
7. **Los veinte años: de la sala de terminales a la ROM del microcomputador.** Qué se perdió en el camino — el time-sharing, la estructura, el compilador, la intención pedagógica.
8. **La acusación: «BASIC arruina programadores».** El reproche clásico, y por qué es a la vez injusto con Dartmouth y certero sobre los dialectos hogareños.
9. **La defensa de los inventores.** Kemeny y Kurtz mirando su propia criatura a diez años vista, y el intento de recuperarla.
10. **Qué sobrevivió de la idea original.** La accesibilidad como objetivo de diseño explícito; la línea que va de ahí a los lenguajes que hoy usa todo el mundo.
11. **Cierre — quién es hoy el estudiante de humanidades.** La pregunta que Dartmouth contestó en 1964 sigue abierta.

**Bibliografía:**

_Fuentes verificadas por fetch el 2026-07-16. Se marca `estable`/`frágil` por entrada._

- [[tr-23]] Kurtz, Thomas E., entrevistado en *Masterminds of Programming* (Federico Biancuzzi & Shane Warden, O'Reilly, 2009) — [archive.org](https://archive.org/details/MastermindsOfProgramming). Capítulo BASIC: la voz de uno de los dos inventores. `estable`. Sesgo de fuente: parte interesada sobre el veredicto de su propia criatura.
- **BASIC nació el 1 de mayo de 1964 en Dartmouth** — página institucional del cincuentenario: [BASIC at Dartmouth](https://www.dartmouth.edu/basicfifty/basic.html) y [BASIC at 50](https://www.dartmouth.edu/basicfifty/). Confirma la fecha (4 a.m., 1 mayo 1964), la expansión «Beginner's All-purpose Symbolic Instruction Code», y que Kemeny fue luego el 13.º presidente de Dartmouth. `frágil` (micrositio de aniversario; respaldar en Wayback antes de publicar).
- [Computer Pioneers — John George Kemeny](https://history.computer.org/pioneers/kemeny.html) (IEEE Computer Society) — confirma la biografía previa de Kemeny: asistente en la Theoretical Division de Los Alamos (1945-1948) y asistente de investigación de Einstein en el Institute for Advanced Study de Princeton (1948-1949); presidente de Dartmouth 1970-1981. `estable`.
- [In Memoriam: Thomas E. Kurtz, 1928–2024](https://computerhistory.org/blog/in-memoriam-thomas-e-kurtz-1928-2024/) (Computer History Museum) — confirma a Kemeny y Kurtz como co-inventores de BASIC y del Dartmouth Time-Sharing System (DTSS), la máquina GE-225, el debut del DTSS junto con BASIC el 1 mayo 1964, la formación del comité ANSI X3J2 (Kurtz presidente 1974-1985) y la fundación de True BASIC, Inc. en 1983. `estable`.
- John G. Kemeny & Thomas E. Kurtz, *Back to BASIC: The History, Corruption, and Future of the Language* (Addison-Wesley, 1985) — ISBN 0-201-13433-0 / 978-0-201-13433-9. Copia en préstamo en [archive.org](https://archive.org/details/backtobasichisto0000keme). El balance de los propios inventores; sustituye la referencia genérica a *The First Ten Years* (ver nota al pie, sin verificar). `estable`.
- [The History of Microsoft — 1975](https://learn.microsoft.com/en-us/shows/history/history-of-microsoft-1975) (Microsoft Learn) — el tramo micros: Popular Electronics enero 1975 (Altair 8800 de MITS), Gates y Allen adaptan BASIC usando un emulador del 8080 en un PDP-10 de Harvard, demo a Ed Roberts en marzo 1975; el BASIC fue el primer producto de Microsoft. Fuente del propio fabricante. `estable`.
- [[tr-19]] Dijkstra, Edsger W., *How do we tell truths that might hurt?* (EWD498, 18 junio 1975) — archivo EWD de UT Austin: [transcripción](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD498.html). Fuente propia del veredicto sobre BASIC. `estable`.
- Kemeny & Kurtz, *BASIC: The First Ten Years* — **referencia sin verificar**: no se pudo confirmar por fetch que exista una publicación discreta con ese título/ficha (año, editorial). No confundir con *Back to BASIC* (1985), que sí está verificada arriba. Mantener el flag hasta ubicar la ficha o retirar la entrada.
- Documentación de Dartmouth BASIC — el manual original de 1964 no tiene URL canónica confirmada; el micrositio [basicfifty](https://www.dartmouth.edu/basicfifty/) es hoy el mejor punto institucional. `frágil` (fijar documento y URL exactos antes de citar).

**Imágenes:** _a definir_

**Tags propuestos:** `['BASIC','Kurtz','Kemeny','Dartmouth','historia','educacion']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (11 secciones), se fijó `Length target: medium` y se escribió un borrador de prosa completo (~2000 palabras de prosa efectiva, sin contar marcas de verificación ni huecos) en la sección «Borrador de prosa» al pie. El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 9 de 18 marcadores [VERIFICAR:].

Lo que quedó **escrito**: el armazón argumental entero — la tesis de que el invento de Dartmouth fue el conjunto lenguaje+time-sharing y no el lenguaje solo; el encuadre del acceso como problema real; las decisiones de diseño derivadas del usuario principiante; la distribución gratuita como causa simultánea del éxito y de la distorsión; el reproche «BASIC arruina programadores» tratado con justicia; y el cierre sobre quién ocupa hoy el lugar del estudiante de humanidades de 1964. Se sostiene solo como ensayo.

Lo que quedó como **hueco**:

- 7 huecos `🕳️` pidiendo a César recuerdos y opiniones propias: en qué máquina y a qué edad escribió BASIC por primera vez, qué dialecto era y si tuvo manual o aprendió por prueba y error, su experiencia real con `GOTO` y el código spaghetti, qué le pasó al leer la entrevista a Kurtz, si BASIC apareció en su formación formal, su opinión sobre si Python ocupa hoy el lugar de BASIC, y el veredicto personal del cierre. Sin eso el post es un ensayo correcto pero impersonal — no es un post de katra todavía.
- De las 18 marcas `[VERIFICAR:]` originales, el 2026-07-16 se resolvieron **9** con fuentes fetcheadas (ver bibliografía): fecha y primer programa (1 mayo 1964, 4 a.m., dos programas simultáneos); expansión de la sigla; cargos de Kemeny y Kurtz más la presidencia de Dartmouth; biografía previa de Kemeny (Los Álamos, asistente de Einstein); nombre y máquina del time-sharing (DTSS sobre GE-225); tramo Altair/Microsoft BASIC; veredicto de Dijkstra (EWD498, cita textual); True BASIC (1983/1985); y el estándar ANSI (X3J2, X3.113-1987, Kurtz presidente del comité 1974-1985). Quedan **9 sin resolver** por falta de fuente fetcheada: la proporción de estudiantes que usaba el sistema (ningún porcentaje confirmado), las 2/3 citas textuales del capítulo de Kurtz en *Masterminds* (requiere el libro en mano), el reparto exacto de tareas Kemeny/Kurtz, los términos legales de la distribución gratuita, el linaje concreto de las BASIC en ROM de Sinclair/Commodore, la ficha de *The First Ten Years*, y la URL exacta del manual Dartmouth de 1964.
- **Punto de decisión antes de escribir en serio**: la bibliografía pasó de tres a nueve entradas y ya no es sólo la voz de los inventores — se sumaron fuentes de tercera parte (IEEE Computer Society, Computer History Museum, UT Austin/EWD) y una fuente del propio fabricante para el tramo micros (Microsoft Learn), que antes no tenía **ninguna** fuente. Sigue en pie la decisión editorial de si el post cuenta el tramo 1975-1985 en detalle o se recorta a «lo que Dartmouth quiso hacer», dejando Spectrum/Commodore para [[A2-04]] y [[A2-05]]; pero ya no por falta de fuentes, sino por foco.
- Ojo con el sesgo de fuente: Kemeny y Kurtz escribiendo sobre BASIC son parte interesada. Donde el borrador dice «los inventores sostienen», eso está bien; donde tienda a deslizarse a «está probado que», hay que frenarlo.
- `**Imágenes:**` sigue en `_a definir_` — los candidatos obvios son una terminal Teletype de la sala de Dartmouth o una pantalla de arranque de BASIC en ROM, pero hay que encontrar una con licencia clara en Wikimedia Commons.

---

## Borrador de prosa

Hay dos lenguajes que se llaman BASIC.

Uno vive en una sala con terminales ruidosas de un college de New Hampshire, a mediados de los sesenta, y lo usa una estudiante de literatura que nunca vio una computadora en su vida y que tampoco planea volver a verla después de esta semana. El otro vive en la ROM de una máquina de plástico enchufada al televisor del living, veinte años después, y lo usa un pibe de trece que quiere que el sprite se mueva. Comparten la sigla. Comparten `PRINT`, `GOTO` y los números de línea. Y a partir de ahí se parecen bastante menos de lo que uno supondría.

Voy a contarte cómo el primero se convirtió en el segundo, porque esa transformación es una de las historias más raras de la computación: un lenguaje diseñado con un objetivo pedagógico explícito y bastante noble terminó, dos décadas más tarde, siendo la puerta de entrada de una generación entera al oficio, y al mismo tiempo la cosa que los programadores serios usaban como insulto. Las dos cosas a la vez. Y el punto de entrada es la entrevista a Thomas E. Kurtz, uno de los dos inventores, en *Masterminds of Programming*.[^masterminds]

### El problema no era el lenguaje

Acá está el malentendido que quiero desarmar primero, porque ordena todo lo demás.

Cuando se cuenta la historia de BASIC, se cuenta como si Kemeny y Kurtz se hubieran sentado a diseñar «un lenguaje fácil». Como si el problema fuera que Fortran era difícil y ellos hubieran inventado un Fortran con menos aristas.

No. El problema era el **acceso**.

En Dartmouth, a principios de los sesenta, había una computadora. Una. Y para usarla tenías que ser parte de un sacerdocio: escribías tu programa en un formulario, lo perforabas en tarjetas o se lo dabas a alguien que las perforara, entregabas el mazo en una ventanilla, y al otro día te devolvían un listado que casi siempre decía que te habías olvidado una coma. Ese ciclo — un intento por día, mediado por un operador — no es difícil. Es otra cosa peor: es **desalentador**. Nadie aprende nada con un ciclo de retroalimentación de veinticuatro horas.

Kemeny y Kurtz querían que cualquier estudiante de Dartmouth — el de historia, el de literatura, el de música, no sólo el de ingeniería — pudiera acercarse a la computadora y usarla. No para volverse programador. Para no tenerle miedo. La idea de fondo era que en el mundo que venía la computación iba a ser parte de la vida educada de cualquiera, y que un college que enseñaba a sus alumnos a leer y a escribir también les debía esto.

Ese es el proyecto. BASIC es una pieza del proyecto, no el proyecto.

A las 4 de la madrugada del 1 de mayo de 1964, en el sótano de College Hall, John Kemeny y un estudiante tipearon `RUN` al mismo tiempo en terminales vecinas; los dos programas corrieron simultáneamente y devolvieron la respuesta correcta. Ese fue el momento de nacimiento conjunto del time-sharing y de BASIC en Dartmouth.[^dartmouth]

La sigla se expande como «Beginner's All-purpose Symbolic Instruction Code».[^dartmouth]

Kemeny y Kurtz eran ambos profesores de matemática en Dartmouth; Kemeny fue después el 13.º presidente del college (1970-1981).[^dartmouth] [^kemeny] Antes de Dartmouth, Kemeny había trabajado en la Theoretical Division del Proyecto de Los Álamos (1945-1948) y fue asistente de investigación de Albert Einstein en el Institute for Advanced Study de Princeton (1948-1949).[^kemeny]

### La mitad olvidada: el time-sharing

Esto es lo que casi nunca se cuenta, y sin esto BASIC no se entiende.

Kemeny y Kurtz no inventaron un lenguaje. Inventaron un **sistema**: un lenguaje más un sistema de tiempo compartido más una sala llena de terminales más la política de que cualquier estudiante entrara y lo usara sin pedir permiso a nadie. Las cuatro cosas juntas eran el invento. El lenguaje solo no hace nada.

Pensalo así: ¿de qué sirve un lenguaje con mensajes de error amables si el error te llega al otro día en un listado? El lenguaje amable **necesita** que la máquina te conteste ahora. Los números de línea, la sintaxis mínima, el arranque instantáneo — todo eso es una respuesta a la pregunta «¿cómo hago para que esta chica escriba algo, vea qué pasa, y lo corrija antes de aburrirse?». La respuesta pedagógica es «reduciendo el ciclo de retroalimentación a segundos», y eso es time-sharing, no diseño de lenguajes.

Por eso me parece un error de encuadre decir que Dartmouth inventó un lenguaje educativo. Dartmouth inventó el **acceso interactivo a la computadora para gente común**, y BASIC es la superficie de ese invento — la parte que se podía copiar y llevar puesta. Que sea la única parte que sobrevivió en la memoria colectiva es, en sí mismo, el tema de este post.

El sistema se llamaba DTSS, Dartmouth Time-Sharing System, corría sobre una mainframe General Electric GE-225 y debutó junto con BASIC el 1 de mayo de 1964.[^kurtz]

[VERIFICAR: la afirmación de que una mayoría amplia de los estudiantes de Dartmouth usaba el sistema. El dato circula como «más del 80%» sin fuente clara. Si *The First Ten Years* da un número, citarlo; si no, escribirlo cualitativamente y sin porcentaje.]

> 🕳️ **HUECO — necesita a César:** ¿cuál fue la primera máquina en la que escribiste BASIC, a qué edad, y en qué contexto — casa, escuela, club, trabajo? Es el ancla del post: sin esto el texto es historia ajena.

> 🕳️ **HUECO — necesita a César:** ¿qué dialecto era? ¿Tenías manual, o aprendiste mirando lo que hacían otros y probando? El contraste entre «manual del fabricante» y «prueba y error» es justo el tema del post.

### Las decisiones que salen de mirar al principiante

Si aceptás que el usuario objetivo es alguien que nunca programó y que tal vez no vuelva a programar nunca, un montón de decisiones de diseño dejan de parecer torpes y pasan a parecer deliberadas.

**Los números de línea.** Hoy son el chiste. En 1964 eran el editor. No había pantalla con cursor: tenías una terminal que imprime en papel. ¿Cómo corregís la línea 30 sin volver a tipear el programa entero? Escribís `30` y lo que va. El número de línea no es una decisión sobre el lenguaje, es una decisión sobre la interfaz — y con el hardware de esa sala, es una buena decisión.

**Los mensajes de error en castellano — bueno, en inglés, pero entendibles.** La cultura de la época te daba un código hexadecimal y te deseaba suerte. Decirle al usuario qué hizo mal, con palabras, es una decisión pedagógica.

**El arranque sin ritual.** Nada de declarar, nada de importar, nada de `main`. Te sentás y escribís `PRINT 2+2`. Esto suena trivial y no lo es: cada línea de ceremonia entre la persona y su primer resultado es una línea donde la persona se va.

**Poco lenguaje.** Un principiante no necesita expresividad, necesita poder tener el lenguaje entero en la cabeza.

Ninguna de estas decisiones es sobre elegancia. Todas son sobre la primera media hora del usuario. Y esa es una forma de diseñar que sigue siendo rarísima: la mayoría de los lenguajes se diseñan pensando en el usuario del año tres, no en el de los primeros treinta minutos.

### Kurtz contándolo

[[E-09]] y [[A1-13]] ya se ocupan de *Masterminds of Programming* como libro y del roster completo de entrevistas, así que acá voy directo a lo que me importa: el capítulo de BASIC es una conversación con Thomas Kurtz, y su valor está en que Kurtz habla de la **intención**, que es lo que ninguna historia técnica conserva.

> 🕳️ **HUECO — necesita a César:** ¿qué te pasó cuando leíste la entrevista a Kurtz? ¿Hay alguna respuesta suya que te haya hecho parar y releer, o que te haya cambiado la opinión que tenías sobre BASIC? Una o dos frases alcanzan.

[VERIFICAR: releer el capítulo de Kurtz en *Masterminds* y anotar 2 o 3 citas textuales aprovechables — en particular sobre el reparto de tareas con Kemeny, sobre qué opina de los dialectos de micro, y sobre si considera que el proyecto original fracasó o triunfó. Este post no debería escribirse sin esas citas en la mano: la entrevista es el punto de entrada declarado y hoy está citada de manera genérica.]

[VERIFICAR: el reparto real de tareas entre Kemeny y Kurtz. La formulación cómoda («Kemeny el matemático, Kurtz el del sistema») es demasiado prolija para ser cierta. Contrastar contra la entrevista y contra *The First Ten Years* antes de afirmar cualquier división de trabajo.]

### Dartmouth lo regaló

Acá está la bisagra de toda la historia, y es una decisión, no un accidente.

Dartmouth no cobró por BASIC. No lo licenció, no lo protegió, no lo convirtió en producto. Lo dejó salir. Y eso hizo dos cosas al mismo tiempo, inseparables:

Lo hizo **universal**. En quince años BASIC estaba en todos lados, y no por marketing sino porque no había fricción para tomarlo.

Y lo hizo **incontrolable**. Si no cobrás y no controlás, no tenés autoridad sobre lo que otros llamen «BASIC». Cada fabricante hizo el suyo, con las restricciones de su hardware y el criterio de sus programadores, y todos le pusieron el mismo nombre. El nombre viajó; el proyecto no.

Hay una ironía dura acá: la decisión más generosa de la historia de BASIC es exactamente la que garantizó que el BASIC que el mundo conoció no fuera el de Dartmouth. Le sacaron el candado, y lo que se escapó fue el prestigio.

[VERIFICAR: los términos concretos de la distribución — ¿dominio público, licencia, «distribuido sin cargo»? ¿Hubo una decisión explícita documentada, y de quién? No inventar la figura legal.]

### Los veinte años que van de la sala al living

El tramo 1964→1984 es el corazón del concepto de este post y es, también, el tramo del que la bibliografía actual del draft **no dice nada**. Así que lo escribo como esqueleto, marcado, y no como relato.

Lo que sí puedo afirmar sin fuente es la forma de la pérdida, porque es deducible del propio hardware: cuando BASIC entró en la ROM de una máquina hogareña, entró **solo**. Sin la sala de terminales, sin el sistema de tiempo compartido, sin el curso, sin el ayudante, sin la institución que había decidido que valía la pena que la chica de literatura aprendiera. Entró el lenguaje y se quedó afuera todo el resto del invento — que, como argumenté arriba, era el invento.

Y encima entró recortado por la máquina: pocos kilobytes, sin las estructuras que Dartmouth había ido agregando, con el `GOTO` como única herramienta real de control de flujo. El BASIC del living no es una degradación cultural del BASIC de Dartmouth: es lo que entra en 8K.

El tramo Altair/Microsoft sí quedó documentado: en enero de 1975 *Popular Electronics* mostró en tapa la Altair 8800 de MITS; Paul Allen y Bill Gates adaptaron BASIC para esa máquina escribiendo un emulador del microprocesador 8080 sobre un PDP-10 de Harvard, y en marzo de 1975 Allen se lo demostró a Ed Roberts en Albuquerque. Ese BASIC fue el primer producto de Microsoft.[^microsoft]

[VERIFICAR: las BASIC en ROM de los micros hogareños (Sinclair, Commodore) — quién las proveía, qué relación de linaje tenían entre sí y con Dartmouth. Ídem: sin fuente en el draft. Coordinar con [[A2-04]] y [[A2-05]], que ya tocan el tema.]

### «BASIC arruina programadores»

El reproche clásico. Hay que tratarlo, y hay que tratarlo con justicia, porque tiene una parte cierta y una parte tramposa.

La parte cierta: un lenguaje sin subrutinas decentes, sin variables locales, sin estructuras de control, con `GOTO` como pegamento universal, efectivamente te enseña a construir cosas que no se pueden mantener. No porque seas descuidado, sino porque el lenguaje no te da con qué. El código spaghetti no es un vicio moral del programador de BASIC: es la única forma disponible.

La parte tramposa: eso describe a los BASIC de ROM, no al BASIC de Dartmouth, que era otra cosa y siguió evolucionando. Cuando la crítica dice «BASIC», está apuntando a los hijos y le pega al padre.

Y hay una tercera parte, la que a mí me interesa: aun aceptando todo lo anterior, **de esa generación salieron programadores**. Un montón. Gente que entró por una máquina de plástico y un `GOTO` y terminó haciendo carrera. Si el lenguaje mutila irreversiblemente, ¿cómo se explican? La respuesta honesta creo que es que la accesibilidad tiene un valor que la crítica no sabe medir: un mal lenguaje que te deja entrar produce más programadores que un buen lenguaje que te deja afuera. Lo cual no vuelve bueno al mal lenguaje. Sólo vuelve incompleta a la crítica.

El veredicto de Dijkstra está en EWD498, *How do we tell truths that might hurt?*, del 18 de junio de 1975: «It is practically impossible to teach good programming to students that have had a prior exposure to BASIC: as potential programmers they are mentally mutilated beyond hope of regeneration».[^dijkstra]

> 🕳️ **HUECO — necesita a César:** ¿escribiste código spaghetti con `GOTO` de verdad? ¿Te acordás del momento en que un programa tuyo se te volvió inmanejable y no sabías por qué? Y la contracara: ¿cuándo y con qué lenguaje te cayó la ficha de que había otra forma?

> 🕳️ **HUECO — necesita a César:** ¿BASIC apareció alguna vez en tu formación formal — escuela, facultad — o fue siempre algo de afuera del aula? Si estuvo, ¿cómo lo trataban los docentes: como herramienta o como algo de lo que había que curarse?

### Los inventores mirando su criatura

*BASIC: The First Ten Years*[^tenyears] es el balance que Kemeny y Kurtz hacen de su propio invento a diez años vista, y ya el título dice algo: en 1974 esto todavía era un proyecto vivo con dueños, no un fósil.

Hay que leerlo con la advertencia puesta: son parte interesada. Es la fuente más valiosa sobre la intención y la menos confiable sobre el veredicto.

[VERIFICAR: la ficha bibliográfica completa de *BASIC: The First Ten Years* — año, editorial o si es un informe técnico de Dartmouth, y si hay copia accesible. No inventar editorial ni ISBN. La fecha «1974» que sugiere el título es inferencia, no dato.]

Sí lo hicieron: en 1983 Kurtz se sumó a Kemeny y a tres ex alumnos de Dartmouth para fundar True BASIC, Inc., cuyo objetivo era un compilador de BASIC independiente de plataforma y software educativo de calidad; True BASIC se lanzó en 1985.[^kurtz]

Y sí hubo estándar: Kurtz ayudó a formar el comité ANSI X3J2 y lo presidió de 1974 a 1985; ese trabajo desembocó en el estándar ANSI X3.113-1987 para Full BASIC, que extendía el anterior X3.60-1978 para Minimal BASIC.[^kurtz]

### Lo que sobrevivió

Sacale a BASIC los números de línea, el `GOTO` y la nostalgia. ¿Qué queda?

Queda una idea, y sigue siendo minoritaria: **que la accesibilidad para el principiante puede ser un objetivo de diseño de primera clase, y no una concesión que se hace después de que el lenguaje ya está diseñado para expertos.**

Eso es lo que Dartmouth hizo y casi nadie más hizo. La mayoría de los lenguajes se diseñan para el que ya sabe, y después alguien escribe un tutorial. BASIC se diseñó al revés: desde la primera media hora del que no sabe, hacia afuera.

Y esa idea ganó, aunque el lenguaje perdiera. Cada vez que alguien elige que su lenguaje arranque sin ceremonia, que el error se explique con palabras, que se pueda probar una línea suelta y ver qué pasa — está en la línea de Dartmouth, sepa o no. El REPL de Python es la sala de terminales de 1964 con mejor tipografía.

> 🕳️ **HUECO — necesita a César:** ¿estás de acuerdo con que Python ocupa hoy el lugar que BASIC ocupó en el 64 — el lenguaje que le enseñás a alguien que no va a ser programador? ¿O te parece que ya no hay ningún lenguaje en ese lugar y la puerta de entrada hoy es otra cosa?

### ¿Quién es hoy el estudiante de humanidades?

Cierro con la pregunta que me quedó dando vueltas, que es más grande que BASIC.

Kemeny y Kurtz partieron de una convicción: que en el mundo que venía, entender algo de computación iba a ser parte de estar educado, y que por lo tanto la universidad tenía la obligación de que la chica de literatura pudiera sentarse frente a la máquina sin pedirle permiso a un sacerdote.

Sesenta años después ganaron tanto que el planteo se volvió invisible. Todos tienen una computadora encima. Nadie le tiene miedo. Y sin embargo casi nadie puede decirle a la suya que haga algo que el fabricante no previó. Cambiamos la sala de terminales por un dispositivo que hace mil cosas y no se programa. El miedo se fue; el acceso, en el sentido fuerte que le daban ellos, no estoy tan seguro.

Así que la pregunta de 1964 sigue abierta, sólo que ahora no es «cómo hacemos que se anime a tocarla» sino «cómo hacemos que se anime a decirle qué hacer». Y para esa pregunta todavía no hay una sala de terminales.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto, no el mío. ¿La historia de BASIC te da nostalgia, bronca, o alegría? ¿Y qué le contestarías a Kurtz si te preguntara si valió la pena regalarlo?

---

[^masterminds]: Entrevista a Thomas E. Kurtz sobre BASIC, en *Masterminds of Programming* — ver [[tr-23]] en el plan editorial.
[^tenyears]: John G. Kemeny y Thomas E. Kurtz, *BASIC: The First Ten Years*. [VERIFICAR: ficha bibliográfica completa — año, editorial o naturaleza del documento, y si existe copia accesible en línea. No inventar datos de edición. Nota 2026-07-16: no se pudo confirmar por fetch que exista una publicación discreta con este título; la que sí está verificada es *Back to BASIC: The History, Corruption, and Future of the Language* (Addison-Wesley, 1985, ISBN 978-0-201-13433-9), que cumple la misma función de «balance de los inventores». Considerar reemplazar esta cita por aquélla.]
[^kemeny]: [Computer Pioneers — John George Kemeny](https://history.computer.org/pioneers/kemeny.html), IEEE Computer Society — Los Álamos (1945-1948), asistente de Einstein en el IAS de Princeton (1948-1949), presidente de Dartmouth 1970-1981.
[^kurtz]: [In Memoriam: Thomas E. Kurtz, 1928–2024](https://computerhistory.org/blog/in-memoriam-thomas-e-kurtz-1928-2024/), Computer History Museum — co-invención de BASIC y DTSS, máquina GE-225, comité ANSI X3J2 (Kurtz presidente 1974-1985) y fundación de True BASIC, Inc. (1983).
[^microsoft]: [The History of Microsoft — 1975](https://learn.microsoft.com/en-us/shows/history/history-of-microsoft-1975), Microsoft Learn — Altair 8800, el emulador del 8080 sobre PDP-10, la demo a Ed Roberts y el BASIC como primer producto de Microsoft.
[^dijkstra]: Edsger W. Dijkstra, *How do we tell truths that might hurt?*, [EWD498](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD498.html) (18 de junio de 1975), archivo EWD de UT Austin — ver [[tr-19]].
[^dartmouth]: [BASIC at Dartmouth](https://www.dartmouth.edu/basicfifty/basic.html) y [BASIC at 50](https://www.dartmouth.edu/basicfifty/), páginas institucionales del cincuentenario — fecha (4 a.m., 1 mayo 1964), expansión de la sigla, y Kemeny como 13.º presidente. [VERIFICAR: el manual original de 1964 como documento concreto — dónde está alojado hoy y su URL — sigue sin fijarse; el micrositio del cincuentenario es por ahora el mejor punto institucional. Respaldar en Wayback antes de publicar (micrositio de aniversario, `frágil`).]
