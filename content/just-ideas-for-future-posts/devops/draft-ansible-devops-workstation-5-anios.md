### G-08 — `ansible-devops-workstation`: 5 años de evolución de mi estación de trabajo como código (FLAGSHIP)

- **Archivo seed (repo POC):** [github.com/CesarBallardini/ansible-devops-workstation](https://github.com/CesarBallardini/ansible-devops-workstation) — Ruby, 2 stars, último push 2026-02-17
- **Slug propuesto:** `ansible-devops-workstation-5-anios`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-ansible-devops-workstation-5-anios/index.md`
- **Serie:** G — flagship operacional + memoir
- **Cross-links:** lleva a [[E-12]] (el patrón Vagrant+Ansible), [[G-01]] (roles/profiles), [[G-09]] (localenv-* family), [[K-02]] (laboratorios docentes); cruza con [[A1-11]] (instala Pharo), [[A2-07]] (instala Racket), [[A1-09]] (instala GnuCOBOL)
- **Idioma:** es
- **Madurez:** **production-ish** — playbook activo, con CI, perfiles selectivos por uso, soporta Ubuntu 22.04/24.04/26.04 y Debian 13/14
- **Length target:** long (2500-3500 palabras) — flagship

**Concepto:** desde hace cinco años mantengo `ansible-devops-workstation`, un suite de playbooks que provisiona una estación de trabajo de desarrollador con todo lo que necesito instalado, configurado y actualizado: Chrome, LibreOffice, editores e IDEs (Atom, IntelliJ, VSCode, Netbeans, Sublime 3, WebStorm), toolchain DevOps (Docker, Terraform/Terragrunt, Vagrant, VirtualBox, Packer, vmWare WS, GOVC), y herramientas específicas de la materia que enseño (SWI-Prolog, Racket, Pharo Smalltalk). Funciona con perfiles selectivos en `vars/tool_profiles.yml` para no instalar todo en cada máquina. Es probablemente el repo más útil que tengo y el que más he refactorizado a lo largo del tiempo. El post cuenta la evolución, las decisiones que cambiaron, las que no, y por qué un playbook personal puede ser tu activo más valioso.

**Hook:** "tengo un playbook de Ansible que arranca con una Ubuntu o Debian limpia, y al final tengo *todo* configurado: navegador, editores, lenguajes para enseñar, toolchain DevOps. Lo escribí hace 5 años, lo refactoré probablemente 50 veces, y hoy es lo primero que corro cuando pongo una notebook nueva. El post cuenta la evolución, las cosas que aprendí, y por qué un playbook personal es la mejor inversión de tiempo en infraestructura que vas a hacer."

**Outline:**
1. La epifanía: el día en que cambié de notebook por décima vez y dije "no más instalación manual".
2. La estructura del playbook: roles atómicos por herramienta, perfiles que componen roles, un master playbook que aplica el perfil deseado.
3. Los perfiles: `dev-frontend`, `dev-backend`, `dev-paradigmas` (clase), `dev-mainframe`, etc. El criterio para crear un perfil nuevo.
4. Las tres categorías de roles:
   - **Software de oficina/personal**: Chrome, LibreOffice, Slack, Telegram, etc.
   - **DevOps toolchain**: Docker, Terraform, Vagrant, VirtualBox, kubectl, helm, Packer.
   - **Lenguajes / IDEs / específicos de docencia**: SWI-Prolog, Racket, Pharo, GnuCOBOL, IntelliJ, VSCode.
5. El CI: por qué tengo CI sobre un playbook personal (para detectar cuándo upstream rompe los repos APT).
6. Las cosas que cambiaron en 5 años: agregué/saqué editores (Atom murió, Sublime perdió cuota, VSCode conquistó), agregué Pharo cuando empecé a enseñarlo, saqué Vmware WS cuando dejé de pagarlo.
7. Las cosas que no cambiaron: el patrón roles/perfiles, el uso de tags Ansible para selección granular, el uso de `become: true` con `become_method: sudo`.
8. Lo que aprendí sobre Ansible escribiendo esto: las trampas de los repos APT con keys deprecadas, los paquetes snap (que evito casi siempre), la diferencia entre `ansible.builtin.package` y `ansible.builtin.apt`.
9. La conexión con [[G-01]] (roles/profiles) y [[E-12]] (el método).
10. Cierre: el repo está abierto, los perfiles son genéricos, podés forkearlo y empezar tu propia versión.

**Bibliografía:**
- Repo del POC: [CesarBallardini/ansible-devops-workstation](https://github.com/CesarBallardini/ansible-devops-workstation).
- [Ansible docs](https://docs.ansible.com/).
- [Jeff Geerling, *Ansible for DevOps*, Leanpub 2024](https://www.ansiblefordevops.com/).
- [Ansible Galaxy](https://galaxy.ansible.com/) — para roles compartidos.
- [Craig Dunn, *Designing Puppet — Roles and Profiles*, 2012](https://www.craigdunn.org/2012/05/239/) — el origen del patrón roles/profiles que uso aquí.
- [Mitchell Hashimoto, *Vagrant: Up and Running*, O'Reilly 2013](https://www.oreilly.com/library/view/vagrant-up-and/9781449336103/).
- [Software Engineering SE — Puppet roles/profiles in Ansible](https://softwareengineering.stackexchange.com/questions/324705/what-is-the-equivalent-of-puppets-roles-profiles-pattern-in-ansible).
- [Ansible best practices — official](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html).
- Cross-links a todos los posts donde aparece como herramienta: [[E-12]], [[G-01]], [[K-02]], [[A1-11]], [[A2-07]], [[A1-09]].

**Imágenes:**
- _Crear_: diagrama del repo: roles → profiles → playbooks → perfiles → master (~1 hora).
- _Crear_: tabla de los 5 años de evolución: qué entró, qué salió, qué se mantuvo (~45 min).
- _Crear_: screenshot del CI corriendo verde sobre Ubuntu 24.04 (~10 min).

**Tags propuestos:** `['Ansible', 'devops', 'workstation', 'playbook', 'memoir', 'roles', 'profiles', 'devenv']`

**Estado actual:** **production-ish** y mantenido. Es uno de los posts más fáciles de defender por la cantidad de evidencia detrás, y al mismo tiempo el más *generoso* — porque entrega un patrón directamente reusable.

