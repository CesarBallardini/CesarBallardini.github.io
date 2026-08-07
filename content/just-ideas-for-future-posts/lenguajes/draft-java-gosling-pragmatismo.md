### A1-20 — Java: el pragmatismo de James Gosling

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `java-gosling-pragmatismo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-java-gosling-pragmatismo/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-13]], [[A1-11]] (Pharo), [[E-09]]
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** James Gosling diseñó Java en Sun en los 90 con un objetivo concreto: que un programa escribiera una vez y corriera en cualquier electrodoméstico ("Write Once, Run Anywhere"). En la entrevista en *Masterminds* dice cosas reveladoras: que sacaría las clases si pudiera (prefiere no usar herencia), que lamenta los generics, que la portabilidad fue el motor real. El post discute esas confesiones y por qué Java sobrevivió 30 años a pesar (o gracias) a los compromisos.

**Hook:** James Gosling, el inventor de Java, dijo que si pudiera rediseñarlo dejaría afuera las clases. Y prefiere no usar herencia. Y los generics fueron un error. Estas son las palabras del padre del lenguaje. ¿Y entonces?

**Outline:**

1. **Hook — el padre desautoriza al hijo.** Las tres confesiones puestas sobre la mesa, con la advertencia de que son material a verificar antes de citarlo.
2. **Qué post es este y qué post no es.** La herencia tiene entrada propia ([[C-10]]); acá la pregunta es otra: qué estaba tratando de resolver Gosling, y qué explica que el lenguaje sobreviva a las objeciones de su autor.
3. **El objetivo real no era el lenguaje.** Portabilidad hacia electrodomésticos, no elegancia. «Write Once, Run Anywhere» como enunciado de ingeniería, no como eslogan.
4. **La máquina virtual es la decisión que manda.** Todo lo demás del diseño se acomoda a esa; el lenguaje es el pasajero, no el conductor.
5. **Parecerse a C fue una decisión política.** El pragmatismo como estrategia de adopción: la sintaxis familiar como caballo de Troya.
6. **Releer las confesiones a la luz de la portabilidad.** Si el objetivo era mover programas entre máquinas, las features del paradigma son medios, no fines — y por eso el autor puede desautorizarlas sin que el lenguaje se caiga.
7. **El caso de los generics.** La cronología importa: llegaron después, y su forma la decidió la compatibilidad hacia atrás, no la teoría de tipos.
8. **Por qué sobrevivió treinta años.** La compatibilidad como valor moral del proyecto; el costo acumulado de nunca romper nada.
9. **La ironía del target.** El lenguaje de los electrodomésticos terminó en los servidores. Qué dice eso sobre planificar el destino de una herramienta.
10. **Cierre — el pragmatismo como postura de diseño.** No «Java es bueno» ni «Java es feo»: Java es lo que pasa cuando un objetivo de ingeniería le gana a la estética, y gana durante treinta años.

**Bibliografía:** _(reforzada y verificada por fetch el 2026-07-16)_
- [[tr-23]] — Federico Biancuzzi y Shane Warden (eds.), [*Masterminds of Programming*](https://archive.org/details/MastermindsOfProgramming), O'Reilly Media, 2009 (ISBN 978-0-596-51517-1). **Cap. 12 «Java», pp. 277-296**: entrevista a James Gosling. Única fuente primaria verificada con sus palabras. Estable.
- [The Java Language Environment: A White Paper](https://www.oracle.com/java/technologies/language-environment.html) — James Gosling y Henry McGilton, Sun Microsystems, oct. 1995 (rev. mayo 1996), 85 pp. La fuente canónica del *design rationale* de Java (metas de diseño, «architecture neutral and portable», features quitadas de C/C++). El host de Oracle bloquea agentes automáticos, pero la página es la oficial y existe; respaldo archival: [Computer History Museum, cat. 102751422](https://www.computerhistory.org/collections/catalog/102751422). Estable.
- [*The Java Language Specification*, 1.ª ed.](https://download.oracle.com/otndocs/jcp/jls1-spec/) — James Gosling, **Bill Joy y Guy L. Steele** (tres autores, no sólo Gosling), Addison-Wesley, 1996 (ISBN 0-201-63451-1 / 978-0-201-63451-8; copyright Sun Microsystems). Texto libre: PDF de la 1.ª ed. en Oracle y [prefacio de la 1.ª ed. en HTML](https://docs.oracle.com/javase/specs/jls/se7/html/jls-0-preface1.html); [copia prestable en archive.org](https://archive.org/details/javalanguagespec00gosl). La 1.ª edición **no** incluye generics: el prefacio los menciona sólo como propuestas de investigación en curso. Estable.
- [*Coders at Work*](https://en.wikipedia.org/wiki/Coders_at_Work) — Peter Seibel, Apress, 2009 (ISBN 978-1-4302-1948-4). ⚠️ **NO entrevista a Gosling** (sí a Guy Steele). No sirve como fuente sobre Gosling; se conserva sólo para dejar registrada la corrección. Estable.
- Cronología (Green Project 1991, Oak → Java, lanzamiento 23-05-1995) y eslogan «Write Once, Run Anywhere»: [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language)) y [Write once, run anywhere](https://en.wikipedia.org/wiki/Write_once,_run_anywhere), Wikipedia. Secundarias, estables.

**Imágenes:** _a definir_

**Tags propuestos:** `['Java','Gosling','Sun','OOP','historia']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (10 secciones), se fijó `Length target: medium` y se escribió un borrador de prosa completo (~1830 palabras de prosa efectiva, sin contar marcas de verificación ni huecos) en la sección «Borrador de prosa» al pie.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron **7 de 11** marcadores `[VERIFICAR:]`. Dos hallazgos son estructurales y afectan al Hook: (1) **Gosling no está entre los entrevistados de *Coders at Work***, así que ese libro no puede citarse sobre él; (2) en *Masterminds* (cap. 12, la única fuente primaria verificada) Gosling **no** habla de sacar las clases ni de evitar la herencia, y sobre los generics dice **lo contrario** de lo que afirma el Hook: que fueron «profundamente buenos» — la crítica al *type erasure* es de Anders Hejlsberg, no de él. Las tres «confesiones» del Hook quedan **sin respaldo en las fuentes de este draft**; hay que localizar su fuente literal real o reescribir el arranque (decisión de César: no se tocó el Hook). Quedan sin resolver 4 marcadores: los quotes literales «sacaría las clases»/«no usa herencia» (fuente aún no ubicada), la lectura del parecido con C (interpretación del autor, sin cita), el grado de participación de Gosling en el diseño de 2004, y el matiz sobre el mercado embebido (que además *Masterminds* complica: Gosling menciona las tarjetas de proximidad tipo Oyster como sistema Java).

Lo que quedó **escrito**: el armazón argumental entero, que no depende de las citas — la tesis de que la portabilidad fue el objetivo y todo lo demás fue medio, la máquina virtual como la decisión que ordena el resto del diseño, el parecido con C leído como estrategia de adopción, la relectura de las confesiones a la luz del objetivo, el argumento sobre la compatibilidad hacia atrás como el valor que explica la supervivencia, la ironía del target original, y el cierre sobre el pragmatismo como postura de diseño. Ese esqueleto se sostiene aunque las citas cambien de forma.

**Reparto con [[C-10]]:** la entrada C-10 (`gosling-vs-herencia`) ya toma la declaración sobre la herencia como tema central. Este post **no** repite ese análisis: lo menciona, lo enlaza y pivota a la pregunta de la portabilidad. Si se publican los dos, respetar esa división; si se publica sólo uno, este necesita absorber un par de párrafos de C-10.

Lo que quedó como **hueco**:

- 7 huecos `🕳️` pidiendo a César lo que el post no puede inventar: su primer contacto con Java y en qué contexto, si vio applets funcionando, si Java apareció en su paso por el sector público santafesino (STG / Ministerio de Cultura) y desde qué lugar habla, si le tocó la migración a generics, si leyó la especificación de 1996, qué le pasó al leer la entrevista en *Masterminds*, y el veredicto del cierre. Sin eso el post es un ensayo de historia de lenguajes correcto pero impersonal.
- 11 marcas `[VERIFICAR:]` (8 en el cuerpo, 3 en las footnotes). Las más importantes: **las tres confesiones del Hook y del Concepto** («sacaría las clases», «prefiere no usar herencia», «los generics fueron un error») están escritas de memoria en el seed y **no se pueden publicar sin la fuente exacta y su contexto**. La tercera es la más urgente porque además tiene un problema de cronología: los generics no estuvieron en el diseño original del lenguaje, así que «lamentarlos» significa algo distinto que lamentar una decisión propia — hay que leer qué dice realmente y reformular. También hay que verificar la autoría de la especificación de 1996 (el draft la atribuye sólo a Gosling; casi seguro tiene coautores), la cronología de Sun/Oak/Java, la fecha y el mecanismo de los generics, y si Gosling está efectivamente entre los entrevistados de *Coders at Work*.
- **Conflicto entre el Hook y la regla de no-inventar**: el Hook afirma las tres confesiones como hechos establecidos («Estas son las palabras del padre del lenguaje»). El borrador las trata como material a verificar y lo dice en voz alta en el segundo párrafo. Si al verificar resultan matizadas o no aparecen, **hay que reescribir el Hook**, no la prosa.
- `**Imágenes:**` sigue en `_a definir_`. Candidatos: un retrato de Gosling con licencia clara en Wikimedia Commons, o algún artefacto de la era Sun. Hay que buscar licencia antes de comprometerse.

---

## Borrador de prosa

Hay un género de declaración que me fascina: el creador de algo enorme que, años después, sentado tranquilo en una entrevista, desarma su propia obra pieza por pieza.

James Gosling es el padre de Java. Java es, muy probablemente, el lenguaje que le enseñó orientación a objetos a más gente que ningún otro en la historia. Y en entrevistas Gosling dice tres cosas que, puestas juntas, suenan a demolición: que si pudiera rediseñar el lenguaje dejaría afuera las clases, que él prefiere no usar herencia, y que los generics fueron un error.[VERIFICAR: **las tres declaraciones son el disparador del post y están escritas de memoria en el seed del plan.** VERIFICACIÓN 2026-07-16 (por fetch): (a) *Coders at Work* queda **descartado** como fuente — no entrevista a Gosling (ver [^seibel]); (b) en *Masterminds* [[tr-23]], cap. 12 «Java», Gosling **no** dice que sacaría las clases ni que evita la herencia (no toca esos temas en esa entrevista), y sobre los generics dice **lo contrario**: que agregarlos «ha sido profundamente bueno» (ver la nota de verificación en la sección de generics). O sea que **ninguna de las tres confesiones queda respaldada por las fuentes de este draft**. Hay que ubicar la fuente literal real de «sacaría las clases» y «no usa herencia» — probablemente otra entrevista, aún sin localizar — o reescribir el arranque. No publicar las tres frases como cita hasta transcribirlas verbatim con su contexto.]

Antes de seguir te aviso de qué va esto, porque la reacción obvia es agarrar esas frases y armar un festival de «Java es un desastre y lo dice hasta el que lo hizo». No es ese post. La declaración sobre la herencia, que es la más jugosa, tiene entrada propia y ahí la desarmo en detalle: [[C-10]]. Acá me interesa una pregunta distinta, y creo que más interesante:

**¿Cómo puede ser que el autor pueda desautorizar las features centrales de su lenguaje y el lenguaje siga ahí, treinta años después, corriendo medio mundo?**

Mi respuesta corta es que a Gosling nunca le importó tanto el lenguaje. Le importaba otra cosa.

### El objetivo no era el lenguaje

Java no nació como un proyecto para hacer un lenguaje mejor. Nació de un problema de ingeniería mucho más chato y mucho más concreto: **hacer que un programa corriera en cualquier aparato.**

No en cualquier computadora. En cualquier *aparato*. La idea original apuntaba a electrodomésticos, dispositivos embebidos, cosas con chips distintos y sistemas distintos y ninguna estandarización entre sí. El eslogan que después Sun convirtió en bandera comercial — «Write Once, Run Anywhere» — es, si le sacás el marketing, un enunciado de ingeniería bastante seco: *el binario que compilaste hoy tiene que correr mañana en un procesador que ni conocés.*

El proyecto arrancó en 1991 en Sun como el «Green Project». El lenguaje se llamó primero **Oak** —por un roble frente a la oficina de Gosling— y se rebautizó **Java** cuando una búsqueda de marca reveló que «Oak» ya estaba tomado. El objetivo original eran dispositivos de consumo y set-top boxes de TV interactiva, no computadoras de escritorio; el propio Gosling arranca su entrevista en *Masterminds* diciendo que Java «surgió de un proyecto para correr en dispositivos pequeños» (trad.).[^masterminds] El lanzamiento público fue el **23 de mayo de 1995**.[^historia]

«Write Once, Run Anywhere» fue un **eslogan de marketing acuñado por Sun en 1995**, no una formulación de ingeniería previa; para 2009 ya estaba tan instalado que Gosling lo usa entre comillas, como frase hecha, al abrir su entrevista.[^masterminds] (Las fuentes lo describen como «slogan»; no pude confirmar que Sun lo registrara formalmente como marca.)[^historia]

Fijate lo que ese objetivo implica. Si tu problema es que el programa corra en un chip desconocido, el lenguaje es casi un detalle. El problema real está abajo.

### La decisión que manda es la máquina virtual

Todo Java sale de acá.

Si querés que el mismo programa corra en cualquier lado, tenés dos caminos. Uno es recompilar para cada máquina, que es lo que hacía C, y que en la práctica significa que el programa no es portable: es *reportable*, con suerte, después de pelearte con las diferencias de cada plataforma. El otro camino es no compilar a la máquina real en absoluto. Compilás a una máquina que no existe — una máquina inventada, con un juego de instrucciones que vos definís — y después escribís, para cada máquina real, un programa que finja ser esa máquina inventada.

Eso es la JVM. Y es, en mi lectura, **la única decisión de diseño verdaderamente importante de todo el proyecto.** Todo lo demás viene después y se acomoda a ella.

El recolector de basura no está ahí porque la gestión automática de memoria sea filosóficamente superior: está ahí porque si el programa maneja punteros crudos, el programa sabe cosas sobre la máquina real, y si sabe cosas sobre la máquina real, se acabó la portabilidad. La ausencia de aritmética de punteros, ídem. Los tipos primitivos con tamaño fijo y definido — un `int` es de 32 bits **siempre**, no «lo que la máquina diga», como en C — ídem. La verificación del bytecode al cargar, ídem.

Ninguna de esas es una decisión sobre orientación a objetos. Son todas decisiones sobre portabilidad. El lenguaje, acá, es el pasajero.

> 🕳️ **HUECO — necesita a César:** ¿cuándo te cruzaste con Java por primera vez, y en qué contexto — facultad, trabajo, curiosidad propia? Y sobre todo: ¿te acordás si la promesa de la portabilidad te sonó a novedad real o a chamuyo de vendedor en ese momento? Ese es el ancla del post.

> 🕳️ **HUECO — necesita a César:** ¿llegaste a ver applets de Java funcionando en un navegador en la época? ¿Te acordás de la sensación — de que efectivamente andaba en cualquier lado, o de que era lento y se colgaba?

### Parecerse a C fue una decisión política

Acá está, para mí, la marca registrada del pragmatismo de Gosling, y es la parte del diseño que menos se le reconoce.

Java podría haberse parecido a cualquier cosa. Si el objetivo era la portabilidad y el lenguaje era el pasajero, la sintaxis era una hoja en blanco: se podría haber parecido a Smalltalk, de donde sale buena parte del modelo de objetos, o haber inventado algo nuevo. Y sin embargo Java se parece a C. Las llaves, el punto y coma, el `for`, la declaración de tipos adelante, `main`. Un programador de C de 1995 abría un archivo `.java` y entendía la mitad sin que nadie le explicara nada.

Eso no es casualidad ni falta de imaginación. Es estrategia de adopción. Gosling necesitaba que los programadores de C y C++ — o sea, en 1995, *los programadores* — pudieran entrar sin sentir que estaban aprendiendo de cero. La sintaxis familiar fue el caballo de Troya que metió adentro las ideas raras: la máquina virtual, el recolector de basura, la ausencia de punteros.

Es exactamente la jugada opuesta a la de Smalltalk, que te pide que cambies de cabeza, de sintaxis y de entorno todo junto, el primer día, antes de dejarte hacer nada — de eso hablo en [[A1-11]]. Smalltalk tenía razón en casi todo y perdió. Java tenía razón en menos cosas y ganó. La diferencia no es técnica, es de estrategia de entrada.

[VERIFICAR: si Gosling explica en alguna de las fuentes ([[tr-23]], *Coders at Work*) el motivo del parecido sintáctico con C — si lo formula como decisión de adopción o de otra manera. Este párrafo es **una lectura mía** de las decisiones del lenguaje, no una afirmación sobre sus intenciones. Si no hay cita, dejarlo marcado como interpretación en el texto publicado.]

### Ahora sí: releé las confesiones

Con eso puesto, volvamos a las tres frases del principio.

Si el objetivo del proyecto era mover programas entre máquinas, entonces las clases, la herencia y el resto del aparato de orientación a objetos **nunca fueron el punto**. Fueron el vehículo disponible en 1995 para organizar código de una manera que la gente entendiera y que la industria aceptara. Eran medios. Y con los medios uno no se casa.

Por eso Gosling puede decir que sacaría las clases sin que se le caiga el proyecto encima. No está renegando de su tesis: está diciendo que ese pedazo no era la tesis. La tesis era la JVM, la tesis era que el programa corra en cualquier lado, y esa tesis **la ganó de manera aplastante**. Un `.jar` compilado hace veinte años corre hoy. Eso funcionó.

Un diseñador de lenguajes enamorado de su paradigma no habla así. Un ingeniero que resolvió el problema que se propuso resolver, sí.

> 🕳️ **HUECO — necesita a César:** ¿qué te pasó cuando leíste la entrevista a Gosling en *Masterminds*? ¿Hubo una respuesta puntual que te haya hecho parar y releer? Una o dos frases alcanzan.

### El caso de los generics merece un párrafo aparte

Con los generics hay un problema de cronología que cambia el sentido de la frase, y no lo puedo pasar por alto.

Los generics **no estaban en el Java original**. Llegaron años después, sobre un lenguaje que ya tenía una base instalada gigantesca y una promesa explícita de no romper el código existente. O sea que «Gosling lamenta los generics» no puede significar lo mismo que «Gosling lamenta las clases»: lo segundo es arrepentirse de una decisión propia, lo primero es opinar sobre un agregado posterior a un lenguaje que ya no estaba del todo en sus manos.

**Nota de verificación (2026-07-16, CONTRADICE AL HOOK):** en *Masterminds* [[tr-23]] Gosling **no lamenta** los generics. Dice literalmente que «hace unos años hicimos todo el ejercicio de agregar generics a Java, y eso ha sido profundamente bueno» (trad.).[^masterminds] La crítica al *type erasure* que suele asociarse a esta idea es de **Anders Hejlsberg** (creador de C#), en el capítulo 13 del mismo libro, no de Gosling. La tercera «confesión» del Hook, por lo tanto, **no se sostiene** en las fuentes verificadas: hay que reescribir el arranque o localizar la fuente real de esa frase antes de publicar. (*Coders at Work* no sirve: no entrevista a Gosling — [^seibel].)

Los generics se agregaron en **Java SE 5.0**, lanzado el 30 de septiembre de 2004 (proceso JSR 14). El mecanismo fue el **borrado de tipos** (*type erasure*): el compilador verifica los tipos y después los borra, de modo que el bytecode resultante sigue siendo compatible con las JVM anteriores. Se eligió *erasure* en lugar de generics reificados justamente para no tocar la máquina virtual ni romper el bytecode existente.[^historia]

[VERIFICAR: qué grado de participación tuvo Gosling en el diseño de Java para la época en que se agregaron los generics. Si ya no estaba a cargo, la frase del hook cambia de peso.]

Y si la queja es sobre la implementación y no sobre la idea, entonces es **el mejor ejemplo de todo el post**: los generics de Java tienen la forma que tienen porque no se podía romper lo viejo. La compatibilidad le ganó a la elegancia. Otra vez.

### Por qué sobrevivió treinta años

Acá está la respuesta a la pregunta del título, y es incómoda para el gusto de cualquiera que ame los lenguajes bonitos.

Java sobrevivió **porque nunca rompió nada.**

Ese es todo el secreto. No es la sintaxis, no es el modelo de objetos, no es la biblioteca estándar. Es que durante treinta años el proyecto trató la compatibilidad hacia atrás como un valor casi moral, y las organizaciones que compran software para veinte años entendieron el mensaje perfectamente. Cuando tenés cuatro millones de líneas corriendo en producción, «el lenguaje es feo» te importa mucho menos que «el lenguaje no me va a romper el lunes».

Y esa decisión tiene una factura, que es todo lo que uno critica de Java. Los generics con borrado de tipos son la factura. La verbosidad acumulada es la factura. Cada rincón raro del lenguaje es un lugar donde alguien decidió no romper lo que ya andaba.

Entonces la pregunta del post — ¿sobrevivió *a pesar* de los compromisos o *gracias* a ellos? — tiene una respuesta que a mí me parece bastante clara: **gracias**. Los compromisos no fueron el precio de la supervivencia. Fueron el mecanismo.

> 🕳️ **HUECO — necesita a César:** ¿te tocó alguna vez la migración de una base de código Java a generics, o convivir con código anterior a ellos? ¿Cómo se sintió esa promesa de compatibilidad desde adentro — como red de seguridad o como cadena?

> 🕳️ **HUECO — necesita a César:** ¿Java apareció en tu paso por el sector público santafesino (STG, Ministerio de Cultura), aunque sea de rebote — algún sistema comprado, algún proveedor que lo trajo, alguna decisión de plataforma? No hace falta detalle: con si estuvo o no estuvo alcanza. Necesito saber desde dónde estás hablando en este post.

### La ironía

Cierro con el detalle que más me gusta de toda la historia.

El lenguaje fue diseñado para electrodomésticos. Para tostadoras, para decodificadores de cable, para aparatitos con poca memoria y procesadores raros.

Los electrodomésticos, en ese sentido, no llegaron nunca. Java terminó en el lugar más lejano imaginable de una tostadora: **el servidor corporativo.** Máquinas grandes, memoria abundante, procesadores estandarizados. Justo el escenario donde el problema que Java venía a resolver casi no existía.

[VERIFICAR: la afirmación de que el mercado embebido original «no llegó» es una simplificación grande — hay que contrastarla contra la historia real de Java en tarjetas SIM, Blu-ray, dispositivos embebidos y, sobre todo, Android. Reformular con precisión o bajarla a una observación acotada al target original. No publicar así.]

Pero fijate que la portabilidad, aun sin electrodomésticos, siguió valiendo — sólo que por otro motivo. En el servidor no te salva de la heterogeneidad de chips: te salva de la heterogeneidad de *proveedores*. Desarrollás en tu máquina y desplegás en el fierro que le tocó comprar a la organización. Es el mismo problema con otro disfraz, y la solución que se diseñó para la tostadora funcionó igual.

Hay algo lindo ahí sobre las herramientas: se las diseña para un destino, y después el mundo las usa para otro, y sobreviven si lo que resolvieron era más general de lo que su autor creía.

### Entonces

Lo que me llevo de Gosling no es una opinión sobre Java. Es una postura de diseño.

Gosling no parece haber querido hacer un lenguaje hermoso. Quiso resolver un problema, eligió las herramientas que había en la góndola en 1995, se las puso encima sin enamorarse de ninguna, y treinta años después puede desarmarlas en público sin que le tiemble la voz — porque nunca fueron el punto. El punto era que el programa corriera en cualquier lado. Y corre.

Es una manera de trabajar que la cultura de los lenguajes de programación no premia mucho. Premiamos la elegancia, la coherencia, la idea que se sostiene sola. Java no tiene casi nada de eso. Tiene otra cosa: **funcionó, y siguió funcionando, y nunca dejó a nadie a pie.** Es poco romántico y es muchísimo.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto, no el mío. ¿Java te parece un buen diseño mal apreciado, un mal diseño que ganó por otras razones, o algo que ni entra en esa dicotomía? Y la de fondo: ¿te parece que el pragmatismo de Gosling es admirable o es la razón por la que programamos peor de lo que podríamos? Una o dos frases tuyas y cierra.

> 🕳️ **HUECO — necesita a César:** ¿leíste alguna vez la especificación del lenguaje de 1996 en serio, o es una fuente que estás citando de referencia? Cambia cómo se puede escribir el párrafo sobre ella.

---

[^masterminds]: Federico Biancuzzi y Shane Warden (eds.), [*Masterminds of Programming*](https://archive.org/details/MastermindsOfProgramming), O'Reilly Media, 2009 (ISBN 978-0-596-51517-1) — ver [[tr-23]]. La entrevista a James Gosling es el **capítulo 12, «Java», pp. 277-296**. Allí Gosling dice que Java «surgió de un proyecto para correr en dispositivos pequeños» y que agregar generics «ha sido profundamente bueno» (ambas trad. mías). Copia en archive.org. Estable.
[^jls]: James Gosling, **Bill Joy y Guy L. Steele**, *The Java Language Specification* (1.ª ed.), Addison-Wesley, 1996 (ISBN 0-201-63451-1 / 978-0-201-63451-8; copyright Sun Microsystems). Verificado 2026-07-16: **son tres autores**, no sólo Gosling (con contribuciones de Richard Tuck, Frank Yellin y Arthur van Hoff, según el prefacio de la 1.ª edición). Texto completo libre: [PDF de la 1.ª ed. en Oracle](https://download.oracle.com/otndocs/jcp/jls1-spec/) y [prefacio de la 1.ª ed. en HTML](https://docs.oracle.com/javase/specs/jls/se7/html/jls-0-preface1.html); [copia prestable en archive.org](https://archive.org/details/javalanguagespec00gosl). Estable (Oracle).
[^seibel]: Peter Seibel, [*Coders at Work: Reflections on the Craft of Programming*](https://en.wikipedia.org/wiki/Coders_at_Work), Apress, 2009 (ISBN 978-1-4302-1948-4). Verificado 2026-07-16: **Gosling NO figura entre los 15 entrevistados** (sí está Guy Steele, coautor de la JLS; los demás son Zawinski, Fitzpatrick, Crockford, Eich, Bloch, Armstrong, Peyton Jones, Norvig, Ingalls, Deutsch, Thompson, Allen, Cosell y Knuth). Por lo tanto **este libro no puede citarse como fuente sobre Gosling**. Estable.
[^historia]: Cronología de Java (Green Project 1991, Oak → Java, lanzamiento del 23 de mayo de 1995) y del eslogan «Write Once, Run Anywhere»: [Java (programming language) — Wikipedia](https://en.wikipedia.org/wiki/Java_(programming_language)) y [Write once, run anywhere — Wikipedia](https://en.wikipedia.org/wiki/Write_once,_run_anywhere). Fuente canónica de diseño: [The Java Language Environment (white paper), Gosling y McGilton, Sun, oct. 1995](https://www.oracle.com/java/technologies/language-environment.html), con respaldo archival en el [catálogo del Computer History Museum, cat. 102751422](https://www.computerhistory.org/collections/catalog/102751422). Generics: Java SE 5.0 (30-09-2004) vía JSR 14, con *type erasure* por compatibilidad hacia atrás. Estable.
