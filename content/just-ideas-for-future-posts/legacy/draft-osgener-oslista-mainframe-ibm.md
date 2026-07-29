### H-14 — OSGENER y OSLISTA: desde fines de los '70 en un mainframe de IBM

- **Archivo seed:** ninguno — nace del proyecto [`CesarBallardini/osgener-oslista`](https://github.com/CesarBallardini/osgener-oslista) (2026-07-27)
- **Slug propuesto:** `osgener-oslista-mainframe-ibm`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-osgener-oslista-mainframe-ibm/index.md`
- **Serie:** H — arqueología legacy; es el caso más extremo de la serie (no se migra un sistema: se reimplementa una *utilería del sistema operativo* a partir de su manual)
- **Cross-links:** hermano técnico de [[H-04]] (migrar COBOL de mainframe a GnuCOBOL) y de [[A1-09]] (GnuCOBOL-lab, RM/COBOL-85); contexto de ejecución en [[H-10]] (MVS 3.8j sobre Hercules), [[H-11]] (s390x emulado) y [[H-12]] (`prtspool` → PDF); contraste con [[H-02]] (el binario que sobrevivió sin recompilar); el ángulo «memoria del cómputo estatal argentino» conecta con la Serie I ([[I-04]], [[I-05]], [[I-14]])
- **Idioma:** es (candidato fuerte a versión en inglés: el README del repo ya está en inglés y el tema tiene audiencia en la comunidad mainframe / GnuCOBOL)
- **Madurez:** outline completo — el material técnico está todo escrito y verificado en el repo; falta la parte biográfica, que sólo la tiene César
- **Length target:** long (2500-3500 palabras)

**Concepto:** en la Argentina de los '70, el centro de cómputos del Estado decidió escribir sus propias utilerías para depender menos de IBM. De ese esfuerzo salieron **OSGENER** y **OSLISTA**: dos programas genéricos manejados por tarjetas de control de 80 columnas que hacían, sin escribir COBOL, lo que de otro modo exigía un programa a medida — filtrar registros, aparear archivos, convertir códigos contra tablas, validar consistencia, calcular dígito verificador módulo 10, imprimir listados con cortes de control. En 2026 reimplementé las dos desde cero en COBOL, a partir del manual original (publicación 1/84), y las validé contra la salida real de un job de producción de 1984.

El post es doble: **una historia** (quién las escribió, por qué, y qué dice la única fuente publicada que las menciona) y **un ejercicio de ingeniería** (cómo se reconstruye un programa a partir de su documentación, y qué encontrás cuando lo comparás contra lo que el programa genuino realmente hacía).

**Hook:** «El libro le dedica un párrafo. Un párrafo, en la página 37, es todo lo que la historia publicada de la informática del Estado argentino tiene para decir sobre dos programas que —según ese mismo párrafo— no hubo implementador, programador ni analista que no haya usado. Yo tengo el manual. Y tengo la salida de un job real que los corrió. Así que hice lo único razonable: los escribí de nuevo.»

**Outline:**

1. **El párrafo.** Fontdevila, Laguado Duca y Cao, *40 años de informática en el Estado argentino* (EDUNTREF, 2007), p. 37, sección «La edad de oro del CUPED». La cita textual: los utilitarios modulares de **Jorge Vattuone**, en el área de programación del CUPED, «diseñados para formar parte del sistema operativo». Y el cierre: «no hubo implementador, programador o analista que no haya echado mano a ellos ante cualquier contingencia».
   - Contexto del párrafo anterior: el área de I+D a la que los compañeros llamaban «los becados», y la política explícita de «reducir la dependencia con la firma norteamericana».
   - Lo que el libro afirma y **no** está corroborado: que IBM los incorporó a su sistema operativo y los usó hasta principios del siglo XXI. Atribuirlo a la fuente, no repetirlo como hecho.
   - Lo que el libro **no** aclara: el `SCD` de la tapa del manual (`SCD - CENTRO DE COMPUTOS - DEPARTAMENTO DE INGENIERIA`) no está identificado con el CUPED. El libro usa esas tres letras una vez, para una asesoría en Sistemas de Computación de Datos bajo la Presidencia — plausible como expansión, insuficiente como identificación.

2. **Qué era el CUPED.** Centro Único de Procesamiento Electrónico de Datos, creado el 18 de octubre de 1967 bajo la Secretaría de Estado de Seguridad Social; durante décadas el centro de cómputos centralizado del Estado. Antes se llamó CUSDI — y el propio libro expande esa sigla de dos maneras distintas en dos lugares distintos, lo cual ya dice algo sobre el estado del registro histórico.
   - 🕳️ **HUECO — necesita a César:** ¿cómo llegaste al manual y a los datos del job de producción? ¿Trabajaste con estas utilerías, o llegaron por otra vía? Esta es la bisagra narrativa del post y no hay fuente que la responda.
   - [VERIFICAR: la datación «fines de los '70» del título]. Lo que las fuentes sostienen hoy es más débil: el libro dice «a partir de los '70 se incursionó en el software de base de IBM y en el diseño de utilitarios», y el manual que tengo es la publicación **1/84**. «Fines de los '70» es una inferencia razonable, no un dato documentado. O se consigue una fuente que fije la fecha, o el post lo dice como estimación explícita.

3. **La idea de diseño, y por qué era buena.** Una utilería genérica manejada por tarjetas de control es, en términos de hoy, un lenguaje de dominio específico embebido en 80 columnas. El código de operación va en la columna 1; los operandos, separados por al menos un blanco. No hay compilación, no hay link-edit, no hay pase por el bibliotecario: escribís el mazo en el JCL y corrés.
   - Comparación honesta: es el mismo movimiento conceptual que `awk`, que `sed`, que las utilerías `SORT`/`ICETOOL` de IBM — resolver una familia entera de problemas con un programa parametrizable en vez de con N programas.
   - Y la contracara: el vocabulario crece hasta que es un lenguaje, con la diferencia de que nadie lo diseñó como lenguaje. Ver [[C-02]] (simple ≠ fácil) para el ángulo filosófico.

4. **El vocabulario, en una tabla.** Lo que el párrafo del libro promete, contra las tarjetas que el manual documenta — el mapeo es uno a uno, y es la mejor evidencia de que la publicación 1/84 documenta efectivamente las herramientas que el libro describe:

   | El libro dice | Tarjeta de control |
   |---|---|
   | aparear archivos o listas | `CLAVE`, `PESQIN` / `PESQOUT` |
   | reemplazar o copiar datos de uno en otro | `COPY`, `FIELD` |
   | convertir datos de una tabla o archivo a otro | `CONV` + tablas de conversión |
   | buscar para seleccionar o eliminar registros | `RCIN` / `RCOUT` |

   Y lo que el libro no menciona: `GENER` (consolidar varias tarjetas de un mismo lote en un área de 800 bytes, ordenadas por prioridad de código y no por orden de llegada), `CODIG` (reglas de presencia obligatoria), `INCON` (ocho tipos de validación, con corrección en el lugar), `ACUM` (nueve acumuladores), `CORTE`/`IMCOR` (diez niveles de corte de control), `xDVy` (dígito verificador módulo 10), `TIT`, `PRINT`, `CARRO`.

5. **El modelo de archivos.** Nueve DDNAMEs, y toda la arquitectura del programa cabe en un diagrama. Entradas: `SYSUT1` (principal), `SYSUT3` (secundaria, para `CLAVE`), `SYSUT6` (archivo de pesquisa), `SYSIN` (las tarjetas). Salidas: `SYSUT2` (principal), `SYSUT4` (secundaria), `SYSUT5` (lotes rechazados), `SYSPRINT` (log), `SYSLIST` (informe de inconsistencias). En el port a sistemas abiertos, los DDNAMEs se resuelven por variables de entorno — `export SYSUT1=./in.dat` y listo.

6. **La reimplementación.** Un solo motor, `src/OSENGINE.CBL` (~4800 líneas de COBOL-85 estricto, formato fijo hasta la columna 72), que lee las tarjetas en tiempo de ejecución y se comporta como una u otra utilería; dos stubs mínimos que hacen `CALL "OSENGINE" USING` un campo `PIC X(7)` con el modo.
   - Por qué un motor y no dos programas: el 90 % del vocabulario es común a ambos. Duplicarlo era garantizar que las dos copias divergieran.
   - Compila con **GnuCOBOL 3.2** en dos perfiles de dialecto (`-std=mvs` y `-std=rm`) desde una sola fuente, y los dos builds producen resultados **byte a byte idénticos** — lo que se prueba en CI con una matriz sobre ambos dialectos, en vez de afirmarlo.
   - El precio de la portabilidad de dialecto: cero funciones intrínsecas. `CURRENT-DATE` → `ACCEPT FROM DATE` con ventana de siglo; los dieciséis usos de `NUMVAL` por dígito → tabla de lookup; `UPPER-CASE` → `INSPECT CONVERTING`; `ORD`/`CHAR` → un redefine `BINARY` big-endian. Y las salidas tempranas escritas como `GO TO <n>-EXIT` + `PERFORM … THRU <n>-EXIT`, que es COBOL-85 clásico. La única línea atada al dialecto quedó aislada en un copybook por dialecto (`SELCONV.cpy`).
   - Lo que se aprende: escribir COBOL portable en 2026 se parece bastante a escribirlo en 1984, porque las dos restricciones son la misma.

7. **La pirámide de verificación** — el corazón del post. Cinco niveles, cada uno probando algo que el anterior no puede:
   1. `OSTESTS.CBL` — 5 asserts en COBOL sobre los algoritmos núcleo (desempaquetado COMP-3 por nibbles, módulo 10, lookup `/INT`).
   2. `run_tests.sh` — 63 casos de comportamiento, límites y parseo negativo.
   3. `manual_examples.sh` — **los 93 ejemplos de tarjetas impresos en el manual**, uno por caso.
   4. `golden_check.sh` — 4 líneas base end-to-end.
   5. `mainframe_check.sh` — **8 pasos de un job de producción real de 1984, diffeados contra la salida que produjo el mainframe genuino**. Seis de los ocho, byte a byte exactos.
   - La distinción que ordena todo: los cuatro primeros miden el motor contra una *lectura* del manual. El quinto lo mide contra lo que la utilería genuina *realmente hacía*.

8. **Arqueología de datos: dos rarezas del EBCDIC** que no son bugs y merecen su propio párrafo:
   - **Colación.** En EBCDIC las letras ordenan *por debajo* de los dígitos; en ASCII, por encima. Los archivos de pesquisa abren con un registro de texto descriptivo que en el mainframe quedaba correctamente ordenado para el merge y, transcodificado a ASCII, lo bloquea. El dato no cambió; cambió el orden del universo.
   - **`X'00'` como dato.** Los datasets originales eran `RECFM=FB` sin terminadores de registro, así que un byte nulo era dato ordinario. En Linux el build de GnuCOBOL lo round-trippea perfecto; en Windows se pierde. El mismo código, el mismo dato, dos resultados: el sistema de archivos también es parte del programa.

9. **Nota de transparencia sobre IA** (convención de la casa). Nombrar la herramienta, y separar explícitamente qué decisiones fueron mías y no tercerizables: la estrategia de un motor único con dos stubs (D0.4/D0.5), la resolución de las contradicciones documentales (D0.1–D0.7), el modelo de conectores y corridas (D0.8), la restricción de que sólo las reglas relacionales admiten alternativas `.O.` (D0.9), el tamaño de registro de 32 760 bytes (D0.10), y la decisión de que el criterio de éxito fuera la salida del mainframe real y no mi lectura del manual.

10. **Cierre.** Dos programas escritos por una persona con nombre y apellido en un organismo público argentino, usados por todo el mundo durante décadas, documentados en un párrafo. El software de infraestructura tiende a volverse invisible exactamente en la medida en que funciona bien. Reimplementarlo es una forma de leerlo — y de dejar por escrito que existió.

**Bibliografía:**

- Pablo A Fontdevila, Arturo Laguado Duca y Horacio Cao, *40 años de informática en el Estado argentino*, EDUNTREF — Universidad Nacional de Tres de Febrero, 1.ª ed., noviembre 2007, 170 pp. Investigación del CIAP, Facultad de Ciencias Económicas, UBA. **El párrafo sobre OSGENER/OSLISTA está en la página 37**, sección «La edad de oro del CUPED». — *estable*
  - PDF publicado gratuitamente por el propio coautor Horacio Cao en su sitio: [horaciocao.com.ar/…/08_Cuarenta_anos_de_informatica_en_el_Estado.pdf](https://www.horaciocao.com.ar/wp-content/uploads/2015/05/08_Cuarenta_anos_de_informatica_en_el_Estado.pdf) — *frágil (sitio personal)*
  - Backup: [snapshot de Wayback Machine, 2023-10-12](https://web.archive.org/web/20231012043250/https://www.horaciocao.com.ar/wp-content/uploads/2015/05/08_Cuarenta_anos_de_informatica_en_el_Estado.pdf) — *estable*. **Citar el sitio del autor como fuente y el snapshot como respaldo**, según la convención de la casa (fuente propia del autor antes que Wikipedia).
  - Tercera copia, en el repo del proyecto: [`docs/Cuarenta_anos_de_informatica_en_el_Estado.pdf`](https://github.com/CesarBallardini/osgener-oslista/blob/main/docs/Cuarenta_anos_de_informatica_en_el_Estado.pdf) — *estable*. Está ahí por ser la fuente citada de `docs/a-little-history.md`. Rama por defecto del repo: **`main`** (no `master`).
- *OSLISTA / OSGENER — Manual de programas utilitarios*, SCD — Centro de Cómputos, Departamento de Ingeniería, publicación **1/84**. 37 hojas. Reproducido íntegro en el repo (`docs/manual/OSLSGEN.txt`, CP437) junto con su traducción completa al inglés (`docs/manual/osgenls-manual.md`). El CUPED liberó binarios y documentación como software de dominio público dentro de la administración pública, que es la razón por la que puede reproducirse. — *estable (en el repo)*
- [`CesarBallardini/osgener-oslista`](https://github.com/CesarBallardini/osgener-oslista) — la reimplementación, MIT. `docs/a-little-history.md` (la procedencia), `docs/plan.md` (las diez fases, las decisiones D0.1–D0.10, los huecos M1–M30), `docs/user-guide.md` (referencia de tarjetas). — *estable*
- [GnuCOBOL — sitio oficial](https://gnucobol.sourceforge.io/) y su [Programmer's Guide](https://gnucobol.sourceforge.io/doc/gnucobol.html). — *estable*
- Ver [[tr-11]] (Computer History Museum) si se busca material de contexto sobre utilerías de sistema en la era System/360-370.
- **Pendiente de buscar:** cualquier fuente secundaria sobre el CUPED que fije fechas del área de I+D («los becados») o que mencione a Jorge Vattuone. Hasta ahora, el párrafo de la página 37 es la única mención publicada que se encontró. Candidatos a revisar: archivos de la Secretaría de Estado de Seguridad Social, actas de SADIO, publicaciones de la época.

**Imágenes:**

- _Hero (2.5:1)_ — **panel frontal de un IBM System/360**. Tres candidatos verificados en Wikimedia Commons el 2026-07-29 (licencia, autor y dimensiones chequeados en la página del archivo, no inferidos). Los tres recortan a 2.5:1 sin deformar; los recortes de prueba se hicieron con Pillow y están fuera del repo.

  | # | Archivo | Qué muestra | Píxeles | Licencia | Autor / año |
  |---|---|---|---|---|---|
  | **A** | [`IBM_System360_control_panel.jpg`](https://commons.wikimedia.org/wiki/File:IBM_System360_control_panel.jpg) | Panel completo de un **Model 30** en el Computer History Museum, con el gabinete rojo y el cartel `IBM System/360` | 2256 × 1496 | CC BY-SA 2.0 | vonguard, 2011 |
  | **B** | [`CHM_Artifacts_IBM_System_360_control_panel_(model_91)_(2375800585).jpg`](https://commons.wikimedia.org/wiki/File:CHM_Artifacts_IBM_System_360_control_panel_(model_91)_(2375800585).jpg) | Macro de los tres diales hexadecimales `CYCLIC PROGRAM COUNTER ENTRY` de un **Model 91** (0-9 A-F grabados en el aluminio) | 3888 × 2588 | CC BY 2.0 | Marcin Wichary, 2008 |
  | **C** | [`IBM_S_360_Model_30_Operator_Panel_(24493686278).jpg`](https://commons.wikimedia.org/wiki/File:IBM_S_360_Model_30_Operator_Panel_(24493686278).jpg) | Panel **original** de Model 30 manejado por una reimplementación en FPGA, sobre un escritorio de taller | 4008 × 2988 | **CC0** (dominio público) | Wolfgang Stief, 2017 |

  **Recomendación: B.** Recorta limpio a `3888 × 1555` (caja `(0, 690, 3888, 2245)`), es el más nítido a tamaño banner, y la licencia CC BY 2.0 es la menos exigente de las tres. Además rima con el post: tres diales hexadecimales para entrar una dirección a mano son la misma clase de interfaz que un mazo de tarjetas de 80 columnas — el operador manipulando directamente la representación de la máquina.

  **Alternativa A** si se prefiere que el hero diga literalmente «esto es un System/360»: recorte `2256 × 902` (caja `(0, 426, 2256, 1328)`). Advertencia verificada al recortar: el panel es **más alto que 2.5:1**, así que hay que elegir entre perder el cartel `IBM System/360` de arriba o los interruptores de abajo — el recorte propuesto conserva el panel completo y pierde el cartel. Además arrastra por la izquierda un cartel explicativo del museo **en inglés**, que en un post en castellano distrae.

  **C se descarta** pese a tener la mejor licencia: el escritorio está demasiado cargado (posters, papel de formulario continuo, una radio roja) y el contexto FPGA obligaría a explicar en la footnote que no es una máquina de época funcionando.

  Footnote de atribución obligatoria (opción B), referenciada inline en algún punto natural del cuerpo:

  ```markdown
  [^img_hero]: Imagen de [CHM Artifacts — IBM System/360 control panel (model 91)](https://commons.wikimedia.org/wiki/File:CHM_Artifacts_IBM_System_360_control_panel_(model_91)_(2375800585).jpg) — CC BY 2.0 — Marcin Wichary, 2008, Computer History Museum. Recortada a 2,5:1 para hero landscape.
  ```
- _Crear_: captura de un mazo de tarjetas de control real (las diez líneas de `jcl/RUNPROC.JCL`), en monoespaciado con la regla de columnas arriba, para que se vea la restricción de las 80 columnas (~20 min).
- _Crear (mermaid)_: el diagrama de conectividad de archivos — `SYSUT1`/`SYSUT3`/`SYSUT6`/`SYSIN` → motor → `SYSUT2`/`SYSUT4`/`SYSUT5`/`SYSPRINT`/`SYSLIST`. Ya existe como Mermaid en `docs/manual/osgenls-manual.md`; se reusa. **Requiere `mermaid: true` en el frontmatter** (~15 min).
- _Crear_: la pirámide de verificación de cinco niveles con los números (5 / 63 / 93 / 4 / 8) (~30 min).
- _Opcional_: recorte de la página 37 del PDF del libro con el párrafo citado. Verificar antes que el recorte de una página de un PDF distribuido libremente por su coautor sea aceptable como cita — la cita textual en el cuerpo del post ya cubre la necesidad, así que la imagen es prescindible.

**Tags propuestos:** `['legacy', 'COBOL', 'GnuCOBOL', 'mainframe', 'IBM', 'MVS', 'JCL', 'EBCDIC', 'arqueologia', 'CUPED', 'Argentina', 'historia']`

**Estado actual:** ✅ **post escrito y listo el 2026-07-29** en `content/es/posts/2026-07-29-osgener-oslista-mainframe-ibm/` (~2700 palabras). Compila limpio: hero procesado, mermaid activo, `tables.css` inlineado, footnotes OK, `public/` regenerado. **El draft se conserva** —pese a que el post ya está escrito— porque quedan mejoras pendientes: los dos derivados listados al final y la versión en inglés.

Decisiones de recorte ya tomadas al escribirlo:

- Se sacaron del outline los puntos **8** (las lecciones M27/M30) y **10** (lo que no se publica del fixture confidencial). Quedan diez secciones. El material de M27/M30 pasa entero al derivado de Serie C listado abajo — sigue disponible acá y en `docs/plan.md` del repo.
- El hero elegido es el **candidato B** (diales hexadecimales del Model 91, CC BY 2.0), recortado a 3888 × 1555 y guardado como `hero-ibm-360-panel.jpg` en el bundle. El candidato A queda como alternativa si se prefiere un panel completo; el swap es cambiar el archivo y la footnote `[^img_hero]`.

Resueltos el 2026-07-29:

1. 🕳️ **El HUECO** — César decidió **no** contar cómo llegaron a sus manos el manual y los datos del job, y borró el bloque marcador. La sección «Qué era el CUPED» cierra en la incógnita de la sigla SCD. Queda como posible ampliación futura, no como pendiente bloqueante.
2. **[VERIFICAR] la datación del título.** Las fuentes sostienen «a partir de los '70» (libro) y «1/84» (manual). Resuelto en el texto con un párrafo que declara explícitamente que «fines de los '70» es una estimación del autor y no un dato documentado. Si aparece una fuente que fije la fecha, ese párrafo se reemplaza por la cita.
3. **`public/` regenerado** con `hugo --cleanDestinationDir`; verificado que no hay artefactos de `hugo server` (la única coincidencia de `localhost:` en todo el árbol es el `http://localhost:4000` que está dentro de un bloque de código del post de Jekyll de 2016, y ya estaba en `HEAD`).

Ediciones de César sobre el texto que salió de esta pasada, para tener en cuenta si se escribe la versión en inglés: agregó la observación sobre perfiles de LinkedIn que todavía declaran manejo de estas utilerías, atenuó «IBM los incorporó» a «se acusa a IBM de incorporarlo», y suavizó el remate de la asimetría del separador `/`.

Posibles derivados:

- **Serie C** — «"La tarjeta fue aceptada" no es "la tarjeta funcionó": lo que M27 y M30 enseñan sobre las aserciones de un test». Sale entero de este material.
- **Serie I** — un post sobre *40 años de informática en el Estado argentino* como fuente: qué registra, qué omite, y por qué la historia del cómputo estatal argentino sobrevive en un párrafo por vez.
- **Versión en inglés** — el README ya está en inglés; el post técnico tiene audiencia natural en la comunidad GnuCOBOL / mainframe. Usar `translationKey`.
