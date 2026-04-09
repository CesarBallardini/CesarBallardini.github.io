### J-05 — Pharo MOOC con audio inglés y subtítulos en español: la solución Rube Goldberg con nginx en Docker

- **Archivo seed (repo POC):** [github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles](https://github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles) — HTML, último push 2025-11-16
- **Slug propuesto:** `pharo-mooc-rube-goldberg-subtitulos`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-pharo-mooc-rube-goldberg-subtitulos/index.md`
- **Serie:** J — curiosidad nerd lateral + memoir corto
- **Cross-links:** lleva a [[A1-11]] (Pharo Smalltalk como tema, el MOOC en cuestión)
- **Idioma:** es
- **Madurez:** **complete-poc** — Dockerfile funciona
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

**Bibliografía:**
- Repo del POC: [CesarBallardini/pharo-mooc-english-audio-spanish-subtitles](https://github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles).
- [MOOC oficial de Pharo en FUN](https://www.fun-mooc.fr/en/courses/pharo-syntax-and-tools/).
- [MDN — CORS explainer](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).
- [nginx — sitio oficial](https://nginx.org/).
- Cross-link [[A1-11]] para Pharo como tema.

**Imágenes:**
- _Crear_: screenshot del reproductor con video Pharo en inglés y subtítulos en español visibles (~10 min).
- _Crear_: las 5 líneas de `nginx.conf` en una caja (~5 min).

**Tags propuestos:** `['nginx', 'Docker', 'CORS', 'Pharo', 'MOOC', 'Rube Goldberg', 'subtitulos', 'nerd lateral']`

**Estado actual:** **POC funcional**. Post corto, divertido, sale en una sesión.

