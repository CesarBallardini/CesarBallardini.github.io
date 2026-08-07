### A1-12 — El documento de Alan Kay sobre qué es realmente OOP (alojado en FU Berlin)

- **Archivo seed:** _draft-rest.md bucket 1 (cosechado 2026-04-09)_
- **Slug propuesto:** `kay-oop-doc-fu-berlin`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-kay-oop-doc-fu-berlin/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-01]] (Kay general), [[C-05]] (filosofía), [[tr-22]] (consolidado)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1600-1900 palabras (lectura de documento primario + contraste; elegido 2026-07-15)

**Concepto:** En `userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en` hay un documento de Alan Kay donde aclara con extensión qué entiende él por OOP — más largo que el famoso quote de "messaging + state hiding + late binding". El post lee el documento, lo contrasta con la lectura mainstream y explica qué se perdió en la traducción a Java/C++.

**Hook:** todos citan el famoso quote de Kay sobre OOP. Casi nadie lee el documento largo donde lo explica con detalle. Está alojado en una URL frágil de FU Berlin. El post lo recupera y lo explica.

**Outline:**

1. **El quote que todos citamos** — la frase de Kay sobre messaging + state hiding + late binding circula sin contexto. Hook: casi nadie leyó de dónde sale.
2. **De dónde sale: dos mails de 2003** — no es un paper ni una charla; son dos respuestas por correo a Stefan Ram, que le preguntó dos cosas concretas (cuándo se usó por primera vez el término, y qué significa para él).
3. **Primer mail (23 de julio de 2003)** — origen del término, la metáfora de las células y la red, la idea de eliminar «data» como concepto, polimorfismo, y por qué Kay rechaza el modelo de herencia de Simula.
4. **Segundo mail (26 de julio de 2003)** — la bifurcación histórica: la rama biológica/de red contra la rama de los tipos abstractos de datos; «dataless programming»; el contraste con RPC.
5. **Qué se perdió en la traducción a Java/C++** — la industria se llevó la rama de los tipos abstractos de datos y le puso el nombre de la otra. Sección que requiere fuentes que hoy el draft no tiene.
6. **El problema de conservación** — la URL de FU Berlin, el PURL canónico, el copyright de Ram, y por qué «recuperar» el documento no puede significar republicarlo.
7. **Cierre** — qué hacer con esto hoy: leer el original antes de citarlo.

**Bibliografía:**

_Fuente primaria (el documento del post):_

- **Kay, Alan / Ram, Stefan — «Dr. Alan Kay on the Meaning of "Object-Oriented Programming"»** (correspondencia por correo, mails del 23 y del 26 de julio de 2003; publicada por Stefan Ram, Berlín; «Copyright 2004 Stefan Ram, Berlin. All rights reserved.»).
  - URL de trabajo: https://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en — **frágil** (userpage universitaria). Fetch verificado 2026-07-15.
  - PURL canónico: https://www.purl.org/stefan_ram/pub/doc_kay_oop_en — **estable**. Cadena de redirección verificada 2026-07-15: `www.purl.org` → `purl.archive.org/stefan_ram/pub/doc_kay_oop_en` (307) → `userpage.fu-berlin.de/~ram/...` (302). Dato relevante para la sección 6: el servicio PURL hoy lo opera Internet Archive, así que el PURL es más estable que la userpage **y** que el propio purl.org original.
  - Backup Wayback: http://web.archive.org/web/20260613163927/http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en — snapshot del 2026-06-13, `status: 200` según la API oficial `http://archive.org/wayback/available` (consultada 2026-07-15). **Ver `[VERIFICAR:]` en la nota al pie `[^wayback]`.**
  - Espejo de cotejo (para verificar transcripción, **no** para citar): gist `eliot-akira/11e071ec47f09631286d89703a5520e5` (raw). Coincide palabra por palabra con el original en el quote famoso, el origen del término, la herencia de Simula y el pasaje de las dos ramas. **Frágil** y sin licencia clara; sirvió como segunda lectura independiente porque `web.archive.org` no es fetcheable desde acá.

_Para la sección 5 (la rama de los tipos abstractos de datos) — sección que antes no tenía ninguna fuente:_

- **Cook, William R. — «On Understanding Data Abstraction, Revisited»**, en _Proceedings of the 24th ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications_ (OOPSLA 2009), Orlando, Florida, 25–29 de octubre de 2009, pp. 557–572. DOI: https://doi.org/10.1145/1640089.1640133 — **estable** (DOI verificado vía `api.crossref.org` el 2026-07-15; ACM DL bloquea el fetch directo).
  - Texto completo libre en la página del propio autor (UT Austin): https://www.cs.utexas.edu/~wcook/Drafts/2009/essay.pdf — **estable** (dominio institucional). PDF descargado y leído el 2026-07-15, no sólo linkeado.
  - Es **la** fuente para la sección 5, y la que obliga a matizarla: ver la nota bajo `**Estado actual:**`.
- **Kay, Alan C. — «The Early History of Smalltalk»**, _ACM SIGPLAN Notices_, vol. 28, nº 3 (marzo de 1993), pp. 69–95. DOI: https://doi.org/10.1145/155360.155364 — **estable** (verificado vía Crossref 2026-07-15). Reimpreso en _History of Programming Languages—II_ (HOPL-II), ACM, 1996, pp. 511–598, DOI: https://doi.org/10.1145/234286.1057828 (también verificado vía Crossref).
  - Espejo HTML libre (versión limpiada por Bret Victor): https://worrydream.com/EarlyHistoryOfSmalltalk/ — **frágil** (sitio personal). Fetch verificado 2026-07-15.
  - **Hallazgo importante**: acá Kay sostiene la tesis de las dos ramas *él mismo y en un paper con revisión*, no sólo en un mail. Textual: «The "official" computer science world started to regard Simula as a possible vehicle for defining abstract data types (even by one of its inventors), and it formed much of the later backbone of ADA.» Y: «To put it mildly, we were quite amazed at this, since to us, what Simula had whispered was something much stronger than simply reimplementing a weak and ad hoc idea.» Citar esto en vez de (o además de) los threads de [[tr-22]].
- **Liskov, Barbara; Zilles, Stephen — «Programming with abstract data types»**, _ACM SIGPLAN Notices_, vol. 9, nº 4 (abril de 1974), pp. 50–59. DOI: https://doi.org/10.1145/942572.807045 — **estable** (verificado vía Crossref 2026-07-15). El documento fundacional de la otra rama; útil para que la sección 5 no la trate como un espantajo.

_Citadas por Kay en el segundo mail (verificadas por si el post las nombra):_

- **Balzer, Robert M. — «Dataless programming»**, en _Proceedings of the AFIPS '67 Fall Joint Computer Conference_ (Anaheim, California, 14–16 de noviembre de 1967), desde p. 535. DOI: https://doi.org/10.1145/1465611.1465683 — **estable** (verificado vía Crossref 2026-07-15). Kay lo fecha «at the end of the 60s (I think)»: es de 1967.
- **Reynolds, John C. — «GEDANKEN—a simple typeless language based on the principle of completeness and the reference concept»**, _Communications of the ACM_, vol. 13, nº 5 (mayo de 1970), pp. 308–319. DOI: https://doi.org/10.1145/362349.362364 — **estable** (verificado vía Crossref 2026-07-15). Kay lo fecha «in 1970 I think»: acertó.

**Imágenes:** _a definir_

**Tags propuestos:** `['Alan Kay','OOP','Smalltalk','historia','documentos primarios']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09; outline y prosa-borrador escritos el 2026-07-15 (Claude, sin revisar por César). **Pasada de fuentes: 2026-07-15** (Claude). El post pasó de tener una (1) URL en la bibliografía a tener siete fuentes verificadas, seis de ellas con DOI confirmado vía Crossref.

⚠️ **PREMISA MATIZADA (no rota):** el Concepto dice que el post «explica qué se perdió en la traducción a Java/C++». La bifurcación en dos ramas está **fuertemente sostenida** —y no sólo por los mails: Kay la cuenta en _The Early History of Smalltalk_, un paper con revisión («The "official" computer science world started to regard Simula as a possible vehicle for defining abstract data types... and it formed much of the later backbone of ADA»)—. Pero la versión fuerte que traía la prosa, «Java y C++ **son** la rama de los tipos abstractos de datos», **no la sostiene la mejor fuente del tema**. William Cook (OOPSLA 2009) dice lo contrario en dos frentes: que los lenguajes modernos soportan *las dos cosas* mezcladas en una sola forma sintáctica, y que en Java *se puede* programar en estilo objetos puro. La prosa de la sección 5 se reescribió alrededor de eso: la tesis ahora es «Java te deja hacer las dos y la cultura eligió una», que es más defendible y —creo— más interesante. El Hook y el Concepto no se tocaron. Si a César la versión matizada le parece más floja que la original, la discusión es suya, pero la versión fuerte no tiene con qué respaldarse.

**Correcciones de hecho encontradas en esta pasada** (todas contra el documento original, cotejadas en dos hosts independientes):

1. **El quote famoso estaba incompleto.** Termina en «...and extreme late-binding **of all things**». El draft (y media internet) lo corta antes. El «of all things» no es decorativo: es donde Kay universaliza el ligado tardío. Corregido en `[^kay_quote]` y en la apertura.
2. **«Dataless programming» no es una expresión de Kay.** Es el título de un paper de **Bob Balzer** que Kay cita en el segundo mail. El paper existe: AFIPS FJCC 1967, DOI verificado. La expresión propia de Kay para su rama es «non-data-procedure route». El draft se lo atribuía a Kay; corregido con nota visible en la prosa.
3. **Kay no «rechazó» la herencia de Simula.** Textual: «I didn't like the way Simula I or Simula 67 did inheritance (though I thought Nygaard and Dahl were just tremendous thinkers and designers)». No le gustaba *cómo* la hacían, y elogia a sus autores en la misma frase. El argumento del post se apoya ahora en una **ausencia** (la herencia no está en la definición de OOP que da Kay), no en un rechazo frontal que no existe.
4. **La fecha de origen son dos fechas, no una.** «At Utah sometime after Nov 66» para la arquitectura; «It was probably in 1967 when someone asked me what I was doing, and I said: "It's object-oriented programming"» para el nombre. La prosa ahora usa la distinción como material.
5. **Kay se despega del término «polymorphism»**: dice que se lo impusieron después («I think by Peter Wegner») y que «it isn't quite valid». Él prefería «genericity». El draft decía sólo que «enmarca el polimorfismo en términos de álgebras» — cierto pero flojo; ahora está el pasaje textual.
6. **El PURL resuelve, y resuelve vía Internet Archive**: `www.purl.org` → 307 → `purl.archive.org` → 302 → FU Berlin. Ese detalle es material nuevo para la sección 6: la permanencia del documento no la garantiza ni la universidad ni el autor, sino un archivo.

Lo que quedó como hueco o pendiente:

- **Dos `[VERIFICAR:]` abiertos, ninguno de hechos:**
  1. En `[^wayback]`: el snapshot del 2026-06-13 existe y da `status: 200` según la API oficial de Wayback, pero **no pude abrirlo** (`web.archive.org` no es fetcheable desde la herramienta). Hay que hacerle un clic antes de publicar. La transcripción del documento **sí** está corroborada, contra un espejo independiente.
  2. En la sección 5: decisión editorial sobre si cosechar [[tr-22]] (threads de Reddit/SE.SE) o quedarse con las primarias. Sugerencia anotada: alcanza con las primarias.
- **Seis huecos de experiencia vivida de César** — sin tocar, como corresponde. Ninguna búsqueda web los responde: cómo llegó al documento, qué OOP le enseñaron, si tocó Smalltalk, si le tocó un sistema de mensajes de verdad, su postura sobre la tesis, y su experiencia con links caídos. Sin eso el post es una glosa impersonal de un documento ajeno, que es exactamente lo que el blog no hace.
- **El hook sigue necesitando ajuste** (nota de la pasada anterior, todavía vigente): dice que el post «recupera» el documento, pero el documento tiene PURL propio, backup en Wayback y copyright con todos los derechos reservados. El ángulo real es *leerlo y explicarlo*, no rescatarlo. Sin tocar, es de César.
- **Longitud:** la sección 5 creció bastante con el matiz de Cook. Con las correcciones, el borrador probablemente pasa el target de 1600-1900 palabras. Hay que podar en la pasada de edición — candidato obvio: la nota de corrección sobre «dataless programming» puede quedar como footnote en vez de bloque.
- **Imágenes:** sigue `_a definir_`. No se buscó en esta pasada (era de fuentes). Opciones: retrato de Kay o screenshot de Smalltalk en Wikimedia Commons. Nada de screenshot de la página de Ram (copyright).

Lo que quedó escrito en la pasada de prosa (2026-07-15, previa a la de fuentes): el encuadre completo del documento (qué es, quién lo hospeda, por qué existe), el recorrido por los dos mails siguiendo la secuencia de temas que efectivamente está en la página, la sección de conservación (URL frágil vs. PURL canónico vs. copyright), y las transiciones.

_(La lista de pendientes que estaba acá quedó saldada o reemplazada por la pasada de fuentes del 2026-07-15; el detalle actualizado está más arriba. Se resolvieron: el PURL y el copyright ya están en la bibliografía, las citas de Kay están verificadas palabra por palabra contra dos hosts independientes, y la sección 5 ya tiene fuentes primarias. Siguen vigentes y se movieron arriba: el ajuste del hook, los seis huecos de César y las imágenes.)_

---

## Borrador de prosa

Hay una frase de Alan Kay que aparece, tarde o temprano, en toda discusión sobre programación orientada a objetos. Alguien dice que Java no es realmente OOP, alguien contesta que Kay dijo tal cosa, y se pega el quote: OOP significa solamente mensajería, retención y protección y ocultamiento local del estado-proceso, y ligado extremadamente tardío **de todas las cosas**[^kay_quote]. Fin de la discusión, o principio de una peor. La frase circula como una moneda gastada: la pasamos de mano en mano sin mirarla.

Lo que casi nadie hace —yo tampoco lo había hecho hasta hace poco— es ir a ver de dónde sale. Y de dónde sale es un lugar bastante menos solemne de lo que el uso del quote sugiere: no es un paper, no es una charla de OOPSLA, no es un capítulo de libro. Son dos mails. Dos respuestas de correo electrónico que Kay le escribió a una persona que le preguntó, en julio de 2003, dos cosas concretas.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste vos a este documento? ¿Buscando el origen del quote, o te lo pasó alguien? Una o dos frases alcanzan para abrir el post con algo tuyo.

### El documento y su hospedador

El documento vive en una userpage de la Freie Universität Berlin, bajo el título «Dr. Alan Kay on the Meaning of "Object-Oriented Programming"»[^doc]. Lo hospeda Stefan Ram, que no es un intermediario accidental: es él quien le escribió a Kay. Le preguntó dos cosas —cuándo se usó por primera vez el término «object-oriented», y qué significa OOP para él— y publicó las respuestas con atribución a ambas partes.

Eso explica el tono del texto, que es la primera cosa que sorprende al leerlo. No está escrito para la posteridad. Está escrito por alguien contestando un mail, con la soltura y las digresiones de quien contesta un mail. Y sin embargo es, hasta donde sé, la explicación más extensa que Kay dejó por escrito de qué entendía él por la cosa que él mismo bautizó.

Hay una ironía ahí que vale la pena registrar. La definición canónica de OOP —la que se cita como si fuera una constitución— es un mail de 2003 sobre algo que pasó en los sesenta, hospedado en la página personal de un tercero. No hay documento fundacional. Hay un recuerdo, contestado por correo, treinta y pico de años después.

### El primer mail

El primer mail es del 23 de julio de 2003[^doc]. Kay arranca por donde le preguntaron: el origen del término. Y lo que da no es una fecha, son dos. Por un lado, el momento en que se le ocurrió la arquitectura: «At Utah sometime after Nov 66», influido —dice— por Sketchpad, Simula, el diseño de ARPAnet, la Burroughs B5000 y su formación en biología y matemática. Por otro, el momento en que la cosa recibió el nombre, que es posterior y bastante más casual: «It was probably in 1967 when someone asked me what I was doing, and I said: "It's object-oriented programming"»[^doc].

Vale la pena no aplanar esa distinción, porque es un dato sobre cómo se hace la historia: primero existió la idea, después alguien preguntó de pasada y salió la etiqueta. El nombre más pesado de la disciplina se dijo por primera vez contestando un «¿en qué andás?».

Pero lo interesante no es la fecha. Es que Kay no explica OOP con vocabulario de programación. Lo explica con una metáfora biológica: células. Organismos que no se abren unos a otros, que no se leen el interior, que sólo se mandan señales. Y con una metáfora de red: computadoras que se comunican por mensajes y nada más. La unidad no es el objeto; es el mensaje que va entre dos objetos. El objeto es apenas lo que queda entre mensaje y mensaje.

De ahí se sigue una idea que es, honestamente, más radical que todo lo que la industria hizo después con la palabra. Kay lo dice en cuatro palabras: «I wanted to get rid of data»[^doc]. Quería **eliminar «data» como concepto**. No «encapsular» los datos. No ponerles getters. Eliminarlos como categoría. Si todo lo que existe es un objeto al que le mandás un mensaje, entonces no hay «un dato» en ningún lado: hay alguien a quien preguntarle algo. Y no era un deseo abstracto: enseguida aclara que la metáfora de la célula y de la computadora entera es justamente lo que se lleva puesto al dato, y que hasta la asignación —el `<-`— pasaría a ser «just another message token»[^doc].

Después pasa por polimorfismo, y acá conviene ir con cuidado, porque el documento dice algo más filoso que «Kay habla de polimorfismo». Kay se despega del término: «The term "polymorphism" was imposed much later (I think by Peter Wegner) and it isn't quite valid, since it really comes from the nomenclature of functions, and I wanted quite a bit more than functions»[^doc]. Él había inventado otra palabra, «genericity», para tratar comportamientos genéricos «in a quasi-algebraic form», y explica por qué: «My math background made me realize that each object could have several algebras associated with it, and there could be families of these»[^doc]. Álgebras, no jerarquías.

Y llega a algo que a mí me parece el momento más subestimado del documento. Kay no dice «rechacé la herencia» —conviene no ponerle en la boca una palabra más dura que la suya—; dice, con una cortesía que hace el golpe más raro: «I didn't like the way Simula I or Simula 67 did inheritance (though I thought Nygaard and Dahl were just tremendous thinkers and designers)»[^doc]. No le gustaba *cómo* la hacían, y lo dice de las dos versiones de Simula, en la misma frase en que elogia sin reservas a sus autores.

Leelo de nuevo. El tipo que inventó el término «orientado a objetos» arranca su definición de OOP sin la herencia, y cuando la nombra es para decir que la implementación que todos heredamos no le gustaba. La herencia —la cosa que durante veinte años fue la primera clase de cualquier curso de OOP, el diagrama de flechitas que dibujábamos en el pizarrón— no aparece en su lista de lo que OOP significa. El quote famoso enumera tres cosas: mensajería, ocultamiento del estado, ligado tardío. La herencia no está.

(Precisión que me importa, porque es fácil sobreactuar acá: Kay no dice que la herencia sea mala ni que «nunca fue el punto». Dice que no le gustaba cómo la hacía Simula. Lo que sostiene el argumento no es un rechazo frontal, es una ausencia: cuando le piden que defina OOP, la herencia no entra en la definición.)

> 🕳️ **HUECO — necesita a César:** cuando aprendiste OOP, ¿por dónde te la enseñaron: herencia primero, o mensajes primero? ¿Y en qué lenguaje?

> 🕳️ **HUECO — necesita a César:** ¿llegaste a tocar Smalltalk alguna vez, aunque sea de curioso? Si sí, ¿cuándo y con qué impresión? Si no, decilo también — es igual de honesto y sirve para el post.

### El segundo mail: la bifurcación

Tres días después, el 26 de julio, Kay manda un segundo mail[^doc]. Y este es el que, para mí, justifica el post entero.

Ahí Kay plantea que después de Simula la cosa se abrió en **dos caminos históricos**, y les pone nombre él mismo: «The early one (just by accident) was the bio/net non-data-procedure route that I took. The other one, which came a little later as an object of study was abstract data types, and this got much more play»[^doc].

Hay que leer despacio esas dos frases, porque dicen más de lo que parecen. Primero, Kay llama a su propia rama «the bio/net non-data-procedure route» —biológica, de red, y definida por lo que *no* es: no procedimientos sobre datos—. Segundo, la otra rama tiene nombre técnico y establecido: **abstract data types**. Y tercero, la frase que a mí me parece la más honesta del documento entero: «this got much more play». No dice que la otra rama sea un error. Dice que ganó. El que acuñó el término reconoce, sin dramatismo, que la rama que se llevó el mundo no fue la suya.

Menciona además influencias concretas —Sketchpad, la B5000, Doug Ross[^doc]— y cita dos papers ajenos que conviene no confundir con vocabulario propio: el de Bob Balzer, «Dataless Programming»[^balzer], y el «Gedanken» de John Reynolds[^gedanken]. Y cierra contrastando su modelo con el enfoque de Remote Procedure Call: «all through the seventies and eighties, there were many people who tried to get by with "Remote Procedure Call" instead of thinking about objects and messages»[^doc].

> **Corrección respecto del draft anterior:** el draft decía que Kay «usa la expresión "dataless programming"». No es una expresión suya: es el **título de un paper de Bob Balzer** que Kay cita («At the end of the 60s (I think) Bob Balzer wrote a pretty nifty paper called "Dataless Programming"»). El paper existe y es de 1967, no de fin de la década[^balzer]. La expresión propia de Kay para su rama es otra: «non-data-procedure route». Vale la pena no atribuirle a Kay una etiqueta que él estaba citando de otro.

Ese contraste con RPC es la llave de todo. Un mensaje, en el sentido de Kay, no es una llamada a procedimiento remoto con otro nombre. En RPC yo sé qué función estoy llamando y qué me va a devolver; el mensaje es apenas un sobre para transportar una invocación que ya tengo decidida. En el modelo de Kay, el emisor manda un mensaje y **no sabe qué va a pasar**. El receptor decide. Eso es el ligado tardío del quote famoso: no un detalle de implementación del despacho de métodos, sino la afirmación de que el que manda el mensaje no tiene autoridad sobre el que lo recibe.

Y acá está lo que se perdió en la traducción.

### Lo que se llevó la industria

La tesis —y la digo como tesis, no como hecho establecido— es que la industria se llevó **la rama equivocada y le puso el nombre de la otra**. Los tipos abstractos de datos no son un invento anónimo: tienen su documento fundacional, el paper de Barbara Liskov y Stephen Zilles de 1974[^liskov], y son una idea excelente que produjo software que funciona y que nos dio de comer a varias generaciones. El problema no es esa rama. Es el etiquetado.

Y no hace falta que lo diga yo, ni un thread de Reddit. Lo dice Kay, en un paper con revisión, veinte años después de los hechos y diez antes del mail: «The "official" computer science world started to regard Simula as a possible vehicle for defining abstract data types (even by one of its inventors), and it formed much of the later backbone of ADA»[^early]. Y agrega, sobre la reacción de su grupo: «To put it mildly, we were quite amazed at this, since to us, what Simula had whispered was something much stronger than simply reimplementing a weak and ad hoc idea»[^early]. Es la misma bifurcación del segundo mail, contada en _The Early History of Smalltalk_, que es una fuente bastante más citable que dos correos.

Ahora, acá hay que frenar, porque la versión fuerte de la tesis —«Java y C++ **son** la rama de los tipos abstractos de datos»— no la sostiene la mejor fuente que existe sobre el tema. William Cook, en «On Understanding Data Abstraction, Revisited»[^cook], dedica el paper entero a separar objetos de tipos abstractos de datos, y su conclusión es que los libros de texto se equivocan: «Objects and abstract data types are not the same thing, and neither one is a variation of the other. They are fundamentally different and in many ways complementary, in that the strengths of one are the weaknesses of the other»[^cook]. Eso respalda la mitad de la tesis: la confusión existe, está en los textbooks, y es un error real.

Pero Cook desarma la otra mitad. No dice que Java sea un tipo abstracto de datos disfrazado; dice que los lenguajes de hoy son **las dos cosas mezcladas**: «most modern programming languages support both objects and abstract data types, often blending them together into one syntactic form. But syntactic blending does not erase fundamental semantic differences»[^cook]. Y llega a mostrar cómo programar en Java en estilo objetos puro, con dos reglas (usar las clases sólo después de `new`, nunca como tipos; no usar `==`): «While Java is not a pure object-oriented language, it is possible to program in a pure object-oriented style»[^cook].

Así que la formulación honesta no es «Java es la otra rama». Es: **Java te deja hacer las dos, y la cultura eligió una**. El lenguaje no te obliga a escribir tipos abstractos de datos con sintaxis de objetos; te lo permite, y nosotros lo hicimos, durante treinta años, mientras usábamos el vocabulario de la rama que no estábamos transitando. Eso es peor que un error de diseño: es un hábito. Y por eso hoy, cuando alguien lee el quote de Kay, lo lee *desde* Java y concluye que Kay está siendo críptico. No está siendo críptico. Está hablando de la otra rama.

[VERIFICAR: decisión editorial, no de fuentes. La sección ya no se apoya en aire — tiene a Cook (OOPSLA 2009), el propio _Early History of Smalltalk_ de Kay y el paper de Liskov-Zilles, todos verificados y en la bibliografía. Lo que queda es decidir si además se cosecha [[tr-22]] (los threads de Reddit y SE.SE consolidados en el plan) como color/recepción, o si con las fuentes primarias alcanza y tr-22 se deja para [[A1-01]]. Mi sugerencia: alcanza con las primarias; tr-22 sólo si querés mostrar la discusión popular como síntoma.]

> 🕳️ **HUECO — necesita a César:** ¿comprás esta tesis, la matizás, o te parece una queja de purista? El post necesita tu postura acá, no la mía. Un párrafo tuyo.

> 🕳️ **HUECO — necesita a César:** ¿te tocó alguna vez trabajar en un sistema donde los objetos sí se hablaban por mensajes de verdad —colas, actores, servicios que no se conocen entre sí— y notaste la diferencia? Si tenés un caso concreto (aunque no puedas nombrar la institución), sirve mucho como aterrizaje.

### El documento es frágil, y no es mío

Queda una cuestión de conservación, que es la que me hizo escribir esto.

La URL de FU Berlin es una userpage: `userpage.fu-berlin.de/~ram/...`. Ese formato —el tilde, el nombre de usuario— es el formato de las cosas que desaparecen. Vive mientras la persona mantenga la cuenta y la universidad mantenga el servicio. Es el documento más citado sobre qué es OOP y cuelga de un hilo administrativo.

Ahora, Ram no es ingenuo: la página declara un PURL canónico propio[^purl], que es exactamente la respuesta correcta al problema. Un PURL es una redirección estable que sobrevive a la mudanza del contenido: la dirección que citás no es la dirección donde el archivo está parado hoy. Si algún día la userpage se cae, el PURL puede apuntar a otro lado y las citas siguen funcionando.

Y hay un detalle lindo que aparece si uno sigue la redirección a mano, que es lo que hice. El PURL que declara la página empieza en `www.purl.org`, pero no termina ahí: rebota a `purl.archive.org` y recién de ahí cae en la userpage de FU Berlin[^purl]. Es decir que el servicio de PURLs hoy lo opera Internet Archive. La infraestructura de permanencia de este documento no es la universidad ni el autor: es un archivo. Que es, si lo pensás, la misma conclusión a la que llega cualquiera que haya intentado citar algo durante veinte años.

Y hay una tercera cosa, que me obliga a bajar el tono épico: la página lleva un aviso de copyright de Stefan Ram, con todos los derechos reservados[^doc]. Así que la idea de «rescatar» el documento republicándolo no va. No es material libre. Lo que puedo hacer es lo que estoy haciendo acá —citarlo corto, linkearlo, explicarlo, mandarte a leerlo— y dejar constancia del backup en la Wayback Machine[^wayback].

> 🕳️ **HUECO — necesita a César:** ¿tenés algún caso propio de un link o un documento técnico que citabas y que se te cayó? Un ejemplo tuyo acá cierra la sección mucho mejor que la teoría sobre PURLs.

### Entonces

Si te llevás una sola cosa: la próxima vez que vayas a pegar el quote de Kay en una discusión, leé antes los dos mails. Son cortos. Están a un clic. Y lo que vas a encontrar no es una definición para ganar discusiones, sino un tipo acordándose por correo de una idea que le parecía obvia y que no prendió: que los objetos no son cosas con datos adentro, sino cosas que se hablan.

El nombre ganó. La idea, no tanto.

[^kay_quote]: La formulación textual, verificada palabra por palabra contra el original el 2026-07-15, es: «OOP to me means only messaging, local retention and protection and hiding of state-process, and extreme late-binding of all things.» Está en el primer mail, el del 23 de julio de 2003. **Ojo con el final**: la versión que circula (y la que traía este draft) corta en «extreme late-binding» y se come el **«of all things»**, que es justamente donde Kay universaliza el criterio — no ligado tardío de los métodos, ligado tardío *de todo*. Ver [^doc].

[^doc]: [Dr. Alan Kay on the Meaning of "Object-Oriented Programming"](https://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en) — Stefan Ram, Berlín. Correspondencia por correo con Alan Kay, mails del 23 y del 26 de julio de 2003. Copyright 2004 Stefan Ram, todos los derechos reservados. URL verificada el 2026-07-15.

[^purl]: PURL canónico que declara la propia página: [purl.org/stefan_ram/pub/doc_kay_oop_en](https://www.purl.org/stefan_ram/pub/doc_kay_oop_en). Resolución verificada paso a paso el 2026-07-15: `www.purl.org/stefan_ram/pub/doc_kay_oop_en` responde 307 hacia `purl.archive.org/stefan_ram/pub/doc_kay_oop_en`, que responde 302 hacia `userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en`. El PURL efectivamente llega al documento, y el servicio lo opera hoy Internet Archive.

[^wayback]: Copia de resguardo en la Wayback Machine: [snapshot del 13 de junio de 2026](http://web.archive.org/web/20260613163927/http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en). [VERIFICAR: abrir este snapshot con el navegador antes de publicar y confirmar que renderiza el documento completo (los dos mails). La existencia y el `status: 200` los confirmé el 2026-07-15 consultando la API oficial `http://archive.org/wayback/available?url=...`, que devolvió exactamente este timestamp — pero **no pude abrir el snapshot yo mismo**, porque `web.archive.org` no es fetcheable desde la herramienta que usé. La transcripción del documento la corroboré contra un espejo independiente (ver Bibliografía), no contra este snapshot.]

[^early]: [Alan C. Kay, «The Early History of Smalltalk»](https://doi.org/10.1145/155360.155364) — _ACM SIGPLAN Notices_, vol. 28, nº 3, marzo de 1993, pp. 69–95. Reimpreso en _History of Programming Languages—II_, ACM, 1996, pp. 511–598 ([DOI](https://doi.org/10.1145/234286.1057828)). Espejo HTML libre: [worrydream.com/EarlyHistoryOfSmalltalk](https://worrydream.com/EarlyHistoryOfSmalltalk/).

[^cook]: [William R. Cook, «On Understanding Data Abstraction, Revisited»](https://doi.org/10.1145/1640089.1640133) — _Proceedings of OOPSLA 2009_, Orlando, Florida, pp. 557–572. Texto completo libre en la página del autor (UT Austin): [essay.pdf](https://www.cs.utexas.edu/~wcook/Drafts/2009/essay.pdf).

[^liskov]: [Barbara Liskov y Stephen Zilles, «Programming with abstract data types»](https://doi.org/10.1145/942572.807045) — _ACM SIGPLAN Notices_, vol. 9, nº 4, abril de 1974, pp. 50–59.

[^balzer]: [R. M. Balzer, «Dataless programming»](https://doi.org/10.1145/1465611.1465683) — _Proceedings of the AFIPS '67 Fall Joint Computer Conference_, Anaheim, California, 14–16 de noviembre de 1967, desde p. 535. Es el paper que Kay cita en el segundo mail, fechándolo «at the end of the 60s (I think)».

[^gedanken]: [John C. Reynolds, «GEDANKEN—a simple typeless language based on the principle of completeness and the reference concept»](https://doi.org/10.1145/362349.362364) — _Communications of the ACM_, vol. 13, nº 5, mayo de 1970, pp. 308–319. El otro paper que Kay cita en el segundo mail.
