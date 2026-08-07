### D-03 — La máquina de Turing: una pizarra infinita y un cabezal terco

- **Archivo seed:** `dev/draft-maquina-de-turing.md`
- **Slug propuesto:** `maquina-de-turing-explicacion`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-maquina-de-turing-explicacion/index.md`
- **Serie:** D
- **Cross-links:** lleva a [[B-06]] (teoría imperativa), [[D-02]] (Sketchpad — el otro extremo: lo concreto), [[A1-04]] (Forth — máquinas mínimas)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** la "máquina de Turing" no es una máquina. Es un argumento matemático escrito por Alan Turing en 1936 para resolver un problema completamente abstracto (el *Entscheidungsproblem* de Hilbert), y resulta que ese argumento — una cinta infinita, un cabezal, un puñado de reglas — define lo que significa "computar". El post explica la máquina sin matemática, muestra por qué define los límites de lo posible, y por qué Turing nunca quiso que se la confundiera con una computadora real.

**Hook:** "en 1936 un estudiante de doctorado de 24 años publica un paper para responder una pregunta de Hilbert sobre lógica formal. En ese paper inventa, casi como herramienta secundaria, una *máquina imaginaria* con una cinta infinita y un cabezal. No quiere construirla. Sólo necesita que se le pueda razonar sobre ella. Diez años después, esa máquina es el modelo del que sale toda la computación."

**Outline:**
1. El contexto: el problema de la decisión de Hilbert (1928). ¿Existe un procedimiento mecánico que decida si un enunciado matemático es demostrable?
2. Quién era Turing en 1936 — estudiante en Cambridge, 24 años, Church en Princeton trabajando en lo mismo (lambda cálculo) en paralelo.
3. La construcción: cinta, alfabeto, estados, función de transición. Sin matemática, con dibujitos.
4. Qué prueba Turing:
   - existe una máquina universal que puede simular cualquier otra máquina (la idea del *programa-como-dato*).
   - el problema de la parada es indecidible — y eso responde negativamente a Hilbert.
5. La pregunta tonta pero importante: si la máquina es imaginaria, ¿por qué nuestras computadoras "son" máquinas de Turing? Respuesta honesta: no lo son exactamente; son aproximaciones con memoria finita. La equivalencia es teórica, no física.
6. La tesis de Church-Turing y por qué después de 90 años no hay candidato serio que la rompa.
7. Cierre: la diferencia entre Turing inventando un modelo formal y los ingleses de Bletchley construyendo Colossus en 1943. No son la misma cosa. Turing trabajó en el modelo formal (1936) y, en la guerra, sobre Enigma y la Bombe — **no** en Colossus, que diseñó Tommy Flowers (sobre planes de Max Newman) contra el cifrado de Lorenz. La cercanía de todo esto en un mismo país y una misma década es lo que confunde a todo el mundo. _(Corregido el 2026-07-16: el outline decía «Turing trabajó en ambas»; las fuentes confirman que no diseñó Colossus.)_

**Bibliografía:** _(verificada por fetch el 2026-07-16; DOI confirmados contra api.crossref.org)_

Fuentes primarias:

- [Alan M. Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society, ser. 2, vol. 42 (1936-37), pp. 230-265](https://doi.org/10.1112/plms/s2-42.1.230) — el paper original. DOI `10.1112/plms/s2-42.1.230` (verificado en Crossref). «Received 28 May, 1936.—Read 12 November, 1936.» Mirror libre (facsímil escaneado, sólo imagen): [PDF en cs.virginia.edu](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf). — DOI **estable**; mirror **frágil** (página personal de curso).
- [Alan M. Turing, *On Computable Numbers… A Correction*, Proceedings of the London Mathematical Society, ser. 2, vol. 43 (1937), pp. 544-546](https://doi.org/10.1112/plms/s2-43.6.544) — la corrección posterior. DOI `10.1112/plms/s2-43.6.544` (verificado en Crossref; el número apareció en 1938). — **estable**.
- [Alonzo Church, *An Unsolvable Problem of Elementary Number Theory*, American Journal of Mathematics, vol. 58 (1936), pp. 345-363](https://doi.org/10.2307/2371045) — el resultado de Church por el cálculo lambda, publicado unos meses antes que el de Turing. — **estable**.

Fuentes secundarias:

- [Charles Petzold, *The Annotated Turing: A Guided Tour through Alan Turing's Historic Paper on Computability and the Turing Machine*, Wiley 2008](https://www.charlespetzold.com/AnnotatedTuring/) — ISBN-13 978-0470229057. El paper de 1936 explicado línea por línea. — sitio del autor **estable**.
- [Andrew Hodges, *Alan Turing: The Enigma*, Princeton University Press 1983](https://archive.org/details/alanturingenigma0000hodg) — la biografía canónica. — archive.org **estable**.
- [Martin Davis, *The Universal Computer: The Road from Leibniz to Turing*, W.W. Norton 2000](https://archive.org/details/universalcompute0000davi) — traza la línea Leibniz→Hilbert→Turing; Davis es además quien acuñó el término «halting problem» (1958). — **estable**.
- [Stanford Encyclopedia of Philosophy — *Turing Machines*](https://plato.stanford.edu/entries/turing-machine/) — cubre la construcción, la máquina universal y por qué Turing prueba la indecidibilidad de los problemas CIRC?/PRINT?, no del «halting problem» tal como se lo enuncia hoy. — **estable**.
- [Stanford Encyclopedia of Philosophy — *The Church-Turing Thesis*](https://plato.stanford.edu/entries/church-turing/) — la tesis y por qué es tesis y no teorema. — **estable**.
- [Stanford Encyclopedia of Philosophy — *Alan Turing*](https://plato.stanford.edu/entries/turing/) — biografía intelectual; Fellow de King's en 1935, Princeton, Church. — **estable**.
- [The Alan Turing Internet Scrapbook](https://www.turing.org.uk/scrapbook/) — mantenido por Hodges. — **estable**.
- [Wikipedia — *Halting problem*](https://en.wikipedia.org/wiki/Halting_problem) — documenta que Turing no usó los términos «halt»/«halting» y que el nombre se atribuye a Davis. — contexto, **estable**.

**Imágenes:**
- _Wikimedia_: foto de Turing — [Alan Turing aged 16](https://commons.wikimedia.org/wiki/File:Alan_Turing_Aged_16.jpg) — license: public domain.
- _Wikimedia_: diagrama esquemático de una máquina de Turing — varios disponibles bajo CC.
- _Crear_: SVG simple de una máquina de Turing reconociendo `01010` como número par de unos (~45 min).
- _Crear_: comparación side-by-side de la cinta de Turing y la memoria RAM de una computadora moderna (~30 min).

**Tags propuestos:** `['Alan Turing', 'computabilidad', 'Hilbert', 'historia', 'fundamentos']`

**Estado actual:** prosa-borrador completa (~1.950 palabras, dentro del target medium), escrita sobre el outline de 7 puntos que ya estaba en el draft. Está escrito y no necesita más trabajo estructural: el encuadre del *Entscheidungsproblem*, la construcción de la máquina en prosa sin matemática, la máquina universal, la parada, la aclaración de que nuestras computadoras no «son» máquinas de Turing, la tesis de Church-Turing y el cierre Turing-modelo vs. Bletchley-fierro.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 6 de 6 marcadores [VERIFICAR:].

Lo que queda pendiente:

- **Marcadores `[VERIFICAR:]`: 0.** Los 6 se resolvieron el 2026-07-16 contra fuentes fetcheadas: (1) Hilbert & Ackermann 1928 / Congreso de Bolonia 1928 (Wikipedia *Entscheidungsproblem*); (2) Turing era *Fellow* de King's desde 1935, no estudiante de doctorado, y tenía 23 años al enviar el paper el 28-05-1936 (SEP, Scrapbook de Hodges); (3) prioridad de Church, apéndice de equivalencia y doctorado en Princeton 1936-1938 (SEP, Church 1936 en *Am. J. Math.* 58:345-363, DOI verificado); (4) **corrección importante halting-problem vs Entscheidungsproblem**: Turing no probó el «problema de la parada» —ese nombre es de Davis, 1952/1958—; probó la indecidibilidad de los problemas *circle-free* y de la impresión, y de ahí derivó la del *Entscheidungsproblem* codificando máquinas en lógica de primer orden (SEP *Turing Machines*, Wikipedia *Halting problem*); la prosa se reescribió para no repetir la atribución falsa; (5) rol en Bletchley: Enigma + Bombe, **no** Colossus (Wikipedia *Colossus computer*); (6) cita completa del paper: PLMS ser. 2, vol. 42, pp. 230-265, recibido 28-05-1936, leído 12-11-1936, DOI `10.1112/plms/s2-42.1.230`; corrección vol. 43, pp. 544-546, DOI `10.1112/plms/s2-43.6.544` (ambos verificados en Crossref).
- **6 huecos `🕳️`** — dónde y cuándo se cruzó César con el paper por primera vez, si dio esto en clase alguna vez, la anécdota de la analogía que usa para explicar la cinta, su opinión sobre Petzold, y el gancho al presente. Sin tocar.
- **Conflicto con el outline original: resuelto.** Las fuentes confirman que Turing no diseñó Colossus (fue Flowers, sobre planes de Newman, contra Lorenz). Se corrigió el punto 7 del outline y la prosa del cierre lo afirma explícitamente.
- Faltan las dos imágenes «_Crear_» (SVG de la cinta reconociendo `01010`, y el side-by-side cinta/RAM). La prosa las referencia en su lugar natural.

---

## Borrador de prosa

**Título tentativo:** La máquina de Turing: una pizarra infinita y un cabezal terco

---

Hay un malentendido que arrastramos hace noventa años y que empieza en el nombre. «Máquina de Turing» suena a máquina. Suena a que en algún sótano de Cambridge hubo un aparato con una cinta de papel, un motorcito y un cabezal que iba y venía haciendo ruido. No lo hubo. Nunca lo hubo, y nunca se intentó que lo hubiera. La máquina de Turing es un argumento: un argumento matemático, escrito adentro de un paper de lógica, para responder una pregunta que no tenía absolutamente nada que ver con construir computadoras.

En 1936 un estudiante de doctorado publica en los *Proceedings of the London Mathematical Society* un trabajo con el título más árido que se pueda pedir: *On Computable Numbers, with an Application to the Entscheidungsproblem*.[^turing1936] Está respondiendo a David Hilbert. Y en el camino, casi como herramienta secundaria — como quien se fabrica una morsa para poder sostener la pieza que en realidad quiere limar —, inventa una máquina imaginaria con una cinta infinita y un cabezal terco. No quiere construirla. Sólo necesita poder razonar sobre ella con precisión. Diez años más tarde, esa herramienta secundaria es el modelo del que sale toda la computación.

> 🕳️ **HUECO — necesita a César:** ¿cuándo y dónde te cruzaste con el paper de 1936 por primera vez — materia de la facultad, lectura por tu cuenta, el libro de Petzold? Una o dos frases alcanzan para abrir el post con algo tuyo.

## La pregunta que hizo Hilbert

Para entender qué está haciendo Turing hay que entender qué le estaban preguntando, y la pregunta es de una ambición hermosa.

Hilbert quería saber si la matemática podía mecanizarse. No metafóricamente: literalmente. El *Entscheidungsproblem* — el «problema de la decisión» — pregunta si existe un procedimiento efectivo, un método fijo, ciego, sin chispa ni intuición, que tomado un enunciado matemático cualquiera responda en una cantidad finita de pasos si ese enunciado es demostrable o no. Hilbert y Wilhelm Ackermann lo plantearon en esa forma en 1928, en su *Grundzüge der theoretischen Logik*; ese mismo año Hilbert dejó planteadas tres preguntas abiertas en el Congreso Internacional de Matemáticos de Bolonia, y la tercera es justamente el *Entscheidungsproblem*.[^davis] [^entscheidung]

Fijate lo que se está pidiendo. No un genio. Al contrario: se está pidiendo explícitamente **la ausencia de genio**. Un procedimiento que un empleado sin idea de matemática pueda ejecutar con lápiz, papel y paciencia, y que igual funcione. Hilbert apostaba a que ese procedimiento existía y que sólo faltaba encontrarlo.

Y acá aparece el problema técnico que le arruina la vida a cualquiera que quiera contestar la pregunta: **¿qué es un procedimiento efectivo?** Todos tenemos una intuición de qué significa «seguir un método mecánico», pero una intuición no se puede meter adentro de una demostración. Para probar que ese procedimiento **no existe** — que es lo que Turing va a probar — primero hay que decir con exactitud matemática qué sería una cosa así. No podés demostrar que no hay ninguna gallina en el gallinero si nadie definió qué es una gallina.

La máquina de Turing es la definición de gallina.

## Quién era Turing en 1936

Un joven matemático de Cambridge, recién egresado. Conviene ser preciso, porque acá circula un error cómodo: en 1936 Turing no era un estudiante de doctorado. Se había graduado en King's College en 1934 y en 1935, con veintidós años, ya lo habían elegido *Fellow* del college.[^scrapbook] [^sep-turing] Cuando envió el paper —la fecha de recepción es el 28 de mayo de 1936— tenía veintitrés; cumplió veinticuatro pocas semanas después, el 23 de junio. El doctorado vino después y en otro continente: recién en Princeton, entre 1936 y 1938. [^hodges]

No es una figura consagrada resolviendo el problema abierto de su generación desde una cátedra. Es alguien joven, medio lateral, que agarra una pregunta central de la lógica y la ataca por un ángulo que a los lógicos profesionales no se les había ocurrido: en vez de definir «procedimiento efectivo» con más lógica, lo define **describiendo a una persona que hace cuentas**. Un tipo con un lápiz, un papel cuadriculado, un estado mental limitado y reglas fijas. Después le saca a la persona, y lo que queda es la máquina.

Y del otro lado del Atlántico, Alonzo Church está llegando al mismo resultado por un camino completamente distinto — el cálculo lambda. Church publicó primero, apenas unos meses antes, en el *American Journal of Mathematics*.[^church] Turing se enteró de ese trabajo mientras preparaba el suyo para publicación, y agregó un apéndice demostrando que su noción de «computable» y la «λ-definibilidad» de Church abarcaban exactamente las mismas funciones.[^sep-ct] Poco después cruzó el Atlántico él mismo: se doctoró en Princeton, bajo la dirección de Church, entre 1936 y 1938.[^petzold] [^sep-turing]

Que dos personas, sin saberlo, con formalismos que no se parecen en nada — una cinta de papel por un lado, funciones puras por el otro —, terminen definiendo exactamente el mismo conjunto de cosas computables, no es una anécdota simpática. Es la evidencia central de la que va a salir la tesis de Church-Turing, y la vamos a ver al final.

## La construcción: una pizarra infinita y un cabezal terco

Acá va la máquina, sin una sola fórmula.

Imaginate una cinta de papel infinita hacia los dos lados, dividida en casilleros. En cada casillero hay un símbolo de un alfabeto finito y chico — pongamos `0`, `1`, y «blanco». Sobre la cinta hay un cabezal, y el cabezal está posado sobre exactamente un casillero. El cabezal puede leer el símbolo que tiene abajo, puede borrarlo y escribir otro, y puede moverse un casillero a la izquierda o un casillero a la derecha. Uno. Nunca dos.

La máquina, además, está en un **estado**, de una lista finita de estados posibles. Llamalos como quieras: `buscando`, `contando`, `volviendo`, `listo`. El estado es toda la memoria interna que la máquina tiene: no hay nada más adentro. Todo lo demás está afuera, escrito en la cinta.

Y eso es todo. El programa entero de la máquina es una tabla que dice, para cada combinación de (estado actual, símbolo leído), tres cosas:

1. qué símbolo escribir en ese casillero,
2. para qué lado moverse,
3. a qué estado pasar.

Nada más. No hay multiplicación, no hay saltos a una dirección arbitraria, no hay variables, no hay pila. Hay una pizarra, un cabezal terco que sólo sabe moverse de a un paso, y un puñado de reglas.[^sep-tm] [^wiki-tm]

Lo primero que uno piensa es «con eso no se puede hacer nada». Lo segundo, cuando lo probás, es que con eso se puede hacer **todo**. Sumar, multiplicar, ordenar una lista, decidir si una cadena tiene una cantidad par de unos, evaluar una expresión, correr un intérprete. Con lentitud absurda, con una tabla que crece feo, pero se puede.

![SVG — máquina reconociendo 01010](maquina-cinta.svg)

> 🕳️ **HUECO — necesita a César:** ¿alguna vez explicaste esto en clase o a alguien de cero? Si tenés una analogía propia para la cinta (el rollo de papel de la calculadora, la caja de un cassette, lo que sea), va acá y le da personalidad al post.

## Lo que Turing prueba

Con la máquina ya definida, el paper hace dos jugadas, y las dos son enormes.

**La primera: existe una máquina universal.** Turing se da cuenta de que la tabla de reglas de una máquina — su programa — se puede escribir como una tira de símbolos. Y una tira de símbolos es exactamente el tipo de cosa que va en la cinta. Entonces construye una máquina, una sola, que lee de la cinta la descripción de cualquier otra máquina más su entrada, y la simula paso por paso.[^sep-tm]

Leelo de nuevo despacio, porque en esa frase está toda la computación del siglo XX: **el programa es dato**. No hay una máquina por tarea; hay una máquina que hace la tarea que le pasás escrita. Eso es un ejecutable en el disco, es un intérprete, es la arquitectura de la computadora que tenés adelante. Turing lo escribió en 1936 como paso intermedio de una demostración sobre lógica, sin hardware, sin transistores, sin nada.

**La segunda: hay cosas que ninguna máquina puede decidir.** Acá conviene contar la historia con cuidado, porque casi todos la contamos mal. La versión que circula dice que Turing demostró que no existe una máquina que decida, para cualquier otra máquina, si «va a terminar» o «se va a colgar para siempre»: el famoso *problema de la parada* (*halting problem*). Es una forma cómoda y correcta en espíritu de explicarlo, pero no es literalmente lo que hizo Turing. En su paper de 1936 no aparecen las palabras «halt» ni «parada»: lo que Turing demuestra indecidible es si una máquina es *circle-free* —si sigue imprimiendo dígitos para siempre— y el *problema de la impresión*, si una máquina llegará alguna vez a imprimir cierto símbolo. El nombre «halting problem» y esa formulación son posteriores; se le atribuyen a Martin Davis, que lo usaba en clases desde 1952 y lo fijó por escrito en *Computability and Unsolvability* (1958).[^parada] Los problemas son equivalentes en fuerza, pero no idénticos, y la diferencia importa para no repetir una atribución falsa.

Lo que sí es de Turing es la estrategia de la prueba: un argumento diagonal con el que uno se muerde la cola. Supongamos que la máquina decisora existe; construimos con ella una máquina que hace exactamente lo contrario de lo que la decisora predice sobre sí misma, y ya está: contradicción. La máquina decisora no puede existir.[^sep-tm] [^petzold]

Y de ahí cae Hilbert. Turing codifica el comportamiento de cualquier máquina como un enunciado de lógica de primer orden, de manera que **un método que decidiera la demostrabilidad de cualquier enunciado serviría para decidir su problema de la impresión** —el que acaba de probar indecidible—. Como ese problema no se puede decidir, el método de Hilbert tampoco puede existir. La respuesta al *Entscheidungsproblem* es **no**, y la trajo un pibe con una cinta de papel imaginaria.[^sep-tm]

## La pregunta tonta pero importante

Si la máquina es imaginaria, ¿por qué decimos que nuestras computadoras «son» máquinas de Turing?

La respuesta honesta es: **no lo son**. Tu notebook no tiene una cinta infinita. Tiene una cantidad de memoria que se puede escribir en un sticker. Y una máquina con memoria finita no es una máquina de Turing: es un autómata finito, formalmente una bestia mucho más débil.

La equivalencia es teórica, no física. Lo que se afirma de verdad es algo más modesto y más interesante: **el modelo de cómputo de tu computadora no puede calcular nada que una máquina de Turing no pueda calcular**. El límite superior es el mismo. La cinta infinita no está ahí para prometer memoria infinita; está ahí para que la demostración no se caiga por una razón aburrida — para que cuando algo sea imposible, sea imposible por la naturaleza del problema y no porque se llenó el disco.

Por eso la cinta y la RAM se parecen tanto en un dibujo y significan cosas tan distintas: una es un artefacto de la ingeniería, la otra es un artefacto de la demostración.

![Comparación cinta de Turing / RAM](cinta-vs-ram.svg)

## La tesis de Church-Turing

Queda una punta suelta y es la más rara del asunto.

Turing definió «computable» como «lo que puede hacer una máquina de Turing». Church lo definió como «lo que se puede expresar en el cálculo lambda». Y las dos definiciones abarcan exactamente el mismo conjunto de funciones. Después aparecieron otros formalismos — otras maneras de decir «procedimiento mecánico» — y todos caen en el mismo conjunto.[^sep-ct]

De ahí sale la tesis de Church-Turing: **todo lo que un ser humano pueda calcular siguiendo un método mecánico, lo puede calcular una máquina de Turing**. Y ojo con la palabra «tesis», porque es deliberada. No es un teorema. No se puede demostrar, porque de un lado del signo igual hay una noción matemática precisa y del otro hay una noción intuitiva, informal, humana. Es una apuesta sobre el significado de una palabra.

Van noventa años y no apareció ningún candidato serio para romperla. Cada modelo de cómputo nuevo que se propuso — y se propusieron muchos, algunos exóticos — terminó siendo equivalente o más débil. Eso no la demuestra. Pero después de nueve décadas de gente inteligente pateando el neumático, empieza a parecerse bastante a un hecho sobre el universo.

> 🕳️ **HUECO — necesita a César:** ¿tenés una postura sobre la tesis? ¿Te resulta un hecho sobre la matemática, un hecho sobre la física, o una convención que nos sirve? El post gana mucho si acá aparece tu opinión y no una síntesis neutral.

## Turing el matemático y Turing el de Bletchley

Cierro con la confusión que hay que deshacer, porque es la razón por la que este post existe.

En la cabeza de mucha gente hay un solo Turing: el que «inventó la computadora», y que además la usó para ganar la guerra. Y son dos historias distintas, separadas por casi diez años y por una diferencia de naturaleza.

El Turing de 1936 escribe un modelo formal. No hay fierro, no hay presupuesto, no hay laboratorio. La máquina universal es un objeto de papel cuya única función es hacer posible una demostración de imposibilidad.

El Turing de Bletchley Park trabaja sobre criptoanálisis con máquinas electromecánicas reales, contra un enemigo real, con plazos reales. Y acá hay que corregir un error que la historia popular repite sin cansancio: Turing trabajó sobre el cifrado **Enigma** y diseñó la **Bombe**, la máquina electromecánica que ayudaba a descartar configuraciones de Enigma. No diseñó Colossus. Colossus —la primera de las cuales funcionó en diciembre de 1943— la diseñó Tommy Flowers, ingeniero del Post Office, sobre ideas de Max Newman, y atacaba otro cifrado por completo, el de Lorenz («Tunny»), no Enigma.[^colossus]

Y acá está el punto: **construir Colossus no requería el paper de 1936, y el paper de 1936 no requería Colossus.** Una es ingeniería de guerra, urgente y concreta, hecha por gente que necesitaba descifrar mensajes antes del martes. El otro es lógica pura, sin apuro, sin aplicación a la vista. Que las dos cosas hayan pasado en el mismo país, en la misma década, y con Turing cerca de ambas, hizo que la historia popular las fundiera en un relato lindo y falso: «el matemático imaginó la computadora y después la construyó para ganar la guerra».

No. Imaginó algo mucho más raro y más difícil de explicar en un documental: imaginó **el límite** de lo que se puede computar. No un aparato: una frontera. Que después esa frontera resultara ser también el plano de la máquina que estás usando para leer esto es una de las ironías más grandes de la historia de la ciencia, y no fue el plan de nadie.

El mismo tema visto desde el otro extremo — lo concreto, el fierro, la pantalla — aparece en [[D-02]], con Sketchpad. La contracara teórica, de qué significa que un lenguaje imperativo «compute», está en [[B-06]]. Y si te quedaste con ganas de máquinas mínimas que hacen todo con casi nada, [[A1-04]] habla de Forth, que es lo más cerca que llegó la ingeniería real al espíritu de la cinta y el cabezal.

> 🕳️ **HUECO — necesita a César:** ¿hay algo del presente que te haya hecho querer escribir esto ahora — alguna discusión sobre IA y «lo que las máquinas pueden hacer», algo que leíste, algo que te dijeron? Un cierre con anclaje en el hoy le daría razón de ser a la fecha de publicación.

> 🕳️ **HUECO — necesita a César:** ¿leíste *The Annotated Turing* de Petzold entero? Si sí, una línea tuya sobre si vale la pena (y para quién) funciona perfecto como recomendación final. Si no, sacamos la mención y queda sólo en las referencias.

> 🕳️ **HUECO — necesita a César:** ¿la traducción de términos te cierra? Usé «cabezal», «casillero», «estado» y «tabla de reglas»; si en tu experiencia docente o de lectura en español usabas otras (celda, cinta, tabla de transiciones), decime cuáles y unifico.

[^turing1936]: [Alan M. Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society, ser. 2, vol. 42 (1936-37), pp. 230-265](https://doi.org/10.1112/plms/s2-42.1.230) — el paper original. DOI `10.1112/plms/s2-42.1.230` (verificado en Crossref). Recibido el 28 de mayo de 1936, leído el 12 de noviembre de 1936. Facsímil libre (escaneo, sólo imagen): [PDF en cs.virginia.edu](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf). La corrección posterior: [*On Computable Numbers… A Correction*, PLMS ser. 2, vol. 43 (1937), pp. 544-546](https://doi.org/10.1112/plms/s2-43.6.544) — DOI `10.1112/plms/s2-43.6.544` (verificado en Crossref).
[^entscheidung]: [Wikipedia — Entscheidungsproblem](https://en.wikipedia.org/wiki/Entscheidungsproblem) — David Hilbert y Wilhelm Ackermann lo plantearon en 1928 (*Grundzüge der theoretischen Logik*); ese año Hilbert dejó tres preguntas abiertas en el Congreso Internacional de Matemáticos de Bolonia, la tercera de las cuales es el *Entscheidungsproblem*.
[^church]: [Alonzo Church, *An Unsolvable Problem of Elementary Number Theory*, American Journal of Mathematics, vol. 58 (1936), pp. 345-363](https://doi.org/10.2307/2371045) — DOI `10.2307/2371045` (verificado en Crossref). Publicado unos meses antes que el paper de Turing.
[^hodges]: [Andrew Hodges, *Alan Turing: The Enigma*, Princeton University Press, 1983](https://archive.org/details/alanturingenigma0000hodg) — la biografía canónica.
[^scrapbook]: [The Alan Turing Internet Scrapbook](https://www.turing.org.uk/scrapbook/) — mantenido por el propio Hodges. Documenta que Turing fue elegido *Fellow* de King's College en 1935.
[^sep-turing]: [Stanford Encyclopedia of Philosophy — Alan Turing](https://plato.stanford.edu/entries/turing/) — nació el 23 de junio de 1912; *Fellow* de King's en 1935; Princeton (doctorado con Church, 1936-1938).
[^petzold]: [Charles Petzold, *The Annotated Turing: A Guided Tour through Alan Turing's Historic Paper on Computability and the Turing Machine*, Wiley, 2008](https://www.charlespetzold.com/AnnotatedTuring/) — ISBN-13 978-0470229057. El paper de 1936 explicado línea por línea.
[^davis]: [Martin Davis, *The Universal Computer: The Road from Leibniz to Turing*, W.W. Norton, 2000](https://archive.org/details/universalcompute0000davi).
[^parada]: [Wikipedia — Halting problem](https://en.wikipedia.org/wiki/Halting_problem) — «Turing did not use the terms "halt" or "halting" in any of his published works, including his 1936 paper». El término y la formulación se atribuyen a Martin Davis (clases desde 1952; *Computability and Unsolvability*, 1958). Turing prueba indecidibles el problema *circle-free* y el problema de la impresión, no el «halting problem» tal como se lo enuncia hoy; son equivalentes en fuerza pero no idénticos. Ver también [SEP — Turing Machines](https://plato.stanford.edu/entries/turing-machine/).
[^colossus]: [Wikipedia — Colossus computer](https://en.wikipedia.org/wiki/Colossus_computer) — «It has sometimes been erroneously stated that Turing designed Colossus». Colossus la diseñó Tommy Flowers (sobre planes de Max Newman), funcionó en diciembre de 1943 y atacaba el cifrado de Lorenz (Tunny). Turing trabajó sobre Enigma y la Bombe.
[^sep-tm]: [Stanford Encyclopedia of Philosophy — Turing Machines](https://plato.stanford.edu/entries/turing-machine/).
[^sep-ct]: [Stanford Encyclopedia of Philosophy — The Church-Turing Thesis](https://plato.stanford.edu/entries/church-turing/).
[^wiki-tm]: [Wikipedia — Turing machine](https://en.wikipedia.org/wiki/Turing_machine) — lectura de contexto.

