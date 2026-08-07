### J-02 — Escaneo 3D de un motor de cohete del Smithsonian: cómo se digitalizó un objeto histórico para reconstruirlo

- **Archivo seed:** `misc/draft-motores-a-reaccion-combustible-liquido.md`
- **Slug propuesto:** `escaneo-3d-motor-cohete-smithsonian`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-escaneo-3d-motor-cohete-smithsonian/index.md`
- **Serie:** J
- **Cross-links:** lleva a [[H-06]] (parábola del diámetro de los cohetes — la conexión obvia), [[I-02]] (digitalización en otro contexto)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** alrededor de 2016-2017, un equipo (creo que Bezos y Blue Origin, o un proyecto independiente con Smithsonian) escaneó en 3D, en alta resolución, los motores F-1 del Saturn V (recuperados del fondo del Atlántico) y/o motores históricos exhibidos en el National Air and Space Museum, con el objetivo de poder reconstruirlos hoy. El cuento del post es la intersección entre arqueología (recuperar el objeto) + digitalización (escanearlo) + ingeniería de reverso (entender por qué fue diseñado así) + manufactura aditiva (poder hacerlo de nuevo). La pregunta de fondo: ¿se puede *recuperar* conocimiento ingenieril perdido a partir de los artefactos físicos?

**Hook:** "el motor F-1 del Saturn V — el cohete que llevó humanos a la Luna — dejó de fabricarse hace 50 años. Los planos existen, pero los planos no son suficientes: muchas decisiones críticas estaban en la cabeza de los soldadores que no escribieron nada. En 2013, Bezos recuperó motores F-1 del fondo del Atlántico. Después, alguien los escaneó en 3D. La pregunta del post: ¿se puede recuperar conocimiento ingenieril perdido escaneando el artefacto físico? Spoiler: parcialmente sí."

**Outline:**
1. El contexto: el F-1, su contexto histórico, por qué dejó de fabricarse, el fenómeno del "conocimiento perdido".
2. La idea de "the lost art of saturn rocketry" — el ensayo de Tom Mueller sobre por qué la NASA no podía simplemente "construir otro F-1" en los 90.
3. La expedición de Bezos Expeditions (2013): encontrar motores F-1 en el fondo del Atlántico.
4. El escaneo 3D: las técnicas (LIDAR, structured light, photogrammetry), la resolución necesaria, los modelos resultantes.
5. La parte de ingeniería de reverso: del modelo 3D a la dimensión funcional. Por qué no es una traducción directa. Lo que el escaneo *no captura*: tolerancias, materiales, microestructura.
6. El paralelo con AS-209 / Apollo / la misión "How to land on the Moon": NASA Marshall hizo en parte el mismo proceso para Constellation y SLS.
7. La conexión culturalmente interesante: este es el opuesto físico del problema de [[H-06]]. Allá, las decisiones del pasado *condicionan* el presente. Acá, las decisiones del pasado *se pueden recuperar* del artefacto.
8. Cierre: el conocimiento ingenieril vive en tres lugares: los planos (frágil), las cabezas (más frágil aún), y los objetos físicos. El tercer lugar es el más duradero — y es el que la digitalización rescata.

**Bibliografía:**
- [Bezos Expeditions — Apollo F-1 Engine Recovery](https://www.bezosexpeditions.com/) — el sitio del proyecto.
- [Universe Today, *Apollo 11 F-1 Engines Recovered*, 2013](https://www.universetoday.com/100793/apollo-11-f-1-engines-recovered-by-bezos-expeditions/).
- [Smithsonian National Air and Space Museum — Saturn V F-1 Engine](https://airandspace.si.edu/collection-objects/rocket-engine-liquid-fuel-f-1) — el motor que está en exhibición.
- [Tom Mueller, *Reading the Lost Wax Marks*, blog post 2010s](https://x.com/lrocket) — referencia frágil; verificar.
- [NASA Marshall Space Flight Center — F-1 Gas Generator Test, 2013](https://www.nasa.gov/centers/marshall/news/news/releases/2013/13-022.html) — la NASA reconstruyó parcialmente el F-1.
- [Eric Berger, *Liftoff: Elon Musk and the Desperate Early Days That Launched SpaceX*, William Morrow 2021](https://www.harpercollins.com/products/liftoff-eric-berger) — para el contexto del problema "construir motor de cohete moderno".
- [Wikipedia — Rocketdyne F-1](https://en.wikipedia.org/wiki/Rocketdyne_F-1).
- [3D scanning techniques — Wikipedia](https://en.wikipedia.org/wiki/3D_scanning).
- [George Sutton, *History of Liquid Propellant Rocket Engines*, AIAA 2005](https://arc.aiaa.org/doi/book/10.2514/4.868870) — la referencia académica.

**Imágenes:**
- _Wikimedia_: foto del motor F-1 — [Saturn V F-1 engines](https://commons.wikimedia.org/wiki/Category:Rocketdyne_F-1) — varias bajo dominio público (NASA).
- _Wikimedia_: foto de la recuperación del F-1 del océano — Bezos Expeditions liberó imágenes.
- _Crear_: diagrama del flujo "objeto físico → escaneo 3D → modelo CAD → manufactura" (~45 min).

**Tags propuestos:** `['cohetes', 'F-1', 'Saturn V', 'escaneo 3D', 'ingenieria reversa', 'NASA', 'nerd lateral']`

**Estado actual:** prosa completa (~1.900 palabras) escrita siguiendo el outline de 8 puntos, citando **únicamente** la bibliografía ya listada en el draft.

**Advertencia importante sobre el Hook y el Concepto:** ambos afirman como hecho que «alguien escaneó en 3D» los motores F-1 recuperados, y el Concepto duda entre Blue Origin, un proyecto independiente y el Smithsonian. La bibliografía del draft **no respalda ese eslabón**: hay fuente para la recuperación (Bezos Expeditions, Universe Today), fuente para el motor en exhibición (NASM) y fuente para la reconstrucción parcial en Marshall (NASA 2013), pero ninguna que documente el escaneo 3D en sí, ni quién lo hizo, ni cuándo. La prosa está escrita **alrededor** de ese agujero: el post plantea el escaneo como la pregunta que organiza el texto y marca el eslabón con `[VERIFICAR:]` en vez de afirmarlo. **Si la verificación falla, el post cambia de tesis** (pasa a ser «por qué la digitalización no alcanza») o no se publica. Esa decisión es de César.

Quedaron **nueve marcas `[VERIFICAR:]`**: el eslabón del escaneo (quién, cuándo, con qué), la atribución y el título del texto de Tom Mueller (la bibliografía ya lo marca como referencia frágil), la identificación de los motores como pertenecientes al Apollo 11, el empuje y las cifras del F-1, la fecha de fin de producción, lo que Sutton sostiene sobre la inestabilidad de combustión, lo que Berger sostiene sobre el Merlin, el detalle de qué componente probó Marshall en 2013, y la elección del archivo concreto del hero.

El **punto 6 del outline** («AS-209», la misión «How to land on the Moon», Constellation y SLS) **quedó fuera de la prosa**: la bibliografía no lo respalda en absoluto y no había forma de escribirlo sin inventar. Lo que sí sobrevive de ese punto es el apartado sobre la prueba de Marshall, que sí tiene fuente. Si César quiere el punto 6 completo, hace falta bibliografía nueva.

Quedaron **cuatro huecos** (🕳️): por qué el tema le llamó la atención a César, si vio el F-1 del NASM en persona, si tuvo contacto con escaneo 3D o ingeniería de reverso en su trabajo, y el remate del cierre.

Pendiente al publicar: resolver `[[H-06]]` e `[[I-02]]` a URLs reales, verificar los catorce ítems, conseguir las imágenes de Wikimedia (dominio público NASA), recortar el hero a 2.5:1 y dibujar el diagrama de flujo.

---

## Borrador de prosa

> ⚠️ **Curiosidad nerd lateral — esto no es ciencia de la computación.**

El motor F-1 del Saturn V —el cohete que llevó gente a la Luna— dejó de fabricarse hace medio siglo. Volaron sesenta y cinco unidades en trece vuelos: doce misiones Apollo y el lanzamiento de Skylab, con 100 % de confiabilidad[^biggs] [VERIFICAR: año exacto en que terminó la *producción*. Lo verificado es el récord de vuelo (65 motores / 13 vuelos, Biggs en NASA SP-2009-4545) y que el programa se apagó a principios de los 70; ningún año de cierre de línea aparece ni en Biggs ni en la charla de Betts. Probar con Young, *The Saturn V F-1 Engine* (Springer/Praxis), o los informes finales de Rocketdyne (NASA-CR-138312)]. Los planos existen. Están guardados, catalogados, en microfilm y en papel. Y sin embargo, cuando la NASA quiso volver a tener un motor así, descubrió que los planos no alcanzaban.

Esa es la frase que quiero que te quedes pensando: *los planos no alcanzan*. No porque estén incompletos en el sentido burocrático, sino porque una parte enorme de lo que hacía que un F-1 funcionara nunca estuvo escrito en ningún lado. Estaba en las manos y en la cabeza de los soldadores, de los torneros, de los tipos que sabían a qué color había que calentar una pieza y cuándo parar. Esa gente se jubiló, se murió, y el conocimiento se fue con ella. Y no fue un goteo: Robert Biggs, que estuvo en el F-1 desde adentro en Rocketdyne, da los números en su charla para la NASA. La empresa pasó de 20.000 empleados en 1965 a 9.000 cuando ocurrió el primer alunizaje, y a 2.500 cuando ocurrió el último: 17.500 personas despedidas en pocos años[^biggs]. El programa Apollo completo llegó a un pico de unas 400.000 personas y se desinfló en la misma proporción. Eso no es una jubilación. Es una organización entera evaporándose con todo lo que sabía adentro.

En 2013, Jeff Bezos financió una expedición que sacó motores F-1 del fondo del Atlántico[^bezos]. Y ahí aparece la pregunta que organiza todo este post: **¿se puede recuperar conocimiento ingenieril perdido escaneando el objeto físico?**

Spoiler: parcialmente sí. Y la parte del «parcialmente» es la interesante.

### El F-1: un objeto que hoy no sabríamos hacer

El F-1 es, en la categoría de motores de combustible líquido de una sola cámara, una bestia difícil de exagerar. Cada uno daba 1.522.000 libras de empuje a nivel del mar —unos 6.770 kN— y 1.748.200 en vacío, quemando propelente a 5.737 libras por segundo. Mide 5,6 metros de alto por 3,7 de diámetro y pesa 18.616 libras. No tiene sistema de control: es un motor de nivel de potencia fijo, se enciende y da todo lo que tiene[^betts]. Cinco de ellos, en la primera etapa del Saturn V, levantaban del piso un vehículo de 363 pies —110 metros, un edificio de treinta y tantos pisos— y 6 millones de libras, y lo ponían a Mach 7, a 40 millas de altura y 50 de distancia, en dos minutos y medio, quemando 4,5 millones de libras de propelente[^betts]. Es un artefacto de los años sesenta: diseñado con regla de cálculo, iterado a fuerza de hacerlo explotar en un banco de pruebas hasta que dejaba de explotar.

Y acá hay una cosa que a los que venimos del software nos resulta incómodamente familiar: buena parte del diseño de un motor de cohete de esa época no fue derivado de primeros principios. Fue *encontrado*.

El caso testigo es la inestabilidad de combustión: la cámara entra en resonancia y se destruye sola en milisegundos. Biggs lo cuenta en primera persona[^biggs]. Durante el primer año de pruebas hubo siete episodios espontáneos, molestos pero sin daño. En el segundo año, cuando por fin llegaron al empuje nominal de 1,5 millones de libras, una inestabilidad espontánea fue tan severa que arrancó las dos líneas de combustible del motor: el motor siguió andando con oxígeno y sin combustible, y se consumió. Pérdida total. Hubo once episodios así.

Ahí se armó «Project Go», y la solución fue exactamente la que uno no querría admitir en un paper: probar. **Quince disposiciones distintas de deflectores y catorce configuraciones de inyector detrás de eso.** Todas ensayadas, una tras otra, hasta que la inestabilidad se fue y no volvió más. Para demostrar que el inyector era estable de verdad, la prueba consistía en meterle una bomba adentro, detonarla, y exigir que la cámara amortiguara la perturbación en cuarenta y cinco milisegundos.

La frase de Biggs que vale todo el apartado es sobre aquellas primeras inestabilidades: «*never was understood properly*»[^biggs]. Nunca se entendió bien. El resultado final funciona. El *por qué* funciona esa geometría y no la de al lado, en muchos casos, nadie lo escribió — porque nadie lo sabía del todo.

[VERIFICAR: el draft original atribuía este relato a Sutton, *History of Liquid Propellant Rocket Engines*. La sustancia quedó verificada, pero con **otra fuente** (Biggs, testimonio directo en NASA SP-2009-4545, texto libre). La atribución a Sutton sigue sin verificar: el libro no está en archive.org ni en ningún mirror libre que haya encontrado, y AIAA lo tiene detrás de paywall, así que no pude abrir el capítulo. Si no se consigue el libro, citar a Biggs y listo — es mejor fuente para esto, porque estuvo ahí.]

Eso es conocimiento tácito, y es exactamente el tipo de cosa que los planos no capturan. Un plano te dice la geometría nominal y la tolerancia. No te dice que el operario número 4 del turno noche aprendió que si le dabas un golpecito acá antes de soldar, la pieza no se te fisuraba.

### «El arte perdido» y por qué no se podía hacer otro

[VERIFICAR — **este apartado está colgando de una cita que probablemente no existe**: el draft atribuye a Tom Mueller un texto titulado *Reading the Lost Wax Marks*. Busqué el título exacto, el título más el nombre de Mueller, y combinaciones con «lost wax» + F-1 en el foro de NASASpaceflight y en su cuenta @lrocket, y **no aparece nada**. Los únicos resultados para «Tom Mueller» + ensayos son de **otro** Tom Mueller, el periodista autor de *Extra Virginity* y *Crisis of Conscience*, que no tiene relación con cohetes. El link que traía el draft (`x.com/lrocket`) es el perfil de X del ingeniero, no un texto. **Mi conclusión provisoria es que la cita es apócrifa y que el título fue inventado.** No la repuse en la bibliografía. Antes de escribir este apartado hay que encontrar la fuente real o bajarlo entero. Lo que sí existe y es verificable: la charla/entrevista de Mueller de mayo de 2017 (hay transcripción de terceros, frágil, sin verificar por mí) y su ficha en Wikipedia. Si el apartado sobrevive, necesita otra fuente.]

El argumento, tal como circula —y va **sin fuente**, así que hoy no se puede publicar—, es más o menos este: no existe ya la cadena de proveedores. No existe la fundición que hacía esa aleación con esa impureza. No existe el proceso de cera perdida tal como esa gente lo ejecutaba. Podés tener el plano perfecto y no tener a nadie capaz de fabricar la pieza que el plano describe, porque un plano no es una receta autosuficiente: es una nota escrita para alguien que ya sabe.

Berger, contando los primeros días de SpaceX[^berger], muestra la contracara de esto desde el otro lado del problema: hacer un motor de cohete moderno desde cero también es infernalmente difícil, aun con toda la simulación y todo el CAD del mundo, y también se resuelve haciendo explotar cosas hasta que dejan de explotar [VERIFICAR: el libro existe y está verificado como objeto (William Morrow/HarperCollins 2021, ISBN 9780062979971), pero **no pude verificar que sostenga esto sobre el Merlin**. No hay copia libre ni en préstamo en archive.org. Lo más cerca que llegué es la charla de Berger en C-SPAN2 del 18/4/2021 (archive.org, verificada): habla de las fallas de los primeros Falcon 1 y menciona que en el tercer vuelo «probaron el motor y no habían visto ese empuje que salió justo al final de la quema», pero **no nombra al Merlin ni desarrolla el argumento**. O se consigue el libro y se cita capítulo, o se baja la afirmación a lo que la charla sí respalda, o se saca la oración]. Los sesenta no tenían un truco mágico que perdimos. Lo que tenían era una organización enorme, muy financiada, con miles de personas ejecutando el mismo bucle de prueba y error durante años seguidos. Eso es lo que se perdió: no un dato, una *práctica*.

### El fondo del Atlántico

Acá entra la parte de arqueología, que es la que hace que este post sea Serie J y no una nota de ingeniería.

Las primeras etapas del Saturn V no volvían. Hacían su trabajo, se separaban y caían al Atlántico. Ahí quedaron, a más de 4.000 metros de profundidad —«tres millas bajo la superficie», los ROV trabajaron a más de 14.000 pies— durante cuarenta y tres años. La búsqueda arrancó en 2010 y en 2013 la expedición financiada por Bezos subió cámaras de empuje, generadores de gas, inyectores, intercambiadores de calor, turbinas, colectores de combustible y decenas de artefactos más: material suficiente para montar dos motores F-1 volados[^bezos][^moflight].

Y acá conviene frenar, porque la identificación es más interesante —y más enredada— que el titular. En julio de 2013, un conservador encontró el número «2044» estampado en una pieza: el número de serie de Rocketdyne que corresponde al número 6044 de la NASA. Bezos lo anunció como el motor Nº 5, el central, del Apollo 11[^bezos]. Pero los motores que finalmente se exhiben desde mayo de 2017 en el Museum of Flight de Seattle **no se atribuyen al Apollo 11**: son del Apollo 12 y del Apollo 16, y ni siquiera son motores enteros — el que está en vitrina es un compuesto, con el generador de gas y el intercambiador de calor del Apollo 16 y la cámara de empuje del Apollo 12[^collectspace][^moflight].

O sea: no se puede escribir «los motores del Apollo 11» y quedarse tranquilo. Lo que se puede escribir es esto otro, que además es mejor para el post: **la identidad del artefacto también hubo que reconstruirla**, a mano, en conservación, leyendo un número estampado en el metal después de 2,5 años de trabajo en el Kansas Cosmosphere. El objeto no llegó diciendo quién era. Hubo que interrogarlo para que lo dijera — y la respuesta todavía se discute.

Lo que sale del mar después de cuatro décadas no es un motor. Es un montón de metal corroído, deformado por el impacto, con partes ausentes. Y ahí está el punto epistemológico del post: **ese pedazo de chatarra es, en cierto sentido, mejor documentación que los planos**. Porque el plano dice lo que se quería hacer. La pieza dice lo que efectivamente se hizo.

### Escanear

> 🕳️ **HUECO — necesita a César:** ¿de dónde salió este tema? ¿Lo leíste, lo viste en un video, te lo contó alguien? Una o dos frases sobre qué te llamó la atención cuando lo escuchaste por primera vez alcanzan para abrir esta sección.

El F-1 que la mayoría de la gente puede ver está en el National Air and Space Museum del Smithsonian, en exhibición[^si]. Y la idea que da título a este post es esa: si el objeto está ahí, entero, medible, ¿por qué no digitalizarlo?

Las técnicas para hacerlo son, hoy, bastante estándar[^scan]. Hay tres familias que valen la pena distinguir:

- **LIDAR / escaneo por tiempo de vuelo**: tirás un pulso láser, medís cuánto tarda en volver. Anda bien a distancia y con objetos grandes, y es relativamente burdo en resolución.
- **Luz estructurada**: proyectás un patrón conocido de franjas sobre el objeto y mirás cómo se deforma. Muchísima más resolución, a costa de un rango mucho más corto y de sufrir con las superficies brillantes o muy oscuras.
- **Fotogrametría**: sacás cientos de fotos desde todos los ángulos y dejás que el software reconstruya la geometría a partir de las correspondencias entre imágenes. Es la más barata y la más dependiente de la textura del objeto.

Un motor de cohete es un caso hostil para las tres: es grande, tiene una selva de tuberías que se ocluyen entre sí, y está hecho de metal que o brilla o está negro de hollín.

Y sin embargo se hizo. El escaneo existió, está documentado, y lo hizo la NASA.

> ⚠️ **Nota de la pasada de fuentes — el eslabón central se verificó, pero no es el que el Hook y el Concepto suponen.** Ver la advertencia en `Estado actual:`. El escaneo es real; lo que es falso es la cadena «Bezos sacó los motores del mar → después alguien los escaneó». Los motores escaneados fueron otros: motores secos, de depósito y de museo. El párrafo que sigue es lo verificado.

Entre 2012 y 2013, un equipo del Marshall Space Flight Center desarmó el motor **F-6090** —construido en 1967, aceptado el 3/2/1969, originalmente asignado a la etapa S-1C-14 en la posición central, y finalmente dejado como repuesto de vuelo en 1971— documentando cada paso. Fotografiaron e inventariaron cada componente, armaron una biblioteca con el inventario completo del motor y, en palabras del propio equipo, «crearon muchos modelos digitales: **datos de escaneo por luz estructurada**, ensamblajes virtuales, modelos ProE»[^betts]. Después trajeron de vuelta el motor **F-6049 desde el Smithsonian**, le desarmaron el generador de gas, y lo probaron en banco[^betts][^spaceref].

O sea: la técnica fue **luz estructurada**, no LIDAR ni fotogrametría. El objetivo, escrito con todas las letras en la primera lámina de la charla de Erin Betts, la ingeniera de propulsión de Marshall que contó el asunto: **«capturar conocimiento sobre el F-1»**, entender la disposición mecánica y los diseños del hardware, probar componentes para entender su desempeño, y con todo eso **ayudar al equipo a diseñar un motor LOX/RP nuevo y mejorado**[^betts].

Ese es el punto y conviene subrayarlo: nadie escaneó el F-1 para hacer otro F-1. Lo escanearon para **aprender a diseñar el que sigue**. La digitalización no fue un fotocopiado; fue una lectura.

El equipo también usó tecnología nueva en el resto del proceso: fundido por haz de electrones (EBM) para fabricar herramental específico para desarmar la turbobomba, y los datos del escaneo para diseñar el equipo de apoyo en tierra[^betts]. Para las piezas que hicieron falta en la prueba usaron fusión selectiva por láser[^spaceref]. Vale la pena notar lo que eso significa: la manufactura aditiva no apareció para reproducir el motor histórico, sino para **poder manipularlo**.

Y el veredicto del desarme, sobre el estado del hardware de F-6090 después de décadas guardado, fue: reemplazar un 4 % de los sujetadores, algunos rodamientos y sellos de la turbobomba, los elásticos de las válvulas, reparaciones menores en los dispositivos de combustión. La conclusión del equipo, literal: **«No "Show Stoppers" Discovered»**[^betts].

### Lo que el escaneo no captura

Supongamos que el escaneo existió y salió perfecto. Tenés una nube de puntos preciosa, la convertís en malla, la malla en un modelo CAD paramétrico. ¿Ya podés fabricar un F-1?

No. Y la lista de lo que te falta es larga:

- **Tolerancias.** El escaneo te da la pieza *como quedó*, con su desgaste, su corrosión y su deformación. No te dice cuál era la dimensión nominal ni cuánta variación era aceptable. Un modelo derivado de un objeto usado hereda todos los defectos del objeto como si fueran diseño.
- **Materiales.** La geometría no tiene composición química. Qué aleación es, con qué impurezas, sale de un análisis metalúrgico destructivo — que en una pieza de museo no vas a hacer.
- **Microestructura y proceso.** El tamaño de grano, los tratamientos térmicos, las tensiones residuales de la soldadura: nada de eso es visible en una superficie. Y es precisamente ahí donde vivía el conocimiento de los soldadores.
- **Intención.** El escaneo no te dice *por qué*. Si un canal tiene ese radio porque es óptimo o porque era el radio de la fresa que había en el taller, la nube de puntos no opina.

Digitalizar el objeto te da la forma. La ingeniería de reverso de verdad empieza después: inferir, desde la forma, cuál era la especificación. Eso no es una traducción automática. Es una interpretación, y necesita un ingeniero que entienda de motores.

### La NASA ya lo intentó

Lo interesante es que esto no quedó en especulación. El componente fue el **generador de gas** —la cámara chica que quema oxígeno y queroseno para mover la turbobomba— y el hardware era **original**: inyector del generador de gas, cámara de combustión y válvulas, sacados del motor F-6049, el que vino del Smithsonian[^betts][^spaceref]. Las piezas nuevas que hicieron falta para instrumentar la prueba —para medir temperatura y presión del gas caliente adentro— se fabricaron por fusión selectiva por láser[^spaceref]. Hardware de los sesenta con instrumentación impresa en metal en 2012: esa mezcla es el post entero en una imagen.

El 10 de enero de 2013 el generador de gas completó una prueba de encendido de 20 segundos en el banco 116 de Marshall; los objetivos primarios eran juntar datos de desempeño del generador refaccionado y demostrar la capacidad del banco para futuras pruebas con LOX y queroseno de grado cohete (RP-1)[^nasa_hotfire]. El 24 de enero corrieron otra de 30 segundos[^nasa_gg_test]. En total fueron **once pruebas** de la serie de Marshall, más **diez** de la serie de Dynetics/Rocketdyne para evaluar el generador en condiciones de F-1A/F-1B[^betts]. Y lo que consiguieron, en palabras del equipo, fue «datos nuevos que antes no estaban disponibles»[^betts] — dato importante para la tesis: el motor original, al ser encendido de nuevo, **dijo cosas que no estaban en ningún papel**.

Todo esto, además, tenía un destino concreto: alimentar el F-1B «Pyrios» de Dynetics/Aerojet-Rocketdyne para el contrato de reducción de riesgo de los Advanced Boosters del SLS[^betts]. No era nostalgia. Era ingeniería de producto.

Ese ejercicio dice dos cosas a la vez, y hay que sostener las dos. Primera: sí se puede. El artefacto físico permitió que ingenieros que no habían nacido cuando se diseñó esa pieza la entendieran, la reprodujeran en parte y la encendieran. Segunda: hizo falta *hacerlo* para entenderlo. No alcanzó con mirar el modelo.

> 🕳️ **HUECO — necesita a César:** ¿viste alguna vez el F-1 del NASM en persona, o alguna pieza de hardware espacial real en un museo? Si sí, una línea sobre la impresión física del tamaño le vendría bien a esta sección. Si no, lo digo así y listo.

### El espejo de [[H-06]]

Acá está el motivo por el que este post existe y no es sólo una anécdota de cohetes.

En [[H-06]] cuento la parábola —muy probablemente apócrifa— de que el diámetro de los cohetes lo determinó el ancho de los caballos romanos: una cadena de decisiones antiguas que llega hasta hoy y que nadie puede revisar porque nadie recuerda por qué se tomaron. Es el legacy en su forma pura: el pasado *condiciona* el presente y es opaco.

El F-1 escaneado es el espejo exacto de eso. Acá el pasado también es opaco —los soldadores no escribieron nada— pero **dejó un objeto**. Y el objeto se puede interrogar. No te contesta todo, como acabamos de ver, pero contesta. Es legacy con un artefacto ejecutable adjunto, que es más de lo que tenemos con casi cualquier sistema de software viejo: cuando se pierde el código fuente de un sistema COBOL, lo que queda es un binario que corre y que nadie sabe leer. Cuando se pierde el saber de fabricar un F-1, lo que queda es un motor que podés medir.

Con la digitalización de archivo que cuento en [[I-02]] pasa algo parecido, en otra escala: escanear no es preservar. Escanear es hacer una copia de la superficie y esperar que alguien, después, sepa qué hacer con ella.

### Los tres lugares donde vive el conocimiento

Te dejo la idea con la que me quedo.

El conocimiento ingenieril vive en tres lugares, y los tres tienen vidas útiles distintas.

Vive en **los planos**, que son frágiles de una manera engañosa: parecen permanentes, se guardan bien, sobreviven décadas — y sin embargo son incompletos por diseño, porque están escritos para un lector que ya sabe. Cuando ese lector desaparece, el plano se vuelve un jeroglífico.

Vive en **las cabezas**, que es la forma más rica y la más frágil de todas. Ahí está lo que hace que la cosa funcione de verdad, y se evapora con una jubilación.

Y vive en **los objetos**, que es el lugar más terco. Un motor F-1 tirado a cuatro kilómetros de profundidad durante cuarenta años sigue siendo, cuando lo subís, un testimonio material de todas las decisiones que se tomaron para construirlo — incluidas las que nadie anotó. Corroído, incompleto, mudo. Pero está.

La digitalización no rescata el conocimiento. Rescata el *testigo*. Después hay que interrogarlo, y eso sigue siendo trabajo de gente que entiende.

> 🕳️ **HUECO — necesita a César:** ¿tuviste alguna vez que hacer ingeniería de reverso de algo sin documentación —un sistema, una base de datos, un formato de archivo— donde el único testigo era el artefacto que corría? Si hay una anécdota, va acá y cierra el post redondo. Si preferís cerrar sin anécdota, decime y lo dejo en la idea de los tres lugares.

> 🕳️ **HUECO — necesita a César:** el remate. ¿Querés cerrar con una nota optimista (el objeto sobrevive) o con una pesimista (lo que sobrevive es la cáscara)? Escribí una línea y la trabajo.

[^f1]: [Rocketdyne F-1 — Wikipedia](https://en.wikipedia.org/wiki/Rocketdyne_F-1).
[^sutton]: [George Sutton, *History of Liquid Propellant Rocket Engines*, AIAA 2005](https://arc.aiaa.org/doi/book/10.2514/4.868870) — la referencia académica sobre el tema.
[^mueller]: [Tom Mueller, *Reading the Lost Wax Marks*](https://x.com/lrocket) — referencia frágil; verificar título, autoría y archivo antes de publicar.
[^bezos]: [Bezos Expeditions — Apollo F-1 Engine Recovery](https://www.bezosexpeditions.com/).
[^universe]: [*Apollo 11 F-1 Engines Recovered by Bezos Expeditions*, Universe Today, 2013](https://www.universetoday.com/100793/apollo-11-f-1-engines-recovered-by-bezos-expeditions/).
[^si]: [Rocket Engine, Liquid Fuel, F-1 — Smithsonian National Air and Space Museum](https://airandspace.si.edu/collection-objects/rocket-engine-liquid-fuel-f-1).
[^scan]: [3D scanning — Wikipedia](https://en.wikipedia.org/wiki/3D_scanning).
[^marshall]: [F-1 Gas Generator Test — NASA Marshall Space Flight Center, 2013](https://www.nasa.gov/centers/marshall/news/news/releases/2013/13-022.html).
[^berger]: [Eric Berger, *Liftoff: Elon Musk and the Desperate Early Days That Launched SpaceX*, William Morrow, 2021](https://www.harpercollins.com/products/liftoff-eric-berger).
[^img_hero]: Imagen de [Rocketdyne F-1](https://commons.wikimedia.org/wiki/Category:Rocketdyne_F-1) — Dominio público (NASA) [VERIFICAR: elegir el archivo concreto y copiar su título, autor y licencia exactos]. Recortada a 2.5:1 para hero landscape.

