### G-14 — Tu propio registry Docker en casa: Harbor bajo Vagrant

- **Archivo seed (repo POC):** [github.com/CesarBallardini/harbor-registry-server](https://github.com/CesarBallardini/harbor-registry-server) — Shell, último push 2020-02-07
- **Slug propuesto:** `harbor-registry-casero`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-harbor-registry-casero/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-06]] (PG en Docker), [[G-08]]
- **Idioma:** es
- **Madurez:** **complete-poc** para install, TODO para LDAP/OIDC auth
- **Length target:** short (1000-1500 palabras)

**Concepto:** Harbor es un registry Docker corporate-grade, libre, con UI web, RBAC, escaneo de vulnerabilidades y replicación. Mi POC lo levanta sobre una VM Vagrant Debian Buster / Ubuntu 18.04 con un script bash. El post explica por qué tener un registry propio (privacy, ancho de banda, control de versiones de imágenes) y cómo lo armé en una tarde.

**Hook:** "subís imágenes a Docker Hub. Llegás al límite de pulls anónimos. Las imágenes que subís son privadas. Empezás a pensar 'necesito mi propio registry'. Harbor es la respuesta libre y robusta. Acá lo levanto en una VM Vagrant en una hora."

**Outline:**
1. Por qué necesitarías tu propio registry: privacidad, ancho de banda, governance.
2. Las opciones: Docker Hub privado (cuesta), GitLab Container Registry, GitHub Container Registry, JFrog Artifactory, Sonatype Nexus, Harbor.
3. Por qué Harbor: libre, CNCF graduated, RBAC, escaneo de imágenes (Trivy), replicación, web UI.
4. La instalación: bash + Vagrant. Por qué bash y no Ansible (legacy del repo, hoy lo haría con Ansible).
5. El primer push: tag local, login, push.
6. Lo que falta en mi POC: LDAP/OIDC auth.
7. Cierre.

**Bibliografía:**
- Repo del POC: [CesarBallardini/harbor-registry-server](https://github.com/CesarBallardini/harbor-registry-server).
- [Harbor — sitio oficial](https://goharbor.io/).
- [CNCF Harbor project page](https://www.cncf.io/projects/harbor/).
- [Trivy — vulnerability scanner](https://github.com/aquasecurity/trivy).

**Imágenes:**
- _Crear_: screenshot del web UI de Harbor (~10 min).

**Tags propuestos:** `['Harbor', 'Docker', 'registry', 'CNCF', 'Vagrant', 'sysadmin']`

**Estado actual:** **complete-poc** para install.

