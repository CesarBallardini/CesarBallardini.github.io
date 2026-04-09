### G-29 — OCS Inventory Agent: inventario automático de hosts con Ansible

- **Archivo seed:** `github.com/CesarBallardini/Ansible-Role-For-UnixAgent` (fork, Apache 2.0, Jun 2021)
- **Slug propuesto:** `ocs-inventory-agent-ansible`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-ocs-inventory-agent-ansible/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-01]] (Ansible roles/profiles), [[G-04]] (Trac: otro tipo de registro)
- **Idioma:** es
- **Madurez:** fork del role con modificaciones menores
- **Length target:** short (700-1200 palabras)

**Concepto:** OCS Inventory NG es una herramienta open source para inventario automático de máquinas (hardware, software instalado, licencias, cambios). Un agente corre en cada host, reporta periódicamente a un servidor central. Clásico, no fashion, útil en empresa chica-mediana que necesita "saber qué tiene". El role Ansible instala el agent en hosts Unix. El post explica el caso de uso, la comparación con alternativas modernas (Snipe-IT, GLPI), y por qué OCS sigue vivo en 2026 para el nicho de "inventario honesto en LAN".

**Hook:** "tu empresa tiene 40 servidores y 300 escritorios. No sabés qué tienen instalado, qué versión, qué licencias. OCS Inventory te da ese dato sin pedir nada a nadie — el agent lo recolecta solo. Es 2008, sigue siendo 2026, y sigue funcionando."

**Outline:**
1. Qué es OCS Inventory NG y por qué nació.
2. El agente vs el server: arquitectura.
3. El role Ansible para el agent en Linux/Unix.
4. Las alternativas: GLPI (primo legal), Snipe-IT (asset management), Fleet (MDM moderno).
5. Cuándo OCS sigue siendo la elección correcta (LAN, on-prem, sin SaaS).
6. Cierre: el role está listo.

**Bibliografía:**
- [OCS Inventory NG — sitio oficial](https://ocsinventory-ng.org/).
- [GLPI project](https://glpi-project.org/).
- [Snipe-IT](https://snipeitapp.com/).

**Imágenes:**
- _Crear_: diagrama agent → server → dashboard (~30 min).

**Tags propuestos:** `['OCS Inventory', 'asset management', 'Ansible', 'sysadmin', 'inventory']`

**Estado actual:** fork funcional, post corto y práctico.

