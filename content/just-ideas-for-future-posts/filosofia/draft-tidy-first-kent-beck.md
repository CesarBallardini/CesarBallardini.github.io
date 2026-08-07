### C-03 — Tidy First: limpiar antes de cambiar (Kent Beck)

- **Archivo seed:** `dev/draft-tidy-first.md`
- **Slug propuesto:** `tidy-first-kent-beck`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-tidy-first-kent-beck/index.md`
- **Serie:** C
- **Cross-links:** depende de [[tr-08]]; lleva a [[C-04]] (TDD, otro framework de Beck), [[C-02]] (Hickey, vocabulario complementario), [[E-04]] (memoir: cuándo aprendí a hacer tidy en mi propio código)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1200-1800 palabras)

**Concepto:** Kent Beck, en *Tidy First?* (2023), propone una distinción operativa entre *tidyings* (limpiezas pequeñas: renombrar, extraer, reordenar) y *behavior changes* (cambios que un usuario notaría). La tesis: separá los dos en commits/PRs distintos, y aprendé a decidir si conviene tidy *antes* de cambiar, *después*, o *nunca*. No es un manual de refactoring — es un libro sobre decisiones económicas y emocionales en el código.

**Hook:** "Kent Beck — el del XP, el del TDD — escribió en 2023 un librito de 100 páginas que se titula *Tidy First?*, con signo de pregunta. Ese signo de pregunta es importante. Beck no te está diciendo *limpiá siempre antes*. Te está diciendo: *aprendé a decidir cuándo*."

**Outline:**
1. Qué es un *tidying* y por qué Beck inventa el término en vez de decir "refactor pequeño".
2. La lista de tidyings del libro: *guard clauses*, *dead code*, *normalize symmetries*, *new interface old implementation*, *reading order*, *cohesion order*, *move declaration and initialization together*, *explaining variables*, *explaining constants*, *explicit parameters*, *chunk statements*, *extract helper*, *one pile*, *explaining comments*, *delete redundant comments*. Quince en total. Comentar 4-5.
3. La pregunta del título: *tidy first?* o *tidy after?* o *never tidy?* — el framework de decisión.
4. La parte económica: cost of money, options, discounting. Beck entra en finanzas reales para defender su posición — esto sorprende a todo el mundo y es lo más interesante del libro.
5. La parte humana: separación tidy/behavior baja la carga cognitiva del review y la fricción del PR.
6. Cierre: por qué este libro se siente como "lo que XP siempre quiso decir y nunca terminó de articular".

**Bibliografía:** _(pasada de fuentes 2026-07-15: cada URL de abajo fue fetcheada y confirmada, salvo donde se aclara lo contrario. Flag de bitrot al final de cada entrada.)_

*Fuente primaria — el libro*
- [[tr-08]] — Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly Media, 2023, 124 pp. ISBN 9781098151249 (impreso) / 9781098151218. Prólogo de Larry Constantine. — **estable**
- [Ficha del editor en O'Reilly](https://www.oreilly.com/library/view/tidy-first/9781098151232/) — referencia canónica del índice. **Devuelve HTTP 403 a fetch automatizado** (igual que las páginas de capítulo `chNN.html`); no verificada directamente. — **estable**
- [Ficha en Google Books](https://books.google.com/books/about/Tidy_First.html?id=-2ndEAAAQBAJ) — 124 pp., las tres partes, el apéndice, y *discounted cash flows* entre los temas. Fetcheada y confirmada. — **estable**
- [Obra en Open Library](https://openlibrary.org/works/OL35973549W) — 3 ediciones, 124-125 pp. Vía `openlibrary.org/works/OL35973549W/editions.json`. — **estable**

*Fuentes primarias — Beck en su propia voz (preferidas sobre reseñas de terceros)*
- [Kent Beck, newsletter *Software Design: Tidy First?*](https://newsletter.kentbeck.com/) — donde gran parte del material apareció primero. **`tidyfirst.substack.com` redirige 301 acá; actualizar el link del borrador viejo.** — **frágil**
- [Kent Beck, «How I Came To Write "Tidy First?"»](https://newsletter.kentbeck.com/p/how-i-came-to-write-tidy-first) — génesis del libro; su capítulo en el *Refactoring* de Fowler (1999); newsletter desde enero 2021, contrato con O'Reilly después. — **frágil**
- [Kent Beck, «First, After, Later, Never», 29-07-2022](https://newsletter.kentbeck.com/p/first-after-later-never) — las **cuatro** opciones. Load-bearing: es la prueba de que el material precede al libro y de que las opciones son cuatro. Desarrollo completo tras paywall. — **frágil**
- [Kent Beck, «The Product Development Triathlon» (3X), Medium](https://medium.com/@kentbeck_7670/the-product-development-triathlon-6464e2763c46) — texto completo legible. **Reemplaza el link de Facebook del borrador, que está muerto tras un muro de login.** — **frágil**
- [Kent Beck, «Tidy First? Kent Beck on Refactoring», QCon Plus, 26-05-2023 (InfoQ)](https://www.infoq.com/presentations/refactoring-cleaning-code/) — charla con transcripción; plantea la pregunta central del libro. No explica el origen de la palabra *tidying*. — **frágil**

*Obra previa de Beck y contexto*
- Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley, 2002 (impr. 2003), xix + 220 pp., ISBN 0321146530 — [copia en Internet Archive](https://archive.org/details/testdrivendevelo0000beck), préstamo digital controlado. — **estable**
- Kent Beck, *Extreme Programming Explained: Embrace Change*, 2.ª ed. con Cynthia Andres, Addison-Wesley, 2004, ISBN 0321278658 — archive.org tiene la [1.ª ed., 2000, ISBN 0201616416, 226 pp.](https://archive.org/details/extremeprogrammi00beck), préstamo controlado, **edición anterior a la citada**. — **estable**
- [Martin Fowler, *Refactoring*, 1.ª ed. 1999 / 2.ª ed. 2018 — sitio del autor](https://martinfowler.com/books/refactoring.html) — «by Martin Fowler, with Kent Beck». Sitio propio del autor, preferido sobre la ficha de O'Reilly del borrador viejo. — **estable**
- Ron Jeffries, *Adventures in C#* — `https://ronjeffries.com/xprog/acsindex/`. **Sitio caído** (`ECONNREFUSED`, dos intentos, 2026-07-15). Wayback reporta snapshot 200 (2016-01-23) vía la availability API, pero web.archive.org no es fetcheable desde este entorno → **snapshot no verificado**. Fallback impreso: *Extreme Programming Adventures in C#*, Microsoft Press, 2004, ISBN 0735619492. — **frágil**

*Reseñas de terceros (corroboración del índice, no cita primaria)*
- [Henrik Warne, «Tidy First?», 10-01-2024](https://henrikwarne.com/2024/01/10/tidy-first/) — confirma independientemente las tres partes, los 15 tidyings y el par tensionado *time value of money* / *optionality*. — **frágil**
- [«Tidy First? A Summary of Kent Beck's Book»](https://www.workingsoftware.dev/summary-of-tidy-first-book/) — índice capítulo por capítulo. — **frágil**

**Imágenes:**
- _Crear_: diagrama de un PR "mezclado" (tidy + behavior) vs dos PRs separados — mostrar la diferencia visual en review (~30 min).
- _Crear_: árbol de decisión "tidy first / after / never" según costo y certidumbre (~45 min).

**Tags propuestos:** `['Kent Beck', 'tidy first', 'refactor', 'XP', 'code review']`

**Estado actual:**

> ⚠️ **PREMISA EN DUDA — el framework tiene cuatro opciones, no tres.** El **Concepto** dice que Beck enseña a decidir si conviene tidy «*antes*, *después*, o *nunca*», y el **Outline (punto 3)** repite «*tidy first?* o *tidy after?* o *never tidy?*». El libro presenta **cuatro**: el capítulo 21 se titula «First, After, Later, Never», y *Later* (anotar el desorden y volver más tarde, en tandas chicas, cuando hay un lote grande sin rédito inmediato) es una categoría propia, distinta de *After*. Verificado contra el índice del libro y contra el post homónimo de la newsletter (29-07-2022), que enumera las cuatro. **La prosa se corrigió; el Concepto y el Outline no se tocaron porque son de César.** La tesis central del draft (Beck enseña a *decidir cuándo*, no a limpiar siempre) sale intacta y hasta reforzada — sólo hay que sumar la cuarta opción.

**Pasada de fuentes (2026-07-15).** Bibliografía reorganizada por tipo de fuente, con flag de bitrot en cada entrada; todas las URLs listadas fueron fetcheadas salvo las marcadas como no verificadas. Se resolvieron **cinco de las siete marcas `[VERIFICAR:]`**:

- ✅ **Extensión:** 124 pp. (Google Books, Open Library). El «poco más de cien páginas» del borrador es correcto.
- ✅ **Estructura:** tres partes (*Tidyings*, *Managing*, *Theory*), 33 capítulos. Se corrigió «el primer tercio del libro» → «quince de los treinta y tres capítulos», porque la proporción en páginas no se pudo verificar y por capítulos no es un tercio.
- ✅ **Cantidad y nombres de los tidyings:** quince, y los quince nombres del borrador coinciden exactamente con el índice.
- ✅ **Capítulos económicos:** 24 «Economics: Time Value and Optionality», 25 «A Dollar Today > A Dollar Tomorrow», 26 «Options».
- ✅ **Newsletter → libro:** confirmado por Beck en «How I Came To Write "Tidy First?"» (newsletter desde enero 2021, O'Reilly después) y demostrable capítulo por capítulo: «First, After, Later, Never» es post de julio 2022 y capítulo 21 del libro de 2023.

**Quedan dos marcas `[VERIFICAR:]`**, ambas por la misma causa —el texto interior del libro está tras paywall y O'Reilly devuelve 403 a fetch automatizado— y ambas requieren el ejemplar impreso:

- ❌ **Origen del término *tidying*:** busqué en el post «How I Came To Write "Tidy First?"» (no lo explica), en la charla de QCon Plus 2023 en InfoQ (usa *tidy* y *structure change* como sinónimos sin justificar la palabra) y en la ficha/índice de O'Reilly. Sólo hay reseñas de terceros parafraseando. Chequear la introducción impresa.
- ❌ **Si Beck cita a Fowler dentro del libro:** el «Appendix A: Annotated Reading List and References» existe y está confirmado en el índice, pero no conseguí su contenido. *Sí* quedó verificado —y ya está en la prosa— que Beck escribió un capítulo del *Refactoring* de Fowler (1999) y que la portada lo acredita. Chequear el apéndice impreso.

**Hallazgos de bitrot (accionables antes de publicar):**
- El link de *3X* a Facebook **está muerto** (muro de login; Facebook discontinuó las Notes). Reemplazado por el Medium del propio Beck, fetcheado y legible. Ya no hace falta el backup de Wayback que pedía el borrador.
- `tidyfirst.substack.com` **redirige 301** a `newsletter.kentbeck.com`. Links actualizados.
- **`ronjeffries.com` está caído** (`ECONNREFUSED`, dos intentos). Wayback reporta snapshot 200 de 2016 vía la availability API, pero web.archive.org no es fetcheable desde este entorno, así que el snapshot **no está verificado**. Reintentar antes de publicar; si sigue caído, citar el libro impreso (ISBN 0735619492).
- El link de Fowler ahora apunta a `martinfowler.com` (sitio del autor) en vez de la ficha de O'Reilly, según la regla de la casa.

Siguen los **cinco huecos** (🕳️) que necesitan a César: cómo llegó al libro, cuándo aprendió a hacer tidy en su propio código (gancho de [[E-04]]), un caso real de PR mezclado, su tidying favorito y su reacción al capítulo económico. Pendiente al publicar: **actualizar el Concepto y el Outline a las cuatro opciones**, resolver los `[[ID]]` a URLs reales, dibujar los dos diagramas de la sección **Imágenes** y conseguir un hero landscape.

---

## Borrador de prosa

Kent Beck —el del XP, el del TDD— publicó en 2023 un librito de poco más de cien páginas titulado *Tidy First?*[^tidyfirst] —124 según la ficha de la edición impresa[^ficha]—. Con signo de pregunta. Y ese signo de pregunta es todo el libro.

Porque lo que uno espera de un tipo que viene del *Extreme Programming*[^xp] es un imperativo: limpiá siempre, limpiá antes, dejá el campamento más limpio de como lo encontraste. Y Beck no dice eso. Beck dice: *aprendé a decidir cuándo*. A veces conviene limpiar antes de tocar el comportamiento, a veces conviene limpiar después, y a veces —esta es la parte que incomoda— conviene no limpiar nunca. El libro es un método para elegir entre esas tres, y en el camino se mete en un lugar donde ningún libro de código se mete: las finanzas.

### Un *tidying* no es «un refactor chiquito»

Lo primero que hace Beck es acuñar una palabra propia[^tidyfirst] [VERIFICAR: si Beck presenta *tidying* como término propio o lo atribuye a alguien — busqué en el post «How I Came To Write "Tidy First?"» de su propia newsletter (no explica el origen del término), en la charla de Beck en QCon Plus 2023 publicada por InfoQ (usa *tidy* y *structure change* como sinónimos pero no justifica la palabra) y en la ficha y el índice de O'Reilly; la introducción del libro es paywall y no pude abrirla. Sólo hay reseñas de terceros parafraseándolo. Chequear contra la introducción impresa]. Podría haber dicho «refactor pequeño» y todos habríamos entendido, porque *Refactoring* de Fowler[^fowler] es el vocabulario compartido de la profesión desde hace décadas y Beck lo da por sabido —literalmente: Fowler lo publicó en 1999 «with Kent Beck» en la portada, y el propio Beck cuenta que escribió un capítulo y opinó sobre casi todo el resto, y que desde entonces quería hacer su propia versión a su manera[^comollegue] [VERIFICAR: si Beck cita explícitamente a Fowler *dentro* de *Tidy First?* y en qué términos — el libro tiene un «Appendix A: Annotated Reading List and References» que sería el lugar natural, y su índice está confirmado, pero no conseguí el contenido del apéndice: O'Reilly devuelve 403 y las reseñas que lo mencionan no lo transcriben. Chequear contra el apéndice impreso]. Pero «refactor» se contaminó. En la práctica de la industria, «voy a refactorizar esto» pasó a significar cualquier cosa entre renombrar una variable y reescribir tres meses de sistema. Es una palabra que ya no discrimina.

*Tidying* discrimina. Un tidying es una limpieza tan chica que la podés hacer y descartar sin remordimiento: renombrar, extraer, reordenar, borrar. Minutos, no horas. Y sobre todo: **un tidying no cambia el comportamiento**. Esa es la línea que el libro traza y sobre la que apoya todo lo demás. Del otro lado de la línea están los *behavior changes*: los cambios que un usuario podría notar. Dos categorías, mutuamente excluyentes, y la regla operativa que sale de ahí es brutalmente simple: **no las mezcles en el mismo commit**.

Suena a obviedad de higiene. No lo es. Es una tesis sobre economía y sobre gente, y el libro tarda cien páginas en explicar por qué.

### Los tidyings: la lista

El libro tiene tres partes —*Tidyings*, *Managing*, *Theory*— y treinta y tres capítulos cortísimos[^ficha]. La primera parte es un catálogo, y ocupa quince de esos treinta y tres capítulos: uno por tidying[^toc]. Quince entradas, en el orden del índice: *guard clauses*, *dead code*, *normalize symmetries*, *new interface, old implementation*, *reading order*, *cohesion order*, *move declaration and initialization together*, *explaining variables*, *explaining constants*, *explicit parameters*, *chunk statements*, *extract helper*, *one pile*, *explaining comments*, *delete redundant comments*.

Ninguno te va a sorprender. Ese es el punto. Te comento cuatro:

**Guard clauses.** Sacar los casos borde al principio de la función, con un `return` temprano, en vez de anidar la lógica principal dentro de un `if` de tres niveles. El efecto no es de performance ni de líneas: es que el lector deja de tener que sostener condiciones en la cabeza mientras baja.

**Dead code.** Borrarlo. Nada más. Y la razón por la que hace falta que alguien lo escriba en un libro es que todos tenemos el reflejo de comentarlo «por las dudas» —un reflejo que tenía sentido antes de `git`, y que sobrevivió treinta años a la desaparición de su motivo.

**Normalize symmetries.** Cuando dos pedazos de código hacen lo mismo de dos maneras distintas, hacé que lo hagan de la misma manera. No los unifiques todavía: primero volvelos idénticos. La deduplicación, si conviene, sale sola después. Es un tidying que prepara el terreno para otro cambio, y ahí ya se ve el espíritu del libro: los tidyings no son el fin, son la pendiente por la que el cambio siguiente baja más rápido.

**One pile.** Este es el contraintuitivo. A veces el código está *demasiado* fragmentado —seis funciones de tres líneas que sólo se llaman entre sí y que te obligan a saltar por el archivo para entender una cosa sola. El tidying es juntar todo en un solo montón, leerlo entero, y recién entonces volver a cortarlo, pero por donde corresponde. Beck te está dando permiso explícito para desandar una abstracción prematura, que es algo que la cultura del «extraé método» nunca te dio.

> 🕳️ **HUECO — necesita a César:** ¿hay algún tidying de esta lista que hagas de manera automática, sin pensarlo, cada vez que abrís un archivo ajeno? ¿Cuál, y en qué lenguaje/proyecto se te hizo costumbre?

### La pregunta del título

La segunda parte es el framework de decisión, y es donde el signo de pregunta cobra sentido. Frente a un cambio de comportamiento que querés hacer sobre código que no está limpio, tenés cuatro opciones —el capítulo se llama, precisamente, «First, After, Later, Never»[^toc] [^falner]:

- **First.** Limpiás, y después el cambio de comportamiento entra fácil. Conviene cuando la limpieza paga de inmediato —en comprensión o en un cambio más barato— y cuando ya sabés qué limpiar y cómo.
- **After.** Hacés el cambio como puedas, y limpiás cuando ya sabés qué forma tenía que tener el código. Conviene cuando esperar hasta la próxima vez saldría más caro.
- **Later.** Anotás el desorden y volvés más tarde. Conviene cuando tenés un lote grande de limpieza sin rédito inmediato, pero sí eventual, y podés hacerla en tandas chicas.
- **Never.** No lo tocás. Conviene cuando no vas a volver a cambiar ese código nunca más y no hay nada que aprender mejorando el diseño.

Lo interesante es que las cuatro son respuestas legítimas y la elección no depende de la estética del código sino de dos variables: **cuánto cuesta** y **cuán seguro estás** de lo que viene después. La incertidumbre es un argumento a favor de esperar. Y «never» deja de ser una confesión de pecado para pasar a ser una decisión de ingeniería, que es un alivio moral considerable.

> ✏️ **Corrección de la pasada de fuentes (2026-07-15):** el borrador original listaba **tres** opciones (first / after / never). El libro presenta **cuatro**: el capítulo 21 se titula «First, After, Later, Never», y *Later* —anotar y volver después— es una categoría propia, distinta de *after*. Verificado contra el índice del libro y contra el post homónimo de la newsletter (29-07-2022), que enumera las cuatro. Se corrigió la prosa. **El Concepto y el Outline (punto 3) siguen diciendo «antes, después o nunca» y hay que actualizarlos — son de César, no los toco.**

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste a *Tidy First?* — ¿por la newsletter de Beck, alguien te lo recomendó, lo cruzaste en O'Reilly? Una o dos frases alcanzan.

### La parte que nadie espera: finanzas

Y acá el libro se va a un lado que no anticipa nadie. Para defender ese framework de decisión, Beck se mete con economía financiera de verdad: el costo del dinero, el descuento de flujos futuros, y la idea de que mantener el código flexible es comprar una **opción**. Los títulos de la tercera parte no dejan lugar a dudas —capítulo 24, «Economics: Time Value and Optionality»; capítulo 25, «A Dollar Today > A Dollar Tomorrow»; capítulo 26, «Options»[^toc]—, y la propia ficha del editor anuncia *discounted cash flows* entre los temas del libro[^ficha].

El argumento, resumido y con toda la cautela del caso, es más o menos así. Un peso hoy vale más que un peso mañana; por lo tanto un cambio de comportamiento que produce valor hoy vale más que una limpieza que produce valor difuso en un futuro incierto. Ese razonamiento, solo, te llevaría a no limpiar nunca. Pero un código ordenado te da algo que el flujo descontado no captura: la **opción** de hacer, más adelante, un cambio que hoy ni sabés que vas a querer hacer. Y las opciones valen más cuanto más incierto es el futuro. Es exactamente al revés que la intuición: cuanto menos sabés lo que viene, más te conviene pagar por mantener abiertas las puertas.

Ahí está la elegancia del planteo. Las dos fuerzas —el descuento, que empuja a no limpiar; la opcionalidad, que empuja a limpiar— tiran para lados opuestos, y el libro no las resuelve con un eslogan. Te da el vocabulario para pesarlas caso por caso. Y de paso fundamenta «dejá el código un poco mejor de como lo encontraste» sin apelar ni una vez a la culpa, que es un cambio de registro notable para un consejo que casi siempre se da en tono de reto.

> 🕳️ **HUECO — necesita a César:** cuando leíste el capítulo de la parte económica, ¿te convenció o te pareció una elaboración de más? ¿Y alguna vez tuviste que justificar tiempo de limpieza ante alguien que manejaba el presupuesto?

### La parte humana: el PR mezclado

La otra mitad del argumento no es económica: es sobre gente. Un pull request que mezcla veinte archivos renombrados con tres líneas de lógica nueva es, para el que revisa, ilegible. No porque sea difícil, sino porque el ruido tapa la señal: el revisor scrollea ciento cincuenta líneas de cambios inofensivos buscando las tres que importan, y si el PR es largo, en algún momento deja de buscar y aprueba. Todos vimos ese PR. Muchos escribimos ese PR.

Separar en dos —uno de tidyings, que se lee en treinta segundos y se aprueba sin pensar; otro de comportamiento, chiquito, donde cada línea merece atención— no es prolijidad. Es bajar la carga cognitiva del revisor al punto donde el review vuelve a ser un acto de pensamiento y no un trámite. La regla de Beck no le sirve al que escribe: le sirve al que lee. Y como en cualquier equipo el código se lee muchas más veces de las que se escribe, el balance cierra.

> 🕳️ **HUECO — necesita a César:** ¿tenés un caso concreto —tuyo o de un equipo tuyo— de un PR mezclado que se aprobó sin que nadie viera lo que importaba? Sin nombres si hace falta, pero con el detalle de qué se coló.

### Lo que XP siempre quiso decir

Cierro con lo que más me quedó. Beck viene de *Extreme Programming Explained*[^xp] y de *TDD by Example*[^tdd], dos libros que le dieron a la profesión prácticas concretas y una cultura entera. Pero XP siempre tuvo un costado de prédica: hacé esto, es lo correcto, confiá. Funcionaba con los convencidos y rebotaba contra todos los demás.

*Tidy First?* es lo mismo dicho veinte años después, sin prédica. Es XP con la economía explicitada y la culpa sacada del medio: acá está la práctica, acá está por qué paga, acá está cuándo no paga, decidí vos. El libro tiene el tono de alguien que ya no necesita convencer a nadie —el subtítulo mismo lo dice: *a personal exercise in empirical software design*. Un ejercicio personal. Nada de manifiesto.

Y es coherente con el resto de su obra tardía: la misma cabeza que separó explorar, expandir y extraer en *3X*[^3x] es la que ahora separa tidying de behavior change. Beck lleva años haciendo la misma jugada: agarrar una decisión que tomamos por instinto, ponerle nombre a las opciones y devolverla convertida en algo que se puede discutir en voz alta.

Si querés ver los tidyings aplicados en serie por otro de los firmantes del manifiesto, Ron Jeffries publicó años de esto en su sitio[^jeffries]. Y buena parte del material del libro apareció primero en la newsletter de Beck[^newsletter]. Él mismo cuenta la secuencia: arrancó el Substack en enero de 2021 como mecanismo para obligarse a escribir, y recién cuando tenía material acumulado firmó con O'Reilly[^comollegue]. Se puede comprobar capítulo por capítulo: «First, After, Later, Never» salió como post el 29 de julio de 2022[^falner] y es el capítulo 21 del libro, publicado en 2023.

> 🕳️ **HUECO — necesita a César:** para enganchar con [[E-04]] — ¿cuándo aprendiste a hacer tidy en tu propio código? ¿Fue leyendo a alguien, fue un code review que te dolió, fue volver a un proyecto tuyo dos años después?

[^tidyfirst]: Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly Media, 2023, 124 pp. ISBN 9781098151249 (impreso), 9781098151218. [[tr-08]]
[^ficha]: [*Tidy First?* — ficha de la edición, Google Books](https://books.google.com/books/about/Tidy_First.html?id=-2ndEAAAQBAJ) — O'Reilly Media, 124 páginas; da las tres partes (*Tidyings*, *Managing*, *Theory*), el apéndice «Annotated Reading List and References», y menciona *discounted cash flows* entre los temas. Corroborado en [Open Library](https://openlibrary.org/works/OL35973549W) (124-125 pp. según edición). Estable.
[^toc]: Índice de *Tidy First?* — 33 capítulos en tres partes: I. *Tidyings* (caps. 1-15, uno por tidying), II. *Managing* (6 caps., incluye el 21 «First, After, Later, Never»), III. *Theory* (12 caps., incluye el 24 «Economics: Time Value and Optionality», el 25 «A Dollar Today > A Dollar Tomorrow» y el 26 «Options»). La ficha canónica es [la del editor en O'Reilly](https://www.oreilly.com/library/view/tidy-first/9781098151232/) (estable, pero devuelve HTTP 403 a fetch automatizado); el índice completo verificado vía [este resumen del libro](https://www.workingsoftware.dev/summary-of-tidy-first-book/) (frágil) y contrastado con la reseña de [Henrik Warne](https://henrikwarne.com/2024/01/10/tidy-first/) (frágil), que confirma independientemente las tres partes y los 15 tidyings.
[^falner]: [Kent Beck, «First, After, Later, Never», *Software Design: Tidy First?*, 29-07-2022](https://newsletter.kentbeck.com/p/first-after-later-never) — las cuatro opciones y el criterio de cada una; el desarrollo completo está tras el paywall del Substack, pero el planteo de las cuatro y el criterio de *Never* son legibles. Frágil (Substack).
[^comollegue]: [Kent Beck, «How I Came To Write "Tidy First?"», *Software Design: Tidy First?*](https://newsletter.kentbeck.com/p/how-i-came-to-write-tidy-first) — «When Martin Fowler wrote Refactoring in 1999, I contributed a chapter & kibitzed on most of it»; cuenta que arrancó la newsletter en enero de 2021 y que firmó con O'Reilly una vez acumulado el material. Frágil (Substack).
[^newsletter]: [Kent Beck, newsletter *Software Design: Tidy First?*](https://newsletter.kentbeck.com/) — donde apareció primero buena parte del material del libro. **Ojo:** el dominio viejo `tidyfirst.substack.com` redirige (301) a `newsletter.kentbeck.com`; usar el nuevo. Frágil (Substack).
[^tdd]: Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley, 2002 (impresión de 2003), xix + 220 pp. ISBN 0321146530. Copia en [Internet Archive](https://archive.org/details/testdrivendevelo0000beck) — préstamo digital controlado. Estable.
[^xp]: Kent Beck, *Extreme Programming Explained: Embrace Change*, 2.ª ed. (con Cynthia Andres), Addison-Wesley, 2004, ISBN 0321278658. Archive.org tiene la [1.ª edición, Addison-Wesley 2000, ISBN 0201616416, 226 pp.](https://archive.org/details/extremeprogrammi00beck) — préstamo digital controlado, edición anterior a la citada. Estable.
[^fowler]: [Martin Fowler, *Refactoring: Improving the Design of Existing Code*, 1.ª ed. 1999 / 2.ª ed. 2018](https://martinfowler.com/books/refactoring.html) — sitio del propio autor; la portada acredita «by Martin Fowler, with Kent Beck». El vocabulario que Beck da por conocido. Estable.
[^jeffries]: Ron Jeffries, *Adventures in C#* — serie de artículos, índice en `https://ronjeffries.com/xprog/acsindex/`. **Link caído:** el dominio devolvió `ECONNREFUSED` en dos intentos (2026-07-15); no pude abrirlo. La API de disponibilidad de Wayback reporta snapshot 200 en `http://web.archive.org/web/20160123083241/http://ronjeffries.com:80/xprog/acsindex/`, pero web.archive.org no es fetcheable desde este entorno, así que **el contenido del snapshot no está verificado**. Reintentar el sitio antes de publicar; si sigue caído, citar el libro impreso: Ron Jeffries, *Extreme Programming Adventures in C#*, Microsoft Press, 2004, ISBN 0735619492. Frágil.
[^3x]: [Kent Beck, «The Product Development Triathlon» (3X: Explore/Expand/Extract), 2016](https://medium.com/@kentbeck_7670/the-product-development-triathlon-6464e2763c46) — texto completo legible en el Medium del propio Beck. **Sustituye al link de Facebook del borrador** (`facebook.com/notes/kent-beck/the-product-development-triathlon/…`), que hoy sólo muestra un muro de login: Facebook discontinuó las Notes. Frágil (Medium).

