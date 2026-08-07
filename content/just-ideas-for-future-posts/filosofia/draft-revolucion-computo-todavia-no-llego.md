### C-05 — La revolución del cómputo todavía no llegó (ángulo filosófico)

- **Archivo seed:** `dev/draft-alan-kay-the-computer-revolution.md` (compartido con [[A1-01]])
- **Slug propuesto:** `revolucion-computo-todavia-no-llego`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-revolucion-computo-todavia-no-llego/index.md`
- **Serie:** C — cross con [[A1-01]] (mismo seed, distinto enfoque)
- **Cross-links:** depende de [[tr-01]] y [[tr-21]]; lleva a [[C-01]] (oxímoron), [[A1-01]] (versión historiográfica), [[D-04]] (Engelbart como contraste práctico)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** este post toma la misma fuente que [[A1-01]] pero la atraviesa por otro ángulo. [[A1-01]] cuenta *qué* dijo Kay y *quién* es Kay. Este post es la pregunta filosófica: ¿qué *sería* una revolución del cómputo, qué criterios usaríamos para reconocerla si pasara, y por qué ninguno de los criterios serios se cumple en 2026? Es un ensayo crítico, no histórico.

**Diferencia con A1-01:** A1-01 está organizado como "el lenguaje/persona y la idea". C-05 está organizado como "el argumento y por qué sigue siendo cierto 30 años después". Misma fuente primaria, distinto contrato de lectura. Pueden citarse mutuamente.

**Hook:** "en 1997 Alan Kay dijo: *the computer revolution hasn't happened yet*. La pregunta interesante no es 'tenía razón'. La pregunta interesante es: ¿con qué criterios estaba juzgando? Porque si los criterios eran serios, entonces 30 años después seguimos sin tenerla. Y si lo importante de la revolución no era la potencia ni el tamaño, ¿qué era?"

**Outline:**
1. El planteo: una "revolución" en sentido fuerte (no marketing) requiere un cambio en *qué se puede pensar*, no en *qué se puede comprar*.
2. Tres criterios candidatos para reconocer una revolución del cómputo:
   - **Criterio Kay:** el cómputo como nuevo medio (como la imprenta). Crítica: el smartphone *no* es un nuevo medio, es una caja de medios viejos.
   - **Criterio Engelbart:** *augmenting human intellect*. Crítica: lo que tenemos es *replacing* en muchos casos, no *augmenting*.
   - **Criterio Licklider:** *man-computer symbiosis*. Crítica: la interfaz sigue siendo asimétrica y el balance se inclinó hacia la dependencia.
3. Las cosas que sí cambiaron pero no son la revolución: velocidad, miniatura, conectividad. Críticas a la confusión entre escala y revolución.
4. Cómo un LLM cambia (o no) este análisis. Esta sección es la actualización honesta del argumento de Kay a 2026.
5. Lo que reconocería Kay como progreso: pista — Etoys con chicos, no GPT-5 con adultos.
6. Cierre: el post como invitación a que el lector arme su propio criterio. No clausurar.

**Bibliografía:**
- [[tr-01]] — Kay, *The Computer Revolution Hasn't Happened Yet*, OOPSLA 1997.
- [[tr-21]] — Kay, *Is "Software Engineering" an Oxymoron?* (Croquet manual, 2002).
- [[tr-22]] — discusiones consolidadas sobre OOP de Kay.
- [J.C.R. Licklider, *Man-Computer Symbiosis*, IRE Transactions on Human Factors in Electronics, 1960](https://groups.csail.mit.edu/medg/people/psz/Licklider.html).
- [Douglas Engelbart, *Augmenting Human Intellect: A Conceptual Framework*, SRI 1962](https://www.dougengelbart.org/content/view/138/) — el otro texto fundacional.
- [Bret Victor, *The Future of Programming*, DBX 2013](https://vimeo.com/71278954) — heredero directo del argumento de Kay, en formato charla.
- [Bret Victor, *Inventing on Principle*, CUSEC 2012](https://vimeo.com/36579366).
- [Ted Nelson, *Computer Lib / Dream Machines*, 1974](https://archive.org/details/computer-lib-dream-machines).
- [Neil Postman, *Technopoly*, Knopf 1992](https://archive.org/details/technopolysurren00post) — referencia para el escepticismo culturalista.
- [Alan Kay & Adele Goldberg, *Personal Dynamic Media*, IEEE Computer 1977](http://www.newmediareader.com/book_samples/nmr-26-kay.pdf) — el texto original del Dynabook.

**Imágenes:**
- _Wikimedia_: ARPA / Xerox PARC vintage shots — varias disponibles bajo licencia libre, mismo set que [[A1-01]].
- _Crear_: tabla didáctica de los tres criterios (Kay / Engelbart / Licklider) y qué pasaría con cada uno hoy (~45 min).
- _Crear_: línea de tiempo simple 1960-2026 con los hitos honestos vs los hitos de marketing (~1 hora).

**Tags propuestos:** `['Alan Kay', 'Engelbart', 'Licklider', 'filosofia', 'historia', 'critica']`

**Estado actual:** prosa completa escrita siguiendo el outline de 6 puntos (~1900 palabras), citando únicamente la bibliografía ya verificada del draft. Quedaron **cinco huecos** (🕳️): cómo llegó César a la charla de Kay y qué le pasó al escucharla, la digitalización del sector público de Santa Fe leída contra el criterio Engelbart, si vio a un chico programando de verdad, la anécdota de la máquina vieja que hacía algo que hoy no se puede hacer, y su propio criterio personal para el cierre. Quedaron **cinco marcas `[VERIFICAR:]`** sobre atribuciones y fraseos que se le adjudican a Kay, Licklider, Engelbart y Victor (la analogía con la imprenta en OOPSLA 1997, la distinción *augmenting*/*replacing* en el reporte del 62, el reparto de tareas de Licklider, el año desde el que se para Victor en DBX, el rol de Etoys): las fuentes están en la bibliografía pero las frases exactas, los años y los detalles de contexto no fueron chequeados contra el original. **Nota de encuadre:** el outline pedía «por qué ninguno de los criterios serios se cumple en 2026» y una sección sobre LLMs; la prosa sostiene el argumento pero lo escribe como criterio y evaluación del lector, no como veredicto del blog, porque la bibliografía del draft llega hasta 2013 y no respalda afirmaciones fácticas sobre 2026 ni sobre qué hacen los LLMs. La sección 4 quedó deliberadamente como preguntas abiertas. Pendiente al publicar: resolver los `[[ID]]` a URLs reales, verificar el link frágil de [[tr-01]] (YouTube) y los dos de Vimeo, armar la tabla de los tres criterios y la línea de tiempo.

---

## Borrador de prosa

En 1997, en el escenario de OOPSLA, Alan Kay dio una charla que tituló *The Computer Revolution Hasn't Happened Yet*[^kay97]. Es una frase que se cita mucho y se piensa poco. Casi siempre se la usa como una queja de viejo gruñón —«nada de lo que hacen ustedes me gusta»— o como profecía de que ya va a llegar lo bueno.

Pero la pregunta interesante no es si Kay tenía razón. La pregunta interesante es con qué criterio estaba juzgando. Porque una afirmación así sólo significa algo si atrás hay una vara: si sabés qué contarías como revolución, entonces podés mirar alrededor y ver si pasó. Y si la vara era seria, entonces treinta años después seguimos sin tenerla, y eso no es una queja: es un diagnóstico que se puede discutir. Eso es lo que quiero hacer acá: no contarte qué dijo Kay —de eso me ocupo en [[A1-01]]— sino desarmar el argumento y ver si aguanta.

### Una revolución no es un producto mejor

Arranquemos por lo aburrido pero necesario: qué querría decir «revolución» en sentido fuerte.

La palabra está arruinada. Todos los años hay tres o cuatro productos revolucionarios, y son todos la misma cosa un poco más rápida. Kay usaba una analogía que sirve para limpiar el término: la imprenta[^kay97stanford]. Lo importante de la imprenta no fue que los libros salieran más baratos. Fue que, un par de siglos después, existían la ciencia moderna, el ensayo, el estado-nación y la idea de discutir públicamente una teoría. La imprenta no aceleró lo que ya se hacía: hizo pensables cosas que antes no lo eran.

> ⚠️ **CORRECCIÓN DE FUENTES (pasada de sourcing, 2026-07-15):** el borrador atribuía la analogía de la imprenta a la keynote de OOPSLA 1997 ([[tr-01]]). **No está ahí.** Bajé el transcript completo de esa charla (7.362 palabras, de «Thank you. Well, I presume most of you have been up all night» hasta «Just play it grand. Thank you.») desde el Viewpoints Intelligent Archive y no aparece ni una vez «printing», «press», «Gutenberg» ni «incunabula»; el transcript de Moryton —que es la misma transcripción de A. R. Svendsen— da el mismo resultado. La analogía **sí es de Kay y sí es de 1997**, pero de **otra charla con el mismo título**: la del 4 de junio de 1997 en el coloquio EE380 de Stanford (dada en Walt Disney Imagineering), cuyo abstract la usa dos veces. Reatribuida a `[^kay97stanford]`. **Ojo al publicar:** hay al menos **dos charlas de 1997 tituladas _The Computer Revolution Hasn't Happened Yet_** (Stanford/Disney en junio, OOPSLA en octubre) más una tercera posterior en la AES (109ª convención, 24 de septiembre); el post tiene que distinguirlas o va a repetir el error. El Hook («en 1997 Alan Kay dijo…») no se toca: es correcto para las dos.

Ese es el filo del criterio. Una revolución cambia **qué se puede pensar**, no **qué se puede comprar**. Si lo único que cambió es la escala —más rápido, más chico, más barato, más conectado— entonces tenés una industria muy exitosa, que no es lo mismo. Y con esa vara, el resultado de mirar alrededor es incómodo.

### Tres criterios que sí son serios

No hay un solo criterio. Hay por lo menos tres, de tres personas distintas, y no dicen lo mismo. Vale la pena separarlos, porque cada uno falla —o no— por motivos diferentes.

**El criterio Kay: el cómputo como medio nuevo.** En *Personal Dynamic Media*, de 1977, Kay y Adele Goldberg describen el Dynabook[^dynabook]: no un aparato, sino un medio. La idea es que la computadora es el primer medio capaz de simular a todos los demás —incluido él mismo— y que además es *activo*: podés escribirle al medio y el medio te responde. Un libro no discute. Una simulación sí.

La crítica se escribe sola. El teléfono en tu bolsillo, medido con esa vara, no es un medio nuevo: es una caja de medios viejos. Tiene la tele adentro, el diario adentro, el correo adentro, el teléfono adentro, la radio adentro. Todos ellos en versión consumo, ninguno en versión escritura. La parte activa —que vos puedas construir un modelo dentro del medio y que el medio corra tu modelo— es exactamente la parte que no viene incluida. El aparato más difundido de la historia es, con el criterio de su propio profeta, un electrodoméstico.

**El criterio Engelbart: aumentar el intelecto.** El reporte de 1962 de Doug Engelbart se llama *Augmenting Human Intellect: A Conceptual Framework*[^engelbart], y no es un catálogo de inventos: es un programa. Engelbart define el término sin rodeos en la primera página: «By "augmenting human intellect" we mean increasing the capability of a man to approach a complex problem situation, to gain comprehension to suit his particular needs, and to derive solutions to problems»[^engelbart]. La tesis es que se puede subir sistemáticamente la capacidad de una persona —y sobre todo de un grupo— para atacar problemas complejos, y que la computadora es la palanca. La palabra que importa es *augmenting*: el humano queda en el centro, más capaz que antes.

La crítica acá es distinta, y quiero ser prolijo con la atribución, porque fui a buscarla al original y no está: **la oposición *augmenting* / *replacing* es mía, no de Engelbart.** En el reporte de 1962 la palabra «replace» no aparece nunca. Engelbart no polemiza contra el reemplazo —sencillamente da por sentado que la persona queda adentro del sistema, que es lo que significa su sigla H-LAM/T: *Human using Language, Artifacts, Methodology, in which he is Trained*. Incluso cuando habla de «automated external symbol manipulation» lo describe como una etapa en la evolución intelectual humana, no como algo que compita con la persona. Y cuando toma prestado el término «intelligence amplification» aclara que no implica «any attempt to increase native human intelligence», sino «amplif[ying] the intelligence of the human by organizing his intellectual capabilities into higher levels of synergistic structuring»[^engelbart]. El contraste con el reemplazo lo agrego yo, sesenta años después, porque hoy hace falta y en 1962 no.

Hecha la salvedad, la crítica se sostiene: buena parte de lo que se construyó no aumenta, reemplaza. Y no es lo mismo. Una herramienta que te aumenta te deja más capaz cuando la apagás; una que te reemplaza te deja igual, o peor. El GPS es el ejemplo doméstico: llegás a destino, sí, pero no aprendiste la ciudad. Engelbart quería lo contrario: gente que, después de años de usar el sistema, pensara mejor.

**El criterio Licklider: simbiosis.** *Man-Computer Symbiosis*, de 1960[^lick], es el más modesto de los tres y por eso el más filoso. Licklider imaginaba un acoplamiento entre persona y máquina en el que cada parte hace aquello para lo que sirve, y el reparto lo deja escrito con todas las letras (sección 4): «Men will set the goals and supply the motivations […] formulate hypotheses […] think of mechanisms, procedures, and models […] define criteria and serve as evaluators», mientras que el equipo de procesamiento de información «will carry out the routinizable, clerical operations that fill the intervals between decisions»[^lick]. Una sociedad, no una servidumbre.

Lo que le da fuerza al planteo es que el dato de partida es autobiográfico, y es humillante. Licklider se cronometró a sí mismo y concluyó (sección 3.1): «About 85 per cent of my "thinking" time was spent getting into a position to think, to make a decision, to learn something I needed to know»[^lick]. Ese 85% —buscar, calcular, graficar, transformar— es exactamente la parte que le quiere dar a la máquina. No le está pidiendo que piense: le está pidiendo que le devuelva el tiempo de pensar.

La crítica es que la simbiosis quedó asimétrica. No en el sentido dramático de que las máquinas nos dominan, sino en uno más pedestre: el reparto de tareas que describía Licklider supone que la persona conserva la parte de los fines —los *goals*, las *motivations*, los *criteria* son suyos en las tres cláusulas. Cuando la máquina también propone los fines —qué mirar, qué leer, qué comprar, qué decir después— dejaste de tener una simbiosis y tenés una dependencia.

### Lo que sí cambió, y por qué no alcanza

Nada de esto niega lo obvio. Cambiaron tres cosas de manera brutal: la velocidad, el tamaño y la conectividad. Cualquier medida de esas tres da un número absurdo comparado con 1968.

El problema es el silogismo escondido: «cambió mucho, luego hubo una revolución». Pero un cambio de escala, por más grande que sea, es un cambio de escala. Miles de veces más rápido sigue siendo lo mismo, más rápido. La prueba está en el software: buena parte de lo que hace tu máquina hoy son las mismas ideas de los sesenta y setenta, corriendo sobre hardware inconcebiblemente mejor, y encima más lentas de lo que deberían. Bret Victor armó una charla entera sobre esto, *The Future of Programming*[^victor], parándose en 1973 y haciendo de cuenta que no sabe nada de lo que vino después; el chiste triste es que desde ese púlpito casi todo el presente parece un retroceso. [VERIFICAR: el año exacto en el que Victor se para para hacer la charla —1973— y el encuadre; está en el video de DBX 2013.]

Y hay una trampa peor, que es la que le interesaba a Neil Postman: que la tecnología no se suma a la cultura, la cambia entera. En *Technopoly*[^postman] el argumento es que una sociedad puede terminar entregándole a la técnica la potestad de decidir qué preguntas valen la pena. Si eso pasa, la escala no sólo no es revolución: es lo que te distrae de notar que la revolución no pasó.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste a la charla de Kay de 1997 —quién te la pasó, en qué año la viste, en qué estabas trabajando entonces— y qué fue lo primero que te molestó o te convenció al escucharla?

### ¿Y los LLMs?

Acá tengo que ser honesto con vos: este post no te va a dar el veredicto.

Todo lo que cité arriba se escribió entre 1960 y 2013. Ninguno de esos textos habla de lo que tenemos hoy, y no me parece serio usar a Kay como ventrílocuo para que diga lo que a mí me gustaría que dijera sobre una tecnología que no vio. Lo que sí se puede hacer —y es más útil— es pasar la cosa por las tres varas y dejar las preguntas planteadas:

- **Vara Kay.** ¿Es un medio nuevo o es una interfaz nueva a los medios viejos? Un medio nuevo tiene que dejarte construir y correr modelos que antes no podías. ¿Escribir en prosa lo que querés es construir un modelo, o es un modo más cómodo de pedir?
- **Vara Engelbart.** ¿Aumenta o reemplaza? La pregunta empírica es simple de enunciar y difícil de contestar: después de un par de años usándolo, ¿la persona quedó más capaz sin él, o menos?
- **Vara Licklider.** ¿Quién conserva la parte de los fines? Si la máquina hace el trabajo preparatorio y vos ponés los objetivos y los criterios, Licklider está sonriendo. Si además te sugiere el objetivo, no.

Fijate que ninguna de las tres preguntas se contesta con un benchmark. Todas se contestan mirando qué le pasa a la persona, que es exactamente el punto de los tres.

### Lo que Kay reconocería como progreso

Hay una pista sobre qué contaría como buena noticia para Kay, y no está en ningún producto. Kay pasó buena parte de su vida haciendo trabajar a chicos con computadoras —Smalltalk primero, Etoys después— y la razón no era enseñar a programar como salida laboral. Era que un chico de once años pudiera construir un modelo de la gravedad, correrlo, ver que está mal, y arreglarlo. Eso es tener un medio: podés tener una idea *dentro* del medio, no sólo sobre él. [VERIFICAR: el rol de Etoys y la franja de edad con la que trabajaba Kay — la bibliografía del draft (tr-01, tr-22) puede respaldar el punto sobre chicos y Smalltalk; si no, atribuirlo con más cuidado.]

Ese es el mismo motivo por el que Ted Nelson, en *Computer Lib / Dream Machines*[^nelson], escribía en la tapa que la gente tiene que entender las computadoras *ya*; y por el que Victor, en *Inventing on Principle*[^principio], insiste en que el creador tiene que ver de inmediato lo que está creando. Los tres están diciendo lo mismo desde ángulos distintos: la vara no es la potencia de la máquina, es cuánto de la máquina queda al alcance de la mano de una persona común.

> 🕳️ **HUECO — necesita a César:** ¿viste alguna vez a un chico —hijo, nieto, alumno— construir algo con una computadora y quedar cambiado por eso? Contame el caso en dos frases, o decime que no y lo saco.

> 🕳️ **HUECO — necesita a César:** en la digitalización que te tocó de cerca en el sector público de Santa Fe, ¿hubo algo que dejara a la gente efectivamente más capaz cuando vos te ibas (criterio Engelbart), o el resultado fue gente que dependía del sistema sin entenderlo? Un ejemplo concreto alcanza.

> 🕳️ **HUECO — necesita a César:** ¿tenés alguna máquina o sistema viejo en la memoria que hiciera algo que hoy, con todo el hardware que tenemos, no se puede hacer o se hace peor? Es el mejor argumento contra «escala = revolución» y tiene que ser tuyo, no un ejemplo de manual.

### No te voy a decir si llegó

Kay tenía otra costumbre que me gusta: no cerraba. En *Is «Software Engineering» an Oxymoron?*[^oximoron] —que es donde se mete con si lo nuestro es ingeniería o artesanía con pretensiones, y que da para otro post: [[C-01]]— el gesto es el mismo. Deja el criterio arriba de la mesa y te hace cargo del resto. Es coherente con el resto de su obra: hasta lo de «orientado a objetos», que él acuñó, se pasó décadas aclarando que casi nadie lo entendió como él lo pensaba[^oop].

Así que no. No te voy a decir si la revolución llegó, porque la respuesta depende enteramente de la vara, y elegir la vara es tu trabajo, no el mío. Lo que sí te dejo es la sospecha de que las varas fáciles —las que se miden en gigahertz, en usuarios, en valuación— no son varas. Son publicidad. Y las tres varas serias que dejaron Kay, Engelbart y Licklider tienen todas la misma forma rara: no preguntan qué puede hacer la máquina, preguntan en qué se convierte la persona que la usa.

Si querés el contraste práctico de todo esto, andá a [[D-04]]: Engelbart no escribió un manifiesto, hizo una demo. Y si te interesa qué dijo Kay exactamente y quién era, [[A1-01]].

> 🕳️ **HUECO — necesita a César:** ¿cuál es *tu* criterio? Si tuvieras que decir en una frase qué tendría que pasar para que vos aceptes que la revolución del cómputo ocurrió, ¿qué dirías? Es el remate del post y no lo puedo escribir yo.

[^kay97]: ver [[tr-01]] en el plan editorial — Alan Kay, *The Computer Revolution Hasn't Happened Yet*, keynote en OOPSLA 1997.
[^oximoron]: ver [[tr-21]] en el plan editorial — Alan Kay, *Is «Software Engineering» an Oxymoron?*, apéndice B de *Croquet: The User Manual*, draft 0.1, octubre 2002.
[^oop]: ver [[tr-22]] en el plan editorial — discusiones consolidadas sobre lo que Kay quiso decir con «orientado a objetos».
[^dynabook]: [Alan Kay y Adele Goldberg, *Personal Dynamic Media*, IEEE Computer, 1977](http://www.newmediareader.com/book_samples/nmr-26-kay.pdf) — el texto original del Dynabook.
[^engelbart]: [Douglas Engelbart, *Augmenting Human Intellect: A Conceptual Framework*, SRI 1962](https://www.dougengelbart.org/content/view/138/).
[^lick]: [J.C.R. Licklider, *Man-Computer Symbiosis*, IRE Transactions on Human Factors in Electronics, 1960](https://groups.csail.mit.edu/medg/people/psz/Licklider.html).
[^victor]: [Bret Victor, *The Future of Programming*, DBX 2013](https://vimeo.com/71278954).
[^principio]: [Bret Victor, *Inventing on Principle*, CUSEC 2012](https://vimeo.com/36579366).
[^nelson]: [Ted Nelson, *Computer Lib / Dream Machines*, 1974](https://archive.org/details/computer-lib-dream-machines).
[^postman]: [Neil Postman, *Technopoly: The Surrender of Culture to Technology*, Knopf 1992](https://archive.org/details/technopolysurren00post).

