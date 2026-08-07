### A1-04 — Modula-2: Pascal después de Pascal

- **Archivo seed:** `dev/draft-modula2.md`
- **Slug propuesto:** `modula-2-pascal-despues-de-pascal`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-modula-2-pascal-despues-de-pascal.md`
- **Serie:** A1
- **Cross-links:** lleva a [[A1-03]] (Forth, otro lenguaje para "una persona"), [[E-08]] (libros que me hicieron programador, donde aparece *Algorithms + Data Structures = Programs*)
- **Idioma:** es
- **Madurez:** prosa-borrador + fuentes verificadas (2026-07-15, generado por Claude; sin revisar por César). Pasada de fuentes hecha el 2026-07-15: bibliografía reconstruida y fetcheada URL por URL, 6 de los 9 `[VERIFICAR:]` originales cerrados con cita, 3 citas heredadas rotas/mal atribuidas corregidas.
- **Length target:** medium (1200-1500 palabras)

**Concepto:** Modula-2 es lo que Wirth hizo después de Pascal cuando se dió cuenta de que Pascal tenía problemas reales para programar en grande. Módulos de verdad, separación clara interface/implementación, coroutines. La pregunta del post: ¿por qué este lenguaje, que era objetivamente mejor que Pascal y anterior a Ada, no ganó?

**Hook:** abrir con la portada del libro de Wirth de 1982. Después: "Pascal era para enseñar; Modula-2 era para construir. Y casi nadie lo usó. ¿Por qué?".

**Outline:**
1. Nicklaus Wirth y la línea Algol → Pascal → Modula → Modula-2 → Oberon. Cada lenguaje es una autocrítica del anterior.
2. Qué agrega Modula-2: módulos con interface separada, coroutines, types low-level controlados.
3. Su uso real: el sistema operativo Lilith, la mayor parte del libro *Algorithms + Data Structures = Programs* de Wirth.
4. Por qué perdió frente a C/C++: timing, free compilers, C era "suficientemente rápido" y ya estaba en Unix.
5. Lecciones para hoy: la cantidad de cosas modernas (Go, Rust modules, etc.) que terminaron pareciéndose a Modula-2.

**Bibliografía:**

> **Estado de verificación (pasada de fuentes, 2026-07-15):** las siete entradas originales se fetchearon una por una. **Tres estaban rotas o mal**: el PDF de *A Brief History* en `people.inf.ethz.ch/wirth/Articles/` daba 404; el dominio `e-collection.library.ethz.ch` de *From Modula to Oberon* **ya no existe** (`ENOTFOUND`); y el catálogo 102746194 del Computer History Museum **no es una oral history de Wirth**, es el panel de LSI Logic (Blair/Koford/Walker/Corrigan, 2011). Además el link de archive.org citado como «1982» es en realidad la 3.ª edición de 1985. Todo eso está corregido abajo.

*Fuente primaria — Wirth sobre Wirth (lo mejor que hay para este post):*
- [Niklaus Wirth, *Modula-2 and Oberon*, HOPL-III, 2007](https://free.oberon.org/files/Modula2_and_Oberon.pdf) — **frágil** (mirror comunitario) pero es el texto completo y verificado; DOI canónico: [10.1145/1238844.1238847](https://doi.org/10.1145/1238844.1238847) (*Proc. 3rd ACM SIGPLAN Conf. on History of Programming Languages*, ACM, 2007) — **estable**, confirmado vía Crossref (el ACM DL bloquea el fetch directo). **Es la fuente central del post**: de acá salen las fechas, el relato de Lilith, la decisión sobre coroutines y la frase sobre el mercado.
- [Niklaus Wirth, *A Brief History of Software Engineering*](https://people.inf.ethz.ch/wirth/Miscellaneous/IEEE-Annals.pdf) — **el link bueno**, en el sitio del propio Wirth (el del draft, en `/Articles/`, da 404). *IEEE Annals of the History of Computing*, vol. 30, n.º 3 (2008), pp. 32-39. DOI: [10.1109/MAHC.2008.33](https://doi.org/10.1109/MAHC.2008.33) — **estable**, confirmado vía Crossref.
- Niklaus Wirth, *From Modula to Oberon*, *Software: Practice and Experience*, vol. 18, n.º 7 (julio 1988), pp. 661-670. DOI: [10.1002/spe.4380180706](https://doi.org/10.1002/spe.4380180706) — **estable**, confirmado vía Crossref. (El PDF del ETH que citaba el draft ya no existe; no encontré mirror libre.)
- N. Wirth y C. A. R. Hoare, *A contribution to the development of ALGOL*, *Communications of the ACM*, vol. 9, n.º 6 (junio 1966), pp. 413-432. DOI: [10.1145/365696.365702](https://doi.org/10.1145/365696.365702) — **estable**, confirmado vía Crossref. El acta de nacimiento de Algol W.

*Libros:*
- Niklaus Wirth, *Programming in Modula-2*, Springer-Verlag, 1982 — la edición canónica, DOI [10.1007/978-3-642-96717-7](https://doi.org/10.1007/978-3-642-96717-7) (**estable**, vía Crossref). En archive.org **no está la de 1982**; hay dos ediciones posteriores, ambas en préstamo controlado: [2.ª ed., 1983, 194 pp.](https://archive.org/details/programminginmod00wirt) y [3.ª ed., 1985, 202 pp.](https://archive.org/details/programminginmod0000wirt) — **estables**.
- [Niklaus Wirth, *Algorithms + Data Structures = Programs*, Prentice-Hall, 1976](https://archive.org/details/algorithmsdatast00wirt) — **estable** — la edición **en Pascal**.
- [Niklaus Wirth, *Algorithms and Data Structures*, Prentice-Hall, 1986 (© 1985), 288 pp.](https://archive.org/details/algorithmsdatast0000wirt_u9b4) — **estable** — **ésta es la reescritura en Modula-2**, y va sin el «= Programs» en el título.
- [Niklaus Wirth, *Algorithms and Data Structures* — versión en Oberon del texto de 1985](https://people.inf.ethz.ch/wirth/AD.pdf) — **frágil** (sitio personal en el ETH) — PDF libre, con nota del traductor Fyodor Tkachov (2012).

*El lenguaje en sí:*
- [*Report on the Programming Language Modula-2*, 4.ª ed. (1988)](https://freepages.modula2.org/report4/modula-2.html) — **frágil**, y con un problema: **no tiene snapshot en Wayback** (lo consulté). Es la fuente de los nombres exactos de `SYSTEM`. Respaldar con la de Ulm antes de publicar.
- [Ulm's Modula-2 Library: SYSTEM](https://www.mathematik.uni-ulm.de/modula/man/man3/SYSTEM.html) — **estable** (dominio universitario) — confirma `WORD`, `ADDRESS = POINTER TO WORD`, `ADR`, `TSIZE`, `NEWPROCESS`, `TRANSFER`.
- [GNU Modula-2: el módulo SYSTEM](https://gcc.gnu.org/onlinedocs/gm2/gm2-libs-coroutines_002fSYSTEM.html) — **estable** — la versión viva del mismo módulo, útil para el punto «Modula-2 hoy tiene compilador libre, cuarenta años tarde».

*Por qué perdió — fuente contemporánea:*
- [Kent Porter, «Examining Room: The State-of-the-Art in Modula-2», *Dr. Dobb's Journal*, septiembre 1988](https://jacobfilipp.com/DrDobbs/articles/DDJ/1988/8809/8809f/8809f.htm) — **frágil** (mirror personal); backup Wayback: [snapshot del 2024-10-15](http://web.archive.org/web/20241015040002/https://jacobfilipp.com/DrDobbs/articles/DDJ/1988/8809/8809f/8809f.htm) — **estable**. Review de FTL, Logitech, TopSpeed y Stony Brook **con precios**. Load-bearing para el punto del compilador comercial.
- [TopSpeed Modula-2 v3.01 (JPI), en archive.org](https://archive.org/details/top-speed-modula-2-v-3.01-ms-dos-already-installed-archive) — **estable** — el compilador comercial, jugable.

*Herencia:*
- [Go FAQ — «What are Go's ancestors?»](https://go.dev/doc/faq) — **estable** — cita explícita de la familia Pascal/Modula/Oberon como input de Go.
- [The Rust Reference — *Influences*](https://doc.rust-lang.org/reference/influences.html) — **estable** — **no** menciona a Wirth; sirve como prueba en negativo.

*Contexto (no citas primarias):*
- [Modula-2](https://en.wikipedia.org/wiki/Modula-2) y [Lilith (computer)](https://en.wikipedia.org/wiki/Lilith_(computer)) en Wikipedia — **estables**.
- [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language)) en Wikipedia — **estable** — cronología del DoD/HOLWG/Steelman/1815A.
- [CHM, *In Memoriam: Niklaus Wirth (1934-2024)*](https://computerhistory.org/blog/in-memoriam-niklaus-wirth-1934-2024/) — **estable** — confirma Pascal 1970 / Modula-2 1979 / Oberon 1988 y trae la cita «people seem to misinterpret complexity as sophistication».
- [CHM, perfil de Niklaus Wirth](https://computerhistory.org/profile/niklaus-wirth/) — **estable** — Fellow Award 2004: «For seminal work in programming languages and algorithms, including Euler, Algol-W, Pascal, Modula, and Oberon».

**Imágenes:**
- _Wikimedia_: [Niklaus Wirth, UrGU](https://commons.wikimedia.org/wiki/File:Niklaus_Wirth,_UrGU.jpg) — **verificada**: foto de **Tyomitch**, **3 de octubre de 2005**, en la Universidad Estatal de los Urales; licencia **«Copyrighted free use»**. ⚠️ El draft la listaba como «(1969)» y «CC-BY-SA»: **ambos datos eran incorrectos**. Es usable (la licencia permite uso comercial y modificación), pero la atribución hay que escribirla bien. Ver [^img_hero].
- _Wikimedia_: [Lilith workstation](https://commons.wikimedia.org/wiki/Category:Lilith_(computer)) — [VERIFICAR: no fetcheé esta categoría en la pasada de fuentes; antes de usar cualquier foto de la Lilith hay que abrir el archivo puntual y confirmar autor y licencia uno por uno, como se hizo con la de Wirth — que resultó estar mal fichada.]
- _Crear_: opcional — comparación side-by-side de un módulo Pascal vs Modula-2 (~30 min).

**Tags propuestos:** `['Modula-2', 'Niklaus Wirth', 'Pascal', 'Lilith', 'historia']`

**Estado actual:**

> **Pasada de fuentes — 2026-07-15.** La premisa central **se sostiene y encima tiene respaldo del propio Wirth**: en su paper de HOPL-3 escribe «The market favors languages of commercial origin, **regardless of their technical merits or defects**. The market's inertia is enormous, as it is driven by a multitude of vicious circles which reinforce themselves», y cierra diciendo que Pascal, Modula-2 y Oberon sí lograron aportar, pero por goteo, «slowly, very slowly over decades», hacia lenguajes comerciales. Eso es, palabra por palabra, la tesis del post («ganó como idea y no como implementación») firmada por el autor del lenguaje. Es la mejor cita que tiene este post y hoy no está en la prosa: **usarla**.
>
> **Dos matices que las fuentes le hacen al argumento** (ninguno rompe el post, los dos están anotados en el cuerpo):
> 1. **«Anterior a Ada»** es discutible. Modula-2 (reporte 1979) precede al estándar de Ada (1980/1983), pero el programa del DoD arrancó en 1975 y el diseño de Modula-2 fue 1978-79: son **contemporáneos**. Decir «llegó antes que el estándar de Ada» es exacto; «llegó antes que Ada» es flojo.
> 2. **«El compilador costaba plata»** es cierto pero más débil de lo que suena: en 1988 Logitech salía USD 99 y TopSpeed USD 99,95 — precio de Turbo Pascal, no de artículo de lujo. El punto fuerte no es el precio sino que **C ya venía puesto**.
>
> **Hallazgo feo:** de las siete entradas de bibliografía del draft original, **tres no servían**: dos URLs muertas (404 el PDF de *A Brief History*; dominio inexistente el de *From Modula to Oberon*) y una **mal atribuida** — el link «oral history con Wirth» del Computer History Museum apunta en realidad al panel de LSI Logic de 2011. Además la foto de Wirth estaba fichada como «1969 / CC-BY-SA» y es **2005 / Copyrighted free use**. Todo corregido; queda como recordatorio de que las citas heredadas se fetchean igual.
>
> **Sourceado y verificado en esta pasada:** el paper de HOPL-3 de Wirth (texto completo extraído del PDF, no un resumen), *A Brief History of Software Engineering* en su URL buena, cuatro DOIs confirmados vía Crossref (Springer 1982, HOPL-III, IEEE Annals, SPE 1988, CACM 1966), las tres ediciones de archive.org de *Programming in Modula-2* / *Algorithms and Data Structures*, el reporte del lenguaje y la librería de Ulm para `SYSTEM`, la review de *Dr. Dobb's* de 1988 con precios (+ backup Wayback), el FAQ de Go, el apéndice *Influences* de Rust, y el obituario y el perfil de Wirth en el CHM.
>
> **Marcadores `[VERIFICAR:]`: 9 al empezar, 5 al terminar.** De los 9 originales, **6 quedaron cerrados con cita verificada**; 2 se acotaron a la parte que no pude probar y 1 (la foto) se resolvió pero destapó otros. Los 5 que quedan son 2 originales acotados + 3 nuevos que aparecieron justamente por fetchear lo que antes nadie había fetcheado. Todos con la búsqueda documentada: (a) las cifras de venta de la Lilith (120 unidades / USD 8.000) sólo salen de la infobox de Wikipedia y no las confirma ninguna fuente primaria; (b) no hay oral history de Wirth en el CHM — el link del draft apuntaba a otra cosa y la entrevista Turing de la ACM devuelve 403; (c) el mirror del reporte del lenguaje no tiene copia en Wayback; (d) la categoría de la Lilith en Commons no fue revisada foto por foto; (e) queda buscar si algún diseñador de Rust reconoció a Wirth (en las fuentes oficiales, no). Los **cinco huecos 🕳️ siguen intactos** — ninguna búsqueda web contesta por la vida de César.

prosa completa escrita contra el outline de 5 puntos (~1.400 palabras, dentro del target `medium`). Lo que está resuelto: el encuadre de la línea Algol → Pascal → Modula-2 → Oberon como cadena de autocríticas, la explicación técnica de `DEFINITION`/`IMPLEMENTATION` y del módulo `SYSTEM`, el episodio Lilith, la hipótesis de por qué perdió frente a C, y el cierre sobre los ecos en Go/Rust/Ada.

Lo que queda como hueco (necesita a César): **cinco huecos** marcados con 🕳️ — todos sobre su contacto real con Modula-2 y Pascal (si tuvo el libro de Wirth del '82 en la mano, con qué compilador de Modula-2 llegó a trabajar si es que llegó, qué Pascal usó en la facultad/trabajo, si vio el `SYSTEM` como escape o como pecado, y qué lenguaje moderno le trae el recuerdo). Sin esas respuestas el post es un ensayo histórico impersonal; con ellas es un post de katra. **No rellenar con anécdota inventada.**

Lo que queda como `[VERIFICAR:]` (actualizado tras la pasada de fuentes del 2026-07-15): **cinco** marcadores, de los nueve originales. **Resueltos con fuente verificada:** años de la línea Algol W → Oberon; ubicación y primitivas de las coroutines (`SYSTEM`, `NEWPROCESS`/`TRANSFER`); tipos exportados por `SYSTEM` (`WORD`, `ADDRESS`, `ADR`, `TSIZE`); equipo y cronología de Lilith; qué edición de *Algorithms and Data Structures* trae el código en Modula-2 (la de 1985/86, con otro título); fechas de Ada; nombres y precios de los compiladores comerciales; la cuestión Go/Rust (Go **sí** declara la influencia, Rust **no**); y la atribución de la foto de Wirth (que estaba mal). **Siguen abiertos:** las cifras comerciales de la Lilith, la oral history inexistente del CHM, el backup del reporte del lenguaje, las fotos de la Lilith en Commons, y si alguien de Rust reconoció alguna vez la deuda con Wirth.

**Pendiente de imágenes:** el Hook pide abrir con la portada del libro de Wirth de 1982, pero la sección **Imágenes** no tiene una portada con licencia clara (Springer, con copyright). O se consigue una portada usable, o el hero pasa a ser la foto de Wirth / la Lilith y la portada se menciona en el texto sin mostrarse. Decidir antes de correr `hugo new` (la decisión de bundle no se revierte).

---

## Borrador de prosa

Hay un libro que, si lo tuviste en la mano en su momento, no se te olvida más: *Programming in Modula-2*, de Niklaus Wirth, Springer-Verlag, 1982.[^wirth82] Es finito. Es seco. No tiene una sola línea de más. Y adentro está, completo, un lenguaje de programación entero: la definición, la biblioteca estándar, y la explicación de por qué cada cosa es como es. Doscientas y pico de páginas para describir un lenguaje que servía para escribir un sistema operativo. Hoy la documentación de un framework de JavaScript que dura dos años ocupa más que eso.

Pascal era para enseñar; Modula-2 era para construir. Y casi nadie lo usó. De eso quiero hablarte: no de nostalgia, sino de la pregunta incómoda que deja atrás un lenguaje que era mejor que su antecesor, llegó antes que Ada, se parecía muchísimo a lo que hoy consideramos buen diseño… y perdió igual.

> 🕳️ **HUECO — necesita a César:** ¿tuviste el *Programming in Modula-2* de Wirth en la mano? ¿Cuál edición, en qué año y cómo llegó a vos (cátedra, librería, fotocopia, biblioteca)?

### Wirth, o la carrera de un hombre que se corrige a sí mismo

La línea es conocida y vale la pena decirla completa, porque el chiste está en la forma de la línea, no en los nombres: Algol 60 → Algol W (1966) → Pascal (1970) → Modula (1975) → Modula-2 (1979) → Oberon (1988).[^hopl] [^algolw]

> **Nota de la pasada de fuentes (2026-07-15):** el draft decía «Modula-2 ~1978» y «Oberon ~1987». Corregido a **1979** y **1988** contra el abstract del propio Wirth en su paper de HOPL-3: «Pascal (1970) reflected the ideas of Structured Programming, Modula-2 (1979) added those of modular system design, and Oberon (1988) catered to the object-oriented style».[^hopl] El obituario del Computer History Museum da las mismas tres fechas.[^chm] Modula queda en 1975 por la frase de Wirth «I had designed and implemented the predecessor language Modula [7-9] in 1975».[^hopl] Algol W no es un año único sino un proceso: el paper fundacional de Wirth y Hoare es de junio de 1966.[^algolw]

Lo notable es que cada eslabón de esa cadena es una crítica del anterior escrita por la misma persona. No es una familia de lenguajes que se ramifica porque discípulos distintos tiraron para lados distintos. Es un tipo que publica un lenguaje, lo usa en serio, descubre dónde le duele, y publica el siguiente. Wirth hizo eso cuatro o cinco veces seguidas a lo largo de treinta años. Y el más brutal de todos con Wirth fue siempre Wirth: *From Modula to Oberon*[^oberon] es, básicamente, un texto donde el autor de Modula-2 explica qué le sobra a Modula-2 y lo saca.

Esa es una ética de diseño que hoy prácticamente no existe. Los lenguajes actuales crecen: cada versión agrega. Wirth restaba. Su idea de progreso era que la versión siguiente fuera **más chica**.

### Qué le faltaba a Pascal (y qué le puso Modula-2)

Pascal es un lenguaje precioso para explicar qué es un tipo de dato, qué es un procedimiento, qué es una estructura de control. Por eso ganó las aulas de medio mundo. Pero cuando querés escribir un programa de cincuenta mil líneas con Pascal estándar, te chocás con una pared: **no hay unidad de compilación separada de verdad**, y por lo tanto no hay forma real de decir «esto es lo que mi pedazo de programa le muestra al resto del mundo, y esto es asunto mío». El programa Pascal canónico es un bloque grande. Andaba bárbaro para enseñar y era impracticable para construir.

Modula-2 responde a eso con tres cosas.

**Uno: módulos con interface separada.** Cada módulo se escribe dos veces, y a propósito. Un `DEFINITION MODULE` dice qué exporta —los tipos, los procedimientos, sus firmas— y nada más. Un `IMPLEMENTATION MODULE` dice cómo se hace, y el resto del programa no tiene derecho a mirar adentro. El compilador lo hace cumplir. Si querés un tipo cuya representación nadie de afuera pueda tocar, lo declarás opaco en la definición y listo: tenés encapsulamiento real, verificado por la máquina, sin objetos, sin clases y sin herencia.[^wirth82] [^wp-m2]

Es exactamente la idea que veinte años después iba a venderse como «programación orientada a interfaces», y estaba ahí, en un lenguaje de los setentas, sin marketing.

**Dos: coroutines.** Modula-2 trae la posibilidad de tener varios hilos de control cooperativos que se ceden el paso explícitamente. No es paralelismo: es concurrencia expresada como corrutinas, con transferencia de control a mano. Con eso Wirth construía manejadores de dispositivos y el scheduling del sistema operativo sin necesidad de bajar a assembler.

La pregunta de dónde viven quedó respondida, y la respuesta es interesante: **no están en el núcleo del lenguaje, están en `SYSTEM`**, y fue una decisión consciente. Wirth lo cuenta así en HOPL-3: la concurrencia era «a hot topic», se barajaron procesos con señales y monitores, «yet, it was decided that only the very basic notion of coroutines would be included in Modula-2, and that higher abstractions should be programmed as modules based on co-routines. This decision was even more plausible, because the primitives could well be classified as low-level facilities».[^hopl] Las primitivas concretas son `NEWPROCESS` y `TRANSFER`, exportadas por `SYSTEM`; el reporte del lenguaje aclara que «the word *process* is here used with the meaning of coroutine».[^report4] [^ulm]

O sea: Modula-2 no te da concurrencia, te da la pieza mínima con la que construirla vos — y te la deja en el mismo cajón de las cosas peligrosas.

**Tres: acceso de bajo nivel, pero acorralado.** Wirth sabía que un lenguaje para escribir sistemas operativos tiene que poder pisar una dirección de memoria. Su solución fue elegante: eso vive en un módulo especial, `SYSTEM`. Podés hacer la porquería que necesites, pero tenés que **importarla explícitamente**, y entonces queda escrito en el encabezado del módulo que ahí adentro hay magia negra.

Los nombres exactos, según el reporte del lenguaje (4.ª edición, 1988): los tipos `WORD` —«represents an individually accessible storage unit», sin más operación que la asignación— y `ADDRESS`, definido literalmente como `POINTER TO WORD` y compatible con todos los tipos puntero y con `CARDINAL`; más los procedimientos `ADR`, `TSIZE`, `NEWPROCESS` y `TRANSFER`.[^report4] [^ulm] Con un matiz que vale la pena: el reporte dice que lo que exporta `SYSTEM` «is specified by individual implementations» y que esos son los que *normalmente* están — es decir, `SYSTEM` es por diseño el lugar donde el lenguaje deja de ser portable, y el estándar lo admite.

Comparalo con C, donde el acceso crudo a memoria no es un permiso especial: es el idioma nativo. Modula-2 te dejaba hacer lo mismo, pero te obligaba a firmar el papel.

> 🕳️ **HUECO — necesita a César:** ese `SYSTEM` importable, ¿te suena a solución elegante o a hipocresía de diseño? ¿Tenés una opinión formada por haber tenido que hacer lo mismo en otro lenguaje (`unsafe`, `Marshal`, punteros en Pascal)?

### El lenguaje tenía una máquina propia

Acá está la parte que más me gusta de la historia. Wirth no escribió Modula-2 para que corriera en la computadora que había: se hizo la computadora. La Lilith[^lilith] fue una workstation diseñada en el ETH cuyo software estaba escrito en Modula-2 de arriba abajo —sistema operativo, editor, compilador— y cuyo hardware ejecutaba un código intermedio pensado para ese lenguaje.

Los datos, ahora chequeados contra el relato del propio Wirth:[^hopl] la máquina la diseñaron **Wirth y R. Ohran**, siguiendo las líneas del Xerox Alto que Wirth había visto en su sabático en PARC en 1976/77; estaba basada en el bit-slice **Am2901 de AMD** y era microprogramada. El compilador de Modula-2 para Lilith lo escribieron **L. Geissmann y Ch. Jacobi** en 1979-80 (antes hubo uno para PDP-11 de K. van Le en 1977, de 7 pasadas, reducido a 5 por U. Ammann en 1979). En **diciembre de 1980** se entregó al ETH una serie piloto de **20 Liliths fabricadas en Utah** bajo supervisión de Ohran, y «by 1981, Modula-2 was in daily use». Wirth remata con una frase que da para el post entero: con esas 20 máquinas el ETH tuvo en 1981 «the first modern computing environment outside America», cinco años antes que el primer sistema comercial equivalente, la Macintosh.

¿Se comercializó? Sí, modestamente: se vendió bajo la empresa **DISER**, y **Modula Computer Systems** (Provo, Utah) siguió vendiéndolas en EE.UU.[^lilith] [VERIFICAR: las cifras de 120 unidades vendidas y precio de USD 8.000 salen de la infobox de Wikipedia y **no** aparecen en el paper de Wirth ni en ninguna fuente primaria que haya podido abrir; no publicar esos números sin un segundo respaldo. El detalle DISER/Modula Computer Systems sí está en Wikipedia pero tampoco lo confirma Wirth, que sólo habla de la serie piloto de 20.]

O sea: la prueba de que Modula-2 servía para construir cosas no era un paper. Era una máquina que arrancaba.

Y hay una segunda prueba, más doméstica: *Algorithms + Data Structures = Programs*[^adsp], el libro que le enseñó estructuras de datos a una generación entera en Pascal, fue reescrito por Wirth con el código en Modula-2.

Resuelto, y con un detalle que conviene no pasar por alto: **la versión en Modula-2 no se llama igual**. El original de 1976 es *Algorithms + Data Structures = Programs* (Prentice-Hall, con el código en Pascal).[^adsp] La reescritura en Modula-2 salió como ***Algorithms and Data Structures*** —sin el «= Programs»— con copyright de 1985 y edición de Prentice-Hall de 1986.[^adsp-m2] Es decir: si alguien busca «el Wirth de estructuras de datos en Modula-2» por el título famoso, no lo encuentra. Hay todavía una tercera vida: el propio Wirth mantuvo en su sitio una versión en Oberon del texto de 1985, que es la que hoy se baja gratis en PDF.[^ad-oberon]

> 🕳️ **HUECO — necesita a César:** ¿en qué versión leíste vos *Algorithms + Data Structures = Programs* — la de Pascal o la de Modula-2? ¿Y qué te quedó de ese libro, treinta años después, en una frase? (Va a cruzarse con [[E-08]].)

### Entonces, ¿por qué perdió?

No perdió por malo. Perdió por cuatro razones que no tienen nada que ver con la calidad del diseño, y que conviene mirar de frente porque siguen operando hoy.

**El compilador costaba plata.** Los compiladores serios de Modula-2 eran productos comerciales. C venía adentro de Unix, y después venía gratis con GCC. En una carrera entre «excelente y pago» y «aceptable y gratis», gana el segundo, siempre.

Los nombres están confirmados por una fuente contemporánea de primera mano: la review «The State-of-the-Art in Modula-2» de Kent Porter en *Dr. Dobb's Journal* de septiembre de 1988, que compara cuatro compiladores de MS-DOS: **FTL** (Workman Associates), **Logitech**, **TopSpeed** (JPI — Jensen & Partners International, fundada por Niels Jensen, cofundador de Borland, sobre el código de un Turbo Modula-2 que Borland nunca lanzó) y **Stony Brook**.[^ddj] [^wp-m2] De TopSpeed hay hasta una copia jugable en archive.org.[^topspeed]

> ⚠️ **Matiz que la fuente le hace al argumento (pasada de fuentes, 2026-07-15):** los precios que da Porter en 1988 son **FTL USD 49,95**, **Logitech USD 99** el core (USD 249 con el toolkit) y **TopSpeed USD 99,95**.[^ddj] Eso no es «carísimo»: es exactamente la banda de precios de Turbo Pascal. El argumento «perdió porque costaba plata» sobrevive frente a GCC —gratis es gratis— pero **no** sobrevive como «era un lujo inaccesible». Si el post mantiene este punto, conviene afilarlo: no era el precio en dólares, era que C **ya estaba ahí**, adentro del sistema operativo, sin decisión de compra de por medio. Sugerencia para César: cambiar el título del punto de «El compilador costaba plata» a algo como «El compilador había que ir a buscarlo».

**El timing.** Modula-2 llegó justo cuando C ya estaba adentro del sistema operativo que se estaba comiendo el mundo, y justo antes de que Ada absorbiera todo el oxígeno institucional del «lenguaje serio para sistemas grandes». Quedó apretado entre el de facto y el de jure.

Las fechas de Ada, verificadas: el DoD formó el **HOLWG en 1975**; los requerimientos *Steelman* son de **1978**; en **mayo de 1979** ganó la propuesta *Green* de Jean Ichbiah (Honeywell); el estándar salió en **1980** como ANSI/MIL-STD-1815, se revisó en **1983** como ANSI/MIL-STD-1815A, y llegó a ISO en **1987**.[^ada]

> ⚠️ **Ojo con el solapamiento (pasada de fuentes, 2026-07-15):** el Concepto dice que Modula-2 fue «anterior a Ada». Depende de qué se cuente. Por **fecha de reporte del lenguaje**, sí y por poco: Modula-2 1979 contra Ada 1980. Por **fecha del programa**, no: el DoD arrancó el HOLWG en 1975, cuando Wirth recién publicaba Modula, y el diseño efectivo de Modula-2 fue 1978-79,[^hopl] es decir en paralelo con el concurso que ganó Green en mayo de 1979. Los dos lenguajes son **contemporáneos**, no consecutivos. El post puede sostener «llegó antes que el estándar de Ada» sin problema; «llegó antes que Ada» a secas es discutible y un lector de la vieja escuela lo va a saltar. Decisión de César.

**No tenía dueño con plata.** Detrás de C estaban los Bell Labs y después toda la industria Unix; detrás de Ada, el Departamento de Defensa de Estados Unidos. Detrás de Modula-2 estaba un profesor suizo con muy buenas ideas y un laboratorio.

**Y el propio Wirth siguió de largo.** Mientras el mundo podría haber estado adoptando Modula-2, Wirth ya estaba insatisfecho y trabajando en Oberon.[^oberon] La misma virtud —la autocrítica permanente— que hace grande a la línea es lo que le impidió consolidar ninguno de sus eslabones. Un lenguaje necesita que alguien lo defienda diez años; Wirth prefería mejorarlo.

### El consuelo: ganó de contrabando

Lo raro es que hoy, cuando miro los lenguajes que la industria decidió que son los buenos, veo Modula-2 por todos lados.

Go tiene módulos y paquetes con exportación explícita, tiene un compilador rapidísimo por diseño (Wirth era fanático de eso[^hse]), y un cuerpo de lenguaje deliberadamente chico al que le sacaron cosas antes que agregárselas. Rust tiene módulos con visibilidad controlada y —esto es literal— un `unsafe` que funciona igual que el `SYSTEM` de Wirth: podés bajar al metal, pero queda escrito quién y dónde. Ada, que ganó donde Modula-2 perdió, separa specification de body con la misma lógica.

Acá la pasada de fuentes trajo un regalo y una advertencia, y son opuestos:

**Con Go se puede decir «desciende de», y con cita.** El FAQ oficial de Go contesta la pregunta «What are Go's ancestors?» así, textual: «Go is mostly in the C family (basic syntax), with significant input from the **Pascal/Modula/Oberon family (declarations, packages)**, plus some ideas from languages inspired by Tony Hoare's CSP».[^gofaq] O sea que la intuición del post no sólo es correcta: está admitida por escrito por los diseñadores, y justo en los dos rubros que el post señala (declaraciones y paquetes).

**Con Rust hay que decir «se parece a», y nada más.** El apéndice *Influences* de la referencia oficial de Rust lista SML/OCaml, C++, ML Kit, Cyclone, Haskell, Newsqueak/Alef/Limbo, Erlang, Swift, Scheme, C#, Ruby, NIL/Hermes y el Unicode Annex #31 — **y no menciona ni a Modula-2, ni a Oberon, ni a Pascal, ni a Wirth**.[^rustinf] El paralelo `unsafe`/`SYSTEM` es una observación del autor del post, buena y defendible como analogía, pero no hay linaje declarado. Mantener «se parece a».

[VERIFICAR: si en algún lado hay una cita de Graydon Hoare (o de la RFC de `unsafe`) que reconozca a Wirth — busqué el apéndice *Influences* de la referencia oficial y el FAQ de Go, y aparece Go pero no Rust; faltaría revisar el blog viejo de Hoare y las notas de diseño pre-1.0. Si no aparece, el post se queda con la analogía, que alcanza.]

Así que la respuesta honesta a «¿por qué no ganó Modula-2?» tal vez sea que sí ganó, pero como idea y no como implementación. Las ideas viajan gratis; los compiladores, no.

Y resulta que Wirth pensaba exactamente eso, y lo dejó escrito. Al final del paper de HOPL-3, después de contar treinta años de su propia obra, la conclusión a la que llega es ésta:[^hopl]

> «The market favors languages of commercial origin, regardless of their technical merits or defects. The market's inertia is enormous, as it is driven by a multitude of vicious circles which reinforce themselves.»

Y en la frase siguiente se contesta a sí mismo la pregunta de este post: las ideas de un lenguaje de investigación «find their ways into new versions of widely used, commercial languages, slowly, very slowly over decades. It is fair to claim that Pascal, Modula-2, and Oberon have been successful in making such contributions over time».[^hopl]

No es resignación: es un tipo que entendió que su trabajo era producir ideas y que el reparto lo hacía otro.

Me queda una lección menos consoladora, igual. Que un artefacto técnico sea mejor no alcanza. Nunca alcanzó. Lo que decide es dónde estaba el compilador, cuánto salía, quién lo bancaba y si alguien se quedó diez años defendiéndolo. Wirth hizo lo primero como pocos y lo segundo casi nunca, y por eso hoy escribimos Go —que es, más o menos, Modula-2 con una empresa atrás.

> 🕳️ **HUECO — necesita a César:** ¿llegaste a compilar Modula-2 alguna vez? Si sí: ¿qué compilador, en qué máquina, para qué, y qué te quedó de esa experiencia? Si no: ¿cuándo y cómo te enteraste de que el lenguaje existía?

> 🕳️ **HUECO — necesita a César:** ¿cuál es el lenguaje moderno que te hace decir «esto ya lo vi en Wirth»? (Sospecho Go por lo del compilador rápido y el lenguaje chico, pero es tu opinión la que va al post, no la mía.)

Si te interesa la idea de un lenguaje diseñado para que quepa entero en la cabeza de una persona, el otro caso extremo lo cuento en [[A1-03]]: Forth, que llegó al mismo lugar por el camino exactamente opuesto.

[^wirth82]: Niklaus Wirth, *Programming in Modula-2*, Springer-Verlag, 1982 — DOI [10.1007/978-3-642-96717-7](https://doi.org/10.1007/978-3-642-96717-7). La edición de 1982 no está en archive.org; sí están la [2.ª ed. de 1983](https://archive.org/details/programminginmod00wirt) y la [3.ª ed. de 1985](https://archive.org/details/programminginmod0000wirt), ambas en préstamo controlado.
[^hopl]: [Niklaus Wirth, *Modula-2 and Oberon*](https://free.oberon.org/files/Modula2_and_Oberon.pdf) — paper presentado en HOPL-III, ACM, 2007. DOI: [10.1145/1238844.1238847](https://doi.org/10.1145/1238844.1238847). El relato del propio Wirth sobre cómo y por qué hizo Modula-2.
[^algolw]: N. Wirth y C. A. R. Hoare, *A contribution to the development of ALGOL*, *Communications of the ACM* 9, 6 (junio 1966), pp. 413-432 — DOI: [10.1145/365696.365702](https://doi.org/10.1145/365696.365702).
[^adsp]: [Niklaus Wirth, *Algorithms + Data Structures = Programs*, Prentice-Hall, 1976](https://archive.org/details/algorithmsdatast00wirt) — la edición con el código en Pascal, la que leyó casi todo el mundo.
[^adsp-m2]: [Niklaus Wirth, *Algorithms and Data Structures*, Prentice-Hall, 1986 (© 1985)](https://archive.org/details/algorithmsdatast0000wirt_u9b4) — la reescritura con el código en Modula-2; notar que el título pierde el «= Programs».
[^ad-oberon]: [Niklaus Wirth, *Algorithms and Data Structures*, versión en Oberon del texto de 1985](https://people.inf.ethz.ch/wirth/AD.pdf) — PDF libre en el sitio del autor.
[^hse]: [Niklaus Wirth, *A Brief History of Software Engineering*](https://people.inf.ethz.ch/wirth/Miscellaneous/IEEE-Annals.pdf) — *IEEE Annals of the History of Computing* 30, 3 (2008), pp. 32-39. DOI: [10.1109/MAHC.2008.33](https://doi.org/10.1109/MAHC.2008.33).
[^oberon]: Niklaus Wirth, *From Modula to Oberon*, *Software: Practice and Experience* 18, 7 (julio 1988), pp. 661-670 — DOI: [10.1002/spe.4380180706](https://doi.org/10.1002/spe.4380180706). La autocrítica de Modula-2 escrita por su propio autor.
[^report4]: [*Report on the Programming Language Modula-2*, 4.ª ed., 1988](https://freepages.modula2.org/report4/modula-2.html) — el reporte del lenguaje. [VERIFICAR: este mirror no tiene copia en Wayback; antes de publicar, conseguir un respaldo estable o citar la de Ulm como principal.]
[^ulm]: [Ulm's Modula-2 Library: SYSTEM](https://www.mathematik.uni-ulm.de/modula/man/man3/SYSTEM.html) — la definición del módulo `SYSTEM` en una implementación real.
[^ddj]: [Kent Porter, «Examining Room: The State-of-the-Art in Modula-2», *Dr. Dobb's Journal*, septiembre 1988](https://jacobfilipp.com/DrDobbs/articles/DDJ/1988/8809/8809f/8809f.htm) ([backup en Wayback](http://web.archive.org/web/20241015040002/https://jacobfilipp.com/DrDobbs/articles/DDJ/1988/8809/8809f/8809f.htm)) — review contemporánea de FTL, Logitech, TopSpeed y Stony Brook, con precios.
[^topspeed]: [TopSpeed Modula-2 v3.01, Jensen & Partners International](https://archive.org/details/top-speed-modula-2-v-3.01-ms-dos-already-installed-archive) — en archive.org.
[^ada]: [Ada (programming language)](https://en.wikipedia.org/wiki/Ada_(programming_language)) en Wikipedia — cronología HOLWG (1975), Steelman (1978), Green (1979), ANSI/MIL-STD-1815 (1980), 1815A (1983), ISO (1987).
[^gofaq]: [Go FAQ, «What are Go's ancestors?»](https://go.dev/doc/faq) — «Go is mostly in the C family (basic syntax), with significant input from the Pascal/Modula/Oberon family (declarations, packages)…».
[^rustinf]: [The Rust Reference — *Influences*](https://doc.rust-lang.org/reference/influences.html) — la lista oficial de influencias de Rust, donde Wirth no aparece.
[^wp-m2]: [Modula-2](https://en.wikipedia.org/wiki/Modula-2) en Wikipedia — lectura de contexto.
[^lilith]: [Lilith (computer)](https://en.wikipedia.org/wiki/Lilith_(computer)) en Wikipedia — la workstation del ETH construida alrededor de Modula-2. Contexto, no fuente primaria: para todo lo que dice Wirth de su propia máquina, citar [^hopl].
[^chm]: [Computer History Museum, *In Memoriam: Niklaus Wirth (1934-2024)*](https://computerhistory.org/blog/in-memoriam-niklaus-wirth-1934-2024/) — obituario del CHM (5 de enero de 2024). **Reemplaza al link de «oral history» del draft original, que apuntaba por error al panel de LSI Logic.** [VERIFICAR: el draft prometía una *oral history* de Wirth en el CHM y no pude encontrar ninguna: el perfil del CHM no linkea transcripción, y la única entrevista larga que apareció es la del premio Turing de la ACM (`amturing.acm.org/pdf/WirthTuringTranscript.pdf`, por Elena Trichina), que **devuelve HTTP 403** y por lo tanto no puedo verificar ni citar. Probar: pedirla por otra vía, o usar la lecture del CHM «Odysseys in Technology: How I Became Interested in Programming Languages», que el obituario menciona pero sin link directo.]
[^img_hero]: Imagen de [Niklaus Wirth](https://commons.wikimedia.org/wiki/File:Niklaus_Wirth,_UrGU.jpg) — foto de **Tyomitch**, 3 de octubre de 2005, dando una charla en la Universidad Estatal de los Urales (UrGU). Licencia: **«Copyrighted free use»** (el titular permite cualquier uso, incluidas redistribución comercial y modificación). **Corrección de la pasada de fuentes:** el draft la daba como «(1969)» y como «CC-BY-SA»; **las dos cosas son falsas** — es de 2005 y la licencia no es CC. Atribución sugerida para el post publicado (nombre de footnote `img_hero`, con el formato de la casa): «Imagen de [Niklaus Wirth en la Universidad Estatal de los Urales](https://commons.wikimedia.org/wiki/File:Niklaus_Wirth,_UrGU.jpg) — Copyrighted free use — Tyomitch, 2005.» Si se recorta a 2.5:1 para el hero, anotarlo al final.

