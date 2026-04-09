### E-04 — Mi entorno de Python en 2026: ruff, pre-commit, pyproject

- **Archivo seed:** `dev/draft-python-dev-environment.md`
- **Slug propuesto:** `entorno-python-2026`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-entorno-python-2026/index.md`
- **Serie:** E
- **Cross-links:** lleva a [[E-05]] (Vue env), [[E-06]] (Ollama para code review), [[G-04]] (Ansible: lint y pre-commit en infra)
- **Idioma:** es
- **Madurez:** seed-with-hints (4 herramientas listadas)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** después de 30 años escribiendo Python on/off, en 2026 mi entorno se reduce a 4 piezas: `ruff` (linter + formatter), `pre-commit` (hooks), `pyproject.toml` (configuración única) y VSCode (editor con LSP). Sin `black`, sin `isort`, sin `flake8`, sin `mypy daemon` corriendo en otro proceso. El post es la justificación de cada elección y por qué tirar piezas mejora la productividad.

**Hook:** "en 2018 mi virtualenv de Python tenía black, isort, flake8, mypy, pylint, autoflake, bandit y un pre-commit que tardaba 25 segundos en correr. En 2026 tengo ruff y pre-commit y la cosa tarda 1.5 segundos. No es que ruff sea más rápido — es que la mayoría de esas herramientas se volvieron innecesarias el día que ruff existió."

**Outline:**
1. El stack que usaba en 2018-2022 y por qué cada pieza estaba ahí.
2. La aparición de ruff (Astral, 2022) y por qué reemplazó cinco herramientas a la vez. La diferencia de performance no es la parte importante — la parte importante es que es *una sola configuración*.
3. `pyproject.toml` como single source of truth — el final de los `setup.cfg`, `tox.ini`, `pylintrc`, `mypy.ini`, `.flake8`. Mostrar el archivo real.
4. `pre-commit` como cinturón de seguridad — qué hooks corro, en qué orden, qué pasa si fallan.
5. VSCode + el LSP de ruff. Por qué saqué Pylance del medio (o no, depende del proyecto).
6. Lo que NO uso y por qué: `mypy` en CI sí, en pre-commit no; `bandit` reemplazado por las reglas S de ruff; `black` ya no existe.
7. El experimento que perdí: `uv` para gestión de entornos. Por ahora sigo con venv + pip-tools, pero lo voy a probar (anotación para el seguimiento del post).
8. Cierre: copy-pasteable `pyproject.toml` mínimo para que el lector se lo lleve.

**Bibliografía:**
- [Astral — ruff](https://docs.astral.sh/ruff/) — docs oficiales.
- [Astral — uv](https://docs.astral.sh/uv/) — el otro proyecto de Astral.
- [pre-commit framework](https://pre-commit.com/).
- [PEP 518 — Specifying Minimum Build System Requirements (pyproject.toml)](https://peps.python.org/pep-0518/).
- [PEP 621 — Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/).
- [Charlie Marsh, *Ruff is in beta*, 2022](https://notes.crmarsh.com/python-tooling-could-be-much-much-faster) — el post que abrió el mundo.
- [Łukasz Langa, *Black: The uncompromising code formatter*](https://black.readthedocs.io/) — referencia histórica.
- [Brett Cannon, *Selecting a packaging tool*, 2024](https://snarky.ca/classifying-python-virtual-environment-workflows/) — para el debate entre venv, poetry, pdm, uv.

**Imágenes:**
- _Crear_: side-by-side de un `pyproject.toml` minimal vs un proyecto-2018 con seis archivos de config (~30 min).
- _Crear_: tabla "antes / después" del stack (~20 min).

**Tags propuestos:** `['Python', 'ruff', 'pre-commit', 'pyproject', 'devenv', 'memoir']`

**Estado actual:** seed con 4 keywords; este es el post más "operacional" de la serie E y el que probablemente más tracción tenga.

