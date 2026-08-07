### J-07 — Relevamiento de departamentos: el script Python que imprimía una etiqueta por unidad

- **Archivo seed:** `github.com/CesarBallardini/relevamiento-deptos` (fork de `DanielMunozT/relevamiento-deptos`, Python, forkeado 2016-05-11; los commits del original son de abril de 2016)
- **Slug propuesto:** `relevamiento-deptos-etiquetas`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-relevamiento-deptos-etiquetas/index.md`
- **Serie:** J
- **Cross-links:** —
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** short (600-900 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** un script Python simple para agilizar el relevamiento de departamentos (unidades residenciales) — toma un CSV con direcciones y numeros, genera una etiqueta imprimible para cada uno. Lo forkeé en 2016 para un trabajo concreto de administración de consorcios. El post es una micro-anécdota sobre "cuándo el software de 100 líneas resuelve un problema real y no necesita nada más".

**Hook:** "en 2016 un amigo que administra edificios me pidió ayuda para imprimir 300 etiquetas de departamentos con dirección, piso, unidad y código de barras. No había un SaaS obvio. Había un script Python de 100 líneas que hacía exactamente eso. Lo forkeé, lo corrí, las etiquetas salieron, el trabajo se hizo. El post es la defensa del software micro que resuelve problemas micro."

**Outline:**
1. El problema: imprimir 300 etiquetas de departamentos desde un CSV.
2. El script Python (ReportLab o similar): 100 líneas, sin tests, sin docs.
3. Lo que aprendí: a veces el software "serio" es hostil al problema pequeño. Los scripts de fin de semana ganan.
4. Cierre: el fork sigue ahí, funciona si lo necesitás.

**Bibliografía:**

_Fuentes primarias — el repositorio (verificadas por fetch 2026-07-16):_
- [CesarBallardini/relevamiento-deptos](https://github.com/CesarBallardini/relevamiento-deptos) — el fork. API: `fork: true`, `parent: DanielMunozT/relevamiento-deptos`, `created_at: 2016-05-11`, `pushed_at: 2016-04-10`, 0 stars / 0 forks / 0 issues, licencia Apache-2.0, `default_branch: master`. **frágil** (un fork personal se borra con un clic) — backup Wayback (200, vía `archive.org/wayback/available`): `http://web.archive.org/web/20201212061818/https://github.com/CesarBallardini/relevamiento-deptos`.
- [DanielMunozT/relevamiento-deptos](https://github.com/DanielMunozT/relevamiento-deptos) — el repositorio original, de Daniel Ángel Muñoz Trejo. **frágil** — backup Wayback (200): `http://web.archive.org/web/20201023051700/https://github.com/DanielMunozT/relevamiento-deptos`.
- `generar.py` — [fuente cruda](https://raw.githubusercontent.com/CesarBallardini/relevamiento-deptos/master/generar.py). API `contents`: **8366 bytes**. Importa `openpyxl`, `docx`, `re`, `sys`, `os.path`, `tkinter` + `tkinter.filedialog`. **No importa ReportLab. No lee CSV. No genera código de barras.** **frágil**.
- `Instrucciones.pdf` — [fuente cruda](https://raw.githubusercontent.com/CesarBallardini/relevamiento-deptos/master/Instrucciones.pdf) (13 páginas; texto extraído con pypdf, el fetch directo devuelve binario). Es el documento que explica para qué existe el programa: relevar edificios fotografiando porteros eléctricos, cargar los datos en un `.xlsx`, y generar un `.docx` **con una página por departamento para imprimir sobre cada sobre** en el que se mete un libro a repartir. Menciona explícitamente que los relevadores se identifiquen «que son de tal iglesia». **frágil**.
- `preguntas.txt` — [fuente cruda](https://raw.githubusercontent.com/CesarBallardini/relevamiento-deptos/master/preguntas.txt). Notas de campo del operativo original: 20 manzanas, 15 personas, grupos de dos o tres durante hora y media por cada dos manzanas. **frágil**.
- Historial de commits (API `/commits`): 9 commits, todos de Daniel Ángel Muñoz Trejo, entre 2016-04-03 y 2016-04-10. **Ninguno de César.** **frágil**.

_Tecnología que el script realmente usa:_
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) — «a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files»; autores Eric Gazoni y Charlie Clark, licencia MIT/Expat. **estable** (readthedocs, proyecto vivo).
- [python-docx](https://python-docx.readthedocs.io/en/latest/) — «a Python library for creating and updating Microsoft Word (.docx) files»; de Steve Canny. **estable**.
- [`tkinter` — Python stdlib](https://docs.python.org/3/library/tkinter.html) — interfaz estándar a Tcl/Tk; `tkinter.filedialog` provee los diálogos de selección de archivo que usa `generar.py` cuando no le pasás los nombres. **estable**.

_Descartadas — estaban en la bibliografía y no corresponden:_
- ~~ReportLab~~ y ~~`csv` (stdlib)~~: el script no usa ninguna de las dos. Ver «PREMISA EN DUDA» en Estado actual. Si el post se reencuadra como «cómo lo habría hecho yo» pueden volver, pero entonces no describen el fork.

**Imágenes:**
- _Crear_: screenshot de una etiqueta generada (anonimizada) (~10 min).

**Tags propuestos:** `['Python', 'openpyxl', 'python-docx', 'etiquetas', 'script', 'nerd lateral']`

_(Corregidos en la pasada de fuentes: `ReportLab` y `CSV` salieron porque el script no usa ninguna de las dos. Sin puntos en los tags, por la limitación de Hugo en Windows — `python-docx` va con guion, que es el nombre real del paquete.)_

**Estado actual:**

> ⚠️ **PREMISA EN DUDA (pasada de fuentes, 2026-07-16).** Abrí el repositorio y el programa no es el que el draft describe. Tres choques, en orden de gravedad:
>
> 1. **La pila técnica del draft es inventada.** `generar.py` no importa `csv` ni ReportLab. Importa `openpyxl` y `docx` (python-docx): **lee `.xlsx` y escribe `.docx`, no lee CSV y no genera PDF.** Tampoco genera código de barras — el Hook los menciona y no existen en el código. Reescribí la sección «El script» contra la fuente real y marqué el cambio ahí mismo. **El Hook y el Concepto no los toqué (son tuyos), pero contradicen el repositorio en tres puntos: «CSV», «ReportLab o similar» y «código de barras».** Hay que reescribirlos o reencuadrar el post.
> 2. **«Etiqueta» probablemente no significa lo que el post cree.** Según `Instrucciones.pdf`, la salida es un `.docx` con **una página por departamento, para imprimir sobre cada sobre** en el que se mete un libro que se va a repartir. No son stickers en una plancha A4. La imagen central del post —la grilla de rectángulos, la etiqueta 214 corrida medio centímetro— no describe este programa.
> 3. **El operativo original no es administración de consorcios.** `preguntas.txt` habla de 20 manzanas y 15 personas relevando de a dos o tres, e `Instrucciones.pdf` explica cómo fotografiar porteros eléctricos y qué decirle al encargado para que no llame a la policía — identificándose como «de tal iglesia», para avisar que van a regalarle un libro a cada departamento. Es un operativo territorial de distribución, no un edificio ni un consorcio. **Esto describe el uso del autor original, no necesariamente el tuyo:** puede que hayas forkeado una herramienta hecha para un censo y la hayas usado para otra cosa. Pero el Concepto afirma «un trabajo concreto de administración de consorcios» y nada en el repositorio lo respalda. Necesito que lo confirmes.
>
> **Ironía que el post debería aprovechar, no esconder:** el borrador se burla de la combinación de correspondencia en un procesador de texto, y el script *es* una combinación de correspondencia en un procesador de texto — sólo que hecha bien, con grupos opcionales `{}` que resuelven el bug clásico de «piso: ,» vacío, y con expansión de rangos para no obligarte a repetir filas. El post mejora si acepta eso en vez de negarlo.
>
> **Camino sugerido (decidís vos):** o el post se reencuadra sobre el programa real —que es más interesante que el imaginario—, o se reencuadra como «el problema que yo tenía y cómo lo habría resuelto», y entonces el fork pasa a ser una anécdota lateral y ReportLab vuelve a la bibliografía como hipótesis, no como descripción.

Fork viejo (2016), proyecto puntual. Prosa completa escrita sobre el outline existente (~870 palabras, dentro del target short, cerca del techo). Lo que quedó escrito: el encuadre del problema (imprimir una etiqueta por unidad desde una planilla y por qué no hay un SaaS obvio para eso), el argumento técnico de por qué dos bibliotecas y un bucle alcanzan y sobran —reescrito en la pasada de fuentes sobre `openpyxl` + `python-docx`, que es lo que el script realmente usa—, la reflexión sobre la hostilidad del software «serio» al problema chico, y el cierre sobre el fork que sigue ahí.

Lo que quedó como hueco y bloquea la publicación:

- **El post sigue siendo enteramente autobiográfico y la bibliografía no puede sostenerlo.** Esta pasada sourceó todo lo que era sourceable —el repositorio entero, sus dos dependencias y la stdlib que usa— y con eso alcanza para el encuadre técnico y para nada más. Todo lo que es anécdota (el amigo, el trabajo, las 300 etiquetas, si el fork se corrió tal cual) sigue dependiendo de que César conteste. Los cinco huecos siguen abiertos y ninguna búsqueda web los va a cerrar.
- ~~**No está confirmado que el script use ReportLab.**~~ **RESUELTO (2026-07-16):** no lo usa. `generar.py` importa `openpyxl` + `python-docx`; lee `.xlsx`, escribe `.docx`, y no genera código de barras. Los `[VERIFICAR:]` 1 y 2 quedaron cerrados y la bibliografía se rehízo contra el código real. La consecuencia está arriba, en PREMISA EN DUDA.
- **«100 líneas» sigue sin medirse y ahora es sospechoso**: el archivo pesa 8366 bytes según la API, lo que hace poco creíble el número. Queda un `[VERIFICAR:]` en la sección «El fork sigue ahí» — se cierra clonando y corriendo `wc -l`. Las «300 etiquetas» son un dato de César, no del repositorio: hueco, no VERIFICAR.

Pendiente además: el screenshot de una etiqueta generada, anonimizada, y decidir si el post enlaza el fork público o sólo lo menciona.

- **Nota de privacidad detectada en esta pasada.** El repositorio (el original y por lo tanto el fork) trae `relevamiento.xlsx` con direcciones de ejemplo —Bv. San Juan, Chacabuco— e `Instrucciones.pdf` incluye el mail personal del autor original y capturas de pantalla de la planilla. Antes de enlazar el fork desde el post, revisá si esos datos de ejemplo son reales o inventados. Y si el post cuenta que el operativo era de una iglesia, eso es información sobre terceros que están identificables por el repositorio: decidí con cuidado cuánto contás.

---

## Borrador de prosa

⚠️ Curiosidad nerd lateral — esto no es ciencia de la computación

---

Hay una clase de problema que la industria del software decidió, sin decirlo nunca en voz alta, que no existe. No es un problema difícil. No escala. No tiene mercado. Es, por ejemplo, esto: tenés una lista de departamentos en una planilla —dirección, piso, unidad— y necesitás una etiqueta impresa por cada uno. Trescientas etiquetas. Para el martes.

Buscá una solución. Vas a encontrar plataformas de gestión de consorcios con abono mensual, suites de etiquetado industrial con licencia por puesto, y una cantidad notable de gente en foros explicando cómo hacer combinación de correspondencia en un procesador de texto, que es la respuesta correcta y también la que te va a hacer llorar cuando la etiqueta número 214 salga corrida medio centímetro. Lo que no vas a encontrar es un botón que diga «tengo este CSV, dame el PDF».

> 🕳️ **HUECO — necesita a César:** El hook dice que en 2016 un amigo que administra edificios te pidió ayuda con esto. ¿Qué era exactamente el trabajo — un relevamiento, un censo de unidades, un cambio de administración? ¿Y para qué eran las etiquetas: pegarlas en las puertas, en medidores, en carpetas del archivo?

> 🕳️ **HUECO — necesita a César:** ¿Antes de buscar código intentaste la vía «normal» — planilla, combinación de correspondencia, algún programa de etiquetas? Si la intentaste y la abandonaste, contame en qué se rompió. Es el mejor argumento del post y no lo puedo inventar.

### El script

> ✏️ **NOTA DE LA PASADA DE FUENTES (2026-07-16) — esta sección fue reescrita.** La versión anterior describía un programa que leía CSV con el módulo `csv` y dibujaba etiquetas en un PDF con ReportLab, sobre una grilla de rectángulos en una hoja A4. **Nada de eso está en el repositorio.** Abrí el fork y `generar.py` no importa `csv` ni ReportLab: importa `openpyxl`, `docx` (python-docx), `re`, `sys`, `os.path` y `tkinter`. Lee `.xlsx` y escribe `.docx`. Reescribí la sección para que describa el programa que existe. El párrafo viejo queda en el historial de git si lo querés recuperar. Ojo: esto choca con el Hook y el Concepto, que no toqué — ver «PREMISA EN DUDA» en Estado actual.

Lo que hay abajo de un problema así, cuando lo mirás de frente, son dos piezas y nada más.

La primera es leer la planilla. No un CSV: un `.xlsx`, porque la persona que carga los datos usa Excel y no le vas a pedir que exporte nada. Eso lo resuelve `openpyxl`, una biblioteca que lee y escribe los formatos de Excel 2010 en adelante.[^openpyxl] No hay decisión de diseño que tomar. Importás, abrís, iterás.

La segunda es escribir el documento. Acá tampoco hay que inventar, y acá está la sorpresa: no es un PDF. Es un `.docx`, generado con `python-docx`.[^pythondocx] La plantilla es un documento de Word que vos editás en Word, con los campos escritos como `<Calle>`, `<Numero>`, `<Piso>`, `<Depto>`; el programa lo abre, reemplaza cada campo y emite una página por unidad.[^instrucciones]

Y hay un detalle que redime todo el asunto: los campos van entre llaves opcionales. Si escribís `<Calle> <Numero>{, piso: <Piso>}{, dep.: "<Depto>"}`, y un edificio no tiene pisos, no queda `San Juan 47, piso: , dep.: "B"` — desaparece la llave entera, coma incluida. Eso es exactamente el bug que hace fea toda combinación de correspondencia hecha en un procesador de texto, y el script de fin de semana lo tiene resuelto en una línea de sintaxis.[^instrucciones]

La pieza más astuta, sin embargo, no es ninguna de las dos. Es la expansión. En la planilla no cargás una fila por departamento: cargás un edificio y decís que tiene pisos del 0 al 12, que no tiene 13, que sigue del 14 al 17 y termina en el 20, y que cada piso tiene A, B y C. El programa expande eso a la lista completa, una fila por unidad, y de paso te deja poner diccionarios (`0=PB`) para que el piso cero se imprima «PB».[^instrucciones] Ahí está el trabajo real: no en dibujar, en *no obligar al humano a repetirse*.

Poné esas piezas una al lado de la otra y el programa se escribe solo: expandí, y por cada fila resultante clonás la plantilla y reemplazás los campos. Eso es todo. No hay arquitectura. No hay capa de servicio. El bucle *es* el programa.

> 🕳️ **HUECO — necesita a César:** ¿De quién era el repositorio original que forkeaste, y por qué lo forkeaste en vez de sólo clonarlo? ¿Le hiciste cambios —el formato de la hoja, los campos, el tamaño de la etiqueta— o lo corriste tal cual salía?

> 🕳️ **HUECO — necesita a César:** ¿Cuánto tardaste, de encontrar el repositorio a tener las etiquetas impresas? Si fue una tarde, decilo; si fueron tres días peleando con márgenes de impresora, decilo también, que es más honesto y más gracioso.

### Lo que aprendí

El software serio es hostil al problema chico, y no por maldad: por economía. Una plataforma tiene que cobrar un abono, y para justificar un abono tiene que hacer veinte cosas, y para hacer veinte cosas tiene que preguntarte quién sos, dónde está tu edificio, cuántas unidades tiene y si querés integrarlo con tu contabilidad. Vos querías trescientos rectángulos con letras adentro. Pagaste con tu tiempo la diferencia entre lo que necesitabas y lo que el producto necesita ser para existir.

El script de fin de semana no tiene ese problema porque no tiene que existir mañana. No tiene usuarios, tiene *un* usuario. No tiene casos de uso, tiene *el* caso de uso. Por eso puede darse el lujo de no tener tests, no tener documentación, no tener configuración: todo eso es infraestructura para sobrevivir al cambio, y este programa no va a cambiar. Va a correr una vez, bien, y después va a quedar quieto.

Me parece importante decirlo sin romanticismo: esto no es una receta general. Escribir así el sistema de facturación de una empresa es una imprudencia. La habilidad no está en escribir código descartable —eso lo hace cualquiera—, está en reconocer cuándo el problema *es* descartable. Trescientas etiquetas, una vez, para un amigo, lo son.

> 🕳️ **HUECO — necesita a César:** ¿Volviste a usar el script alguna otra vez después de 2016, o corrió una sola vez en la vida? El cierre cambia bastante según la respuesta.

### El fork sigue ahí

Diez años después el repositorio sigue en mi cuenta, sin un commit, sin un issue, sin una estrella. No lo mantengo. No pienso mantenerlo. Si lo necesitás, cloná, ajustá la plantilla de Word y corré: probablemente funcione, y si no funciona es un solo archivo, lo leés entero en el colectivo.[^fork]

[VERIFICAR: cuántas líneas tiene `generar.py` exactamente. El draft dice «cien líneas» en el Concepto, el Hook y acá, pero es un dato del propio draft, no una medición: la API de GitHub reporta **8366 bytes** para el archivo, lo que hace muy improbable que sean cien. Un resumen automático estimó ~180 y no lo tomo como verificado. Clonar el fork y correr `wc -l generar.py` antes de imprimir cualquier número. Si son ~180, «cien líneas» hay que corregirlo en los tres lugares — el argumento del post no cambia, pero el número tiene que ser cierto.]

> ✏️ **Verificado en esta pasada (no hace falta chequearlo de nuevo):** «sin un commit, sin un issue, sin una estrella» es literalmente cierto. La API reporta `stargazers_count: 0`, `forks_count: 0`, `open_issues_count: 0`, y los 9 commits del repositorio son todos de Daniel Ángel Muñoz Trejo, entre el 3 y el 10 de abril de 2016. El fork es del 11 de mayo de 2016 y no tiene un solo commit propio. También es cierto lo de «diez años después». Ojo con la vuelta de tuerca: si no le hiciste ningún commit, entonces **no ajustaste nada** — lo corriste tal cual salía, lo cual es un final mejor que el que el borrador imagina.

Eso también es una forma de software libre, y creo que es la más antigua: no un producto, no un proyecto, no una comunidad. Un pedazo de código que alguien dejó en la vereda porque a lo mejor a otro le sirve.

[^openpyxl]: [openpyxl](https://openpyxl.readthedocs.io/en/stable/) — biblioteca de Python para leer y escribir archivos xlsx/xlsm/xltx/xltm de Excel 2010 en adelante. Autores: Eric Gazoni y Charlie Clark. Licencia MIT/Expat.
[^pythondocx]: [python-docx](https://python-docx.readthedocs.io/en/latest/) — biblioteca de Python para crear y modificar documentos `.docx` de Microsoft Word, de Steve Canny.
[^instrucciones]: `Instrucciones.pdf`, en el repositorio [DanielMunozT/relevamiento-deptos](https://github.com/DanielMunozT/relevamiento-deptos), 13 páginas. Documenta el formato de la planilla base, los diccionarios de reemplazo, la sintaxis `<Campo>` y `{grupo opcional}` de la plantilla, y el circuito completo del operativo. El programa se probó con Python 3.5.1 e instala sus dos dependencias con `pip3.5 install openpyxl` y `pip3.5 install python-docx`.
[^fork]: [CesarBallardini/relevamiento-deptos](https://github.com/CesarBallardini/relevamiento-deptos) — fork de [DanielMunozT/relevamiento-deptos](https://github.com/DanielMunozT/relevamiento-deptos), creado el 11 de mayo de 2016. Licencia Apache-2.0.

