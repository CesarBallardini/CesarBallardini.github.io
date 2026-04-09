### E-16 — Tres forks de IA de antes de los LLMs: simpleai, ai-app-prog, HealthyCoderApp

- **Archivo seed:** `github.com/CesarBallardini/simpleai` (fork, Python AI utilities) + `github.com/CesarBallardini/ai-app-prog` (fork, AI application programming) + `github.com/CesarBallardini/HealthyCoderApp` (fork, Java — contexto incierto)
- **Slug propuesto:** `tres-forks-ia-pre-llm`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-tres-forks-ia-pre-llm/index.md`
- **Serie:** E — memoir arqueológico sobre qué era estudiar IA antes de 2022
- **Cross-links:** depende de [[E-13]] (gpt-2 — el punto de quiebre); lleva a [[J-03]] (MindForth — otro ángulo solitario), [[A2-04]] (sistemas expertos en BASIC — el pasado lejano)
- **Idioma:** es
- **Madurez:** **incompletos** — tres forks del tipo "lo cloné para leerlo, nunca lo terminé"
- **Length target:** short (800-1200 palabras)

**Concepto:** antes de 2022 y el boom de los LLMs, estudiar "IA" significaba algo muy distinto — algoritmos de búsqueda, redes neuronales clásicas, sistemas expertos, reinforcement learning tabular. Tengo tres forks en mi GitHub de ese período: *simpleai* (utilidades Python de IA clásica, tipo A*, minimax, genetic algorithms), *ai-app-prog* (repo educativo viejo), *HealthyCoderApp* (uno Java que no recuerdo bien por qué clonéé). El post es una breve arqueología de los tres, honesta sobre la tensión "esto que estudié sigue vigente" vs "esto quedó aplastado por los LLMs".

**Hook:** "tengo en mi GitHub tres forks de repos de IA que cloné entre 2014 y 2019. Ninguno terminó siendo un proyecto. Los cloné porque en ese momento 'IA' significaba *estudiar algoritmos de búsqueda en el libro de Russell & Norvig*, no *correr modelos de 14B parámetros*. El post es la arqueología honesta de tres forks que marcaron una época — y la pregunta: ¿lo que aprendí sigue siendo útil en la era GPT?"

**Outline:**
1. **simpleai** — una biblioteca Python con A*, minimax, iterative deepening, simulated annealing, genetic algorithms. El tipo de código que implementabas a mano para un curso universitario o un challenge.
2. **ai-app-prog** — un repo educativo viejo (verificar contexto, mi fork no tiene muchas pistas).
3. **HealthyCoderApp** — Java, fork 2019, contexto incierto (puede ser un repo de ejemplo de algún curso o tutorial).
4. La pregunta estructural: en 2026, ¿cuánto de la IA clásica sigue siendo útil? Respuesta honesta: muchísimo — los LLMs son grandes pattern matchers, pero *encastrarlos* en aplicaciones reales requiere A\*, planning, search y constraint solving. La IA clásica vive dentro del LLM, como andamiaje.
5. Cierre: el consejo para alguien que hoy quiere "aprender IA". Russell & Norvig *primero*, LLM *después*. Los LLMs son más fáciles de usar cuando entendés qué problema no están resolviendo.

**Bibliografía:**
- [Stuart Russell & Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed Pearson 2020](https://aima.cs.berkeley.edu/) — la biblia.
- [Peter Norvig, *Paradigms of AI Programming*, Morgan Kaufmann 1991](https://github.com/norvig/paip-lisp) — IA clásica en Lisp, ya libre en GitHub.
- [simpleai en github](https://github.com/simpleai-team/simpleai) — el repo original.

**Imágenes:**
- _Crear_: tabla "algoritmo clásico / dónde vive hoy" (A\* en map routing, minimax en AlphaZero, backtracking en SAT solvers) (~30 min).

**Tags propuestos:** `['IA clasica', 'simpleai', 'Russell Norvig', 'A star', 'memoir', 'pre-LLM']`

**Estado actual:** **tres forks incompletos** — marcados como tal. El post es honesto sobre que los tres son "clonelos que nunca fueron proyecto". Si el post nunca se escribe, no se pierde nada. Si se escribe, es un memoir corto con valor arqueológico.

