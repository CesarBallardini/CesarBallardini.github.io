### G-02 — Infraestructura determinística: golden images, CVS y un Makefile

- **Archivo seed:** `sysadmin/draft-infrastructura-deterministica.md`
- **Slug propuesto:** `infraestructura-deterministica`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-infraestructura-deterministica/index.md`
- **Serie:** G
- **Cross-links:** depende conceptualmente de [[G-01]] (Ansible es la versión moderna del mismo problema); lleva a [[G-05]] (sibrom: cómo se ven los despliegues diarios cuando la infra es determinística), [[H-01]] (legacy: cuando no podés ser determinístico)
- **Idioma:** es
- **Madurez:** seed-with-hints (3 keywords: cvs, golden image, makefile)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** mucho antes de que existiera la palabra "infrastructure as code", algunos hicimos infraestructura determinística con las herramientas que había: CVS para versionar configs, una *golden image* construida con un script reproducible, y un Makefile que orquestaba el deploy. El post argumenta que la *idea* de IaC es vieja, lo que cambió es el vocabulario y la potencia de las herramientas. Entender la versión histórica te hace mejor ingeniero hoy.

**Hook:** "armé infraestructura determinística en 1999. No tenía Ansible, no tenía Docker, no tenía Terraform. Tenía CVS, un script de instalación de Red Hat, y un Makefile. Y funcionaba. La parte loca es que las decisiones técnicas que tomé entonces son indistinguibles de las que toman las herramientas modernas — sólo que escritas a mano."

**Outline:**
1. La definición operativa de "determinístico": dado el mismo input (configs + script), obtenés el mismo output (server) sin intervención manual.
2. La trinidad histórica: CVS + golden image + Makefile.
   - **CVS** — el versionador. Antes del Git universal. Por qué versionar las configs ya cambia todo.
   - **Golden image** — la imagen base reproducible. Construida con kickstart en RH/Fedora, preseed en Debian, JumpStart en Solaris.
   - **Makefile** — el orquestador. `make deploy`, `make rollback`, `make verify`. Tres targets.
3. Por qué esto era ya IaC en sentido estricto, sólo que sin la palabra.
4. Lo que faltaba comparado con el stack moderno: convergencia, idempotencia explícita, manejo de drift, abstracción multi-cloud. Y honestamente — ¿cuántos de esos importan en una empresa de 30 servidores?
5. La lección que se llevó la industria: la herramienta importa menos que la disciplina de "todo en VCS, nada a mano".
6. La trampa moderna: con herramientas más potentes, la gente cree que la disciplina es opcional. No lo es.
7. Cierre: el Makefile que todavía uso (versión 2026) tiene 4 targets más, pero la estructura no cambió.

**Bibliografía:**
- [Mark Burgess, *Cfengine — original paper, 1995*](https://www.usenix.org/legacy/publications/library/proceedings/lisa95/full_papers/burgess.pdf) — el ancestro real de Puppet/Ansible/Chef.
- [Steve Traugott, *Bootstrapping an Infrastructure*, LISA 1998](http://www.infrastructures.org/papers/bootstrap/bootstrap.html) — el otro paper fundacional.
- [Red Hat Kickstart documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/automatically_installing_rhel/index) — la herramienta de golden images de RH.
- [Debian preseed](https://www.debian.org/releases/stable/amd64/apb.en.html) — el equivalente Debian.
- [Wikipedia — CVS (Concurrent Versions System)](https://en.wikipedia.org/wiki/Concurrent_Versions_System).
- [GNU Make manual](https://www.gnu.org/software/make/manual/) — sí, todavía sirve.
- [Martin Fowler, *Phoenix Server*](https://martinfowler.com/bliki/PhoenixServer.html) — el bliki que articula la idea moderna.
- [Kief Morris, *Infrastructure as Code*, O'Reilly 2nd ed. 2020](https://www.oreilly.com/library/view/infrastructure-as-code/9781098114664/) — el libro de referencia actual.

**Imágenes:**
- _Crear_: foto del Makefile real (sanitizado) en una caja — esto le da autenticidad (~10 min).
- _Crear_: línea de tiempo "1999 → 2026" de las herramientas equivalentes en cada época (~30 min).

**Tags propuestos:** `['IaC', 'golden image', 'Makefile', 'CVS', 'kickstart', 'historia']`

**Estado actual:** seed con tres palabras clave; el material está en mi memoria y en backups antiguos.

