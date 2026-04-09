### E-14 — Estudios de clean architecture: rentomatic + clean-architecture (el libro que nunca escribí)

- **Archivo seed:** `github.com/CesarBallardini/rentomatic` (fork de la demo Python clean architecture de Leonardo Giordani) + `github.com/CesarBallardini/clean-architecture` (fork del repo de discusión sobre clean architecture para Android/iOS)
- **Slug propuesto:** `clean-architecture-estudios`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-clean-architecture-estudios/index.md`
- **Serie:** E — memoir sobre una idea que estudié con profundidad y nunca apliqué en proyecto real
- **Cross-links:** lleva a [[C-02]] (Hickey simple vs easy — contraste), [[C-03]] (Tidy First — el mismo tipo de disciplina aplicada al código), [[E-10]] (mi pila mental de infra)
- **Idioma:** es
- **Madurez:** dos forks de referencia + material en notas personales
- **Length target:** medium (1500-2000 palabras)

**Concepto:** *Clean Architecture* (Robert C. Martin, 2017) y sus primos (Hexagonal Architecture de Alistair Cockburn, Onion Architecture de Jeffrey Palermo, DDD de Eric Evans) proponen separar la lógica de negocio de los detalles de infraestructura con capas concéntricas. Lo estudié durante años. Hice dos forks didácticos (*rentomatic* en Python, *clean-architecture* para mobile). Nunca lo apliqué en un proyecto real en serio. El post es el memoir honesto de "por qué la idea me sedujo, por qué nunca la apliqué, qué parte sí me sirve hoy".

**Hook:** "estudié clean architecture durante años. Tengo dos repos forkeados como prueba: rentomatic en Python y una discusión para mobile. Nunca la apliqué en un proyecto real. El post no es una venganza — es la pregunta honesta: ¿por qué una idea tan elegante sobre el papel termina siendo tan difícil de sostener en código vivo?"

**Outline:**
1. Qué es clean architecture en 3 bullets: entities → use cases → interface adapters → frameworks & drivers. Las flechas de dependencia apuntan siempre hacia adentro.
2. El enganche: la promesa de código que sobrevive cambios de framework, de DB, de UI. La promesa de tests unitarios rápidos porque no tocan infraestructura.
3. *rentomatic* como ejercicio: la demo de Leonardo Giordani implementa un alquiler de casas siguiendo las capas al pie de la letra. Es hermosa. Leerla es didáctico. Clonarla es un ejercicio.
4. La realidad: en proyectos chicos, las capas son overhead. En proyectos medianos, la disciplina se rompe en la primera semana porque alguien necesita pasar un `request` a un use case "sólo por esta vez". En proyectos grandes, las capas sobreviven pero se convierten en burocracia.
5. La trampa de la ortogonalidad: la teoría promete que cambiar la DB es un drop-in replacement. La práctica muestra que ningún proyecto cambia la DB jamás, y si lo hace, es por razones que atraviesan todas las capas.
6. Lo que sí sobrevive del estudio: *separar intención de mecanismo* como disciplina mental. No como capas con carpetas separadas, sino como el hábito de preguntarse "¿esta función está hablando del dominio o de un framework?".
7. Cierre: la arquitectura más limpia es la que no confunde a quien la lee la primera semana. Para eso no hace falta el libro — hace falta leer el código viejo.

**Bibliografía:**
- [Robert C Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*, Prentice Hall 2017](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/) — el libro canónico.
- [Leonardo Giordani, *Clean Architectures in Python*, Leanpub 2020](https://www.thedigitalcatbooks.com/pycabook-introduction/) — el libro detrás de *rentomatic*.
- [Alistair Cockburn, *Hexagonal Architecture*, 2005](https://alistair.cockburn.us/hexagonal-architecture/) — el original.
- [Jeffrey Palermo, *Onion Architecture*, 2008](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/) — la variante.
- [Eric Evans, *Domain-Driven Design*, Addison-Wesley 2003](https://www.domainlanguage.com/ddd/) — la influencia de fondo.
- [Ben Moseley & Peter Marks, *Out of the Tar Pit*, 2006](http://curtclifton.net/papers/MoseleyMarks06a.pdf) — el contrapunto honesto sobre complejidad.
- [Dan North, *Why Every Element of SOLID is Wrong*, GOTO 2019](https://speakerdeck.com/tastapod/why-every-element-of-solid-is-wrong) — el escéptico serio.

**Imágenes:**
- _Crear_: el clásico diagrama circular de Clean Architecture con las 4 capas + flechas de dependencia (~30 min).
- _Crear_: comparación con un proyecto real de 3 años — dónde sobrevivió la estructura, dónde se rompió (~45 min).

**Tags propuestos:** `['Clean Architecture', 'Robert Martin', 'hexagonal', 'DDD', 'rentomatic', 'memoir', 'arquitectura']`

**Estado actual:** dos forks didácticos en GitHub, material teórico leído, experiencia de "no haberla aplicado" que hace el post honesto. Madurez: concepto claro, falta sentarse a narrar con ejemplos.

