### G-21 — DMOJ online judge para la materia Paradigmas de Programación: Docker Compose + CSV import + sandbox

- **Archivo seed (repo POC):** [github.com/CesarBallardini/online-judge](https://github.com/CesarBallardini/online-judge) — Python, último push 2026-03-09
- **Slug propuesto:** `dmoj-online-judge-paradigmas`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-dmoj-online-judge-paradigmas/index.md`
- **Serie:** G — production-ish, ángulo docente
- **Cross-links:** cruza con [[A1-09]] (GnuCOBOL-lab), [[A2-07]] (DrRacket), [[A1-11]] (Pharo) — todos lenguajes que la materia toca; lleva a [[E-12]] (patrón Vagrant+Ansible)
- **Idioma:** es
- **Madurez:** **production-ish** — usado en clase real
- **Length target:** medium-long (2000-2800 palabras)

**Concepto:** DMOJ (Don Mills Online Judge) es un *online judge* libre de tipo Codeforces / AtCoder, escrito en Django + Python. Mi POC lo levanta con Docker Compose: MariaDB + Redis + sitio Django + worker Celery + bridge del judge + judge mismo (sandbox privilegiado) + nginx. Tiene un `manage.sh` con comandos lifecycle, importación masiva por CSV de profesores/alumnos/problemas, y está localizado a `America/Argentina/Buenos_Aires`. Lo uso para correr la materia Paradigmas de Programación. El post explica el setup, las decisiones (por qué DMOJ y no Codeforces Polygon, por qué Docker Compose y no k8s), y la realidad operativa de tener tu propio judge.

**Hook:** "querés correr una materia de programación con ejercicios autogestionados, evaluación automática, ranking, y sin pagar Hackerrank o Codeforces ni regalar el código de tus alumnos a una empresa. Solución: tu propio online judge. Hay uno libre que se llama DMOJ. Acá lo levanto con Docker Compose para una clase entera, con importación CSV de alumnos y todo."

**Outline:**
1. Por qué un online judge para Paradigmas: feedback inmediato, evaluación reproducible, ranking que motiva, *no* dependencia de un servicio comercial que un día decide cobrar.
2. DMOJ en 30 segundos: Django + Python, fork del judge de Don Mills CI, usado en olimpíadas reales (CCO Canada, Codeforces lo conoce).
3. La arquitectura: 7 servicios en docker-compose:
   - MariaDB (DB principal).
   - Redis (cache + colas Celery).
   - Site (Django web app).
   - Celery worker (procesa submissions en background).
   - Judge bridge (recibe sandbox results).
   - Judge (sandbox privilegiado, requiere `--privileged` y `cap_add`).
   - nginx (frontal, SSL).
4. La importación CSV: scripts en `manage.sh` para cargar profesores, alumnos, problemas en bulk. *Esto es lo que no viene con DMOJ vanilla y lo agregué yo.*
5. La organización: Paradigmas como "organización", alumnos asignados, profesores con permisos.
6. La integración con la materia: cómo se conecta con `programacion-drracket` ([[A2-07]]), `GnuCOBOL-lab` ([[A1-09]]) y los otros laboratorios.
7. Lo que aprendí operándolo en clase real: el sandbox no es trivial (privilegios, ulimits, timeouts), las submissions Python son lentas porque Python arranca lento.
8. Lo que falta y lo que no haré: alta disponibilidad, escalado horizontal, integración con LMS Moodle.
9. Cierre.

**Bibliografía:**
- Repo del POC: [CesarBallardini/online-judge](https://github.com/CesarBallardini/online-judge).
- [DMOJ — sitio oficial](https://dmoj.ca/).
- [DMOJ en GitHub](https://github.com/DMOJ/online-judge).
- [Don Mills CI history](https://en.wikipedia.org/wiki/Don_Mills_Collegiate_Institute).
- [Codeforces Polygon](https://polygon.codeforces.com/) — la alternativa propietaria.
- [Docker Compose docs](https://docs.docker.com/compose/).
- [Django docs](https://docs.djangoproject.com/).
- [Celery docs](https://docs.celeryq.dev/).

**Imágenes:**
- _Crear_: diagrama de los 7 servicios en docker-compose (~45 min — central).
- _Crear_: screenshot del DMOJ corriendo con la organización Paradigmas y alumnos cargados (~10 min, anonimizado).
- _Crear_: tabla de las decisiones operativas (timeouts, ulimits, capabilities) (~20 min).

**Tags propuestos:** `['DMOJ', 'online judge', 'Docker Compose', 'Django', 'Paradigmas', 'enseñanza', 'sandbox']`

**Estado actual:** **production-ish**, usado en clase. Posts sale natural — el README ya es 80% del material.

