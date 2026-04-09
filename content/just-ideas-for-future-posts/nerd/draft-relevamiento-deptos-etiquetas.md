### J-07 — Relevamiento de departamentos: el script Python que imprimía una etiqueta por unidad

- **Archivo seed:** `github.com/CesarBallardini/relevamiento-deptos` (fork, Python, Apr 2016)
- **Slug propuesto:** `relevamiento-deptos-etiquetas`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-relevamiento-deptos-etiquetas/index.md`
- **Serie:** J
- **Cross-links:** —
- **Idioma:** es
- **Madurez:** **fork viejo (2016)**, herramienta puntual para un trabajo específico
- **Length target:** short (600-900 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** un script Python simple para agilizar el relevamiento de departamentos (unidades residenciales) — toma un CSV con direcciones y numeros, genera una etiqueta imprimible para cada uno. Lo forkeé en 2016 para un trabajo concreto de administración de consorcios. El post es una micro-anécdota sobre "cuándo el software de 100 líneas resuelve un problema real y no necesita nada más".

**Hook:** "en 2016 un amigo que administra edificios me pidió ayuda para imprimir 300 etiquetas de departamentos con dirección, piso, unidad y código de barras. No había un SaaS obvio. Había un script Python de 100 líneas que hacía exactamente eso. Lo forkeé, lo corrí, las etiquetas salieron, el trabajo se hizo. El post es la defensa del software micro que resuelve problemas micro."

**Outline:**
1. El problema: imprimir 300 etiquetas de departamentos desde un CSV.
2. El script Python (ReportLab o similar): 100 líneas, sin tests, sin docs.
3. Lo que aprendí: a veces el software "serio" es hostil al problema pequeño. Los scripts de fin de semana ganan.
4. Cierre: el fork sigue ahí, funciona si lo necesitás.

**Bibliografía:**
- [ReportLab — Python PDF library](https://www.reportlab.com/).
- [csv — Python stdlib](https://docs.python.org/3/library/csv.html).

**Imágenes:**
- _Crear_: screenshot de una etiqueta generada (anonimizada) (~10 min).

**Tags propuestos:** `['Python', 'ReportLab', 'CSV', 'etiquetas', 'script', 'nerd lateral']`

**Estado actual:** fork viejo, proyecto puntual. Post micro.

