### C-08 — Por qué MDA y Executable UML nunca cumplieron sus promesas

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `mda-uml-promesas-incumplidas`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mda-uml-promesas-incumplidas/index.md`
- **Serie:** filosofia
- **Cross-links:** [[C-02]] (Hickey simple vs easy), [[C-03]] (Tidy First)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 2000-2200 palabras (elegido 2026-07-15: alcanza para desarrollar el argumento central — la sintaxis no es el problema — con los cuatro momentos históricos, sin convertirse en historia de UML)

**Concepto:** Model Driven Architecture (MDA) y Executable UML prometieron en los 2000 que la "verdadera productividad" venía de abandonar lenguajes de programación tradicionales en favor de notaciones visuales. Veinte años después, casi nadie usa MDA ni Executable UML en producción. El post discute por qué — la clave es que el problema central de la programación no es la sintaxis, es la *especificación de comportamiento*, y los gráficos no resuelven eso mejor que el código.

**Hook:** cada cinco años aparece alguien que dice "el código texto ya fue, ahora vamos a programar con diagramas". MDA. Executable UML. Low-code. No-code. Cada vez. Nunca funciona. ¿Por qué?

**Outline:**

1. **El hook** — el ciclo que se repite cada cinco años: «el código texto ya fue». MDA, Executable UML, low-code, no-code.
2. **Qué prometía MDA, exactamente** — PIM / PSM / transformaciones, según la *MDA Guide* de la OMG. La promesa no era «dibujar en vez de escribir»: era *separar* la especificación de la plataforma.
3. **Qué prometía Executable UML** — Mellor & Balcer: el modelo no documenta el sistema, el modelo *es* el sistema.
4. **Por qué la promesa seduce** — la hipótesis implícita: el cuello de botella de la programación es la sintaxis.
5. **Por qué la hipótesis es falsa** — el trabajo duro es la especificación de comportamiento: qué pasa cuando dos cosas ocurren a la vez, qué pasa cuando falla, qué significa exactamente «cliente activo».
6. **El momento en que el diagrama se convierte en código** — el lenguaje de acción. Todo modelo ejecutable termina necesitando uno, y ahí la notación visual se rinde.
7. **Las críticas contemporáneas** — Meyer («UML: The Positive Spin», 1997 — parodia, y anterior a MDA: apunta a UML), Fowler («Model Driven Architecture», 2004, y «Platform Independent Malapropism», 2003) y Dave Thomas («MDA: Revenge of the Modelers or UML Utopia?», *IEEE Software*, 2004). _(corregido en la pasada de fuentes del 2026-07-15: la pieza de Fowler «MDA-aware tools» que decía este outline no existe; ver Bibliografía.)_
8. **El costo que nadie cotizó** — diff, merge, blame, grep, revisión en pull request. El texto plano no es una limitación: es una infraestructura.
9. **El ciclo se repite** — low-code / no-code son la misma apuesta con otro traje.
10. **Qué sí sobrevivió** — el diagrama como conversación, no como fuente de verdad.
11. **Cierre** — la pregunta que hay que hacerle a la próxima ola.

**Bibliografía:** _(pasada de fuentes 2026-07-15 — todas las URL fetcheadas y verificadas)_

**Fuentes primarias — la promesa**

- **OMG, *MDA Guide Version 1.0.1*** — documento `omg/2003-06-01`, 12 jun 2003, eds. Joaquin Miller y Jishnu Mukerji. [PDF en omg.org](https://www.omg.org/news/meetings/workshops/UML_2003_Manual/00-2_MDA_Guide_v1.0.1.pdf) · [Wayback 2026-02-27](http://web.archive.org/web/20260227105813/http://www.omg.org/news/meetings/workshops/UML_2003_Manual/00-2_MDA_Guide_v1.0.1.pdf) — **estable** (dominio institucional + backup). CIM/PIM/PSM en §2.2.10–2.2.11 y §3.1–3.2. No existe una landing page de la OMG para la guía; el PDF es la fuente canónica disponible.
- **Richard Soley & OMG Staff Strategy Group, *Model Driven Architecture* (MDA White Paper)** — Draft 3.2, 27 nov 2000. [omg.org](https://www.omg.org/mda/mda_files/model_driven_architecture.htm) — **estable**. El documento fundacional, tres años anterior a la guía. Fuente para la promesa de negocio (proliferación de middleware, lock-in).
- **Stephen J. Mellor & Marc J. Balcer, *Executable UML: A Foundation for Model-Driven Architecture*** — Addison-Wesley Professional, 1.ª ed., 14 may 2002, 416 pp., Addison-Wesley Object Technology Series, ISBN 978-0-201-74804-8. [Página del editor (InformIT)](https://www.informit.com/store/executable-uml-a-foundation-for-model-driven-architecture-9780201748048) · [Wayback 2025-11-18](http://web.archive.org/web/20251118130153/https://www.informit.com/store/executable-uml-a-foundation-for-model-driven-architecture-9780201748048) — **frágil** (página comercial). **Sin copia en archive.org** (verificado por advanced search).

**Fuentes primarias — la crítica contemporánea**

- **Bertrand Meyer, «UML: The Positive Spin»** — *American Programmer* (ed. Ed Yourdon), número especial sobre UML, 1997. [archive.eiffel.com](https://archive.eiffel.com/doc/manuals/technology/bmarticles/uml/page.html) · [Wayback 2026-04-30](http://web.archive.org/web/20260430094429/https://archive.eiffel.com/doc/manuals/technology/bmarticles/uml/page.html) — **frágil pero load-bearing**, backup obligatorio. Sitio de la casa del propio Meyer (regla de la casa: autor antes que Wikipedia). Es una **parodia**, no un ensayo — ver nota de tono en el footnote.
- **Martin Fowler, «Model Driven Architecture»** — bliki, 2 feb 2004. [martinfowler.com](https://martinfowler.com/bliki/ModelDrivenArchitecture.html) · [Wayback 2026-05-25](http://web.archive.org/web/20260525214117/https://martinfowler.com/bliki/ModelDrivenArchitecture.html) — **frágil**.
- **Martin Fowler, «Platform Independent Malapropism»** — bliki, 12 sep 2003. [martinfowler.com](https://martinfowler.com/bliki/PlatformIndependentMalapropism.html) — **frágil**.
- **Martin Fowler, «Language Workbenches and Model Driven Architecture»** — 12 jun 2005. [martinfowler.com](https://martinfowler.com/articles/mdaLanguageWorkbench.html) — **frágil**. Útil para el matiz: Fowler considera «irrelevante» la discusión gráfico-vs-texto y objeta los estándares de la OMG, no el modelado. Si el post entra en DSL/language workbenches, es por acá.
- **Dave Thomas, «MDA: Revenge of the Modelers or UML Utopia?»** — *IEEE Software*, vol. 21, n.º 3, may/jun 2004. DOI [10.1109/MS.2004.1293067](https://doi.org/10.1109/MS.2004.1293067) — **estable** (DOI, verificado vía Crossref). Mirror libre: [PDF en martinfowler.com](https://martinfowler.com/ieeeSoftware/mda-thomas.pdf). **La fuente más valiosa de la pasada**: dice la tesis del post en 2004 y desde adentro de IEEE.

**Contexto técnico**

- **«History of Executable UML — Action Language: An OMG Journey»** — modeling-languages.com. [URL](https://modeling-languages.com/uml-action-language-omg-journey/) · [Wayback 2025-12-16](http://web.archive.org/web/20251216112628/https://modeling-languages.com/uml-action-language-omg-journey/) — **frágil**. RFP de Mellor (1998), Action Semantics en UML 1.5 (2002), sin lenguaje estándar en UML 1.x, Alf adoptado en 2010.
- **Dirk Ohst, Michael Welle & Udo Kelter, «Differences between versions of UML diagrams»** — ESEC/FSE 2003, Helsinki, ACM, pp. 227–236. DOI [10.1145/940071.940102](https://doi.org/10.1145/940071.940102) — **estable** (DOI, verificado vía Crossref; ACM DL bloquea fetch). Respalda la sección del costo de infraestructura.

**Descartadas / no encontradas**

- **Fowler, «MDA-aware tools»** — **no existe**. Ver nota de sourcing en la sección de críticas.
- **ooatool.com (Leon Starr), página sobre action languages** — falla el handshake TLS y **no tiene ningún snapshot en Wayback**. Inutilizable.
- **Página de soporte de IBM sobre Rational Rose RealTime Model Integrator** — HTTP 403 al fetch. Sin verificar.

**Imágenes:** _a definir_

**Tags propuestos:** `['MDA','UML','Executable UML','Model Driven','low-code','critica']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (11 puntos), length target (2000-2200 palabras) y un borrador de prosa completo al final del archivo.

Lo que quedó escrito: el argumento entero está armado y es autosuficiente — el ciclo que se repite, la promesa de MDA en términos de PIM/PSM/transformaciones, la apuesta de Mellor & Balcer, la tesis central (el cuello de botella no es la sintaxis sino la especificación de comportamiento), el argumento del lenguaje de acción, el costo de infraestructura del formato binario, y el paralelo con low-code/no-code.

Lo que quedó como hueco (6 marcadores `🕳️`): todo lo biográfico. El post está escrito en primera persona y la voz pide recuerdos concretos que no se pueden inventar — qué herramienta CASE usó César y cuándo, si hubo UML en la STG o en el Ministerio de Cultura de Santa Fe, si enseñó UML, cuál fue el momento en que dejó de creer en la generación de código, y qué ola de low-code le tocó de cerca. Sin eso el post es un ensayo genérico; con eso es un post de katra.

**Pasada de fuentes (2026-07-15).** Se sourceó el draft contra la web: 10 referencias nuevas verificadas por fetch, 9 marcadores `[VERIFICAR:]` bajados a 3. La premisa central **se sostiene y salió reforzada**.

*Lo que se resolvió:*

- **CIM confirmado en la edición de 2003.** El término exacto es «Computation Independent Model» (no «Computational») y está en la MDA Guide v1.0.1 §2.2.11 y §3.1. Documento `omg/2003-06-01`, 12 jun 2003, eds. Miller y Mukerji — todo verificado extrayendo el texto del PDF de omg.org, no de un resumen.
- **Meyer leído entero.** El tono era el riesgo señalado y con razón: no es ironía suave, es una **parodia** completa (carta de un estudiante ficticio, Candide Smith). Se reescribió la sección con sus objeciones reales. Dato de cronología que el draft no tenía: es de **1997**, cuatro años anterior a MDA — Meyer critica UML, no MDA. La sección ahora lo dice explícitamente en vez de dejar que el lector lo suponga.
- **Mellor & Balcer**: editorial, subtítulo, edición, fecha, ISBN y colección confirmados en la página del editor. Sin copia en archive.org (verificado, no asumido).
- **Fowler**: posición precisada con citas textuales de las tres piezas reales, incluido el matiz que el draft pedía (usa UML para bocetar; objeta el salto a fuente de verdad).
- **Hallazgo no buscado**: Dave Thomas en *IEEE Software* 2004 dice la tesis del post —«especificación ejecutable es un oxímoron»— desde adentro del establishment, en la columna que editaba Fowler. Es la mejor fuente de la pasada y está incorporada al outline (punto 7).
- **Historia del lenguaje de acción** documentada: RFP del propio Mellor en 1998, Action Semantics en UML 1.5 (2002), ningún lenguaje estándar en toda la serie 1.x, Alf recién en 2010. Refuerza el argumento del post más de lo que el draft suponía.
- **Bonus para la prosa**: Stephen Mellor figura como contribuyente de la MDA Guide. El autor de Executable UML estaba adentro del comité de MDA.

*Corrección de hecho (el draft estaba mal):* la pieza de Fowler **«MDA-aware tools» no existe**. No es un problema de título aproximado: la frase «MDA-aware» no aparece en ninguna de sus tres piezas sobre el tema. Se reescribió la sección sobre las piezas verificadas y quedó nota visible en el cuerpo y en la Bibliografía.

*Lo que sigue abierto (3 marcadores, todos con el rastro de búsqueda anotado):*

1. **El nombre del lenguaje de acción dentro del libro de 2002** — el editor sólo dice «an action language that conforms to the UML»; el TOC lista «Class Actions» sin nombrarlo; ooatool.com no fetchea ni tiene snapshot. Requiere el libro en mano.
2. **Si «Executable UML» es marca registrada** — sin resultado concluyente. Sólo se confirmó que BridgePoint® sí lo es. TESS/TSDR de la USPTO no es fetcheable; la vía práctica es la página de copyright del libro.
3. **Una herramienta concreta de diff/merge de modelos de la época** — la página de IBM sobre el Rational Rose RealTime Model Integrator devuelve 403 y no se pudo verificar. Se agregó en su lugar el paper de Ohst et al. (ESEC/FSE 2003), que sostiene el punto por otra vía y de hecho lo mejora.

Los 6 huecos 🕳️ siguen intactos: ninguna búsqueda web contesta por la biografía de César, y sin eso el post es un ensayo genérico.

Pendiente además: resolver `**Imágenes:** _a definir_`. Sugerencia — un diagrama de estados de UML de la época en Wikimedia Commons con licencia clara, o una captura de una herramienta CASE de los 2000; requiere búsqueda de licencia antes de usar. (No se trabajó en esta pasada.)

---

## Borrador de prosa

Cada cinco años, más o menos, aparece alguien —una empresa, un consorcio, un consultor con slides muy prolijas— que anuncia que el código de texto ya fue. Que escribir líneas es artesanía medieval. Que de ahora en adelante vamos a *dibujar* los sistemas y una herramienta los va a construir por nosotros. Pasó con MDA. Pasó con Executable UML. Pasó con las herramientas CASE antes que eso. Está pasando ahora mismo con low-code y no-code. Y en algún sentido va a volver a pasar el año que viene, con otro nombre.

Nunca funciona. No del todo, no como se prometió. Y lo que me interesa de este post no es hacer chiste fácil con las promesas incumplidas —eso es barato y ya lo hizo todo el mundo— sino entender *por qué* falla siempre, y por qué el fracaso tiene la misma forma cada vez. Porque si el patrón se repite, entonces no es mala suerte ni mala ejecución: hay un error de diagnóstico abajo. La apuesta de todas estas olas descansa en una hipótesis sobre qué es lo difícil de programar. Y la hipótesis es falsa.

### Qué prometía MDA, exactamente

Vale la pena empezar por ser justo con MDA, porque la caricatura que quedó —«programar con dibujitos»— no le hace honor a la idea. La *MDA Guide* de la Object Management Group[^mdaguide] no proponía dibujar en vez de escribir. Proponía algo más sutil y, en el papel, bastante razonable: **separar la especificación de un sistema de la plataforma sobre la que se implementa**.

El vocabulario era el siguiente. Escribías un PIM —*Platform Independent Model*, el modelo que describe qué hace el sistema sin comprometerse con Java, con CORBA, con una base relacional ni con nada. Después una transformación automática derivaba de ahí un PSM —*Platform Specific Model*, el mismo sistema ya comprometido con una plataforma concreta. Y de ahí, otra transformación bajaba a código.

En realidad los niveles eran tres, no dos. Arriba del PIM la guía define el **CIM** —*Computation Independent Model*—, que es el modelo de los requerimientos y del entorno, sin nada de estructura interna: «un CIM no muestra detalles de la estructura de los sistemas […] a veces se lo llama modelo de dominio», y su usuario previsto es el experto del negocio, del que la guía asume explícitamente que «no tiene conocimiento de los modelos o artefactos usados para realizar la funcionalidad»[^mdaguide]. Vale la pena registrarlo porque el CIM es la parte de MDA que más se parece a la promesa de low-code: el experto de dominio describe el problema en su propio vocabulario, y de ahí para abajo se encadena todo.

La promesa de negocio era explícita y muy de la época, y no hace falta inferirla: el white paper fundacional de la OMG, firmado por Richard Soley y el Staff Strategy Group en noviembre de 2000, plantea MDA directamente como respuesta a la proliferación de middleware —CORBA, EJB, MTS— y a la dependencia de proveedor que eso generaba[^soley]. Si la plataforma cambia —y las plataformas cambiaban todo el tiempo, era el momento de máxima efervescencia del middleware— tu inversión no se evapora, porque tu inversión está en el PIM. Cambiás la transformación, regenerás, y seguís. El modelo es el activo; el código es un derivado, como el `.o` que sale del compilador. Nadie versiona sus `.o`.

Es una idea elegante. Es, de hecho, *la misma* idea que hizo exitosos a los compiladores: escribís una vez en un lenguaje de alto nivel, y el backend baja a x86 o a ARM según haga falta. MDA quería ser el próximo escalón de esa escalera. La pregunta que hay que hacerse —y a la que voy a volver— es por qué esa escalera funcionó tan bien hasta cierto peldaño y después se cayó.

### Y qué prometía Executable UML

Executable UML, tal como lo plantearon Stephen Mellor y Marc Balcer[^mellor], fue la versión más honesta y más radical de la apuesta. Radical porque no se conformaba con generar un esqueleto. La tesis era: **el modelo no documenta el sistema; el modelo *es* el sistema**.

Esa distinción es todo. Un diagrama de clases de UML común es un dibujo *sobre* el software: alguien lo hace, alguien lo mira, y después alguien escribe el software, y a los tres meses el dibujo miente porque el software cambió y el dibujo no. Executable UML rompía eso por la vía más directa posible: si el modelo es lo único que existe y el código sale de ahí, el modelo no puede mentir. No hay dos artefactos que se desincronicen porque hay uno solo.

Para que eso sea posible el modelo tiene que ser completo. No alcanza con las cajas y las flechas: hay que decir *qué pasa*. Y ahí es donde aparece la pieza que, para mí, es la que revela todo el truco. Vuelvo a ella en dos secciones.

> 🕳️ **HUECO — necesita a César:** ¿usaste alguna herramienta CASE o de modelado UML con generación de código en algún trabajo? ¿Cuál (Rational Rose, Together, ArgoUML, Enterprise Architect, otra) y aproximadamente en qué años?

> 🕳️ **HUECO — necesita a César:** ¿hubo UML o modelado formal en la STG o en el Ministerio de Cultura de Santa Fe? Si hubo, ¿fue por decisión técnica, por exigencia de un pliego o de una consultora externa?

### La hipótesis que todas estas olas comparten

Acá está el corazón del asunto. Debajo de MDA, de Executable UML, de CASE, de low-code, hay una hipótesis compartida que casi nunca se enuncia en voz alta:

> El cuello de botella de la programación es la sintaxis.

Es decir: programar es difícil, lento y caro *porque* hay que escribir texto en una notación críptica, con punto y coma, con llaves, con reglas arbitrarias que hay que aprender. Si sacáramos esa capa —si dejáramos que la gente exprese lo que quiere en una forma más natural, más visual, más cercana a cómo piensa— la productividad se multiplicaría.

Y mirá que la hipótesis tiene buena prensa por un motivo legítimo: **fue verdad una vez**. Fue verdad cuando pasamos de assembler a Fortran. Fue verdad cuando pasamos de manejar memoria a mano a que lo haga un runtime. Cada uno de esos saltos sacó del medio una capa de notación accidental y liberó una cantidad enorme de energía humana. La escalera existió. Por eso todo el mundo asume que tiene más peldaños arriba.

El problema es que esos saltos no eliminaron la sintaxis. Eliminaron la sintaxis *accidental* —la parte de la notación que hablaba de la máquina y no del problema. Lo que quedó abajo, después de sacar todo lo accidental, no es sintaxis. Es otra cosa.

### Lo que queda cuando sacás toda la sintaxis

Lo que queda es la **especificación de comportamiento**. Y es acá donde el argumento se cierra.

Pensá en un requerimiento cualquiera, de los aburridos, de los que se escriben en una minuta: «un cliente activo puede reservar un turno». Cuatro sustantivos y un verbo. Ahora empezá a programarlo, y mirá lo que aparece:

- ¿Qué es exactamente «activo»? ¿Pagó la última cuota? ¿Y si la pagó ayer a las 23:59 y el batch corre a las 23:00?
- ¿Qué pasa si dos clientes reservan el último turno en el mismo milisegundo?
- ¿Qué pasa si el cliente se vuelve inactivo *entre* que abrió la pantalla y que apretó «confirmar»?
- ¿Qué pasa si el servicio de pagos no responde? ¿Reservamos igual? ¿Reservamos provisorio? ¿Con qué vencimiento?
- ¿Qué pasa si el mismo cliente ya tiene un turno? ¿Es un error, un reemplazo, o un segundo turno?

Ninguna de esas preguntas es una pregunta de sintaxis. Ninguna se contesta más rápido porque la escribas en una caja con una flecha en vez de en una línea con un punto y coma. Son preguntas sobre el *dominio*, sobre la concurrencia, sobre la falla, sobre el tiempo. Son preguntas difíciles porque el mundo es difícil, no porque el teclado sea difícil.

Y las respuestas, se escriban donde se escriban, tienen que ser exactas. Tienen que decir qué pasa en cada caso, sin ambigüedad, porque una máquina las va a ejecutar. Un artefacto que expresa condiciones, secuencias, alternativas, iteraciones y manejo de excepciones con precisión total, para que una máquina lo ejecute, tiene un nombre. Se llama programa. No importa de qué color lo pintes.

### El momento en que el diagrama se rinde

Esto no es teoría. Hay un lugar preciso donde se puede ver a la notación visual rendirse, y está adentro de Executable UML mismo: el **lenguaje de acción**.

Los diagramas de estados de Executable UML te dejan decir que el objeto pasa de *Pendiente* a *Confirmado* cuando llega tal evento. Perfecto, eso es un dibujo, y es un buen dibujo: se lee de un vistazo. Pero *adentro* de la transición hay que decir qué se hace. Calcular el vencimiento. Recorrer la colección de turnos superpuestos. Decidir. Y eso no se dibuja. Para eso, Executable UML tiene un lenguaje de acción: texto, con sintaxis, con expresiones, con condicionales.

Y no es un detalle de implementación de una herramienta: es una historia larga y bien documentada. Fue **el propio Mellor** quien en 1998 fue a la OMG a pedir que se emitiera un RFP por un lenguaje de acción estándar para UML; el resultado fue el metamodelo de acciones expandido de **UML 1.5, adoptado en 2002** —el mismo año del libro—, pero, y esto es lo revelador, *nunca se adoptó un lenguaje de acción estándar para toda la serie UML 1.x*. Cada herramienta trajo el suyo: OAL (*Object Action Language*, de BridgePoint) y ASL (*Action Specification Language*, de iUML de Kennedy Carter) fueron los dos más usados. Recién en 2010 la OMG estandarizó **Alf**, *Action Language for fUML*, que ya es —en palabras del recuento de esa historia— «un lenguaje hecho y derecho»[^actionlang]. [VERIFICAR: cómo llama Mellor & Balcer al lenguaje de acción *dentro* del libro de 2002 y si le ponen nombre propio. La página del editor (InformIT) sólo dice que el libro incluye «an action language that conforms to the UML» y su TOC lista el capítulo 7 «Class Actions» sin nombrarlo; ooatool.com (sitio de Leon Starr, con una página específica sobre action languages) falla el handshake TLS y no tiene snapshot en Wayback. Hace falta el libro en mano — mirar el capítulo 7 y los apéndices.]

O sea: la propuesta que venía a liberarnos del código termina, en el punto exacto donde el sistema dice qué hace, inventando un lenguaje de programación. Uno nuevo. Uno con menos usuarios, menos libros, menos gente en el mundo que lo sepa, menos herramientas, y ninguna comunidad de Stack Overflow. Y —peor— durante doce años, uno *distinto por cada herramienta*, que es exactamente la fragmentación que MDA decía venir a curar.

El dibujo se quedó con lo fácil —la estructura, los estados, las asociaciones, las cosas que igual entran en una pizarra— y le pasó lo difícil al texto. Que es justamente lo que ya hacía el código, sin la ceremonia.

Esto conecta directo con la distinción de Hickey entre *simple* y *easy* que discutí en [[C-02]]: el diagrama es *easy*, está ahí nomás, se entiende de una ojeada. Pero no hace al sistema más *simple*, porque no desenreda ninguna de las madejas reales. Sólo las mueve de lugar.

### Lo que decían los que miraban de afuera

No hizo falta esperar veinte años para que alguien lo notara. De hecho no hizo falta esperar a MDA: Bertrand Meyer publicó «UML: The Positive Spin»[^meyer] en 1997, en el número especial sobre UML de *American Programmer*, la revista de Ed Yourdon — cuatro años antes de que MDA existiera como iniciativa. Su blanco es UML, no MDA. Pero el tiro le pega igual a MDA, porque MDA se apoyó entera sobre UML.

Y el tono es mucho más filoso de lo que sugiere el título. No es un artículo que le busca educadamente el lado bueno a algo: es una **parodia**. Meyer lo escribe como la carta de un estudiante ficticio, Candide Smith, que reprobó y suplica que le suban la nota ofreciéndose a decir algo bueno de UML — y el chiste es que, por más que se esfuerza, no encuentra qué. El dispositivo le permite a Meyer encadenar objeciones bajo forma de elogio.

Las objeciones centrales, en orden de peso: que UML **no es orientado a objetos** sino «una extensión del modelado entidad-relación», con asociaciones binarias y ternarias que violan la encapsulación; que los **casos de uso son diseño funcional top-down** de los años setenta, contrabandeado adentro de un método que dice ser OO; que la notación es bizantina (sesenta páginas de resumen, un zoológico de `$`, `#`, `-`, `*`, líneas sólidas y punteadas); y —la que más importa para este post— que **no hay *seamlessness***: UML no tiende ningún puente entre el diseño y la implementación, así que llegado el momento hay que empezar de nuevo en un lenguaje de programación. Es, seis años antes, la misma observación que hace este post.

¿Y cuál es el «positive spin» que concede? Uno solo, y es veneno puro: que UML sí sirve, magníficamente, para generar un mercado. «¡Libros! ¡Cursos! ¡Conferencias! ¡Workshops! ¡Estándares! ¡Comités!» Lo único que Meyer le reconoce a UML es que es un excelente negocio para quienes lo venden.

Martin Fowler, por su parte, llegó a la misma conclusión desde otro lado, y en la época exacta de MDA. En su bliki «Model Driven Architecture» (2004) se ubica sin vueltas: hay quien piensa que MDA será el salto más grande desde el pasaje a los lenguajes de alto nivel, y hay quien piensa que no es más que «*Night of the Living Case Tools*» — «yo estoy en el segundo campo», escribe[^fowler]. Su diagnóstico es que UML no provee el salto de abstracción que MDA necesita, y lo dice en los términos de este post: «no veo que dibujar diagramas de secuencia o de actividad sea tan bueno, mucho menos mejor, que escribir código en un lenguaje moderno». En «Platform Independent Malapropism» (2003) desarma además la promesa de negocio: MDA redefine «plataforma» para que signifique «tu entorno de programación», con lo cual «lo único que estás haciendo es cambiar un entorno independiente de la plataforma por otro. No estás ganando ninguna independencia»[^malapropism].

> **Nota de sourcing (2026-07-15):** el draft citaba una pieza de Fowler titulada «MDA-aware tools». **Esa pieza no existe.** Se buscó en martinfowler.com y se fetchearon las tres piezas reales de Fowler sobre el tema —«Model Driven Architecture» (2004-02-02), «Platform Independent Malapropism» (2003-09-12) y «Language Workbenches and Model Driven Architecture» (2005-06-12)— y la frase «MDA-aware» no aparece en ninguna. La sección se reescribió sobre las piezas verificadas. Si a César le suena el título, puede ser un recuerdo cruzado con la discusión sobre *tool interoperability* del artículo de Dave Thomas, o con «MDA compliant» del marketing de la época.

Y conviene registrar el matiz que el draft pedía: la crítica de Fowler a MDA **no** es una crítica a UML en general. Fowler dice explícitamente que usa «UML heavily» para bocetar ideas de diseño; lo que rechaza es el salto de ahí a fuente de verdad ejecutable — «el grado de formalidad y cohesión que se requiere para convertir a UML en la solución completa que MDA necesita es mucho más difícil». Es exactamente la distinción con la que cierra este post.

Y no era una opinión aislada de dos francotiradores. En 2004, en la propia columna de diseño de *IEEE Software* —que en ese momento editaba Fowler—, Dave Thomas publicó «MDA: Revenge of the Modelers or UML Utopia?»[^thomas], y ahí está, en una línea, la tesis entera de este post: «el término *especificación ejecutable* es un oxímoron — si la especificación fuera verdaderamente ejecutable, sería *la cosa misma*. Si no, meramente modela *la cosa*, que es por definición parcial e incompleta». Thomas también anticipa el argumento del lenguaje de acción: para comportamientos restringidos, como una máquina de estados, hacer PIMs y PSMs es relativamente fácil — «pero un modelo de máquina de estados por sí solo puede describir muy pocas aplicaciones completas. Y además, apenas necesitamos MDA para generar código a partir de una máquina de estados».

> 🕳️ **HUECO — necesita a César:** ¿cuál fue *tu* momento de dejar de creer? ¿Hubo un proyecto, una demo, o una reunión concreta donde viste que la generación de código no iba a escalar? Una escena alcanza.

### El costo que nadie cotizó

Hay una parte de la factura que las presentaciones de MDA nunca mostraron, y que hoy, con veinte años de retrospectiva, me parece la más decisiva de todas: **el texto plano no es una limitación del código. Es infraestructura.**

Cuando tu programa es texto en archivos, gratis y sin pedirlo, te viene todo esto:

- `diff`, que te dice exactamente qué cambió entre dos versiones.
- `merge`, que junta el trabajo de dos personas que tocaron cosas distintas.
- `blame`, que te dice quién escribió esta línea y por qué —el commit tiene un mensaje.
- `grep`, que encuentra las 14 ocurrencias de un nombre en 300.000 líneas en un segundo.
- El *pull request*: la posibilidad de que otra persona lea el cambio, lo comente línea por línea, y lo apruebe.

Ahora poné el sistema adentro del repositorio propietario de una herramienta de modelado. ¿Qué es un diff entre dos versiones de un diagrama? ¿Cómo mergeás dos ramas donde dos personas movieron cajas? ¿Cómo revisás un cambio en un *pull request* si el cambio es binario?

Acá hay que ser honesto y no exagerar: **no es que no existiera nada**. Comparar y mergear a nivel de modelo era un problema conocido y activamente trabajado. En 2003 —el año mismo de la MDA Guide— Ohst, Welle y Kelter presentaban «Differences between versions of UML diagrams» en ESEC/FSE, una de las conferencias más serias del rubro[^ohst]. Que un problema esté en ESEC/FSE en 2003 dice dos cosas a la vez, y las dos importan: que había gente competente ocupándose, y que **todavía era un problema de investigación**. El `diff` de texto, para entonces, tenía casi treinta años y venía gratis con el sistema operativo.

Esa es la asimetría real, y es más interesante que «no se podía». Sí se podía, con una herramienta específica, propietaria, comprada aparte, que sólo entendía los modelos de su propio formato. Contra un ecosistema donde diff, merge, blame y grep funcionan sobre *cualquier* archivo de texto, los escribió cualquiera, y se combinan entre sí. [VERIFICAR: sería bueno un dato concreto de herramienta de la época — IBM documenta un «Rational Rose RealTime Model Integrator» que compara y mergea elementos de modelo, pero la página de soporte de IBM devuelve HTTP 403 al fetch automatizado y no pude verificarla; buscar snapshot en Wayback o documentación de Rational de la época antes de nombrar la herramienta en el post.]

Todo el andamiaje social de cómo trabajamos en equipo —revisión, historia, atribución, bisección de bugs— está construido sobre la premisa de que el artefacto es texto. MDA proponía tirar esa premisa y no traía repuesto. Y el andamiaje resultó valer muchísimo más que la comodidad de ver las asociaciones dibujadas.

Es exactamente el tipo de costo que discutí en [[C-03]] a propósito de Tidy First: el trabajo real del software no es escribirlo, es *cambiarlo muchas veces con otras personas mirando*. Cualquier propuesta que optimice el acto de escribir a costa del acto de cambiar está optimizando el 10% del problema.

### La misma apuesta, traje nuevo

Y acá viene lo que me hizo querer escribir esto ahora y no en 2005. Leé de nuevo la promesa de low-code: *tu gente de negocio va a construir las aplicaciones, sin programadores, arrastrando componentes*. Ahora tapá el nombre y compará con la promesa de CASE de los ochenta, o con la de MDA. Es la misma frase. Es la misma hipótesis: que lo difícil es la sintaxis.

Y por eso el fracaso tiene la misma forma. Low-code funciona hermoso en la demo y en el primer 80% del formulario. Después alguien pide una regla que la herramienta no previó, y aparece un cuadrito donde escribís una expresión. Después la expresión se hace larga, y aparece un panel donde escribís una función. Después necesitás versionar eso, y descubrís que el proyecto entero vive en un blob. El lenguaje de acción, otra vez, puntualmente, cada vez.

No estoy diciendo que low-code sea inútil, ojo. Digo que no está haciendo lo que dice el folleto. Está haciendo otra cosa —que puede ser muy valiosa— y el folleto no la nombra.

> 🕳️ **HUECO — necesita a César:** ¿te tocó de cerca alguna ola de low-code/no-code, o algún generador de aplicaciones tipo «arrastrá y soltá», en el sector público o en clientes? ¿Cómo terminó?

### Qué sí sobrevivió

Sería tramposo cerrar sin reconocer lo que quedó, porque quedó bastante, y es lo mejor de todo el asunto.

UML sobrevivió. No como fuente de verdad ejecutable: como **vocabulario de conversación**. Un diagrama de secuencia en una pizarra, hecho a mano, medio mal, para explicarle a alguien por qué el timeout está mal puesto, es una de las herramientas más eficientes que tengo. Un diagrama de estados dibujado entre tres personas para descubrir que hay una transición que nadie pensó vale una tarde de reuniones.

La diferencia es qué le pedís al dibujo. Si le pedís que sea *el sistema*, tiene que ser completo, exacto y actualizado, y ahí muere: un artefacto que tiene que ser completo, exacto y actualizado es un programa, y ya tenemos una tecnología excelente para eso. Si le pedís que sea *una conversación*, puede ser incompleto, aproximado y descartable —y ahí es imbatible, porque esas tres propiedades son exactamente lo que hace que sea barato dibujarlo.

MDA falló al querer ascender el diagrama de conversación a fuente de verdad. Fue una promoción que el diagrama no pidió y para la que no servía.

> 🕳️ **HUECO — necesita a César:** ¿usás UML hoy? ¿Qué diagrama concreto seguís dibujando (secuencia, estados, entidad-relación) y en qué situación típica?

> 🕳️ **HUECO — necesita a César:** ¿enseñaste UML o modelado alguna vez? Si sí, ¿en qué contexto, y cambió con los años lo que les decías a los estudiantes sobre para qué sirve?

### La pregunta para la próxima ola

Va a haber una próxima ola. Ya la estás viendo, con otro nombre y otro entusiasmo, y algo de razón va a tener, porque siempre tienen algo de razón.

La pregunta que le haría, la única que hace falta, es esta: **¿dónde vive el comportamiento?**

Mostrame dónde se dice qué pasa cuando dos cosas ocurren a la vez. Mostrame dónde se dice qué pasa cuando el servicio de pagos no responde. Mostrame dónde se dice qué significa «activo». Si la respuesta está en un cuadro de texto, en un lenguaje de expresiones, en una fórmula, en un script adjunto o en un prompt —entonces no eliminaron el código. Lo escondieron. Y todo lo que sé sobre este oficio dice que el código escondido es peor que el código a la vista: no lo podés versionar, no lo podés revisar, no lo podés buscar, y no lo podés entender seis meses después.

La sintaxis nunca fue el problema. Pensar bien es el problema. Y de eso, hasta ahora, no nos salvó ningún dibujo.

[^mdaguide]: [*MDA Guide Version 1.0.1*](https://www.omg.org/news/meetings/workshops/UML_2003_Manual/00-2_MDA_Guide_v1.0.1.pdf) — Object Management Group, documento omg/2003-06-01, 12 de junio de 2003. Editores: Joaquin Miller y Jishnu Mukerji. Las definiciones de CIM, PIM y PSM están en §2.2.10–2.2.11 y §3.1–3.2. Dato jugoso para el post: entre los contribuyentes figura **Stephen Mellor** (Project Technology) — el autor del libro de Executable UML estaba adentro del comité que escribió MDA. Copia de respaldo: [Wayback, 2026-02-27](http://web.archive.org/web/20260227105813/http://www.omg.org/news/meetings/workshops/UML_2003_Manual/00-2_MDA_Guide_v1.0.1.pdf).
[^soley]: [*Model Driven Architecture* (MDA White Paper)](https://www.omg.org/mda/mda_files/model_driven_architecture.htm) — Richard Soley y OMG Staff Strategy Group, Draft 3.2, 27 de noviembre de 2000. El documento fundacional, anterior a la MDA Guide; plantea MDA como respuesta a la proliferación de middleware (CORBA, EJB, MTS) y al lock-in de proveedor.
[^mellor]: Stephen J. Mellor & Marc J. Balcer, *Executable UML: A Foundation for Model-Driven Architecture*, Addison-Wesley Professional, 1.ª edición, 2002 (publicado el 14 de mayo de 2002), 416 pp., Addison-Wesley Object Technology Series. ISBN-10 0-201-74804-5 / ISBN-13 978-0-201-74804-8. [Página del editor en InformIT](https://www.informit.com/store/executable-uml-a-foundation-for-model-driven-architecture-9780201748048) ([Wayback, 2025-11-18](http://web.archive.org/web/20251118130153/https://www.informit.com/store/executable-uml-a-foundation-for-model-driven-architecture-9780201748048)). **No hay copia en archive.org** — se buscó `title:(executable uml)` en el advanced search y aparecen otros tres libros del rubro (Starr 2002, Milicev 2009), pero no este. [VERIFICAR: si «Executable UML» es marca registrada o término genérico. Busqué sin resultado concluyente: la búsqueda web sólo confirma que **BridgePoint®** (Project Technology → Mentor Graphics) sí lleva marca registrada, no «Executable UML» en sí. TESS/TSDR de la USPTO requiere sesión interactiva y no es fetcheable. Vía alternativa: mirar la página de copyright del propio libro, que suele traer la declaración de marcas.]
[^actionlang]: [«History of Executable UML — Action Language: An OMG Journey»](https://modeling-languages.com/uml-action-language-omg-journey/) — modeling-languages.com. Fuente del RFP de Mellor de 1998, del metamodelo de acciones de UML 1.5 (adoptado en 2002), de la ausencia de lenguaje de acción estándar en toda la serie UML 1.x, y de la adopción de Alf en 2010. Frágil (blog) — respaldo: [Wayback, 2025-12-16](http://web.archive.org/web/20251216112628/https://modeling-languages.com/uml-action-language-omg-journey/).
[^meyer]: [«UML: The Positive Spin»](https://archive.eiffel.com/doc/manuals/technology/bmarticles/uml/page.html) — Bertrand Meyer, publicado en 1997 en el número especial sobre UML de *American Programmer*, editada por Ed Yourdon. Texto alojado en el archivo de Eiffel Software, la casa del propio Meyer (preferido a Wikipedia por regla de la casa). Frágil (`archive.eiffel.com` es un dominio archivado y podría caerse) y **load-bearing** — respaldo obligatorio: [Wayback, 2026-04-30](http://web.archive.org/web/20260430094429/https://archive.eiffel.com/doc/manuals/technology/bmarticles/uml/page.html). Ojo con el tono: es una parodia (carta de un estudiante ficticio, Candide Smith), con disclaimer del propio Meyer aclarándolo.
[^fowler]: [«Model Driven Architecture»](https://martinfowler.com/bliki/ModelDrivenArchitecture.html) — Martin Fowler, bliki, 2 de febrero de 2004. De ahí salen «Night of the Living Case Tools», «I'm in the latter camp» y la cita sobre diagramas de secuencia vs. código. Frágil (sitio personal) — respaldo: [Wayback, 2026-05-25](http://web.archive.org/web/20260525214117/https://martinfowler.com/bliki/ModelDrivenArchitecture.html).
[^malapropism]: [«Platform Independent Malapropism»](https://martinfowler.com/bliki/PlatformIndependentMalapropism.html) — Martin Fowler, bliki, 12 de septiembre de 2003. El argumento de que MDA redefine «plataforma» y por eso «el argumento de la independencia de plataforma no tiene fundamento». Frágil (sitio personal).
[^thomas]: Dave Thomas, «MDA: Revenge of the Modelers or UML Utopia?», *IEEE Software*, vol. 21, n.º 3, mayo/junio de 2004 — DOI [10.1109/MS.2004.1293067](https://doi.org/10.1109/MS.2004.1293067) (verificado vía Crossref; IEEE Xplore bloquea el fetch). Columna «Design», editada en ese momento por Martin Fowler. Mirror libre en PDF, alojado por el propio Fowler: [martinfowler.com/ieeeSoftware/mda-thomas.pdf](https://martinfowler.com/ieeeSoftware/mda-thomas.pdf). Nota de paginación: Crossref registra pp. 15–17, pero el PDF muestra las páginas 22–24 — verificar antes de citar página exacta; para el post alcanza con vol./n.º/año.
[^ohst]: Dirk Ohst, Michael Welle & Udo Kelter, «Differences between versions of UML diagrams», *Proceedings of ESEC/FSE 2003* (9th European Software Engineering Conference / 11th ACM SIGSOFT Symposium on the Foundations of Software Engineering), Helsinki, ACM, septiembre de 2003, pp. 227–236 — DOI [10.1145/940071.940102](https://doi.org/10.1145/940071.940102) (verificado vía Crossref; ACM DL bloquea el fetch). Evidencia de que el diff de modelos era problema de investigación abierto en el año mismo de la MDA Guide.
