### A2-07 — DrRacket + Jupyter + iRacket: Scheme didáctico en el navegador con una VM

- **Archivo seed (repo POC):** [github.com/CesarBallardini/programacion-drracket](https://github.com/CesarBallardini/programacion-drracket) — HTML, 5 stars, último push 2020-08-04
- **Slug propuesto:** `scheme-en-el-navegador-iracket`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-scheme-en-el-navegador-iracket/index.md`
- **Serie:** A2 — complementa [[A2-06]] y [[A2-01]]; cruza con [[E-12]] y [[K-02]] por el ángulo docente
- **Cross-links:** lleva a [[A2-06]] (sicp-spanish), [[A2-01]] (SICP), [[E-12]] (patrón Vagrant+Ansible), [[K-01]] (online judge para la materia)
- **Idioma:** es
- **Madurez:** **complete-poc** para el setup; el material didáctico marcado FIXME en "conceptos de Jupyter"
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

**Bibliografía:**
- Repo del POC: [CesarBallardini/programacion-drracket](https://github.com/CesarBallardini/programacion-drracket).
- [Racket — sitio oficial](https://racket-lang.org/).
- [DrRacket — Programming Environment](https://docs.racket-lang.org/drracket/).
- [iRacket en GitHub](https://github.com/rmculpepper/iracket) — Ryan Culpepper.
- [Project Jupyter](https://jupyter.org/).
- [Matthias Felleisen et al, *How to Design Programs*, MIT Press 2nd ed. 2018](https://htdp.org/) — el libro de la "filosofía Racket" para enseñar programación.
- [[tr-03]] — SICP.
- Cross-link [[A2-06]] (sicp-spanish), [[K-01]] (DMOJ online judge para la materia).

**Imágenes:**
- _Crear_: screenshot del Jupyter Notebook con celdas de Scheme y resultados (~15 min).
- _Crear_: el `Vagrantfile` mínimo en una caja (~10 min).
- _Crear_: comparación side-by-side: DrRacket (escritorio) vs Jupyter+iRacket (navegador) (~20 min).

**Tags propuestos:** `['Racket', 'DrRacket', 'Jupyter', 'iRacket', 'Scheme', 'Vagrant', 'enseñanza']`

**Estado actual:** **POC funcional**, FIXME pendiente en la sección "conceptos de Jupyter". El post se puede escribir en una sola sesión leyendo el README.

