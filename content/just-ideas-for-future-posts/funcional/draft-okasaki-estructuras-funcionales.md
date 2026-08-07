### B-02 — Estructuras de datos puramente funcionales (Okasaki)

- **Archivo seed:** `dev/draft-estructuras-de-datos-funcionales.md`
- **Slug propuesto:** `okasaki-estructuras-funcionales`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-okasaki-estructuras-funcionales/index.md`
- **Serie:** B (deep dive)
- **Cross-links:** depende de [[tr-04]]; lleva a [[B-01]] (lazy eval), [[B-05]] (trampolines), [[B-06]] (teoría imperativa: contraste)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** long (2500-3500 palabras)

**Concepto:** ¿se puede tener una estructura de datos eficiente sin mutación? Sí, y la tesis de Okasaki muestra exactamente cómo. Listas, queues, deques, heaps, todo *persistent* (cualquier versión vieja sigue accesible) y con costos amortizados óptimos. El truco: lazy evaluation usada con disciplina.

**Hook:** "vamos a construir una queue inmutable que es tan rápida como una mutable. Sí, eso suena imposible. Y sin embargo, hace 30 años Chris Okasaki publicó la tesis donde explica cómo. Pasemos por el truco principal: mover el costo en el tiempo, no en el espacio."

**Outline:**
1. El problema: estructuras "persistentes" (mantener todas las versiones viejas accesibles) sin pagar O(n) por operación.
2. La distinción entre eager y lazy y por qué lazy es el corazón de la solución.
3. El amortized analysis y los physicist's debits.
4. La Banker's Queue: cómo una queue persistente puede ser O(1) amortizado.
5. Heaps: pairing heaps, binomial heaps, leftist heaps.
6. Por qué importa hoy: Clojure, Scala collections, Erlang/Elixir, los sistemas reactivos.
7. Cierre: el contraste con el dogma "inmutable es siempre más lento".

**Bibliografía:** _(fuentes verificadas por fetch el 2026-07-16)_

Fuentes primarias de Okasaki:

- [[tr-04]] — Chris Okasaki, *Purely Functional Data Structures*, tesis doctoral CMU-CS-96-177, Carnegie Mellon University, septiembre 1996. [PDF en CMU](https://www.cs.cmu.edu/~rwh/students/okasaki.pdf) (HTTP 200 verificado 2026-07-16). Comité de tesis: **Peter Lee (director/Chair)**, Robert Harper, Daniel Sleator y Robert Tarjan (Princeton). — estable.
- Chris Okasaki, *Purely Functional Data Structures*, Cambridge University Press — tapa dura 1998, rústica 1999, ISBN 978-0-521-66350-2, 232 pp. Es la versión publicada de la tesis: presenta todo el código en **Standard ML y Haskell** (la tesis está en SML) y agrega capítulos introductorios de implementación —leftist heaps, red-black trees— que la tesis no desarrolla (sólo los menciona al pasar). — estable (se cita por ISBN; la única copia en archive.org parece una subida no autorizada, no se enlaza).
- Chris Okasaki, *Simple and Efficient Purely Functional Queues and Deques*, *Journal of Functional Programming* **5(4):583–592, 1995**. DOI canónico: [10.1017/S0956796800001489](https://doi.org/10.1017/S0956796800001489) (verificado vía Crossref y resolución 302 a Cambridge Core). Texto libre equivalente: capítulo 3 de la tesis [[tr-04]]. — estable (DOI).
- Chris Okasaki, *Red-Black Trees in a Functional Setting*, *Journal of Functional Programming* **9(4):471–477, 1999**. DOI: [10.1017/S0956796899003494](https://doi.org/10.1017/S0956796899003494) (verificado vía Crossref) — lectura relacionada; es el algoritmo funcional de inserción red-black que aparece en el libro. — estable (DOI).

Fuentes clásicas que Okasaki cita (para atribuir bien, no como invención suya):

- Robert E. Tarjan, *Amortized Computational Complexity*, *SIAM Journal on Algebraic Discrete Methods* **6(2):306–318, 1985**. DOI: [10.1137/0606031](https://doi.org/10.1137/0606031) — el trabajo del que Okasaki toma **tanto el método del banquero como el método del físico** (los adapta a evaluación perezosa). — estable (DOI).
- Jean Vuillemin, *A data structure for manipulating priority queues*, *Communications of the ACM* **21(4):309–315, 1978**. DOI: [10.1145/359460.359478](https://doi.org/10.1145/359460.359478) — origen de los binomial queues/heaps. — estable (DOI).
- Michael L. Fredman, Robert Sedgewick, Daniel D. K. Sleator y Robert E. Tarjan, *The pairing heap: a new form of self-adjusting heap*, *Algorithmica* **1(1):111–129, 1986**. DOI: [10.1007/BF01840439](https://doi.org/10.1007/BF01840439) — origen del pairing heap. — estable (DOI).

Puente con la práctica actual y lecturas de contexto:

- [Phil Bagwell, *Ideal Hash Trees*, EPFL, 2001](https://lampwww.epfl.ch/papers/idealhashtrees.pdf) (HTTP 200 verificado 2026-07-16) — la base de las collections persistentes de Clojure. — **frágil** (PDF en página de laboratorio de EPFL, load-bearing; sin snapshot en Wayback al 2026-07-16 — archivarla antes de publicar).
- [Rich Hickey, *Are We There Yet?*, JVM Languages Summit 2009](https://www.infoq.com/presentations/Are-We-There-Yet-Rich-Hickey/) (HTTP 200 verificado 2026-07-16) — por qué Clojure usa los HAMT de Bagwell. — estable.
- [Eric Lippert, *Immutability in C#, Part One: Kinds of Immutability*](https://learn.microsoft.com/en-us/archive/blogs/ericlippert/immutability-in-c-part-one-kinds-of-immutability) — para audiencia .NET. — estable.
- [Persistent data structure en Wikipedia](https://en.wikipedia.org/wiki/Persistent_data_structure) — sólo como contexto sobre la taxonomía (parcial / total / confluentemente persistente), no como cita primaria. — estable.
- [Edward Z. Yang, *You could have invented fractional cascading*](http://blog.ezyang.com/2012/03/you-could-have-invented-fractional-cascading/) — relacionado, didáctico. — frágil (blog personal).

**Imágenes:**
- _Crear_: 4-5 SVG progresivos mostrando una banker's queue después de operaciones sucesivas (1-2 horas, esto es el corazón didáctico del post).
- _Crear_: diagrama del HAMT (Hash Array Mapped Trie) (~45 min).

**Tags propuestos:** `['estructuras de datos', 'Okasaki', 'persistent', 'Clojure', 'lazy', 'amortized']`

**Estado actual:** prosa-borrador completa (~3.050 palabras) siguiendo el outline de 7 puntos, escrita abajo en «Borrador de prosa». Sigue siendo uno de los posts más exigentes del plan.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch: tesis CMU-CS-96-177 HTTP 200, ISBN del libro, y DOIs confirmados vía Crossref para los papers de JFP 1995/1999 y para las fuentes clásicas de Tarjan/Vuillemin/Fredman-Sedgewick-Sleator-Tarjan) y se resolvieron 6 de 11 marcadores `[VERIFICAR:]` por completo, 2 de forma parcial (queda un residuo verificable acotado) y 3 se dejaron intactos por no poder confirmarlos con fuente. Corrección de hecho relevante: el director de la tesis fue **Peter Lee**, no Robert Harper (Harper fue sólo miembro del comité).

Lo que quedó escrito: el encuadre del problema (persistencia sin pagar O(n)), la distinción eager/lazy, la explicación del método del banquero con debits, el desarrollo completo de la Banker's Queue (incluido el contraejemplo de la queue ingenua bajo persistencia, que es el corazón didáctico), el panorama de heaps, la bajada a Clojure/HAMT vía Bagwell + Hickey, y el cierre contra el dogma «inmutable es siempre más lento».

Lo que quedó como hueco:
- 6 `🕳️ HUECO` personales: cómo llegó César a la tesis, qué lenguaje usar para los ejemplos de código, si alguna vez implementó una banker's queue, la discusión «inmutable es más lento» en el sector público, si usó Clojure/Scala/Elixir en producción, y el cierre en primera persona.
- `[VERIFICAR:]` originales: 11. Tras la pasada de bibliografía del 2026-07-16 quedan 5 con marcador (2 de ellos ya con la parte principal resuelta y sólo un residuo acotado): la atribución del leftist heap en el **libro** (la tesis no lo desarrolla), el detalle fino de la extensión del libro (ejercicios / conteo de capítulos), el factor de branching de los HAMT de Clojure + si Hickey cita a Okasaki en la charla, los ecosistemas Scala/Erlang/Elixir sin fuente, y la decisión editorial sobre la referencia huérfana de ezyang.

**Nota de conflicto con la bibliografía — RESUELTA (2026-07-16):** el outline (punto 3) dice «los physicist's debits». Verificado contra la tesis (cap. 3): los *debits* son el instrumento del **método del banquero** (cada debit asociado a una ubicación), mientras que el **método del físico** usa una función de potencial que en la versión perezosa acota la deuda acumulada. La prosa —debits con el banquero— es correcta; queda pendiente **corregir el outline**, que usa la expresión imprecisa «physicist's debits».

**Pendiente antes de publicar:** los 4-5 SVG de la banker's queue (sección «Imágenes») son imprescindibles — la prosa de la sección 4 está escrita asumiendo que existen y los referencia.

---

## Borrador de prosa

Vamos a construir una queue inmutable que es tan rápida como una mutable. Ya sé cómo suena eso. Suena a una de esas promesas de conferencia que se desarman apenas alguien mide algo. Y sin embargo, hace treinta años Chris Okasaki escribió una tesis doctoral en Carnegie Mellon que explica exactamente cómo hacerlo,[^tesis] y desde entonces la respuesta está publicada, con demostración, esperando que la leamos.

El truco no es un truco de implementación. No es un buffer escondido, no es hacer trampa con mutación adentro y prometer que no se nota. Es algo más raro y más lindo: **mover el costo en el tiempo, no en el espacio**. En vez de pagar la operación cara cuando la operación cara aparece, la dejamos anotada como deuda, seguimos trabajando, y la vamos pagando de a pedacitos con las operaciones baratas que vienen después. Lazy evaluation, usada con disciplina contable.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste vos a la tesis de Okasaki? ¿Fue por Clojure, por SICP, por alguien que te la pasó, o la encontraste solo? Una o dos frases sobre el momento del encuentro alcanzan para abrir el post en primera persona.

### 1. El problema: persistencia sin pagar O(n)

Empecemos por definir bien qué queremos, porque la palabra que importa acá se usa mal todo el tiempo.

Una estructura de datos es **persistente** cuando, después de modificarla, la versión vieja sigue existiendo y sigue siendo usable.[^wiki-persistent] Nada que ver con «persistir a disco»: es persistencia en el sentido de que las versiones anteriores persisten, no se pisan. Si tengo una lista `L1`, le agrego un elemento y obtengo `L2`, en una estructura persistente `L1` sigue ahí, intacta, y puedo seguir consultándola, pasársela a otra función, guardarla en un `map`. La estructura clásica y mutable, en cambio, es **efímera**: cada operación destruye la versión anterior. Hay una sola versión, la actual, y el pasado no existe.

Esto no es una curiosidad académica. Es exactamente lo que uno quiere cuando hace undo/redo, cuando compara dos estados de un sistema, cuando quiere que dos threads miren la misma estructura sin lock, cuando quiere que una función no le rompa el argumento al que la llamó. Es, básicamente, todo lo que uno quiere siempre y renuncia a tener porque asume que sale caro.

Y la forma ingenua de tener persistencia sí sale caro: copiar. Si cada `insert` copia la estructura entera, tengo persistencia perfecta y O(n) por operación. Fin del asunto, gracias por venir.

La forma menos ingenua es **compartir estructura**. Una lista enlazada inmutable ya lo hace gratis: `cons(x, L1)` no copia `L1`, apunta a `L1`. `L1` y `L2` comparten toda la cola. Agregar al frente es O(1) y ambas versiones viven. Por eso las listas son el póster de la programación funcional: son el caso donde persistencia e inmutabilidad no cuestan nada.

El problema es que las listas son la excepción fácil. Apenas queremos algo con acceso por los dos extremos —una queue, con `enqueue` atrás y `dequeue` adelante— el compartir estructura deja de ser obvio, y ahí es donde la mayoría de la gente se baja y vuelve al array mutable.

La pregunta de la tesis, entonces, es la buena: ¿podemos tener estructuras persistentes con los **mismos costos asintóticos** que sus contrapartes efímeras? Y la respuesta, para una cantidad sorprendente de estructuras, es que sí.

### 2. Eager, lazy, y por qué lazy es el corazón

Antes de la queue hay que pasar por esto, porque sin esto la queue no funciona.

En evaluación **eager** (estricta), una expresión se evalúa cuando aparece. Escribo `f(costoso())`, y `costoso()` se ejecuta antes de entrar a `f`, siempre, aunque `f` ignore su argumento.

En evaluación **lazy** (perezosa), la expresión no se evalúa: se empaqueta. Queda un objeto —un *thunk*, una promesa, una suspensión— que dice «acá adentro hay un cálculo pendiente». Recién cuando alguien necesita el valor, el thunk se ejecuta. Y acá viene la parte que importa: cuando se ejecuta, **el thunk se sobreescribe con el resultado**. Esa segunda parte se llama *memoization*, y sin ella nada de lo que sigue funciona.

Fijate lo que nos da esa combinación. Un cálculo caro se puede escribir hoy y pagar mañana. Puede no pagarse nunca, si nadie lo mira. Y si diez partes distintas del programa lo miran, se paga **una sola vez** — la primera. Las otras nueve encuentran el resultado ya calculado.

Ese «una sola vez» es el pilar de todo el edificio. Es lo que permite que una operación cara compartida entre muchas versiones de una estructura no se cobre una vez por versión.

Si querés el recorrido largo sobre lazy evaluation —qué es un thunk, cómo se implementa, qué se rompe cuando lo mezclás con efectos— eso va en [[B-01]] y ahí lo desarmo con calma. Acá me alcanza con esas dos propiedades: **se difiere** y **se paga una sola vez**.

> 🕳️ **HUECO — necesita a César:** ¿en qué lenguaje querés los ejemplos de código del post? Okasaki usa SML en la tesis[^tesis]; las opciones razonables son seguirlo en SML, traducir a Haskell (donde lazy es el default y el código queda más corto), o traducir a Clojure (más cercano al lector que llegó por Clojure, pero ahí la laziness hay que pedirla). El borrador de abajo está escrito en pseudocódigo neutro a propósito, hasta que decidas.

### 3. Contabilidad: análisis amortizado y debits

El otro pilar es una forma de contar.

El análisis **amortizado** dice: no me importa que una operación suelta sea cara, me importa el promedio sobre una secuencia de operaciones. Si hago n operaciones y en total pago O(n), entonces el costo amortizado es O(1) por operación, aunque alguna operación individual haya costado O(n) ella sola. Es el análisis que justifica el array dinámico que duplica su capacidad: la duplicación es O(n), pero pasa tan poco seguido que se diluye.

Hay dos maneras clásicas de llevar esta contabilidad, y Okasaki trabaja con ambas: el **método del banquero**, que asigna créditos a la estructura y los gasta cuando llega la operación cara, y el **método del físico**, que define una función de potencial sobre la estructura y mide cada operación como costo real más la variación del potencial. Los dos nombres no son de Okasaki: los toma explícitamente de Robert Tarjan, que los describió en *Amortized Computational Complexity* (1985)[^tarjan]; el aporte de la tesis es adaptarlos a la evaluación perezosa, como veremos enseguida.

Ahora, el problema serio, y es acá donde la tesis se pone interesante.

**El análisis amortizado clásico no sobrevive a la persistencia.** El argumento amortizado asume, sin decirlo, que hay una sola línea de tiempo: hago la operación cara una vez, y las operaciones baratas que la pagaron ya pasaron y no vuelven. Pero si la estructura es persistente, yo puedo agarrar la versión anterior a la operación cara y ejecutarla de nuevo. Y de nuevo. Y de nuevo. Cada vez pago el costo completo, y los créditos que había ahorrado los gasté la primera vez. El promedio se va al demonio: la estructura persistente, analizada así, no tiene ninguna garantía amortizada. Un adversario que insista con la misma versión vieja me hace pagar O(n) todas las veces que quiera.

La solución de Okasaki es cambiar el signo de la contabilidad. En vez de **acreditar** trabajo ya hecho, se **debita** trabajo pendiente. Cada suspensión lazy que todavía no se forzó lleva encima una cantidad de *debits*: la deuda que representa el cálculo que quedó adentro. Las operaciones baratas, a medida que pasan, van **pagando debits** — descontando de a poco esa deuda. Y la regla de oro es: una suspensión no se puede forzar hasta que sus debits estén pagos.

¿Por qué esto sí aguanta la persistencia? Porque el memoization cambia la aritmética del adversario. La primera vez que alguien fuerza la suspensión, se paga y el resultado queda guardado. Si el adversario vuelve a la versión vieja y fuerza otra vez, **encuentra el resultado ya calculado** y no paga nada. El trabajo caro no se puede cobrar dos veces, por más que se lo pida dos veces. Eso es lo que hace que la cota amortizada valga aunque haya bifurcaciones en la línea de tiempo.

Y por eso lazy no es un detalle de estilo del lenguaje elegido, sino el mecanismo. Sin memoization, el adversario repite y gana. Con memoization, no.

Confirmado contra la tesis[^tesis] (cap. 3): los *debits* son el instrumento del **método del banquero** —cada debit se asocia a una ubicación concreta de la estructura—, mientras que el **método del físico** usa una función de potencial que, en la versión perezosa, acota la deuda acumulada del objeto tomado como un todo. La prosa de arriba usa debits con el banquero, que es lo correcto; la frase «los physicist's debits» del outline (punto 3) es imprecisa y hay que corregirla en el outline antes de publicar.

### 4. La Banker's Queue

Ahora sí, la queue. Este es el corazón del post y vale la pena hacerlo despacio.

**La queue funcional ingenua.** La representamos con dos listas: `frente` y `atrás`. Los elementos del frente están en orden; los de atrás están al revés.

- `enqueue x`: `cons` de `x` en `atrás`. O(1).
- `dequeue`: sacar la cabeza de `frente`. O(1).
- Si `frente` queda vacío y `atrás` no: **rotación** — `frente := reverse(atrás)`, `atrás := []`. O(n).

Esta queue es correcta y, en un mundo **efímero**, es O(1) amortizado: cada elemento entra a `atrás` una vez, se da vuelta una vez, y sale de `frente` una vez. Tres operaciones O(1) por elemento a lo largo de toda su vida. El `reverse` de O(n) se paga con los n `enqueue` que lo hicieron falta.

**Y bajo persistencia se rompe.** Acá está el contraejemplo, y quiero que quede grabado porque es el que justifica todo lo demás. Armo una queue con `frente` vacío y n elementos en `atrás`. La llamo `q`. Ahora ejecuto `dequeue(q)`: pago el `reverse`, O(n). Pero `q` sigue existiendo — es persistente, ¿no? Entonces ejecuto `dequeue(q)` **otra vez**: pago el `reverse` **otra vez**, porque la primera vez no dejó nada guardado en `q`, dejó una queue nueva. Repito n veces sobre la misma `q` y pagué O(n²) en n operaciones. El costo amortizado O(1) era una ilusión que dependía de que nadie mirara para atrás.

**La Banker's Queue** arregla esto con tres cambios.[^tesis] [^jfp95]

Primero, las listas pasan a ser **streams lazy** en vez de listas estrictas. Segundo, la rotación se escribe como una suspensión: `frente := frente ++ reverse(atrás)`, donde `++` es lazy (produce el primer elemento sin recorrer todo) y el `reverse` queda adentro, pendiente. Tercero, y esto es lo fino, la rotación **no se dispara cuando `frente` queda vacío**, sino antes: se mantiene el invariante `|atrás| ≤ |frente|`, y apenas `atrás` crecería más que `frente`, se rota.

¿Por qué antes? Porque rotar cuando `frente` está vacío significa que la deuda del `reverse` nace y hay que pagarla ya. Rotando temprano, la suspensión del `reverse` nace **con todo `frente` por delante**: hay tantos `dequeue` baratos por venir como debits tiene la deuda. Cada `dequeue` paga un debit. Cuando el `reverse` finalmente se necesita —cuando el `++` lo alcanza— sus debits ya están todos pagos, y forzarlo es legítimo dentro de la contabilidad.

Y por el memoization, si alguien agarra una versión vieja y vuelve a forzar la misma rotación, no paga: ya está calculada. El contraejemplo de recién deja de funcionar. Ese es el momento en que la queue persistente y la efímera se igualan.

[Acá van los 4-5 SVG progresivos: el estado de `frente` y `atrás` después de operaciones sucesivas, con la suspensión del `reverse` dibujada como una nube con su contador de debits bajando a medida que entran los `dequeue`.]

Un detalle más, para no dejarlo colgando: esto da O(1) **amortizado**, no O(1) en el peor caso. Alguna operación individual todavía puede ser cara. Si uno necesita la garantía por operación —sistemas de tiempo real, o cualquier cosa donde el percentil 99 importa más que el promedio— Okasaki muestra cómo pasar de amortizado a peor caso mediante *scheduling*: en vez de dejar que las suspensiones se acumulen y se fuercen de golpe, se fuerza un pedacito en cada operación, a mano, para que ninguna quede cara.[^tesis] La estructura se vuelve más incómoda de escribir y el análisis más pesado, pero la cota es real.

> 🕳️ **HUECO — necesita a César:** ¿alguna vez implementaste una banker's queue, aunque sea de ejercicio? Si sí, ¿en qué lenguaje y qué te sorprendió al hacerlo? Si nunca lo hiciste, decilo también — es una confesión honesta y sirve igual para el post.

### 5. Heaps: el mismo método, otras estructuras

La queue es el ejemplo estrella, pero si fuera lo único, la tesis sería un truco. Lo que hace que sea una tesis es que el método se aplica a un catálogo entero de estructuras, y los heaps son la mejor demostración de eso.[^tesis]

Un **leftist heap** es un árbol binario ordenado por heap donde cada nodo guarda el largo de su «espina derecha», y el invariante fuerza que el hijo izquierdo tenga espina al menos tan larga como el derecho. Eso mantiene la espina derecha corta —logarítmica— y como el `merge` sólo baja por la espina derecha, el `merge` es O(log n). Y como todo lo demás (`insert`, `deleteMin`) se define en términos de `merge`, sale todo gratis. Es persistente sin esfuerzo: el `merge` construye nodos nuevos y comparte los subárboles que no tocó. (Aclaración verificada: los leftist heaps **no se desarrollan en la tesis**[^tesis] —ahí sólo aparecen los «leftist left-perfect leaf trees», que son otra estructura—; son un ejemplo introductorio que Okasaki agrega en el libro[^libro]. Como la tesis no los atribuye, acá van sin atribución de autoría. [VERIFICAR: si el post los conserva, buscar en el libro[^libro] a quién se los adjudica antes de poner un nombre y un año.])

Un **binomial heap** es una colección de árboles binomiales de rangos distintos, y la analogía que lo hace obvio es la aritmética binaria: insertar un elemento es sumar 1 a un número binario, y el «me llevo uno» de la suma es exactamente el link de dos árboles del mismo rango en uno de rango siguiente. Una vez que ves esa correspondencia, el código se escribe solo. Okasaki los llama por su nombre clásico, *binomial queues*, y los atribuye a Jean Vuillemin (1978[^vuillemin]), con estudio posterior de Mark Brown; menciona además que David King mostró en 1994 que se implementan con elegancia en un lenguaje puramente funcional (Haskell).

Un **pairing heap** es el caso más lindo de todos por otra razón: es ridículamente simple de implementar —el `merge` son tres líneas, el `deleteMin` junta los hijos de a pares y después los mergea— y en la práctica anda excelente, pero su análisis es notoriamente difícil. Es un recordatorio útil de que «simple de escribir» y «simple de demostrar» son dos ejes independientes. El pairing heap es de Michael Fredman, Robert Sedgewick, Daniel Sleator y Robert Tarjan (1986[^pairing]); y sobre la fama de difícil de su análisis, el propio Okasaki confirma en la tesis[^tesis] que sus cotas «have only been conjectured, not proved» —hasta donde llega el trabajo, están conjeturadas pero no demostradas—.

El patrón que se repite en los tres: **el árbol comparte estructura**, la operación reconstruye sólo el camino que tocó, y donde hace falta una operación cara se la envuelve en una suspensión con su deuda anotada.

### 6. Por qué esto importa hoy

Podría quedar como una tesis linda de los noventa. No quedó.

El puente más visible pasa por otro lado: por **Phil Bagwell** y los *Ideal Hash Trees*.[^bagwell] Bagwell describe el Hash Array Mapped Trie —el HAMT—, que es un trie donde cada nivel consume unos bits del hash de la clave para elegir rama, y donde cada nodo usa un bitmap para representar de forma compacta qué ramas existen. El resultado es un `map` con acceso efectivamente constante en la práctica, y —esto es lo que nos importa— **naturalmente persistente**: actualizar una clave reconstruye sólo el camino desde la raíz hasta esa hoja y comparte todo el resto del trie con la versión anterior. Un puñado de nodos nuevos, el resto compartido.

Rich Hickey tomó los HAMT de Bagwell como base de las collections persistentes de Clojure, y explicó por qué en *Are We There Yet?*.[^hickey] El argumento de esa charla es el que le da sentido a todo lo anterior: si los valores son inmutables, el estado deja de ser un lugar que se pisa y pasa a ser una sucesión de valores en el tiempo, y entonces la concurrencia deja de necesitar locks para leer. Pero ese modelo sólo se banca si las estructuras persistentes son **baratas**. Sin Bagwell y sin la línea de trabajo que Okasaki representa, la idea es filosofía; con ellos, es una biblioteca estándar que la gente usa en producción.

[VERIFICAR: el factor de branching de los HAMT de Clojure (creo que es 32, o sea 5 bits por nivel) y si Hickey cita explícitamente a Okasaki además de a Bagwell en esa charla[^hickey]. Chequear la charla antes de afirmar cualquiera de las dos cosas.]

[VERIFICAR: el outline menciona además Scala collections y Erlang/Elixir. La bibliografía actual no respalda nada sobre esos ecosistemas — hay que conseguir una fuente por cada uno (documentación oficial, o el paper/charla correspondiente) o recortar la sección a Clojure, que sí está cubierta.]

Y para la audiencia que no vive en el mundo funcional, está el trabajo de Eric Lippert sobre inmutabilidad en C#,[^lippert] que hace algo que le sirve a cualquiera: distinguir **tipos** de inmutabilidad, porque «inmutable» a secas es una palabra que tapa varias cosas distintas y buena parte de las discusiones de oficina se ganan sólo con hacer esa distinción.

> 🕳️ **HUECO — necesita a César:** ¿usaste Clojure, Scala o Elixir en algo real —trabajo, proyecto propio, prueba seria— o tu contacto con las estructuras persistentes fue por otro lado? Si fue por otro lado, ¿por cuál?

> 🕳️ **HUECO — necesita a César:** ¿te tocó alguna vez la discusión «no usemos estructuras inmutables porque son más lentas» en un equipo real (STG, Ministerio de Cultura, o donde sea)? Si sí, ¿cómo terminó? Un ejemplo concreto acá vale más que toda la teoría de arriba.

### 7. Cierre: contra el dogma

El dogma dice «inmutable es siempre más lento». Y como todos los dogmas útiles, tiene un pedacito de verdad adentro: los factores constantes de una estructura persistente suelen ser peores. Hay indirección, hay allocation, hay presión sobre el garbage collector, hay localidad de caché que se pierde. Un array mutable de enteros le va a ganar a cualquier vector persistente en un loop apretado, y eso no se va a arreglar.

Pero «peores factores constantes» y «asintóticamente peor» son afirmaciones distintas, y el dogma las confunde a propósito. Lo que muestra Okasaki es que la parte asintótica —la parte que decide si tu programa escala o no— se puede recuperar casi siempre. La queue persistente es O(1) amortizado, igual que la mutable. El heap persistente es O(log n), igual que el mutable. El `map` persistente de Clojure es efectivamente constante, igual que el `HashMap`. La diferencia está en el factor, no en el exponente.

Y del otro lado del balance hay cosas que la estructura mutable directamente no puede darte a ningún precio: la versión anterior sigue viva, dos threads leen sin coordinarse, ninguna función te rompe el argumento por atrás, el undo es gratis. Eso no es «más lento»: es otra cosa, que además resulta que cuesta parecido.

La comparación honesta, entonces, no es «mutable rápido contra inmutable lento». Es «mutable con un factor mejor y sin persistencia» contra «inmutable con un factor peor y con persistencia gratis». Puesta así, la elección deja de ser obvia en la dirección que el dogma supone, y pasa a depender —como todo— de qué estás haciendo.

Lo cual me lleva al contraste que quiero dejar planteado y que se merece su propio post: buena parte de nuestra intuición sobre costos viene de un modelo de máquina —RAM, acceso constante, mutación barata— que aprendimos como si fuera la naturaleza y es apenas una convención. Cambiá el modelo y los costos cambian. Eso lo desarrollo en [[B-06]]. Y para el otro cabo suelto —qué hacer cuando la recursión y la laziness te llenan el stack— está [[B-05]].

> 🕳️ **HUECO — necesita a César:** el cierre en primera persona. ¿Qué te quedó a vos de leer esta tesis? ¿Te cambió cómo escribís código, te quedó como algo lindo pero lejano, o te dejó una frustración concreta (por ejemplo, no poder usarlo en el lenguaje en el que laburás)? Dos o tres frases tuyas y el post cierra.

[^tesis]: Chris Okasaki, *Purely Functional Data Structures*, tesis doctoral CMU-CS-96-177, Carnegie Mellon University, septiembre 1996. [PDF en CMU](https://www.cs.cmu.edu/~rwh/students/okasaki.pdf) (HTTP 200 verificado 2026-07-16). La portada aclara el punto que quedaba dudoso: el **director de tesis (Chair) fue Peter Lee**, no Robert Harper; Harper fue miembro del comité junto a Daniel Sleator y Robert Tarjan (Princeton). Que el PDF esté alojado en la página de Harper no lo convierte en director.
[^libro]: Chris Okasaki, *Purely Functional Data Structures*, Cambridge University Press — tapa dura 1998, rústica 1999 — ISBN 978-0-521-66350-2, 232 pp. Diferencia verificada con la tesis: el libro trae todo el código en **Standard ML y Haskell** (la tesis está sólo en SML) y agrega capítulos introductorios de implementación —leftist heaps y red-black trees, que la tesis apenas menciona al pasar—. [VERIFICAR: si además incorpora ejercicios y cuántos capítulos nuevos exactamente; la página del editor en Cambridge devolvió HTTP 403 al fetch y no pude confirmar ese detalle fino.]
[^jfp95]: Chris Okasaki, *Simple and Efficient Purely Functional Queues and Deques*, *Journal of Functional Programming* **5(4):583–592, 1995**. DOI canónico: [10.1017/S0956796800001489](https://doi.org/10.1017/S0956796800001489) (verificado vía Crossref; resuelve 302 a Cambridge Core). Mirror de texto libre: el mismo material se reexpone en el capítulo 3 de la tesis[^tesis].
[^tarjan]: Robert Endre Tarjan, *Amortized Computational Complexity*, *SIAM Journal on Algebraic Discrete Methods* **6(2):306–318, 1985**. DOI: [10.1137/0606031](https://doi.org/10.1137/0606031) (verificado vía Crossref). Es la fuente de la que Okasaki toma los nombres «método del banquero» y «método del físico».
[^vuillemin]: Jean Vuillemin, *A data structure for manipulating priority queues*, *Communications of the ACM* **21(4):309–315, 1978**. DOI: [10.1145/359460.359478](https://doi.org/10.1145/359460.359478) (verificado vía Crossref). Origen de los binomial queues.
[^pairing]: Michael L. Fredman, Robert Sedgewick, Daniel D. K. Sleator y Robert E. Tarjan, *The pairing heap: a new form of self-adjusting heap*, *Algorithmica* **1(1):111–129, 1986**. DOI: [10.1007/BF01840439](https://doi.org/10.1007/BF01840439) (verificado vía Crossref). Origen del pairing heap.
[^bagwell]: Phil Bagwell, [*Ideal Hash Trees*](https://lampwww.epfl.ch/papers/idealhashtrees.pdf), EPFL, 2001.
[^wiki-persistent]: [Persistent data structure](https://en.wikipedia.org/wiki/Persistent_data_structure) en Wikipedia — como lectura de contexto sobre la taxonomía (parcialmente persistente, totalmente persistente, confluentemente persistente), no como cita primaria.
[^hickey]: Rich Hickey, [*Are We There Yet?*](https://www.infoq.com/presentations/Are-We-There-Yet-Rich-Hickey/), JVM Languages Summit, 2009.
[^lippert]: Eric Lippert, [*Immutability in C#, Part One: Kinds of Immutability*](https://learn.microsoft.com/en-us/archive/blogs/ericlippert/immutability-in-c-part-one-kinds-of-immutability).
[^ezyang]: Edward Z. Yang, [*You could have invented fractional cascading*](http://blog.ezyang.com/2012/03/you-could-have-invented-fractional-cascading/) — no lo cito en el cuerpo, pero es el mismo espíritu didáctico y es buena lectura siguiente. [VERIFICAR: decidir si esta referencia entra como lectura recomendada al pie o si se saca; hoy está huérfana — sin referencia inline no renderiza.]

