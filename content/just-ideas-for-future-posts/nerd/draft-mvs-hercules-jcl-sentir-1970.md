### J-08 — IBM MVS, Hercules y los jobs JCL que escribí para sentir cómo era 1970

- **Archivo seed:** cruzar con [[H-10]] (mvs-on-hercules) + curso de MVS para estudiantes que armé
- **Slug propuesto:** `mvs-hercules-jcl-sentir-1970`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mvs-hercules-jcl-sentir-1970/index.md`
- **Serie:** J — el ángulo *nerd lateral* de la experiencia H-10 (H-10 es el cómo; J-08 es el por qué lo disfruté)
- **Cross-links:** depende de [[H-10]] (la guía técnica); lleva a [[H-04]] (GnuCOBOL), [[D-03]] (máquina de Turing)
- **Idioma:** es
- **Madurez:** experiencia real, material personal
- **Length target:** medium (1200-1800 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** [[H-10]] explica *cómo* montar IBM MVS 3.8j sobre Hercules. Este post (J-08) explica *por qué me divirtió tanto*: qué se siente escribir un job JCL para imprimir una lista, esperar que corra, ver el output, y entender que estabas usando el vocabulario que Fred Brooks usaba en 1970. Es pura nostalgia ajena. Es maravilloso.

**Hook:** "*JOB* seguido de tu nombre. *EXEC PGM=IEBGENER*. *DD SYSIN=\*,DSN=&&TEMP*. Estás hablando el idioma de la JCL, del sistema operativo que IBM vendió entre 1974 y 1985, y que ahora corre en tu laptop emulado por Hercules. No lo hacés porque sirva para algo. Lo hacés porque es una máquina del tiempo, y porque el vocabulario de Fred Brooks se siente distinto cuando lo tipeás con las manos."

**Outline:**
1. El setup rápido: apuntar a [[H-10]] para el cómo técnico.
2. La sensación de escribir JCL: el vocabulario, la disciplina, la rigidez.
3. El primer job exitoso (`IEBGENER` copiando un archivo), el primer job COBOL (compilar y ejecutar un HELLO WORLD).
4. La belleza del output: columna por columna, como imprimía una LaserPrinter IBM.
5. Por qué esto importa (o no): la arqueología activa como manera de entender un paradigma de computación extinto.
6. Cierre: invitación al lector a intentarlo una tarde.

**Bibliografía:**
- [[H-10]] — la guía técnica.
- [IBM, *JCL Reference for z/OS*](https://www.ibm.com/docs/en/zos/) — la referencia moderna del lenguaje.
- [Fred Brooks, *The Mythical Man-Month*, 1975](https://archive.org/details/mythicalmanmonth00broo).
- [Hercules — sitio oficial](http://www.hercules-390.org/).
- [MVS 3.8J Tur(n)key 4 distribution](https://wotho.ethz.ch/tk4-/) — la distro lista para usar.

**Imágenes:**
- _Crear_: screenshot del terminal 3270 con un job JCL cargado (~15 min).
- _Crear_: ejemplo de un JCL mínimo en una caja (~10 min).

**Tags propuestos:** `['MVS', 'Hercules', 'JCL', 'IBM', 'arqueologia', 'nostalgia', 'nerd lateral']`

**Estado actual:** experiencia real + apunta a [[H-10]]. Post corto, emocional, personal.

