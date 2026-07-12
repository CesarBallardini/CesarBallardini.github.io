---
title: 'El intérprete que ejecuta el paper de Turing tal cual está escrito'
description: 'Construí en Python un intérprete de reescritura perezosa que corre las m-configuraciones y m-funciones de "On Computable Numbers" (1936) literalmente, glifos y todo. Cómo funciona por dentro.'
tags: ['Turing', 'computabilidad', 'interpretes', 'Python', 'programacion funcional', 'term rewriting']
featured_image: 'hero-alan-turing-1951.jpg'
---

Todo el mundo que estudió ciencias de la computación implementó "una máquina de Turing" en algún momento[^img_hero]: una cinta, un cabezal, una tabla de transiciones `(estado, símbolo) → (estado, símbolo, movimiento)`. Es un ejercicio válido, pero no es lo que Turing escribió en 1936. Su notación real —la que usa en _On Computable Numbers, with an Application to the Entscheidungsproblem_[^turing1936]— es bastante más rica que eso, y casi nadie la implementa como está en el paper. Yo quería saber si podía.

El resultado es [`turing-lazy-term-rewriting-interpreter`](https://github.com/CesarBallardini/turing-lazy-term-rewriting-interpreter)[^repo], un intérprete en Python que ejecuta esa notación literalmente: los mismos nombres, las mismas letras góticas, el mismo mecanismo que Turing describe con la frase "la tabla completa se obtiene por sustitución repetida en las tablas esqueleto". Esa frase, tomada en serio, define el diseño entero.

## Lo que Turing escribió, y por qué no es una tabla plana

El objetivo del paper es responder el _Entscheidungsproblem_ de Hilbert: ¿existe un procedimiento mecánico que decida, para cualquier enunciado matemático, si es demostrable? Turing lo contesta que no, pero para hacerlo primero tiene que definir con precisión qué es un "procedimiento mecánico" — y ahí inventa lo que hoy llamamos máquina de Turing.

Hasta acá, la historia que todos conocemos. Lo que se pierde en la versión de manual es que Turing, apenas termina de definir la máquina básica en las primeras secciones, se da cuenta de que escribir tablas de transición completas a mano es insostenible para cualquier máquina interesante. Así que en el §4 introduce una capa de abstracción: las **m-funciones** (_m-functions_), tablas parametrizadas que se combinan entre sí. Su notación usa dos alfabetos separados a propósito:

- **Letras góticas mayúsculas** (ℭ, 𝔅, 𝔄, …) para variables de m-configuración — "andá a esta otra tabla".
- **Letras griegas minúsculas** (α, β, …) para variables de símbolo — "el símbolo que estés leyendo en este momento".

Con eso arma una biblioteca de primitivas reusables: `f(ℭ, 𝔅, α)` encuentra el símbolo `α` más próximo por la izquierda; `e(𝔅, α)` borra todas las ocurrencias de `α`; `c1`, `pe`, `cp` copian y comparan secuencias marcadas. Una máquina real —la que calcula π, o la que enumera números computables— se escribe componiendo estas funciones, no escribiendo cientos de filas de tabla a mano.

La frase clave, la que da origen a todo el diseño del intérprete, está en el §4:

> «The reader should find no difficulty in seeing that this table is really a set of instructions which could be obeyed by a machine. […] The functional relation between a table and the complete table is obtained by repeated substitution.»[^turing1936]

Traducido: las tablas con m-funciones son **abreviaturas**. La tabla completa —la que efectivamente se ejecuta— se obtiene reemplazando cada m-función por su definición, una y otra vez, hasta llegar a instrucciones concretas. Eso no es un detalle de notación. Es, literalmente, la definición de un sistema de reescritura de términos.

## Términos, no estados

Si las tablas de Turing son abreviaturas que se expanden por sustitución, entonces el "estado" de la máquina en cualquier instante no es una etiqueta plana (`q0`, `q1`, …). Es una **expresión** — un término como `f(ℭ, 𝔅, α)` o, ya con todo resuelto, `f(halt, missing, x)`. Así que el primer paso para construir el intérprete fue modelar esa gramática, no una tabla de lookup:

```python
type Term = Sym | SVar | MVar | Atom | MApp

@dataclass(frozen=True, slots=True)
class MApp:
    """Application of an m-function / m-configuration to arguments."""
    name: str
    args: tuple[Term, ...] = ()
```

Un término es un árbol: una hoja (un símbolo literal, una variable de símbolo, una variable de m-configuración) o una aplicación `nombre(arg₁, …, argₙ)` cuyos argumentos son, otra vez, términos. El "estado actual" de la máquina siempre es un `MApp` **ground** — sin variables sueltas.

Hay una ambigüedad genuina acá que Turing no resuelve explícitamente y que el intérprete sí tiene que resolver: una hoja suelta como `x` en minúscula, ¿es el símbolo literal `x` o el nombre de una m-configuración de aridad cero? La respuesta, en el código, es que **no se decide al leer el término** — se decide al consumirlo, según el tipo del parámetro formal que lo recibe:

```python
def bind_params(params: tuple[str, ...], args: tuple[Term, ...]) -> Bindings:
    for param, arg in zip(params, args, strict=True):
        if is_symbol_var(param):     # nombre griego → espera un símbolo
            symbols[param] = _resolve_symbol(arg)
        else:                        # nombre gótico/mayúscula → espera una m-config
            m_configs[param] = _resolve_m_config(arg)
```

Esto evita tener que mantener una tabla separada de "namespace de símbolos" vs. "namespace de configuraciones" — el árbol de sintaxis solo, más la aridad y el tipo del parámetro que consume cada hoja, alcanza. Es la clase de decisión de diseño que uno no anticipa hasta que intenta implementar la ambigüedad tal cual aparece en el texto original.

Con el modelo de términos en su lugar, el programa entero es una tabla de entradas, cada una de dos clases:

| Tipo | Efecto |
|---|---|
| **Alias** | reescribe el término a otro término. Sin acción sobre la cinta. Sustitución pura. |
| **Table** | tiene filas que concuerdan con el símbolo escaneado; la fila que concuerda ejecuta operaciones (imprimir / borrar / mover) y *después* reescribe el estado al término de su `goto`. |

Los alias son las m-funciones "definicionales" del paper — puro azúcar sintáctico. Las tablas son las que de verdad tocan la cinta.

## Perezoso, no ansioso

Acá está la decisión de diseño que le da nombre al proyecto. Si "la tabla completa se obtiene por sustitución repetida", hay dos formas de leer eso:

**Expansión ansiosa (eager):** antes de correr nada, expandir *todas* las m-funciones hasta obtener la tabla plana y finita, y después correr un intérprete trivial sobre esa tabla. Es exactamente lo que Turing describe para producir "la tabla completa", y es lo que necesitás si querés calcular la Descripción Estándar de la máquina (§5, más abajo). El problema —que el propio Turing señala de pasada— es que la sustitución puede generar **infinitos** términos-estado distintos. Si `p` se define en términos de sí misma, expandir ansiosamente puede producir `p`, `p(p(…))`, `p(p(p(…)))`, sin parar nunca. Para una máquina arbitraria, la expansión ansiosa puede no terminar.

**Reescritura perezosa (lazy):** no expandir nada por adelantado. Mantener el estado como término y reescribirlo únicamente cuando hace falta dar el próximo paso. Solo se materializan los términos que la computación realmente visita. Una máquina que corre para siempre —el caso normal para una que calcula una secuencia infinita, como π dígito por dígito— simplemente reescribe para siempre, un paso a la vez, en memoria acotada. Nunca intenta enumerar el espacio de estados completo (que puede ni siquiera ser finito).

El intérprete es perezoso. No es una elección estética: es la que hace que "sustitución repetida" funcione como motor principal sin toparse con el problema de expansión infinita. Y es, casi al pie de la letra, el mismo argumento que separa la evaluación _call-by-need_ de la evaluación _eager_ en cálculo lambda y en lenguajes funcionales — la razón por la que Haskell puede tener listas infinitas sin explotar.[^lazy]

## Un paso, en detalle

El loop principal vive en `machine.py`, y cada paso que toca la cinta hace esto:

```
1. scanned ← cinta.leer()

2. RESOLVER ALIASES:
     mientras la cabeza del término nombre un Alias:
         env ← ligar los parámetros del alias con los argumentos del estado
         estado ← sustituir(cuerpo_del_alias, env)   # reescritura pura, sin cinta
     # ahora la cabeza del término nombra una Table

3. env ← ligar los parámetros de la Table con los argumentos del estado

4. ELEGIR FILA: la primera fila cuyo `Matcher` concuerda con el símbolo escaneado

5. ACTUAR: ejecutar las operaciones de esa fila (imprimir / borrar / mover)

6. REESCRIBIR: estado ← sustituir(goto_de_la_fila, env)
```

Los pasos 2 y 6 son la reescritura de términos propiamente dicha. Los pasos 4 y 5 son donde la reescritura toca físicamente la cinta. Todo el paso 2+4 vive en una única función pura, `resolve_and_select`, que no toca la cinta para nada — y por eso el expansor estático (`expand.py`, el que sí hace la expansión ansiosa para calcular la Descripción Estándar) puede reusarla sin duplicar lógica.

Para que esto se sienta menos abstracto, tomemos `e(𝔅, α)` — "borrar cada ocurrencia de α" — que Turing arma con dos alias y dos primitivas tabulares (`f`, la que ya vimos, y `e1`):

```
e(done, x)
  → e(e(done, x), done, x)                 # alias
  → f(e1(e(done, x), done, x), done, x)    # alias
  → … f camina hasta encontrar la próxima 'x' …   [pasos tabulares]
  → e1(e(done, x), done, x)                # f la encontró, entra a e1
  → (borra la x) ; luego → e(done, x)      # paso tabular + reescritura
  → e(done, x)                             # de vuelta al principio: buscar la próxima x
  → …                                      # repetir hasta que f no encuentre más
```

El término intermedio `e(e(done, x), done, x)` se construyó al vuelo y se descartó enseguida — nunca fue parte de una tabla precalculada. Eso es laziness en acción, no una metáfora.

## Escribir máquinas en los glifos de Turing

Todo lo anterior sería un ejercicio interesante pero incómodo si hubiera que escribir los términos a mano como strings. El proyecto expone un builder fluido que arma tablas y alias sin perder la fidelidad a la notación:

```python
from turing_machine import Machine, Program, Tape, m_function

# Máquina I (§3): imprime 0, _, 1, _, … → 0101…
machine_i = Program(
    m_function('q1').when_blank().write('0').right().goto('q2'),
    m_function('q2').when_blank().erase().right().goto('q3'),
    m_function('q3').when_blank().write('1').right().goto('q4'),
    m_function('q4').when_blank().erase().right().goto('q1'),
)
print(Machine(machine_i, start='q1', tape=Tape.blank()).run(figures=10))  # 0101010101
```

Y la biblioteca estándar del §4 —la que compone `f`, `e`, `c1`, etc.— está escrita con los glifos reales, no con nombres ASCII inventados:

```python
m_function('f', 'ℭ', '𝔅', 'α')
    .when(_S).left().goto('f1(ℭ, 𝔅, α)')
    .when_not(_S).left().goto('f(ℭ, 𝔅, α)')
    .when_blank().left().goto('f(ℭ, 𝔅, α)'),
```

Esto funciona porque las letras góticas y griegas viven dentro de strings del DSL, no como identificadores de Python — así que no hay normalización NFKC[^nfkc] que las aplaste a ASCII por accidente. `is_symbol_var` reconoce una letra griega minúscula (glifo o nombre completo, `α` o `alpha`); `is_m_config_var` reconoce cualquier token que empiece con mayúscula, gótica o latina. El resultado es que se puede escribir literalmente la notación del paper, o su transliteración ASCII, indistintamente — y ambas producen el mismo árbol de términos.

## Números de descripción: el §5

Hay una sección del paper que casi nadie implementa porque no hace falta para "correr" una máquina, pero que es el corazón de la idea de máquina universal: el §5 le asigna a cada máquina un único número entero — su **Descripción Estándar**, convertida a un **Description Number** codificando cada instrucción como una secuencia de símbolos `D`, `A`, `C`, `R`, `L`, `N`, `;`. Esto es lo que permite, más adelante en el paper, que una máquina lea la descripción de *otra* máquina desde su propia cinta y la simule — la máquina universal.

Para calcular esa codificación hace falta la tabla **completa** y **finita** — es decir, la versión ansiosa. Por eso el proyecto tiene las dos estrategias conviviendo a propósito: el intérprete perezoso corre máquinas (incluidas las que nunca terminan), y un expansor ansioso (`expand.py`) enumera el conjunto finito de estados alcanzables de una máquina concreta y produce la tabla plana que alimenta la codificación:

```bash
uv run python -m turing encode examples.machine_i --dn
# 31332531173113353111731113322531111731111335317
```

Que la expansión ansiosa y la ejecución perezosa calculen exactamente la misma secuencia — hay un test que lo verifica machine por machine — es la demostración práctica de que el modelo perezoso es fiel a la "sustitución repetida" del paper: son el mismo cómputo visto de dos maneras.

## Por qué vale la pena hacer esto

Uno podría preguntarse para qué construir esto en 2026, cuando ya sabemos perfectamente qué es computable y no necesitamos a Turing para calcularlo. La respuesta, para mí, no tiene que ver con computabilidad — tiene que ver con lo que se aprende de un texto fundacional cuando lo tomás en serio hasta el nivel de la notación. "On Computable Numbers" no es solo el paper que inventa la máquina de Turing: también es, sin que se lo suela leer así, uno de los primeros textos que describe un **sistema de reescritura de términos** con **funciones parametrizadas** y **sustitución** como mecanismo de evaluación — la misma idea que después reaparece, formalizada, en el cálculo lambda, en el modelo de sustitución de SICP,[^sicp] y en cualquier intérprete que evalúa un AST reemplazando variables por valores.

Implementar la notación tal cual, glifos incluidos, obliga a resolver ambigüedades que una paráfrasis moderna esconde — como la de "¿esta hoja es un símbolo o una configuración?" — y esas ambigüedades, una vez resueltas, terminan explicando decisiones de diseño que uno encuentra después en lenguajes bastante más modernos. Petzold hace un trabajo notable línea por línea sobre el paper en _The Annotated Turing_;[^petzold] este proyecto es la versión "y ahora hacé que compile" de esa misma lectura.

## Las decisiones que son mías

Escribí buena parte del código en colaboración con Claude, de Anthropic — lo cuento con más detalle abajo. Pero el diseño, en el sentido de "qué forma tiene que tener esto para ser correcto y fiel al paper", es mío. Concretamente:

- **Modelar el estado como término, no como etiqueta plana**, y tomar literalmente la frase de Turing de que "la tabla completa se obtiene por sustitución repetida" — esa lectura es la que arma todo el proyecto, y no es la lectura habitual del paper.
- **Reescritura perezosa en vez de expansión ansiosa** como estrategia de ejecución, específicamente para poder correr máquinas que no terminan sin toparse con el problema de expansión infinita que el propio Turing señala.
- **Puertos y dependency injection por constructor**, con una capa de arquitectura que `.importlinter` hace cumplir en cada corrida de CI: `encode → expand → machine → {table, tape} → {terms, ports} → symbols`. `Machine` recibe `ProgramPort` y `TapePort` por constructor y nunca construye un adaptador concreto — la única forma de que el motor no termine acoplado a una cinta o un programa en particular.
- **Table y Alias como dos tipos de entrada distintos**, indexados por `(nombre, aridad)` para que las sobrecargas de Turing (`e/3` vs. `e/2`, varias `ce`/`cp`/`cpe`) convivan sin colisionar.
- **Resolver la ambigüedad símbolo-vs-configuración por el tipo del parámetro que la recibe**, en vez de mantener una tabla de namespaces separada — la decisión que ya conté en la sección de términos.
- **No incluir `cr`** (copiar sin borrar el marcador) en la biblioteca estándar porque no tenía una transcripción confiable de esa tabla — preferí dejarla afuera, documentada como faltante, antes que adivinar una versión y que quedara mal.
- **El layout de casilleros alternados** (cifras en las casillas pares, marcadores en las impares), que es el que usa Turing mismo en el paper y que además es load-bearing: `f` detecta el final de la cinta por dos blancos consecutivos seguidos, así que borrar un marcador mal en el medio de la cinta rompería esa detección.
- **Reusar la misma función `resolve_and_select`** tanto en el intérprete en vivo como en el expansor estático, para que las dos estrategias no puedan divergir silenciosamente — es lo que permite el test que compara ejecución perezosa contra expansión ansiosa y verifica que calculan la misma secuencia.
- **Usar el Número de Descripción de la Máquina I, tal como aparece impreso en el paper, como ancla de corrección**: si el codificador no reproduce ese entero exacto, algo está mal en el modelo, no en un detalle de implementación.

Ninguna de estas es una decisión que uno tercerice completamente a un asistente de IA — son las que definen si el proyecto es fiel al paper o simplemente "otra simulación de máquina de Turing" con nombres bonitos.

El código está completo en el repositorio,[^repo] con un CLI para correr, trazar y codificar máquinas, y un [documento de diseño](https://github.com/CesarBallardini/turing-lazy-term-rewriting-interpreter/blob/main/docs/lazy-term-rewriting-interpreter.md) que explica el modelo de ejecución con más detalle del que entra acá. Si alguna vez leíste el paper de Turing y te quedaste con ganas de ver la notación *correr*, es exactamente para eso que lo escribí.

Una aclaración sobre el repositorio: lo escribí con la asistencia de Claude, de Anthropic. Las decisiones de arriba son mías; buena parte del código que las implementa se escribió en colaboración con la IA.

[^turing1936]: A. M. Turing, [_On Computable Numbers, with an Application to the Entscheidungsproblem_](https://doi.org/10.1112/plms/s2-42.1.230), _Proceedings of the London Mathematical Society_, s2-42(1) (1937), pp. 230–265 (recibido el 28 de mayo de 1936). Copia de acceso libre: [PDF en la University of Virginia](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf). Las citas de este post corresponden a los §§3–5 del paper.

[^repo]: César Ballardini, [_turing-lazy-term-rewriting-interpreter_](https://github.com/CesarBallardini/turing-lazy-term-rewriting-interpreter), repositorio en GitHub. Incluye el intérprete, el CLI `turing`, la biblioteca estándar del §4, el codificador de Números de Descripción del §5, y el documento de diseño citado en este post.

[^petzold]: Charles Petzold, _The Annotated Turing: A Guided Tour Through Alan Turing's Historic Paper on Computability and the Turing Machine_, Wiley, 2008. Recorrido línea por línea del paper de 1936, incluidas las tablas esqueleto y la máquina universal. Disponible para préstamo digital controlado en [archive.org](https://archive.org/details/annotatedturingg0000petz) (requiere cuenta gratuita; no es descarga libre).

[^sicp]: Harold Abelson & Gerald Jay Sussman, con Julie Sussman, _Structure and Interpretation of Computer Programs_, MIT Press, 2.ª ed. 1996 — en particular el modelo de sustitución de evaluación (§1.1.5). [Versión libre online](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html).

[^lazy]: Sobre evaluación perezosa vs. ansiosa en general: [«Evaluation strategy»](https://en.wikipedia.org/wiki/Evaluation_strategy) en Wikipedia da un contraste conciso entre _call-by-value_, _call-by-name_ y _call-by-need_. Graham Hutton, _Programming in Haskell_ (2.ª ed.), cubre la laziness en la práctica; el explicador de Computerphile [«Infinite Data Structures: To Infinity & Beyond!»](https://www.youtube.com/watch?v=bnRNiE_OVWA) es una introducción visual libre a por qué la laziness permite computar con estructuras que nunca se materializan del todo — exactamente lo que hace posible correr máquinas de Turing que no terminan.

[^nfkc]: **NFKC** (_Normalization Form Compatibility Composition_) es una de las cuatro formas estándar de normalización Unicode, definida en el [Unicode Standard Annex #15](https://unicode.org/reports/tr15/). Colapsa caracteres "de compatibilidad" —variantes visual o semánticamente equivalentes de un mismo carácter, como letras de ancho completo, ligaduras o símbolos matemáticos alfanuméricos— a una forma canónica. Importa acá porque Python normaliza los identificadores con NFKC ([PEP 3131](https://peps.python.org/pep-3131/)): si las letras góticas o griegas fueran nombres de variables de Python en vez de texto dentro de strings, el propio lenguaje podría plancharlas a sus equivalentes ASCII antes de que el código las viera, perdiendo la distinción entre, por ejemplo, la ℭ gótica y la C latina.

[^img_hero]: Imagen de portada: [Alan Turing (1951)](https://commons.wikimedia.org/wiki/File:Alan_Turing_(1951).jpg) — fotografía de estudio de Elliott & Fry, 29 de marzo de 1951, vía Computer History Museum — Dominio público. Recortada a 2.5:1 para hero landscape.
