### A1-02 — Erlang the Movie (y por qué deberías ver una película de un lenguaje)

- **Archivo seed:** `dev/draft-erlang.md`
- **Slug propuesto:** `erlang-the-movie`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-erlang-the-movie.md` (sin bundle, archivo plano; las imágenes son embeds de YouTube)
- **Serie:** A1
- **Cross-links:** depende de [[tr-09]]; lleva a [[A1-03]] (Forth, otra concurrencia rara), [[H-04]] (sistemas que no se pueden parar)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** short (700-1000 palabras)

**Concepto:** Erlang/OTP no es un lenguaje "raro". Es la respuesta correcta a "cómo hacer un sistema que no se cae nunca", y la clave es el modelo de actores con fail-fast / supervisar / reiniciar — exactamente lo opuesto a "manejá todas las excepciones, papá".

**Hook:** existe una película institucional de Ericsson de 1990 llamada *Erlang the Movie*. Dura 12 minutos, está mal filmada, los actores son ingenieros leyendo un script, hay ropa de los años 90 y, sin embargo, en esos 12 minutos se entiende mejor el modelo de actores que en cualquier libro. Mostrá la película y ya está medio post escrito.

**Outline:**
1. Existe una película. Mostrarla. Explicar por qué es absurdo y maravilloso a la vez.
2. El problema que Erlang resolvía: telcos, switches que no se pueden reiniciar, 9 nueves de uptime.
3. La idea central — actores aislados, mensajes asíncronos, fail-fast, supervisor trees.
4. "Let it crash" como filosofía: por qué esto te suena raro hasta que entendés que tu código no es lo que debe sobrevivir, sino el sistema.
5. Cierre: qué sobrevive de Erlang en lo que escribimos hoy (Akka, Elixir, OTP en infra moderna).

**Bibliografía:**
- [[tr-09]] — *Erlang the Movie* (1990, Ericsson) + Armstrong, *Programming Erlang* (2.ª ed. 2013). Fuente transversal.
- [*Erlang: The Movie* (1990) en YouTube](https://www.youtube.com/watch?v=BXmOlCy0oBM) — película institucional de Ericsson, 12 min; grabación de la demo dada en ISS90 (Estocolmo, 1990). En cámara: Mike Williams, Joe Armstrong y Bjarne Däcker (Robert Virding suele listarse también), todos del Computer Science Laboratory de Ericsson. Ficha en [Letterboxd](https://letterboxd.com/film/erlang-the-movie/). **frágil** (YouTube; conviene backup en Wayback — no pude generarlo, web.archive.org no responde al fetch).
- [Joe Armstrong, *Making reliable distributed systems in the presence of software errors*](https://erlang.org/download/armstrong_thesis_2003.pdf), tesis doctoral, 2003 — el texto fundacional. **estable** (erlang.org).
- [Joe Armstrong, *A History of Erlang*](https://doi.org/10.1145/1238844.1238850) — en *Proceedings of the Third ACM SIGPLAN Conference on History of Programming Languages* (HOPL III), San Diego, 2007. DOI 10.1145/1238844.1238850. Historia de primera mano. Mirror libre: [PDF en lfe.io](https://lfe.io/papers/%5B2007%5D%20Armstrong%20-%20HOPL%20III%20A%20History%20of%20Erlang.pdf). DOI **estable** / mirror **frágil**.
- [Erlang/OTP — sitio oficial](https://www.erlang.org/) y [página *About*](https://www.erlang.org/about) — "originally developed at the Ericsson Computer Science Laboratory". **estable**.
- [Erlang (programming language) — Wikipedia](https://en.wikipedia.org/wiki/Erlang_(programming_language)) — creadores (Armstrong, Virding, Williams; 1986), nombre (Agner Krarup Erlang / "Ericsson Language"), open source 1998, y AXD301 con "nine 9's" (99,9999999 %). **estable**.
- [Joe Armstrong, *Programming Erlang*, 2.ª ed.](https://pragprog.com/titles/jaerlang2/programming-erlang-2nd-edition/) — Pragmatic Bookshelf, oct. 2013, ISBN 978-1-937785-53-6, 546 pp. **estable**.
- [Joe Armstrong, *The Mess We're In*](https://www.youtube.com/watch?v=lKXe3HUG2l4), Strange Loop 2014 — su charla sobre por qué la programación es un desastre. **frágil** (YouTube).
- [*Erlang the Movie II — The Sequel*](https://www.youtube.com/watch?v=rRbY3TMUcgQ), 2013 — sí, hay segunda parte. **frágil** (YouTube).
- Herederos del modelo de actores: [Elixir](https://en.wikipedia.org/wiki/Elixir_(programming_language)) (José Valim, 2012; corre sobre la BEAM, comparte OTP) y [Akka](https://en.wikipedia.org/wiki/Akka_(toolkit)) (Jonas Bonér; JVM, "inspiration drawn from Erlang"). **estable**.

**Imágenes:**
- _Embed_: thumbnail de YouTube de la película (no es propiamente una imagen, es un iframe).
- _Wikimedia_: foto de Joe Armstrong — [Joe Armstrong (programmer)](https://commons.wikimedia.org/wiki/File:Joe_Armstrong.jpg) — license: ver descripción.
- _Crear_: opcional — diagrama simple SVG de un supervisor tree (3 cajas: supervisor → workers → "let it crash").

**Tags propuestos:** `['Erlang', 'Joe Armstrong', 'concurrencia', 'OTP', 'historia']`

**Estado actual:** prosa-borrador completa (~900 palabras, dentro del target short) escrita sobre el outline original, que se conservó tal cual. Lo que quedó escrito: el encuadre de la película, el problema de las telcos, el modelo de actores, «let it crash» y el cierre sobre qué sobrevive hoy. Lo que quedó como hueco: toda la voz personal de César (cómo llegó a la película, si alguna vez escribió Erlang o Elixir, la analogía con sistemas del sector público que no se podían parar, y su opinión sobre la charla de Armstrong). Los datos no respaldados por la bibliografía existente —duración de la película, quiénes actúan, el número de nueves, el detalle del switch AXD301, la genealogía de Akka/Elixir— quedaron marcados con `[VERIFICAR:]` en vez de afirmarse. Ojo: el Hook del draft afirma duración («12 minutos») y detalles de producción que la bibliografía no cubre; la prosa los rodea en vez de repetirlos como hecho. El 2026-07-16 se reforzó la bibliografía (fuentes verificadas por fetch) y se resolvieron 4 de 4 marcadores [VERIFICAR:]: reparto, duración (12 min, confirmada — el Hook queda respaldado), cifra de "nueve nueves" del AXD301 (confirmada como *reportada*, vía Wikipedia) y la línea de herederos (Elixir/Akka con fuente; los orquestadores quedan como analogía explícita).

---

## Borrador de prosa

Existe una película sobre un lenguaje de programación. No un documental retrospectivo filmado veinte años después por gente nostálgica: una película institucional, hecha por Ericsson en 1990, cuando el lenguaje todavía era un experimento interno y nadie afuera sabía que existía. Se llama *Erlang the Movie*[^movie] y está en YouTube, entera, gratis, esperándote.

Voy a ser honesto sobre lo que vas a encontrar: es un objeto raro. Tiene la estética exacta de un video de capacitación corporativa de principios de los noventa —los planos, la ropa, la música— y los que aparecen en cámara no son actores sino gente de la casa leyendo un guion con la incomodidad de quien preferiría estar tipeando[^cast]. Y sin embargo, en los pocos minutos que dura[^duracion], se entiende el modelo de actores mejor que en la mayoría de los libros que lo explican. Ese es el chiste y el punto: la película es graciosa, pero también es didáctica de una manera que nadie volvió a lograr.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste vos a *Erlang the Movie*? ¿Te la pasó alguien, la encontraste solo, en qué año más o menos?

### El problema no era el lenguaje

Erlang no nació porque alguien quisiera diseñar un lenguaje lindo. Nació en una empresa de telecomunicaciones que tenía un problema concreto y bastante desesperante: los switches telefónicos no se pueden apagar. No hay ventana de mantenimiento. No hay «lo reiniciamos el domingo a las tres de la mañana». El equipo está en producción desde que se enchufa hasta que se jubila, con años de servicio continuo por delante y una tolerancia a la caída que se mide en minutos por década[^nueves].

Ese requisito cambia todo. Si tu sistema puede reiniciarse, un bug es una molestia. Si no puede reiniciarse nunca, un bug es una catástrofe permanente. Y como los bugs existen —siempre existen, es la premisa entera de la tesis de Joe Armstrong, que se llama, literalmente, *Making reliable distributed systems in the presence of software errors*[^tesis]—, la pregunta deja de ser «cómo escribo código sin errores» y pasa a ser «cómo construyo un sistema confiable con software que sé que tiene errores».

Eso último es una pregunta de ingeniería. La primera es una fantasía.

### Procesos aislados y mensajes

La respuesta de Erlang es el modelo de actores, y el modelo de actores tiene menos piezas de las que uno esperaría.

Primero: procesos. No hilos del sistema operativo, sino procesos livianos de la máquina virtual, tan baratos que podés tener cientos de miles corriendo. Segundo: aislamiento total. Un proceso no comparte memoria con ningún otro. No hay estado compartido, así que no hay carrera por el estado compartido, así que no hay mutex, así que no hay deadlock esperándote a los ocho meses en producción. Tercero: mensajes asíncronos. Los procesos se hablan mandándose datos —copias, no punteros— a un buzón. El que manda no espera. El que recibe atiende cuando puede.

Y cuarto, el que cambia el juego: los procesos se pueden vigilar. Un proceso puede quedar ligado a otro y enterarse cuando el otro se muere. Sobre esa primitiva mínima —«avisame si se cae»— se construyen los supervisor trees: árboles donde los nodos internos no hacen trabajo, sólo vigilan hijos, y saben qué hacer cuando un hijo se muere. Reiniciarlo. Reiniciar a todos sus hermanos. Rendirse y morirse también, para que el supervisor de arriba decida.

### «Let it crash»

Acá viene la parte que te suena mal la primera vez. La consigna de Erlang no es manejar todas las excepciones: es dejar que el proceso se caiga.

A mí me educaron —y te apuesto que a vos también— en la doctrina contraria: atrapá todo, defendete de todo, nunca dejes que explote. El problema es que un proceso que atrapó un error que no entiende sigue vivo pero corrupto, y un proceso corrupto es peor que un proceso muerto, porque el muerto al menos avisa. La apuesta de Erlang es que después de un error inesperado el estado ya no es confiable, y el estado más confiable disponible es el inicial. Entonces: morite rápido, ruidosamente, y dejá que alguien de afuera —el supervisor, que no tocó tu estado podrido— te vuelva a arrancar limpio.

El corrimiento es de altura. Lo que tiene que sobrevivir no es tu función. Es el sistema. Tu función es descartable, y aceptar eso es lo que permite que el sistema no lo sea.

> 🕳️ **HUECO — necesita a César:** ¿escribiste Erlang o Elixir alguna vez, aunque sea de juguete? ¿O tu contacto es sólo de lector?

> 🕳️ **HUECO — necesita a César:** ¿te tocó operar algún sistema que no se podía parar (STG, Ministerio de Cultura)? Una frase concreta sobre qué se hacía ahí cuando algo fallaba: ¿se reiniciaba, se parcheaba en caliente, se rezaba?

### Qué queda

Erlang/OTP sigue vivo y mantenido[^otp], y *Programming Erlang*[^prog-erlang] sigue siendo la puerta de entrada. Pero lo interesante es cuánto de esto se filtró hacia afuera sin que le pongamos el nombre: supervisores, reinicio como estrategia de recuperación, procesos aislados que se hablan por mensajes, «que se caiga y lo levantamos». Si trabajás con contenedores que se reinician solos y un orquestador que los vigila, estás usando un supervisor tree con otro vocabulario y muchísimo más YAML[^herederos].

Armstrong tenía una charla, *The Mess We're In*[^mess], sobre por qué la programación terminó siendo el desastre que es. Y hay una segunda película[^sequel], porque por supuesto que la hay. Empezá por la primera igual: doce minutos —o los que sean— bien invertidos.

[^movie]: *Erlang the Movie*, Ericsson, 1990 (grabación de la demo dada en ISS90, Estocolmo) — [vídeo en YouTube](https://www.youtube.com/watch?v=BXmOlCy0oBM).
[^cast]: En cámara aparecen Mike Williams, Joe Armstrong y Bjarne Däcker —del Computer Science Laboratory de Ericsson— demostrando telefonía; Robert Virding suele listarse también entre los participantes. No son actores profesionales sino gente del equipo. Fuentes: [ficha en Letterboxd](https://letterboxd.com/film/erlang-the-movie/) y [«Twenty Years of Open Source Erlang», Erlang Solutions](https://www.erlang-solutions.com/blog/twenty-years-of-open-source-erlang/).
[^duracion]: La película dura **12 minutos**; es la grabación de la demo dada en ISS90 (Estocolmo, 1990). Fuente: [ficha en Letterboxd](https://letterboxd.com/film/erlang-the-movie/).
[^nueves]: El switch AXD301 de Ericsson —más de un millón de líneas de Erlang— es citado habitualmente con una disponibilidad **reportada** de "nueve nueves" (99,9999999 %). Fuente: [Erlang (programming language) — Wikipedia](https://en.wikipedia.org/wiki/Erlang_(programming_language)), que atribuye la cifra al AXD301. No pude localizar la página exacta de la tesis de Armstrong (2003) donde se discute el sistema; la cifra debe presentarse como *reportada*, no como una medición independiente.
[^tesis]: Joe Armstrong, *Making reliable distributed systems in the presence of software errors*, tesis doctoral, 2003 — [PDF](https://erlang.org/download/armstrong_thesis_2003.pdf).
[^otp]: [Erlang/OTP — sitio oficial](https://www.erlang.org/).
[^prog-erlang]: Joe Armstrong, *Programming Erlang*, 2.ª ed., Pragmatic Bookshelf, oct. 2013 — ISBN 978-1-937785-53-6, 546 pp. — [ficha del editor](https://pragprog.com/titles/jaerlang2/programming-erlang-2nd-edition/).
[^herederos]: El modelo se propagó fuera de Erlang: [Elixir](https://en.wikipedia.org/wiki/Elixir_(programming_language)) (José Valim, 2012) corre sobre la misma máquina virtual BEAM y hereda OTP y la supervisión; [Akka](https://en.wikipedia.org/wiki/Akka_(toolkit)) (Jonas Bonér) lleva el modelo de actores a la JVM «with inspiration drawn from Erlang». La comparación con los orquestadores de contenedores (reinicio supervisado, self-healing) es una **analogía**, no una línea de descendencia histórica documentada.
[^mess]: Joe Armstrong, *The Mess We're In*, Strange Loop 2014 — [charla en YouTube](https://www.youtube.com/watch?v=lKXe3HUG2l4).
[^sequel]: *Erlang the Movie II — The Sequel*, 2013 — [vídeo en YouTube](https://www.youtube.com/watch?v=rRbY3TMUcgQ).

> 🕳️ **HUECO — necesita a César:** ¿viste *The Mess We're In*? Si sí, una frase tuya sobre qué te dejó — sirve para cerrar el post con voz propia en vez de con una lista de links.

> 🕳️ **HUECO — necesita a César:** ¿querés que el cierre enganche con [[H-04]] (sistemas que no se pueden parar) o con [[A1-03]] (Forth)? El outline los tiene a los dos como cross-links, pero un post short aguanta un solo puente.

