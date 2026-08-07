### B-03 — Convertir un programa recursivo a iterativo

- **Archivo seed:** `dev/draft-convierte-un-programa-recursivo-a-iterativo.md`
- **Slug propuesto:** `convertir-recursivo-a-iterativo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-convertir-recursivo-a-iterativo/index.md`
- **Serie:** B
- **Cross-links:** lleva a [[B-04]] (la versión "elegante": recursión de cola), [[B-05]] (cuando ni eso sirve: trampolines)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** dada una función recursiva, hay una técnica mecánica para transformarla en iterativa con una pila explícita. El post enseña la receta y muestra cuándo (y cuándo no) usarla.

**Hook:** "vamos a tomar el quicksort recursivo más típico que viste en clase de algoritmos, y lo vamos a convertir en un loop con un array. Sin recursión. Y vamos a entender por qué esa transformación es siempre posible."

**Outline:**
1. Por qué uno querría hacer esto: stack limit, lenguajes sin TCO, performance, debugging.
2. La receta general: cada llamada recursiva → push de continuación + estado.
3. Ejemplo simple: factorial recursivo → factorial con pila explícita.
4. Ejemplo no-tan-simple: traversal de árbol DFS recursivo → con pila.
5. Ejemplo donde duele: quicksort. Por qué no se ve tan elegante.
6. La conexión con CPS: convertir-a-iterativo y CPS-transform son dos caras de lo mismo.
7. Cierre: cuándo NO hacerlo (legibilidad gana al stack limit en el 95% de los casos).

**Bibliografía:**
- [[tr-03]] — SICP, 2.ª ed. 1996. §1.2.1 «Linear Recursion and Iteration» (la distinción proceso recursivo vs. iterativo, verificada por fetch) y §5.1.4 «Using a Stack to Implement Recursion» (la pila explícita en la máquina de registros). Estable — [texto completo en MIT](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book.html).
- [Andrew W. Appel, *Compiling with Continuations*, Cambridge University Press, 1992](https://www.cs.princeton.edu/~appel/papers/cwc.html) — CPS como representación intermedia; el compilador que ilustra el método es Standard ML of New Jersey (confirmado: título/autor/editorial/año y el subject heading «Standard ML of New Jersey» en la página del autor y de CUP). Estable.
- [Olivier Danvy & Lasse R. Nielsen, *A First-Order One-Pass CPS Transformation*, BRICS RS-01-49, diciembre 2001](https://www.brics.dk/RS/01/49/) — transformación a CPS compositiva, de primer orden y en una pasada (autores, número de reporte y año confirmados por fetch). Estable.
- [John C. Reynolds, *Definitional Interpreters for Higher-Order Programming Languages*, ACM '72](https://doi.org/10.1145/800194.805852) — origen de la *defunctionalization*: continuaciones representadas como estructuras de datos en vez de funciones, que es exactamente lo que se hace al desrecursivar a mano. DOI verificado por Crossref (Reynolds, 1972, Proc. ACM annual conference). Reimpreso en *Higher-Order and Symbolic Computation* 11(4), 1998. Estable.
- [Daniel P. Friedman & Mitchell Wand, *Essentials of Programming Languages*, 3.ª ed., MIT Press, 2008](https://mitpress.mit.edu/9780262062794/essentials-of-programming-languages/) — ISBN 978-0-262-06279-4; la 3.ª edición agrega un capítulo entero sobre CPS y el paso a máquina de estados por registros/continuaciones (edición e ISBN verificados). Estable.
- [Tail call en Wikipedia](https://en.wikipedia.org/wiki/Tail_call) — para enlazar con [[B-04]]. Frágil (wiki, no load-bearing).
- [Stack-oriented programming en Wikipedia](https://en.wikipedia.org/wiki/Stack-oriented_programming). Frágil (wiki, no load-bearing).
- [C. A. R. Hoare, *Quicksort*, *The Computer Journal* 5(1):10–16, 1962](https://doi.org/10.1093/comjnl/5.1.10) — el paper original. DOI, revista, volumen, número, páginas y año verificados por Crossref (corrige el «1961» del draft: es 1962). Paywall en Oxford Academic; DOI como canónico. Estable.
- [GCC manual — Optimize Options, `-foptimize-sibling-calls`](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html) — «Optimize sibling and tail recursive calls. Enabled at levels -O2, -O3, -Os» (verificado por fetch). Estable.
- [Guido van Rossum, *Tail Recursion Elimination* (Neopythonic, 2009)](https://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html) — fuente primaria de que CPython no hace TRE por decisión de diseño («I don't want TRE in the language … it's simply unpythonic»). Frágil (blog personal) → conviene backup en Wayback antes de publicar.

**Imágenes:**
- _Crear_: animación frame-by-frame (4-5 SVG) de la pila durante un factorial recursivo y su contraparte iterativa (~1 hora).
- _Crear_: side-by-side de quicksort recursivo vs con pila explícita (~30 min).

**Tags propuestos:** `['recursion', 'iteration', 'stack', 'algoritmos', 'CPS']`

**Estado actual:** prosa completa en borrador (~1700 palabras), siguiendo el outline de 7 puntos tal como estaba. Escrito: el encuadre del hook, los cuatro motivos para desrecursivar, la receta general en tres pasos, el ejemplo de factorial (con la distinción SICP de proceso recursivo vs iterativo), el DFS con pila, el quicksort con pila explícita y su optimización de recursión de cola sobre la partición grande, la conexión con CPS, y el cierre.

Pendiente de César (5 huecos marcados 🕳️): si alguna vez le explotó la pila en producción y dónde; si dio la materia de algoritmos y cómo la enseñaba; si usó la técnica en un proyecto real; su postura sobre el «95% de los casos» del outline; y el cierre personal.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 7 de 7 marcadores `[VERIFICAR:]`. Resueltos: (1) Hoare *Quicksort* = *The Computer Journal* 5(1):10–16, **1962** (no 1961), DOI 10.1093/comjnl/5.1.10, verificado por Crossref; (2) la distinción proceso recursivo vs. iterativo está en SICP **§1.2.1** «Linear Recursion and Iteration»; (3) el límite de recursión de CPython es **1000** por defecto (observado en 3.12.7 con `sys.getrecursionlimit()`); (4) `-foptimize-sibling-calls` queda habilitada en **-O2, -O3, -Os** (manual de GCC); (5) el libro de Appel ilustra CPS con el compilador **SML/NJ** (subject heading confirmado); (6) el paper de Danvy es **BRICS RS-01-49**, con Lasse R. Nielsen como coautor, diciembre 2001; (7) CPython **no** hace TRE por decisión de diseño de Guido van Rossum (fuente primaria: su blog Neopythonic, 2009). Se añadieron además Reynolds 1972 (*defunctionalization*) y EOPL 3.ª ed. (Friedman & Wand, ISBN 978-0-262-06279-4) como respaldo del vínculo CPS↔pila-como-dato.

Pendientes tras esta pasada: verificar que los cinco ejemplos de código Python realmente corren tal como están (no se ejecutaron aquí); poner backup en Wayback de las dos URLs frágiles load-bearing (blog de Guido; entradas de Wikipedia son no load-bearing); y producir las dos imágenes listadas en **Imágenes**.

---

## Borrador de prosa

Vamos a tomar el quicksort recursivo más típico que viste en clase de algoritmos, ese de seis líneas que entra entero en una diapositiva, y lo vamos a convertir en un loop con un array. Sin recursión. Ni una sola llamada a sí mismo.

Y después, cuando lo tengamos funcionando y feo, quiero que entendamos por qué esa transformación siempre es posible. No «casi siempre». Siempre. Cualquier función recursiva que puedas escribir se puede reescribir como un bucle más una pila explícita, y la razón por la que eso es cierto no es un truco de programador: es que la recursión nunca fue otra cosa que un bucle más una pila. Lo único que pasa es que normalmente la pila te la administra el lenguaje, gratis, y no la ves. Desrecursivar es sacarle el trabajo al compilador y hacerlo a mano.

### Por qué querrías hacerte este trabajo

Hay cuatro motivos, y ninguno es «porque la recursión es lenta».

El primero es el límite de pila. La pila de llamadas de tu proceso tiene un tamaño finito, y bastante más chico de lo que la gente supone. Un recorrido recursivo sobre una lista enlazada de un millón de nodos no es un algoritmo profundo conceptualmente, pero son un millón de marcos de activación apilados, y en algún punto el sistema operativo dice basta. En CPython ni siquiera llegás a ese punto: el intérprete tiene un límite artificial de recursión bastante bajo —1000 marcos por defecto (`sys.getrecursionlimit()` devuelve `1000` en CPython 3.12)[^recursionlimit]— que te tira una excepción mucho antes de que la pila real del sistema se agote.

El segundo es que tu lenguaje puede no tener eliminación de llamada de cola. Si una función recursiva termina con la llamada recursiva como última operación —una *tail call*[^tailcall]—, un compilador que implemente eliminación de llamada de cola puede reusar el marco de activación actual en vez de apilar uno nuevo, y ahí la recursión te sale gratis en espacio. Scheme lo exige por especificación. GCC lo hace en C bajo la bandera `-foptimize-sibling-calls`, que queda habilitada por defecto en los niveles `-O2`, `-O3` y `-Os`[^gcc]. Python no: CPython no elimina las llamadas de cola, y no es una omisión pendiente sino una decisión de diseño explícita de Guido van Rossum, que la considera «unpythonic» justamente porque borraría marcos del traceback[^gvr_tre]. Si estás en un lenguaje sin TCO, la elegancia de la recursión de cola no te compra nada y la pila explícita vuelve a la mesa. De eso hablo en detalle en [[B-04]].

El tercero es performance, y acá conviene bajar las expectativas. Una llamada de función tiene un costo —armar el marco, guardar la dirección de retorno, saltar— pero en un lenguaje compilado moderno ese costo es chico y el compilador suele hacer *inlining* de los casos fáciles. Convertir a iterativo para ganar velocidad casi nunca vale la pena, y muchas veces la pila explícita que escribís a mano es *más lenta* que la del hardware, porque la del hardware está optimizada hasta el último ciclo y la tuya es una lista de Python con tuplas adentro.

El cuarto es debugging, y este me parece el más honesto de los cuatro. Con una pila explícita, la pila *es un valor*. La podés imprimir. La podés serializar a disco y retomar el cómputo mañana. La podés inspeccionar en el medio del loop y ver exactamente qué le falta hacer al algoritmo. Con la pila del sistema, eso mismo lo tenés que hacer con un debugger y un `bt`.

> 🕳️ **HUECO — necesita a César:** ¿alguna vez te explotó la pila en un sistema en producción? Si sí: ¿dónde, con qué lenguaje, y cómo lo resolviste (subiste el límite, desrecursivaste, o rediseñaste)? Alcanza con dos frases.

### La receta

La receta general tiene tres pasos y no depende del algoritmo.

**Uno:** identificá el estado. ¿Qué necesita saber una invocación de tu función para hacer su trabajo? Eso son los parámetros, más las variables locales que sobreviven a la llamada recursiva.

**Dos:** identificá los puntos de retorno. Cada llamada recursiva parte el cuerpo de tu función en dos: lo que pasa antes y lo que pasa después de que vuelve. Ese «lo que pasa después» es la *continuación* de la llamada — el trabajo pendiente.

**Tres:** reemplazá la pila implícita por una explícita. Donde había una llamada recursiva, ahora hay un `push` de una tupla (estado, marca de en-qué-punto-estabas). Donde había un retorno, hay un `pop`. El cuerpo entero de la función pasa a vivir adentro de un `while pila:`, y la marca de en-qué-punto-estabas se convierte en un `if` sobre la etiqueta que apilaste.

Ese tercer paso es exactamente lo que hace un lenguaje concatenativo por diseño[^stackprog]: si tu modelo de cómputo ya es una pila de operandos, no tenés que inventarle una.

### Factorial: el caso donde no hacía falta

Empecemos por el ejemplo que *no* necesita la receta, porque entender por qué no la necesita es la mitad del post.

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
```

Esto es lo que SICP llama un **proceso recursivo**[^sicp]: la forma del código es recursiva *y* la forma del cómputo también, porque el `n *` queda pendiente. Cuando la llamada de adentro vuelve, todavía hay trabajo que hacer. La máquina tiene que acordarse de `n` para cada nivel, y por eso el consumo de espacio crece con `n`. La distinción de SICP entre proceso recursivo y proceso iterativo es la idea central acá, y es sutil: **no** es una distinción sobre cómo se ve el código, es sobre cómo se comporta el cómputo. La distinción se desarrolla en SICP §1.2.1, «Linear Recursion and Iteration»[^sicp].

Si acumulás el resultado en un parámetro, el multiplicar deja de quedar pendiente:

```python
def fact(n, acc=1):
    if n == 0:
        return acc
    return fact(n - 1, n * acc)
```

Ahora la llamada recursiva es lo último que pasa. No hay nada que recordar. Es un **proceso iterativo** escrito con sintaxis recursiva, y en Scheme corre en espacio constante sin que toques nada. En Python te sigue explotando, porque Python apila igual — y por eso lo escribís así:

```python
def fact(n):
    acc = 1
    while n > 0:
        acc, n = n * acc, n - 1
    return acc
```

Fijate que acá no aparece ninguna pila explícita. La acumuladora la reemplazó. Esa es la primera lección de la receta: **antes de sacar la pila explícita, fijate si podés reformular el problema como acumulación.** Si podés, terminaste, y el resultado es legible. La pila explícita es para cuando no podés.

### DFS: el caso donde la receta se ve linda

```python
def dfs(nodo, visitar):
    if nodo is None:
        return
    visitar(nodo)
    dfs(nodo.izq, visitar)
    dfs(nodo.der, visitar)
```

Dos llamadas recursivas. La segunda es de cola, la primera no. Acumular no alcanza. Aplicamos la receta:

```python
def dfs(raiz, visitar):
    pila = [raiz]
    while pila:
        nodo = pila.pop()
        if nodo is None:
            continue
        visitar(nodo)
        pila.append(nodo.der)
        pila.append(nodo.izq)
```

Y salió limpio. Salió limpio por una razón muy específica: en el preorden, todo el trabajo de un nodo pasa *antes* de las dos llamadas recursivas. No hay continuación que recordar — cuando volvés de los hijos, no queda nada por hacer. El estado que apilás es un solo puntero.

Probá lo mismo con un recorrido *inorden* y vas a ver aparecer el problema real: ahí hay trabajo después de la primera llamada recursiva, así que ya no alcanza con apilar el nodo — hay que apilar el nodo *y* la marca de si venís a bajar por su subárbol izquierdo o a visitarlo. Esa marca es la continuación hecha dato.

### Quicksort: el caso donde duele

Ahora sí, el del hook.

```python
def qs(a, lo, hi):
    if lo >= hi:
        return
    p = particion(a, lo, hi)
    qs(a, lo, p - 1)
    qs(a, p + 1, hi)
```

El quicksort de Hoare[^hoare] tiene la misma forma que el DFS en preorden: todo el trabajo —la partición— pasa antes de las dos llamadas, y no queda nada pendiente al volver. Así que la conversión es igual de mecánica:

```python
def qs(a, lo, hi):
    pila = [(lo, hi)]
    while pila:
        lo, hi = pila.pop()
        if lo >= hi:
            continue
        p = particion(a, lo, hi)
        pila.append((lo, p - 1))
        pila.append((p + 1, hi))
```

Funciona. Y acá está la parte que quería mostrarte: la versión iterativa te habilita una optimización que la recursiva no te deja hacer cómodamente. En el código de arriba, la pila explícita puede crecer hasta O(n) en el peor caso, igual que la del sistema. Pero si apilás sólo la partición **más grande** y seguís iterando sobre la más chica —o sea, si tratás la mitad chica como una llamada de cola y la resolvés en el mismo loop—, la pila queda acotada a O(log n):

```python
def qs(a, lo, hi):
    pila = []
    while True:
        while lo < hi:
            p = particion(a, lo, hi)
            if p - lo < hi - p:
                pila.append((p + 1, hi))   # la grande, a la pila
                hi = p - 1                 # la chica, en este loop
            else:
                pila.append((lo, p - 1))
                lo = p + 1
        if not pila:
            return
        lo, hi = pila.pop()
```

Eso es hacer a mano la eliminación de llamada de cola que tu compilador quizás no hace. Y fijate que en el código recursivo original la optimización también existe, pero *sólo funciona si el compilador colabora*. Acá la escribiste vos y no depende de nadie.

El precio: mirá ese último bloque y decime honestamente si al leerlo se ve que es un quicksort. La forma del algoritmo —«ordenar es partir, y después ordenar las dos mitades»— desapareció. Quedó una máquina de estados que hace lo mismo. Eso es lo que se paga.

> 🕳️ **HUECO — necesita a César:** ¿diste alguna vez la materia de algoritmos, o la parte de recursión dentro de alguna materia? Si sí: ¿cómo la enseñabas — la recursión primero y la pila después, o al revés? Sirve para encuadrar este párrafo con autoridad propia en vez de en abstracto.

### La conexión que hace que todo cierre

Todo lo que hicimos en este post tiene un nombre en la literatura de compiladores, y no es «desrecursivar».

Cuando convertís una función a estilo de paso de continuaciones (CPS), lo que hacés es reescribirla para que nunca retorne: en vez de devolver un valor, recibe un argumento extra —la continuación— y lo *llama* con el resultado. La propiedad importante es que en CPS **todas** las llamadas son llamadas de cola. Ninguna función tiene trabajo pendiente después de llamar a otra, porque el trabajo pendiente está reificado en la continuación que le pasaste.

Y si todas las llamadas son de cola, y las llamadas de cola no crecen la pila, entonces un programa en CPS corre en un loop plano. Que es exactamente lo que veníamos armando a mano.

Lo que estuvimos haciendo en este post es una transformación a CPS mal escrita. Cada tupla que apilamos —el `(lo, p-1)` del quicksort, la marca de «vengo a visitar este nodo» del inorden— es una continuación representada como dato en vez de como clausura. La literatura tiene los dos lados de esto bien mapeados: Appel dedicó un libro entero a usar CPS como representación intermedia de un compilador real —el de Standard ML of New Jersey, que es el compilador con el que el libro ilustra el método[^appel]—, y Danvy y Nielsen dieron la transformación en una sola pasada y de primer orden[^danvy] — «de primer orden» quiere decir precisamente esto: continuaciones como estructuras de datos, no como funciones. Reynolds ya le había puesto nombre a esa idea en 1972: *defunctionalization*[^reynolds]. Que es lo que escribís sin saberlo cuando desrecursivás a mano.

Convertir-a-iterativo y CPS-transform son la misma operación mirada desde dos lados. Uno lo hace un programador cansado a las tres de la mañana porque le explotó la pila; el otro lo hace un compilador, sistemáticamente, sobre todo el programa. La técnica que estamos aprendiendo acá a mano es la que un compilador de Scheme ya aplica sin preguntarte.

Y cuando ni CPS ni la pila explícita alcanzan —cuando estás en un lenguaje sin TCO y *aun así* querés todas las llamadas en cola— hay un tercer truco. Ese es [[B-05]].

### Cuándo no hacerlo

Casi siempre.

Lo digo en serio. La conversión a iterativo es una técnica de último recurso, y la razón es que destruye lo único que la versión recursiva tenía de bueno: que se parecía al problema. `qs(a, lo, p-1); qs(a, p+1, hi)` *es* la definición de quicksort. El `while pila:` es una implementación de la definición de quicksort. Cuando el próximo que lea tu código tenga que decidir si tiene un bug, va a poder verificar la primera contra la idea, y la segunda sólo contra sí misma.

La regla que me parece defendible: desrecursivá cuando tengas una medición, no cuando tengas una intuición. Un stack overflow reproducible es una medición. «Esto podría ser profundo» no lo es. Y cuando la medición aparezca, probá primero las dos salidas baratas —reformular como acumulación, o subir el límite de pila— antes de reescribir el algoritmo. La pila explícita es la tercera opción, no la primera.

> 🕳️ **HUECO — necesita a César:** el outline decía «legibilidad gana al stack limit en el 95% de los casos». ¿Suscribís ese número o preferís no poner una cifra? Si la ponés, ¿de dónde sale — es una impresión tuya de años de código, o la sacaste de algún lado citable?

> 🕳️ **HUECO — necesita a César:** ¿usaste esta técnica en un proyecto real alguna vez? ¿Cuál era el problema y valió la pena? Si nunca la usaste en producción y la conocés sólo de la teoría, decilo — es un cierre más honesto que inventar un caso.

> 🕳️ **HUECO — necesita a César:** ¿con qué querés cerrar? Opciones: (a) que la recursión es una abstracción sobre la pila y desrecursivar es romper la abstracción a propósito; (b) el gancho hacia [[B-04]] y [[B-05]]; (c) algo tuyo. Una frase alcanza.

[^sicp]: Harold Abelson & Gerald Jay Sussman, *Structure and Interpretation of Computer Programs*, MIT Press, 2.ª ed. 1996 — §1.2.1 «Linear Recursion and Iteration» (proceso recursivo vs. proceso iterativo) y §5.1.4 «Using a Stack to Implement Recursion» (la pila explícita en la máquina de registros). [Texto completo en MIT](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book.html).
[^recursionlimit]: `sys.getrecursionlimit()` devuelve `1000` por defecto (observado directamente en CPython 3.12.7). El [módulo `sys`](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit) documenta el límite pero no fija el número por defecto en el texto; el valor 1000 se verificó ejecutando el intérprete.
[^appel]: Andrew W. Appel, [*Compiling with Continuations*](https://www.cs.princeton.edu/~appel/papers/cwc.html), Cambridge University Press, 1992. El compilador que ilustra el método es Standard ML of New Jersey.
[^danvy]: Olivier Danvy & Lasse R. Nielsen, [*A First-Order One-Pass CPS Transformation*](https://www.brics.dk/RS/01/49/), BRICS Research Series RS-01-49, diciembre 2001.
[^reynolds]: John C. Reynolds, [*Definitional Interpreters for Higher-Order Programming Languages*](https://doi.org/10.1145/800194.805852), Proc. ACM annual conference (ACM '72), 1972 — origen del término *defunctionalization*. Reimpreso en *Higher-Order and Symbolic Computation* 11(4), 1998.
[^tailcall]: [Tail call](https://en.wikipedia.org/wiki/Tail_call) en Wikipedia.
[^stackprog]: [Stack-oriented programming](https://en.wikipedia.org/wiki/Stack-oriented_programming) en Wikipedia.
[^hoare]: C. A. R. Hoare, [*Quicksort*](https://doi.org/10.1093/comjnl/5.1.10), *The Computer Journal* 5(1):10–16, 1962 — el paper original. Revista, volumen, número, páginas y año verificados por Crossref (el «1961» del borrador anterior era incorrecto: la fecha de publicación es 1962). El PDF en Oxford Academic está detrás de paywall; el DOI es la referencia canónica.
[^gcc]: [GCC manual — Optimize Options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html), entrada `-foptimize-sibling-calls`: «Optimize sibling and tail recursive calls. Enabled at levels -O2, -O3, -Os».
[^gvr_tre]: Guido van Rossum, [*Tail Recursion Elimination*](https://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html), blog Neopythonic, 2009 — «I don't want TRE in the language. If you want a short answer, it's simply unpythonic». Blog personal (frágil): conviene un backup en Wayback antes de publicar.
