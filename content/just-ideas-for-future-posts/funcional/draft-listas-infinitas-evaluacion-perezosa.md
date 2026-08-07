### B-01 — Listas infinitas: cómo evaluar lo que no termina

- **Archivo seed:** `dev/draft-listas-infinitas.md`
- **Slug propuesto:** `listas-infinitas-evaluacion-perezosa`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-listas-infinitas-evaluacion-perezosa/index.md`
- **Serie:** B
- **Cross-links:** depende de [[tr-03]]; lleva a [[B-02]] (Okasaki), [[B-05]] (trampolines), [[A2-01]] (SICP §3.5)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** evaluación perezosa permite definir estructuras de datos que no terminan (los primos, los Fibonacci, las primeras N páginas de un crawler). Lo "raro" no es la lista infinita: es la *evaluación estricta* que damos por defecto. El post enseña a pensar en términos de "valores que se van computando cuando los pedís".

**Hook:** "definí los números primos como una lista. Toda la lista. Todos los primos. Y después pedí los primeros 10. Si esto te suena imposible, te falta una idea de Computer Science del año 1976."

**Outline:**
1. La intuición: una lista infinita es plausible si nadie te obliga a calcularla entera.
2. Streams en SICP §3.5: cómo definir `cons-stream` y `force` con poco más que clausuras.
3. El sieve de Eratóstenes en Haskell de 2 líneas (y por qué la versión "obvia" no es eficiente — el detalle del primer paper de Melissa O'Neill).
4. Aplicaciones reales: paginación lazy, parsers, reactive streams.
5. La trampa: leak de memoria si retenés referencias al inicio de un stream infinito (el problema del "head clinger").
6. Cierre: por qué esto cambia cómo ves loops y for-each.

**Bibliografía:**
- [[tr-03]] — SICP §3.5 «Streams»; en particular §3.5.1 (`delay`/`force` y la memoización con `memo-proc`) y §3.5.2 «Infinite Streams» (el sieve, `integers`, `fibs`). Confirmado por fetch de la [edición online, capítulo 3.5](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-24.html) — estable.
- [John Hughes, *Why Functional Programming Matters*](https://doi.org/10.1093/comjnl/32.2.98) — *The Computer Journal* 32(2):98-107, 1989. DOI `10.1093/comjnl/32.2.98` (verificado por Crossref). Mirror libre: [whyfp90.pdf, Univ. of Kent](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf) (reimpresión de 1990 en *Research Topics in Functional Programming*, ed. Turner, pp. 17-42). El argumento canónico de «la evaluación perezosa como pegamento» y las estructuras infinitas (aproximaciones de Newton-Raphson como lista infinita). Estable (DOI); mirror frágil (URL de curso).
- [Peter Henderson & James H. Morris Jr., *A Lazy Evaluator*](https://doi.org/10.1145/800168.811543) — POPL '76, pp. 95-103. DOI `10.1145/800168.811543` (verificado por Crossref). Uno de los dos papers de 1976 que fundan la evaluación perezosa. Estable (DOI, paywall ACM).
- Daniel P. Friedman & David S. Wise, *CONS Should Not Evaluate its Arguments* — en *Automata, Languages and Programming* (ICALP 1976), Edinburgh University Press, pp. 257-284. Sin DOI; registro en [dblp](https://dblp.org/rec/conf/icalp/FriedmanW76.html). El otro paper fundacional de 1976 (estructuras de datos potencialmente infinitas). Estable (dblp).
- [Melissa E. O'Neill, *The Genuine Sieve of Eratosthenes*](https://doi.org/10.1017/S0956796808007004) — *Journal of Functional Programming* 19(1):95-106, 2009. DOI `10.1017/S0956796808007004` (verificado por Crossref). Mirror libre del preprint: [Sieve-JFP.pdf, Harvey Mudd](https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf). Cotas exactas: sieve genuino Θ(n log log n); división de prueba Θ(n√n/(log n)²); «unfaithful sieve» de 2 líneas Θ(n²/(log n)²). Estable (DOI); mirror frágil (URL de curso).
- [Simon Peyton Jones, *The Implementation of Functional Programming Languages*, 1987](https://www.microsoft.com/en-us/research/wp-content/uploads/1987/01/slpj-book-1987.pdf) — referencia clásica de la implementación de lazy eval (reducción de grafos, thunks). Frágil (URL de Microsoft Research).
- [Haskell Wiki — Lazy evaluation](https://wiki.haskell.org/Lazy_evaluation) — explica thunks y usa el término establecido *space leak* (no menciona «head clinger» ni «retainer» en esa página). Frágil (wiki).
- [Stream (computing) en Wikipedia](https://en.wikipedia.org/wiki/Stream_(computing)) — lectura de contexto sobre el término. Estable.

**Imágenes:**
- _Crear_: SVG didáctico — un stream representado como `[1 | <thunk>]` y cómo se va expandiendo cuando lo pedís (~30 min, Excalidraw).
- _Crear_: gráfico simple del sieve mostrando los números tachados (~20 min).

**Tags propuestos:** `['lazy evaluation', 'streams', 'Haskell', 'Scheme', 'SICP']`

**Estado actual:** prosa-borrador completa (~1750 palabras) escrita sobre el outline original, que se respetó punto por punto. Lo que está escrito: la intuición de la lista infinita, `cons-stream`/`delay`/`force` de SICP §3.5, el sieve de dos líneas en Haskell con la objeción de O'Neill, las aplicaciones (paginación, parsers, reactive streams), el head clinger y el cierre sobre loops. Lo que queda pendiente: seis huecos 🕳️ que necesitan a César (primer encuentro con streams, si hizo los ejercicios de §3.5, si vio un space leak en producción, si usó paginación lazy en el sector público, opinión sobre el sieve, anécdota de enseñanza) y seis marcas `[VERIFICAR:]` sobre datos que la bibliografía actual no respalda — sobre todo el «1976» del hook, las cotas de complejidad de O'Neill, la relevancia real de Wadler y de Bagwell para este post, y los nombres exactos de las formas de SICP. Las dos imágenes siguen sin crear.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 5 de 6 marcadores [VERIFICAR:]. Resueltos: el «1976» del hook (confirmado con los dos papers fundacionales de 1976 — Friedman & Wise y Henderson & Morris, ambos agregados a la bibliografía con DOI/dblp); los nombres exactos de las formas de SICP §3.5.1 y el orden `delay`/`force` → `memo-proc` (confirmado contra la edición online); las cotas de O'Neill (sieve genuino Θ(n log log n), división de prueba Θ(n√n/(log n)²), unfaithful sieve Θ(n²/(log n)²)); la terminología «space leak» vs «head clinger» (el Haskell Wiki usa *space leak*; «head clinger» no es término establecido); y la relevancia de Wadler y Bagwell (*Theorems for Free!* no centra los streams y *Ideal Hash Trees* es sobre HAMT — ambos removidos de la bibliografía de este post). Queda pendiente 1 marcador: ubicar el capítulo/sección concreta del libro de Simon Peyton Jones (1987) sobre reducción de grafos y thunks (no se hizo fetch del libro).

---

## Borrador de prosa

Definí los números primos como una lista. Toda la lista. Todos los primos, sin cortar en ningún lado, sin un «hasta acá». Y después, recién después, pedí los primeros diez.

Si eso te suena a chiste o a error de compilación, no te falta un lenguaje: te falta una idea. Una idea vieja, de hace medio siglo: 1976 es el año de los dos papers fundacionales de la evaluación perezosa —Friedman & Wise, *CONS Should Not Evaluate its Arguments*[^friedmanwise], y Henderson & Morris, *A Lazy Evaluator*[^hendersonmorris]—. La idea es tan simple que da un poco de bronca no haberla tenido uno: **una lista infinita es perfectamente plausible mientras nadie te obligue a calcularla entera**.

### Lo raro no es la lista infinita

Acá está el giro que quiero venderte en este post, y es uno solo: lo raro no es la lista infinita. Lo raro es lo otro. Lo raro es la *evaluación estricta*, esa costumbre nuestra de que, cuando escribimos `f(g(x))`, `g(x)` se calcula sí o sí — complete o no complete, la use `f` o la tire a la basura.

Pensalo desde afuera de la profesión. Si te pido «dame los primeros diez primos», vos no te sentás a fabricar todos los primos y después me pasás los diez de arriba. Producís uno, me lo das, producís otro. Parás cuando llegás a diez. La lista de todos los primos existe como *descripción* —«los enteros mayores que 1 sin divisores propios»— y el cálculo aparece recién cuando alguien pide un elemento concreto. La descripción es total; el trabajo es a demanda.

Eso es todo. Evaluación perezosa es mover el momento del cálculo desde «cuando lo escribo» hasta «cuando alguien lo mira». Y el precio de admisión es una sola pieza: un valor que todavía no se computó pero que sabe cómo computarse. En la jerga de Haskell eso se llama **thunk**[^hswiki]; en Scheme lo armás con una clausura de cero argumentos. No hace falta nada más. No hace falta un lenguaje nuevo, ni un runtime especial, ni magia del compilador.

> 🕳️ **HUECO — necesita a César:** ¿cuándo y con qué lenguaje te cruzaste por primera vez con la idea de stream o lista infinita? ¿Fue leyendo SICP, fue en alguna materia, fue en Haskell mucho más tarde? Una o dos frases alcanzan para abrir el post con algo tuyo en vez de con teoría.

### SICP §3.5: la cosa entera con dos primitivas

La construcción canónica está en el capítulo 3 de SICP, en la sección de *Streams*[^sicp]. Y lo lindo del tratamiento de Abelson y Sussman es que no te presentan los streams como una *feature* del lenguaje: te los presentan como una decisión de diseño que podés tomar vos, con lo que ya tenés en la mano.

Las dos primitivas son `delay` y `force`. `delay` toma una expresión y en vez de evaluarla la envuelve; `force` toma ese envoltorio y lo evalúa. Con eso definís el constructor de streams: un stream es un par donde el primer componente ya está calculado y el segundo está diferido.

```scheme
(cons-stream a b)   ; ≡ (cons a (delay b))
(stream-car s)      ; ≡ (car s)
(stream-cdr s)      ; ≡ (force (cdr s))
```

`cons-stream` tiene que ser forma especial y no procedimiento, por la razón obvia: si fuera un procedimiento, sus argumentos se evaluarían antes de entrar, y `b` —que es justamente lo que no queremos evaluar— se evaluaría. La pereza no se puede pedir prestada desde adentro de un lenguaje estricto sin tocar el evaluador, aunque sea un poquito.[^sicp] Los nombres exactos de §3.5.1 son `cons-stream` (forma especial), `stream-car`, `stream-cdr`, `the-empty-stream` y `stream-null?`; y SICP presenta primero `delay`/`force` en su forma básica (`(delay <exp>)` ≡ `(lambda () <exp>)`) y recién después les agrega la memoización envolviéndolos con `memo-proc`.[^sicp]

Con eso ya podés escribir los enteros:

```scheme
(define (integers-from n)
  (cons-stream n (integers-from (+ n 1))))

(define integers (integers-from 1))
```

Esa definición no se cuelga. Cuando la evaluás, lo único que pasa es que se construye un par cuyo `car` es `1` y cuyo `cdr` es una promesa. La recursión infinita está ahí, escrita, mirándote — y no se ejecuta porque nadie la miró todavía. La primera vez que uno ve eso funcionando, algo se reacomoda adentro de la cabeza.

Y hay un detalle que hace que esto sea usable y no una curiosidad de salón: **la promesa se memoiza**. La forzás una vez, se calcula una vez, y a partir de ahí es un valor común y silvestre. Sin memoización, recorrer un stream dos veces recalcula todo, y toda la economía se va al demonio.

> 🕳️ **HUECO — necesita a César:** ¿hiciste los ejercicios de §3.5 en su momento? Si sí, ¿alguno te costó de verdad (el de las series de potencias, el de los pares de enteros, el del integrador)? Va como anécdota de una o dos frases.

### El sieve de dos líneas, y la mala noticia

El ejemplo estrella —el que aparece en toda charla de introducción a Haskell— es el sieve de Eratóstenes en dos líneas:

```haskell
primes = sieve [2..]
sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0]
```

Es hermoso. `[2..]` es la lista infinita de enteros desde 2. `sieve` toma la cabeza, la declara prima, y sigue tamizando la cola con lo que sobró. Pedís `take 10 primes` y te salen diez primos. La demo es impecable y siempre se gana el aplauso.

La mala noticia la escribió Melissa O'Neill en *The Genuine Sieve of Eratosthenes*[^oneill]: **eso no es el sieve de Eratóstenes**. Se le parece de lejos, pero hace otra cosa. El sieve real no pregunta si un número es divisible: *tacha*. Arranca de 2 y tacha 4, 6, 8, 10 saltando de a 2; arranca de 3 y tacha 6, 9, 12 saltando de a 3. Nunca divide, nunca prueba: sólo cuenta y marca. El truco de dos líneas, en cambio, para cada candidato lo prueba contra todos los primos encontrados hasta ese momento. Eso es **división de prueba** disfrazada de sieve, y la diferencia no es estética: es una diferencia de complejidad que se nota apenas salís del ejemplo de juguete y le pedís cien mil primos. O'Neill da las cotas exactas para hallar todos los primos ≤ n: el sieve genuino de Eratóstenes cuesta Θ(n log log n) operaciones; la división de prueba «honesta» (que sólo prueba divisores hasta √x), Θ(n√n/(log n)²); y el truco de dos líneas —que ella bautiza *the unfaithful sieve*, porque prueba cada candidato contra *todos* los primos anteriores, no sólo hasta la raíz— es peor todavía: Θ(n²/(log n)²).[^oneill]

No cuento esto para arruinarle la fiesta a nadie. Lo cuento porque el ejemplo funciona *demasiado* bien como propaganda y termina enseñando la lección equivocada. La lección correcta no es «mirá qué corto sale el sieve en Haskell». La lección correcta es «mirá que puedo escribir una definición que se refiere a una lista infinita, ejecutarla, y que me responda». Que la definición sea además un buen algoritmo es un problema aparte, y es *tu* problema: la pereza te regala la terminación, no la eficiencia.

> 🕳️ **HUECO — necesita a César:** ¿tenés opinión formada sobre el sieve de dos líneas como ejemplo pedagógico — te parece un buen gancho o un mal ejemplo que habría que dejar de usar? El post necesita tu postura acá, no la mía.

### Dónde aparece esto un martes cualquiera

Si la cosa quedara en primos y Fibonacci sería una anécdota de curso. No lo es: aparece por todos lados, casi siempre con otro nombre[^stream].

- **Paginación lazy.** Un cliente de API que expone «todos los registros» como una secuencia y por atrás va pidiendo página por página a medida que el consumidor consume. El que llama escribe un `for` sobre una colección que en el papel tiene tres millones de filas; por el cable pasan doscientas.
- **Parsers.** Un parser que consume un stream de tokens, que a su vez se produce desde un stream de caracteres, que a su vez sale de un archivo que nunca se lee entero. Todo el pipeline avanza tirado desde la punta del consumidor.
- **Reactive streams.** La familia entera de `Observable`/`Flux`/`Flow`, con su *backpressure*, es la misma idea con el productor y el consumidor en hilos distintos: el consumidor pide, el productor produce.
- **Generadores.** El `yield` de Python y compañía es pereza de un solo uso, sin memoización, envuelta en sintaxis imperativa.

Nada de esto es exótico hoy. Lo interesante es que casi siempre lo aprendemos como cuatro herramientas separadas, cuando en el fondo es una sola idea con cuatro etiquetas de marketing distintas.

> 🕳️ **HUECO — necesita a César:** ¿te tocó armar alguna vez un cliente o un exportador con paginación lazy en el sector público (STG o Ministerio de Cultura)? Si sí: ¿qué sistema, qué volumen, llegó a producción? Si no te acordás de un caso concreto, decímelo y saco el ejemplo en vez de inventarlo.

### La trampa: el head clinger

Ahora la letra chica, porque la hay.

Un stream perezoso y memoizado es una lista infinita que se va *materializando* a medida que la recorrés. Y todo lo que ya se materializó vive en memoria mientras alguien lo pueda alcanzar. Si tenés una variable apuntando a la cabeza del stream y a la vez recorrés un millón de elementos, esos elementos no se pueden liberar: hay un camino desde la raíz hasta cada uno. La lista infinita, que en el pizarrón no ocupa nada, en la máquina se te comió la RAM.

El término establecido en la literatura de Haskell para este pecado es *space leak*[^hswiki]; la imagen informal de «aferrarse a la cabeza» del stream (que a veces circula como *head clinger*) describe uno de sus casos típicos. El detalle cruel es que el síntoma no aparece donde está el error: el `OutOfMemory` explota en el consumidor, y la causa es una variable inocente diez frames más arriba que todavía existe. Es el mismo tipo de bug que le dio a la evaluación perezosa su fama de impredecible: el modelo de costo deja de ser local, y razonar sobre un pedazo de código deja de alcanzar. Simon Peyton Jones dedica buena parte de la discusión de implementación a exactamente esto —a que la pereza no es gratis y a qué le cuesta sostenerla a la máquina[^slpj]— [VERIFICAR: ubicar en el libro de SPJ el capítulo o la sección concreta sobre reducción de grafos y thunks, para citarlo con precisión en vez de referenciar el libro entero.] y es la razón por la que los lenguajes estrictos con pereza opcional (Scheme, Scala, y toda la familia de generadores) resultan en la práctica más fáciles de razonar que la pereza por defecto.

> 🕳️ **HUECO — necesita a César:** ¿te comiste alguna vez un space leak de este estilo — en Haskell, en Scala, en un generador de Python que retenías sin querer? ¿Cuánto tardaste en encontrarlo? Es el mejor lugar del post para una cicatriz propia.

### Por qué esto te cambia cómo ves un `for`

Cierro con lo que a mí me parece el verdadero rédito, y no tiene nada que ver con los primos.

Un `for` clásico mezcla dos cosas que no tienen por qué estar juntas: *qué secuencia recorro* y *cuándo se produce cada elemento*. Los streams las separan. La secuencia pasa a ser un valor de primera clase —lo podés nombrar, pasar como argumento, componer con `map` y `filter`, guardar en una estructura— y la producción queda como un efecto que ocurre solo, empujado por el consumo. Una vez que viste eso, el `for` se te vuelve lo que siempre fue: un caso particular, y bastante rígido, de algo más general.

Ahí está el puente hacia el resto de la serie. Cuando las estructuras de datos se vuelven perezosas y persistentes a la vez, el análisis de costo amortizado hay que rehacerlo entero, que es de lo que se ocupa Okasaki [[B-02]]. Cuando la pereza no está disponible y necesitás igual que el control vuelva al que llama, aparecen los trampolines [[B-05]]. Y el tratamiento fundacional, el que conviene leer despacio y con el intérprete abierto al lado, sigue siendo §3.5 de SICP [[A2-01]].[^sicp]

> 🕳️ **HUECO — necesita a César:** ¿alguna vez intentaste explicarle streams a alguien —un alumno, un colega, alguien de tu familia— y viste el momento exacto en que le cayó la ficha (o el momento en que no le cayó)? Sería un buen párrafo de cierre en lugar de terminar en teoría.

[^sicp]: Harold Abelson y Gerald Jay Sussman, *Structure and Interpretation of Computer Programs*, MIT Press, 2.ª ed., 1996 — §3.5 «Streams». [Edición online](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html); [vídeos del curso 6.001 en MIT OCW](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/).
[^oneill]: Melissa E. O'Neill, [*The Genuine Sieve of Eratosthenes*](https://doi.org/10.1017/S0956796808007004), *Journal of Functional Programming* 19(1):95-106, 2009. DOI `10.1017/S0956796808007004`. Mirror libre del preprint: [Sieve-JFP.pdf (Harvey Mudd)](https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf).
[^friedmanwise]: Daniel P. Friedman y David S. Wise, *CONS Should Not Evaluate its Arguments*, en *Automata, Languages and Programming* (ICALP 1976), Edinburgh University Press, pp. 257-284. Registro en [dblp](https://dblp.org/rec/conf/icalp/FriedmanW76.html).
[^hendersonmorris]: Peter Henderson y James H. Morris Jr., [*A Lazy Evaluator*](https://doi.org/10.1145/800168.811543), Proc. 3rd ACM SIGACT-SIGPLAN Symposium on Principles of Programming Languages (POPL '76), pp. 95-103. DOI `10.1145/800168.811543`.
[^slpj]: Simon Peyton Jones, [*The Implementation of Functional Programming Languages*](https://www.microsoft.com/en-us/research/wp-content/uploads/1987/01/slpj-book-1987.pdf), 1987 — la referencia clásica sobre implementación de evaluación perezosa (reducción de grafos, thunks).
[^hswiki]: [Lazy evaluation](https://wiki.haskell.org/Lazy_evaluation), Haskell Wiki — explica thunks y usa el término *space leak*.
[^stream]: [Stream (computing)](https://en.wikipedia.org/wiki/Stream_(computing)), Wikipedia — lectura de contexto sobre el término y sus usos.
