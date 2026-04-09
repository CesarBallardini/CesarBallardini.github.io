### A2-06 — Mi propia traducción de SICP al castellano: el proyecto que casi termina

- **Archivo seed (repo POC):** [github.com/CesarBallardini/sicp-spanish](https://github.com/CesarBallardini/sicp-spanish) — TeX, 10 stars, último push 2022-10-19
- **Slug propuesto:** `mi-traduccion-sicp-castellano`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mi-traduccion-sicp-castellano/index.md`
- **Serie:** A2 — complementa [[A2-01]] (donde se cita la traducción de FedeHC); también E (memoir personal)
- **Cross-links:** depende de [[tr-03]] (SICP) y [[A2-01]]; lleva a [[A2-07]] (DrRacket + Jupyter), [[E-12]] (el patrón Vagrant+Ansible)
- **Idioma:** es
- **Madurez:** **partial-poc** — el toolchain de build (HTML5/ePub/PDF desde `sicp.texi` dentro de una VM Virtualbox) funciona; la traducción avanza incrementalmente desde el capítulo 2 (porque el capítulo 1 ya está cubierto por la traducción de FedeHC).
- **Length target:** medium (1800-2500 palabras)

**Concepto:** SICP (*Structure and Interpretation of Computer Programs*, Abelson & Sussman) es uno de los libros más importantes de la historia de la enseñanza de CS. Tiene traducciones al español, pero la mayoría son parciales, abandonadas o difíciles de mantener. En 2018-2022 me senté a empezar mi propia traducción, partiendo del *texinfo* fuente original del MIT, con un toolchain dentro de una VM (Virtualbox + Ansible) que produce HTML5, ePub y PDF en un solo build. Empecé por el capítulo 2 porque el capítulo 1 ya estaba cubierto por la versión de FedeHC. Después la realidad pateó la pelota y la traducción quedó parcial. El post es la historia honesta de por qué intenté, qué aprendí, y por qué creo que vale la pena que alguien la termine algún día.

**Hook:** "SICP es uno de los libros más importantes de CS. La traducción al español es un patchwork de proyectos abandonados. En 2018 dije: lo hago yo. Armé el toolchain, monté la VM, empecé por el capítulo 2 (el 1 ya estaba traducido por FedeHC), avancé varias secciones... y la realidad me pasó por encima. Quedó parcial. El post es por qué intenté, por qué la pedagogía de SICP merece esfuerzo, y qué le diría a la próxima persona que se anime."

**Outline:**
1. SICP en 30 segundos (cross con [[A2-01]] y [[tr-03]]).
2. El paisaje de las traducciones al español: FedeHC, Andres Raba (PDF moderno), traducciones parciales en blogs, los videos doblados.
3. Por qué decidí empezar de nuevo: tener el `texinfo` fuente como input, no PDF. Habilita ePub, HTML5, PDF, traducciones parciales que se pueden mejorar incrementalmente.
4. La VM: Virtualbox + Ansible + texinfo + texlive + Calibre. El `Vagrantfile` y por qué eligí build dentro de VM en vez de en mi máquina anfitriona.
5. La estrategia de "empezar por el capítulo 2": evitar duplicar trabajo y entrar directo al material técnico más jugoso (data abstraction, generic operations, message passing).
6. Lo que hice y lo que no: las secciones traducidas, las que quedaron a medio, los términos técnicos que me trabaron (¿"closure"?, ¿"thunk"?, ¿"tail call"?).
7. Por qué se frenó: no es una sola razón. Trabajo, otras prioridades, y honestamente — la traducción es un trabajo de horas y no de inspiración.
8. Lo que aprendí del proceso: traducir es leer 4 veces; el toolchain es lo de menos; lo difícil es la consistencia terminológica.
9. Cierre: si alguien quiere continuarla, el repo está abierto. Y si soy yo quien la continúa algún día, ya sé en qué orden hacerlo.

**Bibliografía:**
- Repo del POC: [CesarBallardini/sicp-spanish](https://github.com/CesarBallardini/sicp-spanish).
- [SICP — sitio del MIT (2da edición)](https://web.mit.edu/6.001/6.037/sicp.pdf).
- [SICP-ES — traducción de FedeHC, archivo](https://github.com/FedeHC/SICP-ES) — el otro proyecto de referencia.
- [Andres Raba, *SICP edition modern PDF*](https://github.com/sarabander/sicp-pdf) — el PDF moderno con todas las correcciones tipográficas.
- [HTML5 + ePub3 SICP edition](https://github.com/sarabander/sicp) — base de mi build.
- [iRacket — Racket kernel for Jupyter](https://github.com/rmculpepper/iracket) — herramienta que me permitió experimentar el código en notebooks (cross [[A2-07]]).
- [[tr-03]] — SICP referencia transversal.
- [Stuart Halloway, *Why MIT now uses Python instead of Scheme for its undergraduate CS program*](https://news.ycombinator.com/item?id=602307) — el debate "por qué dejaron de enseñar SICP".

**Imágenes:**
- _Crear_: screenshot del HTML5 generado por mi build, mostrando el capítulo 2 en castellano (~15 min).
- _Crear_: side-by-side de un párrafo en inglés vs su traducción en castellano (~10 min).
- _Crear_: captura del repo en GitHub mostrando la estructura de directorios (~5 min).

**Tags propuestos:** `['SICP', 'traduccion', 'castellano', 'texinfo', 'Vagrant', 'Abelson', 'Sussman', 'pedagogia']`

**Estado actual:** **partial-poc** en GitHub (10 stars, build funciona, traducción parcial). El post es 90% memoir y 10% técnico, así que sale rápido.

