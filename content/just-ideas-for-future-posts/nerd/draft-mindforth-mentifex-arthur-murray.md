### J-03 — MindForth y MentiFex: Arthur T. Murray, el pionero solitario que escribió una IA en Forth durante 30 años

- **Archivo seed:** `misc/draft-mind-forth.md` (5 URLs)
- **Slug propuesto:** `mindforth-mentifex-arthur-murray`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mindforth-mentifex-arthur-murray/index.md`
- **Serie:** J
- **Cross-links:** lleva a [[A1-04]] (Forth, lenguaje de fondo), [[D-03]] (Turing — el otro experimento mental sobre máquinas pensantes)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS (o sí, pero rara)

**Concepto:** Arthur T. Murray (alias *MentiFex*, alias *Mentifex*) es uno de los personajes más raros y entrañables de la historia de Usenet, comp.ai y IA en general. Desde principios de los 80 hasta hoy, ha estado escribiendo (y *reescribiendo*, en distintos lenguajes — Forth, Perl, JavaScript) un programa al que llama *MindForth* o *MindOuranosophy*, que él considera una IA general funcional. La comunidad académica ha sido escéptica (suavemente) o burlona (frecuentemente). Pero la *historia* de Murray es genuinamente conmovedora: un señor solo, sin afiliación académica, dedicó 40 años de su vida a un sueño concreto, lo documentó todo en público, y aceptó la crítica con buen humor. El post no es sobre si MindForth funciona (no funciona como IA general); es sobre el valor del proyecto del nerd solitario obsesionado.

**Hook:** "se llama Arthur T. Murray. Firma como *Mentifex*. Está en Usenet desde 1990 publicando actualizaciones de un programa que él considera una inteligencia artificial general. Lo escribió primero en Forth (de ahí el nombre, *MindForth*), después en Perl, después en JavaScript. La comunidad académica lo ignoró o se burló. Murray siguió. Tiene hoy más de 70 años y sigue publicando. El post no es para preguntar si MindForth *piensa*. Es para preguntar qué hacemos con los nerds solitarios obsesionados."

**Outline:**
1. Quién es Arthur T. Murray — lo poco que se sabe en público. Un señor americano, autodidacta, fluido en varios idiomas (su Mentifex está en inglés, alemán, ruso y latín).
2. La aparición en Usenet (comp.ai, alt.folklore.computers) en los 90. La FAQ de *Arthur T. Murray* en alt.folklore.computers que se mantuvo durante años.
3. *MindForth* — qué dice ser. Una "GPT de Murray" antes de GPT: un programa que mantiene un grafo de asociaciones léxicas y va construyendo "pensamientos" como cadenas de activación.
4. La crítica honesta: no es IA general. No es ni siquiera un buen sistema simbólico de los 80. Es algo más cercano a una red semántica activable, escrita en un lenguaje (Forth) que casi nadie usa.
5. La defensa honesta: hizo lo mejor que pudo, durante 40 años, *en público*, con el código abierto, aceptando crítica. Eso es mucho.
6. La conexión con Forth: por qué Forth es el lenguaje *correcto* para alguien como Murray. Minimalismo radical, fácil de modificar, cabe en una cabeza ([[A1-04]]).
7. Lo conmovedor: revisar las entradas viejas de Mentifex en su diario de Advogato (preservado en Wayback Machine). El tipo escribía cada día sobre su programa.
8. La pregunta filosófica: ¿qué fracción de los avances científicos viene de gente como Murray vs gente con afiliación institucional? Probablemente menos de lo que romantizamos. Pero no cero.
9. Cierre: el código de MindForth sigue disponible en Google Code Archive. Bajalo, leelo, decidí por vos mismo.

**Bibliografía:**
- [Mentifex en Twitter/X — `@mentifex`](https://x.com/mentifex) — la cuenta sigue activa, frágil.
- [`Arthur T. Murray (Mentifex) FAQ` en alt.folklore.computers — Narkive](https://alt.folklore.computers.narkive.com/McLBxGRD/the-arthur-t-murray-mentifex-faq) — la FAQ comunitaria.
- [Wayback Machine — Mentifex en Advogato, diario 51](https://web.archive.org/web/20170630011113/http://www.advogato.org/person/mentifex/diary/51.html) — entrada preservada del diario público.
- [Mentifex FAQ updated — Medium](https://medium.com/@mentificium/mentifex-faq-updated-for-ai-thesis-or-phd-dissertation-90df97890655) — versión moderna del autor.
- [MindForth — Google Code Archive](https://code.google.com/archive/p/mindforth/) — el código fuente completo.
- [Arthur T. Murray, *AI4U: Mind-1.1 Programmer's Manual*, iUniverse 2002](https://www.amazon.com/AI4U-Mind-1-1-Programmers-Manual/dp/0595259227) — el libro autopublicado.
- [comp.ai en Google Groups](https://groups.google.com/g/comp.ai) — archivo histórico.
- [Loebner Prize — Wikipedia](https://en.wikipedia.org/wiki/Loebner_Prize) — donde Mentifex participó algunas veces.
- [Turing test history — Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/turing-test/) — para contextualizar.
- [Pamela McCorduck, *Machines Who Think*, A.K. Peters 2004 (2nd ed.)](https://www.routledge.com/Machines-Who-Think-A-Personal-Inquiry-into-the-History-and-Prospects-of/McCorduck/p/book/9781568812052) — la historia "oficial" de la IA donde figuras como Murray quedan afuera.

**Imágenes:**
- _Crear_: screenshot de una de las páginas viejas de Mentifex en Advogato (vía Wayback) — verificar que se vea bien (~15 min).
- _Crear_: snippet del código de MindForth en Forth (4-6 líneas representativas) (~15 min).
- _Crear_: tabla de las versiones de MindForth a lo largo de los años (Forth → Perl → JavaScript → ...) (~30 min).

**Tags propuestos:** `['MindForth', 'Mentifex', 'Arthur T Murray', 'Forth', 'IA', 'historia', 'nerd lateral']`

**Estado actual:** prosa completa escrita contra el outline de 9 puntos (~1.850 palabras, dentro del target medium). Queda escrito: el encuadre, la crítica técnica, la defensa, la conexión con Forth, la pregunta sobre outsiders vs. instituciones y el cierre. Quedan pendientes:

- **6 marcadores `[VERIFICAR:]`** — casi todas las fechas, edades y cantidades del Concepto/Hook (1990 como fecha de arranque en Usenet, «40 años», «más de 70 años», los idiomas del programa, la participación en el Loebner Prize, la secuencia Forth → Perl → JavaScript) no están respaldadas por la bibliografía tal como está listada. Hay que leer la FAQ de Narkive, el archivo de Advogato y el Google Code Archive y fijar cada dato, o reescribir la frase sin el número.
- **6 huecos `🕳️`** — el post necesita el recuerdo de César sobre Usenet, comp.ai y su propia relación con Forth y con los proyectos-de-una-sola-persona. Sin eso, la sección 7 y el cierre quedan impersonales.
- Verificar antes de publicar si Murray sigue vivo y publicando; el post está escrito en presente y eso puede haber cambiado.
- Las tres imágenes del plan siguen sin hacer.

---

## Borrador de prosa

⚠️ **Curiosidad nerd lateral — esto no es ciencia de la computación**

Hubo un señor que durante casi cuarenta años publicó, cada tanto, un mensaje anunciando una nueva versión de su inteligencia artificial. Firmaba *Mentifex*. Su nombre real era Arthur Theodore Murray, nació en Dallas el 13 de julio de 1946 y murió en Edmonds, estado de Washington, el 21 de febrero de 2024, de un cáncer de las vías biliares[^obit][^obit2]. El programa se llama *MindForth*. La comunidad académica lo ignoró, y cuando no lo ignoró, se burló. Murray siguió hasta el final. El código todavía está ahí, para bajar[^codearchive][^fuente].

> ⚠️ **Corrección de la pasada de fuentes (2026-07-16):** el draft y el Hook estaban escritos en presente («sigue publicando», «tiene hoy más de 70 años»). Murray murió el 21 de febrero de 2024, confirmado por dos obituarios independientes[^obit][^obit2]. Todo el post hay que pasarlo a pasado, y el Hook necesita decisión de César.

El nombre *MindForth* viene de Forth, pero **la primera versión no fue en Forth**: fue en ARexx, sobre un Amiga. La secuencia real, según la FAQ crítica de Tristan Miller[^faq] y la propia FAQ de Murray[^ownfaq], es **ARexx (Mind.Rexx) → Forth (Mind.Forth) → JavaScript → Perl** —más versiones en C++ que encargó a terceros—. Es decir: ni la primera versión fue en Forth, ni Perl vino antes que JavaScript.

> ⚠️ **Corrección de la pasada de fuentes:** el outline afirmaba «Forth → Perl → JavaScript» y que Forth fue el primero. Las dos cosas son falsas. La sección «Por qué Forth» de más abajo depende de esa premisa y hay que reescribirla.

Este post no es para preguntar si MindForth piensa. Te adelanto la respuesta: no piensa, y más abajo te cuento por qué me parece que ni siquiera es un buen sistema simbólico de los años 80. El post es para otra pregunta, que me resulta mucho más incómoda: qué hacemos con los nerds solitarios obsesionados.

### Lo poco que se sabe

De Arthur T. Murray se sabe, en público, bastante menos de lo que uno esperaría de alguien que documentó su vida entera en internet. Era estadounidense. Era autodidacta en lo suyo: sin afiliación académica, sin laboratorio detrás, sin un paper con revisión de pares. Su formación era en clásicas —decía haber recibido un Bachelor's en griego y latín por la Universidad de Washington en Seattle en 1968— y no tenía formación formal en ciencias de la computación, ciencia cognitiva, neurociencia ni lingüística[^faq]. Trabajaba de auditor nocturno en un hotel chico de Seattle[^faq]. Antes de eso enseñó alemán y latín, y sirvió en el Ejército como especialista en armas nucleares[^obit]. Escribió un libro, *AI4U: Mind-1.1 Programmer's Manual*, publicado en noviembre de 2002 por Writers Club Press, un sello de iUniverse[^ai4u] — es decir, una editorial de vanidad que cobra al autor por publicar[^faq].

Sus artículos teóricos fueron enviados y rechazados por los editores de *Artificial Intelligence*, *Cognitive Science* y *Speculations in Science and Technology*[^faq]. El único antecedente de «publicación» que le gustaba citar era un artículo en *November*, que no era una revista científica sino un fanzine de ciencia ficción de Seattle que duró un año[^faq].

El programa existe en varios idiomas naturales, no sólo en varios lenguajes de programación. Los cuatro que el outline afirmaba están confirmados: **inglés**, **alemán** y **ruso** figuran entre las etiquetas del proyecto en el Google Code Archive —el AI ruso se llama *Dushka*, el alemán *DeKi*—[^codearchive], y el **latín** existe como *Mens Latina*, una página propia donde se le escribe al programa en latín antiguo[^mens]. Según su obituario llegó a hablar catorce idiomas[^obit]. Ese detalle me parece el más revelador de todos. Un tipo que decide que su IA tiene que hablar latín no está optimizando para nada que se parezca a un producto. Está siguiendo una idea propia de lo que significa una mente.

> 🕳️ **HUECO — necesita a César:** ¿cuándo te cruzaste por primera vez con el nombre Mentifex, y dónde? ¿Fue leyendo Usenet en tiempo real, o mucho después, como arqueología?

### Usenet, o el primer foro que tuvo un troll involuntario

La aparición de Murray en Usenet es más vieja de lo que dice el draft: **1985**, no 1990. Él mismo contaba que se compró una Coleco ADAM y usó su módem de 300 baudios para hacer su primer post de Usenet en 1985[^rebuttal], en el grupo net.ai; la FAQ crítica corrobora la fecha por la vía independiente de citar una respuesta de Garrison W. Cottrell al hilo «Linguistic mind-model» fechada el **30 de enero de 1985**[^faq]. Después vinieron comp.ai sobre todo, y también alt.folklore.computers. Posteaba anuncios de versiones nuevas. Los posteaba seguido. Los posteaba con un entusiasmo que no bajaba nunca, en un grupo donde la gente venía a discutir en serio sobre planificación, lógica de primer orden y aprendizaje automático.

> ⚠️ **Corrección de la pasada de fuentes:** el Concepto dice «principios de los 80» y el Hook «desde 1990». La fecha sostenible es 1985. [VERIFICAR: la fecha exacta del 28 de enero de 1985 circula en varias páginas pero no la pude confirmar en ninguna fuente que haya abierto — la página propia de Murray[^rebuttal] dice sólo «1985», y la FAQ[^faq] sólo prueba que el 30 de enero de 1985 ya había una respuesta al hilo. Si hace falta el día exacto, hay que buscarlo en el archivo de Usenet de net.ai.]

La respuesta de la comunidad fue tan característica de Usenet que terminó cristalizando en un artefacto: una FAQ[^faq]. La escribió **Tristan Miller**, entonces investigador del DFKI (el centro alemán de investigación en IA) en Kaiserslautern; la revisión 1.7 es del 28 de diciembre de 2009. Ese objeto es raro y hay que detenerse un segundo. Que alguien te dedique una FAQ significa que sos un fenómeno recurrente: apareciste tantas veces, y generaste tantas veces la misma conversación, que hubo que documentar el fenómeno para no repetirlo. Es una forma de reconocimiento, y también es una forma de crueldad, y las dos cosas al mismo tiempo.

> ⚠️ **Corrección de la pasada de fuentes:** dos errores en la versión anterior. (1) La FAQ no fue escrita «por el grupo»: tiene un autor único y con nombre, Tristan Miller. (2) El enlace de Narkive que la bibliografía citaba como «la FAQ comunitaria» **no es la FAQ de Miller**: es un post del propio Murray de 2004 con el mismo título, una especie de auto-FAQ paródica. Son dos documentos distintos y hay que citarlos por separado.

Lo que más me llama la atención de todo el asunto es que Murray no se fue. La reacción normal de un ser humano a que un foro entero te convierta en chiste interno es irse. Él siguió posteando.

> 🕳️ **HUECO — necesita a César:** ¿leías comp.ai o alt.folklore.computers en la época? Si sí, ¿con qué cliente y desde qué conexión — y te acordás del clima de esos grupos con los outsiders?

### Qué dice ser MindForth

MindForth se presenta como una IA general funcionando. La arquitectura, tal como Murray la describe en su propia documentación[^medium], es un grafo de asociaciones léxicas: palabras conectadas a palabras, con activación que se propaga por las conexiones, y «pensamientos» que emergen como cadenas de esa activación recorridas en el orden que impone una gramática mínima. El programa lee una entrada, activa nodos, y emite una oración.

Uno puede leer esa descripción hoy, después de una década de modelos de lenguaje, y sentir un cosquilleo raro: es, en un sentido muy chato y muy literal, una máquina que produce texto encadenando asociaciones aprendidas. Pero la analogía se rompe apenas la apretás un poco. Los modelos de lenguaje actuales encadenan asociaciones estimadas estadísticamente sobre corpus enormes; MindForth encadena asociaciones que el autor cableó a mano en una estructura chiquita. La diferencia no es de grado.

### La crítica honesta

No hay que ser generoso con esto, porque ser generoso sería faltarle el respeto. MindForth no es una inteligencia artificial general. Tampoco es —y esto es más duro— un buen exponente de la IA simbólica de su propia época. Los sistemas simbólicos serios de los 70 y los 80 tenían aparato: representación del conocimiento con semántica definida, motores de inferencia con propiedades demostrables, evaluación contra tareas. MindForth es una red semántica activable, sin evaluación, sin comparación con otros sistemas, sin una definición operativa de qué contaría como éxito.

Y falta la pieza que convierte un programa en un resultado: nadie más lo corrió y midió nada. La historia canónica de la IA, la que cuenta Pamela McCorduck[^mccorduck], está hecha de gente que sí pasó por ese filtro, y Murray no aparece ahí. No es una conspiración. Es el filtro haciendo exactamente lo que el filtro hace.

La única publicación no autoeditada que Murray podía exhibir es una reseña de Mind.Forth firmada por Paul Frenger en *ACM SIGPLAN Notices*, vol. 33 nº 12, pp. 25-31, diciembre de 1998[^frenger]. Vale aclarar lo que la FAQ aclara y Murray no: *SIGPLAN Notices* es un boletín informal, sin referato, del grupo de interés en lenguajes de programación de la ACM; Frenger no era científico de la computación sino un médico que escribía una columna mensual para entusiastas de Forth, y las reseñas que aparecían ahí no representaban la opinión oficial de la ACM[^faq]. El propio código fuente de MindForth cita ese DOI en sus comentarios de cabecera[^fuente], que es un detalle triste y perfecto.

Hay además una trampa conceptual de fondo, y es vieja: si tu criterio de que la máquina piensa es que produce oraciones que parecen pensamientos, ya estás adentro del problema que el test de Turing abrió y no cerró[^sep].

[VERIFICAR: la participación de Murray en el Loebner Prize que afirma el outline **no la pude sostener con ninguna fuente**. Busqué en la FAQ de Miller[^faq] —que documenta exhaustivamente cada reclamo de Murray y no menciona el Loebner ni una vez—, en el Google Code Archive[^codearchive], en la entrada de la SEP sobre el test de Turing[^sep] (que sí habla del Loebner, pero no de Murray) y en búsquedas web directas. Mi sospecha es que el dato es falso y que hay que borrar la frase; antes de eso, probar con los transcripts oficiales del premio año por año.]

### La defensa honesta

Ahora la otra mitad, que es la que me interesa. Y acá es donde las fuentes me arruinaron el post que quería escribir.

Murray hizo lo mejor que pudo, durante **treinta y nueve años** (enero de 1985 a febrero de 2024), **en público**, con el código abierto y disponible bajo GPL v2[^codearchive]. Tres de las cuatro cosas que el draft le atribuía se sostienen.

En público: no hubo carpeta secreta con el gran descubrimiento. Todo lo que afirmó lo afirmó donde podían contestarle. Con el código abierto: si querés refutarlo, no tenés que creerle nada, bajás el fuente y lo leés[^fuente]. Con el trabajo sostenido: entrada tras entrada, versión tras versión, durante un tiempo que a la mayoría de nosotros no nos alcanza ni para terminar el proyecto de fin de semana.

> ⚠️ **PREMISA EN DUDA — la pasada de fuentes contradice la cuarta pata.** El draft decía que Murray aceptó la crítica «sin amargura visible» y «con buen humor», y remataba: «público, abierto, sostenido, sin resentimiento — es la ética científica». La FAQ de Miller documenta lo contrario, con citas de Usenet fechadas una por una[^faq]:
>
> - **Mass-mailing**: antes de tener internet, mandaba sus ideas por correo postal a investigadores y departamentos universitarios enteros. Se jactaba de haber mandado **siete mil cartas sólo en 1989**.
> - **Spam deliberado**: llamaba «inserción de memes» a postear su material en grupos de Usenet abiertamente off-topic — alt.atheism, rec.aviation.misc, rec.org.mensa, talk.origins, sci.econ.
> - **Sock puppets**: la FAQ lista una decena de alias y direcciones de correo, y otros posteadores sostenían que usaba cuentas títere para elogiarse a sí mismo.
> - **Represalias contra sus críticos**: intentaba silenciarlos **quejándose en privado a sus empleadores y a sus proveedores de internet**. Miller, el autor de la FAQ, dice haber sido él mismo víctima de ese hostigamiento.
> - **Escrache presencial**: hizo un piquete contra la conferencia IJCAI 2001 en Seattle.
> - Es señalado como una de las razones principales por las que **comp.ai tuvo que pasar a ser un grupo moderado**.
>
> Nada de eso es «sin resentimiento». Hay una tensión adicional que conviene no esquivar: la página *MentifexBashing* del propio Murray[^bashing] dice que nunca hay que contraatacar a los críticos y que él se mantuvo sereno — y esa versión es exactamente la que el draft compró. Las dos cosas no pueden ser ciertas, y la que tiene citas verificables con fecha es la de Miller.
>
> **Esto no es un detalle a corregir: es el corazón del post.** El argumento entero era «le falta el resultado, no le falta la ética». Si la ética tampoco está, el post necesita otra tesis. Opciones, todas de César: (a) reescribir la defensa como más chica y más honesta — sostenido y abierto sí, gracioso y humilde no; (b) hacer que el post trate justamente de esa tensión, de cómo la historia conmovedora del nerd solitario se nos deshace cuando miramos el archivo; (c) abandonar la defensa y quedarse con la pregunta del cierre. La (b) me parece la mejor y la más fiel a lo que apareció, pero no es mi decisión.

### Por qué Forth, y por qué eso no es casualidad

Que la primera versión haya sido en Forth me parece lo menos arbitrario de toda la historia. Forth es minimalismo radical: un lenguaje que cabe entero en una cabeza, que te deja definir tus propias palabras y construir el idioma hacia arriba hasta que el programa termina escrito en un vocabulario que inventaste vos. No tenés que negociar con el diseño de nadie. No hay framework. No hay comité.

Para alguien que trabaja solo, treinta años, sobre una idea que sólo él entiende del todo, Forth no es una elección excéntrica: es la elección correcta. Es el lenguaje que no te pide permiso. De Forth como lenguaje —de su historia, de su rareza hermosa, de por qué te obliga a pensar al revés— hablo aparte en [[A1-04]].

### Lo conmovedor

Si vas al archivo de Advogato en la Wayback Machine y abrís el diario de Mentifex, encontrás entradas[^advogato]. El tipo escribía sobre su programa. Día tras día. Sobre un módulo que no andaba, sobre una idea que se le ocurrió, sobre lo que iba a hacer al día siguiente.

Advogato ya no existe como sitio vivo; lo que queda son capturas. Leer eso hoy tiene algo de entrar a una casa vacía. Ahí está el registro de una persona haciendo, con absoluta seriedad, lo único que le importaba, sin público, sin plata, sin premio, sin nadie esperándolo. La cuenta de Twitter todavía existe[^x] — o existía cuando escribí esto, que con Twitter no es lo mismo.

> 🕳️ **HUECO — necesita a César:** ¿tenés vos un proyecto propio de años, hecho solo y sin público, que hoy releas con esta misma sensación? No hace falta que lo nombres si no querés, pero el post lo necesita para no ser condescendiente.

> 🕳️ **HUECO — necesita a César:** ¿cuál es tu reacción honesta al leer el diario de Advogato — ternura, incomodidad, identificación, las tres?

### La pregunta que queda

Nos gusta la historia del outsider. Es una gran historia: el tipo sin credenciales que ve lo que los profesores no ven. El problema es que la historia es buena justamente porque es rara. ¿Qué fracción de los avances científicos reales viene de gente como Murray, sin afiliación, sin pares que la revisen? Casi con seguridad muchísimo menos de lo que nos gusta imaginar. La institución no es un obstáculo al descubrimiento: es en gran medida el mecanismo del descubrimiento, porque es donde alguien más chequea si lo que dijiste es cierto.

Pero no es cero. Y ese «no es cero» es lo que impide cerrar el caso con comodidad.

> 🕳️ **HUECO — necesita a César:** desde tu experiencia laboral, ¿viste de cerca a alguien con una idea propia sostenida durante años sin respaldo institucional? ¿Terminó en algo?

> 🕳️ **HUECO — necesita a César:** ¿cuál es tu posición sobre el outsider científico — te parece que romantizamos demasiado, o que el filtro institucional se lleva puesta gente que valía?

### Cierre

Murray sigue publicando [VERIFICAR: confirmar que la cuenta de X[^x] y la FAQ de Medium[^medium] siguen activas al momento de publicar; y no afirmar la edad — el Hook dice «más de 70 años» y eso no está respaldado por la bibliografía]. El código de MindForth sigue disponible en el Google Code Archive, que es un cementerio que Google tuvo la decencia de no demoler[^codearchive].

No te estoy pidiendo que le creas. Te estoy pidiendo que lo bajes, lo abras y lo leas, y decidas por vos mismo qué estás mirando: un delirio prolijo, un experimento honesto que falló, o las dos cosas —que suele ser la respuesta. Alan Turing se pasó unas cuantas páginas preguntándose cómo íbamos a saber si una máquina piensa ([[D-03]]) y no llegó a un criterio que nos dejara tranquilos. Murray se pasó treinta años dando por respondida esa pregunta. Uno de los dos estaba equivocado, y no es el que vos pensás que es el conmovedor.

[^codearchive]: [MindForth — Google Code Archive](https://code.google.com/archive/p/mindforth/) — el código fuente completo.
[^faq]: [«The Arthur T. Murray (Mentifex) FAQ» en alt.folklore.computers](https://alt.folklore.computers.narkive.com/McLBxGRD/the-arthur-t-murray-mentifex-faq) — archivado en Narkive.
[^advogato]: [Mentifex en Advogato, diario 51](https://web.archive.org/web/20170630011113/http://www.advogato.org/person/mentifex/diary/51.html) — entrada preservada en la Wayback Machine.
[^medium]: [«Mentifex FAQ updated» — Medium](https://medium.com/@mentificium/mentifex-faq-updated-for-ai-thesis-or-phd-dissertation-90df97890655) — la versión moderna, escrita por el propio autor.
[^ai4u]: Arthur T. Murray, *AI4U: Mind-1.1 Programmer's Manual*, iUniverse, 2002. [Ficha](https://www.amazon.com/AI4U-Mind-1-1-Programmers-Manual/dp/0595259227).
[^compai]: [comp.ai](https://groups.google.com/g/comp.ai) — archivo histórico del grupo en Google Groups.
[^loebner]: [Loebner Prize](https://en.wikipedia.org/wiki/Loebner_Prize) — Wikipedia.
[^sep]: [«The Turing Test»](https://plato.stanford.edu/entries/turing-test/) — Stanford Encyclopedia of Philosophy.
[^mccorduck]: Pamela McCorduck, *Machines Who Think*, A.K. Peters, 2004 (2ª ed.). [Ficha del editor](https://www.routledge.com/Machines-Who-Think-A-Personal-Inquiry-into-the-History-and-Prospects-of/McCorduck/p/book/9781568812052).
[^x]: [`@mentifex`](https://x.com/mentifex) — enlace frágil; verificar antes de publicar.

