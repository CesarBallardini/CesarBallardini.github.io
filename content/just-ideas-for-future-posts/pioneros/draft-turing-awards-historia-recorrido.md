### D-05 — Turing Awards: un recorrido por los ganadores que cambiaron el mundo

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `turing-awards-historia-recorrido`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-turing-awards-historia-recorrido/index.md`
- **Serie:** pioneros
- **Cross-links:** [[D-01]] (Engelbart), [[D-02]] (Sketchpad/Sutherland), [[D-03]] (Turing)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** long (2200-3000 palabras) — elegido acá: un recorrido por ocho premiados no entra cómodo en el rango medium.

**Concepto:** El premio Turing (ACM, desde 1966) es el "Nobel de Computer Science". Los ganadores son una guía a la historia de la disciplina: Hamming, Knuth, Dijkstra, Hoare, Cook, Karp, Liskov, Wirth, Bachman, Lamport, Hopcroft/Tarjan, etc. El post es un recorrido (selectivo, no exhaustivo) por los premios que más impacto tuvieron y por qué.

**Hook:** el Nobel de la computación se llama Turing Award. Hopcroft y Tarjan lo ganaron por estructuras de datos. Hamming lo ganó por códigos correctores. Liskov lo ganó por OOP en serio. Acá hay 8 que valen la pena conocer.

**Outline:**
1. Qué es el premio Turing, quién lo da, y por qué la lista de ganadores es el índice de la disciplina que nadie escribió a propósito.
2. La regla del recorrido: selectivo, no exhaustivo. Ocho entradas, un criterio explícito (premios que cambiaron lo que se podía *pensar*, no sólo lo que se podía construir).
3. Hamming — el ruido, y la idea de que un dato puede repararse a sí mismo.
4. Dijkstra — programar como disciplina intelectual, con costo moral.
5. Knuth — la algoritmia como ciencia medible, y como libro que nunca termina.
6. Hoare — la corrección demostrable, y el autor arrepentido de su propio invento.
7. Cook y Karp — P vs NP: el premio por descubrir que hay cosas que probablemente no podemos.
8. Hopcroft y Tarjan — las estructuras de datos ascendidas a objeto de estudio.
9. Liskov — abstracción de datos: OOP en serio, antes de que OOP fuera marketing.
10. Lamport — el tiempo, el orden y por qué los sistemas distribuidos son otro planeta.
11. Los que quedaron afuera de los ocho (Wirth, Bachman) y por qué la lista completa vale más que cualquier recorte.
12. Cómo leer las Turing Lectures — la recomendación práctica: el premio viene con una conferencia, y ahí está lo bueno.
13. Cierre.

**Bibliografía:** _(reforzada 2026-07-16 — todas las URL verificadas por fetch; años y textos de citation tomados verbatim de las páginas de perfil oficiales)_

Fuentes de catálogo:
- [ACM A.M. Turing Award](https://amturing.acm.org/) — sitio oficial: lista completa, citation, biografías y enlaces a las conferencias. Estable.
- [ACM Turing Award Lectures](https://amturing.acm.org/lectures.cfm) — listado oficial de las Turing Lectures con título y DOI en la ACM Digital Library (prefijo `10.1145/1283920.*`). Acceso abierto de los PDF en dl.acm.org no verificado. Estable.
- [Turing Award](https://en.wikipedia.org/wiki/Turing_Award) — Wikipedia: tabla cronológica completa, sólo como índice. Estable.

Permalinks por ganador (formato `award_winners/<apellido>_<id>.cfm`, id confirmado uno por uno):
- Perlis (1966, primer premiado): https://amturing.acm.org/award_winners/perlis_0132439.cfm
- Hamming (1968): https://amturing.acm.org/award_winners/hamming_1000652.cfm
- Dijkstra (1972): https://amturing.acm.org/award_winners/dijkstra_1053701.cfm
- Bachman (1973): https://amturing.acm.org/award_winners/bachman_9385610.cfm
- Knuth (1974): https://amturing.acm.org/award_winners/knuth_1013846.cfm
- Hoare (1980): https://amturing.acm.org/award_winners/hoare_4622167.cfm
- Cook (1982): https://amturing.acm.org/award_winners/cook_n991950.cfm
- Wirth (1984): https://amturing.acm.org/award_winners/wirth_1025774.cfm
- Karp (1985): https://amturing.acm.org/award_winners/karp_3256708.cfm
- Hopcroft (1986, compartido): https://amturing.acm.org/award_winners/hopcroft_1053917.cfm
- Tarjan (1986, compartido): https://amturing.acm.org/award_winners/tarjan_1092048.cfm
- Liskov (2008): https://amturing.acm.org/award_winners/liskov_1108679.cfm
- Lamport (2013): https://amturing.acm.org/award_winners/lamport_1205376.cfm

Fuentes complementarias verificadas:
- [Knuth, *The Art of Computer Programming* (página oficial)](https://www-cs-faculty.stanford.edu/~knuth/taocp.html) ([[tr-20]]) — estado de los volúmenes. Estable.
- [P vs NP — Clay Mathematics Institute](https://www.claymath.org/millennium/p-vs-np/) — sigue abierto. Estable.
- [Tony Hoare, *Null References: The Billion Dollar Mistake* (InfoQ, QCon London 2009)](https://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare/) — frágil (grabación de conferencia); agregar respaldo Wayback antes de publicar.

**Imágenes:** _a definir_

**Tags propuestos:** `['Turing Award','ACM','historia CS','premios','Hamming','Knuth','Dijkstra']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09; **outline de 13 puntos construido y prosa completa escrita** el 2026-07-15 (~2400 palabras). El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 23 de 26 marcadores [VERIFICAR:]. Quedan 3 sin resolver, todos por falta de respaldo en las fuentes autoritativas fetcheadas: la anécdota del fin de semana en Bell Labs de Hamming (no figura en su página de amturing), el linaje de construcciones de CLU hacia lenguajes posteriores, y la formulación/publicación original del principio de sustitución de Liskov (la página de amturing nombra a Liskov y Wing pero no cita paper ni año).

**Advertencia sobre la bibliografía:** este draft tenía la bibliografía más flaca de la serie — tres entradas genéricas (`amturing.acm.org`, «Lecturas Turing en ACM», «Wikipedia — Turing Award»), ninguna con URL ni con un dato concreto. Son fuentes de *catálogo*: contienen todo lo que el post necesita (años, textos de los citation, nombres, links a las Turing Lectures), pero **nada de eso fue chequeado contra la fuente**. En consecuencia, la prosa asserta lo mínimo posible y marca con `[VERIFICAR:]` **todos los años de premiación, todos los títulos de Turing Lecture y todas las atribuciones obra→persona**. No se inventó ninguna URL: las notas al pie apuntan sólo a las tres fuentes del draft. Al publicar hay que reemplazar cada `[VERIFICAR:]` por el dato confirmado y agregar el permalink por ganador de `amturing.acm.org` (formato `award_winners/<apellido>_<id>.cfm`, con id distinto por persona — hay que buscarlo, no se puede derivar).

**Huecos (🕳️) — diez**, todos chicos y específicos, uno por sección: el criterio de selección (por qué estos ocho), dónde se cruzó con los códigos de Hamming, qué EWD lo marcó (o con qué idea de Dijkstra está en desacuerdo), si tiene *TAOCP* y hasta dónde lo leyó, si usó verificación formal fuera de un examen, si negoció alguna vez una aproximación ante un problema intratable, con qué libro y en qué máquina aprendió estructuras de datos, si llegó a Liskov por CLU o por SOLID, si lo comió un bug de orden de eventos, y cuál es su premiado favorito. Ninguno se rellenó con prosa genérica.

**Pendiente al publicar:** resolver `[[D-01]]`, `[[D-02]]` y `[[D-03]]` a URLs reales; definir imágenes (la sección dice `_a definir_` — probablemente retratos de Wikimedia con licencia clara, o ninguna y sólo hero); elegir y recortar hero a 2.5:1.

---

## Borrador de prosa

El Nobel no tiene categoría de computación. Alfred Nobel murió en 1896 y no llegó a enterarse de que iba a existir una disciplina entera dedicada a las máquinas que calculan, así que cuando la computación creció y quiso su propio premio, tuvo que inventárselo. Se lo inventó la ACM en 1966[^amturing], y le puso el nombre de Alan Turing. El primero se lo dieron ese mismo año, 1966, a Alan J. Perlis[^perlis].

Y acá está lo que me parece fascinante del asunto: la lista de ganadores terminó siendo, sin proponérselo, el mejor índice de la historia de la ciencia de la computación que existe. Nadie se sentó a escribir «la historia de la disciplina en sesenta capítulos». Simplemente, año tras año, un comité fue eligiendo qué había sido importante. Y si leés la lista completa de corrido, te queda la disciplina entera: los códigos, los lenguajes, los algoritmos, la complejidad, las bases de datos, la criptografía, los sistemas distribuidos, la abstracción. Cada nombre es un capítulo que alguien ya escribió por vos.

Este post es un recorrido por ocho de esos capítulos. No son los ocho mejores —esa discusión no la voy a ganar— sino ocho que valen la pena conocer aunque nunca vayas a usar ninguno directamente.

### La regla del recorrido

Antes de arrancar, el criterio, porque un recorrido sin criterio es una lista de Wikipedia con adjetivos.

El premio Turing se dio muchas veces por construir algo enorme. Está bien, pero no es lo que me interesa acá. Los ocho que elegí son premios que cambiaron **lo que se podía pensar**, no sólo lo que se podía construir. Después del trabajo de cada uno de estos, había una pregunta nueva que antes no se podía ni formular, o una pregunta vieja que dejó de tener sentido. Ese es el filtro.

Es un recorte selectivo y no pretende ser exhaustivo. La lista completa está en el sitio del premio[^amturing] y en Wikipedia[^wikipedia], y te recomiendo mirarla entera después de leer esto.

> 🕳️ **HUECO — necesita a César:** ¿cuál es tu criterio real para elegir estos ocho, y cuál dejarías afuera de los que puse? Una frase alcanza; si tu criterio es distinto al que escribí acá («cambiaron lo que se podía pensar»), reemplazalo por el tuyo y reordeno.

### Hamming: un dato que se repara solo

Richard Hamming trabajaba en Bell Labs y tenía un problema de esos que hoy suenan a chiste y en su momento eran una tortura: la máquina corría los fines de semana sin operadores, encontraba un error de paridad, y abandonaba el trabajo[^t_hamming] [VERIFICAR: la anécdota del fin de semana en Bell Labs y las circunstancias que llevaron a Hamming a los códigos correctores — NO figura en su biografía de amturing.acm.org (la página sólo menciona su paper de 1950 en el Bell System Technical Journal); conseguir una fuente que respalde la anécdota o reescribir sin ella]. Detectaba que algo estaba mal y se rendía. El lunes te enterabas de que habías perdido dos días.

Hamming hizo la pregunta que estaba ahí y nadie hacía: si la máquina puede **detectar** que un bit está mal, ¿por qué no puede **deducir cuál** está mal y arreglarlo sola? Y la respuesta fue que sí puede, si organizás la redundancia con cabeza en vez de tirar un bit de paridad al bulto.

Eso son los códigos de Hamming, y le valieron el premio Turing en 1968 —el citation lo reconoce «por su trabajo en métodos numéricos, sistemas de codificación automática y códigos detectores y correctores de errores»[^t_hamming]—. La idea de fondo —que la información puede llevar encima la estructura necesaria para sobrevivir a su propia corrupción— es una de esas cosas que una vez que la entendés la ves en todos lados: en la memoria ECC de un servidor, en un código QR arrugado que igual escanea, en el disco rígido que lee un sector rayado, en la señal que vuelve de una sonda a miles de millones de kilómetros. Nada de eso funcionaría si la única opción fuera «detecté un error, me rindo».

Hamming además dejó una conferencia sobre cómo hacer investigación, *You and Your Research*, que se cita muchísimo, pero cuidado con mezclarla con la Turing Lecture: son cosas distintas. Su Turing Lecture se llama *One man's view of computer science*[^t_hamming]; *You and Your Research* es una charla aparte de Bell Labs.

> 🕳️ **HUECO — necesita a César:** ¿te cruzaste con los códigos de Hamming en la facultad, en el trabajo, o los aprendiste por curiosidad después? Interesa el contexto concreto, aunque sea una materia y un año.

### Dijkstra: el costo moral de programar

Si Hamming es el ingeniero que resuelve, Edsger Dijkstra es el que te dice que estás resolviendo mal.

Dijkstra ganó el Turing en 1972 —el citation habla de «contribuciones fundamentales a la programación como un desafío intelectual de alto nivel» y de su insistencia en que los programas se compongan correctamente en vez de depurarlos hasta que anden[^t_dijkstra]— y su contribución técnica es gigante: algoritmos de grafos, semáforos, la disciplina de la programación estructurada, la idea de derivar el programa junto con su demostración de corrección en vez de escribirlo primero y rezar después.

Pero lo que lo hace irrepetible es el tono. Dijkstra escribía como si programar fuera una obligación moral y la mayoría de nosotros la estuviéramos incumpliendo. Sostenía que la programación es una de las actividades intelectualmente más difíciles que emprendió la humanidad, y que la industria se comportaba como si fuera una tarea de oficina. Su Turing Lecture, *The humble programmer* (1972), es célebre por eso[^t_dijkstra].

Lo que me gusta de Dijkstra no es que tuviera razón siempre —no la tenía— sino que la disciplina necesitaba a alguien que subiera la vara sin pedir permiso. Si nadie dice «esto está mal hecho», todo se convierte en costumbre. Y en este oficio, la costumbre es el enemigo.

> 🕳️ **HUECO — necesita a César:** ¿hay un EWD en particular que te haya marcado, o una idea de Dijkstra con la que estés en desacuerdo frontal? Cualquiera de las dos sirve, y la segunda es más interesante.

### Knuth: la algoritmia como ciencia (y como libro infinito)

Donald Knuth ganó el premio Turing en 1974 —el citation lo premia «por sus contribuciones fundamentales al análisis de algoritmos y al diseño de lenguajes de programación, y en particular por sus contribuciones al "arte de programar computadoras" a través de sus conocidos libros»[^t_knuth]— esencialmente por convertir el análisis de algoritmos en una ciencia con matemática de verdad adentro, y por *The Art of Computer Programming*, el libro que arrancó en 1962 como un encargo de Addison-Wesley para *un* tomo sobre compiladores, se reorganizó en siete volúmenes y todavía crece: van publicados los volúmenes 1 (1968), 2, 3, 4A (2011) y 4B (2023), con el 4C y el 5 aún en preparación[^t_knuth_taocp].

La palabra clave del título es **art**. Knuth no quería decir que programar fuera improvisación; quería decir que es un oficio que se hace bien o se hace mal, y que la diferencia se puede medir. Antes de él, decir que un programa era «rápido» era una opinión. Después de él, es una función de *n* que se demuestra.

Y hay un detalle que lo pinta entero: Knuth se puso a escribir el libro, no le gustó cómo lo estaba tipografiando la imprenta, y se desvió años a inventar un sistema de composición tipográfica antes de volver al libro. Así nació TeX: según su biografía en la ACM, en 1973 lo decepcionó la tipografía computarizada con que Addison-Wesley compuso la segunda edición del volumen 2, y en 1977 empezó a desarrollar su propio sistema de composición para *TAOCP*[^t_knuth]. Cualquier otro habría aceptado la tipografía fea. Ese desvío es la personalidad de la disciplina en una anécdota.

> 🕳️ **HUECO — necesita a César:** ¿tenés *TAOCP* en el estante? ¿Lo leíste, lo consultás, o está ahí como monumento? La respuesta honesta —incluida «lo abrí dos veces y me rendí»— es mejor post que la respuesta prolija.

### Hoare: demostrar que está bien, y arrepentirse de lo que hiciste

C. A. R. Hoare ganó el Turing en 1980, «por sus contribuciones fundamentales a la definición y el diseño de lenguajes de programación»[^t_hoare], por un conjunto de aportes que incluye la lógica de Hoare: un sistema formal para razonar sobre programas con precondiciones y postcondiciones. La idea de que podés **demostrar** que un fragmento de código hace lo que decís que hace, en vez de probarlo con tres casos y cruzar los dedos.

Su Turing Lecture, *The Emperor's Old Clothes* (publicada en *Communications of the ACM* en febrero de 1981), es de las más honestas que se hayan dado, porque en buena parte es una autocrítica[^t_hoare].

Y después está la otra confesión, la más famosa: Hoare llamó a la referencia nula su «error de mil millones de dólares» en una charla titulada *Null References: The Billion Dollar Mistake*, dada en la conferencia QCon London 2009 —no en su Turing Lecture—, y explicó que la había puesto en ALGOL W en 1965 simplemente porque era fácil de implementar[^hoare_null].

Un tipo que inventa medio lenguaje moderno, gana el máximo premio de la disciplina, y usa el micrófono para pedir disculpas por una decisión de diseño. Eso, para mí, es tan valioso como el teorema.

> 🕳️ **HUECO — necesita a César:** ¿usaste alguna vez lógica de Hoare / verificación formal fuera de un examen? Y si no: ¿te parece que la industria hizo bien en ignorarla, o es una deuda pendiente?

### Cook y Karp: el premio por descubrir que no podemos

Este es mi favorito conceptual, porque es el único caso en el que la disciplina premió una **mala noticia**.

Stephen Cook y Richard Karp ganaron el Turing por separado —Cook en 1982[^t_cook], Karp en 1985[^t_karp]—, y entre los dos armaron una de las ideas más raras y más profundas del siglo: la NP-completitud.

La versión corta y sin fórmulas: hay una familia enorme de problemas —planificar, empaquetar, rutear, colorear, satisfacer restricciones— que parecen no tener nada que ver entre sí, y resulta que son **el mismo problema disfrazado**. Si encontrás una solución rápida para uno, los tenés todos. Y como llevamos décadas sin encontrarla para ninguno, la sospecha razonable es que no existe. El resultado de Cook —su paper de 1971 *The Complexity of Theorem-Proving Procedures*— probó que el problema de satisfacibilidad booleana (SAT) es NP-completo; Karp, en *Reducibility Among Combinatorial Problems* (1972), mostró que otros veintiún problemas combinatorios conocidos son igual de duros[^t_cook] [^t_karp].

¿Por qué importa en la práctica? Porque te cambia lo que hacés cuando te trabás. Antes de Cook y Karp, si no podías resolver un problema, la conclusión era que no eras lo bastante inteligente. Después, hay una tercera opción: podés **demostrar** que el problema es duro, dejar de buscar la solución exacta, y pasar a heurísticas o aproximaciones con la conciencia tranquila. El resultado no te da un algoritmo. Te da permiso para rendirte bien, que es una herramienta de ingeniería subestimadísima.

Y encima, la pregunta que dejaron abierta —si P es igual a NP— sigue abierta: es uno de los siete Millennium Prize Problems del Clay Mathematics Institute, con un millón de dólares sin reclamar[^pnp].

> 🕳️ **HUECO — necesita a César:** ¿te pasó alguna vez, en un proyecto real, reconocer que el problema que te habían pedido era intratable y tener que negociar una aproximación? Si hay un caso concreto —aunque no puedas nombrar la institución— es el mejor ejemplo posible de por qué esta teoría es práctica.

### Hopcroft y Tarjan: las estructuras de datos, en serio

John Hopcroft y Robert Tarjan ganaron el premio Turing juntos en 1986, «por logros fundamentales en el diseño y análisis de algoritmos y estructuras de datos»[^t_hopcroft] [^t_tarjan].

Suena a materia de segundo año. Y esa es exactamente la medida del logro: **es** materia de segundo año *porque ellos la hicieron*. Antes de este trabajo, una estructura de datos era una decisión de implementación, algo que elegías por intuición y por costumbre. Después, es un objeto matemático con propiedades demostrables, y elegir mal es un error que se puede señalar con una demostración en vez de con una opinión.

Cada vez que alguien dice «esto es O(n log n)» sobre un grafo y todos entienden qué significa y por qué importa, hay un pedazo de este premio ahí abajo. La contribución más difícil de valorar es la que se volvió invisible por lo bien que salió.

> 🕳️ **HUECO — necesita a César:** ¿con qué libro aprendiste estructuras de datos, y en qué máquina las implementaste por primera vez? Sirve para anclar la sección en algo tuyo en vez de dejarla como apunte de cátedra.

### Liskov: abstracción de datos antes del marketing

Barbara Liskov ganó el Turing en 2008, «por contribuciones a los fundamentos prácticos y teóricos del diseño de lenguajes de programación y sistemas, en especial las relacionadas con la abstracción de datos, la tolerancia a fallas y la computación distribuida»[^t_liskov], por su trabajo en fundamentos de lenguajes y diseño de sistemas, en particular la abstracción de datos.

Acá hay que decir algo incómodo. Casi todo lo que se enseña como «programación orientada a objetos» en un curso de tres días es sintaxis: clases, herencia, la palabra `extends`. El trabajo de Liskov es lo que hay *debajo* de esa sintaxis y lo que le da sentido: la idea de que un tipo se define por su **comportamiento observable** y no por su representación interna, y que el compilador y el lenguaje tienen que ayudarte a sostener esa frontera. Eso lo hizo concreto en CLU, un lenguaje que casi nadie usó y que dejó huellas en casi todos los que sí usás [VERIFICAR: qué construcciones de CLU se consideran ancestros directos de qué lenguajes posteriores — no atribuir de memoria].

El nombre con el que la mayoría se la cruza es el principio de sustitución de Liskov, la L de SOLID: si S es subtipo de T, tenés que poder usar un S donde se esperaba un T sin que nada se rompa [VERIFICAR: formulación original del principio de sustitución, publicación donde aparece y año]. Es una de las pocas reglas de diseño de objetos que no es una preferencia estética sino un enunciado con contenido.

Que se lo conozca por un acrónimo de consultoría es un poco injusto, pero al menos sobrevivió.

> 🕳️ **HUECO — necesita a César:** ¿llegaste a Liskov por CLU y los papers, o por SOLID y la industria? El orden importa para el tono de esta sección.

### Lamport: el tiempo no existe

Leslie Lamport ganó el premio Turing en 2013, «por contribuciones fundamentales a la teoría y la práctica de los sistemas distribuidos y concurrentes, en particular la invención de conceptos como la causalidad y los relojes lógicos, la seguridad y la vivacidad, las máquinas de estados replicadas y la consistencia secuencial»[^t_lamport].

La idea que lo cambia todo es esta: **en un sistema distribuido no hay «antes» y «después»**. Cuando tenés varias máquinas separadas, cada una con su reloj, no existe un orden global de los eventos. Podés preguntarte si A pasó antes que B y la pregunta puede, literalmente, no tener respuesta. Lamport tomó eso —que suena a filosofía— y lo convirtió en herramientas de ingeniería: el orden causal, los relojes lógicos (los «Lamport timestamps»), un modo de razonar sobre qué se puede saber y qué no. Su paper de 1978 *Time, Clocks, and the Ordering of Events in a Distributed System* es el más citado de toda su obra[^t_lamport].

Todo lo que hoy damos por sentado —replicación, consenso, tolerancia a fallas, la razón por la que tu base de datos distribuida se comporta raro exactamente como la documentación dice que se va a comportar raro— sale de haber aceptado primero que el tiempo compartido no existe.

Y Lamport, encima, escribió LaTeX, el conjunto de macros que él creó sobre el TeX de Knuth[^t_lamport]. Dos de los ocho de esta lista terminaron desviándose a hacer herramientas de tipografía. Eso dice algo sobre la disciplina que no termino de descifrar.

> 🕳️ **HUECO — necesita a César:** ¿alguna vez te comió un bug de orden de eventos en un sistema con más de una máquina? Es el tipo de cicatriz que hace que esta sección deje de ser abstracta.

### Los que quedaron afuera

Ocho es un número arbitrario y dejé gente importante afuera.

Niklaus Wirth ganó el Turing en 1984 —el citation lo premia «por desarrollar una secuencia de lenguajes de computación innovadores: EULER, ALGOL-W, MODULA y PASCAL»[^t_wirth]— por una obra de diseño de lenguajes —Pascal, Modula, Oberon— guiada por una convicción impopular: que la simplicidad es una característica y que hay que pagar por ella, sacando cosas. Media generación aprendió a programar en un lenguaje suyo. Su ausencia de mi lista de ocho es discutible y la discuto yo mismo.

Charles Bachman ganó el Turing en 1973, «por sus destacadas contribuciones a la tecnología de bases de datos»[^t_bachman], por su trabajo en bases de datos, antes del modelo relacional, cuando organizar datos en disco era territorio sin mapa. Es un buen recordatorio de que el premio también reconoció a la generación que resolvió los problemas que hoy ni sabemos que existieron.

Y esos son sólo dos. La lista completa tiene décadas de nombres[^wikipedia], y ahí están la criptografía, los compiladores, la inteligencia artificial, la web, los gráficos. Varios de esos nombres tienen su propio capítulo en este blog: Engelbart, que ganó el suyo, está en [[D-01]]; Ivan Sutherland, que ganó el suyo, está en [[D-02]]; y el hombre que le da nombre al premio está en [[D-03]].

### Lo que hay que hacer con esta lista

Acá va la parte práctica, que es la razón real por la que escribí el post.

El premio Turing no es sólo una medalla: viene con una obligación. El ganador da una conferencia, la **Turing Lecture**, y la ACM las publica[^lecturas]. Eso significa que hay un archivo con decenas de textos en los que la persona que definió un área se para frente a sus pares y explica, en lenguaje humano y sin la coraza del paper, qué estuvo haciendo toda su vida y qué cree que significa.

No conozco mejor material de lectura para alguien que quiere entender esta disciplina en profundidad y no tiene ganas de empezar por un libro de texto. Son cortas. Son personales. Están escritas por gente que ya no tenía nada que demostrar y podía decir lo que pensaba de verdad. Y muchas envejecieron sorprendentemente bien, en parte porque los problemas que describen siguen sin resolverse.

Mi sugerencia concreta: entrá al sitio del premio[^amturing], mirá la lista, buscá el año en que naciste o el año en que empezaste a programar, y leé esa Turing Lecture. No la mejor, no la más famosa: la tuya. Después seguí con la de al lado.

> 🕳️ **HUECO — necesita a César:** de todos los premiados, ¿cuál es *tu* favorito y por qué? El post pide que el lector elija uno; sería raro no decir el propio. Una o dos frases.

Sesenta años de premios y todavía hay un problema abierto planteado por dos de ellos que nadie pudo cerrar. Ese es el estado de la disciplina, y no está tan mal: significa que todavía queda por qué darle el premio a alguien.

---

[^amturing]: [ACM A.M. Turing Award](https://amturing.acm.org/) — sitio oficial del premio: lista completa de ganadores, texto del *citation* de cada uno, biografías y enlaces a las conferencias. Estable.
[^perlis]: [Alan J. Perlis — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/perlis_0132439.cfm) — primer premiado, 1966. Estable.
[^lecturas]: [ACM Turing Award Lectures](https://amturing.acm.org/lectures.cfm) — listado oficial de todas las Turing Lectures con su título y enlace a la versión en la ACM Digital Library (DOIs bajo el prefijo `10.1145/1283920.*`). El estado de acceso abierto de cada PDF en dl.acm.org no fue verificado. Estable.
[^wikipedia]: [Turing Award](https://en.wikipedia.org/wiki/Turing_Award) — Wikipedia: la tabla cronológica completa, útil como índice de entrada. Estable.
[^t_hamming]: [Richard W. Hamming — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/hamming_1000652.cfm) — premio 1968; citation verbatim: «For his work on numerical methods, automatic coding systems, and error-detecting and error-correcting codes». Turing Lecture: [*One man's view of computer science*](https://dl.acm.org/doi/10.1145/1283920.1283923). Estable.
[^t_dijkstra]: [Edsger W. Dijkstra — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/dijkstra_1053701.cfm) — premio 1972. Turing Lecture: [*The humble programmer*](https://dl.acm.org/doi/10.1145/1283920.1283927). Estable.
[^t_knuth]: [Donald E. Knuth — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/knuth_1013846.cfm) — premio 1974; la biografía relata el encargo de Addison-Wesley (enero de 1962), la decepción de 1973 con la composición de la 2.ª edición del volumen 2 y el arranque de TeX en 1977. Turing Lecture: [*Computer programming as an art*](https://dl.acm.org/doi/10.1145/1283920.1283929). Estable.
[^t_knuth_taocp]: [Donald Knuth, *The Art of Computer Programming* (página oficial)](https://www-cs-faculty.stanford.edu/~knuth/taocp.html) ([[tr-20]]) — volúmenes publicados: 1 (1968), 2, 3, 4A (2011, ISBN 0-201-03804-8) y 4B (2023, ISBN 0-201-03806-4); el volumen 5, *Syntactic Algorithms*, figura «in preparation». Estable.
[^t_hoare]: [C. Antony R. Hoare — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/hoare_4622167.cfm) — premio 1980; citation verbatim: «For his fundamental contributions to the definition and design of programming languages». Turing Lecture: *The Emperor's Old Clothes*, *Communications of the ACM*, vol. 24, núm. 2, febrero de 1981, pp. 75-83. Estable.
[^hoare_null]: Tony Hoare, *Null References: The Billion Dollar Mistake* — charla en QCon London 2009; grabación en [InfoQ](https://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare/) (venue «QCon London 2009» confirmado en la propia página). No es la Turing Lecture. Frágil (grabación de conferencia) — agregar respaldo en Wayback Machine antes de publicar.
[^t_cook]: [Stephen A. Cook — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/cook_n991950.cfm) — premio 1982; el citation cita su paper de 1971 *The Complexity of Theorem Proving Procedures* (STOC 1971), que fundó la teoría de la NP-completitud. Estable.
[^t_karp]: [Richard M. Karp — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/karp_3256708.cfm) — premio 1985; la biografía describe *Reducibility Among Combinatorial Problems* (1972) y sus veintiún problemas NP-completos. Turing Lecture: *Combinatorics, Complexity, and Randomness* (*CACM*, vol. 29, núm. 2, febrero de 1986). Estable.
[^pnp]: [P vs NP — Clay Mathematics Institute](https://www.claymath.org/millennium/p-vs-np/) — uno de los siete Millennium Prize Problems; sigue sin resolverse y el premio de un millón de dólares sigue sin reclamar (verificado 2026-07-16). Estable.
[^t_hopcroft]: [John E. Hopcroft — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/hopcroft_1053917.cfm) — premio 1986 (compartido con Tarjan); citation verbatim: «With Robert E Tarjan, for fundamental achievements in the design and analysis of algorithms and data structures». Turing Lecture: [*Computer science: the emergence of a discipline*](https://dl.acm.org/doi/10.1145/1283920.1283943). Estable.
[^t_tarjan]: [Robert E. Tarjan — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/tarjan_1092048.cfm) — premio 1986 (compartido con Hopcroft); citation verbatim: «With John E Hopcroft, for fundamental achievements in the design and analysis of algorithms and data structures». Turing Lecture: *Algorithm design* (el enlace de la página `lectures.cfm` apunta por error al DOI de Hopcroft; usar el permalink del perfil hasta confirmar el DOI propio). Estable.
[^t_liskov]: [Barbara Liskov — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/liskov_1108679.cfm) — premio 2008; citation verbatim: «For contributions to practical and theoretical foundations of programming language and system design, especially related to data abstraction, fault tolerance, and distributed computing». Turing Lecture: *The Power of Abstraction*. Estable.
[^t_lamport]: [Leslie Lamport — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/lamport_1205376.cfm) — premio 2013; la biografía confirma que *Time, Clocks, and the Ordering of Events in a Distributed System* (1978) es su trabajo más citado y que creó LaTeX sobre el TeX de Knuth. Turing Lecture: *An Incomplete History of Concurrency*. Estable.
[^t_wirth]: [Niklaus Wirth — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/wirth_1025774.cfm) — premio 1984; citation verbatim: «For developing a sequence of innovative computer languages, EULER, ALGOL-W, MODULA and PASCAL...». Turing Lecture: [*From programming language design to computer construction*](https://dl.acm.org/doi/10.1145/1283920.1283941). Estable.
[^t_bachman]: [Charles W. Bachman — A.M. Turing Award Laureate](https://amturing.acm.org/award_winners/bachman_9385610.cfm) — premio 1973; citation verbatim: «For his outstanding contributions to database technology». Turing Lecture: [*The programmer as navigator*](https://dl.acm.org/doi/10.1145/1283920.1283928). Estable.
