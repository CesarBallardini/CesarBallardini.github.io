### H-07 — Migración FoxBase → PostgreSQL en un ministerio (la otra mitad de G-04)

- **Archivo seed:** `sysadmin/draft-trac-en-ministerio-de-cultura.md` (compartido con [[G-04]])
- **Slug propuesto:** `foxbase-postgresql-ministerio`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-foxbase-postgresql-ministerio/index.md`
- **Serie:** H — comparte proyecto con [[G-04]] pero ángulo distinto
- **Cross-links:** depende de [[H-03]] (FoxBase técnico); lleva a [[G-04]] (Trac: el sistema que registró la migración), [[H-06]] (la parábola: por qué *sí* migraron en este caso), [[I-04]] (MerLinux: los escritorios del mismo proyecto Ministerio de Cultura Santa Fe)
- **Idioma:** es
- **Madurez:** seed compartido
- **Length target:** medium (1500-2200 palabras)

**Concepto:** este post es el ángulo *legacy* del mismo proyecto que [[G-04]]. Mientras [[G-04]] cuenta la herramienta de gestión (Trac, tickets, wiki), H-07 cuenta la sustancia técnica: cómo se hizo la migración real de un sistema FoxBase con N años de datos, esquema desnormalizado, eñes mal codificadas, índices corruptos, y todo lo que viene con un sistema vivo y crítico, hacia PostgreSQL con esquema nuevo. Los dos posts pueden leerse independientes pero referirse mutuamente.

**Hook:** "el sistema lo había escrito alguien que ya no estaba en el ministerio. Tenía 12 años. Estaba en FoxBase. Tenía 47 archivos `.dbf`, sin normalizar, con eñes en CP850 mezcladas con eñes en CP437, y dos índices que se rompían cada tres semanas. La gente del ministerio lo necesitaba todos los días. Migrarlo no era opcional. Tampoco era simple. El post cuenta cómo se hizo."

**Outline:**
1. El contexto del ministerio (anonimizado pero suficiente para entender la escala).
2. El sistema viejo: 47 DBF, sin normalizar, índices CDX corruptibles, codificación inconsistente.
3. La decisión: ¿emular como [[H-03]] o portar como [[H-04]]? Por qué acá la respuesta fue *portar*: el sistema *iba a evolucionar*, no congelarse. El nuevo cliente necesitaba reportes y APIs que FoxBase no podía dar.
4. La estrategia: dos sistemas en paralelo durante 18 meses.
   - lectura: ambos.
   - escritura: doble (todo cambio en el viejo se replica al nuevo).
   - validación: comparación nocturna automática.
5. El problema de las eñes: cómo se detectó, cómo se corrigió retroactivamente sin perder datos.
6. El problema del esquema: la base era un solo "todo aplanado". Normalizarla en serio implicaba 30+ tablas. Cómo se modeló el mapping.
7. El problema del downtime cero: el switchover real se hizo un fin de semana, después de 18 meses de validación, en 4 horas. Funcionó.
8. La lección humana: el equipo del ministerio necesitaba entender el sistema *nuevo* antes del switch. Capacitación tan importante como código.
9. Cierre: el sistema sigue corriendo en 2026. Ya no hay nadie del proyecto original ahí. Sobrevive porque el código se entiende.

**Bibliografía:**
- [Pramod Sadalage & Scott Ambler, *Refactoring Databases*, Addison-Wesley 2006](https://databaserefactoring.com/) — el libro central de esta migración.
- [Martin Fowler, *Evolutionary Database Design*](https://martinfowler.com/articles/evodb.html) — el bliki original.
- [PostgreSQL — `pg_migrate` y herramientas relacionadas](https://www.postgresql.org/about/news/) — buscar releases.
- [`dbf2sql` y herramientas de conversión DBF](https://www.dbf2002.com/) — recursos frágiles, verificar.
- [Strangler Fig pattern — Martin Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html) — el patrón aplicado.
- [Mike Murphy & Frank Cohen, *Modernizing Legacy Systems*](https://www.oreilly.com/library/view/modernizing-legacy-systems/0321118847/).
- [PostgreSQL — *Foreign Data Wrappers* documentation](https://www.postgresql.org/docs/current/postgres-fdw.html) — relevante para algunas estrategias de migración paralela.

**Imágenes:**
- _Crear_: diagrama de la arquitectura de "doble escritura" durante los 18 meses (~45 min — central del post).
- _Crear_: diagrama del switchover de 4 horas (~30 min).
- _Crear_: tabla de los 5 problemas y sus soluciones (~20 min).

**Tags propuestos:** `['legacy', 'FoxBase', 'PostgreSQL', 'migracion', 'ministerio', 'arqueologia']`

**Estado actual:** seed compartido con [[G-04]]; los dos posts surgen del mismo material dividido por ángulo.

