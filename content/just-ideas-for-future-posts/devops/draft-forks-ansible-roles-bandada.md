### G-33 — La bandada de roles Ansible que forkeé para estudiar (locales, gnu-cobol, packer-templates, ...)

- **Archivo seed:** colección — `github.com/CesarBallardini/ansible-locales` (fork, Feb 2020) + `github.com/CesarBallardini/ansible-role-gnu-cobol` (fork, Jul 2022) + `github.com/CesarBallardini/packer-templates` (fork, Sep 2016) y otros roles forkeados sueltos
- **Slug propuesto:** `forks-ansible-roles-bandada`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-forks-ansible-roles-bandada/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-01]] (roles/profiles), [[E-12]] (Vagrant + Ansible pattern)
- **Idioma:** es
- **Madurez:** **forks sueltos** — estudios breves, ninguno proyecto en serio
- **Length target:** short (800-1200 palabras)

**Concepto:** en mi GitHub hay una bandada de Ansible roles forkeados "para leer": `ansible-locales`, `ansible-role-gnu-cobol`, `packer-templates` y otros. Ninguno es un proyecto propio — son estudios breves. El post es un catálogo honesto de "qué forkeé para aprender, qué aprendí, y por qué ninguno se convirtió en proyecto". Es un meta-post sobre el hábito de forkear repos como método de estudio.

**Hook:** "mi GitHub tiene 25 forks de roles Ansible que nunca se convirtieron en proyecto. No es acumulación. Es método: cuando quiero entender cómo se resuelve un problema puntual (por ejemplo, cómo se setean locales en Debian headless sin prompt), busco un role existente, lo forkeo, lo leo, lo pruebo, y si aprendí lo que quería, el fork queda como archivo. El post es el catálogo y la defensa del método."

**Outline:**
1. La defensa del forkeo-como-estudio: leer código ajeno es la manera más rápida de aprender un patrón.
2. `ansible-locales`: qué aprendí sobre `locale-gen` y `update-locale`, y por qué se equivoca todo el mundo.
3. `ansible-role-gnu-cobol`: cómo instalar GnuCOBOL desde source con Ansible, las trampas.
4. `packer-templates`: qué convenciones se usan en los templates Packer de la comunidad.
5. La regla honesta: un fork estudio ≠ un proyecto productivo. Si no tenés caso de uso, no lo uses en producción.
6. Cierre: la lista completa de forks Ansible en mi GitHub, con una línea de "qué aprendí de cada uno".

**Bibliografía:**
- [Ansible Galaxy](https://galaxy.ansible.com/) — la tienda de roles comunitarios.
- [DebOps](https://docs.debops.org/) — proyecto que usa el patrón roles/profiles/components.

**Imágenes:**
- _Crear_: tabla de los forks + 1 línea de "qué aprendí" (~45 min).

**Tags propuestos:** `['Ansible', 'forks', 'aprendizaje', 'roles', 'estudio']`

**Estado actual:** **catálogo abierto**, el post se completa enumerando forks.

