### A1-21 — Anders Hejlsberg: el hombre detrás de Turbo Pascal, Delphi, C# y TypeScript

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `hejlsberg-delphi-csharp-typescript`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-hejlsberg-delphi-csharp-typescript/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-13]], [[E-05]] (Vue + TypeScript), [[A1-04]] (Modula-2 — Pascal cousin)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** Pocos diseñadores de lenguajes pueden decir que crearon 4 lenguajes/sistemas comerciales exitosos en distintas empresas y décadas: Turbo Pascal en Borland (años 80), Delphi en Borland (años 90), C# en Microsoft (años 2000), TypeScript en Microsoft (años 2010). Anders Hejlsberg es ese hombre. El post discute la entrevista en *Masterminds* (que cubre Delphi/C#) y agrega lo que pasó después con TypeScript.

**Hook:** el mismo señor diseñó Turbo Pascal, Delphi, C# y TypeScript. Cuatro lenguajes en cuatro décadas en dos empresas distintas. Probablemente el diseñador de lenguajes industriales más exitoso de la historia. ¿Quién es?

**Outline:**

1. **Hook — cuatro lenguajes, cuatro décadas, dos empresas.** El planteo: si el diseño de lenguajes fuera un deporte, este señor tendría el récord. ¿Por qué casi nadie lo nombra?
2. **Turbo Pascal — el compilador que costaba lo que una pizza.** Los años 80 en Borland: velocidad de compilación y precio como decisiones de diseño, no como detalles de marketing.
3. **Delphi — los años 90 y el componente arrastrable.** Pascal con objetos más un constructor visual; la apuesta de que la productividad se diseña, no se documenta.
4. **El pase a Microsoft.** El cambio de empresa y de escala; qué significa rediseñar cuando el que paga es el dueño de la plataforma.
5. **C# — los 2000, y la entrevista de *Masterminds*.** El punto de entrada bibliográfico del post: qué dice Hejlsberg sobre sus propias decisiones.
6. **TypeScript — los 2010, y el giro más raro de todos.** Por primera vez no diseña un lenguaje nuevo: le pone tipos a uno ajeno que no puede cambiar.
7. **El hilo conductor.** La tesis: no es un teórico de lenguajes, es un ingeniero de herramientas. El compilador al servicio del programador que escribe, no de la elegancia del modelo.
8. **Lo que la carrera no explica.** Cuánto de los cuatro éxitos es diseño y cuánto es posición: Borland y Microsoft le dieron distribución. El contrafáctico honesto.
9. **Por qué no está en el panteón.** Wirth, Stroustrup, McCarthy tienen estatua; Hejlsberg no. Hipótesis: el panteón premia la idea original, no el producto que funciona.
10. **Cierre — el veredicto personal.** Qué tipo de éxito es este, y si es el que uno querría.

**Bibliografía:**

_Fuentes verificadas por fetch el 2026-07-16. Todas las afirmaciones de fecha/precio/rol de la prosa se apoyan en alguna de estas._

- [[tr-23]] — *Masterminds of Programming* (Federico Biancuzzi & Shane Warden, O'Reilly 2009), capítulo de entrevista a Anders Hejlsberg sobre Delphi y C#. [archive.org](https://archive.org/details/MastermindsOfProgramming) — **estable**.
- [Turbo Pascal — Wikipedia (EN)](https://en.wikipedia.org/wiki/Turbo_Pascal) — lanzamiento 20-nov-1983, precio US$49.95 por venta directa, origen en el compilador previo de Hejlsberg (Blue Label Pascal, 1981 / «PolyPascal» de su empresa danesa *Poly Data*, cuyo core licenció Borland). **estable**.
- [Delphi (software) — Wikipedia (EN)](https://en.wikipedia.org/wiki/Delphi_(software)) — Borland, 1995; herramienta RAD sucesora de Turbo Pascal, sobre el dialecto Object Pascal. **estable**.
- [Anders Hejlsberg — Wikipedia (EN)](https://en.wikipedia.org/wiki/Anders_Hejlsberg) — pase a Microsoft en 1996; primeros trabajos J++ y Windows Foundation Classes; arquitecto líder de C# desde 2000; anuncio de TypeScript en 2012 («a superset of JavaScript»); título actual Technical Fellow. **estable**.
- [Sun, Microsoft settle Java lawsuit — InfoWorld (2001)](https://www.infoworld.com/article/2159673/sun-microsoft-settle-java-lawsuit.html) — Sun demandó a Microsoft en octubre de 1997 por distribuir una versión de Java incompatible con la de Sun (afecta Visual J++); acuerdo el 23-ene-2001 por US$20 millones. **frágil** (URL de nota vieja; buscar backup en Wayback antes de publicar si se vuelve load-bearing).
- [TypeScript Design Goals — wiki oficial en GitHub](https://github.com/microsoft/TypeScript/wiki/TypeScript-Design-Goals) — Goal 3 «Impose no runtime overhead on emitted programs», Goal 4 «Emit clean, idiomatic, recognizable JavaScript code», Goal 9 «Use a consistent, fully erasable, structural type system»; Non-goal 5 «Add or rely on run-time type information». **estable**.
- [A 10x Faster TypeScript — devblogs.microsoft.com, Anders Hejlsberg, 11-mar-2025](https://devblogs.microsoft.com/typescript/typescript-native-port/) — anuncio del port nativo del compilador a Go («reduce most build times by 10x»); benchmarks 10.4x (VS Code), 13.5x (TypeORM); se publicará como TypeScript 7.0. Código en [github.com/microsoft/typescript-go](https://github.com/microsoft/typescript-go). Confirma que Hejlsberg sigue como arquitecto activo. **estable**.
- [Announcing TypeScript 1.0 — devblogs.microsoft.com, 2-abr-2014](https://devblogs.microsoft.com/typescript/announcing-typescript-1-0/) — confirma «our first release, TypeScript 0.8 in October 2012». **estable**.
- [Channel 9 (Microsoft) — Wikipedia (EN)](https://en.wikipedia.org/wiki/Channel_9_(Microsoft)) — el sitio fue fusionado con Microsoft Learn: anunciado el 5-nov-2021, completado el 1-dic-2021; los videos migrados quedaron en Microsoft Learn (Shows/Events) y hay copias de rescate en el Internet Archive. **estable** (para la ficha de discontinuación; los videos puntuales de Hejlsberg siguen sin URL fija verificada — ver footnote).

**Imágenes:** _a definir_

**Tags propuestos:** `['Hejlsberg','Delphi','C#','TypeScript','Turbo Pascal','historia','Borland']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (10 secciones), se fijó `Length target: medium` y se escribió un borrador de prosa completo (~1400 palabras de prosa efectiva, sin contar marcas de verificación ni huecos) en la sección «Borrador de prosa» al pie. Está en el piso del `Length target`: al resolver los huecos con material de César la prosa debería llegar cómoda a las 1700-1900.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 10 de 13 marcadores `[VERIFICAR:]` de la prosa/footnotes. Los 3 restantes quedaron **acotados** (no eliminados): (1) el encuadre de Delphi como competidor «directo» de Visual Basic —ninguna fuente fetchada lo dice con esas palabras—; (2) si Hejlsberg sigue igual de activo en 2026 —la fuente más nueva confirmada es de marzo de 2025—; (3) la URL de un video puntual de Hejlsberg en el archivo de Channel 9 (el sitio se fusionó con Microsoft Learn en dic-2021; no se localizó una URL de video específica verificable). La bibliografía pasó de 3 referencias sin URL a 9 con URL verificada; el «riesgo bibliográfico serio» previo (Channel 9 y las design notes sin URL) quedó saneado: las design notes ahora apuntan a la wiki oficial y Channel 9 quedó documentado como discontinuado.

Lo que quedó **escrito**: el armazón argumental entero — el recorrido por los cuatro lenguajes, la tesis central (Hejlsberg como ingeniero de herramientas y no como teórico de lenguajes), el contrafáctico honesto sobre cuánto del éxito es diseño y cuánto es distribución, la hipótesis sobre por qué no está en el panteón, y el cierre. Se sostiene solo como ensayo.

Lo que quedó como **hueco**:

- 6 huecos `🕳️` pidiendo a César lo que el post no puede inventar: si usó Turbo Pascal y en qué contexto, si Delphi apareció en su vida profesional o en el sector público, su relación real con C# y con TypeScript, qué le pasó al leer la entrevista de *Masterminds*, y el veredicto del cierre. Sin eso es un ensayo correcto pero impersonal.
- Marcas `[VERIFICAR:]` (actualización 2026-07-16): de las ~13 marcas originales en prosa y footnotes, quedaron **resueltas con fuente fetchada** las de la asignación de cada lenguaje a su década, fechas y precio de Turbo Pascal ($49.95, 20-nov-1983), el compilador previo a Borland (Blue Label/PolyPascal, licenciado), la autoría (Hejlsberg arquitecto del compilador; Borland puso UI/editor), el año de Delphi (1995), el pase a Microsoft (1996) y el trabajo previo a C# (J++/WFC + litigio Sun-Microsoft), las fechas de C# (1.0 en ene-2002, .NET 1.0 el 13-feb-2002) y de TypeScript (0.8 en oct-2012, anunciado por Hejlsberg), el borrado de tipos en compilación (design goals oficiales), el estado de adopción (5º lenguaje más usado, 38.5%, SO Survey 2024) y el rol actual (Technical Fellow; port a Go anunciado por él en mar-2025). Quedan **3 marcas acotadas**: el encuadre Delphi-vs-Visual-Basic, si sigue activo en 2026, y la URL de un video puntual de Channel 9.
- **Riesgo bibliográfico**: saneado el 2026-07-16. Las «TypeScript design notes» ahora apuntan a la wiki oficial (`microsoft/TypeScript/wiki/TypeScript-Design-Goals`, verificada). Channel 9 quedó documentado como discontinuado (fusionado con Microsoft Learn en dic-2021; copias en Internet Archive), aunque falta fijar la URL de un video concreto de Hejlsberg. La única fuente marcada **frágil** es la nota de InfoWorld sobre el acuerdo Sun-Microsoft (URL de noticia vieja; conseguir backup en Wayback si se vuelve load-bearing). El resto son URLs estables (Wikipedia, devblogs.microsoft.com, github.com, archive.org).
- El post cubre cuatro lenguajes, lo que roza la regla de la casa de **un concepto por post**. La defensa es que el concepto único es «el hilo conductor de una carrera», no los lenguajes. Si al releerlo se siente como cuatro miniposts pegados, hay que podar — probablemente sacrificando Turbo Pascal y Delphi a un párrafo cada uno.
- `**Imágenes:**` sigue en `_a definir_`. Candidatos: una caja o pantalla de Turbo Pascal, o el IDE de Delphi. Hay que encontrar algo con licencia clara en Wikimedia Commons; las capturas de software propietario **no** son automáticamente usables.

---

## Borrador de prosa

Hacé el ejercicio conmigo. Pensá en un diseñador de lenguajes de programación que la haya pegado. Uno solo. Alguien que haya hecho un lenguaje que la gente usó de verdad, para trabajar, para ganarse la vida.

Ahora pensá en alguien que lo haya hecho **cuatro veces**. En cuatro décadas distintas. En dos empresas distintas. Con cuatro lenguajes que no se parecen entre sí y que salieron cada uno en un mundo tecnológico diferente.

Hay una sola persona en esa lista y se llama Anders Hejlsberg. Turbo Pascal en los 80 (Borland lo lanzó el 20 de noviembre de 1983), Delphi en los 90 (Borland, 1995), C# en los 2000 (versión 1.0 en enero de 2002, arquitecto líder desde 2000) y TypeScript en los 2010 (anunciado en 2012). Cuatro de cuatro. Y si te pregunto quién diseñó Pascal me vas a decir Wirth, y si te pregunto quién diseñó C++ me vas a decir Stroustrup, pero si te pregunto quién diseñó TypeScript hay una posibilidad razonable de que no me contestes nada.

Eso es lo que me interesa de este post. No la biografía. La pregunta de por qué el diseñador de lenguajes industriales más exitoso de la historia no tiene estatua.

### Turbo Pascal: el compilador que costaba lo que una pizza

Los años 80. Un compilador era una cosa cara, lenta y solemne. Escribías el código, mandabas a compilar, te ibas a hacer otra cosa, volvías.

Turbo Pascal rompió las dos cosas a la vez: era rapidísimo y era barato.

Turbo Pascal salió el 20 de noviembre de 1983 y se vendía por correo directo a US$49.95 — alrededor de una décima parte de lo que costaban los compiladores comparables de la época.

No salió de la nada. Hejlsberg ya había escrito su propio compilador de Pascal antes de Borland: el Blue Label Pascal de 1981 para el microcomputador Nascom, que evolucionó en el «PolyPascal» de su empresa danesa Poly Data. Borland licenció ese core y le sumó la interfaz de usuario y el editor. Es decir: el compilador era de Hejlsberg — fue el arquitecto de todas las versiones de Turbo Pascal — y Borland puso el envoltorio.

Lo que quiero marcar es que **esas dos decisiones son decisiones de diseño**, no de marketing. Que el compilador sea rápido no es un detalle de implementación: cambia lo que el programador hace. Si compilar cuesta tres segundos, compilás cada tres minutos y el compilador se vuelve parte de cómo pensás. Si cuesta cinco minutos, compilás dos veces por día y programás a ciegas.

Y el precio hace lo mismo a otra escala. Un compilador que cuesta lo que un disco define quién puede programar. No es filantropía — es una decisión sobre a quién está dirigida la herramienta.

Guardate esta idea, porque es la única que va a sobrevivir intacta las cuatro décadas.

> 🕳️ **HUECO — necesita a César:** ¿usaste Turbo Pascal? ¿En la facultad, en tu casa, en un trabajo? Y si lo usaste: ¿te acordás de la sensación de la velocidad de compilación, o eso es un dato que aprendiste después leyendo?

### Delphi: el componente que se arrastra

Los 90 traen un problema nuevo: Windows. La gente quiere ventanas, botones, formularios. Y programar una interfaz gráfica a mano era un suplicio de mensajes y punteros.

Delphi fue la respuesta de Borland: tomá Pascal, ponele objetos, y ponele arriba un constructor visual donde arrastrás un botón a un formulario y hacés doble click para escribir qué pasa cuando alguien lo aprieta.

Borland lanzó Delphi en 1995: una herramienta RAD (rapid application development) presentada como la sucesora de Turbo Pascal, sobre el dialecto Object Pascal. [VERIFICAR: el encuadre de que competía «directamente» con Visual Basic de Microsoft no lo confirma ninguna fuente que haya podido fetchear — Wikipedia (Delphi, Visual Basic, RAD) no lo dice con esas palabras; conseguir fuente antes de afirmarlo, o bajarlo a «RAD para Windows de la misma generación que Visual Basic».]

Fijate el patrón, porque es el mismo de antes con otra ropa. La pregunta que resuelve Delphi no es «¿cuál es el modelo de objetos correcto?». Es «¿cómo hago para que alguien tenga una aplicación andando en veinte minutos?». Es otra vez la velocidad, otra vez el acceso, otra vez el programador concreto sentado frente a la máquina en lugar del programador ideal del paper.

> 🕳️ **HUECO — necesita a César:** ¿Delphi apareció alguna vez en tu vida profesional? En el sector público argentino hubo mucho sistema hecho en Delphi — ¿te tocó alguno, aunque sea de refilón, para mantener o para migrar?

### El pase a Microsoft

En 1996 Hejlsberg deja Borland y se va a Microsoft. Sus primeros trabajos ahí fueron Visual J++ y las Windows Foundation Classes: herramientas de Java para Windows. Y ahí se cruza con un litigio que le cambió el rumbo. En octubre de 1997 Sun demandó a Microsoft por distribuir una versión de Java incompatible con la suya — el pleito tocaba justamente a Visual J++ — y terminó en un acuerdo el 23 de enero de 2001 por US$20 millones, con Microsoft impedido de seguir construyendo sobre Java. De ese callejón sin salida salieron C# y .NET.

Lo que sí se puede decir sin arriesgar nada es lo que cambia de escala. En Borland diseñaba productos que competían contra la plataforma. En Microsoft diseña **para** la plataforma, y la plataforma es de la casa. Eso te cambia todo: qué podés romper, qué tenés que sostener por veinte años, y a cuánta gente le arruinás el día si te equivocás.

### C#: el capítulo del libro

Acá entra la fuente que originó este post.

*Masterminds of Programming*[^masterminds] es un libro de entrevistas a creadores de lenguajes — le dediqué un post al roster completo de las entrevistas [[A1-13]], así que acá voy directo al capítulo que importa. Hejlsberg es uno de los entrevistados, y la conversación cubre Delphi y C#.

Hejlsberg es arquitecto líder del equipo de C# desde 2000; la versión 1.0 del lenguaje salió en enero de 2002 junto con Visual Studio .NET, y el .NET Framework 1.0 se publicó el 13 de febrero de 2002.

> 🕳️ **HUECO — necesita a César:** ¿qué te pasó leyendo la entrevista a Hejlsberg en *Masterminds*? ¿Hubo alguna respuesta que te haya hecho parar y releer? Es el ancla personal del post — sin eso, el capítulo de C# es una ficha de Wikipedia.

> 🕳️ **HUECO — necesita a César:** ¿escribiste C# alguna vez, o es un lenguaje que mirás de afuera? Tu relación real con él cambia el tono de toda esta sección.

Lo que a mí me quedó de ese capítulo — y esto es lectura mía, no cita — es que Hejlsberg no habla como un teórico. Habla como alguien que tiene que entregar algo que millones de personas van a usar mañana y que no puede darse el lujo de tener razón dentro de quince años.

### TypeScript: el giro más raro

Y acá viene lo verdaderamente extraño de la carrera, que es el motivo por el que este post no es una lista.

En los tres casos anteriores Hejlsberg diseñó un lenguaje. Con TypeScript hizo otra cosa: agarró un lenguaje **ajeno**, que no podía modificar, que no controlaba, que tenía millones de líneas de código escrito y una semántica que nadie iba a cambiarle — JavaScript — y le puso un sistema de tipos encima.

Pensá en la restricción. No podés romper nada. Todo el JavaScript que existe tiene que seguir siendo TypeScript válido. No podés inventar un runtime propio: lo que escribís tiene que terminar siendo JavaScript que corre en el navegador de cualquiera.

Y esto no es lectura mía: son los objetivos de diseño declarados del proyecto. La wiki oficial de TypeScript los lista textualmente — «Impose no runtime overhead on emitted programs», «Emit clean, idiomatic, recognizable JavaScript code», «Use a consistent, fully erasable, structural type system» — y entre los no-objetivos, «Add or rely on run-time type information in programs». El sistema de tipos es completamente borrable: en tiempo de compilación se evapora y lo que queda es JavaScript común.

TypeScript se anunció públicamente en 2012 (la primera versión, 0.8, es de octubre de 2012), y quien lo presentó fue el propio Hejlsberg.

Diseñar así no es diseñar un lenguaje. Es diseñar un **encastre**. Es ingeniería de restricciones, no de ideas: la pregunta no es «¿cuál es el mejor sistema de tipos?», sino «¿cuál es el mejor sistema de tipos que puedo ponerle a esto sin que se caiga nada de lo que ya está escrito?».

Y funcionó, que es la parte increíble. En la Stack Overflow Developer Survey 2024, TypeScript aparece como el 5º lenguaje más usado por los desarrolladores (38.5% de los encuestados lo había usado en el último año), por detrás de JavaScript, HTML/CSS, Python y SQL. No es «el default de facto» de nada, pero para un lenguaje nacido en 2012 estar entre los cinco más usados de la profesión no es poca cosa.

> 🕳️ **HUECO — necesita a César:** vos usás TypeScript con Vue [[E-05]]. ¿Qué te da y qué te cuesta, en tu experiencia concreta? ¿Hubo algún momento en que el tipado te salvó de un bug real, o algún momento en que te sentiste peleando contra el compilador por nada?

### El hilo

Poné los cuatro en fila y buscá qué se repite. No es la sintaxis. No es el paradigma — hay Pascal estructurado, hay objetos, hay tipado gradual sobre un lenguaje dinámico. No es la empresa ni la década.

Lo que se repite es la **postura frente al programador**.

Los cuatro proyectos contestan la misma pregunta: ¿qué necesita la persona que está sentada escribiendo código ahora mismo? Turbo Pascal contesta «que compile rápido y que lo pueda pagar». Delphi contesta «que arrastre un botón y funcione». C# contesta «que tenga la plataforma entera y no me pelee con ella». TypeScript contesta «que el editor me avise antes de que rompa producción».

Ninguna de esas es una pregunta de teoría de lenguajes. Todas son preguntas de **herramientas**.

Esa es mi tesis sobre Hejlsberg: no es un teórico que además hizo productos. Es un ingeniero de herramientas que usa el diseño de lenguajes como medio. Y creo que ahí está el secreto de los cuatro de cuatro. Los teóricos aciertan cuando la idea es buena; los toolmakers aciertan cuando entienden al que sufre.

### Ahora la parte incómoda

Si voy a decir que es el diseñador industrial más exitoso de la historia, tengo que decir también lo que juega en contra.

**Los cuatro lenguajes tuvieron distribución.** Borland tenía un canal comercial y Microsoft tenía la plataforma. C# no compitió de igual a igual con nadie: venía adentro de la casa del dueño de Windows. TypeScript tampoco: venía con el peso de Microsoft y con VS Code, que es el editor de casi todos.

Entonces la pregunta honesta es: ¿cuánto de esos cuatro éxitos es diseño y cuánto es posición?

Mi respuesta, que es discutible: la posición explica que un lenguaje **arranque**, no que sobreviva. Microsoft empujó muchas cosas con toda la fuerza de la casa y se murieron igual. Distribución te compra la primera versión; la décima te la compra que la herramienta sea buena. Cuatro de cuatro, en cuatro contextos distintos, es demasiada suerte seguida como para ser sólo suerte.

Pero no quiero venderte la versión heroica. Wirth diseñó Pascal sin Microsoft atrás, y Pascal está en el árbol genealógico de todo, incluido Turbo Pascal, incluido Delphi, incluido — por herencia — buena parte de lo que Hejlsberg hizo después [[A1-04]]. Hay más de una manera de ganar.

### Por qué no tiene estatua

Vuelvo a la pregunta del principio.

Mi hipótesis es que el panteón premia la **idea original**, no el producto que funciona. McCarthy tiene estatua porque Lisp es una idea. Wirth tiene estatua porque Pascal es una posición sobre cómo se enseña a programar. Ninguno de los cuatro lenguajes de Hejlsberg es una idea nueva: Turbo Pascal es Pascal rápido y barato, Delphi es Pascal con objetos y un IDE, C# es un lenguaje de la familia C con una plataforma, TypeScript es tipado sobre JavaScript.

Todos son **ejecución**. Y la ejecución no da fama académica, aunque sea lo que hace que la computación funcione.

Hay algo casi injusto ahí, y algo casi justo. Injusto porque hacer que millones de personas programen mejor es un aporte enorme. Justo porque el panteón mide otra cosa, y está bien que mida otra cosa: no todos los oficios son el mismo oficio.

El rol formal de Hejlsberg en Microsoft es el de Technical Fellow, y seguía activo al frente de TypeScript hasta hace poco: en marzo de 2025 fue él quien anunció el port nativo del compilador a Go (el trabajo que se publicará como TypeScript 7.0, con builds hasta 10 veces más rápidos). [VERIFICAR: si sigue igual de activo en 2026 — la fuente más reciente que pude confirmar es de marzo de 2025; el dato envejece rápido.]

### El veredicto

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu opinión, no la mía. Después de recorrer los cuatro: ¿la carrera de Hejlsberg te parece admirable o te parece la carrera de alguien que siempre estuvo en el lugar correcto? ¿Y qué preferirías vos — la estatua de Wirth o los cuatro de cuatro?

---

[^masterminds]: Entrevista a Anders Hejlsberg sobre Delphi y C#, en *Masterminds of Programming* — ver [[tr-23]] en el plan editorial.
[^channel9]: Sobre Channel 9: Microsoft fusionó el sitio con Microsoft Learn — lo anunció el 5 de noviembre de 2021 y lo completó el 1 de diciembre de 2021; los videos migrados quedaron en Microsoft Learn (secciones Shows/Events) y hay copias de rescate en el Internet Archive ([Channel 9 — Wikipedia](https://en.wikipedia.org/wiki/Channel_9_(Microsoft))). [VERIFICAR: todavía falta fijar la URL concreta a un video puntual de Hejlsberg dentro de Microsoft Learn o del Internet Archive — no pude verificar una específica; no pegar una URL de memoria. Alternativa ya verificada si se necesita fuente en video/entrevista: el post «A 10x Faster TypeScript» firmado por Hejlsberg, https://devblogs.microsoft.com/typescript/typescript-native-port/ .]
[^designnotes]: Objetivos de diseño de TypeScript — [TypeScript Design Goals](https://github.com/microsoft/TypeScript/wiki/TypeScript-Design-Goals), wiki oficial del repositorio `microsoft/TypeScript` en GitHub (verificada 2026-07-16). De ahí salen las citas literales de los goals 3, 4 y 9 y del non-goal 5.
