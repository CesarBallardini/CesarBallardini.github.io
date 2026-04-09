### E-12 — El patrón Vagrant + Ansible: mi método para aprender tecnologías nuevas

- **Archivo seed (repo POC):** *no es un repo único — es el patrón observable en ~25 de mis 40 repos públicos*. Ejemplos representativos: [GnuCOBOL-lab](https://github.com/CesarBallardini/GnuCOBOL-lab), [programacion-drracket](https://github.com/CesarBallardini/programacion-drracket), [kl1c](https://github.com/CesarBallardini/kl1c), [localenv-python](https://github.com/CesarBallardini/localenv-python), [mvs-on-hercules](https://github.com/CesarBallardini/mvs-on-hercules), [mysql-backup](https://github.com/CesarBallardini/mysql-backup), [ansible-devops-workstation](https://github.com/CesarBallardini/ansible-devops-workstation).
- **Slug propuesto:** `mi-metodo-para-aprender-vagrant-ansible`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mi-metodo-para-aprender-vagrant-ansible/index.md`
- **Serie:** E (memoir + meta-pattern) — meta-post que ata juntas casi toda la serie G y varias de A1, A2 y H
- **Cross-links:** lleva a (literalmente) [[A1-08]] [[A1-09]] [[A2-06]] [[A2-07]] [[G-08]] [[G-09]] [[G-10]] [[G-11]] [[G-12]] [[G-13]] [[G-14]] [[G-15]] [[G-16]] [[G-17]] [[G-18]] [[G-19]] [[H-10]] [[H-11]] [[I-04]] — todos los posts cuyo POC sigue este patrón
- **Idioma:** es
- **Madurez:** seed observado (no hay un repo "del patrón", pero el patrón está vivo en 25+ repos)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** desde hace muchos años, cada vez que quiero aprender una tecnología nueva — un lenguaje, una base de datos, una herramienta de infraestructura — sigo el mismo procedimiento: armo una VM con Vagrant (Virtualbox o Docker como backend), la provisiono con un playbook de Ansible que instala *exactamente* la versión que quiero estudiar, escribo un README que explica qué problema resuelve, y subo todo a un repo de GitHub. Después uso ese repo como "mi cuaderno de laboratorio" para esa tecnología. La consecuencia: tengo más de 25 repos públicos que comparten el mismo esqueleto. El post no es sobre Vagrant ni Ansible — es sobre *por qué adopté este patrón* y por qué creo que es la mejor manera de aprender tecnología técnica seria sin contaminar tu máquina anfitriona ni perderte en setups frágiles.

**Hook:** "tengo más de 25 repos públicos en GitHub que tienen exactamente la misma estructura: un Vagrantfile, una carpeta `provision/` con un playbook de Ansible, un README que dice 'cloná y corré `vagrant up`'. No es coincidencia. Es mi método para aprender. Cuando aprendí KL1, fue así. Cuando aprendí GnuCOBOL, fue así. Cuando aprendí Pharo, fue así. El post explica por qué."

**Outline:**
1. La fricción que me cansé de pagar: cada nueva tecnología tiene su propia receta de instalación, sus dependencias rotas, sus versiones que se pelean con las que ya tengo, sus archivos de config en `~/.config/` que se cruzan con otras herramientas.
2. La epifanía: *no instalo nada en mi máquina*. Todo va en una VM dedicada, descartable, reproducible.
3. Vagrant como wrapper: por qué `vagrant up` es la abstracción correcta. La elección entre Virtualbox y Docker como backend.
4. Ansible como provisión: por qué *no* uso scripts bash para la instalación. La idempotencia, la legibilidad, la reusabilidad.
5. La estructura común de mis repos:
   - `Vagrantfile` en la raíz.
   - `provision/playbook.yml` con los roles que necesita la VM.
   - `provision/roles/<algo>/` con los roles específicos.
   - `README.md` con el "qué resuelve esto".
   - opcionalmente: subdirectorios con material didáctico (capítulos, ejercicios, tests).
6. El boilerplate que voy reciclando: las 80 líneas de `Vagrantfile` que comparten casi todos mis repos. Mostrar el archivo.
7. Las trampas que descubrí en el camino: el problema de pyenv en el controlador Ansible, los abstract sockets de X11 para correr GUIs, los ports forwarded vs bridged, la diferencia de filesystem performance Windows host vs WSL2 vs Linux nativo.
8. Por qué este método sobrevive a la moda devops: porque la *idea* (entorno aislado, reproducible, declarativo, descartable) es independiente de la herramienta. Mañana lo haré con Devbox o Nix; el patrón será el mismo.
9. Cierre: si querés copiar el método, mi `ansible-devops-workstation` ([[G-08]]) es el ejemplo más completo.

**Bibliografía:**
- [Vagrant docs](https://developer.hashicorp.com/vagrant) — la herramienta central.
- [Ansible docs](https://docs.ansible.com/) — la provisión.
- [Mitchell Hashimoto, *Vagrant: Up and Running*, O'Reilly 2013](https://www.oreilly.com/library/view/vagrant-up-and/9781449336103/) — el libro del creador.
- [Jeff Geerling, *Ansible for DevOps*, Leanpub 2024](https://www.ansiblefordevops.com/) — el libro de referencia.
- [Devbox](https://www.jetify.com/devbox) — la nueva onda de "dev environments as code", usa Nix por debajo.
- [Nix flakes](https://nix.dev/concepts/flakes.html) — la alternativa moderna que estoy mirando.
- [Docker docs](https://docs.docker.com/) — el otro backend posible.
- Cross-links a todos los repos POC que citan el patrón.

**Imágenes:**
- _Crear_: diagrama del patrón: host → Vagrant → VM/container → Ansible → tecnología bajo estudio (~45 min).
- _Crear_: tabla con los 25 repos que siguen el patrón, ordenados por tecnología (~30 min).
- _Crear_: el `Vagrantfile` template en una caja (~15 min).

**Tags propuestos:** `['Vagrant', 'Ansible', 'aprendizaje', 'metodo', 'memoir', 'devenv', 'reproducibilidad']`

**Estado actual:** patrón observable en muchísimos repos públicos; el post sale natural sentándose una tarde y enumerando lo que ya hice.

