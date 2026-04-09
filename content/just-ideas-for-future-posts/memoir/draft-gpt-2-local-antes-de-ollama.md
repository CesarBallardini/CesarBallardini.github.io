### E-13 — El día que bajé GPT-2 de OpenAI antes de que fuera famoso

- **Archivo seed:** `github.com/CesarBallardini/gpt-2` (fork de 2021 del repo de OpenAI para el paper *Language Models are Unsupervised Multitask Learners*)
- **Slug propuesto:** `gpt-2-local-antes-de-ollama`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-gpt-2-local-antes-de-ollama/index.md`
- **Serie:** E — memoir técnico sobre mi trayectoria con LLMs locales
- **Cross-links:** lleva a [[E-06]] (Ollama para criticar código — el sucesor moderno), [[J-03]] (Mentifex/MindForth — el otro "IA del hombre solitario"), [[E-08]] (libros que me marcaron — contraste con la generación LLM actual)
- **Idioma:** es
- **Madurez:** fork del repo de OpenAI, con experimentos locales de mi parte
- **Length target:** medium (1500-2000 palabras)

**Concepto:** en 2019 OpenAI publicó el paper *Language Models are Unsupervised Multitask Learners* y liberó GPT-2 — primero el modelo chico (124M parámetros), luego el más grande (1.5B) meses después. Bajé el repo, lo corrí en mi máquina con CPU, generé texto incoherente pero sorprendente, y lo dejé reposar. En 2022 llegó ChatGPT y el mundo descubrió que los LLMs existían. El post es el memoir honesto de esa experiencia pre-hype: qué hacía GPT-2, qué no hacía, cómo se sentía correrlo localmente antes de que la conversación pública estuviera contaminada por expectativas infladas y por vendedores de cursos.

**Hook:** "en 2019 bajé GPT-2 de OpenAI, lo corrí en mi máquina y generé dos párrafos sobre unicornios que hablaban español. El texto era casi coherente pero no del todo. Cerré la terminal pensando: 'interesante juguete, pobre'. Tres años después salió ChatGPT y la gente decía que la IA había llegado. La había visto venir y no me había dado cuenta. El post es la historia de esa ceguera — y lo que se aprende de correr un LLM antes de saber que va a cambiar el mundo."

**Outline:**
1. Contexto 2019: qué era OpenAI, por qué GPT-2 era notable, el debate sobre liberar el modelo grande (OpenAI inicialmente no lo hizo, por miedo a "usos maliciosos" que hoy parecen cuarta).
2. La instalación: clonar el repo, bajar los pesos (124M era factible en laptop), TensorFlow 1.x, Python 3.6, las dependencias peleonas.
3. Los primeros prompts: generación de texto a partir de prompts cortos. Qué funcionaba, qué no. El famoso ejemplo de los unicornios andinos.
4. La *vibe* de 2019-2021: los LLMs eran curiosidad académica. No había ecosistema, no había aplicaciones, no había quejas sobre "alucinaciones". Era puro experimento.
5. Lo que pasé por alto: la curva de capacidad con escala. GPT-2 era rudimentario; GPT-3 fue cualitativamente distinto; GPT-4 otra vez; Claude 3 otra vez. No había razón para predecir esa progresión, pero había señales.
6. El contraste con 2026 ([[E-06]] Ollama): hoy corro un modelo de 14B localmente y critica mi código. Entre medio pasaron 7 años, 6 generaciones de modelos y un cambio cultural entero. Pero el *ritual* de bajar un modelo, correrlo offline y generar texto es idéntico.
7. La lección: cuando una tecnología es "mitad cool, mitad pavada", ese es el momento de prestarle atención. No cuando ya todo el mundo habla de ella.
8. Cierre: el repo sigue ahí. GPT-2 sigue funcionando. Podés correrlo hoy y entender qué era lo que había en ese mundo antes del hype.

**Bibliografía:**
- [Alec Radford et al, *Language Models are Unsupervised Multitask Learners*, OpenAI 2019](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) — el paper.
- [OpenAI blog — *Better Language Models and Their Implications*, 14 feb 2019](https://openai.com/blog/better-language-models/) — el anuncio original.
- [OpenAI blog — *GPT-2 1.5B Release*, 5 nov 2019](https://openai.com/blog/gpt-2-1-5b-release/) — la liberación del modelo grande.
- [github.com/openai/gpt-2](https://github.com/openai/gpt-2) — el repo original (fork en mi cuenta).
- [Gwern Branwen, *GPT-2 Neural Network Poetry*, 2019](https://gwern.net/gpt-2) — el análisis canónico de las capacidades de GPT-2 hecho por un outsider.
- [Andrej Karpathy, *Let's build GPT: from scratch, in code, spelled out*, YouTube 2023](https://www.youtube.com/watch?v=kCc8FmEb1nY) — la explicación moderna, retrospectiva.
- [Ilya Sutskever et al — historia de OpenAI](https://openai.com/about/) — contexto institucional.
- [Simon Willison, *My AI/LLM predictions for the next 1, 3 and 6 years*, 2023](https://simonwillison.net/2023/May/27/my-ai-llm-predictions/) — contraste con "predicciones honestas de alguien que sí estaba mirando".

**Imágenes:**
- _Crear_: screenshot de una sesión de GPT-2 generando texto en 2019 (recreación — el repo sigue corriendo) (~30 min).
- _Crear_: línea de tiempo LLMs 2018-2026 (GPT-2 → GPT-3 → ChatGPT → GPT-4 → Llama → Claude → locales modernos) (~1 hora).
- _Crear_: meme honesto "lo que yo veía vs lo que era" (~15 min).

**Tags propuestos:** `['GPT-2', 'OpenAI', 'LLM', 'memoir', 'TensorFlow', 'IA', 'pre-hype']`

**Estado actual:** fork de 2021 en mi GitHub, repo de OpenAI funcional, material técnico y narrativo listo. Post fácil — una tarde de redacción.

