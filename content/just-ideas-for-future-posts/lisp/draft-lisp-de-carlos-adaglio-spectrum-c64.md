### A2-05 — El LISP de Carlos Adaglio (Lisp en el Spectrum)

- **Archivo seed:** `dev/draft-lisp-de-carlos-adaglio.md`
- **Slug propuesto:** `lisp-de-carlos-adaglio-spectrum-c64`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-lisp-de-carlos-adaglio-spectrum-c64/index.md`
- **Serie:** A2 — cross con [[A1-07]] (cultura Spectrum), [[I-03]] (versión local del mismo tema)
- **Cross-links:** depende de [[A1-07]]; lleva a [[A2-01]] (SICP, ¿se podía aprender desde acá?), [[E-01]] (cómo llegué al software libre)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** short (700-1000 palabras)

**Concepto:** un Lisp para Spectrum/C64 portado por un autor latinoamericano (Carlos Adaglio, vía Compusyst en su momento) es un artefacto cultural y técnico al mismo tiempo: prueba que en máquinas de 48 KB se podía correr el lenguaje "del MIT". La memoria personal se cruza con lo poco que queda en archivos públicos de retrocomputing.

**Hook:** "el primer Lisp que vi en mi vida cabía en una Spectrum de 48 KB. Lo había portado un argentino. Y fue la primera vez que entendí que un lenguaje no tiene por qué ser pesado para ser poderoso."

**Outline:**
1. Memoria personal: cómo apareció ese Lisp, cómo lo usé, qué lograba hacer.
2. Lisp en máquinas de 8-bit: por qué era plausible (intérpretes pequeños, garbage collectors simples, REPL friendly).
3. Otros Lisps en la misma época: ZX Spectrum, C64, Apple II, Z80 Lisp.
4. Quién era Carlos Adaglio (revisar fuentes locales, archivar la información antes de que se pierda).
5. Cierre: lo que un Lisp de 48 KB me enseñó que ningún tutorial moderno me iba a enseñar.

**Bibliografía:** *(pasada de fuentes 2026-07-15: todas las URLs de abajo fueron fetcheadas y verificadas salvo donde se indique lo contrario)*

*El Lisp de la Spectrum — fuente primaria*
- [Eugene Zaikonnikov, *Serious Software SpecLisp for Sinclair ZX Spectrum*](https://blog.funcall.org/lisp/2015/10/30/zx-spectrum-lisp/) (2015-10-30) — **frágil** (blog personal), load-bearing. Backup Wayback: [snapshot 2026-03-09](http://web.archive.org/web/20260309012227/http://blog.funcall.org//lisp/2015/10/30/zx-spectrum-lisp/). **Es la fuente real**: el artículo de Vintage is The New Old es una nota *sobre* este post. Aporta: SpecLisp desciende de Lisp 1.5 (usa marcadores de plist `PNAME` y `APVAL`), binding dinámico con el problema FUNARG sin resolver, `QUOTE` explícito sin azúcar, FFI vía propiedad `SUBR` del plist, case-sensitive y lowercase por defecto, y una extensión de gráficos tipo tortuga (Logo) que sugiere intención educativa.
- [Eugene Zaikonnikov, *A tiny Lisp bytecode interpreter in Z-80 assembly*](https://blog.funcall.org/lisp/2018/07/03/spectrum-lisp-vm/) (2018-07-03) — **frágil** (blog personal). Su propio intérprete de bytecode Lisp para Spectrum, basado en el AIM-514 del MIT, con GC mark-and-sweep. Útil para la sección 2. Ojo: **no da cifras de footprint en bytes** — no inventarlas.
- [LISP Interpreter (SpecLisp) — ficha 8718, Spectrum Computing](https://spectrumcomputing.co.uk/entry/8718/ZX-Spectrum/LISP_Interpreter) — **frágil** (base de datos comunitaria). Backup Wayback: [snapshot 2025-01-15](http://web.archive.org/web/20250115002710/https://spectrumcomputing.co.uk/entry/8718/ZX-Spectrum/LISP_Interpreter). **Datos verificados de la ficha:** publisher *Serious Software (UK)*, año **1983**, ZX-Spectrum 48K, idioma inglés, precio £15.00, género "Programming: General", **sin autor individual acreditado**. Reseñas en Personal Computer News y ZX Computing (1983). Descargable en TAP/TZX (v1.3).
- [LISP — ficha 20318, Spectrum Computing](https://spectrumcomputing.co.uk/entry/20318/ZX-Spectrum/LISP) — **frágil**. Un *segundo* Lisp para Spectrum, distinto del 8718: publisher *AFI Software (UK)*, **1985**, 48K, £15.00, estado **MIA** (no preservado). Sin autor acreditado. Publicitado en Popular Computing Weekly y Your Computer. Relevante: hubo más de un Lisp para la máquina, así que "el Lisp de la Spectrum" no es unívoco.

*Lisp en micros modestos (sección 2 y 3)*
- [muLISP-87 Reference Manual](https://archive.org/details/mu-lisp-87-reference-manual-ocr-final) — **estable** (archive.org, descarga libre, PDF + texto completo). Soft Warehouse, 1988, versión MS-DOS. Descripción verificada: "muLISP was a small but efficient LISP system for microcomputers"; **nació en CP/M dentro de 64 KB** y después se portó a MS-DOS; fue la base de muSIMP, muMATH y finalmente Derive. Es *la* cita para "un Lisp serio entraba en 64 KB".
- [Microsoft MULISP-83 (1983)](https://archive.org/details/microsoft-mulisp) — **estable** (archive.org, descarga libre). Contemporáneo exacto de SpecLisp. Nota: Microsoft licenció los productos muLISP de Soft Warehouse entre 1980 y 1986.
- [LISP 64 por Hamster (2014), CSDb](https://csdb.dk/release/?id=130534) — **frágil** (base de datos de la escena C64). Versión corregida del **LISP 64 de Peter Feldtmann, publicado originalmente en INPUT 64 04/1986**. Es el Lisp de C64 concreto para la sección 3 (el draft menciona C64 en el slug pero no lo desarrolla).

*Las Lisp machines — el contraste*
- Guy L. Steele Jr. y Gerald J. Sussman, **"Design of a LISP-based microprocessor"**, *Communications of the ACM*, vol. 23, núm. 11, noviembre de 1980, pp. 628-645. DOI: [10.1145/359024.359031](https://doi.org/10.1145/359024.359031) — **estable**. Datos de revista/volumen/número/páginas **verificados vía `api.crossref.org`** (el fetch directo a ACM DL no se intentó por política del sitio). Versión previa: AI Memo **AIM-514** del MIT AI Lab, marzo de 1979, 75 pp., con el título largo *"Design of LISP-based Processors, or SCHEME: A Dielectric LISP, or Finite Memories Considered Harmful, or LAMBDA: The Ultimate Opcode"*. Reemplaza con ventaja a la cita de Wikipedia para el punto "hardware especializado para Lisp".
- [Software Preservation Group — LISP](https://softwarepreservation.computerhistory.org/LISP/index.html) y [SCHEME family](https://softwarepreservation.computerhistory.org/LISP/scheme_family.html), Computer History Museum, ed. Paul McJones — **estable** (dominio institucional aprobado). Índice curado de implementaciones históricas de Lisp; incluye la Herbert Stoyan Collection. Es un finding aid, no un repositorio de textos.

*Lisp 1.5 — la raíz de SpecLisp*
- John McCarthy, **"Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I"**, *Communications of the ACM*, vol. 3, núm. 4, abril de 1960, pp. 184-195. DOI: [10.1145/367177.367199](https://doi.org/10.1145/367177.367199) (vol/núm/páginas verificados vía `api.crossref.org`). Texto libre en **el sitio propio de McCarthy**: [www-formal.stanford.edu/jmc/recursive.html](http://www-formal.stanford.edu/jmc/recursive.html) — **estable** (dominio institucional; ojo: el alias `jmc.stanford.edu` tiene el certificado roto, usar `www-formal`). Regla de la casa: el archivo del autor antes que Wikipedia.
- [LISP 1.5 Programmer's Manual (2ª ed., 1985) — colección bitsavers en archive.org](https://archive.org/details/bitsavers_mitrlelisprammersManual2ed1985_9279667) — **estable**, descarga libre (PDF 8.8M + texto completo). Edición canónica: McCarthy, Abrahams, Edwards, Hart y Levin, MIT Press. Sirve para verificar los marcadores `PNAME`/`APVAL` que Zaikonnikov usa para datar el linaje de SpecLisp.

*El eslabón argentino (pista de investigación, no resultado)*
- [La Spectrum en Argentina](https://czspectrum.speccy.org/enarg.html), Speccy — **frágil**. Verificado: la Spectrum fue segunda en el mercado local, muy detrás del C64 fabricado por Drean; clon Timex Sinclair 2068; versión MSX de Talent; revistas **K64** y **Programación Popular**; comercios **Valente Computación** y **Real-Time** donde se copiaban casetes. **No menciona ni a Compusyst ni a Adaglio.**
- [Programación Popular — colección en archive.org](https://archive.org/details/ProgramacionPopular) — **estable**, descarga libre con **texto completo OCR buscable**. Revista argentina en castellano, 36 números, diciembre 1984 – noviembre 1987. Faltan los números 18 y 25-36. **Es la mejor pista concreta que queda**: el OCR permite buscar "Adaglio" y "Compusyst" número por número. Pendiente de hacer.
- **Pendiente:** buscar en la colección OCR de Programación Popular y en K64; contactar a la comunidad de retrocomputing argentina. Ver la nota de premisa en `Estado actual`.

*Fuentes descartadas en la pasada del 2026-07-15 (no volver a agregarlas sin verificar)*
- ~~`iment.com/maida/computer/lisp-ptrs/lp-i.1.50-2.htm`~~ (citada en el draft anterior como "Lisp Pointers, abril 1987 — Lisp Implementations") — **no verificable**: el dominio devuelve error de certificado TLS ("unable to verify the first certificate") y el snapshot de Wayback existe (20250807171148) pero no se pudo abrir desde esta herramienta. **No se pudo confirmar que el documento diga lo que el draft le atribuía**, así que se eliminó la afirmación "los surveys de la época listan implementaciones de Lisp para hardware sorprendentemente modesto" que dependía de ella, y se la reemplazó por los casos concretos de muLisp, SpecLisp, AFI y LISP 64, todos verificados. Si alguien logra abrir el documento, puede volver.
- ~~`vintageisthenewold.com/program-in-lisp-using-the-zx-spectrum`~~ — se fetcheó y es real, pero es una **nota derivada** que comenta el post de Zaikonnikov y ni siquiera da el año del producto. Se la reemplazó por la fuente primaria (regla de la casa: el autor antes que el rebote).
- ~~`en.wikipedia.org/wiki/Lisp_machine`~~ — reemplazada por Steele & Sussman (CACM 1980) + el archivo del Computer History Museum. Wikipedia queda como lectura de contexto, no como cita.
- ~~`archive.org/search?query=mulisp`~~ — era una URL de *búsqueda*, no de ítem. Reemplazada por los dos ítems concretos (muLISP-87 Reference Manual y MULISP-83), ambos verificados y de descarga libre.

**Imágenes:**
- _Wikimedia_: [ZX Spectrum 48k](https://commons.wikimedia.org/wiki/File:ZXSpectrum48k.jpg) — license: CC-BY-SA — la máquina.
- _Crear_: screenshot del REPL Lisp de Spectrum corriendo en un emulador moderno (Fuse o ZEsarUX) (~15 min).
- _Pendiente de búsqueda_: scan de la documentación original (si existe en algún archivo personal).

**Tags propuestos:** `['LISP', 'ZX Spectrum', 'Carlos Adaglio', 'Argentina', 'retrocomputing']`

---

## Borrador de prosa

El primer Lisp que vi en mi vida entraba en una Spectrum de 48 KB. Eso es menos memoria que la que hoy ocupa el ícono de una aplicación en tu teléfono, y ahí adentro había un intérprete completo del lenguaje del que todo el mundo hablaba con reverencia: el lenguaje del MIT, el de la inteligencia artificial, el que corría en máquinas carísimas diseñadas especialmente para él.

Y sin embargo estaba ahí, en una máquina de cassette, en un living argentino.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegó ese Lisp a tus manos? ¿Cassette copiado de un amigo, revista, comprado en un local, bajado de un BBS? Una o dos frases con la escena concreta.

> 🕳️ **HUECO — necesita a César:** ¿en qué máquina lo corrías, y en qué año, aproximadamente? ¿Spectrum propia, prestada, del club, de la escuela?

> 🕳️ **HUECO — necesita a César:** ¿qué llegaste a hacer con él? No hace falta que sea impresionante — al contrario, si fue «escribí un factorial recursivo y me quedé mirando la pantalla», eso es exactamente lo que quiero contar.

> 🕳️ **HUECO — necesita a César:** ¿tenías documentación? ¿Un manual fotocopiado, hojas escritas a máquina, nada? Y si tenías: ¿en español o en inglés?

### Por qué un Lisp entraba ahí

Cuando uno se entera de que existieron las Lisp machines —computadoras enteras diseñadas alrededor del lenguaje, al punto de que Steele y Sussman publicaron en 1980 el diseño de un microprocesador cuyo *set de instrucciones* era Lisp[^lispproc]— la conclusión intuitiva es que Lisp debe ser algo pesado, algo que necesita una máquina grande. Es exactamente al revés, y ese malentendido es el corazón de este post.

El argumento de Steele y Sussman, de hecho, apunta en la dirección contraria a la intuición: Lisp les parecía un buen lenguaje alrededor del cual diseñar una arquitectura de programa almacenado precisamente porque, como el lenguaje de máquina y a diferencia de casi todos los lenguajes de alto nivel, guarda programas y datos de la misma forma y deja manipular programas como datos. No construyeron una máquina grande porque Lisp fuera pesado; construyeron una máquina *de Lisp* porque Lisp era simple.

Lisp es barato de implementar. El núcleo del lenguaje es minúsculo: un lector que convierte texto en estructuras de datos, un evaluador que es esencialmente un `case` sobre unas pocas formas especiales, un puñado de primitivas sobre pares, y un ciclo que lee, evalúa e imprime. Todo lo demás —y «todo lo demás» es casi todo el lenguaje— se construye encima, en el propio Lisp. Comparado con lo que hace falta para un compilador de Pascal o de C, un intérprete de Lisp es un programa chico.

Lo caro no es el intérprete: es la memoria de trabajo. Cada par que consumís vive en el heap, y el heap hay que reciclarlo. Pero en 48 KB tampoco necesitás un recolector sofisticado; con un mark-and-sweep sencillo y una pausa perceptible cada tanto alcanza y sobra. Que se note el garbage collector no es un defecto en una máquina así — es parte de la experiencia.

Y hay un tercer factor, menos técnico y más cultural: el REPL. Una máquina de 8 bits te dejaba prendido en un prompt, sin sistema operativo en el medio, sin ciclo de compilación. Eso es precisamente el hábitat natural de Lisp. En cierto sentido, la Spectrum era una máquina *más* hospitalaria para Lisp que una PC de oficina de la misma época.

No era una rareza aislada, tampoco. muLisp —que nació en CP/M, dentro de 64 KB, y recién después se portó a MS-DOS— circuló como un Lisp de microcomputadora perfectamente serio: tan serio que terminó siendo la base de muSIMP, muMATH y finalmente Derive, el sistema de álgebra simbólica[^mulisp]. Para la Spectrum en particular quedan registrados al menos *dos* intérpretes de Lisp distintos: el de Serious Software, de 1983, catalogado como «LISP Interpreter» y conocido como SpecLisp[^speccy]; y otro, sencillamente llamado «LISP», de AFI Software, de 1985, que hoy está dado por perdido[^afi]. En el C64 la historia se repite: Peter Feldtmann publicó un LISP 64 en la revista INPUT 64 en abril de 1986[^lisp64].

De SpecLisp sabemos bastante, y no por la ficha de catálogo sino porque Eugene Zaikonnikov —que también aprendió a programar en un clon de Spectrum— lo desenterró en 2015, lo corrió en un emulador y lo diseccionó[^zaik]. Su linaje se lee a simple vista: desciende de Lisp 1.5, hasta en el detalle de usar los marcadores de property list `PNAME` y `APVAL` del manual de McCarthy[^lisp15]. Tiene binding dinámico, el problema FUNARG sin resolver del todo, hay que escribir `QUOTE` completo, y las funciones nativas se enganchan guardando su dirección de llamada en la propiedad `SUBR` de un símbolo — «quizás la FFI más concisa jamás hecha», dice Zaikonnikov. Traía además una extensión de gráficos con comandos de tortuga al estilo Logo, lo que delata para qué se lo pensaba usar: para enseñar.

[VERIFICAR: si el «LISP Interpreter» de la ficha 8718 (SpecLisp) es el mismo producto que César recuerda, o si era el de AFI Software (ficha 20318), o uno tercero. La parte web de esta pregunta está resuelta — los datos de ambas fichas están verificados y volcados en la Bibliografía —, pero **la comparación contra el recuerdo de César sólo la puede hacer él**. Dato clave para el careo: la ficha de SpecLisp acredita publisher británico (Serious Software), 1983, en inglés, y **no acredita ningún autor individual**.]

### El eslabón argentino

Acá es donde el post se vuelve arqueología, y donde tengo que ser honesto con vos: la parte que más me importa es la que menos puedo probar.

La Spectrum tuvo una vida local propia y bastante documentada. Fue segunda en el mercado argentino, muy detrás del Commodore 64 que fabricaba Drean; circuló también el clon Timex Sinclair 2068; hubo revistas propias —K64, Programación Popular— y hubo comercios como Valente Computación o Real-Time donde uno iba con casetes vírgenes y volvía con software[^enarg]. Ese es el suelo sobre el que apoya todo lo demás. Lo que no encontré todavía es el papel.

[VERIFICAR: la atribución del port a Carlos Adaglio. **Pasada de búsqueda web hecha el 2026-07-15, resultado: cero.** Busqué "Carlos Adaglio" + LISP/Spectrum, "Adaglio" + Compusyst, "Adaglio" + Lisp/Argentina, y "Adaglio"/"Adagio" + LISP/C64/retrocomputing. El apellido Adaglio existe en Argentina (registros comerciales, LinkedIn, un autor en el catálogo de la Asociación Psicoanalítica Argentina) pero **no aparece ninguna persona vinculada a software, Lisp ni retrocomputing**. Tampoco lo mencionan czspectrum/enarg, Spectrum Computing (ninguna de las dos fichas acredita autor individual), ZX-Art ni el post de Zaikonnikov. **Lo que falta probar:** buscar "Adaglio" en el OCR de texto completo de la colección Programación Popular en archive.org (link en Bibliografía) y en K64; preguntar en la comunidad de retrocomputing argentina. No afirmar la autoría hasta entonces.]

[VERIFICAR: si Compusyst fue editorial/distribuidora del producto, o si la asociación viene de otro lado. **Buscado el 2026-07-15, sin resultado.** "Compusyst" + revista/Argentina/Spectrum y "Compusyst" + software/Spectrum/Commodore/cassette no devuelven **ninguna** revista, editorial ni distribuidora argentina con ese nombre — sólo una cuenta de X homónima y empresas sin relación. Los índices de revistas argentinas de los 80 que sí están relevados (Museo de la Informática, homecomputer.com.ar, czspectrum/enarg) listan K64, Programación Popular, Drean Commodore y Replay, y **ninguno menciona Compusyst**. **Lo que falta probar:** que el nombre esté mal recordado o sea de un local/importadora chica que no dejó rastro digital. Preguntarle a César de dónde sale el nombre antes de seguir buscando.]

> 🕳️ **HUECO — necesita a César:** ¿de dónde te viene el nombre «Carlos Adaglio»? ¿Figuraba impreso en el manual, en la pantalla de arranque, te lo dijo alguien? La fuente de tu recuerdo es un dato del post.

> 🕳️ **HUECO — necesita a César:** ¿lo conociste, o supiste algo de él después? ¿Hay alguien de esa época a quien podamos preguntarle?

Si esto quedara acá, el post sigue teniendo sentido: es un pedido de auxilio público. Alguien tiene el cassette. Alguien tiene el manual fotocopiado en una caja. Esa es una de las razones por las que escribo esto.

### Lo que me enseñó

Un Lisp de 48 KB me enseñó algo que ningún tutorial moderno me iba a enseñar, porque ningún tutorial moderno tiene motivos para enseñármelo: que el poder de un lenguaje no se mide en megabytes. Que la distancia entre «lenguaje de juguete» y «lenguaje serio» no la fija el tamaño del runtime. Que se puede tener recursión, listas, funciones de primera clase y un evaluador que se explica a sí mismo, en menos espacio del que hoy ocupa un archivo de configuración.

Cuando años después me crucé con SICP y con la idea de que el evaluador cabe en una página, no me sorprendió. Ya lo había visto cargar desde un cassette.

> 🕳️ **HUECO — necesita a César:** ¿esta lectura es tuya de aquel momento o es reconstrucción de ahora? Vale cualquiera de las dos, pero conviene decirlo.

[^speccy]: [LISP Interpreter (SpecLisp) — ZX Spectrum](https://spectrumcomputing.co.uk/entry/8718/ZX-Spectrum/LISP_Interpreter), ficha 8718 de Spectrum Computing: Serious Software (UK), 1983, 48K, £15.00. Sin autor individual acreditado. [Copia en Wayback](http://web.archive.org/web/20250115002710/https://spectrumcomputing.co.uk/entry/8718/ZX-Spectrum/LISP_Interpreter).
[^afi]: [LISP — ZX Spectrum](https://spectrumcomputing.co.uk/entry/20318/ZX-Spectrum/LISP), ficha 20318 de Spectrum Computing: AFI Software (UK), 1985, 48K, £15.00, estado MIA (no preservado).
[^zaik]: Eugene Zaikonnikov, [*Serious Software SpecLisp for Sinclair ZX Spectrum*](https://blog.funcall.org/lisp/2015/10/30/zx-spectrum-lisp/), 30 de octubre de 2015. [Copia en Wayback](http://web.archive.org/web/20260309012227/http://blog.funcall.org//lisp/2015/10/30/zx-spectrum-lisp/). Zaikonnikov también escribió su propio [intérprete de bytecode Lisp en assembler Z-80 para Spectrum](https://blog.funcall.org/lisp/2018/07/03/spectrum-lisp-vm/) (2018), con recolector mark-and-sweep.
[^lisp15]: John McCarthy, Paul W. Abrahams, Daniel J. Edwards, Timothy P. Hart y Michael I. Levin, *LISP 1.5 Programmer's Manual*, MIT Press. [2ª edición (1985) escaneada por bitsavers, en archive.org](https://archive.org/details/bitsavers_mitrlelisprammersManual2ed1985_9279667). El paper fundacional es John McCarthy, [*Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I*](http://www-formal.stanford.edu/jmc/recursive.html), *Communications of the ACM*, vol. 3, núm. 4, abril de 1960, pp. 184-195 — [doi:10.1145/367177.367199](https://doi.org/10.1145/367177.367199) — enlazado acá al archivo del propio McCarthy en Stanford.
[^lisp64]: [LISP 64 por Hamster (2014)](https://csdb.dk/release/?id=130534), CSDb — versión corregida del LISP 64 de Peter Feldtmann publicado originalmente en la revista INPUT 64, número 04/1986.
[^enarg]: [La Spectrum en Argentina](https://czspectrum.speccy.org/enarg.html), Speccy.
[^lispproc]: Guy L. Steele Jr. y Gerald J. Sussman, *Design of a LISP-based microprocessor*, *Communications of the ACM*, vol. 23, núm. 11, noviembre de 1980, pp. 628-645 — [doi:10.1145/359024.359031](https://doi.org/10.1145/359024.359031). Versión previa: AI Memo AIM-514 del MIT AI Lab, marzo de 1979. Para el panorama general de implementaciones históricas, ver el [archivo LISP del Software Preservation Group](https://softwarepreservation.computerhistory.org/LISP/index.html) del Computer History Museum, editado por Paul McJones.
[^mulisp]: [*muLISP-87 Reference Manual*](https://archive.org/details/mu-lisp-87-reference-manual-ocr-final), Soft Warehouse, 1988 — «muLISP was a small but efficient LISP system for microcomputers»; nació en CP/M dentro de 64 KB y fue la base de muSIMP, muMATH y Derive. Ver también [Microsoft MULISP-83 (1983)](https://archive.org/details/microsoft-mulisp), contemporáneo exacto de SpecLisp.

**Estado actual:**

⚠️ **PREMISA EN DUDA:** el Hook afirma dos cosas —«el primer Lisp que vi cabía en una Spectrum de 48 KB» y «lo había portado un argentino»—. La primera quedó **sólidamente respaldada** por esta pasada. La segunda **no tiene ni un gramo de respaldo documental, y ahora hay evidencia que apunta en contra**:

- Los **dos** Lisps para ZX Spectrum que están catalogados son británicos: *LISP Interpreter* / SpecLisp, de **Serious Software (UK), 1983**, en inglés (ficha 8718, verificada); y *LISP*, de **AFI Software (UK), 1985** (ficha 20318, verificada, hoy MIA). Ninguna de las dos fichas acredita autor individual alguno, ni argentino ni de ningún lado.
- **«Carlos Adaglio» no aparece en ninguna fuente de retrocomputing** — ni en Spectrum Computing, ni en ZX-Art, ni en czspectrum/enarg, ni en el post de Zaikonnikov, ni en ninguna búsqueda web (detalle de lo buscado, en la marca `[VERIFICAR:]` de la sección «El eslabón argentino»).
- **«Compusyst» no existe como revista, editorial ni distribuidora argentina** en ninguno de los relevamientos de prensa informática local que sí están digitalizados (Museo de la Informática, homecomputer.com.ar, czspectrum/enarg listan K64, Programación Popular, Drean Commodore y Replay — nada más).

Esto **no prueba que César se equivoque**: pudo haber sido un port o una traducción local sin registro, distribuido por canales que no dejaron rastro digital, o el nombre puede estar levemente mal recordado. Pero **la autoría argentina no se puede afirmar como hecho en el post tal como está el Hook hoy**. Hay que resolverlo antes de publicar, no después. Camino concreto y barato: la colección de **Programación Popular en archive.org tiene OCR de texto completo** (36 números, dic-1984 a nov-1987, faltan el 18 y del 25 al 36) — se puede buscar «Adaglio» y «Compusyst» ahí directamente. Es la mejor pista que queda y está sin hacer.

**Pasada de fuentes hecha el 2026-07-15.** Se agregaron 11 fuentes verificadas por fetch y se descartaron 4 de las viejas (ver «Fuentes descartadas» en la Bibliografía; la más importante: el link a Lisp Pointers en `iment.com` **no se pudo verificar** —certificado TLS roto— así que se eliminó la afirmación que dependía de él en vez de dejarla colgada). Ganancias reales de la pasada:

- **Fuente primaria sobre SpecLisp encontrada**: el post de Eugene Zaikonnikov (2015), que es de donde sale todo lo que circula sobre el tema. Permitió escribir un párrafo técnico concreto y verificado (linaje Lisp 1.5 vía `PNAME`/`APVAL`, binding dinámico, FUNARG, FFI por propiedad `SUBR`, case-sensitivity, gráficos de tortuga) donde antes había generalidades.
- **Segundo Lisp de Spectrum descubierto** (AFI Software, 1985): «el Lisp de la Spectrum» no era unívoco, dato que le suma al careo con el recuerdo de César.
- **El C64 del slug ahora tiene contenido**: LISP 64 de Peter Feldtmann, INPUT 64 04/1986.
- **Citas primarias en lugar de Wikipedia**: Steele & Sussman (CACM 23(11), 1980, DOI verificado por crossref) para las Lisp machines, y McCarthy en su propio archivo de Stanford + el manual de LISP 1.5 en bitsavers.
- **muLisp bien citado**: el dato «nació en CP/M dentro de 64 KB y terminó siendo Derive» es la mejor munición para la tesis del post, y ahora tiene manual escaneado detrás.

Lo que sigue **abierto**: (a) los 7 huecos personales —todo el eje autobiográfico— que sólo contesta César; (b) las 3 marcas `[VERIFICAR:]`, ninguna de las cuales se resolvió por web (dos por ausencia total de fuentes, una porque depende del recuerdo de César); (c) la búsqueda en el OCR de Programación Popular. Si (c) no da resultado y César no puede precisar el origen del nombre, el post **publica igual** como memoria personal + pedido de auxilio público, pero entonces **hay que reescribir el Hook** para que plantee la autoría argentina como recuerdo a confirmar y no como hecho establecido. Esa decisión es de César.

