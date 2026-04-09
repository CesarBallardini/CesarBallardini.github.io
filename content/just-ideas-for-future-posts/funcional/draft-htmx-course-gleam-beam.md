### B-07 — htmx-course con Gleam: HTMX desde el BEAM (Erlang OTP) en un curso de 28 capítulos

- **Archivo seed (repo POC):** [github.com/CesarBallardini/htmx-course](https://github.com/CesarBallardini/htmx-course) — Markdown content, último push 2026-02-26
- **Slug propuesto:** `htmx-course-gleam-beam`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-htmx-course-gleam-beam/index.md`
- **Serie:** B — Gleam es funcional tipada sobre BEAM, encaja en CS funcional aunque el ángulo del repo sea web/HTMX
- **Cross-links:** lleva a [[A1-02]] (Erlang the Movie — el BEAM en el otro extremo de la grilla), [[A2-04]] (Clojure — la otra "funcional moderna"), [[B-04]] (recursión + tail calls — Gleam los tiene); también se conecta con [[K-01]] (DMOJ docencia)
- **Idioma:** es
- **Madurez:** **complete-poc para el contenido** (28 capítulos + 3 apéndices, contenido recién pulido en febrero 2026), pero el curso es un *libro vivo* y va a evolucionar.
- **Length target:** medium (1500-2200 palabras) — el post es una introducción al curso, no una réplica del curso

**Concepto:** **Gleam** es un lenguaje funcional moderno con tipos estáticos y sintaxis amigable, que compila a la VM del BEAM (la VM de Erlang/Elixir). **HTMX** es una biblioteca JavaScript de ~14 KB que extiende HTML con atributos `hx-*` para permitir interacciones AJAX/SSE/WebSocket directas desde el HTML, sin escribir JavaScript. La intersección de las dos cosas — un servidor Gleam con OTP actors atrás, hablando HTML+HTMX al cliente — es una de las arquitecturas web más interesantes del 2026: tipos estáticos, hot code reload heredado del BEAM, *zero JavaScript* en el cliente, y un modelo de concurrencia que viene de los años 80 de la telefonía. Mi `htmx-course` es un curso estructurado de 28 capítulos que enseña HTMX *a través de* construir una aplicación de pizarrón colaborativa llamada "Teamwork" en Gleam, usando Wisp + Mist + Lustre + SQLite (sqlight) + OTP actors para background jobs.

**Hook:** "imaginate una pila web donde el frontend es HTML con atributos `hx-*`, *sin JavaScript escrito por vos*, y el backend es Gleam (un funcional tipado moderno) corriendo sobre la VM de Erlang con OTP actors haciendo trabajos en segundo plano. Si nunca pensaste en eso, es porque casi nadie lo cuenta. El curso `htmx-course` lo enseña en 28 capítulos construyendo una pizarra colaborativa. El post explica por qué armé el curso y por qué esta pila puede ser el backend más sano del año."

**Outline:**
1. Las dos piezas raras: Gleam (lenguaje) y HTMX (biblioteca). Por qué se llevan tan bien.
2. La VM BEAM en 30 segundos: actores, mensajes, supervisión, hot code reload. Por qué es absurdamente buena para servidores web.
3. Wisp + Mist + Lustre + sqlight: el ecosistema Gleam para web, en 4 librerías.
4. La aplicación que se construye en el curso: "Teamwork", un pizarrón colaborativo (tareas, estados, equipos, asignaciones). Por qué elegí ese ejemplo (suficientemente real para tocar todos los problemas, suficientemente chico para entrar en 28 capítulos).
5. La estructura del curso, capítulo por capítulo (resumen alto):
   - 1-5: HTTP fundamentals y routing en Gleam.
   - 6-10: el modelo HTMX (intercambios, eventos, swap targets).
   - 11-15: SSE para tiempo real.
   - 16-20: auth, sesiones, formularios.
   - 21-25: persistencia con SQLite, modelos relacionales.
   - 26-28: OTP actors para background jobs.
   - Apéndices: a11y, performance de DB, deploy.
6. Lo que el curso *no* cubre y por qué: testing avanzado (lo dejo para la próxima edición), Lustre full SPA (la pila no lo necesita).
7. Por qué es un buen camino de entrada al BEAM si venís de Python o JavaScript.
8. Cierre: el curso está abierto y se puede leer libre — link al repo.

**Bibliografía:**
- Repo del curso: [CesarBallardini/htmx-course](https://github.com/CesarBallardini/htmx-course).
- [Gleam — sitio oficial](https://gleam.run/).
- [Gleam — *Language Tour*](https://tour.gleam.run/).
- [HTMX — sitio oficial](https://htmx.org/).
- [Carson Gross, *HTMX in Action*, Manning 2024](https://www.manning.com/books/htmx-in-action) — el libro "oficial" de HTMX.
- [Wisp — Gleam web framework](https://github.com/gleam-wisp/wisp).
- [Mist — Gleam HTTP server](https://github.com/rawhat/mist).
- [Lustre — Gleam UI framework](https://hexdocs.pm/lustre/).
- [sqlight — SQLite bindings for Gleam](https://github.com/lpil/sqlight).
- [Joe Armstrong, *Programming Erlang*, 2nd ed Pragmatic Bookshelf 2013](https://pragprog.com/titles/jaerlang2/programming-erlang-2nd-edition/) — el libro fundacional del BEAM (cross [[A1-02]]).
- [Hypermedia Systems book — Carson Gross et al](https://hypermedia.systems/) — la filosofía detrás de HTMX.
- [Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures*, PhD thesis 2000](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) — REST original, base teórica para HTMX.

**Imágenes:**
- _Crear_: diagrama de la pila Gleam + Wisp + Mist + Lustre + sqlight + OTP — cómo se conectan (~1 hora — central).
- _Crear_: snippet de Gleam con un endpoint HTMX típico (~15 min).
- _Crear_: screenshot del pizarrón Teamwork funcionando (~10 min).

**Tags propuestos:** `['Gleam', 'HTMX', 'BEAM', 'Erlang', 'Wisp', 'Mist', 'Lustre', 'OTP', 'web', 'curso']`

**Estado actual:** **POC completo** — curso de 28 capítulos publicado en GitHub. El post se puede armar como "introducción al curso" en una sesión.

