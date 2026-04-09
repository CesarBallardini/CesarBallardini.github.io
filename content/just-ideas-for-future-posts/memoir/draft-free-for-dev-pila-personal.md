### E-15 — free-for-dev: mi pila personal de hobby projects contra el costo cero

- **Archivo seed:** `github.com/CesarBallardini/free-for-dev` (fork del conocido índice de servicios con tier gratis para devs)
- **Slug propuesto:** `free-for-dev-pila-personal`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-free-for-dev-pila-personal/index.md`
- **Serie:** E — memoir operativo de cómo mantengo hobby projects sin gastar plata
- **Cross-links:** lleva a [[G-14]] (Harbor como alternativa self-hosted a Docker Hub pago), [[G-24]] (cuttlefish SMTP — self-hosted alternative), [[G-25]] (mailserver en Docker)
- **Idioma:** es
- **Madurez:** fork del índice comunitario + mi selección personal de tools en uso
- **Length target:** short-medium (1000-1500 palabras)

**Concepto:** [free-for-dev](https://github.com/ripienaar/free-for-dev) es un índice comunitario de servicios SaaS/PaaS/IaaS que tienen un free tier útil para desarrolladores. Lo forkeé hace años. El post no es el índice — es *mi selección de los servicios que realmente uso* para hobby projects en 2026, con los criterios de elección, los límites con los que me pegué, y la comparación honesta con las alternativas self-hosted ([[G-14]] [[G-24]] [[G-25]]).

**Hook:** "mi blog está en GitHub Pages (gratis). Mi DNS en Cloudflare (gratis). Mis secrets en 1Password free tier. Mi CI en GitHub Actions (gratis para repos públicos). Mi tracking de visitas en Plausible self-hosted. Mi backup en Backblaze B2 (gratis hasta 10 GB). Llevo años operando así. El post es el catálogo: qué servicios uso, qué límites tienen, cuándo me molesté en levantar self-hosted, cuándo me quedé con el gratis."

**Outline:**
1. La regla de partida: hobby project → nada de plata mensual. Todo gratis o self-hosted.
2. La pila que uso hoy: hosting (GitHub Pages, Cloudflare Pages, Netlify), DNS (Cloudflare), CI/CD (GitHub Actions), storage (Backblaze B2, archive.org), email transaccional (postmark free/SES/self-hosted Cuttlefish), analytics (Plausible self-hosted), registry (Harbor self-hosted), DB managed (Supabase free, Neon free).
3. Los servicios que probé y abandoné: Heroku (ya no hay tier gratis), AWS Free Tier (la trampa de los 12 meses), etc.
4. Los límites reales: cuándo un free tier empieza a doler. La discusión de "cuánto vale tu tiempo vs $5/mes".
5. La frontera con self-hosted: cuándo conviene levantar Cuttlefish vs usar Mailgun, Harbor vs Docker Hub, Plausible vs Google Analytics.
6. Cierre: el catálogo actualizado es `github.com/CesarBallardini/free-for-dev` — aceptar PRs.

**Bibliografía:**
- [free-for-dev en GitHub](https://github.com/ripienaar/free-for-dev) — el índice original.
- [Cloudflare pricing](https://www.cloudflare.com/plans/) — el proveedor más usado.
- [GitHub Actions pricing](https://github.com/pricing) — límites del free tier.
- [Backblaze B2 pricing](https://www.backblaze.com/b2/cloud-storage-pricing.html).
- [Plausible self-hosted docs](https://plausible.io/docs/self-hosting).

**Imágenes:**
- _Crear_: tabla "servicio / qué uso / límite / alternativa self-hosted" (~30 min).
- _Crear_: diagrama de la pila hobby-project-zero-cost (~45 min).

**Tags propuestos:** `['free-for-dev', 'hobby projects', 'self-hosted', 'SaaS', 'devops', 'memoir']`

**Estado actual:** fork del índice + material operativo en uso diario. Post fácil — una tarde.

