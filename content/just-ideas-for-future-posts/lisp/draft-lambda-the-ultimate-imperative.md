### A2-09 — Lambda the Ultimate Imperative: el paper de Steele que cambió cómo pensar imperativo

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `lambda-the-ultimate-imperative`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-lambda-the-ultimate-imperative/index.md`
- **Serie:** lisp
- **Cross-links:** [[A2-02]] (Scheme papers), [[B-03]] (recursivo a iterativo), [[B-04]] (tail recursion)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** long (1800-2200 palabras) — elegido al expandir: el argumento del paper necesita tres ejemplos (loop, goto, escape) y no entra en formato medium

**Concepto:** *Lambda: The Ultimate Imperative* (Guy L Steele, 1976) es uno de los famosos "Lambda Papers" donde Steele muestra que cualquier construcción de control imperativo (loops, gotos, exception handlers) puede expresarse como un caso particular de una llamada a procedimiento con continuaciones. El post explica el argumento del paper en términos modernos, con ejemplos en Scheme y JavaScript, y discute por qué este paper sigue siendo la base teórica de los compiladores modernos.

**Hook:** cualquier loop, cualquier goto, cualquier try/catch, es secretamente una llamada a una función. Eso lo demostró Guy Steele en 1976 en un paper de 19 páginas. El post lo explica sin matemática.

**Outline:**
1. Hook: el `for` que escribiste esta mañana es una llamada a función disfrazada. Steele lo demostró en 1976.
2. Qué es el paper y dónde cae: los Lambda Papers, el MIT AI Lab, el clima de la época (la llamada a procedimiento tenía mala fama).
3. La tesis en una línea: `lambda` no es sólo abstracción de datos, es **el** mecanismo de control.
4. Ejemplo 1 — el loop: `while` reescrito como procedimiento que se llama a sí mismo en posición de cola. Nada crece.
5. Ejemplo 2 — el `goto`: una llamada en posición de cola *es* un salto que además pasa argumentos.
6. Ejemplo 3 — la salida no local (`return`, `break`, `try/catch`): reificar «qué viene después» y llamarlo, o no llamarlo. Continuaciones.
7. El giro: si todo esto es una llamada a procedimiento, entonces la llamada a procedimiento tiene que ser barata. El argumento es tanto de expresividad como de compilación.
8. Herencia: CPS, SSA, los compiladores de hoy. Por qué el paper no envejeció.
9. Cierre: qué me llevo — no hay «constructos de control», hay una sola cosa.

**Bibliografía:** _(pasada de fuentes 2026-07-15: todas las URLs de abajo fueron fetcheadas y verificadas; los flags de bitrot van al final de cada ficha)_

**Fuentes primarias — los memos:**
- **[^lti]** Guy Lewis Steele Jr. y **Gerald Jay Sussman**, *LAMBDA: The Ultimate Imperative*, MIT AI Lab, **AI Memo No. 353, 10 de marzo de 1976, 40 páginas**. Canónico: [DSpace del MIT, handle 1721.1/5790](https://dspace.mit.edu/handle/1721.1/5790) (el landing devuelve 405 a fetch automatizado; hay [snapshot Wayback 2026-05-10](http://web.archive.org/web/20260510053942/https://dspace.mit.edu/handle/1721.1/5790)). Escaneo fetcheado y contado: [bitsavers AIM-353.pdf](https://www.bitsavers.org/pdf/mit/ai/aim/AIM-353.pdf) + [snapshot 2024-06-05](http://web.archive.org/web/20240605070111/http://bitsavers.org/pdf/mit/ai/aim/AIM-353.pdf). — estable.
- **[^lti_transcripcion]** [Transcripción HTML del AIM-353](https://research.scheme.org/lambda-papers/lambda-papers-ltu-imperative.html), research.scheme.org — abstract e índice de secciones. — frágil, **sin snapshot en Wayback**.
- **[^goto]** Guy Lewis Steele Jr., *Debunking the "Expensive Procedure Call" Myth…; or, LAMBDA: The Ultimate GOTO*, **AI Memo No. 443, octubre de 1977, 23 páginas**. [DSpace 1721.1/5753](https://dspace.mit.edu/handle/1721.1/5753) + [snapshot 2026-04-06](http://web.archive.org/web/20260406130250/http://dspace.mit.edu/handle/1721.1/5753). **Memo clave que le faltaba a este draft**: trae el encuadre del «llamar es caro» y la frase «GOTO que pasa argumentos», las dos cosas que el draft le atribuía al 353. — estable.
- **[^goto_acm]** Versión en actas del anterior: *Proceedings of the 1977 Annual Conference (ACM '77)*, pp. 153-162. DOI [10.1145/800179.810196](https://doi.org/10.1145/800179.810196) (verificado vía Crossref; ACM DL no fetcheable). Mirror libre: [CMPT 383, Simon Fraser University](https://www2.cs.sfu.ca/CourseCentral/383/havens/pubs/lambda-the-ultimate-goto.pdf) — frágil, **sin snapshot en Wayback**.

**Catálogos de la serie:**
- **[^chm]** [SCHEME family — Software Preservation Group](https://softwarepreservation.computerhistory.org/LISP/scheme_family.html), Computer History Museum — autoría, memo, fecha y páginas de cada AI Memo. — estable.
- **[^readscheme]** [The Original 'Lambda Papers'](https://conservatory.scheme.org/readscheme/page1.html) — readscheme (mirror vivo; reemplaza al `library.readscheme.org` que citaba el draft). — frágil.
- **[^lambdapapers]** [The Lambda Papers](https://research.scheme.org/lambda-papers/) — índice de la serie. — frágil.

**Herencia CPS/SSA (respaldo nuevo para la sección de compiladores):**
- **[^kelsey]** Richard A. Kelsey, «A Correspondence between Continuation Passing Style and Static Single Assignment Form», *ACM SIGPLAN Notices* 30(3), marzo 1995, pp. 13-22. DOI [10.1145/202530.202532](https://doi.org/10.1145/202530.202532). Texto completo verificado: [PDF](https://bernsteinbear.com/assets/img/kelsey-ssa-cps.pdf) — frágil. — DOI estable.
- **[^appel]** Andrew W. Appel, «SSA is Functional Programming», *ACM SIGPLAN Notices* 33(4), abril 1998, pp. 17-20. DOI [10.1145/278283.278285](https://doi.org/10.1145/278283.278285). [Copia del autor](https://www.cs.princeton.edu/~appel/papers/ssafun.pdf) + [snapshot 2026-07-09](http://web.archive.org/web/20260709171212/https://www.cs.princeton.edu/~appel/papers/ssafun.pdf). — estable.

**Especificación:**
- **[^r7rs]** [*Revised⁷ Report on the Algorithmic Language Scheme*](https://standards.scheme.org/corrected-r7rs/r7rs-Z-H-5.html), §3.5 «Proper Tail Recursion» (eds. Shinn, Cowan, Gleckler). [PDF oficial](https://standards.scheme.org/official/r7rs.pdf), 88 pp. — estable.

**Sin usar / pendiente:**
- [[tr-14]] Lambda the Ultimate classic papers — sigue sin respaldar ninguna afirmación concreta de este post; queda como puerta de entrada al corpus.

**Imágenes:** _a definir_

**Tags propuestos:** `['Scheme','Steele','lambda papers','continuations','compilers','historia CS']`

---

## Borrador de prosa

El `for` que escribiste esta mañana no es un `for`. Es una llamada a función. El `break` que pusiste adentro tampoco es un `break`: es otra llamada a función. Y el `try/catch` que envuelve todo, lo mismo.

No lo digo como metáfora ni como provocación de blog. Lo digo porque hay un paper de 1976 que lo demuestra, construcción por construcción, y que se llama *Lambda: The Ultimate Imperative*.[^lti] Guy Lewis Steele Jr. y Gerald Jay Sussman agarraron el catálogo completo de la programación imperativa —el que todavía hoy aparece en el capítulo 3 de cualquier libro de introducción— y lo fueron reescribiendo, uno por uno, en términos de una sola cosa: la aplicación de un procedimiento. Voy a contarte cómo funciona el argumento, sin una sola línea de matemática, porque cuando lo entendés cambia para siempre la manera en que mirás un lenguaje de programación.

> ⚠️ **Corregido en la pasada de fuentes (2026-07-15):** el memo es de **Steele y Sussman en coautoría**, no de Steele solo. Lo confirman la portada del escaneo del MIT, el catálogo del Computer History Museum, la transcripción de research.scheme.org y la bibliografía de readscheme.[^lti] [^chm] [^readscheme] El Concepto y el Hook del draft (que dicen «Guy L Steele, 1976» y «lo demostró Guy Steele») quedan sin tocar por ser de César, pero hay que arreglarlos antes de publicar.

> ⚠️ **Corregido en la pasada de fuentes (2026-07-15):** el paper **no tiene 19 páginas: tiene 40**. Conté las páginas del escaneo original de bitsavers con `pypdf` (40 páginas exactas), y coinciden el catálogo del Computer History Museum (que lista «40 pages» para el AIM-353) y el índice del DjVu en Wikisource (40 páginas de escaneo, cuerpo numerado hasta la 39).[^chm] [^lti] No hay lectura bajo la cual dé 19. El Hook de César dice «un paper de 19 páginas» y hay que corregirlo antes de publicar.

### Un paper con nombre de chiste interno

Los que se llaman «los Lambda Papers» son una serie de memos del AI Lab del MIT de mediados de los setenta, escritos alrededor del nacimiento de Scheme, todos con el mismo molde de título: *Lambda: The Ultimate X*. El chiste es que el título es siempre el mismo y la X va cambiando —imperativo, declarativo, GOTO, opcode— y cada memo demuestra que `lambda` también alcanza para eso.

La lista canónica, con los títulos y los números de memo tal como figuran en el catálogo del Computer History Museum y en la bibliografía de readscheme:[^chm] [^readscheme]

| Memo | Título | Autores | Fecha | Págs |
|---|---|---|---|---|
| AIM-349 | *SCHEME: An Interpreter for Extended Lambda Calculus* | Sussman y Steele | dic 1975 | 43 |
| AIM-353 | *LAMBDA: The Ultimate Imperative* | Steele y Sussman | 10 mar 1976 | 40 |
| AIM-379 | *LAMBDA: The Ultimate Declarative* | Steele | nov 1976 | 47 |
| AIM-443 | *Debunking the "Expensive Procedure Call" Myth; or, Procedure Call Implementations Considered Harmful; or, LAMBDA: The Ultimate GOTO* | Steele | oct 1977 | 23 |
| AIM-452 | *The Revised Report on SCHEME: A Dialect of LISP* | Steele y Sussman | ene 1978 | 35 |
| AIM-453 | *The Art of the Interpreter; or, The Modularity Complex* | Steele y Sussman | may 1978 | 75 |
| AIM-514 | *Design of LISP-based Processors; or, SCHEME: A Dielectric LISP; or, Finite Memories Considered Harmful; or, LAMBDA: The Ultimate Opcode* | Steele y Sussman | mar 1979 | 75 |

Ojo con dos cosas al usar esta tabla. Primero, «los Lambda Papers» no es una lista cerrada con acta fundacional: research.scheme.org incluye además *Compiler Optimization Based on Viewing LAMBDA as RENAME plus GOTO* (Steele, mayo 1977) y la tesis *RABBIT: A Compiler for SCHEME* (AITR-474, Steele, mayo 1978), que el catálogo del CHM no lista en la misma serie.[^lambdapapers] [^readscheme] Segundo, el orden de autoría varía entre catálogos para el AIM-453. Si el post nombra memos además del 353, conviene citar la ficha de cada uno y no la serie en bloque.

Para entender por qué esto era noticia, hay que meterse en el clima de la época. En ese momento la llamada a procedimiento tenía mala fama. Era cara: llamar a una función quería decir armar un frame, guardar registros, saltar, volver, desarmar el frame. Y esa fama tenía consecuencias culturales bien concretas: si llamar es caro, entonces la abstracción es cara, entonces el programador «serio» escribe loops y no funciones, y el que factoriza su código en procedimientos chiquitos está siendo un derrochador. Vos ya conocés la versión moderna de esa discusión: es la misma que se repite cada vez que alguien dice que un método de tres líneas «tiene overhead».

Y esto no es la memoria colectiva de internet: es lo que dice Steele, con todas las letras, aunque **no en este memo**. La introducción del AIM-353 no argumenta nada sobre costos: arranca por el lambda-cálculo como meta-lenguaje y pasa directo a los cuatro grupos de construcciones que va a modelar. El encuadre del «llamar es caro» es el tema central de *otro* de los Lambda Papers, el AIM-443 de octubre de 1977 —el que se llama, justamente, *Debunking the "Expensive Procedure Call" Myth*—, cuyo abstract abre así: «Folklore states that `GOTO` statements are "cheap", while procedure calls are "expensive". This myth is largely a result of poorly designed language implementations.»[^goto] Y sobre la consecuencia cultural, Steele es explícito: «Because procedure calls are "expensive", we tend to avoid using them in our code. Unfortunately, this produces a detrimental effect on our programming style.»[^goto]

> ⚠️ **Nota de la pasada de fuentes (2026-07-15):** el párrafo de arriba estaba escrito como si el clima del «llamar es caro» fuera el punto de partida del AIM-353. No lo es —lo verifiqué contra la introducción del propio memo— y por eso el párrafo ahora cita el AIM-443 explícitamente. Si el post quiere sostener este encuadre, tiene que hacerlo con el 443 en la mano, no con el 353.

El paper entra justo ahí, y lo hace con una jugada elegante: en vez de defender la llamada a procedimiento diciendo «no es tan cara», demuestra que **no hay nada más**. Que todos los constructos de control que considerás baratos y familiares ya son llamadas a procedimiento, sólo que con la etiqueta cambiada.

> 🕳️ **HUECO — necesita a César:** ¿cuándo te cruzaste por primera vez con los Lambda Papers, y por dónde llegaste — por SICP, por Scheme, por alguien que te los pasó? Con una o dos frases alcanza; es el párrafo que ancla el post en tu biografía y no en la de Steele.

### La tesis, en una línea

`lambda` no es solamente la manera de darle nombre a un pedazo de cálculo. Es el mecanismo de control. El único que hace falta.

Todo lo demás —el loop, el salto, la salida anticipada, el manejo de errores— es azúcar sintáctica sobre eso. No «se parece a». No «se puede simular con». **Es** eso, y el paper lo muestra escribiendo cada construcción como una llamada.

Veamos los tres casos que importan.

### Ejemplo 1: el loop

Este es el más fácil y el más desconcertante. Tomá un `while` cualquiera de JavaScript:

```js
function sumaHasta(n) {
  let i = n, acc = 0;
  while (i > 0) {
    acc = acc + i;
    i = i - 1;
  }
  return acc;
}
```

Tres cosas pasan acá: hay estado mutable (`i` y `acc` cambian), hay una condición, y hay un salto implícito al principio del bloque cada vez que se llega al final. Ahora mirá lo mismo en Scheme:

```scheme
(define (suma-hasta n)
  (define (bucle i acc)
    (if (= i 0)
        acc
        (bucle (- i 1) (+ acc i))))
  (bucle n 0))
```

No hay `while`. No hay asignación. No hay salto. Hay un procedimiento que se llama a sí mismo y ya.

Y acá viene lo importante, porque si esto fuera nada más un cambio de estilo no valdría un paper: **las dos versiones compilan a lo mismo**. Las variables del loop se volvieron parámetros; la asignación se volvió pasaje de argumentos; el salto al principio del bloque se volvió la llamada a `bucle`; la condición de corte se volvió un `if`. Ninguna de esas traducciones agrega trabajo. Y como la llamada a `bucle` está en **posición de cola** —es lo último que la función hace, no hay nada pendiente después—, no hace falta guardar a dónde volver. No hay a dónde volver. El compilador reutiliza el frame que ya está y emite un salto.

O sea: la versión recursiva no es la versión «elegante pero lenta» de la versión con `while`. Es la misma máquina, escrita en un vocabulario donde no hay palabras especiales. Todo esto lo desarmo con más calma en [[B-03]] y en [[B-04]]; acá lo que me interesa es el giro conceptual, que es éste: el loop dejó de ser una construcción primitiva y pasó a ser un caso particular de otra cosa.

[VERIFICAR: correr los dos snippets (Node LTS y un Scheme R7RS, digamos Guile o Chez) antes de publicar. Son míos, no salen del paper. Confirmar además que el Scheme elegido efectivamente no crece la pila. — Pasada de fuentes 2026-07-15: **no resuelto y no resoluble por web**; esto pide ejecución, no bibliografía. Lo único que se pudo sourcear es la garantía formal: el R7RS §3.5 exige tail recursion propia («Implementations of Scheme are required to be properly tail-recursive»),[^r7rs] así que la expectativa está respaldada — pero que *este* snippet en *esa* implementación no crezca la pila hay que verlo corriendo.]

> 🕳️ **HUECO — necesita a César:** ¿te acordás de la primera vez que viste un loop escrito así, como llamada recursiva en posición de cola? ¿Te resultó natural o te pareció una perversión? Me interesa la reacción honesta del momento, incluso —sobre todo— si fue de rechazo.

### Ejemplo 2: el `goto`

Si el loop es una llamada, el `goto` es todavía más directo.

Un `goto` hace exactamente una cosa: mandar el control a otro lado y no volver. Una llamada en posición de cola hace exactamente eso mismo… y además pasa argumentos. La llamada es el `goto` con equipaje.

Puesto al revés, que es como se entiende mejor: si tenés llamadas en posición de cola que no crecen la pila, no necesitás `goto` nunca. Cada etiqueta de tu programa spaghetti es un procedimiento; cada `goto etiqueta` es `(etiqueta)`; y cada variable global que usabas para llevar información de un lado al otro —esa que te obligaba el `goto` porque no podía pasar nada— se vuelve un parámetro honesto, escrito, visible en la firma.

Y ahí hay un detalle que me parece hermoso: la crítica clásica al `goto` es que oscurece el flujo de datos, porque el salto no dice qué información viaja con él. La llamada en posición de cola arregla eso de taquito. No prohíbe el salto: lo obliga a declarar qué se lleva puesto.

La frase existe y es de Steele, pero **no está en el AIM-353**: está en el AIM-443, el *Ultimate GOTO*, y dice así: «In general, procedure calls may be usefully thought of as `GOTO` statements which also pass parameters, and can be uniformly encoded as `JUMP` instructions.»[^goto] Lo verifiqué extrayendo el texto del PDF de la versión publicada en las actas de la ACM '77, donde el pasaje aparece con esta variante: «procedure calls can uniformly be treated as GOTO statements which pass parameters, with return addresses being pushed at a conceptually different point (the commencement of argument evaluation)».[^goto_acm] O sea: al citarla hay que atribuirla al 443 (1977), no al 353 (1976).

### Ejemplo 3: irse antes de tiempo

Los dos casos anteriores son los cómodos. Éste es donde el argumento se pone interesante, porque acá lo que hay que expresar no es «seguir», sino «abandonar»: un `return` en medio de una función, un `break` que se sale del loop, un `throw` que se sale de veinte llamadas de golpe.

La idea es la misma de antes, con una vuelta de tuerca: si «qué viene después» es un procedimiento, entonces salirse es simplemente **no llamarlo**, o llamar a otro.

```js
function buscar(lista, p, siEncontrado, siNoEncontrado) {
  const paso = (resto) =>
    resto.length === 0
      ? siNoEncontrado()
      : p(resto[0])
        ? siEncontrado(resto[0])
        : paso(resto.slice(1));
  return paso(lista);
}
```

No hay `return` anticipado, no hay `break`, no hay excepción. Hay dos procedimientos que se pasan como argumentos —el «qué hago si encuentro» y el «qué hago si no»— y la función llama a uno o al otro. La salida anticipada se volvió una decisión sobre a quién llamar.

Eso que le pasás como argumento, ese «resto del cómputo» convertido en un valor que se puede guardar, pasar y postergar, es una **continuación**. Y una vez que las continuaciones son valores de primera clase, el catálogo entero se te cae solo: el `return` es llamar a la continuación de la función; el `break` es llamar a la continuación del loop; el `try/catch` es llevar dos continuaciones en el bolsillo, la normal y la de error, y elegir; la corrutina es guardarte una continuación para invocarla más tarde. Todos casos particulares del mismo movimiento.

> ⚠️ **Nota de la pasada de fuentes (2026-07-15):** el abstract del AIM-353 enumera exactamente lo que el memo modela: «Simple Recursion, Iteration, Compound Statements and Expressions, GO TO and Assignment, Continuation-Passing, Escape Expressions, Fluid Variables, Call by Name, Call by Need, and Call by Reference», repartido en cuatro secciones: Simple Loops, Imperative Programming, Continuations y Parameter Passing Mechanisms.[^lti] [^lti_transcripcion] Conclusión para el post: los ejemplos 1 (loop) y 2 (`goto`) están respaldados por el memo sin problema, y las continuaciones y la salida no local también —son la sección 3, «Escape Expressions»—. **Pero el `try/catch` no.** El memo no trata manejo de excepciones en el sentido moderno; lo más cercano es la escape expression, que es salida anticipada, no un mecanismo de errores con handlers. El Hook de César dice «cualquier try/catch» y el Concepto dice «exception handlers»: eso es una extrapolación del post, legítima como lectura mía pero que no hay que presentar como algo que demuestra el paper. Tampoco hay que perderse que el memo cubre dos cosas que el post ni menciona (fluid variables y los mecanismos de pasaje de parámetros: call by name, need y reference).

[VERIFICAR: correr el snippet de `buscar`. Es mío. Ojo con la profundidad de `paso` en un motor sin tail calls: es probable que reviente con listas grandes, y si revienta, hay que decirlo en el post en vez de disimularlo — es justamente la mitad del argumento. — Pasada de fuentes 2026-07-15: **la ejecución sigue pendiente** (no es sourceable). Lo que sí quedó verificado es el contexto: ES6/ES2015 especifica proper tail calls, y el hilo de TC39 donde el equipo de JavaScriptCore defiende la versión implícita confirma que **Safari/JSC las implementó** según la spec.[^tc39_ptc] Lo que **no** pude verificar con fuente primaria es el estado en V8/Node —la creencia difundida es que V8 las implementó y las volvió a sacar, pero eso sale de blogs personales, no del tracker de V8: buscar en `bugs.chromium.org` / `v8.dev` antes de afirmarlo en el post. Si el snippet revienta en Node, ése es el dato empírico que importa igual.]

> 🕳️ **HUECO — necesita a César:** ¿tuviste alguna vez que enseñar o explicar esto —lambda como mecanismo de control— a alguien que venía de un lenguaje imperativo? ¿Qué fue lo que hizo clic, y qué fue lo que no entró nunca? Sirve como sección propia y no sólo como anécdota.

### El corolario que es el verdadero punto

Ahora, si todo esto es cierto, hay una consecuencia que muerde: **la llamada a procedimiento tiene que ser barata**. Obligatoriamente. Si es cara, no podés permitirte que tu loop sea una llamada, y todo el argumento se vuelve un juego de salón.

Por eso el paper no es sólo una pieza de expresividad; es también una pieza de ingeniería de compiladores. La tesis «todo es una llamada» y la exigencia «las llamadas en posición de cola no crecen la pila» son la misma afirmación mirada de los dos lados. Scheme es el lenguaje que se tomó eso en serio y lo puso en la especificación: no es una optimización que el compilador puede hacer si tiene ganas, es una propiedad del lenguaje con la que podés contar. Y está escrito con esas palabras — el R7RS le dedica la sección 3.5 entera, titulada «Proper Tail Recursion», y la regla es de una línea: «Implementations of Scheme are required to be *properly tail-recursive*.»[^r7rs] No «se recomienda»: *required*.

Y ahí se cierra el círculo con el clima de los setenta. La respuesta al «llamar es caro» no fue defender la abstracción a pesar del costo. Fue mostrar que el costo era un artefacto de cómo estábamos compilando, no una ley de la naturaleza — y que si compilás bien, la abstracción es gratis. Es exactamente el mismo tipo de movimiento que cuento en [[B-03]]: lo que parecía un límite del universo era una decisión de implementación.

### Por qué el paper no envejeció

Cincuenta años después, esto no es historia: es el interior de las herramientas que usás.

Cuando un compilador moderno pasa tu programa a **continuation-passing style** para optimizarlo, está usando esta tesis como representación intermedia: si todo es una llamada, alcanza con saber optimizar llamadas. Cuando pasa a **SSA** —cada variable se asigna una sola vez, y los bloques básicos reciben sus valores como parámetros— está describiendo un programa donde los bloques son procedimientos y los saltos son llamadas con argumentos. Que es, palabra por palabra, el ejemplo 2 de más arriba.

Y esto último tiene literatura propia, no es una analogía mía. Richard Kelsey lo demostró en 1995 en un paper que se llama, sin vueltas, *A Correspondence between Continuation Passing Style and Static Single Assignment Form*: «We define syntactic transformations that convert continuation passing style (CPS) programs into static single assignment form (SSA) and vice versa.»[^kelsey] Tres años después Andrew Appel lo puso en el título directamente —*SSA is Functional Programming*— y lo mostró en la correspondencia más concreta posible: las funciones φ del SSA son los parámetros formales de las funciones del programa funcional. «Wherever there is a formal parameter of a function (in the functional form), there is a φ-function (in the SSA form).»[^appel]

Un detalle honesto que conviene no comerse: Kelsey aclara que la traducción no es total en un sentido. «Some CPS programs cannot be converted to SSA, but these are not produced by the usual CPS transformation.»[^kelsey] Así que la frase correcta es «mutuamente traducibles en la práctica», no «son la misma cosa».

Y del lado del programador, la herencia es todavía más visible, aunque nadie la nombre: cada vez que escribís un callback, un `Promise`, un `async/await`, un generador con `yield`, estás reificando el resto del cómputo y pasándolo como valor. Estás haciendo lo del paper. Lo que en 1976 era una demostración teórica publicada en un memo del AI Lab, hoy es el estilo por defecto de la programación web, y llegó ahí sin que casi nadie supiera de dónde venía.

> 🕳️ **HUECO — necesita a César:** ¿esto te sirvió alguna vez en trabajo real, o lo tenés archivado como cultura general de la que uno se enorgullece? Cualquiera de las dos respuestas es buena para el post; la segunda incluso mejor, porque es la honesta para la mayoría de la gente. Si hubo un caso concreto —en Santa Fe o donde sea— donde pensar «esto es una llamada a procedimiento» te destrabó un problema, ése es el párrafo que le falta al post.

> 🕳️ **HUECO — necesita a César:** ¿escribiste alguna vez un intérprete o un compilador propio, aunque haya sido de juguete? Si sí, ¿el manejo de control lo hiciste con este enfoque o a la manera imperativa? Es la anécdota que mejor cerraría la sección de compiladores.

### Lo que me llevo

Que no existen los constructos de control.

Existe uno solo, y le pusimos veinte nombres distintos. `while`, `for`, `do`, `goto`, `break`, `continue`, `return`, `throw`, `catch`, `yield`, `await`: veinte palabras reservadas, veinte entradas en la gramática, veinte páginas de manual — para lo que en el fondo es una única operación, aplicar un procedimiento a unos argumentos, mirada desde ángulos distintos.

Eso es lo que hace que este paper siga vivo. No te enseña una técnica que vayas a usar el lunes. Te saca una capa de encima: donde antes veías un catálogo de herramientas que hay que memorizar, empezás a ver una sola idea repetida con disfraces. Y eso, que suena a filosofía, tiene una consecuencia muy práctica — es la diferencia entre aprender un lenguaje nuevo memorizando su tabla de constructos, o entrar preguntando cómo escribió éste la única cosa que hay.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto en una o dos frases. ¿Es *Lambda: The Ultimate Imperative* un paper que le recomendarías leer a alguien hoy, o es de esos que conviene conocer de oídas porque el argumento ya está absorbido en todas partes y el original se lee incómodo?

---

[^lti]: Guy Lewis Steele Jr. y Gerald Jay Sussman, [*LAMBDA: The Ultimate Imperative*](https://dspace.mit.edu/handle/1721.1/5790), MIT Artificial Intelligence Laboratory, AI Memo No. 353, 10 de marzo de 1976, 40 páginas. Escaneo del original en [bitsavers](https://www.bitsavers.org/pdf/mit/ai/aim/AIM-353.pdf) (verificado: 40 páginas contadas con `pypdf`). Backup Wayback del registro del MIT: [snapshot 2026-05-10](http://web.archive.org/web/20260510053942/https://dspace.mit.edu/handle/1721.1/5790); del PDF de bitsavers: [snapshot 2024-06-05](http://web.archive.org/web/20240605070111/http://bitsavers.org/pdf/mit/ai/aim/AIM-353.pdf). — estable.

[^lti_transcripcion]: [*LAMBDA: The Ultimate Imperative* — transcripción HTML](https://research.scheme.org/lambda-papers/lambda-papers-ltu-imperative.html), research.scheme.org. Transcripción navegable con el índice de secciones y el abstract completo; útil para citar sin abrir el escaneo. — frágil (sin snapshot en Wayback al 2026-07-15: lo consulté y no hay ninguno; si el post se apoya en esta URL, pedir el archivado antes de publicar).

[^chm]: [SCHEME family — Software Preservation Group](https://softwarepreservation.computerhistory.org/LISP/scheme_family.html), Computer History Museum. Catálogo de los AI Memos de Scheme con autoría, número de memo, fecha y cantidad de páginas de cada uno (es la fuente que da «40 pages» para el AIM-353). — estable.

[^readscheme]: [The Original 'Lambda Papers' by Guy Steele and Gerald Sussman](https://conservatory.scheme.org/readscheme/page1.html) — bibliografía de readscheme (la que el draft citaba como `library.readscheme.org`; el mirror vivo está en conservatory.scheme.org). — frágil.

[^lambdapapers]: [The Lambda Papers](https://research.scheme.org/lambda-papers/), research.scheme.org. Índice de la serie; incluye dos piezas que el catálogo del CHM no lista en la serie (*Compiler Optimization Based on Viewing LAMBDA as RENAME plus GOTO*, 1977, y la tesis *RABBIT*, AITR-474, 1978). — frágil.

[^goto]: Guy Lewis Steele Jr., [*Debunking the "Expensive Procedure Call" Myth; or, Procedure Call Implementations Considered Harmful; or, LAMBDA: The Ultimate GOTO*](https://dspace.mit.edu/handle/1721.1/5753), MIT AI Laboratory, AI Memo No. 443, octubre de 1977, 23 páginas. Backup Wayback: [snapshot 2026-04-06](http://web.archive.org/web/20260406130250/http://dspace.mit.edu/handle/1721.1/5753). Es el memo que trae el encuadre del «llamar es caro» y la frase «GOTO statements which also pass parameters». Transcripción HTML: [research.scheme.org](https://research.scheme.org/lambda-papers/lambda-papers-ltu-goto.html) (frágil). — estable.

[^goto_acm]: Versión publicada en actas: Guy Lewis Steele Jr., «Debunking the "expensive procedure call" myth; or, procedure call implementations considered harmful; or, LAMBDA: The Ultimate GOTO», *Proceedings of the 1977 Annual Conference (ACM '77)*, ACM Press, 1977, pp. 153-162. DOI: [10.1145/800179.810196](https://doi.org/10.1145/800179.810196) (ficha verificada vía `api.crossref.org`; el landing de la ACM DL no se puede fetchear). Mirror libre de texto completo: [copia en la cátedra CMPT 383 de Simon Fraser University](https://www2.cs.sfu.ca/CourseCentral/383/havens/pubs/lambda-the-ultimate-goto.pdf) — de ahí extraje el texto citado. — DOI estable; el mirror de SFU es frágil y **no tiene snapshot en Wayback** (lo consulté el 2026-07-15): si el post cita el mirror, archivarlo antes.

[^kelsey]: Richard A. Kelsey, «A Correspondence between Continuation Passing Style and Static Single Assignment Form», *ACM SIGPLAN Notices*, vol. 30, n.º 3, marzo de 1995, pp. 13-22 (actas del *ACM SIGPLAN Workshop on Intermediate Representations*, IR'95). DOI: [10.1145/202530.202532](https://doi.org/10.1145/202530.202532) (ficha verificada vía `api.crossref.org`). Copia de texto completo verificada: [PDF](https://bernsteinbear.com/assets/img/kelsey-ssa-cps.pdf) — frágil (blog personal). — DOI estable.

[^appel]: Andrew W. Appel, «SSA is Functional Programming», *ACM SIGPLAN Notices*, vol. 33, n.º 4, abril de 1998, pp. 17-20 (columna Functional Programming). DOI: [10.1145/278283.278285](https://doi.org/10.1145/278283.278285) (ficha verificada vía `api.crossref.org`). Copia del propio autor: [cs.princeton.edu/~appel/papers/ssafun.pdf](https://www.cs.princeton.edu/~appel/papers/ssafun.pdf), backup Wayback: [snapshot 2026-07-09](http://web.archive.org/web/20260709171212/https://www.cs.princeton.edu/~appel/papers/ssafun.pdf). — estable.

[^r7rs]: [*Revised⁷ Report on the Algorithmic Language Scheme*](https://standards.scheme.org/corrected-r7rs/r7rs-Z-H-5.html), sección 3.5 «Proper Tail Recursion». Edición corregida en standards.scheme.org; [PDF oficial](https://standards.scheme.org/official/r7rs.pdf) (88 pp., eds. Alex Shinn, John Cowan, Arthur A. Gleckler; §3.5 verificada en el índice del PDF). — estable.

[^tc39_ptc]: [Response to the proposal to add explicit tail call syntax to ECMAScript](https://github.com/tc39/ecma262/issues/535) — issue #535 del repositorio de la especificación de ECMAScript (TC39), donde el equipo de JavaScriptCore argumenta contra la sintaxis explícita de tail calls y deja constancia de que Safari ya implementó las tail calls tal como las especifica ES6. — estable (repo oficial de TC39).

**Estado actual:**

> ⚠️ **PREMISA EN DUDA** (pasada de fuentes, 2026-07-15). El argumento central del post —que todo constructo de control es una llamada a procedimiento— **se sostiene y está bien respaldado por el memo**. Lo que no se sostiene son tres datos concretos del Hook y el Concepto, que no toqué por ser de César pero que hay que arreglar antes de publicar:
>
> 1. **Autoría.** El Concepto dice «Guy L Steele, 1976» y el Hook «lo demostró Guy Steele». El AIM-353 es de **Steele y Gerald Jay Sussman en coautoría**, confirmado por cuatro fuentes independientes (escaneo del MIT, catálogo del Computer History Museum, transcripción de research.scheme.org, bibliografía de readscheme).[^lti] [^chm] [^readscheme] [^lti_transcripcion]
> 2. **«Un paper de 19 páginas».** Son **40**. Conté el escaneo original de bitsavers con `pypdf` (40 páginas exactas); coinciden el CHM («40 pages») y el índice DjVu de Wikisource (40 de escaneo, cuerpo hasta la 39). No hay lectura bajo la cual dé 19.[^lti] [^chm]
> 3. **«Cualquier try/catch».** El Hook promete `try/catch` y el Concepto habla de «exception handlers». El abstract del AIM-353 enumera lo que el memo modela y **no incluye manejo de excepciones**: lo más cercano son las *escape expressions* (salida anticipada), que no son un mecanismo de errores con handlers.[^lti] [^lti_transcripcion] La extrapolación es defendible como lectura propia, pero no como «lo demostró el paper».
>
> Bonus del mismo hallazgo: **dos de las cosas que el draft le atribuía al 353 son en realidad del AIM-443** (*LAMBDA: The Ultimate GOTO*, 1977): el encuadre del «llamar es caro» y la frase «GOTO que pasa argumentos». El post gana si trabaja los dos memos en vez de uno; la bibliografía ya tiene la ficha del 443.

Seed cosechado de `draft-rest.md` el 2026-04-09, expandido a prosa-borrador el 2026-07-15. Se construyó el outline de nueve puntos desde el Concepto + Hook + Bibliografía y se escribió la prosa contra él (~2000 palabras sin contar código ni marcadores). Lo que está escrito: el encuadre histórico de los Lambda Papers, la tesis (`lambda` como mecanismo de control), los tres ejemplos (loop, `goto`, salida no local) en Scheme y JavaScript, el argumento de que la llamada a procedimiento tiene que ser barata, la herencia hacia CPS/SSA y el cierre.

Lo que queda pendiente antes de publicar:

- **6 huecos** que necesitan a César: cuándo y cómo se cruzó con los Lambda Papers, si tradujo o enseñó esta parte de SICP, si alguna vez escribió un compilador o intérprete con esta arquitectura, qué le pasó la primera vez que vio un loop escrito como llamada recursiva, si le sirvió en trabajo real (sector público) o quedó como cultura, y su veredicto para el cierre.
- **Marcadores `[VERIFICAR:]`: de 11 quedaron 2.** Resueltos en la pasada de fuentes del 2026-07-15: autoría del AIM-353 (Steele **y** Sussman), cantidad de páginas (40, no 19), URL estable del memo (DSpace + bitsavers + backups Wayback), lista canónica de los Lambda Papers (tabla con memo/autores/fecha/páginas en el cuerpo), el encuadre del «llamar es caro» (es del AIM-443, **no** del 353), la frase «GOTO que pasa argumentos» (AIM-443, cita textual), qué construcciones cubre el 353 (las del abstract: recursión simple, iteración, statements compuestos, GO TO y asignación, continuation-passing, escape expressions, fluid variables y los tres mecanismos de pasaje de parámetros — **sin** manejo de excepciones), la relación CPS/SSA (Kelsey 1995 + Appel 1998, con el caveat de Kelsey de que la traducción no es total) y la ficha completa del footnote `[^lti]`.
- **Los 2 marcadores que quedan son los mismos dos: correr los snippets** (el de Scheme y el de `buscar` en JS). No son sourceables — piden ejecución, no bibliografía —, así que sobreviven a propósito. Lo que sí se sourceó alrededor: el R7RS §3.5 exige proper tail recursion,[^r7rs] y el issue #535 de TC39 confirma que Safari/JSC implementó las tail calls de ES6.[^tc39_ptc] El estado de V8/Node quedó **sin fuente primaria** (buscar en `v8.dev` / `bugs.chromium.org`; los blogs no alcanzan).
- **6 huecos** que necesitan a César, intactos: cuándo y cómo se cruzó con los Lambda Papers, qué le pasó la primera vez que vio un loop escrito como llamada recursiva en posición de cola, si enseñó esto a gente que venía de lenguajes imperativos, si le sirvió en trabajo real (sector público) o quedó como cultura, si escribió alguna vez un intérprete o compilador propio y con qué enfoque, y su veredicto para el cierre.
- **Imágenes:** sigue en `_a definir_` — falta al menos la pieza de portada.
- **Bibliografía:** pasó de 3 entradas (una sola primaria) a **11 fichas verificadas**, todas fetcheadas: los dos memos (353 y 443) con backup en Wayback, la versión en actas del 443 con DOI verificado vía Crossref + mirror libre de SFU, tres catálogos de la serie, Kelsey y Appel para CPS/SSA, el R7RS y el issue de TC39. Descartadas por no resolver o no aportar: ResearchGate y DeepDyve (no dan texto verificable), Wikipedia (contexto, no cita primaria por regla de la casa), y `library.readscheme.org` tal como lo citaba el draft (el mirror vivo es `conservatory.scheme.org/readscheme/`). [[tr-14]] sigue sin respaldar ninguna afirmación concreta de este post.
- **Riesgo de bitrot a atender antes de publicar:** la transcripción de research.scheme.org y el mirror del 443 en la cátedra de SFU son frágiles y **no tienen snapshot en Wayback** (verificado el 2026-07-15). Si el post se apoya en cualquiera de las dos, hay que pedir el archivado primero.
