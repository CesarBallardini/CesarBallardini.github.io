### A2-04 — Sistemas expertos en BASIC (lo que salió en Byte)

- **Archivo seed:** `dev/draft-expert-system-en basic.md` (atención: filename con espacio antes de "basic")
- **Slug propuesto:** `sistemas-expertos-en-basic-byte-1981`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-sistemas-expertos-en-basic-byte-1981/index.md`
- **Serie:** A2 (Lisp lineage — el código original de Byte fue un port de un sistema en Lisp de Winston)
- **Cross-links:** depende de [[tr-05]] (Winston *LISP*), [[tr-10]] (Byte archive); lleva a [[A2-02]] (Lambda papers), [[J-03]] (MindForth como descendiente moral)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-1800 palabras)

**Concepto:** en septiembre de 1981 *Byte Magazine* publicó "Knowledge-Based Expert Systems Come of Age" con código BASIC funcional para construir tu propio sistema experto. El código era un port directo del capítulo 18 del libro *LISP* de Patrick Winston. El post es sobre por qué eso era totalmente normal en los 80 y por qué hoy nos parece marciano.

**Hook:** "en 1981 podías comprar una revista en el quiosco que te enseñaba a hacer un sistema experto. En BASIC. Para tu IBM PC. Y funcionaba. Hoy te explican cómo hacer un wrapper de OpenAI y eso se llama AI."

**Outline:**
1. Contexto 1981: AI hype #1, expert systems en boca de todos, MYCIN, DENDRAL.
2. Byte Magazine, septiembre 1981 — el issue dedicado a expert systems. Quiénes lo escribieron (Duda, Gaschnig).
3. El código BASIC: ~290 líneas numeradas para un motor de inferencia (backward chaining como MYCIN, IF-THEN rules; subrutina recursiva VERIFY emulada con stacks explícitos).
4. El código original en Lisp (Winston cap. 18): cómo se ve el mismo motor en una página de Lisp.
5. Por qué BASIC era un objetivo razonable: era *el* lenguaje de las microcomputadoras.
6. Cierre: la lección que olvidamos — un sistema experto bien hecho de 50 líneas es más explicable que un LLM de 70B parámetros, y para muchos dominios, suficiente.

**Bibliografía:** (reforzada y verificada por fetch el 2026-07-16)
- [[tr-05]] — Winston & Horn, *LISP* (Addison-Wesley, 1981), capítulo 18 «Expert Problem Solving Using If-Then Rules» — título verificado en el índice del libro. Contiene el programa DIAGNOSE que el artículo de Byte reimplementó en BASIC. [Ejemplar en archive.org](https://archive.org/details/lisp-1981-addison-wesley) — estable.
- [[tr-10]] — Byte Magazine archive (archive.org + vintageapple.org).
- [*Byte Magazine*, septiembre de 1981 (vol. 6 nº 9), número especial «Artificial Intelligence»](https://archive.org/details/byte-magazine-1981-09) — archive.org, **estable**. Contiene «Knowledge-Based Expert Systems Come of Age», de Richard O. Duda y John G. Gaschnig (p. 238), con la Listing 1 (programa de identificación de animales en BASIC, ~290 líneas numeradas, impreso en las pp. 263, 268 y 274) y la Listing 2 (corrida de ejemplo). El texto declara que la Listing 1 es "essentially a recoding of the DIAGNOSE program used by Winston and Horn in their book LISP" (referencia 35 del artículo = Winston & Horn, *LISP*, cap. 18).
- [Texto completo OCR del número (djvu.txt)](https://archive.org/stream/byte-magazine-1981-09/BYTE_Vol_06-09_1981-09_Artifical_Intelligence_djvu.txt) — para citar frases exactas del artículo; estable.
- [*Byte Magazine*, abril de 1985 (vol. 10 nº 4), número «Artificial Intelligence»](https://archive.org/details/byte-magazine-1985-04) — archive.org, **estable**. «Inside an Expert System», de Beverly A. Thompson y William A. Thompson (p. 315), traza un sistema de reglas "from index cards to a Pascal program". (El PDF en [vintageapple.org](https://vintageapple.org/byte/pdf/198504_Byte_Magazine_Vol_10-04_Artificial_Intelligence.pdf) es la misma edición — **frágil**, mirror de un solo host.)
- [E. A. Feigenbaum, «Expert Systems in the 1980s», Stanford University (Stanford Heuristic Programming Project, © 1980)](https://stacks.stanford.edu/file/druid:vf069sz9374/vf069sz9374.pdf) — repositorio digital de Stanford (stacks.stanford.edu); **fuente primaria, estable**. Panorama de los sistemas expertos escrito al comienzo de la década; discute DENDRAL y MYCIN. (Reemplaza a la URL `web.stanford.edu/dept/cs/historical/...` de la versión anterior, que devolvía 404.)
- [MYCIN — Wikipedia](https://en.wikipedia.org/wiki/Mycin) — para el dato de ~600 reglas (encadenamiento hacia atrás; Edward H. Shortliffe, tesis doctoral en Stanford, primeros años 70).
- [DENDRAL — Wikipedia](https://en.wikipedia.org/wiki/Dendral) — Stanford desde 1964; Feigenbaum, Lederberg, Buchanan y Djerassi; espectrometría de masas → estructura molecular; suele citarse como el primer sistema experto.
- [«Professor Patrick Winston, former director of MIT's Artificial Intelligence Laboratory, dies at 76»](https://news.mit.edu/2019/patrick-winston-professor-obituary-0719) — MIT News, **estable** (URL corregida; la anterior, `.../professor-patrick-winston-obituary-0719`, daba 404). Murió el 19 de julio de 2019 a los 76 años; dirigió el AI Lab del MIT de 1972 a 1997.

**Imágenes:**
- _Archive.org_: scan de las páginas relevantes del Byte 1981-09 (uso académico/educativo, atribución a Byte).
- _Crear_: comparación side-by-side del mismo motor en BASIC vs Lisp (~30 min).

**Tags propuestos:** `['expert system', 'BASIC', 'LISP', 'Patrick Winston', 'Byte', 'AI history']`

**Estado actual:** prosa completa escrita contra el outline (sección "Borrador de prosa" al pie, ~1650 palabras, dentro del target medium). Lo que quedó escrito: el encuadre histórico de 1981, la descripción del artículo de Byte, la comparación conceptual BASIC/Lisp, el argumento sobre por qué BASIC era el target obvio, y el cierre sobre explicabilidad. Lo que quedó como hueco: **todo el recuerdo personal de César** — si leía Byte en Argentina en esa época y cómo llegaba, si tipeó alguna vez un listado largo de revista, si tuvo el Winston & Horn en papel, si llegó a construir un sistema experto. Además quedaron marcados con `[VERIFICAR:]` todos los datos duros que la bibliografía existente no respalda de forma directa: el conteo de líneas del listado, el sentido de encadenamiento del motor, la afiliación institucional de Duda y Gaschnig, los detalles de MYCIN y DENDRAL, y sobre todo la afirmación central del Concepto (que el código BASIC sea un port directo del capítulo 18 de Winston) — hay que abrir el scan y confrontarlo con el libro antes de publicar, porque es la bisagra del post.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch, incluido el texto OCR del propio número de *Byte*) y se resolvieron 10 de 11 marcadores [VERIFICAR:]. El único que queda es una decisión editorial (si nombrar un tamaño concreto de LLM o dejarlo genérico), no un dato verificable. **La bisagra del post quedó confirmada**: el artículo de Duda y Gaschnig declara en la propia página la Listing 1 como "essentially a recoding of the DIAGNOSE program used by Winston and Horn" (cap. 18, referencia 35 del artículo), con sus quince reglas de identificación de animales — así que el Concepto se sostiene tal cual está escrito. Datos duros verificados: número especial de IA (vol. 6 nº 9); afiliaciones (Duda en Fairchild, Gaschnig en SRI International, ambos ex-PROSPECTOR); motor con encadenamiento hacia atrás (como MYCIN); listado de ~290 líneas (VERIFY recursivo en 1210–1830, impreso en pp. 263/268/274); MYCIN (~600 reglas, Shortliffe, Stanford); DENDRAL (Stanford desde 1964; Feigenbaum, Lederberg, Buchanan, Djerassi); muerte de Winston (19-jul-2019, 76 años, director del AI Lab 1972–1997). Se corrigieron dos URLs muertas (obituario del MIT y PDF de Feigenbaum).

**Bloqueantes antes de escribir el post final:**
1. ~~Abrir el scan del Byte 1981-09 y leer el artículo y los listados de verdad.~~ **HECHO (2026-07-16)** vía el OCR del número; casi todos los `[VERIFICAR:]` resueltos.
2. ~~Confrontar el listado BASIC con el capítulo 18 del Winston & Horn para confirmar la tesis del port.~~ **HECHO (2026-07-16)**: el artículo declara explícitamente que la Listing 1 es "essentially a recoding of the DIAGNOSE program" del cap. 18 (referencia 35). La tesis del port se confirma; el Concepto y el título de la sección 4 quedan tal cual.
3. Responder los huecos 🕳️ (pendiente — solo César).
4. Producir la imagen side-by-side BASIC/Lisp — ya se puede hacer (bloqueantes 1 y 2 cumplidos).

---

## Borrador de prosa

En 1981 podías comprar una revista en el quiosco que te enseñaba a hacer un sistema experto. En BASIC. Para tu microcomputadora. Y funcionaba.

Hoy te explican cómo hacer un wrapper de la API de OpenAI y eso se llama AI.

No lo digo como chiste de viejo — bueno, un poco sí —, pero el contraste me viene dando vueltas hace rato. El número de septiembre de 1981 de *Byte* traía un artículo llamado «Knowledge-Based Expert Systems Come of Age», firmado por Richard Duda y John Gaschnig[^byte8109], y unas páginas más adelante los listados: el código, entero, para que lo tipees vos.[^listados] No un diagrama de arquitectura, no un «ejercicio para el lector», no un link a un repo que hoy estaría 404. El programa completo, impreso, en una revista que se vendía en el quiosco.

> 🕳️ **HUECO — necesita a César:** ¿leías *Byte* en esa época? Si sí: ¿cómo llegaba a Argentina un número de *Byte* en 1981 — suscripción, alguien que viajaba, la biblioteca de la facultad, una fotocopia que circulaba? Con una o dos frases alcanza; es el gancho del segundo bloque.

## Qué se respiraba en 1981

Estábamos en el primer gran hype de la inteligencia artificial. No el de ahora, no el de los 90: el de los sistemas expertos. La promesa era concreta y sonaba razonable: si un experto humano sabe diagnosticar algo, y ese saber se puede escribir como un montón de reglas «si esto entonces aquello», entonces se puede meter el saber en una computadora y la computadora diagnostica.

Los ejemplares canónicos ya estaban ahí. MYCIN, de Stanford, diagnosticaba infecciones bacterianas y recomendaba antibióticos a partir de un cuerpo de unas 600 reglas IF-THEN[^mycin] con encadenamiento hacia atrás; lo construyó Edward H. Shortliffe como su tesis doctoral en Stanford a comienzos de los años 70. DENDRAL, también de Stanford y anterior —arrancó en 1964—, infería estructuras moleculares a partir de datos de espectrometría de masas; fue obra de Edward Feigenbaum, Joshua Lederberg, Bruce Buchanan y Carl Djerassi, y suele citarse como el primer sistema experto de la historia. El propio Feigenbaum, que estuvo metido hasta el cuello en esa tradición, dejó un panorama de los sistemas expertos escrito al comienzo de la década que sirve justamente para medir cuánto se prometía y cuánto se cumpliría.[^feigenbaum]

Lo interesante para este post no es la historia grande. Es que ese conocimiento no se quedó en los papers. Bajó al quiosco en menos de lo que hoy tarda un modelo en salir de preview.

## El artículo

*Byte* de septiembre de 1981 fue un número especial entero dedicado a la inteligencia artificial —el título de tapa es directamente «Artificial Intelligence»— y ahí Duda y Gaschnig explican qué es un sistema experto, para qué sirve, y cómo hacerte uno.[^byte8109] Al momento del artículo, Richard O. Duda trabajaba en Fairchild Camera and Instrument Corp (Palo Alto) y John G. Gaschnig en SRI International (Menlo Park); los dos venían de construir PROSPECTOR, el sistema experto para exploración mineral del AI Center de SRI, y de hecho el artículo lo usa como caso testigo de lo que un sistema experto podía llegar a hacer.

El texto hace lo que hoy haría un buen post técnico: define el problema, muestra la arquitectura mínima —base de reglas, base de hechos, motor de inferencia— y después baja a código. La diferencia es que en 1981 «baja a código» significaba literalmente páginas de listado con números de línea a la izquierda, y del otro lado un lector con la revista abierta al lado del teclado, tipeando.

Y funcionaba. Esa es la parte que me sigue pareciendo notable. No era una demo de juguete que ilustraba el concepto y después «para hacer algo serio contactá a nuestro departamento de ventas». Era el motor. Chico, limitado, pero el motor.

Y no era un chiste de cuarenta líneas: el programa —la Listing 1 del artículo, impresa a lo largo de las páginas 263, 268 y 274— corre a unas 290 líneas numeradas de BASIC, con la subrutina recursiva VERIFY entre las líneas 1210 y 1830. El motor hace encadenamiento hacia atrás (backward chaining), el mismo esquema que usa MYCIN: parte de una hipótesis y va pidiendo las observaciones que la confirmarían o la descartarían. Como BASIC no tiene recursión, el autor tuvo que salvar a mano las variables locales en pilas explícitas cada vez que VERIFY se llamaba a sí misma.

> 🕳️ **HUECO — necesita a César:** ¿alguna vez tipeaste un listado largo de revista? ¿Cuál, en qué máquina, y cuánto tardaste en encontrar el error de tipeo? El post necesita una frase tuya acá, porque es la experiencia física que el lector de 2026 no tiene.

## El mismo motor, en Lisp

Acá está la vuelta de tuerca que hace que este post pertenezca a la serie del linaje Lisp y no a una de nostalgia de revistas.

El mismo año, Patrick Winston y Berthold Horn publicaron *LISP*, y su capítulo 18 se llama «Expert Problem Solving Using IF-THEN Rules».[^winston] Es exactamente la misma idea, en el lenguaje en el que esa idea nació: un motor de reglas escrito en Lisp, en el libro con el que un par de generaciones aprendieron Lisp.

Y acá está la parte que no hace falta que yo interprete, porque el artículo la dice con todas las letras. La Listing 1 es, en sus propias palabras, "essentially a recoding of the DIAGNOSE program used by Winston and Horn in their book LISP" —cita a Winston & Horn como su referencia 35, capítulo 18— e incluye "their set of fifteen rules for identifying animals". No es una inspiración vaga ni un parecido de familia: es el mismo programa DIAGNOSE, las mismas quince reglas, la misma taxonomía de siete animales (albatros, pingüino, avestruz, cebra, jirafa, tigre, guepardo), transcrito de Lisp a BASIC. La tesis del port no es una lectura mía: la firma el propio Duda.

La comparación side-by-side es el corazón de lo que quiero mostrar. En Lisp, el motor cabe cómodo en una página: las reglas son listas, los hechos son listas, y aplicar una regla es recorrer estructuras y ligar variables. El lenguaje ya te da representación simbólica gratis; el motor es casi transcripción de la idea. En BASIC no tenés nada de eso: no hay listas, no hay símbolos, no hay recursión cómoda. Tenés arrays, `GOTO` y strings. Y aun así el motor entra. Más largo, más feo, con la representación de las reglas hecha a mano sobre arrays de strings — pero entra.

Eso dice algo lindo sobre el motor de inferencia: la idea es tan chica que sobrevive a la traducción a un lenguaje que la odia.

> 🕳️ **HUECO — necesita a César:** ¿tuviste el Winston & Horn en papel? ¿Cuándo y cómo llegó a tus manos? ¿Y llegaste a construir alguna vez un sistema de reglas, en la facultad o en el trabajo? Si la respuesta es no, también sirve: el post puede decirlo.

## Por qué BASIC no era una humillación

Al lector de hoy, «sistema experto en BASIC» le suena a chiste. En 1981 no lo era, y no porque la gente no supiera lo que hacía.

BASIC era *el* lenguaje de las microcomputadoras. Venía en ROM. Prendías la máquina y estabas adentro del intérprete: no había instalar, no había toolchain, no había entorno que configurar. Era el denominador común absoluto — si publicabas código en BASIC, todo el mundo podía correrlo.

Publicar el motor en Lisp habría sido publicarlo para las pocas personas con acceso a una máquina con Lisp, que en 1981 significaba una universidad o un laboratorio. Publicarlo en BASIC era publicarlo para cualquiera con una micro sobre el escritorio. Duda y Gaschnig no estaban rebajando la idea: la estaban distribuyendo.

Y el patrón se repitió. En abril de 1985 *Byte* volvió sobre lo mismo con una versión en Pascal y pseudocódigo[^byte8504] — Pascal, porque para entonces ya era razonable suponer que el lector tenía un compilador. El vehículo cambia; la idea es la misma.

## Lo que olvidamos

Un motor de reglas de un par de páginas de listado tiene una propiedad que ningún modelo de lenguaje tiene hoy: podés preguntarle *por qué*. Y la respuesta no es una racionalización generada a posteriori, es la traza literal de las reglas que se dispararon. Regla 12, después regla 5, después regla 31, conclusión. Si la conclusión está mal, sabés cuál regla está mal, la arreglás, y sabés que la arreglaste.

Eso no es poco. Es, de hecho, lo que todo el mundo dice querer cuando dice «AI explicable».

No estoy proponiendo volver a los sistemas expertos. Fracasaron, y fracasaron por razones reales: escribir las reglas era carísimo, había que sacárselas de la cabeza a un experto humano a fuerza de entrevistas, y no escalaban a dominios donde el saber no se deja escribir como reglas. El invierno de la AI no fue mala suerte.

Pero hay una franja enorme de problemas —validaciones de negocio, triage, elegibilidad, ruteo, diagnóstico acotado— donde el dominio *sí* se deja escribir como reglas, donde alguien ya las tiene escritas en un manual, y donde hoy se tira un LLM de setenta mil millones de parámetros [VERIFICAR: si conviene un número concreto acá, o dejarlo genérico como «un modelo de lenguaje grande» para que el post no envejezca en seis meses] porque es lo que está de moda. Un motor de cincuenta líneas resolvería el problema, sería auditable, correría en un teléfono y costaría cero por consulta.

La revista de 1981 sabía algo que nosotros dejamos de saber: que a veces la técnica adecuada es la chiquita, y que si la técnica chiquita entra en dos páginas de listado, lo mejor que podés hacer es imprimirla y que la tipee todo el mundo.

Patrick Winston murió el 19 de julio de 2019, a los 76 años; había dirigido el Laboratorio de Inteligencia Artificial del MIT de 1972 a 1997.[^winston_obit] El capítulo 18 sigue ahí, y sigue siendo más corto que la documentación de cualquier framework de agentes de hoy.

[^byte8109]: [«Knowledge-Based Expert Systems Come of Age», *Byte Magazine*, septiembre de 1981 (vol. 6 nº 9), p. 238 — Richard O. Duda y John G. Gaschnig](https://archive.org/details/byte-magazine-1981-09) — número completo en archive.org (estable). El [texto OCR](https://archive.org/stream/byte-magazine-1981-09/BYTE_Vol_06-09_1981-09_Artifical_Intelligence_djvu.txt) permite citar las frases exactas.
[^listados]: Listing 1 y Listing 2 del artículo (programa de identificación de animales en BASIC y su corrida de ejemplo), *Byte* 1981-09, impresas en las pp. 263, 268 y 274. La Listing 1 corre a ~290 líneas numeradas, con la subrutina recursiva VERIFY en las líneas 1210–1830.
[^winston]: Patrick Henry Winston y Berthold Klaus Paul Horn, *LISP*, Addison-Wesley, 1981 — capítulo 18, «Expert Problem Solving Using If-Then Rules» (título verificado en el índice). El artículo de *Byte* lo cita como su referencia 35 y reimplementa su programa DIAGNOSE. [Ejemplar en archive.org](https://archive.org/details/lisp-1981-addison-wesley) — estable. Ver [[tr-05]].
[^byte8504]: «Inside an Expert System», de Beverly A. Thompson y William A. Thompson, en [*Byte Magazine*, abril de 1985 (vol. 10 nº 4), número «Artificial Intelligence», p. 315](https://archive.org/details/byte-magazine-1985-04) — archive.org, estable. Trazan un sistema de reglas "from index cards to a Pascal program". (Mismo número en [vintageapple.org](https://vintageapple.org/byte/pdf/198504_Byte_Magazine_Vol_10-04_Artificial_Intelligence.pdf) — frágil, un solo host.)
[^feigenbaum]: [E. A. Feigenbaum, «Expert Systems in the 1980s», Stanford University (Stanford Heuristic Programming Project, © 1980)](https://stacks.stanford.edu/file/druid:vf069sz9374/vf069sz9374.pdf) — repositorio digital de Stanford, estable. Panorama de los sistemas expertos escrito al comienzo de la década; discute DENDRAL y MYCIN.
[^mycin]: [E. A. Feigenbaum, «Expert Systems in the 1980s» (Stanford)](https://stacks.stanford.edu/file/druid:vf069sz9374/vf069sz9374.pdf) presenta a MYCIN como sistema experto canónico del grupo de Stanford; el dato de ~600 reglas y la autoría de Edward H. Shortliffe surgen de [MYCIN — Wikipedia](https://en.wikipedia.org/wiki/Mycin).
[^winston_obit]: [«Professor Patrick Winston, former director of MIT's Artificial Intelligence Laboratory, dies at 76»](https://news.mit.edu/2019/patrick-winston-professor-obituary-0719) — MIT News (título exacto verificado; URL corregida respecto de la versión anterior, que daba 404).

