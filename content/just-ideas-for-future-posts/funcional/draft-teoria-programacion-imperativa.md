### B-06 — Teoría de la programación imperativa

- **Archivo seed:** `dev/draft-teoria-de-programacion-imperativa.md`
- **Slug propuesto:** `teoria-programacion-imperativa`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-teoria-programacion-imperativa/index.md`
- **Serie:** B (deep dive — pero el ángulo es "la teoría detrás del paradigma que nos parece el más obvio")
- **Cross-links:** depende de [[tr-19]] (Dijkstra), [[tr-18]] (Hoare); lleva a [[B-04]] (recursión vs iteración), [[C-05]] (revolución del cómputo)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** long (2500-3500 palabras)

**Concepto:** la programación imperativa parece "obvia" (asignás, secuencía, decidís, repetís) y sin embargo tiene una base teórica seria: Hoare logic, weakest preconditions de Dijkstra, separation logic. El post es una introducción honesta para alguien que escribió código imperativo toda la vida sin saber que había una teoría detrás.

**Hook:** "vos escribiste `x = x + 1` mil veces sin pensarlo. Ahora vamos a probar formalmente que ese `x = x + 1` es correcto. Y resulta que la matemática para hacerlo es más interesante que la matemática para los lenguajes funcionales."

**Outline:**
1. La pregunta tonta: ¿qué *significa* `x := x + 1`? Si pensás en términos de cuánto tiempo lleva responderla, el ejercicio recién empieza.
2. Hoare triples: `{P} S {Q}`. Pre, post, programa.
3. Las reglas de inferencia: assignment axiom, sequence rule, while rule, etc.
4. Weakest precondition de Dijkstra: la transformación inversa.
5. Loop invariants: la herramienta más infravalorada de la programación.
6. Más allá: separation logic (Reynolds, O'Hearn) — para cuando hay punteros y mutación compartida.
7. Cierre: por qué en 2026 las herramientas de verificación basadas en estas ideas (Dafny, Frama-C, Verified Software Toolchain) están más vivas que nunca.

**Bibliografía:** (reforzada y verificada por fetch el 2026-07-16)

_Fundacionales — lógica de programas_
- [C.A.R. Hoare, *An Axiomatic Basis for Computer Programming*, CACM 12(10):576-580, 1969](https://doi.org/10.1145/363235.363259) — el paper fundacional. DOI canónico verificado en Crossref (`10.1145/363235.363259`). Mirror libre en PDF escaneado: [CMU 15-819](https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf) y [Cornell CS7194](https://www.cs.cornell.edu/courses/cs7194/2019sp/slides/hoare.pdf). — **estable** (DOI); mirrors de curso **frágiles**.
- Robert W. Floyd, *Assigning Meanings to Programs*, en *Proceedings of Symposia in Applied Mathematics*, vol. 19 (Mathematical Aspects of Computer Science), American Mathematical Society, 1967. — el trabajo previo sobre flowcharts que Hoare reconoce como semilla de su sistema. (Sin URL libre verificada por fetch; buscar un mirror estable antes de publicar.) — **frágil / pendiente de link.**
- [Edsger W. Dijkstra, *A Discipline of Programming*, Prentice-Hall, 1976](https://archive.org/details/disciplineofprog0000dijk) — el libro de las precondiciones más débiles (`wp`). — **estable** (Internet Archive, préstamo).
- [Edsger W. Dijkstra, *Guarded commands, non-determinacy and formal derivation of programs*, EWD472](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html) — introduce los comandos guardados y define `wp(S, R)`; versión corta y citable frente al libro entero (título verificado por fetch en el archivo EWD). También apareció en CACM 18(8), 1975. — **estable** (archivo EWD, [[tr-19]]).
- [[tr-19]] — EWD archive (`https://www.cs.utexas.edu/~EWD/`).

_Separation logic_
- [John C. Reynolds, *Separation Logic: A Logic for Shared Mutable Data Structures*, LICS 2002, pp. 55-74](https://doi.org/10.1109/LICS.2002.1029817) — DOI canónico verificado en Crossref (`10.1109/LICS.2002.1029817`). Mirror libre: [PDF de Reynolds en CMU](https://www.cs.cmu.edu/~jcr/seplogic.pdf). — **estable** (DOI); mirror **frágil**.
- [Peter O'Hearn, *Separation Logic*, CACM 62(2):86-95, 2019](https://doi.org/10.1145/3211968) — overview moderno; cuenta el paso de la teoría a analizadores industriales (Infer/Facebook). DOI verificado en Crossref (`10.1145/3211968`). Mirror libre (author accepted manuscript): [UCL Discovery](https://discovery.ucl.ac.uk/10075346/1/O%27Hearn_AAM_sl-cacm-cameraready.pdf). — **estable**.
- P. O'Hearn, J. C. Reynolds y H. Yang, *Local Reasoning about Programs that Alter Data Structures*, CSL 2001 (Springer LNCS 2142). — origen de la **frame rule** y del razonamiento local (atribución confirmada por fetch en Wikipedia/O'Hearn 2019). (DOI y URL sin verificar por fetch; confirmar antes de publicar.) — **pendiente de link.**

_Verificación mecánica y herramientas_
- [Mike Gordon, *Mechanizing Programming Logics in Higher Order Logic*, 1989](https://www.cl.cam.ac.uk/archive/mjcg/papers/MechanizingProgrammingLogics.pdf) — puente a la verificación mecánica. (URL de Cambridge no verificada por fetch — es un PDF; confirmar que responde y guardar respaldo en Wayback.) — **frágil.**
- [Dafny — verification-aware programming language](https://dafny.org/) — `requires`/`ensures`/`invariant` como sintaxis (descripción verificada por fetch en el sitio oficial). Creado por Rustan Leino (Microsoft Research); el desarrollo pasó al Automated Reasoning Group de Amazon/AWS (~2022-2023, Dafny 4 en 2023). — **estable / activo**.
- [Frama-C](https://frama-c.com/) — plataforma de análisis de código C con especificaciones ACSL. Activo en 2026: release 32.0 (Germanium) del 2025-12-03, 33.0~beta (Arsenic) del 2026-06 (verificado por fetch). — **estable / activo**.
- [Verified Software Toolchain (VST) — Princeton](https://vst.cs.princeton.edu/) — separation logic con pruebas mecánicas sobre C, *sound* respecto de la semántica operacional de CompCert (el compilador C verificado). Descripción y relación con CompCert verificadas por fetch. Nota: el sitio dice "last overhaul April 2013" y lista publicaciones hasta 2019; **su mantenimiento activo en 2026 no pudo confirmarse desde el sitio** — verificar antes de afirmar que sigue vivo. — **estado incierto.**

**Imágenes:**
- _Crear_: diagrama SVG de un Hoare triple aplicado a un swap simple (~30 min).
- _Crear_: comparison side-by-side de un loop con/sin invariante anotado (~30 min).
- _Crear_: opcional, tabla resumen de Hoare logic, wp, separation logic (~45 min).

**Tags propuestos:** `['Hoare logic', 'Dijkstra', 'separation logic', 'verificacion', 'imperativo']`

**Estado actual:** prosa completa de ~2.900 palabras siguiendo el outline de 7 puntos, escrita el 2026-07-15. Todo el desarrollo técnico (triples de Hoare, axioma de asignación, reglas de secuencia y `while`, `wp`, invariantes, separation logic, herramientas) está escrito y se apoya sólo en la bibliografía ya listada.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch: DOIs de Hoare 1969, Reynolds 2002 y O'Hearn 2019 cotejados en Crossref; EWD472, Dafny, Frama-C y VST verificados en sus sitios/archivos; se agregaron Floyd 1967, EWD472 y O'Hearn-Reynolds-Yang 2001) y se resolvieron 6 de 8 marcadores [VERIFICAR:]. Quedan 2 sin resolver: el estado de mantenimiento de VST en 2026 (parcial — descripción confirmada, actividad 2026 no) y la genealogía Gordon → HOL → herramientas modernas (no verificable por fetch; el paper de Gordon es un PDF escaneado y la «descendencia directa» a Dafny/Frama-C/VST es dudosa: Dafny usa Boogie/Z3, Frama-C usa Why3, VST usa Coq — conviene reescribirla como «continuidad de ideas»). Además no se pudo OCR-ear el PDF escaneado de Hoare 1969, así que las reglas se confirmaron por fuentes secundarias fetch (Wikipedia «Hoare logic») y falta cotejar la notación literal del paper.

Quedan pendientes:

- **8 huecos 🕳️** que necesitan a César: su primer contacto con Dijkstra y con Hoare, si dio o cursó la materia donde esto se enseña, el bug real de invariante que sirva de ejemplo de apertura, si alguna vez usó Dafny/Frama-C/ACSL, la anécdota de código del sector público (STG / Min. Cultura Santa Fe) donde un invariante hubiera ayudado, y su opinión sobre la afirmación fuerte del Hook.
- **8 marcadores [VERIFICAR:]** — casi todos son atribuciones o datos que la bibliografía actual no cubre: el crédito a Floyd que Hoare reconoce en el paper del 69, la relación entre `wp` y el lenguaje de comandos guardados, la regla exacta de `while` tal como aparece en CACM 1969, el estado de la regla de consecuencia, el frame rule y su enunciado en Reynolds 2002 vs O'Hearn 2019, la genealogía Gordon → HOL → herramientas actuales, y el estado de Dafny/Frama-C/VST en 2026.
- **Nota de fricción con el Hook:** el Hook afirma que la matemática de la verificación imperativa es «más interesante» que la de los lenguajes funcionales. La prosa lo mantiene, pero lo trata explícitamente como opinión del autor y no como hecho; el cierre lo reencuadra en vez de defenderlo. Si a César no le cierra ese encuadre, hay que reescribir el Hook (que el spec pide no tocar) antes de publicar.
- Faltan las tres imágenes listadas en **Imágenes**; la prosa tiene marcadas las posiciones donde entran.
- Los cross-links `[[tr-18]]`, `[[tr-19]]`, `[[B-04]]` y `[[C-05]]` quedan sin resolver hasta publicación.

---

## Borrador de prosa

Escribiste `x = x + 1` mil veces. Diez mil. Nunca te detuviste a pensarlo, porque no hay nada que pensar: la variable valía algo, ahora vale uno más. Es la operación más aburrida de la programación, tan aburrida que la mayoría de los lenguajes te dejan escribirla más corto todavía, `x++`, para que no gastes ni las teclas.

Ahora te propongo algo incómodo: probá que está bien. No que anda, que anda ya lo sabés. Probá, en el sentido en que se prueba un teorema, que ese `x = x + 1` hace lo que creés que hace. Vas a descubrir dos cosas. La primera es que no es tan fácil como parece. La segunda es que la matemática que hace falta para conseguirlo es rarísima y hermosa, y que en 2026 sigue viva y corriendo dentro de herramientas que quizás uses sin saberlo.

### 1. La pregunta tonta

¿Qué *significa* `x := x + 1`?

La respuesta de programador es «suma uno a x». Pero eso no es un significado, es una paráfrasis: reemplacé un símbolo por unas palabras y quedamos igual. La respuesta de máquina es «carga el contenido de la dirección de x en un registro, incrementa el registro, escribe el registro de vuelta en la dirección de x». Eso ya es mejor, pero ahora el significado de mi programa depende de qué máquina lo corre, que es exactamente lo que no quiero: si el sentido de mi código vive en el silicio, no puedo razonar sobre el código, sólo puedo ejecutarlo y mirar.

La tercera respuesta es la interesante, y es la que abre todo el resto del post. El significado de `x := x + 1` es una *relación entre lo que era cierto antes y lo que es cierto después*. Si antes de ejecutarlo era cierto que `x = 5`, después es cierto que `x = 6`. Si antes era cierto que `x < 10`, después es cierto que `x <= 10`. Si antes era cierto que `x` es par, después es cierto que `x` es impar. La instrucción no *es* nada por sí sola: es una función que transforma afirmaciones sobre el estado en otras afirmaciones sobre el estado.

Esa idea —programa como transformador de afirmaciones, no como secuencia de eventos— es el corazón de todo lo que viene. Y viene de un paper de 1969.

> 🕳️ **HUECO — necesita a César:** ¿cuándo y cómo te cruzaste por primera vez con la idea de que un programa se puede *probar* correcto? ¿Fue en la facultad, en un libro, en un trabajo? Una o dos frases alcanzan para abrir el post con algo tuyo.

### 2. Los triples de Hoare

En 1969 Tony Hoare publicó en *Communications of the ACM* un paper con el título más seco posible: *An Axiomatic Basis for Computer Programming*.[^hoare69] Es corto. Y propone una notación que, una vez que la ves, ya no podés dejar de verla en todos lados:

```
{P} S {Q}
```

Se lee: si la afirmación `P` es verdadera antes de ejecutar el programa `S`, y `S` termina, entonces la afirmación `Q` es verdadera después. `P` es la **precondición**, `Q` es la **postcondición**, `S` es el programa. Eso es todo. Ese objeto de tres partes se llama, con justicia, *triple de Hoare*.

Fijate en la cláusula que metí al pasar: «y `S` termina». La formulación clásica del triple no promete que el programa termine. Promete que *si* termina, la postcondición se cumple. A eso se lo llama corrección parcial, y a la versión que además exige terminación se la llama corrección total. Es una distinción que parece burocrática y no lo es: separar «hace lo correcto» de «hace algo» permite atacar los dos problemas con herramientas distintas, porque probar terminación es un problema de naturaleza diferente a probar corrección.

Volvamos a nuestro `x := x + 1`. Un triple verdadero sería:

```
{x = 5} x := x + 1 {x = 6}
```

Y otro:

```
{x = n} x := x + 1 {x = n + 1}
```

Y otro más, que parece trampa pero no lo es:

```
{true} x := x + 1 {true}
```

Ese último es verdadero y completamente inútil: no promete nada, así que se cumple siempre. Los triples inútiles importan, porque te enseñan que el arte no está en escribir un triple verdadero sino en escribir el triple verdadero *más fuerte* que puedas.

[IMAGEN: diagrama SVG de un triple de Hoare aplicado a un swap simple — ver sección **Imágenes**]

### 3. Las reglas de inferencia

Un triple suelto no sirve de mucho. Lo que hace que esto sea una *lógica* y no una notación es que Hoare dio reglas para derivar triples nuevos a partir de triples viejos.[^hoare69] Y acá viene la parte que a mí me sigue pareciendo un truco de magia después de años.

**El axioma de asignación.** ¿Cómo probás algo sobre `x := e`? Uno esperaría una regla que diga «tomá lo que sabías de `x`, aplicale `e`, y eso sabés después». Hoare hace exactamente lo contrario. La regla es:

```
{Q[x := e]} x := e {Q}
```

Es decir: si querés que después de la asignación valga `Q`, lo que tenía que valer antes es `Q` con todas las apariciones de `x` reemplazadas por `e`. La regla camina para atrás. Empieza en el final y deduce el principio.

Probémoslo con nuestro caso. Quiero que después valga `Q ≡ x = 6`. Sustituyo `x` por `x + 1` en `Q` y obtengo `x + 1 = 6`, o sea `x = 5`. La regla me *dedujo* la precondición. No la adiviné: salió de una sustitución mecánica de símbolos.

La primera vez que uno ve esto siente que está al revés. Es que está al revés, y ese es el punto: es la primera pista de que el razonamiento sobre programas imperativos fluye naturalmente hacia atrás, del efecto a la causa, y no hacia adelante como los ejecutamos. Guardá esa idea porque en la sección 4 se convierte en el protagonista.

**La regla de secuencia.** Si `{P} S1 {R}` y `{R} S2 {Q}`, entonces `{P} S1; S2 {Q}`. La postcondición de uno es la precondición del siguiente, y el `R` del medio hace de bisagra. Esto es exactamente lo que hacés mentalmente cuando leés código ajeno línea por línea, salvo que ahora es un teorema.

**La regla de consecuencia.** Podés siempre fortalecer la precondición y debilitar la postcondición: si `{P} S {Q}` vale, y `P'` implica `P`, y `Q` implica `Q'`, entonces `{P'} S {Q'}` también vale. Prometer menos, exigiendo más, siempre es seguro. Esta es la regla que conecta la lógica de programas con la lógica común: es el único lugar donde entran a jugar implicaciones matemáticas que no tienen nada que ver con el código. [CONFIRMADO 2026-07-16: sí es la «rule of consequence» (Hoare 1969); su forma estándar es la de dos mitades — `P₁ → P₂, {P₂} S {Q₂}, Q₂ → Q₁ ⊢ {P₁} S {Q₁}`: se puede fortalecer la precondición y/o debilitar la postcondición. Fuente fetch: Wikipedia «Hoare logic», que la atribuye a Hoare 1969. Falta cotejar la notación literal del paper escaneado (no OCR-eable por fetch).]

**La regla del condicional.** Para `if B then S1 else S2`, probás `{P ∧ B} S1 {Q}` y `{P ∧ ¬B} S2 {Q}`, y concluís `{P} if B then S1 else S2 {Q}`. Cada rama se prueba sabiendo en qué rama está. Nada sorprendente, pero notá lo que formaliza: la intuición de que dentro del `then` sabés más que afuera.

Y falta la regla que importa. Esa se merece su propia sección, y la vemos en la 5.

> 🕳️ **HUECO — necesita a César:** ¿enseñaste alguna vez esto, o lo cursaste? Si diste una materia donde aparecían los triples de Hoare, ¿cómo reaccionaban los alumnos al axioma de asignación que va para atrás? Es el mejor lugar del post para una anécdota de aula.

[CONFIRMADO 2026-07-16: Hoare reconoce como semilla el trabajo previo de Robert W. Floyd, *Assigning Meanings to Programs* (1967), «a similar system for flowcharts». Fuentes fetch: Wikipedia «Hoare logic» y overviews que citan Hoare 1969. Falta la cita textual del párrafo exacto del paper escaneado (no OCR-eable por fetch); ver Floyd 1967 en la bibliografía.]

### 4. La precondición más débil de Dijkstra

Dijkstra agarró la idea de que el razonamiento camina para atrás y la llevó hasta el final. En *A Discipline of Programming*, de 1976, la propuesta ya no es «acá tenés reglas para verificar programas que ya escribiste».[^edp] La propuesta es: el programa y su prueba se derivan juntos, y la prueba viene primero.

La herramienta se llama **precondición más débil**. Se escribe `wp(S, Q)` y significa: el conjunto de todos los estados desde los cuales ejecutar `S` termina y deja valiendo `Q`. Todos. El más débil, o sea el más permisivo, o sea el que no exige un gramo más de lo estrictamente necesario.

La diferencia con Hoare es sutil y decisiva. `{P} S {Q}` es una afirmación que verificás: te dan `P`, `S` y `Q`, y decís sí o no. `wp(S, Q)` es una *función*: le das el programa y lo que querés lograr, y te devuelve lo que hace falta. Un triple se chequea; una `wp` se calcula. Es la diferencia entre corregir un examen y resolverlo.

Y `{P} S {Q}` vale, en corrección total, exactamente cuando `P` implica `wp(S, Q)`. La lógica de Hoare queda subsumida: los triples pasan a ser consecuencias de un cálculo, y no un sistema aparte.

Para la asignación, `wp(x := e, Q) = Q[x := e]`, que es el axioma de Hoare de nuevo, ahora como definición de una función y no como regla. Para la secuencia, `wp(S1; S2, Q) = wp(S1, wp(S2, Q))`: componés hacia atrás, del final al principio, como una composición de funciones. Esa ecuación es de una elegancia que me sigue impresionando. Toda tu función de 40 líneas es una composición de 40 transformadores de predicados, y su especificación sale de aplicarlos en orden inverso.

Lo que Dijkstra construye sobre esto es un método de programación, no de verificación. La idea es que si sabés qué querés que valga al final, la estructura del programa que lo consigue está casi forzada: la `wp` te dice qué te falta, y lo que te falta te sugiere la instrucción siguiente. Se programa desde la postcondición hacia atrás. Los programas que salen así, decía él, son cortos y tienen su prueba adentro.

[CONFIRMADO 2026-07-16: sí, el aparato de `wp` de Dijkstra va montado sobre los comandos guardados. El EWD citable más breve que el libro entero es **EWD472**, *Guarded commands, non-determinacy and formal derivation of programs* (título verificado por fetch en el archivo EWD, [[tr-19]]): introduce los comandos guardados y define `wp(S, R)` como «weakest pre-condition for the initial state»; también salió en CACM 1975. Ya está en la bibliografía. — Queda como decisión editorial de César (no es dato a verificar) si explicar los comandos guardados en el post o presentar `wp` sobre pseudocódigo convencional.]

> 🕳️ **HUECO — necesita a César:** ¿tenés *A Discipline of Programming*? ¿Lo leíste entero, lo abandonaste, lo consultás? Cualquiera de las tres respuestas sirve, y la segunda es la más honesta y la más divertida de contar.

### 5. Invariantes: la herramienta más infravalorada

Ahora sí, el `while`.

Todo lo anterior funcionaba porque los programas tenían un tamaño fijo: tantas instrucciones, tantas reglas, listo. Un loop rompe eso. Un loop es un programa de longitud desconocida: puede correr cero veces, tres, un millón. No podés probar cada caso. Necesitás algo que valga para *todas* las vueltas a la vez.

Eso es el **invariante**: una afirmación `I` que es verdadera antes de entrar al loop, y que sigue siendo verdadera después de cada iteración. Si `I` sobrevive una vuelta, sobrevive todas, por inducción. La regla, en esencia, dice que si `{I ∧ B} S {I}` —o sea, el cuerpo preserva el invariante cuando la guarda es verdadera—, entonces `{I} while B do S {I ∧ ¬B}`: al salir sabés que el invariante sigue valiendo *y* que la guarda se rompió.[^hoare69] [CONFIRMADO 2026-07-16: la forma estándar atribuida a Hoare 1969 es `{P ∧ B} S {P} ⊢ {P} while B do S {¬B ∧ P}` — `P` es el invariante; al salir vale el invariante y la negación de la guarda. Coincide con la formulación de la prosa. Fuente fetch: Wikipedia «Hoare logic». Falta cotejar la notación literal del paper escaneado (no OCR-eable por fetch).]

Esa conjunción final, `I ∧ ¬B`, es todo el truco. El invariante solo es demasiado débil para probar nada interesante; la negación de la guarda sola no te dice nada del cómputo. Juntas te dan el resultado. Buscar un invariante es, en la práctica, buscar la afirmación que combinada con «el loop terminó» te entrega justo lo que querías.

Y acá está el punto que le da título a esta sección: **vos ya usás invariantes, sólo que no los escribís**.

Cuando programás un loop que suma los elementos de un arreglo, en algún lugar de tu cabeza está la frase «después de `i` vueltas, `suma` tiene la suma de los primeros `i` elementos». Eso *es* el invariante. Está completo, es correcto, y lo tenés claro mientras escribís el loop. Después lo tirás a la basura: no lo anotás en ningún lado, y a los seis meses el que lee el loop —vos— tiene que reconstruirlo leyendo el cuerpo al revés.

Es un desperdicio enorme y perfectamente evitable. Escribir el invariante en un comentario de una línea arriba del `while` cuesta quince segundos y es el comentario más útil que vas a escribir en tu vida, porque no repite el código (pecado capital de los comentarios): dice lo que el código *no puede decir*, que es la razón por la cual funciona.

Fijate qué se compra con eso. Casi todos los bugs de loop que sufriste en tu vida son alguna de estas tres cosas: el invariante no vale al entrar (falta inicializar algo), el cuerpo lo rompe (actualizaste una variable y no la otra), o vale pero es demasiado débil para darte la postcondición al salir (el clásico off-by-one, donde el invariante habla de `i` y la postcondición necesitaba `i + 1`). Tener el invariante escrito convierte un bug difuso de «esto no anda» en una pregunta de tres opciones.

[IMAGEN: comparación side-by-side de un loop con y sin invariante anotado — ver sección **Imágenes**]

> 🕳️ **HUECO — necesita a César:** necesito un bug real de loop tuyo para anclar esta sección — idealmente uno donde el invariante escrito lo hubiera prevenido, o donde lo encontraste justamente reconstruyendo el invariante a mano. ¿Tenés uno? Con el contexto mínimo (qué hacía el loop, qué salió mal) alcanza.

> 🕳️ **HUECO — necesita a César:** ¿acostumbrás anotar invariantes en tus loops? Quiero saber si esta sección la escribo como consejo que seguís o como consejo que sabés que es bueno y no seguís. Las dos versiones son publicables, pero son posts distintos.

La terminación, que dejamos de lado, va aparte: se prueba con una **variante**, una expresión entera que decrece en cada vuelta y no puede bajar de cero. Si tenés una de esas, el loop termina, porque no existe una sucesión infinita de naturales estrictamente decreciente. Es la misma idea que usa la recursión bien fundada, que es un puente lindo hacia [[B-04]].

### 6. Punteros, o por qué esto no alcanzaba

Todo lo anterior tiene un supuesto escondido, y es grande: que cuando escribo `x`, hablo de una cosa, y cuando escribo `y`, hablo de otra.

Metele punteros y el supuesto se cae. Si `p` y `q` son punteros, `*p := 3` puede cambiar el valor de `*q` —si `p` y `q` apuntan al mismo lado—, y no hay nada en la sintaxis que te avise. De golpe cada afirmación sobre el estado tiene que arrastrar la lista completa de cosas que podrían haber cambiado, y todo lo que no cambió tenés que decirlo explícitamente. Escribir una prueba de un programa con punteros en Hoare logic pura es posible y es un martirio: la mayor parte de la prueba se va en decir todo lo que *no* pasó.

La salida llegó con la **separation logic**, en el trabajo de John Reynolds y Peter O'Hearn.[^reynolds][^ohearn] La idea central es un conector nuevo, la conjunción separante, que se escribe `P * Q` y se lee «`P` y `Q` valen, en porciones *disjuntas* del heap». Ese asterisco no es un «y» común: es un «y» que además promete que las dos mitades no se pisan.

Con eso podés razonar sobre un pedazo de memoria ignorando el resto, y —lo importante— podés hacerlo *válidamente*, con una regla que te autoriza a decir que lo que probaste sobre una porción de memoria sigue valiendo cuando la ponés adentro de un programa más grande que toca otras porciones. El razonamiento se vuelve local. Y el razonamiento local es lo que hace que una prueba escale de un ejemplo de juguete a un sistema real, por la misma razón por la que la modularidad hace que el código escale.

[CONFIRMADO 2026-07-16: la regla es la **frame rule**, y habilita el razonamiento local — «un programa que se ejecuta con seguridad en un estado chico (que satisface `P`) también se ejecuta en cualquier estado más grande (`P ∗ R`) sin afectar la parte adicional». Se atribuye a **O'Hearn, Reynolds y Yang**, *Local Reasoning about Programs that Alter Data Structures* (CSL 2001); O'Hearn 2019 (CACM) la cuenta como la versión citable. Fuentes fetch: Wikipedia «Separation logic» + O'Hearn 2019.]

[CONFIRMADO 2026-07-16: sí. La herramienta central es **Infer** (Facebook/Meta), analizador estático para Java, C y Objective-C basado en separation logic y *bi-abduction*. La escala reportada: una base de código de millones de líneas modificada miles de veces por día en «code diffs»; en vez de análisis global por cada diff, Infer analiza los cambios composicionalmente y reporta regresiones como un bot en la revisión de código. Fuentes fetch: O'Hearn 2019 (CACM) + Wikipedia «Separation logic».]

### 7. Por qué esto está más vivo que nunca

La historia que se cuenta habitualmente es que la verificación formal fue un sueño de los setenta que fracasó: demasiado trabajo, demasiada matemática, programas de juguete. Y durante un buen rato fue verdad. Pero la parte que casi nunca se cuenta es qué pasó después, y lo que pasó después es que la máquina se puso a hacer la parte aburrida.

El puente lo empezó a construir gente como Mike Gordon, cuyo *Mechanizing Programming Logics in Higher Order Logic* de 1989 es exactamente lo que el título dice: agarrar las lógicas de programas de Hoare y Dijkstra y meterlas adentro de un asistente de pruebas para que la máquina las manipule.[^gordon] Ese movimiento —de lógica en papel a lógica mecanizada— es el que cambia la ecuación, porque el cuello de botella de la verificación nunca fue la idea, fue la contabilidad.

Hoy eso decantó en herramientas que un programador puede tocar:

- **Dafny**[^dafny] es un lenguaje donde escribís `requires`, `ensures` e `invariant` como parte del programa, y el verificador te dice si tu código cumple. Los triples de Hoare dejaron de ser notación de pizarrón y son sintaxis.
- **Frama-C**[^framac] hace lo propio sobre C real, el de verdad, con punteros y todo, mediante anotaciones en comentarios.
- **Verified Software Toolchain**[^vst], de Princeton, va al fondo: pruebas mecánicas sobre C, con separation logic adentro, verificadas hasta el compilador.

[PARCIALMENTE CONFIRMADO 2026-07-16 (fetch a los tres sitios oficiales): **Dafny** — sitio vivo; se describe como «verification-aware programming language» con `requires`/`ensures`/`invariant`; desarrollo hoy en el Automated Reasoning Group de Amazon/AWS (Dafny 4 en 2023); activo. **Frama-C** — muy activo: release 32.0 (Germanium) del 2025-12-03 y 33.0~beta del 2026-06; plataforma de análisis de C con ACSL. **VST** — la descripción de arriba es correcta según el sitio (separation logic; *sound* respecto de la semántica operacional de CompCert, el compilador C verificado), PERO ⚠️ el sitio dice «last overhaul April 2013» y sus publicaciones llegan hasta 2019: **no se pudo confirmar mantenimiento activo en 2026**. No afirmar que VST «sigue vivo» sin corroborarlo aparte (repo GitHub / releases recientes de Coq).]

[VERIFICAR: la línea Gordon → HOL → asistentes de pruebas modernos → Dafny/Frama-C/VST está contada de memoria como genealogía. Verificar que sea defendible, o reescribirla como «hay una continuidad de ideas» sin sugerir descendencia directa de herramientas.]

> 🕳️ **HUECO — necesita a César:** ¿usaste alguna vez alguna de estas tres? ¿Aunque sea un rato, aunque sea el tutorial de Dafny? Si la respuesta es no, también sirve y lo digo así: es más honesto que fingir experiencia.

> 🕳️ **HUECO — necesita a César:** el post pide un aterrizaje en tu experiencia del sector público (STG, Ministerio de Cultura de Santa Fe). ¿Hubo algún sistema donde la falta de una especificación escrita —un invariante, una precondición, un contrato— haya costado caro? No hace falta nombrar a nadie ni dar detalles comprometedores; con el tipo de sistema y el tipo de falla alcanza.

### El cierre

Vuelvo al `x = x + 1` del principio.

Lo que quería mostrarte no es que puedas probar formalmente cada línea que escribís. No podés, y probablemente no deberías: el costo de una prueba completa sólo se justifica cuando la falla es cara de verdad, y la mayoría de nuestro código no está ahí. Lo que quería mostrarte es otra cosa: que cuando programás, ya estás razonando con estos objetos. Tenés precondiciones en la cabeza cada vez que escribís un `if` que chequea que algo no sea nulo. Tenés invariantes cada vez que escribís un `while`. Tenés postcondiciones cada vez que ponés un nombre a una función.

La lógica de Hoare, la `wp` de Dijkstra y la separation logic no te enseñan a pensar de una manera nueva. Te enseñan a *escribir* lo que ya pensás. Y lo que se escribe se puede revisar, discutir, versionar y chequear con una máquina; lo que queda en la cabeza se evapora en seis meses.

Ese, para mí, es el motivo real por el cual esto vale la pena aunque nunca corras un verificador en tu vida. El paper de Hoare no te regala una herramienta: te regala un vocabulario para decir por qué tu código anda. Y una vez que tenés el vocabulario, empezás a notar todos los lugares donde no podés explicarlo. Esos lugares son, con una regularidad que da miedo, exactamente donde después aparecen los bugs.

> 🕳️ **HUECO — necesita a César:** el Hook del draft afirma que la matemática de la verificación imperativa es «más interesante» que la de los lenguajes funcionales. Escribí el post manteniendo eso como opinión tuya, pero necesito saber si la sostenés y por qué, para no dejarlo colgado. Si no la sostenés, hay que cambiar el Hook.

[IMAGEN: opcional, tabla resumen Hoare logic / wp / separation logic — ver sección **Imágenes**]

[^hoare69]: C.A.R. Hoare, *An Axiomatic Basis for Computer Programming*, Communications of the ACM 12(10):576-580, 1969. [DOI 10.1145/363235.363259](https://doi.org/10.1145/363235.363259). Mirror libre en PDF escaneado: [CMU 15-819](https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf).
[^edp]: Edsger W. Dijkstra, *A Discipline of Programming*, Prentice-Hall, 1976. [Copia en Internet Archive](https://archive.org/details/disciplineofprog0000dijk).
[^reynolds]: John C. Reynolds, *Separation Logic: A Logic for Shared Mutable Data Structures*, LICS 2002, pp. 55-74. [DOI 10.1109/LICS.2002.1029817](https://doi.org/10.1109/LICS.2002.1029817). Mirror libre: [PDF de Reynolds en CMU](https://www.cs.cmu.edu/~jcr/seplogic.pdf).
[^ohearn]: Peter O'Hearn, *Separation Logic*, Communications of the ACM 62(2):86-95, 2019. [DOI 10.1145/3211968](https://doi.org/10.1145/3211968). Mirror libre (AAM): [UCL Discovery](https://discovery.ucl.ac.uk/10075346/1/O%27Hearn_AAM_sl-cacm-cameraready.pdf).
[^gordon]: Mike Gordon, *Mechanizing Programming Logics in Higher Order Logic*, 1989. [PDF](https://www.cl.cam.ac.uk/archive/mjcg/papers/MechanizingProgrammingLogics.pdf).
[^dafny]: [Dafny](https://dafny.org/) — lenguaje con verificación integrada.
[^framac]: [Frama-C](https://www.frama-c.com/) — plataforma de análisis y verificación para C.
[^vst]: [Verified Software Toolchain](https://vst.cs.princeton.edu/) — Princeton.

