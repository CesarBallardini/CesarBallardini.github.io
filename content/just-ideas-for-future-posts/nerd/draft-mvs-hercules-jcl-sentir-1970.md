### J-08 — IBM MVS, Hercules y los jobs JCL que escribí para sentir cómo era 1970

- **Archivo seed:** cruzar con [[H-10]] (mvs-on-hercules) + curso de MVS para estudiantes que armé
- **Slug propuesto:** `mvs-hercules-jcl-sentir-1970`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mvs-hercules-jcl-sentir-1970/index.md`
- **Serie:** J — el ángulo *nerd lateral* de la experiencia H-10 (H-10 es el cómo; J-08 es el por qué lo disfruté)
- **Cross-links:** depende de [[H-10]] (la guía técnica); lleva a [[H-04]] (GnuCOBOL), [[D-03]] (máquina de Turing)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
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

**Estado actual:** prosa-borrador escrita sobre el outline de 6 puntos (~1450 palabras, dentro del target medium). Lo que quedó escrito: el encuadre de serie J, el hook reformulado, el andamiaje técnico de JCL (vocabulario, rigidez posicional, el ciclo submit → spool → output), el argumento de la «arqueología activa» y el cierre-invitación. Todo el material técnico se apoya sólo en la bibliografía ya listada.

Lo que quedó como hueco: **todo el contenido emocional y biográfico**, que es justamente la razón de ser del post — J-08 es el *por qué me divirtió* de [[H-10]], y ese porqué es memoria de César, no dato público. Hay 11 huecos marcados: el primer job real que corrió, el error de la primera vez, el curso de MVS para estudiantes mencionado en el seed, la reacción de los alumnos, cuánto tiempo le dedicó, y el veredicto final del cierre. Además hay 6 marcadores `[VERIFICAR:]`: los más importantes son (a) las fechas «1974 y 1985» del Hook, que ninguna fuente de la bibliografía respalda, (b) la atribución a Fred Brooks del vocabulario JCL — *The Mythical Man-Month* es de 1975 y habla de OS/360, no de JCL en particular, y (c) la sintaxis exacta de los ejemplos JCL, que hay que correr contra TK4- antes de publicar porque la referencia de la bibliografía es la de z/OS moderno, no la de MVS 3.8j.

**Nota de conflicto con el Hook:** el Hook afirma fechas y una atribución a Brooks que la bibliografía no sostiene. Por instrucción, el Hook queda intacto; la prosa lo reformula sin asumir esos datos y los marca para verificación.

---

## Borrador de prosa

> ⚠️ **Curiosidad nerd lateral — esto no es ciencia de la computación.**

`//MIJOB    JOB  (ACCT),'CESAR',CLASS=A,MSGCLASS=H`. Esa línea no hace nada útil. No resuelve un problema de tu trabajo, no te va a servir en una entrevista, no mejora ningún sistema que esté en producción hoy. Lo único que hace es abrir un job en un sistema operativo que IBM dejó de vender hace décadas[^fechas] y que ahora corre emulado en mi notebook. Y sin embargo la escribí muchas veces, de noche, con la misma cara de idiota feliz con la que otros arman maquetas de barcos.

Voy a contarte por qué. En [[H-10]] está el *cómo*: Hercules[^hercules], la distribución Tur(n)key 4-[^tk4], el `vagrant up`, el LOGON, la pila entera armada y replicable. Esto no es eso. Esto es el *por qué me divirtió tanto*, que es una pregunta bastante menos respetable y bastante más honesta.

### El setup, en una línea

No voy a repetir la guía. Si querés montar el mainframe, andá a [[H-10]] y seguí los pasos: Hercules es un emulador open-source de mainframes IBM y Tur(n)key 4- es una distribución de MVS 3.8j lista para arrancar, empaquetada por la comunidad. La parte técnica está resuelta y es aburridamente sólida: sale, arranca, funciona.

Lo interesante empieza después, cuando ya tenés el prompt adelante y te das cuenta de que no tenés la menor idea de cómo se le habla a esta cosa.

### El vocabulario

JCL —Job Control Language— no es un lenguaje de programación. Es un lenguaje para *pedir*. Vos no le decís al sistema qué hacer paso a paso: le declarás qué programa querés ejecutar y qué recursos necesita, y el sistema decide cuándo y cómo dártelos. Tres verbos alcanzan para la mayoría de las cosas: `JOB` para abrir el trabajo, `EXEC` para ejecutar un programa, `DD` para describir un archivo[^jcl].

Lo primero que te golpea es la rigidez. Las sentencias empiezan con `//` en las columnas 1 y 2. El nombre va en la columna 3. El operando arranca después. Si te corriste un espacio, no compila; y no te dice «te corriste un espacio», te dice algo con un código de mensaje que tenés que ir a buscar. Venís de un mundo donde el editor te subraya el error en rojo mientras tipeás, y de golpe estás en un mundo donde el error aparece diez segundos después, en un listado, escrito en mayúsculas, con un tono que no es de ayuda sino de acta.

Y ahí está la cosa: esa rigidez no es una falla de diseño, es la forma que toma un sistema pensado para una máquina que costaba una fortuna y que no era tuya. El tiempo de CPU era el recurso escaso; el tuyo, no. Todo el vocabulario está construido alrededor de esa asimetría. Cuando escribís `CLASS=A` estás declarando en qué cola te formás. Cuando escribís `MSGCLASS` estás decidiendo dónde va a salir impreso lo que el sistema tenga para decirte. Estás negociando con una máquina que no te está esperando a vos.

Eso no se entiende leyéndolo. Se entiende cuando lo tipeás y esperás.

> 🕳️ **HUECO — necesita a César:** ¿cuál fue el primer job JCL que corriste vos, concretamente, y qué hacía? ¿Fue el `IEBGENER` del outline u otra cosa?

> 🕳️ **HUECO — necesita a César:** ¿te acordás del primer error que te comió una noche? (el código del mensaje, o al menos qué era: JCL mal formado, dataset que no existía, allocation, otra cosa).

### El primer job que sale

El ciclo es siempre el mismo: escribís el JCL, lo mandás (`SUBMIT`), el job entra a una cola, corre, y el output aparece en el spool. No hay ejecución interactiva, no hay `print()` que aparece mientras corre. Mandás y esperás. El resultado es un listado.

Mi primer objetivo fue el mínimo digno: copiar un archivo de un lado a otro con `IEBGENER`, la utilidad de copia de toda la vida del sistema. Es literalmente un `cp`. Tres líneas de JCL para hacer un `cp`[^sintaxis]. Y cuando salió —cuando fui al spool y vi el listado con el código de retorno en cero— sentí algo completamente desproporcionado para la magnitud del logro.

> 🕳️ **HUECO — necesita a César:** describí en una o dos frases qué sentiste cuando salió el primer job limpio. ¿Alivio, risa, ganas de mostrárselo a alguien? ¿A quién se lo mostraste?

Después vino el paso que de verdad importaba: compilar un COBOL y ejecutarlo. Un HELLO WORLD, nada más. Pero un HELLO WORLD compilado con el compilador de IBM, adentro del sistema operativo de IBM, con el JCL de IBM llamando al compilador en un paso y al binario resultante en el paso siguiente. No es GnuCOBOL en Linux emulando el ambiente — cross-link a [[H-04]], que es otra historia y otra sensación. Acá el ambiente es el ambiente.

> 🕳️ **HUECO — necesita a César:** ¿el COBOL en MVS fue antes o después de tu laboratorio de GnuCOBOL? El orden cambia el relato: ¿llegaste al mainframe *desde* GnuCOBOL o al revés?

### El listado

Y acá viene la parte que no puedo explicarle a nadie sin sonar raro: el output es hermoso.

Un listado de MVS no está diseñado para tu pantalla. Está diseñado para papel continuo, ancho fijo, columnas alineadas, cabecera en cada página. El sistema no te está mostrando información: te está *imprimiendo* información, aunque el papel hoy sea un archivo de texto en el spool[^prtspool]. Hay una estética completa ahí adentro —el uso del espacio, la jerarquía tipográfica hecha con nada más que mayúsculas y sangrías, la disciplina de las 132 columnas[^columnas]— que es de una época en la que el output de una computadora era un objeto físico que alguien iba a leer sentado en un escritorio.

Yo crecí con pantallas. Esto es de antes de las pantallas. Y se nota en cada decisión.

> 🕳️ **HUECO — necesita a César:** ¿alguna vez viste o usaste listados de mainframe reales, en papel, en tu vida profesional? Si sí, ¿dónde y cuándo? (Esto cambia el post entero: si hay memoria propia, no es nostalgia ajena.)

### ¿Y esto para qué sirve?

Para nada, y esa es una respuesta legítima. Pero hay una versión menos cómoda de la pregunta que sí me interesa.

Se puede leer sobre el batch processing. Se puede leer que antes se mandaban jobs a una cola y se esperaba el turno. Uno asiente, entiende las palabras, y no entiende nada. Lo que no se transmite por lectura es la *fricción*: la longitud real del ciclo, la ansiedad de mandar algo sabiendo que el feedback llega después, la manera en que esa espera te obliga a leer tu propio código antes de mandarlo porque no vas a tener veinte intentos gratis.

Eso es lo que yo llamo arqueología activa. No leer sobre el paradigma extinto: habitarlo un rato. Es la misma razón por la que uno programa una máquina de Turing a mano una vez en la vida ([[D-03]]) aunque sepa perfectamente que no la va a usar nunca. El punto no es el resultado. El punto es que el paradigma se te mete en el cuerpo por un rato, y después leés a los que vivieron ahí y los entendés distinto.

Que es, creo, lo que le pasa a cualquiera que lea *The Mythical Man-Month*[^brooks] después de haber tipeado JCL. Brooks escribe desde adentro de un mundo donde el ciclo de compilación se medía en horas y donde el sistema operativo era un proyecto de miles de personas. Uno puede leerlo como historia de la gestión de proyectos. O puede leerlo después de haber esperado su propio job, y ahí las quejas de Brooks dejan de ser anécdotas de museo[^brooks_jcl].

### Una tarde

> 🕳️ **HUECO — necesita a César:** en el seed decís que armaste un curso de MVS para estudiantes. ¿Para quiénes fue, en qué contexto (institución, materia, taller), y cuándo?

> 🕳️ **HUECO — necesita a César:** ¿cuál fue la reacción de los estudiantes? ¿Les pareció una pérdida de tiempo, les divirtió, alguno enganchó de verdad?

> 🕳️ **HUECO — necesita a César:** ¿qué era lo que más les costaba? (esto sería un gran detalle: el punto exacto donde una persona formada hoy choca contra el modelo mental de 1970).

> 🕳️ **HUECO — necesita a César:** ¿cuánto tiempo te llevó en total, entre montar el ambiente y sentirte cómodo mandando jobs? ¿Días, meses, sigue abierto?

Si tenés una tarde libre y algo de curiosidad, hacelo. Seguí [[H-10]], montá el ambiente, y escribí tres líneas de JCL para copiar un archivo. Vas a perder la tarde y no vas a ganar nada, en el sentido en que se suele usar la palabra ganar.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto en primera persona, en dos o tres frases. ¿Qué te dejó, honestamente? ¿Volvés al mainframe cada tanto o fue una fase que se cerró?

> 🕳️ **HUECO — necesita a César:** ¿hay algo que hayas entendido de tu trabajo *actual* gracias a esto? Si la respuesta es «no, nada, fue puro gusto», también sirve — y es un mejor final.

[^fechas]: [VERIFICAR: el Hook del draft afirma que IBM vendió este sistema «entre 1974 y 1985». Ninguna fuente de la bibliografía del draft respalda esas fechas. Chequear el rango real de comercialización de MVS y de MVS 3.8j antes de publicar, y sólo entonces poner la fecha en el cuerpo del post.]

[^hercules]: [Hercules — sitio oficial](http://www.hercules-390.org/).

[^tk4]: [MVS 3.8J Tur(n)key 4- distribution](https://wotho.ethz.ch/tk4-/).

[^jcl]: [IBM, *JCL Reference for z/OS*](https://www.ibm.com/docs/en/zos/) — la referencia moderna del lenguaje. [VERIFICAR: la referencia de la bibliografía es la de z/OS actual; MVS 3.8j es muy anterior. Confirmar que la descripción de `JOB`/`EXEC`/`DD` y el formato posicional que uso acá valen tal cual en MVS 3.8j, o aclarar en el texto que estoy describiendo el JCL moderno.]

[^sintaxis]: [VERIFICAR: escribir el JCL de `IEBGENER` completo y correrlo contra TK4- antes de publicar, y pegar acá el listado real. No poner un ejemplo de sintaxis en el post sin haberlo ejecutado.]

[^prtspool]: [VERIFICAR: acá corresponde un cross-link a [[H-12]] (prtspool / imprimir desde MVS a PDF) si ese post sale antes o cerca. Confirmar el ID y si el mecanismo que describo — el output queda en el spool — es el que efectivamente usa TK4-.]

[^columnas]: [VERIFICAR: el ancho de 132 columnas es lo que recuerdo como estándar de impresora de línea de la época, pero no está respaldado por ninguna fuente de la bibliografía del draft. Chequearlo o sacarlo.]

[^brooks]: [Fred Brooks, *The Mythical Man-Month*, 1975](https://archive.org/details/mythicalmanmonth00broo).

[^brooks_jcl]: [VERIFICAR: el Hook del draft dice «el vocabulario de Fred Brooks». Brooks escribe sobre el proyecto OS/360, no sobre JCL específicamente, y el libro es de 1975. Antes de publicar: buscar en *The Mythical Man-Month* un pasaje concreto sobre el ciclo de compilación / el turnaround de un job y citarlo textual — o bajar el tono de la atribución y no hacerle decir a Brooks lo que no dijo.]

