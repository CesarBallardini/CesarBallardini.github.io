### G-25 — Mailserver completo en Docker: el servidor de mail full-featured self-hosted

- **Archivo seed:** `github.com/CesarBallardini/mailserver` (fork, Shell, Jan 2020)
- **Slug propuesto:** `mailserver-docker-full-featured`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mailserver-docker-full-featured/index.md`
- **Serie:** G
- **Cross-links:** contrasta con [[G-24]] (Cuttlefish: solo SMTP transaccional); lleva a [[G-14]] (Harbor: otra pieza self-hosted)
- **Idioma:** es
- **Madurez:** fork de `tomav/docker-mailserver` — proyecto comunitario activo
- **Length target:** medium (1500-2000 palabras)

**Concepto:** correr tu propio servidor de mail completo (IMAP + SMTP + filtros + antispam + DKIM + quotas + webmail) es uno de los retos clásicos de sysadmin. `docker-mailserver` (el proyecto original de Tom Volkov) lo reduce a `docker-compose up` + DNS bien configurado. El post documenta el setup real, las trampas (el famoso tema del rDNS), y la pregunta filosófica: ¿tiene sentido self-hostear tu email personal en 2026?

**Hook:** "tu propio servidor de email. IMAP. SMTP. Antispam. DKIM. Cuotas. Webmail. Todo corriendo en tu VPS. Suena a sysadmin de los 2000. Y sin embargo, en 2026, docker-mailserver hace que el setup inicial sea 30 minutos. Lo difícil no es la instalación — es *seguir vivo* los siguientes 5 años con la reputación intacta."

**Outline:**
1. Por qué alguien querría esto en 2026: soberanía de datos, curiosidad técnica, evitar Gmail/Outlook.
2. docker-mailserver: Postfix + Dovecot + SpamAssassin + ClamAV + DKIM + rspamd + config declarativa.
3. El setup: `docker-compose.yml`, MX records, SPF, DKIM, DMARC, reverse DNS, TLS con LetsEncrypt.
4. Los primeros días: el tráfico de spam legítimo, los blacklists de IPs residenciales, las blacklists de ASNs de VPS baratos.
5. El largo plazo: mantener el patch level, los upgrades de schema, los backups (ver [[G-03]]), la recuperación de desastres.
6. La pregunta honesta: ¿vale la pena? Mi respuesta: para un dominio vanity + 2-3 direcciones personales, sí. Para un dominio con familia/pareja que dependen del mail, no.
7. Cierre: el fork en mi GitHub está atado a una versión concreta; el proyecto upstream es activo y recomendado.

**Bibliografía:**
- [docker-mailserver en GitHub](https://github.com/docker-mailserver/docker-mailserver) — el proyecto upstream.
- [Mailcow — alternativa más pesada](https://mailcow.email/).
- [Poolp.org, *Postfix and OpenSMTPD* blog posts](https://poolp.org/) — referencias técnicas.
- [Migadu pricing](https://www.migadu.com/) — la alternativa honesta "email boutique".
- [Fastmail](https://www.fastmail.com/) — la otra alternativa no-bigtech.

**Imágenes:**
- _Crear_: diagrama de servicios: Postfix + Dovecot + rspamd + ClamAV + LetsEncrypt (~45 min).
- _Crear_: flujo de un mail entrante desde el remitente hasta el inbox del usuario (~30 min).

**Tags propuestos:** `['mailserver', 'Docker', 'Postfix', 'Dovecot', 'self-hosted', 'sysadmin']`

**Estado actual:** fork del proyecto comunitario, posible deployment funcional, post operativo listo para escribir.

