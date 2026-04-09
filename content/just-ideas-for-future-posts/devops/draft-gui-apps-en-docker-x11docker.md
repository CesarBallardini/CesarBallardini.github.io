### G-18 — GUI apps en Docker: pgModeler + el problema del display + x11docker

- **Archivo seed (repo POC):** [github.com/CesarBallardini/pgModeler](https://github.com/CesarBallardini/pgModeler) — Shell, último push 2025-04-25 — más [github.com/CesarBallardini/gui-apps-on-docker](https://github.com/CesarBallardini/gui-apps-on-docker)
- **Slug propuesto:** `gui-apps-en-docker-x11docker`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-gui-apps-en-docker-x11docker/index.md`
- **Serie:** G — niche pero util
- **Cross-links:** lleva a [[G-19]] (apps GUI en VMs), [[G-09]] (localenv-python tiene el truco socat)
- **Idioma:** es
- **Madurez:** **complete-poc**
- **Length target:** medium (1500-2000 palabras)

**Concepto:** Docker fue diseñado para apps stateless de servidor, no para apps GUI. Pero a veces necesitás correr un GUI propietario (pgModeler, Visual Paradigm, Enterprise Architect) sin instalarlo en tu host. Las opciones para mostrar el display son: bind-mount del socket Unix de X11, x11docker (wrapper que automatiza permisos), x11vnc + xvfb (display headless con VNC encima). Mi POC lo demuestra con pgModeler compilado desde tarball, en VirtualBox VM y también en Docker container.

**Hook:** "pgModeler es una herramienta GUI excelente para diseñar esquemas PostgreSQL. La querés correr sin instalarla en tu laptop. ¿Docker? Sí, pero Docker no fue diseñado para GUIs. Hay tres trucos canónicos para hacerlo. Acá los explico todos, con ejemplo funcional."

**Outline:**
1. Por qué correr GUIs en Docker: aislar dependencias de una app que no usás todos los días.
2. El problema fundamental: Docker no tiene noción de display.
3. **Truco 1 — bind-mount del socket Unix `/tmp/.X11-unix`**: el más simple, requiere que el host corra X11 (no Wayland). El issue de `xhost +local:docker` y por qué casi siempre es la solución *peligrosa*.
4. **Truco 2 — x11docker**: un wrapper que automatiza los permisos correctamente, soporta Wayland host, soporta autenticación con xauth.
5. **Truco 3 — x11vnc + xvfb dentro del container**: display virtual headless, accedido por VNC desde el host. Útil cuando el host no tiene X11 (CI, server, Mac).
6. Mi POC: pgModeler compilado desde tarball, en VirtualBox VM (truco 1) y en Docker container (truco 2).
7. Cuándo elegir cuál.
8. Cierre.

**Bibliografía:**
- Repos: [pgModeler](https://github.com/CesarBallardini/pgModeler), [gui-apps-on-docker](https://github.com/CesarBallardini/gui-apps-on-docker).
- [pgModeler — sitio oficial](https://pgmodeler.io/).
- [x11docker en GitHub](https://github.com/mviereck/x11docker) — la herramienta clave.
- [x11vnc — sitio oficial](http://www.karlrunge.com/x11vnc/).
- [Wayland docs](https://wayland.freedesktop.org/).
- [Wikipedia — X Window System](https://en.wikipedia.org/wiki/X_Window_System).

**Imágenes:**
- _Crear_: diagrama de los 3 trucos side-by-side (~45 min — central).
- _Crear_: screenshot de pgModeler corriendo desde un container (~10 min).

**Tags propuestos:** `['Docker', 'GUI', 'X11', 'x11docker', 'pgModeler', 'Wayland']`

**Estado actual:** **complete-poc** para pgModeler. `gui-apps-on-docker` necesita verificación.

