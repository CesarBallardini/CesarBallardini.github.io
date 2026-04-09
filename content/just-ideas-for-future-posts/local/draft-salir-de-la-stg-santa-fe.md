### I-05 — Salir de la STG: memoir de un técnico que renunció a un cargo público provincial

- **Archivo seed:** `misc/draft-salir-de-stg.md` (vacío — el contenido vive en la memoria del autor)
- **Slug propuesto:** `salir-de-la-stg-santa-fe`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-salir-de-la-stg-santa-fe/index.md`
- **Serie:** I — encaja por el ángulo "memoria del cómputo en estas latitudes" (administración pública provincial argentina)
- **Cross-links:** lleva a [[E-01]] (FOSS journey, contexto previo), [[I-01]] (LUGLi, comunidad técnica del litoral), [[G-01]] (Ansible roles/profiles — patrones que se podían aplicar adentro), [[H-07]] (migración legacy en otra repartición pública); cruza tematicamente con [[C-01]] (oxímoron — la "ingeniería" en el Estado)
- **Idioma:** es
- **Madurez:** seed vacío + clarificación del concepto del autor (2026-04-08)
- **Length target:** medium (1500-2500 palabras) — es un memoir, el largo se ajusta a la honestidad emocional del relato

**Concepto:** la STG (Secretaría de Tecnologías para la Gestión) es una repartición del gobierno de la provincia de Santa Fe encargada de las decisiones técnicas y la infraestructura informática del Estado provincial. En algún momento trabajé ahí, en algún momento renuncié, y este post es el memoir honesto de qué se hace y qué no se hace en un cargo de tecnología en la administración pública provincial argentina, contado desde adentro y desde la salida.

**Hook:** "trabajé en la Secretaría de Tecnologías para la Gestión del gobierno de Santa Fe. En algún momento renuncié. Este post no es una venganza ni una denuncia — es lo opuesto: es la lista honesta de lo que aprendí sobre la *posibilidad real* de hacer ingeniería en serio dentro del Estado provincial argentino. Hay cosas que sí se pueden. Hay cosas que no. Y la diferencia entre las dos no es ideológica: es estructural, y vale la pena entenderla."

**Outline:**
1. Qué es la STG: la Secretaría de Tecnologías para la Gestión, su rol formal en el organigrama de Santa Fe, qué decide, qué no decide, a quién reporta. Contexto institucional sin nombres propios.
2. Por qué entré: la oportunidad de hacer infraestructura "de verdad" en una escala que no se ve en el sector privado provincial. La curiosidad, el deber cívico, las dos cosas honestamente mezcladas.
3. Lo que sí se pudo hacer: los proyectos concretos que dejaron huella positiva. (Listar sin entrar en detalles sensibles — los proyectos hablan por sí mismos años después).
4. Lo que no se pudo hacer y por qué: las restricciones estructurales (compras públicas, ciclos políticos, dependencia de proveedores históricos, normativa que envejeció mal). Sin culpar personas — son fricciones del sistema.
5. La cultura técnica del Estado provincial: el contraste entre los técnicos de carrera (los que conocen los sistemas desde hace 20 años) y los que entran y salen con cada gestión. La sabiduría implícita y el costo de no escucharla.
6. La decisión de renunciar: en qué momento, por qué razones, qué fue lo que finalmente inclinó la balanza. Honesto pero sin amargura — la reflexión que se construye con tiempo y distancia.
7. Lo que me llevé: las lecciones técnicas (algunas de las cuales aparecen en [[G-01]], [[G-02]], [[H-07]]), las lecciones humanas, y la convicción de que el Estado provincial argentino *necesita* ingenieros de software con experiencia, aunque el sistema no esté diseñado para retenerlos.
8. La pregunta abierta para el lector: ¿hay manera de que un técnico pueda hacer carrera en el Estado sin que la frustración estructural le coma el oficio? Mi respuesta provisional, sin pretender que sea la única.
9. Cierre: lo que vale la pena que sepan los técnicos jóvenes que están considerando un cargo público. Tres recomendaciones concretas.

**Bibliografía:**
- [Provincia de Santa Fe — Secretaría de Tecnologías para la Gestión](https://www.santafe.gob.ar/) — sitio oficial; verificar URL exacta del organigrama actual antes de publicar (frágil, cambia con cada gestión).
- [Decreto provincial de creación de la STG](https://www.santafe.gob.ar/normativa/) — buscar el decreto original y su normativa.
- [Federico Heinz, *Por qué el Estado debe usar Software Libre*, Vialibre 2003](https://www.vialibre.org.ar/) — el ensayo argentino canónico sobre IT en el Estado.
- [Vía Libre — *Software libre en la administración pública*](https://www.vialibre.org.ar/) — colección de textos sobre el tema, contexto histórico argentino.
- [Beatriz Busaniche y otros, *Argentina Copyleft*, Vía Libre 2010](https://www.vialibre.org.ar/2010/06/05/argentina-copyleft/) — referencia a la cultura técnica libre argentina.
- [Diego Saravia, *Software libre y administración pública*](https://www.cs.unsa.edu.ar/saravia/) — referencia académica argentina, frágil.
- [Tomás Pomar, Cony Sturniolo et al, *Estado abierto en Argentina* — papers en SADIO/JAIIO](https://www.sadio.org.ar/jaiio/) — buscar ediciones recientes.
- [Steven Goodman, *Bureaucracy: What Government Agencies Do and Why They Do It* — James Q. Wilson, Basic Books 1989](https://archive.org/details/bureaucracywhatg00wils) — el libro académico clásico sobre por qué las burocracias funcionan como funcionan; útil para no caer en la trampa "es culpa de los políticos".
- [Tom Loosemore, *Government as a Platform*, GDS UK 2014](https://gds.blog.gov.uk/2014/03/19/we-need-to-talk-about-government-as-a-platform/) — el contraste internacional moderno: lo que se podría hacer si la voluntad estructural existiera.
- [Jennifer Pahlka, *Recoding America*, Metropolitan 2023](https://www.recodingamerica.us/) — el libro de la fundadora de Code for America sobre por qué las reformas de IT en el Estado fracasan, con datos.
- [Schneier on Security — *Government IT* posts](https://www.schneier.com/) — buscar la serie sobre IT pública.

**Imágenes:**
- _Crear_: ninguna obligatoria — es un post ensayístico, vive del texto. Si se quisiera ilustrar, una foto de Rosario o Santa Fe ciudad sin elementos identificables del edificio (~10 min).
- _Opcional_: el organigrama (anonimizado / esquemático) que muestre dónde encajaba la STG en la cadena de decisiones, sin nombres (~30 min). Útil pedagógicamente para que el lector entienda qué clase de cargo era.

**Tags propuestos:** `['memoir', 'STG', 'Santa Fe', 'administracion publica', 'IT en el Estado', 'renuncia', 'historia local']`

**Estado actual:** seed vacío en disco, **concepto clarificado por el autor el 2026-04-08**: la STG es la Secretaría de Tecnologías para la Gestión del gobierno de Santa Fe; el post es un memoir sobre haber trabajado allí y haber renunciado. El contenido sustantivo (proyectos concretos, fechas, las razones honestas de la renuncia) tiene que escribirlo el autor — no se puede inventar. Recomendación: dejar reposar 2-3 borradores antes de publicar; los memoirs sobre cargos públicos se templan mejor con tiempo, y la honestidad necesaria para que el post valga la pena exige distancia emocional.

