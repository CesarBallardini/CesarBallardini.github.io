### D-03 — La máquina de Turing: una pizarra infinita y un cabezal terco

- **Archivo seed:** `dev/draft-maquina-de-turing.md`
- **Slug propuesto:** `maquina-de-turing-explicacion`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-maquina-de-turing-explicacion/index.md`
- **Serie:** D
- **Cross-links:** lleva a [[B-06]] (teoría imperativa), [[D-02]] (Sketchpad — el otro extremo: lo concreto), [[A1-04]] (Forth — máquinas mínimas)
- **Idioma:** es
- **Madurez:** bare-seed (archivo vacío)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** la "máquina de Turing" no es una máquina. Es un argumento matemático escrito por Alan Turing en 1936 para resolver un problema completamente abstracto (el *Entscheidungsproblem* de Hilbert), y resulta que ese argumento — una cinta infinita, un cabezal, un puñado de reglas — define lo que significa "computar". El post explica la máquina sin matemática, muestra por qué define los límites de lo posible, y por qué Turing nunca quiso que se la confundiera con una computadora real.

**Hook:** "en 1936 un estudiante de doctorado de 24 años publica un paper para responder una pregunta de Hilbert sobre lógica formal. En ese paper inventa, casi como herramienta secundaria, una *máquina imaginaria* con una cinta infinita y un cabezal. No quiere construirla. Sólo necesita que se le pueda razonar sobre ella. Diez años después, esa máquina es el modelo del que sale toda la computación."

**Outline:**
1. El contexto: el problema de la decisión de Hilbert (1928). ¿Existe un procedimiento mecánico que decida si un enunciado matemático es demostrable?
2. Quién era Turing en 1936 — estudiante en Cambridge, 24 años, Church en Princeton trabajando en lo mismo (lambda cálculo) en paralelo.
3. La construcción: cinta, alfabeto, estados, función de transición. Sin matemática, con dibujitos.
4. Qué prueba Turing:
   - existe una máquina universal que puede simular cualquier otra máquina (la idea del *programa-como-dato*).
   - el problema de la parada es indecidible — y eso responde negativamente a Hilbert.
5. La pregunta tonta pero importante: si la máquina es imaginaria, ¿por qué nuestras computadoras "son" máquinas de Turing? Respuesta honesta: no lo son exactamente; son aproximaciones con memoria finita. La equivalencia es teórica, no física.
6. La tesis de Church-Turing y por qué después de 90 años no hay candidato serio que la rompa.
7. Cierre: la diferencia entre Turing inventando un modelo formal y los ingleses de Bletchley construyendo Colossus en 1943. No son la misma cosa, y Turing trabajó en ambas, y eso confunde a todo el mundo.

**Bibliografía:**
- [Alan Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society 1936](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf) — el paper original.
- [Andrew Hodges, *Alan Turing: The Enigma*, Princeton University Press 1983](https://archive.org/details/alanturingenigma0000hodg) — la biografía canónica.
- [Charles Petzold, *The Annotated Turing*, Wiley 2008](https://www.charlespetzold.com/AnnotatedTuring/) — el libro que explica el paper línea por línea.
- [Martin Davis, *The Universal Computer: The Road from Leibniz to Turing*, W.W. Norton 2000](https://archive.org/details/universalcompute0000davi).
- [Stanford Encyclopedia of Philosophy — Turing Machines](https://plato.stanford.edu/entries/turing-machine/).
- [Wikipedia — Turing machine](https://en.wikipedia.org/wiki/Turing_machine).
- [The Alan Turing Internet Scrapbook](https://www.turing.org.uk/scrapbook/) — Hodges mantiene el sitio.
- [Church-Turing Thesis en SEP](https://plato.stanford.edu/entries/church-turing/).

**Imágenes:**
- _Wikimedia_: foto de Turing — [Alan Turing aged 16](https://commons.wikimedia.org/wiki/File:Alan_Turing_Aged_16.jpg) — license: public domain.
- _Wikimedia_: diagrama esquemático de una máquina de Turing — varios disponibles bajo CC.
- _Crear_: SVG simple de una máquina de Turing reconociendo `01010` como número par de unos (~45 min).
- _Crear_: comparación side-by-side de la cinta de Turing y la memoria RAM de una computadora moderna (~30 min).

**Tags propuestos:** `['Alan Turing', 'computabilidad', 'Hilbert', 'historia', 'fundamentos']`

**Estado actual:** archivo vacío, sólo título.

