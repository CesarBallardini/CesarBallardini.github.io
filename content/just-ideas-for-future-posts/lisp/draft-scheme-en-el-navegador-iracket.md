### A2-07 — DrRacket + Jupyter + iRacket: Scheme didáctico en el navegador con una VM

- **Archivo seed (repo POC):** [github.com/CesarBallardini/programacion-drracket](https://github.com/CesarBallardini/programacion-drracket) — HTML, 5 stars, último push 2020-08-04
- **Slug propuesto:** `scheme-en-el-navegador-iracket`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-scheme-en-el-navegador-iracket/index.md`
- **Serie:** A2 — complementa [[A2-06]] y [[A2-01]]; cruza con [[E-12]] y [[K-02]] por el ángulo docente
- **Cross-links:** lleva a [[A2-06]] (sicp-spanish), [[A2-01]] (SICP), [[E-12]] (patrón Vagrant+Ansible), [[K-01]] (online judge para la materia)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** para enseñar Scheme a estudiantes que recién llegan a la programación funcional, enfrentás dos fricciones a la vez: instalar DrRacket en cada máquina del laboratorio, *y* explicar el editor + REPL + workflow. Este POC resuelve las dos al mismo tiempo: una VM Vagrant con Racket + Jupyter + el kernel `iracket` instalados, donde el estudiante abre su navegador, ve un Jupyter Notebook, y escribe Scheme directamente en celdas — el resultado aparece debajo de la celda como en cualquier notebook moderno. Reusa la familiaridad con notebooks (Python, R, etc.) en lugar de pedirle al estudiante que aprenda DrRacket *y* Scheme al mismo tiempo. Recetas de instalación para Windows 10 (Chocolatey) y Ubuntu 18.04.

**Hook:** "querés enseñar Scheme. Tu estudiante nunca usó un IDE Lisp en su vida. ¿Le decís 'instalá DrRacket'? Le tira para atrás. Solución: una VM Vagrant que arranca con Jupyter Notebook + el kernel `iracket`, y el estudiante escribe Scheme en su navegador como si fuera un notebook de Python. Mismo workflow familiar, lenguaje nuevo. El post explica el setup y por qué es la mejor onboarding curve que encontré para enseñar funcional."

**Outline:**
1. El problema: la instalación de DrRacket asusta a estudiantes nuevos. La sintaxis de Scheme también. *Ambas barreras juntas* es demasiado.
2. La idea: separar las dos barreras. Reusá la familiaridad con notebooks (que ya conocen de Python en otra materia) y abandoná el IDE específico.
3. iRacket: el kernel Jupyter para Racket, mantenido por Ryan Culpepper.
4. La VM Vagrant + Ansible: Ubuntu 18.04 + Racket + Jupyter + iracket. Justifico por qué eligí Ubuntu y no Debian.
5. La instalación nativa para los estudiantes que prefieren no usar VM: Chocolatey en Windows 10, apt en Ubuntu, Homebrew en macOS.
6. El primer notebook: definir un par de funciones, evaluar expresiones, ver resultados inline. La sensación de "ah, esto es Python pero con paréntesis".
7. Las limitaciones: DrRacket tiene cosas que iRacket no replica (debugger, stepper, contracts visualizer). Cuándo conviene saltar a DrRacket.
8. Cierre: cuál es el flujo que recomiendo después de un cuatrimestre de uso real.

**Bibliografía:** *(todas las URLs fetcheadas y verificadas el 2026-07-16, salvo donde se indica lo contrario)*

**El POC**
- Repo del POC: [CesarBallardini/programacion-drracket](https://github.com/CesarBallardini/programacion-drracket) — `frágil` (repo personal, sin push desde 2020-08-04). Verificado: trae varios `Vagrantfile` (estándar + variantes 32/64 bits), guías Markdown para Windows 10 / Ubuntu 18.04 / Chocolatey, y los directorios `notebooks/`, `slides/`, `ejercicios-resueltos/pdf`, `teach-yourself-scheme-in-fixnum-days`. **No hay Ansible.** Flujo del README: clonar → `vagrant up` → `http://127.0.0.1:8888/`.

**iRacket**
- [iRacket en GitHub](https://github.com/rmculpepper/iracket) — Ryan Culpepper. `frágil` (repo personal, aunque con 103 stars y ring 1 en el catálogo). BSD-3-Clause, fork de `ppaml-op3/iracket`. Instalación: `raco pkg install iracket` + `raco iracket install`; prerrequisito ZeroMQ.
- [IRacket: Racket Kernel for Jupyter — doc oficial](https://docs.racket-lang.org/iracket/index.html) — `estable` (docs.racket-lang.org). Fuente canónica de `#lang iracket/lang #:require lang-mod [#:reader reader-mod]`.
- [`examples/getting-started.ipynb`](https://github.com/rmculpepper/iracket/blob/master/examples/getting-started.ipynb) — `frágil`. **Load-bearing**: es la única fuente que dice explícitamente que iRacket es un REPL y no soporta `#lang` de notebook completo. Backup Wayback pendiente de generar antes de publicar.
- [`iracket` en el catálogo de paquetes de Racket](https://pkgs.racket-lang.org/package/iracket) — `estable`. Ring 1, build y tests verdes al 2026-07-16; «Last edited» 2019-11-06.

**Racket / DrRacket**
- [Racket — sitio oficial](https://racket-lang.org/) — `estable`.
- [Racket — Download](https://racket-lang.org/download/) — `estable`. Versión 9.2 (mayo 2026).
- [PPA de Racket — equipo PLT en Launchpad](https://launchpad.net/~plt/+archive/ubuntu/racket) — `estable` (launchpad.net). Racket 9.1 en Questing/Noble/Jammy; 8.1 es el techo para Bionic 18.04.
- [Homebrew cask `racket`](https://formulae.brew.sh/cask/racket) — `estable`. `brew install --cask racket`, v9.2.
- [DrRacket — Programming Environment](https://docs.racket-lang.org/drracket/) — `estable`.
- [DrRacket — 1.1 Buttons](https://docs.racket-lang.org/drracket/buttons.html) — `estable`. **Load-bearing**: el dato de que `Step` sólo aparece en los teaching languages de HTDP y `Debug` sólo fuera de ellos.
- [The Stepper](https://docs.racket-lang.org/stepper/index.html) — `estable`.
- [The Racket Guide — 7.1 Contracts and Boundaries](https://docs.racket-lang.org/guide/contract-boundaries.html) y [Reference — 8 Contracts](https://docs.racket-lang.org/reference/contracts.html) — `estable`. Los contratos son del lenguaje, no un panel de DrRacket.
- ❌ *Descartada*: `community.chocolatey.org/packages/racket` — HTTP 403 a fetch automatizado, su API OData también, y sin snapshot en Wayback. No se cita.

**Jupyter**
- [Project Jupyter](https://jupyter.org/) — `estable`.
- [Jupyter Documentation — Kernels](https://docs.jupyter.org/en/latest/projects/kernels.html) — `estable`. Definición canónica de «kernel».

**Libros**
- [*How to Design Programs, Second Edition*](https://htdp.org/) — Felleisen, Findler, Flatt & Krishnamurthi. `estable`. Edición en línea liberada 2024-11-06, copyright 2014, MIT Press, CC BY-NC-ND. ⚠️ La bibliografía anterior decía «2.ª ed. 2018»: **no pude verificar ese año** (mitpress.mit.edu devuelve 403). Se cita la edición en línea, que sí es verificable.
  - [Preface](https://htdp.org/2024-11-6/Book/part_preface.html) — `estable`. «We have therefore created DrRacket, a programming environment for novices»; BSL / ISL / `*SL`.
  - [1.ª edición en Internet Archive](https://archive.org/details/howtodesignprogr0000unse_t5c9) — `estable`. MIT Press, 2001, ISBN 0262062186. Préstamo digital controlado. No es la edición citada.
- [[tr-03]] — SICP. Abelson & Sussman, MIT Press, 2.ª ed., 1996.
  - [1.ª edición en Internet Archive](https://archive.org/details/structureinterpr00abel) — `estable`. Abelson, Sussman & Sussman, MIT Press / McGraw-Hill, 1985, ISBN 0262010771. Préstamo digital controlado. No es la edición citada.
- Cross-link [[A2-06]] (sicp-spanish), [[K-01]] (DMOJ online judge para la materia).

**Imágenes:**
- _Crear_: screenshot del Jupyter Notebook con celdas de Scheme y resultados (~15 min).
- _Crear_: el `Vagrantfile` mínimo en una caja (~10 min).
- _Crear_: comparación side-by-side: DrRacket (escritorio) vs Jupyter+iRacket (navegador) (~20 min).

**Tags propuestos:** `['Racket', 'DrRacket', 'Jupyter', 'iRacket', 'Scheme', 'Vagrant', 'enseñanza']`

**Estado actual:** **POC funcional** (FIXME pendiente en la sección "conceptos de Jupyter" del repo), y ahora además **prosa completa escrita contra el outline de 8 puntos** (~1750 palabras), citando **únicamente** las fuentes ya listadas en la bibliografía: el repo del POC, racket-lang.org, la doc de DrRacket, iRacket de Ryan Culpepper, Project Jupyter, *How to Design Programs* y [[tr-03]].

Quedaron **once huecos** (🕳️) que necesitan a César. Este draft parece un post de tema público pero es sobre **su propio POC y su propia experiencia docente**, y casi nada de eso está escrito en el draft: en qué materia/institución y en qué año se usó, cuántos estudiantes, si el POC llegó a correr en un cuatrimestre real o quedó en prueba, la anécdota de la instalación de DrRacket que motivó todo, el motivo real de elegir Ubuntu y no Debian, qué era el FIXME de «conceptos de Jupyter», la reacción de los estudiantes al primer notebook, si alguno pidió saltar a DrRacket, cuál es el flujo que recomienda hoy, y la relación con [[K-01]] (DMOJ). La prosa está escrita *alrededor* de los huecos: el encuadre técnico y las transiciones están, el recuerdo se pide.

Quedaron **ocho marcas `[VERIFICAR:]`**, casi todas contra el README del repo y contra la doc de iRacket: si el repo efectivamente trae Vagrantfile + playbook Ansible (el seed lo describe como repo «HTML», último push 2020-08-04, lo cual sugiere que puede ser sobre todo documentación), la versión exacta de Ubuntu/Racket/Jupyter que fija el POC, los comandos exactos de instalación del kernel, el nombre del paquete en Chocolatey y en Homebrew, si iRacket expone `#lang scheme`/`#lang racket` o R5RS, qué se rompió del kernel desde 2020, y si HTDP recomienda DrRacket explícitamente.

**Nota de conflicto con la regla de no-inventar:** el Hook afirma en primera persona que ésta es «la mejor onboarding curve que encontré para enseñar funcional» y el Concepto habla de recetas Windows 10 / Ubuntu 18.04 como si el uso docente estuviese consumado. No toqué ninguna de las dos secciones, pero la prosa no repite esas afirmaciones en voz del autor: las deja como huecos para que César las confirme o las baje de tono. Si el POC nunca llegó al aula, el post sigue siendo escribible —cambia de «lo que me funcionó» a «lo que armé y por qué»— pero hay que reescribir el cierre.

Pendiente al publicar: resolver `[[A2-01]]`, `[[A2-06]]`, `[[E-12]]`, `[[K-01]]` y `[[K-02]]` a URLs reales; producir las tres imágenes de la sección **Imágenes**; y decidir si vale la pena revalidar el POC contra un Racket y un Ubuntu actuales antes de publicarlo, o si el post se publica explícitamente como registro de 2020.

---

## Borrador de prosa

Querés enseñar programación funcional. Tenés un cuatrimestre, un laboratorio, y estudiantes que nunca en su vida vieron un paréntesis en esa posición. Y antes de poder mostrarles una sola función recursiva, tenés que pedirles que instalen un IDE que no conocen, para un lenguaje que no conocen, con un modelo de trabajo —editor arriba, REPL abajo, `Run` en el medio— que tampoco conocen. Son tres cosas nuevas al mismo tiempo, y ninguna de las tres es la que querías enseñar.

Lo que hice en su momento fue separar los problemas: dejar el lenguaje nuevo y sacar todo lo demás. El estudiante abre el navegador, ve un Jupyter Notebook —que ya vio en otra materia—, escribe Scheme en una celda, aprieta `Shift+Enter`, y el resultado aparece abajo. Mismo workflow de siempre, lenguaje nuevo. Todo el setup vive en una máquina virtual: Racket, Jupyter y el kernel `iracket` ya instalados y andando. El POC está publicado[^repo].

### Dos barreras que no conviene sumar

La barrera del lenguaje es la que querés que enfrenten. Es la materia. Que el estudiante se pelee con la recursión, con que no hay asignación, con que una función es un valor como cualquier otro: perfecto, eso es el aprendizaje.

La barrera del entorno no es la materia. Es peaje. Y es cara: en un laboratorio con máquinas heterogéneas, la primera clase se te va en versiones, permisos, paths y en el estudiante que instaló otra cosa. Peor todavía, ese peaje se cobra justo en el momento de mayor fragilidad, cuando el estudiante todavía no tiene ninguna razón para creer que del otro lado hay algo que vale la pena.

El razonamiento fue: si sólo puedo eliminar una de las dos barreras, elimino la que no me interesa. La del entorno.

> 🕳️ **HUECO — necesita a César:** ¿en qué materia, institución y año fue esto? ¿Fue una materia tuya, una ayudantía, un curso propio? Una o dos frases alcanzan para encuadrar el post.

> 🕳️ **HUECO — necesita a César:** ¿hay una anécdota concreta de instalación de DrRacket que haya sido la gota que rebalsó el vaso? (la máquina del laboratorio sin permisos de administrador, el estudiante con Windows en una versión rara, el antivirus institucional…). El post gana muchísimo si el problema arranca en una escena real y no en una generalidad.

### Por qué un notebook y no un IDE

DrRacket es un buen ambiente[^drracket]. No lo eliminé por malo; lo eliminé por *nuevo*. Y acá está el punto que me parece el corazón del asunto: la familiaridad es un recurso didáctico, y es un recurso que ya tenías comprado sin darte cuenta.

Si tus estudiantes vieron notebooks en alguna materia de Python —y a esta altura es lo más probable[^jupyter]— entonces el modelo mental «celda / ejecutar / resultado debajo» ya está instalado en sus cabezas. Es gratis. Usarlo significa que la única cosa desconocida en la pantalla es el código, que es exactamente donde querés que miren.

Es lo contrario de lo que hace la tradición Racket, que tiene una postura pedagógica fuerte y explícita. El prefacio de *How to Design Programs* no deja lugar a dudas: «We have therefore created DrRacket, a programming environment for novices»[^htdp_pref]. El ambiente no es un accesorio del método, es parte del método — y por eso el libro viene con lenguajes por niveles que crecen con el estudiante: *Beginning Student Language* (BSL), descripto en el prefacio como «essentially the foreign language that students acquire in pre-algebra courses», y de ahí en adelante *Intermediate Student Language* y los dialectos avanzados, agrupados bajo el nombre `*SL`[^htdp_pref]. No estoy discutiendo con eso. Estoy diciendo que ese diseño supone que podés invertir tiempo en el ambiente, y hay contextos donde no podés.

### iRacket: el kernel que hace posible el truco

La pieza que hace que todo esto funcione es `iracket`, el kernel de Jupyter para Racket, de Ryan Culpepper[^iracket]. La definición no es mía: la documentación oficial de Jupyter dice que los kernels son «programming language specific processes that run independently and interact with the Jupyter Applications and their user interfaces»[^jupyter_kernels]. Es decir, el proceso que recibe el texto de la celda, lo evalúa, y devuelve el resultado para que el navegador lo muestre. Jupyter no sabe nada de Racket; el kernel sí.

La instalación son dos pasos, y no más que dos: `raco pkg install iracket` instala el paquete, y `raco iracket install` lo registra ante Jupyter[^iracket]. El único prerrequisito propio es ZeroMQ, que el README resuelve por plataforma: `libzmq5` en Debian/Ubuntu, `zeromq` en RedHat/Fedora, `brew install zmq` en macOS, y en Windows se instala solo vía `zeromq-r-lib` de Racket[^iracket]. Hecho eso, se arranca `jupyter notebook` normalmente y Racket aparece en el menú de *New* como aparece Python.

Ahora, una advertencia importante para un post que promete «enseñar Scheme», y que me tomó por sorpresa al releer la documentación: **iRacket no es un `#lang` por celda.** El notebook de ejemplo del repo lo dice sin vueltas: «IRacket is like a REPL; it doesn't support treating the whole notebook as one module, so we can't use `#lang slideshow`»[^iracket_ejemplo]. Las celdas son formas de nivel superior evaluadas en un namespace, no un módulo. Lo que sí existe es una declaración especial, `#lang iracket/lang #:require lang-mod [#:reader reader-mod]`, que «creates a new empty namespace, populates it by requiring lang-mod (a module path), and installs it as the kernel's current namespace, used for evaluation»[^iracket_docs]. Tiene que ir primero en la celda, sin nada antes —ni comentarios ni espacios—, afecta al resto de esa celda y a las evaluaciones siguientes, y puede aparecer en más de una celda, no sólo en la primera[^iracket_docs]. El ejemplo que da la doc es `#lang iracket/lang #:require racket/base #:reader scribble/reader`.

O sea: lo que el estudiante escribe en una celda vacía es Racket, no Scheme R5RS. El metadato del kernel en el notebook de ejemplo lo confirma de costado — `kernelspec.name: "Racket"`, `language_info.name: "Racket"`, `pygments_lexer: "racket"` — con la única guiñada a Scheme en `codemirror_mode: "scheme"`, que es sólo el resaltador de sintaxis del editor[^iracket_ejemplo].

[VERIFICAR: si `#lang iracket/lang #:require r5rs` (o el módulo que corresponda) efectivamente da un dialecto Scheme usable en las celdas. La doc de iRacket documenta el mecanismo pero **no da ningún ejemplo con Scheme/R5RS** — su único ejemplo es `racket/base` + `scribble/reader`, y no menciona R5RS en ninguna parte. Busqué en docs.racket-lang.org/iracket/, en el README y en el notebook `examples/getting-started.ipynb` del repo, sin resultado. Hay que probarlo en una VM antes de afirmar nada: es la pregunta que decide si el post se llama «enseñar Scheme» o «enseñar Racket».]

[VERIFICAR: compatibilidad con Jupyter/JupyterLab actuales. Lo que sí pude confirmar: el catálogo de paquetes de Racket muestra `iracket` en ring 1, con «Compiled successfully» y «Tests succeeded» al chequeo del 2026-07-16, autor `ryanc`, dependencias `base`, `zeromq-r-lib`, `sandbox-lib`, `uuid`, `sha`[^iracket_pkg]. Pero el paquete figura «Last edited Wednesday, November 6th, 2019», el notebook de ejemplo declara `version: "6.11"` de Racket[^iracket_ejemplo], y **ni el README ni la doc declaran versión mínima de Racket ni de Jupyter, ni dicen una palabra sobre JupyterLab** (busqué explícitamente en ambos). El build verde prueba que compila, no que el kernel converse con un JupyterLab de 2026. Hay que probarlo y decir en qué versiones anduvo.]

### La VM: el setup como artefacto reproducible

El otro lado del POC es que nada de esto se instala a mano. La receta vive en una máquina virtual que se levanta con un comando y llega andando: Ubuntu, Racket, Jupyter, `iracket`, y el servicio escuchando para que el estudiante sólo tenga que abrir el navegador. Son tres pasos: clonar el repo, `vagrant up`, y abrir `http://127.0.0.1:8888/`[^repo].

> **Corrección contra el repo (2026-07):** el outline decía «Vagrantfile + playbook de Ansible». **No hay Ansible en el repo.** El árbol tiene varios `Vagrantfile` (uno estándar más variantes de 32 y 64 bits), guías de instalación en Markdown para Windows 10, Ubuntu 18.04 y Chocolatey, y los directorios `notebooks/`, `slides/`, `ejercicios-resueltos/pdf` y `teach-yourself-scheme-in-fixnum-days`[^repo]. El «97% HTML» que reporta GitHub —y que el seed leyó como «repo de documentación»— es casi con seguridad el HTML embebido en los notebooks, no páginas escritas a mano. Conviene describir el mecanismo como Vagrant + provisioning por shell y **no** invocar el patrón Vagrant+Ansible de [[E-12]] como si estuviera acá: el paralelo es conceptual, no literal. VirtualBox aparece como requisito de virtualización.

[VERIFICAR: versiones exactas fijadas en el POC. Confirmado desde el repo: Ubuntu 18.04 (Bionic), VirtualBox como provider, puerto 8888. **No pude confirmar** desde la vista de GitHub la versión de Racket ni la de Jupyter que fija el provisioning, ni si Jupyter queda con token/password o abierto — hay que abrir el/los `Vagrantfile` y el script de provisioning en el clon local y leerlos. Dato de contexto: el notebook de ejemplo de iRacket declara Racket `6.11`[^iracket_ejemplo], que es de la época, pero eso no dice nada sobre lo que fija este POC.]

Este patrón —la receta de infraestructura como el entregable, no como el paso previo— es el mismo que uso en otros lados y del que hablo en [[E-12]]. Lo interesante en contexto docente es que el `Vagrantfile` deja de ser una herramienta de DevOps y pasa a ser material de cátedra: es la versión ejecutable de la guía de instalación que nadie lee.

> 🕳️ **HUECO — necesita a César:** el outline dice «justifico por qué elegí Ubuntu y no Debian». ¿Cuál fue el motivo real? ¿Paquetes de Racket más nuevos, box de Vagrant mejor mantenida, que era lo que ya usaban en el laboratorio, familiaridad tuya? Una frase honesta —incluso si el motivo fue «era lo que tenía a mano»— vale más que una racionalización.

> 🕳️ **HUECO — necesita a César:** ¿la VM la corrían los estudiantes en sus máquinas, o estaba levantada en un servidor y se conectaban por red? Cambia por completo el post: en el segundo caso el tema es multiusuario, y hay que hablar de eso.

### Para los que no quieren VM

No todos van a querer bajar una VM de varios gigas, y es razonable. El POC documenta también la instalación nativa: Chocolatey en Windows 10, `apt` en Ubuntu, Homebrew en macOS[^repo].

En macOS es un cask, no una fórmula: `brew install --cask racket`, hoy en la versión 9.2[^brew].

En Ubuntu, el camino de `apt` tiene una vuelta que conviene decirle al estudiante de entrada. La página oficial de descargas avisa que «Racket may also be available through your distribution's package manager, although it may be older than the latest Racket version», y ofrece como alternativa el PPA del equipo PLT[^racket_download]. Ese PPA da hoy Racket 9.1 para Questing (25.10), Noble (24.04) y Jammy (22.04) —y versiones viejas (8.6, 8.5, 8.3, 8.1) para Focal, Bionic, Xenial y Trusty—, con `sudo add-apt-repository ppa:plt/racket` y `sudo apt update`[^ppa]. Para el Bionic 18.04 del POC, el techo del PPA es 8.1.

[VERIFICAR: nombre exacto y estado del paquete de Racket en Chocolatey. Busqué la página `community.chocolatey.org/packages/racket` y **el sitio devuelve HTTP 403 a fetch automatizado**, igual que su API OData (`/api/v2/Packages()`); tampoco hay snapshot en Wayback (`archive.org/wayback/available` responde `has_archived_snapshot: false`). Los resultados de búsqueda sugieren id `racket` y versión 8.18.0, pero **no abrí esa página, así que no lo escribo como hecho**. Verificar corriendo `choco search racket` o `choco info racket` en una Windows con Chocolatey instalado, que además es el chequeo que vale.]

[VERIFICAR: si la versión de Racket que da `apt` alcanza para iRacket. No es contestable hoy: iRacket **no declara versión mínima de Racket** en ningún lado (ver el VERIFICAR de compatibilidad más arriba). Sin ese número, «alcanza o no alcanza» sólo se resuelve probando.]

Mi recomendación práctica, igual, es dar la VM como camino por omisión y la instalación nativa como camino para el que ya se anima. No porque la nativa sea mala, sino porque la VM te da algo que la nativa no: cuando algo se rompe, la respuesta es `vagrant destroy && vagrant up` y seguimos con la clase.

### El primer notebook

La primera celda de la primera clase no debería enseñar nada. Debería demostrar que la máquina responde. `(+ 1 2)`, `Shift+Enter`, `3`.

Después sí: definir una función, evaluarla, definir otra que use a la primera, y ver aparecer los resultados uno debajo del otro. El notebook queda como un documento leíble de arriba hacia abajo, con el texto explicativo intercalado entre el código —que es, dicho sea de paso, bastante parecido al espíritu del libro con el que uno enseña esto[^sicp], donde el programa y su explicación van juntos.

La reacción que buscaba era exactamente ésta: «ah, esto es Python pero con paréntesis». Es una frase técnicamente falsa y didácticamente perfecta. Falsa porque las diferencias entre Scheme y Python son justo lo que vas a pasar el cuatrimestre desarmando. Perfecta porque baja la ansiedad a cero en los primeros diez minutos, y a partir de ahí ya se puede trabajar.

> 🕳️ **HUECO — necesita a César:** ¿qué dijeron realmente los estudiantes la primera vez? ¿Hubo una frase textual? Si no la hay, decilo y bajo el párrafo de arriba a hipótesis en vez de recuerdo.

> 🕳️ **HUECO — necesita a César:** ¿cuál fue el primer notebook que armaste? ¿Qué funciones tenía? Si sobrevive el archivo, es la mejor imagen del post.

> 🕳️ **HUECO — necesita a César:** en el repo hay un FIXME en la sección «conceptos de Jupyter». ¿Qué ibas a escribir ahí? ¿Qué es lo mínimo de Jupyter que un estudiante necesita entender —kernel, estado compartido entre celdas, orden de ejecución— para no clavarse?

### Lo que perdés

Sería deshonesto vender esto como si no costara nada. DrRacket trae cosas que el notebook no replica, y la doc oficial les pone nombre exacto[^drracket_botones]:

- El **Stepper** (botón `Step`), que la doc describe como un «algebraic stepper, a tool which proceeds through the evaluation of a set of definitions and expressions, one step at a time»[^stepper]. Acá hay un detalle que le da vuelta el argumento del post: el botón `Step` «appears only for the How to Design Programs teaching languages Beginning Student through Intermediate Student with Lambda»[^drracket_botones]. El stepper —la herramienta más didáctica de todo DrRacket— **existe únicamente en los lenguajes de HTDP**, no en `#lang racket`. Así que no es sólo que iRacket no lo replique: es que el stepper y el notebook viven en mundos distintos por diseño.
- El **Debugger** (botón `Debug`), que es simétrico: «does not appear for the How to Design Programs teaching languages» y arranca «a more conventional stepping debugger»[^drracket_botones]. Está documentado como «Graphical Debugging Interface», con panel de stack y soporte multi-archivo[^drracket].
- **Check Syntax**, que anota el texto del programa y además corre solo mientras editás, con un indicador de estado en el ángulo inferior derecho de la ventana[^drracket_botones].
- El **Module Browser** y la selección de lenguaje («Choosing a Language»)[^drracket].

Corrijo de paso algo que traía el outline: hablé de un «visualizador de contratos» de DrRacket, y **no encontré tal herramienta en la doc de DrRacket**. Los contratos son una construcción del lenguaje —con su sistema de *blame* documentado en la guía y la referencia de Racket[^contratos]—, no un panel del IDE. Si el post lo menciona, que sea como feature del lenguaje, no como algo que se pierde al salir de DrRacket.

[VERIFICAR: cuáles de estas herramientas tienen algún equivalente vía iRacket. Revisé el README, `docs.racket-lang.org/iracket/` y el notebook de ejemplo: **ninguno menciona stepper, debugger ni Check Syntax**, lo que sugiere fuertemente que no hay equivalente, pero «no está documentado» no es lo mismo que «no existe» y no lo voy a afirmar sin probarlo. Confirmar en la VM.]

Y hay una pérdida más sutil, que es la del estado. En un notebook el orden en que ejecutaste las celdas importa, y no siempre coincide con el orden en que están escritas. Un estudiante que redefine una función arriba y no vuelve a correr lo de abajo se encuentra con un resultado que no se explica por el código que tiene en pantalla. Es una fuente de confusión clásica, y en una materia donde el punto es razonar sobre el modelo de evaluación, es peor que clásica: es contraproducente.

Por eso el notebook no es el destino, es la puerta. En algún momento del cuatrimestre conviene hacer el salto a DrRacket, y sospecho que el momento correcto es cuando el estudiante ya tiene una razón para querer la herramienta —cuando necesita el stepper, o cuando el programa dejó de entrar en una celda.

> 🕳️ **HUECO — necesita a César:** ¿hubo un salto a DrRacket en la práctica? ¿En qué momento del cuatrimestre, y disparado por qué? ¿O el notebook alcanzó de punta a punta?

> 🕳️ **HUECO — necesita a César:** ¿algún estudiante pidió DrRacket por su cuenta, o al revés, alguno se resistió a dejar el notebook?

### El flujo que recomiendo

> 🕳️ **HUECO — necesita a César:** el outline cierra con «cuál es el flujo que recomiendo después de un cuatrimestre de uso real». Hacen falta dos cosas: (a) ¿hubo cuatrimestre de uso real, o el POC quedó en prueba? y (b) si lo hubo, ¿cuál es la recomendación en tres pasos? Si no lo hubo, el cierre se reescribe como «lo que armaría hoy» y el post no pierde nada, pero el Hook hay que ajustarlo.

> 🕳️ **HUECO — necesita a César:** ¿esto se combinó con el online judge del que hablo en [[K-01]]? ¿El estudiante exploraba en el notebook y entregaba en el judge, o eran mundos separados?

Lo que sí puedo dejar dicho, con POC o sin él, es la idea que me quedó y que uso en otros contextos: **cuando enseñás algo difícil, gastá tu presupuesto de novedad en una sola cosa**. Todo lo demás que aparezca en la pantalla debería ser algo que el estudiante ya sepa manejar. El paréntesis es la novedad. El botón de `Run` no.

Si te interesa el lado del contenido más que el del setup, en [[A2-01]] hablo del libro con el que se enseña esto, y en [[A2-06]] de por qué me metí a traducirlo.

[^repo]: Repo del POC: [CesarBallardini/programacion-drracket](https://github.com/CesarBallardini/programacion-drracket).
[^racket]: [Racket — sitio oficial](https://racket-lang.org/).
[^racket_download]: [Racket — Download](https://racket-lang.org/download/) — versión 9.2 (mayo 2026); nota sobre paquetes de distribución posiblemente desactualizados y enlace al PPA de Ubuntu.
[^ppa]: [PPA de Racket — equipo PLT en Launchpad](https://launchpad.net/~plt/+archive/ubuntu/racket) — Racket 9.1 para Questing/Noble/Jammy; 8.6, 8.5, 8.3 y 8.1 para Focal, Bionic, Xenial y Trusty.
[^brew]: [Homebrew cask `racket`](https://formulae.brew.sh/cask/racket) — `brew install --cask racket`, versión 9.2.
[^drracket]: [DrRacket — Programming Environment](https://docs.racket-lang.org/drracket/) — secciones «1.2 Choosing a Language», «1.8 Graphical Debugging Interface», «1.9 The Module Browser».
[^drracket_botones]: [DrRacket — 1.1 Buttons](https://docs.racket-lang.org/drracket/buttons.html) — descripciones exactas de los botones `Run`, `Break`, `Step`, `Check Syntax` y `Debug`.
[^stepper]: [The Stepper](https://docs.racket-lang.org/stepper/index.html) — «algebraic stepper»; disponible en los niveles Beginning Student e Intermediate Student.
[^contratos]: [The Racket Guide — 7.1 Contracts and Boundaries](https://docs.racket-lang.org/guide/contract-boundaries.html) y [The Racket Reference — 8 Contracts](https://docs.racket-lang.org/reference/contracts.html).
[^iracket]: [iRacket](https://github.com/rmculpepper/iracket) — kernel de Jupyter para Racket, de Ryan Culpepper. BSD-3-Clause; fork de `ppaml-op3/iracket`. Instalación: `raco pkg install iracket` + `raco iracket install`; prerrequisito ZeroMQ (`libzmq5` en Debian/Ubuntu).
[^iracket_docs]: [IRacket: Racket Kernel for Jupyter](https://docs.racket-lang.org/iracket/index.html) — documentación oficial; define `#lang iracket/lang #:require lang-mod [#:reader reader-mod]` y `raco iracket install --untrusted`.
[^iracket_ejemplo]: [`examples/getting-started.ipynb`](https://github.com/rmculpepper/iracket/blob/master/examples/getting-started.ipynb) ([raw](https://raw.githubusercontent.com/rmculpepper/iracket/master/examples/getting-started.ipynb)) — notebook de ejemplo del repo; sigue el tutorial *Quick* de Racket, declara `kernelspec.name: "Racket"` y Racket `6.11`, y advierte que «IRacket is like a REPL; it doesn't support treating the whole notebook as one module».
[^iracket_pkg]: [`iracket` en el catálogo de paquetes de Racket](https://pkgs.racket-lang.org/package/iracket) — autor `ryanc`, ring 1, «Compiled successfully» / «Tests succeeded»; «Last edited Wednesday, November 6th, 2019».
[^jupyter]: [Project Jupyter](https://jupyter.org/).
[^jupyter_kernels]: [Jupyter Documentation — Kernels](https://docs.jupyter.org/en/latest/projects/kernels.html) — «Kernels are programming language specific processes that run independently and interact with the Jupyter Applications and their user interfaces».
[^htdp]: Matthias Felleisen, Robert Bruce Findler, Matthew Flatt & Shriram Krishnamurthi, *How to Design Programs, Second Edition* — [htdp.org](https://htdp.org/). Edición en línea liberada el 2024-11-06, copyright 2014, distribuida por MIT Press bajo CC BY-NC-ND.
[^htdp_pref]: [*How to Design Programs*, 2.ª ed. — Preface](https://htdp.org/2024-11-6/Book/part_preface.html) — «We have therefore created DrRacket, a programming environment for novices»; descripción de BSL, ISL y `*SL`.
[^htdp_ia]: [*How to Design Programs: An Introduction to Programming and Computing*](https://archive.org/details/howtodesignprogr0000unse_t5c9) en Internet Archive — **1.ª edición**, MIT Press, 2001, ISBN 0262062186. Préstamo digital controlado. (No es la 2.ª edición que se cita arriba.)
[^sicp]: Harold Abelson & Gerald Jay Sussman, *Structure and Interpretation of Computer Programs*, MIT Press, 2.ª ed., 1996. [[tr-03]]
[^sicp_ia]: [*Structure and Interpretation of Computer Programs*](https://archive.org/details/structureinterpr00abel) en Internet Archive — **1.ª edición**, Abelson, Sussman & Sussman, MIT Press / McGraw-Hill, 1985, ISBN 0262010771. Préstamo digital controlado. (La edición citada en el post es la 2.ª, de 1996.)

