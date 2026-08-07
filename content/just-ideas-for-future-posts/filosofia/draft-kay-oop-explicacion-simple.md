### C-07 — La explicación simple de qué quiso decir Kay con OOP (consolidación de Reddit/SE)

- **Archivo seed:** _draft-rest.md bucket 1 (cosechado 2026-04-09)_
- **Slug propuesto:** `kay-oop-explicacion-simple`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-kay-oop-explicacion-simple/index.md`
- **Serie:** filosofia
- **Cross-links:** [[A1-01]], [[A1-12]], [[C-06]], [[tr-22]]
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1100-1300 palabras (post corto de aclaración conceptual, con un ejemplo; el Concepto pide «versión cortita, sin condescendencia»)

**Concepto:** Hay un thread de Reddit (`/r/programming/comments/bqu8td/a_simple_explanation_of_what_alan_kay_meant_when/`) y otro de Software Engineering Stack Exchange que consolidan, en lenguaje plano, la respuesta a "¿qué quiso decir Kay realmente?". El post toma esa consolidación, la simplifica todavía más, y la usa como punto de entrada para principiantes que intentan entender por qué los paradigmas OO modernos son distintos de la visión original.

**Hook:** si alguna vez te confundió que la gente dice "OOP no es lo que vos pensás", este post es para vos. Versión cortita, sin condescendencia, con ejemplos.

**Outline:**

1. **Hook** — la frase «OOP no es lo que vos pensás» y por qué suena a esnobismo cuando la escuchás por primera vez.
2. **Lo que casi todos aprendimos que era OOP** — la tríada de manual: clases, herencia, encapsulamiento. Es una definición operativa, funciona, y no es lo que Kay tenía en la cabeza.
3. **La consolidación de los foros** — qué responden el thread de Reddit y el de Software Engineering SE cuando alguien pregunta en serio qué quiso decir Kay. El punto central: la unidad no es el objeto, es el **mensaje**.
4. **El desplazamiento del acento** — de «qué es una cosa» a «qué se le puede pedir a una cosa, y qué decide ella al respecto». Ejemplo con pseudocódigo: llamada a método vs. envío de mensaje.
5. **Por qué la diferencia tiene consecuencias** — late binding, el receptor como dueño de la decisión, y por qué eso emparenta a la visión original más con sistemas distribuidos que con jerarquías de clases.
6. **Qué hacer con esto si recién empezás** — no es una corrección moral: es un segundo mapa del mismo territorio. Ninguno de los dos te habilita a despreciar el otro.
7. **Cierre** — la parte de la visión de Kay que no entró en los lenguajes que usamos, con salida hacia [[A1-01]].

**Bibliografía:**

_Pasada de fuentes 2026-07-15: todo lo que sigue fue verificado por fetch salvo donde se aclara lo contrario._

**Fuentes primarias de Kay** (todas verificadas):

- **Kay, Alan — «Dr. Alan Kay on the Meaning of "Object-Oriented Programming"»**, correos a Stefan Ram del 23 y 26 de julio de 2003. https://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en — **estable** (página institucional de FU Berlin; la propia página ofrece la URI canónica alternativa https://www.purl.org/stefan_ram/pub/doc_kay_oop_en). Es el documento de [[A1-12]]. Fuente primaria de: los «tres ingredientes», la analogía con células, y la decisión de dejar la herencia afuera del Smalltalk original.
- **Kay, Alan — «prototypes vs classes was: Re: Sun's HotSpot»**, lista squeak-dev, 10 de octubre de 1998. http://lists.squeakfoundation.org/pipermail/squeak-dev/1998-October/017019.html — **frágil** (archivo pipermail; la API de Wayback no reporta snapshot al 2026-07-15 — **pedir uno antes de publicar**, es load-bearing). Fuente de «The big idea is "messaging"».
- **Kay, Alan C. — «The Early History of Smalltalk»**, HOPL-II, ACM, 1993, pp. 69-95. DOI canónico: https://doi.org/10.1145/154766.155364 — **estable** (metadatos verificados vía https://api.crossref.org/works/10.1145/154766.155364; la página de ACM DL no se abre sin suscripción). Mirror libre en HTML: https://worrydream.com/EarlyHistoryOfSmalltalk/ — **frágil**; backup Wayback verificado: http://web.archive.org/web/20260703092243/https://worrydream.com/EarlyHistoryOfSmalltalk/
- **Kay, Alan — keynote de OOPSLA 1997, «The Computer Revolution Hasn't Happened Yet»**. Transcripción completa en el archivo del Viewpoints Research Institute (el instituto del propio Kay): https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet — **frágil** (wiki); backup Wayback verificado: http://web.archive.org/web/20250721031221/https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet — Fuente de la frase sobre C++ **y de su contexto**, que es lo que la vuelve interesante.

**Sobre Erlang y OOP:**

- **Armstrong, Joe — «Why OO Sucks»** (sección fechada en 2000). https://www.cs.otago.ac.nz/staffpriv/ok/Joe-Hates-OO.htm — **frágil** (página personal alojada en cátedra de Otago; Wayback no reporta snapshot al 2026-07-15 — pedir uno). Verificada. Importante: **contradice el folclore** — Armstrong dice que la respuesta verdadera a «¿Erlang es OO?» era «No of course not».
- **«Ralph Johnson, Joe Armstrong on the State of OOP»**, InfoQ, entrevista de Werner Schuster en QCon London 2010, publicada 2010-07-08. https://www.infoq.com/interviews/johnson-armstrong-oop/ — **frágil**. ⚠️ Abrí la página: confirma título, fecha y participantes, pero **no expone la transcripción**. La frase «Erlang might be the only object oriented language» **no quedó verificada**. No citarla hasta conseguir video o transcripción.

**Threads de foro** (la bibliografía original del draft — ⚠️ **ninguno pudo verificarse**):

- https://www.reddit.com/r/programming/comments/bqu8td/a_simple_explanation_of_what_alan_kay_meant_when/ — ⚠️ fetch bloqueado en `reddit.com` y `old.reddit.com`, sin snapshot en Wayback, y la búsqueda por el ID `bqu8td` no devuelve nada. Título y contenido **sin confirmar**.
- https://softwareengineering.stackexchange.com/questions/46592/so-what-did-alan-kay-really-mean-by-the-term-object-oriented (también [[tr-22]]) — ⚠️ fetch bloqueado; `api.stackexchange.com` también bloqueado; sin snapshot en Wayback. Título y contenido **sin confirmar**.

**Imágenes:** _a definir_

**Tags propuestos:** `['Alan Kay','OOP','paradigmas','introduccion']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado y un borrador de prosa completo (~1200 palabras). **El 2026-07-15 se le hizo la pasada de fuentes** (Claude; sin revisar por César).

⚠️ **PREMISA EN DUDA (de sourcing, no de contenido):** el **Concepto** dice que el post «toma esa consolidación» de los dos threads (Reddit y SE.SE) y la simplifica. Problema: **ninguno de los dos threads pudo abrirse** — `reddit.com`, `old.reddit.com`, `softwareengineering.stackexchange.com` y `api.stackexchange.com` están todos bloqueados para fetch desde este entorno, y Wayback no tiene snapshot de ninguno de los dos. O sea que el andamio declarado del post es, hoy, íntegramente **no verificado**: no sabemos ni el título real de los threads ni qué dicen.

La buena noticia es que **el contenido resistió sin ellos, y mejor**. Todo lo sustantivo que el draft atribuía a Kay quedó anclado en fuentes primarias del propio Kay, no en foros: los tres ingredientes y la analogía con células salen de sus correos a Stefan Ram (2003, doc de [[A1-12]]); «the big idea is messaging» sale de su mail a squeak-dev (1998); la frase sobre C++ sale de la transcripción de su keynote de OOPSLA 1997 alojada en el archivo de su propio instituto. Ninguna afirmación del post depende ya de los threads.

Eso deja una **decisión editorial para César**, que no es mía: el post ahora se sostiene solo con fuentes primarias, y el rol de los threads quedó reducido a «así fue como esta pregunta se volvió folclore». Opciones: (a) reencuadrar el Concepto — el post ya no consolida foros, va a las fuentes; (b) mantener el marco de foros y verificar los dos threads a mano en un navegador; (c) dejar los threads como color de apertura («la pregunta se hace todo el tiempo») y no como bibliografía. El Hook y el Concepto quedaron **sin tocar**, como corresponde.

Lo que se ganó en esta pasada:

- **6 fuentes nuevas verificadas por fetch**, 4 de ellas primarias de Kay, más el ensayo propio de Armstrong y la ficha de la entrevista de InfoQ. DOI del paper de HOPL-II confirmado vía Crossref. Backups de Wayback agregados para las dos frágiles load-bearing que sí tenían snapshot (worrydream y tinlizzie).
- **Un hallazgo que mejora el post:** la frase de C++ está siempre mal citada. Kay sigue, inmediatamente, con «I have many of the same feelings about Smalltalk». La cita que circula como chicana anti-C++ es en el original una advertencia de que ningún lenguaje, ni el suyo, es dueño de la idea. Eso está incorporado a la prosa y es probablemente lo mejor que tiene el post ahora.
- **Un hallazgo que va en contra del draft:** el párrafo de Erlang. Armstrong, en «Why OO Sucks», dice explícitamente que Erlang **no** es OO. La frase contraria que todo el mundo le atribuye («Erlang might be the only object oriented language») viene de la entrevista de QCon 2010, cuya página abrí pero no expone transcripción. Ver el marcador en la prosa: hay tres salidas posibles y la más interesante es contar la contradicción.

Lo que quedó pendiente:

- **4 marcadores `[VERIFICAR:]`** (eran 7: se resolvieron 4 y se agregó 1 nuevo). **Resueltos:** los tres ingredientes, la analogía con células, la herencia (Kay la dejó afuera a propósito, y lo dice él) y la frase sobre C++ con su contexto. **Quedan:** (1) el párrafo de Erlang, que necesita la transcripción o el video de QCon London 2010; (2) los detalles finos de versiones/años/autoría de Smalltalk, que requieren leer el paper de HOPL-II y citar página — el fetch del mirror devolvió resumen, no texto literal, y eso no cuenta como verificado; (3) el título real del thread de Reddit. **Nuevo:** (4) el título real de la pregunta de SE.SE — antes se daba por bueno y resulta que también sale del slug de la URL y tampoco pude abrirlo. Los dos últimos hay que copiarlos a mano de un navegador.
- **Pedir snapshots de Wayback** para dos frágiles load-bearing que no tienen: el mail de squeak-dev de 1998 y el «Why OO Sucks» de Otago. Ambas son la única copia verificada de sus respectivas citas.
- **5 huecos `🕳️` que necesitan a César.** Sin tocar: ninguna búsqueda web contesta por su vida. El hook («este post es para vos») sigue pidiendo al menos una experiencia propia de haber creído la versión de manual y haberse topado con la otra.
- **Imágenes:** siguen `_a definir_`. La captura del thread de SE.SE era lo obvio y ahora además es lo no verificable; conviene buscar algo en Wikimedia Commons (¿Alto de Xerox PARC? ¿Kay?) — no busqué imágenes en esta pasada.
- **Cross-links:** [[A1-12]] (el doc de FU Berlin) aparece en la prosa pero no está en el bullet de `Cross-links` del encabezado — agregarlo cuando se toque la metadata. Ahora también es la fuente primaria principal del post, así que con más razón.

---

## Borrador de prosa

Si alguna vez posteaste código orientado a objetos y alguien te contestó «bueno, en realidad eso no es OOP, Alan Kay quiso decir otra cosa», sabés exactamente de qué tono estoy hablando. Es una frase que llega con una sonrisita incorporada. Y lo peor es que quien la dice casi nunca sigue con la explicación: suelta el dato y se va, como si el resto fuera obvio.

Este post es el resto. Versión corta, sin condescendencia, con un ejemplo. No vengo a decirte que estuviste programando mal todos estos años. Vengo a contarte qué hay del otro lado de esa frase, porque cuando la desarmás resulta que es bastante más interesante que el pase de facturas al que la reducen.

### Lo que aprendimos que era OOP

Casi todos aprendimos la misma definición, y viene en tríada: **clases**, **herencia**, **encapsulamiento**. A veces se le agrega polimorfismo para hacer cuatro. Un objeto es una instancia de una clase, la clase describe qué datos tiene y qué puede hacer, la herencia te deja reusar una clase modificándola, y el encapsulamiento esconde los campos internos detrás de métodos públicos.

Esa definición no es una mentira. Es una definición **operativa**: describe con precisión lo que hacen Java, C++, C#, Python. Si programás con esa tríada en la cabeza, escribís programas que funcionan y que otros entienden. No hay nada que corregir ahí.

El problema es que esa tríada no es lo que Kay tenía en la cabeza cuando acuñó el término. Es una descripción de lo que la industria construyó *después*, con ese nombre puesto encima.

### Lo que responden los foros cuando se les pregunta en serio

Hay un thread de Reddit y una pregunta de Software Engineering Stack Exchange que hacen exactamente el trabajo que la gente del «en realidad» no hace: explican, en lenguaje plano y con cierta paciencia, qué era la idea original.[^reddit][^se]

El núcleo de la respuesta cabe en una oración: **la unidad de la orientación a objetos no es el objeto, es el mensaje**.

Leelo de nuevo, porque es contraintuitivo. El nombre del paradigma dice «objeto» y el nombre te miente. Lo importante no son las cosas, es lo que pasa **entre** las cosas.

Y no hace falta que me creas a mí ni a los foros: lo dijo Kay con todas las letras en la lista de correo de Squeak, en octubre de 1998. «Lamento haber acuñado hace mucho el término *objetos* para este tema, porque hace que mucha gente se concentre en la idea menor. La idea grande es la *mensajería*».[^squeak]

La formulación que se cita una y otra vez es del propio Kay, en un intercambio de correos con Stefan Ram en julio de 2003: «OOP to me means only messaging, local retention and protection and hiding of state-process, and extreme late-binding of all things».[^kay2003] Es decir, tres ingredientes: mensajería, retención y ocultamiento local del estado, y ligadura extremadamente tardía de absolutamente todo.

La analogía biológica también es de él, en ese mismo texto: pensaba los objetos «como células biológicas y/o computadoras individuales en una red, capaces de comunicarse sólo mediante mensajes».[^kay2003] Cada objeto es una célula, y las células no se abren entre sí: se mandan señales y cada una decide qué hacer con la que recibe. La misma imagen, ampliada, es el eje de «The Early History of Smalltalk», donde Kay escribe que la reducción de complejidad exigía abandonar las estructuras de datos y de control en favor de «un esquema más biológico de células universales protegidas que interactúan sólo a través de mensajes».[^earlyhistory]

Fijate lo que **no** está en esa lista de tres: no está la herencia. No están las clases. Y no es un descuido de redacción: en el mismo intercambio con Ram, Kay cuenta que no le gustaba cómo Simula I y Simula 67 resolvían la herencia, y que por eso decidió dejarla afuera como característica incorporada del Smalltalk original.[^kay2003] La herencia no es que esté mal vista en la visión original — es que directamente no estaba invitada.

### El desplazamiento del acento

Vamos al ejemplo, que es donde esto se vuelve concreto.

Cuando escribís esto en un lenguaje de la tríada:

```java
cuenta.depositar(100);
```

lo que estás diciendo, en el fondo, es: *ejecutá el código que está en el método `depositar` de la clase de `cuenta`, con el argumento 100*. El compilador chequea que `cuenta` tenga ese método. Si no lo tiene, no compilás. Quien decide qué código corre es, en buena medida, el **tipo** de `cuenta`, y se decide temprano.

En la visión de mensajes, la misma línea dice otra cosa: *le mando a `cuenta` el mensaje `depositar` con el dato 100, y que ella vea qué hace*. Nadie garantiza de antemano que sepa qué hacer. Puede atenderlo. Puede reenviarlo a otro. Puede contestar que no entiende. Puede decidirlo en tiempo de ejecución, en base al estado en que esté. El emisor no tiene derecho a saber nada de eso: mandó una señal a una caja negra.

Esa es toda la diferencia, y es más grande de lo que parece:

- En la tríada, el que llama sabe qué va a pasar. La estructura del programa está en las **clases**.
- En la visión de mensajes, el que llama sabe qué **pidió**, no qué va a pasar. La estructura del programa está en la **conversación**.

La ligadura tardía es lo que hace posible lo segundo. Si el vínculo entre el mensaje y el código que lo atiende se resuelve lo más tarde posible, entonces podés cambiar el receptor sin tocar al emisor, y podés cambiarlo *mientras el sistema corre*.

### Por qué esto tiene consecuencias

Cuando lo mirás así, te das cuenta de a qué se parece de verdad la visión original: se parece mucho más a **sistemas distribuidos** que a jerarquías de clases. Procesos autónomos que no comparten memoria y se mandan mensajes que pueden o no llegar y pueden o no ser entendidos. Es exactamente el problema de una red.

Se suele señalar que Erlang, que en el papel no es «orientado a objetos», está mucho más cerca de esa idea que la mayoría de los lenguajes que sí llevan la etiqueta. [VERIFICAR: **la fuente encontrada apunta en contra y hay que decidir qué hacer con este párrafo.** Busqué el origen de la comparación con Erlang. La frase «Erlang might be the only object oriented language» se le atribuye a Joe Armstrong vía la entrevista de QCon London 2010 en InfoQ (`infoq.com/interviews/johnson-armstrong-oop/`): abrí la página, confirma título, fecha (2010-07-08), entrevistados (Armstrong y Ralph Johnson) y entrevistador (Werner Schuster), pero **no expone transcripción**, así que la frase quedó sin verificar. En cambio sí verifiqué el ensayo propio de Armstrong «Why OO Sucks», donde dice lo contrario con todas las letras: que la respuesta verdadera a «¿Erlang es OO?» era «No of course not — but we didn't care to say this out loud».[^whyoosucks] Opciones: (a) sacar el párrafo; (b) conservarlo pero atribuyéndolo al folclore de foro y no a Armstrong; (c) contar la contradicción, que es más interesante que la afirmación — Armstrong dijo las dos cosas con diez años de diferencia. Antes de elegir, conseguir la transcripción o el video de QCon 2010 y ver qué dijo exactamente.]

También se cita mucho la aclaración de Kay de que él no tenía a C++ en mente cuando inventó el término. La frase existe, es textual, y es de su keynote en OOPSLA 1997, «The Computer Revolution Hasn't Happened Yet»: «en realidad yo inventé el término *orientado a objetos*, y les puedo decir que no tenía a C++ en la cabeza».[^oopsla97]

Pero acá está lo bueno, y es la parte que nunca se cita. Kay no se detiene ahí: sigue, en la misma respiración, con «tengo muchos de los mismos sentimientos respecto de Smalltalk». No estaba defendiendo su lenguaje contra el ajeno. Estaba diciendo que ni siquiera *su propio lenguaje* era el punto — que lo importante de Smalltalk «no tiene casi nada que ver ni con la sintaxis ni con la biblioteca de superclases acumulada».[^oopsla97] La frase que circula como chicana de tribuna es, en el original, exactamente lo contrario: una advertencia de que ningún lenguaje, ni el suyo, es dueño de la idea.

Y está el detalle histórico de que el lenguaje donde esto se encarnó primero fue Smalltalk, en Xerox PARC, a lo largo de los años setenta.[^earlyhistory] [VERIFICAR: la fuente primaria ya está en la bibliografía —«The Early History of Smalltalk», Kay, HOPL-II 1993— y el DOI está confirmado vía Crossref, pero **todavía no verifiqué textualmente los detalles finos**: versiones (Smalltalk-71 / -72 / -76 / -80), años, y quién hizo qué (Ingalls, Goldberg, Kaehler, Thacker, Lampson). El fetch del mirror de worrydream devolvió un resumen, no el texto literal. Si el post va a afirmar cualquier versión, año o autoría concreta, leer el paper y citar página; si no, dejarlo en la generalidad de «Xerox PARC, años setenta», que es lo que está escrito ahora y sí está respaldado.]

> 🕳️ **HUECO — necesita a César:** ¿Cuál fue tu primer contacto con la tríada de manual (clases/herencia/encapsulamiento)? ¿Fue en un libro, en una cátedra, en el laburo? Nombre del lenguaje y contexto alcanza.

> 🕳️ **HUECO — necesita a César:** ¿Te acordás del momento en que te enteraste de que la visión original de Kay era otra? ¿Qué te lo mostró — un texto, una charla, un lenguaje que te obligó a pensar en mensajes?

> 🕳️ **HUECO — necesita a César:** ¿Escribiste alguna vez código en un lenguaje de mensajes de verdad (Smalltalk, Pharo, Objective-C, Erlang)? Si sí: ¿qué te resultó incómodo al principio?

> 🕳️ **HUECO — necesita a César:** ¿Tenés una opinión propia sobre si la distinción sirve para algo en el trabajo diario, o si es una discusión de sobremesa? El post necesita tu veredicto, no el mío.

### Qué hacer con esto si recién empezás

Nada dramático. En serio.

No estamos ante una corrección moral. La tríada de manual y la visión de mensajes son dos mapas del mismo territorio, dibujados con criterios distintos, y ninguno de los dos te habilita a despreciar el otro. El código que escribís mañana en el laburo va a seguir siendo de la tríada, porque los lenguajes que te pagan por usar son de la tríada.

Lo que ganás con la segunda definición es un lugar desde dónde mirar. Cuando entendés que el acento podría haber estado en el mensaje y no en la clase, empezás a ver decisiones donde antes veías naturaleza. La herencia deja de ser «así son las cosas» y pasa a ser «alguien eligió esto». Y una vez que ves una decisión, podés discutirla.

Ese es todo el valor del asunto, y es bastante. Lo que no tiene ningún valor es usarlo para hacer callar a alguien en un thread.

> 🕳️ **HUECO — necesita a César:** ¿Querés cerrar con algún caso propio donde pensar «en mensajes» te haya cambiado un diseño (por ejemplo, algo de la época de Ministerio de Cultura de Santa Fe)? Si no hay nada, se cierra sin anécdota y listo — no inventemos una.

Hay una parte más grande de esta historia, que es qué más había en la visión de Kay además de los mensajes, y por qué casi nada de eso llegó a los lenguajes que usamos todos los días. Eso lo cuento en [[A1-01]].

[^reddit]: [A simple explanation of what Alan Kay meant when he coined the term «object oriented»](https://www.reddit.com/r/programming/comments/bqu8td/a_simple_explanation_of_what_alan_kay_meant_when/) — thread de `/r/programming`. [VERIFICAR: sigue sin confirmar el título real del thread; el de acá está reconstruido desde el slug de la URL. Intenté `reddit.com` y `old.reddit.com` (fetch bloqueado en ambos), la API de disponibilidad de Wayback (`archive.org/wayback/available`) devuelve `archived_snapshots` vacío, y la búsqueda por el ID `bqu8td` no devuelve resultados. Hace falta abrirlo a mano en un navegador y copiar el título tal cual, o pedir un snapshot a Wayback.]

[^se]: [So what did Alan Kay really mean by the term «object-oriented»?](https://softwareengineering.stackexchange.com/questions/46592/so-what-did-alan-kay-really-mean-by-the-term-object-oriented) — Software Engineering Stack Exchange. [VERIFICAR: tampoco pude abrirlo — `softwareengineering.stackexchange.com` y `api.stackexchange.com` están bloqueados para fetch y no hay snapshot en Wayback. El título de acá viene del slug de la URL. Confirmar a mano antes de publicar.]

[^squeak]: [prototypes vs classes was: Re: Sun's HotSpot](http://lists.squeakfoundation.org/pipermail/squeak-dev/1998-October/017019.html) — Alan Kay, lista de correo squeak-dev, 10 de octubre de 1998. Original: «I'm sorry that I long ago coined the term "objects" for this topic because it gets many people to focus on the lesser idea. The big idea is "messaging"».

[^kay2003]: [Dr. Alan Kay on the Meaning of «Object-Oriented Programming»](https://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en) — correos de Alan Kay a Stefan Ram, 23 y 26 de julio de 2003. Original de la definición: «OOP to me means only messaging, local retention and protection and hiding of state-process, and extreme late-binding of all things»; de la analogía: «I thought of objects being like biological cells and/or individual computers on a network, only able to communicate with messages»; de la herencia: «I didn't like the way Simula I or Simula 67 did inheritance… So I decided to leave out inheritance as a built-in feature».

[^earlyhistory]: Alan C. Kay, «The Early History of Smalltalk», en *The Second ACM SIGPLAN Conference on History of Programming Languages* (HOPL-II), ACM, 1993, pp. 69-95. DOI: [10.1145/154766.155364](https://doi.org/10.1145/154766.155364). Texto libre en HTML: [worrydream.com/EarlyHistoryOfSmalltalk](https://worrydream.com/EarlyHistoryOfSmalltalk/).

[^oopsla97]: [Alan Kay en OOPSLA 1997: «The Computer Revolution Hasn't Happened Yet»](https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet) — transcripción completa de la keynote, alojada en el archivo del Viewpoints Research Institute, el instituto del propio Kay. El pasaje completo: «…and actually, I made up the term object-oriented, and I can tell you I did not have C++ in mind. [Laughter and applause] An important thing here is — I have many of the same feelings about Smalltalk — … but it has almost nothing to do with either the syntax or the accumulated superclass library».

[^whyoosucks]: [Why OO Sucks](https://www.cs.otago.ac.nz/staffpriv/ok/Joe-Hates-OO.htm) — Joe Armstrong (sección fechada en 2000), copia alojada en la cátedra de Otago. Original: «"Is Erlang OO" — well, of course the true answer was "No of course not" — but we didn't care to say this out loud».
