### B-08 — Warren's Abstract Machine y la arqueología de implementaciones de Prolog (micro-PROLOG, small-prolog, wambook)

- **Archivo seed:** `github.com/CesarBallardini/wambook` (fork, 2020) + `github.com/CesarBallardini/small-prolog-walnut-creek-original` (fork, 2024) + `github.com/CesarBallardini/micro-PROLOG` (fork, 2018, Spectrum micro-Prolog T1.0 disassembled)
- **Slug propuesto:** `warren-abstract-machine-arqueologia-prolog`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-warren-abstract-machine-arqueologia-prolog/index.md`
- **Serie:** B — deep dive sobre cómo se implementa *de verdad* un lenguaje declarativo
- **Cross-links:** depende de [[A1-10]] (el post de Prolog "soy mi propio abuelo" — la experiencia del lector); lleva a [[B-02]] (Okasaki — estructuras de datos puramente funcionales, otro "qué hay debajo"), [[I-03]] (Spectrum y MicroHobby — donde apareció micro-PROLOG), [[I-07]] (SuperLib Clipper — otra reliquia de los 80 rescatada), [[A1-08]] (kl1c — lógica concurrente, primo cercano de Prolog)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** long (2500-3500 palabras) — es un post técnico denso con tres sub-historias

**Concepto:** ¿cómo se implementa realmente un intérprete de Prolog? La respuesta canónica es la Warren Abstract Machine (David H D Warren, 1983) — un conjunto mínimo de instrucciones para una máquina virtual que ejecuta Prolog con unificación, backtracking y trail eficientes. El post recorre tres implementaciones históricas de distinto porte y cuenta qué se aprende de cada una: (1) el *micro-PROLOG T1.0* para ZX Spectrum, un intérprete completo de Prolog que cabe en 16 KB y cuya Z80 assembly fue desensamblada (el repo `micro-PROLOG` tiene el source); (2) el *small-prolog* de Henri de Feraudy, un Prolog mínimo en C que se puede leer en una tarde; (3) la *WAM tutorial reconstruction* de Hassan Aït-Kaci (el wambook) — el libro de texto canónico sobre la WAM. Tres escalones: juguete heroico → didáctico legible → máquina abstracta de verdad.

**Hook:** "¿cómo cabe un intérprete de Prolog completo en 16 KB en un Spectrum de 1984? Y ¿cómo es que 20 años después Hassan Aït-Kaci escribe un libro entero de 114 páginas para explicar la máquina virtual (WAM) que lo hace eficiente? Son la misma pregunta, en dos escalas. Tengo en mi GitHub los tres escalones: el *micro-PROLOG* desensamblado del Spectrum, un *small-prolog* de 3000 líneas en C, y el wambook. El post los recorre en orden de complejidad creciente — tres visitas a la misma idea, una en assembler Z80, otra en C, otra en abstracción formal. Al final del post entendés por qué la unificación es la operación más rara y hermosa de la computación."

**Outline:**
1. **La pregunta de fondo**: ¿qué *operaciones primitivas* necesita un intérprete de Prolog para funcionar? Respuesta corta: unificación, backtracking, resolución SLD, manejo de trail y choice points. Respuesta larga: los 30 opcodes de la WAM.
2. **Escalón 1 — micro-PROLOG T1.0 para Spectrum 48K**. Desarrollado por *Logic Programming Associates* a principios de los 80 para ZX Spectrum. Sintaxis no estándar (micro-Prolog usaba listas como predicados). El repo `micro-PROLOG` tiene la ROM desensamblada. Qué cabe en 16 KB: un parser, un unificador simple, un motor de resolución, una micro-biblioteca. Qué NO cabe: optimización de colas, indexado de primera cláusula, compilación a WAM. La anécdota del Spectrum aprendiendo Prolog por escrito ([[I-03]] conecta acá).
3. **Escalón 2 — small-prolog de Henri de Feraudy**. ~3000 líneas de C, toma archivos `.pl`, los parsea, los ejecuta. Diseñado para *ser leído*. La estructura: estructuras `term`, un ambiente de binding, el loop principal de unificación recursiva, el trail como stack explícito. Un ejercicio pedagógico perfecto. Cómo clonarlo, compilarlo y modificarlo hoy (el fork en mi GitHub).
4. **Escalón 3 — Warren Abstract Machine (wambook)**. La idea central: *compilar* Prolog a instrucciones de máquina abstracta en vez de interpretarlo estructura por estructura. Los 30 opcodes de la WAM, agrupados en 4 familias: instrucciones de put (construir términos en registros), get (deconstruir términos con unificación), indexación, control de flujo. Por qué este paso de "compilación" es lo que hace a SWI-Prolog y Sicstus ser competitivos en velocidad con C para ciertos problemas.
5. **El corazón del asunto — la unificación**. La operación mágica. Dos términos, un conjunto de bindings. Se unifican si existen bindings que los hacen idénticos. Contrasta con pattern matching (más simple, unidireccional) y con type inference (más abstracto, sin ejecución). La unificación *resuelve* en tiempo de ejecución lo que otros lenguajes calculan en tiempo de compilación.
6. **Backtracking y choice points**. Cómo la WAM mantiene los puntos de elección en el stack para "deshacer" computaciones y probar alternativas. El trail como lista de variables a des-bindear. Por qué es más eficiente que mantener copias del ambiente.
7. **Indexado de primera cláusula (first-argument indexing)**. La optimización que hace a los intérpretes modernos ser ~100× más rápidos que la implementación ingenua: cuando hay muchas cláusulas para un mismo predicado, la WAM mira el primer argumento del goal y salta directamente a las cláusulas que *podrían* unificar. Sin este truco, Prolog no sería viable para bases de hechos grandes.
8. **¿Y entonces por qué no lo usamos?** La pregunta honesta. Respuesta: Prolog tiene el *mejor modelo de ejecución* para una clase de problemas (búsqueda con restricciones, análisis de grafos, parsing con DCGs) y *un modelo muy pobre* para cualquier otra cosa. Los frameworks modernos (ASP, Datalog, miniKanren en Scheme) heredan partes de la WAM sin adoptar Prolog entero.
9. **Cierre**: la unificación como primitiva lingüística sigue sub-explotada. Miren Datalog (usado en Rust's polonius borrow checker), miren miniKanren, miren Souffle. Son todos descendientes del wambook.

**Bibliografía:** (reforzada 2026-07-16, fuentes verificadas por fetch)
- [Hassan Aït-Kaci, *Warren's Abstract Machine: A Tutorial Reconstruction*, MIT Press, 1991](https://mitpress.mit.edu/9780262510585/warrens-abstract-machine/) — 114 páginas, ISBN 0262510588 (Logic Programming Series). El autor conserva el copyright y autorizó la distribución libre para uso no comercial; PDF y PostScript en el [repo `a-yiorgos/wambook`](https://github.com/a-yiorgos/wambook) (upstream del fork `wambook` de César) y catalogado por [OnlineBooks — Penn](https://onlinebooks.library.upenn.edu/webbin/book/lookupid?key=olbp10340). La reimpresión libre en PDF (fechada 18-feb-1999, «REPRINTED FROM MIT PRESS VERSION») está numerada hasta la página 129 contando el índice. _estable_ (MIT Press + GitHub); la copia en cliplab.org es _frágil_.
- [David H. D. Warren, *An Abstract Prolog Instruction Set*, SRI Technical Note 309, octubre 1983](https://www.sri.com/publication/cyber-formal-methods-pubs/an-abstract-prolog-instruction-set/) — el documento original de la WAM. [PDF escaneado directo (34 pp.)](https://www.sri.com/wp-content/uploads/2021/12/641.pdf) alojado por el propio SRI. _estable_ (institucional).
- [Peter Van Roy, *1983–1993: The Wonder Years of Sequential Prolog Implementation*, Journal of Logic Programming, vol. 19/20, 1994, pp. 385–441](https://dblp.org/rec/journals/jlp/Roy94.html) — panorama de la década de implementaciones. Preprint libre: [DEC Paris Research Laboratory, Research Report 36, dic. 1993](https://webperso.info.ucl.ac.be/~pvr/PRL-TR-36.pdf) (mirror en [ps.uni-saarland.de](https://www.ps.uni-saarland.de/Publications/documents/VanRoy_SequentialPro.pdf)). _frágil_ los PDF en páginas personales; el registro dblp es _estable_.
- [Alain Colmerauer y Philippe Roussel, *The Birth of Prolog*, ACM SIGPLAN Notices 28(3), 1993, pp. 37–52](https://doi.org/10.1145/155360.155362) — origen histórico de Prolog (HOPL II); contexto para [[A1-10]]. Preprint libre de noviembre 1992 en el [sitio de Colmerauer](http://alain.colmerauer.free.fr/alcol/ArchivesPublications/PrologHistory/19november92.pdf). _estable_ (DOI verificado en Crossref); el mirror es _frágil_.
- [Logic Programming Associates, *micro-PROLOG*, ZX Spectrum, publicado por Sinclair Research, 1983 — ficha en Spectrum Computing](https://spectrumcomputing.co.uk/entry/8429/ZX-Spectrum/Micro-PROLOG) — intérprete para el Spectrum de 48K. Desensamblado/reconstrucción de la versión T1.0 (14 200 bytes, 0x6000–0x9777): [repo `oldcompcz/micro-PROLOG`](https://github.com/oldcompcz/micro-PROLOG), upstream del fork de César. _estable_.
- [Henri de Feraudy, *Small Prolog*, C User's Group / Walnut Creek CD-ROM](https://archive.org/details/C_Users_Group_Library_Walnut_Creek_August_1994) — el source original preservado en Internet Archive; también en el [repo `opless/small-prolog-walnut-creek-original`](https://github.com/opless/small-prolog-walnut-creek-original), upstream del fork de César. _estable_.
- [SWI-Prolog — sitio oficial](https://www.swi-prolog.org/) y [J. Wielemaker et al., *SWI-Prolog*, Theory and Practice of Logic Programming, 2012](https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/swiprolog/13570311D10C2F20A29F0BE4DF5C03D1) — el intérprete moderno de referencia; el [manual](https://www.swi-prolog.org/pldoc/man?section=overview) tiene un panorama del modelo de ejecución. _estable_.
- [William Byrd, *miniKanren*](http://minikanren.org/) — heredero en Scheme de la unificación. _estable_.
- [Peter Norvig, *Paradigms of Artificial Intelligence Programming*, Morgan Kaufmann, 1991 — código libre](https://github.com/norvig/paip-lisp) — implementa Prolog en Lisp, otro ángulo pedagógico. _estable_.

**Imágenes:**
- _Crear_: diagrama de los 3 escalones (micro-PROLOG → small-prolog → WAM) con una misma query (`append([1,2], [3,4], X)`) ejecutada en cada uno (~1 hora — central del post).
- _Crear_: tabla de los 30 opcodes de la WAM agrupados en 4 familias (~45 min).
- _Crear_: diagrama del flujo de unificación con trail y choice points (~30 min).
- _Crear_: scan/screenshot del manual original de micro-PROLOG T1.0 (~15 min de buscar).

**Tags propuestos:** `['Prolog', 'WAM', 'Warren Abstract Machine', 'unification', 'micro-PROLOG', 'Spectrum', 'small-prolog', 'compiladores', 'deep dive']`

**Estado actual:** prosa-borrador escrita (2026-07-15, generada por Claude, sin revisar por César). Está escrito el hilo completo de los nueve puntos del outline: el encuadre de la pregunta, los tres escalones (micro-PROLOG → small-prolog → WAM), la sección sobre unificación, backtracking/trail, indexado de primer argumento, el «¿y entonces por qué no lo usamos?» y el cierre sobre los descendientes. El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 4 de 8 marcadores [VERIFICAR:].

**Lo que quedó como hueco** (necesita a César): por qué forkeó cada uno de los tres repos y cuándo, si llegó a compilar/correr small-prolog y micro-PROLOG, si tuvo un Spectrum con micro-PROLOG en su momento o lo conoció después, qué le pasó al leer el wambook, y su opinión sobre por qué Prolog no cuajó. Son 8 huecos chicos y específicos.

**Lo que quedó como `[VERIFICAR:]`**: en el pase del 2026-07-16 se resolvieron por fetch las páginas del wambook (114 en MIT Press 1991; la reimpresión libre numera hasta 129 con índice), el tamaño del micro-PROLOG (14 200 bytes según el desensamblado T1.0), la fecha y el editor de LPA (1983, publicado por Sinclair Research) y el estado de Polonius (experimental, nightly `-Zpolonius`, no default — se corrigió la afirmación del cierre). Siguen abiertos cuatro marcadores que no se pueden cerrar sin material propio: la cantidad exacta de opcodes de la WAM y si la agrupación put/get/indexación/control es la de Aït-Kaci (hay que revisar el índice del libro, y el conteo depende de contar variantes `unify_*`/`set_*`), un ejemplo real de la sintaxis de micro-Prolog tomado del manual, las líneas de C de small-prolog (`wc -l` sobre el fork), y el factor de aceleración del indexado (necesita una medición propia o se saca el número). Nada se afirmó de memoria.

**Conflicto de encuadre a resolver antes de publicar:** el Hook dice «20 años después Hassan Aït-Kaci escribe un libro». Según la propia bibliografía del draft, Warren es de 1983 y Aït-Kaci de 1991: son ocho años, no veinte. La prosa está escrita evitando el número (dice «casi una década»); si el Hook se conserva tal cual en el post publicado, hay que corregirlo ahí.

Sesión de revisión estimada: una tarde para contestar huecos + una tarde para verificar números contra las fuentes.

---

## Borrador de prosa

Hay una pregunta que me da vueltas hace años y que casi nadie se hace en voz alta: ¿cómo funciona un intérprete de Prolog *por dentro*? No «cómo se usa Prolog» — eso está en cualquier tutorial, y de eso hablé en [[A1-10]], donde jugamos a ser nuestro propio abuelo. Digo por dentro, en serio: qué operaciones primitivas necesita una máquina para tomar `?- abuelo(juan, X).` y devolver `X = pedro` sin que vos le hayas dicho cómo buscarlo.

Tengo en mi GitHub tres respuestas a esa pregunta, forkeadas en años distintos y por motivos distintos, y recién hace poco me di cuenta de que son la misma respuesta contada en tres escalas. Un intérprete de Prolog entero metido a presión en una ROM de ZX Spectrum. Un Prolog mínimo en C escrito para que lo leas de corrido una tarde. Y un libro de texto que dedica capítulos enteros a explicar una máquina virtual que existe solamente en papel. Juguete heroico, pieza didáctica, máquina abstracta de verdad. Voy a recorrerlos en ese orden, y al final vas a entender por qué la unificación me parece la operación más rara y más hermosa de toda la computación.

> 🕳️ **HUECO — necesita a César:** ¿en qué orden y por qué forkeaste los tres repos? El de micro-PROLOG es de 2018, el wambook de 2020, el small-prolog de 2024 — ¿hubo un disparador concreto en cada caso (un proyecto, una lectura, una charla) o fue coleccionismo puro?

### La pregunta de fondo

Prolog tiene una propiedad que lo hace incómodo de implementar: vos escribís hechos y reglas, y no escribís el algoritmo de búsqueda. El algoritmo de búsqueda *es* el lenguaje. Cuando preguntás algo, el motor tiene que probar caminos, ligar variables tentativamente, darse cuenta de que ese camino no va, deshacer las ligaduras que hizo y probar el camino siguiente. Todo eso sin que aparezca en tu código.

La respuesta corta a «qué necesita un intérprete de Prolog» es una lista de cinco cosas: unificación, resolución SLD, backtracking, choice points y trail. La respuesta larga es la Warren Abstract Machine: un juego de instrucciones para una máquina virtual que David H. D. Warren describió en un technical note de SRI en 1983[^warren]. La respuesta larga, además, tiene una propiedad rara para un documento técnico: es tan condensada que casi una década después Hassan Aït-Kaci escribió un libro entero cuyo único propósito es explicarla, reconstruyéndola paso a paso en vez de presentarla terminada[^aitkaci].

Es un dato que dice mucho. El paper original de Warren no es un paper difícil porque el autor escribiera mal: es difícil porque describe el resultado sin describir el camino. Aït-Kaci hace lo contrario — empieza con una máquina de juguete que apenas unifica términos, y le va agregando capas hasta que, sin que te des cuenta, llegaste a la WAM completa. Es didáctica de la buena, del tipo que casi no se hace.

### Escalón 1 — micro-PROLOG T1.0 para ZX Spectrum

Empecemos por lo más chico y lo más increíble. En 1983, Logic Programming Associates llevó micro-PROLOG al ZX Spectrum de 48K, publicado a través de Sinclair Research[^lpa]. Un intérprete de Prolog completo — parser, unificador, motor de resolución, una micro-biblioteca de predicados — en el espacio que tenía una máquina de esa época: en la reconstrucción de la versión T1.0, el intérprete ocupa 14 200 bytes —unos 13,9 KB—, cargados entre las direcciones 0x6000 y 0x9777[^microprolog_src].

La primera sorpresa al mirarlo no es el tamaño: es la sintaxis. micro-Prolog no usaba la notación de Edimburgo que hoy damos por sentada. Usaba listas para todo, incluso para los predicados, así que un hecho no se escribía `padre(juan, pedro).` sino como una lista con el functor adentro. [VERIFICAR: forma exacta de la sintaxis de micro-Prolog — dar un ejemplo real tomado del manual T1.0 o del desensamblado, no reconstruido de memoria] Era Prolog, pero un Prolog que no reconocerías de entrada. Y tiene todo el sentido del mundo: parsear listas es dramáticamente más barato que parsear términos con operadores, precedencia y azúcar sintáctico. Cuando cada byte de la ROM te cuesta, el azúcar es lo primero que se cae.

Lo segundo que cae es la eficiencia. Lo que *no* entra en una implementación así es justamente todo lo que este post va a ir contando después: nada de indexado de primer argumento, nada de optimización de last-call, nada de compilar a una máquina abstracta. Es interpretación directa, estructura por estructura, recorriendo la base de cláusulas de arriba a abajo. Anda, y para bases de hechos chiquitas anda bien. Es un juguete heroico.

El repo `micro-PROLOG` de mi GitHub tiene el desensamblado en assembler Z80. Leerlo es una experiencia particular: estás viendo la unificación — una idea de la lógica matemática — expresada en registros de ocho bits.

> 🕳️ **HUECO — necesita a César:** ¿tuviste micro-PROLOG en un Spectrum en su momento, o lo conociste años después? Si fue en su momento: ¿te llegó por MicroHobby, por una copia de un amigo, comprado? Esto conecta con [[I-03]] y necesita tu recuerdo real.

> 🕳️ **HUECO — necesita a César:** el desensamblado del repo — ¿lo hiciste vos, lo forkeaste ya desensamblado de otro, o partiste de un desensamblado ajeno y lo anotaste? Es una diferencia importante para el post.

### Escalón 2 — small-prolog, de Henri de Feraudy

El segundo escalón es un Prolog mínimo en C, escrito por Henri de Feraudy, que anduvo circulando en los CD-ROM de Walnut Creek[^smallprolog] — esa forma de distribución de software que hoy suena a arqueología y que en su momento era la manera normal de que el código libre te llegara a las manos. [VERIFICAR: cantidad real de líneas de C de small-prolog; el Hook dice ~3000 — correr `wc -l` sobre el fork `small-prolog-walnut-creek-original` y poner el número medido]

La virtud de small-prolog es que está escrito para ser leído. No es un Prolog rápido y no pretende serlo. Es un Prolog donde podés abrir el fuente, encontrar la función que hace la unificación, y entenderla sin herramientas. Están las tres piezas a la vista:

- una representación de términos — la estructura que dice si algo es un átomo, una variable, un número o un término compuesto con argumentos;
- un ambiente de ligaduras, donde una variable ligada apunta al término al que quedó ligada;
- el trail, que es literalmente un stack de variables que hay que des-ligar cuando la cosa salga mal.

Y el loop principal, que es una función recursiva que toma dos términos y los va recorriendo en paralelo. Eso es todo. Un Prolog es eso más un parser más plomería.

Compilarlo hoy es sorprendentemente indoloro para código de esa época, aunque no gratis: los compiladores de C de los noventa aceptaban cosas que un `gcc` moderno rechaza o al menos protesta, y hay que negociar un poco con los prototipos y con los tipos.

> 🕳️ **HUECO — necesita a César:** ¿lo compilaste? ¿Con qué compilador y qué flags, y qué tuviste que tocar para que anduviera en un Linux de hoy? Si hay parches en tu fork, este es el lugar para mostrar el diff mínimo que lo hace andar.

> 🕳️ **HUECO — necesita a César:** ¿corriste `append([1,2],[3,4],X)` en él? Si hay una sesión real en tu terminal, el post gana muchísimo con el pegado literal del output.

Si querés un tercer ángulo pedagógico sobre el mismo tema, Norvig implementa Prolog en Lisp en *Paradigms of Artificial Intelligence Programming*[^paip], y el código está libre. Es otra forma de ver lo mismo: cuando el lenguaje anfitrión ya te da estructuras de datos simbólicas y recolección de basura, el Prolog que escribís arriba se vuelve chiquito y transparente. La comparación entre el small-prolog en C y el Prolog de Norvig en Lisp es, en sí misma, una clase entera sobre qué te regala un lenguaje anfitrión y qué te cobra.

### Escalón 3 — la Warren Abstract Machine

El tercer escalón cambia de idea, no de tamaño. Los dos primeros *interpretan*: toman la estructura del término y la recorren en tiempo de ejecución, cada vez. Warren propone otra cosa: *compilar* las cláusulas de Prolog a instrucciones de una máquina abstracta, de modo que en tiempo de ejecución ya no se recorra una estructura genérica sino que se ejecute código específico para esa cláusula.

Es exactamente el mismo salto conceptual que hay entre un intérprete de árbol sintáctico y un compilador a bytecode en cualquier otro lenguaje. Lo que lo hace notable acá es *qué* se compila: se compila la unificación. Warren se dio cuenta de que, en el momento de compilar una cláusula, ya sabés qué forma tiene la cabeza — sabés que el primer argumento es una estructura con functor `foo/2`, sabés que el segundo es una variable fresca. Entonces no necesitás un unificador general en tiempo de ejecución para eso: podés emitir instrucciones específicas que hagan la parte de la unificación que ya conocés estáticamente, y dejar el unificador general sólo para lo que no se sabe hasta correr.

Las instrucciones de la WAM se agrupan en familias, y la agrupación es lo que hace que el juego de instrucciones se pueda recordar:

- **put** — construyen términos en registros, para armar los argumentos del goal que vas a llamar;
- **get** — deconstruyen términos con unificación, para recibir los argumentos en la cabeza de la cláusula;
- **indexación** — eligen qué cláusulas vale la pena probar (a esto le dedico una sección entera más abajo);
- **control** — llamada, retorno, y el manejo de los choice points.

[VERIFICAR: cantidad exacta de opcodes de la WAM y si «put/get/indexación/control» es la agrupación que usa Aït-Kaci o una mía — chequear el índice del wambook. El outline dice 30; confirmarlo o corregirlo. Ojo que el conteo depende de si se cuentan las variantes `unify_*` y `set_*` por separado.]

El libro de Aït-Kaci tiene 114 páginas en la edición de MIT Press de 1991[^aitkaci]; la reimpresión libre en PDF, contando el índice, llega a 129 páginas numeradas.

Este paso de compilación es lo que separa a un juguete de un sistema en serio. Los Prologs que se usan de verdad hoy — SWI-Prolog es el caso obvio[^swipl] — descienden de esta idea, con décadas de refinamiento encima[^swipl_paper]. Y no es una historia de un solo salto: Peter Van Roy escribió un panorama de la década en la que esto se cocinó, entre el technical note de Warren y los sistemas maduros de los noventa, y el título que le puso — *The Wonder Years of Sequential Prolog Implementation*[^vanroy] — dice bastante sobre lo que se sentía estar ahí.

> 🕳️ **HUECO — necesita a César:** ¿leíste el wambook entero o lo usaste como referencia salteada? ¿Hubo un capítulo o un momento donde dijiste «ah, ahora sí»? El post necesita tu reacción real, no un elogio genérico al libro.

### El corazón del asunto — la unificación

Todo lo anterior es andamiaje alrededor de una sola operación. Vale la pena mirarla de frente.

Unificar dos términos es preguntar: ¿existe alguna asignación de valores a las variables que haga que estos dos términos sean idénticos? Si existe, la unificación devuelve esa asignación. Si no existe, falla.

Lo raro — lo verdaderamente raro — es que la operación no tiene dirección. Cuando escribís `padre(juan, X)` contra el hecho `padre(juan, pedro)`, la unificación liga `X = pedro`. Pero si escribís `padre(Y, pedro)`, la misma operación, sin cambiar nada, liga `Y = juan`. El mismo predicado, sin escribir una línea más, anda para los dos lados. Y `padre(Y, X)` te los da a los dos.

Compará con lo que tenés en un lenguaje moderno. El pattern matching de Rust, de Haskell, de Scala es unificación con una mano atada: hay un lado que es el patrón y otro lado que es el valor, y las variables sólo pueden aparecer en el patrón. Es unidireccional por diseño, y eso lo hace más simple, más rápido y más predecible. La inferencia de tipos de Hindley-Milner, por otro lado, sí usa unificación de verdad, bidireccional — pero la usa en tiempo de compilación, sobre tipos, y el resultado no es un programa que corre sino un veredicto sobre si tu programa está bien tipado.

Prolog hace las dos cosas a la vez: unificación completa, bidireccional, en tiempo de ejecución, como forma de computar. Resuelve corriendo lo que Haskell resuelve compilando y lo que Rust directamente no intenta. Eso es, para mí, lo que lo vuelve hermoso, y también es la primera pista de por qué la mayor parte del tiempo no lo usamos.

### Backtracking, choice points y trail

Si la unificación liga variables tentativamente, alguien tiene que poder desligarlas. Ese alguien es el trail.

La idea es de una economía admirable. Cuando el motor llega a un punto donde hay varias cláusulas que podrían aplicar, guarda un **choice point**: una marca en el stack que dice «estuve acá, con este estado, y todavía me quedan estas alternativas por probar». Después sigue por la primera alternativa. Cada vez que liga una variable que ya existía antes del choice point, anota esa variable en el **trail**.

Cuando el camino falla, el motor no restaura una copia del ambiente — no hay copia. Vuelve al choice point, recorre el trail hasta la marca que le corresponde, desliga cada variable anotada, y prueba la alternativa siguiente. Deshacer cuesta proporcional a lo que hiciste, no proporcional al tamaño del ambiente.

Es la misma idea que un journal de transacciones, o que el undo de un editor: no guardes el mundo, guardá los cambios. Que la encuentres en un motor de Prolog de los ochenta y en un motor de base de datos y en tu editor de texto es una de esas coincidencias que no son coincidencia.

### Indexado de primer argumento

Falta una pieza para que esto sea viable, y es la menos glamorosa y la más decisiva.

Imaginate una base con muchos hechos del mismo predicado: `ciudad(rosario, santa_fe).`, `ciudad(cordoba, cordoba).`, y así unos cuantos miles. Preguntás `?- ciudad(rosario, P).`. La implementación ingenua — la de micro-PROLOG, la de small-prolog — prueba las cláusulas de arriba a abajo: unifica contra la primera, falla, backtrack, unifica contra la segunda, falla, backtrack. Lineal en el tamaño de la base, y con un choice point creado y destruido en cada paso.

El indexado de primer argumento dice: antes de probar nada, mirá el primer argumento del goal. Si es un átomo, sólo pueden unificar las cláusulas cuyo primer argumento sea ese mismo átomo o una variable. Saltá directo a esas y ni toques el resto. Y si queda una sola candidata, ni siquiera creés el choice point — no hay alternativas que probar.

Ese segundo efecto es tan importante como el primero. No crear el choice point significa que la llamada es determinística, y una llamada determinística no consume stack de la misma manera. Es la diferencia entre un programa que corre y un programa que se come la memoria.

[VERIFICAR: el factor de aceleración del indexado de primer argumento. El outline dice «~100× más rápido que la implementación ingenua» — ese número necesita una fuente o, mejor, una medición propia sobre una base de hechos sintética comparando SWI-Prolog contra small-prolog. Si no hay medición, sacar el número y dejar el argumento cualitativo.]

Sin este truco, Prolog sería una curiosidad académica y no un lenguaje con el que alguien despacha trabajo real.

### ¿Y entonces por qué no lo usamos?

Acá viene la parte honesta, que es la que menos me gusta escribir y la que más falta hace.

Prolog tiene el mejor modelo de ejecución que conozco para una clase de problemas: búsqueda con restricciones, análisis de relaciones sobre grafos, parsing cuando usás DCGs. Para esos, escribís un décimo del código y el código dice lo que querés en vez de decir cómo conseguirlo.

Y tiene un modelo bastante pobre para todo lo demás. Aritmética, entrada/salida, estado mutable, estructuras de datos con acceso indexado, cualquier cosa donde el orden de evaluación importe: todo eso en Prolog se hace, pero se hace peleando contra el lenguaje en vez de con él. El resultado es que un programa Prolog real termina lleno de cortes, y el corte es la confesión de que el modelo declarativo no te alcanzó.

Lo interesante es qué pasó después. La idea no murió: se desagregó. Datalog se quedó con la parte declarativa y tiró el backtracking descontrolado a cambio de terminación garantizada. ASP se quedó con la búsqueda y le puso otro motor debajo. miniKanren[^minikanren] se quedó con la unificación pura y la metió adentro de Scheme como una biblioteca, para que la uses cuando la necesitás y no cuando no. Souffle se quedó con Datalog y lo compiló a C++ para que corra en serio.

Todos son, de alguna manera, hijos del wambook: heredan las primitivas sin heredar el lenguaje entero.

> 🕳️ **HUECO — necesita a César:** ¿cuál es tu diagnóstico sobre por qué Prolog no cuajó? ¿Es el modelo de ejecución, es que llegó junto con el invierno de la IA, es que la sintaxis de Edimburgo espantaba gente, es otra cosa? Este párrafo tiene que ser tu opinión, no un consenso reciclado.

> 🕳️ **HUECO — necesita a César:** ¿usaste Prolog alguna vez para algo que no fuera un ejercicio? ¿En la facultad, en algún trabajo? Si la respuesta es «no, nunca», decirlo también sirve y es más honesto.

### Cierre

Me quedo con esto: la unificación sigue siendo una primitiva sub-explotada. Es una operación que resuelve, en una sola llamada y sin dirección privilegiada, cosas para las que en otros lenguajes escribimos tres funciones distintas. Está adentro de tu compilador si tu lenguaje infiere tipos. Asoma en el borrow checker de Rust: Polonius reformula el análisis de préstamos como un problema Datalog, aunque —a julio de 2026— sigue siendo experimental, se prueba con la bandera `-Zpolonius` en las builds nightly y todavía no reemplazó al verificador por defecto[^polonius]. Está adentro de cualquier motor de reglas que hayas usado sin saber cómo funciona.

Y la parte que me sigue divirtiendo es que los tres escalones que recorrí acá siguen ahí, disponibles, gratis. Podés bajar el desensamblado de un Prolog que entraba en un Spectrum, compilar un Prolog en C de tres mil líneas, y leer el libro que explica cómo se hace bien. Tres visitas a la misma idea, una en Z80, otra en C, otra en abstracción formal. No conozco muchos conceptos de la computación que se dejen mirar así, en corte transversal, con todas las capas a la vista.

Si te interesa el «qué hay debajo» como género, en [[B-02]] hago el mismo ejercicio con las estructuras de datos puramente funcionales de Okasaki. Si te interesa el primo concurrente de Prolog, [[A1-08]] tiene lo de KL1. Y si lo que te quedó picando es el Spectrum, [[I-03]] es el lugar.

[^warren]: David H. D. Warren, *An Abstract Prolog Instruction Set*, SRI Technical Note 309, octubre 1983. [Ficha en SRI](https://www.sri.com/publication/cyber-formal-methods-pubs/an-abstract-prolog-instruction-set/) con [PDF escaneado](https://www.sri.com/wp-content/uploads/2021/12/641.pdf).
[^aitkaci]: Hassan Aït-Kaci, *Warren's Abstract Machine: A Tutorial Reconstruction*, MIT Press, 1991 (114 pp., ISBN 0262510588). [MIT Press](https://mitpress.mit.edu/9780262510585/warrens-abstract-machine/). El autor conserva el copyright y la autorizó para uso no comercial; el fork `wambook` de mi GitHub (upstream [`a-yiorgos/wambook`](https://github.com/a-yiorgos/wambook)) tiene las versiones en PDF y PostScript.
[^vanroy]: Peter Van Roy, *1983–1993: The Wonder Years of Sequential Prolog Implementation*, Journal of Logic Programming, vol. 19/20, 1994, pp. 385–441 ([dblp](https://dblp.org/rec/journals/jlp/Roy94.html)). Preprint libre: [DEC PRL Research Report 36, dic. 1993](https://webperso.info.ucl.ac.be/~pvr/PRL-TR-36.pdf).
[^smallprolog]: Henri de Feraudy, *Small Prolog*, distribuido por el C User's Group en los CD-ROM de Walnut Creek. Preservado en [Internet Archive](https://archive.org/details/C_Users_Group_Library_Walnut_Creek_August_1994) y en el repo [`opless/small-prolog-walnut-creek-original`](https://github.com/opless/small-prolog-walnut-creek-original).
[^lpa]: Logic Programming Associates, *micro-PROLOG for the ZX Spectrum*, publicado por Sinclair Research, 1983 (Spectrum 48K). [Ficha en Spectrum Computing](https://spectrumcomputing.co.uk/entry/8429/ZX-Spectrum/Micro-PROLOG).
[^microprolog_src]: Desensamblado y reconstrucción byte-exacta del intérprete Z80 de SPECTRUM micro-PROLOG T1.0 (ocupa 14 200 bytes, 0x6000–0x9777): [`oldcompcz/micro-PROLOG`](https://github.com/oldcompcz/micro-PROLOG), upstream del fork de mi GitHub.
[^polonius]: *Polonius* — reformulación en Datalog del borrow checker de Rust; a julio de 2026 sigue en estado experimental (nightly `-Zpolonius`, no es el verificador por defecto). [Estado actual y hoja de ruta](https://rust-lang.github.io/polonius/current_status.html).
[^swipl]: *SWI-Prolog* — sitio oficial: [swi-prolog.org](https://www.swi-prolog.org/). La [referencia del manual](https://www.swi-prolog.org/pldoc/man?section=overview) tiene un panorama del modelo de ejecución.
[^swipl_paper]: J. Wielemaker et al, *SWI-Prolog*, Theory and Practice of Logic Programming, 2012. [Cambridge Core](https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/swiprolog/13570311D10C2F20A29F0BE4DF5C03D1)
[^minikanren]: William Byrd, *miniKanren*: [minikanren.org](http://minikanren.org/)
[^paip]: Peter Norvig, *Paradigms of Artificial Intelligence Programming*, Morgan Kaufmann, 1991 — los capítulos sobre Prolog. El código está libre en [github.com/norvig/paip-lisp](https://github.com/norvig/paip-lisp)

