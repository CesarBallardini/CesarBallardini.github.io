### B-05 — Trampolines: saltar para no apilar

- **Archivo seed:** `dev/draft-trampoline.md`
- **Slug propuesto:** `trampolines-saltar-para-no-apilar`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-trampolines-saltar-para-no-apilar/index.md`
- **Serie:** B
- **Cross-links:** depende de [[B-04]]; lleva a [[A2-02]] (Lambda papers, donde aparece el truco), [[B-02]] (Okasaki, otra manera de no apilar)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1200-1500 palabras)

**Concepto:** un trampoline es la manera de simular tail call optimization en un lenguaje que no la tiene. La función recursiva no se llama a sí misma directamente; devuelve una *thunk* que el trampoline después invoca. Resultado: stack flat aunque tu lenguaje (Java, Python, JS pre-ES6 sin TCO) no coopere.

**Hook:** "Java no optimiza tail calls. Por lo tanto Java no puede hacer recursión profunda. ERROR. Java *sí* puede hacer recursión arbitrariamente profunda, sólo que tenés que enseñarle el truco. Se llama trampoline, y cabe en 10 líneas."

**Outline:**
1. El problema: lenguajes sin TCO + recursión profunda = StackOverflowError.
2. La idea del trampoline: en vez de llamarte recursivamente, devolvé una función que cuando se invoque haga el siguiente paso.
3. La implementación mínima en JavaScript / Java / Python (10 líneas cada una).
4. Ejemplo: factorial mutuo (par/impar) — el caso donde ni tail recursion clásica ayuda.
5. Conexión con CPS: el trampoline es CPS-to-trampolined-style transformation.
6. Cierre: por qué este truco aparece en intérpretes (Lua bytecode dispatcher), parsers (combinator libraries) y otros lugares "lejos" de funcional puro.

**Bibliografía:**
- [Steven E. Ganz, Daniel P. Friedman y Mitchell Wand, *Trampolined Style*, ICFP '99, ACM SIGPLAN, pp. 18-27](https://doi.org/10.1145/317636.317779) — el paper canónico; DOI verificado en Crossref. Mirror libre en la página del propio Wand: `http://www.ccs.neu.edu/home/wand/papers/icfp-99.ps` (PostScript, vivo al 2026-07-16). **estable** (DOI) / mirror **frágil**. El enlace previo a `cs.indiana.edu/~dyb/pubs/stack.pdf` quedó muerto (301 → página del departamento tras el rediseño del sitio de Indiana).
- [Henry G. Baker, *CONS Should Not CONS Its Arguments, Part II: Cheney on the M.T.A.*, ACM SIGPLAN Notices 30(9):17-20, 1995](https://doi.org/10.1145/214448.214454) — el antecedente clásico del truco: traducir Scheme a C en CPS de modo que las funciones nunca retornen, porque «C compilers are not required to be properly tail-recursive». DOI verificado en Crossref. Texto libre en el archivo de Baker: [CheneyMTA.html](https://plover.com/~mjd/misc/hbaker-archive/CheneyMTA.html) (la página propia de Baker en `home.pipeline.com/~hbaker1` no responde). **estable** (DOI) / mirror **frágil**.
- [`clojure.core/trampoline` (ClojureDocs)](https://clojuredocs.org/clojure.core/trampoline) — firma `(trampoline f)` / `(trampoline f & args)`; presente desde Clojure 1.0; su docstring lo describe como forma de «convert algorithms requiring mutual recursion without stack consumption». **estable**.
- [Special Forms — `recur` (clojure.org)](https://clojure.org/reference/special_forms) — confirma que Clojure «has no tail-call optimization» y que `recur` sólo es válido en posición de cola dentro de una misma función (no cubre recursión mutua). **estable**.
- [«Tail call» (Wikipedia)](https://en.wikipedia.org/wiki/Tail_call) — estado real de *proper tail calls* de ES6 en los motores JS. **estable**.
- [Rúnar Bjarnason, *Stackless Scala With Free Monads*, Scala Days 2012](https://blog.higher-order.com/assets/trampolines.pdf) — el trampoline como base de estructuras que no crecen la pila. **frágil**.
- [Jim Duey, *Clojure trampoline tutorial*](https://web.archive.org/web/20150906131833/http://jimduey.com/perm/2010-05-08T15:04:55+00:00.html) — el original desapareció; queda la copia de Wayback. **frágil**. (La documentación oficial de arriba lo reemplaza como fuente primaria.)
- [Continuation-passing style (Wikipedia)](https://en.wikipedia.org/wiki/Continuation-passing_style). **estable**.
- [Roshan James y Amr Sabry, *Yield: Mainstream Delimited Continuations*](https://legacy.cs.indiana.edu/~rpjames/yield.pdf) — pariente conceptual moderno. **frágil** (el host `legacy.cs.indiana.edu` no resolvía al 2026-07-16; falta conseguir un backup vivo).

**Imágenes:**
- _Crear_: animación SVG conceptual (3-4 frames) — la diferencia entre llamada recursiva tradicional (stack crece) y trampoline (stack se mantiene plano) (~45 min).

**Tags propuestos:** `['trampoline', 'tail recursion', 'CPS', 'Java', 'Clojure']`

**Estado actual:** prosa-borrador completa (~1600 palabras de prosa, sin contar código ni marcadores) escrita contra el outline existente, que se respetó punto por punto. Quedó algo por encima del *length target* de 1200-1500: hay margen de recorte en la sección de los tres lenguajes (podría quedarse con JavaScript y Java y mandar Python a una nota) y en el cierre. Lo que está escrito: el problema (lenguaje sin TCO + recursión profunda), la idea del trampoline, implementación mínima en JavaScript / Python / Java, el ejemplo de par/impar mutuo como el caso donde el acumulador de [[B-04]] no alcanza, la conexión con CPS, y el cierre sobre dónde reaparece el truco. Lo que queda pendiente:

- **5 huecos** que necesitan a César: si vio un `StackOverflowError` real en producción, si escribió alguna vez un evaluador/parser/máquina de estados con funciones mutuamente recursivas, si usó `trampoline` de Clojure, su opinión sobre el intercambio legibilidad/robustez, y otro caso donde haya tenido que reconstruir a mano una feature ausente del lenguaje (cierre).
- **8 marcadores `[VERIFICAR:]`** (7 inline + 1 en la footnote del paper): casi todos sobre afirmaciones técnicas que la bibliografía actual no respalda de manera directa (límite de recursión de CPython y profundidad de la JVM, estado real de TCO en ES6/motores —incluida la afirmación «JS pre-ES6 sin TCO» que trae el propio **Concepto:** del draft—, existencia y firma de `clojure.core/trampoline`, qué afirma exactamente el paper de Ganz/Friedman/Wand, el origen del nombre «trampoline», el dispatcher de Lua y el caso de los parser combinators, y si los snippets de código compilan/corren tal cual están).
- Los tres snippets (JS/Python/Java) son míos, no salen de ninguna fuente de la bibliografía; están sin ejecutar. Correrlos es requisito para publicar.
- Falta la animación SVG de la sección **Imágenes:** — es la pieza que hace el post.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch: DOIs de Ganz/Friedman/Wand y de Baker confirmados en Crossref, mirrors libres localizados, y se agregó el antecedente de Baker 1995 más la documentación oficial de Clojure y de ECMAScript/TCO) y se resolvieron 2 de 7 marcadores `[VERIFICAR:]` por completo (el estado real de TCO en los motores JS y la ficha del paper de Ganz/Friedman/Wand) más 2 de forma parcial (qué afirma el paper —confirmado el abstract, no el cuerpo— y la parte de Clojure del marcador de cierre). Quedan 3 abiertos: los dos que exigen correr código (límites de recursión de CPython/JVM y compilar los snippets) y el del origen del término «trampoline» (ni Wikipedia ni las fuentes fetcheadas documentan quién lo acuñó ni la metáfora del rebote como etimología). El enlace de Ganz a `cs.indiana.edu/~dyb/pubs/stack.pdf` estaba muerto y se reemplazó por DOI + mirror de Wand.

---

## Borrador de prosa

Hay una frase que se repite en cualquier discusión sobre recursión, y que es medio verdad y medio mentira: «Java no optimiza tail calls, así que en Java no podés hacer recursión profunda».

La primera mitad es cierta. La segunda no. Java puede hacer recursión arbitrariamente profunda —millones de niveles, si te dan ganas— sin tocar el compilador, sin flags de JVM, sin trucos sucios. Sólo hay que enseñarle un movimiento que tiene nombre propio, cabe en unas diez líneas, y se llama **trampoline**. Voy a contarte cómo funciona, porque es una de esas ideas que, una vez que la ves, la empezás a ver en todos lados: en intérpretes, en parsers, en librerías que juran no tener nada que ver con programación funcional.

### El problema: la pila no es infinita

Recapitulemos rápido lo que vimos en [[B-04]]. Cuando una función se llama a sí misma, la máquina tiene que anotar en algún lado dónde volver cuando la llamada termine. Ese «algún lado» es la pila de llamadas, y cada nivel de recursión le apila un frame más.

Si la llamada recursiva está en **posición de cola** —o sea, es lo último que la función hace, y su resultado es directamente el resultado de la función, sin ningún cálculo pendiente encima— entonces ese frame no hace falta. No hay nada a lo que volver. Un compilador que lo sabe reemplaza la llamada por un salto y reutiliza el frame que ya está. Eso es tail call optimization: Scheme la exige, ML y Erlang la hacen, Clojure la hace explícita con `recur`.

Java no.[^wiki_trampoline] Python tampoco, y encima Guido lo explicó públicamente en su momento: no es un olvido, es una decisión. Así que podés escribir tu función perfectamente tail-recursiva, con acumulador y todo, hecha un primor de disciplina funcional, y a los pocos miles de niveles te vuela con un `StackOverflowError` (o un `RecursionError`, según el idioma en que grite tu runtime). La transformación de [[B-04]] te dejó el código en la forma correcta; el lenguaje simplemente se niega a aprovecharla.

[VERIFICAR: el límite de recursión por defecto de CPython (`sys.getrecursionlimit()`) y el orden de magnitud de la profundidad a la que revienta una JVM con stack por defecto. No pegar números de memoria: correr ambos y reportar lo que salga, aclarando versión y plataforma.]

> 🕳️ **HUECO — necesita a César:** ¿te comiste alguna vez un `StackOverflowError` o un `RecursionError` en un sistema real, no en un ejercicio? Con el contexto mínimo alcanza (qué estaba recorriendo el código: un árbol, un grafo, un parser) y con lo que hiciste para salir del paso. Es el párrafo que baja todo esto de la teoría al martes a la tarde.

### La idea: no te llames, devolvé la llamada

Acá viene el movimiento, y es más un cambio de modales que un algoritmo.

El problema de la recursión es que la función **se llama a sí misma**, y por eso la pila crece: la llamada de adentro tiene que terminar para que la de afuera pueda devolver. La solución del trampoline es que la función **no se llame**. En vez de llamarse, devuelve —como resultado normal, como quien devuelve un entero— una *thunk*: un paquetito sin argumentos que, cuando alguien lo invoque, va a hacer el paso siguiente.

Fijate lo que cambia. La función ahora termina. Termina de verdad: su frame se destruye, la pila vuelve a donde estaba. Y devuelve un objeto que dice «el trabajo no está listo, pero acá tenés lo que hay que hacer después».

Alguien tiene que invocar esa thunk. Ese alguien es el trampoline: un loop tonto, en el nivel de afuera, que recibe el resultado, ve que es una función y no un valor, la invoca, recibe otra función, la invoca de nuevo, y así hasta que finalmente le llega algo que no es una función. Eso es el resultado.

De ahí el nombre, que es la mejor metáfora de todo el asunto: cada paso del cómputo **rebota** contra el loop de afuera. Sube, toca, vuelve. La pila nunca crece más de un nivel, porque siempre es el mismo trampoline el que está llamando, desde la misma altura. La recursión se volvió iteración sin que vos reescribieras la lógica como un `while`.

[VERIFICAR: si el paper de Ganz, Friedman y Wand —o el artículo de Wikipedia— documenta el origen del término «trampoline» y la metáfora del rebote, o si es folclore posterior. El párrafo de arriba afirma el porqué del nombre; si no hay fuente, hay que reescribirlo como lectura mía y no como etimología.]

### Diez líneas, tres lenguajes

En JavaScript sale casi solo, porque las funciones son valores y no hay ceremonia:

```js
function trampoline(fn) {
  return function (...args) {
    let resultado = fn(...args);
    while (typeof resultado === 'function') {
      resultado = resultado();
    }
    return resultado;
  };
}

const sumaHasta = (n, acc = 0) =>
  n === 0 ? acc : () => sumaHasta(n - 1, acc + n);

trampoline(sumaHasta)(1000000);
```

Mirá la única diferencia con la versión que explota: donde antes decía `sumaHasta(n - 1, acc + n)`, ahora dice `() => sumaHasta(n - 1, acc + n)`. Seis caracteres. Eso es todo el truco: en vez de hacer el paso, describilo.

Python es igual de directo:

```python
def trampoline(f, *args):
    r = f(*args)
    while callable(r):
        r = r()
    return r

def suma_hasta(n, acc=0):
    if n == 0:
        return acc
    return lambda: suma_hasta(n - 1, acc + n)

trampoline(suma_hasta, 1_000_000)
```

Java necesita más ropa, porque hay que decirle al sistema de tipos qué es «un valor o un paso pendiente», pero la idea es idéntica:

```java
@FunctionalInterface
interface Trampoline<T> {
    Trampoline<T> saltar();

    default boolean aterrizo() { return false; }
    default T valor() { throw new IllegalStateException("todavía saltando"); }

    default T correr() {
        Trampoline<T> t = this;
        while (!t.aterrizo()) t = t.saltar();
        return t.valor();
    }

    static <T> Trampoline<T> listo(T v) {
        return new Trampoline<T>() {
            public Trampoline<T> saltar() { throw new IllegalStateException(); }
            public boolean aterrizo() { return true; }
            public T valor() { return v; }
        };
    }
}
```

Y con eso, sumar hasta un millón en Java corre. No porque la JVM haya aprendido nada: corre porque le sacamos el trabajo de encima y lo pusimos en un `while`. Eso es lo que quiere decir «simular TCO a mano».

[VERIFICAR: compilar y correr los tres snippets antes de publicar (Java 17+, Python 3.11+, Node LTS), y ajustar el texto a lo que efectivamente pase. No publicar código no ejecutado.]

Un paréntesis sobre JavaScript, porque suele confundir: ES6 (ES2015) *sí* especificó proper tail calls, pero de los motores mayoritarios sólo los implementó Safari/JavaScriptCore; V8 (Chrome/Node) y SpiderMonkey (Firefox) los rechazaron y nunca los enviaron.[^es6tco] Por eso el trampoline sigue haciendo falta también en JS en todos lados menos en Safari, aunque el estándar diga otra cosa.

### El caso donde el acumulador no te salva: par e impar mutuos

Hasta acá podrías decirme, con razón, que para sumar hasta un millón escribís un `for` y listo. Cierto. Así que vamos al ejemplo donde el trampoline gana de verdad: **recursión mutua**.

```python
def es_par(n):
    if n == 0:
        return True
    return lambda: es_impar(n - 1)

def es_impar(n):
    if n == 0:
        return False
    return lambda: es_par(n - 1)

trampoline(es_par, 1_000_000)
```

Es un algoritmo idiota para saber si un número es par —hay un operador para eso— pero es el esqueleto de algo que no es idiota para nada: dos o más funciones que se llaman entre sí en posición de cola, cada una haciendo un pedazo del trabajo. Un evaluador que alterna entre `eval` y `apply`. Un parser que alterna entre reglas gramaticales. Una máquina de estados donde cada estado es una función que devuelve el estado siguiente.

Y acá está el punto: la receta de [[B-04]] —«agregale un acumulador y convertilo en tail call»— no te sirve. Estas funciones **ya están** en posición de cola. No hay nada que acumular, no hay nada que reordenar; el problema no es la forma de tu código, es que el lenguaje no cumple. Y reescribir a mano el ida y vuelta entre **es_par/1** y **es_impar/1** como un solo `while` te obliga a fusionar dos funciones en una y a llevar vos el estado de cuál toca ahora: perdiste exactamente la claridad por la que las habías escrito separadas.

El trampoline te deja las dos funciones tal cual, cada una diciendo su parte, y le da el `while` a otro. Esa es la venta.

> 🕳️ **HUECO — necesita a César:** ¿escribiste alguna vez un evaluador, un parser o una máquina de estados donde tuviste dos o más funciones llamándose entre sí? Si tenés un caso concreto, reemplaza al par/impar como ejemplo motivador y el post mejora muchísimo.

### El pariente que estaba escondido: CPS

Si te suena de algún lado, es porque lo es.

Cuando escribís `return lambda: es_impar(n - 1)` estás haciendo algo muy parecido a lo que hace una transformación a **continuation-passing style**: en vez de dejar que el runtime maneje implícitamente «qué viene después», lo estás haciendo explícito, empaquetado en una función, como un dato que se puede devolver, guardar, pasar.[^cps] En CPS le pasás a cada función la continuación; en estilo trampolinado la devolvés. Es la misma idea de fondo —el resto del cómputo, reificado— con la plomería puesta al revés. Ese mismo movimiento —traducir a CPS para que las funciones nunca tengan que retornar— es el que Henry Baker propuso ya en 1995 para compilar Scheme a C, otro lenguaje que no garantiza tail calls.[^baker]

Esa es la conexión que hace el paper de Ganz, Friedman y Wand: hay una transformación sistemática, no un truco ad hoc, que lleva de un programa a su versión trampolinada.[^ganz] No es que a alguien se le ocurrió devolver lambdas: es una técnica con teoría atrás, del mismo linaje que los Lambda Papers que vemos en [[A2-02]].

[VERIFICAR: resuelto parcialmente (2026-07-16). Del abstract y de resúmenes secundarios queda confirmado que el paper organiza el programa como un único loop-scheduler donde cada cómputo devuelve al scheduler el trabajo restante, que introduce el nombre «trampolined style» y que lo usa para dar multithreading sin soporte de continuaciones en el lenguaje. Pendiente: el cuerpo del paper no se pudo leer (el mirror es PostScript y no se convirtió a texto), así que falta confirmar la forma exacta de la transformación y su relación formal precisa con CPS antes de afirmarlas como del paper.]

Del otro lado del linaje están las continuaciones delimitadas, que son la manera moderna y respetable de decir lo mismo: el `yield` que usás todos los días en Python o en JavaScript es pariente cercano de todo esto.[^yield] Cuando un generador se suspende y vuelve, está haciendo una versión disciplinada del mismo movimiento: guardar el resto del cómputo en vez de tenerlo colgado de la pila.

### Dónde aparece el truco cuando no lo estás buscando

Lo lindo del trampoline es que no vive solamente en el barrio funcional.

En Scala, Rúnar Bjarnason lo usó como base para construir cómputos que no crecen la pila, y de ahí salió toda una familia de estructuras —free monads y compañía— que en el fondo son trampolines vestidos de gala.[^bjarnason] En Clojure el trampoline viene incorporado en el lenguaje (`clojure.core/trampoline`, desde la 1.0), precisamente porque `recur` sólo funciona en posición de cola dentro de una misma función y no cubre la recursión mutua; su docstring lo describe como la forma de «convertir algoritmos que requieren recursión mutua sin consumir pila».[^clojuretramp] En las librerías de parser combinators, la profundidad de recursión es proporcional a la profundidad de la gramática, y hay más de una que terminó trampolinando por eso mismo. Y en cualquier intérprete de bytecode, el loop de dispatch —traé la instrucción, ejecutala, traé la siguiente— es un trampoline con otro nombre: cada instrucción devuelve el control al loop en vez de llamar a la siguiente.[^wiki_trampoline]

[VERIFICAR: la parte de Clojure quedó resuelta (2026-07-16) contra la documentación oficial —`clojure.core/trampoline` existe con firma `(trampoline f)` / `(trampoline f & args)` desde la 1.0, y `recur` no cubre recursión mutua—. Sigue pendiente: si el dispatcher de bytecode de Lua se describe efectivamente como trampoline en alguna fuente citable o es una analogía mía; y para los parser combinators, identificar una librería concreta que lo haga documentadamente o bajar el tono de la afirmación.]

> 🕳️ **HUECO — necesita a César:** ¿usaste `trampoline` de Clojure alguna vez, o el equivalente en algún otro lenguaje? Aunque haya sido jugando. Si nunca lo usaste en serio, decímelo también: el post puede admitir con toda tranquilidad que es una técnica que conocés y que casi nunca necesitaste, y esa honestidad vale más que fingir cancha.

### Lo que me llevo

El trampoline es, para mí, el ejemplo más limpio de una idea que aparece una y otra vez en esta serie: **cuando el lenguaje no te da lo que necesitás, casi siempre podés construirlo vos, pagando en explicitud lo que el compilador te habría dado gratis.**

Java no te da tail calls; el trampoline te los da, a cambio de que escribas `() =>` en el lugar correcto y de que aceptes un poco de ruido en el tipo de retorno. Es el mismo intercambio que Okasaki hace en [[B-02]] para conseguir estructuras persistentes eficientes sin que el lenguaje coopere: no hay magia, hay diseño y una factura.

Ahora, la factura existe. El código trampolinado es más difícil de leer que el original, el tipo de retorno miente un poco —esa función que dice devolver un número a veces devuelve una función—, y el stack trace, cuando algo se rompe, ya no te cuenta la historia del cómputo: te muestra el `while` del trampoline y nada más. Perdiste el mapa de cómo llegaste hasta acá.

> 🕳️ **HUECO — necesita a César:** ¿te parece que ese intercambio vale la pena, o que un trampoline en un código que van a mantener otros es una elegancia cara? Tu veredicto acá arma el cierre, y me interesa especialmente si tu respuesta es «depende de quién lo mantiene».

> 🕳️ **HUECO — necesita a César:** ¿hay algún otro caso en tu experiencia donde hayas tenido que reconstruir a mano una feature que el lenguaje no te daba? No hace falta que sea sobre recursión. Sería el párrafo que generaliza la lección y cierra el post.

Pero el punto no es que uses trampolines mañana. El punto es más chico y más útil: **la profundidad de la pila no es una propiedad de tu algoritmo, es una propiedad de cómo elegiste ejecutarlo.** El día que entendés eso, «este lenguaje no puede hacer recursión profunda» deja de sonar a límite de la naturaleza y empieza a sonar a lo que realmente es: una decisión de implementación, que podés no acatar.

---

[^ganz]: [Steven E. Ganz, Daniel P. Friedman y Mitchell Wand, *Trampolined Style*, ICFP '99, ACM SIGPLAN, pp. 18-27](https://doi.org/10.1145/317636.317779) — el paper canónico; DOI verificado en Crossref. La URL previa (`cs.indiana.edu/~dyb/pubs/stack.pdf`) quedó muerta; mirror libre del propio Wand en `http://www.ccs.neu.edu/home/wand/papers/icfp-99.ps`.
[^wiki_trampoline]: [Trampoline (computing) en Wikipedia](https://en.wikipedia.org/wiki/Trampoline_(computing)) — contexto general; ojo que el artículo cubre varios sentidos distintos de «trampoline», no sólo el de recursión.
[^bjarnason]: [Rúnar Bjarnason, *Stackless Scala With Free Monads*, Scala Days 2012](https://blog.higher-order.com/assets/trampolines.pdf).
[^duey]: [Jim Duey, *Clojure trampoline tutorial*](https://web.archive.org/web/20150906131833/http://jimduey.com/perm/2010-05-08T15:04:55+00:00.html) — el original desapareció; el link es a la copia de Wayback.
[^cps]: [Continuation-passing style en Wikipedia](https://en.wikipedia.org/wiki/Continuation-passing_style).
[^yield]: [Roshan James y Amr Sabry, *Yield: Mainstream Delimited Continuations*](https://legacy.cs.indiana.edu/~rpjames/yield.pdf) — frágil: el host `legacy.cs.indiana.edu` no resolvía al 2026-07-16.
[^baker]: [Henry G. Baker, *CONS Should Not CONS Its Arguments, Part II: Cheney on the M.T.A.*, ACM SIGPLAN Notices 30(9):17-20, 1995](https://doi.org/10.1145/214448.214454) — DOI verificado en Crossref; texto libre en el [archivo de Baker (CheneyMTA.html)](https://plover.com/~mjd/misc/hbaker-archive/CheneyMTA.html). El paper traduce Scheme a C en continuation-passing style para que las funciones nunca retornen, apoyándose en que «C compilers are not required to be properly tail-recursive».
[^es6tco]: [«Tail call» (Wikipedia)](https://en.wikipedia.org/wiki/Tail_call) — «ECMAScript 6.0 compliant engines should have tail calls which is now implemented on Safari/WebKit but rejected by V8 and SpiderMonkey». Verificado por fetch el 2026-07-16.
[^clojuretramp]: [`clojure.core/trampoline` (ClojureDocs)](https://clojuredocs.org/clojure.core/trampoline) — firma `(trampoline f)` / `(trampoline f & args)`, presente desde Clojure 1.0. Que Clojure «has no tail-call optimization» y que `recur` se verifica en posición de cola figura en [Special Forms](https://clojure.org/reference/special_forms). Verificado por fetch el 2026-07-16.
