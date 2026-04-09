### E-02 — fixperm: cómo escribí un Lisp en C porque tenía que arreglar permisos en SCO Unix

- **Archivo seed:** `dev/draft-fixperm-sco-unix.md`
- **Slug propuesto:** `fixperm-lisp-en-c-sco`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-fixperm-lisp-en-c-sco/index.md`
- **Serie:** E
- **Cross-links:** depende de [[tr-05]] (LISP de Winston-Horn); lleva a [[A2-02]] (Lisp papers), [[H-01]] (SCO Unix), [[E-09]] (Masterminds — el patrón de "necesitaba algo y me lo hice")
- **Idioma:** es
- **Madurez:** seed (una línea: "escrito en C, imitando lisp de patrick winston")
- **Length target:** medium (1200-1800 palabras)

**Concepto:** en algún momento de los 90, en una empresa que corría SCO Unix, necesitaba arreglar permisos sobre miles de archivos según reglas no triviales (por usuario, por extensión, por ruta, con excepciones). Hacerlo con `find` + `chmod` no alcanzaba. Lo terminé escribiendo en C, pero como había leído el LISP de Winston-Horn, lo escribí en *estilo Lisp*: una estructura tipo cons-cell, un evaluador chiquito, un mini DSL para las reglas. Funcionó. Y en el proceso entendí mucho más Lisp que leyendo el libro.

**Hook:** "tenía un problema concreto en SCO Unix: arreglar permisos de archivos según reglas que no entraban en `find -exec`. Lo lógico era usar Perl. No usé Perl. Escribí un Lisp en C. Sí, sin saber bien Lisp. Sí, fue una mala decisión para el cronograma. Sí, fue la mejor cosa que aprendí ese año."

**Outline:**
1. El contexto: SCO Unix, la empresa, el problema real con permisos masivos.
2. Por qué `find` + `chmod` no servía: las reglas eran condicionales y dependientes del estado.
3. La trampa: leí el LISP de Winston-Horn ese verano. Quería usarlo. No tenía Lisp instalado. Tenía cc.
4. La implementación — cons cells en C, un eval recursivo, un parser de S-expressions de juguete. Cuántas líneas (estimación: 800-1200).
5. El DSL resultante: cómo se escribían las reglas, ejemplo concreto.
6. Lo que aprendí en serio: por qué Lisp se siente *natural* desde adentro. No es la sintaxis — es la manipulación de estructuras como datos.
7. Lo que no aprendí en ese momento: hygienic macros, garbage collection real, tail calls. Eso vino después con [[A2-01]].
8. Cierre: el script todavía existe, en alguna cinta, con suerte.

**Bibliografía:**
- [[tr-05]] — Winston & Horn, *LISP*, Addison-Wesley 3.ª ed.
- [[tr-03]] — SICP, para el lector que quiera entender el patrón "intérprete metacircular".
- [Peter Norvig, *(How to Write a (Lisp) Interpreter (in Python))*, 2010](https://norvig.com/lispy.html) — la versión moderna del mismo ejercicio.
- [Paul Graham, *Roots of Lisp*, 2002](http://www.paulgraham.com/rootsoflisp.html) — el ensayo que muestra por qué Lisp puede caber en una página.
- [SCO Unix en Wikipedia](https://en.wikipedia.org/wiki/SCO_UNIX).
- [POSIX `find` y `chmod` — manuales modernos](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/find.html) — para contraste.

**Imágenes:**
- _Crear_: snippet del DSL resultante (4-6 líneas) en una caja, con la regla equivalente en `find` para mostrar la diferencia (~20 min).
- _Crear_: diagrama simple de cómo se representa una S-expression como árbol de cons cells (~30 min).

**Tags propuestos:** `['memoir', 'Lisp', 'C', 'SCO Unix', 'DSL', 'Winston Horn']`

**Estado actual:** seed con una línea; necesita reconstruir el código original o al menos un esbozo del DSL para que el post sea técnico, no sólo nostálgico.

