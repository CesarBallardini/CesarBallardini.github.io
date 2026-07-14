---
title: 'El tooling de un backend Python en serio, antes de escribir la primera ruta'
description: 'Gestor de dependencias, linting, dos type checkers a propósito, seguridad estática y de dependencias, tests organizados por tipo, y todo enganchado a pre-commit y CI — la base de calidad de un backend Python, con configuración real generalizada.'
tags: ['Python', 'tooling', 'linting', 'type checking', 'testing', 'CI', 'ruff', 'pytest']
featured_image: 'hero-toolbox.jpg'
---

Antes de escribir la primera ruta de un backend nuevo, vale la pena invertir un rato en el tooling que va a hacer cumplir la calidad del código automáticamente[^img_hero]. La apuesta es simple: "está prolijo" tiene que ser lo que pasa *por default*, no lo que alguien se acuerda de hacer antes de un commit. Esto es lo que arma esa base en un proyecto Python real — la configuración es genérica y generalizada a propósito: no hay una línea de negocio, ni un nombre de cliente, ni nada que identifique de dónde sale. Lo único que se comparte es la parte compartible: cómo se arma el tooling. Armé además un scaffold público con todo esto funcionando de verdad — cloná, `make install`, y andá probando cada sección de este post contra el repo real[^repo].

## Gestión de dependencias y entorno

El punto de partida es [`uv`](https://docs.astral.sh/uv/)[^uv] como gestor de paquetes y de entornos virtuales, con `uv.lock` commiteado al repo — así todo el mundo instala exactamente las mismas versiones, no "lo que resuelva pip hoy". La versión de Python queda fija en un archivo `.python-version`, y el build backend es `hatchling`.

Lo que vale la pena copiar es la separación de **grupos de dependencias**, usando la sintaxis nativa de `uv` (`[dependency-groups]` en `pyproject.toml`) en vez de la vieja costumbre de un solo `requirements-dev.txt` con todo mezclado:

```toml
[dependency-groups]
dev = [
    "pytest>=8",
    "pytest-cov",
    "ruff",
    "pyright",
    "bandit",
    "pre-commit",
]
deploy = [
    "docker",
]
```

El grupo `dev` junta test, lint, type-check y seguridad — todo lo que necesita cualquiera que vaya a tocar código. El grupo `deploy` es sólo tooling de infraestructura: no se instala en un entorno de desarrollo normal, y tampoco corre en el job de tests de CI. La separación evita el típico entorno virtual de 400 paquetes donde nadie sabe bien para qué está la mitad.

## Linting: una sola herramienta en vez de cuatro

[`ruff`](https://docs.astral.sh/ruff/)[^ruff] reemplaza, en una sola herramienta escrita en Rust, lo que antes eran flake8 + black + isort + pyupgrade + pydocstyle corriendo por separado. La configuración real activa, entre otras, las categorías `B` (bugbear — errores comunes de diseño que el intérprete no detecta), `S` (reglas de estilo bandit, seguridad), `I` (orden de imports, isort), `N` (naming, PEP 8), `SIM` (simplificaciones), `RET`/`PIE` (patrones de retorno prolijos), `UP`/`YTT` (sintaxis moderna de Python), `TCH` (imports que sólo hacen falta para type checking) y `D` (pydocstyle, convención Google) — línea máxima de 119 caracteres, comillas simples, complejidad ciclomática máxima 15 vía `mccabe`.

Lo interesante no es la lista de reglas — es cómo se manejan las excepciones. En vez de apagar una regla globalmente porque "molesta en algún lado", las excepciones van acotadas por archivo y con una razón:

```toml
[tool.ruff.lint.per-file-ignores]
"tests/**" = ["S101"]  # assert es la forma idiomática de testear
```

`S101` marca el uso de `assert` fuera de tests. La razón no es estética: `assert` se **elimina por completo** cuando Python corre con la optimización `-O` activada, así que un `assert` en código de producción que valida algo importante es una validación que puede desaparecer en runtime sin que nadie se entere. En tests no hay ese riesgo — ahí `assert` es exactamente la herramienta correcta, y por eso la excepción está acotada a `tests/**`, no aplicada en todos lados.

## Dos type checkers, a propósito

Acá viene la parte menos obvia: el proyecto de referencia corre **dos** type checkers, `pyright`[^pyright] y `pyrefly`, y no es una migración a medio camino — es una decisión deliberada. `pyright`, en modo "standard" con varias reglas escaladas a `error` (imports sin usar, acceso a un `Optional` sin chequear antes, compatibilidad de overrides entre clases), es el gate que corre en CI y bloquea el merge. `pyrefly` corre en paralelo, local, como parte del flujo de desarrollo (`make types`), porque es sensiblemente más rápido para iterar mientras se escribe código.

¿Por qué no elegir uno solo? La propia configuración del proyecto lo documenta: hay un puñado de comentarios `# type: ignore` que hacen falta para `pyright` — casos genuinamente difíciles de tipar, como kwargs dinámicos en la configuración o mapeo imperativo/clásico de un ORM — y resulta que `pyrefly` respeta esas mismas supresiones por default. Mantener los dos corriendo "en paridad" es una decisión de cinturón y tiradores: dos motores de inferencia distintos que, sobre el mismo código, tienden a encontrar cosas diferentes. No es indecisión, es redundancia elegida.

## Seguridad: dos preguntas distintas, dos herramientas distintas

Hay dos preguntas de seguridad que no son la misma pregunta, y por eso conviene no mezclarlas en una sola herramienta:

- **¿El código que escribimos tiene patrones inseguros?** — la responde `bandit`[^bandit] (SAST, análisis estático). Su configuración deja preparado el flujo de *baseline*, que es la clave para adoptar un scanner de seguridad sobre un código base que ya tiene historia: se genera una vez una foto de los hallazgos actuales, se la commitea al repo, y de ahí en adelante sólo fallan los hallazgos **nuevos**. Los que ya existían y fueron revisados y aceptados no rompen el build cada vez — sin baseline, ese primer scan sobre código preexistente termina en una pantalla roja imposible de limpiar de una sola vez, y el equipo termina apagando la herramienta entera. (En un scaffold que arranca limpio como este todavía no hay nada que baselinear; el valor del baseline aparece el día que se apunta la herramienta a un proyecto real.)
- **¿Las dependencias que usamos tienen vulnerabilidades conocidas?** — la responden `pip-audit` y `OSV-Scanner`[^osv] (SCA, ambos contra el lockfile), corriendo como workflow separado de CI. Un detalle chico pero real: `pip-audit` por default también intenta auditar el propio paquete del proyecto, que —al no estar publicado en PyPI— siempre sale como "no se puede auditar". El flag `--skip-editable` saca ese ruido sin ocultar nada real: sigue fallando si una dependencia de verdad tiene una vulnerabilidad conocida, sólo deja de quejarse por el propio código. Otro detalle no tan obvio: `OSV-Scanner` no es un paquete de Python — es un binario de Go de Google, así que no entra en el mundo `uv`. En vez de forzarlo ahí, se lo trata como lo que es: un binario que tiene que estar en el `PATH` (se instala aparte, por ejemplo con Chocolatey en Windows) y que `make security` invoca directo, sin pasar por `uv run`. En CI corre el mismo binario, vía el *reusable workflow* oficial de GitHub Actions que Google publica para eso — misma herramienta, dos formas distintas de invocarla según el contexto, cada una la que tiene sentido en ese contexto.

## Tests, organizados por lo que realmente cuesta correrlos

`pytest` se configura directamente en `pyproject.toml` (no un `pytest.ini` aparte, un archivo menos), con `--strict-markers` — un marker con un typo falla en vez de silenciarse en un `pytest -m marker_que_no_existe` que simplemente no corre nada.

La organización de carpetas separa los tests por lo que realmente les cuesta correr, no por capricho:

- **Unitarios** — sin infraestructura, rápidos, corren en cada guardado de archivo.
- **De integración** — necesitan una base de datos real (o al menos un contenedor), más lentos.
- **De aceptación (BDD)** — con [`pytest-bdd`](https://pytest-bdd.readthedocs.io/)[^pytestbdd], archivos `.feature` en su propia carpeta y los *step definitions* en una carpeta hermana, describiendo comportamiento en lenguaje natural estructurado (Gherkin).
- **End-to-end** — contra un navegador real, vía [`pytest-playwright`](https://playwright.dev/python/docs/test-runners)[^playwright], los más lentos y los que menos se corren en el loop de desarrollo del día a día.

Markers custom (`unit`, `integration`, `bdd`, `e2e`, y un `snapshot` que queda excluido por default y sólo corre a demanda) le dan a cada quien la posibilidad de correr sólo la porción de la suite que le importa en ese momento — nadie necesita esperar los e2e completos para saber si rompió algo unitario. Para generar datos de prueba sin hardcodear objetos gigantes a mano, `factory-boy` + `faker`. Para coverage, `pytest-cov` corriendo en paralelo vía `pytest-xdist` (`-n auto`, usa todos los cores disponibles), con el reporte en XML listo para subir a un servicio externo de tracking.

## pre-commit: la red de contención antes del commit

[`pre-commit`](https://pre-commit.com/)[^precommit] engancha todo lo anterior — o una parte, la más rápida — al momento del commit, no al momento del CI. Los hooks estándar de `pre-commit-hooks` (archivos grandes accidentalmente agregados, YAML/TOML/JSON mal formado, fin de archivo faltante, espacios en blanco colgados) van primero. Después, cuatro hooks locales propios del proyecto: `ruff check --fix`, `ruff format`, `uv lock --check` (que el lockfile esté sincronizado con `pyproject.toml`, para no descubrir un desfasaje recién en CI) y `bandit`.

Ahí hay una decisión que vale la pena explicar, porque no es la default: `ruff` corre como hook **local**, invocado con `uv run --frozen`, en vez de usar el repo `astral-sh/ruff-pre-commit` ya armado para eso (que es lo que la mayoría de los tutoriales muestra). La razón es concreta: `ruff-pre-commit` fija su propia versión de ruff, independiente de la que está pineada en `uv.lock`. Con el tiempo esas dos versiones divergen — y ahí el lint que corre en pre-commit deja de ser exactamente el mismo lint que corre en CI o en `make lint`, lo que produce el peor tipo de bug de tooling: uno que pasa local y falla en CI (o al revés) sin ningún cambio de código de por medio. Invocar `uv run --frozen ruff` en vez del hook empaquetado garantiza que pre-commit, `make` y CI corren *exactamente* la misma versión, siempre, porque los tres leen del mismo `uv.lock`. Lo mismo aplica a `bandit`: como hook local corriendo por `system`, sin pasar por `uv run`, terminaba llamando a un `bandit` que ni siquiera estaba en el `PATH` fuera del entorno virtual del proyecto — un fallo silencioso hasta que alguien clona el repo sin haber activado el venv a mano.

La idea de fondo, más allá de este caso puntual: cuanto más temprano se encuentra un problema, más barato sale arreglarlo. Un lint que falla en el editor cuesta un segundo. El mismo lint fallando en CI, después de hacer push, cuesta un ida y vuelta completo — y si encima pre-commit y CI corren versiones distintas de la misma herramienta, ese ida y vuelta puede ser puro ruido.

## Un Makefile como única interfaz

Nadie tiene por qué memorizar el comando exacto de cada herramienta, con todos sus flags. Un puñado de targets alcanza, cada uno respondiendo una sola pregunta:

- **`help`** (el target por default: correr `make` sin argumentos alcanza) — lista todos los targets disponibles con una descripción de una línea cada uno, generada a partir de comentarios `##` en el propio Makefile.
- **`install`** — sincroniza el entorno con `uv` e instala los hooks de pre-commit, en un solo paso.
- **`lint`** — corre `ruff check` y `ruff format --check`, sin modificar nada (para CI).
- **`format`** — la versión que sí modifica: `ruff format` más `ruff check --fix`.
- **`types`** — corre los dos type checkers, `pyright` y `pyrefly`.
- **`test`** — la suite completa, unit + integration + acceptance (los e2e quedan afuera por default).
- **`test-bdd`** / **`test-integration`** / **`test-e2e`** — cada tipo de test por separado, para cuando sólo importa una porción de la suite.
- **`security`** — `bandit` contra el baseline, más `pip-audit` y `OSV-Scanner` contra el lockfile.
- **`precommit`** — corre todos los hooks de pre-commit a mano, sin esperar a un commit.

Es una capa de indirección chiquita, pero es la diferencia entre "che, ¿cómo corrías los tests de nuevo?" y simplemente `make test` — o, si ni eso te acordás, `make` a secas. Y como cada target responde una sola pregunta, nada de un `make check-todo` gigante que corre todo junto y te deja adivinando cuál de las cinco herramientas fue la que rompió.

## CI: no un job por responsabilidad, un workflow por responsabilidad

La separación por responsabilidad se puede llevar un paso más allá de "varios jobs en un mismo workflow de CI": tres **workflows** de GitHub Actions completamente independientes, cada uno en su propio archivo.

- **`check`** — lint, formato, tipos.
- **`pytest`** — con contenedores de servicio reales para Postgres y Redis (no mocks de infraestructura, la infraestructura real corriendo en el pipeline).
- **`security`** — bandit contra el baseline, pip-audit y OSV-Scanner contra el lockfile.

La razón de separarlos en archivos distintos y no sólo en jobs de un mismo workflow es concreta: GitHub genera un badge de estado por *workflow*, no por job. Con tres workflows separados, el README puede mostrar tres badges — uno por cada pregunta — en vez de un único badge verde/rojo que no dice cuál de las tres cosas fue la que rompió. Si el badge de seguridad está rojo, ya sabés qué mirar antes de abrir un solo log.

## Lo que este tooling no resuelve

Todo esto hace cumplir *calidad* — que el código esté tipado, testeado, sin vulnerabilidades conocidas, con un estilo consistente. Lo que no dice nada es *cómo organizar el código en sí*: dónde va la lógica de negocio, cómo se relaciona con la base de datos, qué tan fácil es cambiar de framework web sin reescribir todo. Eso es arquitectura, no tooling, y es el tema de la segunda parte de este post.

[^repo]: César Ballardini, [*localenv-python*](https://github.com/CesarBallardini/localenv-python), repositorio en GitHub. El scaffold completo, funcionando: `uv sync`, `make lint`, `make types`, `make test`, todo corre de verdad, no es pseudocódigo.

[^img_hero]: Imagen de portada: [*Socket set with two ratchets in box*](https://commons.wikimedia.org/wiki/File:Socket_set_with_two_ratchets_in_box.jpeg) — fotografía de Pittigrilli, vía Wikimedia Commons — CC BY-SA 4.0. Recortada a 2.5:1 para hero landscape.

[^uv]: [uv](https://docs.astral.sh/uv/) — gestor de paquetes y proyectos Python de Astral, escrito en Rust.

[^ruff]: [Ruff](https://docs.astral.sh/ruff/) — linter y formatter de Python, también de Astral.

[^pyright]: [Pyright](https://microsoft.github.io/pyright/) — type checker estático de Microsoft.

[^bandit]: [Bandit](https://bandit.readthedocs.io/) — analizador estático de seguridad (SAST) para Python, del proyecto PyCQA.

[^osv]: [pip-audit](https://pypi.org/project/pip-audit/) (PyPA) y [OSV-Scanner](https://google.github.io/osv-scanner/) (Google) — análisis de vulnerabilidades conocidas en dependencias (SCA) contra el lockfile.

[^pytestbdd]: [pytest-bdd](https://pytest-bdd.readthedocs.io/) — plugin de pytest para escribir tests de aceptación estilo Gherkin/Cucumber.

[^playwright]: [Playwright para Python](https://playwright.dev/python/docs/test-runners) — automatización de navegador para tests end-to-end.

[^precommit]: [pre-commit](https://pre-commit.com/) — framework para gestionar hooks de git multi-lenguaje.
