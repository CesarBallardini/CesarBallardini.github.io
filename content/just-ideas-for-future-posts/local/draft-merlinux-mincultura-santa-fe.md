### I-04 — MerLinux: la distro de Debian que armé para el Ministerio de Cultura de Santa Fe (con la trilogía bash → Puppet → Ansible)

- **Archivo seed:** `sysadmin/draft-merlinux.md`
- **Slug propuesto:** `merlinux-mincultura-santa-fe`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-merlinux-mincultura-santa-fe/index.md`
- **Serie:** I — el post ancla del proyecto MinCultura visto desde el ángulo "memoria del cómputo en estas latitudes"
- **Cross-links:** lleva a [[G-01]] (Ansible roles/profiles — la lección que destilé del fin del ciclo Puppet→Ansible de este proyecto), [[G-04]] (Trac en MinCultura — la otra herramienta del mismo proyecto), [[H-07]] (la migración FoxBase→PostgreSQL en el mismo ministerio), [[I-05]] (otro cargo provincial mío), [[H-09]] (UDPcast: cómo distribuíamos las imágenes); depende conceptualmente de [[H-08]] (ThinStation, la idea hermana de "instalación liviana centralizada")
- **Idioma:** es
- **Madurez:** seed con tres líneas + clarificación del autor (2026-04-08) sobre la arquitectura real
- **Length target:** medium-long (2000-3000 palabras) — es un post denso con tres capítulos (instalador, configuración remota, evolución de herramientas)

**Concepto:** MerLinux fue una distribución Debian remasterizada que armé para el **Ministerio de Cultura de la provincia de Santa Fe**, Argentina. La situación: la repartición tenía muchos edificios distribuidos en varias ciudades de la provincia, y cada puesto de trabajo administrativo necesitaba un escritorio Linux funcional. La estrategia tenía dos tiempos: **(1)** un instalador interactivo que pedía parámetros y dejaba un Debian base configurado correctamente para esa sede; **(2)** después del primer boot, el equipo se registraba en un puppetmaster, y Puppet terminaba de instalar todo el software adicional específico del *puesto de trabajo* (no del edificio). Más tarde, Puppet fue reemplazado por Ansible. Y antes de Puppet, el trabajo lo hacía un *bunch* de scripts bash. El post cuenta la trilogía completa: la distro, el sistema de gestión remota, y la evolución bash → Puppet → Ansible.

**Hook:** "el Ministerio de Cultura de Santa Fe tiene muchos edificios en varias ciudades, y cada puesto de trabajo administrativo necesitaba un Linux funcional. Armé una distro propia, que se llamaba MerLinux (sí, el nombre era un chiste). Tenía un instalador que te pedía cuatro o cinco parámetros, te dejaba un Debian listo, y después un puppetmaster te terminaba de instalar el software específico para tu puesto. Más adelante Puppet fue reemplazado por Ansible. Antes de Puppet, eran scripts en bash. El post no es sólo sobre la distro — es sobre la *evolución completa* de cómo se gestionaba la configuración de escritorios públicos a lo largo de los años, y por qué cada herramienta llegó cuando llegó."

**Outline:**
1. El contexto: Ministerio de Cultura de la provincia de Santa Fe. Muchos edificios, varias ciudades, equipos administrativos heterogéneos. Por qué Linux era la respuesta correcta (presupuesto, libertad, sustentabilidad).
2. **Capítulo 1 — La distro**: cómo se construye un Debian remasterizado en serio. La elección de Debian (estable, repos enormes, política rigurosa). Build con `live-build` de Debian. Lo que se incluía en la imagen base: kernel, X, escritorio (¿XFCE?, ¿LXDE? — verificar), navegador, suite ofimática, lectores PDF, drivers de impresoras comunes.
3. **El instalador interactivo**: la parte que el seed describe como "pedía parámetros". Qué preguntaba: hostname, usuario administrativo, edificio, sede, servidor de archivos local, posiblemente impresoras de red por defecto. Sin auto-detección — la *interacción humana* es parte del diseño porque la información que necesita NO está disponible en el cable.
4. **Capítulo 2 — La gestión remota post-instalación**: una vez que MerLinux terminó la instalación base, el equipo *se registraba en un puppetmaster*. Esta es la pieza central del post — separar "instalación de la base" (MerLinux) de "configuración del puesto específico" (Puppet) fue la decisión arquitectónica que hizo que todo escalara.
5. **Cómo se modelaban los puestos de trabajo en Puppet**: cada puesto tenía un tipo (administrativo de tesorería, despacho, archivo, biblioteca, atención al público) y cada tipo cargaba un manifest distinto. Aplicaciones específicas, accesos a servidores, configuración de impresoras, política de actualizaciones.
6. **Capítulo 3 — La evolución bash → Puppet → Ansible**:
   - **Antes de Puppet**: los puestos se configuraban con scripts bash sueltos. Cada nuevo puesto era una variante del script anterior. La deuda crecía. Funcionaba, pero a duras penas.
   - **La llegada de Puppet**: el momento en que entendí (a través de Craig Dunn) que había una manera disciplinada de modelar esto, y la migración fue cuestión de meses. Lo que ganamos: idempotencia, reportes, drift detection.
   - **El reemplazo por Ansible**: por qué se hizo el cambio (push vs pull, Python vs Ruby, comunidad, ergonomía de YAML, *agentless*). Lo que se perdió y lo que se ganó. La migración iterativa de manifests Puppet a roles Ansible.
   - El patrón de roles/components/profiles que decanté en este proceso es exactamente el que cuento en [[G-01]] — esa entrada es el *resumen abstracto*, esta es la *historia vivida*.
7. **La distribución de la imagen MerLinux**: DVDs estampados al principio, después UDPcast ([[H-09]]) para reinstalaciones masivas en una sede.
8. Lo que aprendimos durante todo el ciclo:
   - el instalador interactivo *funciona* mejor que la auto-detección heurística cuando los datos críticos sólo viven en la cabeza del operador.
   - la separación "base + post-config remoto" es la decisión que realmente importa; la herramienta de post-config (bash, Puppet, Ansible) es secundaria.
   - los upgrades de versión mayor de Debian se manejaban no upgradando: cuando había que renovar, se reinstalaba con una imagen MerLinux nueva. Más simple, menos drift.
   - el ciclo herramienta-gana-feature → migración → nueva-herramienta-gana-feature es real, y el costo de migrar entre herramientas es mucho menor que la deuda de quedarse con la vieja.
9. Cierre: el origen del nombre "MerLinux" (anécdota corta, si se puede contar). Lo que sobrevive del proyecto, lo que no, y por qué la lección estructural ("base + post-config separados") sigue siendo la decisión correcta en 2026, sólo que ahora se llama "image + cloud-init + Ansible".

**Bibliografía:**
- [Debian — Live build manual](https://live-team.pages.debian.net/live-manual/) — la herramienta de construcción de la imagen.
- [Debian Live project — Wikipedia](https://en.wikipedia.org/wiki/Debian_Live).
- [Puppet documentation — sitio oficial actual](https://www.puppet.com/docs/puppet/latest/puppet_index.html).
- [Craig Dunn, *Designing Puppet — Roles and Profiles*, 2012](https://www.craigdunn.org/2012/05/239/) — el post fundacional del patrón roles/profiles que me ayudó a estructurar los manifests de MinCultura.
- [Ansible — documentación oficial](https://docs.ansible.com/) — la herramienta que terminó reemplazando Puppet.
- [Software Engineering Stack Exchange — Puppet roles/profiles en Ansible](https://softwareengineering.stackexchange.com/questions/324705/what-is-the-equivalent-of-puppets-roles-profiles-pattern-in-ansible) — la respuesta clave durante la migración.
- [Provincia de Santa Fe — Ministerio de Cultura, sitio oficial](https://www.santafe.gob.ar/index.php/cultura) — verificar URL exacta antes de publicar (frágil, cambia con cada gestión).
- [Federico Heinz, *Por qué el Estado debe usar Software Libre*, Vialibre 2003](https://www.vialibre.org.ar/) — el contexto político de software libre en el Estado argentino.
- [Vía Libre — *Software libre en la administración pública argentina*](https://www.vialibre.org.ar/) — colección de textos.
- [Klaus Knopper, *Knoppix*](http://www.knoppix.org/) — el ancestro de la idea de live distro / remaster.
- [Cloud-init documentation](https://cloud-init.io/) — el equivalente moderno del instalador interactivo de MerLinux.
- [Mark Burgess, *Cfengine — paper LISA 1995*](https://www.usenix.org/legacy/publications/library/proceedings/lisa95/full_papers/burgess.pdf) — el ancestro académico de Puppet/Ansible/Chef, contexto histórico.

**Imágenes:**
- _Crear_: foto del DVD físico de MerLinux estampado, si existe en mis backups (~10 min de buscar).
- _Crear_: screenshot del instalador pidiendo parámetros (recreación si no tengo el original) (~30 min).
- _Crear_: diagrama del flujo completo: **DVD MerLinux → instalación base + parámetros → primer boot → registro en puppetmaster → Puppet aplica manifest del tipo de puesto → operativo** (~1 hora — esta es la imagen central del post).
- _Crear_: línea de tiempo de la evolución **bash → Puppet → Ansible** con las fechas aproximadas y los factores que motivaron cada cambio (~45 min).

**Tags propuestos:** `['MerLinux', 'Debian Live', 'Puppet', 'Ansible', 'Ministerio de Cultura', 'Santa Fe', 'IaC', 'historia local']`

**Estado actual:** seed con tres líneas + **clarificación del autor el 2026-04-08**: el proyecto era para el Ministerio de Cultura de la provincia de Santa Fe (no anonimizado), el instalador era *interactivo* (pedía parámetros, no auto-detección), la configuración post-instalación se hacía con un puppetmaster, y la evolución completa fue bash → Puppet → Ansible. La arquitectura "base separada de post-config" es el corazón del post. El material concreto (manifests, ejemplos, fechas) tiene que reconstruirse del backup del proyecto y de los repos viejos antes de publicar.

