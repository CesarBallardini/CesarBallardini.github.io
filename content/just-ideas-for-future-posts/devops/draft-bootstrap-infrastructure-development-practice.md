### G-32 — infrastructure-development: el repo meta sobre cómo se bootea una práctica de infra

- **Archivo seed:** `github.com/CesarBallardini/infrastructure-development` (own, Aug 2018)
- **Slug propuesto:** `bootstrap-infrastructure-development-practice`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-bootstrap-infrastructure-development-practice/index.md`
- **Serie:** G — meta-post
- **Cross-links:** depende de [[G-02]] (infra determinística); lleva a [[G-08]] (devops workstation), [[G-01]] (roles/profiles)
- **Idioma:** es
- **Madurez:** **incompleto** — repo propio de 2018, más enunciado que ejecución
- **Length target:** medium (1500-2000 palabras)

**Concepto:** el repo `infrastructure-development` es un meta-repo que yo armé en 2018 para documentar *cómo se bootea una práctica de infrastructure development* en una empresa chica: qué herramientas, qué convenciones, qué workflow, qué roles mínimos, qué pipeline. Nunca lo terminé. El post es una versión actualizada y honesta de ese documento en 2026: las herramientas cambiaron, los principios no.

**Hook:** "en 2018 armé un repo llamado *infrastructure-development* con la idea de escribir 'el librito que le daría a una empresa chica que arranca a hacer devops'. Lo dejé a medias. Ocho años después, la mayoría de los títulos de capítulo siguen vigentes; las herramientas cambiaron todas. El post es la reescritura de ese librito en 2026, con 8 años de experiencia extra detrás."

**Outline:**
1. La lista de capítulos del repo original (qué iba a cubrir, en orden).
2. Para cada capítulo: la herramienta 2018 vs la herramienta 2026.
3. Qué principios sobrevivieron intactos: IaC, versionar todo, revisión por pares, pipeline reproducible, logs centralizados, secrets bien.
4. Qué ha cambiado fundamentalmente: el rol del container, el rol de kubernetes (ver [[G-22]]), la aparición de LLMs en el loop.
5. Cierre: el librito que le daría a una empresa chica en 2026.

**Bibliografía:**
- [Nicole Forsgren, Jez Humble & Gene Kim, *Accelerate*, IT Revolution 2018](https://itrevolution.com/product/accelerate/).
- [Gene Kim, Kevin Behr & George Spafford, *The Phoenix Project*, IT Revolution 2013](https://itrevolution.com/product/the-phoenix-project/).
- [Mike Nygard, *Release It!*, 2nd ed Pragmatic 2018](https://pragprog.com/titles/mnee2/release-it-second-edition/).
- [Kief Morris, *Infrastructure as Code*, O'Reilly 2020](https://www.oreilly.com/library/view/infrastructure-as-code/9781098114664/).

**Imágenes:**
- _Crear_: tabla comparativa 2018 vs 2026 de herramientas por capítulo (~1 hora).

**Tags propuestos:** `['devops', 'infrastructure', 'bootstrap', 'meta', 'memoir', 'IaC']`

**Estado actual:** **incompleto** — repo propio con el skeleton del librito; el post es la reescritura actualizada.

