### G-07 — Docker en Windows: lo que nadie te cuenta cuando elegís WSL2 vs Hyper-V

- **Archivo seed:** `sysadmin/ms-windows-docker-containers.md`
- **Slug propuesto:** `docker-en-windows-wsl2-hyperv`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-docker-en-windows-wsl2-hyperv/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-06]] (Postgres en Docker, también en Windows), [[E-05]] (Vue env: corre en WSL2 también)
- **Idioma:** es
- **Madurez:** bare-seed (archivo vacío)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** Docker en Windows tiene tres modos posibles: Docker Desktop con backend WSL2, Docker Desktop con backend Hyper-V, o Docker corriendo nativo en WSL2 sin Docker Desktop. Cada uno tiene trade-offs reales en performance, compatibilidad y licenciamiento. El post explica los tres, dice cuándo elegir cuál, y termina con la opción que yo elijo en 2026 (spoiler: Docker en WSL2 sin Docker Desktop, cuando podés).

**Hook:** "Docker en Windows es un campo minado de decisiones que parecen idénticas y son muy distintas. WSL2 vs Hyper-V suena a 'da lo mismo, son backends'. No, no da lo mismo. Y desde 2021 Docker Desktop tiene una licencia comercial que te puede afectar. Vamos a desarmar las tres opciones honestamente."

**Outline:**
1. El paisaje en 2026: tres maneras de correr Docker en Windows. Mapa rápido.
2. **Opción A: Docker Desktop + WSL2 backend** — la más popular. Cómo funciona internamente (la VM hidden, el moby distro). Performance de filesystem real (un benchmark concreto). Cuándo conviene.
3. **Opción B: Docker Desktop + Hyper-V backend** — la "vieja". Por qué casi nadie la elige hoy. Casos donde sigue siendo correcta (Windows containers).
4. **Opción C: Docker en WSL2 sin Docker Desktop** — la opción "pura". Instalación manual del daemon en una distro WSL2. Sin GUI. Sin license management. Cómo se ve.
5. La trampa de licenciamiento: Docker Desktop pasó a tener licencia comercial para empresas grandes en 2021. Qué quiere decir exactamente, qué empresas afecta, alternativas.
6. Performance real: un benchmark sencillo (build de una imagen Python con muchas dependencies, mismo Dockerfile, tres setups). Resultados con números.
7. La trampa del filesystem: bind-mounts entre Windows y WSL2 son lentos. Mucho. Cómo evitarlos: mantener los proyectos *dentro* del filesystem WSL2 (`\\wsl$\Ubuntu\home\user\proyecto`).
8. Mi configuración actual (2026) — los 6 pasos.
9. Cierre: cuándo Rancher Desktop / Podman Desktop son mejores opciones.

**Bibliografía:**
- [Docker Desktop on Windows — official docs](https://docs.docker.com/desktop/install/windows-install/).
- [Docker Subscription Service Agreement — pricing & licensing](https://www.docker.com/legal/docker-subscription-service-agreement/) — leer cuidadoso.
- [Microsoft — WSL2 documentation](https://learn.microsoft.com/en-us/windows/wsl/).
- [Microsoft — WSL2 architecture](https://learn.microsoft.com/en-us/windows/wsl/compare-versions).
- [Rancher Desktop — sitio oficial](https://rancherdesktop.io/) — la alternativa libre.
- [Podman Desktop](https://podman-desktop.io/) — la otra alternativa libre.
- [Brendan Gregg, *Linux Performance Tools*](https://www.brendangregg.com/linuxperf.html) — para los benchmarks.
- [Hyper-V Architecture — Microsoft Learn](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/hyper-v-architecture) — para entender la opción B.

**Imágenes:**
- _Crear_: diagrama comparativo de los tres setups con cajas (host / VM / containers / volumes) (~1 hora — esta es la imagen central del post).
- _Crear_: gráfico de barras del benchmark (~30 min, después de correrlo).
- _Crear_: tabla decision tree "qué elegís según tu caso" (~20 min).

**Tags propuestos:** `['Docker', 'Windows', 'WSL2', 'Hyper-V', 'Rancher Desktop', 'devenv']`

**Estado actual:** archivo vacío; tengo que correr el benchmark para tener números honestos antes de publicar.

