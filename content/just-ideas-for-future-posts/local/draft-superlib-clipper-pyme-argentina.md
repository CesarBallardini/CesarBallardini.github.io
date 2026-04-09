### I-07 — SuperLib y Clipper: rescate de las herramientas de la PyME argentina de los 90

- **Archivo seed (repos POC):** [github.com/CesarBallardini/supfreec52](https://github.com/CesarBallardini/supfreec52) (Garry A. Prefontaine SuperLib free release, 1 star, 2021-06-30) + [github.com/CesarBallardini/vagrant-clip-itk](https://github.com/CesarBallardini/vagrant-clip-itk) (Vagrant + Debian + Clip itk, 2024-08-21)
- **Slug propuesto:** `superlib-clipper-pyme-argentina`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-superlib-clipper-pyme-argentina/index.md`
- **Serie:** I — fuerte cruce con [[A1-05]] (Clipper como lenguaje), [[H-03]] (FoxBase como hermano de los DBF)
- **Cross-links:** lleva a [[A1-05]], [[H-03]], [[I-09]] (ZinjaI: la otra herramienta argentina de los 90)
- **Idioma:** es
- **Madurez:** **complete-poc** ambos repos — `supfreec52` es archivo (rescate de la versión libre de SuperLib), `vagrant-clip-itk` es lab funcional con scripts de provisión
- **Length target:** medium (1500-2200 palabras)

**Concepto:** Clipper era *el* lenguaje de los desarrolladores de software de gestión en la Argentina de los 90. SuperLib (Garry A. Prefontaine) era *la* librería que la mayoría de los proyectos Clipper usaba para interfaces de usuario, archivos indexados, manejo de errores y reportes. Cuando Clipper murió comercialmente, el ecosistema sobrevivió en archivos `.zip` que circulaban en BBSs y FTPs, hasta que internet los empezó a perder. Mis dos repos preservan eso: `supfreec52` es la versión libre de SuperLib (Garry liberó la última versión 5.2d sin cargo) subida a GitHub para que no desaparezca; `vagrant-clip-itk` es una VM Debian que compila el compilador Clip (de itk.ru, un fork open-source moderno de Clipper) junto con SuperLib, dejando el entorno listo para abrir un fuente `.prg` y compilarlo. El post cuenta el rol cultural de Clipper en la PyME argentina, el rescate de las herramientas, y cómo usar Clip moderno para mantener código viejo.

**Hook:** "si fuiste programador de gestión en la Argentina de los 90, casi seguro escribiste Clipper. Y casi seguro usaste SuperLib. Cuando Clipper murió comercialmente, ese código se quedó huérfano en miles de PyMEs. Hoy, en 2026, tenés todavía la opción de levantar una VM Debian, compilar tu `.prg` viejo con Clip (la implementación libre moderna), enlazar contra SuperLib, y obtener un binario que corre. Acá explico cómo, y cuento por qué importa que esas herramientas no desaparezcan."

**Outline:**
1. Clipper en la Argentina de los 90: *el* lenguaje de la PyME. Anécdota cultural.
2. SuperLib: qué hacía, por qué todo el mundo la tenía, qué pasó cuando Clipper murió.
3. La liberación: Garry A. Prefontaine puso la última versión 5.2d como freeware con un release-note TXT. Mi repo `supfreec52` la preserva.
4. Clip (itk.ru): el fork open-source moderno de Clipper, mantenido en Rusia, con compatibilidad razonable.
5. Mi `vagrant-clip-itk`: VM Debian 10 + Clip + SuperLib + scripts de provisión `compila_clip`, `compila_superlib`, `instala_clip`. Cómo se usa.
6. La conexión con Harbour y xHarbour (los otros forks libres de Clipper).
7. Lo que se rescata: no es sólo código, es una *manera de programar* que existía en español y que casi nadie documenta hoy.
8. Cierre: si tenés un sistema Clipper viejo y querés mantenerlo, la receta funciona.

**Bibliografía:**
- Repos: [supfreec52](https://github.com/CesarBallardini/supfreec52), [vagrant-clip-itk](https://github.com/CesarBallardini/vagrant-clip-itk).
- [Clip (itk.ru)](http://www.itk.ru/clipper/clip.en.html) — la implementación libre rusa.
- [Harbour](https://harbour.github.io/) — el fork libre principal.
- [xHarbour](http://www.xharbour.org/) — el otro fork.
- [Wikipedia — Clipper (programming language)](https://en.wikipedia.org/wiki/Clipper_(programming_language)).
- [c2 wiki — Clipper](https://wiki.c2.com/?ClipperLanguage).
- Cross-link [[A1-05]] [[H-03]].

**Imágenes:**
- _Crear_: screenshot del prompt de Clip compilando un `.prg` simple en la VM (~10 min).
- _Crear_: scan de la documentación física de SuperLib si la tengo (~15 min, opcional).

**Tags propuestos:** `['Clipper', 'SuperLib', 'Clip', 'Harbour', 'PyME', 'Argentina', 'Vagrant', 'historia local']`

**Estado actual:** **POC funcional** — los dos repos en GitHub. Post combina los dos en una historia de rescate cultural.

