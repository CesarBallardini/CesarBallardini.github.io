### C-09 — DCI: Data, Context, Interaction — la idea olvidada de Trygve Reenskaug

- **Archivo seed:** _draft-rest.md bucket 5 (cosechado 2026-04-09)_
- **Slug propuesto:** `dci-data-context-interaction-reenskaug`
- **Comando:** `hugo new content/es/posts/2026-08-04-dci-data-context-interaction-reenskaug/index.md`
- **Serie:** filosofia
- **Cross-links:** **[[C-17]] (la continuación en Python — parte 2 de este par)**, [[E-14]] (clean architecture), [[C-02]] (Hickey), [[tr-01]] (Kay, OOPSLA 1997)
- **Idioma:** es
- **Madurez:** prosa-borrador ampliada (2026-08-03, generado por Claude; sin revisar por César)
- **Length target:** medium-long — **~3840 palabras de prosa** (más ~1100 de notas al pie y ~300 del apéndice «quién es quién», que es opcional). Bajó desde las ~5500 del borrador unificado al mudar la parte de Python a [[C-17]].

> **Este post es la parte 1 de un par.** El 2026-08-03 el borrador había crecido a ~5500 palabras porque incluía una implementación completa en Python. Se partió en dos: **C-09 (este)** cuenta la historia y la idea; **[[C-17]]** la implementa en Python, la hace andar y después la rompe. Cada uno se lee solo, pero C-17 asume C-09 leído.
>
> **Fechas decididas: C-09 sale el 2026-08-04 y [[C-17]] el 2026-08-05.** ⚠️ Las dos son **posteriores a hoy (2026-08-03)**, y Hugo **excluye en silencio** todo post con fecha futura: el deploy no falla, el post simplemente no aparece en el sitio (ver `CLAUDE.md` → Deployment). Antes de buildear, correr `hugo list future`; si hay que publicar antes de esas fechas, usar `hugo --cleanDestinationDir --buildFuture`. A partir del 2026-08-05 un build normal ya produce el árbol correcto sin flags.

**Concepto:** Trygve Reenskaug — el inventor del patrón MVC y del paradigma de roles en Smalltalk — publicó en 2009, junto con James O. Coplien, un paper proponiendo *DCI: Data, Context, Interaction* como una alternativa a la OOP centrada en datos. La idea: separar lo que un objeto *es* (datos persistentes) de lo que un objeto *hace en este caso de uso* (rol contextual). DCI nunca despegó comercialmente pero tiene admiradores serios. Este post cuenta de dónde salió la idea, qué dice exactamente, qué le criticaron y por qué (casi) nadie la usa.

**Hook:** el inventor del patrón MVC volvió cuarenta años después con una idea que él consideraba mejor que MVC. Se llama DCI. Casi nadie la conoce. Vamos a ver de dónde salió —hay trescientas toneladas de acero mal cortado en el origen— y qué propone exactamente.

**Outline:**
1. Hook: el tipo que inventó MVC volvió cuarenta años después con otra idea, y esta vez casi nadie lo escuchó.
2. Quién es Reenskaug: Autokon, las 300 toneladas de chatarra, el rechazo de Simula, PARC, MVC, OOram, BabyUML→BabyDCI. Por qué su currículum obliga a tomarlo en serio.
3. El problema que DCI ataca: mirás el modelo de objetos y no ves el caso de uso. Las *shear layers* de Coplien.
4. Las tres letras: Data (lo que el objeto *es*), Context (el caso de uso reificado), Interaction (los roles y su guion).
5. El ejemplo canónico contado sin código: la transferencia bancaria, y por qué los roles son contextuales.
6. Las críticas serias: Feathers, Zabroski, la respuesta de Reenskaug, y el único experimento controlado que existe.
7. Por qué (casi) nadie lo usa: lenguaje, ecosistema, economía.
8. Qué sí sobrevivió: el eco en Clean Architecture ([[E-14]]) y el paralelo con Hickey ([[C-02]]).
9. Cierre + puerta a la parte 2 ([[C-17]]).

**Bibliografía:** _(reforzada 2026-07-16; ampliada y re-verificada por fetch 2026-08-03)_

**Fuentes primarias — Reenskaug y Coplien**

- [Trygve Reenskaug & James O. Coplien, *The DCI Architecture: A New Vision of Object-Oriented Programming*, Artima, 20 de marzo de 2009](https://www.artima.com/articles/the-dci-architecture-a-new-vision-of-object-oriented-programming) — el paper fundacional. Usa la transferencia bancaria (*Source Account* → *Destination Account*) como ejemplo canónico. Menciona C++, Java, C#, Smalltalk, Python, Ruby, Scala, Squeak y Groovy. **frágil** (artima) → backup Wayback: `http://web.archive.org/web/20260703092833/https://www.artima.com/articles/the-dci-architecture-a-new-vision-of-object-oriented-programming`
- **[Trygve Reenskaug, *The Roots of DCI*, julio de 2010 (PDF, 9 pp.)](https://fulloo.info/Documents/2010DCI-Origin.pdf)** — ⭐ **hallazgo 2026-08-03**: éste es el documento que sostenía `[^roots]` y que en el pase anterior no se había podido localizar (la URL tentativa `.../babyide/roots.html` daba 404). Está vivo en fulloo.info y verificado por fetch. Es autobiográfico y contiene, con palabras del propio Reenskaug: Autokon (1963) y el accidente de las 300 toneladas de acero; el rechazo de Simula porque «el emisor de un mensaje debe conocer la clase del receptor»; su estadía en Xerox PARC en 1978/79; el primer OOram demostrado en el primer OOPSLA (Portland, 1986); su retiro en 1997 y el proyecto BabyUML; el rebautizo a BabyDCI el 28 de agosto de 2008; y la frase sobre Coplien. **estable** (fulloo.info, HTTP 200 al 2026-08-03).
- [Trygve Reenskaug, *The Common Sense of Object Oriented Programming*, abril de 2009 (PDF)](https://fulloo.info/Documents/200904commonsense.pdf) — el informe «Common Sense», dirigido al programador. Es la contraparte de bajo nivel del libro de Coplien. **estable**.
- [James O. Coplien & Trygve Reenskaug, *The DCI Paradigm: Taking Object Orientation Into the Architecture World* (PDF, 45 pp.)](https://fulloo.info/Documents/CoplienReenskaugASA2012.pdf) — capítulo publicado en *Agile Software Architecture*, Elsevier/Morgan Kaufmann, 2014 (la copia de fulloo.info está fechada 2013; DOI del capítulo en ScienceDirect: `B9780124077720000022`, que responde 403 al fetch automatizado). ⭐ Es la fuente del argumento de las *shear layers* y del pasaje sobre los roles del ejemplo bancario. **Corrección 2026-08-04:** el texto dice «*One possible mental model has three Roles: Source Account, Destination Account, and Transfer Amount*» — el «possible» es de ellos, así que no corresponde afirmar que el modelo mental «tiene tres roles y no dos». El paper de Artima escribe el algoritmo entre dos (*Source Account* / *Destination Account*) y nombra además al *Account Holder* como actor del caso de uso. Verificado contra el PDF (extracción de texto, 2026-08-04). También ahí está la afiliación de Reenskaug tal como él la firma: «Professor Emeritus of Informatics, University of Oslo». **estable**.
- [Trygve Reenskaug & James O. Coplien, *Working with objects — in computer and mind*, enero de 2014 (PDF)](https://fulloo.info/Documents/CommSenseCurrentDraft.pdf) — el último texto largo de Reenskaug sobre DCI, en estado de borrador con comentarios bienvenidos. **estable**.
- [Trygve Reenskaug, *DCI Execution Model*, mayo de 2012 (PDF)](https://fulloo.info/Documents/DCIExecutionModel-2.1.pdf) y [*DCI Glossary*, julio de 2014 (PDF)](https://folk.universitetetioslo.no/trygver/2011/DCI-Glossary.pdf) — la definición operacional y el glosario. Útiles si se quiere ser preciso con la terminología. El glosario **no** está en fulloo.info sino en el sitio personal: `fulloo.info/Documents/DCI-Glossary.pdf` da 404, y el enlace del índice de fulloo apunta a `folk.uio.no/trygver/2011/DCI-Glossary.pdf`, que hace 301 al host canónico nuevo. **mixto**.
- [Trygve Reenskaug, *Thing-Model-View-Editor*, Xerox PARC, 12 de mayo de 1979 (PDF)](https://folk.universitetetioslo.no/trygver/1979/mvc-1/1979-05-MVC.pdf) y [*Models-Views-Controllers*, 10 de diciembre de 1979 (PDF)](https://folk.universitetetioslo.no/trygver/1979/mvc-2/1979-12-MVC.pdf) — las dos notas fundacionales de MVC. **frágil**.
- [Página personal de Trygve Reenskaug](https://folk.universitetetioslo.no/trygver/) — MVC, roles/OOram, BabyUML, DCI. **frágil**. El dominio histórico `folk.uio.no/trygver/` hace **301 → `folk.universitetetioslo.no/trygver/`**.

**Libros**

- [James O. Coplien & Gertrud Bjørnvig, *Lean Architecture for Agile Software Development*, Wiley, julio de 2010](https://books.google.com/books/about/Lean_Architecture.html?id=lpvY36MPMUwC) — ISBN-13 978-0-470-68420-7 (ISBN-10 0-470-68420-8), 384 pp. **Ojo con la autoría:** el coautor es **Gertrud Bjørnvig**, no Reenskaug. Es el desarrollo largo de DCI y el propio Reenskaug lo reseñó (ver `The Roots of DCI`). estable.
- [Trygve Reenskaug con P. Wold y O. A. Lehne, *Working with Objects: The OOram Software Engineering Method*, Manning / Prentice Hall, 1996](https://archive.org/details/workingwithobjec0000reen) — ISBN 1-884777-10-4 (Manning) / 0-13-452930-8 (Prentice Hall), xxi + 366 pp. Fuera de imprenta; préstamo controlado en Internet Archive. **Además, y corregido el 2026-08-04**: el borrador libre completo está en [`1996/book/book11d.pdf`](https://folk.universitetetioslo.no/trygver/1996/book/book11d.pdf) — 466 pp., fechado el 1 de febrero de 2001, con nota de los autores en la portada («*This is a .pdf version of the last draft before publication*»). La URL que daba este draft antes, `1995/95Article/951010-paper.pdf`, es un paper suelto de Taskon de 14 páginas sobre modelado y bases de datos — **el error viene de la bibliografía de *The Roots of DCI*, que da esa misma URL equivocada**. estable.

**Autokon (la parte de los años sesenta)**

- [Trygve Reenskaug, *Applications and Technologies for Maritime and Offshore Industries — Technological Significance of Early Norwegian Applications*, en *History of Nordic Computing* (HiNC1, Trondheim 2003), IFIP AICT vol. 174, Springer, 2005, pp. 369-390](https://dl.ifip.org/db/conf/hinc/hinc2003/Reenskaug03.pdf) — DOI [`10.1007/0-387-24168-X_34`](https://doi.org/10.1007/0-387-24168-X_34). ⭐ **hallazgo 2026-08-04**: es la retrospectiva del propio autor sobre Autokon, y el abstract lo dice de entrada («*Autokon, a CAD/CAM system for ships, was one of the most important early Norwegian applications*»). El PDF de la biblioteca de IFIP es libre pero es un **escaneo sin capa de texto** (22 pp.), así que hay que leerlo a ojo. **Trampa de citación:** en el mismo volumen hay otro capítulo con título idéntico, de **Trond Vahl**, pp. 359-367, DOI `..._33` — son dos ponencias de la misma sesión, y los buscadores devuelven la de Vahl. **estable** (dl.ifip.org, HTTP 200 al 2026-08-04).
- [Trygve Reenskaug, *Administrative Control in the Shipyard*, preprint ICCAS, Tokio, agosto de 1973 (PDF, 11 pp.)](https://folk.universitetetioslo.no/trygver/1973/iccas/1973-08-ICCAS.pdf) — ⭐ el paper contemporáneo, escaneado por él mismo en 2003; ficha en [DUO](https://www.duo.uio.no/handle/10852/9175) (que hoy redirige a `nva.sikt.no`). Fig. 1 es Autokon. Es la fuente para Prokon-0 y los *Communicating Data Processes*: procesos que residen en la base de datos, pasivos, que se cargan a memoria al recibir un mensaje, con una tabla por proceso que decide qué procedimiento lo atiende — o sea, persistencia y despacho dinámico hechos a mano, que es exactamente lo que Simula no le daba. **frágil** (sitio personal en host universitario).
- E. Mehlum & P. F. Sørensen, *Example of an existing system in the ship-building industry: the Autokon system*, *Proceedings of the Royal Society A*, vol. 321, nº 1545, 9 de febrero de 1971, pp. 219-233 — DOI [`10.1098/rspa.1971.0028`](https://doi.org/10.1098/rspa.1971.0028). La descripción técnica contemporánea, por dos del equipo. De pago, y royalsocietypublishing devuelve **403 al fetch automatizado**; citar por DOI. Metadatos confirmados vía Crossref.
- [SINTEF, *1960: Digital shipbuilding*](https://www.sintef.no/en/sintef-group/timeline/1960-digital-shipbuilding/) — la versión institucional: Thomas Hysing al frente en el SI, prototipo de control numérico en Aker Stord, Kongsberg Våpenfabrikk fabricando las máquinas de dibujo y los sopletes, y Shipping Research Services vendiéndolo al mundo desde 1967. Útil para lo que Reenskaug no cuenta de sí mismo. **estable**.
- Para el paréntesis sobre persistencia: Malcolm Atkinson et al., *An Approach to Persistent Programming*, *The Computer Journal* 26(4), noviembre de 1983, pp. 360-365, DOI [`10.1093/comjnl/26.4.360`](https://doi.org/10.1093/comjnl/26.4.360) (el paper de PS-algol, donde se acuña la idea), y Atkinson & Morrison, *Orthogonally persistent object systems*, *The VLDB Journal* 4(3), julio de 1995, pp. 319-401, DOI [`10.1007/BF01231642`](https://doi.org/10.1007/BF01231642).

**Crítica y evidencia empírica**

- [Sadek Drobi, *Data, Context and Interaction: A New Architectural Approach*, InfoQ, 8 de mayo de 2009](https://www.infoq.com/news/2009/05/dci-coplien-reenskau/) — ⭐ la recopilación contemporánea de las objeciones. **Michael Feathers** y otros sostienen que poner la responsabilidad de la transferencia en la cuenta origen es arbitrario y no encaja con el modelo mental del usuario, donde la transferencia no la hace ninguna de las dos cuentas sino el banco o un objeto-transacción; **John Zabroski** propone en cambio una clase de análisis `TransferSlip`. Otros dicen que DCI no es más que traits, o la vieja idea funcional de que los algoritmos importan. Incluye las respuestas de Coplien y Reenskaug. **estable**.
- [Hector A. Valdecantos, *An empirical study on code comprehension: DCI compared to OO*, tesis de M.Sc. en Software Engineering, Rochester Institute of Technology, 2016](https://repository.rit.edu/theses/9245/) — ⭐ **el único experimento controlado con sujetos humanos que compara DCI contra OO**. Conclusión: el enfoque DCI-trygve produce código *más comprensible* y concentra mejor la atención en los archivos críticos, pero el estudio **no pudo determinar con significancia estadística** cuál de los dos enfoques permite resolver la tarea en menos tiempo. estable.
- Versión de conferencia del anterior: Valdecantos, Coplien et al., *An Empirical Study on Code Comprehension: Data Context Interaction Compared to Classical Object Oriented*, ICPC 2017, DOI [`10.1109/ICPC.2017.23`](https://doi.org/10.1109/ICPC.2017.23). IEEE Xplore y ACM DL devuelven 403 al fetch automatizado; el DOI resuelve.

**Sitios e implementaciones** _(el detalle por lenguaje vive en [[C-17]])_

- [fulloo.info](https://fulloo.info/) — el sitio del proyecto DCI. [Documentos](https://fulloo.info/Documents/) y [ejemplos por lenguaje](https://fulloo.info/Examples/). **frágil** → backup Wayback: `http://web.archive.org/web/20260520130201/https://www.fulloo.info/`
- [dci.github.io](https://dci.github.io/) — el sitio comunitario, más moderno. **frágil**.
- [`jcoplien/trygve`](https://github.com/jcoplien/trygve) — el lenguaje `trygve`, GPL-2.0, ~106 estrellas. El [manual de usuario](https://github.com/jcoplien/trygve/blob/master/doc/trygve.md) (13 de agosto de 2017) lo escribió Coplien. **estable** (GitHub).
- [Lista de correo `object-composition`](https://groups.google.com/g/object-composition) — la creó Coplien en 2008 y sigue siendo el foro donde se discute DCI. Reenskaug dice en *The Roots of DCI* que las discusiones de esa lista inspiraron buena parte de su trabajo posterior. **frágil** (Google Groups).

**Videos** _(URLs y títulos verificados vía oEmbed el 2026-08-03)_

- [James Coplien — *The DCI Architecture: Supporting the Agile Agenda*](https://www.youtube.com/watch?v=SxHqhDT9WGI) — la exposición canónica de Coplien. Subido por el canal «Xin Huang» (recompilación, no canal oficial — ojo con el bitrot). **frágil**.
- [*Discussion about DCI (Data Context Interaction) with James Coplien*](https://www.youtube.com/watch?v=-3hqqdnnzHE) — canal «Sensing Ontologies»; conversación informal grabada en el Code Camp de Timișoara, marzo de 2023. Lo más reciente de Coplien sobre DCI. **frágil**.
- [*DCI Tokyo 2 — Commonality / Variability Analysis: Practical MPD by James Coplien (Part 1 of 4)*](https://www.youtube.com/watch?v=4rgPBzR8nVg) — canal «DCI Tokyo». **frágil**.

**Biografías (Wikipedia)** _(todas verificadas por HTTP el 2026-08-03; van como lectura de contexto, no como cita primaria — ver «Convenciones de la casa»)_

| Persona | Español | Inglés |
| --- | --- | --- |
| Trygve Reenskaug | [es](https://es.wikipedia.org/wiki/Trygve_Reenskaug) | [en](https://en.wikipedia.org/wiki/Trygve_Reenskaug) |
| James O. Coplien | — | [en](https://en.wikipedia.org/wiki/James_O._Coplien) |
| Adele Goldberg | [es](https://es.wikipedia.org/wiki/Adele_Goldberg) | [en](https://en.wikipedia.org/wiki/Adele_Goldberg_(computer_scientist)) |
| Alan Kay | [es](https://es.wikipedia.org/wiki/Alan_Kay) | [en](https://en.wikipedia.org/wiki/Alan_Kay) |
| Kristen Nygaard | [es](https://es.wikipedia.org/wiki/Kristen_Nygaard) | [en](https://en.wikipedia.org/wiki/Kristen_Nygaard) |
| Ole-Johan Dahl | [es](https://es.wikipedia.org/wiki/Ole-Johan_Dahl) | [en](https://en.wikipedia.org/wiki/Ole-Johan_Dahl) |
| Douglas Engelbart | [es](https://es.wikipedia.org/wiki/Douglas_Engelbart) | [en](https://en.wikipedia.org/wiki/Douglas_Engelbart) |
| Ivar Jacobson | [es](https://es.wikipedia.org/wiki/Ivar_Jacobson) | [en](https://en.wikipedia.org/wiki/Ivar_Jacobson) |
| Rebecca Wirfs-Brock | [es](https://es.wikipedia.org/wiki/Rebecca_Wirfs-Brock) | [en](https://en.wikipedia.org/wiki/Rebecca_Wirfs-Brock) |
| Christopher Alexander | [es](https://es.wikipedia.org/wiki/Christopher_Alexander) | [en](https://en.wikipedia.org/wiki/Christopher_Alexander) |
| Fred Brooks | [es](https://es.wikipedia.org/wiki/Fred_Brooks) | [en](https://en.wikipedia.org/wiki/Fred_Brooks) |
| Grady Booch | [es](https://es.wikipedia.org/wiki/Grady_Booch) | [en](https://en.wikipedia.org/wiki/Grady_Booch) |
| Ward Cunningham | [es](https://es.wikipedia.org/wiki/Ward_Cunningham) | [en](https://en.wikipedia.org/wiki/Ward_Cunningham) |
| Peter Naur | [es](https://es.wikipedia.org/wiki/Peter_Naur) | [en](https://en.wikipedia.org/wiki/Peter_Naur) |
| Edsger W. Dijkstra | [es](https://es.wikipedia.org/wiki/Edsger_W._Dijkstra) | [en](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) |
| Robert C. Martin | [es](https://es.wikipedia.org/wiki/Robert_C._Martin) | [en](https://en.wikipedia.org/wiki/Robert_C._Martin) |
| Rich Hickey | — | [en](https://en.wikipedia.org/wiki/Rich_Hickey) |

**Sin artículo de Wikipedia** (verificado, 404 en ambos idiomas): **Michael Feathers**, **Gertrud Bjørnvig**, **Jim Gay**, **Arjan Molenaar**, **Andreas Söderlund**, **Hector A. Valdecantos**. Para éstos hay que enlazar sitio propio / repositorio institucional, o no enlazar.

**Conceptos con artículo propio**: [DCI (en)](https://en.wikipedia.org/wiki/Data,_context_and_interaction) — **no hay versión en español**; [Modelo–vista–controlador (es)](https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador); [Simula (es)](https://es.wikipedia.org/wiki/Simula); [Smalltalk (es)](https://es.wikipedia.org/wiki/Smalltalk).

**Imágenes:**

### ✅ Hero — listo, descargado y recortado (2026-08-03)

El archivo ya vive en el bundle del post: `content/es/posts/2026-08-04-dci-data-context-interaction-reenskaug/hero-manchester-baby.jpg` — **2560 × 1024 px, exactamente 2.5:1, 436 KB**, JPEG progresivo.

- **Origen**: [`File:SSEM Manchester museum.jpg`](https://commons.wikimedia.org/wiki/File:SSEM_Manchester_museum.jpg) en Wikimedia Commons — original 3477 × 2296, foto del 1 de noviembre de 2009.
- **Licencia**: **CC BY-SA 3.0**, autor **Parrot of Doom**, trabajo propio. `AttributionRequired: true` — la atribución **no es opcional**, y como es *ShareAlike* conviene que la footnote diga la licencia con nombre y enlace.
- **Qué se ve**: la réplica del *Manchester Baby* en el Museum of Science and Industry de Manchester. Se leen los carteles «Control and Arithmetic» y «Tube Separator» sobre los bastidores, y hay dos visitantes leyendo el panel explicativo a la izquierda, que dan escala humana.
- **Cómo se recortó**: se probaron tres encuadres (alto / centro / bajo) sobre el original. Se eligió el **alto** (`top=150`, ventana de 3477 × 1391) porque es el único que conserva los carteles legibles arriba y a la vez mantiene a los visitantes y la estructura completa de los bastidores; el centrado pierde los carteles y el bajo corta la parte superior de la máquina. Después se redimensionó a 2560 × 1024 con Lanczos y se guardó con `quality=86`, para quedar en el mismo rango que los heroes 2.5:1 recientes del blog (`1920×768` … `2560×1024`, 490–945 KB).
- **Por qué esta imagen y no otra**: no es decorativa. Reenskaug bautizó BabyUML —y después BabyDCI— **por esa máquina**, y lo explica en *The Roots of DCI*: «el primer computador electrónico digital de programa almacenado del mundo se llamaba "The Baby"». El post ya menciona el dato; el hero lo ilustra.
- **Footnote de atribución** (ya está puesta como `[^img_hero]` y referenciada inline donde el cuerpo menciona «The Baby»):
  `[^img_hero]: Imagen de [SSEM Manchester museum](https://commons.wikimedia.org/wiki/File:SSEM_Manchester_museum.jpg) — [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) — Parrot of Doom, 2009. Recortada a 2.5:1 para hero landscape.`

**Alternativas descartadas pero verificadas** (misma licencia CC BY-SA 3.0, por si se quiere cambiar): [`File:The-baby-replica-mosi-manchester-gt-britain-1.jpg`](https://commons.wikimedia.org/wiki/File:The-baby-replica-mosi-manchester-gt-britain-1.jpg) (1024 × 768 — alcanza justo para 2.5:1, sin margen para elegir encuadre) y [`File:Manchester Baby architecture.svg`](https://commons.wikimedia.org/wiki/File:Manchester_Baby_architecture.svg) (vectorial, es un diagrama y no una foto).

### Lo que falta

- **Diagrama mermaid**: sigue sin dibujarse. Ver más abajo por qué no se puede copiar el del paper.
- La foto de astillero noruego de los sesenta que sería ideal para el arranque de Autokon: se buscó en Wikimedia Commons el 2026-08-03 y **no hay resultados**; habría que ir al Nasjonalbiblioteket o a un museo marítimo noruego y verificar licencia ahí. **Descartada por ahora.**
- Retrato de Reenskaug: **no se verificó ninguna licencia** — no dar por sentado que la imagen del artículo de Wikipedia es libre.

### Sobre usar un diagrama del artículo original — la respuesta corta es que no se puede El paper de Artima tiene cinco figuras y la quinta es justo la que uno querría (*Figure 5. Mapping Roles to Objects*: el objeto Context mapeando identificadores de rol a objetos de dominio durante la ejecución del caso de uso; las otras cuatro son *Direct Manipulation*, *Model-View-Controller-User*, y las dos de *Combining Structure and Algorithm* en clase y en objeto). El problema es el pie de página: **«Copyright © 1996-2026 Artima, Inc. All Rights Reserved»** — sin licencia libre, sin CC, nada. Lo mismo vale para las figuras de los PDF de fulloo.info: *The Roots of DCI* trae cuatro imágenes (entre ellas el diagrama de comunicación de astillero que Reenskaug reusó de su paper de ICCAS de 1973) y el capítulo ASA trae otras cuatro (una es el Dynabook, otra la de *Design emergence*), y ninguna declara licencia de reuso.

Tres caminos, en orden de recomendación:

1. **Redibujar la figura 5, no copiarla.** Las ideas no son copiables; un diagrama propio que muestre lo mismo, sí. Es además lo que hace la casa: un diagrama mermaid, con `mermaid: true` en el frontmatter y —porque los rótulos van a llevar tildes y flechas— probablemente también `mermaid_html_labels: true` (ver `CLAUDE.md`). Propuesta concreta: el mismo par de cuentas visto dos veces, el diagrama de clases (lo que el sistema *es*) al lado del diagrama del contexto con los roles mapeados (lo que el sistema *hace*).
2. **Hero con licencia verificada — y hay uno que encaja perfecto.** [`File:SSEM Manchester museum.jpg`](https://commons.wikimedia.org/wiki/File:SSEM_Manchester_museum.jpg), la réplica del *Manchester Baby* en el museo de Manchester: **CC BY-SA 3.0**, autor «Parrot of Doom», **3477 × 2296 px** (sobra para recortar a 2.5:1). Verificado por API de Commons el 2026-08-03. No es un adorno: Reenskaug bautizó BabyUML/BabyDCI *por esa máquina*, y lo explica en *The Roots of DCI*. Alternativas del mismo tema y misma licencia: [`File:The-baby-replica-mosi-manchester-gt-britain-1.jpg`](https://commons.wikimedia.org/wiki/File:The-baby-replica-mosi-manchester-gt-britain-1.jpg) (CC BY-SA 3.0, 1024 × 768 — justo para 2.5:1, sin margen) y [`File:Manchester Baby architecture.svg`](https://commons.wikimedia.org/wiki/File:Manchester_Baby_architecture.svg) (CC BY-SA 3.0, vectorial).
3. **Pedir permiso.** Coplien es localizable y contesta correos. Para un blog personal probablemente sea desproporcionado, pero es la única vía legítima si se quiere la figura original tal cual.

**Descartado**: la foto de astillero noruego de los sesenta que sería ideal para el arranque de Autokon. Se buscó en Wikimedia Commons el 2026-08-03 y **no hay resultados**; habría que ir al Nasjonalbiblioteket o a un museo marítimo noruego y verificar licencia ahí. Tampoco se verificó ninguna foto retrato de Reenskaug — **no dar por sentado que la imagen del artículo de Wikipedia es libre**.

Atribución obligatoria del hero, con footnote nombrada: `[^img_hero]: Imagen de [SSEM Manchester museum](https://commons.wikimedia.org/wiki/File:SSEM_Manchester_museum.jpg) — CC BY-SA 3.0 — Parrot of Doom. Recortada a 2.5:1 para hero landscape.` Referenciarla inline donde se menciona «The Baby».

**Tags propuestos:** `['DCI','Reenskaug','MVC','arquitectura','OOP','Coplien','Smalltalk','Simula']`

**Estado actual:** ✅ **ESCRITO — pendiente de commit/push.** El post final vive en `content/es/posts/2026-08-04-dci-data-context-interaction-reenskaug/index.md`, con `hero-manchester-baby.jpg` en el bundle. Buildeado y verificado el 2026-08-03 (ver checklist abajo). **No está publicado todavía**: falta el commit y el push, que los hace César.

Decisiones editoriales que tomó César el 2026-08-03 y que quedaron aplicadas en el post final:

1. **Se menciona la muerte de Reenskaug** y el cierre pasa a tiempo pasado. El post cierra como homenaje al oficio: el arco de 1963 a 2024, alguien que a los 78 seguía tratando de arreglar lo que había ayudado a construir.
2. **Se eliminó por completo la sección del eco con Hickey.** Era una lectura del redactor, no de las fuentes. El post cierra ahora sólo con el eco en Clean Architecture. Se quitó el cross-link a [[C-02]].
3. **Sin anécdota del sector público.** El párrafo del síntoma quedó en framing genérico; el 🕳️ HUECO se cerró sin inventar nada.
4. **Clean Architecture no se enlaza a [[E-14]]** porque ese post **no está publicado** y el link daría 404. Se cita en su lugar el post original de Robert C. Martin (verificado, HTTP 200).

Pasada de verificación del 2026-08-04 (aplicada a los dos posts **y sincronizada en este draft**):

1. **Autokon quedó apoyado en fuentes de terceros**, no sólo en la autobiografía: capítulo de Reenskaug en HiNC1 (IFIP/Springer 2005), Mehlum & Sørensen en *Proc. R. Soc. A* (1971) y la ficha institucional de SINTEF. Nueva nota `[^autokon]`.
2. **«Máquinas de corte por llama» → «máquinas de oxicorte»**, que es el término del oficio en castellano (el original dice *flame cutter*).
3. **El obstáculo de Simula se explica**, no sólo se enuncia: los objetos morían con la corrida, no había persistencia. Nuevas notas `[^persistencia]` (PS-algol, 1983) y `[^iccas]` — y con ella un párrafo nuevo sobre el paper de ICCAS 1973, donde Reenskaug se construye a mano la persistencia y el despacho dinámico que Simula le negaba.
4. **La URL libre de *Working with Objects* estaba mal** (era la que da la bibliografía de *The Roots of DCI*, y apunta a otro paper). El borrador completo es `1996/book/book11d.pdf`, 466 pp.
5. **«Tres roles y no dos» quedó matizado**: el capítulo dice «*One possible mental model…*». Ver la entrada del ASA en la bibliografía.
6. **Se corrigió el ejemplo del descubierto.** Decía que hay contextos —«un ajuste contable, una acreditación de haberes»— donde la regla de saldo no aplica; una acreditación es un *crédito*, así que la regla ni siquiera entra en juego y el ejemplo no probaba nada. Ahora el argumento es que el piso del saldo depende del producto y del caso de uso (caja de ahorro vs. acuerdo de descubierto; comisiones y embargos que dejan en rojo).
7. **Todo el código y los diagramas pasaron a identificadores en inglés**, con los nombres canónicos de Coplien y Reenskaug: `Account`, `SourceAccount`, `DestinationAccount`, `MoneyTransferContext`, `Context`, `debit`/`credit`, `transfer`/`receive`. En el post 2 se re-corrió `dci_demo.py` y se reemplazaron los nueve bloques de salida por lo que imprime de verdad. Los `print()` del demo siguen en castellano, por decisión de César.
8. **«Factoriza» → «deja afuera»** en el pasaje sobre rol y clase como abstracciones opuestas; es lo que quiere decir el *factors out* de Reenskaug y en castellano se entendía como descomposición en factores.

Historial previo: seed cosechado de `draft-rest.md` el 2026-04-09; prosa completa el 2026-07-15; bibliografía reforzada el 2026-07-16; ampliación mayor el 2026-08-03; partido en dos posts el 2026-08-03.

**Checklist de pre-publicación, corrido contra el build (`hugo --buildFuture -d ...`):**

| Chequeo | Resultado |
| --- | --- |
| `hugo list future` | lista los dos posts (esperado: están fechados adelante) |
| Footnotes def/ref | 14 / 14, sin huérfanas en ninguna dirección |
| `[^` sueltos en el HTML | 0 |
| Links internos rotos | 0 de 15 |
| Bloques mermaid renderizados | 3 |
| URLs externas | 26/26 responden 200 |
| `localhost:` en `public/` | sólo el hit legítimo del post de Jekyll de 2016 |

Lo que cambió el 2026-08-03:

1. **Se encontró `The Roots of DCI`** (fulloo.info, PDF de 9 páginas, julio de 2010). Era la fuente faltante que sostenía `[^roots]`, y confirma —con palabras del propio Reenskaug— *todos* los datos que estaban marcados: el retiro en 1997, OOram demostrado en el primer OOPSLA de Portland en 1986, el rebautizo BabyUML→BabyDCI el 28 de agosto de 2008, y la cita sobre Coplien. **Cinco `[VERIFICAR:]` del cuerpo quedaron resueltos con esto.** Además aportó todo el material nuevo del arranque: Autokon, las 300 toneladas, el rechazo de Simula, las dos escuelas de OOP en PARC.
2. **Se encontró el capítulo ASA** (*The DCI Paradigm*, 45 pp.), que resuelve `[^asa]` y aporta las *shear layers*. Corrige un detalle: los roles del ejemplo bancario son **tres**, no dos — hay un rol `Transfer Amount`.
3. **Se agregaron todas las footnotes que estaban citadas y no tenían definición** (`[^mvc]`, `[^asa]`, `[^roots]`, `[^ooram]`, `[^obituario]`). Ya no queda ninguna referencia huérfana: 12 definidas, 12 referenciadas.
4. **Se agregó la tabla de biografías de Wikipedia** (ES + EN), con la verificación de quiénes **no** tienen artículo.
5. **Se resolvió la cuestión del hero, y el archivo ya está hecho.** La idea de usar un diagrama del artículo original **no es viable** (Artima es «All Rights Reserved»; las figuras de fulloo.info tampoco declaran licencia). En su lugar se bajó de Commons la foto de la réplica del *Manchester Baby* (CC BY-SA 3.0), se probaron tres encuadres y se recortó a **2560 × 1024 (2.5:1 exacto, 436 KB)**. Vive en el bundle del post. La footnote `[^img_hero]` ya está escrita y referenciada inline. Ya no queda `_a definir_`.
6. **Se corrigió un enlace mal copiado**: el *DCI Glossary* apuntaba al PDF del *DCI Execution Model*.
7. **Se partió el post en dos.** La implementación en Python —que era la mitad del borrador— se mudó completa a **[[C-17]]**, junto con su bibliografía específica (la librería `roles`, el tutorial de TypeScript, el bug de Python 3.13) y el script ejecutable. Este post quedó en ~2900 palabras y se lee solo. La sección «Por qué (casi) nadie lo usa» conserva el argumento pero delega la demostración técnica a C-17.

**Sigue pendiente (nada de esto se puede resolver sin César):**

- Los **tres 🕳️ HUECO** de este post: el caso del sector público (STG / Min. Cultura), cómo se cruzó con DCI, y si compra la comparación Reenskaug/Hickey. El cuarto hueco (el cierre en primera persona) también sigue acá; el de «¿intentaste aplicarlo?» se mudó a [[C-17]].
- El **`[VERIFICAR:]` del cierre**, que sigue abierto porque pide una decisión editorial de tono, no un dato. Los hechos ya están confirmados: Reenskaug nació el 21 de junio de 1930 y murió el 14 de junio de 2024, a los 93, una semana antes de cumplir 94; en 2009, cuando salió el paper de Artima, tenía 78.
- Resolver los `[[ID]]` a URLs reales al publicar — **incluido el link a [[C-17]]**. Como C-09 sale un día antes, durante 24 h el link a la parte 2 va a apuntar a un slug que todavía no existe: o se publican los dos bundles juntos (recomendado: Hugo los buildea a la vez y el enlace nunca queda roto), o el link se agrega en un segundo commit. Los cuatro enlaces a completar en el cuerpo son los `[la segunda parte](#)` / `[la parte 2](#)` con `#` de placeholder: apuntan a `/posts/dci-en-python-roles-en-runtime/` (**sin fecha y sin `/es/`**).
- **Imágenes**: el hero ✅ **ya está listo** (`hero-manchester-baby.jpg`, 2560 × 1024, CC BY-SA 3.0 atribuida). Falta **copiarlo al bundle** al correr `hugo new`, y falta **dibujar el diagrama mermaid** — eso sigue sin hacerse.

---

## Borrador de prosa

Hay una cosa que me pasa cada vez que abro un sistema orientado a objetos que no escribí yo. Miro las clases, entiendo perfectamente qué es cada una —`Account`, `Customer`, `LedgerEntry`, `Branch`—, y no tengo la menor idea de qué hace el sistema. El dominio está modelado con prolijidad de manual. El caso de uso, el que el usuario tenía en la cabeza cuando pidió el software, no está en ninguna parte. Está repartido en pedacitos de dos líneas dentro de once métodos de siete clases, y para reconstruirlo tengo que hacer el trabajo del compilador a mano.

Resulta que el tipo que inventó MVC piensa lo mismo, lo escribió, y propuso una salida. Se llama DCI —*Data, Context, Interaction*— y casi nadie la conoce. Este post cuenta de dónde salió y qué dice. En [la segunda parte](#) la escribimos en Python, la hacemos andar, y después la rompemos.

### El currículum obliga a escuchar

Trygve Reenskaug es el autor del patrón Model-View-Controller. Los dos documentos fundacionales siguen publicados en [su propia página](https://folk.universitetetioslo.no/trygver/): «[Thing-Model-View-Editor](https://folk.universitetetioslo.no/trygver/1979/mvc-1/1979-05-MVC.pdf)», del 12 de mayo de 1979, y «[Models-Views-Controllers](https://folk.universitetetioslo.no/trygver/1979/mvc-2/1979-12-MVC.pdf)», del 10 de diciembre de 1979. El primer nombre que le puso fue *Thing-Model-View-Editor*; el que quedó salió recién después de discutirlo largo con Adele Goldberg[^mvc]. Eso solo ya es raro de asimilar: MVC es probablemente la sigla más repetida de la historia del software de aplicación, la que aparece en el primer capítulo de todo tutorial de framework web desde hace veinte años, y tiene un autor con nombre, apellido y página personal todavía en línea en un servidor universitario noruego[^trygver]. Reenskaug fue profesor emérito de informática en la Universidad de Oslo —así firma él mismo sus papers de DCI[^asa]— y se había retirado en 1997, lo que hace que todo lo que sigue sea, literalmente, su proyecto de jubilación[^roots].

Pero MVC ni siquiera es el principio de la historia, y el principio vale la pena porque explica todo lo demás.

En los años sesenta Reenskaug trabajaba en Autokon[^autokon], un sistema CAD/CAM para diseño de barcos que entró en producción en 1963 y que terminaron usando la mayoría de los astilleros importantes del mundo[^autokon_sintef]. Y ahí pasó algo que él cuenta, cuarenta años después, como el origen de todo. El sistema guardaba el modelo del producto en una base de datos central[^autokon_rs]. Alguien vivo en el departamento de trazado se dio cuenta de que, si el modelo ya estaba en la base, se podían sacar directamente de ahí las cintas de control para las máquinas de oxicorte. Cortaron más de trescientas toneladas de acero antes de descubrir la diferencia entre *precisión* y *exactitud*: los datos tenían cuarenta bits de precisión, sí, pero las dimensiones seguían siendo tan aproximadas como en los planos 1:50 de los que habían salido[^roots].

Trescientas toneladas de chatarra y un tendal de dedos acusadores. Y —esto es lo interesante— Reenskaug concluyó que la culpa era del sistema, no del muchacho: antes, cada departamento era dueño de sus datos, y la transferencia entre departamentos estaba controlada, firmada por quien la mandaba y chequeada por quien la recibía. La base de datos común había roto ese patrón. No había dueño y no había control.

De ahí salió su obsesión: los sistemas de computación tienen que reflejar la estructura de responsabilidad de la organización real. Intentó construirlo con Simula —que Nygaard y Dahl acababan de inventar en el Norsk Regnesentral[^patio_nr], del otro lado del patio de su oficina[^patio]— y se dio contra dos paredes. Una: un programa Simula corría segundos o minutos, y sus objetos nacían y morían dentro de esa corrida; él necesitaba que la ejecución durara un año o más. Es el problema de la persistencia[^persistencia_survey], y en 1970 no tenía solución — «los objetos persistentes todavía estaban esperando ser inventados», anota él mismo entre paréntesis[^roots]; el término *persistent programming* aparece recién en 1983, con PS-algol[^persistencia]. La otra fue el verdadero problema: **Simula exigía que el emisor de un mensaje conociera la clase del receptor**[^roots]. Eso rompía la idea entera de componentes que se comunican por un protocolo estándar y son opacos por dentro. Chau Simula.

Sin lenguaje que le sirviera, se construyó las dos cosas a mano. En el paper que llevó a la conferencia ICCAS de Tokio, en agosto de 1973, describe el lenguaje Prokon-0 y su principio de *Communicating Data Processes*: los procesos viven guardados en la base de datos, pasivos la mayor parte del tiempo, y se cargan a memoria recién cuando les llega un mensaje; cuál procedimiento se ejecuta lo decide una tabla que cada proceso tiene para sí, de modo que el mismo mensaje puede ser atendido de manera diferente en procesos distintos[^iccas]. Persistencia y despacho dinámico, escritos a mano en un astillero noruego, treinta y cinco años antes de DCI.

El proyecto se cayó cuando se derrumbó el mercado de barcos nuevos, y con el tiempo libre que le quedó escribió los papers que después lo llevaron a Xerox PARC como científico visitante en 1978/79, al grupo de Smalltalk. Ahí las ideas encajaron. En el grupo, cuenta él, decían que había dos escuelas de orientación a objetos: la de la Costa Este, la de C++, «un artefacto de programación donde un objeto es una instancia de una clase y también una estructura de datos con métodos incorporados»; y la de la Costa Oeste, la de ellos, donde «la esencia de la orientación a objetos es que los objetos interactúan para realizar una tarea»[^roots]. Toda la historia posterior de DCI es un intento de escribir código donde esa segunda definición sea visible.

Si bien coincidía con la definición de orientación a objetos de Alan Kay, sus reparos apuntaban a dos supuestos de la *implementación* de Smalltalk. El primero: que si un objeto está programado «para hacer lo correcto», se va a portar bien cuando interactúe con otros. Anda en los casos simples y falla en los sistemas donde el valor del todo es mayor que la suma de las partes, porque ahí qué es «lo correcto» depende del sistema entero — es decir, del contexto. El segundo: que la clase sea la unidad ideal de reutilización. Las clases se diseñan de a conjuntos y fuera de su conjunto no sirven; el ejemplo que da es el framework, un montón de clases que se complementan y que están pensadas para subclasearse juntas. Su conclusión es de una línea: «las clases no son independientes, y hace falta un constructo de nivel más alto para especificar el todo»[^roots]. Treinta años después, ese constructo de nivel más alto es la C de DCI.

Y le siguió el paradigma de roles y el método OOram —*Object Oriented Role Analysis and Modeling*—, cuya primera herramienta demostró en el primer OOPSLA, en Portland, en 1986[^roots]. Llegó a formato libro como *Working with Objects: The OOram Software Engineering Method*, escrito con Per Wold y Odd Arild Lehne[^ooram]. Es la pista que importa para lo que sigue: Reenskaug venía pensando hace décadas que la unidad interesante no es el objeto, sino el **rol** que el objeto juega mientras algo pasa.

Y después, décadas más tarde, llegó DCI. Acá conviene ser preciso con las fechas, porque se citan mal todo el tiempo. El 28 de agosto de 2008 Reenskaug declaró que su proyecto BabyUML había llegado a su meta y lo rebautizó BabyDCI: esa «versión 2008» es la fecha de nacimiento del paradigma, y él mismo la escribe así[^roots]. El paper —*The DCI Architecture: A New Vision of Object-Oriented Programming*, firmado junto con James O. Coplien— se publicó en Artima recién el 20 de marzo de 2009[^dci]. O sea: la idea es de 2008, el paper es de 2009. Las dos fechas son correctas; lo que hay que decidir es de cuál de las dos cosas se está hablando.

Lo de «Baby», dicho sea de paso, tiene dos motivos. El primero es literal: la versión de 2008 era una criatura que él esperaba que creciera hasta convertirse en algo viable y potente. El segundo es una humorada con ambición: el primer computador electrónico digital de programa almacenado del mundo, en Manchester en 1948, se llamaba *The Baby*[^img_hero]. «Como todos sabemos, mucho vino después de ese comienzo endeble»[^roots].

Que DCI haya salido del escritorio de Reenskaug y llegado a alguna parte es obra de Coplien, y no hace falta que lo diga yo: lo dice Reenskaug. «Después de 2008, DCI salió al mundo bajo el liderazgo de James Coplien. Sin él, DCI habría quedado como una curiosidad oscura»[^roots]. Y es Coplien quien lo llevó a formato libro: *Lean Architecture for Agile Software Development* lo escribió con Gertrud Bjørnvig —no con Reenskaug[^lean]—, y es ahí donde la idea aparece desarrollada en serio y no en formato paper. El propio Reenskaug lo reseñó como «una lectura obligada para todos los que quieran entender la verdadera naturaleza del desarrollo de sistemas»[^roots].

Cuando el inventor de MVC dice, cuarenta años después, «che, esto se puede hacer mejor», uno se sienta a escuchar.

### El síntoma: ¿dónde está el comportamiento?

El diagnóstico de DCI es corto y es incómodo.

La orientación a objetos, tal como se practica, modela muy bien **lo que las cosas son**. Una `Account` tiene un saldo, un titular, un CBU. Eso es estable: la cuenta va a seguir siendo una cuenta el año que viene, y ese modelo casi no cambia. Hasta ahí, todo bien.

El problema es que el sistema no existe para que las cuentas sean cuentas. Existe para que alguien transfiera plata, pague un servicio, cierre un ejercicio. Eso es **lo que el sistema hace**, y es la parte que cambia todo el tiempo. Y en OOP clásica esa parte no tiene dónde vivir. Las opciones son dos, y las dos son malas.

La primera: metés el comportamiento adentro de los objetos de dominio. Entonces `Account` empieza a tener un método `transfer_to()`, y después `pay_bill()`, y después `apply_court_order()`, y a los tres años tu clase `Account` tiene mil quinientas líneas y sabe de juzgados. El objeto estable se contaminó con todos los casos de uso inestables que lo tocan.

La segunda: sacás el comportamiento afuera, a una capa de servicios. Entonces `Account` queda anémica —un montón de getters y setters, una fila de la base con disfraz— y toda la lógica vive en `TransferService`, que es un procedimiento con sombrero de objeto. Escribiste COBOL con llaves.

Coplien tiene un nombre prestado de la arquitectura de verdad para esto: las ***shear layers***, las capas de una construcción que evolucionan a ritmos distintos. Una casa necesita techo nuevo cada tantos años pero casi nunca necesita una pared exterior nueva, y una buena arquitectura pone interfaces limpias entre esas capas. La programación orientada a clases, dice, mete la evolución de los datos y la evolución de los métodos **en la misma capa**: la clase. Los datos tienden a ser estables; los métodos cambian todo el tiempo para dar servicios nuevos. Esa diferencia de ritmos es la que le hace fuerza al diseño hasta romperlo[^asa].

DCI dice que las dos opciones de arriba son malas porque las dos parten de una pregunta mal hecha. La pregunta no es «¿en qué clase pongo este método?». La pregunta es «¿por qué el caso de uso no es una cosa?».

> 🕳️ **HUECO — necesita a César:** ¿tenés un caso concreto de tu paso por el sector público (STG o Ministerio de Cultura) donde te pasó esto: abrir un sistema, entender las entidades y no encontrar el caso de uso por ningún lado? Una o dos frases con el sabor de la situación —qué buscabas, dónde terminó estando— anclan todo este párrafo en algo real en vez de en un ejemplo de manual.

### Las tres letras

La propuesta de DCI es partir el sistema en tres, y darle a cada parte un criterio de cambio distinto[^dci].

**Data** es lo que el objeto *es*. Chiquito, tonto, estable. La `Account` sabe su saldo y sabe sumarlo y restarlo, y nada más. Es el modelo de datos, y es la parte que dura décadas. Coplien lo llama, sin cariño y con precisión, *barely smart data*.

**Context** es la novedad, y es la letra que hace toda la fuerza. El caso de uso deja de ser un método suelto y pasa a ser **un objeto de primera clase**. `MoneyTransferContext` no es un servicio: es un contexto, una cosa que existe, que se instancia cuando la transferencia empieza y que muere cuando termina. Su trabajo es uno solo: agarrar los objetos de datos que participan y asignarles los roles que van a jugar en este caso de uso puntual.

**Interaction** es el guion. Los **roles** —`SourceAccount`, `DestinationAccount`— no son clases, no son objetos: son comportamiento que se le pega a un objeto de datos *mientras dura el contexto*. Y la interacción es el diálogo entre roles: el origen se debita, el destino se acredita, y listo.

Los nombres de los roles no se inventan, y ese es un punto en el que Reenskaug y Coplien insisten bastante: salen del modelo mental del usuario. «Podés reconstruirlos fácilmente pidiéndole a cualquiera que tengas cerca que te describa cómo se transfiere plata entre sus cuentas, y escuchando con atención lo que dice»[^asa]. Va a nombrar los objetos por el papel que juegan en la transacción. Eso es un rol.

La clave, la que hace que valga la pena todo el aparato, es esta: en el contexto vos leés el algoritmo completo del caso de uso, de corrido, en un lugar. Y se lee como el usuario lo cuenta. «Tomás fondos del origen, los ponés en el destino.» No hay que perseguirlo por siete archivos.

### El ejemplo que todo el mundo usa

El ejemplo canónico de DCI es la transferencia bancaria: es el que usan Reenskaug y Coplien en el paper de Artima, con un caso de uso de cajero automático[^dci], y el que desarrollan en el capítulo de arquitectura, donde dicen que «un modelo mental posible tiene **tres** roles»: *Source Account*, *Destination Account* y *Transfer Amount*[^asa]. Ese tercero es el interesante: el monto no es una entidad del dominio y sin embargo puede ser un rol. Un rol no tiene por qué corresponder a una tabla.

Es un ejemplo bien elegido porque parece trivial y no lo es.

En OOP clásica, si escribís `source.transfer_to(destination, amount)`, la `Account` origen ahora sabe qué es una transferencia. Sabe de comisiones, sabe de límites diarios, sabe de horarios de acreditación. Le cargaste un caso de uso a una entidad que existía **antes** de que ese caso de uso se inventara y que va a seguir existiendo cuando lo deroguen. Y ninguna de esas reglas es sobre lo que una cuenta *es*.

En DCI, `Account` no sabe nada de transferencias. Sabe debitar y acreditar, punto — como un entero sabe sumarse. Ni siquiera valida que no quedes en descubierto, porque el piso del saldo no es un dato de la cuenta: en una caja de ahorro es cero, en una cuenta corriente con acuerdo de descubierto es el negativo del acuerdo, y una comisión o un embargo te dejan en rojo sin preguntar. El contexto `MoneyTransferContext` toma dos cuentas cualesquiera, le dice a una «vos, en este rato, sos la `SourceAccount`» y a la otra «vos sos la `DestinationAccount`», y ejecuta el guion. La misma cuenta que hoy es origen mañana es destino, y no le agregaste ni una línea.

Y hay un detalle que a mí me parece el más lindo de toda la propuesta: los roles son **contextuales**. Un objeto no *tiene* un rol, un objeto *juega* un rol, y sólo mientras dura la obra. Cuando el contexto termina, la cuenta vuelve a ser una cuenta. Eso es mucho más parecido a cómo funciona el mundo real que la herencia, donde una vez que sos `SalariedEmployee` lo sos hasta que te destruyan.

Y —esto importa para lo que viene— el objeto tiene que **seguir siendo el mismo objeto** mientras juega el rol. No alcanza con envolverlo en un decorador y devolver otra cosa: la identidad se conserva. Ahí es donde la idea empieza a pedirle al lenguaje cosas que el lenguaje no quiere dar, y de eso se trata [la segunda parte](#).

La tesis fuerte, entonces, es esta: **el código tiene que leerse como el modelo mental del usuario**, no como el diagrama de clases del arquitecto. El diagrama de clases te dice qué hay. El contexto te dice qué pasa. Los usuarios no piensan en qué hay; piensan en qué pasa. Coplien lo dice más filoso: «vendemos casos de uso, no clases, y ni siquiera objetos»[^asa].

### Las críticas serias

Conviene no presentar esto como una idea perfecta que el mundo ignoró por tonto. Las objeciones aparecieron rápido y algunas son buenas.

La más citada es de Michael Feathers, y va al corazón del ejemplo: poner la responsabilidad de la transferencia en la cuenta origen **es arbitrario**. En el modelo mental del usuario, la transferencia no la hace ninguna de las dos cuentas; la hace el banco, o un objeto-transacción. John Zabroski propuso directamente una clase de análisis `TransferSlip` — el papelito de la transferencia — como el lugar donde vive esa lógica[^infoq]. Y es una crítica incómoda porque DCI se vende justamente por respetar el modelo mental del usuario. Si el ejemplo canónico no lo respeta, algo falla.

Otros dijeron que DCI no era nada nuevo: que son *traits* con otro nombre, o la vieja idea funcional de que los algoritmos importan y deberían poder escribirse de corrido. La respuesta de Coplien es que los traits son *una* forma de implementarlo y que otros constructos sirven igual; el valor está en separar el comportamiento estable del dominio de la lógica de negocio contextual, no en el mecanismo[^infoq]. Reenskaug, por su lado, contestó algo más duro y menos tranquilizador: que entender DCI exige adoptar una abstracción adicional —el rol— y que el rol es *la abstracción opuesta* a la clase. La clase deja afuera la identidad del objeto y se concentra en su construcción interna —atributos y métodos—; el rol hace lo contrario: deja afuera la construcción interna y se concentra en la identidad. Por eso, dice, DCI le resulta tan difícil a una persona formada en clases: «tratá de explicarle la noción de color a alguien completamente daltónico; tratá de explicarle la noción de rol a alguien centrado en clases»[^roots].

Uno puede leer eso como profundidad o como la respuesta de alguien que ya decidió que quien no entiende es porque no puede. Yo creo que hay las dos cosas.

Y después está la evidencia, que es escasísima: hay **un solo** experimento controlado con sujetos humanos comparando DCI con OO clásica, la tesis de maestría de Hector A. Valdecantos en el RIT, de 2016, con versión de conferencia en ICPC 2017[^valdecantos]. El resultado es honesto y moderado: el código DCI resultó **más comprensible** y logró que los programadores concentraran mejor la atención en los archivos que importaban, pero el estudio **no pudo mostrar con significancia estadística** que se resolviera la tarea en menos tiempo. Un experimento, con estudiantes, sobre un sistema chico. Es lo que hay. Cualquiera que te diga que DCI está probado —o refutado— está hablando de más.

### Por qué (casi) nadie lo usa

La respuesta tiene tres capas, y ninguna es «porque la idea es mala».

La primera es que **el lenguaje pelea en contra**. Para que DCI funcione de verdad necesitás poder inyectar comportamiento a un objeto en tiempo de ejecución, por la duración de un contexto, sin tocar su clase y sin que el objeto deje de ser él mismo. Java no hace eso. C# no hace eso. Los lenguajes con traits o mixins te dejan acercarte, pero la composición suele ser estática, decidida al definir el tipo y no al armar el contexto. Python y Ruby sí te dejan hacerlo — y el precio que se paga es exactamente el tema de [la parte 2](#), donde se ve la línea en la que se rompe. Coplien terminó escribiendo un lenguaje entero, `trygve`, precisamente para no tener que pelear; y `trygve` es un proyecto de GitHub con cien estrellas[^trygve].

La segunda es que **no hay ecosistema**. No hay un framework DCI con diez mil estrellas, no hay una generación de programadores que lo aprendió en la facultad, no hay ofertas de laburo que lo pidan. Y las ideas de arquitectura, guste o no, se propagan por framework y por oferta laboral, no por paper.

La tercera es la más honesta: **el beneficio recién se ve cuando el sistema es grande**. En un CRUD de cuatro pantallas, DCI es puro overhead: te hace escribir contextos y roles para algo que se resolvía con un método. El dolor que DCI cura es el de los sistemas de diez años y cien casos de uso, y para cuando llegás a ese dolor ya tenés cien mil líneas escritas del otro modo. El costo se paga por adelantado y el retorno llega tarde. Eso, en cualquier organización, se llama «no».

> 🕳️ **HUECO — necesita a César:** ¿cómo te cruzaste con DCI la primera vez —te lo recomendó alguien, saliste de un rabbit hole leyendo sobre MVC, apareció en una discusión de trabajo?

### Lo que sí sobrevivió

Lo interesante de las ideas que no ganan es que casi nunca desaparecen del todo: se filtran.

El diagnóstico de DCI —que el caso de uso merece ser una cosa y no un método perdido— es exactamente el mismo diagnóstico que hace Clean Architecture cuando pone los *use cases* en el centro y los convierte en objetos con nombre propio ([[E-14]]). La solución es distinta y bastante menos ambiciosa —los use cases de Clean Architecture son objetos comunes, no hay inyección de roles en ningún lado—, pero el síntoma que describe es idéntico. Alguien más llegó a la misma sala por otra puerta.

Y hay otro eco, más lateral. Cuando Rich Hickey ([[C-02]]) sostiene que el problema de la orientación a objetos es enredar identidad, estado y comportamiento en un mismo paquete, está señalando el mismo nudo que Reenskaug quiere desatar. Los dos quieren separar lo que la cosa *es* de lo que la cosa *hace*. Hickey lo resuelve sacando el comportamiento a funciones y dejando los datos desnudos; Reenskaug lo resuelve dejando los datos flacos y metiendo el comportamiento en roles contextuales. Vienen de tradiciones opuestas y coinciden en el diagnóstico. Cuando dos personas que no se ponen de acuerdo en nada coinciden en cuál es la enfermedad, conviene prestarle atención a la enfermedad.

> 🕳️ **HUECO — necesita a César:** ¿comprás la comparación Reenskaug/Hickey, o te parece forzada? Es una lectura mía y el post gana si la firmás o si la discutís explícitamente.

### Vale la pena igual

Yo no te voy a decir que uses DCI. No lo uso, no conozco a nadie que lo use, y ya expliqué por qué la economía no cierra.

Pero hay una categoría de lecturas que sirven aunque nunca escribas una línea de código en ese estilo, porque lo que te dejan no es una técnica: es una pregunta que después no te podés sacar de encima. DCI me dejó ésta: **¿por qué el caso de uso, que es la única razón por la que el sistema existe, es lo único que no tiene nombre en el código?**

Cada vez que abro una carpeta `services/` llena de clases terminadas en `Service`, con métodos de trescientas líneas que orquestan objetos anémicos, me acuerdo de que hay un noruego que a los ochenta y pico escribió que eso está mal y explicó por qué, y que tenía la autoridad de haber inventado la sigla que ese mismo framework tiene tatuada en el README.[VERIFICAR: dos cosas de esta frase, las dos para que las decidas vos. (1) **Reenskaug murió el 14 de junio de 2024**, una semana antes de cumplir 94 (nació el 21 de junio de 1930)[^obituario]; el párrafo está escrito como si viviera y el post saldría después de su muerte — decidir si se menciona, y si el cierre cambia de tono. (2) «a los ochenta y pico» no cuadra con el paper: en 2009 tenía 78. Sí cuadra con lo último que escribió de DCI (*Working with objects — in computer and mind*, con Coplien, enero de 2014, a los 83). Ajustar la edad o mover la referencia a los textos tardíos.]

Si querés seguir, hay una tarde entera de material y está todo libre. El paper de Artima es la puerta de entrada[^dci]. *The Roots of DCI* son nueve páginas autobiográficas que se leen como una charla de sobremesa y explican de dónde salió todo, chatarra de astillero incluida[^roots]. El libro de Coplien y Bjørnvig es el desarrollo largo[^lean]. Y si preferís que te lo cuenten, están las charlas de Coplien en video, incluida una conversación informal de 2023 que es lo más reciente que hay del tema[^videos].

> 🕳️ **HUECO — necesita a César:** un cierre en primera persona, dos o tres frases. ¿Qué te dejó DCI a vos —una técnica que descartaste, una pregunta que te quedó, una sospecha sobre cómo escribís hoy? El post necesita terminar con tu voz y no con una recomendación bibliográfica.

**Y si querés dejar de leer y empezar a escribir**: en [la segunda parte](#) implementamos todo esto en Python, de cero y sin librerías. Anda. Y después vemos exactamente en qué línea deja de andar.

---

### Apéndice: quién es quién

_(Nota para publicación: esta sección es opcional. Si se conserva, va al pie. Los enlaces son a Wikipedia como lectura de contexto; las citas del cuerpo apuntan a las fuentes primarias.)_

- **[Trygve Reenskaug](https://es.wikipedia.org/wiki/Trygve_Reenskaug)** (1930-2024), noruego. Autokon, MVC, OOram, DCI. Profesor emérito de la Universidad de Oslo.
- **[James O. Coplien](https://en.wikipedia.org/wiki/James_O._Coplien)** («Cope»), estadounidense. Comunidad de patrones, *Lean Architecture*, el lenguaje `trygve`. Sin artículo en Wikipedia en español.
- **[Adele Goldberg](https://es.wikipedia.org/wiki/Adele_Goldberg)**, del grupo de Smalltalk en Xerox PARC. Con ella discutió Reenskaug el nombre de MVC.
- **[Alan Kay](https://es.wikipedia.org/wiki/Alan_Kay)**, Smalltalk y el Dynabook. Reenskaug suscribía su definición de orientación a objetos; sus dos reparos, anotados en *The Roots of DCI*[^roots], eran a la implementación de Smalltalk, no a la definición.
- **[Kristen Nygaard](https://es.wikipedia.org/wiki/Kristen_Nygaard)** y **[Ole-Johan Dahl](https://es.wikipedia.org/wiki/Ole-Johan_Dahl)**, los autores de [Simula](https://es.wikipedia.org/wiki/Simula), del otro lado del patio de la oficina de Reenskaug.
- **[Douglas Engelbart](https://es.wikipedia.org/wiki/Douglas_Engelbart)**, la computadora como extensión del intelecto humano.
- **[Ivar Jacobson](https://es.wikipedia.org/wiki/Ivar_Jacobson)**, los casos de uso — que en la lectura de Coplien quedaron «al lado de, pero no en el centro de» la arquitectura.
- **[Rebecca Wirfs-Brock](https://es.wikipedia.org/wiki/Rebecca_Wirfs-Brock)**, diseño dirigido por responsabilidades y las tarjetas CRC. Coplien cuenta que quiso rebautizarlas «RRC» —*Roles*, Responsibilities, Collaborators— y que al final dejó la sigla intacta y reemplazó *Class* por *Candidate*, «como un rol». La fuente es un correo privado de ella a Coplien, del 14 de octubre de 2009 (ref. [54] del capítulo), citado en el capítulo de arquitectura[^asa].
- **[Christopher Alexander](https://es.wikipedia.org/wiki/Christopher_Alexander)**, el arquitecto (de edificios) del que salió la idea de patrones.
- **Michael Feathers**, el crítico más citado de DCI. No tiene artículo en Wikipedia.
- **Gertrud Bjørnvig**, coautora de *Lean Architecture*. No tiene artículo en Wikipedia.

---

[^dci]: [Trygve Reenskaug & James O. Coplien, *The DCI Architecture: A New Vision of Object-Oriented Programming*, Artima, 20 de marzo de 2009](https://www.artima.com/articles/the-dci-architecture-a-new-vision-of-object-oriented-programming) — título y fecha verificados por fetch (2026-07-16 y 2026-08-03); el paradigma se gestó en 2008, el paper es de 2009. Backup Wayback: `http://web.archive.org/web/20260703092833/https://www.artima.com/articles/the-dci-architecture-a-new-vision-of-object-oriented-programming`.
[^roots]: [Trygve Reenskaug, *The Roots of DCI*, julio de 2010 (PDF)](https://fulloo.info/Documents/2010DCI-Origin.pdf) — nueve páginas autobiográficas escritas como respuesta a una pregunta en la lista `object-composition`. De acá salen Autokon y las 300 toneladas, el rechazo de Simula, PARC 1978/79, OOram en el primer OOPSLA (Portland, 1986), el retiro en 1997, el rebautizo BabyUML→BabyDCI el 28 de agosto de 2008, el chiste con «The Baby» de Manchester (1948), y la frase «sin él, DCI habría quedado como una curiosidad oscura» sobre Coplien. Verificado por fetch (2026-08-03).
[^asa]: [James O. Coplien & Trygve Reenskaug, *The DCI Paradigm: Taking Object Orientation Into the Architecture World* (PDF)](https://fulloo.info/Documents/CoplienReenskaugASA2012.pdf) — capítulo de *Agile Software Architecture* (Elsevier/Morgan Kaufmann, 2014); la copia de fulloo.info está fechada 2013. Es la fuente de la afiliación de Reenskaug tal como él la firma («Professor Emeritus of Informatics, University of Oslo»), del argumento de las *shear layers*, del modelo mental de tres roles del ejemplo bancario —textual: «*One possible mental model has three Roles: Source Account, Destination Account, and Transfer Amount*»— y de «vendemos casos de uso, no clases, y ni siquiera objetos». Verificado por fetch (2026-08-03).
[^mvc]: [Página de MVC en el sitio del propio Reenskaug](https://folk.universitetetioslo.no/trygver/themes/mvc/mvc-index.html), que es donde está la frase: «*After long discussions, particularly with Adele Goldberg, we ended with the terms Model-View-Controller*». **Corrección 2026-08-04:** los dos papers de 1979 —que el cuerpo enlaza directamente— **no** mencionan a Goldberg; se extrajo su texto para comprobarlo. La atribución sale de esta página índice, no de los papers.
[^trygver]: [Página personal de Trygve Reenskaug](https://folk.universitetetioslo.no/trygver/) — sus documentos originales, incluidos los de MVC (1979) y los de roles/OOram. Verificada por fetch (2026-07-16): el dominio histórico `folk.uio.no/trygver/` responde pero hace 301 al nuevo host canónico `folk.universitetetioslo.no/trygver/` (Universidad de Oslo).
[^ooram]: Trygve Reenskaug, con Per Wold y Odd Arild Lehne, *Working with Objects: The OOram Software Engineering Method*, Manning / Prentice Hall, 1996; ISBN 1-884777-10-4 (Manning) / 0-13-452930-8 (Prentice Hall), xxi + 366 pp. Fuera de imprenta. Hay dos maneras de leerlo: **el libro**, [en préstamo controlado en Internet Archive](https://archive.org/details/workingwithobjec0000reen), y **el borrador**, [libre en el sitio de la Universidad de Oslo](https://folk.universitetetioslo.no/trygver/1996/book/book11d.pdf) — PDF de 466 páginas fechado el 1 de febrero de 2001, sin el paso del *copy editor* pero, dicen los autores en la portada, con el contenido del libro impreso. Ése es el link correcto: la bibliografía de *The Roots of DCI* lo da mal, apuntando a `1995/95Article/951010-paper.pdf`, que es otro paper de catorce páginas y sobre otro tema.
[^autokon]: La retrospectiva del propio Reenskaug sobre el proyecto: [*Applications and Technologies for Maritime and Offshore Industries — Technological Significance of Early Norwegian Applications*, en *History of Nordic Computing* (HiNC1, Trondheim 2003), IFIP AICT vol. 174, Springer, 2005, pp. 369-390](https://dl.ifip.org/db/conf/hinc/hinc2003/Reenskaug03.pdf) — DOI [`10.1007/0-387-24168-X_34`](https://doi.org/10.1007/0-387-24168-X_34). El PDF gratuito de la biblioteca de IFIP es un escaneo de 22 páginas, sin capa de texto. Ojo al citarlo: en el mismo volumen hay otro capítulo con título idéntico, de Trond Vahl, pp. 359-367 (DOI `..._33`), y es el que devuelven los buscadores.
[^autokon_sintef]: [SINTEF, *1960: Digital shipbuilding*](https://www.sintef.no/en/sintef-group/timeline/1960-digital-shipbuilding/) — la versión del instituto donde se hizo: el proyecto arrancó en el SI (Sentralinstitutt for industriell forskning) con Thomas Hysing a la cabeza, el control numérico prototipo se instaló en Aker Stord, Kongsberg Våpenfabrikk fabricó las máquinas de dibujo y los sopletes, y desde 1967 Shipping Research Services lo vendió al mundo.
[^autokon_rs]: La descripción técnica contemporánea, por dos del equipo: E. Mehlum & P. F. Sørensen, *Example of an existing system in the ship-building industry: the Autokon system*, *Proceedings of the Royal Society A*, vol. 321, nº 1545, 9 de febrero de 1971, pp. 219-233 — DOI [`10.1098/rspa.1971.0028`](https://doi.org/10.1098/rspa.1971.0028). De pago, y royalsocietypublishing rechaza el acceso automatizado; no hay copia libre. Metadatos confirmados vía Crossref.
[^patio]: El patio es textual: «*Simula had been invented by Nygaard and Dahl at the Norwegian Computing Center across the yard from my office*», escribe Reenskaug en *The Roots of DCI*. Y es un patio de verdad: el SI —Sentralinstitutt for industriell forskning, donde él trabajaba— se había mudado en 1956 a un edificio nuevo en **Gaustad**, al lado del campus universitario de Blindern ([Wikipedia en noruego](https://no.wikipedia.org/wiki/Sentralinstitutt_for_industriell_forskning)). Así firmaba él sus papers de la época: «Central Institute for Industrial Research, Blindern, Oslo 3».
[^patio_nr]: El [Norsk Regnesentral](https://no.wikipedia.org/wiki/Norsk_Regnesentral) se mudó a su sede actual —el **Kristen Nygaards hus**, Gaustadalléen 23a— recién en 1988, así que ése no es el edificio de esta historia. Qué edificio ocupaba en los años sesenta **no está documentado en ninguna fuente pública** que se haya podido consultar (2026-08-04: se revisaron la historia oficial de NR, ambas Wikipedias, SNL y el paper de Elgsaas & Hegna sobre el Univac 1107 en HiNC1 — ninguno da la dirección de esos años; la pista abierta es el libro conmemorativo *Norsk Regnesentral 1952-2002*, que no está en línea).
[^iccas]: [Trygve Reenskaug, *Administrative Control in the Shipyard*, preprint para la conferencia ICCAS, Tokio, agosto de 1973 (PDF, 11 pp.)](https://folk.universitetetioslo.no/trygver/1973/iccas/1973-08-ICCAS.pdf) — escaneado por el propio autor en 2003 y publicado en su sitio de la Universidad de Oslo; ficha en el repositorio [DUO](https://www.duo.uio.no/handle/10852/9175). La figura 1 es Autokon. De acá salen Prokon-0, los *Communicating Data Processes*, los procesos que residen en la base de datos y la tabla por proceso que resuelve qué procedimiento atiende cada mensaje. Firma como profesor del Central Institute for Industrial Research, Blindern, Oslo.
[^persistencia]: El paper de PS-algol, donde se acuña la idea: Malcolm Atkinson, P. J. Bailey, K. J. Chisholm, W. P. Cockshott & R. Morrison, *An Approach to Persistent Programming*, *The Computer Journal*, vol. 26, nº 4, noviembre de 1983, pp. 360-365 — DOI [`10.1093/comjnl/26.4.360`](https://doi.org/10.1093/comjnl/26.4.360).
[^persistencia_survey]: El panorama del problema, doce años más tarde y con el campo ya maduro: Malcolm Atkinson & Ronald Morrison, *Orthogonally persistent object systems*, *The VLDB Journal*, vol. 4, nº 3, julio de 1995, pp. 319-401 — DOI [`10.1007/BF01231642`](https://doi.org/10.1007/BF01231642).
[^lean]: [James O. Coplien & Gertrud Bjørnvig, *Lean Architecture for Agile Software Development*, Wiley, 2010](https://books.google.com/books/about/Lean_Architecture.html?id=lpvY36MPMUwC) — ISBN-13 978-0-470-68420-7. Verificado por fetch (2026-07-16): el coautor es **Gertrud Bjørnvig**, no Reenskaug. No se halló copia en préstamo controlado (archive.org) al 2026-08-03.
[^trygve]: [`jcoplien/trygve`](https://github.com/jcoplien/trygve) — el lenguaje DCI de Coplien, GPL-2.0, construido con OpenJDK 17 + Gradle; ~106 estrellas al 2026-08-03. [Manual de usuario](https://github.com/jcoplien/trygve/blob/master/doc/trygve.md), escrito por Coplien, fechado el 13 de agosto de 2017.
[^infoq]: [Sadek Drobi, *Data, Context and Interaction: A New Architectural Approach*, InfoQ, 8 de mayo de 2009](https://www.infoq.com/news/2009/05/dci-coplien-reenskau/) — recopilación de las objeciones contemporáneas al paper de Artima, incluidas las de Michael Feathers (la responsabilidad en la cuenta origen es arbitraria) y John Zabroski (`TransferSlip`), con las respuestas de Coplien y Reenskaug.
[^valdecantos]: [Hector A. Valdecantos, *An empirical study on code comprehension: DCI compared to OO*, tesis de M.Sc. en Software Engineering, Rochester Institute of Technology, 2016](https://repository.rit.edu/theses/9245/) — el único experimento controlado con sujetos humanos que compara los dos enfoques. Versión de conferencia: ICPC 2017, DOI [`10.1109/ICPC.2017.23`](https://doi.org/10.1109/ICPC.2017.23) (IEEE Xplore y ACM DL bloquean el fetch automatizado; el DOI resuelve).
[^videos]: Charlas de James Coplien sobre DCI: [*The DCI Architecture: Supporting the Agile Agenda*](https://www.youtube.com/watch?v=SxHqhDT9WGI); [*Discussion about DCI (Data Context Interaction) with James Coplien*](https://www.youtube.com/watch?v=-3hqqdnnzHE), grabada en el Code Camp de Timișoara en marzo de 2023; y la serie [*DCI Tokyo 2 — Commonality / Variability Analysis*](https://www.youtube.com/watch?v=4rgPBzR8nVg) (4 partes). Títulos y disponibilidad verificados vía oEmbed el 2026-08-03.
[^obituario]: Trygve Mikkjel Heyerdahl Reenskaug, 21 de junio de 1930 – 14 de junio de 2024. Ver [su artículo en Wikipedia](https://es.wikipedia.org/wiki/Trygve_Reenskaug) y [la versión en inglés](https://en.wikipedia.org/wiki/Trygve_Reenskaug). **Pendiente para publicación**: buscar una fuente primaria (obituario de la Universidad de Oslo, o el aviso de Fonus Begravelsesbyrå) en vez de citar Wikipedia para un dato biográfico — ver «Convenciones de la casa».
[^img_hero]: Imagen de [SSEM Manchester museum](https://commons.wikimedia.org/wiki/File:SSEM_Manchester_museum.jpg) — [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) — Parrot of Doom, 2009. Réplica del *Manchester Baby* en el Museum of Science and Industry. Recortada a 2.5:1 para hero landscape.
