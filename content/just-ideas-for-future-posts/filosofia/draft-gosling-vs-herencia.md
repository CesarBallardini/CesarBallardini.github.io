### C-10 — James Gosling sobre la herencia: el inventor de Java prefiere no usarla

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `gosling-vs-herencia`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-gosling-vs-herencia/index.md`
- **Serie:** filosofia
- **Cross-links:** [[A1-20]] (Java/Gosling), [[A1-13]] (roster), [[C-02]]
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** En la entrevista en *Masterminds* (y en otras posteriores), James Gosling — el padre de Java — dice claramente: "si pudiera rediseñar Java, sacaría las clases" y "prefiero no usar herencia, prefiero composición". Esto contradice 30 años de enseñanza de OOP donde la herencia es el plato principal. El post toma estas declaraciones y discute por qué los inventores de los lenguajes OO terminan recomendando NO usar las features estrella de OOP.

**Hook:** el inventor de Java te dice que NO uses herencia. El inventor de C++ te dice que NO uses excepciones. El inventor de Smalltalk te dice que la mayoría de los lenguajes OO no son OO. ¿Qué pasa?

**Outline:**

1. **Hook — los tres desmentidos.** Gosling sobre la herencia, y los otros dos casos del hook planteados con cautela (no están respaldados por la bibliografía de este draft).
2. **Qué dijo Gosling, y qué no dijo.** Las dos declaraciones del concepto, tratadas como material a verificar antes de citarlas; separar «sacaría las clases» de «prefiero composición» — son dos afirmaciones distintas y la primera es mucho más fuerte.
3. **La herencia como plato principal.** Cómo se enseña OOP: `Animal → Perro → Caniche`, y por qué el ejemplo de juguete nunca muestra la factura.
4. **Dónde se rompe.** Acoplamiento a la implementación del padre, el problema de la clase base frágil, la jerarquía que se elige el primer día y se paga durante diez años.
5. **La pista estaba en el propio Java.** `interface` sin implementación, herencia simple y no múltiple, `final`: el lenguaje ya venía con la desconfianza adentro.
6. **Composición: qué compra y qué cuesta.** No es gratis; es más ceremonia a cambio de menos acoplamiento.
7. **Los otros dos del hook.** Stroustrup y las excepciones, Kay y el sentido original de «orientado a objetos» — con marcas de verificación, no como hechos.
8. **Por qué pasa esto.** El inventor ve el costo agregado de la feature; el docente ve el ejemplo que entra en una diapositiva. No es hipocresía, son dos puntos de observación distintos.
9. **Un lenguaje no es su manual.** Lo que un lenguaje es, en la práctica, lo decide lo que su comunidad hace con él — no lo que su autor recomienda.
10. **Cierre — qué hacer con esto.** La lectura sensata: no «la herencia es mala», sino «la feature estrella no es la que más se debería usar».

**Bibliografía:** (reforzada y verificada 2026-07-16)

- [James Gosling on Java (parte 3)](https://www.artima.com/intv/gosling3.html) — entrevista de Bill Venners, Artima/JavaWorld; grabada el 2001-05-10, publicada el 2001-06-15. **Fuente primaria y citable** de las palabras textuales de Gosling: preguntado por qué rediseñaría de Java, responde que le gustaría un lenguaje «sin jerarquía de herencia; en vez de subclasificar, usar interfaces puras» y aclara «no es que la herencia de clases sea particularmente mala, es que tiene problemas» («*without an inheritance hierarchy. Rather than subclassing, just use pure interfaces. It's not so much that class inheritance is particularly bad. It just has problems.*»). Confirma la preferencia interfaces/composición sobre herencia, en tono matizado. `estable`
- [Allen Holub, «Why extends is evil»](https://www.infoworld.com/article/2160788/why-extends-is-evil.html) — InfoWorld, 2003-08-01. **Origen de la cita-meme «I'd leave out classes».** Holub relata que en una reunión de un Java user group preguntaron a Gosling qué cambiaría de Java y respondió «I'd leave out classes»; tras las risas aclaró que el problema real es la herencia de *implementación* (`extends`), no las clases en sí. **Es un relato de segunda mano** (Holub contando lo que oyó), no una transcripción: la frase literal «sacaría las clases» sale de acá, no de una fuente primaria, y el propio Gosling la matizó en el acto. `estable` (recomendable backup en Wayback antes de publicar)
- [[tr-23]] *Masterminds of Programming* (Federico Biancuzzi & Shane Warden, O'Reilly 2009) — Capítulo 12 «Java» entrevista a James Gosling; el capítulo «C++» entrevista a Bjarne Stroustrup. [archive.org](https://archive.org/details/MastermindsOfProgramming). `estable`. Nota: no se verificó contra el escaneo si Gosling discute la herencia *específicamente* en este capítulo; las citas verificadas de arriba provienen de la entrevista de Artima, no de este libro.
- [Peter Seibel, *Coders at Work: Reflections on the Craft of Programming*](https://archive.org/details/codersatworkrefl0000seib) — Apress, 2009, ISBN 1-4302-1948-3. **CORRECCIÓN: Gosling NO figura entre los 15 entrevistados** (Zawinski, Fitzpatrick, Crockford, Eich, Bloch, Armstrong, Peyton Jones, Norvig, Steele, Ingalls, Deutsch, Thompson, Allen, Cosell, Knuth) — no sirve como fuente de citas de Gosling. Sí entrevista a **Joe Armstrong** (Erlang), autor de la crítica «You wanted a banana but what you got was a gorilla holding the banana and the entire jungle» sobre el acoplamiento implícito de OOP — fuente de apoyo para la sección «dónde se rompe». `estable`
- [[tr-01]] Alan Kay, *The Computer Revolution Hasn't Happened Yet* (OOPSLA 1997) + [[tr-22]] (hilos consolidados sobre qué quiso decir Kay con «orientado a objetos») — respaldan la **tercera** afirmación del Hook (Kay: la mayoría de los lenguajes OO no son OO). Ya verificados en el plan. `frágil` (YouTube; backup archive.org)
- **Stroustrup y las excepciones (segunda afirmación del Hook — NO respaldada, falsa tal como está):** Stroustrup es un *defensor* de las excepciones («exception handling is extremely cheap when you don't throw an exception»; sostiene que hacen el código «simpler, cleaner, and less likely to miss errors»). Fuentes: su [C++ Style and Technique FAQ](https://stroustrup.com/bs_faq2.html) y el paper [P1947 «C++ exceptions and alternatives»](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1947r0.pdf) (2019), donde argumenta *contra* reemplazarlas. La idea de que «desaconseja usar excepciones» es una deformación del caso JSF++ (C++ para aviónica de tiempo real crítico), un dominio acotado con restricciones de timing. Hay que reformular o sacar la frase del Hook. `estable`

**Imágenes:** _a definir_

**Tags propuestos:** `['Gosling','Java','herencia','composicion','OOP','critica']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (10 secciones), se fijó `Length target: medium` y se escribió un borrador de prosa completo (~1800 palabras de prosa efectiva, sin contar marcas de verificación ni huecos) en la sección «Borrador de prosa» al pie.

Lo que quedó **escrito**: todo el armazón argumental, que no depende de citas — la herencia como plato principal de la enseñanza de OOP, dónde se rompe (acoplamiento a la implementación del padre, clase base frágil, la jerarquía elegida el primer día), la lectura de `interface`/herencia simple/`final` como desconfianza ya incorporada al propio Java, composición como intercambio (menos acoplamiento a cambio de más ceremonia), la asimetría inventor/docente, y el cierre sobre lo que un lenguaje es en la práctica. Ese esqueleto se sostiene solo aunque las citas cambien.

Lo que quedó como **hueco**:

- 5 huecos `🕳️` pidiendo a César lo que el post no puede inventar: dónde se enteró de la declaración de Gosling y si lo sorprendió, cómo le enseñaron OOP a él (y cómo la enseñó, si dio clase), si le tocó pelearse con una jerarquía de herencia ajena, si trabajó con Java en serio y desde qué lugar habla, y su veredicto del cierre. Sin eso el post es un ensayo de opinión genérico sobre OOP, que hay cien en internet.
- 8 marcas `[VERIFICAR:]`. Las más importantes: **las dos citas del Concepto** («si pudiera rediseñar Java, sacaría las clases» y «prefiero no usar herencia, prefiero composición») están escritas de memoria en el seed y **no se pueden publicar sin la fuente exacta** — hay que ubicarlas en [[tr-23]], en Channel 9 o en *Coders at Work*, con contexto, y transcribirlas literalmente. Si no aparecen, el post cambia de tesis o no se publica.
- **Las dos afirmaciones extra del Hook no están respaldadas por la bibliografía de este draft**: que Stroustrup desaconseje las excepciones y que Kay diga que la mayoría de los lenguajes OO no son OO. La segunda es reciclable vía [[tr-01]] / [[tr-22]] del plan, que ya están verificados, pero **habría que sumarlos a la `Bibliografía:` de esta entrada**. La primera necesita fuente propia (el candidato natural es la entrevista a Stroustrup en [[tr-23]], si dice eso). En el borrador ambas están escritas como afirmaciones a chequear, no como hechos.
- El estado de la fuente «Gosling en Channel 9» es dudoso: Channel 9 era el sitio de video de Microsoft y **el archivo puede no estar más en línea**. Hay que identificar la entrevista concreta (no «Channel 9» en abstracto), conseguir URL viva o copia en Wayback, o bajarla de la bibliografía.
- `**Imágenes:**` sigue en `_a definir_`. El post no tiene un objeto obvio que fotografiar; la salida más probable es un hero conceptual o un retrato de Gosling con licencia clara en Wikimedia Commons.

El 2026-07-16 se reforzó la bibliografía y se verificaron las atribuciones de citas; se resolvieron 5 de 7 marcadores `[VERIFICAR:]` presentes (el seed hablaba de «8», pero en el cuerpo había 7). Hallazgos clave: (a) la cita fuerte de Gosling («interfaces/composición sobre herencia») **queda confirmada por fuente primaria** — entrevista de Bill Venners para Artima, 2001; (b) la frase-meme «sacaría las clases» **no tiene fuente primaria**: viene del relato de segunda mano de Allen Holub (InfoWorld 2003), y el propio Gosling la matizó (apuntaba a la herencia de implementación) — hay que presentarla como boutade reportada, no como tesis; (c) **corrección de misatribución**: *Coders at Work* NO entrevista a Gosling (sí a Joe Armstrong, del que se rescata la cita «gorila + banana + selva»), así que queda descartada como fuente de citas de Gosling; (d) **la afirmación del Hook sobre Stroustrup es falsa**: Stroustrup defiende las excepciones, la deformación viene de JSF++ — hay que reformular o sacar esa frase (no se tocó el Hook, sólo se dejó anotado); (e) la afirmación de Kay del Hook sí está documentada y se sumaron [[tr-01]]/[[tr-22]] a la bibliografía. Quedaron **sin resolver** 2 marcadores: la fuente «Channel 9» resultó inhallable (sitio dado de baja, sin URL viva ni copia en Wayback identificable — candidata a eliminarse en publicación, ya cubierta por Artima), y la lectura de las decisiones de diseño de Java (`interface`/`final`/herencia simple) sigue siendo interpretación propia sin cita que la respalde. Residuales menores: páginas exactas del capítulo 12 de *Masterminds* y un cotejo opcional de Stroustrup en ese libro. Sin tocar los 5 huecos `🕳️` ni el Hook/Concepto.

---

## Borrador de prosa

Imaginate que vas treinta años a una escuela de cocina donde todo el plan de estudios gira alrededor de una salsa. Toda la carrera: la salsa. Los exámenes, la salsa. Y un día el chef que inventó la salsa da una entrevista y dice, tranquilo, que él prefiere no usarla.

Eso es, más o menos, lo que pasó con la herencia y James Gosling.

Gosling es el padre de Java, el lenguaje que le enseñó orientación a objetos a dos generaciones enteras de programadores — incluida, sospecho, buena parte de los que están leyendo esto. Y en entrevistas dice dos cosas que, si las escuchás con la formación de OOP puesta, chirrían: que si pudiera rediseñar Java le sacaría las clases, y que él prefiere no usar herencia, que prefiere composición.[^gosling_citas]

[^gosling_citas]: Las dos frases tienen procedencias distintas y desigual solidez, verificadas el 2026-07-16. (1) «Prefiero interfaces/composición sobre herencia» **está confirmada como fuente primaria**: en la entrevista de Bill Venners para Artima (2001), Gosling dice que rediseñaría Java «sin jerarquía de herencia; en vez de subclasificar, usar interfaces puras», y matiza «no es que la herencia de clases sea particularmente mala, es que tiene problemas»[^artima]. (2) «Sacaría las clases» es una **cita de segunda mano**: viene del relato de Allen Holub («Why extends is evil», InfoWorld 2003) de una reunión de un Java user group donde Gosling, preguntado qué cambiaría, respondió «I'd leave out classes» y, tras las risas, aclaró que apuntaba a la herencia de *implementación* (`extends`), no a las clases[^holub]. No hay transcripción primaria de esa frase; el post debe presentarla como lo que es (una boutade reportada que Gosling matizó en el acto), no como una tesis literal de diseño. La versión de *Masterminds* [[tr-23]] no se cotejó contra el escaneo; *Coders at Work* queda descartada como fuente porque Gosling no está entre sus entrevistados.

Y no está solo. El hook completo de este post, tal como lo anoté cuando se me ocurrió, era: el inventor de Java te dice que no uses herencia, el inventor de C++ te dice que no uses excepciones, el inventor de Smalltalk te dice que la mayoría de los lenguajes que se llaman orientados a objetos no lo son. ¿Qué está pasando acá?

Antes de seguir tengo que ser honesto con vos sobre esas otras dos: son afirmaciones que arrastro de memoria y todavía no verifiqué.

Verificado el 2026-07-16: la afirmación «Stroustrup desaconseja usar excepciones» es **falsa tal como está**. Stroustrup es un defensor de las excepciones — sostiene que hacen el código «más simple, más limpio y menos propenso a dejar pasar errores» y que «el manejo de excepciones es extremadamente barato cuando no se lanza una excepción»[^stroustrup]. La deformación viene del caso JSF++ (C++ para aviónica de tiempo real crítico), un dominio acotado con restricciones de *timing*, no una recomendación general. **Hay que reformular o sacar esta frase del hook antes de publicar** — como está, atribuye a Stroustrup lo contrario de lo que sostiene. [VERIFICAR: si se quiere conservar algún matiz de Stroustrup sobre excepciones, cotejar además su entrevista en *Masterminds* [[tr-23]], que no se leyó para este punto.]

Resuelto el 2026-07-16: la afirmación de Kay sobre que la mayoría de los lenguajes OO no son OO está bien documentada; se agregaron [[tr-01]] (keynote OOPSLA 1997 *The Computer Revolution Hasn't Happened Yet*) y [[tr-22]] a la `Bibliografía:` de este draft. Al publicar, citar desde ahí y no de memoria; expandir la cita literal desde la fuente (ambas ya verificadas en el plan).

Con esa aclaración hecha, sigo. Porque incluso si las otras dos se caen, la de Gosling sola ya alcanza para el post.

Las fuentes las pongo sobre la mesa desde el principio porque este es un post que se apoya entero en lo que un señor dijo. La cita fuerte y verificable sale de la entrevista de Bill Venners a Gosling para Artima en 2001[^artima]; la frase-meme «sacaría las clases» viene del relato de segunda mano de Allen Holub en InfoWorld[^holub]; y de fondo está la entrevista a Gosling en *Masterminds of Programming*[^masterminds]. (Descarté dos fuentes que traía de memoria: la «entrevista en Channel 9» no la pude ubicar con URL viva[^channel9], y *Coders at Work* de Peter Seibel[^seibel] resultó **no** incluir a Gosling — aunque sí a Joe Armstrong, cuya crítica del «gorila con la banana» me sirve para la parte de acoplamiento.)

### Primero: separá las dos frases

Las dos declaraciones que se le atribuyen a Gosling se citan siempre juntas y son muy distintas en tamaño.

«Prefiero composición antes que herencia» es una preferencia de ingeniería. Es discutible, es defendible, y hoy es casi consenso — está en los libros de diseño, está en las revisiones de código de medio mundo. Que lo diga el autor de Java le agrega peso, no rareza.

«Si rediseñara Java, le sacaría las clases» es otra cosa. Eso no es una preferencia: es una amputación. Java sin clases no es Java con menos features, es un lenguaje distinto. Si esa frase es literal y en serio, el autor del lenguaje OO más masivo de la historia está diciendo que el mecanismo central de su lenguaje fue un error de diseño.

Por eso insisto tanto con la verificación. Una frase así, sacada de contexto, es una bomba de humo: puede ser una boutade en una charla distendida, puede ser una exageración retórica sobre un punto más chico, o puede ser una convicción firme. Cambia todo. Y el género «declaración polémica de creador famoso» está lleno de citas que sobrevivieron sin su contexto porque el contexto arruinaba el titular.

> 🕳️ **HUECO — necesita a César:** ¿cuándo y dónde te enteraste vos de esto? ¿Leyendo *Masterminds*, viendo la entrevista, o de rebote en alguna discusión? Y sobre todo: ¿te sorprendió o te confirmó algo que ya venías masticando? Ese es el ancla personal del post y no lo puedo escribir por vos.

### La salsa

Pensá cómo te enseñaron orientación a objetos. Apostaría a que fue así.

Primero un objeto es «datos más comportamiento». Después encapsulamiento, que se entiende rápido. Y después viene el plato fuerte, el momento en que la materia se pone seria: **la herencia**. `Animal`. De `Animal` sale `Perro`. De `Perro` sale `Caniche`. `Caniche` hereda `ladrar()` y no lo tiene que escribir. Aparece la palabra reuso, aparece polimorfismo, y el ejemplo cierra tan redondo que uno sale convencido de que acaba de ver el corazón del asunto.

Y ahí está el truco, que tardé años en ver: el ejemplo de juguete nunca te muestra la factura. `Animal → Perro → Caniche` funciona perfecto en una diapositiva porque la jerarquía tiene tres niveles, cero excepciones, y nadie la va a mantener el año que viene. Es un ejemplo diseñado para que la herencia se luzca. Nunca te muestran el `Animal` que después tuvo que soportar un ornitorrinco.

> 🕳️ **HUECO — necesita a César:** ¿cómo te enseñaron OOP a vos, y con qué lenguaje? ¿Y si alguna vez la enseñaste o la explicaste a alguien más, la enseñaste con la herencia al frente como te la enseñaron a vos, o ya venías desconfiando?

### Dónde se rompe

La herencia falla por un motivo que el ejemplo del perro esconde: **te acopla a la implementación del padre, no sólo a su interfaz.**

Cuando `Caniche extends Perro`, no estás diciendo «un caniche se comporta como un perro». Estás diciendo «un caniche *es* un perro, con todo lo que un perro tiene adentro, incluidos los atributos protegidos, el orden en que el constructor hace las cosas, y los métodos que hoy se llaman entre sí de una manera que mañana pueden dejar de llamarse». Heredaste la clase entera, no la promesa.

De ahí sale el problema de la clase base frágil, que tiene el nombre más honesto de la ingeniería de software: un cambio interno en la clase padre — un cambio que no toca su interfaz pública, un cambio que su autor considera un detalle privado — puede romper a los hijos. La clase base es frágil porque no puede moverse sin lastimar a gente que ni conoce.

Y hay algo peor, que es de calendario más que de técnica. **La jerarquía se elige el primer día del proyecto, que es el día en que menos sabés del dominio, y se paga durante los diez años siguientes.** El día uno decidís que `Empleado` es un `Persona` y que `Gerente` es un `Empleado`. El año tres aparece el contratista, que trabaja pero no es empleado. El año cinco aparece el gerente que además factura como contratista. Y ahí estás vos, con una taxonomía que se decidió antes de que nadie entendiera el negocio, tratando de que un caso real entre en un árbol que ya no lo admite. La composición, mientras tanto, se puede reordenar un martes cualquiera.

> 🕳️ **HUECO — necesita a César:** ¿te tocó alguna vez agarrar una jerarquía de herencia ya construida por otro y tener que meter un caso que no entraba? No hace falta que nombres el sistema ni el organismo — con el tipo de contorsión que tuviste que hacer alcanza. Es el párrafo que le da carne a toda esta sección.

### La pista estaba adentro de Java

Acá va la parte que a mí me parece la más linda del asunto, y es que si Gosling desconfía de la herencia, no es una conversión tardía: **el propio Java ya venía con esa desconfianza incorporada.**

Mirá las decisiones. Java tiene `interface`, un mecanismo para declarar qué se puede hacer sin heredar nada de cómo se hace — o sea, exactamente la parte útil de la herencia sin el acoplamiento a la implementación. Java tiene herencia simple y no múltiple, cuando C++ tenía múltiple: una restricción deliberada, poner un límite a la profundidad del enredo posible. Java tiene `final`, que es literalmente una palabra clave para decir «de acá no heredás».

Un lenguaje cuyo autor cree que la herencia es la gran idea no se diseña así. Se diseña con herencia múltiple, sin `final`, y con la clase como único ciudadano. Java se diseñó como alguien que sabe que la feature es peligrosa y le pone barandas antes de dejarla salir. Las declaraciones de Gosling veinte años después no contradicen a Java: explicitan lo que Java ya decía en su gramática.

[VERIFICAR: si Gosling explica en alguna de las tres fuentes (*Masterminds*, Channel 9, *Coders at Work*) el motivo de estas decisiones de diseño — herencia simple, `interface`, `final` — citarlo. Este párrafo es una **lectura mía** de las decisiones del lenguaje, no una afirmación sobre sus intenciones, y si no hay cita hay que dejarlo escrito claramente como interpretación.]

### Composición no es magia

Antes de que suene a sermón: composición tampoco es gratis.

Cuando en vez de heredar `Perro` le pasás a tu clase un objeto que sabe ladrar, tenés que escribir el reenvío. Tenés que sostener la referencia, tenés que exponer el método, tenés que armar el cableado. Es más código y es más ceremonia. El chiste de que en Java todo se resuelve con otra fábrica de fábricas no salió de la nada: en gran medida es lo que pasa cuando reemplazás herencia por composición sin tener el soporte del lenguaje para hacerlo barato.

Lo que estás comprando con esa ceremonia es **la posibilidad de cambiar de opinión**. Una relación de composición se reordena; una relación de herencia se demuele. Ese es el intercambio, y como todo intercambio, a veces no conviene.

Por eso la lectura de Gosling que me interesa no es «la herencia es mala». Es más incómoda que eso: **la feature estrella de un paradigma no tiene por qué ser la que más se usa.** Puede ser la más vistosa, la más fácil de enseñar, la que mejor entra en un examen, y aun así ser la que menos deberías tocar en producción.

### Por qué los inventores dicen estas cosas

Queda la pregunta del hook, la de fondo. ¿Por qué el que inventó la cosa termina recomendando no usarla?

Mi respuesta es que inventor y docente miran desde lugares distintos, y ninguno de los dos miente.

El docente necesita un ejemplo que entre en una diapositiva y que se entienda en cuarenta minutos. La herencia es fantástica para eso: `Caniche` hereda `ladrar()` y toda el aula asiente. El docente ve la feature en su mejor día.

El inventor ve otra cosa. El inventor ve la feature agregada sobre millones de líneas y treinta años, en manos de gente que no la usa como él pensaba, en sistemas que él nunca imaginó. Ve la factura completa, con intereses. Después de eso, «prefiero componer» no es una boutade de viejo: es un informe de campo.

Y hay un tercer punto de observación, que es el que más me interesa: **un lenguaje no es lo que dice su manual, ni lo que recomienda su autor. Es lo que su comunidad hace con él, todos los días, durante décadas.** Gosling puede preferir composición todo lo que quiera; el Java que existe en el mundo, el que está corriendo ahora mismo en un banco, está lleno de jerarquías de seis niveles que nadie se anima a tocar. El autor propone; la comunidad dispone; el mantenimiento paga. De eso hablo también en [[C-02]], y a Gosling y a Java les dedico un post propio en [[A1-20]].

> 🕳️ **HUECO — necesita a César:** ¿trabajaste con Java en serio, y en qué contexto? Necesito saber desde dónde estás hablando en este post: ¿desde el que lo sufrió en producción, desde el que lo miró de afuera, desde el que lo enseñó? Cambia el tono de todo el cierre.

### Entonces, ¿qué hago mañana?

Nada dramático. No hace falta que salgas a desarmar tus jerarquías.

Lo que yo me llevo es una regla de sospecha, no una prohibición: cuando estés por escribir `extends`, preguntate si lo estás haciendo porque hay una relación real de sustitución — cualquier lugar donde va el padre puede ir el hijo, para siempre, sin excepciones — o porque te da fiaca escribir el reenvío. La segunda razón es la que te va a costar cara en el año tres.

Y la lección grande, la que sobrevive a Java: cuando alguien te vende un paradigma con una feature estrella al frente, andá a buscar qué dice de esa feature la gente que la construyó. No siempre lo que dice el folleto. Casi nunca, en realidad.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto. ¿Usás herencia hoy, y cuándo? ¿Te parece que Gosling tiene razón, que exagera, o que la discusión ya la ganó la composición sin necesidad de que él la firmara? Una o dos frases tuyas y el post cierra.

---

[^artima]: [James Gosling on Java (parte 3)](https://www.artima.com/intv/gosling3.html), entrevista de Bill Venners, Artima/JavaWorld; grabada el 2001-05-10, publicada el 2001-06-15. Gosling: «*Yes—without an inheritance hierarchy. Rather than subclassing, just use pure interfaces. It's not so much that class inheritance is particularly bad. It just has problems.*» Fuente primaria verificada el 2026-07-16. `estable`
[^holub]: [Allen Holub, «Why extends is evil»](https://www.infoworld.com/article/2160788/why-extends-is-evil.html), InfoWorld, 2003-08-01. Relata de segunda mano una reunión de un Java user group donde Gosling, preguntado qué cambiaría de Java, respondió «I'd leave out classes» y luego aclaró que el blanco era la herencia de implementación (`extends`), no las clases. Origen de la cita-meme; no es transcripción primaria. Verificado el 2026-07-16. `estable` (backup Wayback recomendado antes de publicar).
[^stroustrup]: Bjarne Stroustrup, [C++ Style and Technique FAQ](https://stroustrup.com/bs_faq2.html) y [P1947 «C++ exceptions and alternatives»](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1947r0.pdf) (2019). Stroustrup defiende las excepciones y argumenta contra reemplazarlas; la excepción es JSF++ (aviónica de tiempo real crítico). Verificado el 2026-07-16. `estable`
[^masterminds]: Entrevista a James Gosling en *Masterminds of Programming* (Biancuzzi & Warden, O'Reilly 2009), **Capítulo 12 «Java»** — ver [[tr-23]] en el plan editorial. Verificado el 2026-07-16 que Gosling es el entrevistado de ese capítulo. [VERIFICAR: páginas exactas de la entrevista contra el escaneo en [archive.org](https://archive.org/details/MastermindsOfProgramming); no inventar la referencia de página.]
[^channel9]: Presunta entrevista a James Gosling en Channel 9. [VERIFICAR: no se pudo ubicar una entrevista concreta ni una URL viva el 2026-07-16 — Channel 9 (el sitio de video de Microsoft) fue dado de baja y el archivo parece haber desaparecido. La cita primaria fuerte se cubre con la entrevista de Artima[^artima]; **si no aparece una entrevista de Channel 9 identificable con copia en Wayback, sacar esta nota de la versión publicada**. No pegar URL de memoria.]
[^seibel]: Peter Seibel, *Coders at Work: Reflections on the Craft of Programming*, Apress, 2009, ISBN 1-4302-1948-3; [copia en archive.org](https://archive.org/details/codersatworkrefl0000seib). Verificado el 2026-07-16: **Gosling NO está entre los entrevistados** — no sirve como fuente de citas de Gosling. Sí entrevista a Joe Armstrong, autor de la crítica del «gorila sosteniendo la banana y toda la selva» sobre el acoplamiento implícito de OOP, utilizable como fuente de apoyo para la sección «dónde se rompe».
