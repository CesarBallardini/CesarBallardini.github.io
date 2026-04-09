### G-26 — LetsEncrypt con Cloudflare DNS vía Ansible (el role mínimo que tenía que existir)

- **Archivo seed:** `github.com/CesarBallardini/ansible-letsencrypt-cloudflare` (fork, HTML, Jan 2023)
- **Slug propuesto:** `letsencrypt-cloudflare-ansible-role`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-letsencrypt-cloudflare-ansible-role/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-01]] (Ansible roles/profiles), [[G-11]] (PowerDNS — el contraste self-hosted)
- **Idioma:** es
- **Madurez:** fork funcional con role Ansible
- **Length target:** short (700-1000 palabras)

**Concepto:** emitir certificados LetsEncrypt usando el DNS-01 challenge contra Cloudflare, automatizado por Ansible. Es el caso más común (wildcard certs, servidores no expuestos al puerto 80) y tiene el workflow más limpio. El post muestra el role y explica por qué esta combinación es la default razonable en 2026.

**Hook:** "necesitás un certificado wildcard para `*.ejemplo.com`. LetsEncrypt lo permite, pero sólo con el DNS-01 challenge. Tu DNS está en Cloudflare. Querés que sea automático, que se renueve solo, y que te avise cuando algo falla. El role Ansible hace exactamente eso en 60 líneas."

**Outline:**
1. Por qué DNS-01 y no HTTP-01: wildcards, servidores internos, no exponer puerto 80.
2. El API token de Cloudflare: permisos mínimos (Zone:DNS:Edit + Zone:Zone:Read sobre el dominio específico).
3. El role: certbot + plugin cloudflare + systemd timer.
4. Los gotchas: propagation delay del DNS, rate limits de LetsEncrypt staging vs prod, múltiples wildcards en el mismo cert.
5. Cierre: el role está en mi fork.

**Bibliografía:**
- [Let's Encrypt — DNS-01 challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge).
- [Certbot DNS Cloudflare plugin](https://certbot-dns-cloudflare.readthedocs.io/).
- [Cloudflare API tokens documentation](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Imágenes:**
- _Crear_: diagrama del flujo DNS-01: certbot → Cloudflare API → TXT record → validation → cert (~30 min).

**Tags propuestos:** `['LetsEncrypt', 'Cloudflare', 'Ansible', 'DNS-01', 'certificados', 'TLS']`

**Estado actual:** fork funcional, post corto y práctico.

