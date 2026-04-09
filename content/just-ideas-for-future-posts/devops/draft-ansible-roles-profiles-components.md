### G-01 — Components, roles y profiles en Ansible (el patrón de Puppet bien aplicado)

- **Archivo seed:** `sysadmin/draft-componets-roles-profiles-usando-ansible.md` (318 líneas, con prosa, citas y un Q&A interno; el más maduro de toda la serie G)
- **Slug propuesto:** `ansible-roles-profiles-components`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-ansible-roles-profiles-components/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-02]] (infraestructura determinística), [[C-02]] (Hickey: simple vs easy aplicado a IaC), [[G-04]] (registro de incidencias para los runs de Ansible), [[I-04]] (MerLinux — la historia vivida de donde decanté este patrón, con la trilogía bash → Puppet → Ansible)
- **Idioma:** es
- **Madurez:** **near-complete** — el seed tiene la discusión completa entre dos personas, la cita de StackExchange, los links a Craig Dunn y al blog que originó el patrón. Falta estructurar y rescribir como post de blog.
- **Length target:** long (2500-3500 palabras) — es uno de los anclas operacionales del blog

**Concepto:** el patrón *components / profiles / roles* viene del mundo Puppet (Craig Dunn, 2012) y resuelve un problema real: cómo dejar de tener inventarios de Ansible que crecen sin estructura, donde cada server termina siendo un copy-paste del anterior con tres cambios. La traducción a Ansible no es obvia porque "role" en Puppet ≠ "role" en Ansible. El post explica los tres niveles, propone una convención de nombres, y muestra cómo modelar correctamente "n aplicaciones contra m servidores".

**Hook:** "tu inventario de Ansible tiene 30 hosts y 80 roles, y cada host tiene su propia variante porque *este* webserver necesita un módulo extra y *este otro* tiene una versión vieja. Eso no es un inventario, es un cementerio. El patrón roles/profiles/components, traducido del mundo Puppet, te saca de ese pozo en una semana de refactor."

**Outline:**
1. El problema: cómo crece mal un repo de Ansible — la deuda de "playbook por servidor".
2. La presentación de Craig Dunn (2012, Puppet) — el origen del patrón. Por qué no es obvio que sirve también para Ansible.
3. Los tres niveles, traducidos al vocabulario de Ansible:
   - **Component** (rol Ansible) — instala y configura *un* paquete genérico (`component-apache`, `component-postgresql`, `component-nginx`). Sin opinión.
   - **Profile** (rol Ansible que depende de components) — implementa *un perfil técnico* (`profile-webserver`, `profile-database-cluster`). Combina components + tiene opinión.
   - **Role** (rol Ansible que depende de profiles) — implementa *un rol de negocio* (`role-portal-clientes`, `role-erp-produccion`). Combina profiles + variables específicas del proyecto.
4. La convención de nombres: por qué `component-`, `profile-`, `role-` como prefijos vale la pena, aunque sea fea.
5. Donde van las variables: `defaults/main.yml` para parámetros del component, `vars/main.yml` para defaults funcionales, group_vars/host_vars para overrides.
6. El Q&A real (del seed): ¿qué pasa con `profile-database` cuando puede ser MySQL o Oracle? Respuesta: dos profiles distintos, no uno con un switch. Justificación.
7. La modelización n×m (n aplicaciones × m servidores) — el ejemplo que más confunde a la gente. Mostrar la solución concreta.
8. Cierre: el repo template que armé y por qué este patrón cambió cómo escribo IaC.

**Bibliografía:**
- [Craig Dunn, *Designing Puppet — Roles and Profiles*, 2012](https://www.craigdunn.org/2012/05/239/) — el post fundacional del patrón.
- [Puppet Labs, *Roles Talk*, slideshare](https://www.slideshare.net/PuppetLabs/roles-talk) — diapos del seed original.
- [PuppetConf — Designing Puppet Roles/Profiles, YouTube](https://www.youtube.com/watch?v=ZpHtOnlSGNY).
- [Software Engineering Stack Exchange — *What is the equivalent of Puppet's roles/profiles pattern in Ansible?*](https://softwareengineering.stackexchange.com/questions/324705/what-is-the-equivalent-of-puppets-roles-profiles-pattern-in-ansible) — la respuesta que aterriza el patrón.
- [Ansible — Roles documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html).
- [Ansible — meta/main.yml para dependencies](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#using-role-dependencies).
- [DebOps — DevOps en Debian](https://docs.debops.org/) — el proyecto que usa este patrón en serio.
- [Jeff Geerling, *Ansible for DevOps*, Leanpub 2024](https://www.ansiblefordevops.com/) — referencia operacional moderna.
- [Martin Fowler, *Infrastructure as Code*](https://martinfowler.com/bliki/InfrastructureAsCode.html) — el bliki que pone vocabulario.

**Imágenes:**
- _Crear_: diagrama de los tres niveles (component → profile → role) con flechas de dependencia y un ejemplo concreto en cada caja (~1 hora — esto es el centro didáctico).
- _Crear_: esquema "antes / después" del repo de Ansible — un cementerio de playbooks vs un árbol limpio (~30 min).
- _Crear_: tabla traducción Puppet ↔ Ansible (~20 min).

**Tags propuestos:** `['Ansible', 'Puppet', 'roles', 'profiles', 'components', 'IaC', 'patterns']`

**Estado actual:** **near-complete** — el seed contiene 318 líneas con la conversación original entre dos personas, citas de StackExchange completas, links de Craig Dunn y Puppet Labs, y la mitad de las preguntas operativas ya respondidas. El post se puede publicar con 2-3 sesiones de redacción.

