### C-11 — Goodhart's Law en software: cuando la métrica se vuelve el objetivo

- **Archivo seed:** _draft-rest.md bucket 6 (cosechado 2026-04-09)_
- **Slug propuesto:** `goodhart-law-en-software`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-goodhart-law-en-software/index.md`
- **Serie:** filosofia
- **Cross-links:** [[C-03]] (Tidy First), [[C-12]] (Forest and Desert), [[C-13]] (anti-productivity)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1800–2200 palabras (ensayo corto de opinión con casos)

**Concepto:** La Ley de Goodhart dice: "cuando una medida se vuelve un objetivo, deja de ser una buena medida". En software se aplica brutalmente: si medís lines of code, los devs escriben más líneas; si medís commits, los devs hacen más commits; si medís bugs cerrados, los devs cierran bugs sin arreglarlos. Kent Beck en su conversación con Abi Noda (DX) abre el debate sobre métricas con esta ley. El post discute Goodhart en software con casos concretos y propuestas de mitigación.

**Hook:** "cuando una medida se vuelve un objetivo, deja de ser una buena medida". Charles Goodhart, 1975. Aplicado a software, Kent Beck dice que esto es "100% verdadero". Acá está cómo te muerde y cómo evitarlo.

**Outline:**

1. **El hook** — la frase, y Beck diciendo que es «100% verdadero». Dos párrafos, sin rodeos.
2. **De dónde sale la ley** — Goodhart 1975, contexto de política monetaria británica; la reformulación de Strathern 1997 (que es, en realidad, la versión que todos citamos). Aclarar la atribución.
3. **Por qué muerde tan fuerte en software** — el trabajo es invisible, y la métrica es lo único visible. Toda métrica de software es un proxy.
4. **El catálogo de mordeduras** — LOC, commits, bugs cerrados, story points, cobertura, tiempo de ciclo. Cada una con su patología.
5. **Las dos mitades de Goodhart** — presión (te optimizan la métrica) y selección (el proxy se rompe solo, sin mala fe). La segunda es la interesante.
6. **La tentación del dashboard** — por qué la organización *quiere* la métrica aunque sepa que miente. Cross-link a [[C-13]].
7. **Mitigaciones honestas** — no medir para evaluar personas; métricas en canasta y no sueltas; medir el freno y no la producción; rotar la métrica; la métrica como pregunta y no como respuesta.
8. **Cierre** — no es una ley que se derrota, es una ley con la que se convive. Bosque y desierto ([[C-12]]).

**Bibliografía:**
- [Charles A. E. Goodhart, *Problems of Monetary Management: The U.K. Experience* (1975)](https://doi.org/10.1007/978-1-349-17295-5_4) — ponencia de 1975 (*Papers in Monetary Economics*, Vol. I, Reserve Bank of Australia, Sydney); reimpresa como cap. 4, pp. 91–121, de *Monetary Theory and Practice: The U.K. Experience*, Macmillan, 1984 (el DOI apunta a esa reimpresión). Formulación original: «Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.» estable.
- Marilyn Strathern, «'Improving ratings': audit in the British University system», *European Review* 5(3):305–321 (1997). DOI canónico (verificado en Crossref): <https://doi.org/10.1002/(sici)1234-981x(199707)5:3%3C305::aid-euro184%3E3.0.co;2-4>. Paywall Cambridge; texto completo libre en [Internet Archive](https://archive.org/details/ImprovingRatingsAuditInTheBritishUniversitySystem). Fuente de la formulación popular: «When a measure becomes a target, it ceases to be a good measure.» estable.
- [Kent Beck × Abi Noda, «Developer Productivity Metrics: Education Necessary», *Software Design: Tidy First?* (29 ene 2025)](https://newsletter.kentbeck.com/p/developer-productivity-metrics-education) — conversación patrocinada por DX. Noda: «Goodhart's Law is 100% true…»; Beck: «It's worse than inaccurate, because people degrade the system to produce the number.» frágil (Substack; sin snapshot en Wayback al 2026-07-16 — conviene archivarlo antes de publicar).
- [Donald T. Campbell, «Assessing the Impact of Planned Social Change», Occasional Paper Series #8 (dic 1976)](https://eric.ed.gov/?id=ED303512) — la Ley de Campbell, pariente cercana de Goodhart. No entró al texto del post; queda como referencia de fondo. estable.
- [«Goodhart's law», Wikipedia](https://en.wikipedia.org/wiki/Goodhart's_law) — panorama y trazado de la atribución Goodhart→Strathern.

**Imágenes:** _a definir_

**Tags propuestos:** `['Goodhart','metricas','productividad','Beck','critica']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le construyó el outline (8 puntos) y se escribió el borrador de prosa completo (~2000 palabras) al final del archivo.

Lo que quedó **escrito y cerrado**: el encuadre de la ley, la distinción entre las dos mitades (presión vs. selección), el catálogo de métricas patológicas de software, la sección de mitigaciones y el cierre. Todo eso es argumentación y no depende de datos externos.

Lo que quedó como **hueco (necesita a César)** — 6 marcadores:

1. Métricas que le impusieron en la STG o en el Ministerio de Cultura de Santa Fe.
2. Métrica que él mismo instaló y que salió mal.
3. Anécdota concreta de bugs cerrados sin arreglar.
4. Postura personal sobre cobertura de tests como objetivo.
5. Si alguna vez le pidieron un dashboard de productividad y qué hizo.
6. Si tiene hoy alguna métrica que sí le sirva, y por qué esa sí.

Lo que quedó como **`[VERIFICAR:]`** — 5 marcadores. Los importantes:

- **La atribución del hook está mal y el borrador lo trabaja explícitamente.** La frase «cuando una medida se vuelve un objetivo, deja de ser una buena medida» no es la formulación de Goodhart 1975 sino la reformulación de Strathern 1997; Goodhart escribió algo más técnico y acotado a agregados monetarios. El Hook del draft se lo atribuye a Goodhart. La prosa convierte ese error en el punto 2 del post (queda mejor así), pero **hay que corregir el Hook o dejarlo como gancho deliberado con la aclaración inmediata**. Decisión pendiente de César.
- Falta chequear la cita textual y la formulación exacta de Goodhart 1975, la de Strathern 1997 (título y publicación), y las palabras exactas de Beck en la entrevista con Abi Noda (el draft dice «100% verdadero» pero no hay transcripción a mano).
- Ni Campbell, ni DORA, ni SPACE, ni el efecto cobra, ni la fábrica de clavos soviética entraron al texto: no están en la bibliografía. Si se los quiere, hay que verificarlos y agregarlos primero.

El 2026-07-16 se reforzó la bibliografía (Goodhart 1975 y Strathern 1997 con fuentes verificadas) y se resolvieron 4 de 5 marcadores [VERIFICAR:]. La decisión sobre el Hook sigue pendiente de César. Detalle: se confirmaron las dos formulaciones textuales (Goodhart original vs. Strathern popular), la cita y URL de la conversación Beck×Noda (29 ene 2025, no 2026), y se corrigieron las fechas/datos de los tres footnotes; se agregó Campbell 1976 (Ley de Campbell) a la bibliografía como referencia de fondo, sin inyectarla en la prosa. El único [VERIFICAR:] que queda es el de la formulación de John Cutler (sección «Medir el freno»), que depende de la fuente del post [[C-13]] y no se investigó en esta pasada.

Antes de publicar: resolver el Hook, completar los huecos, y decidir imágenes (siguen `_a definir_`).

---

## Borrador de prosa

> ✏️ **Corrección de la pasada de fuentes (2026-07-15):** este párrafo decía que **Kent Beck** afirmaba que la ley es «100% verdadero». La transcripción del newsletter lo desmiente: la frase es de **Abi Noda**, y Noda a su vez se la atribuye a Google. Beck contesta otra cosa —mejor para este post—. Se corrigió la prosa. **El Hook y el Concepto siguen con la atribución vieja y hay que arreglarlos** (ver `Estado actual`).

«Cuando una medida se vuelve un objetivo, deja de ser una buena medida.» La frase circula hace décadas por oficinas, papers y slides de consultoría, y casi siempre viene con el nombre de Charles Goodhart colgado al lado. En enero de 2025, en el newsletter de Kent Beck —*Software Design: Tidy First?*—, quien la trae al terreno del software es Abi Noda, fundador de DX, una empresa que vende exactamente eso: medición de productividad de desarrolladores. Y concede: «Goodhart's Law is 100% true. As soon as these measures become something folks are incentivized to game and manipulate, the very signal you worked so hard and paid for becomes useless or inaccurate.»[^beck] Viniendo de alguien que vive de vender el instrumento, la afirmación tiene algo de confesión. Noda ni siquiera se la adjudica: dice habérsela robado a Google.

La respuesta de Beck es de una línea, y es el corazón de este post: «It's worse than inaccurate, because people degrade the system to produce the number.»[^beck] Viniendo de alguien que se pasó la vida proponiendo prácticas —TDD, XP, refactorización— que otros después convirtieron en checklists de auditoría, la línea tiene su propio peso. El problema no es que el número mienta. Es que, para producir el número, se rompe el sistema que el número decía observar.

Quiero contarte por qué esa ley te muerde a vos, en tu trabajo, esta semana. Y por qué la mordida no viene, casi nunca, de un jefe malvado con una planilla.

### De dónde sale, en serio

Vale la pena una corrección antes de seguir, porque hace a la sustancia del asunto.

Goodhart no escribió esa frase. Lo que Goodhart publicó en 1975, en el contexto de la política monetaria británica, fue una observación bastante más técnica y bastante más acotada: sobre las regularidades estadísticas que el Banco de Inglaterra usaba para controlar la oferta monetaria, y sobre cómo esas regularidades se deshacían apenas se las adoptaba como instrumento de control[^goodhart]. Era una advertencia gremial de economista para economistas.

Goodhart, en 1975, había escrito algo bastante más técnico: «Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.»[^goodhart] La frase pulida —«When a measure becomes a target, it ceases to be a good measure.»—, la que todos citamos, es de Marilyn Strathern, que en 1997 la reformuló en términos generales[^strathern]. O sea: la versión famosa de la Ley de Goodhart no es de Goodhart.

Me detengo acá no por pedantería bibliográfica sino porque el destino de la frase es un ejemplo de sí misma. Una observación cuidadosa, con dominio de aplicación limitado, se volvió un eslogan; el eslogan se volvió un objetivo retórico; y hoy «eso es Goodhart» se usa para clausurar discusiones que no clausura. La medida se volvió el objetivo, también acá.

### Por qué en software muerde más fuerte

Todo oficio tiene el problema. Pero el software tiene una agravante particular: el trabajo es invisible.

Un albañil deja una pared. Un cirujano deja un paciente vivo o muerto. Un programador deja… ¿qué? Un texto que casi nadie lee, cuyo valor depende de cosas —lo que va a pasar cuando haya que cambiarlo dentro de dos años, lo que *no* va a fallar en producción— que por definición todavía no ocurrieron. El producto real del trabajo de software es en buena medida un conjunto de problemas que no van a suceder. Y los problemas que no suceden no se ven, no se cuentan, y no entran en el dashboard.

Entonces la organización mide lo único que puede: los rastros. Líneas, commits, tickets, puntos, porcentajes. Ninguno de esos es el trabajo. Todos son proxies del trabajo. Y un proxy sostiene su correlación con lo real exactamente hasta el momento en que alguien anuncia que vamos a optimizarlo.

### El catálogo de las mordeduras

Las conocés todas. Las repito igual, porque puestas juntas forman un patrón:

**Líneas de código.** Si medís LOC, se escriben más líneas. No con mala fe: simplemente el refactor que borra doscientas líneas se vuelve, contablemente, un día de productividad negativa. Y el que borra código deja de borrar.

**Commits.** Si medís commits, aparecen commits más chicos y más frecuentes, lo cual suena bien hasta que notás que aparecen commits vacíos de contenido, y que la historia del repositorio —que era una herramienta de comprensión— se vuelve ruido.

**Bugs cerrados.** Esta es la más siniestra, porque tiene una salida trivial: se cierran bugs sin arreglarlos. «No reproducible.» «Comportamiento esperado.» «Duplicado de #4471», que a su vez está cerrado como duplicado de éste. La métrica sube, el sistema empeora, y nadie mintió del todo.

**Story points.** El punto nació como unidad de incertidumbre relativa para conversar; cuando se vuelve objetivo de velocity, la inflación es inmediata y silenciosa. La misma tarea que valía tres ahora vale cinco. Nadie lo decidió. Pasó.

**Cobertura de tests.** Ochenta por ciento obligatorio y aparecen tests que ejecutan código sin asertar nada. Terminás con una suite lenta que no te protege y que además no te deja refactorizar, porque romperla es romper el número.

**Tiempo de ciclo.** Medí cuánto tarda un ticket de abierto a cerrado y vas a obtener tickets más chicos. Que a veces es exactamente lo que querías, y a veces significa que el trabajo grande e importante simplemente no se registra en ningún lado.

Fijate el patrón: en ningún caso la gente hace trampa. En casi todos los casos la gente responde racionalmente a lo que la organización dijo que le importaba.

### Las dos mitades de la ley

Acá está, me parece, lo que más se pierde cuando se cita a Goodhart como eslogan. La ley tiene dos mecanismos distintos, y sólo uno es el que todo el mundo discute.

**El primero es la presión.** Le decís a alguien que vas a medir X, y la persona optimiza X. Es el mecanismo obvio, el que aparece en las charlas, el que se ataca con discursos sobre cultura y confianza.

**El segundo es la selección, y es peor**, porque no necesita ninguna intención. Una métrica funcionaba como proxy porque estaba correlacionada con lo que importa *en el rango de comportamientos que se daban naturalmente*. Cuando la volvés objetivo, empujás al sistema fuera de ese rango. La correlación no se rompe porque alguien la haya roto: se rompe porque nunca fue una relación causal, y vos la estás usando como si lo fuera.

Es la diferencia entre «me están haciendo trampa» y «mi instrumento nunca midió lo que yo creía». La primera se resuelve con confianza. La segunda no se resuelve: es una propiedad del instrumento.

Por eso la respuesta habitual —«bueno, pero con un buen equipo esto no pasa»— es tan mala. Con un buen equipo el mecanismo uno se atenúa. El mecanismo dos sigue intacto.

> 🕳️ **HUECO — necesita a César:** ¿Qué métrica te impusieron alguna vez desde arriba en la STG o en el Ministerio de Cultura de Santa Fe? Alcanza con nombrar cuál era, quién la pedía y para qué decían que servía.

> 🕳️ **HUECO — necesita a César:** ¿Alguna vez instalaste vos una métrica en un equipo y te salió mal? ¿Cuál era y qué empezó a pasar que no esperabas?

> 🕳️ **HUECO — necesita a César:** ¿Te tocó ver de cerca el caso de los bugs cerrados sin arreglar? Una o dos frases sobre cómo se cerraban y qué pasaba después.

### Por qué la organización quiere la métrica igual

Lo interesante es que nada de esto es novedad para nadie. Preguntale a cualquier gerente técnico si medir LOC es una buena idea y te va a decir que no, con cara de ofendido. Y sin embargo el dashboard existe.

Existe porque la métrica no está resolviendo un problema de conocimiento. Está resolviendo un problema de legitimidad. Alguien tiene que explicarle a alguien de más arriba —que no programó nunca, que no va a leer el código, que tiene su propio dashboard que rendir— por qué el equipo cuesta lo que cuesta. Y ese alguien necesita un número. Cualquier número. Un número malo es infinitamente más presentable que un «confiá en mí».

Ese es el punto donde Goodhart deja de ser un problema de medición y pasa a ser un problema político. La métrica es mala como instrumento y excelente como escudo. Y mientras siga siendo excelente como escudo, ninguna demostración de que es mala como instrumento la va a sacar de la pared.

> 🕳️ **HUECO — necesita a César:** ¿Te pidieron alguna vez un dashboard de productividad del equipo? ¿Qué hiciste — lo armaste, lo negociaste, lo saboteaste?

### Mitigaciones, sin milagros

No tengo una solución. Tengo cinco cosas que me parecen menos malas que la alternativa.

**No usar la métrica para evaluar personas.** Es la línea que lo cambia todo. La misma métrica que es información útil cuando la mira el equipo se vuelve veneno cuando decide un aumento. Si el número tiene consecuencias sobre el sueldo de alguien, el número miente. No es una cuestión de honestidad: es aritmética de incentivos.

**Medir en canasta, nunca sueltas.** Una métrica sola siempre se puede jugar. Cuatro métricas que se tensionan entre sí —velocidad contra defectos, contra deuda, contra algo que represente el costo humano— hacen que jugarlas requiera más trabajo que hacer el trabajo. No es que no se pueda; es que deja de convenir.

**Medir el freno, no la producción.** Es la línea que sigue John Cutler y que discuto aparte en [[C-13]]: preguntar «¿qué te frenó esta semana?» en lugar de «¿cuánto produjiste?». El impedimento es más difícil de falsear que el output, porque nadie gana nada inventándose impedimentos. [VERIFICAR: la formulación exacta de Cutler y dónde la escribió — no está en la bibliografía de este draft; o se agrega la fuente o se cita sólo vía el post [[C-13]].]

**Rotar.** Una métrica nueva es honesta por un tiempo, hasta que el sistema aprende a servirla. Cambiarla antes de que eso pase suena a truco barato, y lo es, pero funciona por la misma razón por la que Goodhart funciona.

**Tratar la métrica como pregunta, no como respuesta.** El número que baja no es un problema: es un lugar donde ir a mirar. En el momento en que el número que baja *es* el problema, ya perdiste — porque a partir de ahí la forma más barata de resolver el problema es arreglar el número.

> 🕳️ **HUECO — necesita a César:** ¿Tenés hoy alguna medición que sí te sirva —en tu trabajo o en tus proyectos personales— y por qué esa sí y las otras no?

> 🕳️ **HUECO — necesita a César:** ¿Cuál es tu postura sobre la cobertura de tests como objetivo obligatorio? Es un tema donde probablemente tengas una opinión fuerte y conviene que sea tuya y no mía.

### Lo que queda

La Ley de Goodhart no se derrota. No hay una métrica lo bastante inteligente, y sospecho que la búsqueda de esa métrica es en sí misma una forma de caer en la ley: el objetivo se corrió de «entender el trabajo» a «tener el indicador correcto».

Con lo que sí se puede es convivir. Y convivir significa, básicamente, aceptar una incomodidad: que buena parte de lo que hace bueno a un equipo de software no se va a poder mostrar en una pantalla, y que esa parte hay que defenderla con argumentos, con confianza y con historial, no con evidencia numérica. Es un trabajo peor. Es el que hay.

Beck tiene otra metáfora para todo esto —el bosque y el desierto, que trabajo en [[C-12]]—: la del terreno que se degrada de a poco mientras cada decisión individual parece razonable. Las métricas convertidas en objetivos son una de las máquinas que fabrican desierto. Cada una tiene sentido el día que la instalás. El desierto llega después, y para entonces todos los números están en verde.

[^goodhart]: Charles A. E. Goodhart, *Problems of Monetary Management: The U.K. Experience*, ponencia de 1975 publicada en *Papers in Monetary Economics*, Vol. I, Reserve Bank of Australia, Sydney; reimpresa como cap. 4 (pp. 91–121) de *Monetary Theory and Practice: The U.K. Experience*, Macmillan, 1984, [doi:10.1007/978-1-349-17295-5_4](https://doi.org/10.1007/978-1-349-17295-5_4). Formulación original: «Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.»

[^strathern]: Marilyn Strathern, «'Improving ratings': audit in the British University system», *European Review* 5(3):305–321 (1997). DOI verificado en Crossref: <https://doi.org/10.1002/(sici)1234-981x(199707)5:3%3C305::aid-euro184%3E3.0.co;2-4>. Texto completo libre en [Internet Archive](https://archive.org/details/ImprovingRatingsAuditInTheBritishUniversitySystem). Es la fuente de la formulación popular de la ley: «When a measure becomes a target, it ceases to be a good measure.»

[^beck]: Kent Beck en conversación con Abi Noda, «Developer Productivity Metrics: Education Necessary», newsletter *Software Design: Tidy First?*, 29 de enero de 2025, <https://newsletter.kentbeck.com/p/developer-productivity-metrics-education>. Abi Noda: «Goodhart's Law is 100% true. As soon as these measures become something folks are incentivized to game and manipulate, the very signal you worked so hard and paid for becomes useless or inaccurate.» Beck responde: «It's worse than inaccurate, because people degrade the system to produce the number.»
