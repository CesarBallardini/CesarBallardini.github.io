### A1-08 — Resucitando KL1 (Kernel Language 1) y el proyecto japonés de 5ta generación con `kl1c`

- **Archivo seed (repo POC):** [github.com/CesarBallardini/kl1c](https://github.com/CesarBallardini/kl1c) — Makefile, 6 stars, último push 2023-09-27
- **Slug propuesto:** `kl1-icot-quinta-generacion` — publicado como `content/es/posts/2026-07-12-kl1-icot-quinta-generacion/index.md`
- **Comando:** _no aplica — post ya publicado, este entry es para anclar el cross-link en el plan_
- **Serie:** A1 — pero cruza fuerte con [[H-06]] (parábola del legacy) y [[D-03]] (Turing)
- **Cross-links:** lleva a [[A1-04]] (Modula-2: otra utopía de los 80), [[A1-05]] (Clipper: el otro extremo de los 80), [[H-06]] (la parábola); puede inspirar una entrada propia sobre *concurrent logic programming*
- **Idioma:** es
- **Madurez:** **publicado** (2026-07-12)
- **Length target:** ya escrito (~2264 palabras, 11 min de lectura)

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

**Bibliografía (verificada contra el repo real y contra las fuentes primarias antes de publicar):**
- Repo del POC: [CesarBallardini/kl1c](https://github.com/CesarBallardini/kl1c).
- Kazunori Ueda, *Guarded Horn Clauses*, tesis de maestría, Universidad de Tokio, 1986 — [PDF](https://www.ueda.info.waseda.ac.jp/~ueda/pub/GHCthesis.pdf). El paper fundacional de GHC, antecesor inmediato de KL1 (no estaba en la bibliografía original del draft; se agregó al escribir el post).
- Matthew M Huntbach & Graem A Ringwood, *Agent-Oriented Programming: From Prolog to Guarded Definite Clauses*, LNAI 1630, Springer 1999 — [DOI 10.1007/3-540-47938-4](https://doi.org/10.1007/3-540-47938-4). **Corrección:** el DOI original del draft (`10.1007/3-540-46998-7`) estaba mal (no resuelve, 404 en Crossref); el correcto es `10.1007/3-540-47938-4`. La copia en archive.org que el README del repo cita (`archive.org/details/springer_10.1007-3-540-47938-4`) ya no existe (ítem marcado `dark` — probable takedown) — el post usa el DOI como referencia canónica más un mirror de texto completo en [theswissbay.ch](https://theswissbay.ch/pdf/Gentoomen%20Library/Artificial%20Intelligence/General/Agent-Oriented%20Programming%20-%20From%20Prolog%20to%20Guarded%20Definite%20Clauses%20-%20Matthew%20M.%20Huntbach.pdf) (mirror personal, frágil).
- Edward Feigenbaum & Pamela McCorduck, *The Fifth Generation*, Addison-Wesley 1983 — [préstamo digital controlado en archive.org](https://archive.org/details/fifthgenerationa00feig). Verificado, sin cambios.
- Kazunori Ueda, *Logic/Constraint Programming and Concurrency: The Hard-Won Lessons of the Fifth Generation Computer Project*, Science of Computer Programming vol. 164 (2018) — [DOI 10.1016/j.scico.2017.06.002](https://doi.org/10.1016/j.scico.2017.06.002). Verificado vía Crossref (ScienceDirect bloquea fetch directo, HTTP 403).
- Joe Armstrong, *A History of Erlang*, HOPL III 2007 — [DOI 10.1145/1238844.1238850](https://doi.org/10.1145/1238844.1238850). Verificado.
- Takashi Chikayama, *KLIC: A Portable Parallel Implementation of a Concurrent Logic Programming Language*, LNCS, Springer 1996 — [DOI 10.1007/BFb0023068](https://doi.org/10.1007/BFb0023068). No estaba en la bibliografía original del draft; el PDF vive en `biblio/` dentro del propio repo del POC — es la fuente primaria de KLIC, se agregó al leer el repo.
- Edsger W Dijkstra, EWD472 — [*Guarded commands, non-determinacy and formal derivation of programs*](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html), 1975. **Corrección importante:** el draft original citaba mal este EWD — decía "EWD472 — *On the foolishness of 'natural language programming'*" pero linkeaba a la URL de EWD667 (que sí tiene ese título). El README real del repo cita EWD472 correctamente con su título real ("guarded commands"), que además es temáticamente más relevante para este post (es el origen conceptual de la idea de "guarda" que GHC/KL1 heredan) — el post usa EWD472, no EWD667.
- ICOT Free Software archives: el link original del draft (`icot.or.jp/ARCHIVE/HomePage-E.html`) está caído (404). El mirror real y vivo está en Waseda ([ueda.info.waseda.ac.jp/software.html](https://www.ueda.info.waseda.ac.jp/software.html)), con [backup en Wayback Machine](https://web.archive.org/web/20251201151637/https://www.ueda.info.waseda.ac.jp/software.html) por si acaso; el dominio viejo tiene su propio [snapshot de 2008 en Wayback](https://web.archive.org/web/20081231075254/http://www.icot.or.jp:80/ARCHIVE/HomePage-E.html).

**Imágenes:** _ya incorporadas al post publicado_ — se descartó el plan original (línea de tiempo + snippet comparativo + logo ICOT, todos "crear") a favor de un hero fotográfico único: `hero-icot-kl1.jpg`, foto de Akihabara 1976 (CC BY 2.0, Wikimedia Commons) recortada a 2.5:1 — no es una foto de ICOT ni de una PIM (no existen fotos de acceso público de ninguna de las dos, confirmado durante la búsqueda), es el barrio electrónico de Tokio para ambientar época y lugar. El código KL1 en el cuerpo del post son snippets reales extraídos de `examples/` y `agent-oriented-programming/` del repo (`not.kl1`, `primes.kl1`), no inventados ni recreados.

**Tags propuestos:** `['KL1', 'KLIC', 'ICOT', 'Prolog concurrente', 'Japon', 'Vagrant', 'Debian']` (los tags reales del post; se sacó "Quinta Generacion" e "historia" por no usarse como tags en el post final).

**Estado actual:** **publicado el 2026-07-12**, [post en vivo](/posts/kl1-icot-quinta-generacion/). El post terminó siendo más rico que el plan original porque se clonó el repo real (no había clon local, se clonó al scratchpad para la sesión) en vez de escribir sólo a partir del resumen del draft: la sección de empaquetado usa la historia real encontrada en el `Vagrantfile` y los tres parches del repo (autodetección de `bcmp`/`bzero`/`strchr` rota en la libc moderna, y el instalador `expect` que no conocía las rutas multiarch de Debian) en vez de la descripción genérica "Vagrant + scripts" del outline original. Acciones pendientes desde el plan editorial:
- Agregar links a este post desde [[A1-04]] y [[A1-05]] cuando se escriban.
- Cross-link con [[H-06]] (parábola del legacy) cuando ese post exista — comparten el tema de "código que sobrevive a su propio proyecto".
- Posible entrada propia sobre *concurrent logic programming* en general, inspirada por este post (queda anotado pero sin ID asignado todavía).

