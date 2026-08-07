### J-04 — Tipografiar Biblias históricas con LaTeX: Reina-Valera 1865 y Geneva 1564

- **Archivo seed (repos POC):** [github.com/CesarBallardini/rv1865](https://github.com/CesarBallardini/rv1865) (TeX, 1 star, 2015) + [github.com/CesarBallardini/geneve_1564](https://github.com/CesarBallardini/geneve_1564) (fork, TeX, 2015)
- **Slug propuesto:** `biblias-historicas-latex`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-biblias-historicas-latex/index.md`
- **Serie:** J — curiosidad nerd lateral
- **Cross-links:** lleva a [[I-02]] (digitalización en otro contexto)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** en 2015, por una mezcla de curiosidad lingüística y nerd-LaTeX, me senté a tipografiar la **Reina-Valera 1865** (la revisión española de la Biblia previa a las revisiones de 1881 y 1909, las que circulan hoy) usando LaTeX. El motivo declarado fue: "quería una Biblia de estudio sin las críticas que se hacían a las revisiones posteriores a 1881". El motivo *real* fue probablemente la combinación de proyecto chico-pero-largo + LaTeX + texto histórico + dominio público. El proyecto hermano `geneve_1564` (fork) hace lo mismo con la **Geneva Bible 1564** (la Biblia inglesa pre-King James). El post no es sobre teología — es sobre el oficio de tipografiar texto histórico con herramientas modernas, los problemas técnicos (encoding, font selection, división por capítulos, índices, footnotes históricas) y el placer del proyecto largo de fin de semana.

**Hook:** "tengo un repo en GitHub que se llama `rv1865`. Adentro hay LaTeX. Compilás y obtenés la Biblia Reina-Valera revisión 1865, tipografiada decentemente, en PDF, ePub y HTML. ¿Por qué? La razón teológica está en el README. La razón técnica es más interesante: tipografiar texto histórico en LaTeX es un proyecto perfecto para alguien al que le gusta el detalle, las herramientas viejas y los textos en dominio público. Acá cuento cómo y por qué."

**Outline:**
1. La cosa rara primero: tengo un repo de la Biblia en LaTeX. Sí, en serio.
2. La motivación teológica (corto, sin entrar en detalles): variantes textuales y revisiones.
3. La motivación técnica (largo, lo interesante): por qué LaTeX es el mejor amigo del texto histórico.
4. Los problemas concretos:
   - **Encoding**: textos del siglo XIX tienen caracteres raros (eñes con tildes, comillas francesas, signos pre-modernos).
   - **Font selection**: cuál font usar para que se sienta histórica sin perder legibilidad.
   - **División por capítulos y versículos**: cómo modelar la estructura sin que el LaTeX se vuelva ilegible.
   - **Índices y referencias cruzadas**: la parte donde LaTeX brilla.
   - **Output múltiple**: PDF para imprimir, ePub para leer en e-reader, HTML para web.
5. El proyecto hermano `geneve_1564`: la Geneva Bible inglesa de 1564, fork de un proyecto upstream.
6. Lo que aprendí del proceso: el oficio de tipografiar texto histórico es lento, tranquilo, y tiene una recompensa estética muy específica.
7. Cierre: si querés un proyecto de fin de semana que no se termine, agarrá un texto histórico en dominio público y tipográfialo en LaTeX.

**Bibliografía:**
- Repos: [rv1865](https://github.com/CesarBallardini/rv1865), [geneve_1564](https://github.com/CesarBallardini/geneve_1564).
- [Reina-Valera 1865 — texto en archive.org](https://archive.org/) — buscar la edición específica.
- [Geneva Bible 1560/1564 — Wikipedia](https://en.wikipedia.org/wiki/Geneva_Bible).
- [LaTeX project](https://www.latex-project.org/).
- [Donald E Knuth, *The TeXbook*, Addison-Wesley 1984](https://www-cs-faculty.stanford.edu/~knuth/abcde.html) — el libro fundacional, oblicuo pero relevante.
- [The TeX Catalogue](https://ctan.org/topic/biblical) — paquetes específicos para textos bíblicos.
- [Project Gutenberg — Bibles](https://www.gutenberg.org/) — fuentes en dominio público.

**Imágenes:**
- _Crear_: screenshot del PDF compilado de rv1865 mostrando una página típica (~10 min).
- _Crear_: side-by-side de un versículo en RV 1865 vs RV 1909 (~15 min).
- _Crear_: snippet del LaTeX en una caja (~10 min).

**Tags propuestos:** `['LaTeX', 'Biblia', 'Reina Valera', 'Geneva Bible', 'tipografia', 'texto historico', 'nerd lateral']`
**Estado actual:** **POC funcional** rv1865 + fork de geneve_1564. Prosa completa escrita al outline existente (~1.900 palabras, dentro del target medium). Lo que quedó escrito: el encuadre nerd-lateral, la motivación técnica genérica (por qué LaTeX y texto histórico se llevan bien), la estructura de los seis problemas concretos y el cierre-invitación. Lo que quedó como hueco: **todo lo específico de los repos** — año y circunstancia de arranque, de dónde salió el texto fuente de la RV1865, qué motor TeX y qué paquetes usó, qué font eligió, cómo modeló capítulos/versículos, si el pipeline ePub/HTML funciona o quedó a medias, de dónde salió el upstream de `geneve_1564` y por qué lo forkeó, y si el proyecto sigue vivo. Hay 16 huecos `🕳️` y 4 marcas de verificación (todas en las footnotes: fechas/licencia del repo, upstream del fork, 1560-vs-1564 de la Geneva, y la anécdota de las galeras de Knuth). **Antes de publicar hay que abrir los dos repos y leer el README + el Makefile/latexmkrc**: buena parte de los huecos se contestan solos ahí, pero no los inventé.

---

## Borrador de prosa

⚠️ **Curiosidad nerd lateral — esto no es ciencia de la computación.**

Tengo un repo en GitHub que se llama `rv1865`.[^rv1865] Adentro hay LaTeX. Lo clonás, lo compilás, y obtenés la Biblia Reina-Valera en su revisión de 1865, tipografiada decentemente, en PDF, en ePub y en HTML. No es una app, no es una librería, no resuelve el problema de nadie. Es un repositorio cuyo artefacto de salida es un libro de mil y pico de páginas que ya existe desde hace más de un siglo y medio.

¿Por qué? La razón teológica está en el README, y la voy a despachar en tres párrafos porque no es lo interesante. La razón técnica sí me parece que vale un post: tipografiar texto histórico en LaTeX es el proyecto perfecto para alguien al que le gustan el detalle, las herramientas viejas y los textos en dominio público. Es un proyecto que no se termina nunca, que no te apura nadie, y que cada tanto te devuelve una página que quedó *linda*. Voy a contarte cómo y por qué.

### La motivación declarada, y la de verdad

Cuando arranqué, el motivo que dije en voz alta fue: quería una Biblia de estudio sin las críticas que se le hacen a las revisiones posteriores a 1881. La Reina-Valera que circula hoy en las iglesias de habla hispana es descendiente de las revisiones de 1909 y 1960; la de 1865 es anterior a esa línea, y para cierta discusión sobre variantes textuales eso importa.

> 🕳️ **HUECO — necesita a César:** ¿en qué contexto apareció el interés por la RV1865? ¿Fue una discusión concreta (alguien de tu iglesia, una lectura, un foro), o llegaste al texto ya desde el lado nerd y la justificación teológica vino después?

> 🕳️ **HUECO — necesita a César:** ¿qué decís exactamente sobre las variantes textuales sin abrir una polémica? Una o dos frases tuyas, en tus términos, que dejen claro de qué lado estás parado sin convertir el post en un debate de crítica textual.

No voy a profundizar más que eso, y lo digo en serio: este post no es sobre teología. Si viniste buscando una defensa o un ataque a alguna familia de manuscritos, hay internet entero para eso y está lleno de gente más enojada que yo.

Porque el motivo *real*, sospecho, fue otro. Fue la combinación de cuatro cosas que a mí me resultan irresistibles juntas: un proyecto chico pero largo, LaTeX, un texto histórico, y dominio público. Sacale cualquiera de las cuatro y no lo hago. Las cuatro juntas y me senté un fin de semana. Y después otro.

> 🕳️ **HUECO — necesita a César:** ¿cuánto tiempo real le dedicaste? ¿Fueron un par de fines de semana, o el proyecto se estiró durante meses con ratos sueltos? Un dato concreto acá vale más que cualquier adjetivo.

### Por qué LaTeX es el mejor amigo del texto histórico

Acá va la parte que me interesa defender.

Un texto histórico tiene una propiedad rara: el contenido está congelado y la presentación está completamente abierta. Nadie va a discutirte una palabra —el texto es el que es, transcripto de una edición concreta— pero *cómo* lo mostrás es una decisión de diseño enteramente tuya. Eso es exactamente al revés de lo que pasa en casi todo lo demás que uno escribe, donde el contenido cambia todo el tiempo y el formato lo pone un template.

LaTeX[^latex] fue diseñado para ese mundo. Es un sistema donde vos declarás la estructura semántica del documento y el algoritmo de composición resuelve la apariencia, y donde ese algoritmo es determinista: la misma entrada produce la misma página, hoy y dentro de diez años. Knuth escribió TeX porque le devolvieron unas pruebas de galera de su propio libro y le parecieron feas.[^texbook] Ese origen —un tipo obsesivo peleándose con el espaciado de una línea— es exactamente la energía que un proyecto así necesita.

Hay tres cosas concretas que un procesador de texto no te da y LaTeX sí:

La primera es que el texto fuente es texto plano y va a git. Podés versionar una corrección de una coma en el Salmo 119. Podés hacer `git diff` entre dos transcripciones. Podés abrir un issue que diga «acá falta un versículo». El texto histórico se convierte en un artefacto de software, con todo lo bueno que eso trae.

La segunda es que la composición de párrafo de TeX es realmente buena, y en un libro de dos columnas con miles de párrafos cortos eso se nota. El algoritmo optimiza el salto de línea a nivel párrafo entero, no línea por línea, y el resultado es una mancha de texto pareja que uno percibe sin saber por qué.

La tercera es que la salida es reproducible y múltiple. Un fuente, varios formatos. De eso hablo más abajo.

### Los problemas concretos

Ahora, nada de esto es gratis. Van los seis lugares donde el proyecto se pone entretenido.

#### Encoding

Un texto del siglo XIX no es UTF-8 con acentos españoles modernos y listo. Aparecen convenciones ortográficas que ya no usamos, abreviaturas, comillas que no son las de hoy, y decisiones de la edición impresa original que hay que resolver una por una: ¿lo transcribo tal cual está, o lo normalizo a la ortografía actual? No hay respuesta correcta; hay una respuesta que elegís y después tenés que sostener en las mil páginas siguientes.

> 🕳️ **HUECO — necesita a César:** ¿de dónde salió el texto fuente de la RV1865? ¿Lo transcribiste vos, lo bajaste de algún lado, lo pasaste por OCR? Esto define todo el resto de la sección y no lo puedo inventar.

> 🕳️ **HUECO — necesita a César:** ¿qué decidiste con la ortografía histórica — normalizar o conservar? ¿Y te acordás de algún caso concreto que te haya hecho dudar?

> 🕳️ **HUECO — necesita a César:** ¿qué encoding tenía la fuente cuando la conseguiste, y hubo que hacer algún trabajo de conversión que valga la pena contar?

#### Elección de tipografía

Acá la tensión es entre que se sienta histórica y que se pueda leer. Una tipografía demasiado de época convierte el libro en una pieza de museo que nadie usa; una demasiado neutra lo convierte en un PDF cualquiera. Y hay una restricción práctica adicional: el font tiene que tener la cobertura de caracteres que el texto necesita, y tiene que estar disponible en el formato que tu motor TeX consume.

> 🕳️ **HUECO — necesita a César:** ¿qué font terminaste usando en rv1865, y probaste otros antes? El «probé X, no me gustó por Y, quedé en Z» es la parte buena de esta sección.

> 🕳️ **HUECO — necesita a César:** ¿usaste pdfTeX, XeLaTeX o LuaLaTeX? La elección de motor y la de font son la misma decisión, y determina si el post habla de `fontspec` o de paquetes de font clásicos.

#### Estructura: libros, capítulos, versículos

Este es el problema de modelado, y es el más lindo. Una Biblia tiene una jerarquía propia —libro, capítulo, versículo— que no concuerda con la jerarquía de LaTeX —parte, capítulo, sección. Y el versículo es una unidad rara: no es un párrafo, no es un salto de línea, es una marca numerada que puede caer en cualquier lugar de un párrafo y que tiene que poder referenciarse desde afuera.

O sea que tenés que definir tus propios comandos. Y ahí aparece la disyuntiva de siempre: si los hacés demasiado inteligentes, el fuente queda limpio pero el preámbulo se vuelve un lenguaje de programación que sólo entendés vos; si los hacés demasiado tontos, el fuente se llena de ruido de marcado y perdés la capacidad de cambiar la presentación después. Vale la pena mencionar que en CTAN hay una categoría entera de paquetes para textos bíblicos, así que el problema tiene soluciones previas.[^ctan]

> 🕳️ **HUECO — necesita a César:** ¿cómo modelaste el versículo en rv1865? ¿Macro propia, paquete de CTAN, o el texto viene con marcado de otro formato y lo convertís? Un snippet de tres líneas del fuente real sería el corazón del post.

> 🕳️ **HUECO — necesita a César:** ¿evaluaste alguno de los paquetes bíblicos de CTAN y lo descartaste? Si sí, ¿por qué?

#### Índices y referencias cruzadas

Es donde LaTeX brilla y donde el trabajo se paga solo. Una vez que cada versículo es una etiqueta referenciable, las tablas de contenido, los índices y las referencias cruzadas dejan de ser trabajo manual y pasan a ser una consecuencia de la compilación. Es la diferencia entre mantener un libro y generarlo.

> 🕳️ **HUECO — necesita a César:** ¿rv1865 genera índices/tablas de referencia, o eso quedó pendiente? Si quedó pendiente, decilo — un POC honesto es mejor que un POC embellecido.

#### Salida múltiple: PDF, ePub, HTML

El objetivo declarado del repo son tres salidas: PDF para imprimir, ePub para el e-reader, HTML para la web. Y el chiste es que las tres tienen filosofías incompatibles. El PDF tiene páginas y el salto de página es una decisión estética; el ePub no tiene páginas en absoluto y el lector decide todo; el HTML tampoco, y encima tiene que sobrevivir a que alguien lo lea en un teléfono. Sacar los tres del mismo fuente LaTeX implica que las macros no pueden asumir nada sobre la página.

> 🕳️ **HUECO — necesita a César:** ¿cómo generás ePub y HTML desde el fuente TeX? ¿`tex4ht`, pandoc, un script propio? ¿Y las tres salidas funcionan hoy, o el PDF anda bien y las otras dos están a medio hacer?

#### El proyecto hermano: `geneve_1564`

Después vino `geneve_1564`,[^geneve] que es un fork y hace lo mismo con la Geneva Bible,[^geneva] la Biblia inglesa anterior a la King James. Que sea un fork y no un proyecto de cero es el dato importante: alguien más ya había hecho el trabajo de tipografiar el texto y yo llegué a una base andando.

> 🕳️ **HUECO — necesita a César:** ¿de qué repo upstream forkeaste `geneve_1564`, y qué le cambiaste vos? Si el fork quedó igual al upstream, también es una respuesta válida y hay que decirla.

> 🕳️ **HUECO — necesita a César:** ¿el fork fue antes o después de rv1865, y te sirvió como fuente de ideas para el otro? Me interesa la dirección del préstamo.

### Lo que aprendí

Tipografiar texto histórico es lento y tranquilo. No hay usuarios, no hay tickets, no hay deadline, no hay nadie esperando el release. Compilás, mirás la página, movés un parámetro, volvés a compilar. Es probablemente la actividad más parecida a la carpintería que se puede hacer con una computadora: el material te opone resistencia, la herramienta es vieja y buena, y el progreso se mide en superficie terminada.

Y tiene una recompensa estética muy específica, que es difícil de explicarle a alguien que no la sintió: hay un momento en que abrís el PDF y la página *está bien*. El interlineado, la mancha, los números de versículo que no molestan. No sirve para nada. Es hermoso igual.

> 🕳️ **HUECO — necesita a César:** ¿el proyecto está vivo, dormido o cerrado? ¿Volviste a tocarlo alguna vez desde 2015? ¿Hay algo que te gustaría arreglar y nunca arreglaste?

> 🕳️ **HUECO — necesita a César:** ¿alguien lo usó alguna vez? ¿Recibiste un issue, un mail, una estrella de alguien que no conocés? Cualquier señal de vida externa es un buen cierre.

### Si querés hacerlo vos

Agarrá un texto histórico en dominio público —Project Gutenberg está lleno[^gutenberg]— y tipografialo en LaTeX. No importa cuál. No lo hagas para terminarlo; hacelo para tener adónde ir cuando no querés hacer nada útil. Es un proyecto que te espera, no que te apura.

Y si te interesa el otro lado de la moneda —qué pasa cuando la digitalización de un texto tiene que sobrevivir a una institución y no a un fin de semana— eso lo cuento en [[I-02]].

[^rv1865]: [`CesarBallardini/rv1865`](https://github.com/CesarBallardini/rv1865) — fuentes LaTeX de la Reina-Valera 1865. [VERIFICAR: confirmar en el repo el año de los commits, la licencia y si el README declara efectivamente las tres salidas PDF/ePub/HTML antes de afirmarlo en el post.]
[^geneve]: [`CesarBallardini/geneve_1564`](https://github.com/CesarBallardini/geneve_1564) — fork. [VERIFICAR: identificar el repo upstream del que sale el fork y acreditarlo con nombre y URL en esta misma nota; el draft no lo registra.]
[^geneva]: [Geneva Bible — Wikipedia](https://en.wikipedia.org/wiki/Geneva_Bible). [VERIFICAR: la fecha 1564 vs 1560 — la edición canónica que suele citarse es la de 1560 y el repo se llama `geneve_1564`; chequear qué edición es realmente la del proyecto antes de escribir «la Biblia inglesa anterior a la King James» con una fecha.]
[^latex]: [The LaTeX Project](https://www.latex-project.org/).
[^texbook]: Donald E. Knuth, *The TeXbook*, Addison-Wesley, 1984. Ver [la página de libros de Knuth](https://www-cs-faculty.stanford.edu/~knuth/abcde.html). [VERIFICAR: la anécdota de las galeras feas de *The Art of Computer Programming* como origen de TeX es archiconocida pero no está respaldada por ninguna fuente del draft; buscar dónde la cuenta Knuth él mismo, o sacarla.]
[^ctan]: [CTAN — paquetes del tópico *biblical*](https://ctan.org/topic/biblical).
[^gutenberg]: [Project Gutenberg](https://www.gutenberg.org/).

