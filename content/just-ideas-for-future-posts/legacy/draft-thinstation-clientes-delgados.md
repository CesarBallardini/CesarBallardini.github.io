### H-08 — ThinStation: clientes delgados con soporte sólo del lado del servidor

- **Archivo seed:** `sysadmin/draft-thinstation.md`
- **Slug propuesto:** `thinstation-clientes-delgados`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-thinstation-clientes-delgados/index.md`
- **Serie:** H — el post de "infraestructura legacy" más que "código legacy"
- **Cross-links:** lleva a [[H-09]] (UDPcast: para distribuir las imágenes de ThinStation), [[G-02]] (infra determinística)
- **Idioma:** es
- **Madurez:** seed (3 líneas)
- **Length target:** medium (1200-1800 palabras)

**Concepto:** ThinStation es una distribución Linux minimal pensada para correr en un cliente delgado que arranca por red (PXE) y conecta a un servidor remoto vía RDP, NX, X11, ICA o VNC. Lo usé en un proyecto donde había 40 puestos de trabajo en una oficina y la PC de cada uno era literalmente una caja sin disco duro: BIOS bootea por red, baja la imagen de ThinStation, se conecta al servidor de aplicaciones, y el usuario ve su sesión. El hardware client es desechable. El soporte vive sólo del lado del servidor.

**Hook:** "tenía 40 escritorios y ningún técnico in situ. La regla del cliente: cuando una PC se rompe, hay que poder reemplazarla en 5 minutos por la del al lado, sin que el usuario pierda nada. Solución: clientes delgados sin disco, ThinStation por PXE, todo el estado en el servidor. Cuando una caja se rompe, agarrás otra del armario, la enchufás, y andando. El soporte se vuelve trivial. El post explica cómo lo armé."

**Outline:**
1. El problema: 40 puestos en una oficina, mantenimiento on-site caro, exigencia de continuidad.
2. La idea de cliente delgado — pre-2010 vs post-2010, qué cambió y qué no.
3. ThinStation: distribución Linux que cabe en 30 MB, bootea por PXE, no toca disco.
4. La arquitectura completa:
   - servidor PXE + DHCP + TFTP.
   - imagen ThinStation customizada con los protocolos que necesitaba (RDP a un terminal server Windows + NX a un Linux).
   - servidor de aplicaciones (Windows Server con servicios de escritorio remoto).
   - storage compartido para perfiles roaming.
5. El proceso de configuración: el `build.conf` de ThinStation, cuál es el infierno, qué se incluye y qué no.
6. La distribución de la imagen — UDPcast multicast para *empujar* la imagen a todos los clientes a la vez ([[H-09]]).
7. El día que se rompió: PXE no funcionaba, los clientes se quedaban en el boot loader. Diagnóstico: switch sin IGMP snooping. Solución: no la cambies, configurá el switch.
8. Cierre: en 2026, ¿esto sigue siendo válido? Sí, en escenarios donde la PC física es hostil (kiosks, fábricas, escuelas). Para oficinas modernas, una laptop es igual de barata y más cómoda.

**Bibliografía:**
- [ThinStation — sitio oficial](https://thinstation.github.io/thinstation/).
- [ThinStation en GitHub](https://github.com/Thinstation/thinstation) — repo activo.
- [PXE — Wikipedia](https://en.wikipedia.org/wiki/Preboot_Execution_Environment).
- [iPXE — Open Source Network Boot Firmware](https://ipxe.org/) — para casos donde el BIOS PXE no alcanza.
- [LTSP — Linux Terminal Server Project](https://ltsp.org/) — el alternativo más conocido.
- [NX Technology — NoMachine](https://www.nomachine.com/) — para X remoto eficiente.
- [Microsoft — Remote Desktop Protocol documentation](https://learn.microsoft.com/en-us/windows/win32/termserv/remote-desktop-protocol).
- [Wikipedia — Thin client](https://en.wikipedia.org/wiki/Thin_client).

**Imágenes:**
- _Crear_: diagrama de la arquitectura completa (cliente sin disco → switch → PXE server → app server) (~45 min).
- _Crear_: foto del rack de servidores si todavía tengo (~10 min).
- _Crear_: secuencia del boot — pantallas que ve el usuario en orden (~30 min).

**Tags propuestos:** `['legacy', 'ThinStation', 'PXE', 'cliente delgado', 'sysadmin', 'arqueologia']`

**Estado actual:** seed con tres líneas; el material está en notas de configuración.

