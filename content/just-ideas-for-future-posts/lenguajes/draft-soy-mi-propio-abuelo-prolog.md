### A1-10 — "Soy mi propio abuelo": modelar una humorada folklórica en Prolog

- **Archivo seed (repo POC):** [github.com/CesarBallardini/prolog-me-case-con-una-viuda](https://github.com/CesarBallardini/prolog-me-case-con-una-viuda) — Prolog, 1 star, último push 2021-07-22
- **Slug propuesto:** `soy-mi-propio-abuelo-prolog`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-soy-mi-propio-abuelo-prolog/index.md`
- **Serie:** A1 — cruza con [[I-03]] (cultura local hispanohablante, el chiste circulaba en castellano) y con un eventual post sobre Prolog
- **Cross-links:** lleva a [[A1-08]] (KL1, otro descendiente lógico), [[A1-11]] (Pharo: otro lenguaje "explorás el mundo desde adentro"), [[I-03]] (Spectrum/MicroHobby donde aparecía Prolog también)
- **Idioma:** es
- **Madurez:** **complete-poc** — 10 tests `plunit` pasando, Travis CI configurado
- **Length target:** short (800-1200 palabras) — el post divertido por excelencia

**Concepto:** existe una humorada folklórica española/hispanoamericana muy vieja: un hombre se casa con una viuda con hija; su padre se casa con esa hija; cierre del razonamiento — *"resulta que soy mi propio abuelo"*. El chiste necesita que el oyente siga una cadena de relaciones de parentesco. Y resulta que el Prolog es *el* lenguaje natural para modelar exactamente eso: declarás los hechos (`padre/2`, `casado_con/2`), las reglas (`abuelo/2`), y el motor de inferencia se encarga del resto. El post toma la humorada, la modela en SWI-Prolog en 50 líneas, y muestra cómo `plunit` puede confirmar que efectivamente se cumple "soy mi propio abuelo".

**Hook:** "hay una humorada folklórica que circulaba en español hace décadas: un hombre se casa con una viuda que tiene una hija, el padre del hombre se casa con esa hija, y al final, después de seguir la cadena, *resulta que él es su propio abuelo*. Si nunca te lo contaron, googlealo. Si te lo contaron, te frustró. Te traigo la solución: lo modelamos en Prolog, los tests se ejecutan y nos dicen quién es abuelo de quién. Cinco minutos de Prolog, una hora de risa."

**Outline:**
1. El chiste, contado bien — la versión folklórica completa en castellano.
2. Por qué Prolog es el lenguaje natural para esto: hechos + reglas = inferencia.
3. La modelización paso a paso:
   - los predicados base: `padre/2`, `madre/2`, `casado_con/2`.
   - las reglas: `abuelo(X,Y) :- padre(X,Z), padre(Z,Y).` (con todos los casos: padre del padre, padre de la madre, etc.).
4. La query mágica: `?- abuelo(yo, yo).` y la respuesta: `true.`.
5. El test con `plunit`: cómo escribir un test que afirme la conclusión y por qué eso es valor agregado para no perderse en el árbol genealógico mental.
6. Cierre: por qué este es el "hello world" perfecto de Prolog para alguien hispanohablante.

**Bibliografía:**
- Repo del POC: [CesarBallardini/prolog-me-case-con-una-viuda](https://github.com/CesarBallardini/prolog-me-case-con-una-viuda).
- [SWI-Prolog — sitio oficial](https://www.swi-prolog.org/).
- [SWI-Prolog `plunit` — testing framework](https://www.swi-prolog.org/pldoc/doc_for?object=section%28%27packages/plunit.html%27%29).
- [Ivan Bratko, *Prolog Programming for Artificial Intelligence*, 4th ed Pearson 2011](https://www.pearson.com/) — la referencia canónica para Prolog.
- [William F Clocksin & Christopher S Mellish, *Programming in Prolog*, 5th ed Springer 2003](https://link.springer.com/book/10.1007/978-3-642-55481-0) — el otro clásico.
- [Wikipedia — *I'm My Own Grandpa*](https://en.wikipedia.org/wiki/I%27m_My_Own_Grandpa) — la canción country de 1947 con la misma estructura lógica, prueba que el chiste no es sólo hispanoamericano.
- Cross-link a [[A1-08]] para la familia lógica.

**Imágenes:**
- _Crear_: árbol genealógico SVG mostrando cómo se cierra el ciclo "soy mi propio abuelo" (~45 min — la imagen central del post).
- _Crear_: snippet del Prolog en una caja (~10 min).
- _Crear_: screenshot del `plunit` corriendo con los 10 tests verdes (~10 min).

**Tags propuestos:** `['Prolog', 'SWI Prolog', 'humor', 'familia', 'logica', 'plunit', 'folklore']`

**Estado actual:** **POC completo, 10 tests pasando**. Es el post más fácil y divertido de toda la grilla — se puede sentar a escribir y publicar en una sola sesión.

