### G-17 — Recetas Partman/Preseed con Packer: testear instalaciones automatizadas Debian

- **Archivo seed (repo POC):** [github.com/CesarBallardini/partman-lab](https://github.com/CesarBallardini/partman-lab) — Shell, último push 2019-11-26
- **Slug propuesto:** `partman-preseed-packer`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-partman-preseed-packer/index.md`
- **Serie:** G — niche
- **Cross-links:** lleva a [[G-02]] (golden image)
- **Idioma:** es
- **Madurez:** **complete-poc**
- **Length target:** short (1000-1500 palabras)

**Concepto:** las recetas de partman son la sintaxis arcana del instalador Debian para definir cómo se particionan los discos durante una instalación automatizada con Preseed. Casi nadie las escribe. Mi `partman-lab` usa Packer para construir VMs Vagrant Ubuntu 18.04 con distintas recetas (desktop default, crypto, LVM-default, d1pv1vg1lv2, d1pv1vg2lv7) y verifica con `pvdisplay/vgdisplay/lvdisplay` que cada receta efectivamente produzca el layout esperado. Es niche, pero útil para cualquiera que tenga que mantener una flota de Debian con particionado custom.

**Hook:** "particionado automatizado de Debian con Preseed: la documentación oficial es críptica, los ejemplos son escasos, y la única manera de saber si tu receta funciona es bootear el instalador. Mi lab usa Packer para construir VMs Vagrant con cada receta, y verifica el resultado automáticamente. Acá está, con cinco recetas listas para reusar."

**Outline:**
1. Qué es Preseed (instalador Debian no-interactivo).
2. Qué es partman (la parte de Preseed que decide el particionado del disco).
3. Por qué partman es difícil: sintaxis arcana, errores silenciosos, sin validador offline.
4. La estrategia: usar Packer para construir una VM con cada receta, y validar con LVM commands.
5. Las cinco recetas en mi repo y qué layout producen.
6. Cierre.

**Bibliografía:**
- Repo del POC: [CesarBallardini/partman-lab](https://github.com/CesarBallardini/partman-lab).
- [Debian Installer — Preseed manual](https://www.debian.org/releases/stable/amd64/apb.en.html).
- [partman-auto recipe format](https://wiki.debian.org/DebianInstaller/Preseed/PartMan).
- [Packer — sitio oficial](https://www.packer.io/).

**Imágenes:**
- _Crear_: tabla de las 5 recetas y los layouts resultantes (~20 min).

**Tags propuestos:** `['Debian', 'Preseed', 'partman', 'Packer', 'instalacion', 'LVM']`

**Estado actual:** **complete-poc**.

