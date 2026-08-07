### A1-14 — APL: el lenguaje de los símbolos griegos (entrevista a Adin D Falkoff)

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `apl-falkoff-iverson`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-apl-falkoff-iverson/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-13]] (roster), [[E-09]]
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** APL (A Programming Language) — inventado por Iverson en los 60, popularizado por Falkoff en IBM — es famoso por usar símbolos no-ASCII, programas extremadamente concisos, y un modelo basado en operaciones sobre arrays. El post toma la entrevista a Falkoff en *Masterminds* como punto de entrada y discute por qué APL desapareció del mainstream pero sus ideas viven en NumPy, Pandas, J, K, Q.

**Hook:** el lenguaje que usa símbolos griegos. El lenguaje que en una línea hace lo que C hace en 30. APL no se enseña en ninguna facultad de Latinoamérica. Sin embargo, NumPy y Pandas son APL disfrazado. El post es el rescate.

**Outline:**

1. **Hook — una línea contra treinta.** El lenguaje de los símbolos raros; la promesa de concisión; el planteo de que no murió, se disolvió.
2. **Iverson primero escribió una notación, no un lenguaje.** *A Programming Language* (1962) como notación para describir y enseñar, antes de que hubiera nada que ejecutarla.
3. **Falkoff y el salto a máquina.** La entrevista de *Masterminds* como punto de entrada: cómo la notación se volvió un lenguaje corriendo en IBM, y qué decisiones de diseño se tomaron ahí.
4. **El teclado como barrera y como virtud.** Los símbolos no-ASCII: qué compraban (densidad, ausencia de palabras clave, neutralidad respecto del idioma) y qué costaban (hardware especial, cultura de tribu).
5. **Por qué desapareció del mainstream.** Hipótesis a sopesar, no veredicto: el costo de entrada, el ecosistema propietario, la ola C/Unix/ASCII, la reputación de «write-only».
6. **Lo que sobrevivió: el modelo de arrays.** La idea central — operar sobre el agregado, no sobre el elemento; el bucle implícito. NumPy y Pandas como APL sin los símbolos.
7. **La línea directa de sangre: J, K, Q.** Los descendientes explícitos que volvieron a ASCII pero conservaron la densidad.
8. **Probarlo hoy.** GNU APL y Dyalog: cómo un lector puede escribir su primera expresión esta tarde.
9. **Cierre — la notación como herramienta de pensamiento.** Qué se pierde cuando un lenguaje se vuelve ilegible para los de afuera, y qué se gana cuando se vuelve legible para los de adentro.

**Bibliografía:**
- [Kenneth E. Iverson, *A Programming Language*, John Wiley & Sons, Nueva York, 1962](https://archive.org/details/aprogramminglanguage1962) — el libro que fundó la sigla APL. Es anterior al sistema ISBN (que empezó a usarse hacia 1970), así que no tiene ISBN. Copia completa en Internet Archive. `estable`
- [Adin D. Falkoff & Kenneth E. Iverson, «The Design of APL», *IBM Journal of Research and Development*, vol. 17, n.º 4, 1973, pp. 324-334](https://doi.org/10.1147/rd.174.0324) — DOI canónico (verificado en api.crossref.org). Texto completo libre en [jsoftware.com](https://www.jsoftware.com/papers/APLDesign.htm) y scan del original en [bitsavers](https://bitsavers.org/pdf/ibm/IBM_Journal_of_Research_and_Development/174/ibmrd1704F.pdf). `estable`
- [Kenneth E. Iverson, «Notation as a Tool of Thought», conferencia del Premio Turing 1979, *Communications of the ACM*, vol. 23, n.º 8, agosto de 1980, pp. 444-465](https://doi.org/10.1145/358896.358899) — DOI canónico (verificado en api.crossref.org). Texto completo libre en [jsoftware.com](https://www.jsoftware.com/papers/tot.htm). Es el texto donde Iverson formula la tesis del cierre del post. `estable`
- [[tr-23]] Masterminds of Programming (entrevista a Adin D. Falkoff sobre APL) — ver ficha en el plan editorial.
- [GNU APL](https://www.gnu.org/software/apl/) — intérprete libre (proyecto GNU, GPL), mantenido por Jürgen Sauermann; implementa el estándar ISO 13751 (*Programming Language APL, Extended*); corre en GNU/Linux, BSD, macOS y Windows. `estable`
- [Dyalog APL](https://www.dyalog.com/) — implementación comercial; ofrece una [Basic Licence gratuita para uso personal / no comercial](https://www.dyalog.com/prices-and-licences.htm). `estable`
- Para las fechas biográficas e históricas del post: [Kenneth E. Iverson en Computer Pioneers (IEEE Computer Society)](https://history.computer.org/pioneers/iverson.html), [APL (programming language) — Wikipedia](https://en.wikipedia.org/wiki/APL_(programming_language)) y [Adin Falkoff — Wikipedia](https://en.wikipedia.org/wiki/Adin_Falkoff). `estable`

**Imágenes:** _a definir_

**Tags propuestos:** `['APL','Iverson','Falkoff','arrays','historia','NumPy']`


**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (9 secciones), se fijó `Length target: medium` y se escribió un borrador de prosa completo (~1590 palabras de prosa efectiva, sin contar marcas de verificación ni huecos) en la sección «Borrador de prosa» al pie.

Lo que quedó **escrito**: el encuadre completo (notación antes que lenguaje, el salto a máquina vía Falkoff, el teclado como barrera, la disolución en el mainstream, el linaje NumPy/Pandas/J/K/Q, el cierre sobre notación como herramienta de pensamiento). El armazón argumental está entero y se sostiene solo.

Lo que quedó como **hueco**:

- 6 huecos `🕳️` pidiendo a César recuerdos y opiniones propias: si alguna vez se cruzó con APL y dónde, si lo vio en la facultad o en el sector público, su experiencia real con NumPy/Pandas, qué le pasó al leer la entrevista a Falkoff, y el veredicto personal del cierre. Sin esos, el post es un ensayo correcto pero impersonal — no es un post de katra todavía.
- 21 marcas `[VERIFICAR:]` sobre datos que **no** están respaldados por la bibliografía listada: fechas y nombre del primer APL ejecutable, la trayectoria de Falkoff e Iverson en IBM y el reparto real de tareas entre ellos, el mecanismo del teclado (typeball / terminales), la genealogía de J/K/Q con autores y años, el nicho financiero de Q/kdb+, el origen de NumPy y Pandas y si la influencia de APL sobre ellos es documentada o convergente, el estado actual de GNU APL / Dyalog (licencia, plataformas, free tier), las URLs de las cuatro fuentes, la ficha bibliográfica de Iverson 1962, la ejecución real de los ejemplos de código, y la afirmación del hook sobre las facultades de Latinoamérica.
- La bibliografía sigue siendo delgada a propósito: sólo se cita Iverson 1962, [[tr-23]], GNU APL y Dyalog. **Antes de publicar hay que decidir** si se resuelven los `[VERIFICAR:]` agregando fuentes nuevas al plan (el paper de Iverson del Turing Award y el «The Design of APL» de Falkoff & Iverson serían los candidatos naturales, si se los verifica) o si se recorta el post a lo que las cuatro fuentes actuales sostienen.
- Los ejemplos de código APL del borrador están escritos de memoria y **no fueron ejecutados**. Hay que correrlos en GNU APL o Dyalog y corregirlos antes de publicar.
- `**Imágenes:**` sigue en `_a definir_` — el candidato obvio es un teclado APL o un typeball, pero hay que encontrar uno con licencia clara en Wikimedia Commons.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 15 de 19 marcadores `[VERIFICAR:]` (los dos [VERIFICAR:] extra que cuenta el grep están dentro de este mismo apartado de estado, no en el cuerpo). Se agregaron a la bibliografía, con cita completa y URL verificada: «The Design of APL» (DOI 10.1147/rd.174.0324, verificado en api.crossref.org, más mirror libre en jsoftware/bitsavers), «Notation as a Tool of Thought» (DOI 10.1145/358896.358899, verificado, más mirror en jsoftware), la ficha completa de Iverson 1962 (John Wiley, Nueva York; copia en archive.org; sin ISBN por ser previo al sistema), las URLs oficiales de GNU APL y Dyalog con su estado de licencia actual, y las fuentes biográficas/históricas (Computer Pioneers de IEEE CS, y Wikipedia para APL\360, Falkoff, IBM 2741, NumPy, pandas, J y K). La influencia de APL sobre NumPy quedó confirmada como **documentada** (Numeric lista «la familia de lenguajes APL» entre sus influencias), no como mera convergencia. Quedan **sin resolver a propósito** 4 marcadores: (1) la ejecución real de los ejemplos de código APL —no se pueden correr desde acá—; (2) el reparto fino de tareas Iverson/Falkoff, que el marcador pide contrastar contra la entrevista de *Masterminds* (no releída); (3) la universal negativa del hook sobre las facultades de Latinoamérica, que sigue siendo de César; (4) la vigencia **en 2026** del nicho financiero de Q/kdb+, que no se pudo confirmar con una fuente actual. Los 6 huecos `🕳️` y el Hook/Concepto quedaron intactos.

---

## Borrador de prosa

Hay un lenguaje de programación en el que esta línea:

```apl
(+/X) ÷ ⍴X
```

calcula el promedio de una lista de números. No hay bucle. No hay variable acumuladora. No hay `for (int i = 0; i < n; i++)`. Sumá todo, dividí por la cantidad de elementos, listo. En C te lleva unas treinta líneas si le ponés el andamiaje completo — declarar, iterar, acumular, dividir, cuidar el caso de la lista vacía. Acá son ocho caracteres, y tres de ellos no están en tu teclado.[VERIFICAR: correr esta expresión en GNU APL o Dyalog antes de publicar; está escrita de memoria y no fue ejecutada]

El lenguaje se llama APL, y voy a hacer una afirmación que suena a nostalgia de museo pero no lo es: APL no murió. Se disolvió. Está adentro de tu `import numpy as np` y no te diste cuenta.

### Primero fue una notación, no un lenguaje

Este es el detalle que a mí me reordenó la cabeza cuando lo entendí, y es el que casi nunca se cuenta.

Kenneth Iverson no se sentó a diseñar un lenguaje de programación. Escribió un libro que se llama, literalmente, *A Programming Language* — de ahí sale la sigla APL — y lo publicó en 1962.[^iverson1962] Pero lo que hay adentro de ese libro no es un manual de un lenguaje que existía. Es una **notación**. Una manera de escribir algoritmos en papel, con símbolos, para poder pensarlos y enseñarlos con precisión — de la misma forma en que la notación matemática te deja escribir `∑` en vez de un párrafo en castellano explicando que hay que sumar todos los términos.

O sea: la notación vino antes que el intérprete. El lenguaje nació como una herramienta para pensar y recién después alguien la enchufó a una computadora.

Iverson había empezado a desarrollar esa notación mientras era profesor asistente en Harvard, entre 1955 y 1960; recién en 1960 entró a la división de investigación de IBM, y el libro salió en 1962.[^iverson_bio]

Eso explica muchísimo de por qué APL se ve como se ve. Si tu objetivo original es escribir en un pizarrón, no te importa que el símbolo esté en ASCII. ASCII ni siquiera es el problema, porque el problema es el pizarrón. Los símbolos raros de APL no son una excentricidad de diseñador: son el residuo fósil de un lenguaje que empezó siendo matemática escrita a mano.

### Falkoff y el salto a la máquina

Acá entra Adin Falkoff, y acá entra la razón por la que este post existe.

*Masterminds of Programming*[^masterminds] es un libro de entrevistas a creadores de lenguajes — ya le dediqué un post entero [[E-09]] y otro al roster completo de las entrevistas [[A1-13]], así que acá voy directo al grano. El capítulo de APL es una conversación con Adin Falkoff. Iverson puso la notación; Falkoff fue central en el proceso de convertirla en algo que corriera de verdad, en IBM.

> 🕳️ **HUECO — necesita a César:** ¿qué te pasó cuando leíste la entrevista a Falkoff en *Masterminds*? ¿Hubo alguna respuesta puntual que te haya hecho parar y releer? Una o dos frases alcanzan — es el ancla personal del post.

La primera implementación con el juego de símbolos reconocible de APL fue APL\360, completada en noviembre de 1966 sobre un IBM System/360.[^apl360]

Falkoff era investigador y gerente en IBM Research desde 1955; Iverson entró en 1960, y desde ese año hasta 1980 los dos colaboraron en el diseño, el desarrollo y el uso de APL.[^falkoff_ibm]

[VERIFICAR: el reparto real de tareas entre Iverson y Falkoff en el diseño del lenguaje ejecutable. La formulación de este párrafo («Iverson puso la notación, Falkoff la llevó a la máquina») es una simplificación que hay que contrastar contra la entrevista antes de afirmarla así.]

Lo que sí quiero marcar es el cambio de naturaleza. Pasar de notación a lenguaje ejecutable no es una traducción mecánica: es donde se toman las decisiones irreversibles. En el papel podés ser ambiguo y el lector te entiende igual. En la máquina no. Cada símbolo tiene que tener un significado exacto, cada combinación tiene que estar definida, y de repente tenés que decidir qué pasa cuando alguien hace algo que en el pizarrón nunca se le habría ocurrido hacer.

### El teclado

APL necesitaba un teclado que no existía.

Los símbolos — `⍳`, `⍴`, `⌽`, `⍉`, `∘.` — no están en ninguna máquina de escribir estándar. Para escribir APL había que tener hardware especial.

Para escribir APL hacía falta un IBM 2741 (o un IBM 1050) con un *typeball* APL — la bocha intercambiable del mecanismo Selectric. Ese typeball tenía sólo 26 letras, todas en mayúscula itálica, y muchos símbolos especiales se armaban por *overstrike*, superponiendo dos golpes en la misma posición.[^typeball]

Vale la pena ser justo con lo que los símbolos compraban, porque el chiste fácil es reírse del teclado y ahí termina la discusión. Compraban tres cosas concretas:

- **Densidad real.** Un símbolo, una operación primitiva. No `array.reverse()` — `⌽`. Cuando toda la expresión te entra en una línea, la ves entera de un vistazo, y eso cambia cómo la pensás.
- **Cero palabras clave.** Nada de `if`, `while`, `return`. Y por lo tanto, nada de sintaxis en inglés.
- **Neutralidad de idioma.** Este me parece el punto más subestimado. `⍴` significa lo mismo para un programador de Buenos Aires que para uno de Tokio. `while` no.

Y costaban una sola cosa, pero grande: la barrera de entrada. No podías escribir APL en la máquina que ya tenías. No podías pegar un fragmento en un mail. No podías imprimirlo sin que se rompiera. En un mundo que se estaba estandarizando sobre ASCII, APL exigía un dialecto de hardware propio.

> 🕳️ **HUECO — necesita a César:** ¿llegaste a ver alguna vez un teclado APL, un typeball, o una terminal con el juego de caracteres, en persona? ¿O tu contacto con APL fue siempre por papel y pantalla?

### Por qué desapareció

Acá tengo que frenar y ser honesto: no tengo un veredicto, tengo hipótesis. Ofrezco cuatro, para sopesar, no para cerrar.

**El costo de entrada.** Ya lo dije: hardware especial. En una época donde el resto del mundo convergía a ASCII y a la terminal barata, APL pedía una excepción.

**El ecosistema propietario.** APL vivió mucho tiempo adentro de máquinas grandes y caras de un solo proveedor. Cuando la computación se movió a la máquina chica y al software libre, ese linaje no viajó bien.

**La ola C/Unix.** No hace falta que APL hiciera nada mal para perder. Alcanza con que otra cosa haya ganado más fuerte, y C con Unix atrás ganó de una manera que arrasó con casi todo lo que no se les pareciera.

**La reputación de «write-only».** El chiste clásico es que APL es un lenguaje de sólo escritura: lo escribís, funciona, y a la semana no entendés lo que escribiste. Yo creo que esta acusación es medio tramposa. Toda notación densa es ilegible para el que no la conoce — mirá una página de matemática de posgrado. La pregunta real no es si es legible para cualquiera, sino si es legible para el que la aprendió. Y ahí el veredicto ya no es tan obvio.

Sobre esto tengo que decir algo del hook original de este post, y prefiero decirlo con precisión: la afirmación de que APL «no se enseña en ninguna facultad de Latinoamérica» es del tipo de cosa que suena verdadera y no se puede probar.

[VERIFICAR: la afirmación «APL no se enseña en ninguna facultad de Latinoamérica» es una universal negativa, imposible de verificar y muy probablemente falsa en sentido estricto. Reescribir como algo defendible («no lo vi en ningún plan de estudios que conozca») o bajarla a anécdota personal.]

> 🕳️ **HUECO — necesita a César:** en tu carrera de grado, ¿APL apareció alguna vez? ¿Aunque sea mencionado al pasar en alguna materia de lenguajes o de historia de la computación? Si no apareció nunca, decilo así de simple — es el dato que reemplaza la afirmación grandilocuente.

> 🕳️ **HUECO — necesita a César:** ¿te cruzaste con APL en algún momento de tu vida profesional — en el sector público, en alguna consultoría, en algún sistema heredado? ¿O es un lenguaje que conocés puramente por lectura?

### Lo que sobrevivió

Ahora sí, el punto del post.

Sacale a APL los símbolos. ¿Qué queda? Queda una idea, y es esta: **operás sobre el agregado, no sobre el elemento.**

No recorrés el array. Le aplicás algo *al array*. El bucle está adentro de la operación, implícito, y vos nunca lo escribís. Cuando escribís `(+/X) ÷ ⍴X`, no le estás diciendo a la máquina *cómo* recorrer `X`. Le estás diciendo *qué querés de* `X`.

Ahora mirá esto:

```python
X.sum() / len(X)
```

Ese es el mismo pensamiento. Mismo modelo mental, misma ausencia de bucle, misma operación sobre el agregado. Lo único que cambió es que los símbolos se volvieron palabras y el teclado dejó de ser un problema.

Eso es NumPy. Y Pandas es lo mismo con etiquetas encima. Cuando escribís `df[df.edad > 30].salario.mean()` estás haciendo APL — selección booleana sobre un array, proyección, reducción — con sintaxis que entra en un teclado común. El broadcasting de NumPy es pensamiento de arrays. La vectorización es pensamiento de arrays. La regla de oro de NumPy («si escribiste un `for`, probablemente lo estás haciendo mal») es, palabra por palabra, la tesis de Iverson.

Y acá hay que ser preciso sobre el tipo de parentesco, porque es fácil exagerarlo. No es descendencia directa: es influencia documentada. Numeric —el paquete predecesor del que salió NumPy— declaraba explícitamente, entre sus fuentes de inspiración, «la familia de lenguajes APL», junto con MATLAB, Fortran, S y otros.[^numpy] O sea: APL no es el único padre de NumPy, pero figura, con nombre y apellido, en la lista de influencias reconocidas. No es un parecido que uno tenga que forzar con lente de arqueólogo: está escrito.

NumPy en su forma actual lo creó Travis Oliphant en 2005 (la versión 1.0 salió en 2006), unificando dos paquetes previos: Numeric —el original, iniciado por Jim Hugunin— y Numarray.[^numpy]

Pandas lo empezó Wes McKinney en 2008, mientras trabajaba en AQR Capital Management, una firma financiera; lo liberó como open source en 2009. El nombre viene de *panel data*, un término de econometría.[^pandas]

> 🕳️ **HUECO — necesita a César:** ¿usaste NumPy o Pandas en algún trabajo real? Si sí, ¿te acordás del momento en que «te cayó la ficha» de que había que dejar de escribir bucles y empezar a pensar en arrays enteros? Ese recuerdo es el puente perfecto entre las dos mitades del post.

### La línea directa de sangre

NumPy es un pariente. Pero hay descendientes explícitos, con apellido.

J, K y Q son lenguajes que vienen de APL de manera directa y declarada, y que tomaron la decisión que APL no había tomado: volver a ASCII. Conservaron la densidad, conservaron el modelo de arrays, y resignaron los símbolos griegos por combinaciones de caracteres que entran en cualquier teclado. Q, en particular, tiene un nicho industrial vivo en el mundo financiero — series de tiempo, datos de mercado, volúmenes enormes con latencia baja.

J lo desarrollaron a principios de los 90 el propio Kenneth Iverson junto con Roger Hui (primera aparición en 1990), y usa únicamente ASCII: para no repetir el problema de los símbolos especiales de APL, recurre al punto y a los dos puntos como *inflexiones* que forman palabras cortas.[^j_lang]

K lo desarrolló Arthur Whitney en 1993 —otra variante de APL— y lo comercializó Kx Systems. Sobre K se construyó kdb+, una base de datos columnar en memoria; y Q es el lenguaje que se agregó dentro de kdb+, fusionando el K subyacente con ksql para dar una sintaxis más parecida a SQL.[^k_lang]

[VERIFICAR: la afirmación sobre el nicho financiero de Q/kdb+ — verificar que sigue vigente en 2026 y no repetir un dato de hace diez años.]

Lo notable de J es lo que dice sobre el diagnóstico. Si el creador de la notación original terminó haciendo una versión en ASCII, eso es una admisión: el problema del teclado era real, y era grave, y valía la pena pagar fealdad sintáctica para resolverlo.

### Probalo esta tarde

Nada de esto es arqueología inaccesible. APL corre hoy, en tu máquina, gratis.

**GNU APL**[^gnuapl] es una implementación libre. La instalás, abrís el intérprete, y estás escribiendo APL en diez minutos.

**Dyalog APL**[^dyalog] es la implementación comercial, la que sostiene el APL profesional que todavía existe.

Es software libre del proyecto GNU (GPL), lo mantiene Jürgen Sauermann, implementa el estándar ISO 13751 (*Programming Language APL, Extended*) y compila en GNU/Linux, BSD, macOS y Windows.[^gnuapl]

Al día de hoy Dyalog ofrece una *Basic Licence* gratuita para uso no comercial —uso educativo, personal, experimental, pruebas de concepto, concursos, «por diversión»—; el uso comercial requiere licencia paga.[^dyalog]

El problema del teclado, que fue la herida mortal de APL, hoy es un detalle de configuración: las implementaciones modernas resuelven la entrada de símbolos con teclas muertas o prefijos. Lo que en 1970 exigía una pieza de hardware, en 2026 es una opción en un menú.

Hay algo casi cruel en eso. APL perdió una guerra por un problema que después se resolvió solo.

### La notación como herramienta de pensamiento

Cierro con lo que me parece la lección, y es más grande que APL.

Iverson no estaba tratando de hacer que las computadoras hicieran cosas. Estaba tratando de hacer que los humanos pensaran mejor. La notación no era el envoltorio del algoritmo: era el lugar donde el algoritmo se piensa. Cambiá la notación y cambiás qué pensamientos te resultan fáciles de tener.

Cuando escribís un `for` para recorrer una lista, la notación te está empujando a pensar en el elemento. Cuando escribís `+/`, te empuja a pensar en el conjunto. Son la misma computación y son dos cabezas distintas.

Por eso digo que APL no murió: la notación perdió, la idea ganó. Todos los que hoy escriben Pandas están pensando como Iverson quería que pensáramos, sin saberlo y sin haber tocado un símbolo griego en su vida. Es una victoria rara — la de las ideas que triunfan tan completamente que se vuelven invisibles, y el nombre del que las tuvo se pierde en el camino.

Y esto no es una lectura mía puesta en su boca: Iverson lo formuló con todas las letras. Cuando le dieron el Premio Turing en 1979, su conferencia se llamó, justamente, «Notation as a Tool of Thought» —la notación como herramienta de pensamiento— y se publicó en *Communications of the ACM* en agosto de 1980.[^notation]

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto, no el mío. ¿Te dan ganas de aprender APL en serio, o te alcanza con haber entendido de dónde viene NumPy? Las dos respuestas son buenas — pero la que cierra el post tiene que ser la tuya.

---

[^iverson1962]: Kenneth E. Iverson, *A Programming Language*, John Wiley & Sons, Nueva York, 1962. Copia completa en [Internet Archive](https://archive.org/details/aprogramminglanguage1962). El libro es anterior al sistema ISBN, así que no tiene uno.
[^masterminds]: Entrevista a Adin D. Falkoff sobre APL, en *Masterminds of Programming* — ver [[tr-23]] en el plan editorial.
[^gnuapl]: [GNU APL](https://www.gnu.org/software/apl/) — intérprete libre del proyecto GNU (GPL), mantenido por Jürgen Sauermann; implementa el estándar ISO 13751 (*Programming Language APL, Extended*) y corre en GNU/Linux, BSD, macOS y Windows.
[^dyalog]: [Dyalog APL](https://www.dyalog.com/) — implementación comercial; condiciones de licencia en [Prices and Licences](https://www.dyalog.com/prices-and-licences.htm), con una *Basic Licence* gratuita para uso no comercial.
[^iverson_bio]: [Kenneth E. Iverson — Computer Pioneers, IEEE Computer Society](https://history.computer.org/pioneers/iverson.html): profesor asistente en Harvard entre 1955 y 1960, entró a la división de investigación de IBM en 1960, y publicó *A Programming Language* (John Wiley) en 1962.
[^apl360]: La primera implementación con el juego de símbolos reconocible de APL fue APL\360, completada en noviembre de 1966 sobre un IBM System/360; ver [APL (programming language) — Wikipedia](https://en.wikipedia.org/wiki/APL_(programming_language)).
[^falkoff_ibm]: [Adin Falkoff — Wikipedia](https://en.wikipedia.org/wiki/Adin_Falkoff): investigador y gerente en IBM Research desde 1955; colaboró con Iverson de 1960 a 1980 en el diseño, desarrollo y uso de APL.
[^typeball]: [IBM 2741 — Wikipedia](https://en.wikipedia.org/wiki/IBM_2741): el terminal IBM 2741 (y el IBM 1050) usaba el mecanismo de la máquina Selectric con una bocha (*typeball*) intercambiable; APL requería un typeball APL específico. El juego de caracteres se completaba con *overstrikes*.
[^numpy]: [NumPy — Wikipedia](https://en.wikipedia.org/wiki/NumPy): NumPy lo creó Travis Oliphant en 2005 (versión 1.0 en 2006), unificando Numeric (iniciado por Jim Hugunin) y Numarray. Numeric declaraba influencias «de la familia de lenguajes APL, Basis, MATLAB, Fortran, S y S+, entre otros».
[^pandas]: [pandas (software) — Wikipedia](https://en.wikipedia.org/wiki/Pandas_(software)): Wes McKinney empezó pandas en 2008 en AQR Capital Management y lo liberó como open source en 2009. El nombre viene de *panel data*.
[^j_lang]: [J (programming language) — Wikipedia](https://en.wikipedia.org/wiki/J_(programming_language)): desarrollado a principios de los 90 por Kenneth E. Iverson y Roger Hui (primera aparición en 1990); usa sólo ASCII, con el punto y los dos puntos como inflexiones.
[^k_lang]: [K (programming language) — Wikipedia](https://en.wikipedia.org/wiki/K_(programming_language)): K lo desarrolló Arthur Whitney en 1993, comercializado por Kx Systems; es la base de kdb+ (base de datos columnar en memoria), y Q es el lenguaje incorporado a kdb+ que fusiona K con ksql.
[^notation]: [Kenneth E. Iverson, «Notation as a Tool of Thought»](https://doi.org/10.1145/358896.358899), conferencia del Premio Turing 1979, *Communications of the ACM*, vol. 23, n.º 8, agosto de 1980, pp. 444-465. Texto completo libre en [jsoftware.com](https://www.jsoftware.com/papers/tot.htm).
