### G-24 — Cuttlefish: mi propio servidor SMTP transaccional autohospedado

- **Archivo seed:** `github.com/CesarBallardini/cuttlefish` (fork, Ruby, Feb 2021)
- **Slug propuesto:** `cuttlefish-smtp-autohosted`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-cuttlefish-smtp-autohosted/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-25]] (mailserver completo — el primo full-featured), [[E-15]] (free-for-dev: cuándo vale la pena self-hosted vs pagar Mailgun)
- **Idioma:** es
- **Madurez:** fork de un proyecto Rails funcional (Cuttlefish es un proyecto de Matthew Landauer)
- **Length target:** medium (1000-1500 palabras)

**Concepto:** *Cuttlefish* es un servidor SMTP transaccional con UI web bonita — pensado como alternativa self-hosted a Mailgun, SendGrid, Postmark. Lo forkeé para correrlo en mi infraestructura. El post explica cuándo *sí* conviene self-hostear email transaccional (hobby projects sobre todo) y cuándo *no* (cualquier cosa con tráfico real, porque los filtros anti-spam castigan IPs nuevas).

**Hook:** "querés mandar mails desde tu app — transaccionales, de confirmación, de reset de password. Mailgun cuesta. Postmark cuesta. SES cuesta lo suficiente como para que lo pienses. Cuttlefish es gratis, self-hosted, con una UI web linda para ver el historial de mensajes. El post explica cómo lo monté y la pregunta honesta: ¿vale la pena?"

**Outline:**
1. El problema del email transaccional desde hobby projects.
2. Cuttlefish: Rails + Postfix + web UI con dashboard.
3. El deployment con Docker.
4. El dolor del deliverability: SPF, DKIM, DMARC, el reverse DNS, la reputación de la IP.
5. La regla que aprendí: para hobby projects con pocos destinatarios (yo mismo, mis tests), Cuttlefish funciona. Para cualquier volumen, pagá Postmark.
6. Cierre: link al repo y al deployment Docker.

**Bibliografía:**
- [Cuttlefish en GitHub](https://github.com/mlandauer/cuttlefish) — el original de Matthew Landauer.
- [Postfix documentation](http://www.postfix.org/documentation.html).
- [Mailgun vs Postmark vs SES comparison](https://mailgun.com/) — comparaciones comerciales.

**Imágenes:**
- _Crear_: screenshot de la UI de Cuttlefish (~15 min).
- _Crear_: diagrama SPF/DKIM/DMARC (~30 min).

**Tags propuestos:** `['SMTP', 'Cuttlefish', 'self-hosted', 'email', 'Rails', 'sysadmin']`

**Estado actual:** fork funcional, montado en homelab, post fácil.

