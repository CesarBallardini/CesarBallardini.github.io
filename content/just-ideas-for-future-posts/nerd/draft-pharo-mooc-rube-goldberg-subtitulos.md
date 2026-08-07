### J-05 — Pharo MOOC con audio inglés y subtítulos en español: la solución Rube Goldberg con nginx en Docker

- **Archivo seed (repo POC):** [github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles](https://github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles) — HTML, último push 2025-11-16
- **Slug propuesto:** `pharo-mooc-rube-goldberg-subtitulos`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-pharo-mooc-rube-goldberg-subtitulos/index.md`
- **Serie:** J — curiosidad nerd lateral + memoir corto
- **Cross-links:** lleva a [[A1-11]] (Pharo Smalltalk como tema, el MOOC en cuestión)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César) — base: **complete-poc**, Dockerfile funciona
- **Length target:** short (800-1200 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** existe un MOOC oficial de Pharo Smalltalk dictado en la plataforma FUN (France Université Numérique) con audio en francés e inglés y subtítulos en varios idiomas. Yo quería mirarlo con audio en *inglés* (que entiendo) y subtítulos en *español* (que prefiero leer). El reproductor oficial de FUN no me permitía esa combinación porque cargaba el video y los VTT desde dominios distintos y mi browser cortaba por CORS. Mi solución, en sus propias palabras del README: *"solución estilo Rube Goldberg :wink:"*. Primer intento: un HTML player local que cargaba ambos. Falló por CORS. Segundo intento (que sí funcionó): un container Docker con nginx actuando como proxy local que servía todo desde el mismo origen, y el reproductor HTML local tirando contra ese proxy. Cinco líneas de nginx.conf y todo el problema se evaporó. El post es la historia chica y la lección general: a veces la solución correcta a un problema de browser web es *poner un nginx en el medio*.

**Hook:** "yo quería mirar un MOOC de Pharo Smalltalk con audio en inglés y subtítulos en español. El reproductor oficial no me dejaba combinarlo. CORS. Mi solución: un container Docker con nginx que servía el video y los subtítulos desde el mismo origen, y un HTML local que se conectaba ahí. La llamé 'Rube Goldberg' en mi propio README. Funcionó. Acá cuento cómo, en 800 palabras."

**Outline:**
1. El MOOC oficial de Pharo en FUN: qué es, por qué lo quería mirar.
2. La preferencia: audio en inglés + subtítulos en español. Combinación que el reproductor oficial no soporta.
3. Primer intento: HTML local con `<video>` y `<track>`, cargando el video y el VTT desde URLs externas. El error CORS.
4. La explicación de CORS en una párrafo (sin entrar en headers).
5. Segundo intento: nginx en Docker como proxy. Cinco líneas de `nginx.conf`. Todo desde el mismo origen.
6. La parte autocrítica: sí, esto es Rube Goldberg. Sí, hay maneras más elegantes (extensión browser, descargar todo localmente, ver con VLC). Pero esta era la que me salía rápido.
7. La lección general: cuando un browser corta por CORS, *poner un nginx en el medio* es la respuesta correcta sorprendentemente a menudo.
8. Cierre.

**Bibliografía:** _(todas las URLs de abajo fueron fetcheadas y verificadas en la pasada de fuentes del 2026-07-16; flag de bitrot al final de cada una)_

- Repo del POC: [CesarBallardini/pharo-mooc-english-audio-spanish-subtitles](https://github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles) — verificado: existe, contiene `Dockerfile`, `nginx.conf`, `index.html`, `pharo-mooc-english-audio-spanish-subtitles-with-cors-issues.html`, `LICENSE`, `README.md`. El README confirma la frase del Concepto: «usar un contenedor Docker para correr un proxy nginx para simplemente mostrar una página Web con links, parece una solución estilo Rube Goldberg 😉», y también «Por problemas de CORS, este enfoque ya no funciona» sobre el primer intento. **frágil** (repo propio, puede renombrarse).
- [*Live Object Programming in Pharo* — ficha del curso en FUN](https://www.fun-mooc.fr/en/courses/live-object-programming-pharo/) — organiza Inria. Dice literal: «This course is fully dubbed in french and english» y «Subtitles in french, english, spanish and japanese». Campo *Languages*: «English and french». **frágil** (las URLs de curso en FUN se mueven — ver nota de corrección abajo) → backup [Wayback 2026-04-12](http://web.archive.org/web/20260412054709/https://www.fun-mooc.fr/en/courses/live-object-programming-pharo/) — **estable**.
- [*Pharo MOOC: Live Object Programming in Pharo*](https://mooc.pharo.org/) — sitio propio del MOOC, preferido sobre terceros por regla de la casa. Dice literal: «The Pharo Mooc is fully dubbed in french and english. It comes with subtitles in Japanese, english, french and spanish». Ofrece descarga directa de slides, ejercicios, videos EN, videos FR y subtítulos en los cuatro idiomas. Corre en FUN «in average every 18 months». **frágil** → backup [Wayback 2026-06-29](http://web.archive.org/web/20260629151918/https://mooc.pharo.org/) — **estable**.
- [MDN — *Cross-Origin Resource Sharing (CORS)*](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) — **estable**. Ojo: la URL vieja `/Web/HTTP/CORS` que tenía el draft redirige, pero la canónica ahora lleva `/Guides/`; usar la canónica.
- [MDN — *Same-origin policy*](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy) — canónica actual (lleva `/Defenses/`). **estable**.
- [MDN — *`<track>`: The Embed Text Track element*](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track) — **estable**. Fuente que resuelve la marca de verificación sobre `<track>`: el atributo `src` «must have the same origin as the document — unless the `<audio>` or `<video>` parent element of the `track` element has a `crossorigin` attribute».
- [nginx — sitio oficial](https://nginx.org/) — **estable**. Se define como «an HTTP web server, reverse proxy, content cache, load balancer, TCP/UDP proxy server, and mail proxy server»; escrito originalmente por Igor Sysoev, licencia BSD de 2 cláusulas.
- [nginx — directiva `proxy_pass` (`ngx_http_proxy_module`)](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass) — **estable**. «Sets the protocol and address of a proxied server and an optional URI to which a location should be mapped». Es la directiva que menciona la sección de autocrítica.
- Cross-link [[A1-11]] para Pharo como tema.

**Imágenes:**
- _Crear_: screenshot del reproductor con video Pharo en inglés y subtítulos en español visibles (~10 min).
- _Crear_: las 5 líneas de `nginx.conf` en una caja (~5 min).

**Tags propuestos:** `['nginx', 'Docker', 'CORS', 'Pharo', 'MOOC', 'Rube Goldberg', 'subtitulos', 'nerd lateral']`

**Estado actual:** **POC funcional + fuentes verificadas (pasada del 2026-07-16)**.

> ⚠️ **CORRECCIÓN — el draft citaba un curso que no existe.** El footnote `[^fun]` y la Bibliografía apuntaban a `fun-mooc.fr/en/courses/pharo-syntax-and-tools/` con el título *«Pharo: Syntax and Tools»*. **Esa URL devuelve HTTP 404 y ese curso no existe**: era una cita inventada por la pasada de prosa. El MOOC real es **[*Live Object Programming in Pharo*](https://www.fun-mooc.fr/en/courses/live-object-programming-pharo/)**, de Inria, dictado por Damien Cassou, Stéphane Ducasse y Luc Fabresse. Corregido en el footnote y en la Bibliografía. Moraleja para el próximo que edite este archivo: la prosa generada trae URLs plausibles que no resuelven — hay que abrirlas.

> ⚠️ **Nota — un párrafo quedó con el argumento flojo.** La sección «Sí, es Rube Goldberg» dice que «bajar el video hay que averiguar cómo», pero mooc.pharo.org ofrece descarga directa de videos y subtítulos. El Concepto y el Hook **no están en duda** (el CORS y el proxy nginx están confirmados por el README del propio repo), pero ese párrafo necesita una decisión de César: ver la nota al pie de esa sección.

**Sourceado en esta pasada** (todo fetcheado y verificado, nada de memoria): la ficha del curso real en FUN + su backup en Wayback; el sitio propio del MOOC (mooc.pharo.org) + backup, preferido sobre terceros por regla de la casa; MDN CORS y MDN Same-origin policy, ambos con su URL canónica actualizada (las viejas redirigen); MDN `<track>`, que resolvió su marca con cita textual; nginx sitio oficial y la doc de `proxy_pass`; y el repo del POC, cuyo README confirma textualmente la frase «solución estilo Rube Goldberg 😉» y el «Por problemas de CORS, este enfoque ya no funciona» del primer intento.

**Las dos marcas de verificación quedaron resueltas**: (1) idiomas del MOOC — doblaje completo en francés e inglés, subtítulos en francés, inglés, español y japonés, confirmado por dos fuentes independientes que coinciden; no encontré histórico de si la oferta cambió desde 2025, pero el snapshot de Wayback de 2026-04 ya la muestra así. (2) `<track>` y mismo origen — MDN lo documenta explícitamente en el atributo `src`, con la excepción del atributo `crossorigin` en el `<video>` padre; el párrafo de CORS se reescribió para apoyarse en la cita textual en vez de afirmarlo al voleo.

**Lo que sigue pendiente y ninguna búsqueda web puede resolver:** los 7 huecos 🕳️ — todos son memoria o código de César (por qué y cuándo encaró el MOOC, si lo terminó, el mensaje de error exacto, los dominios que cruzaron el origen, si el video arrancaba o no, si hubo tercera iteración, y el contenido literal de `nginx.conf` y `Dockerfile`). El repo existe y tiene esos dos archivos: hay que abrirlos y pegar el código real. También sigue pendiente el cross-link [[A1-11]].

Post corto, divertido, sale en una sesión. Ya tiene **borrador de prosa completo** (ver abajo, ~1150 palabras tras la pasada de fuentes, dentro del target short) siguiendo el outline de 8 puntos. Lo que quedó escrito: el encuadre del MOOC, la explicación de CORS apoyada en MDN, el arco de los dos intentos, la autocrítica y la lección general.

**Checklist antes de publicar:** (1) abrir el repo del POC y pegar el `nginx.conf` y el `Dockerfile` reales, sin reconstruirlos de memoria; (2) contestar los 7 huecos 🕳️; (3) decidir qué hacer con el párrafo de «bajar el video» (ver la nota en la sección «Sí, es Rube Goldberg»); (4) resolver el cross-link [[A1-11]]; (5) elegir entre `docker run` y `docker compose up` para el ejemplo de arranque.

---

## Borrador de prosa

⚠️ **Curiosidad nerd lateral — esto no es ciencia de la computación.**

Yo quería mirar un MOOC de Pharo Smalltalk con el audio en inglés y los subtítulos en español. Nada más que eso. El reproductor oficial no me dejaba combinarlo: elegías un idioma y te llevabas el paquete completo, audio y subtítulos juntos, tomalo o dejalo. Y cuando intenté armar la combinación a mano, el browser me cortó por CORS.

La solución que terminó funcionando fue un container Docker con nginx adentro, haciendo de proxy, sirviendo el video y los subtítulos desde el mismo origen, y un HTML local mío conectándose contra ese proxy. En mi propio README la llamé «solución estilo Rube Goldberg :wink:», y no me arrepiento del rótulo. Funcionó. Acá te cuento cómo, y cuál es la lección general que me llevé.

### El MOOC

Hay un MOOC oficial de Pharo dictado en FUN, la plataforma de France Université Numérique.[^fun] Es el curso de referencia para entrar a Pharo: sintaxis, herramientas, el ambiente vivo, todo eso que en Smalltalk se aprende mejor mirando a alguien usarlo que leyendo un libro. De Pharo como lenguaje y como ambiente hablo en [[A1-11]]; acá no me interesa el lenguaje sino el trámite de poder mirar los videos.

> 🕳️ **HUECO — necesita a César:** ¿en qué momento y por qué encaraste el MOOC de Pharo? ¿Fue curiosidad suelta, un proyecto concreto que querías arrancar en Pharo, o venías de leer algo que te empujó? Una o dos frases.

> 🕳️ **HUECO — necesita a César:** ¿lo terminaste? ¿Cuánto llegaste a ver con el reproductor casero antes de aburrirte, terminar el curso, o abandonarlo?

Siendo un curso francés publicado en una plataforma francesa, el material viene, en palabras del propio sitio del MOOC, «totalmente doblado en francés e inglés», y «con subtítulos en japonés, inglés, francés y español».[^moocpharo] La ficha del curso en FUN dice lo mismo: doblaje en francés e inglés, subtítulos en francés, inglés, español y japonés.[^fun] Es decir: las dos piezas que yo quería —el audio en inglés y los subtítulos en español— existían, y estaban publicadas. El problema no era de disponibilidad. Era de combinatoria.

### La combinación que nadie ofrece

Mi preferencia es rara pero no exótica: entiendo el inglés hablado sin esfuerzo, pero leo mucho más rápido en español. Si tengo las dos cosas al mismo tiempo, el audio en inglés me da el contenido y el subtítulo en español me da el respaldo cuando el disertante se apura o pronuncia un término que no espero. El reproductor oficial no contempla ese cruce, y es entendible: para el 99 % de la gente, «idioma del curso» es una sola perilla.

Yo quería dos perillas. Y en la web, cuando querés dos perillas y hay una, la respuesta obvia es armarte el reproductor vos mismo.

### Primer intento: un HTML de doce líneas

El primer intento fue lo mínimo posible: un archivo HTML local con un `<video>` apuntando a la URL del video con audio en inglés, y un `<track>` apuntando a la URL del archivo VTT con los subtítulos en español. Ambas URLs, las públicas, las que servía la plataforma.

Falló. CORS.

> 🕳️ **HUECO — necesita a César:** ¿tenés a mano el mensaje de error exacto que tiraba la consola del browser? ¿Y qué browser estabas usando? Si el repo o tus notas lo guardan, va literal en el post: los mensajes de CORS son parte del folclore.

> 🕳️ **HUECO — necesita a César:** ¿de qué dominios venían cada cosa? El Concepto dice «dominios distintos» — ¿el video salía de un CDN y los VTT de otro host, o eran dos subdominios de la misma plataforma? Sin esto no puedo contar bien de dónde salía el cruce de orígenes.

### CORS en un párrafo

Para el que no lo sufrió: el browser, por diseño, no deja que una página cargada desde un origen lea libremente recursos de otro origen. Es la política de mismo origen —un mecanismo de seguridad que «restringe cómo un documento o script cargado por un origen puede interactuar con un recurso de otro origen», en la definición de MDN[^sop]— y CORS es el mecanismo por el cual un servidor puede decir «este recurso sí, dejalo pasar», mandando ciertos headers en la respuesta.[^cors] Si el servidor no lo dice, el browser corta, y no hay nada que vos puedas hacer del lado del cliente para convencerlo. Ese es el punto importante y el que más cuesta aceptar: **el CORS no es un permiso que vos otorgás, es un permiso que el servidor remoto otorga**. Si el dueño del servidor no puso el header, tu página no lee el archivo. Punto.

Y el `<track>` de subtítulos no es un caso al pasar: es un caso explícito en la especificación. MDN lo dice sin vueltas sobre el atributo `src` del `<track>`: la URL «debe tener el mismo origen que el documento — a menos que el elemento padre `<audio>` o `<video>` del elemento `track` tenga un atributo `crossorigin`».[^track] O sea que el `<track>` cross-origin es, por default, imposible; y la única puerta que deja abierta —el atributo `crossorigin`— sigue dependiendo de que el servidor remoto mande los headers. La perilla existe, pero no es mía.

> 🕳️ **HUECO — necesita a César:** cuando falló el primer intento, ¿el video igual se reproducía y lo único que faltaba eran los subtítulos, o no arrancaba nada? Es un detalle chico pero le da color al párrafo.

### Segundo intento: poner un nginx en el medio

Si el problema es que las cosas vienen de orígenes distintos, la solución es hacer que vengan del mismo origen. No hace falta cambiar el mundo: alcanza con mentirle al browser de manera honesta. Un nginx local[^nginx] que reciba mis pedidos y los reenvíe a la plataforma, devolviendo todo — video y subtítulos — bajo `localhost`. Desde el punto de vista del browser hay un solo origen y no hay nada que autorizar. La política de mismo origen queda satisfecha porque efectivamente hay un solo origen.

Lo armé como un container Docker con nginx adentro y un `nginx.conf` de cinco líneas útiles.[^repo] Mi HTML local dejó de apuntar a las URLs públicas y pasó a apuntar al proxy. Y el problema se evaporó.

> 🕳️ **HUECO — necesita a César:** ¿salió a la primera o hubo pelea? Si hubo una tercera iteración intermedia que no quedó en el repo, contala en dos frases: los posts de este tipo mejoran mucho cuando el segundo intento tampoco anda del todo.

> 🕳️ **HUECO — necesita a César:** acá va el `nginx.conf` real, copiado del repo (no lo voy a reconstruir de memoria). ¿Podés pegarlo? Igual el `Dockerfile`, y decime si el post debería mostrar `docker run` o `docker compose up` para levantarlo.

### Sí, es Rube Goldberg

No pienso defender la elegancia de esto. Levantar un container con un servidor web de producción para poder leer subtítulos es, digamos, desproporcionado. Había alternativas más sobrias: una extensión de browser que relaje los chequeos, bajarme el video y el VTT a disco y abrirlos con VLC, o incluso pedirle a la plataforma que sirva la combinación. Todas mejores en abstracto.

Pero las alternativas mejores en abstracto tienen un costo que nadie mide: el tiempo que tardás en llegar a ellas. Yo ya tengo Docker instalado, ya sé escribir un `proxy_pass`, y la distancia entre «tengo el problema» y «tengo la solución andando» era de unos minutos. La extensión hay que buscarla, evaluarla, confiar en ella. Bajar el video hay que averiguar cómo. La solución fea que ya sabés hacer le gana casi siempre a la solución linda que tenés que aprender, cuando el problema es tuyo, es chico, y no lo va a mantener nadie más.

> ⚠️ **Nota de la pasada de fuentes — el argumento de arriba tiene un flanco flojo.** Fui a verificar la alternativa «bajar el video» y resulta que el sitio propio del MOOC, [mooc.pharo.org](https://mooc.pharo.org/), ofrece **descarga directa** de los videos EN, los videos FR y los subtítulos en los cuatro idiomas, semana por semana, con links visibles en la página.[^moocpharo] O sea que «bajar el video hay que averiguar cómo» no se sostiene tal como está escrito: no había nada que averiguar, estaba a un click en la página oficial del curso. Eso **no rompe** el Concepto ni el Hook —el reproductor de FUN efectivamente no combina las dos perillas, el CORS efectivamente cortó el primer intento, y el README lo confirma— pero sí debilita este párrafo en particular. Dos salidas posibles, César, elegí vos: (a) si en su momento no sabías que existían esas descargas, decilo así, que es más honesto y más gracioso — «la solución fea ganó porque ni miré si había una linda»; o (b) si lo sabías y aun así preferiste el proxy (por no bajar ~7 semanas de video a disco, por querer el player web, por lo que sea), contá ese motivo, que es mejor argumento que el actual. Lo que no conviene es dejar la frase como está, porque un lector que abra el sitio del MOOC la desarma en diez segundos.

### La lección

Me quedó una regla práctica, y la uso más seguido de lo que me gustaría admitir: **cuando el browser te corta por CORS y no controlás el servidor remoto, poner un nginx en el medio es la respuesta correcta sorprendentemente a menudo**. No es un truco sucio; es exactamente el mecanismo que la política de mismo origen contempla. El browser no pregunta quién es realmente el dueño del contenido: pregunta de qué origen lo estás cargando. Si vos sos el origen, vos decidís.

Y bueno: pude ver el MOOC con audio en inglés y subtítulos en español, que era todo lo que quería.

[^repo]: Repo del POC: [CesarBallardini/pharo-mooc-english-audio-spanish-subtitles](https://github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles).
[^fun]: [*Live Object Programming in Pharo*, France Université Numérique](https://www.fun-mooc.fr/en/courses/live-object-programming-pharo/) — MOOC dictado por Inria. Ficha del curso: doblaje en francés e inglés, subtítulos en francés, inglés, español y japonés. Copia de respaldo: [Wayback Machine, 2026-04-12](http://web.archive.org/web/20260412054709/https://www.fun-mooc.fr/en/courses/live-object-programming-pharo/).
[^moocpharo]: [*Pharo MOOC: Live Object Programming in Pharo*](https://mooc.pharo.org/) — sitio propio del MOOC (Inria / RMoD). A cargo de Damien Cassou (Université de Lille), Stéphane Ducasse (Inria) y Luc Fabresse (Mines Douai). Desde acá se descargan slides, ejercicios, videos EN y FR, y los subtítulos en los cuatro idiomas. Copia de respaldo: [Wayback Machine, 2026-06-29](http://web.archive.org/web/20260629151918/https://mooc.pharo.org/).
[^sop]: [MDN — *Same-origin policy*](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy).
[^cors]: [MDN — *Cross-Origin Resource Sharing (CORS)*](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS).
[^track]: [MDN — *`<track>`: The Embed Text Track element*](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track) — la restricción de mismo origen está documentada en el atributo `src`.
[^nginx]: [nginx — sitio oficial](https://nginx.org/). La directiva usada para el proxy es [`proxy_pass`, del módulo `ngx_http_proxy_module`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass).

