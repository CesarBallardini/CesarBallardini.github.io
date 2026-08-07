### A1-01 — Alan Kay y la revolución del cómputo que todavía no llegó

- **Archivo seed:** `dev/draft-alan-kay-the-computer-revolution.md`
- **Slug propuesto:** `alan-kay-revolucion-no-llego`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-alan-kay-revolucion-no-llego/index.md` (page bundle, lleva imágenes)
- **Serie:** A1 — cross con Serie C ([[C-05]] es el mismo seed con ángulo filosófico)
- **Cross-links:** depende de [[tr-01]]; lleva a [[A2-01]] (SICP), [[C-01]] (oxymoron), [[C-05]] (revolución como crítica)
- **Idioma:** es+en (perfecto para inaugurar `content/en/posts/`, usar `translationKey: 'kay-revolution'`)
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1200-1800 palabras)

**Concepto:** la "revolución del cómputo personal" que Kay imaginó (y por la que trabajó en Xerox PARC) jamás ocurrió como él la describió. Tenemos máquinas más rápidas, pero la idea de la computadora como medio para *amplificar el pensamiento humano* sigue pendiente.

**Hook:** abrir con la cita "the computer revolution hasn't happened yet" en pantalla negra, y después contar la trampa: la dijo en 1997, hace casi 30 años, y sigue siendo cierta. Smartphones más potentes que las Cray no nos hicieron pensar mejor.

**Outline:**
1. Quién es Kay (Smalltalk, Xerox PARC, ARPA, la idea del Dynabook).
2. La keynote de OOPSLA 1997: contexto de cuándo se dió y por qué impactó.
3. Los tres puntos de Kay sobre qué *sería* una revolución (medios para pensar, programación end-user, late binding extremo).
4. Por qué no pasó: incentivos de la industria, complejidad acumulada, optimización local.
5. Croquet, Etoys, Squeak — los intentos de Kay por hacer la cosa como él la quería.
6. Cierre: ¿qué reconocería Kay hoy como un avance hacia la revolución? Spec: probablemente nada, y eso es importante.

**Bibliografía:** (reforzada el 2026-07-16; cada fuente marcada estable/frágil se verificó por fetch)

- [[tr-01]] — Kay, *The Computer Revolution Hasn't Happened Yet*, keynote de OOPSLA '97 (12.ª ACM SIGPLAN OOPSLA, Atlanta, 5-9 de octubre de 1997 — evento y año confirmados por el título del vídeo y por la transcripción). Vídeo: [YouTube `oKg1hTOQXoY`](https://www.youtube.com/watch?v=oKg1hTOQXoY) — **frágil**; hay backup en [Internet Archive](https://archive.org/details/AlanKayAtOOPSLA1997TheComputerRevolutionHasntHappenedYet). Transcripción de texto en el archivo de Viewpoints Research (el instituto de Kay): [tinlizzie.org](https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet) — **estable** (wiki del instituto; conviene guardar copia en Wayback antes de publicar).
- [[tr-21]] — Kay, *Is "Software Engineering" an Oxymoron?* — apéndice B de *Croquet: The User Manual*, draft 0.1, octubre de 2002. [PDF en Wayback Machine](http://web.archive.org/web/20030407181600/www.opencroquet.org/downloads/Croquet0.1.pdf) — **estable** (ya archivado).
- [[tr-22]] — hilos consolidados en [Reddit r/programming](https://www.reddit.com/r/programming/comments/bpb5v6/alan_kay_on_his_original_thoughts_when_he_came_up/) y [Software Engineering SE](https://softwareengineering.stackexchange.com/questions/46592/so-what-did-alan-kay-really-mean-by-the-term-object-oriented) sobre qué quiso decir Kay con OOP — **frágil** (agregadores). Ojo: la cita canónica del «extreme late-binding» proviene del correo de Kay a Stefan Ram (2003), **no** de esta keynote.
- Kay, *The Early History of Smalltalk* — **ACM SIGPLAN Notices**, vol. 28, n.º 3 (marzo de 1993), actas de HOPL-II. DOI [10.1145/155360.155364](https://doi.org/10.1145/155360.155364) (metadatos verificados en Crossref: título, autor, revista, volumen, número y año). Mirror libre de texto completo: [worrydream.com](http://worrydream.com/EarlyHistoryOfSmalltalk/) — **estable**.
- Kay, *A Personal Computer for Children of All Ages* — presentado en la **ACM National Conference**, Boston, agosto de 1972 (documento de Xerox PARC). [PDF](http://www.mprove.de/diplom/gui/Kay72a.pdf) — **frágil** (sitio personal mprove.de; conviene backup en Wayback). Título y autor confirmados por fetch; las especificaciones concretas del Dynabook no se pudieron leer del PDF (contenido escaneado/binario).
- [Bret Victor, *A Brief Rant on the Future of Interaction Design*](http://worrydream.com/ABriefRantOnTheFutureOfInteractionDesign/) — heredero filosófico de Kay. **Estable**.
- Croquet: [Croquet Project en Wikipedia](https://en.wikipedia.org/wiki/Croquet_Project) (**estable**) y [OpenCroquet en c2 wiki](https://wiki.c2.com/?OpenCroquet) (**frágil**).

**Imágenes:**
- _Wikimedia_: foto de Alan Kay — [Alan Kay (cropped)](https://commons.wikimedia.org/wiki/File:Alan_Kay2.jpg) — license: CC-BY-SA 4.0 (Marcin Wichary).
- _Wikimedia_: la maqueta del Dynabook — [Dynabook mockup](https://commons.wikimedia.org/wiki/File:Alan_Kay_and_the_prototype_of_Dynabook,_pt._5_(3010032738).jpg) — license: CC-BY 2.0.
- _Crear_: ninguno necesario.

**Tags propuestos:** `['Alan Kay', 'OOPSLA', 'Smalltalk', 'Dynabook', 'Xerox PARC', 'historia']`

**Estado actual:** prosa completa escrita al outline (~1550 palabras, dentro del target medium), en la sección «Borrador de prosa» al final de este archivo. Fuentes originales recolectadas en `draft-alan-kay-the-computer-revolution.md` y en `draft-rest.md` (líneas 8-21).

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 2 de 8 marcadores `[VERIFICAR:]`: el papel de Kay en ARPA/ARPANET (con cita textual de la transcripción de la keynote) y las fechas de Croquet (Wikipedia). Se agregaron/confirmaron: el DOI de *The Early History of Smalltalk* (10.1145/155360.155364, Crossref → SIGPLAN Notices 28(3), 1993), la transcripción de texto de la keynote en tinlizzie.org y un backup del vídeo en Internet Archive.

⚠️ PREMISA EN DUDA (hallazgo del 2026-07-16): la transcripción de la keynote alojada en el propio instituto de Kay (tinlizzie.org) **no contiene** las palabras «print/printing/press/Gutenberg/paper/medium/media/late binding/end-user»; el borrador de moryton.blogspot.com tampoco muestra la analogía de la imprenta. Es decir: la analogía Gutenberg (§«Qué quiso decir con revolución» y cierre), los «tres ejes» (medio para pensar / programación de usuario final / late binding extremo) y el «late binding» atribuido a la keynote **no aparecen en las transcripciones que se pudieron leer**. Puede que las transcripciones estén incompletas, así que los marcadores correspondientes se dejaron **sin resolver**; antes de publicar hay que mirar el vídeo de [[tr-01]] con el reloj a la vista para confirmar o descartar cada uno. Si el vídeo tampoco los tiene, hay que reescribir esas secciones alrededor de lo que Kay efectivamente dice.

Qué quedó escrito: el arco completo — hook con la cita, quién es Kay, encuadre de la keynote de OOPSLA 1997, los tres ejes de qué sería una revolución, el diagnóstico de por qué no pasó, Croquet como intento, y el cierre.

Qué quedó como hueco:

- **7 huecos `🕳️`** — todos piden recuerdo, opinión o dato biográfico de César: qué máquina tenía en 1997 y qué escribía en ella; si vio la keynote y cuándo/cómo llegó a ella; si tocó Smalltalk/Squeak alguna vez y con qué resultado; si vio en la STG o en el Ministerio de Cultura de Santa Fe a un usuario final construirse su propia herramienta; el caso de la planilla de cálculo como única programación end-user que sobrevivió; su veredicto personal sobre si la revolución llegó; y el cierre en primera persona.
- **8 marcadores `[VERIFICAR:]` originales, 6 aún sin resolver tras la pasada del 2026-07-16** — el grueso cae sobre el contenido de la keynote misma: el outline afirma que Kay articula «tres puntos» (medios para pensar, programación end-user, late binding extremo) y la bibliografía no lo respalda, así que cada uno de los tres ejes está escrito con su marcador pidiendo timestamp en [[tr-01]]; a esos tres se suma la analogía de la imprenta. Las transcripciones consultadas el 2026-07-16 **no** los muestran (ver la nota ⚠️ de arriba), pero como pueden estar incompletas los marcadores se dejaron. También siguen marcados: los detalles del Dynabook de 1972 más allá del título del paper (el prose no afirma ninguno a propósito) y la relación Squeak/Etoys con Croquet (Squeak y Etoys **no están en la bibliografía**). **Resueltos:** la afiliación de Kay a ARPA (cita textual de la transcripción) y las fechas de Croquet (Wikipedia).

Antes de publicar, la tarea número uno es **mirar el vídeo de [[tr-01]] con el reloj a la vista** y resolver los marcadores de la sección de los tres ejes; si la keynote no está organizada como el outline supone, hay que reescribir esa sección alrededor de lo que Kay efectivamente dice, no al revés.

Pendiente adicional: decidir si el par en inglés (`translationKey: 'kay-revolution'`) se escribe en la misma pasada; el post cita un vídeo en inglés y una cita famosa en inglés, así que la versión EN es casi gratis una vez cerrada la ES.

---

## Borrador de prosa

> «The computer revolution hasn't happened yet.»

Es el título de una keynote que Alan Kay dio en OOPSLA en 1997.[^kay-oopsla] La trampa está en la fecha. No la dijo un pesimista de café en un hilo de foro la semana pasada: la dijo hace veintinueve años el tipo que ayudó a inventar la computadora personal, parado frente a la sala llena de la gente que estaba construyendo el software del mundo. Y sigue siendo cierta.[^img_kay]

Eso es lo que me pone incómodo. Si la frase hubiera envejecido mal, sería una anécdota simpática: mirá, en el 97 este señor se quejaba y después vino todo lo bueno. Pero envejeció al revés. Desde entonces cada uno de nosotros pasó a llevar en el bolsillo una máquina más rápida que la Cray a la que un país entero le rendía culto, y con esa máquina hacemos, básicamente, lo mismo que hacíamos antes pero con más notificaciones. La velocidad llegó. La revolución, no.

> 🕳️ **HUECO — necesita a César:** ¿Qué máquina tenías en 1997 y qué estabas escribiendo en ella? Una o dos frases alcanzan (marca/modelo o tipo de máquina + qué tipo de código). Sirve para anclar el «yo también estaba ahí» justo acá.

## El tipo que dice esto no es un cronista

Conviene saber quién habla, porque cambia el peso de la frase.

Alan Kay acuñó el término _object-oriented_. Fue el padre de Smalltalk, y él mismo contó esa historia con lujo de detalle en _The Early History of Smalltalk_, el texto que presentó en HOPL II en 1993 y que es, todavía hoy, la mejor entrada a cómo pensaba.[^smalltalk-history] Trabajó en Xerox PARC, el laboratorio donde se armó buena parte de lo que hoy damos por natural cuando prendemos una computadora. Antes de eso, siendo estudiante de posgrado, orbitó el mundo de ARPA: en esta misma keynote lo cuenta sin grandilocuencia —«jugué un papel muy menor en el diseño de ARPANET; fui uno de treinta estudiantes de posgrado que iban a las reuniones de diseño de sistemas»—, hacia fines de los sesenta (la red empezó a funcionar alrededor de 1969).[^kay-oopsla]

Y en 1972 escribió un paper con un título que parece de librería infantil y era un manifiesto: _A Personal Computer for Children of All Ages_.[^dynabook] Ahí describe el Dynabook. La palabra clave del título no es _computer_: es _children_. Kay no estaba imaginando una herramienta de productividad para oficinistas. Estaba imaginando un instrumento que un chico agarrara para pensar cosas que sin el instrumento no podría pensar. [VERIFICAR: cualquier especificación concreta del Dynabook — tamaño, peso, precio objetivo, autonomía — leerlas del PDF de 1972 antes de afirmarlas; acá no afirmo ninguna a propósito].

Esa es la vara. Y es una vara rara, porque no es de ingeniería: es de alfabetización.

> 🕳️ **HUECO — necesita a César:** ¿Tocaste Smalltalk alguna vez —o Squeak, o Pharo— aunque sea de curioso? ¿Cuándo, y qué te quedó? Si la respuesta es «nunca, y me da culpa», también sirve y es más honesta.

## Qué quiso decir con «revolución»

Acá está el malentendido que hace que la frase circule mal. Cuando alguien la cita en un hilo, casi siempre la usa como «uf, qué mal está el software». Y no es eso. Kay no está diciendo que el software sea malo. Está diciendo que todavía no pasó **la otra cosa**, la que él esperaba, y que confundimos el ruido del progreso con la cosa.

La analogía que usa —y que es la que hay que verificar contra el vídeo antes de publicar— es la de la imprenta. Gutenberg no fue la revolución. Gutenberg fue la máquina. La revolución fue lo que pasó cuando, siglos después, la sociedad desarrolló los géneros, los hábitos y la alfabetización necesarios para que la imprenta cambiara cómo se piensa: el ensayo, el método científico, el artículo. La computadora, en esa cuenta, todavía está en la etapa Gutenberg: tenemos la máquina y estamos imprimiendo, con tipos móviles carísimos, versiones más brillantes de los manuscritos que ya teníamos. [VERIFICAR: que la analogía de la imprenta esté efectivamente en la keynote de 1997 y con qué formulación — anotar timestamp de [[tr-01]]].

El outline de este post supone que Kay articula tres ejes de qué _sería_ una revolución. Los escribo, pero cada uno va marcado, porque la bibliografía que tengo no me alcanza para atribuírselos así de limpio:

**Primero: la computadora como medio para pensar.** No como medio para _ver_, ni para consumir, ni para comunicar: para pensar. Un medio te da representaciones nuevas, y las representaciones nuevas te dan pensamientos nuevos. [VERIFICAR: formulación exacta y timestamp en [[tr-01]]].

**Segundo: la programación de usuario final.** Que la persona que usa el sistema pueda modificarlo desde adentro, sin cambiar de rol, sin pedir permiso, sin abrir un ticket. [VERIFICAR: que este eje esté en la keynote y no sea sólo un tema recurrente de Kay en otras charlas — timestamp en [[tr-01]]].

**Tercero: el late binding llevado al extremo.** Sistemas que se puedan cambiar mientras corren, sin apagarlos, porque las decisiones no están congeladas en tiempo de compilación. Esto sí está en el centro de lo que Kay quiso decir con «orientado a objetos» —mensajes y ligadura tardía, no clases ni herencia—, y es lo que discuten hasta el cansancio los hilos de Reddit y Software Engineering SE que junté como fuente.[^kay-oop] [VERIFICAR: que el extremismo de late binding aparezca como tal en la keynote del 97, no sólo en las citas por correo que circulan en esos hilos].

> 🕳️ **HUECO — necesita a César:** ¿Cómo llegaste vos a esta keynote — te la mandó alguien, la encontraste solo, en qué época? Y sobre todo: ¿te acordás qué te pareció la primera vez? (Una frase. Si la reacción fue «no entendí nada», eso es más útil que si fue «me voló la cabeza»).

## Por qué no pasó

La tentación es explicarlo con villanos: la industria es corta de miras, el marketing ganó, nadie lee. Es cómodo y no explica nada. Lo que a mí me cierra es más aburrido y más difícil de arreglar.

**Los incentivos no premian el medio, premian el producto.** Un medio para pensar no se factura por unidad. Un producto sí. Todo el aparato económico que financió las últimas décadas de software está calibrado para hacer que hagas más cosas por minuto, no para hacerte pensar mejor —eso último no tiene métrica trimestral.

**La complejidad acumulada tiene interés compuesto.** Cada capa que agregamos para no romper lo que ya existe encarece la siguiente. Después de suficientes capas, cambiar la idea de base deja de ser una decisión técnica y pasa a ser una decisión geopolítica.

**Y la optimización local es una trampa perfecta.** Cada paso individual fue razonable. Nadie decidió no hacer la revolución. Simplemente, en cada bifurcación, la rama que mejoraba un 5% lo que ya había siempre le ganó a la rama que empezaba de nuevo con un 50% peor y una promesa. Repetí eso cuarenta años y llegás exactamente acá: máquinas prodigiosas ejecutando ideas de 1975.

Kay volvió sobre esta incomodidad cinco años después de la keynote, en un lugar improbable: el apéndice B del manual de Croquet, borrador 0.1 de octubre de 2002, titulado _Is «Software Engineering» an Oxymoron?_.[^kay-oximoron] Es un buen indicio de cómo trabaja: la crítica más filosa no la publica como ensayo, la deja al final de un documento técnico. De ese apéndice sale otro post de este blog ([[C-01]]), así que acá no me meto.

> 🕳️ **HUECO — necesita a César:** ¿Viste alguna vez, en la STG o en el Ministerio de Cultura de Santa Fe, a un usuario final construirse su propia herramienta —una macro, una consulta, un formulario, algo— sin pedirle permiso al área de sistemas? ¿Cómo terminó? Es el mejor lugar del post para bajar el punto 2 de Kay a algo que viviste.

> 🕳️ **HUECO — necesita a César:** ¿Comprás la idea de que la planilla de cálculo es lo más cerca que estuvimos de la programación de usuario final —y que ganó justamente porque nadie la llamó programación? ¿Sí, no, con qué matiz? Va como párrafo corto acá.

## Croquet: hacer la cosa como él la quería

Kay no se quedó en la queja, y eso hay que decirlo. Croquet fue un intento de construir un sistema de colaboración 3D con la arquitectura que él consideraba correcta, no la que la industria consideraba vendible.[^croquet] Los que estuvieron cerca dejaron su rastro en el c2 wiki, que es el lugar donde estas cosas se discutían antes de que discutir fuera un producto.[^opencroquet]

Croquet no ganó. Smith y Kay lo arrancaron a fines de 2001; el primer código funcionó en enero de 2002; la beta del SDK 1.0 se liberó como open source el 18 de abril de 2006 y la versión 1.0 recién salió el 24 de diciembre de 2009; después la posta la tomaron los proyectos Open Croquet y Open Cobalt.[^croquet] Y esa es la parte importante: no es que Kay tuviera razón y nadie lo escuchara. Es que Kay tuvo la razón, el prestigio, el financiamiento y la sala llena, construyó la cosa, y aun así la cosa no prendió. Cuando el proyecto que hace todo bien igual pierde, el problema no era el proyecto.

[VERIFICAR: Squeak y Etoys **no están en la bibliografía de este draft**. Si van a entrar en el post —el outline los pide— hay que agregar fuentes propias para cada uno antes de escribir el párrafo. No lo escribo con lo que tengo].

## ¿Qué reconocería Kay hoy?

Ésta es la pregunta con la que quiero cerrar, y la respuesta honesta me parece que es: probablemente nada.

No porque no haya pasado nada. Pasaron cosas enormes. Pero casi todas son mejoras de escala sobre la idea vieja: más rápido, más barato, más chico, más conectado, más disponible. Ninguna cambia lo que un chico de doce años puede pensar con la máquina en la mano que no podía pensar sin ella. Y ésa era la vara del paper de 1972.

El heredero directo de esta incomodidad es Bret Victor, que escribió _A Brief Rant on the Future of Interaction Design_ y que hospeda, en su propio sitio, el texto de Kay sobre la historia de Smalltalk.[^victor] No es casualidad: son la misma queja con treinta años de diferencia. Tenemos manos capaces de sentir el filo de una hoja de papel y las usamos para arrastrar el dedo sobre un vidrio liso.

Y sin embargo. Lo que me llevo de la frase de Kay no es la resignación, es lo contrario. «Todavía no llegó» no es «no va a llegar». Es una descripción de dónde estamos parados: en el año 30 después de Gutenberg, imprimiendo biblias hermosas, sin haber inventado todavía el ensayo. Eso no es un fracaso. Es una tarea pendiente, y está pendiente para nosotros.

> 🕳️ **HUECO — necesita a César:** Después de tus treinta años en esto: ¿tu veredicto es «Kay tenía razón y sigue teniéndola», «Kay tenía razón pero la vara era imposible», o algo intermedio? Dos o tres frases en primera persona. Este es el párrafo final del post y no lo puedo escribir por vos.

> 🕳️ **HUECO — necesita a César:** ¿Hay alguna herramienta —una sola— que en tu experiencia sí te hizo pensar cosas que no podías pensar sin ella? Si la hay, nombrala y decí en una frase qué te destrabó. Sería el mejor cierre posible: el único candidato honesto a «avance hacia la revolución».

[^kay-oopsla]: Alan Kay, [*The Computer Revolution Hasn't Happened Yet*](https://www.youtube.com/watch?v=oKg1hTOQXoY) — keynote de OOPSLA '97 (Atlanta, 5-9 de octubre de 1997). Ver [[tr-01]] en el plan editorial. **Frágil (YouTube):** backup del vídeo en [Internet Archive](https://archive.org/details/AlanKayAtOOPSLA1997TheComputerRevolutionHasntHappenedYet); transcripción de texto en [tinlizzie.org](https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997:_The_Computer_Revolution_has_not_Happened_Yet) (archivo de Viewpoints Research). La cita sobre ARPANET está tomada de esa transcripción.

[^smalltalk-history]: Alan Kay, [*The Early History of Smalltalk*](http://worrydream.com/EarlyHistoryOfSmalltalk/) — ACM SIGPLAN Notices, vol. 28, n.º 3 (marzo de 1993), actas de HOPL-II. DOI [10.1145/155360.155364](https://doi.org/10.1145/155360.155364) (verificado en Crossref). El enlace es el mirror libre alojado en el sitio de Bret Victor (worrydream.com).

[^dynabook]: Alan Kay, [*A Personal Computer for Children of All Ages*](http://www.mprove.de/diplom/gui/Kay72a.pdf) — documento de Xerox PARC presentado en la ACM National Conference, Boston, agosto de 1972. El paper original del Dynabook.

[^kay-oop]: Los hilos consolidados sobre qué quiso decir Kay con «orientado a objetos»: [Reddit r/programming](https://www.reddit.com/r/programming/comments/bpb5v6/alan_kay_on_his_original_thoughts_when_he_came_up/) y [Software Engineering SE](https://softwareengineering.stackexchange.com/questions/46592/so-what-did-alan-kay-really-mean-by-the-term-object-oriented). Ver [[tr-22]] en el plan editorial.

[^kay-oximoron]: Alan Kay, *Is "Software Engineering" an Oxymoron?* — apéndice B de *Croquet: The User Manual*, draft 0.1, octubre de 2002. [PDF en Wayback Machine](http://web.archive.org/web/20030407181600/www.opencroquet.org/downloads/Croquet0.1.pdf). Ver [[tr-21]] en el plan editorial.

[^croquet]: [Croquet Project](https://en.wikipedia.org/wiki/Croquet_Project) en Wikipedia.

[^opencroquet]: [OpenCroquet](https://wiki.c2.com/?OpenCroquet) en el c2 wiki.

[^victor]: Bret Victor, [*A Brief Rant on the Future of Interaction Design*](http://worrydream.com/ABriefRantOnTheFutureOfInteractionDesign/).

[^img_kay]: Imagen de [Alan Kay](https://commons.wikimedia.org/wiki/File:Alan_Kay2.jpg) — CC BY-SA 4.0 — Marcin Wichary. Recortada a 2.5:1 para hero landscape.

[^img_dynabook]: Imagen de [Alan Kay and the prototype of Dynabook, pt. 5](https://commons.wikimedia.org/wiki/File:Alan_Kay_and_the_prototype_of_Dynabook,_pt._5_(3010032738).jpg) — CC BY 2.0. **Pendiente: referenciar esta footnote inline en el cuerpo (probablemente en la sección del Dynabook) — una footnote huérfana no renderiza.**

