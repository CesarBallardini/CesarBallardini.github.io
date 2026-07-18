---
title: 'Un lector en voz alta para los posts'
description: 'Cómo agregué un reproductor de lectura en voz alta a este blog sin contratar ningún servicio de TTS en la nube: la Web Speech API del navegador, un hook de Ananke y un asset de Hugo. Setup, servicios, y la integración de punta a punta.'
tags: ['blog', 'Hugo', 'ananke', 'JavaScript', 'accesibilidad', 'text to speech', 'Web Speech API']
featured_image: 'hero-globo-de-dialogo.jpg'
---

A partir de hoy, cada post de este blog se puede **escuchar**. Abajo a la izquierda aparece un botoncito con un ▶; lo apretás y una voz empieza a leer el artículo, párrafo por párrafo, mientras resalta el que está sonando[^img_hero]. La voz la pone tu propio navegador.

<!--more-->

## El servicio que decidí *no* usar

Lo primero que uno piensa cuando quiere «texto a voz» de calidad es contratar uno de los servicios de síntesis neuronal que están de moda. Suenan increíble. Pero para un blog personal traen una lista de problemas que no me convencía: hay que pagar por carácter, hace falta un backend que guarde la API key (esto es un sitio estático en GitHub Pages: no tengo ni quiero un backend), y —lo que más me pesó— **habría que mandarle el texto de cada post a un tercero** para que lo convierta en audio. Demasiada complicación en mi opinión.

La alternativa es la Web Speech API[^webspeech], y más concretamente su interfaz `speechSynthesis`, que está en todos los navegadores modernos desde hace años. Es text-to-speech del lado del cliente: le pasás un texto, elige una de las voces que el sistema operativo tiene instaladas, y lo lee. Gratis, sin API key, sin backend, sin mandarle nada a nadie. El texto nunca sale de la máquina de quien lee.

El trato tiene su letra chica, claro. La voz **depende del dispositivo**: no controlo cuál se usa ni cómo suena, y la calidad va desde «sorprendentemente natural» en un Mac o un Windows reciente hasta bastante robótica en un GNU/Linux. No es la voz de estudio de un servicio pago. Pero para «escuchar un post mientras viajás» es más que suficiente, y el precio —cero, sin dependencias— es imbatible.

## Qué lee, y qué no

El corazón del reproductor es una función que recorre el cuerpo del post y arma una lista de párrafos para leer. No es tan simple como agarrar todo el texto: hay cosas que no querés escuchar. La recolección de datos:

- **Empieza por el título** del artículo (el `<h1>` del header), que en la plantilla de Ananke vive *afuera* del cuerpo, así que hay que buscarlo aparte.
- Después toma, en orden de aparición, los **encabezados** (`h2`–`h4`), **párrafos**, **ítems de lista** y **citas** (`blockquote`).
- **Saltea** lo que sería ruido: las etiquetas (tags) que aparecen al pie del post, las definiciones de footnotes, y los bloques de código (`<pre>`) —escuchar un `for i in range(10)` deletreado no le sirve a nadie—. El código *inline* entre backticks, en cambio, sí se lee, porque suele ser una palabra dentro de una oración.
- Limpia cada fragmento antes de leerlo: le saca los superíndices de las footnotes y los links-ancla de los encabezados, para que la voz no diga «uno» en medio de una oración cada vez que hay una referencia.

## Bilingüe de verdad

El blog es bilingüe (español por defecto, algo de inglés), así que el reproductor tenía que hablar el idioma de la página. Hugo expone el idioma en `.Language.Lang`, y lo bajo a JavaScript con una línea:

```javascript
var LANG = "{{ .Language.Lang }}";
```

A partir de ahí, todo va en tablas por idioma: los textos de la interfaz («Escuchar el artículo» / «Listen to this article»), el locale de la síntesis, y —lo más entretenido— el orden de preferencia de voces. Para un post en español, el reproductor busca primero una voz `es-AR`, después `es-419` (español latinoamericano genérico), y recién al final `es-ES`. Para inglés prioriza `en-US` y `en-GB`. Hay una excepción por dispositivo: en Android la única voz de español que suele venir instalada es la de España, así que ahí el orden arranca por `es-US` para conseguir un acento más neutro en lugar del castellano.  No hay ningún post en francés, la idea es primero trabajar con castellano e inglés, segundo Francia.

La Web Speech API **no expone el género de la voz**, así que para preferir una voz masculina —que es la que me pareció que mejor combinaba con el tono del blog— hay que inferirlo del nombre de la voz contra una lista de nombres conocidos. Es un truco medio artesanal, pero funciona razonablemente. Y por si el resultado no le gusta a quien escucha, hay un selector de voz que guarda la elección en `localStorage` de tu browser, separada por idioma.

## La integración con Hugo y Ananke

Toda esta maquinaria se enchufa en un solo punto de extensión del tema. Ananke tiene un mecanismo de *hooks*: busca parciales con nombres tipo `hooks/<nombre>.html` y, si existen en el proyecto, los inyecta. Ya lo usaba para [los diagramas mermaid](/posts/soy-mi-propio-abuelo-prolog/), en `layouts/partials/hooks/body-end.html`. Ese mismo archivo ahora tiene un segundo bloque:

```go-html-template
{{- if and .IsPage (ne .Params.audio_player false) }}
  ...markup del reproductor + <script>...
{{- end }}
```

La condición dice dos cosas. `.IsPage` limita el reproductor a las páginas de contenido (nada de esto aparece en la home ni en los listados de tags). Y `ne .Params.audio_player false` lo hace **opt-out**: está activado en todos los posts por default, y para desactivarlo en alguno puntual alcanza con poner `audio_player: false` en el frontmatter. No hay que tocar nada para que un post nuevo tenga su reproductor.

El CSS —el resaltado del párrafo que se está leyendo, el estilo del control de progreso— vive aparte, en `assets/ananke/css/audio-player.css`, y se inyecta inline sólo cuando el reproductor está presente, usando el [pipeline de assets de Hugo](https://gohugo.io/hugo-pipes/):

```go-html-template
{{- with resources.Get "ananke/css/audio-player.css" }}
<style>{{ .Content | safeCSS }}</style>
{{- end }}
```

El único acoplamiento fino con el tema es el selector que ubica dónde está la prosa del post: en la plantilla `single` de Ananke, el cuerpo del artículo está dentro de un `article .nested-copy-line-height`. Si ese selector no existe en la página —por ejemplo en una que no sea un post— el script se esconde solo y no molesta. Lo mismo si el navegador no soporta `speechSynthesis`: el reproductor se oculta antes de dibujar nada.

## Los detalles molestos

Como siempre, lo que parece un botón de play esconde un montón de casos borde:

- **La pausa nativa no es confiable.** En Chrome de escritorio, `synth.pause()` y `synth.resume()` funcionan bien. En Android y en Firefox, no: la pausa a veces mata la locución en vez de suspenderla. Así que el reproductor detecta esos navegadores y, en lugar de pausar, **cancela y vuelve a leer el párrafo actual** desde el principio cuando lo reanudás. No es elegante, pero es lo que hace que el botón se comporte igual en todos lados.
- **No hay barra de progreso real**, porque la API no te dice cuánto falta. Estimo la duración de cada párrafo por su cantidad de caracteres (con un factor que se ajusta según la velocidad elegida) y voy sumando. Es una aproximación, pero alcanza para que la barra avance de forma creíble.
- **Normalización de abreviaturas** antes de leer: «p. ej.» se convierte en «por ejemplo», «etc.» en «etcétera», las comillas angulares en rectas, los guiones largos en pausas. Sin eso, la voz deletrea o tropieza.

Hay un lindo efecto recursivo en todo esto: **este mismo post se puede escuchar**. Apretá el ▶ de abajo a la izquierda y vas a oír a tu navegador leyéndote la explicación de cómo funciona el reproductor que lo está leyendo.

## Transparencia

El código de este reproductor lo escribí con la asistencia de Claude[^claude], de Anthropic[^anthropic]. Las decisiones de diseño, en cambio, fueron mías: la elección de la Web Speech API por sobre un servicio pago, que fuera opt-out en vez de opt-in, que la voz por defecto siguiera el idioma de la página priorizando el acento local, y que todo se enchufara en el hook que ya existía en vez de hacer un fork del tema. La implementación de esas decisiones —los casos borde de la pausa, la estimación de progreso, la heurística de voces— es donde la asistencia rindió.

[^img_hero]: Globo de diálogo de historieta — ilustración propia hecha con Pillow para este post, dominio público.
[^webspeech]: [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) en MDN — documentación de `speechSynthesis`, `SpeechSynthesisUtterance` y el evento `voiceschanged`.
[^claude]: [Claude](https://www.claude.com/) — asistente de IA de Anthropic, usado acá como par de programación para escribir el código del reproductor.
[^anthropic]: [Anthropic](https://www.anthropic.com/) — empresa de investigación en seguridad de IA, creadora de Claude.
