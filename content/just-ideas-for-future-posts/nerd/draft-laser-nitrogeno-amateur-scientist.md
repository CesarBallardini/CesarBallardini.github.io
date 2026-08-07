### J-01 — Construir un láser de nitrógeno (en homenaje a *The Amateur Scientist*)

- **Archivo seed:** `misc/draft-construyendo-un-laser-de-nitrogeno.md`
- **Slug propuesto:** `laser-nitrogeno-amateur-scientist`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-laser-nitrogeno-amateur-scientist/index.md`
- **Serie:** J
- **Cross-links:** lleva a [[I-02]] (revistas de quiosco — el equivalente local), [[D-03]] (Turing — la otra "máquina mínima inventada en una mesa")
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2000 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** *The Amateur Scientist* fue una columna mensual de *Scientific American* desde 1928 hasta 2001 (escrita por C.L. Stong, Jearl Walker y otros), donde un lector podía aprender a construir en su casa cosas como un acelerador de partículas, un microscopio electrónico de barrido, un sismómetro o — *un láser de nitrógeno funcional*. El post cuenta el contexto de la columna, el plano del láser de nitrógeno (uno de los proyectos más famosos), por qué era posible construirlo en una cochera, y lo que significaba culturalmente que eso fuera *publicable* en una revista de divulgación masiva.

**Hook:** "*The Amateur Scientist* fue una columna que publicó *Scientific American* durante 73 años. En esa columna, en julio de 1974, salió el plano de cómo construir en tu casa un láser de nitrógeno funcional. No un puntero láser de juguete: un láser pulsado real, con descargas eléctricas, un canal entre dos electrodos paralelos y un haz UV invisible. Un menor de edad podía juntar los materiales en una ferretería y armarlo. La pregunta del post no es *cómo*. La pregunta es: ¿qué tipo de cultura científica produce que algo así sea normal publicar?"

**Outline:**
1. Qué es un láser de nitrógeno y por qué es perfecto para amateurs: usa nitrógeno del aire, no necesita medio óptico, descarga eléctrica directa, longitud de onda 337 nm (UV).
2. *The Amateur Scientist* — historia de la columna en *Scientific American*. C.L. Stong (1955-1977), Jearl Walker (1977-1990), Forrest Mims y otros (1990-2001). El cierre.
3. El plano original: el artículo de julio 1974 sobre láser de nitrógeno (atribuido a I.G. von Stamwitz). La lista de materiales (alguien la traduce a tornillos de ferretería).
4. Por qué funcionaba: los electrodos paralelos cargados con un transformador de neón, descarga rápida (decenas de nanosegundos), nitrógeno del aire excitado al estado láser, emisión espontánea estimulada en ese ancho de pulso.
5. Qué necesitabas en 1974 que ya no encontrás en 2026: transformadores de neón, condensadores cerámicos de alta tensión, una mesa metálica grande. Sustitutos modernos.
6. La parte cultural: lo que significaba que la divulgación científica masiva *asumiera* que el lector podía soldar y manejar 30 kV. Comparación con la divulgación científica actual.
7. Otros proyectos icónicos de la columna: el microscopio electrónico de Eiichi Goto / Forrest Mims, el reloj atómico de cesio casero (sí), el espectrómetro de masas amateur.
8. Cierre: ¿lo armaría hoy? Sí. ¿Lo recomiendo? Sólo si entendés electricidad de alta tensión y querés vivir.

**Bibliografía:** (reforzada 2026-07-16, fuentes verificadas por fetch)

- [*The Amateur Scientist* — Wikipedia](https://en.wikipedia.org/wiki/The_Amateur_Scientist) — historia y cronología de autores de la columna (verificado: 1928-2001, tramos de cada editor). Estable.
- [C. L. Stong, «An unusual kind of gas laser that puts out pulses in the ultraviolet», *The Amateur Scientist*, *Scientific American* vol. 230, n.º 6 (junio de 1974), pp. 122-127](https://www.scientificamerican.com/article/the-amateur-scientist-1974-06/) — **el artículo original del láser de nitrógeno**. Título, autor, volumen y páginas verificados por fetch en la ficha pública de SciAm (el texto completo está tras paywall). Estable.
- [Sam Goldwasser, *Sam's Laser FAQ — Home-Built Nitrogen (N2) Laser*](https://www.repairfaq.org/sam/lasercn2.htm) — la referencia técnica amateur más completa; confirma 337,1 nm, superradiancia sin espejos, tiempos de pulso y la geometría Blumlein de baja inductancia; también cita el artículo de Stong de junio de 1974. **URL corregida**: la anterior (`lasersn2.htm`) devuelve 404. Estable.
- [*Nitrogen laser* — Wikipedia](https://en.wikipedia.org/wiki/Nitrogen_laser) — física: 337,1 nm, segundo sistema positivo del N₂, transición autoterminante, superradiancia, diseño TEA a presión atmosférica; menciona el artículo de *Scientific American* de 1974 como uno de los primeros de construcción casera. Estable.
- [Jearl Walker (ed.), *Light and Its Uses: Making and Using Lasers, Holograms, Interferometers, and Instruments of Dispersion — Readings from Scientific American*, W. H. Freeman, 1980. ISBN 9780716711841 (tapa dura) / 9780716711858 (rústica)](https://search.worldcat.org/oclc/1150209443) — la compilación en libro donde se reeditó el artículo del láser de nitrógeno de Stong. Estable.
- C. L. Stong, *The Amateur Scientist*, Simon & Schuster, 1960. ISBN 9780671207472 — compilación en libro de la columna (57 proyectos; agotada desde 1972). ISBN según Wikipedia; no verificado contra una copia en archive.org. Estable.
- [Jearl Walker, *The Flying Circus of Physics*, Wiley, 1977 (2ª ed. 2006)](https://www.flyingcircusofphysics.com/) — libro del segundo autor de la columna. Estable.
- [Forrest Mims III, *Getting Started in Electronics*, Master Publishing, 1983 — copia en Internet Archive](https://archive.org/details/Getting_Started_in_Electronics) — otro pilar de la cultura amateur. Estable.
- [«The Poor Man's Nitrogen Laser», *American Journal of Physics* vol. 38, n.º 5 (1970), p. 655](https://pubs.aip.org/aapt/ajp/article-abstract/38/5/655/1048616/The-Poor-Man-s-Nitrogen-Laser) — artículo académico real de construcción de un láser de N₂ amateur (337,1 nm). **Reemplaza** la referencia «I.G. von Stamwitz, AJP 1976» del draft anterior, que NO se pudo verificar en ninguna base y es probablemente inexistente o mal atribuida. Frágil (paywall AIP; abstract público).
- [Scientific American — archivo de la sección *The Amateur Scientist*](https://www.scientificamerican.com/section/the-amateur-scientist/) — página oficial moderna. Estable.
- [Bell Jar — Stephen Hansen (belljar.net)](http://www.belljar.net/) — sitio de ciencia amateur de vacío/plasma; carga (verificado por fetch), pero no se confirmó que cubra específicamente láseres de nitrógeno. Frágil.
- [The Society for Amateur Scientists — sas.org](https://sas.org/) — heredero comunitario de la columna. Frágil (no verificado por fetch en esta pasada).
- [CD-ROM *Scientific American's «The Amateur Scientist»: The Complete 20th Century Collection* (ed. Shawn Carlson y Sheldon Greaves, Tinker's Guild, 2000)](https://archive.org/details/Scientific_American_The_Amateur_Scientist_Tinkers_Guild_2000) — ~72 años de columna en HTML text-searchable. **URL corregida**: la del draft anterior (`the-amateur-scientist-4.0`) devuelve 404; ésta es el ítem real en archive.org. Frágil.

**Imágenes:**
- _Wikimedia_: foto/diagrama de un láser de nitrógeno casero — varios disponibles bajo CC.
- _Wikimedia_: scan de una página de *The Amateur Scientist* — verificar derechos.
- _Crear_: diagrama esquemático del circuito (capacitor + electrodos paralelos + transformador de neón) (~45 min).

**Tags propuestos:** `['Amateur Scientist', 'Scientific American', 'laser', 'nitrogeno', 'divulgacion', 'nerd lateral']`

**Estado actual:** prosa completa escrita sobre el outline de 8 puntos (~1.750 palabras, dentro del target medium). Lo que quedó escrito: el encuadre de la columna, la descripción técnica del láser (apoyada en Sam's Laser FAQ), el argumento cultural — que es el eje real del post —, la comparación con la divulgación actual y el cierre.

Lo que quedó como hueco:

- **Toda la capa personal.** El draft no tenía ni una línea de experiencia vivida, y el post la necesita para no ser una nota enciclopédica. Hay 6 huecos `🕳️` pidiendo cosas concretas: si César leyó la columna (y en qué idioma / qué edición llegaba a Argentina), si se cruzó con los libros de Walker y Mims, si alguna vez armó algo de alta tensión, cuál fue su «página 112», qué proyecto de la columna se quedó con ganas de construir, y su respuesta al cierre.
- **Casi toda la línea de tiempo y las atribuciones.** Hay 10 marcas `[VERIFICAR:]`. La bibliografía sostiene *que* la columna existió y *quiénes* la escribieron a grandes rasgos (Wikipedia), pero no alcanza para afirmar fechas exactas, tramos de autoría, ni la referencia del artículo del láser.
- **Conflicto sin resolver dentro del propio draft:** el Hook dice «julio de 1974» y la Bibliografía dice «American Journal of Physics 1976 — verificar referencia exacta». Son dos publicaciones distintas (*Scientific American* vs. AJP) y dos fechas distintas. La prosa está escrita alrededor del conflicto sin comprometerse con ninguna de las dos versiones; hay que resolverlo antes de publicar, porque el Hook depende de esa fecha.
- **Otros proyectos icónicos (punto 7 del outline):** escrito en condicional y marcado, porque ninguna de las fuentes listadas respalda todavía la lista concreta (microscopio electrónico, reloj de cesio, espectrómetro de masas).

Próximo paso sugerido: abrir el CD-ROM de la columna (está en archive.org, ya en la bibliografía con la URL corregida) y resolver las marcas que quedan, sobre todo la lista de materiales del plano original y los «otros proyectos».

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 6 de 10 marcadores [VERIFICAR:]. Resueltos: (1) el artículo del láser salió en **junio de 1974** (no julio), *Scientific American* vol. 230 n.º 6, pp. 122-127, firmado por **C. L. Stong** — la atribución a «I.G. von Stamwitz» del outline/bibliografía NO se pudo verificar y quedó descartada; (2) 337,1 nm y transición C³Πu → B³Πg del segundo sistema positivo del N₂; (3) superradiancia/ASE, espejo trasero opcional; (4) tiempos de pulso (unos ns; vida del nivel superior 40 ns → 1-2 ns con la presión); (5) cronología de la columna 1928-2001 con hueco en los noventa; (6) tramos de autoría corregidos (Ingalls, Stong, Walker 1978-1990, Mims tres columnas en 1990, Carlson 1995-2001). Quedaron sin resolver (4): si el plano original usaba aire o nitrógeno de tubo; la lista de materiales y los valores de tensión/capacidad del plano; el respaldo citable de los sustitutos modernos; y qué «otros proyectos» (microscopio electrónico, reloj de cesio, espectrómetro de masas) salieron efectivamente y en qué números — todo requiere el texto del artículo/CD-ROM.

**Nota para César (Hook, no la toqué):** el Hook dice «julio de 1974»; la fecha confirmada es **junio de 1974**. Hay que corregir «julio» → «junio» en el Hook antes de publicar. El conflicto de fecha/publicación que señalaba el draft queda resuelto: la fuente real es el artículo de Stong en *Scientific American* (junio 1974), no un paper de AJP de 1976.

---

## Borrador de prosa

> ⚠️ **Curiosidad nerd lateral — esto no es ciencia de la computación.**

Hubo una época en que una revista de divulgación científica de circulación masiva publicaba, mes a mes, instrucciones para que construyeras cosas en tu casa. No manualidades. Cosas como un sismómetro, un acelerador de partículas, un espectrómetro. Y, en uno de sus números más recordados, un láser de nitrógeno funcional[^wiki]. El artículo apareció en la columna *The Amateur Scientist* de *Scientific American* de **junio de 1974** (vol. 230, n.º 6, pp. 122-127), firmado por el editor de la columna, C. L. Stong, bajo el título «An unusual kind of gas laser that puts out pulses in the ultraviolet»[^laser74].

No un puntero láser de juguete: un láser pulsado real, con descargas eléctricas de decenas de kilovoltios, un canal entre dos electrodos paralelos y un haz ultravioleta que no ves y que justamente por eso es peligroso. La pregunta que me interesa no es *cómo* se construye. La pregunta es: **¿qué tipo de cultura científica hace que publicar eso sea normal?**

### Por qué el nitrógeno es el láser del pobre

Casi todos los láseres son un problema de ingeniería fina. Necesitás un medio activo bien elegido, dos espejos alineados con precisión ridícula, y algo que bombee energía al medio de manera sostenida. Cualquiera de esas tres cosas, sola, te saca del garaje.

El láser de nitrógeno se escapa de las tres[^samfaq]. El medio activo es nitrógeno gaseoso, que es el 78% del aire que estás respirando ahora [VERIFICAR: si la versión del plano de 1974 usaba directamente aire ambiente o nitrógeno de tubo con la cámara purgada; Sam's Laser FAQ documenta ambas variantes en general (el nitrógeno de soldadura alcanza), pero no tengo el texto del artículo original para saber cuál eligió Stong]. La transición emite en 337,1 nanómetros, en el ultravioleta cercano: es la línea dominante del «segundo sistema positivo» del N₂ (transición C³Πu → B³Πg)[^samfaq][^wikilaser]. Y el detalle que lo vuelve mágico para un amateur: la ganancia es tan brutal que **no necesita cavidad óptica**. El pulso se amplifica en un solo paso a lo largo del canal por superradiancia (emisión espontánea amplificada, ASE); los espejos no hacen falta. Un espejo de un lado ayuda a que salga todo para el mismo lado — es opcional y a lo sumo duplica la salida —, pero no hay alineación crítica que sostener; no hay nada que «desafinar» un martes a la mañana[^samfaq][^wikilaser].

La contrapartida es que el nivel superior de la transición vive poquísimo. Si tu descarga eléctrica tarda demasiado, no hay láser: hay una chispa cara. Toda la ingeniería del aparato se reduce entonces a un solo requisito, y es un requisito de tiempo, no de óptica: **descargar mucha energía muy rápido**, en el orden de los nanosegundos. La vida del nivel superior va de unos 40 ns a baja presión hasta apenas 1-2 ns a presión atmosférica, y el pulso de luz resultante dura sólo unos pocos nanosegundos — típicamente 6 a 8 ns de ancho a media altura, y hasta unos 600-800 ps en las versiones a presión atmosférica[^samfaq][^wikilaser].

Eso explica la forma física del bicho, que es lo primero que llama la atención cuando ves una foto: dos electrodos largos y paralelos, separados por unos milímetros, montados sobre dos placas conductoras grandes separadas por una lámina de dieléctrico. Esas placas *son* el condensador. No es que el condensador esté conectado al láser: la geometría del láser es el condensador, porque cualquier cable entre uno y otro agregaría inductancia y la inductancia es exactamente lo que te arruina el nanosegundo. Es una de esas piezas donde la restricción física dicta el dibujo, y a mí ese tipo de objeto siempre me ganó.

### La columna

*The Amateur Scientist* fue una columna mensual de *Scientific American* que corrió, con un hueco a comienzos de los noventa, desde mayo de 1928 hasta marzo de 2001[^wiki]. Empezó con otro nombre — *The Back Yard Astronomer* — y recién en abril de 1952 pasó a llamarse *The Amateur Scientist*. La firmaron sucesivamente Albert G. Ingalls (1928-1955), C. L. Stong (1955-1977), Jearl Walker (1978-1990), Forrest Mims III (que alcanzó a publicar sólo tres columnas en 1990 antes de que *Scientific American* revocara el encargo) y Shawn Carlson (noviembre de 1995 hasta el cierre, en marzo de 2001)[^wiki].

Los dos nombres del medio dejaron libros que sobrevivieron a la columna. Walker escribió *The Flying Circus of Physics*[^circus], que es un catálogo de preguntas de física sobre el mundo cotidiano y que sigue siendo uno de los mejores libros de divulgación que conozco de leer salteado. Mims escribió *Getting Started in Electronics*[^mims], dibujado a mano, cuadriculado, y que formó a una cantidad de gente que no tiene ninguna proporción con lo humilde que parece el objeto.

> 🕳️ **HUECO — necesita a César:** ¿leíste *Scientific American* o su edición en español (*Investigación y Ciencia*)? ¿Llegaba a tu quiosco / biblioteca / facultad, y en qué años? Si nunca la tuviste en la mano y todo esto lo conociste por el CD-ROM o por internet, decilo también — ese también es el dato.

> 🕳️ **HUECO — necesita a César:** ¿te cruzaste con alguno de estos dos libros, *The Flying Circus of Physics* o *Getting Started in Electronics*? ¿En papel, fotocopiado, bajado? Una línea alcanza.

### Lo que en 1974 estaba en la ferretería

La lista de materiales es la parte que más envejeció, y envejeció de una manera rara: no por obsolescencia tecnológica, sino porque el mundo dejó de tener esas cosas tiradas.

Necesitabas un transformador de neón — de los que alimentaban los carteles luminosos — para levantar la tensión. Condensadores cerámicos de alta tensión. Una lámina de polietileno o de vidrio como dieléctrico. Chapa. Bronce o aluminio para los electrodos. Un pedazo de mesa metálica grande y plana [VERIFICAR: la lista de materiales concreta del plano original y los valores de tensión y capacidad; Sam's Laser FAQ y, si se recupera, el artículo de Bell Jar de Stephen Hansen].

En 2026 nada de eso está en la esquina. Los carteles de neón se murieron y se los comió el LED, así que el transformador que era chatarra ahora es artículo de coleccionista. En cambio aparecieron sustitutos que en 1974 no existían: los módulos elevadores de tensión para tubos de rayos catódicos o para encendedores piezoeléctricos, las fuentes de flyback recicladas de televisores viejos, y directamente los módulos chinos de alta tensión que comprás por menos de lo que sale el envío [VERIFICAR: si Sam's Laser FAQ o alguna fuente de la bibliografía documenta específicamente estos sustitutos modernos, o si esto es sólo conocimiento de foro sin respaldo citable].

Es una inversión curiosa: el proyecto hoy es *más* fácil de alimentar y *más* difícil de conseguir. Y la parte crítica — la geometría de baja inductancia, la separación de los electrodos, el dieléctrico que no perfore — no cambió ni un milímetro, porque la física tampoco.

### La parte que me importa

Acá está el punto del post, y es cultural, no técnico.

Una revista de divulgación masiva publicaba instrucciones que **asumían** que su lector podía soldar, entender un circuito, y manipular treinta mil voltios sin matarse. No lo asumía como un gesto temerario: lo asumía porque era cierto. El lector medio de esa columna tenía taller, o conocía a alguien que tenía taller. La divulgación no era una narración *sobre* la ciencia; era una invitación a *hacer*, con la confianza implícita de que ibas a hacerla bien.

Comparalo con la divulgación científica de hoy, que es buenísima y es otra cosa completamente distinta. Hoy la divulgación te *explica* el láser: te cuenta la historia del láser, te muestra una animación preciosa de la emisión estimulada, te entrevista a alguien que trabaja con láseres. Vos mirás. Es un cambio de verbo — de construir a entender — y no es gratis.

No quiero ser injusto ni nostálgico barato. Hay razones legítimas para el cambio: la responsabilidad civil existe, la audiencia se masificó muchísimo más allá del que tiene taller, y varios de aquellos proyectos eran objetivamente peligrosos. Y hay una contracara enorme del lado bueno: el mundo maker de hoy — Arduino, impresión 3D, los foros, el propio Sam's Laser FAQ[^samfaq] que sigue vivo — es más grande y más accesible de lo que fue jamás la comunidad de *The Amateur Scientist*. Lo que se perdió no es la posibilidad de construir. Lo que se perdió es que construir estuviera **en la corriente principal**, en la revista que compraba cualquiera, sin necesidad de haberse identificado antes como «alguien que construye».

Esa distinción me parece la más importante que tiene el tema. Hoy el que va a construir un láser de nitrógeno ya sabía que quería construir un láser de nitrógeno. En 1974 te lo encontrabas en la página 112 sin haberlo buscado, y ahí se te abría una puerta que no sabías que existía. La divulgación de entonces reclutaba. La de ahora, en el mejor de los casos, atiende a los ya reclutados.

> 🕳️ **HUECO — necesita a César:** ¿alguna vez armaste algo de alta tensión — bobina de Tesla, encendido de auto, fuente de un televisor, flyback? ¿Te pegó alguna vez en serio?

> 🕳️ **HUECO — necesita a César:** ¿cuál fue tu «página 112»? El artículo, revista o libro que te abrió una puerta que no estabas buscando. Es el paralelo local de la anécdota y engancha con [[I-02]].

### Los otros proyectos

La columna tiene una lista de proyectos legendarios que circula entre nostálgicos: un microscopio electrónico casero, un espectrómetro de masas amateur, y — esto es lo que siempre me hizo levantar las cejas — un reloj atómico de cesio de fabricación hogareña [VERIFICAR: cuáles de estos proyectos salieron efectivamente en *The Amateur Scientist* y en qué números. Ninguna de las fuentes listadas lo respalda todavía; el outline los menciona pero sin cita. El CD-ROM 4.0 es la manera de chequearlo].

> 🕳️ **HUECO — necesita a César:** de los proyectos de la columna, ¿cuál te habría gustado construir y nunca construiste? Ésa es la frase que le da alma a esta sección; sin ella queda como una enumeración.

### ¿Lo armarías?

El plano sigue estando. La física no caducó. Los materiales, con sustituciones, se consiguen. El conocimiento comunitario que hacía falta está mejor documentado que nunca, y encima gratis[^samfaq].

Lo único que cambió es que hoy alguien tiene que decidir buscarlo. Y para decidir buscarlo, tenés que saber primero que se puede.

> 🕳️ **HUECO — necesita a César:** el cierre es tuyo. ¿Lo armarías hoy? ¿Y lo recomendás? El outline propone «sí, y sólo si entendés alta tensión y querés vivir», pero necesito tu versión — y si tenés lugar donde armarlo, decilo, porque es la mitad graciosa de la respuesta.

Un párrafo de advertencia que va en serio y no es literario: treinta kilovoltios te matan. Un condensador cargado te sigue matando después de que desenchufaste todo. Y el haz de 337 nm es invisible, lo cual significa que tu ojo no tiene reflejo de parpadeo para defenderse: el daño ocurre sin que te enteres. Si algo de esto te suena a detalle, el proyecto no es para vos, y eso está perfectamente bien.

La otra opción, la que estoy tomando yo al escribir esto, es admirar el objeto por lo que dice de su época. Un aparato cuya forma la dicta el nanosegundo. Publicado en una revista de quiosco. Para que lo hiciera cualquiera.

[^wiki]: [*The Amateur Scientist* — Wikipedia](https://en.wikipedia.org/wiki/The_Amateur_Scientist). Ver también el [archivo oficial de la columna en *Scientific American*](https://www.scientificamerican.com/section/the-amateur-scientist/) y el [CD-ROM *Scientific American's «The Amateur Scientist»: The Complete 20th Century Collection*](https://archive.org/details/Scientific_American_The_Amateur_Scientist_Tinkers_Guild_2000) (ed. Carlson y Greaves, Tinker's Guild, 2000), que recopila unos 72 años de columna.
[^samfaq]: Sam Goldwasser, [*Sam's Laser FAQ — Home-Built Nitrogen (N2) Laser*](https://www.repairfaq.org/sam/lasercn2.htm). Es la referencia técnica más completa que existe para construcción amateur de estos aparatos.
[^laser74]: C. L. Stong, «An unusual kind of gas laser that puts out pulses in the ultraviolet», *The Amateur Scientist*, [*Scientific American* vol. 230, n.º 6 (junio de 1974), pp. 122-127](https://www.scientificamerican.com/article/the-amateur-scientist-1974-06/). Reeditado en *Light and Its Uses* (W. H. Freeman, 1980).
[^wikilaser]: [*Nitrogen laser* — Wikipedia](https://en.wikipedia.org/wiki/Nitrogen_laser): 337,1 nm, segundo sistema positivo del N₂ (transición C³Πu → B³Πg), transición autoterminante, superradiancia y diseño TEA a presión atmosférica.
[^circus]: Jearl Walker, *The Flying Circus of Physics*, Wiley, 1977 (2ª edición 2006). Sitio del libro: [flyingcircusofphysics.com](https://www.flyingcircusofphysics.com/).
[^mims]: Forrest Mims, *Getting Started in Electronics*, Master Publishing, 1983. [Copia en Internet Archive](https://archive.org/details/Getting_Started_in_Electronics).

