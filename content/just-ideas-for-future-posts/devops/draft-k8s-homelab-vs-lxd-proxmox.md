### G-22 — k8s-homelab: el cluster Kubernetes que armé y por qué sigo usando LXD para casi todo

- **Archivo seed:** `github.com/CesarBallardini/k8s-homelab` (own, MIT, Mar 2021)
- **Slug propuesto:** `k8s-homelab-vs-lxd-proxmox`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-k8s-homelab-vs-lxd-proxmox/index.md`
- **Serie:** G
- **Cross-links:** contrasta con [[G-12]] (Proxmox) y [[G-13]] (LXD); lleva a [[G-02]] (infra determinística)
- **Idioma:** es
- **Madurez:** **parcialmente completo** — repo con manifests y documentación, experiencia real, pero no sostenido en el tiempo
- **Length target:** medium (1500-2000 palabras)

**Concepto:** armé un Kubernetes homelab siguiendo el evangelio ("todos deberían correr k8s en casa"), corrí cargas, medí, aprendí. La conclusión honesta: para homelab, k8s es sobre-ingeniería para casi todo. LXD ([[G-13]]) y Proxmox ([[G-12]]) cubren el 90% de los casos con 10% de la complejidad. El post es la comparación honesta de los tres stacks para el mismo tipo de uso doméstico.

**Hook:** "monté Kubernetes en casa. Lo sostuve 8 meses. Lo desarmé. Volví a LXD. El post no es un take anti-Kubernetes — es la explicación honesta de por qué una herramienta diseñada para clusters de cientos de nodos es *la respuesta incorrecta* para tu laptop con 3 Raspberry Pis conectadas."

**Outline:**
1. El stack k8s-homelab: k3s, MetalLB, Traefik, cert-manager, Longhorn. Bonito sobre el papel.
2. Lo que funcionó: GitOps, self-healing de workloads, rolling updates. Real y valioso.
3. Lo que NO funcionó a escala hobby: el peso operativo (60% del tiempo era mantener el cluster, no usarlo), la curva de aprendizaje permanente (cada upgrade rompe algo), la huella de RAM (k8s se come 2GB antes de correr un solo workload), el debugging multi-capa.
4. La comparación fría con LXD: para correr 15 servicios en una LAN, `lxc launch` gana. Sin ingress, sin MetalLB, sin Longhorn. SSH al container.
5. La comparación con Proxmox: para VMs de verdad (Windows, Hercules, cosas que no son containers), Proxmox gana.
6. El mapa honesto: k8s sirve cuando *realmente* necesitás orquestación multi-nodo con rollouts atómicos. Casi nunca es el caso en casa.
7. Cierre: el repo sigue como referencia por si alguien quiere repetir el experimento. Yo volví a LXD y no me arrepentí.

**Bibliografía:**
- [k3s — sitio oficial](https://k3s.io/) — la distribución ligera de k8s para homelab.
- [Kelsey Hightower, *Kubernetes The Hard Way*](https://github.com/kelseyhightower/kubernetes-the-hard-way) — para entender qué hay adentro.
- [Jérôme Petazzoni, *Container Training*](https://container.training/) — referencia educativa.
- [LXD documentation](https://documentation.ubuntu.com/lxd/en/latest/).
- [Proxmox VE documentation](https://pve.proxmox.com/pve-docs/).
- [Dan Luu, *Why does Kubernetes take so much memory?*](https://danluu.com/) — buscar posts honestos sobre overhead.

**Imágenes:**
- _Crear_: tabla comparativa k3s vs LXD vs Proxmox (~45 min).
- _Crear_: gráfico de uso de RAM del cluster en reposo (~15 min).

**Tags propuestos:** `['Kubernetes', 'k3s', 'homelab', 'LXD', 'Proxmox', 'sysadmin', 'memoir']`

**Estado actual:** repo con manifests de 2021, experiencia real, **post honesto y sin hype** pendiente de escribir.

