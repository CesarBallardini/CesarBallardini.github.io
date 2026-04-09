### H-12 — Hercules `prtspool`: imprimir desde MVS 3.8 a PDF

- **Archivo seed (repo POC):** [github.com/CesarBallardini/hercules-prtspool](https://github.com/CesarBallardini/hercules-prtspool) — C, último push 2021-11-19
- **Slug propuesto:** `hercules-prtspool-imprimir-mvs-pdf`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-hercules-prtspool-imprimir-mvs-pdf/index.md`
- **Serie:** H — apéndice técnico de [[H-10]]
- **Cross-links:** depende de [[H-10]]
- **Idioma:** es
- **Madurez:** **complete-poc** (custodia de la herramienta de Tim Pinkawa)
- **Length target:** short (800-1200 palabras)

**Concepto:** cuando hacés un job en MVS 3.8 y mandás output a impresora, MVS lo manda al device 00E (la "impresora de líneas"). Hercules emula ese device como un archivo plano. Si querés *ver* el output como lo verías en una impresora real, necesitás un postprocesador. Tim Pinkawa escribió `prtspool`, una herramienta C chica que convierte el archivo crudo en PDF. Mi repo es la custodia (con permiso) del código y la documentación de Tim, que originalmente vivía en una página personal frágil.

**Hook:** "submitís un job COBOL en tu MVS 3.8j de Hercules. El output va al spooler de impresora. Lo querés ver. ¿Cómo? Con `prtspool`, una herramienta de 200 líneas en C que toma el spool crudo y te lo entrega como PDF, listo para abrir. La escribió Tim Pinkawa. La preservé en mi repo."

**Outline:**
1. El problema: Hercules emula la impresora como un archivo plano sin forma.
2. La solución: `prtspool`.
3. Quién es Tim Pinkawa y por qué la herramienta está en mi repo (preservación).
4. El flujo paso a paso: submit job → output a spool → `prtspool` → PDF.
5. Un job de ejemplo: "hello world" en COBOL, output al spooler, conversión, abrir el PDF.
6. Cierre: por qué las herramientas chicas como esta son el alma del ecosistema Hercules.

**Bibliografía:**
- Repo del POC: [CesarBallardini/hercules-prtspool](https://github.com/CesarBallardini/hercules-prtspool).
- [Hercules — sitio oficial](http://www.hercules-390.org/).
- Cross-link [[H-10]] [[H-04]].

**Imágenes:**
- _Crear_: screenshot del PDF generado de un job COBOL (~10 min).
- _Crear_: ASCII del flujo (~10 min).

**Tags propuestos:** `['Hercules', 'MVS', 'prtspool', 'PDF', 'COBOL', 'mainframe', 'arqueologia']`

**Estado actual:** **complete-poc**, herramienta funcional preservada.

