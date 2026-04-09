### E-06 — Uso Ollama para criticar mi código antes de commitearlo

- **Archivo seed:** `dev/draft-uso-ollama-para-criticar-mi-codigo.md`
- **Slug propuesto:** `ollama-revisa-mi-codigo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-ollama-revisa-mi-codigo/index.md`
- **Serie:** E
- **Cross-links:** lleva a [[E-04]] (Python env, donde se integra el hook), [[C-04]] (TDD: el ciclo similar), [[G-06]] (LLM en el pipeline de despliegue)
- **Idioma:** es
- **Madurez:** bare-seed (archivo vacío)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** corro Ollama localmente con un modelo mediano (probablemente Qwen2.5-Coder-14B o Llama 3.3 según fecha) y tengo un hook de pre-commit que le pasa el diff y le pide *que critique*, no *que apruebe*. La diferencia de prompt es enorme. El post explica el setup, el prompt, los falsos positivos, y por qué un LLM local es la solución correcta a este problema (no Copilot, no Claude API, no GitHub Actions con un modelo en la nube).

**Hook:** "tengo un pre-commit hook que le pasa mi diff a un modelo que corre en mi laptop y le pide que lo critique. No es Copilot. No es Claude. No es Cursor. Es un Ollama local con un prompt de 8 líneas, y atrapa más bugs por dólar que cualquier otra cosa que probé."

**Outline:**
1. El problema: el code review honesto es valioso pero caro en atención. ¿Y si tuviera un revisor que mira *cada commit* sin cansarse?
2. Por qué un LLM local y no la API: privacidad del código, latencia, costo cero por commit, offline.
3. El stack: Ollama + un modelo coder + un script Python de 50 líneas + integración pre-commit.
4. El prompt — texto completo. Lo importante: *"sé crítico, no aprobador. Si todo te parece bien, sospechá."*
5. Los modelos que probé en orden cronológico, con observaciones honestas (Qwen2.5-Coder, DeepSeek-Coder, Llama 3.3, qué tal Code Llama).
6. Los falsos positivos: cuando el LLM se inventa problemas. Cómo decidir cuándo escucharlo.
7. Lo que no resuelve: arquitectura, intención de negocio, refactors grandes. El revisor humano sigue siendo necesario para esos.
8. Cierre: por qué este patrón ("LLM local + prompt crítico + integración silenciosa") es probablemente el futuro de la programación asistida, mucho más que Cursor.

**Bibliografía:**
- [Ollama — sitio oficial](https://ollama.com/).
- [Ollama en GitHub](https://github.com/ollama/ollama).
- [Qwen2.5-Coder en HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) — verificar fecha y tamaño en el momento de publicar.
- [DeepSeek-Coder en GitHub](https://github.com/deepseek-ai/DeepSeek-Coder).
- [Simon Willison, *Run Llama 3.1 locally with Ollama*, 2024](https://simonwillison.net/2024/Jul/23/run-llama-3-locally/) — modelo del estilo de post.
- [pre-commit framework](https://pre-commit.com/) — para el lado integración.
- [Anthropic, *Prompting best practices*](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — útil aunque uses modelos abiertos.

**Imágenes:**
- _Crear_: screenshot del pre-commit hook corriendo, con la salida del LLM en consola (~20 min).
- _Crear_: diagrama del flujo: `git commit` → `pre-commit` → `script` → `ollama` → `output` → `decisión` (~30 min).

**Tags propuestos:** `['Ollama', 'LLM', 'code review', 'pre-commit', 'memoir', 'devenv']`

**Estado actual:** archivo vacío; el setup existe en mi máquina actualmente, hay que sentarse a sistematizarlo.

