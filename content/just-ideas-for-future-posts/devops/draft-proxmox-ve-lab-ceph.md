### G-12 — Proxmox VE como laboratorio: del nodo único al cluster hiperconvergido con Ceph

- **Archivo seed (repo POC):** [github.com/CesarBallardini/pve6-lab](https://github.com/CesarBallardini/pve6-lab) — Shell, último push 2021-07-29
- **Slug propuesto:** `proxmox-ve-lab-ceph`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-proxmox-ve-lab-ceph/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-13]] (LXD homelab — el otro paradigma), [[E-12]]
- **Idioma:** es
- **Madurez:** **partial-poc** — 3 sub-labs incrementales
- **Length target:** medium-long (2000-2800 palabras)

**Concepto:** Proxmox VE es la solución libre/open-source más madura para virtualización + contenedores en un mismo cluster. Mi `pve6-lab` arma 3 escenarios incrementales: (1) nodo único con Terraform manejando contenedores LXC y VMs, (2) cluster de 3 nodos con almacenamiento local (no compartido), (3) cluster de 3 nodos con almacenamiento hiperconvergido vía Ceph. El post recorre los 3 niveles, explica qué problema resuelve cada uno, y por qué Proxmox VE es la elección honesta para homelabs y para PyMEs.

**Hook:** "Proxmox VE no es una alternativa a vSphere — es algo distinto: una manera honesta de virtualizar en serio sin pagar licencias enterprise. Mi lab arma tres escenarios incrementales: solo, 3 nodos, 3 nodos hiperconvergidos con Ceph. El post recorre los tres y dice cuándo conviene cada uno."

**Outline:**
1. Por qué Proxmox VE: licencia libre, base Debian, soporta KVM (VMs) y LXC (contenedores) en el mismo cluster, web UI decente, API REST.
2. **Lab 1 — un solo nodo**: instalación fresca, primer container, primera VM, manejo desde Terraform (provider `Telmate/proxmox`).
3. **Lab 2 — cluster de 3 nodos**: corosync, fencing, migration en vivo entre nodos. Limitación: almacenamiento local no compartido = la migración requiere copia.
4. **Lab 3 — cluster + Ceph**: tres nodos donde cada uno aporta discos al pool Ceph, almacenamiento compartido distribuido, migration en vivo *real*. Esto es hiperconvergencia.
5. Lo que se rompe en cada salto: cluster sin Ceph es frágil; cluster con Ceph requiere disciplina de redes (separación de cluster network y data network).
6. Cuándo conviene Proxmox VE en producción y cuándo no.
7. Cierre: el lab vive en GitHub, podés correrlo en tu laptop con Vagrant + Virtualbox (sí, virtualizando en virtualizando, sí funciona).

**Bibliografía:**
- Repo del POC: [CesarBallardini/pve6-lab](https://github.com/CesarBallardini/pve6-lab).
- [Proxmox VE — sitio oficial](https://www.proxmox.com/en/proxmox-virtual-environment/overview).
- [Proxmox VE Wiki](https://pve.proxmox.com/wiki/Main_Page).
- [Telmate Proxmox Terraform provider](https://registry.terraform.io/providers/Telmate/proxmox/latest/docs).
- [Ceph — sitio oficial](https://ceph.io/).
- [Proxmox + Ceph guide en su Wiki](https://pve.proxmox.com/wiki/Deploy_Hyper-Converged_Ceph_Cluster).

**Imágenes:**
- _Crear_: diagrama de los 3 escenarios incrementales (~1 hora).
- _Crear_: foto del web UI de Proxmox con un cluster funcionando (~10 min).

**Tags propuestos:** `['Proxmox', 'Ceph', 'cluster', 'KVM', 'LXC', 'Terraform', 'homelab']`

**Estado actual:** **partial-poc**, los 3 sub-labs existen, completar el de Ceph es lo más exigente.

