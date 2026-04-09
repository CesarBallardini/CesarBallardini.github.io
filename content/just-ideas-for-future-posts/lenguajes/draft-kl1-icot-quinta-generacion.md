### A1-08 — Resucitando KL1 (Kernel Language 1) y el proyecto japonés de 5ta generación con `kl1c`

- **Archivo seed (repo POC):** [github.com/CesarBallardini/kl1c](https://github.com/CesarBallardini/kl1c) — Makefile, 6 stars, último push 2023-09-27
- **Slug propuesto:** `kl1-icot-quinta-generacion`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-kl1-icot-quinta-generacion/index.md`
- **Serie:** A1 — pero cruza fuerte con [[H-06]] (parábola del legacy) y [[D-03]] (Turing)
- **Cross-links:** lleva a [[A1-04]] (Modula-2: otra utopía de los 80), [[A1-05]] (Clipper: el otro extremo de los 80), [[H-06]] (la parábola); puede inspirar una entrada propia sobre *concurrent logic programming*
- **Idioma:** es
- **Madurez:** **complete-poc** — el repo construye `.deb` empaquetados de KLIC sobre Vagrant + Ubuntu 16.04 i686 Trusty, y los artefactos `.deb` están versionados en el repo.
- **Length target:** medium-long (2000-3000 palabras) — es un post denso por la historia detrás

**Concepto:** entre 1982 y 1992 Japón gastó **el equivalente a 850 millones de dólares** en el *Fifth Generation Computer Systems Project* (5GCS), una apuesta a redefinir la computación alrededor de **programación lógica concurrente** corriendo en hardware paralelo dedicado (las máquinas PIM). El lenguaje del proyecto fue **KL1 (Kernel Language 1)**, descendiente de Concurrent Prolog y antecesor conceptual de cosas que hoy hacen Erlang/Elixir. El proyecto "fracasó" en términos de su objetivo declarado (no produjimos máquinas pensantes), pero produjo trabajo técnico enorme y sigue siendo una de las grandes ucronías de la computación. Mi POC `kl1c` empaqueta KLIC (la implementación portable en C) en un Vagrant moderno para que se pueda *correr* hoy.

**Hook:** "en los años 80, mientras Estados Unidos discutía si Lisp o C, Japón apostaba 850 millones de dólares a algo completamente distinto: programación lógica concurrente sobre hardware paralelo dedicado. El lenguaje se llamaba KL1. Las máquinas se llamaban PIM. El proyecto se cerró en 1992 sin haber cambiado el mundo. Pero el código sobrevivió. En este post lo recompilamos en una notebook moderna y lo hacemos correr."

**Outline:**
1. ICOT y el 5GCS: contexto político (la respuesta japonesa al miedo de los 80 sobre IA en EE.UU.), las metas declaradas, la apuesta tecnológica.
2. KL1 como lenguaje: qué hereda de Prolog, qué hereda de Concurrent Prolog y GHC (Guarded Horn Clauses), qué le agrega Ueda. La idea de "guardas" y por qué la concurrencia logica importa.
3. Las máquinas PIM (Parallel Inference Machine): hardware dedicado a inferencia, el sueño paralelo japonés.
4. Por qué "fracasó" — y por qué la palabra fracaso es injusta. Lo que sobrevivió: papers, librerías, la influencia indirecta sobre Erlang y los modelos modernos de actores.
5. KLIC — la implementación portable en C, mantenida después del cierre del proyecto. Cómo se obtiene en 2026 (los archivos del ICOT están preservados).
6. Mi POC `kl1c`: Vagrant + Ubuntu 16.04 i686 + scripts para construir los `.deb`. Por qué i686 (alguna dependencia de 32-bit ininstalable en 64-bit moderno).
7. Un "hello, concurrent world" en KL1: dos goals que se sincronizan por unificación de variables compartidas. El momento *aha*.
8. Cierre: lo que aprendí escribiendo el packaging — el legacy de un proyecto cerrado en 1992 sigue siendo recuperable si alguien se sienta tres tardes a hacerlo.

**Bibliografía:**
- Repo del POC: [CesarBallardini/kl1c](https://github.com/CesarBallardini/kl1c) — incluye bibliografía detallada en el README.
- [ICOT Free Software archives](http://www.icot.or.jp/ARCHIVE/HomePage-E.html) — el archivo oficial del proyecto, frágil pero existente.
- [Kazunori Ueda, *Logic/Constraint Programming and Concurrency: The Hard-Won Lessons of the Fifth Generation Computer Project*, Science of Computer Programming 2018](https://www.sciencedirect.com/science/article/pii/S0167642316301472) — el balance retrospectivo del propio Ueda.
- [Matthew M. Huntbach & Graem A. Ringwood, *Agent-Oriented Programming: From Prolog to Guarded Definite Clauses*, LNAI 1630, Springer 1999](https://link.springer.com/book/10.1007/3-540-46998-7) — el libro que conecta KL1 con sistemas multi-agente modernos.
- [Edward Feigenbaum & Pamela McCorduck, *The Fifth Generation: Artificial Intelligence and Japan's Computer Challenge to the World*, Addison-Wesley 1983](https://archive.org/details/fifthgenerationa00feig) — el libro alarmista de la época, hoy lectura histórica.
- [Edsger W Dijkstra, EWD472 — *On the foolishness of "natural language programming"*, 1978](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html) — citado en el README, contexto crítico.
- [Wikipedia — Fifth generation computer](https://en.wikipedia.org/wiki/Fifth_generation_computer).
- [GHC, KL1 y la familia de lenguajes en Wikipedia](https://en.wikipedia.org/wiki/Guarded_Horn_Clauses).
- [Joe Armstrong, *A History of Erlang*, HOPL III 2007](https://dl.acm.org/doi/10.1145/1238844.1238850) — para la conexión indirecta KL1 → Erlang.

**Imágenes:**
- _Wikimedia_: foto de una PIM (Parallel Inference Machine) — verificar disponibilidad.
- _Crear_: línea de tiempo 1982-1992 de los hitos del proyecto 5GCS (~1 hora).
- _Crear_: snippet de KL1 lado a lado con Prolog clásico y con Erlang, mostrando el parecido familiar (~30 min).
- _Crear_: foto del logo del ICOT (verificar derechos).

**Tags propuestos:** `['KL1', 'KLIC', 'ICOT', 'Quinta Generacion', 'Prolog concurrente', 'Japon', 'historia', 'Vagrant']`

**Estado actual:** **POC completo** en GitHub. El README del repo ya tiene gran parte de la bibliografía. El post se puede armar en 1-2 sesiones leyendo el paper de Ueda 2018 y reusando el README.

