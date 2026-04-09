### C-03 — Tidy First: limpiar antes de cambiar (Kent Beck)

- **Archivo seed:** `dev/draft-tidy-first.md`
- **Slug propuesto:** `tidy-first-kent-beck`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-tidy-first-kent-beck/index.md`
- **Serie:** C
- **Cross-links:** depende de [[tr-08]]; lleva a [[C-04]] (TDD, otro framework de Beck), [[C-02]] (Hickey, vocabulario complementario), [[E-04]] (memoir: cuándo aprendí a hacer tidy en mi propio código)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** medium (1200-1800 palabras)

**Concepto:** Kent Beck, en *Tidy First?* (2023), propone una distinción operativa entre *tidyings* (limpiezas pequeñas: renombrar, extraer, reordenar) y *behavior changes* (cambios que un usuario notaría). La tesis: separá los dos en commits/PRs distintos, y aprendé a decidir si conviene tidy *antes* de cambiar, *después*, o *nunca*. No es un manual de refactoring — es un libro sobre decisiones económicas y emocionales en el código.

**Hook:** "Kent Beck — el del XP, el del TDD — escribió en 2023 un librito de 100 páginas que se titula *Tidy First?*, con signo de pregunta. Ese signo de pregunta es importante. Beck no te está diciendo *limpiá siempre antes*. Te está diciendo: *aprendé a decidir cuándo*."

**Outline:**
1. Qué es un *tidying* y por qué Beck inventa el término en vez de decir "refactor pequeño".
2. La lista de tidyings del libro: *guard clauses*, *dead code*, *normalize symmetries*, *new interface old implementation*, *reading order*, *cohesion order*, *move declaration and initialization together*, *explaining variables*, *explaining constants*, *explicit parameters*, *chunk statements*, *extract helper*, *one pile*, *explaining comments*, *delete redundant comments*. Quince en total. Comentar 4-5.
3. La pregunta del título: *tidy first?* o *tidy after?* o *never tidy?* — el framework de decisión.
4. La parte económica: cost of money, options, discounting. Beck entra en finanzas reales para defender su posición — esto sorprende a todo el mundo y es lo más interesante del libro.
5. La parte humana: separación tidy/behavior baja la carga cognitiva del review y la fricción del PR.
6. Cierre: por qué este libro se siente como "lo que XP siempre quiso decir y nunca terminó de articular".

**Bibliografía:**
- [[tr-08]] — Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*, O'Reilly 2023.
- [Kent Beck, newsletter *Software Design: Tidy First?*](https://tidyfirst.substack.com/) — donde gran parte del material apareció primero.
- [Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley 2002](https://www.oreilly.com/library/view/test-driven-development/0321146530/) — el texto previo.
- [Kent Beck, *Extreme Programming Explained*, 2.ª ed. 2004](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/).
- [Martin Fowler, *Refactoring*, 2.ª ed. 2018](https://martinfowler.com/books/refactoring.html) — la referencia que Beck asume conocida.
- [Ron Jeffries, *Adventures in C#*](https://ronjeffries.com/) — para ver tidyings aplicados en serie por otro de los firmantes del manifiesto ágil.
- [Kent Beck, *3X: Explore/Expand/Extract*, Facebook 2016](https://www.facebook.com/notes/kent-beck/the-product-development-triathlon/1215075478525314/) — backup en Wayback recomendado.

**Imágenes:**
- _Crear_: diagrama de un PR "mezclado" (tidy + behavior) vs dos PRs separados — mostrar la diferencia visual en review (~30 min).
- _Crear_: árbol de decisión "tidy first / after / never" según costo y certidumbre (~45 min).

**Tags propuestos:** `['Kent Beck', 'tidy first', 'refactor', 'XP', 'code review']`

**Estado actual:** sólo título y dos palabras ("kent beck", "tidy first") en el seed.

