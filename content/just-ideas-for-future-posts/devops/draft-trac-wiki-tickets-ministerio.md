### G-04 — Trac, wiki y tickets: registro de incidencias en un ministerio público

- **Archivo seed:** `sysadmin/draft-trac-en-ministerio-de-cultura.md` + `sysadmin/draft-como-uso-un-sistema-de-registro-de-incidencias.md` (los dos seeds se combinan en este post)
- **Slug propuesto:** `trac-wiki-tickets-ministerio`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-trac-wiki-tickets-ministerio/index.md`
- **Serie:** G
- **Cross-links:** depende conceptualmente del libro de Limoncelli; lleva a [[G-01]] (Ansible: dónde se registran los runs), [[G-05]] (sibrom: el flujo de despliegue diario que sale de los tickets), [[E-07]] (dbaid: las herramientas internas del mismo proyecto), [[I-04]] (MerLinux — la distro de escritorios del mismo ministerio), [[H-07]] (la migración FoxBase→PostgreSQL del mismo proyecto)
- **Idioma:** es
- **Madurez:** seed-with-hints (dos seeds combinables, uno con la lista del workflow completo)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** Trac (ticket + wiki + browser de SVN integrado) fue, durante años, la mejor herramienta para llevar incidencias y conocimiento operacional en proyectos chicos-medianos. El post cuenta el caso concreto de un ministerio público donde armé el flujo: dev sube código → migración de DBF a PostgreSQL → migración de esquema → deploy → ajuste de parámetros → restart, todo trazado en tickets de Trac, todo documentado en el wiki de Trac, todo ligado al commit en SVN. Y la lección que se llevó hasta hoy: el sistema de tickets es la documentación viva de la infraestructura.

**Hook:** "en el Ministerio de Cultura de la provincia de Santa Fe, hace algunos años, armé un flujo de incidencias en Trac que sobrevivió cambios de gestión. La gente nueva entraba, leía el wiki, miraba los tickets cerrados de los últimos seis meses, y sabía cómo se trabajaba ahí sin que nadie le explicara nada. El post es sobre cómo armé eso y por qué Trac, en 2026, todavía es una respuesta razonable para proyectos donde Jira es overkill."

**Outline:**
1. El contexto: ministerio público, equipo chico, sistema legacy en FoxBase migrándose a PostgreSQL.
2. Por qué Trac y no Jira / Redmine / GitLab Issues. La respuesta de 2010 y la respuesta de 2026 son distintas.
3. Las cuatro piezas integradas en Trac:
   - Tickets (incidencias + tareas + bugs).
   - Wiki (procedimientos, glosario, runbooks).
   - Browser de SVN (commits enlazados a tickets por sintaxis `refs #123`).
   - Timeline (la actividad consolidada).
4. El flujo del proyecto, paso por paso:
   - dev sube código → SVN commit con `refs #N`.
   - migración DBF → PG (script versionado, ticket aparte).
   - migración de esquema vieja → nueva (otro ticket).
   - deploy de código (ticket de release).
   - set de parámetros (subticket).
   - restart con verificación (subticket de cierre).
5. Tom Limoncelli, *Time Management for System Administrators* (2005) — el libro que articula la idea de "el ticket *es* tu memoria".
6. Lo que aprendí: el sistema de tickets sólo funciona si *todos* lo usan. La regla es uno: ningún cambio en producción sin ticket, ni siquiera "sólo es 5 minutos".
7. Cierre: cuándo elegir Trac hoy (proyectos chicos, equipos sin DevOps, infra Python instalable en una VM) y cuándo no (CI/CD heavy, integraciones modernas).

**Bibliografía:**
- [Trac — sitio oficial](https://trac.edgewall.org/) — sigue vivo, con releases recientes.
- [Tom Limoncelli, *Time Management for System Administrators*, O'Reilly 2005](https://www.oreilly.com/library/view/time-management-for/0596007833/) — el libro fundacional del seed.
- [Reddit — *Is Time Management for System Administrators worth reading?* (2017)](https://www.reddit.com/r/sysadmin/comments/5lsg4h/is_time_management_for_system_administrators/) — discusión de la comunidad.
- [Tom Limoncelli, Strata Chalup & Christina Hogan, *The Practice of System and Network Administration*, 3rd ed. 2016](https://www.oreilly.com/library/view/the-practice-of/9780321919175/).
- [Apache Subversion — sitio oficial](https://subversion.apache.org/) — para los lectores que olvidaron que existió antes de Git.
- [GitLab Issues vs Jira vs Trac — comparison (DevOps Stack Exchange)](https://devops.stackexchange.com/) — buscar comparativas modernas.

**Imágenes:**
- _Crear_: screenshot (anonimizado) de un ticket real del ministerio, mostrando cómo se enlaza con un commit (~30 min).
- _Crear_: diagrama del flujo de los 6 pasos (dev → DBF → esquema → deploy → params → restart) (~45 min).

**Tags propuestos:** `['Trac', 'tickets', 'wiki', 'Subversion', 'Limoncelli', 'sysadmin', 'ministerio']`

**Estado actual:** dos seeds que combinan bien — uno tiene el flujo del ministerio, el otro tiene el ángulo de Limoncelli. Mergear y escribir.

