### E-10 — Cómo pienso la infraestructura corporativa: la pila que tengo en la cabeza

- **Archivo seed (repo POC):** [github.com/CesarBallardini/infrastructure-development](https://github.com/CesarBallardini/infrastructure-development) — sin lenguaje primario, último push 2018-08-30
- **Slug propuesto:** `como-pienso-la-infraestructura`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-como-pienso-la-infraestructura/index.md`
- **Serie:** E (memoir / mi manera de pensar) — fuerte cruce con [[C-02]] (Hickey simple vs easy aplicado a infra) y con toda la serie [[G]]
- **Cross-links:** lleva a [[G-01]] (roles/profiles) — la materialización del modelo, [[G-02]] (infra determinística), [[C-02]] (Hickey), [[I-04]] (MerLinux: una aplicación concreta de este modelo), [[E-12]] (el patrón Vagrant+Ansible)
- **Idioma:** es
- **Madurez:** **partial-poc** — el repo es un *manifesto / draft* operacional, no código corriendo. Lo que falta es la prosa de blog que lo contextualice y lo actualice a 2026.
- **Length target:** medium-long (2000-3000 palabras) — es un ensayo personal con base operativa

**Concepto:** todo el mundo dice "infraestructura" y nadie está hablando exactamente de lo mismo. En 2018 me senté a escribir mi propia definición operativa: cuáles son los niveles de la pila, qué clase de servicios viven en cada nivel, cómo se bootstrappean (manual primero, automatizado después), y cuándo conviene saltar entre niveles. El draft está en GitHub. El post es la versión adulta de ese draft, ocho años después, con la perspectiva de haberlo aplicado en proyectos reales.

**Hook:** "alguien dice 'tenés que mejorar la infraestructura'. ¿De qué te está hablando? ¿De los servidores? ¿De los procesos? ¿De los roles del equipo? ¿De la nube? ¿Del CI/CD? Cada uno entiende otra cosa. En 2018 me cansé de la confusión y escribí mi propia pila de capas conceptuales. La pongo acá, ocho años después, con las correcciones que haría hoy."

**Outline:**
1. La pregunta filosófica: ¿qué es "infraestructura" para un ingeniero de software, separada del rol del sysadmin? Por qué la palabra es tan vaga.
2. Mi pila de capas:
   - Capa 0 — el hardware o la nube subyacente.
   - Capa 1 — el sistema operativo y su configuración mínima.
   - Capa 2 — los servicios de plataforma (DNS, NTP, identidad, monitoreo, almacenamiento).
   - Capa 3 — los runtimes de aplicación (containers, JVM, Python venvs, etc.).
   - Capa 4 — las aplicaciones del negocio.
   - Capa 5 — los procesos humanos que las operan.
3. Bootstrapping en dos modos: manual (la primera vez, para *entender*) y automatizado (la segunda vez en adelante, para *escalar*). Por qué la primera vez tiene que ser manual.
4. La regla de oro que aprendí: nadie debería empezar por la capa 4 sin haber subido las capas 0-3 con disciplina. Pero todo el mundo lo hace, y por eso fallan los proyectos.
5. Cómo cambió mi modelo entre 2018 y 2026 — la nube *no* eliminó las capas, sólo movió quién las opera.
6. Lo que ya no escribiría igual: la confianza en VirtualBox como pieza central (hoy reemplazado por containers + cloud); la palabra "DevOps" como concepto (hoy diluida).
7. La conexión con [[C-02]] Hickey: cada capa puede ser *simple* o *fácil*, y elegimos mal la mayoría de las veces.
8. Cierre: el draft está en GitHub. Si quieren la versión cruda, ahí está. Si quieren la versión 2026, este post es ella.

**Bibliografía:**
- Repo del POC: [CesarBallardini/infrastructure-development](https://github.com/CesarBallardini/infrastructure-development).
- [Kief Morris, *Infrastructure as Code*, 2nd ed O'Reilly 2020](https://www.oreilly.com/library/view/infrastructure-as-code/9781098114664/) — el libro de referencia.
- [Mark Burgess, *Cfengine* paper LISA 1995](https://www.usenix.org/legacy/publications/library/proceedings/lisa95/full_papers/burgess.pdf) — el ancestro académico.
- [Steve Traugott, *Bootstrapping an Infrastructure*, LISA 1998](http://www.infrastructures.org/papers/bootstrap/bootstrap.html).
- [Tom Limoncelli, Strata Chalup, Christina Hogan, *The Practice of Cloud System Administration*, Addison-Wesley 2014](https://www.oreilly.com/library/view/the-practice-of/9780133478549/).
- [Charity Majors, *Database Reliability Engineering*, O'Reilly 2017](https://www.oreilly.com/library/view/database-reliability-engineering/9781491925935/).
- [[tr-07]] — Hickey *Simple Made Easy*.
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) — el libro libre.

**Imágenes:**
- _Crear_: diagrama de la pila de capas (0-5) con un ejemplo en cada capa (~1 hora — central del post).
- _Crear_: side-by-side de cómo se ve la pila en 2018 vs 2026 (~30 min).

**Tags propuestos:** `['infraestructura', 'arquitectura', 'IaC', 'devops', 'memoir', 'capas']`

**Estado actual:** repo con un draft de manifesto, sin actualizar desde 2018. El post vendría a ser la versión madura del draft.

