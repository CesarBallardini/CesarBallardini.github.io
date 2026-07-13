### G-34 — El tooling de un backend Python en serio: linting, tipado, tests y seguridad antes de escribir la primera ruta

- **Archivo seed:** ninguno — nace de la experiencia real en un proyecto privado (cliente no nombrable); sólo se comparte lo genérico: configuración de herramientas, no código de negocio. Verificado contra un repo real (no nombrar en el post) vía agente de exploración con instrucciones explícitas de confidencialidad.
- **Slug propuesto:** `python-tooling-backend-desde-cero` — publicado como `content/es/posts/2026-07-14-python-tooling-backend-desde-cero/index.md`
- **Comando:** _no aplica — post ya publicado, este entry es para anclar el cross-link en el plan_
- **Serie:** G — "arquitectura como CS" a nivel de proceso de desarrollo, no de infraestructura. Primera parte de un díptico; la segunda es [[G-35]] (arquitectura hexagonal).
- **Cross-links:** lleva a [[G-35]] (parte 2: una vez que el tooling está andando, cómo organizar el código en sí); cruza con [[G-01]] (mismo espíritu de "patrón reusable que ataca el desorden", ahí en Ansible)
- **Idioma:** es
- **Madurez:** **publicado** (2026-07-14)
- **Length target:** ya escrito (~1664 palabras)

**Concepto:** antes de escribir la primera ruta de un backend, vale la pena invertir un rato en el tooling que va a hacer cumplir la calidad del código automáticamente — para que "está prolijo" no dependa de la memoria ni de la buena voluntad de nadie. Este post recorre, con configuración real (generalizada, sin revelar nada de un proyecto de cliente concreto), cómo se arma esa base: gestor de dependencias, linting, dos type checkers corriendo en paralelo a propósito, seguridad estática y de dependencias, testing organizado por tipo, y todo enganchado a pre-commit y CI para que nadie tenga que acordarse de correr nada a mano.

**Restricción explícita del post:** el tooling y su configuración (nombres de herramientas, reglas activadas, estructura de jobs de CI) es 100% genérico y compartible. Lo que NO aparece: nombre del cliente/proyecto, nombres de módulos o clases de negocio, lógica concreta. Cualquier ejemplo de código es un ejemplo de juguete, no un recorte real.

**Hook:** _pendiente._

**Outline:**
1. Por qué invertir tiempo en tooling antes de la primera línea de negocio — la apuesta: "prolijo" tiene que ser lo que pasa por default, no lo que alguien recuerda hacer.
2. Gestión de dependencias y entorno con `uv`: `uv.lock` commiteado, `.python-version` fijo, build backend `hatchling`, grupos de dependencias (`dev` vs `deploy`) separando qué se instala en desarrollo de qué es sólo para el pipeline de deploy.
3. Linting con `ruff`: una sola herramienta reemplazando flake8+black+isort+pyupgrade. Categorías de reglas reales (bugbear, seguridad estilo bandit, naming, simplificación, pydocstyle), línea de 119 caracteres, complejidad ciclomática máxima 15. El caso concreto de `S101` (assert): permitido sólo en tests, nunca en producción, porque `python -O` los elimina — un ejemplo de regla con una razón técnica real detrás, no arbitraria.
4. Type checking con dos herramientas a la vez, a propósito: `pyright` como gate de CI, `pyrefly` corriendo en paralelo local como segundo chequeo más rápido. Por qué mantener los dos en vez de migrar a uno solo — la lógica de "cinturón y tiradores" documentada en la propia config del proyecto de referencia.
5. Seguridad: `bandit` (SAST, con baseline commiteado — sólo fallan hallazgos *nuevos*) y `pip-audit`/`osv-scanner` (SCA contra el lockfile) como job separado, generando SBOM.
6. Testing con `pytest`: organización en carpetas por tipo (unit, integration, acceptance/BDD con `pytest-bdd`, e2e con `pytest-playwright`), markers custom (`unit`, `integration`, `e2e`, `snapshot` opt-in), `factory-boy` + `faker` para datos de prueba, coverage con `pytest-cov` + `pytest-xdist` en paralelo.
7. pre-commit como red de contención local: qué hooks corren antes de cada commit (formato, lint, lockfile sincronizado, límites de arquitectura — mencionado brevemente, desarrollado en la Parte 2) para que los problemas se encuentren en el editor, no en la review.
8. Makefile como interfaz única: `make lint`, `make types`, `make test`, `make security` — nadie memoriza el comando exacto de cada herramienta.
9. CI dividido por responsabilidad: un job de chequeos estáticos, un job de tests con contenedores de servicio (Postgres, Redis), un job de seguridad — separados para que un fallo de seguridad no oscurezca un fallo de tipo, y viceversa.
10. Cierre + forward-link: todo este tooling hace cumplir *calidad*, pero no dice nada sobre *cómo organizar el código en sí* — eso es el tema de la Parte 2 ([[G-35]]).

**Bibliografía:**
- [Ruff — documentación oficial](https://docs.astral.sh/ruff/).
- [uv — documentación oficial](https://docs.astral.sh/uv/).
- [pyright — documentación](https://microsoft.github.io/pyright/).
- [pytest-bdd — documentación](https://pytest-bdd.readthedocs.io/).
- [pytest-playwright — documentación](https://playwright.dev/python/docs/test-runners).
- [Bandit — documentación](https://bandit.readthedocs.io/).
- [pip-audit](https://pypi.org/project/pip-audit/) / [OSV-Scanner](https://google.github.io/osv-scanner/).
- [pre-commit — documentación](https://pre-commit.com/).
- [CycloneDX](https://cyclonedx.org/) — formato de SBOM mencionado en el job de seguridad de CI.

**Imágenes:** _ya incorporada al post publicado_ — se descartó el diagrama mermaid de jobs de CI (el post terminó sin necesitarlo, la prosa alcanzó) a favor de un hero fotográfico: `hero-toolbox.jpg`, foto de una caja de herramientas Proxxon organizada (CC BY-SA 4.0, Wikimedia Commons) recortada a 2.5:1 — metáfora directa: cada herramienta en su lugar definido, como cada tool de este post cumple un rol específico.

**Tags propuestos:** `['Python', 'tooling', 'linting', 'type checking', 'testing', 'CI', 'ruff', 'pytest']` (confirmado, son los tags reales del post).

**Estado actual:** **publicado el 2026-07-14**, [post en vivo](/posts/python-tooling-backend-desde-cero/) (nota: fecha futura respecto del reloj del sistema al momento de escribir — el post no aparece en `public/` hasta que Hugo se rebuildee sin `--buildFuture` en o después de esa fecha; ver [[G-35]] para el mismo patrón con el post de KL1). El post siguió el outline casi sin desvíos — la única diferencia real es que no se incluyeron ejemplos de configuración TOML/YAML tal cual del repo real (ni siquiera generalizados con nombres de fantasía) para no arriesgar ninguna filtración; los snippets de código que aparecen (grupos de dependencias, `per-file-ignores`) son ejemplos genéricos escritos para el post, no extraídos ni parafraseados del repo real. Acciones pendientes:
- Publicar [[G-35]] (la segunda parte, arquitectura hexagonal) y cross-linkearla desde acá.
- Cross-link con [[G-01]] cuando ese post se revise/actualice.
