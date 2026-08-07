### A1-03 — Forth: el lenguaje hecho para una sola persona

- **Archivo seed:** `dev/draft-forth-language.md`
- **Slug propuesto:** `forth-lenguaje-para-una-persona`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-forth-lenguaje-para-una-persona.md`
- **Serie:** A1
- **Cross-links:** depende de [[tr-23]] (Charles Moore en *Masterminds*); lleva a [[J-03]] (MindForth — Forth como AI), [[A2-04]] (sistemas expertos en BASIC: contraste)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1200-1500 palabras)

**Concepto:** Forth no fue diseñado para escalar equipos. Fue diseñado por Charles Moore para que una persona pueda controlar todo el sistema. Y ahí está su valor: si alguna vez te sentiste "abrumado por la complejidad innecesaria", Forth es el lenguaje que te muestra el otro extremo.

**Hook:** "lo escribió en una tarde para apuntar el telescopio del observatorio" — esa frase casi mítica resume el espíritu de Forth. Después aclaramos qué tan literal es.

**Outline:**
1. Charles Moore en una tarde, en un observatorio, controlando un telescopio. El origen real (no exageremos pero tampoco apaguemos el mito).
2. Cómo se ve un programa Forth: notación postfija, stack de datos, "palabras" definibles.
3. Por qué eso significa que en Forth podés redefinir el lenguaje mismo. El compilador es del tamaño de un párrafo.
4. La filosofía Moore: "si necesitás más de mil líneas, lo estás haciendo mal".
5. Donde sigue vivo: bootloaders (Open Firmware/OpenBoot), PostScript es básicamente Forth con dibujos, embebidos críticos.
6. Cierre: lo que Forth te enseña incluso si nunca lo vas a usar — la diferencia entre simplicidad y facilidad.

**Bibliografía:** (reforzada y verificada por fetch el 2026-07-16)

- [Charles H. Moore, *Forth — The Early Years* (1991)](https://colorforth.github.io/HOPL.html) — el relato del propio Moore sobre el origen del lenguaje, en su sitio (colorForth). Fuente primaria del autor; preferida sobre Wikipedia por convención de la casa. **estable**.
- [Elizabeth D. Rather, Donald R. Colburn y Charles H. Moore, «The Evolution of Forth», *ACM SIGPLAN Notices* 28(3), marzo 1993, pp. 177-199 (HOPL II)](https://doi.org/10.1145/154766.155369) — historia técnica de referencia. DOI canónico **verificado vía CrossRef** (`https://api.crossref.org/works/10.1145/154766.155369`: autores, páginas 177-199, marzo 1993). El texto completo en ACM DL está tras registro; no se encontró un espejo libre estable con URL confirmable (el path `forth.com/resources/evolution/index.html` que circula devuelve 404). **estable** (DOI).
- [Charles H. Moore, *Programming a Problem-Oriented Language* (1970, manuscrito inédito liberado al dominio público)](https://archive.org/details/chuck-moore-forth-book) — el pensamiento previo a Forth en palabras de Moore; copia digital en Internet Archive (subida 2022, dominio público). **estable**.
- [Leo Brodie, *Starting Forth*, FORTH, Inc. / Prentice-Hall, 1981](https://www.forth.com/starting-forth/) — el libro de iniciación canónico, edición oficial libre online. **estable**.
- [Leo Brodie, *Thinking Forth*, 1984 — reimpresión CC BY-NC-SA, ISBN 0-9764587-0-5](http://thinking-forth.sourceforge.net/) — no cómo escribir Forth, sino cómo *pensar* en Forth; PDF libre autorizado. **estable**.
- [FORTH, Inc., «Forth programming language, history and evolution»](https://www.forth.com/resources/forth-programming-language/) — resumen público del origen (NRAO/Kitt Peak, 1971), la etimología y los estándares Forth-79 / Forth-83 / ANS Forth (1994). **estable**.
- [Open Firmware / IEEE 1275-1994](https://www.openfirmware.info/) — documentación del estándar e implementaciones libres (proyecto OpenBIOS); Forth como firmware de arranque. Contexto en [Wikipedia](https://en.wikipedia.org/wiki/Open_Firmware). **estable**.
- [Charles Moore en *Masterminds of Programming*](https://archive.org/details/MastermindsOfProgramming) — entrevista, capítulo «FORTH»; ver [[tr-23]] en el plan editorial. **estable**.
- [Chuck Moore, comentarios y *Fireside Chat*](https://www.ultratechnology.com/moore4th.htm) — transcripciones de charlas de Moore (UltraTechnology); fuente del precepto de las «mil instrucciones». **frágil** (sitio personal antiguo; agregar backup de Wayback antes de publicar).
- [Jupiter Ace en Wikipedia](https://en.wikipedia.org/wiki/Jupiter_Ace) — la microcomputadora que trajo Forth en ROM en vez de BASIC (1982, Jupiter Cantab). **estable**.
- [comp.lang.forth en Google Groups](https://groups.google.com/g/comp.lang.forth) — archivo de la comunidad. **frágil**.
- [[tr-07]] (Hickey, *Simple Made Easy*) — para enlazar la idea "simple ≠ fácil" con la filosofía de Forth.

**Imágenes:**
- _Wikimedia_: [Jupiter Ace computer](https://commons.wikimedia.org/wiki/File:Jupiter_ACE.jpg) — license: CC-BY-SA — foto de la maquinita que llevaba Forth en ROM.
- _Wikimedia_: foto de Charles Moore (revisar Commons; si no, usar screenshot de su charla con atribución).
- _Crear_: SVG didáctico de un stack Forth ejecutando `2 3 + .` paso a paso (~30 min con Excalidraw).

**Tags propuestos:** `['Forth', 'Charles Moore', 'stack', 'concatenative', 'simplicidad']`

**Estado actual:** El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 10 de 13 marcadores [VERIFICAR:]. Resueltos con fuente confirmada: el origen real (NRAO/Kitt Peak, 1971, Honeywell 316, radiotelescopio de 36 pies) desmontando el «una tarde» sin tocar el hook-como-mito; la etimología «FOURTH → FORTH» (límite de 5 caracteres en Mohasco, 1968); el tamaño del núcleo (3-8 KB, según el propio Moore); la fuente y la palabra exacta del precepto (**«mil instrucciones»**, no «líneas», de las charlas de Moore en UltraTechnology, no de *Masterminds* ni de *The Early Years*); Open Firmware (IEEE 1275-1994, «OpenBoot» = la implementación de Sun, más Apple/PowerPC e IBM); y la ficha de la Jupiter Ace (1982, Jupiter Cantab, Altwasser y Vickers, Forth en ROM de 8 KB). Además se corrigió la URL de la footnote `[^moore]` (apuntaba a la página de FORTH Inc.; ahora apunta al relato propio de Moore en colorForth) y se agregó fuente primaria para Open Firmware (openfirmware.info) por sobre Wikipedia. **Quedan 3 marcadores sin resolver, por falta de fuente o de ejecución:** correr los ejemplos en gforth (no ejecutado), la afirmación «PostScript es básicamente Forth» (ninguna fuente fetcheada la respalda — sigue pendiente decidir entre conseguir fuente o rebajar a analogía declarada), y el uso de Forth en misiones espaciales / embebidos críticos (sin fuente concreta todavía).

El seed original tenía sólo título. El 2026-07-15 se escribió un borrador de prosa completo (~1450 palabras efectivas, dentro del `Length target: medium`) siguiendo el outline de 6 puntos que ya estaba en el draft, en la sección «Borrador de prosa» al pie. El outline no se tocó: ya era real.

Lo que quedó **escrito**: el arco entero — el origen (con el mito del telescopio tratado como mito, no como dato), la mecánica de la notación postfija y el stack, la idea central de que en Forth el diccionario *es* el lenguaje y por eso se redefine solo, la filosofía Moore de las mil líneas, la supervivencia en firmware y embebidos, y el cierre sobre simple ≠ fácil enganchado a [[tr-07]]. El argumento se sostiene solo.

Lo que quedó como **hueco**:

- 6 huecos `🕳️` pidiendo a César material propio: si alguna vez escribió Forth, si se cruzó con el prompt `ok` de OpenBoot en máquinas Sun (candidato fuerte por su historia en el sector público santafesino, pero **no verificado** — el hueco pregunta, no afirma), si leyó *Thinking FORTH*, la reacción personal al precepto de las mil líneas, y el veredicto del cierre.
- 13 marcas `[VERIFICAR:]` sobre datos que la bibliografía listada no respalda tal como están escritos: el episodio del telescopio y el observatorio (el hook del post depende de él y **hay que leer el relato de Moore antes de publicar**), el año y el contexto institucional del origen, la etimología «Forth ← Fourth» y la restricción de nombres de archivo, la formulación exacta y la existencia de la cita de las mil líneas, el tamaño real de un núcleo Forth, qué máquinas embarcaron Open Firmware y en qué años, la relación entre PostScript y Forth (afirmada en el outline, **no respaldada por ninguna fuente del draft**), la ficha del Jupiter Ace (año, autores, ROM), el uso de Forth en misiones espaciales, y la ejecución real de los ejemplos de código.

Decisiones pendientes antes de publicar:

1. **El punto 5 del outline menciona PostScript** y la bibliografía no tiene ninguna fuente sobre PostScript. O se suma una fuente verificada al plan, o el párrafo se recorta a una analogía declarada como analogía. El borrador lo dejó marcado, no resuelto.
2. La afirmación del hook («lo escribió en una tarde para apuntar el telescopio») está escrita **como mito citado**, no como hecho. Si el relato de Moore la contradice, el hook se cae y hay que reescribir la apertura.
3. Los ejemplos de Forth del borrador están escritos de memoria y **no fueron ejecutados**. Correrlos en gforth y corregir antes de publicar.
4. `**Imágenes:**` ya tiene candidatos; falta confirmar que exista foto de Charles Moore con licencia clara en Commons y hacer el SVG del stack.


---

## Borrador de prosa

Hay una frase que circula sobre Forth y que es casi un cuento de fogón: que Charles Moore lo escribió en una tarde, en un observatorio, para poder apuntar un telescopio. Me encanta esa frase. Y desconfío de esa frase. Las dos cosas al mismo tiempo.

Desconfío porque ningún lenguaje se escribe en una tarde, y porque las anécdotas fundacionales de la computación tienen una tendencia bien documentada a mejorar con cada repetición. Pero me encanta porque, aun si es exagerada, apunta a algo verdadero: Forth es el único lenguaje que conozco que fue diseñado explícitamente para que **una sola persona** pueda tener el sistema entero en la cabeza. No un equipo. No una organización. Una persona, sentada frente a una máquina, que necesita que la máquina haga algo esta tarde.

Y eso lo convierte en el espejo exacto de casi todo lo que hacemos hoy.

El relato del propio Moore desactiva la parte literal del mito y confirma la verdadera. Forth no nació en una tarde: fue la decantación de más de una década de intérpretes que Moore fue puliendo de trabajo en trabajo —MIT, Stanford, la empresa Mohasco— a lo largo de los años sesenta.[^moore] Y sí, hubo un telescopio real: en 1971, en el National Radio Astronomy Observatory (NRAO) de Kitt Peak, Arizona, Moore escribió la primera implementación completa y autónoma de Forth para programar una minicomputadora Honeywell 316 que debía controlar un nuevo banco de filtros del radiotelescopio de 36 pies. Ese sistema apuntaba y seguía el telescopio, grababa los datos en cinta magnética y manejaba una terminal gráfica interactiva donde el astrónomo analizaba lo ya registrado.[^moore][^forthhistory]

Así que el telescopio es verdad y el observatorio es verdad. Lo que es folklore es «una tarde»: lo que se cuenta como un gesto instantáneo fue en realidad el punto de llegada de años de trabajo de una sola persona sobre la misma idea. Y esa, si se la mira bien, es una versión más fuerte del mito, no más débil.

La etimología —esa historia demasiado buena— también resultó cierta. Moore quería «FORTH» por *fourth-generation software*, software de cuarta generación; pero el sistema operativo que usaba en Mohasco, allá por 1968, no aceptaba nombres de archivo de más de cinco caracteres, así que «FOURTH» perdió la «U» y quedó «FORTH».[^moore][^forthhistory] La grafía en mayúsculas persistió durante los años setenta porque los dispositivos de entrada/salida de la época sólo tenían caja alta; «Forth» se volvió la forma habitual recién cuando las minúsculas se generalizaron.[^forthhistory]

### Cómo se ve

Antes de la filosofía, la mecánica, porque sin la mecánica la filosofía no se entiende.

Forth no usa paréntesis ni precedencia de operadores. Usa un stack y notación postfija: primero los datos, después la operación. Escribís esto:

```forth
2 3 + .
```

y la máquina hace, literalmente, esto: pone el `2` en el stack, pone el `3` arriba del `2`, el `+` saca los dos de arriba y deja la suma en su lugar, y el `.` saca lo que haya arriba y lo imprime. Sale un `5`.[VERIFICAR: correr los ejemplos de este post en gforth antes de publicar, y transcribir la salida real del intérprete —incluido el `ok`— en vez de escribirla de memoria.]

No hay evaluador de expresiones. No hay árbol sintáctico. No hay reglas de precedencia que memorizar. Hay un stack, y palabras que lo manipulan, y se ejecutan de izquierda a derecha en el orden en que las leés. Eso es todo el modelo de ejecución.

Y ahora la parte que importa: vos podés definir palabras nuevas.

```forth
: cuadrado  dup * ;
5 cuadrado .
```

`dup` duplica lo de arriba del stack; `*` multiplica los dos de arriba. Entre `:` y `;` definiste una palabra que se llama `cuadrado`, y desde ese momento `cuadrado` **es parte del lenguaje**. No es una función que llamás desde el lenguaje. Es una palabra más, indistinguible de `+` o de `dup`, con los mismos derechos.

*Starting FORTH*, de Leo Brodie,[^starting] es el libro que enseña esto, y sigue libre online. Es de 1981 y no envejeció, porque lo que enseña no es una API: es una manera de pensar. Si algo de este post te da curiosidad, andá directo ahí.

### El lenguaje es el diccionario

Acá está el concepto que quiero que te lleves, y es uno solo.

En casi todos los lenguajes que usás, hay una frontera. De un lado está el lenguaje —lo que definieron los diseñadores, lo que implementa el compilador, lo que no podés tocar—. Del otro lado está tu código. Podés escribir todas las funciones que quieras, pero no podés escribir un `if`. El `if` es de ellos.

En Forth esa frontera no existe. Todo el lenguaje es un diccionario de palabras, y tus palabras entran al mismo diccionario que las que vinieron de fábrica. Las estructuras de control son palabras. Podés definir las tuyas. Podés redefinir las que hay.

Eso tiene una consecuencia que suena a exageración y no lo es: en Forth, escribir un programa y extender el lenguaje son la misma actividad. No escribís una aplicación *en* Forth. Hacés crecer un Forth que, cuando terminaste, resulta que hace lo que necesitabas. El programa y el lenguaje convergen.

Por eso el núcleo es tan chico. Un Forth completo entra en una cantidad de memoria que hoy nos parece un chiste, porque casi nada tiene que estar en el núcleo: lo que se puede definir en Forth, se define en Forth.

Los números lo confirman: en su propio relato, Moore describe un Forth completo de entre 3 y 8 KB de código, compilado a partir de 10 a 20 páginas de fuente, e implementable sin problemas por un solo programador en una computadora chica.[^moore] La Jupiter Ace —que aparece más abajo— metió su Forth entero, diccionario y sistema operativo incluidos, en una ROM de apenas 8 KB.[^ace]

Y por eso Forth es un lenguaje para una persona. Si vos definís las palabras, vos sabés qué significan. Un Forth de un año de uso es un dialecto privado: legible para su autor como la letra de uno mismo, opaco para cualquier otro. Es una potencia enorme y es un problema de equipo enorme, y son la misma característica mirada desde dos lados.

*Thinking FORTH*[^thinking] —el segundo libro de Brodie, también libre— es justamente el intento de convertir eso en disciplina: no cómo escribir Forth, sino cómo pensar en Forth sin que el dialecto privado se te vuelva ilegible a vos mismo en seis meses.

> 🕳️ **HUECO — necesita a César:** ¿escribiste Forth alguna vez, aunque sea un rato jugando? ¿En qué máquina y con qué implementación? Si la respuesta es «nunca», decilo así de simple — el post funciona igual y queda más honesto.

> 🕳️ **HUECO — necesita a César:** ¿leíste *Starting FORTH* o *Thinking FORTH*? Si leíste el segundo, ¿te quedó alguna idea aplicable a lenguajes que sí usás?

### Mil líneas

Hay un precepto que se le atribuye a Moore[^masterminds] y que es la parte más incómoda de todo esto: que si tu problema te está pidiendo más de mil líneas, el problema no es el tamaño del problema — sos vos, que lo estás planteando mal.

Conviene ser preciso con la fuente, porque acá el folklore mezcla cosas. La formulación no aparece en *Masterminds of Programming* ni en *The Early Years*: viene de las propias charlas de Moore, y el número que repite es de **mil instrucciones** —no «mil líneas»— como el tamaño natural de casi cualquier programa que valga la pena escribir.[^moore4th] Por eso lo dejo como paráfrasis de su actitud y no entre comillas: la cita textual habla de instrucciones, y el espíritu es el mismo que el párrafo de arriba enuncia con líneas.

La reacción normal ante esa idea es que es soberbia. Y puede que lo sea. Pero probá invertirla un segundo. La pregunta que hace Moore no es «¿cómo escribo bien estas cincuenta mil líneas?». Es «¿por qué son cincuenta mil?». Y la respuesta honesta, en muchos de los sistemas que uno se cruza, no es «porque el dominio es intrínsecamente así de complejo». Es: capas de abstracción que nadie pidió, generalidad especulativa para requerimientos que nunca llegaron, frameworks que resuelven problemas que no teníamos, y configuración para hacer configurable algo que jamás se reconfiguró.

Moore, en esa lectura, no es un fanático. Es un tipo que se niega a pagar impuestos que los demás pagamos sin discutir.

> 🕳️ **HUECO — necesita a César:** ¿te acordás de algún sistema concreto —de tu carrera, sin nombrar a nadie si no querés— donde hayas mirado el tamaño del código y hayas pensado «esto no debería pesar esto»? Con una frase de la sensación alcanza; no hace falta el detalle institucional. Sin esto, el párrafo de arriba es opinión genérica de internet en vez de tu experiencia.

### Dónde sigue vivo

Forth no está en un museo. Está abajo tuyo.

Open Firmware —el estándar IEEE 1275— es firmware de arranque escrito en Forth, con un intérprete Forth interactivo disponible antes de que exista un sistema operativo.[^openfirmware] Pensalo un segundo: en la máquina que todavía no bootea, hay un lenguaje completo, interactivo, esperándote con un prompt. Esa es exactamente la clase de cosa para la que Forth fue hecho — una persona, una máquina que no anda, y la necesidad de hablarle directo.

Ese estándar, IEEE 1275-1994, nació en Sun Microsystems, donde su implementación se llamó **OpenBoot** —así que «OpenBoot» es el Open Firmware de Sun, no un sinónimo genérico del estándar—. Después lo adoptaron Apple en las Power Macintosh basadas en PowerPC, e IBM en parte de sus equipos. La norma dejó de reafirmarse en 1998 y la IEEE la retiró formalmente en 2005, pero las máquinas que la llevaban siguen existiendo.[^openfirmware]

[VERIFICAR: la afirmación del outline de que «PostScript es básicamente Forth con dibujos». Es una analogía que se repite mucho y que **ninguna fuente de la bibliografía de este draft respalda**. Antes de publicar: o se consigue una fuente sobre el diseño de PostScript y se la suma al plan, o el párrafo se escribe explícitamente como analogía propia —«se le parece en esto y en esto»— sin afirmar linaje ni influencia.]

[VERIFICAR: el uso de Forth en sistemas embebidos críticos y en misiones espaciales. Es un dato que circula mucho y las fuentes listadas acá no lo cubren. Conseguir una fuente concreta o directamente sacar la mención del post.]

El otro lugar donde Forth dejó huella es más romántico y más chico: la Jupiter Ace,[^ace] una microcomputadora que en plena era del BASIC en ROM decidió traer Forth en ROM. Comercialmente fue lo que te imaginás. Pero es el fósil perfecto de un camino que no se tomó: un mundo donde la primera experiencia de programación de una generación entera hubiera sido un stack y un diccionario en vez de `10 PRINT`.

La ficha, confirmada: la Jupiter Ace salió el 22 de septiembre de 1982, la fabricó Jupiter Cantab y la diseñaron Richard Altwasser y Steven Vickers, dos que venían del equipo de la ZX Spectrum. Traía su Forth en una ROM de 8 KB como lenguaje primario, en lugar del BASIC en ROM que traían casi todas sus contemporáneas.[^ace]

> 🕳️ **HUECO — necesita a César:** ¿te tocó alguna vez caer en el prompt `ok` de una máquina Sun sin sistema operativo? Si sí, ¿sabías en ese momento que estabas parado adentro de un Forth?

> 🕳️ **HUECO — necesita a César:** ¿conociste la Jupiter Ace en su momento —revistas, publicidades, alguien que tuviera una— o es una máquina que descubriste mucho después, leyendo?

### Simple no es lo mismo que fácil

Y acá cierro, porque este es el punto por el que el post existe.

Forth no es fácil. La notación postfija te pelea, el stack te obliga a llevar la cuenta en la cabeza, no hay red de contención, y cuando te equivocás el sistema no te dice nada útil. Un principiante sufre.

Pero Forth es simple. No hay nada oculto. El modelo de ejecución entra en un párrafo. El diccionario está ahí, abierto. No hay una capa que no puedas mirar, no hay una parte del lenguaje que sea de otro. Todo lo que hay, lo podés ver.

Esa distinción —simple contra fácil— es la que trabaja Rich Hickey en *Simple Made Easy* [[tr-07]], y Forth es el caso extremo que la vuelve visible: un lenguaje que se corrió tan lejos hacia lo simple que resignó por completo lo fácil. Lo que usamos todos los días suele estar en el otro extremo: fácil de empezar, imposible de tener entero en la cabeza. Y confundimos una cosa con la otra todo el tiempo, porque las dos se sienten bien el primer día.

Probablemente nunca escribas Forth en producción. Pero conocerlo te deja una vara: cuando alguien te diga que la complejidad de un sistema es inevitable, vas a poder pensar en un tipo que decidió que no lo era, y que se pasó la vida demostrándolo con un lenguaje que cabe en tu cabeza.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu opinión, no la mía. ¿Forth te resulta admirable, insensato, o las dos cosas? ¿Y hay algo de la actitud de Moore que hayas aplicado de verdad en tu trabajo, o te parece un ideal lindo que en el mundo real no sobrevive?

---

[^starting]: Leo Brodie, [*Starting Forth*](https://www.forth.com/starting-forth/), FORTH, Inc. / Prentice-Hall, 1981 — el libro de iniciación canónico, edición oficial libre online.
[^thinking]: Leo Brodie, [*Thinking Forth*](http://thinking-forth.sourceforge.net/), 1984 (reimpresión CC BY-NC-SA, ISBN 0-9764587-0-5) — no cómo escribir Forth, sino cómo pensar en Forth.
[^moore]: Charles H. Moore, [*Forth — The Early Years*](https://colorforth.github.io/HOPL.html), 1991 — el relato del propio Moore sobre el origen del lenguaje, en su sitio colorForth (fuente primaria del autor).
[^forthhistory]: FORTH, Inc., [«Forth programming language, history and evolution»](https://www.forth.com/resources/forth-programming-language/) — origen en el NRAO/Kitt Peak (1971), la etimología «fourth → FORTH» y los estándares Forth-79 / Forth-83 / ANS Forth (1994).
[^masterminds]: Entrevista a Charles Moore, capítulo «FORTH», en [*Masterminds of Programming*](https://archive.org/details/MastermindsOfProgramming) — ver [[tr-23]] en el plan editorial.
[^moore4th]: Charles H. Moore, [comentarios y *Fireside Chat* transcritos en UltraTechnology](https://www.ultratechnology.com/moore4th.htm) — fuente del precepto de las «mil instrucciones» («it only needs 1000 instructions to do that», entrevista de 1993). **URL frágil**: agregar backup de Wayback Machine antes de publicar.
[^openfirmware]: [Open Firmware / IEEE 1275-1994](https://www.openfirmware.info/) — documentación del estándar e implementaciones libres (proyecto OpenBIOS), usado como cita primaria; Forth como firmware de arranque interactivo. [Wikipedia](https://en.wikipedia.org/wiki/Open_Firmware) como lectura de contexto.
[^ace]: [Jupiter Ace](https://en.wikipedia.org/wiki/Jupiter_Ace) — la microcomputadora que trajo Forth en ROM en vez de BASIC (1982, Jupiter Cantab).
