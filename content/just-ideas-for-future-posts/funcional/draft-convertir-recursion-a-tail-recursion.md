### B-04 — Convertir recursión a recursión de cola

- **Archivo seed:** `dev/draft-convierte-programa-recursivo-a-recursivo-de-cola.md`
- **Slug propuesto:** `convertir-recursion-a-tail-recursion`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-convertir-recursion-a-tail-recursion/index.md`
- **Serie:** B
- **Cross-links:** depende de [[B-03]]; lleva a [[B-05]] (trampolines, cuando el lenguaje no optimiza tail calls)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1200-1600 palabras)

**Concepto:** si tu lenguaje optimiza tail calls (Scheme, ML, Haskell, Erlang, Clojure con `recur`), podés escribir loops como funciones recursivas elegantes. La transformación es mecánica: agregar un acumulador.

**Hook:** "el factorial recursivo que aprendiste en la primera clase de programación tiene un problema escondido: si lo corrés con n=100000, te explota la pila. La buena noticia es que se arregla con un cambio de una línea, y el resultado es más limpio. Mostremos."

**Outline:**
1. Recap: qué es una llamada en posición de cola.
2. Por qué los compiladores que optimizan tail calls pueden reemplazar una llamada por un jump.
3. La transformación con acumulador, paso a paso, con factorial.
4. Ejemplo más interesante: `length` de una lista, `map` de una lista (mostrar el truco del "reverse al final").
5. Ejemplo donde no funciona: `tree-sum` (traversal binario — no podés acumular en tail position porque tenés dos hijos).
6. Cierre: qué hacés cuando tu lenguaje *no* optimiza tail calls. Pista: ver [[B-05]].

**Bibliografía:** (reforzada 2026-07-16 — fuentes verificadas por fetch)

- [[tr-03]] — Abelson & Sussman, *SICP*, 2.ª ed. (MIT Press, 1996), §1.2.1 «Linear Recursion and Iteration». Es la sección donde SICP separa el *proceso recursivo* del *proceso iterativo* y define «tail-recursive»: verificado que dice literalmente que una implementación con esa propiedad «will execute an iterative process in constant space, even if the iterative process is described by a recursive procedure», y usa el ejemplo `fact-iter` que reusa esta prosa. [Copia libre HTML](https://sarabander.github.io/sicp/html/1_002e2.xhtml) — estable. (Ver ficha [[tr-03]] en la bibliografía transversal.)
- Guy Lewis Steele Jr., *Debunking the "Expensive Procedure Call" Myth, or, Procedure Call Implementations Considered Harmful, or, Lambda: The Ultimate GOTO* — MIT AI Memo 443, octubre 1977. El paper que justifica la optimización. [Registro en DSpace @ MIT](https://dspace.mit.edu/handle/1721.1/5753) — estable. Versión de actas: DOI [`10.1145/800179.810196`](https://doi.org/10.1145/800179.810196) (*Proceedings of the 1977 annual conference*, ACM '77 — verificado vía Crossref). Espejo PDF de texto completo: [SFU CMPT 383](https://www2.cs.sfu.ca/CourseCentral/383/havens/pubs/lambda-the-ultimate-goto.pdf) — frágil (página de cátedra), [backup Wayback 2025-04-10](https://web.archive.org/web/20250410150107/https://www2.cs.sfu.ca/CourseCentral/383/havens/pubs/lambda-the-ultimate-goto.pdf).
- *Revised⁷ Report on the Algorithmic Language Scheme* (R7RS-small), **§3.5 «Proper tail recursion»**. Verificado que abre con «Implementations of Scheme are required to be *properly tail-recursive*» y que exige soportar un número no acotado de tail calls activos. [PDF oficial](https://small.r7rs.org/attachment/r7rs.pdf), [copia HTML por secciones](https://standards.scheme.org/corrected-r7rs/r7rs-Z-H-5.html) — estable.
- [`recur` — Clojure, special forms](https://clojure.org/reference/special_forms#recur). Verificado que dice «recur in other than a tail position is an error» y «recur … its use in tail-position is verified by the compiler» — estable.
- [Guido van Rossum, *Tail Recursion Elimination* (Neopythonic, 2009-04-22)](https://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html) — el post de por qué Python no la hace. Link verificado (responde 200). Frágil (blog personal): [backup Wayback 2026-07-03](https://web.archive.org/web/20260703214224/http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html).
- Rust — tail calls explícitos: [RFC PR #3407 «Explicit Tail Calls»](https://github.com/rust-lang/rfcs/pull/3407) (palabra clave `become`) y su [tracking issue #112788](https://github.com/rust-lang/rust/issues/112788) (feature gate `explicit_tail_calls`, experimental/no estabilizado al 2026-07). Discusión general previa: [issue #2691 «Reviving tail-call elimination»](https://github.com/rust-lang/rfcs/issues/2691) (abierto). Nota: NO es la «RFC 81».
- [Tail call — Wikipedia](https://en.wikipedia.org/wiki/Tail_call) — referencia general de apoyo.

**Imágenes:**
- _Crear_: 3 SVG mostrando las stack frames del factorial recursivo (crece) vs tail-recursivo + TCO (no crece) (~30 min).

**Tags propuestos:** `['tail recursion', 'TCO', 'Scheme', 'Clojure', 'compiladores']`

**Estado actual:** prosa completa escrita contra el outline existente (~1.450 palabras, dentro del target medium). Todos los ejemplos de código son propios (Scheme, Clojure, Python) y no dependen de la bibliografía. Quedan 4 huecos que necesitan a César (dónde vio por primera vez el stack overflow del factorial; si hay una anécdota de sector público con recursión y pila; qué lenguaje sin TCO usa hoy; si quiere que B-05 salga como post separado o como sección final).

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 6 de 6 marcadores [VERIFICAR:]: (1) SICP §1.2.1 «Linear Recursion and Iteration», 2.ª ed. 1996, confirmada; (2) título canónico de Steele = MIT AI Memo 443, oct. 1977, confirmado vía Crossref + DSpace; (3) R7RS-small §3.5 «Proper tail recursion», confirmada; (4) link de Guido responde (200) + backup Wayback agregado; (5) doc de Clojure confirma que el compilador verifica la posición de cola («recur in other than a tail position is an error»); (6) referencia de Rust corregida: no es la «RFC 81» sino la RFC PR #3407 (`become`) + tracking issue #112788, experimental. Ningún marcador quedó sin resolver.

**Nota sobre la bibliografía (resuelta 2026-07-16):** el ítem listado como «Rust RFC 81 — guaranteed tail call» estaba mal por partida doble. La URL apuntaba a `rust-lang/rfcs/issues/2691`, cuyo título real es «Reviving tail-call elimination» (issue de discusión, abierto), y *no* es la RFC 81 (una RFC vieja distinta). La referencia canónica moderna de tail calls explícitos en Rust es la [RFC PR #3407 «Explicit Tail Calls»](https://github.com/rust-lang/rfcs/pull/3407) —la que introduce la palabra clave `become`— con su [tracking issue #112788](https://github.com/rust-lang/rust/issues/112788) bajo el feature gate `explicit_tail_calls`, todavía experimental / sin estabilizar al 2026-07. El ítem de bibliografía ya quedó corregido arriba.

---

## Borrador de prosa

El factorial recursivo que te enseñaron en la primera clase de programación tiene un problema escondido. Andá y corré esto en tu Scheme favorito con `n` igual a 100000:

```scheme
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
```

Si tenés suerte, te tira un error de stack overflow. Si no tenés suerte, el proceso se muere sin decirte por qué. Y lo llamativo es que el problema no está en el algoritmo —multiplicar cien mil números es tedioso pero perfectamente posible— sino en la *forma* en que escribiste la recursión. La buena noticia: se arregla con un cambio casi mecánico, y el resultado, en mi opinión, queda más limpio que el original. Vamos a hacerlo paso a paso.

### Qué es una llamada en posición de cola

Una llamada está en **posición de cola** cuando es lo último que hace la función: su resultado *es* el resultado de la función que la contiene, sin ningún trabajo pendiente después.

Mirá de nuevo el factorial. La llamada `(factorial (- n 1))` *no* está en posición de cola, aunque parezca que está al final. Después de que vuelve, todavía falta multiplicarla por `n`. La llamada está adentro de un `*`. Alguien tiene que acordarse de ese `n` mientras la llamada de adentro trabaja, y ese «alguien» es un stack frame. Cien mil llamadas anidadas, cien mil frames vivos al mismo tiempo, cien mil multiplicaciones pendientes esperando el retorno de la más profunda. De ahí la explosión.

Compará con esto:

```scheme
(define (loop i acc)
  (if (= i 0)
      acc
      (loop (- i 1) (* acc i))))
```

Acá `(loop (- i 1) (* acc i))` sí está en posición de cola. Cuando esa llamada devuelva un valor, `loop` no tiene absolutamente nada más que hacer: devuelve ese valor tal cual. No hay trabajo pendiente. No hay nada que recordar.

Es la distinción que SICP planta en su §1.2 cuando separa un *proceso recursivo* de un *proceso iterativo*.[^sicp] Y es una distinción sutil, porque las dos funciones son sintácticamente recursivas: las dos se llaman a sí mismas. Lo que cambia es la forma del *proceso* que generan al ejecutarse: una construye una cadena de operaciones diferidas que crece con `n`; la otra no difiere nada, lleva todo su estado en los argumentos. SICP insiste —y con razón— en que un procedimiento recursivo puede generar un proceso iterativo, y que confundir las dos cosas es confundir la sintaxis con la semántica.

### Por qué el compilador puede reemplazar la llamada por un jump

Acá está el truco, y es más simple de lo que parece. Si una llamada está en posición de cola, el frame de la función que llama ya no sirve para nada. Sus variables locales no se van a volver a leer. Su dirección de retorno es exactamente la misma dirección a la que va a tener que volver la función llamada. Entonces: ¿para qué apilar un frame nuevo? Reusá el que ya está. Pisá los argumentos, saltá al principio.

Eso convierte una llamada en un `jump`, y la recursión de cola en un loop, sin que vos hayas escrito un loop. La memoria de stack pasa de O(n) a O(1). No es una optimización cosmética: es un cambio de clase de complejidad espacial.

El argumento canónico de por qué esto vale la pena es el paper de Guy Steele de 1977 que desmonta el mito del «llamado a procedimiento caro».[^steele] La tesis, en criollo: la llamada a procedimiento no es intrínsecamente cara; es cara porque los compiladores la implementan mal. Si la compilás bien, un llamado en posición de cola cuesta lo mismo que un `goto`, y entonces no hay ninguna razón de eficiencia para preferir los loops de la sintaxis del lenguaje por sobre las llamadas a funciones. La abstracción deja de tener peaje.

Scheme se tomó esto tan en serio que lo puso en el estándar. R7RS no dice «el compilador puede optimizar tail calls si tiene ganas»: exige que las implementaciones sean *properly tail-recursive*, es decir, que ejecuten llamadas en posición de cola en espacio constante.[^r7rs] Es una garantía del lenguaje, no un favor del compilador. Podés escribir un servidor que corre un año entero como una llamada recursiva y no se te va a llenar la pila.

### La transformación, paso a paso

La receta es siempre la misma: **agregá un acumulador**. El acumulador es el lugar donde ponés el trabajo que antes quedaba pendiente en el stack.

Del factorial original:

```scheme
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
```

Preguntate: ¿qué queda pendiente después de la llamada recursiva? Una multiplicación. Bueno: hacela *antes*, y pasá el resultado parcial como argumento.

```scheme
(define (factorial n)
  (fact-iter n 1))

(define (fact-iter n acc)
  (if (= n 0)
      acc
      (fact-iter (- n 1) (* acc n))))
```

Tres cambios, siempre los mismos:

1. Aparece un parámetro nuevo, `acc`, que arranca con el **elemento neutro** de la operación que quedaba pendiente. Para el producto es `1`; para la suma sería `0`; para construir una lista, `'()`.
2. El caso base ya no devuelve el neutro: devuelve el acumulador. Toda la respuesta ya está adentro.
3. La operación pendiente se mudó adentro de la llamada, al argumento.

Y hay un envoltorio que oculta el acumulador para que quien llama no tenga que saber de su existencia. Ese wrapper importa: la elegancia de la versión con acumulador se paga con una interfaz más fea, y la solución es esconderla.

### `length`, `map`, y el truco del reverse

`length` sale igual de fácil. El trabajo pendiente es un `+ 1`, y el neutro es `0`:

```scheme
(define (length lst)
  (len-iter lst 0))

(define (len-iter lst acc)
  (if (null? lst)
      acc
      (len-iter (cdr lst) (+ acc 1))))
```

`map` es más interesante, porque expone algo que el factorial esconde. En el factorial la operación pendiente es conmutativa: multiplicar `1×2×3` o `3×2×1` da lo mismo, así que podés acumular en cualquier orden y nadie se entera. Con listas, no. `cons` construye para adelante, y si acumulás con `cons` mientras recorrés, la lista te sale al revés:

```scheme
(define (map f lst)
  (reverse (map-iter f lst '())))

(define (map-iter f lst acc)
  (if (null? lst)
      acc
      (map-iter f (cdr lst) (cons (f (car lst)) acc))))
```

El `reverse` final no es una chapuza: es el precio conocido de la transformación. Recorrés una vez construyendo al revés en espacio constante de stack, y das vuelta el resultado en una segunda pasada, también en tail position. Dos pasadas de O(n) tiempo, O(1) de stack. Contra: una pasada de O(n) tiempo, O(n) de stack. Y ojo con este detalle: si `reverse` mismo no está escrito de forma tail-recursiva, acabás de mover el problema de lugar en vez de resolverlo.

### Dónde la receta se rompe

Ahora el caso incómodo, que es el que más enseña. Sumar los nodos de un árbol binario:

```scheme
(define (tree-sum t)
  (if (leaf? t)
      (value t)
      (+ (tree-sum (left t))
         (tree-sum (right t)))))
```

Acá hay **dos** llamadas recursivas, y sólo una puede estar en posición de cola —a lo sumo. Mientras el subárbol izquierdo se procesa, alguien tiene que acordarse de que después falta el derecho. Ese recuerdo tiene que vivir en algún lado, y el acumulador solo no alcanza: no es un valor lo que hay que recordar, es *trabajo pendiente estructurado*.

Esto no es un defecto de la técnica, es una propiedad del problema. La recursión de cola te da loops; los árboles no son loops, son recursión genuina. Podés forzarlo, claro: llevás una pila explícita de subárboles pendientes, o transformás el programa a estilo continuation-passing y trampolinás. Pero fijate lo que pasó: la pila no desapareció, la escribiste vos a mano en el heap. A veces eso es exactamente lo que querés (el heap es grande, el stack es chico y tiene un límite duro). A veces es cambiar un problema por otro más feo.

La regla práctica que uso: si el árbol está balanceado, la profundidad es logarítmica y no te va a explotar nada; dejalo recursivo y andá a hacer algo más útil. Si el árbol puede degenerar en una lista de cien mil nodos, ahí sí necesitás una estrategia.

> 🕳️ **HUECO — necesita a César:** ¿tenés un caso concreto propio donde te comiste un stack overflow por un traversal recursivo (lenguaje, qué estructura era, cómo lo resolviste)? Con dos frases alcanza; iría acá como aterrizaje del párrafo anterior.

### ¿Y si tu lenguaje no optimiza tail calls?

Porque muchos no lo hacen, y no por descuido. Python es el caso más documentado: Guido van Rossum escribió un post explicando por qué no piensa agregar eliminación de recursión de cola.[^guido] Vale la pena leerlo entero antes de indignarse, porque los argumentos no son de implementación sino de diseño —tienen que ver con qué querés que muestre un traceback y con qué estilo de programación querés fomentar.

Clojure hizo algo más honesto que la mayoría: como corre sobre la JVM, que no garantiza tail calls, no finge. En vez de optimizar silenciosamente te da `recur`, una forma especial que salta al punto de recursión y que **falla en tiempo de compilación** si no la ponés en posición de cola.[^recur] Me parece la decisión de diseño correcta: si no podés dar la garantía, al menos dale al programador un lugar donde pedirla explícitamente y que el compilador le avise cuando se equivoca. Nada peor que un lenguaje que a veces optimiza y a veces no, según el humor del JIT: escribís código que anda en tus pruebas y explota en producción con datos más grandes.

Del lado de Rust, el debate lleva años: hay tail calls explícitos en camino con la palabra clave `become`, propuestos en la RFC #3407 e implementados de forma experimental bajo el feature gate `explicit_tail_calls`, pero todavía sin estabilizar.[^rust]

> 🕳️ **HUECO — necesita a César:** ¿en qué lenguaje sin TCO trabajás hoy más seguido, y cómo convivís con eso? Serviría para cerrar sin sonar a «usá Scheme y listo».

Cuando el lenguaje no coopera, quedan tres salidas: escribir el loop a mano y aceptar que perdiste la elegancia; llevar una pila explícita; o usar un **trampolín**, que es la técnica de devolver una descripción de la próxima llamada en vez de hacerla, y dejar que un loop de afuera la ejecute. De esa última voy a hablar en [[B-05]], que es donde se pone divertido.

Mientras tanto, lo que me gustaría que te lleves es esto: la recursión de cola no es un truco para hacer que el código «ande más rápido». Es la constatación de que el loop y la llamada a función eran la misma cosa todo el tiempo, y que fue el compilador —no la matemática— el que nos hizo creer que había que elegir. Steele lo dijo en el 77.[^steele] Todavía lo estamos discutiendo.

[^sicp]: Harold Abelson y Gerald Jay Sussman, *Structure and Interpretation of Computer Programs*, 2.ª ed. (MIT Press, 1996), §1.2.1 «Linear Recursion and Iteration». Es la sección que define «tail-recursive» y dice que una implementación con esa propiedad «will execute an iterative process in constant space, even if the iterative process is described by a recursive procedure». Ver [[tr-03]]. [Copia libre HTML](https://sarabander.github.io/sicp/html/1_002e2.xhtml).

[^steele]: Guy Lewis Steele Jr., *Debunking the "Expensive Procedure Call" Myth, or, Procedure Call Implementations Considered Harmful, or, Lambda: The Ultimate GOTO* — MIT AI Memo 443, octubre 1977. [Registro en DSpace @ MIT](https://dspace.mit.edu/handle/1721.1/5753). Versión de actas (ACM '77), DOI [`10.1145/800179.810196`](https://doi.org/10.1145/800179.810196); espejo PDF: [SFU CMPT 383](https://www2.cs.sfu.ca/CourseCentral/383/havens/pubs/lambda-the-ultimate-goto.pdf) ([backup Wayback](https://web.archive.org/web/20250410150107/https://www2.cs.sfu.ca/CourseCentral/383/havens/pubs/lambda-the-ultimate-goto.pdf)).

[^r7rs]: *Revised⁷ Report on the Algorithmic Language Scheme* (R7RS-small), §3.5 «Proper tail recursion»: «Implementations of Scheme are required to be *properly tail-recursive*.» [PDF oficial](https://small.r7rs.org/attachment/r7rs.pdf), [copia HTML por secciones](https://standards.scheme.org/corrected-r7rs/r7rs-Z-H-5.html).

[^guido]: Guido van Rossum, [*Tail Recursion Elimination*](https://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html), Neopythonic, 2009-04-22 (link verificado; [backup Wayback](https://web.archive.org/web/20260703214224/http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html)).

[^recur]: [`recur` — Clojure, special forms](https://clojure.org/reference/special_forms#recur). La doc dice «recur in other than a tail position is an error» y que «recur … its use in tail-position is verified by the compiler» — es decir, el chequeo de posición de cola lo hace el compilador.

[^rust]: [RFC PR #3407 «Explicit Tail Calls»](https://github.com/rust-lang/rfcs/pull/3407) (palabra clave `become`) y su [tracking issue #112788](https://github.com/rust-lang/rust/issues/112788) (feature gate `explicit_tail_calls`, experimental al 2026-07). Discusión previa: [issue #2691 «Reviving tail-call elimination»](https://github.com/rust-lang/rfcs/issues/2691).

---

**Notas para el pase a post:**

> 🕳️ **HUECO — necesita a César:** ¿dónde viste por primera vez explotar la pila con un factorial o similar —cátedra, laburo, jugando— y en qué lenguaje? Es el candidato natural para reemplazar el arranque impersonal del primer párrafo por una entrada en primera persona.

> 🕳️ **HUECO — necesita a César:** ¿[[B-05]] (trampolines) va como post aparte, o preferís absorberlo como sección final acá? Si va aparte, la sección «¿Y si tu lenguaje no optimiza tail calls?» hay que podarla para no pisarlo.

