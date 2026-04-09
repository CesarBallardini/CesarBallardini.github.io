### B-08 — Warren's Abstract Machine y la arqueología de implementaciones de Prolog (micro-PROLOG, small-prolog, wambook)

- **Archivo seed:** `github.com/CesarBallardini/wambook` (fork, 2020) + `github.com/CesarBallardini/small-prolog-walnut-creek-original` (fork, 2024) + `github.com/CesarBallardini/micro-PROLOG` (fork, 2018, Spectrum micro-Prolog T1.0 disassembled)
- **Slug propuesto:** `warren-abstract-machine-arqueologia-prolog`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-warren-abstract-machine-arqueologia-prolog/index.md`
- **Serie:** B — deep dive sobre cómo se implementa *de verdad* un lenguaje declarativo
- **Cross-links:** depende de [[A1-10]] (el post de Prolog "soy mi propio abuelo" — la experiencia del lector); lleva a [[B-02]] (Okasaki — estructuras de datos puramente funcionales, otro "qué hay debajo"), [[I-03]] (Spectrum y MicroHobby — donde apareció micro-PROLOG), [[I-07]] (SuperLib Clipper — otra reliquia de los 80 rescatada), [[A1-08]] (kl1c — lógica concurrente, primo cercano de Prolog)
- **Idioma:** es
- **Madurez:** tres repos forkeados listos (wambook, small-prolog-walnut-creek-original, micro-PROLOG) — material abundante, falta hilar la narrativa
- **Length target:** long (2500-3500 palabras) — es un post técnico denso con tres sub-historias

**Concepto:** ¿cómo se implementa realmente un intérprete de Prolog? La respuesta canónica es la Warren Abstract Machine (David H D Warren, 1983) — un conjunto mínimo de instrucciones para una máquina virtual que ejecuta Prolog con unificación, backtracking y trail eficientes. El post recorre tres implementaciones históricas de distinto porte y cuenta qué se aprende de cada una: (1) el *micro-PROLOG T1.0* para ZX Spectrum, un intérprete completo de Prolog que cabe en 16 KB y cuya Z80 assembly fue desensamblada (el repo `micro-PROLOG` tiene el source); (2) el *small-prolog* de Henri de Feraudy, un Prolog mínimo en C que se puede leer en una tarde; (3) la *WAM tutorial reconstruction* de Hassan Aït-Kaci (el wambook) — el libro de texto canónico sobre la WAM. Tres escalones: juguete heroico → didáctico legible → máquina abstracta de verdad.

**Hook:** "¿cómo cabe un intérprete de Prolog completo en 16 KB en un Spectrum de 1984? Y ¿cómo es que 20 años después Hassan Aït-Kaci escribe un libro entero de 114 páginas para explicar la máquina virtual (WAM) que lo hace eficiente? Son la misma pregunta, en dos escalas. Tengo en mi GitHub los tres escalones: el *micro-PROLOG* desensamblado del Spectrum, un *small-prolog* de 3000 líneas en C, y el wambook. El post los recorre en orden de complejidad creciente — tres visitas a la misma idea, una en assembler Z80, otra en C, otra en abstracción formal. Al final del post entendés por qué la unificación es la operación más rara y hermosa de la computación."

**Outline:**
1. **La pregunta de fondo**: ¿qué *operaciones primitivas* necesita un intérprete de Prolog para funcionar? Respuesta corta: unificación, backtracking, resolución SLD, manejo de trail y choice points. Respuesta larga: los 30 opcodes de la WAM.
2. **Escalón 1 — micro-PROLOG T1.0 para Spectrum 48K**. Desarrollado por *Logic Programming Associates* a principios de los 80 para ZX Spectrum. Sintaxis no estándar (micro-Prolog usaba listas como predicados). El repo `micro-PROLOG` tiene la ROM desensamblada. Qué cabe en 16 KB: un parser, un unificador simple, un motor de resolución, una micro-biblioteca. Qué NO cabe: optimización de colas, indexado de primera cláusula, compilación a WAM. La anécdota del Spectrum aprendiendo Prolog por escrito ([[I-03]] conecta acá).
3. **Escalón 2 — small-prolog de Henri de Feraudy**. ~3000 líneas de C, toma archivos `.pl`, los parsea, los ejecuta. Diseñado para *ser leído*. La estructura: estructuras `term`, un ambiente de binding, el loop principal de unificación recursiva, el trail como stack explícito. Un ejercicio pedagógico perfecto. Cómo clonarlo, compilarlo y modificarlo hoy (el fork en mi GitHub).
4. **Escalón 3 — Warren Abstract Machine (wambook)**. La idea central: *compilar* Prolog a instrucciones de máquina abstracta en vez de interpretarlo estructura por estructura. Los 30 opcodes de la WAM, agrupados en 4 familias: instrucciones de put (construir términos en registros), get (deconstruir términos con unificación), indexación, control de flujo. Por qué este paso de "compilación" es lo que hace a SWI-Prolog y Sicstus ser competitivos en velocidad con C para ciertos problemas.
5. **El corazón del asunto — la unificación**. La operación mágica. Dos términos, un conjunto de bindings. Se unifican si existen bindings que los hacen idénticos. Contrasta con pattern matching (más simple, unidireccional) y con type inference (más abstracto, sin ejecución). La unificación *resuelve* en tiempo de ejecución lo que otros lenguajes calculan en tiempo de compilación.
6. **Backtracking y choice points**. Cómo la WAM mantiene los puntos de elección en el stack para "deshacer" computaciones y probar alternativas. El trail como lista de variables a des-bindear. Por qué es más eficiente que mantener copias del ambiente.
7. **Indexado de primera cláusula (first-argument indexing)**. La optimización que hace a los intérpretes modernos ser ~100× más rápidos que la implementación ingenua: cuando hay muchas cláusulas para un mismo predicado, la WAM mira el primer argumento del goal y salta directamente a las cláusulas que *podrían* unificar. Sin este truco, Prolog no sería viable para bases de hechos grandes.
8. **¿Y entonces por qué no lo usamos?** La pregunta honesta. Respuesta: Prolog tiene el *mejor modelo de ejecución* para una clase de problemas (búsqueda con restricciones, análisis de grafos, parsing con DCGs) y *un modelo muy pobre* para cualquier otra cosa. Los frameworks modernos (ASP, Datalog, miniKanren en Scheme) heredan partes de la WAM sin adoptar Prolog entero.
9. **Cierre**: la unificación como primitiva lingüística sigue sub-explotada. Miren Datalog (usado en Rust's polonius borrow checker), miren miniKanren, miren Souffle. Son todos descendientes del wambook.

**Bibliografía:**
- [Hassan Aït-Kaci, *Warren's Abstract Machine: A Tutorial Reconstruction*, MIT Press 1991](https://direct.mit.edu/books/book/2275/Warren-s-Abstract-MachineA-Tutorial-Reconstruction) — libro de referencia, hoy libre (el fork `wambook` lo tiene en PostScript).
- [David H D Warren, *An Abstract Prolog Instruction Set*, SRI Technical Note 309, 1983](https://www.sri.com/publication/computer-science/an-abstract-prolog-instruction-set/) — el paper original de Warren.
- [Peter Van Roy, *1983-1993: The Wonder Years of Sequential Prolog Implementation*, JLP 1994](https://www.info.ucl.ac.be/~pvr/jlp.html) — panorama histórico de las implementaciones.
- [Henri de Feraudy, *small-prolog* archive en Walnut Creek CDROM](https://www.cdrom.com/titles/linux/) — el source original de referencia.
- [Logic Programming Associates, *micro-PROLOG for the ZX Spectrum*](https://spectrumcomputing.co.uk/entry/23358/ZX-Spectrum/micro-PROLOG) — contexto histórico del intérprete para Spectrum.
- [Kevin Buzzard et al, *SWI-Prolog* — sitio oficial](https://www.swi-prolog.org/) — el intérprete moderno que vale la pena comparar.
- [J Wielemaker et al, *SWI-Prolog*, TPLP 2012](https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/swiprolog/13570311D10C2F20A29F0BE4DF5C03D1) — paper del intérprete de referencia moderno.
- [William Byrd, *miniKanren*](http://minikanren.org/) — el heredero Scheme de la unificación.
- [Peter Norvig, *Paradigms of Artificial Intelligence Programming*, Morgan Kaufmann 1991, capítulos sobre Prolog](https://github.com/norvig/paip-lisp) — implementa Prolog en Lisp, otro ángulo pedagógico.
- [SWI-Prolog manual — WAM overview](https://www.swi-prolog.org/pldoc/man?section=overview) — referencia moderna.

**Imágenes:**
- _Crear_: diagrama de los 3 escalones (micro-PROLOG → small-prolog → WAM) con una misma query (`append([1,2], [3,4], X)`) ejecutada en cada uno (~1 hora — central del post).
- _Crear_: tabla de los 30 opcodes de la WAM agrupados en 4 familias (~45 min).
- _Crear_: diagrama del flujo de unificación con trail y choice points (~30 min).
- _Crear_: scan/screenshot del manual original de micro-PROLOG T1.0 (~15 min de buscar).

**Tags propuestos:** `['Prolog', 'WAM', 'Warren Abstract Machine', 'unification', 'micro-PROLOG', 'Spectrum', 'small-prolog', 'compiladores', 'deep dive']`

**Estado actual:** tres repos forkeados con material listo (`wambook`, `small-prolog-walnut-creek-original`, `micro-PROLOG`). El post es un deep dive que requiere leer los tres en orden y escribir la narrativa que los hila. Sesión de redacción estimada: 2-3 tardes.

