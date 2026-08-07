### B-07 — htmx-course con Gleam: HTMX desde el BEAM (Erlang OTP) en un curso de 28 capítulos

- **Archivo seed (repo POC):** [github.com/CesarBallardini/htmx-course](https://github.com/CesarBallardini/htmx-course) — Markdown content, último push 2026-02-26
- **Slug propuesto:** `htmx-course-gleam-beam`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-htmx-course-gleam-beam/index.md`
- **Serie:** B — Gleam es funcional tipada sobre BEAM, encaja en CS funcional aunque el ángulo del repo sea web/HTMX
- **Cross-links:** lleva a [[A1-02]] (Erlang the Movie — el BEAM en el otro extremo de la grilla), [[A2-04]] (Clojure — la otra "funcional moderna"), [[B-04]] (recursión + tail calls — Gleam los tiene); también se conecta con [[K-01]] (DMOJ docencia)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
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

**Bibliografía:** _(fuentes verificadas por fetch el 2026-07-16)_
- [CesarBallardini/htmx-course](https://github.com/CesarBallardini/htmx-course) — el repo del curso; descripción oficial "Teamwork: An HTMX Course with Gleam", 28 capítulos + 3 apéndices. **estable** (repo propio).
- [Gleam — sitio oficial](https://gleam.run/) — funcional tipado que compila a la VM del BEAM (Erlang) y a JavaScript (con generación de definiciones TypeScript); "No null values, no exceptions" (errores vía tipo `Result`). Versión 1.17.0 (2026-06-02). **estable**.
- [Gleam — *Language Tour*](https://tour.gleam.run/) — tour interactivo. **estable**.
- [Gleam — *Command line reference*](https://gleam.run/command-line-reference/) — documenta `gleam new`, `gleam add`, `gleam build`, `gleam run`, `gleam test`. **estable**.
- [HTMX — sitio oficial](https://htmx.org/) — extiende HTML con atributos `hx-*` para AJAX / SSE / WebSocket. Versión 2.0.10 (v4 en beta); el sitio cita "~16k min.gz'd". Mantenido por Big Sky Software (Carson Gross). **estable**.
- [Carson Gross, Adam Stepinski, Deniz Akşimşek, *Hypermedia Systems*](https://hypermedia.systems/) — libro que arma la teoría y la práctica de HTMX; texto completo libre online, CC BY-NC-SA 4.0. Es el único libro de HTMX de Gross (Manning encargó *HTMX in Action* pero no lo publicó; los derechos volvieron al autor y se editó como *Hypermedia Systems*). **estable**.
- [Wisp — Gleam web framework](https://github.com/gleam-wisp/wisp) — "a practical Gleam web framework"; handlers + middleware (vía `use`), logging, static files, formularios. **estable**.
- [Mist — Gleam HTTP server](https://github.com/rawhat/mist) — "a glistening Gleam web server"; HTTP, WebSocket, file serving. **estable**.
- [Lustre — Gleam UI framework](https://lustre.hexdocs.pm/) — HTML templates, SPAs, Web Components y server components; el *server-side rendering* de HTML es una funcionalidad de primera clase (guía "Server side rendering"). **estable**.
- [sqlight — SQLite bindings for Gleam](https://github.com/lpil/sqlight) — "Use SQLite from Gleam!". **estable**.
- [Joe Armstrong, *Programming Erlang*, 2ª ed., Pragmatic Bookshelf, 2013](https://pragprog.com/titles/jaerlang2/programming-erlang-2nd-edition/) — el libro fundacional del BEAM (cross [[A1-02]], [[tr-09]]). **estable** (página del editor).
- [Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures*, tesis doctoral, 2000](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) — REST original, base teórica para HTMX. **estable** (sitio institucional UCI).

**Imágenes:**
- _Crear_: diagrama de la pila Gleam + Wisp + Mist + Lustre + sqlight + OTP — cómo se conectan (~1 hora — central).
- _Crear_: snippet de Gleam con un endpoint HTMX típico (~15 min).
- _Crear_: screenshot del pizarrón Teamwork funcionando (~10 min).

**Tags propuestos:** `['Gleam', 'HTMX', 'BEAM', 'Erlang', 'Wisp', 'Mist', 'Lustre', 'OTP', 'web', 'curso']`

**Estado actual:** **POC completo** — curso de 28 capítulos publicado en GitHub (contenido pulido en febrero 2026; el curso es un *libro vivo* y va a evolucionar). Sobre esa base hay ahora un **borrador de prosa completo** (~1.900 palabras, dentro del target medium) escrito al outline de 8 puntos, agregado al final de este archivo.

Lo que quedó escrito: el encuadre de las dos piezas (Gleam y HTMX), el resumen del BEAM, la presentación del ecosistema web de Gleam, la descripción del curso y su estructura, el argumento de por qué es una puerta de entrada al BEAM viniendo de Python o JavaScript, y el cierre con link al repo.

Lo que quedó como hueco: **todo lo que es experiencia vivida y decisión de autor**. El post es sobre un proyecto propio de César, así que casi todos los «por qué» son huecos: por qué eligió Gleam y no Elixir, por qué el ejemplo es un pizarrón, cuánto tardó, qué se rompió, qué dejó afuera y por qué, si el curso se usó con alumnos. Hay 13 huecos 🕳️.

El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 6 de 7 marcadores [VERIFICAR:]. Resueltos contra sitios oficiales y contra el índice real del repo: tamaño de HTMX (~16 KB min.gz, htmx 2.0.10), targets de compilación de Gleam (BEAM + JavaScript con defs TypeScript, v1.17.0), *server-side rendering* de Lustre como uso de primera clase, comandos de la CLI de Gleam, y **el reparto capítulo por capítulo — que en el outline estaba mal**: el repo real tiene 4 partes (Principiante 1-6, Intermedio 7-12, Avanzado 13-18, Mundo real 19-28) y 3 apéndices (A: bibliografía, B: _hyperscript, C: instalar mise), no el agrupamiento SSE-por-quintiles del outline; accesibilidad, performance de DB y deploy son capítulos (26, 27, 17), no apéndices. Queda 1 marcador sin resolver: el [VERIFICAR:] del BEAM (cifras de procesos concurrentes / detalles de schedulers / hot code reload), que es un recordatorio condicional — la prosa hoy no afirma números, así que no hay nada que fijar hasta que se decida citarlos, y entonces hay que ir a *Programming Erlang* 2ª ed.

**Corrección importante de fabricación:** el draft citaba «Carson Gross, *HTMX in Action*, Manning 2024». Ese libro **no existe**: Manning encargó el libro pero decidió no publicarlo, los derechos volvieron a Gross y el material se editó como *Hypermedia Systems* (autoeditado, libre online). La URL de Manning devuelve 404. Se eliminó esa cita fabricada de la bibliografía, del texto y de las notas al pie; queda solo *Hypermedia Systems*, que es el libro real y cubre teoría y práctica.

**Pendiente antes de publicar:** responder los huecos, resolver los [VERIFICAR:] contra el repo y los sitios oficiales, resolver los `[[ID]]` a URLs reales, y producir las tres imágenes listadas.

---

## Borrador de prosa

Imaginate una pila web donde el frontend es HTML con atributos raros — `hx-get`, `hx-post`, `hx-swap` — y no hay una sola línea de JavaScript escrita por vos. Ningún bundler, ningún estado duplicado entre cliente y servidor, ninguna carrera entre el JSON que llega y el componente que ya se desmontó. Y ahora imaginate que atrás de ese HTML hay un lenguaje funcional con tipos estáticos, compilado a la máquina virtual que Ericsson inventó para no dejar caer llamadas telefónicas, con actores y supervisores haciendo el trabajo en segundo plano.

Si nunca pensaste en esa combinación, no es culpa tuya: casi nadie la cuenta. Yo armé un curso de 28 capítulos para contarla. Se llama `htmx-course`[^repo], enseña HTMX construyendo una aplicación real en Gleam, y este post es la introducción: qué son las dos piezas raras, por qué se llevan tan bien, y por qué creo que esta pila puede ser el backend más sano del año.

### Las dos piezas raras

**HTMX** es una biblioteca JavaScript chiquita — del orden de los 16 KB minificados y comprimidos con gzip (el sitio oficial cita "~16k min.gz'd" para htmx 2.0.x)[^htmx] — cuya idea entera cabe en una frase: extender HTML para que cualquier elemento pueda hacer un pedido HTTP y reemplazar cualquier pedazo del documento con la respuesta[^htmx]. Un botón puede hacer un `POST` y meter el HTML devuelto adentro de un `<div>`. Un input puede disparar un `GET` mientras escribís. Un elemento puede quedarse escuchando Server-Sent Events. Todo eso son atributos, no código.

Lo interesante no es el ahorro de JavaScript. Es lo que implica sobre la arquitectura: si el servidor devuelve HTML en vez de JSON, entonces el servidor volvió a ser el dueño del estado y de la representación, y el cliente volvió a ser lo que la tesis de Fielding describía[^fielding] — un motor genérico que sigue hipermedia. Carson Gross, que escribió HTMX, escribió también el libro que arma tanto la teoría como la práctica de todo esto: *Hypermedia Systems*[^hypermedia], con texto completo libre online. Vale la pena leerlo junto con la documentación oficial de htmx[^htmx], según cuánto aguantes la abstracción antes del código.

**Gleam** es la otra pieza: un lenguaje funcional con tipos estáticos, inferencia, y una sintaxis que no espanta a nadie que venga de Rust o de TypeScript[^gleam]. Compila a la VM del BEAM — la de Erlang y Elixir — y también a JavaScript, para lo cual además genera definiciones TypeScript[^gleam]. Es inmutable, no tiene `null`, y no tiene excepciones en el sentido habitual: los errores viajan en el tipo de retorno y el compilador te obliga a mirarlos.

¿Por qué se llevan bien? Porque HTMX le pide al servidor exactamente aquello que un lenguaje funcional tipado sabe hacer mejor: tomar un pedido, calcular un fragmento de HTML, devolverlo. Sin estado escondido. Una función de request a respuesta. HTMX borra la mitad del problema — el estado del cliente — y Gleam le pone tipos a la mitad que queda.

> 🕳️ **HUECO — necesita a César:** ¿Por qué Gleam y no Elixir, que tiene Phoenix + LiveView y muchísima más masa crítica? ¿Fue por los tipos estáticos, por el tamaño del lenguaje, por curiosidad, o porque LiveView resuelve el problema de una manera que no te convence?

> 🕳️ **HUECO — necesita a César:** ¿Cómo llegaste a Gleam? ¿Lo viste en una charla, en Hacker News, te lo mostró alguien? Una frase alcanza.

### El BEAM en 30 segundos

El BEAM es la máquina virtual de Erlang, y su modelo mental es corto: todo es un proceso, los procesos no comparten memoria, se hablan por mensajes, y cuando uno se rompe hay otro proceso — el supervisor — cuyo único trabajo es decidir qué hacer con el cadáver. Los procesos son baratísimos: se cuentan de a cientos de miles, no de a docenas. El scheduler es preemptivo, así que un proceso colgado en un loop no le come el turno a los demás. Y el sistema puede reemplazar el código de un módulo con todo andando: *hot code reload*. Todo eso está contado en el libro de Joe Armstrong[^armstrong], que sigue siendo la mejor puerta de entrada [VERIFICAR: si al escribir el post se afirman cifras de procesos concurrentes, detalles de los schedulers o del mecanismo de hot code reload, chequear capítulo y página en *Programming Erlang* 2ª ed. antes de publicarlas].

Todo esto se diseñó para centrales telefónicas: sistemas donde «se cayó, reiniciá» no es una respuesta aceptable. Y resulta que un servidor web tiene exactamente la misma forma. Miles de cosas concurrentes, mayormente independientes, cada una de las cuales puede fallar sin que las otras se enteren. Cada request es un proceso. Cada conexión SSE es un proceso. Cada background job es un proceso supervisado. No hay `async`/`await` de colores, no hay event loop que se bloquea porque alguien llamó a una función sincrónica, no hay pool de threads que configurás a ojo y mirás con miedo. Es la arquitectura que el resto del mundo viene reinventando de a pedazos desde hace veinte años.

Del otro extremo de esta misma grilla ya escribí en [[A1-02]], y la recursión y las tail calls que Gleam hereda del BEAM las cuento en [[B-04]].

### El ecosistema web de Gleam, en cuatro librerías

La pila del curso son cuatro piezas, y me gusta que se puedan nombrar todas en un párrafo:

- **Mist**[^mist] es el servidor HTTP: el que habla el protocolo y maneja las conexiones.
- **Wisp**[^wisp] es el framework web que va arriba de Mist: routing, request/response, middleware, formularios.
- **Lustre**[^lustre] es el framework de UI. En esta pila lo uso para generar HTML del lado del servidor — lo que su documentación llama *server-side rendering*, una funcionalidad de primera clase (Lustre también sabe hacer SPAs, Web Components y server components, pero acá no los necesito).
- **sqlight**[^sqlight] son los bindings a SQLite: la persistencia.

Cuatro librerías. Ninguna hace magia. Esa es la parte que más me gusta y la que más cuesta explicar en un mundo acostumbrado a frameworks que traen cuarenta decisiones ya tomadas y una carpeta que no sabés quién generó.

> 🕳️ **HUECO — necesita a César:** ¿Alguna de estas cuatro te dio pelea en serio mientras escribías el curso? Un detalle concreto («la API de X cambió a mitad de camino», «tuve que leer el código fuente de Y para entender Z») le da carne al párrafo.

> 🕳️ **HUECO — necesita a César:** ¿Por qué SQLite y no Postgres, siendo que el resto del blog vive bastante en Postgres? ¿Es una decisión pedagógica (cero setup para el alumno) o también te gusta para producción?

### La aplicación: «Teamwork»

Un curso de HTMX que enseñe con un contador y una lista de tareas de tres líneas no enseña nada: los problemas reales aparecen recién cuando hay usuarios, permisos, concurrencia y datos que cambian mientras alguien los está mirando. Así que el curso construye **Teamwork**, un pizarrón colaborativo: tareas, estados, equipos, asignaciones. Suficientemente real para tocar todos los problemas, suficientemente chico para entrar en 28 capítulos.

Un pizarrón es un ejemplo casi tramposo de lo bien que se porta esta pila. Alguien mueve una tarjeta de columna: eso es un `hx-post` que devuelve el HTML de la tarjeta en su nueva posición, y listo. Los demás tienen que enterarse: eso es SSE, y del otro lado hay un proceso del BEAM por cada mirón, que es exactamente el tipo de cosa para la que el BEAM fue construido. Hay que recalcular algo pesado sin frenar a nadie: eso es un actor OTP supervisado. Cada problema del ejemplo cae en una piedra que la pila ya tenía puesta.

> 🕳️ **HUECO — necesita a César:** ¿De dónde salió «Teamwork»? ¿Es un *scratch your own itch* (algo que necesitabas de verdad), una reducción de algún sistema que hiciste en el sector público, o lo diseñaste desde cero para el curso?

> 🕳️ **HUECO — necesita a César:** ¿Cuánto te llevó escribir los 28 capítulos, y en qué período? Un rango sirve: «entre tal y tal mes, unos N fines de semana».

### La estructura del curso

El curso está dividido en cuatro partes, 28 capítulos y tres apéndices. A grandes rasgos, el recorrido es este:

- **Parte 1 — Principiante (capítulos 1 a 6)** — cómo funciona la web de verdad, servir páginas HTML, routing, la primera interacción HTMX, la tríada *click / trigger / swap*, y estado en el servidor entre requests.
- **Parte 2 — Intermedio (capítulos 7 a 12)** — formularios y validación, estrategias de *swap* y actualizaciones *out-of-band*, listas / filtros / búsqueda, múltiples tableros y navegación, y cookies / sesiones / autenticación.
- **Parte 3 — Avanzado (capítulos 13 a 18)** — tiempo real con Server-Sent Events, endurecimiento de seguridad, testing de aplicaciones HTMX, extensiones, deploy y producción, e integración de JavaScript de terceros (Flatpickr).
- **Parte 4 — Patrones del mundo real (capítulos 19 a 28)** — manejo de errores y degradación elegante, *response headers* de HTMX, edición inline (*click-to-edit*), diálogos modales, patrones de _hyperscript, formularios dinámicos y dependientes, subida de archivos, HTMX accesible, performance de base de datos, y —al final— *background jobs* con procesos del BEAM.
- **Apéndices** — A: bibliografía y recursos; B: _hyperscript, el lenguaje compañero de HTMX; C: instalar *mise*.

El orden no es casual: primero los fundamentos de HTTP y el HTML que viaja por el cable, después el modelo de HTMX en serio, y recién al final —capítulo 28— los procesos del BEAM para el trabajo en segundo plano. Los actores quedan para el final a propósito. Son lo más ajeno para quien viene de otro lado, y para cuando llegás ahí ya tenés una aplicación que los pide sola — que es la única forma decente de enseñar una abstracción: cuando el alumno ya siente el dolor que la abstracción cura.

> 🕳️ **HUECO — necesita a César:** ¿Ese orden fue el plan desde el principio o lo reordenaste sobre la marcha? Si hubo un capítulo que se mudó de lugar porque no funcionaba donde estaba, es una buena anécdota.

### Lo que el curso no cubre

Dos ausencias, las dos deliberadas. **Testing avanzado**: hay lo básico, pero el tratamiento serio queda para la próxima edición. **Lustre como SPA completa**: Lustre puede hacer una aplicación cliente entera al estilo Elm, y el curso no lo usa así, porque la pila directamente no lo necesita. Meter una SPA acá sería contradecir la tesis del curso en el último capítulo.

> 🕳️ **HUECO — necesita a César:** ¿Hay una tercera cosa que quedó afuera y te duele? (¿WebSockets? ¿Clustering multi-nodo? ¿Deploy real en producción con releases del BEAM?)

> 🕳️ **HUECO — necesita a César:** Lo de testing avanzado, ¿es «no me dio el tiempo» o «todavía no tengo una opinión firme sobre cómo se testea bien esto»? Son dos posts distintos y conviene saber cuál es.

### Por qué es una buena puerta de entrada al BEAM

Si venís de Python o de JavaScript, el BEAM te suena a otro planeta: sintaxis rara, comunidad chica, documentación que asume que sabés de telefonía. Gleam corta casi todo eso. La sintaxis se lee sin diccionario, el compilador te agarra los errores que en Erlang te agarraría producción, y la herramienta es una sola: `gleam new`, `gleam add`, `gleam build`, `gleam test`, `gleam run` — todos documentados en la referencia de línea de comandos oficial[^gleam].

Y HTMX corta la otra mitad del miedo: no tenés que aprender un framework de frontend nuevo *además* del lenguaje nuevo y de la máquina virtual nueva. El frontend es HTML. El que ya sabés. Aprendés un lenguaje y una VM, no tres cosas a la vez. Ese es el argumento entero del curso, y es la razón por la que existe.

> 🕳️ **HUECO — necesita a César:** ¿El curso se usó con alguien? ¿Alumnos, colegas, gente de la comunidad? Si hubo feedback real de un lector, aunque sea uno solo, vale más que todo este párrafo. Conecta con [[K-01]].

> 🕳️ **HUECO — necesita a César:** Cuando empezaste el curso, ¿venías de Python/JS o ya venías de Erlang/Elixir? Cambia bastante quién es el «vos» al que le habla el curso.

### Cierre

`htmx-course` está abierto y se lee gratis[^repo]. Es un libro vivo: va a cambiar, va a tener errores, y si encontrás uno el issue tracker está ahí. No es un curso que te enseña una biblioteca; es un curso que usa una biblioteca para defender una idea — que el servidor puede seguir siendo el dueño del estado, y que hay una máquina virtual de los años 80 esperando hace cuarenta años a que volvamos a darnos cuenta.

> 🕳️ **HUECO — necesita a César:** ¿Hay una próxima edición planeada con fecha o intención concreta, o «libro vivo» significa parches cuando aparecen? Conviene no prometer lo que no vas a hacer.

> 🕳️ **HUECO — necesita a César:** ¿Querés pedirle algo puntual al lector (issues, PRs, una traducción al inglés, que te cuenten si lo usaron)? Un cierre con pedido concreto funciona mejor que uno sin.

[^repo]: [CesarBallardini/htmx-course](https://github.com/CesarBallardini/htmx-course) — el repo del curso.
[^htmx]: [HTMX — sitio oficial](https://htmx.org/). Versión 2.0.10 al momento de escribir (v4 en beta); el sitio cita "~16k min.gz'd". Mantenido por Big Sky Software (Carson Gross).
[^gleam]: [Gleam — sitio oficial](https://gleam.run/), versión 1.17.0 (2026-06-02); compila a la VM del BEAM y a JavaScript. Para arrancar a escribir código, el [Language Tour](https://tour.gleam.run/) es interactivo y se hace de una sentada; los comandos de la CLI están en la [referencia de línea de comandos](https://gleam.run/command-line-reference/).
[^hypermedia]: Carson Gross, Adam Stepinski y Deniz Akşimşek, [*Hypermedia Systems*](https://hypermedia.systems/) — la teoría y la práctica detrás de HTMX; texto completo libre online, CC BY-NC-SA 4.0.
[^fielding]: Roy Fielding, [*Architectural Styles and the Design of Network-based Software Architectures*](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm), tesis doctoral, 2000.
[^armstrong]: Joe Armstrong, [*Programming Erlang*](https://pragprog.com/titles/jaerlang2/programming-erlang-2nd-edition/), 2ª ed., Pragmatic Bookshelf, 2013.
[^wisp]: [Wisp — Gleam web framework](https://github.com/gleam-wisp/wisp).
[^mist]: [Mist — Gleam HTTP server](https://github.com/rawhat/mist).
[^lustre]: [Lustre — Gleam UI framework](https://lustre.hexdocs.pm/). Ofrece *server-side rendering* de HTML como funcionalidad de primera clase, además de SPAs, Web Components y server components.
[^sqlight]: [sqlight — SQLite bindings for Gleam](https://github.com/lpil/sqlight).
