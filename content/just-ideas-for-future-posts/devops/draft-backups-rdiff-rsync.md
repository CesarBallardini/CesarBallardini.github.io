### G-03 — Backups con rdiff-backup + rsync (y por qué los backups no sirven, lo que sirve es el restore)

- **Archivo seed:** `sysadmin/draft-rdiff-rsync-backup.md` (15 líneas, con un párrafo introductorio escrito y la frase clave del post)
- **Slug propuesto:** `backups-rdiff-rsync`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-backups-rdiff-rsync/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-02]] (infraestructura determinística — los backups son parte del determinismo), [[H-04]] (sistemas que no se pueden parar)
- **Idioma:** es
- **Madurez:** prose-started (intro escrita, falta el método)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** un esquema de backups *simple* con dos herramientas Unix bien establecidas: `rdiff-backup` (para mantener historia con costos diferenciales) y `rsync` (para la copia inicial y para sincronizar a un sitio remoto). El post no es sobre las herramientas — es sobre el principio: *los backups no sirven, lo que sirve es el restore*. Y por lo tanto, el post enseña a probar restores, no sólo a configurar backups.

**Hook:** "los backups no sirven para nada. Lo que sirve es el restore. Esa frase la digo desde 2003 y todavía me la peleo en cada empresa nueva. El post es sobre cómo armé un esquema con rdiff-backup y rsync que durante 15 años no me falló — pero sobre todo, cómo verifiqué que el restore funcionaba *antes* de necesitarlo."

**Outline:**
1. La frase del título — explicada con dos anécdotas reales (sin nombres) de restores que fallaron en producción.
2. ¿Por qué `rdiff-backup` y no Bacula / BorgBackup / restic? — honestidad: porque ya estaba ahí cuando lo elegí, y porque el formato es transparente (hard-links + diffs reverse-incremental). Si arrancás en 2026, BorgBackup es probablemente mejor.
3. ¿Por qué `rsync` también? — para el primer pull y para replicar a un sitio remoto offsite. Diferentes herramientas para diferentes capas.
4. El esquema completo:
   - tier 1: `rdiff-backup` local con histórico de N días.
   - tier 2: `rsync` a NAS en otro rack.
   - tier 3: `rsync` (con `--link-dest`) a un sitio remoto, semanal.
5. La parte que la mayoría no hace: el script de *restore-test* que cada lunes elige un archivo random del backup y verifica que se puede restaurar.
6. Lo que rompió en 15 años: 2 incidentes documentados. Qué aprendí.
7. Cierre: el camino moderno (BorgBackup + restic + Backblaze B2) y por qué el principio sigue siendo el mismo.

**Bibliografía:**
- [rdiff-backup — sitio oficial](https://rdiff-backup.net/).
- [rsync man page](https://download.samba.org/pub/rsync/rsync.1).
- [BorgBackup — sitio oficial](https://www.borgbackup.org/).
- [restic — sitio oficial](https://restic.net/).
- [W. Curtis Preston, *Modern Data Protection*, O'Reilly 2021](https://www.oreilly.com/library/view/modern-data-protection/9781492094043/) — referencia moderna.
- [W. Curtis Preston, *Backup & Recovery*, O'Reilly 2007](https://archive.org/details/backuprecovery0000pres) — el libro clásico, todavía válido conceptualmente.
- [Tarsnap — Colin Percival](https://www.tarsnap.com/) — el otro enfoque (cifrado fuerte, online).
- [Schneier on Security — *Backups*](https://www.schneier.com/blog/archives/2014/06/iphone_encrypti.html) — perspectiva de seguridad.

**Imágenes:**
- _Crear_: diagrama de los tres tiers (local + NAS + offsite) con flechas y frecuencias (~30 min).
- _Crear_: snippet del script de restore-test (~15 min, sólo formateo).

**Tags propuestos:** `['backup', 'rdiff-backup', 'rsync', 'restore', 'sysadmin']`

**Estado actual:** prose-started; ya hay 2 párrafos en el seed con la frase del título. Es uno de los más rápidos de cerrar.

