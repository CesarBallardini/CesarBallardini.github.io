### C-04 — TDD bass drop: cuando el test rojo te da dopamina

- **Archivo seed:** `dev/tdd-bass-drop-snl.md`
- **Slug propuesto:** `tdd-bass-drop-dopamina`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-tdd-bass-drop-dopamina/index.md`
- **Serie:** C
- **Cross-links:** depende de [[tr-08]] (Beck, TDD by Example); lleva a [[C-03]] (Tidy First, mismo autor), [[E-06]] (memoir: cómo enseñé TDD en clase 2020 de Paradigmas)
- **Idioma:** es
- **Madurez:** bare-seed (3 palabras: SNL, dopamina, paradigmas 2020)
- **Length target:** short (800-1200 palabras)

**Concepto:** TDD no se vende bien explicando "calidad" o "regresión". Se vende contando que el ciclo *red → green → refactor* es un loop de recompensa pequeño y constante, como un bass drop en una canción de Saturday Night Live: cada test que pasa es una micro-descarga de dopamina. El que practica TDD no lo hace por disciplina; lo hace porque se siente bien.

**Hook:** "TDD se enseña como si fuera medicina: amargo pero te hace bien. Está mal vendido. TDD se siente como un sketch de Saturday Night Live con bass drops cada 30 segundos. Te das cuenta cuando lo practicás dos semanas y empezás a *querer* escribir el test antes que el código, no porque sos disciplinado, sino porque querés el bajo."

**Outline:**
1. El sketch de SNL del bass drop (tengo que verificar exactamente cuál es — anotación para mí mismo).
2. La analogía: red bar / green bar / commit. Cada green es un bass drop pequeño.
3. La explicación neurológica honesta — el ciclo de recompensa variable de Skinner y Csíkszentmihályi (flow). Sin pretensión de ser psicólogo.
4. Por qué esto explica la diferencia entre quien probó TDD y dejó vs quien lo adoptó: los primeros no completaron el ciclo lo suficiente como para que el cerebro lo registre como recompensa.
5. Anécdota de la clase de Paradigmas 2020 — qué pasó cuando los alumnos vieron una sesión de TDD live coding por primera vez.
6. Cierre: el truco para "engancharte" — empezá con un bug que ya tenés, escribí el test que lo reproduce, mirá la barra roja, arreglalo, mirá la barra verde. Eso es todo.

**Bibliografía:**
- [[tr-08]] — Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley 2002 (para los fundamentos).
- [Kent Beck, James Grenning, Robert Martin et al, *Agile Manifesto*](https://agilemanifesto.org/) — contexto histórico.
- [Robert C. Martin, *The Three Laws of TDD*](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html) — la formulación más estricta.
- [Mihály Csíkszentmihályi, *Flow: The Psychology of Optimal Experience*, 1990](https://archive.org/details/flowpsychologyof00csik) — la base teórica del estado de flujo.
- [Saturday Night Live — sketches con "bass drop"](https://www.youtube.com/results?search_query=snl+bass+drop) — verificar cuál exactamente; probable referencia: *When Will the Bass Drop?* (2014, con Andy Samberg). [Vídeo](https://www.youtube.com/watch?v=BACGAfZqDBo).
- [Martin Fowler, *Is TDD Dead?* — series con DHH y Kent Beck, 2014](https://martinfowler.com/articles/is-tdd-dead/) — la otra cara del debate.
- [DHH, *TDD is dead. Long live testing.*, 2014](https://dhh.dk/2014/tdd-is-dead-long-live-testing.html) — la opinión disidente.

**Imágenes:**
- _Crear_: GIF animado / SVG del ciclo red→green→refactor con ondas de sonido tipo bass drop (~1 hora — el chiste visual del post).
- _Embed_: vídeo del sketch de SNL (verificar derechos / usar embed oficial de YouTube).

**Tags propuestos:** `['TDD', 'Kent Beck', 'flow', 'dopamina', 'red green refactor']`

**Estado actual:** sólo tres palabras en el seed; nota personal: revisar el material de la clase de Paradigmas 2020 antes de escribir.

