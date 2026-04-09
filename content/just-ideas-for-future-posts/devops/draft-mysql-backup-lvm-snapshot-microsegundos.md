### G-16 — Backups MySQL con LVM snapshot y ventana de bloqueo de microsegundos (GEM)

- **Archivo seed (repo POC):** [github.com/CesarBallardini/mysql-backup](https://github.com/CesarBallardini/mysql-backup) — Shell, último push 2019-08-09
- **Slug propuesto:** `mysql-backup-lvm-snapshot-microsegundos`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mysql-backup-lvm-snapshot-microsegundos/index.md`
- **Serie:** G — single-concept gem
- **Cross-links:** lleva a [[G-03]] (rdiff/rsync backups), [[G-06]] (PG en Docker)
- **Idioma:** es
- **Madurez:** **complete-poc** para backup, **partial** para restore
- **Length target:** medium (1500-2000 palabras)

**Concepto:** la técnica clásica para backupear MySQL con downtime mínimo: combinar `FLUSH TABLES WITH READ LOCK` con un snapshot LVM, dentro de una ventana de bloqueo del orden de microsegundos. El truco: el snapshot LVM es atómico a nivel de block device, así que el lock se libera *inmediatamente después* de crearlo. Después restaurás los archivos consistentes desde el snapshot, sin que el servidor MySQL haya estado bloqueado más allá del tiempo del snapshot. El post explica el mecanismo, lo aplica, y muestra cómo medir el tiempo real de bloqueo.

**Hook:** "tenés que hacer backup de un MySQL en producción. No querés `mysqldump` (no escala). No querés Percona Xtrabackup (otra dependencia). Querés un truco honesto del nivel del kernel: bloquear el server durante *microsegundos*, sacar un snapshot LVM, y restaurar los archivos desde el snapshot tranquilo. Acá está cómo, en una VM Vagrant con MySQL 5.7."

**Outline:**
1. El problema: backup consistente de MySQL sin downtime.
2. Las soluciones que descarté: `mysqldump` (lento, locks largos), `Percona Xtrabackup` (dependencia extra), replicación slave (complejidad, no es backup).
3. La idea: `FLUSH TABLES WITH READ LOCK` adquiere lock a nivel servidor; `LVM snapshot` es atómico a nivel block device. El lock se libera apenas el snapshot está creado.
4. La secuencia exacta:
   - `FLUSH TABLES WITH READ LOCK` (en sesión MySQL)
   - `lvcreate --size 5G --snapshot --name backup-snap /dev/vg0/mysql-data` (en shell)
   - `UNLOCK TABLES` (en sesión MySQL, *inmediatamente*)
5. La ventana real: medir con `time` cuánto tarda el `lvcreate`. En mi VM: del orden de milisegundos.
6. La restauración: `mount /dev/vg0/backup-snap /mnt/backup` y `rsync` los datafiles a otro lado, o `tar` para enviarlos a S3.
7. Las tres estrategias backup que monto sobre eso: incremental con rsync, snapshot mensual completo, send a S3.
8. Honestidad: el script de *restore* tiene TODOs.
9. Cierre.

**Bibliografía:**
- Repo del POC: [CesarBallardini/mysql-backup](https://github.com/CesarBallardini/mysql-backup).
- [MySQL — `FLUSH TABLES` reference](https://dev.mysql.com/doc/refman/5.7/en/flush.html).
- [LVM snapshot guide — Red Hat](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logical_volumes/managing-lvm-snapshots_configuring-and-managing-logical-volumes).
- [W Curtis Preston, *Backup & Recovery*, O'Reilly 2007](https://archive.org/details/backuprecovery0000pres).

**Imágenes:**
- _Crear_: diagrama timeline mostrando la ventana de microsegundos (~30 min — central).
- _Crear_: snippet del script bash en una caja (~15 min).

**Tags propuestos:** `['MySQL', 'LVM', 'snapshot', 'backup', 'restore', 'Vagrant']`

**Estado actual:** **complete-poc** para backup, restore parcial. Single-concept gem post.

