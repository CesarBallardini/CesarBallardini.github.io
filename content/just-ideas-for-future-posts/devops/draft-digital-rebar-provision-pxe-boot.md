### G-27 — Digital Rebar Provision: PXE y orquestación de boot para provisioning masivo

- **Archivo seed:** `github.com/CesarBallardini/ansible-role-dr-provision` (fork, Python, Mar 2021)
- **Slug propuesto:** `digital-rebar-provision-pxe-boot`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-digital-rebar-provision-pxe-boot/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[H-08]] (ThinStation: el primo legacy), [[H-09]] (UDPcast: otro approach), [[G-17]] (Partman + Preseed con Packer)
- **Idioma:** es
- **Madurez:** **incompleto** — fork del role, repo corto; no tengo despliegue en producción documentado
- **Length target:** short (800-1200 palabras)

**Concepto:** Digital Rebar Provision (DRP) es una herramienta moderna de *metal provisioning*: PXE server + DHCP + TFTP + orchestration para booteear decenas de máquinas desde cero. Es el reemplazo natural de ThinStation ([[H-08]]) + UDPcast ([[H-09]]) para infraestructura moderna (UEFI, netboot HTTPS, workflows declarativos). El role Ansible instala DRP con una configuración mínima. El post explica el escenario (bootstrap de cluster bare metal) y cuándo preferir DRP a alternativas (MAAS, Foreman, kickstart puro).

**Hook:** "tenés 10 servidores físicos nuevos. Los enchufás. Prende cada uno. Bootea por red. A los 15 minutos cada uno tiene Ubuntu instalado, ssh keys cargadas, su rol Ansible inicial aplicado. Vos no tocaste ninguno. Eso es Digital Rebar Provision."

**Outline:**
1. El escenario: bootstrap de un cluster bare metal / homelab / racks de servers.
2. Las alternativas: MAAS (Canonical), Foreman, kickstart + DHCP manual, Cobbler.
3. DRP: qué es, qué ofrece (workflows declarativos, plugins, API REST).
4. El role Ansible forkeado: setup mínimo de DRP en una VM de gestión.
5. Lo que me falta: experiencia en producción con DRP; el post es más un mapa que un tutorial.
6. Cierre: si vas a hacer bootstrapping masivo, DRP es una opción seria; documentate antes de comprometerte.

**Bibliografía:**
- [Digital Rebar Provision](https://docs.rackn.io/).
- [RackN — el proyecto atrás de DRP](https://rackn.com/).
- [MAAS — Metal As A Service, Canonical](https://maas.io/).
- [Foreman project](https://www.theforeman.org/).
- [Cobbler — red hat](https://cobbler.github.io/).

**Imágenes:**
- _Crear_: diagrama PXE boot → DRP → Ubuntu install → Ansible inicial (~45 min).

**Tags propuestos:** `['Digital Rebar', 'PXE', 'bare metal', 'provisioning', 'Ansible']`

**Estado actual:** **fork incompleto** — el post es honesto sobre que es un mapa, no un tutorial con experiencia productiva.

