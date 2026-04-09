### G-10 — La trampa del `delegate_to: localhost` vs `connection: local` en Ansible cuando el controlador vive en un virtualenv

- **Archivo seed (repo POC):** [github.com/CesarBallardini/localenv-ansible](https://github.com/CesarBallardini/localenv-ansible) — Shell, 1 star, último push 2022-06-23
- **Slug propuesto:** `delegate-to-vs-connection-local-virtualenv`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-delegate-to-vs-connection-local-virtualenv/index.md`
- **Serie:** G — single-concept, advanced
- **Cross-links:** depende de [[G-08]] [[G-09]]; lleva a [[E-04]] (Python env)
- **Idioma:** es
- **Madurez:** **complete-poc** con TODO de "dockerize on Alpine"
- **Length target:** short (800-1200 palabras) — single-concept

**Concepto:** cuando corrés Ansible desde un controlador que vive dentro de un virtualenv Python (que tiene módulos como `pyvmomi`, `proxmoxer`, `boto3` instalados *sólo en ese venv*) y necesitás que Ansible ejecute módulos *contra APIs externas* (VMware vSphere, Proxmox, AWS, etc.), te chocás con una distinción que casi nadie explica bien: `delegate_to: localhost` vs `connection: local`. Las dos cosas suenan iguales. No son. Una respeta tu virtualenv; la otra no. El post explica la diferencia con un ejemplo reproducible y dice cuándo elegir cuál.

**Hook:** "tenés un controlador Ansible en una VM, con un virtualenv Python que tiene `pyvmomi` instalado. Querés correr un módulo de Ansible que llama a vSphere. Y de pronto Ansible te dice 'no module named pyvmomi'. ¿Cómo, si está instalado? Bienvenido a la trampa de `delegate_to: localhost` vs `connection: local`. Acá está la diferencia, en 800 palabras."

**Outline:**
1. El setup: VM controlador con Python venv + módulos instalados, target node es la propia VM (loopback).
2. La sintaxis tentadora: `delegate_to: localhost`. Lo que parece pasar.
3. Lo que *en realidad* pasa: Ansible re-ssh-ea a localhost, lo cual *reactiva el shell* del usuario remoto, *no* el venv en el cual estás corriendo `ansible-playbook`.
4. La sintaxis correcta: `connection: local`. Cómo y cuándo.
5. La trampa adicional: `ansible_python_interpreter` para cuando hasta `connection: local` no alcanza (cuando Ansible eligió Python del sistema y tu venv no es el default de la sesión).
6. El ejemplo reproducible: un playbook chico que falla con `delegate_to` y funciona con `connection: local`.
7. Cierre: la regla operativa que aprendí — *cuando el controlador y el target son la misma máquina y necesitás módulos instalados sólo en el venv del controlador, usá `connection: local` + `ansible_python_interpreter` explícito*.

**Bibliografía:**
- Repo del POC: [CesarBallardini/localenv-ansible](https://github.com/CesarBallardini/localenv-ansible).
- [Ansible docs — `delegate_to`](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_delegation.html).
- [Ansible docs — `connection: local`](https://docs.ansible.com/ansible/latest/inventory_guide/connection_details.html#non-ssh-connection-types).
- [Ansible docs — `ansible_python_interpreter`](https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html).
- [pyvmomi — VMware Python SDK](https://github.com/vmware/pyvmomi).
- [proxmoxer — Proxmox Python SDK](https://github.com/proxmoxer/proxmoxer).

**Imágenes:**
- _Crear_: diagrama de los dos modos (delegate_to vs connection:local) con el venv resaltado (~30 min — central del post).

**Tags propuestos:** `['Ansible', 'Python', 'virtualenv', 'delegate_to', 'connection', 'gotcha']`

**Estado actual:** **POC funcional**, single-concept gem post.

