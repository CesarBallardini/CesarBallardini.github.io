### C-06 — Curtis Poe sobre qué quiso decir Alan Kay con OOP

- **Archivo seed:** _draft-rest.md bucket 1 (cosechado 2026-04-09)_
- **Slug propuesto:** `curtis-poe-on-kay-oop`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-curtis-poe-on-kay-oop/index.md`
- **Serie:** filosofia
- **Cross-links:** [[A1-01]], [[A1-12]] (FU Berlin doc), [[C-05]], [[tr-22]]
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1600-2000 palabras (elegido 2026-07-15: es un post de discusión punto por punto de un texto ajeno, necesita espacio para citar y contra-argumentar, pero no es un deep-dive histórico)

**Concepto:** Curtis Poe (Perl developer veterano, autor de Test::Most) escribió en `curtispoe.org/articles/alan-kay-and-oo-programming.html` una lectura crítica de la definición de OOP de Kay, argumentando que la mayoría de los lenguajes "OO" mainstream nunca cumplieron lo que Kay quería. El post discute la lectura de Poe — dónde tiene razón, dónde simplifica, y qué dice esto del estado actual del paradigma OO.

**Hook:** cuando un Perl developer veterano lee a Alan Kay, sale algo interesante. Curtis Poe argumenta que C++/Java/Python no son OOP en el sentido de Kay, y que casi nadie programa OOP en serio. ¿Tiene razón? El post discute punto por punto.

**Outline:**

1. **El hook** — un Perl developer veterano lee a Alan Kay y llega a una conclusión incómoda: casi nadie programa OOP en serio.
2. **Qué dice Poe, en sus términos** — la definición de Kay (mensajería + retención/protección/ocultamiento local del estado-proceso + late-binding extremo) y la lectura que Poe hace de ella.
3. **La distinción fuerte: encapsulamiento ≠ aislamiento** — la analogía celular, y por qué es el mejor aporte del artículo.
4. **Dónde Poe tiene razón** — el mainstream se quedó con clases y herencia; el late-binding se perdió en el camino.
5. **Dónde Poe simplifica** — el propio Poe admite que Kay fue vago con «mensajería»; el argumento de Erlang como OOP verdadero es fuerte pero incompleto; el ejemplo de Python es una crítica al modelo de excepciones más que al paradigma.
6. **El cierre de Poe: «los objetos son expertos»** — la metáfora práctica, y qué gana y qué pierde.
7. **Coda personal** — qué me deja esto después de años de escribir sistemas «OO» que no lo eran.

**Bibliografía:**

- **[Alan Kay and OO Programming](https://curtispoe.org/articles/alan-kay-and-oo-programming.html)** — Curtis "Ovid" Poe, publicado 2019-05-17. Fuente central del post. **frágil** (blog personal) — backup Wayback: https://web.archive.org/web/20260610061001/http://curtispoe.org/articles/alan-kay-and-oo-programming.html (snapshot 2026-06-10). Verificado por fetch 2026-07-15: fecha, byline y todas las citas usadas en el borrador.
- **[Dr. Alan Kay on the Meaning of "Object-Oriented Programming"](http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en)** — Stefan Ram (FU Berlin), correspondencia por mail con Kay del 23 y 26 de julio de 2003. **Fuente primaria de la definición canónica** y la que el propio Poe enlaza. **frágil** (userpage personal) — mirror estable vía PURL: https://www.purl.org/stefan_ram/pub/doc_kay_oop_en (verificado: redirige a purl.archive.org y de ahí a la userpage) — backup Wayback: https://web.archive.org/web/20260613163927/http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en (snapshot 2026-06-13). Cubre el cross-link [[A1-12]].
- **[Alan Kay at OOPSLA 1997: The Computer Revolution has not Happened Yet](https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet)** — transcripción del keynote, Viewpoints Intelligent Archive (tinlizzie.org). Contiene el fraseo verificado «I made up the term object-oriented, and I can tell you I did not have C++ in mind». **frágil** (wiki) — backup Wayback: https://web.archive.org/web/20250721031221/https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet (snapshot 2025-07-21).
- **[Test::Most — Most commonly needed test functions and features](https://metacpan.org/pod/Test::Most)** — POD en metacpan; la sección AUTHOR dice literalmente «Curtis Poe, `<ovid at cpan.org>`». **estable** (metacpan). Respalda la credencial de Poe que el seed afirmaba y que su propio artículo no menciona.

**Imágenes:** _a definir_

**Tags propuestos:** `['Alan Kay','OOP','Curtis Poe','Perl','critica','paradigmas']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09; expandido a outline + prosa borrador el 2026-07-15 (generado por Claude, sin revisar por César). **Pasada de fuentes hecha el 2026-07-15** (Claude): 4 fuentes verificadas por fetch agregadas a la bibliografía, 10 de 11 marcas `[VERIFICAR:]` resueltas.

La premisa central **se sostiene**: el artículo de Poe existe, es del 2019-05-17, y todas las citas que el borrador le atribuía están efectivamente ahí con el fraseo que se suponía (analogía celular, «touch vague», «objects are simply experts», Erlang y Smalltalk como contraejemplos, el ejemplo de Python con división por cero).

Qué quedó escrito: el arco completo de discusión del artículo de Poe — resumen de su lectura de Kay, la distinción encapsulamiento/aislamiento, tres puntos donde le doy la razón, tres donde creo que simplifica, y el cierre sobre la metáfora de «los objetos son expertos».

Qué se resolvió en la pasada de fuentes:

- **Fecha del artículo**: 2019-05-17, expuesta en el sitio.
- **Credencial de Poe**: `Test::Most` confirmado vía el POD en metacpan (AUTHOR: «Curtis Poe, `<ovid at cpan.org>`»). Ojo: **el artículo no menciona esa credencial**; el dato es de CPAN, no del texto. Si César quiere presentarlo así, la nota al pie ya lo respalda.
- **Definición de Kay**: fuente primaria localizada y verificada — los mails a Stefan Ram del 23 y 26 de julio de 2003, que es además la fuente que el propio Poe enlaza. Esto cubre [[A1-12]].
- **Corrección de contenido (importante)**: el borrador decía que «el reproche de Poe a Java es que liga métodos en tiempo de compilación». **Eso no es lo que dice Poe.** Poe reconoce que los lenguajes OO en general no ligan el método hasta run time, y su reproche a Java es que *chequea en compilación que el método exista*; aparte distingue un segundo sentido de binding (tipo↔variable en Java vs. tipo↔dato en Perl). El párrafo se reescribió con el argumento real. La sospecha que el propio borrador anotaba estaba bien fundada.

Qué queda pendiente:

- **La cita «I did not have C++ in mind» (única marca `[VERIFICAR:]` viva).** Poe la reproduce como «I **invented** the term Object-Oriented…» sin citar fuente alguna. La única fuente primaria verificable que encontré —la transcripción de OOPSLA 1997 en tinlizzie.org— dice «I **made up** the term object-oriented…». No hay original de Kay con el fraseo «I invented». Hay que elegir: citar la transcripción con su fraseo real, o marcarla explícitamente como cita de segunda mano vía Poe. Sin verificar todavía: el video de la charla en Vimeo, y [[tr-22]].
- **Huecos de experiencia vivida.** Cinco huecos marcados: la exposición de César a Smalltalk/Pharo, si trabajó con Erlang, su relación real con Perl, el caso concreto de un sistema «OO» del sector público que no era OO, y su veredicto sobre el paradigma (que es el cierre del post). Ninguna búsqueda web los toca.
- **Imágenes.** Sigue `_a definir_`; una opción es un diagrama mermaid propio contrastando llamada a método vs. mensaje (no requiere licencia de terceros).
- **Cross-links.** [[A1-01]], [[A1-12]], [[C-05]] y [[tr-22]] quedan sin resolver, como corresponde en drafting.

---

## Borrador de prosa

Hay un género de texto que me gusta mucho y que casi no existe: el programador veterano de un lenguaje que nadie asocia con el tema, leyendo con atención al fundador de ese tema. No el evangelista, no el consultor con curso a la venta. El tipo que lleva veinte años resolviendo problemas reales en otra parte y que se sienta a leer las fuentes.

Eso es lo que hace Curtis «Ovid» Poe —desarrollador Perl de larga data, autor de `Test::Most`[^testmost]— en un artículo sobre Alan Kay y la programación orientada a objetos, publicado en mayo de 2019.[^poe] Y la conclusión a la que llega es incómoda: lo que casi todos llamamos OOP no es lo que Kay quiso decir, y por lo tanto casi nadie programa OOP en serio. Yo creo que tiene razón en lo importante y que simplifica en un par de lugares que vale la pena marcar. Vamos punto por punto.

### La definición, que es corta y que casi nadie leyó

El artículo arranca donde hay que arrancar: por lo que Kay realmente escribió. Poe cita la definición canónica:

> OOP to me means only messaging, local retention and protection and hiding of state-process, and extreme late-binding of all things.[^kaydef]

Leela despacio, porque tiene una ausencia que grita. No dice «clases». No dice «herencia». No dice «jerarquía de tipos». Dice tres cosas: **mensajería**, **retención y protección y ocultamiento local del estado-proceso**, y **late-binding extremo de todas las cosas**. Es decir: exactamente las tres cosas que el OOP mainstream no hace, o hace a medias, o hizo alguna vez y después optimizó hasta desaparecerlas.

Poe apunta además que Kay quedó amargado con haber elegido esa palabra —«objeto»—: «sigue amargado por haber elegido esa palabra. Hizo que la gente se enfocara en la implementación en vez del comportamiento, y de ahí en adelante fue todo cuesta abajo».[^amargo] Es una queja que uno entiende recién cuando ve el daño: enseñamos OOP dibujando cajitas con atributos adentro. La cajita es el sustantivo. El mensaje es el verbo. Kay quería que el paradigma se llamara por el verbo, y le quedó el nombre del sustantivo. Cuarenta años de currícula universitaria después, la cajita ganó.

Esto es el mismo hilo que tiro en [[A1-01]] y en [[C-05]]: la revolución del cómputo que Kay imaginaba no es que no llegó, es que llegó una versión con el nombre correcto y las ideas equivocadas.

### El mejor párrafo del artículo: encapsulamiento no es aislamiento

Si el artículo de Poe tuviera que sobrevivir en una sola línea, sería esta: **vos no te morís cuando se te mueren tus células, y eso no es encapsulamiento, es aislamiento**.[^celulas]

Acá Poe está separando dos cosas que la industria mezcló hasta volverlas sinónimos, y la separación es correcta y es importante.

**Encapsulamiento** es una promesa sobre el acceso: no toques mis campos, pasá por mis métodos. Es una convención de disciplina, y en la mayoría de los lenguajes es una convención que se puede violar con reflexión, con un cast, o con un guión bajo que todo el mundo ignora.

**Aislamiento** es una promesa sobre la falla: si yo me rompo, vos seguís. Eso es infinitamente más fuerte. Y es lo que Kay tenía en la cabeza, porque su modelo mental venía de la biología: un organismo con billones de células donde las células mueren todo el tiempo y el organismo no se entera.

Poe usa un ejemplo en Python para mostrar el contraste: un método al que le pasás una entrada inválida —una división por cero— lanza una excepción que se lleva puesto no sólo al objeto sino al código que lo contiene, y la falla se propaga hacia arriba hasta que alguien la atrapa o hasta que todo se cae.[^python] Un objeto que puede matar a todo el sistema al fallar no es una célula. Es un órgano vital, que es lo contrario de lo que Kay pedía.

Y del otro lado están los dos lenguajes que Poe pone como ejemplos de que sí se puede: **Smalltalk** y **Erlang** —al que llama, sin ahorrar entusiasmo, «un lenguaje de programación maravilloso» que encarna los principios de Kay—.[^erlang] Smalltalk porque podés modificar el sistema mientras corre —eso es el late-binding extremo llevado a la práctica, no a la diapositiva—. Erlang porque un proceso que se muere no se lleva puesto a nadie: se muere, alguien lo nota, alguien lo levanta de nuevo. Aislamiento de verdad, con el runtime haciéndose cargo.

> 🕳️ **HUECO — necesita a César:** ¿tuviste contacto real con Smalltalk o Pharo en algún momento (cátedra, curiosidad personal, trabajo)? Una o dos frases sobre cuándo y qué te dejó — si la respuesta es «nunca en serio», eso también sirve y lo escribo así.

> 🕳️ **HUECO — necesita a César:** ¿trabajaste alguna vez con Erlang, o con algún sistema con supervisión de procesos al estilo OTP? Si no, ¿desde dónde lo mirás: lectura, charlas, envidia sana?

### Dónde le doy la razón

**Uno: el mainstream se quedó con lo accesorio.** C++, Java, Python. Poe recuerda que Kay dijo que inventó el término y que no tenía a C++ en la cabeza.[^cpp] [VERIFICAR: Poe reproduce la cita como «I invented the term Object-Oriented, and I can tell you I did not have C++ in mind» **sin citar fuente alguna** (verificado por fetch 2026-07-15: el artículo se la atribuye a «Dr. Kay» y no enlaza nada). La única fuente primaria que pude verificar es la transcripción del keynote de OOPSLA 1997 en tinlizzie.org, y ahí el fraseo es distinto: «I **made up** the term object-oriented…». No encontré ningún original de Kay con el fraseo «I invented». Decidir antes de publicar: o se cita la transcripción de OOPSLA con su fraseo real, o se escribe «Poe cita a Kay diciendo…» y se asume la cita de segunda mano. Buscar además en la charla completa (hay video en Vimeo, sin verificar) y en tr-22.] La frase suena a chicana de foro, pero es literalmente la queja de un diseñador viendo su idea deformada: lo que se popularizó fue el sistema de tipos y la herencia, que son detalles de implementación, y lo que se perdió fue la mensajería, que era el punto.

**Dos: el late-binding se murió y nadie fue al velorio.** Acá conviene ser preciso, porque el reproche de Poe a Java no es exactamente el que suele resumirse. Poe no dice que Java ligue métodos en tiempo de compilación —de hecho arranca reconociendo que los lenguajes OO en general no seleccionan el método para el invocante hasta tiempo de ejecución—. Lo que dice es que en Java «ese código ni siquiera compila si el método no existe», porque Java chequea de antemano que el método exista y sea invocable.[^javabind] Y después distingue un segundo sentido de «binding»: ligar el *tipo* al *contenedor* (Java) contra ligar el tipo al *dato* mismo (Perl). Son dos argumentos separados, y el que hace fuerza contra el late-binding de Kay es el primero: un objeto que no puede recibir un mensaje que su clase no declaró de antemano no es el objeto-computadora que Kay tenía en la cabeza. Más allá de la letra chica, el diagnóstico general aguanta: la industria eligió performance y verificación estática, decisiones perfectamente defendibles, y en el paquete se llevó puesta la propiedad que Kay puso como tercera pata de su definición. No es que se debatió y se descartó. Es que se descartó sin debatir, y después se siguió llamando OOP al resultado.

**Tres: la palabra «objeto» hizo daño pedagógico real.** Cualquiera que haya enseñado esto lo vio: el alumno aprende a modelar sustantivos. `Cliente`, `Factura`, `Vehiculo`. Y termina con un modelo de datos anémico con getters, que es una base de datos disfrazada, no un sistema de agentes que se mandan mensajes.

### Dónde creo que simplifica

**Uno: «mensajería» sigue siendo vago, y Poe lo admite.** Es la honestidad más valiosa del artículo: Poe reconoce que este es «el único punto donde creo que Kay ha sido un poco vago», y arriesga una explicación: que Kay se quedó en la idea porque «muchos desarrolladores piensan que las ideas están buenas, pero quieren ver una implementación o una prueba de concepto».[^vago] Y no es un detalle menor: si mensajería significa «el objeto recibe datos y decide él qué hacer», entonces un `dispatch` dinámico sobre un diccionario de handlers en Python es mensajería, y `obj.metodo()` en Ruby —que es literalmente `send`— también lo es. La frontera entre «llamar a una función con nombre» y «mandar un mensaje» es más borrosa de lo que el artículo necesita que sea para que el argumento cierre limpio. Poe la deja borrosa y sigue. Yo hubiera querido que se quedara ahí un rato más.

**Dos: el ejemplo de Python prueba algo más chico de lo que parece.** Que una excepción no atrapada se lleve puesto el proceso es una propiedad del modelo de concurrencia y de errores del runtime, no del paradigma de objetos. Erlang tiene aislamiento porque tiene procesos livianos y supervisión, no porque sus módulos sean «más objetos» que una clase de Python. Es decir: Poe está usando a Erlang para ganar una discusión sobre OOP cuando en realidad está ganando una discusión sobre modelos de falla. Que igual es la discusión que hay que tener —pero conviene decir cuál es.

**Tres: «casi nadie programa OOP» corre el riesgo del escocés verdadero.** Si la definición es tan exigente que sólo la cumplen Smalltalk y Erlang, entonces sí, casi nadie hace OOP. Pero eso es una observación sobre la definición tanto como sobre la industria. La pregunta más interesante no es «¿esto es OOP de verdad?» sino «¿qué perdimos concretamente al quedarnos con la versión degradada?». Poe responde esa pregunta sin formularla, y el artículo sería más fuerte si la formulara.

### «Los objetos son expertos»

El cierre de Poe es una metáfora propia y me parece lo mejor que se llevó del ejercicio: los objetos son simplemente expertos; vos les decís qué necesitás y ellos se encargan.[^expertos]

Me gusta porque es operativa. No le decís al experto *cómo* hacer su trabajo —eso sería pasarle los pasos, o peor, leerle los campos y hacerle el trabajo vos—. Le decís *qué* necesitás. Si esa frase se hubiera enseñado en lugar de «un objeto es una instancia de una clase», habríamos escrito otro software.

Lo que la metáfora pierde es justo lo que Poe pasó todo el artículo defendiendo: el experto de la metáfora no se muere. La versión completa sería «los objetos son expertos, y si un experto se muere, la organización sigue funcionando y contrata otro». Que es, otra vez, Erlang.

### Lo que me queda

Escribí sistemas orientados a objetos durante años. Casi ninguno era orientado a objetos.

> 🕳️ **HUECO — necesita a César:** ¿cuál es tu relación real con Perl? El artículo es de un perlero y me gustaría abrir o cerrar con eso, pero necesito el dato tuyo: ¿lo usaste en producción, en qué época, para qué?

> 🕳️ **HUECO — necesita a César:** un caso concreto de un sistema del sector público (STG o Ministerio de Cultura de Santa Fe) que se llamaba «orientado a objetos» y era, en los hechos, estructuras de datos con getters y setters. ¿Cuál, de qué año, y qué era en realidad? Sin nombres propios de personas si preferís.

> 🕳️ **HUECO — necesita a César:** ¿tu veredicto? ¿El OOP mainstream es (a) un fracaso disfrazado, (b) una degradación razonable que compró performance y tooling a cambio de las ideas de Kay, o (c) otra cosa? Una frase alcanza y es el cierre del post.

Poe no escribió un artículo sobre Alan Kay. Escribió un artículo sobre cuánto tiempo puede sobrevivir una palabra después de que se le murió el significado adentro. Y eso sí es un tema de ingeniería.

[^poe]: [Alan Kay and OO Programming](https://curtispoe.org/articles/alan-kay-and-oo-programming.html) — Curtis "Ovid" Poe, 2019-05-17. [Copia en Wayback Machine](https://web.archive.org/web/20260610061001/http://curtispoe.org/articles/alan-kay-and-oo-programming.html) por si el sitio personal se cae.

[^testmost]: [Test::Most — Most commonly needed test functions and features](https://metacpan.org/pod/Test::Most) — la sección AUTHOR del POD dice «Curtis Poe, `<ovid at cpan.org>`». El artículo sobre Kay no menciona esta credencial; viene de CPAN.

[^kaydef]: [Dr. Alan Kay on the Meaning of "Object-Oriented Programming"](http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en) — correspondencia de Alan Kay con Stefan Ram, 23 y 26 de julio de 2003. Es la fuente que el propio Poe enlaza. Enlace estable vía PURL: <https://www.purl.org/stefan_ram/pub/doc_kay_oop_en>; [copia en Wayback Machine](https://web.archive.org/web/20260613163927/http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en). En el mismo intercambio Kay explica que pensaba los objetos como células o como computadoras individuales en una red, comunicándose sólo por mensajes, y que eso «se puede hacer en Smalltalk y en LISP».

[^amargo]: Poe, art. cit.: «And he's still bitter about choosing that word. It made people focus on the implementation rather than the behavior and it's all been downhill from there.» La atribución del enojo es de Poe; no cita una fuente de Kay para ese punto.

[^celulas]: Poe, art. cit.: «You not dying when your cells die isn't encapsulation; it's isolation.» En el mismo pasaje: «It's estimated that around 50 to 70 _billion_ cells die in your body every day.»

[^python]: Poe, art. cit. — el ejemplo es una división por cero que lanza una excepción y hace fallar tanto al objeto como al código que lo contiene.

[^erlang]: Poe, art. cit. — llama a Erlang «a marvelous programming language» y lo presenta como encarnación de los principios de Kay; a Smalltalk lo trae a propósito de cambiar el comportamiento del software mientras corre.

[^cpp]: Poe, art. cit., atribuye a Kay: «I invented the term Object-Oriented, and I can tell you I did not have C++ in mind», sin citar fuente. El fraseo verificable en la transcripción del keynote [Alan Kay at OOPSLA 1997: The Computer Revolution has not Happened Yet](https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet) (Viewpoints Intelligent Archive) es distinto: «I made up the term object-oriented, and I can tell you I did not have C++ in mind». [Copia en Wayback Machine](https://web.archive.org/web/20250721031221/https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet).

[^javabind]: Poe, art. cit.: «OOP languages generally don't select (bind) the method (`invoice`) for the invocant (`$order`) until run time» / «In a language like Java, that code won't even compile if the method doesn't exist. That's because Java at least checks to ensure that the method exists and can be called.» El segundo sentido de binding, en el mismo artículo: «Binding can also refer to binding a variable type to data… static languages such as Java often bind the data type to the variable… while dynamic languages such as Perl bind the data type to the data itself».

[^vago]: Poe, art. cit.: «But that doesn't really get to the core concept of messaging and frankly, this is the one area where I think Kay has been a touch vague, largely because many developers think that ideas are nice, but they want to see an implementation or proof of concept.»

[^expertos]: Poe, art. cit., párrafo final: «And that's it. Objects are simply experts. You tell them what you need and they get it done. Forget all of the handwaving about blueprints or 'data with behaviors.' Those are implementation details. And once you start thinking about objects as simply experts about a particular problem domain, OOP becomes much easier.» El artículo no atribuye la formulación a nadie más, así que se lee como propia de Poe.
