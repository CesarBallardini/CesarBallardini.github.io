### A1-11 — Pharo Smalltalk: el sistema vivo donde el código y el mundo son la misma cosa

- **Archivo seed (repo POC):** ninguno propio aún; el POC pedagógico vive en [github.com/CesarBallardini/ansible-devops-workstation](https://github.com/CesarBallardini/ansible-devops-workstation) (instala Pharo) y en [github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles](https://github.com/CesarBallardini/pharo-mooc-english-audio-spanish-subtitles) (la solución para mirar el MOOC oficial)
- **Slug propuesto:** `pharo-smalltalk-sistema-vivo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-pharo-smalltalk-sistema-vivo/index.md`
- **Serie:** A1 — el lenguaje "raro" que faltaba en la grilla original; cruza con [[A1-01]] (Kay → Smalltalk), [[A2-03]] (Y combinator vivo en Ruby — el otro post sobre lenguajes-como-entornos), [[J-05]] (la solución Rube-Goldberg para mirar el MOOC oficial)
- **Idioma:** es
- **Madurez:** seed — concepto claro, hace falta sentarse a escribir
- **Length target:** medium (1500-2200 palabras)

**Concepto:** Smalltalk no es "un lenguaje". Es un *sistema*: una imagen de objetos vivos que persisten entre sesiones, donde editás el código *desde adentro del sistema mientras corre*, y cualquier cambio entra en efecto inmediatamente. Pharo es la implementación moderna, libre, mantenida, viva. El post explica por qué la idea de "imagen viva" es radical, qué se siente programar así por primera vez, y por qué Alan Kay (ver [[A1-01]]) sigue insistiendo en que esto es lo más cerca que estuvimos de la "revolución que no llegó".

**Hook:** "abrís Pharo. Aparece una ventana con varios paneles. Hacés click en una clase. Aparece su código. Lo modificás. Apretás Ctrl-S. Listo, ya funciona. *No compilaste nada*. *No reiniciaste nada*. El sistema entero está vivo, todo el tiempo, mientras vos escribís. Vos no programás *un programa*; vos hablás con un mundo de objetos vivos. Si nunca tuviste esa sensación, este post es para vos."

**Outline:**
1. Smalltalk en 30 segundos: Xerox PARC, los 70, Alan Kay, Adele Goldberg, Dan Ingalls. Smalltalk-80 como punto de referencia (ver [[A1-01]]).
2. Pharo en 30 segundos: la implementación moderna, fork de Squeak (2008), liderada por Stéphane Ducasse y la INRIA de Lille.
3. La idea de imagen: por qué tu *estado del sistema* persiste como un blob, en vez de regenerarse desde fuentes. Las ventajas (productividad mágica) y las desventajas (dependencia de la imagen, dificultad de versionar).
4. Las 5 clases que hay que conocer en Pharo para empezar: `Object`, `Number`, `Collection`, `String`, `Transcript`.
5. El "do it" / "print it" / "inspect it" del workspace — el REPL pero persistente.
6. El browser de clases — por qué editás clases en una ventana de 5 paneles en vez de en un archivo.
7. Lo extraño que cuesta entender al principio: que el código de Pharo *no vive en archivos*. Vive en la imagen. Los archivos son un export, no la fuente de verdad.
8. Cómo conviven Pharo y git en 2026: Iceberg, Metacello, Tonel.
9. El MOOC oficial de Pharo (FUN) y mi solución para mirarlo — cross-link [[J-05]].
10. Cierre: por qué incluso si nunca vas a programar Pharo en producción, una semana usándolo te cambia la cabeza.

**Bibliografía:**
- [Pharo — sitio oficial](https://pharo.org/).
- [*Pharo by Example* (libro libre, varias ediciones)](https://books.pharo.org/).
- [Stéphane Ducasse et al, *Deep into Pharo*, libro libre](https://books.pharo.org/deep-into-pharo/).
- [MOOC oficial de Pharo en FUN](https://www.fun-mooc.fr/en/courses/pharo-syntax-and-tools/) — el curso de Inria, gratuito.
- [Alan Kay, *The Early History of Smalltalk*, HOPL II 1993](http://worrydream.com/EarlyHistoryOfSmalltalk/).
- [Adele Goldberg & David Robson, *Smalltalk-80: The Language and its Implementation*, Addison-Wesley 1983 (el "Blue Book")](https://archive.org/details/smalltalk80imple00gold) — el libro fundacional.
- [Squeak — el ancestro libre de Pharo](https://squeak.org/).
- [Dan Ingalls, *Design Principles Behind Smalltalk*, Byte Magazine August 1981](https://www.cs.virginia.edu/~evans/cs655/readings/smalltalk.html) — el manifiesto.
- [Bret Victor, *Inventing on Principle*, CUSEC 2012](https://vimeo.com/36579366) — heredero estético de la idea de "sistema vivo".
- Cross-link [[A1-01]] para la conexión con Kay, [[J-05]] para el MOOC.

**Imágenes:**
- _Wikimedia_: foto de Alan Kay y/o Dan Ingalls — disponibles bajo CC.
- _Crear_: screenshot del Pharo browser de clases con código abierto (~15 min — esto es la imagen central del post).
- _Crear_: GIF / animación corta del "do it" en el playground (~30 min, opcional).
- _Crear_: comparación side-by-side de un pequeño programa en Pharo vs en Java/Python (~20 min).

**Tags propuestos:** `['Pharo', 'Smalltalk', 'sistema vivo', 'imagen', 'Alan Kay', 'Squeak', 'INRIA', 'lenguajes vivos']`

**Estado actual:** sin seed propio escrito, pero el material está bien sembrado: el `ansible-devops-workstation` instala Pharo (lo uso para enseñar), y el repo `pharo-mooc-english-audio-spanish-subtitles` muestra que ya estoy mirando el MOOC oficial. Post tirado a publicar después de terminar el MOOC.

