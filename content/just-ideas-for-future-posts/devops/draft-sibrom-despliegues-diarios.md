### G-05 — sibrom: despliegues diarios antes de que existiera "continuous deployment"

- **Archivo seed:** `sysadmin/draft-sibrom-despliegues-diarios.md`
- **Slug propuesto:** `sibrom-despliegues-diarios`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-sibrom-despliegues-diarios/index.md`
- **Serie:** G
- **Cross-links:** depende de [[G-02]] (infra determinística — pre-requisito); lleva a [[G-01]] (Ansible: la herramienta moderna del mismo flujo), [[G-04]] (Trac: dónde se registraban los despliegues), [[C-04]] (TDD: el otro loop de feedback rápido)
- **Idioma:** es
- **Madurez:** bare-seed (archivo vacío)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** *sibrom* fue un proyecto donde, antes de que la palabra "continuous deployment" existiera en español, hicimos despliegues diarios en producción. Un equipo chico, una base de datos en evolución constante, un cliente que pedía cambios ayer-para-hoy. El post cuenta cómo era el ciclo (commit → tests → migration → deploy → smoke test → rollback ready), qué herramientas usábamos, y por qué la *cultura* (no las herramientas) fue lo que hizo posible que esto funcionara durante años sin un downtime serio.

**Hook:** "*continuous deployment* es una palabra de 2010. Yo hacía despliegues diarios en sibrom en mucho antes, sin saber que tenía nombre. No teníamos Jenkins, ni Docker, ni feature flags, ni canary releases. Teníamos Subversion, un script de migración cuidadoso, y la disciplina de probar el restore antes del deploy. El post explica cómo y por qué."

**Outline:**
1. Qué era sibrom (descripción funcional sin revelar detalles confidenciales): un sistema de gestión interno con base de datos relacional, cliente web, backend en Python/PHP (verificar fecha exacta).
2. La presión: el cliente quería ver cambios cada día. Negociar "ciclos largos" no era opción.
3. La solución cultural: el equipo aceptó que cada commit que entraba en master era candidato a deploy en menos de 24 horas.
4. La cadena del despliegue:
   - commit en SVN con tests obligatorios verdes.
   - migración versionada (script numerado en el repo).
   - smoke test en staging (que era idéntico a prod por [[G-02]]).
   - deploy con rollback preparado (`rdiff-backup` snapshot inmediatamente antes — ver [[G-03]]).
   - verificación post-deploy.
5. Las técnicas que descubrimos sin saber que ya tenían nombre:
   - **expand/contract migrations** — agregar columnas antes, sacar después; el código vive con ambos esquemas durante un release.
   - **smoke tests automatizados** — un Makefile target que pegaba en 5 endpoints y comparaba con golden output.
   - **dark deploys** — código nuevo en producción pero detrás de un flag de configuración.
6. Los incidentes — los honestos. Dos reales, qué aprendimos, qué cambiamos.
7. Cierre: las herramientas modernas (CI/CD, GitLab pipelines, Argo CD) hacen todo esto más fácil, pero la *parte difícil* sigue siendo la cultura. La cultura no se compra.

**Bibliografía:**
- [Jez Humble & David Farley, *Continuous Delivery*, Addison-Wesley 2010](https://martinfowler.com/books/continuousDelivery.html) — el libro que le puso vocabulario a lo que ya hacíamos.
- [Martin Fowler, *Continuous Delivery*](https://martinfowler.com/bliki/ContinuousDelivery.html) — bliki resumen.
- [Jez Humble, *Continuous Delivery vs Continuous Deployment*](https://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/) — la distinción importante.
- [Pramod Sadalage & Scott Ambler, *Refactoring Databases*, Addison-Wesley 2006](https://databaserefactoring.com/) — el libro que da nombre a expand/contract.
- [Charity Majors, *Test in Production!*, 2018](https://charity.wtf/2018/02/02/test-in-production-yes-you-should/) — el ensayo que defiende la postura.
- [Nicole Forsgren, Jez Humble & Gene Kim, *Accelerate*, IT Revolution 2018](https://itrevolution.com/product/accelerate/) — los datos que prueban que despliegues frecuentes correlacionan con calidad.
- [GitLab CI/CD docs](https://docs.gitlab.com/ee/ci/) — la herramienta moderna que más se acerca a este flujo.

**Imágenes:**
- _Crear_: diagrama de la pipeline (commit → tests → migration → deploy → smoke → verify) con tiempos típicos (~45 min).
- _Crear_: gráfico cultural — "lo que la gente ve" (1 herramienta) vs "lo que realmente importa" (5 prácticas) (~20 min).

**Tags propuestos:** `['CI/CD', 'continuous deployment', 'sibrom', 'Subversion', 'expand contract', 'memoir']`

**Estado actual:** archivo vacío; el material está en notas viejas y en mi memoria. Necesita un par de tardes de reconstrucción del cronograma.

