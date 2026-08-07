### J-06 — Automagica: generar un libro listo para imprenta con LaTeX (y tres Biblias antiguas)

- **Archivo seed:** `github.com/CesarBallardini/automagica` (fork, TeX, Oct 2017) — hermano de [[J-04]] (Reina-Valera 1865 y Geneva 1564)
- **Slug propuesto:** `automagica-libros-latex-imprenta`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-automagica-libros-latex-imprenta/index.md`
- **Serie:** J
- **Cross-links:** depende de [[J-04]] (Biblias históricas — caso de uso); lleva a [[I-02]] (digitalización)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César) — fork funcional, caso de uso real con tres proyectos de Biblias
- **Length target:** short-medium (1000-1500 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** *automagica* es un fork de un proyecto en TeX que genera automáticamente libros listos para imprenta (PDF interior + tapa + contratapa con dimensiones exactas para servicios tipo Lulu / Amazon KDP / Bibliomanía) a partir de un Markdown/LaTeX fuente. El post describe el sistema y lo cruza con [[J-04]] (mi proyecto de tipografiar la Reina-Valera 1865 y la Biblia de Ginebra 1564), porque es el mismo stack: TeX + scripts + pipelines para convertir texto limpio en objeto físico imprimible.

**Hook:** "tenés un texto. Querés un libro físico. No querés pasar por un diseñador. Querés que un script Make lo genere listo para Lulu o KDP. Automagica hace eso con LaTeX + scripts. El post cuenta el sistema y cómo lo usé para tipografiar tres Biblias históricas."

**Outline:**
1. El problema: self-publishing técnico sin diseñador profesional.
2. Automagica: LaTeX + scripts + Makefile + templates de cover.
3. El workflow: Markdown → LaTeX → PDF interior + PDF tapa.
4. El cruce con [[J-04]]: las tres Biblias como caso de uso (Reina-Valera 1865, Geneva 1564, y la tercera que esté en desarrollo).
5. Las trampas: fonts libres que tengan glifos antiguos, hyphenation para español antiguo, CMYK vs RGB en las tapas.
6. Cierre: si querés auto-publicar un libro técnico sin diseñador, este es el camino.

**Bibliografía:**
- [automagica — upstream de Juan José Conti (`jjconti`)](https://github.com/jjconti/automagica) — proyecto en TeX, licencia GPL-3.0; descripción oficial: «Permite crear en forma fácil libros listos para imprenta o para distribuir digitalmente». Confirmado por fetch el 2026-07-16. *estable* (GitHub; conviene capturar copia en Wayback antes de publicar, es la fuente principal).
- [automagica — fork de César Ballardini](https://github.com/CesarBallardini/automagica) — fork de `jjconti/automagica`, GPL-3.0, última actividad 2017-10-12. Contenido del fork verificado por API el 2026-07-16 (`automagica.py`, `template.tex`, `template.py`, `utils.py`, `epub.py`, `pdf/booklet.py`, `config.example.py`; **sin** Makefile, **sin** `.cls`, **sin** script de tapa). *estable/frágil* (repo propio; backup Wayback recomendado).
- [pandoc — «a universal document converter», de John MacFarlane](https://pandoc.org/) — GPL; convierte Markdown a LaTeX y a PDF vía `pdflatex`/`xelatex`/`lualatex`. Es el primer eslabón del pipeline de automagica. *estable*.
- [Donald E. Knuth — página de libros (Stanford)](https://www-cs-faculty.stanford.edu/~knuth/abcde.html) — *The TeXbook*, Addison-Wesley, 1984, ISBN 0-201-13448-9 (Vol. A de *Computers & Typesetting*). *estable* (página académica de Knuth).
- [TeX — historia (Wikipedia)](https://en.wikipedia.org/wiki/TeX) — Knuth arrancó TeX en 1977 tras recibir (30-mar-1977) las galeras defectuosas de la 2.ª edición del vol. 2 de *The Art of Computer Programming*; memo fundacional del 13-may-1977; TeX78 (primera versión, en SAIL sobre PDP-10) en 1978; reescritura TeX82 en 1982. *estable*.
- [Leslie Lamport — lista de publicaciones (entrada 71: *LaTeX: A Document Preparation System*)](https://lamport.azurewebsites.net/pubs/pubs.html#latex) — *frágil* (dominio azurewebsites; backup Wayback recomendado).
- [*LaTeX: A Document Preparation System*, 2.ª ed. — ficha del editor (Pearson)](https://www.pearson.com/en-us/subject-catalog/p/latex-a-document-preparation-system/P200000000419/9780201529838) — Addison-Wesley, 1994, ISBN-13 978-0-201-52983-8 (ISBN-10 0-201-52983-1). *frágil* (página de catálogo comercial).
- [LaTeX Project — «Books with LaTeX»](https://www.latex-project.org/help/books/) — la clase `book` estándar. *estable*.
- [Paquete `memoir` en CTAN](https://www.ctan.org/pkg/memoir) — clase para libros con control fino de caja, stock de papel y preliminares (recomendación propia; **no** es la clase que usa el fork de automagica). *estable*.
- [Make (software) — historia](https://en.wikipedia.org/wiki/Make_(software)) — creado por Stuart Feldman en Bell Labs, versión temprana en abril de 1976; ACM Software System Award 2003. *estable*.
- [Lulu](https://www.lulu.com/) y [Amazon KDP](https://kdp.amazon.com/) — especificaciones de impresión (perfil de color, sangrado, cálculo de lomo). Enlazar la página concreta de specs y **fechar la consulta al momento de publicar**: estos números cambian. *frágil* por diseño.

**Imágenes:**
- _Crear_: screenshot de un libro generado por automagica (~15 min).
- _Crear_: diagrama del pipeline Markdown → LaTeX → PDF → impresora (~30 min).

**Tags propuestos:** `['LaTeX', 'self-publishing', 'libros', 'automagica', 'Biblias', 'nerd lateral']`

**Estado actual:** fork + caso de uso real. Post fácil, complementa [[J-04]]. Prosa escrita contra el outline de seis puntos (~1.350 palabras, dentro del target short-medium). El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 4 de 8 marcadores [VERIFICAR:].

- **Lo que quedó cerrado:** el encuadre del problema (self-publishing técnico sin diseñador), la explicación conceptual de por qué LaTeX es la herramienta natural para esto (`memoir` y la clase `book` sí están respaldados por la bibliografía), el capítulo de trampas (fonts con glifos antiguos, hyphenation de español antiguo, CMYK vs RGB, sangrado), el cruce con [[J-04]] como marco narrativo, y el cierre.
- **Huecos `🕳️` (8):** todo lo que es memoria o decisión de César — por qué forkeó, qué le cambió al upstream, cómo lo encontró, cuál es la tercera Biblia, si llegó a mandar algo a imprenta y con qué servicio, qué tipografía eligió y qué trampa lo mordió de verdad. El post **no se puede publicar** sin responder al menos «por qué forkeaste», «qué le cambiaste» y «¿lo imprimiste?»: sin eso no hay post, hay un tutorial genérico de LaTeX.
- **Datos con `[VERIFICAR:]` — resueltos el 2026-07-16 (fetch del repo):** el upstream **no** es `jorgearaya/automagica` (URL 404, era un error del draft) sino **`jjconti/automagica`** de Juan José Conti (TeX, GPL-3.0, vivo); el fork **parte de Markdown vía pandoc**; **no hay Makefile** (scripts de Python, `automagica.py`); el fork **genera sólo el interior** (PDF + cuadernillo + EPUB), **sin** tapa/lomo (el upstream actual sí tiene tapa —`bookcover.cls`, `automagica-cover.py`—, pero eso es posterior al fork de 2017); la clase **no es `memoir`** sino una `template.tex` propia (`memoir` es recomendación mía).
- **Datos con `[VERIFICAR:]` — todavía abiertos (2):** (1) si existe un set de patrones de hyphenation para español antiguo o si la salida real es `\hyphenation{}` a mano — no encontrado, sin confirmar; (2) los requisitos concretos y actuales de Lulu y de KDP (sangrado, cálculo de lomo, perfil de color) — se dejan a propósito para leer y fechar al momento de publicar.
- **Conflicto con la regla de no-inventar — ahora resuelto por verificación:** el Concepto y el Hook afirman «Markdown → LaTeX → PDF interior + PDF tapa» y «un script Make». Verificado contra el repo: acierta el Markdown, pero en el fork **no hay Makefile** (son scripts Python) y **no se genera tapa** (sólo interior). La prosa de la sección 3 ya quedó reescrita con los hechos; el Concepto y el Hook (que son de César) siguen sin tocar y habrá que ajustarlos antes de publicar.
- **Imágenes:** las dos siguen pendientes y ambas dependen de los huecos (no se puede screenshotear un libro generado sin saber cuál).

---

## Borrador de prosa

> ⚠️ **Curiosidad nerd lateral — esto no es ciencia de la computación.**

Tenés un texto. Está terminado, corregido, limpio. Y querés que sea un libro: un objeto con tapa, con lomo, que pese, que se pueda poner en un estante. Entre esas dos cosas —el texto y el objeto— la industria puso, durante siglos, a una persona: alguien que sabe de tipografía, de márgenes, de sangrado, de cuánto mide el lomo según cuántas páginas tenga el interior. Un diseñador editorial. Y está perfecto que exista, porque hace bien un trabajo difícil.

Pero si tu libro es un texto histórico en dominio público que vas a imprimir en tres ejemplares para vos y dos amigos, contratar a un diseñador es como llamar a un arquitecto para colgar un estante. Lo que querés es escribir `make` y que del otro lado salgan dos PDF: el interior y la tapa, con las dimensiones exactas que el servicio de impresión te va a pedir. Eso es lo que hace *automagica*, un proyecto en TeX que tengo forkeado[^automagica] y que usé para el proyecto del que ya hablé en [[J-04]]: tipografiar Biblias viejas por gusto.

### El problema real no es tipografiar: es el milímetro

Acá conviene separar dos cosas que se confunden todo el tiempo.

La primera es **componer el texto**: elegir una tipografía, fijar la caja, decidir el interlineado, partir en capítulos, poner las notas al pie donde corresponde. Eso LaTeX lo hace bien desde hace cuarenta años y no hay discusión. La clase `book` estándar te da un libro decente sin que hagas nada,[^book] y `memoir` —que es una clase pensada específicamente para libros— te da control fino sobre el stock de papel, la caja de texto, los encabezados y las páginas preliminares.[^memoir]

La segunda es **preparar el archivo para una imprenta**, y ahí es donde se pudre todo. Un servicio de impresión bajo demanda no quiere un PDF lindo: quiere un PDF con el tamaño de página exacto que elegiste en su catálogo, con el sangrado que pide, con los márgenes interiores que su encuadernación se come, y —para la tapa— **una sola pieza** que contenga contratapa, lomo y tapa juntos, donde el ancho del lomo es una función de la cantidad de páginas del interior y del gramaje del papel.[^lulu][^kdp]

Esa dependencia es la clave de todo el asunto: **no podés diseñar la tapa hasta que el interior esté compilado**, porque hasta que no compilás no sabés cuántas páginas tiene, y hasta que no sabés cuántas páginas tiene no sabés cuánto mide el lomo. Es una dependencia de build. Y cuando algo es una dependencia de build, la herramienta correcta no es un programa de diseño: es un Makefile.

Por eso el proyecto se llama *automagica* y no «plantilla de libro».

El upstream —verificado el 2026-07-16— no es `jorgearaya/automagica` (esa anotación del draft estaba equivocada y esa URL da 404) sino **[`jjconti/automagica`](https://github.com/jjconti/automagica), de Juan José Conti**: un proyecto en TeX, licencia GPL-3.0, cuya descripción oficial es «Permite crear en forma fácil libros listos para imprenta o para distribuir digitalmente». El upstream sigue vivo. Mi [fork](https://github.com/CesarBallardini/automagica) quedó congelado en su última actividad de octubre de 2017, así que describe una foto vieja del proyecto, no el estado actual de Conti.

### Qué hay adentro

Abrí el repo de mi fork el 2026-07-16 en vez de escribir esto de memoria, y esto es lo que hay de verdad. (a) **El pipeline arranca en Markdown y pasa por pandoc**: las dependencias que pide son `pandoc`, `pdflatex`, Python 2 y `pdfrw`. (b) **No hay Makefile**: son scripts de Python sueltos, con `automagica.py` como punto de entrada (más `template.py`, `utils.py`, `epub.py` y `pdf/booklet.py`). (c) **Mi fork genera sólo el interior**, en tres formatos —PDF, PDF en formato cuadernillo (`pdf/booklet.py`) y EPUB (`epub.py`)—: **no** trae generación de tapa con lomo calculado. Ojo con esto, porque es donde el fork se aparta del upstream: el `jjconti/automagica` de hoy sí incluye generación de tapa (`bookcover.cls`, `automagica-cover.py`), pero eso llegó después de que yo congelara mi copia en 2017. (d) La clase LaTeX **no es `memoir`**: el fork usa una plantilla propia, `template.tex`. `memoir` es una recomendación mía para quien quiera control fino, no lo que automagica usa. (e) **No trae presets de dimensiones por servicio de impresión.**

Así que el Concepto de este draft —«Markdown → LaTeX → PDF interior + PDF tapa» con «un script Make»— acierta en el Markdown y falla en dos puntos verificables: en mi fork no hay Makefile (son scripts Python) y no se genera la tapa (sólo el interior). Es exactamente el tipo de desajuste que un fork tiene con el recuerdo que uno guarda de él.

Lo que sí puedo decir sin abrir nada es la **forma** que tiene la solución, porque es la misma forma que tiene cualquier build decente. Hay fuentes de texto que un humano edita. Hay un archivo de configuración donde declarás las cosas que el impresor necesita saber: tamaño de página, márgenes, gramaje. Hay una regla que compila el interior. Hay una regla que lee el resultado del interior —el número de páginas— y con eso arma la tapa. Y hay un `all` que las encadena. Nada de eso es original: es la lógica de `make` —que Stuart Feldman escribió en los Bell Labs en 1976— haciendo lo que hace desde entonces, aunque en automagica esa lógica la lleven scripts de Python y no un Makefile. Lo raro es que el artefacto final sea un objeto de papel.

> 🕳️ **HUECO — necesita a César:** ¿Por qué forkeaste automagica en vez de usarlo tal cual? ¿Le faltaba algo concreto (español, un tamaño de página, un servicio de impresión) o fue un fork defensivo para no depender del upstream?

> 🕳️ **HUECO — necesita a César:** ¿Qué le cambiaste al fork? Dos o tres cosas puntuales alcanzan.

> 🕳️ **HUECO — necesita a César:** ¿Lo encontraste buscando «cómo genero un libro para Lulu» o llegaste por otro lado?

### El cruce con las Biblias

El caso de uso no fue hipotético. Todo esto lo miré por el proyecto de [[J-04]]: la Reina-Valera 1865 y la Geneva Bible 1564. Y una Biblia es, para este pipeline, el peor cliente posible y por eso el mejor test: son mil y pico de páginas, tiene una estructura de capítulo y versículo que no se parece a la de ningún otro libro, tiene notas al margen, y el lomo que sale de mil páginas es lo suficientemente ancho como para que el error de un milímetro se note.

> 🕳️ **HUECO — necesita a César:** El outline habla de «tres Biblias»: RV 1865, Geneva 1564 y «la tercera que esté en desarrollo». ¿Cuál es la tercera? Si no existe, el título del post tiene que decir dos.

> 🕳️ **HUECO — necesita a César:** ¿Llegaste a mandar alguno de estos PDF a imprimir de verdad, o el proyecto terminó en el PDF? Esto define el tono del post entero: «te cuento cómo se hace» vs «tengo el libro en la mano».

> 🕳️ **HUECO — necesita a César:** Si lo imprimiste: ¿qué servicio, cuánto salió, y qué salió mal en la primera prueba? La anécdota del primer ejemplar que llega con algo torcido es el mejor final posible para este post.

### Las trampas

Las cosas que rompen no son las que uno espera. Ninguna tiene que ver con LaTeX; todas tienen que ver con que el resultado va a existir físicamente.

**Los glifos.** Un texto del siglo XIX o XVI tiene caracteres que las tipografías modernas no traen, y una tipografía libre que se vea bien en pantalla puede no tener el glifo que necesitás en la página 400. Te enterás compilando, cuando aparece un cuadradito.

> 🕳️ **HUECO — necesita a César:** ¿Qué tipografía terminaste usando y qué glifo específico te obligó a cambiar de idea (si pasó)?

**La partición de palabras.** LaTeX corta palabras con patrones de hyphenation por idioma, y los patrones que existen son de español moderno. El español de 1865 tiene ortografía y morfología que esos patrones no vieron nunca. En un texto a dos columnas y justificado, un corte mal hecho no es una molestia: es una línea fea cada tres páginas, mil páginas seguidas.

[VERIFICAR: si existe algún paquete o set de patrones para español antiguo, o si la salida real es una lista de excepciones a mano con `\hyphenation{}`. No afirmar ninguna de las dos sin comprobarlo.]

**El color.** La pantalla es RGB, la imprenta es CMYK, y el naranja que elegiste para la tapa puede no existir en tinta. Los servicios de impresión bajo demanda documentan qué perfil de color esperan.[^lulu][^kdp]

[VERIFICAR: qué pide exactamente cada servicio hoy — perfil de color, sangrado en milímetros o pulgadas, si aceptan RGB y convierten ellos, y cómo calculan el lomo. Estos números cambian; hay que leerlos en la documentación de Lulu y de KDP al momento de publicar, y fechar la afirmación en el post.]

**Y la trampa madre: el sangrado.** Todo lo que llega al borde de la tapa tiene que extenderse más allá del corte, porque la guillotina no es exacta. Si tu tapa termina justo donde termina la página, vas a recibir un libro con una línea blanca de un pelo en el borde. Esto es obvio para cualquiera que haya trabajado en gráfica y es invisible para cualquiera que venga del software.

> 🕳️ **HUECO — necesita a César:** ¿Cuál de estas cuatro te mordió a vos de verdad? Prefiero contar una que te pasó que enumerar cuatro que podrían pasar.

### Por qué me gusta esto

Hay algo que me cierra mucho en este proyecto y no es la tipografía. Es que un Makefile termine en un objeto físico. Casi todo lo que compilamos se queda del lado del vidrio: un binario, un sitio, un PDF que nadie imprime. Acá el último eslabón de la cadena de dependencias es un tipo con una guillotina, y el `make` que corrés en tu casa a las once de la noche llega, catorce días después, en forma de un paquete.

Si tenés un texto y querés un libro —un manual interno, tu tesis, un texto viejo en dominio público que te gusta—, este es el camino. Es más lento de arrancar que abrir un procesador de texto y muchísimo más rápido la segunda vez, que es la propiedad que tienen todas las herramientas que valen la pena.

[^automagica]: Upstream: [`jjconti/automagica`](https://github.com/jjconti/automagica), de Juan José Conti — proyecto en TeX, licencia GPL-3.0, activo (verificado 2026-07-16). Mi fork: [`CesarBallardini/automagica`](https://github.com/CesarBallardini/automagica), última actividad 2017-10-12. La URL `jorgearaya/automagica` que traía el draft era incorrecta (da 404).
[^book]: [LaTeX Project — Books with LaTeX](https://www.latex-project.org/help/books/).
[^memoir]: [Paquete `memoir` en CTAN](https://www.ctan.org/pkg/memoir).
[^lulu]: [Lulu](https://www.lulu.com/) — especificaciones de impresión. [VERIFICAR: enlazar la página concreta de specs y anotar la fecha de consulta.]
[^kdp]: [Amazon KDP](https://kdp.amazon.com/) — opciones de impresión. [VERIFICAR: enlazar la página concreta de specs y anotar la fecha de consulta.]

