### G-35 — Arquitectura hexagonal en FastAPI: puertos, adaptadores, y las formas de crear una abstracción en Python

- **Archivo seed:** ninguno — nace de la experiencia real en un proyecto privado (cliente no nombrable); sólo se comparte lo genérico: patrones de arquitectura, no código de negocio. Verificado contra un repo real (no nombrar en el post) vía agente de exploración con instrucciones explícitas de confidencialidad.
- **Slug propuesto:** `fastapi-hexagonal-ports-adapters`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-fastapi-hexagonal-ports-adapters/index.md`
- **Serie:** G — "arquitectura como CS" a nivel de código de aplicación. Segunda parte de un díptico; la primera es [[G-34]] (tooling de Python).
- **Cross-links:** depende de [[G-34]] (parte 1: el tooling que hace cumplir todo esto); cruza con [[G-01]] (mismo espíritu: patrón de organización reusable); posible cruce con Serie C (filosofía — dependency inversion como decisión de diseño)
- **Idioma:** es
- **Madurez:** seed-with-sources — outline completo, arquitectura verificada contra un proyecto real (generalizada, sin nombres de cliente/dominio). Falta prosa.
- **Length target:** medium-long (2000-2800 palabras)

**Concepto:** cómo organizar el código de un backend FastAPI para que la lógica de negocio (el dominio) no dependa de FastAPI, ni de SQLAlchemy, ni de ningún detalle de infraestructura — sino de **abstracciones** (puertos) que la infraestructura implementa (adaptadores). Esto es arquitectura hexagonal / puertos y adaptadores, aplicada con las herramientas reales de Python: `typing.Protocol` para definir puertos, `import-linter` para hacer cumplir la regla de dependencia automáticamente (no a confianza), y un contenedor de inyección de dependencias para wirear todo sin que el dominio se entere de qué adaptador concreto está usando en cada momento.

**Restricción explícita del post:** el código real pertenece a un proyecto privado de un cliente y no se puede compartir ni el dominio, ni nombres de clases de negocio, ni la lógica concreta. Lo que sí se comparte, generalizado a un ejemplo de juguete (no el dominio real): la forma de las carpetas, los contratos de `import-linter`, y el dato real de que el proyecto de referencia eligió `Protocol` sobre `ABC` para todos sus puertos de infraestructura genérica (reloj, envío de email, storage de archivos, hasher de contraseñas, renderer de PDF, servicio de tokens, unit-of-work, asignador de secuencias).

**Hook:** _pendiente — asume que el lector ya vio o puede asumir el tooling de [[G-34]]; empieza directo con el problema de arquitectura._

**Outline:**
1. El problema: por qué "todo en un solo router" funciona el primer mes y se vuelve inmantenible al sexto — lógica de negocio, framework web y base de datos todos mezclados en los mismos archivos.
2. Puertos y adaptadores, explicado con una analogía simple antes de meterse en Python. Cita al artículo original de Alistair Cockburn (2005).
3. La regla de dependencia: el dominio no importa nada de afuera; todo lo demás importa hacia el dominio. Cómo se hace cumplir automáticamente con `import-linter`, no a mano ni a confianza:
   - Contrato de **capas**: `adapters` → `application` → `domain`, las de arriba pueden importar las de abajo, nunca al revés.
   - Contrato **prohibido**: el paquete `domain` no puede importar FastAPI, SQLAlchemy, Celery, la librería de DI, ni Pydantic — tiene que poder describirse en Python puro.
   - Corre en pre-commit, CI, y como target de Makefile — se rompe el build, no la buena fe.
4. Las formas de crear una abstracción en Python — sección central del post:
   - `abc.ABC` + método abstracto: clásico, explícito, requiere herencia nominal (el adaptador declara que hereda del puerto).
   - `typing.Protocol`: structural typing — "duck typing con chequeo estático", no requiere herencia. **Caso real:** el proyecto de referencia define todos sus puertos como `Protocol`.
   - Por qué esa elección tiene sentido para puertos de infraestructura genérica — en particular, para envolver una librería de terceros que ya existe y no se puede (o no conviene) forzar a heredar de una clase propia.
   - Regla práctica de cuándo usar cada una: `Protocol` cuando el adaptador es ajeno o ya existe; `ABC` cuando conviene compartir código default entre varias implementaciones propias.
5. Cómo se ve la carpeta `src/` en un proyecto hexagonal real: `domain/`, `application/` (con `ports/` adentro), `adapters/inbound/` y `adapters/outbound/`, `config/` (settings + wiring de DI) — genéricos, no los nombres reales del proyecto privado.
6. Wiring de dependencias — cómo un puerto se conecta a un adaptador concreto sin que el dominio lo sepa. Dos caminos:
   - Manual (factory functions / parámetros por defecto): el camino sin librería, suficiente para un proyecto chico.
   - Con un contenedor DI (`dependency-injector`: `DeclarativeContainer`, providers `Factory`/`Singleton`, decorador `@inject` + `Provide[...]`): el camino que usa el proyecto de referencia, útil cuando el grafo de dependencias crece. Contraste con el `Depends()` nativo de FastAPI.
7. Ejemplo de juguete de punta a punta: un puerto (`Protocol`), dos adaptadores (uno real, uno fake para tests), wireado en una ruta FastAPI — mostrar cómo el dominio ni se entera de cuál está usando, y cómo eso permite testear sin levantar infraestructura real.
8. Cierre: qué se gana con este andamiaje cuando el proyecto crece (testear el dominio sin DB, cambiar de framework sin tocar negocio, onboarding más rápido), y cuándo NO vale la pena (proyectos chicos, prototipos descartables, scripts de un solo uso).

**Bibliografía:**
- Alistair Cockburn, [*Hexagonal architecture*](https://alistair.cockburn.us/hexagonal-architecture/) — el artículo original que nombra el patrón (2005).
- [`typing.Protocol` — documentación oficial de Python](https://docs.python.org/3/library/typing.html#typing.Protocol) — structural subtyping.
- [`abc` — documentación oficial de Python](https://docs.python.org/3/library/abc.html) — clases base abstractas.
- [import-linter — documentación](https://import-linter.readthedocs.io/).
- [dependency-injector — documentación](https://python-dependency-injector.ets-labs.org/).
- [FastAPI — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) — el mecanismo `Depends()` nativo del framework, para contrastar con un contenedor DI externo.
- Robert C Martin, *Clean Architecture*, Prentice Hall 2017 — evaluar si se cita o si Cockburn alcanza como referencia de la regla de dependencia.

**Imágenes:** _pendiente_ — candidato obvio: diagrama de capas (dominio en el centro, adaptadores alrededor) — el clásico hexágono de Cockburn, hecho con mermaid (`mermaid: true` en frontmatter, ver Convenciones de la casa → Diagramas).

**Tags propuestos:** `['Python', 'FastAPI', 'arquitectura hexagonal', 'ports and adapters', 'dependency injection', 'Protocol']` (a confirmar contra tags ya usados).

**Estado actual:** **seed-with-sources.** Split de lo que era un draft único (G-34 combinado) en dos posts — este es la mitad de arquitectura. Falta hook y prosa completa.
