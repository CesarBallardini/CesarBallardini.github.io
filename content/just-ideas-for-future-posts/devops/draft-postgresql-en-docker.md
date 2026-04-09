### G-06 — PostgreSQL en un contenedor Docker (sin perder los datos)

- **Archivo seed:** `sysadmin/draft-postgresql-en-un-contenedor-docker.md`
- **Slug propuesto:** `postgresql-en-docker`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-postgresql-en-docker/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-07]] (Docker en Windows, el caso especial), [[G-02]] (infra determinística), [[E-04]] (Python env: cómo conectarse desde el container del dev)
- **Idioma:** es
- **Madurez:** bare-seed (archivo vacío)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** correr Postgres en Docker es trivial *hasta que necesitás guardar los datos*. El post cubre las decisiones que la mayoría de los tutoriales saltea: bind-mount vs volume, ownership y permisos, backups dentro/fuera del container, upgrades de versión mayor de Postgres con `pg_upgrade`, y por qué la imagen oficial de Docker Hub *no* es la mejor opción para todos los casos.

**Hook:** "*docker run postgres:16* y listo, dirías. Después reiniciás el container y los datos ya no están. O sí están, pero la próxima versión de Postgres no los puede leer. O están, pero el usuario del container no tiene permisos. Postgres en Docker es trivial *hasta que dejás de usarlo de juguete*. El post es la guía honesta de lo que tenés que entender antes de poner esto en producción."

**Outline:**
1. El caso "developer laptop": correr Postgres efímero para tests. Trivial. `--rm`. Sin volumen.
2. El caso "developer laptop con persistencia": volume nombrado, ownership, qué pasa cuando borrás el container y volvés a crearlo. Cuándo bind-mount tiene sentido.
3. El caso "staging": Postgres en Docker en una VM compartida. La pregunta de los networks de Docker.
4. El caso "producción". Aquí está la decisión crítica: *no la pongas en producción sin entender los puntos siguientes*.
   - **Storage**: bind-mount a un FS confiable (ZFS, ext4 + LVM). El driver overlay2 *no* es para tu data.
   - **Backups**: `pg_basebackup` desde *fuera* del container, hacia un FS persistente. WAL archiving.
   - **Upgrades de versión mayor**: `pg_upgrade` requiere las dos versiones presentes. Estrategia con dos volumes.
   - **Recursos**: `--shm-size` o el container va a fallar bajo carga.
   - **Networking**: por qué publicar el puerto en `0.0.0.0` es probablemente malo.
5. Por qué Bitnami / Crunchy / Zalando publican imágenes propias y por qué a veces son mejores que la oficial.
6. La alternativa honesta: *no uses Docker para tu Postgres de producción*. Usá un Postgres bare metal o un servicio gestionado. Docker sirve para dev/staging.
7. Cierre: el `compose.yml` mínimo + el script de backup + el procedimiento de upgrade.

**Bibliografía:**
- [PostgreSQL — sitio oficial](https://www.postgresql.org/).
- [Docker Hub — postgres oficial](https://hub.docker.com/_/postgres) — la imagen de referencia, leer el README completo.
- [Crunchy Data — Postgres Operator](https://access.crunchydata.com/documentation/postgres-operator/v5/) — la opción Kubernetes-nativa.
- [Zalando Postgres Operator](https://github.com/zalando/postgres-operator) — el otro operador serio.
- [PostgreSQL — `pg_upgrade` documentation](https://www.postgresql.org/docs/current/pgupgrade.html).
- [PostgreSQL — backup and restore documentation](https://www.postgresql.org/docs/current/backup.html).
- [Why does PostgreSQL need shared memory? — Robert Haas](https://rhaas.blogspot.com/2012/03/postgresql-and-shared-memory.html).
- [Werner Vogels, *All Things Distributed* — sobre por qué databases en containers](https://www.allthingsdistributed.com/) — buscar posts específicos.
- [Brendan Gregg, *Linux Containers Performance Analysis*, USENIX 2017](https://www.brendangregg.com/blog/2017-05-15/container-performance-analysis-dockercon-2017.html) — performance honesta.

**Imágenes:**
- _Crear_: diagrama del compose.yml mostrando volume + container + host bind (~30 min).
- _Crear_: diagrama del flujo de upgrade con dos volumes (~45 min).
- _Crear_: tabla "ambiente / estrategia recomendada" (~20 min).

**Tags propuestos:** `['PostgreSQL', 'Docker', 'volumes', 'pg_upgrade', 'sysadmin', 'devenv']`

**Estado actual:** archivo vacío; el material está en notas operacionales actuales.

