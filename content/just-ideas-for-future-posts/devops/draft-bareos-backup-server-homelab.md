### G-28 — Bareos: el backup server enterprise en mi homelab (fork + role)

- **Archivo seed:** `github.com/CesarBallardini/ansible-role-bareos-server` (fork, Apr 2017)
- **Slug propuesto:** `bareos-backup-server-homelab`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-bareos-backup-server-homelab/index.md`
- **Serie:** G
- **Cross-links:** contrasta con [[G-03]] (rdiff-backup + rsync: la opción simple); lleva a [[G-13]] (LXD: donde corre el director)
- **Idioma:** es
- **Madurez:** fork viejo (2017) del role Ansible
- **Length target:** medium (1200-1800 palabras)

**Concepto:** Bareos es un fork moderno de Bacula, el backup server "enterprise" clásico. Arquitectura cliente/servidor: director, storage daemon, file daemon, catalog. Complejo para un homelab, pero la pregunta del post es: ¿cuándo conviene pagar la complejidad de Bareos vs quedarse con la simplicidad de rdiff-backup + rsync ([[G-03]])? Spoiler: casi nunca en homelab; en empresa, cuando necesitás retention policies, multi-host, tape library, compliance.

**Hook:** "Bareos es un backup server enterprise. Arquitectura distribuida, catálogo en Postgres, agentes en cada host. Armar un homelab con Bareos es como comprar un camión para ir a la panadería. Lo hice. El post explica cuándo *sí* conviene la complejidad y cuándo es over-engineering."

**Outline:**
1. Bareos en 3 bullets: fork de Bacula, cliente/servidor, director/sd/fd/catalog.
2. El role Ansible forkeado: setup mínimo del director y el storage daemon.
3. La curva de aprendizaje: archivar vs pool vs job vs schedule vs client. Vocabulario denso.
4. El contraste con [[G-03]]: rdiff-backup hace 80% del trabajo con 5% de la complejidad. Bareos gana cuando hay retention policies formales, multi-host, restore granular por usuario.
5. Mi conclusión personal: en homelab, rdiff-backup. En empresa chica, Bareos si la compliance lo exige. En empresa grande, la pregunta ni se hace.
6. Cierre: el role está viejo (2017) y el post sería más una comparación que un tutorial.

**Bibliografía:**
- [Bareos — sitio oficial](https://www.bareos.com/) y [Bareos docs](https://docs.bareos.org/).
- [Bacula — el original del que viene el fork](https://www.bacula.org/).
- [W Curtis Preston, *Modern Data Protection*, O'Reilly 2021](https://www.oreilly.com/library/view/modern-data-protection/9781492094043/).

**Imágenes:**
- _Crear_: diagrama de la arquitectura director/SD/FD/catalog (~45 min).
- _Crear_: tabla "Bareos vs rdiff-backup / cuándo cada uno" (~20 min).

**Tags propuestos:** `['Bareos', 'Bacula', 'backup', 'Ansible', 'enterprise', 'homelab']`

**Estado actual:** fork viejo, post más honesto como "compararon" que como tutorial.

