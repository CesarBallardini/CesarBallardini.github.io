### A1-02 — Erlang the Movie (y por qué deberías ver una película de un lenguaje)

- **Archivo seed:** `dev/draft-erlang.md`
- **Slug propuesto:** `erlang-the-movie`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-erlang-the-movie.md` (sin bundle, archivo plano; las imágenes son embeds de YouTube)
- **Serie:** A1
- **Cross-links:** depende de [[tr-09]]; lleva a [[A1-03]] (Forth, otra concurrencia rara), [[H-04]] (sistemas que no se pueden parar)
- **Idioma:** es
- **Madurez:** seed-with-sources
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
- [[tr-09]] — *Erlang the Movie* + Armstrong, *Programming Erlang*.
- [Joe Armstrong, *Making reliable distributed systems in the presence of software errors*](https://erlang.org/download/armstrong_thesis_2003.pdf), tesis SICS 2003 — el texto fundacional.
- [Erlang the Movie en YouTube](https://www.youtube.com/watch?v=BXmOlCy0oBM) — embed directo.
- [Erlang/OTP en su sitio oficial](https://www.erlang.org/).
- [The Pragmatic Bookshelf — Programming Erlang](https://pragprog.com/titles/jaerlang2/programming-erlang-2nd-edition/) — segunda edición.
- [Joe Armstrong: *The Mess We're In*](https://www.youtube.com/watch?v=lKXe3HUG2l4), Strange Loop 2014 — su charla sobre por qué la programación es un desastre.
- [Erlang the Movie II — The Sequel](https://www.youtube.com/watch?v=rRbY3TMUcgQ) — sí, hay segunda parte.

**Imágenes:**
- _Embed_: thumbnail de YouTube de la película (no es propiamente una imagen, es un iframe).
- _Wikimedia_: foto de Joe Armstrong — [Joe Armstrong (programmer)](https://commons.wikimedia.org/wiki/File:Joe_Armstrong.jpg) — license: ver descripción.
- _Crear_: opcional — diagrama simple SVG de un supervisor tree (3 cajas: supervisor → workers → "let it crash").

**Tags propuestos:** `['Erlang', 'Joe Armstrong', 'concurrencia', 'OTP', 'historia']`

**Estado actual:** seed con sources en `draft-erlang.md`.

