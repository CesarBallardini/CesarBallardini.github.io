### D-02 — Sketchpad: Ivan Sutherland inventa todo en 1963

- **Archivo seed:** `dev/draft-sketchpad.md`
- **Slug propuesto:** `sketchpad-sutherland-1963`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-sketchpad-sutherland-1963/index.md`
- **Serie:** D
- **Cross-links:** depende de [[tr-13]]; lleva a [[D-01]] (Engelbart, mismo período), [[A1-01]] (Kay — Sketchpad fue una de sus influencias declaradas), [[A2-04]] (programación dirigida por restricciones)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** Ivan Sutherland presentó en 1963 su tesis doctoral en MIT: un programa llamado Sketchpad que corría en un TX-2 con una pantalla CRT y un *light pen*. En esa tesis aparecen, antes de que la palabra existiera: la programación orientada a objetos (con instancias y "masters"), la restricción declarativa, la edición gráfica directa, el zoom, el modelado paramétrico. Alan Kay diría después que toda su carrera fue tratar de entender Sketchpad.

**Hook:** "antes que existiera el mouse, antes que existiera la palabra 'gráfico' en computación, antes que la palabra *object-oriented* fuera acuñada, Ivan Sutherland defendió en MIT una tesis donde ya estaba todo. 1963. Light pen. CRT. Restricciones. Instancias. Si te suena increíble es porque lo es."

**Outline:**
1. El contexto: MIT Lincoln Lab, el TX-2, la era de las máquinas de habitación entera.
2. Qué hacía Sketchpad: el video del demo (sí, hay video del 63) muestra dibujar geometría restringida con un lápiz óptico.
3. Los conceptos que inventa sin nombrarlos:
   - **Masters and instances** — el patrón de instanciación que después llamaríamos "clase / objeto".
   - **Constraints** — restricciones declarativas, antecedente directo de Prolog.
   - **Atomic operations** — antecedente del comando undo/redo.
   - **Recursive operations on hierarchies** — el árbol de escena, primer ancestro de todo motor 3D.
4. Por qué Kay considera Sketchpad la influencia número uno de Smalltalk.
5. Sutherland no se quedó en eso: cofundó Evans & Sutherland (gráficos 3D), el HMD original (1968), el Turing 1988.
6. La conexión moderna: Inkscape, Figma, los CAD paramétricos como Fusion 360, todo es Sketchpad sobreviviendo.
7. Cierre: si quisieras inventar algo grande, mirá lo que ya estaba inventado en 1963.

**Bibliografía:**
- **[[tr-13]]** — Ivan E. Sutherland, *Sketchpad: A Man-Machine Graphical Communication System*, tesis doctoral MIT, enero de 1963. Reeditada como University of Cambridge Technical Report UCAM-CL-TR-574 (septiembre de 2003, **149 páginas**, con nuevo prefacio de Alan Blackwell y Kerry Rodden): [PDF](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf) — fetch verificado 2026-07-16 (resuelve, 3,9 MB; es una edición electrónica **re-tipografiada**, no un escaneo). Fuente directa de casi todos los datos duros del post: TX-2, *master drawing*/*instance*, *one pass method* + *relaxation*, 17 restricciones atómicas. **estable**.
- Registro canónico de la tesis en el repositorio del MIT: [hdl.handle.net/1721.1/14979](https://hdl.handle.net/1721.1/14979) — DSpace bloquea el fetch automatizado (HTTP 405); confirmado por búsqueda (el handle `1721.1/6933` de notas viejas es incorrecto). **estable**.
- Versión de conferencia (la más citada, más corta): Ivan E. Sutherland, *Sketchpad: A Man-Machine Graphical Communication System*, AFIPS Spring Joint Computer Conference, vol. 23 (1963), p. 329 y ss. DOI canónico [10.1145/1461551.1461591](https://doi.org/10.1145/1461551.1461591) (verificado vía api.crossref.org, 2026-07-16; ACM DL con paywall). Espejo libre del PDF: [cl.cam.ac.uk/~pr10/iui/sutherland63.pdf](https://www.cl.cam.ac.uk/~pr10/iui/sutherland63.pdf) (HTTP 200, 2026-07-16). DOI **estable**; espejo **frágil**.
- **[[tr-01]]** — Alan C. Kay, *The Early History of Smalltalk*, ACM SIGPLAN Notices 28(3):69–95 (1993). Copia en línea: [worrydream.com/EarlyHistoryOfSmalltalk](http://worrydream.com/EarlyHistoryOfSmalltalk/) — fetch verificado 2026-07-16. Kay cuenta que al llegar a Utah (otoño de 1966) Dave Evans le dio a leer la tesis de Sketchpad («Take this and read it. Every newcomer got one») y enumera sus «tres grandes ideas», entre ellas «the invention of modern interactive computer graphics» y que «things were described by making a 'master drawing' that could produce 'instance drawings'». El sitio es personal (**frágil**); registro ACM SIGPLAN como respaldo estable.
- Prefacio de la edición de Cambridge (Alan Blackwell y Kerry Rodden, 2003, incluido en el PDF de [[tr-13]]): documenta que la herencia basada en clase e instancia de Sketchpad «predated Simula by several years» y que Kay atribuye la génesis de Smalltalk a «the coincidental appearance on his desk of both a distribution tape of Simula and a copy of Sutherland's Sketchpad thesis». Confirma también el Turing 1988 y que Sketchpad corría en «a customized machine at the MIT Lincoln Laboratory». **estable**.
- [Ivan E. Sutherland, *A Head-Mounted Three Dimensional Display*, AFIPS Fall Joint Computer Conference (1968)](https://doi.org/10.1145/1476589.1476686) — DOI 10.1145/1476589.1476686 (ACM DL). El primer HMD. **estable** (DOI).
- [ACM A.M. Turing Award 1988 — Ivan Sutherland](https://amturing.acm.org/award_winners/sutherland_3467412.cfm) — la página devolvió HTTP 403 al fetch automatizado (2026-07-16); el premio de 1988 queda confirmado además por el prefacio de [[tr-13]]. **estable**.
- Evans & Sutherland: fundada en 1968 por Ivan Sutherland y **David C. Evans** (Universidad de Utah), hardware de gráficos 3D en tiempo real — [Evans & Sutherland (Wikipedia)](https://en.wikipedia.org/wiki/Evans_%26_Sutherland) y [ficha del Computer History Museum](https://www.computerhistory.org/brochures/d-f/evans-and-sutherland-computer-corporation/). **estable**.
- [Computer History Museum, *Ivan Sutherland Oral History*](https://www.computerhistory.org/collections/catalog/102702072) — entrevista de 2005. **frágil** (no verificado por fetch en esta pasada).
- [Bret Victor, *The Future of Programming*, DBX 2013](https://vimeo.com/71278954) — donde Victor usa Sketchpad como ejemplo de "ya lo teníamos". **frágil**.
- Video del demo: [Sketchpad — film de 16 mm, ~16:41 min](https://www.youtube.com/watch?v=mOZqRJzE8xg) — **frágil** (YouTube; sin snapshot en Wayback Machine al 2026-07-16 — pendiente crear copia antes de publicar).

**Imágenes:**
- _Wikimedia_: foto del TX-2 — ⚠️ el archivo `File:TX-2_console.jpg` **devolvió HTTP 404 el 2026-07-16 (no existe con ese nombre)**. Hay que buscar una foto real del TX-2 en Wikimedia Commons (probar la categoría del TX-2 o del Lincoln Laboratory) y verificar su licencia antes de usarla.
- _Wikimedia_: foto de Ivan Sutherland — [Ivan Sutherland at CHM](https://commons.wikimedia.org/wiki/File:Ivan_Sutherland_at_CHM.jpg) — **verificado 2026-07-16**: autor **Dick Lyon**, doble licencia **GFDL 1.2+ y CC BY-SA 3.0**; Sutherland en su cumpleaños 70 en el Computer History Museum, 22 de mayo de 2008.
- _Embed_: el video del demo del 63 (YouTube).
- _Crear_: diagrama simple del modelo masters/instances de Sketchpad y cómo se mapea a clases/objetos modernos (~30 min).

**Tags propuestos:** `['Sutherland', 'Sketchpad', 'MIT', 'graficos', 'historia', 'CAD']`

**Estado actual:** El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch: PDF de la tesis en Cambridge UCAM-CL-TR-574 —149 páginas, texto extraído y leído directamente—, prefacio de Blackwell y Rodden, *The Early History of Smalltalk* de Kay, DOI del paper AFIPS verificado vía api.crossref.org, licencia de la foto hero) y se resolvieron **9 de 11** marcadores `[VERIFICAR:]`. Resueltos con fuente: cantidad de páginas (149, re-tipografiadas, no ~200 escaneadas), sede del TX-2 (MIT Lincoln Laboratory, 1956), características del TX-2 (36 bits, ~70.000 palabras, 64 index registers, cinta magnética, lápiz óptico), duración del video (~16:41, no «6 minutos»), terminología literal (*master drawing*/*instance*, Cap. VI), mecanismo de restricciones (*one pass method* + *relaxation*, 17 restricciones atómicas), formulación exacta de Kay, y fundación de Evans & Sutherland (1968, con David C. Evans). Corregido contra la fuente: el «undo» —la tesis documenta *delete*/*erase*, no un `undo` general— y la afirmación de páginas escaneadas. **Quedan 2 abiertos**: (a) la filiación documentada Sketchpad→Prolog/constraint programming (ninguna fuente obtenida la acredita; sigue como parecido conceptual, remite a [[A2-04]]); (b) la licencia de la foto del TX-2 (el archivo `File:TX-2_console.jpg` **no existe** en Commons —HTTP 404—, hay que hallar otra imagen). Además quedó un **nuevo hueco menor**: no pude confirmar quién opera en la filmación del demo (la duración sí). La foto hero (`Ivan_Sutherland_at_CHM.jpg`) quedó verificada: Dick Lyon, CC BY-SA 3.0 / GFDL.

Prosa completa escrita siguiendo el outline de 7 puntos, citando únicamente la bibliografía ya verificada del draft. Quedaron **tres huecos** (🕳️): el primer contacto de César con el video del demo, si alguna vez usó un lápiz óptico o tableta gráfica de la era pre-mouse, y qué herramienta paramétrica/vectorial usa hoy (para anclar el punto 6 en experiencia propia en vez de en una lista genérica de productos). Quedaron **once marcas `[VERIFICAR:]`** sobre detalles que la bibliografía existente probablemente respalda pero que no fueron chequeados contra la fuente: cantidad de páginas de la tesis, sede exacta del TX-2 y su relación con el Lincoln Laboratory, características de la máquina, duración real del video del demo y quién lo opera, terminología literal de la tesis (*master*/*instance*), el mecanismo y algoritmo de resolución de restricciones, el alcance real del deshacer, la formulación exacta de la deuda que Kay declara con Sketchpad, la cofundación de Evans & Sutherland (año, socio, producto inicial) y la licencia de la foto del TX-2. Además, **la afirmación del outline de que las restricciones de Sketchpad son «antecedente directo de Prolog» quedó escrita con reserva explícita**: la prosa la baja a «mismo espíritu, filiación no comprobada» y deja un `[VERIFICAR:]` para buscar la línea causal documentada antes de afirmarla. Pendiente al publicar: resolver los `[[ID]]` a URLs reales, verificar la licencia de las dos imágenes de Wikimedia (la del TX-2 está marcada «verificar» en el propio draft), recortar el hero a 2.5:1, armar el diagrama masters/instances y chequear que el video de YouTube siga vivo (link frágil — guardar copia en Wayback Machine).

---

## Borrador de prosa

Antes de que existiera el mouse, antes de que la palabra «gráfico» significara algo en computación, antes de que alguien acuñara el término *object-oriented*, un estudiante de doctorado del MIT defendió una tesis donde ya estaba todo. Año 1963. Una pantalla CRT, un lápiz óptico, una computadora del tamaño de un departamento, y un programa llamado Sketchpad que hacía cosas que tu CAD de hoy hace parecido y que tu editor de texto todavía no hace.

Si te suena increíble, es porque lo es. Y la parte incómoda no es que Ivan Sutherland haya sido un genio —eso ya lo sabemos, la ACM le dio el Turing en 1988[^turing]—. La parte incómoda es que la tesis está online, gratis: la reedición de Cambridge (UCAM-CL-TR-574) tiene **149 páginas** —re-tipografiadas, no escaneadas— con un prefacio nuevo de Alan Blackwell y Kerry Rodden[^sketchpad], y que sesenta y tres años después seguimos redescubriendo de a pedazos lo que ahí ya estaba resuelto.

### El contexto: una máquina que no era para vos

Sketchpad corría en el TX-2, una computadora experimental del **MIT Lincoln Laboratory** (Lexington, Massachusetts), construida en 1956; el prefacio de la edición de Cambridge la describe como «a customized machine at the MIT Lincoln Laboratory», y las copias ejecutables de Sketchpad nunca salieron de ahí[^sketchpad]. Para entender lo que sigue tenés que sacarte de la cabeza cualquier idea moderna de «usar la computadora». En 1963 la computación normal era batch: escribías, perforabas, entregabas, esperabas, y al otro día te devolvían un listado con tu error de sintaxis. La máquina no era tuya. Era de la institución, la usabas por turnos, y la idea de sentarte *frente* a ella a dibujar era, literalmente, un despilfarro de un recurso carísimo.

El TX-2 era la excepción: una máquina experimental con pantalla, pensada para uso interactivo por una persona a la vez. La tesis la describe con precisión: palabras de 36 bits, unas **70.000 palabras de memoria de núcleos** (una memoria «S» de 65.536 palabras más una memoria «T» de 4.096, más rápida), **64 registros índice**, cinta magnética como almacenamiento auxiliar, y como entrada el lápiz óptico y una fila de botones (Apéndice G)[^sketchpad]. Sutherland tuvo acceso a eso, y en vez de usarlo para calcular más rápido, lo usó para preguntarse algo distinto: ¿y si la computadora y yo pudiéramos *conversar* dibujando?

> 🕳️ **HUECO — necesita a César:** ¿llegaste a usar alguna vez un lápiz óptico, una tableta digitalizadora o algún dispositivo de entrada gráfica de la era pre-mouse? Si sí, ¿en qué máquina y para qué? Una o dos frases: sirve para anclar el contraste con el batch en experiencia propia y no en historia leída.

### Qué hacía Sketchpad

Hay video. Eso es lo primero que hay que decir, porque nadie lo cree: existe una filmación del demo[^demo], de la época: un film de 16 mm de unos **16 minutos y medio** (no los «6 minutos» que decía el plan), donde se ve a una persona sentada frente al TX-2 dibujando con el lápiz óptico sobre la pantalla [VERIFICAR: quién opera exactamente en la filmación —¿Sutherland u otra persona?—; la duración (~16:41) surge de metadatos del video, el operador no lo pude confirmar].

Lo que se ve no es «un programa de dibujo». Un programa de dibujo, en el sentido de MS Paint, pinta píxeles. Sketchpad no pintaba nada: manipulaba *geometría con relaciones*. Dibujabas dos líneas a mano alzada, torcidas, feas, y le decías al sistema: estas dos son perpendiculares. Y el dibujo se acomodaba solo. Decías: estos cuatro segmentos tienen que tener el mismo largo, y estos dos vértices tienen que coincidir. Y el sistema resolvía el sistema de restricciones y te devolvía un cuadrado[^sketchpad].

Vos no dibujabas un cuadrado. Dibujabas una intención, y la máquina la satisfacía.

Ese salto —de «pinto lo que quiero ver» a «declaro lo que tiene que ser cierto y la máquina lo hace cierto»— es el corazón del asunto, y es la razón por la que este post existe.

### Los conceptos que inventó sin ponerles nombre

Acá viene la lista que da vértigo. En esa tesis, en 1963, aparecen —funcionando, no como especulación— por lo menos cuatro ideas que la disciplina iba a redescubrir y bautizar mucho más tarde[^sketchpad].

**Masters e instancias.** En Sketchpad definías un dibujo *master* —digamos, un remache— y después lo instanciabas cuantas veces quisieras en el dibujo grande. Las instancias no eran copias: eran referencias al master. Cambiabas el master y cambiaban todas las instancias, en todos lados, al mismo tiempo. Cambiá la palabra «master» por «clase» y la palabra «instancia» por «objeto» y contame qué te queda. Sutherland no dijo «orientado a objetos» porque el término todavía no existía; simplemente lo implementó y siguió. Las palabras son de él: la tesis habla de un *master drawing* (por ejemplo, «a single master transistor drawing» del que se crean todos los símbolos de transistor) y de *instances*, con una «recursive instance expansion» que permite instancias dentro de instancias; el comportamiento del *instance* se detalla en el Capítulo VI[^sketchpad]. El prefacio de Cambridge lo resume sin vueltas: esa «class and instance-based inheritance (though not called objects)» de Sketchpad «predated Simula by several years»[^sketchpad].

**Restricciones declarativas.** Las relaciones que le imponías al dibujo no eran instrucciones: eran hechos que el sistema tenía que mantener verdaderos. Vos decías *qué*, no *cómo*, y adentro había un motor que se encargaba del cómo. Eso es programación declarativa, en 1963, en una máquina de válvulas y transistores, resuelta a mano por un doctorando que estaba tratando de dibujar puentes[^sketchpad]. La tesis usa dos métodos, el barato primero: un *one pass method* (propagación —cuando el valor que falta se deduce directo de lo ya conocido—, emparentado con una técnica de «maze-solving» que Sutherland liga al algoritmo de Moore para el camino más corto) y, cuando ese no alcanza, *relaxation* (relajación numérica que empuja los valores reduciendo el «error» de cada restricción hasta que converge). El conjunto de restricciones **atómicas** son 17 (arrancó con 5 y creció a 17 en unos dos días, listadas en el Apéndice A)[^sketchpad]. El outline de este post decía que esto es «antecedente directo de Prolog»; yo lo diría con más cuidado: es el mismo espíritu, pero la línea causal entre Sketchpad y la programación lógica no me consta [VERIFICAR: si existe una filiación documentada entre Sketchpad y la tradición de constraint programming/Prolog, o si es sólo un parecido conceptual; buscar en la bibliografía secundaria antes de afirmar «antecedente directo»]. Lo que sí es seguro es que la idea de programación dirigida por restricciones tiene acá un ancestro que casi nadie cita — de eso hablo en [[A2-04]].

**Operaciones atómicas sobre la estructura.** Sketchpad opera con operaciones atómicas sobre su estructura de anillos (crear, relacionar, borrar componentes). Acá conviene ser honesto con la fuente: lo que la tesis documenta explícitamente es un botón *delete* / *erase* —se apunta con el lápiz y se borra una línea, un círculo o un símbolo entero, y borrar una línea borra también su restricción asociada— pero **no** encontré en la tesis un `undo`/rehacer general en el sentido moderno[^sketchpad]. El parentesco con el `undo` de hoy es conceptual (pensar la edición como operaciones discretas y reversibles sobre una estructura), no una función llamada así que esté en el documento.

**Jerarquías recursivas.** Un master podía contener instancias de otros masters, que a su vez contenían instancias de otros. Un árbol de dibujos anidados, con las operaciones aplicándose recursivamente hacia abajo. Eso es un *scene graph*. Todo motor 3D, todo CAD, todo SVG, todo el DOM de tu navegador: árboles de nodos con transformaciones que se componen hacia abajo. Primer ancestro documentado, 1963[^sketchpad].

Sumale zoom, sumale que el modelo era paramétrico —cambiás un parámetro del master y se reacomoda el dibujo entero— y tenés la descripción de un producto que hoy se vende por suscripción mensual.

### Kay: «toda mi carrera fue tratar de entender Sketchpad»

Alan Kay es explícito sobre esta deuda. En *The Early History of Smalltalk*[^kay] cuenta que al llegar a la Universidad de Utah, en el otoño de 1966, el profesor Dave Evans le puso la tesis en la mano: «Take this and read it. Every newcomer got one. The title was 'Sketchpad: A man-machine graphical communication system'». Y enumera sus «tres grandes ideas»: «it was the invention of modern interactive computer graphics» y que «things were described by making a 'master drawing' that could produce 'instance drawings'»[^kay]. El prefacio de la edición de Cambridge remata la genealogía: la génesis de Smalltalk estuvo en «the coincidental appearance on his desk of both a distribution tape of Simula and a copy of Sutherland's Sketchpad thesis»[^sketchpad].

Y tiene todo el sentido del mundo, porque lo que Kay vio en Sketchpad no fue el dibujo: fue el *modelo de cómputo*. Masters que se comportan, instancias que heredan comportamiento, un sistema donde el usuario y la máquina se responden en tiempo real. Sacale la pantalla y la geometría y te queda una máquina de objetos. De esa raíz sale Smalltalk, y de Smalltalk sale casi todo lo que programás — ver [[A1-01]].

### Sutherland no se quedó ahí

Lo que suele arruinar estas historias es que el pionero hace una cosa gigante a los veinticinco años y después administra su leyenda durante cuarenta. Con Sutherland no pasó. En 1968 cofundó Evans & Sutherland junto a **David C. Evans** (colega en la Universidad de Utah), la empresa que básicamente inventó la industria del hardware de gráficos 3D en tiempo real —y de cuyas filas salieron, entre otros, Jim Clark (Silicon Graphics), Ed Catmull (Pixar) y John Warnock (Adobe)[^es]. Ese mismo 1968 publicó el trabajo sobre un display tridimensional montado en la cabeza[^hmd]: el primer HMD, el abuelo declarado de todo lo que hoy se vende como realidad virtual. Y en 1988 la ACM le dio el Premio Turing[^turing] [^img_hero].

Es decir: inventó la interfaz gráfica, después inventó la industria que la iba a renderizar, después inventó los anteojos. Hay currículums y currículums.

### Todo lo que usás es Sketchpad sobreviviendo

Abrí Figma y agrupá elementos: árbol de escena. Creá un componente y usalo en veinte pantallas: masters e instancias. Alineá dos objetos con una guía inteligente que los pega solos: restricción. Abrí Inkscape y clonás un objeto: master e instancia otra vez, con ese nombre. Abrí un CAD paramétrico y ponele a un boceto que dos aristas sean tangentes y que el radio sea la mitad del ancho: constraint solver, exactamente el de la tesis, sesenta años más rápido.

No es que se «parezcan» a Sketchpad. Es que son Sketchpad, con más memoria y peor documentación.

> 🕳️ **HUECO — necesita a César:** ¿qué herramienta de este tipo usás vos hoy (Inkscape, algún CAD, Figma, otra)? ¿Y hay alguna función de esa herramienta donde se te haya hecho evidente que estabas usando una idea vieja? Con un ejemplo concreto alcanza para que este párrafo hable de vos y no de un catálogo.

Bret Victor usa precisamente este ejemplo en *The Future of Programming*[^victor], esa charla donde se disfraza de ingeniero de 1973 para hablar del futuro y te deja con una incomodidad que no se te va en una semana. El argumento es simple y devastador: muchas de las cosas que hoy presentamos como innovación ya las teníamos, y las perdimos, y las estamos reinventando peor.

### El cierre, que es una recomendación

Si algún día querés inventar algo grande, hay un atajo que casi nadie toma: leé lo que ya estaba inventado en 1963.

La tesis está completa, escaneada y gratis[^sketchpad]. El video está a un clic[^demo]. La oral history de Sutherland en el Computer History Museum está publicada[^chm]. No hay barrera de acceso, no hay paywall, no hay excusa. Lo único que hay es la sospecha, muy cómoda, de que un trabajo de hace seis décadas sobre una máquina que ya no existe no puede tener nada para enseñarnos.

Tiene todo. Es exactamente al revés: como no tenían nada, tuvieron que pensar. Nosotros tenemos todo, y a veces se nota.

> 🕳️ **HUECO — necesita a César:** ¿cuándo viste por primera vez el demo de Sketchpad o leíste la tesis, y qué te sorprendió más? Si nunca la leíste entera y sólo viste el video, decilo así —es más honesto y es mejor cierre.

Y si el post te dejó con la sensación de que la computación interactiva nació dos veces en la misma década, tenés razón: cinco años después, a unos kilómetros de ahí, Doug Engelbart hizo lo suyo. Esa es otra historia, y está en [[D-01]].

---

[^sketchpad]: Ivan E. Sutherland, [*Sketchpad: A Man-Machine Graphical Communication System*](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf), tesis doctoral MIT, enero de 1963 — reeditada como reporte técnico UCAM-CL-TR-574 (149 páginas, re-tipografiada, no escaneada) del Computer Laboratory de la Universidad de Cambridge, septiembre de 2003, con prefacio de Alan Blackwell y Kerry Rodden. Registro canónico en el MIT: [hdl.handle.net/1721.1/14979](https://hdl.handle.net/1721.1/14979). PDF verificado por fetch 2026-07-16.
[^demo]: [Sketchpad — demo filmado, Ivan Sutherland](https://www.youtube.com/watch?v=mOZqRJzE8xg) — film de 16 mm, ~16:41 min. Enlace frágil (YouTube); al 2026-07-16 no hay snapshot en Wayback Machine — guardar copia antes de publicar.
[^kay]: Alan C. Kay, [*The Early History of Smalltalk*](http://worrydream.com/EarlyHistoryOfSmalltalk/), ACM SIGPLAN Notices 28(3):69–95, 1993 — donde Kay declara su deuda con Sketchpad («the invention of modern interactive computer graphics», el mecanismo de *master drawing*/*instance drawings*). Copia en línea verificada por fetch 2026-07-16; sitio personal (frágil), registro ACM SIGPLAN como respaldo.
[^hmd]: Ivan E. Sutherland, [*A Head-Mounted Three Dimensional Display*](https://doi.org/10.1145/1476589.1476686), AFIPS Fall Joint Computer Conference, 1968 — DOI 10.1145/1476589.1476686.
[^turing]: [ACM A.M. Turing Award 1988 — Ivan Sutherland](https://amturing.acm.org/award_winners/sutherland_3467412.cfm) (la página devuelve HTTP 403 a fetch automatizado; el premio de 1988 lo confirma además el prefacio de [^sketchpad]).
[^es]: Evans & Sutherland — fundada en 1968 por Ivan Sutherland y David C. Evans (Universidad de Utah), hardware de gráficos 3D en tiempo real. [Evans & Sutherland (Wikipedia)](https://en.wikipedia.org/wiki/Evans_%26_Sutherland); [ficha del Computer History Museum](https://www.computerhistory.org/brochures/d-f/evans-and-sutherland-computer-corporation/).
[^chm]: [*Ivan Sutherland Oral History*](https://www.computerhistory.org/collections/catalog/102702072), Computer History Museum, entrevista de 2005.
[^victor]: Bret Victor, [*The Future of Programming*](https://vimeo.com/71278954), DBX 2013.
[^img_hero]: Imagen de [Ivan Sutherland at CHM](https://commons.wikimedia.org/wiki/File:Ivan_Sutherland_at_CHM.jpg) — CC BY-SA 3.0 / GFDL 1.2+ — autor Dick Lyon (Sutherland en su cumpleaños 70 en el Computer History Museum, 22 de mayo de 2008; licencia verificada 2026-07-16). Recortar a 2.5:1 para hero landscape.
[^img_tx2]: ⚠️ El archivo `File:TX-2_console.jpg` de Wikimedia Commons **devolvió HTTP 404 el 2026-07-16 (no existe con ese nombre)**. Falta encontrar una foto real del TX-2 en Commons y verificar su licencia antes de publicar. (Footnote sin uso en el cuerpo hasta que haya imagen válida.)

