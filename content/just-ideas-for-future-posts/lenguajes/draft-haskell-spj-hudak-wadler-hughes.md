### A1-18 — Haskell: el lenguaje que no quería existir (Peyton Jones, Hudak, Wadler, Hughes)

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `haskell-spj-hudak-wadler-hughes`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-haskell-spj-hudak-wadler-hughes/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-13]], [[B-01]] (listas infinitas), [[B-02]] (Okasaki)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 2000-2400 palabras (elegido 2026-07-15: es un post histórico con cuatro voces que hay que dejar hablar y una tesis que necesita desarrollo — «consolidar es diseñar»; menos de 2000 lo deja en anécdota)

**Concepto:** La entrevista colectiva en *Masterminds* a los 4 principales arquitectos de Haskell (Simon Peyton Jones, Paul Hudak, Philip Wadler, John Hughes) cuenta la historia de cómo el comité no quería crear un nuevo lenguaje, sino consolidar los varios lenguajes funcionales lazy que existían en los 80. La consolidación terminó siendo tan opinionada que se volvió un lenguaje propio. El post discute esa historia y qué hace a Haskell distinto de su propósito original.

**Hook:** el lenguaje funcional puro más conocido del mundo se diseñó por COMITÉ para EVITAR diseñar un nuevo lenguaje. Spoiler: no funcionó. Acá está la historia.

**Outline:**

1. **El hook** — un comité que se juntó explícitamente para *no* hacer un lenguaje nuevo, y salió con el lenguaje funcional más conocido del mundo.
2. **El paisaje de los 80** — media docena de lenguajes funcionales lazy, cada uno con su universidad, su compilador y sus tres usuarios. El problema real que había que resolver no era teórico, era social.
3. **El mandato de consolidación** — qué se propuso el comité, en sus propias palabras (Masterminds + *A History of Haskell*).
4. **La tesis del post: consolidar es diseñar** — no existe la unión neutral de opiniones ajenas. Cada elección de consolidación es una elección de diseño con dueño.
5. **Las opiniones que se colaron** — pureza (sin escape hatch), type classes, y más tarde las monadas. Ninguna era «el consenso de lo que ya existía».
6. **«Avoid success at all costs»** — el chiste que era una política de diseño, y por qué le compró al lenguaje veinte años de libertad.
7. **Las cuatro voces** — dónde Peyton Jones, Hudak, Wadler y Hughes cuentan la misma historia distinto, que es la parte interesante de la entrevista colectiva.
8. **Qué le hizo el comité a Haskell** — el lenguaje resultante es más opinionado que cualquiera de sus insumos. Diseño por comité como *fortaleza*, contra todo el folclore de la industria.
9. **Coda personal** — mi relación real con Haskell y con los comités.

**Bibliografía:**
- **Fuente primaria del post.** Paul Hudak, John Hughes, Simon Peyton Jones y Philip Wadler, «A History of Haskell: Being Lazy with Class», en *Proceedings of the Third ACM SIGPLAN Conference on History of Programming Languages* (HOPL III), San Diego, 2007. DOI canónico [10.1145/1238844.1238856](https://doi.org/10.1145/1238844.1238856) (ACM DL; verificado vía api.crossref.org) — mirror libre en PDF en la página del propio Peyton Jones: [haskell-being-lazy-with-class.pdf](https://simon.peytonjones.org/assets/pdfs/haskell-being-lazy-with-class.pdf). `estable`. Toda fecha, la lista de lenguajes lazy y las atribuciones (type classes, mónadas, I/O temprano) del post salen de acá.
- [[tr-23]] *Masterminds of Programming* — Federico Biancuzzi & Shane Warden, O'Reilly, 2009. El capítulo **8, «Haskell»**, es la entrevista colectiva a Simon Peyton Jones, Paul Hudak, Philip Wadler y John Hughes. [Copia en archive.org](https://archive.org/details/MastermindsOfProgramming). `estable`.
- John Hughes, «Why Functional Programming Matters», *The Computer Journal*, vol. 32, n.º 2 (1989), pp. 98–107. DOI canónico [10.1093/comjnl/32.2.98](https://doi.org/10.1093/comjnl/32.2.98) (Oxford Academic, posible paywall; verificado vía api.crossref.org) — mirror libre (versión ampliada de 1990) en las páginas de Miranda de la Universidad de Kent: [whyfp90.pdf](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf). `estable`. Contexto para el rol de Hughes (combinadores de orden superior y modularidad) en la historia.
- [[tr-14]] [Papers de Philip Wadler](https://homepages.inf.ed.ac.uk/wadler/). Fuente primaria para el diseño de type classes (Wadler & Blott, 1989) y para el uso de mónadas siguiendo a Moggi. `estable`.
- Página y publicaciones de Simon Peyton Jones (hoy Engineering Fellow en Epic Games; antes Microsoft Research Cambridge, 1998–2022): [simon.peytonjones.org/publications](https://simon.peytonjones.org/publications/). `estable`.

**Imágenes:** _a definir_

**Tags propuestos:** `['Haskell','Peyton Jones','Wadler','Hughes','Hudak','historia','comité']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09; expandido a outline + prosa borrador el 2026-07-15 (generado por Claude, sin revisar por César). El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch: DOIs comprobados en api.crossref.org, texto de *A History of Haskell* extraído del PDF de la página de Peyton Jones) y se resolvieron 9 de 10 marcadores `[VERIFICAR:]`. El único que queda abierto es el de la frase «avoid success at all costs» (línea del apartado homónimo): **no aparece en *A History of Haskell*** —el paper articula la idea en su §3.7 («Haskell has not become too successful… the trouble with runaway success, such as that of Java…»), pero sin usar esa frase—, así que la autoría y el contexto exacto de acuñación siguen sin fuente en mano.

Qué quedó escrito: el arco completo — el paisaje fragmentado de los lenguajes lazy en los 80, el mandato de consolidación, la tesis central (consolidar es diseñar, y por eso el comité terminó pariendo un lenguaje propio), las tres opiniones fuertes que se colaron (pureza, type classes, monadas), «avoid success at all costs» como política y no como chiste, y la lectura de por qué el diseño por comité funcionó acá y casi nunca en otro lado.

Qué queda pendiente:

- **Verificación de hechos (mayormente resuelta el 2026-07-16).** Se abrió *A History of Haskell* (PDF de la página de Peyton Jones) y se resolvieron contra su texto: la reunión fundacional (septiembre 1987, FPCA, Portland, Oregón), la lista de lenguajes lazy (Miranda, LML, Orwell/OL, Alfl, Id, Clean, Ponder, Daisy), los dos modelos de I/O temprano (stream-based y continuation-based), la atribución de las type classes (Wadler & Blott, 1989) y la cronología de las mónadas (Moggi 1989 → Wadler 1992 → I/O monádico en Haskell 1.3, 1996). La bibliografía ya tiene DOI canónico + mirror libre para *A History of Haskell* y para *Why Functional Programming Matters*. **Queda un solo `[VERIFICAR:]` abierto**: la frase «avoid success at all costs» no está en el paper (ver Estado actual), así que su autoría/contexto sigue sin fuente. Sigue en pie que las **citas textuales de la entrevista colectiva** (los 🕳️ HUECO) requieren abrir *Masterminds* y las elige César.
- **La atribución de las citas de la entrevista colectiva** es el riesgo mayor del post: son cuatro personas hablando del mismo hecho y es fácil ponerle a uno la frase del otro. Cada `[VERIFICAR:]` de atribución es bloqueante.
- **Huecos de experiencia vivida.** Seis huecos: contacto real con Haskell, exposición a lenguajes lazy pre-Haskell, el momento «type classes», si le enseñó/estudió funcional en la facultad, la experiencia con comités de estándares en el sector público (que es el contrapunto que hace propio al post) y el veredicto de cierre.
- **Imágenes.** Sigue `_a definir_`. Opciones sin problema de licencia: un diagrama mermaid propio con el árbol de lenguajes lazy que confluyen en Haskell 1.0 (requiere que la lista de lenguajes esté verificada primero).
- **Cross-links.** [[A1-13]], [[B-01]] y [[B-02]] quedan sin resolver, como corresponde en drafting.

---

## Borrador de prosa

Casi todos los lenguajes de programación que conocés nacieron de alguien que quería un lenguaje. Haskell nació de un grupo de gente que explícitamente **no** quería otro lenguaje más. Se juntaron para arreglar el problema contrario: había demasiados.

Y el resultado de esa reunión antilenguaje es hoy el lenguaje funcional puro más conocido del planeta, el que aparece en las entrevistas de trabajo que nadie aprueba, el que le prestó ideas a media industria durante treinta años sin que casi nadie lo escribiera en producción. El comité falló en su objetivo declarado de la manera más rotunda posible: falló hacia arriba. Quiero contarte cómo pasó eso, porque la explicación no es un accidente gracioso. Es una tesis sobre qué significa consolidar.

### El problema no era teórico: era social

A mediados de los 80 la programación funcional lazy no tenía un problema de ideas. Tenía un problema de dispersión. Cada grupo de investigación serio tenía su propio lenguaje funcional perezoso, con su propio compilador, su propia sintaxis y su propio puñado de usuarios que eran, básicamente, los tesistas del mismo pasillo. *A History of Haskell* lo llama sin piedad «esta Torre de Babel lazy» y enumera los que confluyeron: **Miranda** (David Turner, sucesor de SASL y KRC, con tipado polimórfico fuerte), **Lazy ML (LML)** (Augustsson y Johnsson en Chalmers, cuna de la G-machine), **Orwell** (Wadler) y su variante **OL**, **Alfl** (Hudak, en Yale), **Id** (Arvind y Nikhil, en el MIT, dataflow), **Clean** (Plasmeijer y colegas, en Nijmegen), **Ponder** (Jon Fairbairn) y **Daisy** (un dialecto lazy de Lisp, en Indiana). La introducción del paper habla de «más de una docena de lenguajes no estrictos y puramente funcionales» en circulación.

Pensá en lo que eso significa en la práctica. Si escribías un paper con un algoritmo elegante en tu lenguaje, el grupo de la universidad de al lado tenía que traducirlo para probarlo. Si escribías una biblioteca, moría con tu tesis. Si querías comparar dos técnicas de compilación, no había forma limpia de hacerlo porque estabas comparando dos lenguajes distintos a la vez. Toda la comunidad estaba haciendo el mismo trabajo seis veces en paralelo, y ninguna de las seis versiones podía capitalizar sobre las otras cinco.

Ese es un problema de coordinación, no de investigación. Y los problemas de coordinación se resuelven con comités — que es exactamente la palabra que en nuestra industria funciona como insulto.

### El mandato: no inventen nada

Entonces se armó el comité. La historia canónica la cuentan los propios protagonistas en dos lugares: el paper de HOPL III de 2007 —firmado por Paul Hudak, John Hughes, Simon Peyton Jones y Philip Wadler, los mismos cuatro que después reaparecen en *Masterminds of Programming*[^masterminds]— y la entrevista colectiva de ese libro.[^history]

El mandato era modesto y explícito: no hacía falta un lenguaje nuevo, hacía falta **un** lenguaje. Uno solo, común, sobre el que la comunidad pudiera acumular. Tomar lo que ya funcionaba en los lenguajes existentes, limar las diferencias que eran de gusto más que de fondo, y publicar un estándar abierto que cualquiera pudiera implementar. La reunión fundacional está fechada con precisión en el paper: **septiembre de 1987, en la conferencia FPCA (Functional Programming Languages and Computer Architecture), en Portland, Oregón** — la versión que circulaba resultó exacta. El propio Peyton Jones, camino a esa FPCA, paró en Yale a ver a Hudak, y entre los dos (con Wadler, que estaba de visita) decidieron convocar el encuentro. El mandato quedó escrito en el Prefacio del primer Haskell Report (versión 1.0, fechado el 1 de abril de 1990): había «más de una docena» de lenguajes lazy equivalentes, su uso estaba «obstaculizado por la falta de un lenguaje común», y por eso «se decidió que un comité debía formarse para diseñar semejante lenguaje».

Fijate lo que hay adentro de ese mandato: la palabra «limar». Ahí está enterrada toda la historia.

> 🕳️ **HUECO — necesita a César:** ¿tuviste contacto con alguno de los lenguajes funcionales lazy anteriores a Haskell (Miranda sobre todo, que era el comercial)? ¿O tu primer encuentro con la familia fue directamente con Haskell? Una o dos frases con la época alcanzan; si la respuesta es «nunca», también sirve y escribo el post desde afuera.

### La tesis: consolidar es diseñar

Acá está el punto del post, y quiero decirlo derecho: **no existe la consolidación neutral**.

Cuando juntás seis lenguajes que difieren, cada diferencia te obliga a una decisión. Y las decisiones no vienen etiquetadas como «esta es de gusto» y «esta es de fondo». Alguien tiene que decidir *cuál* es cuál, y esa persona ya está diseñando. Si el lenguaje A es puro y el lenguaje B tiene una válvula de escape para hacer entrada/salida, no podés «promediar». Elegís. Y al elegir, no estás resumiendo el consenso de la comunidad: estás emitiendo una opinión sobre qué es la programación funcional, con la autoridad prestada de un comité que se presentaba como notario.

El comité de Haskell hizo esto una y otra vez. Y cada vez que lo hizo, en lugar de elegir el promedio, eligió la posición más exigente. Es un patrón sistemático y es lo que convierte a Haskell en un lenguaje con carácter en vez de en un mínimo común denominador — que es lo que el folclore de la industria predice que sale de un comité, y lo que efectivamente sale casi siempre.

### Las tres opiniones que se colaron

**La pureza, sin escape.** Haskell no tiene una puerta trasera cómoda para hacer efectos. Esa decisión no es la unión de lo que existía: es una posición, y una posición incómoda, porque durante los primeros años el lenguaje no tenía una respuesta buena para algo tan básico como leer una línea de la entrada estándar. El paper confirma que el Haskell temprano cargaba con **dos modelos alternativos de entrada/salida** conviviendo en el estándar: el *stream-based* (el programa como una función de una lista perezosa de respuestas a una lista de peticiones, `Request`/`Response`, heredado de Ponder y Miranda) y el *continuation-based* (las mismas transacciones envueltas en estilo de continuaciones, con una continuación de éxito y otra de fallo). Cada request tenía su transacción, y uno se podía definir en términos del otro. Un comité que buscara consenso hubiera agregado la válvula de escape en la primera reunión, porque la válvula resuelve el problema del día. El comité de Haskell aguantó el problema abierto durante años antes que ceder en el principio.

Eso no es actuar como notario. Eso es tener una idea de qué querés que sea el lenguaje y bancársela contra la conveniencia.

**Las type classes.** El sistema de clases de tipos de Haskell —la manera de decir «este tipo sabe comparar por igualdad», «este tipo sabe imprimirse»— es un mecanismo que resuelve el sobrecargamiento de operadores sin renunciar a la inferencia de tipos. El paper confirma la atribución: las type classes fueron propuestas por **Philip Wadler y su estudiante Steven Blott** (nótese la grafía, *Steven*, no Stephen), publicadas en «Wadler and Blott, 1989»; Blott formuló las reglas de tipos y probó el sistema correcto, completo y coherente en su tesis doctoral. *A History of Haskell* remarca lo accidental del asunto: fue «una feliz coincidencia de timing» que Wadler y Blott dieran con la idea justo cuando el diseño del lenguaje todavía estaba en flujo, y se adoptó «con poco debate». (Stefan Kaes formuló una idea parecida de forma independiente en 1988.) Y es, literalmente, la definición de lo contrario de consolidar: es material nuevo, inventado sobre la marcha, para resolver un problema que aparecía justamente porque se estaban juntando lenguajes con criterios distintos. El comité que no iba a diseñar un lenguaje nuevo inventó, en el camino, uno de los mecanismos de tipos más influyentes de las tres décadas siguientes. Hoy le podés rastrear los nietos en Rust, en Scala, en Swift.

**Las monadas.** Llegaron después, no estaban en el mandato, y son la razón por la que la pureza sin escape terminó siendo sostenible en vez de suicida. La cronología que da el paper es nítida: en **1989, Eugenio Moggi** publicó en LICS un trabajo sobre el uso de las mónadas de la teoría de categorías para describir rasgos de los lenguajes de programación (Moggi, 1989; Moggi, 1991); **Wadler** se dio cuenta de que esa misma técnica servía para *estructurar* programas funcionales, no solo para describirlos (Wadler, 1992), y él y otros en Glasgow vieron enseguida que las mónadas eran el marco ideal para la entrada/salida. El **I/O monádico se adoptó recién en Haskell 1.3, en 1996** — es decir, años después del mandato original y de los dos modelos de I/O anteriores. Es el episodio más interesante de la historia porque muestra el orden real de las cosas: **primero se sostuvo el principio, después apareció la técnica que lo hacía habitable**. Al revés de como trabaja la industria, que primero busca lo que funciona hoy y después escribe el manifiesto que lo justifica.

Si el comité hubiera cedido en la pureza en 1988 para poder imprimir por pantalla, nadie habría tenido la presión de encontrarle una solución elegante al problema, y la monada como interfaz de efectos probablemente no habría entrado nunca a un lenguaje de uso general. La terquedad fue productiva. Eso tiene que decirse más seguido.

Del hilo de las listas infinitas y la evaluación perezosa —que es la otra mitad de por qué Haskell es Haskell— hablo aparte en [[B-01]]; y de qué pasa con las estructuras de datos cuando las querés puras y eficientes al mismo tiempo, en [[B-02]].

### «Avoid success at all costs»

El eslogan del que Peyton Jones hizo un chiste corriente —evitar el éxito a toda costa— se cita siempre como humor inglés, y lo es, pero es también la descripción exacta de una política.[VERIFICAR: la frase «avoid success at all costs», su autoría y el contexto en que se acuñó; aparece en charlas de Peyton Jones y probablemente en *A History of Haskell*, pero no la cito sin fuente en mano]

El chiste tiene dos lecturas y las dos son verdad. La lectura tonta: nadie usa esto, ja. La lectura seria: **mientras nadie dependa de vos, podés seguir cambiando el lenguaje**. Un lenguaje exitoso es un lenguaje congelado, porque cada cambio le rompe el código a alguien que factura con eso. Haskell se pasó dos décadas pudiéndose romper a sí mismo. Cada vez que encontraban una idea mejor, la metían, y el costo era bajo porque la base instalada eran los propios investigadores.

Es un privilegio que casi ningún lenguaje se puede dar, y explica por qué Haskell sigue produciendo ideas que después emigran a lenguajes que sí tienen usuarios. Es el laboratorio, no la fábrica. Y el comité lo supo antes de que fuera obvio.

### Cuatro personas, una historia, cuatro versiones

Lo que hace valiosa a la entrevista colectiva de *Masterminds* no es que los cuatro cuenten la historia: es que la cuentan **distinto**, y en las juntas se ve el diseño real. (Del libro entero hablo en [[A1-13]]; el de Haskell es el **capítulo 8** y reúne a cuatro entrevistados a la vez — el grupo más grande del libro. No es el único capítulo colectivo, ojo: el de AWK junta a Aho, Weinberger y Kernighan, y el de UML a Booch, Rumbaugh y Jacobson, tres cada uno. Pero es el único con cuatro, y no es casualidad.)

> 🕳️ **HUECO — necesita a César:** este es el punto donde el post necesita las citas concretas de la entrevista. ¿Tenés el libro a mano (archive.org tiene el escaneo) para elegir vos qué respuesta de cada uno te parece la más reveladora? Si preferís, lo hago yo en una segunda pasada con el libro abierto, pero la elección de qué citar es editorial y es tuya.

Lo que sí puedo decir sin abrir el libro es cuál es la pregunta que le haría a la entrevista: los cuatro vienen de lugares distintos —y el propio paper deja ver de dónde viene cada uno—: **Peyton Jones**, el implementador de compiladores (Lazy ML y la G-machine en Glasgow, después GHC, y con el tiempo editor único del Report); **Wadler**, el de la teoría de tipos (type classes con Blott, y las mónadas siguiendo a Moggi); **Hughes**, el de los combinadores de orden superior y el testing (autor de «Why Functional Programming Matters» y, más tarde, coautor de QuickCheck con Koen Claessen); y **Hudak**, el organizador de Yale que coconvocó la reunión de FPCA y fue editor del primer Report. Y sin embargo firman juntos un paper de historia. Eso es rarísimo. Cuatro personas que sostienen la misma versión oficial de un evento son, casi siempre, cuatro personas que negociaron la versión oficial. El paper de HOPL es un documento notable y es, al mismo tiempo, un documento escrito por los ganadores de una discusión que ya terminó.

> 🕳️ **HUECO — necesita a César:** ¿alguno de los cuatro te resulta una figura conocida por otro lado (charlas, papers, el ecosistema QuickCheck)? Si tenés una relación con la obra de alguno de ellos en particular, ese es el ángulo por el que abriría esta sección.

### El comité que funcionó

En nuestra industria «diseñado por comité» significa: nadie se hizo cargo, todo el mundo metió su feature, el resultado no tiene forma. Y es una descripción justa de un montón de cosas.

Haskell es el contraejemplo, y creo que la razón es exactamente la que este post viene persiguiendo. **El comité de Haskell no negociaba entre stakeholders con intereses económicos: negociaba entre gente que compartía una estética.** No había un fabricante de hardware defendiendo su instrucción favorita ni un vendor con clientes que proteger. Había una discusión sobre qué es elegante, entre gente que estaba de acuerdo en que la elegancia importaba. Un comité así no produce el mínimo común denominador. Produce el **máximo** común denominador: lo más exigente que todos pueden aceptar.

Ese es el chiste final. Se juntaron a no diseñar un lenguaje, y lo que salió es más opinionado, más terco y más coherente que cualquiera de los lenguajes que venían a reemplazar. Porque la única manera de consolidar seis opiniones es tener una séptima.

### Lo que me queda

> 🕳️ **HUECO — necesita a César:** ¿cuál es tu relación real con Haskell? ¿Lo estudiaste, lo usaste, lo abandonaste, te da culpa no haberlo aprendido nunca? Cualquiera de esas es una buena apertura para el cierre — necesito la verdadera.

> 🕳️ **HUECO — necesita a César:** el contrapunto que haría propio a este post: trabajaste en el sector público (STG, Ministerio de Cultura de Santa Fe), donde los comités y los estándares son parte del paisaje. ¿Viviste algún comité técnico que haya producido algo *mejor* que lo que hubiera hecho una persona sola? ¿O tu experiencia confirma el folclore? Un caso concreto, aunque sea sin nombres.

> 🕳️ **HUECO — necesita a César:** ¿tu veredicto sobre la tesis del post? ¿«Consolidar es diseñar» te parece una verdad general —también para estándares, para APIs, para normas— o Haskell es un caso especial porque los que consolidaban eran todos académicos sin clientes? Una frase, y es el último párrafo.

[^masterminds]: *Masterminds of Programming: Conversations with the Creators of Major Programming Languages* — Federico Biancuzzi & Shane Warden, O'Reilly, 2009. [Copia en archive.org](https://archive.org/details/MastermindsOfProgramming). El **capítulo 8, «Haskell»**, es una entrevista colectiva a Simon Peyton Jones, Paul Hudak, Philip Wadler y John Hughes (confirmado en el [índice de O'Reilly](https://www.oreilly.com/library/view/masterminds-of-programming/9780596801670/ch08.html)). — [[tr-23]].

[^history]: Paul Hudak, John Hughes, Simon Peyton Jones y Philip Wadler, «A History of Haskell: Being Lazy with Class» (subtítulo confirmado), en *Proceedings of the Third ACM SIGPLAN Conference on History of Programming Languages* (HOPL III), San Diego, 2007. DOI canónico [10.1145/1238844.1238856](https://doi.org/10.1145/1238844.1238856) (verificado vía api.crossref.org); mirror libre en PDF: [haskell-being-lazy-with-class.pdf](https://simon.peytonjones.org/assets/pdfs/haskell-being-lazy-with-class.pdf), en la página de Peyton Jones. `estable`.

[^wadler]: [Papers de Philip Wadler](https://homepages.inf.ed.ac.uk/wadler/topics/parametricity.html) y los clásicos recopilados en [Lambda the Ultimate](http://lambda-the-ultimate.org/classic/papers.html) — [[tr-14]]. Fuente primaria para el trabajo sobre type classes y mónadas mencionado en el post.
