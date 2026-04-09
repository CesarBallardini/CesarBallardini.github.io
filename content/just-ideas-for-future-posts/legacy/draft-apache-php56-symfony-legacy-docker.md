### H-13 — Apache + PHP 5.6 + Symfony 1.4 y 3.4: correr una app PHP legacy en Docker

- **Archivo seed:** `github.com/CesarBallardini/apache-php56` (fork, PHP, Nov 2019)
- **Slug propuesto:** `apache-php56-symfony-legacy-docker`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-apache-php56-symfony-legacy-docker/index.md`
- **Serie:** H — legacy software hecho ejecutable con container moderno
- **Cross-links:** depende de [[G-06]] (Postgres en Docker), [[G-18]] (GUI apps en Docker); lleva a [[H-01]] (Linux ABI: la familia "viejo binario nuevo kernel")
- **Idioma:** es
- **Madurez:** fork funcional de Dockerfile para Apache + PHP 5.6 + Composer 1.8.5 + Symfony 1.4 y 3.4
- **Length target:** medium (1200-1800 palabras)

**Concepto:** tenés una app PHP vieja — Symfony 1.4 o 3.4, PHP 5.6, Composer 1.x, Apache — y el cliente no la puede reescribir. Los repositorios de tu distro moderna ya no traen PHP 5.6. Solución: containerizar el entorno viejo completo. Apache + PHP 5.6 + extensiones + Composer 1.8.5 como Docker image base, y la app como volumen. La app sigue corriendo en 2026 sobre una Debian 12 host. El post es el caso real y la defensa de "containerizar lo viejo" como estrategia legacy paralela a la de Linux ABI ([[H-01]]).

**Hook:** "tenés una app Symfony 1.4 que necesita PHP 5.6. Los repos de Debian 12 no lo traen. Las alternativas: reescribir (el cliente dice no), dejar un servidor viejo (inaceptable), o containerizar el stack exacto. Elegí la tercera. Acá está el Dockerfile que funciona en 2026."

**Outline:**
1. El escenario: Symfony 1.4 o 3.4, PHP 5.6, Composer 1.8.5, Apache 2.4. Todo EoL hace años.
2. La estrategia: Docker image con Debian base + PHP 5.6 compilado desde Ondrej Sury repo, + extensiones viejas (mcrypt, mysql), + Composer 1.x.
3. El Dockerfile (forkeado, funcional).
4. El patrón "bind-mount del código fuente + container efímero con el runtime".
5. Los gotchas: `mcrypt`, `pecl install` con versiones específicas, SSL certs modernos que confunden a librerías viejas.
6. La política de upgrade: *no upgrade*. Cuando la app necesita seguir viva, el container se construye una vez y no se toca.
7. Cierre: la conexión con [[H-01]] (mismo patrón para SCO Unix, distinta herramienta).

**Bibliografía:**
- [Docker — PHP official images](https://hub.docker.com/_/php) — el upstream moderno.
- [Ondřej Surý — PHP PPAs para Debian/Ubuntu](https://deb.sury.org/) — la fuente histórica de PHP antiguos.
- [Symfony 1.4 documentation archive](https://symfony.com/legacy/doc/reference/1_4/en/) — legacy oficial.
- [Symfony 3.4 LTS documentation](https://symfony.com/releases/3.4).
- [Joel Spolsky, *Things You Should Never Do, Part I*, 2000](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — el ensayo contra rewrite.

**Imágenes:**
- _Crear_: diagrama Dockerfile → image → running container con bind mount al código (~30 min).
- _Crear_: tabla comparativa "rewrite vs emulate vs containerize" (~30 min).

**Tags propuestos:** `['PHP', 'Symfony', 'legacy', 'Docker', 'Apache', 'containers', 'arqueologia']`

**Estado actual:** fork funcional del Dockerfile; el post se arma con el material del repo.

