### H-09 — UDPcast: instalar 40 escritorios al mismo tiempo con multicast

- **Archivo seed:** `sysadmin/draft-udpcast.md`
- **Slug propuesto:** `udpcast-instalacion-masiva`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-udpcast-instalacion-masiva/index.md`
- **Serie:** H — cierra la serie con la herramienta más nicho
- **Cross-links:** depende de [[H-08]] (ThinStation: el caso de uso); lleva a [[G-02]] (golden image como concepto)
- **Idioma:** es
- **Madurez:** seed (3 líneas: udpcast, golden image, instalación masiva)
- **Length target:** short (800-1200 palabras)

**Concepto:** UDPcast es una herramienta minúscula y mágica: copia un archivo (típicamente una imagen de disco) desde un sender a *muchos* receivers simultáneamente usando multicast UDP. En vez de descargar la imagen N veces secuenciales, todos los receivers reciben la misma transmisión a la vez. Para instalar 40 PCs idénticas, esto reduce 40 horas a 30 minutos. El post explica la herramienta, su contexto histórico (cuando los SSD no existían y los discos eran lentos), y cuándo todavía es la respuesta correcta hoy.

**Hook:** "tenía que clonar la misma imagen de disco a 40 PCs idénticas. Hacerlo de una en una hubiera llevado dos días enteros. UDPcast lo hizo en 35 minutos. La herramienta cabe en 200 KB, está escrita en C, y la mantiene un señor de Suiza desde el 2000. No hay magia — es multicast UDP bien usado. El post explica qué es, cómo funciona y por qué en 2026 sigue siendo la mejor respuesta para algunos escenarios."

**Outline:**
1. El problema clásico: clonar la misma imagen a N máquinas idénticas en una LAN.
2. Las soluciones lentas: copiar de a una con dd, descargar N veces de un servidor, USB stick rotativo (dolor).
3. La idea del multicast: el sender transmite *una sola vez* y los N receivers escuchan la misma transmisión.
4. UDPcast — historia: Alain Knaff, año 2000, sigue mantenido.
5. Cómo se usa: `udp-receiver` en cada cliente (booteado desde un live CD mínimo de UDPcast), `udp-sender` en el server, los clientes se sincronizan y arranca la transmisión.
6. Los problemas reales:
   - **switches sin IGMP snooping** — el multicast se vuelve broadcast, satura todo. Cómo detectarlo.
   - **paquetes perdidos** — la corrección es por capa de aplicación (FEC) no por UDP. Cuándo activarla.
   - **clientes que llegan tarde** — el sender espera. Cómo manejar el timeout.
7. Cuándo en 2026 sigue siendo la mejor opción: laboratorios de informática, fábricas con muchas PCs idénticas, despliegues de ATMs, golden images de VMs (con virtualización igual sirve).
8. Cierre: el repo está en sourceforge, el binario cabe en una imagen de boot mínima, y el author sigue respondiendo emails. Eso es software bien hecho.

**Bibliografía:**
- [UDPcast — sitio oficial](https://www.udpcast.linux.lu/).
- [UDPcast en SourceForge](https://sourceforge.net/projects/udpcast/).
- [Alain Knaff — author page](https://www.linux.lu/) — el mantainer histórico.
- [IP multicast — Wikipedia](https://en.wikipedia.org/wiki/IP_multicast).
- [IGMP snooping explicado — Cisco](https://www.cisco.com/c/en/us/support/docs/lan-switching/multilayer-switching-mls/10094-83.html).
- [Forward error correction — Wikipedia](https://en.wikipedia.org/wiki/Error_correction_code) — para entender cómo UDPcast recupera paquetes.
- [Clonezilla con multicast](https://clonezilla.org/) — la herramienta moderna que usa UDPcast por debajo.
- [PartImage](http://www.partimage.org/) — alternativa histórica.

**Imágenes:**
- _Crear_: diagrama del flujo multicast — sender + N receivers + switch (~30 min).
- _Crear_: gráfico de tiempos: secuencial vs UDPcast (~20 min).

**Tags propuestos:** `['legacy', 'UDPcast', 'multicast', 'golden image', 'sysadmin', 'arqueologia']`

**Estado actual:** seed con tres líneas; herramienta sigue viva, post fácil de cerrar.

