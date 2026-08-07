### D-06 — El paper de Sutherland sobre constraints (MIT 1963): el ancestro del álgebra de restricciones

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `sutherland-constraint-paper-1963`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-sutherland-constraint-paper-1963/index.md`
- **Serie:** pioneros
- **Cross-links:** [[D-02]] (Sketchpad), [[A1-10]] (Prolog), [[B-08]] (WAM)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1800-2200 palabras (deep-dive medio) — elegido al expandir: el tema pide leer un capítulo de tesis y proyectarlo a herramientas modernas, no alcanza con una story de 800.

**Concepto:** *The Definition and Implementation of a Computer Programming Language Based on Constraints* (Ivan Sutherland, MIT PhD thesis 1963 — la misma tesis que produjo Sketchpad) tiene un capítulo dedicado a un mini-lenguaje basado en restricciones que es el ancestro directo de SAT solvers, álgebra de restricciones, Prolog, y los modernos constraint propagators. El post discute ese capítulo (a menudo eclipsado por el trabajo gráfico de Sketchpad) y muestra qué se conserva en herramientas modernas.

**Hook:** Sketchpad es famoso por la parte gráfica. Pero la tesis de Sutherland del 63 también define un mini-lenguaje basado en restricciones. Es básicamente Prolog 9 años antes de Prolog. Vamos a leerlo.

**Outline:**

1. **Hook** — Sketchpad es famoso por el lápiz óptico y las líneas en la pantalla. Pero adentro de la misma tesis hay un motor de restricciones. Vamos a leer esa parte.
2. **Advertencia bibliográfica** — el título que circula pegado a este tema (*The Definition and Implementation of a Computer Programming Language Based on Constraints*) **no** es el de la tesis de Sutherland según [[tr-13]]. Aclarar cuál es cuál antes de seguir, o el post arranca citando mal.
3. **Qué es una restricción en Sketchpad** — la relación se declara, no se ejecuta; el dibujo se corrige solo. El salto conceptual respecto de dibujar coordenadas a mano.
4. **El mini-lenguaje** — cómo se definen restricciones nuevas, qué es una restricción compuesta, en qué sentido eso es un lenguaje y no una biblioteca de casos especiales.
5. **Cómo se satisfacen** — propagación de valores conocidos primero, relajación numérica cuando la propagación no alcanza. El método barato antes que el método general.
6. **Qué es y qué no es «Prolog antes de Prolog»** — el parecido real (declarar relaciones, dejar que la máquina busque la asignación) y la diferencia real (aritmética numérica vs unificación simbólica y backtracking). Cross-links a [[A1-10]] y [[B-08]].
7. **Qué sobrevive hoy** — solvers de layout, hojas de cálculo, propagadores de constraints, SAT/SMT. Dónde se ve el linaje y dónde es convergencia y no descendencia.
8. **Por qué se eclipsó** — la demo gráfica se ve, el motor de restricciones no.
9. **Cierre** — leer las tesis viejas por el capítulo que nadie cita.

**Bibliografía:**
- **[[tr-13]]** — Ivan E. Sutherland, *Sketchpad: A Man-Machine Graphical Communication System*, MIT PhD thesis, enero de 1963. Reeditada como University of Cambridge Technical Report UCAM-CL-TR-574 (sept. 2003, prefacio de Alan Blackwell y Kerry Rodden): [PDF](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf) — fetch verificado 2026-07-16 (resuelve, 3,9 MB). El capítulo VIII «Constraint Satisfaction» y el Apéndice A «Constraint Descriptions» son las secciones que sostienen este post. **estable**.
- Registro canónico de la tesis en el repositorio del MIT: [hdl.handle.net/1721.1/14979](https://hdl.handle.net/1721.1/14979) — *Sketchpad, a man-machine graphical communication system*, Sutherland, MIT Dept. of Electrical Engineering, 1963 (confirmado por búsqueda; el handle `1721.1/6933` de la nota vieja **era incorrecto**). DSpace bloquea el fetch automatizado (HTTP 405), no se pudo abrir por WebFetch. **estable**.
- Versión de conferencia (más citada, más corta): Ivan E. Sutherland, *Sketchpad: A Man-Machine Graphical Communication System*, AFIPS Spring Joint Computer Conference, vol. 23 (1963), p. 329 y ss. DOI canónico [10.1145/1461551.1461591](https://doi.org/10.1145/1461551.1461591) (verificado vía api.crossref.org, 2026-07-16; ACM DL, con paywall). Espejo libre del PDF: [cl.cam.ac.uk/~pr10/iui/sutherland63.pdf](https://www.cl.cam.ac.uk/~pr10/iui/sutherland63.pdf). DOI **estable**; espejo **frágil**.
- Guy L. Steele Jr., *The Definition and Implementation of a Computer Programming Language Based on Constraints*, tesis doctoral MIT, 1980 (lenguaje CONSTRAINTS sobre Scheme) — la tesis cuyo título se había confundido con la de Sutherland. [hdl.handle.net/1721.1/15890](https://hdl.handle.net/1721.1/15890); ficha en [ACM DL 10.5555/889490](https://dl.acm.org/doi/10.5555/889490). **estable**.
- Linaje a la POO (cross-links [[D-02]] y [[tr-01]]): el prefacio de Blackwell y Rodden en [[tr-13]] documenta, citando a Alan Kay, *The Early History of Smalltalk* (ACM SIGPLAN Notices 28(3):69–95, 1993), que la génesis de Smalltalk está en la aparición simultánea, sobre el escritorio de Kay, de una cinta de Simula y una copia de la tesis de Sketchpad. **estable**.

**Imágenes:** _a definir_

**Tags propuestos:** `['Sutherland','constraints','Sketchpad','historia CS','MIT','restricciones']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09; expandido a outline + prosa el 2026-07-15 (Claude, sin revisar por César). El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch: tesis en el PDF de Cambridge UCAM-CL-TR-574, DOI del paper AFIPS verificado vía api.crossref.org, tesis de Steele 1980 identificada) y se resolvieron 7 de 9 marcadores [VERIFICAR:] (quedan 2 abiertos: el año de Prolog —remite a [[A1-10]]— y la evidencia documentada de influencia directa sobre constraint programming, que las fuentes obtenidas no acreditan).

Lo que quedó escrito: el arco completo (hook → advertencia bibliográfica → qué es una restricción → el mini-lenguaje → cómo se satisface → «Prolog antes de Prolog», sí y no → linaje moderno → por qué se eclipsó → cierre), ~1950 palabras.

**Bloqueante antes de publicar — conflicto en el propio draft.** El **Concepto:** atribuye a la tesis de Sutherland de 1963 el título *The Definition and Implementation of a Computer Programming Language Based on Constraints*. La bibliografía del mismo draft ([[tr-13]]) dice que la tesis de Sutherland de 1963 se titula *Sketchpad: A Man-Machine Graphical Communication System*. Son dos títulos distintos para la misma cita, así que al menos uno está mal, y el handle `dspace.mit.edu/handle/1721.1/6933` no está verificado a cuál de los dos apunta. La prosa está escrita de modo de no depender de esa atribución (trata «la parte de restricciones de la tesis de Sketchpad») y deja el conflicto marcado inline, pero **hay que resolverlo antes de publicar**: si el título del Concepto corresponde a otra tesis de otro autor y otro año, el post cambia de eje y el Hook («Prolog 9 años antes de Prolog») cambia de aritmética.

**Resuelto parcialmente (2026-07-16):** el título *The Definition and Implementation of a Computer Programming Language Based on Constraints* **es** de otra tesis, de otro autor y otro año — Guy L. Steele Jr., MIT, 1980. El **Concepto:** de arriba, entonces, lo atribuye mal a Sutherland/1963; corregir esa atribución es tarea de César (no toco el Concepto). La prosa del cuerpo ya quedó reescrita con la atribución correcta y no depende del error. El Hook y su «nueve años antes» siguen apoyados en la tesis de Sketchpad (1963), que es y sigue siendo el eje del post.

Lo que quedó como hueco: todo el contenido específico del capítulo de restricciones está marcado con `[VERIFICAR:]` contra el PDF de [[tr-13]] — la bibliografía disponible acredita que la tesis existe y dónde está, no qué dice cada sección. Y quedan huecos `🕳️` para la voz de César: si leyó la tesis y cuándo, su experiencia con solvers de restricciones en herramientas reales, y su opinión sobre el cierre. Faltan también **Imágenes:** (siguen `_a definir_`).

---

## Borrador de prosa

De Sketchpad todo el mundo se acuerda de lo mismo: un tipo joven sentado frente a una pantalla circular, un lápiz óptico en la mano, líneas que aparecen en el vidrio. Es la imagen fundacional de la computación gráfica interactiva, y está en el video del demo, que se puede ver todavía hoy.[^tr13] Es una imagen buenísima. También es una trampa, porque lo que se ve es lo menos interesante que pasa ahí adentro.

Lo interesante es que Sketchpad no dibuja lo que vos le pedís. Dibuja lo que vos le pedís **corregido para que cumpla las reglas que le declaraste antes**. Vos marcás dos líneas y decís «estas dos son perpendiculares»; después arrastrás una y la otra se acomoda sola. No escribiste el código que la acomoda. Declaraste una relación y el sistema se hizo cargo de sostenerla. Eso, en 1963, no es una función de dibujo: es un motor de restricciones, y vive en la misma tesis.[^sketchpad] Vamos a leer esa parte.

### Antes de seguir: cuál tesis estamos leyendo

Acá tengo que frenar y hacer una aclaración incómoda, porque este tema arrastra una confusión bibliográfica y no quiero propagarla.

El título que circula pegado a «lenguaje basado en restricciones» es *The Definition and Implementation of a Computer Programming Language Based on Constraints*. La tesis de Sutherland de 1963, según la referencia que yo tengo verificada, se titula *Sketchpad: A Man-Machine Graphical Communication System*.[^tr13] Son dos títulos distintos. No son variantes del mismo: uno habla de comunicación gráfica hombre-máquina y el otro de definir e implementar un lenguaje de programación.

Resuelto (2026-07-16): *The Definition and Implementation of a Computer Programming Language Based on Constraints* es una tesis **distinta** —la opción (b)—: es la tesis doctoral de **Guy L. Steele Jr.** en el MIT, de **1980**, que define el lenguaje CONSTRAINTS sobre Scheme.[^steele] No tiene nada que ver con la tesis de Sutherland de 1963, salvo el tema. Y el handle que yo tenía anotado (`1721.1/6933`) tampoco apuntaba a Sutherland: el registro correcto de la tesis de Sketchpad en el repositorio del MIT es `1721.1/14979`.[^sketchpad] La confusión era, entonces, juntar dos tesis del MIT sobre restricciones separadas por diecisiete años y por autor.

Lo digo así de crudo porque es exactamente el tipo de error que se reproduce solo: alguien lo escribe con seguridad, otro lo cita, y a los diez años es «sabido». Con el título ya devuelto a su dueño —Steele, 1980—, en este post hablo de **la parte de restricciones de la tesis de Sketchpad** (Sutherland, 1963), que es de lo que trata su capítulo VIII.

### Qué es una restricción acá

La idea es más vieja que la computación y más simple de lo que suena. Una restricción es una afirmación sobre un dibujo que tiene que seguir siendo verdadera: este punto está sobre esta línea, estos dos segmentos miden lo mismo, este ángulo es recto, estas dos líneas son paralelas.

Lo raro —lo genuinamente nuevo— es el modo verbal. En el paradigma que todos aprendimos, vos escribís el procedimiento: calculá esta coordenada, después esta otra, después redibujá. La geometría del resultado es una consecuencia accidental del orden en que hiciste las cuentas. Si querés que el ángulo siga siendo recto después de mover algo, es problema tuyo: escribís el código que lo mantiene, y si te olvidás de un caso, el dibujo miente.

En Sketchpad das vuelta la carga de la prueba. Vos declarás la relación una vez. Después movés lo que quieras, y **la relación es responsabilidad de la máquina**. Eso ya no es dibujar: es afirmar. El dibujo pasa a ser la solución de un sistema de afirmaciones, y el lápiz óptico pasa a ser un modo de perturbar el sistema para ver cómo se reacomoda.

Dicho así en 2026 suena a poco, porque hoy convivimos con esto sin registrarlo. Pero pensá qué máquina había abajo: Sketchpad corría en el **TX-2** del MIT Lincoln Laboratory, la máquina experimental de Wesley Clark.[^tr13] Sutherland menciona que «la gran capacidad de almacenamiento del TX-2» le permitió no obsesionarse con ahorrar espacio en la estructura de anillos (la tesis lo dice cualitativamente; en los pasajes que revisé no da una cifra exacta de memoria). Sostener un sistema de relaciones geométricas en tiempo interactivo, con eso, es una decisión de diseño agresiva, no una comodidad.

### El mini-lenguaje

Acá está el punto que el video del demo no muestra y que es la razón de este post: las restricciones de Sketchpad no son una lista cerrada de casos especiales cableados en el programa.

Si fueran eso —«el sistema sabe hacer perpendicular, paralelo e igual longitud»— sería una biblioteca de funciones de dibujo, prolija pero anecdótica. Lo que la vuelve interesante es que hay un mecanismo para **definir restricciones nuevas** y para **componerlas**: armar una restricción compuesta a partir de otras y usarla como si fuera primitiva. En el momento en que el usuario puede extender el vocabulario de relaciones sin tocar el programa, eso deja de ser una biblioteca y empieza a ser un lenguaje. Tiene primitivas, tiene una regla de composición y tiene abstracción: nombrar una composición y olvidarse de cómo estaba hecha.

En la tesis esto tiene dos niveles. Componer restricciones existentes en una compuesta y reusarla como si fuera primitiva es lo que Sutherland llama *definition copying*: se arma, por ejemplo, «estas dos líneas paralelas y de igual longitud» y se aplica de un botonazo; «el número de operaciones que se pueden definir a partir de las restricciones básicas es casi ilimitado», y se hace desde la interfaz, sin programar.[^tr13] Agregar un tipo de restricción **atómico** nuevo, en cambio, sí requiere código: hay que escribir una subrutina que compute el *error* que introduce esa restricción. Sutherland cuenta que, una vez que definió las restricciones en términos de ese error, «es tan fácil programar tipos de restricción nuevos» que amplió el conjunto atómico de cinco a diecisiete en unos dos días.[^tr13]

Las restricciones atómicas de Sketchpad son **diecisiete** (arrancó con cinco y creció a diecisiete, listadas en el Apéndice A de la tesis): hacer líneas verticales, horizontales, paralelas o perpendiculares; forzar puntos a estar sobre líneas o círculos; hacer símbolos verticales, alineados uno sobre otro o de igual tamaño; fijar tamaños (de 1/32 a 1 pulgada); y relacionar símbolos con puntos y líneas.[^tr13]

Eso también explica por qué el sistema de instancias y «masters» de Sketchpad —lo que hoy llamaríamos definir un símbolo una vez y usarlo en muchos lugares— y el sistema de restricciones son la misma idea vista dos veces: definir algo una vez, nombrarlo, y que las copias se mantengan coherentes solas. Es herencia y es propagación. Por eso Sketchpad aparece citado en genealogías de cosas tan distintas como el diseño asistido por computadora y la programación orientada a objetos. Sobre esa otra rama hablo en [[D-02]]. Confirmado en la tesis: si se cambia el dibujo *master* —el hexágono base, el símbolo de transistor—, «el cambio aparece de inmediato en todos» sus instances sin más trabajo; y el prefacio de la edición de Cambridge señala que esa herencia basada en clase e instancia de Sketchpad «precede a Simula en varios años», aunque Sutherland no la llamara objetos.[^tr13]

### Cómo se satisface: primero barato, después general

Un sistema de restricciones no sirve de nada si no lo podés resolver. Y resolver un sistema de relaciones geométricas arbitrarias, en el caso general, es caro.

La estrategia de Sutherland es la que uno reinventa cada vez que se topa con este problema, y que sigue siendo correcta: **dos métodos, el barato primero**.

El primero es propagación. Si de una restricción y de los valores que ya conocés se deduce directamente el valor que falta, lo escribís y seguís. Es el método de la hoja de cálculo: A1 cambió, B1 depende de A1, recalculo B1, sigo por las dependencias. Es rapidísimo y no requiere inteligencia. El problema es que sólo funciona mientras el grafo de dependencias sea lo bastante manso: en cuanto hay un ciclo —dos restricciones que se determinan mutuamente— la propagación se queda mirando el techo.

El segundo, para cuando la propagación no alcanza, es relajación numérica: en vez de despejar, medís cuánto está violada cada restricción, empujás los valores en la dirección que reduce el error, y repetís hasta que el error es lo bastante chico. No despeja: converge. Es más lento y más general, y es lo que salva los casos con ciclos.

Los nombres de Sutherland: el método barato es el *one pass method*, que él también describe como una técnica de «maze-solving» —resolver el laberinto de restricciones detectando qué variables quedan «libres», con una difusión análoga al algoritmo de Moore para el camino más corto—; el general es *relaxation*.[^tr13] Sketchpad intenta primero hallar un orden en que reevaluar las variables para satisfacer todo en una sola pasada; cuando ese orden no existe —sistemas redundantes o sobredeterminados, como el reticulado de un puente—, cae a la relajación, que define el error de cada restricción como una «energía» y la reduce monótonamente (es estable, pero puede no dar una solución correcta en tiempo finito). Para los casos redundantes usa una macro aritmética, SOLVE, que busca el ajuste de mínimos cuadrados.[^tr13]

Esa arquitectura —intentá el camino barato y determinístico, caé al método general y numérico sólo cuando haga falta— es hoy el diseño estándar de cualquier motor de restricciones serio. No es un detalle de implementación de 1963: es la forma del problema.

### «Prolog nueve años antes de Prolog»: sí y no

Es una frase linda y por eso hay que desarmarla.

Lo que sí. El gesto es el mismo, y es el gesto que define la programación declarativa: vos describís **qué relaciones tienen que valer** y el sistema se encarga de encontrar una asignación que las cumpla. No hay orden de ejecución en tu cabeza. Escribís hechos sobre el mundo, no pasos. En eso, Sketchpad y Prolog son parientes de sangre, y Sketchpad llega antes. [VERIFICAR: el año de Prolog y la aritmética del «nueve años antes» del hook — no lo doy por sabido acá; ver [[A1-10]].]

Lo que no. Prolog resuelve sobre términos simbólicos, con unificación y backtracking cronológico: si una rama falla, deshace y prueba otra. Sketchpad resuelve sobre números, con propagación y relajación: si no converge, no hay «otra rama», hay error numérico. Son máquinas distintas resolviendo problemas distintos. Llamar a Sketchpad «Prolog temprano» comprime la historia hasta romperla, y encima le hace un flaco favor a Sutherland, porque lo interesante no es que se haya anticipado a Prolog: es que llegó a la misma **postura** —declarar en vez de ordenar— desde un problema completamente distinto, el de dibujar. La convergencia es más interesante que la primogenitura. De la máquina de Prolog propiamente dicha hablo en [[B-08]].

> 🕳️ **HUECO — necesita a César:** ¿leíste la tesis de Sutherland en algún momento, o la conocés por el video del demo y por citas de terceros? Si la leíste, ¿cuándo y por qué motivo caíste ahí?

### Qué sobrevive

El linaje honesto es este: cada vez que declarás una relación y dejás que otro la sostenga, estás en esta tradición. Los motores de layout que resuelven «este botón está a 8 píxeles del borde y centrado respecto de aquel». Las hojas de cálculo, que son propagación pura con una interfaz que la disimula. Los solvers de restricciones sobre dominios finitos. Los SAT y SMT que hoy son la maquinaria abajo de la verificación formal y de medio compilador optimizante.

Ahora, honestidad histórica: eso es **linaje conceptual**, no necesariamente descendencia. Que Sketchpad haya llegado primero no prueba que los demás lo hayan copiado. [VERIFICAR: si hay evidencia documentada de influencia directa de Sketchpad sobre trabajos posteriores de constraint programming — no afirmarlo sin una cita concreta; la bibliografía actual de este draft no la tiene.] La versión sobria es la que puedo defender: la tesis del 63 planteó el problema completo —declarar relaciones, componerlas, satisfacerlas con un método barato y uno general— y lo resolvió lo bastante bien como para que anduviera en tiempo real en una máquina de 1963. Que después la disciplina haya vuelto una y otra vez a las mismas decisiones dice algo sobre las decisiones.

> 🕳️ **HUECO — necesita a César:** ¿te tocó pelearte con algún motor de restricciones en herramientas reales — layout de UI, un solver, dependencias que se resuelven solas — y sentir que estabas del lado del que declara y no del que ordena? Una o dos frases y sirve como aterrizaje del post.

### Por qué se eclipsó

Por la razón más tonta y más humana: la demo gráfica se ve y el motor de restricciones no.

Un video de líneas que aparecen bajo un lápiz óptico se explica solo en cuatro segundos. «Hay un mecanismo para definir relaciones nuevas por composición y satisfacerlas por propagación con caída a relajación» no entra en un video: entra en un capítulo que hay que sentarse a leer. La historia de la computación se transmite mucho más por imágenes que por lectura, y en esa competencia el lápiz óptico ganó por afano.

Y ahí está la moraleja que me llevo, que es más sobre nosotros que sobre Sutherland: las tesis viejas conviene leerlas por el capítulo que nadie cita. La parte famosa ya la procesó todo el mundo y no queda nada para vos. La parte que quedó tapada por la parte famosa suele ser donde está el trabajo pesado — y a veces, como acá, es donde estaba la idea que iba a tardar décadas en volver.

> 🕳️ **HUECO — necesita a César:** el cierre pide tu opinión, no la mía. ¿Cuál es tu regla propia para leer papers viejos — vas al capítulo que nadie cita, o pensás que la fama del capítulo famoso suele estar bien puesta?

[^sketchpad]: Ivan E. Sutherland, *Sketchpad, A Man-Machine Graphical Communication System*, tesis doctoral, Dept. of Electrical Engineering, MIT, enero de 1963. Registro canónico en el repositorio del MIT: [hdl.handle.net/1721.1/14979](https://hdl.handle.net/1721.1/14979) (el handle `1721.1/6933` que figuraba en la nota vieja era incorrecto). Texto completo reeditado como University of Cambridge Technical Report UCAM-CL-TR-574 (2003) — ver [[tr-13]].
[^steele]: Guy L. Steele Jr., *The Definition and Implementation of a Computer Programming Language Based on Constraints*, tesis doctoral, MIT, 1980 — lenguaje CONSTRAINTS construido sobre Scheme. Registro en el repositorio del MIT: [hdl.handle.net/1721.1/15890](https://hdl.handle.net/1721.1/15890); ficha en [ACM DL 10.5555/889490](https://dl.acm.org/doi/10.5555/889490).
[^tr13]: Ivan Sutherland, *Sketchpad: A Man-Machine Graphical Communication System*, MIT PhD thesis, 1963. [PDF en University of Cambridge](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf), [vídeo del demo](https://www.youtube.com/watch?v=mOZqRJzE8xg).
