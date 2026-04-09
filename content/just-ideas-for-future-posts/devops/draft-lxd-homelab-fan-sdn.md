### G-13 — LXD homelab: cluster con FAN overlay y SDN

- **Archivo seed (repo POC):** [github.com/CesarBallardini/lxd-homelab](https://github.com/CesarBallardini/lxd-homelab) — Shell, último push 2021-01-21
- **Slug propuesto:** `lxd-homelab-fan-sdn`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-lxd-homelab-fan-sdn/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-12]] (Proxmox — el otro paradigma); cruza con [[G-15]] (Ceph storage)
- **Idioma:** es
- **Madurez:** **partial-poc** — labs definidos pero el último (Ceph) puede no estar completo
- **Length target:** medium (1500-2200 palabras)

**Concepto:** LXD es la otra alternativa seria a Docker para containerización Linux nativa, pero con ergonomía de "containers como VMs livianas". Mi `lxd-homelab` arma escenarios incrementales: nodo único, cliente-API remoto, cluster de 3 nodos con red FAN (overlay), SDN entre containers, y storage Ceph. El post explica qué hace LXD distinto de Docker (system containers vs application containers), por qué FAN es una idea elegante, y cuándo elegir LXD en vez de Docker o Proxmox.

**Hook:** "Docker te da application containers — un proceso por container, ephemeral, stateless. LXD te da *system containers* — un Linux completo dentro de un container, con init, servicios, persistencia. Es otra cosa. Mi homelab arma un cluster LXD con red FAN (overlay), SDN y storage Ceph. El post explica qué hace LXD distinto y cuándo conviene."

**Outline:**
1. La diferencia LXC/LXD vs Docker en una frase.
2. Lab 1 — nodo único: instalación, primer container, persistencia de filesystem.
3. Lab 2 — cliente API remoto: cómo usar `lxc` desde otra máquina sin SSH a la propia.
4. Lab 3 — cluster de 3 nodos con FAN overlay: la idea de FAN (Fully Automatic Networks) de Ubuntu — un /16 por host que se subdivide automáticamente sin DHCP central.
5. Lab 4 — SDN: cómo separar redes virtuales entre containers en distintos hosts.
6. Lab 5 — storage Ceph: opcional, complejo (cross [[G-12]]).
7. Cuándo LXD es mejor que Docker y cuándo no.
8. Cierre.

**Bibliografía:**
- Repo del POC: [CesarBallardini/lxd-homelab](https://github.com/CesarBallardini/lxd-homelab).
- [LXD — sitio oficial](https://canonical.com/lxd).
- [Ubuntu FAN networking](https://ubuntu.com/blog/an-overview-of-ubuntu-fan).
- [Stéphane Graber, *LXD blog*](https://stgraber.org/) — el creador.

**Imágenes:**
- _Crear_: diagrama de FAN overlay con un /16 por host (~45 min).

**Tags propuestos:** `['LXD', 'LXC', 'FAN', 'SDN', 'cluster', 'homelab', 'Ubuntu']`

**Estado actual:** **partial-poc**.

