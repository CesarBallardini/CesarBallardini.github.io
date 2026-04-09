### G-11 — Recreando la arquitectura DNS/IPAM de Maynooth con PowerDNS, nsedit y phpIPAM

- **Archivo seed (repo POC):** [github.com/CesarBallardini/dns-infra](https://github.com/CesarBallardini/dns-infra) — Jinja, último push 2021-04-26 — más [github.com/CesarBallardini/ansible-role-nsedit](https://github.com/CesarBallardini/ansible-role-nsedit)
- **Slug propuesto:** `dns-ipam-maynooth-powerdns`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-dns-ipam-maynooth-powerdns/index.md`
- **Serie:** G — meaty
- **Cross-links:** depende de [[E-12]]; lleva a [[G-08]]
- **Idioma:** es
- **Madurez:** **partial-poc** — varias VMs operativas, otras con FIXME explícitos
- **Length target:** long (2500-3500 palabras) — es un post-serie en sí mismo

**Concepto:** Bart Busschots (Maynooth University) presentó hace algunos años una arquitectura completa de DHCP + DNS + IPAM (IP Address Management) con redundancia, multi-master y separación de visibility (interno vs público). Mi `dns-infra` es un intento de reproducirla paso a paso con ~10 roles VM (blindmaster, ipam, localmaster/slave, globalmaster/slave, ddiscript, dhcpmaster/slave, dnsresolver, MySQL cluster, test nodes), usando PowerDNS + nsedit (web UI) + phpIPAM. Algunos roles están terminados, otros no — el README marca explícitamente "Que está funcionando en este momento". El post cuenta la arquitectura, qué reproduje y qué no, y la lección de fondo: *recrear* una arquitectura ajena de cero te enseña más que leer 10 papers sobre el tema.

**Hook:** "Bart Busschots dio una charla en Maynooth sobre cómo armar DNS/DHCP/IPAM redundante, con visibility separada y un único panel de control. Me pareció una arquitectura honesta. La intenté reproducir paso a paso en mi laptop con ~10 VMs. Algunas funcionan; otras tienen FIXMEs gordos. El post cuenta la arquitectura, qué aprendí, y por qué los proyectos de 'recrear lo que otro mostró' son la mejor manera de aprender infraestructura."

**Outline:**
1. El problema: DNS/DHCP/IPAM en una red mediana (universidades, empresas con varias subredes, etc.). Por qué nadie lo hace bien.
2. La arquitectura de Maynooth en su charla: blindmaster, master/slave hierarchies, IPAM como single source of truth, scripts de sincronización (ddiscript).
3. Las herramientas elegidas: PowerDNS (con MySQL backend), nsedit (UI web), phpIPAM (UI IPAM). Por qué cada una.
4. Mi reproducción: ~10 VMs, cada una con un role específico. Tabla de "qué hace cada VM y cuál es su par redundante".
5. El estado real (honesto): qué funciona, qué no, qué dejé en TODO. Esto es la sección más útil.
6. Lo que aprendí intentándolo: la sincronización maestro-maestro de PowerDNS no es trivial; nsedit es elegante pero frágil; phpIPAM tiene su propia lógica que no siempre coincide con la de PowerDNS.
7. La conexión con [[G-01]] (roles/profiles): cada uno de los ~10 roles VM es un *role-as-server-type* en el sentido del patrón Puppet.
8. Cierre: el repo está abierto, faltan los últimos 30%. Si alguien quiere continuarlo, hay un README detallado.

**Bibliografía:**
- Repos: [dns-infra](https://github.com/CesarBallardini/dns-infra), [ansible-role-nsedit](https://github.com/CesarBallardini/ansible-role-nsedit).
- [PowerDNS — sitio oficial](https://www.powerdns.com/).
- [nsedit — PowerDNS web UI](https://github.com/tuxis-ie/nsedit).
- [phpIPAM — sitio oficial](https://phpipam.net/).
- [Bart Busschots, *Bart B's blog*](https://www.bartbusschots.ie/) — buscar la charla específica de DNS/IPAM.
- [DNS and BIND — Liu & Albitz, 5th ed O'Reilly 2006](https://www.oreilly.com/library/view/dns-and-bind/0596100574/) — referencia clásica.

**Imágenes:**
- _Crear_: diagrama de la arquitectura completa (blindmaster, master/slave, IPAM, ddiscript, etc.) (~1.5 horas — la imagen central).
- _Crear_: tabla de las ~10 VMs con su rol y estado actual (~30 min).

**Tags propuestos:** `['DNS', 'PowerDNS', 'nsedit', 'phpIPAM', 'IPAM', 'Maynooth', 'Vagrant', 'partial-poc']`

**Estado actual:** **partial-poc** — buen material para post largo, pero el lector debe entender que la reproducción es parcial.

