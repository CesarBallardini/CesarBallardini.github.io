### A1-17 — Perl: el lenguaje del lingüista (entrevista a Larry Wall)

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `perl-larry-wall-linguista`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-perl-larry-wall-linguista/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-13]], [[C-02]] (Hickey simple vs easy — contraste cultural)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** Larry Wall es lingüista de formación. Eso explica casi todo lo raro y maravilloso de Perl: el contexto sensible, las múltiples maneras de decir lo mismo, la elegancia desordenada, "There's More Than One Way To Do It". El post toma la entrevista de Wall en *Masterminds* y discute cómo el background lingüístico influyó en el diseño del lenguaje, y por qué Perl envejeció raro pero todavía tiene cosas para enseñarnos.

**Hook:** Larry Wall es lingüista. Eso explica todo lo raro de Perl. Acá está la entrevista que me hizo entender por qué Perl tiene "There Is More Than One Way To Do It" como religión.

**Outline:**

1. **Hook — el dato que reordena todo.** Larry Wall es lingüista de formación, no ingeniero. Todo lo raro de Perl deja de ser raro cuando sabés eso.
2. **Qué significa «ser lingüista» acá.** La distinción descriptivo/prescriptivo: el lingüista describe cómo se habla, no legisla cómo habría que hablar. Ese es el eje del post.
3. **TMTOWTDI no es pereza de diseño, es una tesis sobre el lenguaje.** «There's More Than One Way To Do It» leído como observación lingüística — ningún idioma natural tiene una sola manera de decir las cosas.
4. **Contexto sensible: el rasgo más lingüístico de todos.** Escalar vs lista; la misma expresión significa cosas distintas según dónde aparece. Eso es gramática, no ingeniería.
5. **Los sigilos como partes del discurso.** `$`, `@`, `%` leídos como número gramatical y categoría, no como decoración.
6. **El Camel Book no es un manual: es una gramática.** Cómo el libro de 1991 se parece más a una descripción de un idioma que a una especificación.
7. **El contraste cultural: Perl contra la escuela de la parsimonia.** Perl eligió *easy* donde otros eligieron *simple* — cruce con [[C-02]] (Hickey).
8. **Por qué Perl envejeció raro.** Hipótesis a sopesar, no veredicto: el costo de la libertad total, el «write-only», la fractura de Perl 6.
9. **Lo que Perl todavía tiene para enseñarnos.** La idea que sobrevive incluso si no volvés a escribir Perl nunca más.
10. **Cierre — el idioma que se dejó hablar mal.**

**Bibliografía:**

_Fuentes primarias — Wall en sus propias palabras:_

- [[tr-23]] Masterminds of Programming (entrevista a Larry Wall). Federico Biancuzzi y Shane Warden, O'Reilly, 2009 (ISBN 9780596515171). **No hay copia libre ni en préstamo en archive.org** (verificado en Open Library: la obra no tiene `ia` asociado). `estable` (ficha), sin texto accesible.
- Larry Wall, [«Natural Language Principles in Perl»](http://www.wall.org/~larry/natural.html) — sitio propio de Wall. Las 16 «principios de lenguaje natural» que dice haber puesto en Perl, incluidos sigilos como `this`/`these`, tópico, pronominalización, dialectos. **La fuente primaria central del post.** `frágil` (dominio personal) — backup Wayback: `http://web.archive.org/web/20260216083442/http://www.wall.org/~larry/natural.html`
- Larry Wall, [«The Culture of Perl»](https://www.perl.com/pub/1997/wall/keynote.html/) — keynote de The Perl Conference, 20/08/1997, publicada en perl.com. Tagmemics, «There's more than one way to do it» leído como antropología, y «any language essentially *should* be out of control, because no one person or institution is capable of controlling a language without destroying it». `frágil` — backup Wayback: `http://web.archive.org/web/20260302114141/https://www.perl.com/pub/1997/wall/keynote.html/`
- Larry Wall, [«Perl, the first postmodern computer language»](https://wall.org/~larry/pm.html) — keynote de LinuxWorld Expo, San José, primavera 1999 (perl.com la publicó el 09/03/1999). De ahí sale: «I combined these cool features in a way that makes sense to me as a postmodern linguist, not in a way that makes sense to the typical Modernistic computer scientist». `frágil` — backup Wayback: `http://web.archive.org/web/20260603200551/https://www.wall.org/~larry/pm.html`
- [Índice de artículos y charlas de Larry Wall en perl.com](https://www.perl.com/authors/larry-wall/) — **este es el «Wall's Talks» que pedía la bibliografía vieja**. 17 piezas fechadas, de «The Culture of Perl» (1997) a «Programming is Hard, Let's Go Scripting…» (2007), pasando por los State of the Onion 1998–2006 y los Apocalypse 1–12. `frágil` (perl.com reorganizó URLs históricamente).
- [Larry Wall's Very Own Home Page](https://www.wall.org/~larry/) — índice de su sitio; lista las charlas 1997–1999 y confirma SPU como alma mater. `frágil`.

_Entrevistas publicadas:_

- Marjorie Richardson, [«Larry Wall, the Guru of Perl»](https://www.linuxjournal.com/article/3394) — Linux Journal, 01/05/1999. **Fuente verificada de la formación de Wall** (SPU, major autodiseñado «Natural and Artificial Languages», posgrado en lingüística en Berkeley y UCLA, plan de ser traductores de la Biblia abandonado por razones de salud). `frágil` — backup Wayback: `http://web.archive.org/web/20260703214157/https://www.linuxjournal.com/article/3394`
- Eugene Eric Kim, «A Conversation with Larry Wall» — Dr. Dobb's Journal, febrero 1998. Copia accesible: [alma.ch/perl/lw-interview.htm](https://alma.ch/perl/lw-interview.htm). De acá salen «I'm one of those people that packed four years into eight», el major autoconstruido, y el origen de `patch` (lo escribió porque los parches de `rn` eran «too mess» de aplicar a mano). `frágil` (sitio personal de terceros) — backup Wayback: `http://web.archive.org/web/20241202095620/https://alma.ch/perl/lw-interview.htm`
- Lorrie Faith Cranor, «Programming Perl: an interview with Larry Wall». *XRDS: Crossroads, The ACM Magazine for Students*, vol. 1, nº 2 (1994), pp. 10–11. DOI: [10.1145/197149.197157](https://doi.org/10.1145/197149.197157) — **la ACM DL devuelve 403 al fetch automatizado**; metadatos verificados vía `https://api.crossref.org/works/10.1145/197149.197157`. `estable` (DOI). Sin mirror libre encontrado.

_Documentación oficial de Perl:_

- [`perldata`](https://perldoc.perl.org/perldata) — perldoc oficial. Dice literalmente: «`$` … works semantically like the English word 'the'»; «`@` … works much as the word 'these' or 'those' does in English»; «Every variable type has its own namespace … This means that `$foo` and `@foo` are two different variables»; «If you evaluate an array in scalar context, it returns the length of the array». `estable`.
- [`perlhist`](https://perldoc.perl.org/perlhist) — cronología oficial. Perl 1.000: **18 de diciembre de 1987**. Incluye la nota de Wall: «Perl 0 introduced Perl to my officemates. Perl 1 introduced Perl to the world». `estable`.

_El Camel Book:_

- Larry Wall y Randal L. Schwartz, *Programming Perl*. Sebastopol, CA: O'Reilly & Associates, 1991. Serie «A Nutshell handbook». ISBN 0-937175-64-1 / 978-0-937175-64-4. xxi + 465 pp. LCCN 94114950. Ficha verificada en el registro de edición de Open Library: [openlibrary.org/books/OL1144106M](https://openlibrary.org/isbn/0937175641) (`by_statement`: «Larry Wall and Randal L. Schwartz.»). `estable`.
  - Escaneo de la **1ª edición** en archive.org: [programmingperl000wall](https://archive.org/details/programmingperl000wall) — `access-restricted-item: true`, **no prestable**; sirve para confirmar la ficha, no para leerlo.
  - **2ª edición** (1996, Wall + Schwartz + Christiansen, ISBN 1-56592-149-6, 690 pp): [programmingperl00wall](https://archive.org/details/programmingperl00wall). `estable`.

_Contexto histórico y académico:_

- Michael Stevenson, «Having it both ways: Larry Wall, Perl and the technology and culture of the early web». *Internet Histories: Digital Technology, Culture and Society*, vol. 2, nº 3-4 (2018), pp. 264–280. DOI: [10.1080/24701475.2018.1495810](https://doi.org/10.1080/24701475.2018.1495810) — **Taylor & Francis devuelve 403**; metadatos verificados vía Crossref. Mirror libre de texto completo (CC BY-NC-ND) en el repositorio de la Universidad de Ámsterdam: [pure.uva.nl PDF](https://pure.uva.nl/ws/files/44161021/Having_it_both_ways_Larry_Wall_Perl_and_the_technology_and_culture_of_the_early_web.pdf). `estable` (DOI + repositorio institucional). **Es el respaldo académico de la sección CGI y del envejecimiento de Perl.**
- Sharon Hopkins (Telos Corporation), «Camels and Needles: Computer Poetry Meets the Perl Programming Language». *Proceedings of the USENIX Winter 1992 Technical Conference*, San Francisco, 20–24 de enero de 1992, pp. 391–404. Volumen completo escaneado y libre en archive.org: [winter92_usenix_technical_conf](https://archive.org/details/winter92_usenix_technical_conf) (índice y texto del paper verificados en el OCR del propio escaneo). `estable`.
- [`patch(1)` — Linux manual page](https://www.man7.org/linux/man-pages/man1/patch.1.html), sección AUTHORS: «Larry Wall wrote the original version of patch.» `estable`.
- Mark-Jason Dominus, [«Report on the Perl 6 Announcement»](https://www.perl.com/pub/2000/07/perl6.html/) — perl.com, 25/07/2000. Crónica de primera mano del anuncio de Perl 6 en el State of the Onion de la Perl Conference. `frágil`.
- Larry Wall, [«State of the Onion 2000»](https://www.perl.com/pub/2000/10/23/soto2000.html/) — perl.com, 24/10/2000. La charla donde se anunció Perl 6. `frágil`. _(Listada desde el índice de autor verificado; no fetcheada en profundidad.)_
- [Anuncio de release de Rakudo, diciembre 2015](https://github.com/rakudo/rakudo/blob/nom/docs/announce/2015.12.md) — el release de Navidad que apunta a la especificación **v6.c «Christmas»**. `estable` (repo git).
- [Raku/problem-solving PR #89, «Path to raku»](https://github.com/Raku/problem-solving/pull/89) — abierto por lizmat, **mergeado el 14/10/2019**. Larry Wall (TimToady) comenta a favor citando la parábola del vino nuevo en odres nuevos. **Fuente primaria del rebautizo.** `estable`.
- Neil Bowers, [«CPAN Report 2026»](https://neilb.org/2026/01/13/cpan-report-2026.html) — 13/01/2026. «As of January 2026 more than 43,500 different distributions have been released during the lifetime of CPAN»; 108 altas de PAUSE en 2025 (el número más bajo desde 1997); desarrollo fuerte 2002–2014, caída 2015–2022, meseta actual. `frágil`.
- [www.cpan.org](https://www.cpan.org/) — contador en vivo. Al 15/07/2026: «32,912,869 Perl modules in 47,487 distributions, written by 14,717 authors». `frágil` (el número cambia; citar con fecha).
- Neil Bowers, [history-of-cpan/history.md](https://github.com/neilb/history-of-cpan/blob/master/history.md) — cronología documentada de CPAN: lista perl-packrats creada el 02/12/1993; Andreas König propone un «MASTER site for modules» el 17/04/1995; primer upload el 16/08/1995; **JHI anuncia CPAN en comp.lang.perl.announce el 26/10/1995**. `estable` (repo git).
- Dave Jacoby, [«Perl and CGI»](https://www.perl.com/article/perl-and-cgi/) — perl.com, 12/11/2018. El arco de `CGI.pm`: deprecado en Perl 5.20, sacado del core en 5.22. `frágil`.

**Imágenes:** candidatos verificados en Wikimedia Commons (el camello de O'Reilly **no** sirve: es marca registrada).

- **Hero recomendado:** [File:FOSDEM 2015 Larry Wall and Camelia the Perl6 logo.jpg](https://commons.wikimedia.org/wiki/File:FOSDEM_2015_Larry_Wall_and_Camelia_the_Perl6_logo.jpg) — Larry Wall en FOSDEM 2015, autor **Klapi**, **CC BY-SA 4.0**, 3450×2490 px. Metadatos verificados vía la API de Commons. Es 1,39:1: hay margen de sobra para recortar a 2,5:1 con Pillow.
  - Footnote de atribución (borrador): `[^img_wall]: Imagen de [Larry Wall, FOSDEM 2015](https://commons.wikimedia.org/wiki/File:FOSDEM_2015_Larry_Wall_and_Camelia_the_Perl6_logo.jpg) — CC BY-SA 4.0 — Klapi. Recortada a 2.5:1 para hero landscape.`
- **Alternativa (con guiño):** [File:Larry Wall YAPC 2007.jpg](https://commons.wikimedia.org/wiki/File:Larry_Wall_YAPC_2007.jpg) — YAPC::NA, Houston, 24/06/2007. Autor: **Randal Schwartz** (sí: el coautor del Camel Book fotografiando a Wall), **CC BY-SA 2.0**, vía Flickr. Contra: 411×578 px, retrato y chica — inservible como hero, quizá como imagen interior.

**Tags propuestos:** `['Perl','Larry Wall','lingüística','historia']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (10 secciones), se fijó `Length target: medium` y se escribió un borrador de prosa completo (~1800 palabras de prosa efectiva, sin contar marcas de verificación ni huecos) en la sección «Borrador de prosa» al pie.

Lo que quedó **escrito**: el armazón argumental entero — la distinción descriptivo/prescriptivo como eje, TMTOWTDI leído como tesis lingüística y no como pereza, el contexto sensible y los sigilos como gramática, el Camel Book como descripción de un idioma, el contraste con la escuela de la parsimonia ([[C-02]], Hickey), las hipótesis sobre el envejecimiento raro, y el cierre. Se sostiene solo como ensayo.

Lo que quedó como **hueco**:

- 6 huecos `🕳️` pidiendo a César recuerdos y opiniones propias: qué le pasó al leer la entrevista a Wall, si tuvo el Camel Book en papel, si vivió la espera de Perl 6, si escribió Perl en un trabajo real (¿sector público? ¿scripts de sysadmin?), si le tocó mantener Perl ajeno, y el veredicto personal del cierre. Sin esos, el post es correcto pero impersonal — no es un post de katra todavía.
- 14 marcas `[VERIFICAR:]` sobre datos que **no** están respaldados por la bibliografía listada: la formación concreta de Wall (qué estudió, dónde, y si terminó el posgrado) — que es **la premisa misma del post** y por lo tanto la verificación más urgente de todas; la autoría real del acrónimo TMTOWTDI y dónde se formuló primero; la ficha bibliográfica del Camel Book y su autoría compartida; el contexto de nacimiento de Perl y la atribución de `patch` a Wall; la afirmación sobre Perl como lenguaje dominante del CGI; la cronología Perl 6 → Raku completa; si la entrevista de *Masterminds* habla de Perl 6 y qué dice; la Perl poetry y el estado de CPAN en 2026; la URL y los títulos/años de las charlas en perl.com; y la ejecución real de los dos fragmentos de código (contexto escalar/lista, y si `$foo`/`@foo` son identificadores distintos bajo `use strict`).
- La bibliografía es delgada a propósito: sólo [[tr-23]], el Camel Book y *Wall's Talks*. **Antes de publicar hay que decidir** si se resuelven los `[VERIFICAR:]` sumando fuentes nuevas al plan (las charlas de Wall en perl.com son el candidato natural y ya están listadas, pero hay que fijar título/año/URL de cada una que se cite) o si se recorta el post a lo que las tres fuentes actuales sostienen.
- Los ejemplos de código Perl del borrador están escritos de memoria y **no fueron ejecutados**. Hay que correrlos antes de publicar.
- `**Imágenes:**` sigue en `_a definir_` — el candidato obvio es el camello del Camel Book, pero es marca registrada de O'Reilly y **no** sirve; hay que buscar otra cosa con licencia clara en Wikimedia Commons (¿una foto de Wall en una conferencia?).

---

## Borrador de prosa

Hay un dato biográfico sobre Larry Wall que, cuando lo escuché por primera vez, me reordenó la cabeza entera respecto de Perl: Wall no viene de la ingeniería. Viene de la lingüística.

Lo cuenta él mismo, con el humor de siempre, en una entrevista de 1999[^lj1999]:

> For the third half of my childhood, I went to Seattle Pacific University, where I started off majoring in chemistry and music, later switched to premed, and eventually (after taking several years off to work in the SPU computer center) ended up majoring in Natural and Artificial Languages (a self-designed major).

«Natural and Artificial Languages» — lenguajes naturales y artificiales — es un major que Wall **se inventó**: no existía, lo armó él. En otra entrevista lo resume mejor que nadie: «I'm one of those people that packed four years into eight», y el major autoconstruido «seems positively prescient considering where I ended up»[^ddj1998].

Y sigue: «After that, my wife and I attended grad school in linguistics at Berkeley and UCLA. At the time, we were actually planning to be missionaries (more specifically, Bible translators), but we had to drop that idea for health reasons.»[^lj1999]

O sea: no es que Wall haya leído algo de lingüística. Wall se estaba entrenando para ir a algún lado del mundo, encontrar un idioma que no tuviera escritura, y **inventarle una escritura**. Ese era el plan de vida. Perl es lo que hizo cuando ese plan se cayó.

[VERIFICAR: si Wall **completó o no** el posgrado de lingüística. La entrevista de Linux Journal (1999) dice que fueron a grad school en Berkeley y UCLA y que abandonaron el plan misionero por razones de salud, pero **no dice explícitamente** que haya dejado el posgrado sin título; la de Dr. Dobb's (1998) tampoco. La versión de «abandonó sin terminar» circula por la web pero no la encontré en boca de Wall. Buscado en: wall.org (su sitio propio), las entrevistas de Linux Journal 1999 y Dr. Dobb's 1998, y el índice de charlas de perl.com — sin resultado. Probar: la entrevista de *Masterminds* [[tr-23]], y la de XRDS/ACM 1994 (DOI 10.1145/197149.197157, la ACM DL da 403 — conseguir el PDF por otra vía). **Mientras tanto, no afirmar que abandonó.**]

Y con eso solo, casi todo lo que a la gente le parece raro, feo o directamente indefendible de Perl deja de ser raro. No se vuelve necesariamente *bueno* — eso lo discutimos más abajo — pero se vuelve **coherente**. Perl no es un lenguaje de ingeniería que salió mal. Es un lenguaje de lingüística que salió exactamente como tenía que salir, y que después fue juzgado por un jurado de ingenieros que estaban puntuando otra competencia.

Este post sale de la entrevista a Wall en *Masterminds of Programming*[^masterminds] — el libro de entrevistas a creadores de lenguajes al que ya le dediqué un post entero con el roster completo [[A1-13]]. Acá voy a tirar de un solo hilo: qué le hace a un lenguaje de programación que lo diseñe alguien entrenado para estudiar cómo hablan los humanos.

> 🕳️ **HUECO — necesita a César:** ¿qué te pasó cuando leíste la entrevista a Wall en *Masterminds*? ¿Hubo alguna respuesta puntual que te haya hecho parar y releer? Una o dos frases alcanzan — es el ancla personal del post.

### Qué significa «ser lingüista» acá

Acá hay que ser preciso, porque «lingüista» suena a «sabe muchos idiomas» y no es eso.

La lingüística moderna es, antes que nada, **descriptiva**. El lingüista no se sienta a decidir cómo habría que hablar: sale a mirar cómo se habla, y describe lo que encuentra. Si toda una región dice «haiga», el lingüista no anota una falta: anota un dato. La pregunta «¿está bien dicho?» le resulta, en el mejor de los casos, secundaria; en el peor, mal planteada.

Lo contrario es la actitud **prescriptiva**: la de la academia, la del manual de estilo, la del profesor que te corrige. Esa mirada tiene una idea previa de cómo debe ser el idioma y evalúa el habla real contra esa idea.

Ahora agarrá esas dos actitudes y llevalas al diseño de lenguajes de programación. La tradición dominante en el diseño de lenguajes es **prescriptiva** hasta la médula: el diseñador decide cuál es la manera correcta de expresar algo, y el lenguaje te empuja hacia ahí — a veces con azúcar sintáctica, a veces a los empujones, a veces prohibiéndote directamente lo demás. Python tiene esto escrito en su documento fundacional: debería haber una manera obvia de hacerlo, y preferentemente una sola.

Wall hizo lo otro. Wall diseñó un lenguaje como quien describe un idioma: dejando que convivan las variantes, aceptando la redundancia, tolerando que haya registros distintos para hablantes distintos.

### TMTOWTDI no es pereza

«There's More Than One Way To Do It» — TMTOWTDI, que se pronuncia, dicen, «tim-toady».

Lo que sí está documentado es que el lema es de Wall y que él mismo lo defendió en público, en sus propias charlas, como argumento **antropológico y lingüístico** — no como excusa de diseño. En el keynote de The Perl Conference de 1997[^cultura] lo pone como una manera de romper las «cultural preconceptions»: distintas culturas dicen verdades equivalentes de maneras distintas, y buena parte de las peleas son por vocabulario y no por sustancia. Y en su lista de principios de lenguaje natural[^natural], el punto es explícito: es «Officially Okay in the Perl realm» programar en el subconjunto de Perl que se parece a sed, o a awk, o a C.

[VERIFICAR: quién acuñó el **acrónimo** TMTOWTDI (y la pronunciación «tim-toady»), y dónde aparece **formulado por primera vez** la frase completa. Busqué en: wall.org (natural.html, pm.html), el índice completo de charlas de Wall en perl.com, el keynote «The Culture of Perl» de 1997, y perldoc (`perl`, `perlfaq1`, `perlstyle`, `perlintro` de Perl 5.42 — el motto no aparece literal en ninguno). El candidato natural es el prefacio del Camel Book de 1991, pero el escaneo de la 1ª edición en archive.org es `access-restricted` y **no es prestable**, así que no pude leerlo; la búsqueda full-text de archive.org tampoco responde para ese ítem. **Para resolverlo hace falta un ejemplar físico del Camel Book 1ª ed. — si César lo tiene (ver hueco más abajo), se mira el prefacio y se cierra.** Mientras tanto: atribuir el lema a Wall (documentado), NO afirmar dónde apareció primero.]

Durante años leí ese lema como una excusa. Como el equivalente de diseño a encogerse de hombros: no me decidí, poné lo que quieras. Y es una lectura tentadora, porque el resultado superficial se parece: en Perl podés escribir lo mismo de cinco maneras, y las cinco andan.

Pero si venís de la lingüística, TMTOWTDI no es una excusa. **Es una observación empírica sobre cómo funcionan los idiomas de verdad.**

Pensalo en castellano. «No vino porque estaba lloviendo». «Como estaba lloviendo, no vino». «Estaba lloviendo, así que no vino». «No vino: llovía». Cuatro maneras de decir exactamente lo mismo. ¿Cuál es la correcta? La pregunta no tiene sentido. Son todas correctas y ninguna es intercambiable del todo, porque cada una pone el énfasis en otro lado, tiene otro ritmo, sirve para otro registro. Un idioma que tuviera una sola manera de decir cada cosa no sería un idioma más limpio: sería un idioma **muerto**, o sería código Morse.

Esa es la tesis de Perl, y no es pereza: es una postura. Wall miró los lenguajes de programación y dijo, en efecto, «esto que ustedes llaman rigor, yo lo llamo empobrecimiento del habla».

Lo que sigue es la parte incómoda: puede ser una postura hermosa y aun así ser un desastre operativo cuando el «hablante» no sos vos sino el que mantiene tu código tres años después. Voy a llegar a eso.

### Contexto sensible

Si tuviera que elegir un solo rasgo de Perl para probar la tesis del post, elijo este.

En Perl, la misma expresión significa cosas distintas según dónde esté parada. Un array en «contexto escalar» da su longitud; en «contexto de lista» da sus elementos. No cambiaste la expresión: cambiaste el lugar donde la pusiste, y con eso cambiaste lo que quiere decir.

```perl
my @cosas = ('a', 'b', 'c');
my $cuantas = @cosas;      # 3 — contexto escalar
my ($primera) = @cosas;    # 'a' — contexto de lista
```

_(Ejecutado el 2026-07-15 bajo `perl 5.42.2` con `use strict; use warnings;` — imprime `cuantas=3 primera=a`. El fragmento anda tal como está escrito.)_

Y no es un accidente de implementación ni folklore: está en la documentación oficial del lenguaje. `perldata`[^perldata] lo dice sin vueltas — «If you evaluate an array in scalar context, it returns the length of the array» — y describe los sigilos en términos **gramaticales**, no de tipos: `$` «works semantically like the English word 'the'», `@` «works much as the word 'these' or 'those' does in English». La documentación de referencia de Perl explica su propia sintaxis comparándola con el inglés. Eso no lo hace ningún otro lenguaje del canon.

A un ingeniero esto le parece una bomba de tiempo, y tiene sus razones: la misma cara sintáctica con dos comportamientos según un contexto que no es local ni evidente. Es exactamente el tipo de cosa que un lenguaje «serio» prohíbe.

Pero mirá esto: «¿tenés fuego?». No estoy preguntando si sos dueño de fuego. Y «hay mucha gente» — ¿cuántos verbos hay en castellano que cambien de significado según qué tengan al lado? Todos. **El contexto sensible es la manera normal de funcionar de los idiomas humanos.** No es una anomalía: es el mecanismo central por el cual un vocabulario finito expresa infinitas cosas sin explotar de tamaño.

Wall metió eso en un lenguaje de programación a propósito. No es un accidente de implementación: es gramática.

### Los sigilos son partes del discurso

Lo mismo pasa con `$foo`, `@foo`, `%foo`.

La lectura habitual — «notación húngara obligatoria, ruido visual» — se queda corta. La lectura lingüística es otra: el sigilo marca **número gramatical y categoría**. `$` es singular, `@` es plural, `%` es una relación entre pares. No estás anotando el tipo por burocracia: estás declinando la palabra, igual que en un idioma con marcas morfológicas.

Y esto no es una interpretación mía forzada sobre el lenguaje: es lo que dice Wall que hizo. En su lista de principios de lenguaje natural en Perl[^natural], los sigilos `$` y `@` están explicados como «this» y «these» — marcas de singular y plural sobre sustantivos. La misma explicación, palabra por palabra, terminó en `perldata`[^perldata].

Y hay algo más: en Perl el mismo nombre puede vivir en varias categorías a la vez. `$foo` y `@foo` conviven siendo cosas distintas, y no es un descuido tolerado sino una decisión documentada. `perldata`[^perldata]: «Every variable type has its own namespace, as do several non-variable identifiers. This means that you can, without fear of conflict, use the same name for a scalar variable, an array, or a hash… This means that `$foo` and `@foo` are two different variables.»

_(Verificado también corriéndolo: bajo `perl 5.42.2` con `use strict; use warnings;`, tanto `my $foo = "escalar"; my @foo = (1,2,3);` como la versión con `our` compilan y conviven sin queja.)_

Eso es homonimia entre categorías gramaticales, que es rigurosamente lo que pasa cuando decimos «el **poder** ejecutivo» y «**poder** hacerlo».

### El Camel Book no es un manual

El *Programming Perl*[^camel] de 1991 — Larry Wall y Randal L. Schwartz, O'Reilly & Associates, colección «Nutshell handbook», 465 páginas —, el libro del camello, es la otra evidencia.

La mayoría de los libros de lenguajes son especificaciones con tono amable: acá está la sintaxis, acá la semántica, acá los casos borde. El Camel Book se parece más a la **gramática descriptiva de un idioma** escrita por alguien que lo ama. Hay digresiones sobre estilo, hay observaciones sobre lo que la gente efectivamente hace, hay chistes, hay una voz. No te está diciendo solamente qué es legal: te está contando cómo se habla Perl, quiénes lo hablan y con qué acento.

> 🕳️ **HUECO — necesita a César:** ¿tuviste el Camel Book en papel? ¿Lo leíste de punta a punta o lo usaste como referencia de consulta? Si te acordás de la edición y de en qué momento de tu vida cayó en tus manos, mejor.

### Perl contra la escuela de la parsimonia

Acá está el contraste que le da filo al post.

Rich Hickey tiene una charla que ya trabajé aparte [[C-02]] cuya tesis, resumida a los golpes, es que *simple* y *easy* no son lo mismo: *simple* es no estar entrelazado, es una propiedad objetiva de la cosa; *easy* es estar a mano, es una propiedad de tu relación con la cosa, y depende de a qué estés acostumbrado. Y el argumento de Hickey es que la industria elige *easy* sistemáticamente y paga el precio en complejidad accidental para siempre.

Perl es, con toda claridad, el campeón mundial de *easy*. Perl te deja hacer lo que se te ocurra, de la manera que se te ocurra, ya mismo, sin ceremonia. Perl te dice «vos escribí, yo te entiendo».

Y ahora las dos lecturas, honestamente:

- **La lectura de Hickey**: Perl es exactamente el error. Cinco maneras de hacer todo es entrelazamiento cultural puro; lo que ganás en fluidez lo perdés multiplicado cuando hay que leer, mantener o razonar sobre el código.
- **La lectura de Wall**: Hickey está describiendo un idioma artificial y llamándolo virtud. Los idiomas humanos son «complejos» según esa vara, y sin embargo son la tecnología más exitosa que produjo nuestra especie.

No creo que haya que declarar un ganador, y creo que el post no debería. Lo que sí me parece que hay que decir es que **están optimizando cosas distintas**: Hickey optimiza para el que va a razonar sobre el sistema, Wall optimiza para el que lo está escribiendo ahora. Perl es el lenguaje del que tiene el problema adelante y quiere resolverlo hoy.

Y eso, dicho sea de paso, no es casual: Perl nace como herramienta de sysadmin, para gente con un problema encima y sin ganas de escribir cien líneas. La versión 1.000 salió el **18 de diciembre de 1987**[^perlhist], y el propio Wall lo cuenta así: «Perl 0 introduced Perl to my officemates. Perl 1 introduced Perl to the world.»[^perlhist] En 1999 lo resumía como «a problem I couldn't solve with the tools I had. Or rather, that I couldn't *easily* solve», con «a fortuitous surplus of the three chief virtues of a programmer: Laziness, Impatience and Hubris»[^lj1999].

El dato de `patch` sí se confirma, y de la mejor manera posible: **la página de manual de `patch` lo dice en su sección AUTHORS** — «Larry Wall wrote the original version of patch»[^patch]. Y Wall cuenta el motivo, que es puro Perl avant la lettre: había publicado `rn`, empezó a mandar parches para `rn`, «and it was a total mess»; escribió `patch` «so that they wouldn't have this excuse that it was too hard»[^ddj1998]. Es decir: Wall inventó la herramienta que hizo posible el desarrollo distribuido por correo porque le daba fiaca explicarle a la gente cómo aplicar un diff a mano.

[VERIFICAR: **dónde trabajaba Wall** cuando escribió Perl y **para qué problema concreto**. La entrevista de Dr. Dobb's (1998) menciona a Seagate Software pero como empleador *del momento de la entrevista*, no de 1987 — no sirve. La de Linux Journal (1999) sólo dice «programming and sys admin jobs like anyone else», y desliza que un administrador de la NSA le contó años después que había «shut down the NSA project Perl was (indirectly) written to support» — o sea que sí hubo un proyecto NSA de por medio, pero Wall no lo detalla ahí. La versión «System Development Corporation, después Unisys» aparece en Wikipedia y derivados, **no en boca de Wall en ninguna fuente que haya podido abrir**. Buscado en: wall.org, perlhist, Linux Journal 1999, Dr. Dobb's 1998, el paper de Stevenson 2018. Probar: *Masterminds* [[tr-23]] y la entrevista de XRDS/ACM 1994. **No escribir el nombre del empleador sin fuente primaria.**]

### Por qué envejeció raro

No tengo veredicto, tengo hipótesis. Van tres.

**La libertad total tiene un precio diferido.** Escribir Perl es un placer y leer Perl ajeno puede ser una arqueología. La acusación de «write-only» que le cae a Perl es la misma que le cae a APL, pero por el motivo inverso: APL era ilegible por denso, Perl es ilegible por **libre**. Si cada quien habla su dialecto, no hay dialecto común.

**Perl fue tan bueno para lo suyo que se quedó pegado a lo suyo.** Cuando la web explotó, Perl era el lenguaje del CGI. Cuando el mundo se movió a otras formas, esa asociación se volvió un ancla.

[VERIFICAR: la afirmación sobre Perl como lenguaje dominante del CGI en los 90 y su desplazamiento posterior. Es memoria colectiva, no una cita; conseguir fuente o bajar el tono a lo que se pueda sostener.]

**Perl 6.** Esta es la grande. Perl 6 se anunció como el rediseño desde cero, y la espera fue tan larga que hizo daño real: partió a la comunidad y le dio a todo el mundo una razón para tratar a Perl 5 como algo con fecha de vencimiento. Al final Perl 6 terminó rebautizándose Raku y separándose formalmente en dos lenguajes distintos.

[VERIFICAR: cronología de Perl 6 — año del anuncio, años de espera hasta un release usable, año del rebautizo a Raku, y cómo quedó formalmente la relación con Perl 5. Todos los números de esta sección están escritos de memoria y ninguno está respaldado por la bibliografía de este draft.]

[VERIFICAR: si la entrevista de Wall en *Masterminds* habla de Perl 6, y qué dice. El libro es de una época en que Perl 6 todavía era futuro; eso puede ser material buenísimo para el post — o puede no estar. Releer antes de escribir esta sección en firme.]

> 🕳️ **HUECO — necesita a César:** ¿viviste la espera de Perl 6 en tiempo real? ¿Te acordás de qué se decía en ese momento, y si en algún punto dejaste de esperarlo?

### Lo que todavía tiene para enseñarnos

Aun si no volvés a escribir una línea de Perl, hay algo que me parece que sobrevive, y no es técnico: es una pregunta.

**¿Para quién estás diseñando: para el que escribe o para el que lee?**

Casi todo el discurso moderno sobre lenguajes contesta «para el que lee», y lo contesta tan automáticamente que ya ni se nota que es una elección. Perl es el recordatorio incómodo de que la otra respuesta también tiene defensa, y de que hubo una época en que ganaba.

Y hay una segunda cosa, más rara: Perl es la prueba de que un lenguaje de programación puede ser un **objeto cultural** y no sólo una herramienta. Tenía chistes internos, tenía poesía — literalmente, gente escribía poemas ejecutables —, tenía una comunidad con folklore propio y un archivo de módulos enorme construido por gente que no le pagaba nadie.

[VERIFICAR: la «Perl poetry» y el estado de CPAN — cuántos módulos tiene hoy, si sigue activo en 2026, y desde qué año existe. No tirar números de memoria.]

Eso no lo produce un lenguaje que te dice cómo tenés que hablar. Lo produce uno que te deja hablar.

> 🕳️ **HUECO — necesita a César:** ¿escribiste Perl en algún trabajo real? ¿En qué contexto — scripts de sysadmin, procesamiento de texto, CGI, alguna migración? Si fue en el sector público, ¿en cuál de los dos lugares y para qué?

> 🕳️ **HUECO — necesita a César:** ¿te tocó alguna vez **mantener** Perl escrito por otro? Si sí, ¿confirmás el chiste del «write-only» o te parece injusto? Este es el contrapeso honesto de todo el post: sin él, queda como una defensa de Perl escrita por alguien que nunca lo sufrió.

### El idioma que se dejó hablar mal

Cierro con lo que me parece la lección, y es más grande que Perl.

Los lenguajes de programación son artefactos de ingeniería, sí. Pero también son **idiomas**, y los diseñamos casi siempre como si no lo fueran: legislando, prohibiendo, buscando la forma canónica. Wall fue el único que entró al problema con las herramientas del que estudia idiomas de verdad, y produjo la cosa más extraña del canon: un lenguaje que te deja hablarlo mal, a propósito, porque su diseñador sabía que todos los idiomas vivos se hablan mal y que ahí, justamente, es donde están vivos.

Que Perl haya terminado donde terminó no refuta la idea. Refuta, a lo sumo, que la industria estuviera lista para ella.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto, no el mío. ¿Perl te parece un experimento hermoso que falló, una herramienta que todavía usarías, o un error del que aprendimos? Las tres respuestas son buenas — pero la que cierra el post tiene que ser la tuya.

---

[^masterminds]: Entrevista a Larry Wall sobre Perl, en *Masterminds of Programming* — ver [[tr-23]] en el plan editorial.
[^camel]: Larry Wall, *Programming Perl* (el «Camel Book»), 1991. [VERIFICAR: ficha bibliográfica completa — editorial, coautores, edición. No inventar ISBN ni número de páginas.]
[^talks]: *Wall's Talks* — charlas de Larry Wall recopiladas en perl.com. [VERIFICAR: URL exacta de la recopilación en perl.com, y título + año de cada charla que se termine citando en el cuerpo. No pegar URLs de memoria; si se cita el «Perl is postmodern» o similar, confirmar título y fecha contra la fuente.]
