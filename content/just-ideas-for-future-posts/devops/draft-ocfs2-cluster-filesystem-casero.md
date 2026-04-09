### G-15 — OCFS2 cluster filesystem casero: sobre NBD y sobre disco compartido VirtualBox

- **Archivo seed (repo POC):** [github.com/CesarBallardini/global-filesystem-lab](https://github.com/CesarBallardini/global-filesystem-lab) — Ruby, 1 star, último push 2020-02-13
- **Slug propuesto:** `ocfs2-cluster-filesystem-casero`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-ocfs2-cluster-filesystem-casero/index.md`
- **Serie:** G — high novelty
- **Cross-links:** cruza con [[G-12]] (Ceph como alternativa), [[G-13]] (LXD storage)
- **Idioma:** es
- **Madurez:** **complete-poc** para 2 labs, TODO para GFS2 y online grow
- **Length target:** medium (1500-2200 palabras)

**Concepto:** OCFS2 (Oracle Cluster File System v2) es un cluster filesystem POSIX que dejé olvidado durante años. Mi `global-filesystem-lab` lo arma de dos formas: (1) sobre un dispositivo NBD compartido entre dos nodos, y (2) sobre un disco "shareable" de VirtualBox montado simultáneamente en dos VMs. El post explica qué es un cluster filesystem (vs un network filesystem como NFS), cuándo conviene usarlo, y por qué OCFS2 sobrevive en ciertos escenarios donde Ceph es overkill.

**Hook:** "tenés dos servidores. Querés que ambos lean *y escriban* al mismo filesystem, simultáneamente, sin un servidor NFS en el medio. NFS no es la respuesta. Tampoco lo es Ceph. La respuesta menos conocida se llama *cluster filesystem*: OCFS2, GFS2, GPFS. Acá levanto OCFS2 con dos nodos en VirtualBox compartiendo un disco virtual. Funciona. Y casi nadie habla de esto en español."

**Outline:**
1. La diferencia conceptual: network filesystem (NFS) vs cluster filesystem (OCFS2/GFS2/GPFS). Por qué importa.
2. OCFS2 en 30 segundos: Oracle, GPL, en mainline kernel desde 2.6.16.
3. Lab 1 — sobre NBD: levantar `nbd-server` en un nodo y `nbd-client` en dos. OCFS2 sobre el block device.
4. Lab 2 — sobre disco shareable VirtualBox: marcar el disco virtual como "shareable" y bootear dos VMs que vean el mismo `/dev/sdX`.
5. Configuración OCFS2: `o2cb` cluster stack, `cluster.conf`, `mkfs.ocfs2`, `mount`.
6. La prueba: escribir desde uno, leer desde el otro, verificar consistencia.
7. Cuándo usar OCFS2 y cuándo no — vs NFS, vs Ceph, vs GlusterFS.
8. Cierre.

**Bibliografía:**
- Repo del POC: [CesarBallardini/global-filesystem-lab](https://github.com/CesarBallardini/global-filesystem-lab).
- [OCFS2 user's guide — Oracle](https://docs.oracle.com/cd/E37670_01/E37355/html/ol_about_ocfs2.html).
- [Linux kernel OCFS2 docs](https://www.kernel.org/doc/Documentation/filesystems/ocfs2.txt).
- [GFS2 — Red Hat docs](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_gfs2_file_systems/index).
- [NBD — Network Block Device](https://nbd.sourceforge.io/).

**Imágenes:**
- _Crear_: diagrama side-by-side: NFS vs OCFS2 (~30 min).
- _Crear_: ASCII de los dos labs (~30 min).

**Tags propuestos:** `['OCFS2', 'cluster filesystem', 'NBD', 'VirtualBox', 'Oracle', 'Vagrant']`

**Estado actual:** **complete-poc** para los 2 labs.

