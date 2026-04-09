### G-09 — `localenv-*`: un patrón para entornos de desarrollo locales (Python, WordPress, Symfony6)

- **Archivo seed (repo POC):** familia de tres repos: [localenv-python](https://github.com/CesarBallardini/localenv-python), [localenv-wordpress](https://github.com/CesarBallardini/localenv-wordpress), [localenv-symfony6](https://github.com/CesarBallardini/localenv-symfony6)
- **Slug propuesto:** `localenv-pattern-python-wp-symfony`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-localenv-pattern-python-wp-symfony/index.md`
- **Serie:** G
- **Cross-links:** depende de [[E-12]] (el patrón); lleva a [[G-08]] (`ansible-devops-workstation` que provisiona el host), [[G-10]] (la trampa de delegate_to en localenv-ansible)
- **Idioma:** es
- **Madurez:** **complete-poc** los tres
- **Length target:** medium (1500-2200 palabras)

**Concepto:** los repos `localenv-*` son una familia que muestra cómo aplicar el mismo patrón Vagrant + Ansible (ver [[E-12]]) a tres stacks distintos: Python con pyenv + virtualenv, WordPress con PHP/MariaDB/nginx con SSL, y Symfony 6 con PHP 8 + MariaDB. Tres dominios distintos, mismo esqueleto. El post no es sobre Python, ni WP, ni Symfony — es sobre el *patrón* de "una VM por stack de proyecto", las decisiones repetidas (Virtualbox vs Docker como provider, instalación de versiones específicas, persistencia de DB, certificados SSL self-signed vs LetsEncrypt) y por qué el mismo template sirve para los tres.

**Hook:** "tengo tres repos en GitHub que se llaman `localenv-python`, `localenv-wordpress` y `localenv-symfony6`. A primera vista parecen tres cosas distintas. En realidad son el mismo esqueleto aplicado a tres stacks. El post no es sobre Python, WP o Symfony — es sobre cómo cuando armás bien un patrón de entorno local, podés *aplicarlo* a stacks nuevos en una hora."

**Outline:**
1. El problema: cada vez que arrancás un proyecto en un stack distinto, terminás contaminando tu host con dependencias raras o sufriendo Docker Compose ad-hoc.
2. La solución repetible: una VM Vagrant por proyecto, provider intercambiable (Virtualbox o Docker), provisión Ansible que instala las versiones exactas que el proyecto necesita.
3. Caso 1 — `localenv-python`: pyenv + virtualenv, GUI VSCode corriendo *dentro* de la VM y proxyado al host con socat sobre los abstract sockets de X11 (esto es lo más raro del repo y merece subsección propia).
4. Caso 2 — `localenv-wordpress`: PHP 7.4/8.0/8.1 (selectable), versión de WP configurable, MariaDB, nginx, SSL self-signed o LetsEncrypt, WP-CLI. Provider Virtualbox o Docker (incluyendo Apple M1).
5. Caso 3 — `localenv-symfony6`: Symfony 6 + PHP 8 + MariaDB 10.3 sobre Ubuntu 20.04. Cómo scaffoldear un symfony/symfony-demo desde cero.
6. Las decisiones repetidas en los tres: cuándo Virtualbox y cuándo Docker como provider, cómo persistir la DB entre destrucciones de VM, cómo manejar puertos forwarded.
7. Lo que cambia entre los tres: nada estructural. Sólo los roles Ansible que instalan las dependencias específicas.
8. Cierre: el patrón es reusable. Se puede armar `localenv-rails`, `localenv-django`, `localenv-laravel` con 2 horas de trabajo cada uno.

**Bibliografía:**
- Repos: [localenv-python](https://github.com/CesarBallardini/localenv-python), [localenv-wordpress](https://github.com/CesarBallardini/localenv-wordpress), [localenv-symfony6](https://github.com/CesarBallardini/localenv-symfony6).
- [pyenv](https://github.com/pyenv/pyenv).
- [WordPress — sitio oficial](https://wordpress.org/).
- [Symfony — sitio oficial](https://symfony.com/).
- [Vagrant docs](https://developer.hashicorp.com/vagrant).
- Cross-link [[E-12]] para el patrón abstracto.

**Imágenes:**
- _Crear_: tabla side-by-side de los tres repos mostrando qué cambia y qué no (~30 min).
- _Crear_: diagrama del flujo de socat para X11 abstract sockets (~30 min, esta es la subsección más rara).

**Tags propuestos:** `['Vagrant', 'Ansible', 'devenv', 'Python', 'WordPress', 'Symfony', 'pyenv', 'localenv']`

**Estado actual:** los tres repos en GitHub están funcionales. Post fácil de cerrar.

