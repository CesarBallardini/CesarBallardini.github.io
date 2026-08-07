### C-14 — XP: valores, principios, prácticas — el framework tripartito de Kent Beck

- **Archivo seed:** _draft-rest.md bucket 6 (cosechado 2026-04-09)_
- **Slug propuesto:** `xp-values-principles-practices`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-xp-values-principles-practices/index.md`
- **Serie:** filosofia
- **Cross-links:** [[C-03]] (Tidy First), [[C-04]] (TDD), [[C-12]] (Forest/Desert)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** Kent Beck dividió Extreme Programming deliberadamente en tres niveles: valores (lo que importa), principios (cómo razonar), prácticas (qué hacer concretamente). Esto es muy distinto de cómo se enseña XP popularmente (lista de prácticas). En el podcast con Abi Noda, Beck explica por qué esa división era central: las prácticas se distorsionan ("hago TDD porque me dijeron"), los valores son demasiado vagos, y los principios son el puente. El post discute el framework completo y por qué es relevante en 2026.

**Hook:** Extreme Programming no es "una lista de prácticas que tenés que hacer". Es tres capas: valores, principios, prácticas. Si solo conocés las prácticas, no entendés XP. Acá está el framework completo, contado por Beck.

**Outline:**
1. Cómo se aprende XP en la calle: una lista de prácticas (pair programming, TDD, integración continua, cliente en el equipo…). Nadie te cuenta que hay dos capas más arriba.
2. La estructura de tres niveles tal como la plantea Beck en la 2.ª edición de *Extreme Programming Explained*: valores, principios, prácticas.
3. Los valores: qué son, y por qué solos no alcanzan — son verdaderos pero no te dicen qué hacer el lunes a la mañana.
4. Las prácticas: qué son, y por qué solas se pudren — quedan como ritual sin la razón que las sostiene («hago TDD porque me dijeron»).
5. Los principios: el puente. Cómo se usa el puente en concreto — el principio es lo que te deja adaptar o descartar una práctica sin traicionar el valor.
6. Por qué la división es la parte que no sobrevivió a la popularización de XP, y qué se perdió cuando XP se volvió una checklist de certificación.
7. Beck × Abi Noda, enero 2026: por qué sigue insistiendo con esto veinte y pico de años después.
8. Relevancia en 2026: el mismo error se repite con cada framework ágil vendido como lista de ceremonias. Conexión con [[C-03]] (Tidy First es el mismo movimiento aplicado a otra escala), [[C-04]] (TDD como práctica que sólo tiene sentido con su principio detrás) y [[C-12]] (Forest/Desert).
9. Cierre: el test práctico — para cada práctica que hacés, ¿podés nombrar el principio y el valor? Si no, estás haciendo cargo cult.

**Bibliografía:**
- [Kent Beck, *Extreme Programming Explained: Embrace Change*, 1.ª ed., Addison-Wesley, 1999](https://archive.org/details/extremeprogrammi00beck) — ISBN 0-201-61641-6 / 978-0-201-61641-5. La edición que fijó los **4 valores** (comunicación, simplicidad, retroalimentación, coraje) y las 12 prácticas clásicas. Copia en préstamo controlado en archive.org. — estable.
- [Kent Beck (con Cynthia Andres), *Extreme Programming Explained: Embrace Change*, 2.ª ed., Addison-Wesley, 2004](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/) — ISBN 0-321-27865-8 / 978-0-321-27865-4 (copyright 2005). Reescritura completa: agrega el 5.º valor (**respeto**), 14 principios y la división prácticas **primarias** (13) / **corolarias** (11). Índice completo verificable en la [muestra oficial de Pearson (PDF)](https://ptgmedia.pearsoncmg.com/images/9780321278654/samplepages/9780321278654.pdf). — estable.
- [Kent Beck y Abi Noda, «Developer Productivity Metrics: Education Necessary», newsletter *Software Design: Tidy First?*, 29 de enero de 2025](https://newsletter.kentbeck.com/p/developer-productivity-metrics-education) — transcripción escrita de una conversación **patrocinada por DX** (no un podcast, no enero de 2026). Contiene la cita clave: «Extreme Programming is deliberately divided into values, principles and practices…». — estable. (En la newsletter de Beck; cf. [[tr-08]].)
- [c2 wiki — *ExtremeProgramming*](https://wiki.c2.com/?ExtremeProgramming) ([[tr-16]]) — el wiki original de Ward Cunningham donde nació XP; fuente histórica de la comunidad. **El marco valores/principios/prácticas como tal es del libro (2.ª ed., cap. 3), no del wiki.** — frágil (se renderiza por JavaScript): conseguir respaldo Wayback antes de publicar.

**Imágenes:** _a definir_

**Tags propuestos:** `['Kent Beck','XP','extreme programming','valores','principios','practicas']`

**Estado actual:** prosa-borrador escrita (2026-07-15, generado por Claude; sin revisar por César). Está escrito el armazón completo: el encuadre de XP-como-lista-de-prácticas, la presentación de las tres capas, por qué los valores solos no alcanzan y las prácticas solas se pudren, los principios como puente con un ejemplo trabajado, la parte de qué se perdió en la popularización, el gancho con la entrevista de Beck con Abi Noda, la relevancia en 2026 y el cierre con el test práctico. Quedan **8 huecos** que necesitan a César (su propia historia con XP, si lo enseñó, qué prácticas vio imponerse sin principio en el sector público, y su lectura de la entrevista de 2026) y **9 marcas `[VERIFICAR:]`**. La bibliografía de este draft es mínima y **sin URLs**: los nombres concretos de los cinco valores, la lista de principios, la lista de prácticas primarias/corolarias, la diferencia entre la 1.ª y la 2.ª edición, y todo contenido específico de la entrevista con Abi Noda están escritos como afirmaciones a chequear contra la fuente, no como hechos verificados. Antes de publicar hay que tener el libro en la mano y la entrevista abierta, y conseguir las URLs reales para las footnotes.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch: índice oficial de Pearson de la 2.ª ed., texto del libro, copia archive.org de la 1.ª ed., y la transcripción de la entrevista en la newsletter de Beck) y se resolvieron **10 de 11** marcadores `[VERIFICAR:]`. Quedan confirmados: la estructura de tres capas (libro cap. 3), los **5 valores** de la 2.ª ed. con «respeto» como el 5.º agregado (la 1.ª ed. tenía 4), los **14 principios**, las **13 prácticas primarias + 11 corolarias**, y la metáfora del «puente» como terminología propia de Beck. El único marcador sin resolver es el de la trayectoria histórica de la popularización/certificación de XP (no hay fuente; queda como opinión del autor). **Corrección importante:** la entrevista Beck×Noda es del **29 de enero de 2025** (no enero de 2026) y es una **transcripción escrita patrocinada por DX**, no un podcast; el **Concepto** y el **Outline** todavía dicen «podcast»/«enero 2026» y hay que corregirlos al escribir la versión final.

---

## Borrador de prosa

Si aprendiste Extreme Programming como lo aprendí yo —de segunda mano, por lo que contaban otros— seguramente lo aprendiste como una lista. Programación de a pares. Escribir los tests primero. Integrar continuamente. Tener al cliente sentado en el equipo. Semana de cuarenta horas. Refactorizar sin pedir permiso. Doce prácticas, o trece, según a quién le preguntes. Una checklist. Y la conversación sobre XP terminaba siempre en el mismo lugar: discutiendo cuáles de las prácticas eran realistas y cuáles no, cuáles se podían adoptar sueltas y cuáles había que dejar pasar.

Esa conversación entera se da un nivel más abajo de donde está el asunto. XP no son doce prácticas: son tres capas. Valores arriba, principios en el medio, prácticas abajo. Kent Beck armó *Extreme Programming Explained* alrededor de esa división de manera deliberada.[^epe] Si sólo conocés las prácticas, tenés el piso de un edificio del que ignorás que existen dos plantas más, y el problema no es que te estés perdiendo algo lindo: es que sin las otras dos capas las prácticas no significan nada. Son gestos.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste vos a XP la primera vez —leíste el libro, te lo contaron, lo viste practicar en algún lado? ¿Y en qué año, más o menos?

> 🕳️ **HUECO — necesita a César:** ¿leíste la 1.ª edición (1999) o la 2.ª (2004)? Si leíste las dos, ¿te acordás de haber notado el cambio de estructura?

### Las tres capas

La estructura, tal como la plantea Beck, va así.[^epe]

Los **valores** son lo que importa. Son las cosas que un equipo sostiene como buenas en sí mismas, y son pocas, abstractas y casi imposibles de discutir en serio: nadie va a decirte que está en contra de la comunicación.

Las **prácticas** son lo que hacés. Son concretas, observables, verificables desde afuera. Alguien puede mirarte trabajar una tarde y decir con certeza si hacés pair programming o no.

Los **principios** están en el medio, y son la parte que casi nadie recuerda. Son las reglas de razonamiento que te dejan derivar una práctica desde un valor, o juzgar una práctica que ya tenés a la luz del valor que dice servir.

[VERIFICADO 2026-07-16: confirmado en la 2.ª ed. El libro está organizado alrededor de la división: la Sección 1 se titula «Exploring XP» y su cap. 3 se llama literalmente «Values, Principles, and Practices» (p. 13), seguido del cap. 4 «Values», el cap. 5 «Principles» y los caps. 6-7 y 9 sobre prácticas. La afirmación «Beck armó el libro alrededor de esa división» es sostenible. Fuente: índice de la muestra oficial de Pearson, ISBN 978-0-321-27865-4.]

[VERIFICADO 2026-07-16: confirmado. El cap. 4 «Values» de la 2.ª ed. enumera cinco —Communication, Simplicity, Feedback, Courage y **Respect**— más una sección «Others». La 1.ª ed. (1999) tenía sólo cuatro; «respeto» se suma en la 2.ª. La enumeración del draft (comunicación, simplicidad, retroalimentación, coraje, respeto) es correcta. Fuente: índice Pearson 2.ª ed. + copia archive.org de la 1.ª ed. (ISBN 0-201-61641-6).]

[VERIFICADO 2026-07-16: confirmado. El cap. 5 «Principles» lista **catorce**: Humanity, Economics, Mutual Benefit, Self-Similarity, Improvement, Diversity, Reflection, Flow, Opportunity, Redundancy, Failure, Quality, Baby Steps y Accepted Responsibility. Son 14 y coinciden exactamente con la lista del draft (los nombres en español son traducción propia; el libro está en inglés). Fuente: índice Pearson 2.ª ed.]

[VERIFICADO 2026-07-16: confirmado. La 2.ª ed. divide las prácticas en 13 «Primary Practices» (cap. 7: Sit Together, Whole Team, Informative Workspace, Energized Work, Pair Programming, Stories, Weekly Cycle, Quarterly Cycle, Slack, Ten-Minute Build, Continuous Integration, Test-First Programming, Incremental Design) y 11 «Corollary Practices» (cap. 9: Real Customer Involvement, Incremental Deployment, Team Continuity, Shrinking Teams, Root-Cause Analysis, Shared Code, Code and Tests, Single Code Base, Daily Deployment, Negotiated Scope Contract, Pay-Per-Use). Los rótulos primary/corollary son textuales del libro. Fuente: índice Pearson 2.ª ed.]

### Por qué los valores solos no alcanzan

Poné a un equipo en una sala y hacelos acordar en que valoran la comunicación. Van a acordar en cinco minutos. Ahora preguntales qué van a hacer distinto el lunes a la mañana. Ahí se acaba el acuerdo, porque «valoramos la comunicación» es compatible con absolutamente todo: con hacer una reunión diaria y con no hacerla, con documentar cada decisión y con no documentar ninguna, con sentarse de a dos frente a la máquina y con no sentarse nunca. El valor no discrimina. No sirve para elegir entre dos cursos de acción, que es exactamente para lo que uno querría usarlo.

Esto no es un defecto de los valores de XP en particular. Es lo que son los valores. Sirven para saber en qué dirección mirar; no sirven para caminar. Cualquiera que haya visto una jornada de «definamos los valores del área» en una organización grande sabe cómo termina: con un póster.

### Por qué las prácticas solas se pudren

El otro extremo es peor, porque parece que funciona.

Una práctica es tan concreta que se puede mandar. «A partir de ahora hacemos TDD.» Y la gente lo hace, más o menos, durante un tiempo. Escriben los tests. Los tests pasan. Alguien hace un gráfico con la cobertura. Y sin embargo no pasa nada de lo que se suponía que iba a pasar, porque lo que se copió fue la forma. El que escribe el test después del código para llegar al 80% de cobertura está haciendo, observablemente, «tests unitarios». No está haciendo TDD —está haciendo el gesto de TDD sin la razón que lo sostiene, y la razón es la parte que producía el efecto.

Es el «hago TDD porque me dijeron». Y el que lo hace no es un tonto ni un vago: es alguien a quien le entregaron el piso de abajo del edificio y le dijeron que ese era el edificio. Cuando la práctica no rinde lo prometido —y no va a rendirlo— la conclusión razonable, desde donde está parado, es que XP no funciona.

> 🕳️ **HUECO — necesita a César:** ¿viste vos, en concreto, una práctica ágil bajada por decreto en alguna organización donde trabajaste? Sin nombrar a nadie si no querés: ¿cuál fue la práctica y qué pasó?

> 🕳️ **HUECO — necesita a César:** en tu experiencia en el sector público (STG, Ministerio de Cultura de Santa Fe), ¿hubo algún intento de adoptar prácticas ágiles? ¿Cómo se planteó —desde arriba, desde el equipo, no se planteó nunca?

### Los principios son el puente

Acá es donde el framework se pone interesante, y donde entiendo por qué Beck insiste tanto con esta parte.

Un principio es la razón por la que una práctica sirve a un valor. Y como es una razón, se puede *usar*. Tomá una práctica cualquiera de XP y preguntate: ¿a qué valor sirve, y por qué mecanismo? Si podés contestar las dos cosas, tenés el principio en la mano. Y con el principio en la mano podés hacer algo que con la práctica sola no podés: adaptarla.

Porque el punto de todo esto no es la obediencia. Supongamos que tu equipo está distribuido en tres husos horarios y el pair programming presencial, tal como está en el libro, no se puede. Si sólo tenés la práctica, tenés dos opciones y las dos son malas: forzarla hasta que sea un simulacro, o descartarla y quedarte sin nada. Si tenés el principio —qué es lo que el pairing produce, y a qué valor sirve eso— tenés una tercera: buscar otra forma de producir el mismo efecto en tus condiciones, y saber si la conseguiste o no. El principio es lo que te da el criterio para juzgar el reemplazo.

Y funciona también en la otra dirección, que es la que más me interesa. Agarrá una práctica que ya tenés en tu equipo —una que nadie eligió, que está ahí desde antes que vos— y preguntale lo mismo. Muchas no van a tener respuesta. Ese silencio es información.

[VERIFICADO 2026-07-16: la metáfora del «puente» es del propio Beck, se puede poner en su boca. El libro dice textualmente «Principles bridge the gap between values and practices» y «The principles of XP provide a set of domain-specific guidelines for finding practices in harmony with XP's values». Fuente: texto de *Extreme Programming Explained*, 2.ª ed.]

### Lo que se perdió cuando XP se volvió popular

Hay una ironía en todo esto: XP se difundió justamente por su capa más copiable. Las prácticas viajan bien. Son nombrables, enseñables, certificables, tercerizables a una consultora. Los valores viajan como póster. Y los principios —la capa que hacía que las otras dos se sostuvieran— no viajaron casi nada, porque exigen que cada equipo haga el trabajo de razonar por su cuenta, y ese trabajo no se puede vender en un curso de dos días.

El resultado es el XP que la mayoría conoce: una lista. Y de ahí en más, cada framework ágil que vino después repitió el mismo movimiento con sus propias ceremonias.

[VERIFICAR: si el post va a afirmar algo sobre la trayectoria histórica de la popularización de XP, o sobre la industria de las certificaciones ágiles, hace falta una fuente. Con la bibliografía actual esto es opinión mía, y debería estar escrito como opinión mía y no como historia. Revisar la redacción del párrafo con ese criterio, o conseguir fuente. — Nota 2026-07-16: sin resolver. El propio libro tiene una sección «Certification and Accreditation» (cap. 21 «Purity», p. 146) que respalda la postura *de Beck*, pero no es una historia de la industria de certificaciones ágiles; no alcanza para escribir el párrafo como historia.]

### Beck en 2026

Lo que me hizo volver sobre esto es que Beck sigue insistiendo. En la entrevista con Abi Noda, de enero de 2025, vuelve sobre la división de tres capas y sobre por qué le parecía —le sigue pareciendo— la parte central de XP.[^noda]

[VERIFICADO 2026-07-16: la entrevista está en <https://newsletter.kentbeck.com/p/developer-productivity-metrics-education> (newsletter *Software Design: Tidy First?*, 29-01-2025). Beck sí vuelve sobre la división de tres capas; cita textual: «Extreme Programming is deliberately divided into values, principles and practices. That was a choice I made early on because I had seen focus on practice be twisted», y agrega que el nivel de los valores «is too vague» y por eso quería los principios en el medio, «because every situation is different». (Lo que le llamó la atención a César sigue en el HUECO de abajo.)]

[VERIFICADO 2026-07-16: es una **transcripción escrita** de una conversación **patrocinada por DX** (Abi Noda es CEO de DX; Beck: «Thank you to DX for sponsoring this conversation. They paid me for my time & this space»), NO un podcast. Publicada el **29 de enero de 2025**, no en enero de 2026. Corregí la fecha en este párrafo; el **Concepto** («podcast») y el **Outline** («enero 2026») siguen desactualizados y hay que corregirlos al escribir la versión final. El encabezado «Beck en 2026» conviene revisarlo también.]

> 🕳️ **HUECO — necesita a César:** ¿qué fue lo que te llamó la atención de esa entrevista? ¿Hubo una frase concreta que te hizo querer escribir el post?

> 🕳️ **HUECO — necesita a César:** ¿seguís la newsletter de Beck (Tidy First) habitualmente, o caíste en esta entrevista de casualidad?

Y tiene sentido que insista, porque es el mismo movimiento que viene haciendo en todo lo demás. [[C-03]] —Tidy First— es esto otra vez, a otra escala: no es una lista de refactorings chiquitos, es un criterio para decidir cuándo aplicarlos. [[C-04]] es esto otra vez: TDD sin su principio es cobertura de tests. Y [[C-12]] es la misma idea vista desde el paisaje.

### El test

Si querés usar este framework para algo hoy mismo, hay una manera barata.

Hacé la lista de las prácticas que tiene tu equipo. Todas: las que están escritas y las que no, el code review, la reunión de los lunes, el naming de las ramas, lo que sea. Al lado de cada una escribí dos cosas: el principio por el que la práctica funciona, y el valor al que sirve.

Vas a ver tres resultados. Algunas prácticas van a tener las dos columnas llenas —esas están bien, y además ahora sabés bajo qué condiciones dejarían de estarlo. Otras van a tener el valor pero no el principio: sabés para qué están, pero no por qué funcionarían; ahí hay que pensar. Y algunas no van a tener ninguna de las dos. Esas son las que hacés porque te dijeron.

Ninguna de esas prácticas huérfanas se muere sola. Ese es el punto: no se mueren, se acumulan. Sobreviven a la persona que las instauró, a la razón que las justificaba y a veces al proyecto entero, y para cuando llegás vos ya son «cómo se hacen las cosas acá». Nombrarlas no es poco.

> 🕳️ **HUECO — necesita a César:** ¿hiciste este ejercicio alguna vez, aunque sea informalmente? Si lo hacés ahora con un equipo que recuerdes bien, ¿cuántas prácticas huérfanas te salen?

> 🕳️ **HUECO — necesita a César:** ¿enseñaste XP alguna vez —en un curso, en una materia, adentro de un equipo? Si sí, ¿enseñaste las tres capas o enseñaste la lista? (Si enseñaste la lista, decilo: es el mejor cierre posible para este post.)

Extreme Programming no es una lista de prácticas que tenés que hacer. Es un edificio de tres pisos del que la industria copió el planta baja y tiró el resto. Y la parte que tiraron es la única que te sirve el día que tus condiciones no son las del libro —o sea, siempre.

[^epe]: Kent Beck (con Cynthia Andres), *Extreme Programming Explained: Embrace Change*, 2.ª edición, Addison-Wesley, 2004 — ISBN 0-321-27865-8 (978-0-321-27865-4). El subtítulo es «Embrace Change» y la 2.ª edición está coescrita **con Cynthia Andres** (la 1.ª, de 1999, es sólo de Beck). La estructura de tres capas es el eje del libro: cap. 3 «Values, Principles, and Practices», cap. 4 «Values», cap. 5 «Principles», caps. 6-7 y 9 sobre prácticas. Ficha del editor: <https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/>. La 1.ª edición (Addison-Wesley, 1999, ISBN 0-201-61641-6) tenía sólo 4 valores; copia en préstamo controlado en archive.org: <https://archive.org/details/extremeprogrammi00beck>.
[^noda]: Kent Beck y Abi Noda, «Developer Productivity Metrics: Education Necessary», newsletter *Software Design: Tidy First?*, **29 de enero de 2025** (no enero de 2026): transcripción escrita de una conversación **patrocinada por DX** («Thank you to DX for sponsoring this conversation. They paid me for my time & this space»). <https://newsletter.kentbeck.com/p/developer-productivity-metrics-education> — estable.
[^wiki]: La fuente canónica del marco valores/principios/prácticas es el propio libro (2.ª ed., cap. 3 «Values, Principles, and Practices»). El wiki histórico donde nació XP es el c2 wiki de Ward Cunningham: [ExtremeProgramming](https://wiki.c2.com/?ExtremeProgramming) ([[tr-16]]) — frágil (se renderiza por JavaScript); conseguir respaldo en Wayback Machine antes de publicar, o citar directamente el libro y borrar esta footnote.
