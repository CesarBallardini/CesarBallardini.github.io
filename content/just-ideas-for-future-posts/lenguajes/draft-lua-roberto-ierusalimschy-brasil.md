### A1-19 — Lua: el lenguaje brasileño que terminó embebido en cada motor de videojuegos

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `lua-roberto-ierusalimschy-brasil`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-lua-roberto-ierusalimschy-brasil/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[A1-13]], [[I-09]] (ZinjaI argentino), [[I-10]] (Huayra) — éxitos LATAM
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** Lua nació en 1993 en la PUC-Rio (Pontificia Universidad Católica de Río de Janeiro) por Roberto Ierusalimschy y Luiz Henrique de Figueiredo. Hoy está en World of Warcraft, en Roblox, en Adobe Photoshop, en cada motor de videojuegos importante. El post toma la entrevista en *Masterminds* y discute cómo un lenguaje creado en una universidad latinoamericana terminó embebido en la industria del entretenimiento global.

**Hook:** Roblox usa Lua. World of Warcraft usa Lua. Photoshop usa Lua. Lua se inventó en una universidad de Río de Janeiro hace 30 años. Es probablemente el caso de éxito latinoamericano más grande de la historia de los lenguajes. ¿Cómo pasó?

**Outline:**

1. **Hook — tres productos gigantes y un origen improbable.** Roblox, World of Warcraft, Photoshop; el planteo de que el lenguaje salió de Río de Janeiro y casi nadie lo sabe.
2. **Qué es Lua, en una frase.** No es un lenguaje para escribir aplicaciones: es un lenguaje para meter *adentro* de una aplicación escrita en otra cosa. La categoría «lenguaje embebido» como clave de todo el post.
3. **PUC-Rio, 1993.** El contexto de origen y la hipótesis central: la restricción como motor de diseño, no como handicap.
4. **La entrevista en *Masterminds*.** El punto de entrada del post: qué cuentan Ierusalimschy y de Figueiredo sobre sus propias decisiones.
5. **Las decisiones de diseño que lo hicieron embebible.** Tamaño chico, ANSI C portable, una sola estructura de datos (la tabla), mecanismos en vez de políticas.
6. **La licencia.** MIT, sin fricción: la parte aburrida que probablemente explica más el éxito que cualquier virtud técnica.
7. **Los casos: WoW, Roblox, Photoshop.** Qué hace Lua en cada uno y por qué el patrón se repite — el motor en C/C++, la lógica en Lua.
8. **Por qué importa que sea brasileño.** El contraste con [[I-09]] (ZinjaI) e [[I-10]] (Huayra): exportar un lenguaje no es lo mismo que exportar un producto.
9. **Probalo esta tarde.** lua.org, *Programming in Lua*, y lo poco que hace falta para empezar.
10. **Cierre — la periferia como ventaja.** Qué se puede aprender del caso y qué no se puede generalizar de él.

**Bibliografía:**

_Fuentes primarias — los autores sobre su propio lenguaje (todas fetcheadas y verificadas el 2026-07-16):_

- **[FUENTE PRINCIPAL]** R. Ierusalimschy, L. H. de Figueiredo, W. Celes, «The evolution of Lua», *Proceedings of the third ACM SIGPLAN conference on History of Programming Languages* (HOPL III), ACM, 2007. DOI [10.1145/1238844.1238846](https://doi.org/10.1145/1238844.1238846) — _estable_ (DOI verificado vía `api.crossref.org`). Texto completo libre en el sitio de los autores: [lua.org/doc/hopl.pdf](https://www.lua.org/doc/hopl.pdf) — _estable_. **Es la fuente que sostiene casi todo el post**: origen, Tecgraf, DEL/SOL, Petrobras, reserva de mercado, licencia, la tabla, «developing country», WoW. Leída completa en esta pasada. Nota operativa: el mirror `lua.inf.puc-rio.br/doc/hopl.pdf` que enlaza lua.org/papers.html **falla por certificado TLS**; usar el de lua.org.
- R. Ierusalimschy, L. H. de Figueiredo, W. Celes, «A look at the design of Lua», *Communications of the ACM*, vol. 61, n.º 11, pp. 114–123, 2018. DOI [10.1145/3186277](https://doi.org/10.1145/3186277) — _estable_ (verificado vía Crossref; ACM DL no se deja fetchear). Segundo paper de historia firmado por los tres — sirve para confirmar la autoría triple.
- [Página de papers de lua.org](https://www.lua.org/papers.html) — _estable_. Bibliografía oficial; da la ficha del capítulo de *Masterminds* («pp. 161–176») y de «The implementation of Lua 5.0» (*Journal of Universal Computer Science* 11 #7, 2005) y «Lua: an extensible extension language» (*Software: Practice & Experience* 26 #6, 1996), no usados todavía pero disponibles.
- [[tr-23]] *Masterminds of Programming*, ed. Federico Biancuzzi y Shane Warden, O'Reilly Media, 1.ª edición, marzo de 2009, ISBN 978-0-596-51517-1. Capítulo 7, «Lua», entrevista a Luiz Henrique de Figueiredo y Roberto Ierusalimschy, **pp. 161–176**. En archive.org hay dos copias: [`MastermindsOfProgramming`](https://archive.org/details/MastermindsOfProgramming) — **ojo: es sólo material preliminar, 23 páginas**, sirve para el índice y la ficha, no trae el capítulo — y [`mastermindsofpro0000unse`](https://archive.org/details/mastermindsofpro0000unse) (edición 2009, **préstamo digital controlado**) — _estable_. ⚠️ Las tres citas del capítulo que usa el borrador **no están verificadas** (ver la marca en la sección «La entrevista»).

_Sitio oficial de Lua (todas fetcheadas y verificadas; dominio institucional, `lua.org` — estables):_

- [lua.org](https://www.lua.org/) — sitio oficial.
- [lua.org/about.html](https://www.lua.org/about.html) — definición del lenguaje, origen en PUC-Rio/Tecgraf, mantenimiento actual en LabLua, y las cifras de tamaño de Lua 5.5.0 (388 K / 1,5 M; ~32.000 líneas de C; intérprete 293 K y biblioteca 484 K en Linux 64 bits).
- [lua.org/license.html](https://www.lua.org/license.html) — MIT desde Lua 5.0; relicenciamiento retroactivo de las versiones previas.
- [lua.org/pil/](https://www.lua.org/pil/) — ficha de las cuatro ediciones de *Programming in Lua* con ISBNs, y la 1.ª edición libre en línea ([lua.org/pil/contents.html](https://www.lua.org/pil/contents.html)), apuntando a Lua 5.0.
- [lua.org/demo.html](https://www.lua.org/demo.html) — **no** hostea intérprete propio; sólo enlaza a terceros y no declara versión. No sirve para verificar los ejemplos de código.

_Los tres casos (fetcheadas y verificadas):_

- [Warcraft Wiki — World of Warcraft API](https://warcraft.wiki.gg/wiki/World_of_Warcraft_API) — _frágil_ (wiki comunitaria; ya migró de wowpedia/fandom a `wiki.gg` una vez). Backup Wayback verificado: [snapshot del 2026-04-06](http://web.archive.org/web/20260406114746/https://warcraft.wiki.gg/wiki/World_of_Warcraft_API). Fuente de la cita «The WoW API is used by Blizzard's user interface in Lua and available to AddOns and macro scripts». Load-bearing → backup obligatorio.
- [Roblox Creator Docs — Luau](https://create.roblox.com/docs/luau) — _frágil_ (docs de producto, se reorganizan). Backup Wayback verificado: [snapshot del 2026-06-23](http://web.archive.org/web/20260623061111/https://create.roblox.com/docs/luau). Fuente **exacta** de «Luau is a fast, small, safe, gradually typed embeddable scripting language derived from Lua 5.1» — confirmado que dice «5.1». Nota: la home de [luau.org](https://luau.org/) usa otra redacción («based on Lua with a gradual type system») y el README de GitHub omite el «5.1»; si se cita la frase con «5.1», hay que citar **esta** página.
- [luau.org/why](https://luau.org/why) — _frágil_. Sostiene la historia del fork: «Around 2006, Roblox started using Lua 5.1 as a scripting language for games», que no podían permitirse breaking changes, que gran parte de Luau está escrita desde cero, y el combo linting + gradual type system. También dice que LuaJIT no les servía «in terms of portability, ease of change».
- [Adobe — Lightroom Classic SDK Guide 2020 (PDF)](https://ioconsolerykerprodcdn.azureedge.net/static/installers/lr/sdk/2020/doc/Lightroom%20Classic%20SDK%20Guide%202020.pdf) — _frágil_ (CDN de Adobe, URL con año embebido; es la clase de URL que se cae). Leído en esta pasada; de acá salen «The SDK defines a Lua-language scripting API», la recomendación de lua.org y del libro de Ierusalimschy, «Lightroom 5 uses version 5.1.4 of the Lua language» y el modelo de objetos derivado del capítulo 16 de *Programming in Lua*. **Load-bearing y sin backup: conseguir uno antes de publicar** (Wayback no tenía snapshot al 2026-07-16).
- [Adobe — portal de desarrollo de Lightroom Classic](https://developer.adobe.com/lightroom-classic/) — _frágil_. Backup Wayback verificado: [snapshot del 2026-06-21](http://web.archive.org/web/20260621064357/https://developer.adobe.com/lightroom-classic/). ⚠️ El fetch en vivo llegó **truncado**: el lema «Unleash Lightroom Classic with Lua» está confirmado como título de la página en resultados de búsqueda pero **no lo pude leer en el cuerpo**. Si el post lo cita entre comillas, abrirlo a mano primero.
- [Adobe — Photoshop UXP API Reference](https://developer.adobe.com/photoshop/uxp/2022/ps_reference/) y [guías de UXP para Photoshop](https://developer.adobe.com/photoshop/uxp/2022/guides/) — _frágiles_. Las dos fetcheadas: **Lua no aparece en ninguna**; automatización vía UXP/JavaScript, con la DOM API como «the successor to ExtendScript». Es el respaldo de la corrección «Photoshop no usa Lua». Nota: `helpx.adobe.com/photoshop/using/scripting.html` (que sería la fuente para VBScript y AppleScript) **no se dejó fetchear** —timeout y ECONNRESET— y no tiene snapshot en Wayback; por eso la prosa se recortó a lo verificable.

_LuaJIT:_

- [luajit.org/luajit.html](https://luajit.org/luajit.html) — _frágil_ (sitio personal de un solo mantenedor). Autor Mike Pall, MIT, «in continuous development since 2005», Lua 5.1 API+ABI, BitOp, FFI, copyright 2005-2026.
- [github.com/LuaJIT/LuaJIT](https://github.com/LuaJIT/LuaJIT) — _estable-ish_. «Mirror of the LuaJIT git repository», rama v2.1. Sin fecha de release ni declaración de estado (ver marca `[VERIFICAR:]`).

_Nota de descarte:_

- Hay un artículo de Wikipedia sobre Luau que aparece en las búsquedas. **No se agrega y no se debe usar como cita**: no lo fetcheé, y además para todo lo que cubre hay fuente de primera mano (Roblox docs, luau.org/why). Regla de la casa: la fuente del autor le gana a Wikipedia.

**Imágenes:** _a definir_

**Tags propuestos:** `['Lua','Ierusalimschy','Brasil','PUC-Rio','videojuegos','historia local']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (10 secciones), se fijó `Length target: medium` y se escribió un borrador de prosa completo (~1750 palabras de prosa efectiva) en la sección «Borrador de prosa» al pie.

**Pasada de fuentes del 2026-07-16.** La premisa central del post **se sostiene y está mejor respaldada que antes**: la tesis de que Lua es el mayor caso de éxito de un lenguaje de la periferia la dicen los propios autores, textual, en el paper de HOPL III — «Lua is the only language created in a developing country to have achieved global relevance» — y eso está verificado leyendo el PDF completo, no un resumen. Todo el andamiaje histórico del post (Tecgraf creado en mayo de 1987, DEL y SOL para Petrobras, la reserva de mercado del 77-92, el nombre sugerido por Carlos Henrique Levy, la historia de la licencia, la tabla como única estructura) quedó verificado palabra por palabra contra esa misma fuente.

Lo que **agregó** esta pasada:

- **Se definieron los 11 footnotes que la prosa citaba pero que no existían.** El borrador referenciaba `[^hopl]`, `[^about]`, `[^license]`, `[^wowapi]`, `[^luau]`, `[^robloxluau]`, `[^lrsdk]`, `[^lradobe]`, `[^psuxp]`, `[^luajit]` y `[^hopl2]` sin definirlos en ninguna parte: el post citaba fuentes fantasma. Ahora todas están definidas y fetcheadas.
- Bibliografía reescrita: de 3 entradas sueltas a ~20 fuentes verificadas, con flag de bitrot y backups de Wayback en las frágiles load-bearing.
- Los dos papers de historia de los autores (HOPL III 2007 y CACM 2018), con DOI verificado vía Crossref, más el texto libre del HOPL en lua.org.

**Dos hallazgos que corrigen a la pasada anterior — leer antes de tocar el texto:**

1. **⚠️ Las tres citas de *Masterminds* no están verificadas.** La pasada del 2026-07-15 las declaró «verificadas contra el texto del libro» y dijo haber «releído el capítulo entero». **Esa declaración no es confiable**: la misma pasada dio el capítulo como «pp. 161–183» cuando el índice del propio libro lo ubica en **161–176** (cap. 7 en p. 161, cap. 8 en p. 177), error que no cometería quien hubiera leído el capítulo hasta el final; lua.org confirma «pp. 161–176» de forma independiente. Esta pasada no consiguió el cuerpo del capítulo (el PDF de archive.org es sólo front matter; O'Reilly da 403; el préstamo controlado no es consultable desde acá). **Las tres citas hay que cotejarlas contra el libro antes de publicar.** La buena noticia: la más importante —la de «developing country»— está verificada en su versión del paper de HOPL III, así que la tesis del post no depende de esto.
2. **La corrección Photoshop→Lightroom se confirma y se refuerza.** Dos páginas oficiales de Adobe fetcheadas: Lua no aparece en la documentación de Photoshop (automatización vía UXP/JavaScript, con la DOM API como sucesora de ExtendScript). La guía del SDK de Lightroom Classic 2020 sí dice, textual, «The SDK defines a Lua-language scripting API» y «Lightroom 5 uses version 5.1.4 of the Lua language». Se recortó de la prosa la mención a VBScript y AppleScript: `helpx.adobe.com` no se dejó fetchear (timeout / ECONNRESET, sin snapshot en Wayback) y el dato quedó fuera por no verificable. **El Hook y el `**Concepto:**` de esta entrada siguen diciendo «Photoshop» y siguen mal** — hay que corregirlos (son de César, esta pasada no los toca).

Lo que sigue **pendiente** (ver las marcas en el texto):

- Cotejar las tres citas de *Masterminds* contra el papel (marca en «La entrevista»).
- Correr los ejemplos de código Lua (marca en «Las decisiones»). Ojo: `lua.org/demo.html` no sirve — no hostea intérprete propio, sólo enlaza a terceros sin declarar versión.
- El estado de LuaJIT en 2026 (marca en «Probalo esta tarde»). Se agotó el camino obvio: ni luajit.org ni el repo de GitHub declaran versión estable con fecha ni estado del proyecto. Recomendación: no opinar sobre su vitalidad.
- Conseguir backup de Wayback para el PDF del SDK de Lightroom — es load-bearing y su URL (CDN de Adobe, con el año embebido) es de las que se caen.
- **La autoría triple** (Ierusalimschy, de Figueiredo **y Waldemar Celes**) queda **confirmada por partida doble**: el paper de HOPL III dice «The creators of Lua were Roberto Ierusalimschy, Luiz Henrique de Figueiredo, and Waldemar Celes», y los tres firman los dos papers de historia. El `**Concepto:**` y el Hook nombran sólo a dos y hay que corregirlos antes de publicar.
- Los 7 huecos `🕳️` de César, intactos.
- `**Imágenes:**` sigue en `_a definir_`.

_(Lo que sigue es el registro de la pasada anterior, del 2026-07-15.)_

Lo que quedó **escrito**: el armazón argumental entero — la categoría «lenguaje embebido» como clave de todo, la restricción como motor de diseño, las decisiones técnicas (tamaño, ANSI C, la tabla como única estructura, mecanismos en vez de políticas), la licencia como explicación aburrida y probablemente correcta del éxito, el patrón motor-en-C/lógica-en-Lua que se repite en los tres casos, el contraste con [[I-09]] e [[I-10]], y el cierre sobre la periferia. Se sostiene solo como ensayo.

Lo que quedó como **hueco**:

- 7 huecos `🕳️` pidiendo a César recuerdos y opiniones propias: si escribió Lua alguna vez y en qué contexto, si se cruzó con lenguajes embebidos en el sector público, qué le pasó al leer la entrevista en *Masterminds*, si conoció el origen brasileño antes o después de usar el lenguaje, su lectura del contraste con los casos argentinos, y el veredicto del cierre. Sin eso es un ensayo correcto pero impersonal — todavía no es un post de katra.
- 17 marcas `[VERIFICAR:]` sobre datos que **no** están respaldados por la bibliografía listada: el año y el lugar de origen, la autoría (ver punto siguiente), el contexto institucional del grupo en PUC-Rio y sus proyectos previos, la hipótesis del contexto brasileño de restricción a la importación, la licencia exacta y desde qué versión, el tamaño real del intérprete, la cronología de WoW / Roblox / Photoshop y qué hace Lua en cada uno, la relación entre Lua y LuaJIT / Luau, la ficha bibliográfica de *Programming in Lua* 4.ª ed y si hay una edición libre en línea, y las URLs.
- **Punto abierto importante — la autoría.** El `**Concepto:**` de este draft nombra a dos autores (Ierusalimschy y de Figueiredo). Hay que chequear contra `lua.org` y contra el capítulo de [[tr-23]] si el equipo original tuvo un tercer integrante; si lo tuvo, el concepto y el hook de esta entrada están incompletos y hay que corregirlos antes de publicar. La prosa está escrita de manera que no se rompe si aparece un tercer nombre, pero la marca está puesta.
- Los ejemplos de código Lua del borrador están escritos de memoria y **no fueron ejecutados**. Hay que correrlos antes de publicar.
- La bibliografía es delgada a propósito (tres fuentes). **Antes de publicar hay que decidir** si se resuelven los `[VERIFICAR:]` sumando fuentes nuevas al plan — los papers de historia del lenguaje escritos por los propios autores serían el candidato natural, si se los verifica — o si se recorta el post a lo que estas tres sostienen.
- `**Imágenes:**` sigue en `_a definir_`.

---

## Borrador de prosa

Si jugaste World of Warcraft y te instalaste un addon, ejecutaste Lua.[^wowapi] Si tu hijo o tu sobrino hace juegos en Roblox, escribe Luau, un derivado de Lua.[^luau] Si automatizaste algo en Adobe Lightroom, hay Lua abajo.[^lrsdk]

> **Corrección de la pasada de fuentes (2026-07-15):** el borrador decía «Photoshop». **Es falso.** Photoshop se automatiza con JavaScript — hoy vía UXP, antes vía ExtendScript, que la documentación de Adobe da por sucedido: la API de UXP es «the successor to ExtendScript». Lua no aparece en ninguna parte de la documentación oficial de Photoshop.[^psuxp] [^psuxpg] El producto de Adobe que sí usa Lua es **Lightroom**, cuyo SDK «defines a Lua-language scripting API».[^lrsdk] La confusión tiene una raíz real y vale la pena contarla en el post: el producto se llamó durante años *Adobe Photoshop Lightroom*, y el propio capítulo de *Masterminds* lo nombra así — «Adobe's Photoshop Lightroom».[^masterminds] Alguien recortó la marca a «Photoshop» y el dato viajó mal desde entonces. El Hook y el `**Concepto:**` de esta entrada todavía dicen «Photoshop» y hay que corregirlos antes de publicar (ver `**Estado actual:**`).

Ese lenguaje se diseñó en una universidad de Río de Janeiro. Y voy a decir algo más fuerte todavía: es, con bastante distancia, el caso de éxito latinoamericano más grande de la historia de los lenguajes de programación. No hay segundo cómodo.

Lo raro no es que haya pasado. Lo raro es que casi nadie lo sepa.

### Qué es Lua, en una frase

Antes de la historia, la categoría, porque si no se entiende esto no se entiende nada del resto.

Lua no es un lenguaje para escribir aplicaciones. Es un lenguaje para meter **adentro** de una aplicación escrita en otra cosa.

Esa distinción parece un detalle y es todo el post. Python compite con Java por ver quién escribe tu backend. Lua no compite con nadie por eso, porque no está jugando ese partido. Lua es lo que le enchufás a tu programa en C o C++ cuando tenés un motor que anda rápido pero necesitás que la lógica de arriba se pueda cambiar sin recompilar, y ojalá que la puedan escribir personas que no son tus programadores de sistemas — diseñadores de niveles, artistas, usuarios finales, chicos de doce años.

Cuando entendés que la categoría es «lenguaje embebido», el resto de las decisiones de Lua dejan de parecer minimalismo estético y se vuelven consecuencias lógicas.

### PUC-Rio, 1993

Lua nació en 1993, en la Pontificia Universidad Católica de Río de Janeiro. No en el departamento de computación en abstracto: adentro de **Tecgraf**, el Grupo de Tecnología en Computación Gráfica de la PUC-Rio, un laboratorio de I+D creado en mayo de 1987 que trabajaba con socios industriales.[^hopl]

Y fueron **tres**, no dos: Roberto Ierusalimschy, Luiz Henrique de Figueiredo y **Waldemar Celes**.[^hopl] Los tres eran miembros de Tecgraf, con formaciones distintas — Roberto era profesor asistente de computación e investigaba lenguajes de programación; Luiz Henrique era matemático, posdoc primero en el IMPA y después en Tecgraf, interesado en herramientas de software y computación gráfica; Waldemar era doctorando en computación, ingeniero interesado en aplicaciones de computación gráfica.[^hopl]

> **Corrección de la pasada de fuentes (2026-07-15):** el `**Concepto:**` y el Hook de esta entrada nombran sólo a dos autores. **Es un error y hay que corregirlo antes de publicar.** El origen del error es identificable: en *Masterminds* el capítulo de Lua entrevista sólo a de Figueiredo y a Ierusalimschy — pero el propio texto de presentación del capítulo dice que Lua fue creado «by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, and Waldemar Celes in 1993».[^masterminds] Los dos entrevistados no son los dos autores. Waldemar Celes es coautor del lenguaje y de los dos papers de historia que firman los tres.[^hopl] [^hopl2] Un post sobre reconocimiento latinoamericano que se olvida de nombrar a uno de los suyos sería exactamente la falla que denuncia.

Y hubo antecesores directos, que son la mejor parte de la historia y que el borrador no tenía. El socio más grande de Tecgraf era —y sigue siendo— **Petrobras**, la petrolera brasileña. Para Petrobras, Tecgraf había desarrollado dos «little languages» específicos que fueron los ancestros de Lua:[^hopl]

- **DEL** («data-entry language»), de 1992: un lenguaje declarativo para describir formularios de carga de datos para simuladores numéricos, cuyos archivos de entrada eran columnas de números heredadas de la época de las tarjetas perforadas. Cuando los usuarios empezaron a pedir condicionales y bucles, quedó claro que hacía falta un lenguaje de verdad.[^hopl]
- **SOL** («Simple Object Language»): el lenguaje de configuración de PGM, un generador de reportes de perfiles litológicos, también para Petrobras. De SOL salió la sintaxis de constructores de Lua.[^hopl]

El nombre sale de ahí: SOL es *sol* en portugués, y un colega de Tecgraf, Carlos Henrique Levy, sugirió llamar **Lua** —*luna*— al lenguaje que lo sucedía.[^hopl]

Acá hay una hipótesis que quiero poner sobre la mesa con cuidado, porque es seductora y por eso mismo hay que desconfiar de ella: la idea de que Lua salió como salió **a causa** de la restricción, no a pesar de ella.

Buena noticia para la hipótesis: **no hay que ponérsela en la boca a nadie, porque la dicen ellos.** Y hay que decir dónde la dicen, que no es un detalle menor.

Entre 1977 y 1992 Brasil tuvo una política de fuertes barreras comerciales para hardware y software —la famosa **reserva de mercado**— motivada, en palabras de los propios autores, por «a nationalistic feeling that Brazil could and should produce its own hardware and software». La consecuencia concreta para Tecgraf, según el paper de HOPL III que firman los tres:[^hopl]

> «In that atmosphere, Tecgraf's clients could not afford, either politically or financially, to buy customized software from abroad: by the market reserve rules, they would have to go through a complicated bureaucratic process to prove that their needs could not be met by Brazilian companies. Added to the natural geographical isolation of Brazil from other research and development centers, those reasons led Tecgraf to implement from scratch the basic tools it needed.»

Y sobre por qué no adoptaron un lenguaje existente en 1993, tampoco hay que inferir nada:[^hopl]

> «In 1993, the only real contender was Tcl […] However, Tcl had unfamiliar syntax, did not offer good support for data description, and ran only on Unix platforms. We did not consider LISP or Scheme because of their unfriendly syntax. Python was still in its infancy. In the free, do-it-yourself atmosphere that then reigned in Tecgraf, it was quite natural that we should try to develop our own scripting language.»

**Advertencia de procedencia, importante para la honestidad del post:** esto está en *The Evolution of Lua* (HOPL III, 2007), **no** en la entrevista de *Masterminds*. Revisé el capítulo entero de Lua del libro y la reserva de mercado no aparece: ni «market reserve», ni «Brazil», ni «Petrobras», ni «Tecgraf» figuran en las respuestas de los entrevistados. Así que el post no puede decir «como cuentan en la entrevista»; tiene que citar el paper. Es una fuente mejor, además: es de los tres autores y es la historia oficial del lenguaje.

El argumento es este. Si estás en el centro del mundo, con presupuesto y con acceso, tu solución natural a «necesito un lenguaje de scripting» es comprar o adoptar uno que ya existe. Si estás lejos, y la respuesta obvia no está disponible o no está en tu idioma o no corre en la máquina que tenés, tenés que hacerlo vos. Y cuando lo hacés vos, con un equipo chico y sin recursos, el resultado tiende a ser chico, portable y sin dependencias — porque no te podés dar el lujo de otra cosa.

Chico, portable y sin dependencias resultó ser, exactamente, la especificación de lo que la industria de los videojuegos iba a necesitar diez años después. Nadie lo planeó así.

### La entrevista

*Masterminds of Programming*[^masterminds] es un libro de entrevistas a creadores de lenguajes — ya le dediqué un post al roster completo [[A1-13]], así que acá voy directo al capítulo que importa.

> 🕳️ **HUECO — necesita a César:** ¿qué te pasó cuando leíste el capítulo de Lua en *Masterminds*? ¿Hubo alguna respuesta que te haya hecho parar? Una o dos frases — es el ancla personal del post.

> 🕳️ **HUECO — necesita a César:** ¿vos sabías que Lua era brasileño antes de leer la entrevista, o te enteraste ahí? La respuesta cambia el tono del post entero: si te enteraste tarde, el post es una confesión; si ya lo sabías, es una reivindicación.

El capítulo de Lua es el **capítulo 7**, y lo firman —en ese orden— Luiz Henrique de Figueiredo y Roberto Ierusalimschy. Va de la **página 161 a la 176** de la primera edición de O'Reilly (marzo de 2009), y tiene tres secciones: «The Power of Scripting» (p. 162), «Experience» (p. 165) y «Language Design» (p. 169).[^mmtoc] [^luapapers]

> **Corrección de la pasada de fuentes (2026-07-16):** una pasada anterior escribió acá «páginas 161–183». **Es incorrecto.** El índice de la propia edición de O'Reilly da el capítulo 7 (LUA) en la página 161 y el capítulo 8 (HASKELL) en la 177, o sea que el capítulo de Lua termina en la 176.[^mmtoc] La página de papers de lua.org lo confirma de forma independiente: «pp. 161–176».[^luapapers]

Las tres citas que siguen las dejó anotadas esa misma pasada anterior como «verificadas contra el texto del libro». **Esta pasada no las pudo confirmar** y hay que tratarlas como no verificadas hasta que alguien las coteje contra el libro en papel (ver la marca al pie del bloque):

**Sobre el éxito y la periferia** — es la cita que sostiene la tesis central del post, y la dice Luiz Henrique de Figueiredo, no el post:

> «Finally, Lua is the only language created in a developing country to have achieved such global relevance. It is the only such language to have ever been featured in ACM HOPL.»[^masterminds]

(La misma afirmación, con las mismas palabras, aparece en el paper de HOPL III: «Lua is the only language created in a developing country to have achieved global relevance».[^hopl] Los autores la repiten a propósito.)

**Sobre qué es Lua**, definición de de Figueiredo en una línea:

> «An embeddable, lightweight, fast, powerful scripting language.»[^masterminds]

**Sobre la palabra «scripting»**, Ierusalimschy, que sirve para la sección «Qué es Lua, en una frase» y explica por qué el post insiste tanto con la categoría:

> «Unfortunately, more and more people use "scripting language" as a synonym for "dynamic language." […] That is sad, because we lose the precision to describe a particular class of dynamic languages. Lua is a scripting language in the original meaning of the expression.»[^masterminds]

[VERIFICAR: **las tres citas de *Masterminds* de arriba, palabra por palabra, contra el libro en papel.** Una pasada anterior las declaró «verificadas contra el texto del libro»; esta pasada no pudo reproducir esa verificación y esa declaración quedó desacreditada por otro lado: la misma pasada dio el capítulo como «161–183» cuando el índice del propio libro dice 161–176, que es un error que no cometería quien hubiera leído el capítulo hasta el final. Dónde busqué: el PDF de archive.org (`MastermindsOfProgramming`) resultó ser **sólo material preliminar, 23 páginas** — tiene el índice (que sí sirvió para fijar el capítulo y las páginas) pero no el cuerpo del capítulo; el préstamo controlado (`mastermindsofpro0000unse`) existe pero su búsqueda interna no es accesible desde acá; la API de full-text de archive.org no respondió; el capítulo en oreilly.com (`.../9780596801670/ch07.html`) devuelve HTTP 403. Nota importante: la cita de «developing country» **sí está verificada en su versión del paper de HOPL III** —textual, la leí en el PDF— así que la tesis del post no depende de esta marca; lo que está sin confirmar es que de Figueiredo diga eso *en la entrevista*, y la frase de HOPL dice «to have achieved global relevance», sin la segunda oración sobre ACM HOPL. **Camino más corto:** si César tiene el libro, se resuelve en dos minutos. Si no, usar la versión de HOPL y citar el paper.]

[VERIFICAR: cuáles de estas tres citas entran y dónde — decisión editorial de César, no un problema de fuentes (supuesto que se resuelva la marca anterior). La de «developing country» debería entrar sí o sí: es la tesis del post dicha por uno de los autores, y en su versión de HOPL III está verificada y es citable ya mismo.]

### Las decisiones

Lo que hace que Lua se pueda embeber no es una cosa, son cuatro, y todas apuntan al mismo lado.

**El tamaño.** El intérprete entero es minúsculo. Entra en tu binario sin que se note. Y acá van los números reales, que el sitio oficial publica para Lua 5.5.0:[^about]

- el tarball completo —código fuente **y** documentación— pesa 388 K comprimido y 1,5 M sin comprimir;
- el fuente son unas **32.000 líneas de C**;
- en Linux de 64 bits, el intérprete compilado con todas las bibliotecas estándar ocupa **293 K**, y la biblioteca de Lua **484 K**.

Trescientos kilobytes. Un lenguaje de programación completo, con su biblioteca estándar, ocupa menos que una foto del celular.

**ANSI C puro.** Lua está escrito en C estándar, sin extensiones. Eso significa que compila en cualquier lado donde haya un compilador de C, que es casi la definición de «en cualquier lado»: consolas de videojuegos con toolchains propietarios raros, sistemas embebidos, plataformas que no existían cuando Lua se escribió. Es la decisión menos glamorosa de la lista y probablemente la más rentable.

**Una sola estructura de datos.** Lua tiene tablas. Nada más. La tabla es el arreglo, el diccionario, el objeto, el módulo y el espacio de nombres.

```lua
local jugador = { nombre = "Ana", hp = 100 }
jugador.hp = jugador.hp - 10
```

Eso es un objeto. Y también es un diccionario. Y si le ponés claves numéricas, es una lista. Una estructura, cinco usos. Para un lenguaje que tiene que caber en pocos kilobytes, no poder darse el lujo de tener cinco estructuras es una restricción; que la única que quede alcance para todo es diseño.[VERIFICAR: ejemplo escrito de memoria y **no ejecutado** — sigue pendiente. No es un problema de fuentes sino de ejecución. Sobre el camino que sugería la marca anterior: `lua.org/demo.html` **no hostea un intérprete propio**, sólo enlaza a terceros (OneCompiler, Tutorials Point, myCompiler) y no declara qué versión corre cada uno, así que no sirve como verificación citable. Lo correcto es instalar Lua (`lua -v` no existe en esta máquina) y correr el snippet. La afirmación conceptual que rodea al ejemplo —que la tabla es la única estructura de datos de Lua— **sí** quedó verificada, textual, contra el paper de los autores: «Lua offers tables as its sole data-structuring mechanism».[^hopl]]

Y no es una lectura del post: es lo que los autores señalan como la característica principal del lenguaje. «The main characteristic of Lua, and a vivid expression of its simplicity, is that it offers a single kind of data structure, the table […] Although most scripting languages offer associative arrays, in no other language do associative arrays play such a central role.»[^hopl]

**Mecanismos, no políticas.** Lua no te trae un sistema de objetos con herencia y clases. Te trae metatablas, que son el mecanismo con el que vos te construís el sistema de objetos que quieras — o ninguno, si no lo necesitás. La consecuencia es que Lua no te impone una manera de programar, y eso es justamente lo que querés de un lenguaje que va a vivir adentro del programa de otro, con las convenciones de otro.

Es una filosofía de diseño con la que se puede discutir — hay quien dice que «armate el tuyo» produce quince sistemas de objetos incompatibles, y tiene un punto. Pero para la categoría «embebido», ganó.

### La parte aburrida que explica todo

Ahora la razón que a nadie le gusta escuchar, porque no es técnica ni romántica.

La licencia.

Lua se distribuye bajo la licencia **MIT** — no «de tipo MIT»: la MIT, la conocida.[^license] Podés meterlo en tu juego comercial, no publicar tu código, no pagar nada, no pedir permiso, no avisarle a nadie.

Pero la intuición del borrador era correcta: **Lua no siempre tuvo esta licencia**, y la historia del cambio es mejor que la licencia misma. Son tres etapas:[^hopl] [^license]

1. **Lua 1.1** (1994) salió con una licencia restrictiva: libre para uso académico, pero el uso comercial había que negociarlo. Los autores son brutales sobre el resultado: «That part of the license did not work: although we had a few initial contacts, **no commercial uses were ever negotiated**».
2. **Lua 2.1** pasó a software libre sin restricciones, con un texto propio escrito por ellos: «Naively, we wrote our own license text as a slight collage and rewording of existing licenses». Ese texto casero terminó siendo un problema — no estaba claro si era compatible con la GPL.
3. **Lua 5.0** (mayo de 2002) adoptó la MIT. Ironía fina: en julio de 2002 la Free Software Foundation confirmó que la licencia vieja **sí** era compatible con GPL, pero ya estaban comprometidos con la MIT. «Questions about our license have all but vanished since then.»

El sitio oficial aclara además que las versiones anteriores a la 5.0 pueden considerarse retroactivamente relicenciadas bajo MIT.[^license]

Y fijate el detalle que le da fuerza a la sección: los autores no cambiaron de licencia por ideología. Cambiaron porque la restricción comercial **no les servía ni siquiera para lo académico** — «restrictions on commercial uses might even discourage academic uses, since some academic projects plan to go to market eventually».[^hopl] Es un argumento pragmático, y es el que terminó habilitando todo lo demás.

Pensá en el escenario real. Sos un estudio de videojuegos en 2004, tenés un motor en C++, necesitás scripting, tenés abogados y tenés deadline. La pregunta que decide no es «¿cuál lenguaje tiene mejor semántica?». Es «¿cuál puedo meter en el disco que vendo sin que legales tarde tres meses?». Lua contestaba esa pregunta con un «ya, ahora mismo, gratis».

Me resisto a la conclusión y creo que es cierta igual: buena parte del éxito global de un lenguaje académico brasileño se explica por un archivo de texto de veinte líneas.

### El patrón se repite

Mirá los tres casos del principio y vas a ver la misma forma.

Motor pesado en C o C++, escrito por especialistas, optimizado hasta el hueso, que casi nunca cambia. Lógica de arriba en Lua, escrita por gente que no es de sistemas, que cambia todos los días. El límite entre las dos capas es la API de C de Lua.

**En World of Warcraft**, la interfaz y los addons. La wiki de referencia de la API lo dice sin vueltas: «The WoW API is used by Blizzard's user interface in Lua and available to AddOns and macro scripts».[^wowapi] O sea: no es que los addons sean en Lua y el juego en otra cosa — **la interfaz propia de Blizzard también está escrita en Lua**, y los addons usan exactamente la misma API. Es el patrón motor/lógica en su forma más pura. (WoW ya figuraba en la lista de juegos famosos con Lua del paper de 2007.[^hopl])

**En Roblox**, con una aclaración que el post necesita hacer: Roblox **ya no usa Lua a secas**. Usa **Luau**, un lenguaje derivado que Roblox mantiene y que su propia documentación define como «a fast, small, safe, gradually typed embeddable scripting language derived from Lua 5.1».[^robloxluau] Roblox venía usando Lua 5.1 desde alrededor de 2006 y, al no poder permitirse romper compatibilidad con una base de código enorme, terminó bifurcando: reescribieron el compilador desde cero y le agregaron un sistema de tipos gradual y linting.[^luau] Decir «Roblox usa Lua» en 2026 es, entonces, media verdad: usa un descendiente de Lua 5.1 que ya tomó su propio camino. Lo cual, dicho sea de paso, **refuerza** la tesis del post en vez de debilitarla — que la industria bifurque tu lenguaje para escalarlo es una forma de éxito, no de fracaso.

**En Lightroom** —no en Photoshop, ver la corrección del principio— la automatización y los plug-ins. El SDK oficial de Adobe lo dice literalmente: «The SDK defines a Lua-language scripting API. For guidance on using the Lua language, we recommend reviewing the official Lua web site, http://www.lua.org/, and the book "Programming in Lua, second edition," by Roberto Ierusalimschy». O sea que Adobe le manda sus propios desarrolladores de plug-ins al sitio y al libro de los autores. Y precisa la versión: «Lightroom 5 uses version 5.1.4 of the Lua language».[^lrsdk] Detalle que le sirve al post: esa frase sigue impresa tal cual en la **guía de 2020**, años después de Lightroom 5 — otra vez Lua 5.1 congelada como sustrato, igual que Roblox y LuaJIT. El modelo de objetos del SDK, además, sale del libro: «Lightroom's object and class model is derived from the one described in Chapter 16 of "Programming in Lua"».[^lrsdk] Sigue vigente: Adobe mantiene la página de desarrollo de Lightroom Classic bajo el lema «Unleash Lightroom Classic with Lua».[^lradobe]

Y el caso de Roblox tiene una vuelta que me parece la más linda de toda la historia. Un lenguaje diseñado en una universidad para que la lógica de aplicaciones la pudiera escribir gente que no era programadora terminó siendo, treinta años después, el primer lenguaje de programación de millones de chicos en todo el planeta. La restricción original — «tiene que ser simple para el que no es de sistemas» — se convirtió, sin que nadie lo buscara, en política educativa a escala global.

> 🕳️ **HUECO — necesita a César:** ¿escribiste Lua alguna vez? ¿En qué contexto — un juego, un plugin, un dispositivo, un archivo de configuración de algo? Si nunca lo escribiste, decilo así de simple: un post sobre Lua escrito por alguien que lo admira desde afuera es igual de honesto, pero hay que declararlo.

> 🕳️ **HUECO — necesita a César:** ¿te cruzaste con lenguajes embebidos en tu trabajo en el sector público — algo con scripting adentro, un sistema donde la lógica se cambiaba sin recompilar? No hace falta que sea Lua; el punto es si el patrón te resulta familiar desde la experiencia o sólo desde la lectura.

### Por qué importa que sea brasileño

Acá está el nudo del post, y quiero llegar con cuidado.

En este plan tengo otros dos casos de software latinoamericano que salieron bien: ZinjaI [[I-09]], el IDE argentino de C++ con el que estudió mucha gente, y Huayra [[I-10]], la distro del Conectar Igualdad. Los dos son buenos. Los dos son motivo de orgullo. Y los dos son de otra especie que Lua.

La diferencia no es de calidad, es de categoría. ZinjaI y Huayra son **productos**: los usás, se ven, tienen nombre en la pantalla, y su alcance es el de su comunidad. Lua es **infraestructura**: no lo ves nunca, no tiene pantalla, y está adentro de productos ajenos que facturan miles de millones.

Exportar un producto es difícil. Exportar una pieza de infraestructura que la industria del centro adopta sin preguntar de dónde vino es otra cosa. Es más difícil, dura más, y — este es el precio — es invisible. Millones de personas usan Lua todos los días. Un porcentaje ínfimo sabe que salió de Río.

> 🕳️ **HUECO — necesita a César:** ¿comprás la distinción producto/infraestructura, o te parece que le estoy bajando el precio a ZinjaI y a Huayra para que Lua brille? Es el párrafo más discutible del post y prefiero tu veredicto antes que el mío.

> 🕳️ **HUECO — necesita a César:** ¿hay algo que te toque personalmente en esto de que el software de la periferia sea reconocido o no? Tu paso por el sector público te da una perspectiva sobre software local que yo no puedo inventar — pero sólo vos podés decir cuál es.

### Probalo esta tarde

Lua se baja de lua.org[^lua], compila en minutos y arranca en un intérprete interactivo. Es de los lenguajes más rápidos de tener andando que conozco: no hay entorno, no hay gestor de paquetes, no hay ceremonia. Hay un binario.

Y para aprenderlo hay algo poco común: *Programming in Lua*[^pil], escrito por el propio Ierusalimschy. El manual del lenguaje escrito por quien lo diseñó, que es la clase de fuente que uno querría tener para todos los lenguajes y casi nunca tiene.

La ficha, verificada contra el sitio oficial: *Programming in Lua*, 4.ª edición, editorial **Lua.org**, **agosto de 2016**, ISBN **8590379868**. Hay cuatro ediciones, todas de Lua.org y todas de Ierusalimschy: 1.ª (diciembre de 2003, ISBN 8590379817), 2.ª (marzo de 2006, ISBN 8590379825), 3.ª (enero de 2013, ISBN 859037985X) y 4.ª (agosto de 2016, ISBN 8590379868).[^pil]

Y el dato práctico que le sirve al lector: **la primera edición está completa y gratis en línea**, en `lua.org/pil/contents.html`. Apunta a Lua 5.0, así que hay diferencias con las versiones actuales — el propio sitio avisa que «remains largely relevant for later versions, but there are some differences» y pide considerar comprar la edición vigente para bancar el proyecto. Para decidir si Lua te interesa, sobra.[^pil]

Sobre **LuaJIT**, que el borrador se preguntaba si mencionar: sí, conviene, aunque sea en un párrafo. Es un compilador Just-In-Time para Lua escrito por **Mike Pall**, en desarrollo desde 2005 y distribuido también bajo MIT. Implementa **Lua 5.1** —su API y su ABI— y le suma JIT, la biblioteca BitOp y una FFI.[^luajit] Es decir: igual que Roblox, la industria se quedó anclada en 5.1 y construyó para el costado. Ese patrón —Lua 5.1 como sustrato del que salen Luau y LuaJIT mientras la rama oficial va por 5.5— es material para un párrafo bueno sobre qué significa «éxito» para un lenguaje chico.

[VERIFICAR: el estado de LuaJIT en 2026 — **sigue sin resolverse, y ya se agotó el camino obvio.** Verificado en luajit.org/luajit.html: «LuaJIT is Copyright © 2005-2026 Mike Pall, released under the MIT open source license», «LuaJIT has been in continuous development since 2005», y que implementa la «Lua 5.1 API+ABI» más JIT, BitOp y FFI.[^luajit] Lo que **no** está en el sitio oficial: número de versión estable actual, fecha de release, o declaración de estado del proyecto. La marca anterior mandaba a chequear GitHub: lo hice (github.com/LuaJIT/LuaJIT, «Mirror of the LuaJIT git repository»), y la rama es **v2.1**, pero el repo tampoco trae fecha de release ni declaración de estado ni recomendación explícita de rama.[^luajitgh] Queda por probar: las tags/releases del repo con `gh api repos/LuaJIT/LuaJIT/tags`, o la lista de correo. **Alternativa segura y recomendada:** decir sólo lo verificado —autor, licencia MIT, que implementa la API/ABI de 5.1, que existe desde 2005— y no opinar sobre su vitalidad hoy. El párrafo funciona igual sin eso.]

### La periferia

Cierro con lo que me parece la lección, y con la advertencia de que no se puede estirar.

La historia de Lua se cuenta fácil como fábula: la periferia gana, la restricción es virtud, no hace falta plata, hace falta talento. Y es una fábula peligrosa, porque por cada Lua hay cientos de proyectos igual de buenos hechos en universidades igual de buenas que no llegaron a ningún lado. La restricción no es una ventaja competitiva. Es una restricción.

Lo que sí me parece verdadero, y más modesto, es esto: el equipo de PUC-Rio no trató de competir de frente. No hizo «el Python brasileño». Encontró un hueco que en el centro nadie estaba mirando con atención — un lenguaje chiquito, portable, sin licencia molesta, para meter adentro de otra cosa — y lo llenó tan bien que cuando la industria necesitó exactamente eso, la única respuesta madura sobre la mesa venía de Río de Janeiro.

No ganaron por ser de la periferia. Ganaron porque miraron un problema que el centro consideraba menor.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto. ¿Lua te da orgullo latinoamericano, o te da bronca que treinta años después haya que explicarle a la gente de dónde salió? Cualquiera de las dos cierra bien, pero tiene que ser la tuya.

---

[^masterminds]: Luiz Henrique de Figueiredo y Roberto Ierusalimschy, entrevistados en el capítulo 7 («Lua»), pp. 161–176, de *Masterminds of Programming*, ed. Federico Biancuzzi y Shane Warden, O'Reilly Media, 1.ª edición, marzo de 2009, ISBN 978-0-596-51517-1 — ver [[tr-23]] en el plan editorial. Copia en préstamo digital controlado en [archive.org](https://archive.org/details/mastermindsofpro0000unse).
[^mmtoc]: Índice de *Masterminds of Programming* (O'Reilly, 2009): capítulo 7, «LUA — Luiz Henrique de Figueiredo and Roberto Ierusalimschy», p. 161; capítulo 8, «HASKELL», p. 177. Verificado contra el [material preliminar en PDF en archive.org](https://archive.org/details/MastermindsOfProgramming) (23 páginas: sólo front matter e índice, no el cuerpo del libro).
[^luapapers]: [Papers sobre Lua](https://www.lua.org/papers.html) — bibliografía oficial mantenida por los autores en lua.org.
[^hopl]: Roberto Ierusalimschy, Luiz Henrique de Figueiredo y Waldemar Celes, [«The evolution of Lua»](https://www.lua.org/doc/hopl.pdf), en *Proceedings of the third ACM SIGPLAN conference on History of Programming Languages* (HOPL III), ACM, 2007 — DOI [10.1145/1238844.1238846](https://doi.org/10.1145/1238844.1238846). Texto completo libre en el sitio de los autores.
[^hopl2]: Roberto Ierusalimschy, Luiz Henrique de Figueiredo y Waldemar Celes, «A look at the design of Lua», *Communications of the ACM*, vol. 61, n.º 11 (2018), pp. 114–123 — DOI [10.1145/3186277](https://doi.org/10.1145/3186277).
[^lua]: [Sitio oficial de Lua](https://www.lua.org/) — lua.org.
[^about]: [«About Lua»](https://www.lua.org/about.html) — sitio oficial; de acá salen las cifras de tamaño de Lua 5.5.0.
[^license]: [«Lua license»](https://www.lua.org/license.html) — sitio oficial; licencia MIT desde Lua 5.0.
[^pil]: Roberto Ierusalimschy, *Programming in Lua*, 4.ª edición, Lua.org, agosto de 2016, ISBN 8590379868. Ficha y ediciones anteriores en [lua.org/pil](https://www.lua.org/pil/); la 1.ª edición (2003, Lua 5.0) está [completa y gratis en línea](https://www.lua.org/pil/contents.html).
[^wowapi]: [World of Warcraft API](https://warcraft.wiki.gg/wiki/World_of_Warcraft_API) — Warcraft Wiki ([backup en Wayback, 2026-04-06](http://web.archive.org/web/20260406114746/https://warcraft.wiki.gg/wiki/World_of_Warcraft_API)).
[^luau]: [«Why Luau?»](https://luau.org/why) — documentación oficial de Luau, sobre el origen del fork y el uso de Lua 5.1 en Roblox desde alrededor de 2006.
[^robloxluau]: [«Luau»](https://create.roblox.com/docs/luau) — Roblox Creator Documentation ([backup en Wayback, 2026-06-23](http://web.archive.org/web/20260623061111/https://create.roblox.com/docs/luau)).
[^lrsdk]: [*Lightroom Classic SDK Guide 2020*](https://ioconsolerykerprodcdn.azureedge.net/static/installers/lr/sdk/2020/doc/Lightroom%20Classic%20SDK%20Guide%202020.pdf) (PDF), Adobe — «The Lua language» y «The Lightroom SDK scripting environment».
[^lradobe]: [«Unleash Lightroom Classic with Lua»](https://developer.adobe.com/lightroom-classic/) — portal de desarrollo de Adobe para Lightroom Classic ([backup en Wayback, 2026-06-21](http://web.archive.org/web/20260621064357/https://developer.adobe.com/lightroom-classic/)).
[^psuxp]: [Photoshop UXP API Reference](https://developer.adobe.com/photoshop/uxp/2022/ps_reference/) — Adobe. Documenta la automatización de Photoshop vía UXP/JavaScript y ExtendScript; Lua no aparece.
[^psuxpg]: [Photoshop UXP — guías para desarrolladores](https://developer.adobe.com/photoshop/uxp/2022/guides/) — Adobe; la DOM API como «the successor to ExtendScript».
[^luajit]: [LuaJIT](https://luajit.org/luajit.html) — sitio oficial de Mike Pall.
[^luajitgh]: [LuaJIT/LuaJIT](https://github.com/LuaJIT/LuaJIT) — «Mirror of the LuaJIT git repository», rama v2.1.
