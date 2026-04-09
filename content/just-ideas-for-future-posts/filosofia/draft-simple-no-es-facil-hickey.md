### C-02 — Simple no es lo mismo que fácil (Rich Hickey)

- **Archivo seed:** `dev/draft-simple-o-facil.md`
- **Slug propuesto:** `simple-no-es-facil-hickey`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-simple-no-es-facil-hickey/index.md`
- **Serie:** C
- **Cross-links:** depende de [[tr-07]]; lleva a [[C-03]] (Tidy First, otro framework para hablar de cambio), [[A2-04]] (Clojure y la práctica de Hickey), [[B-02]] (Okasaki — estructuras simples pero no fáciles)
- **Idioma:** es
- **Madurez:** bare-seed (sólo el título y "rick hickey")
- **Length target:** medium (1500-2000 palabras)

**Concepto:** la charla *Simple Made Easy* de Rich Hickey (Strange Loop 2011) es uno de esos textos que cambia el vocabulario con el que pensás tu trabajo. La distinción entre *simple* (sin entrelazar, sin nudos: una propiedad objetiva del diseño) y *easy* (cerca de tu mano, conocido, instalable con un comando: una propiedad subjetiva del usuario) explica por qué todo el tiempo elegimos lo "fácil" y luego pagamos en complejidad.

**Hook:** "Rich Hickey, el creador de Clojure, dio una charla en 2011 que vino a romper el vocabulario con el que hablábamos de software. Después de esa charla ya no podés decir 'esta solución es simple' sin que te corrija una vocecita interna: querés decir *fácil*. Hay una diferencia, y la diferencia importa."

**Outline:**
1. La etimología que abre la charla: *simple* viene de *simplex* (un pliegue), su opuesto es *complex* (varios pliegues entrelazados). *Easy* viene de *adjacens* — cerca de vos.
2. Por qué la confusión es sistemática: los vendedores de herramientas optimizan para easy (tutorial de 5 minutos), pero el costo de simple se paga después.
3. La lista de Hickey de cosas "simples" vs "complejas":
   - state vs values
   - methods vs functions
   - vars vs managed refs
   - inheritance, switch, matching vs polymorphism
   - syntax vs data
   - imperative loops, fold vs set functions
   - actors vs queues
   - ORM vs declarative data manipulation
   - conditionals vs rules
4. La tesis fuerte: *no podés construir cosas confiables a partir de partes complejas*. Reliability requires understanding requires simplicity.
5. La crítica que se le hace a Hickey y por qué la critica falla: "simple es subjetivo también" — no, es estructural; podés contar los entrelazamientos.
6. Aplicaciones prácticas: cómo usar este vocabulario en code review y en arquitectura. Ejemplo concreto con un caso de mi experiencia.
7. Cierre: el costo de elegir easy todo el tiempo es la deuda de complejidad que después no podés pagar.

**Bibliografía:**
- [[tr-07]] — Rich Hickey, *Simple Made Easy*, Strange Loop 2011.
- [Rich Hickey, *Hammock Driven Development*, Clojure Conj 2010](https://www.youtube.com/watch?v=f84n5oFoZBc) — la charla compañera, sobre el modo de pensar.
- [Rich Hickey, *The Value of Values*, JaxConf 2012](https://www.youtube.com/watch?v=-6BsiVyC1kM).
- [Stuart Halloway, *Narcissistic Design*, Clojure/conj 2015](https://www.youtube.com/watch?v=LEZv-kQUSi4) — extiende el argumento de Hickey con humor.
- [Fred Brooks, *No Silver Bullet — Essence and Accident in Software Engineering*, IEEE Computer 1987](https://www.cs.unc.edu/techreports/86-020.pdf) — antecedente directo: complejidad esencial vs accidental.
- [Out of the Tar Pit — Ben Moseley & Peter Marks, 2006](https://curtclifton.net/papers/MoseleyMarks06a.pdf) — el otro texto canónico sobre complejidad.
- [Transcripción oficial de la charla en GitHub matthiasn](https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md) — para citar literal.

**Imágenes:**
- _Crear_: tabla SVG con dos columnas — *simple* a la izquierda, *easy* a la derecha — replicando la lista de Hickey con íconos (~1 hora).
- _Crear_: diagrama del "tejido" — un nudo de cuerdas entrelazadas (complex) vs cuerdas paralelas (simple) (~30 min).
- _Crear_: opcional, screenshot del slide "what's simple?" de la charla original (verificar uso justo / fair use).

**Tags propuestos:** `['Rich Hickey', 'Clojure', 'simple', 'complejidad', 'arquitectura']`

**Estado actual:** sólo título y dos palabras en el seed.

