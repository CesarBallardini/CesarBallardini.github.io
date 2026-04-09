### J-06 — Automagica: generar un libro listo para imprenta con LaTeX (y tres Biblias antiguas)

- **Archivo seed:** `github.com/CesarBallardini/automagica` (fork, TeX, Oct 2017) — hermano de [[J-04]] (Reina-Valera 1865 y Geneva 1564)
- **Slug propuesto:** `automagica-libros-latex-imprenta`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-automagica-libros-latex-imprenta/index.md`
- **Serie:** J
- **Cross-links:** depende de [[J-04]] (Biblias históricas — caso de uso); lleva a [[I-02]] (digitalización)
- **Idioma:** es
- **Madurez:** fork funcional, caso de uso real con tres proyectos de Biblias
- **Length target:** short-medium (1000-1500 palabras)
- **⚠️ Etiqueta de serie:** Curiosidad nerd lateral — no es CS

**Concepto:** *automagica* es un fork de un proyecto en TeX que genera automáticamente libros listos para imprenta (PDF interior + tapa + contratapa con dimensiones exactas para servicios tipo Lulu / Amazon KDP / Bibliomanía) a partir de un Markdown/LaTeX fuente. El post describe el sistema y lo cruza con [[J-04]] (mi proyecto de tipografiar la Reina-Valera 1865 y la Biblia de Ginebra 1564), porque es el mismo stack: TeX + scripts + pipelines para convertir texto limpio en objeto físico imprimible.

**Hook:** "tenés un texto. Querés un libro físico. No querés pasar por un diseñador. Querés que un script Make lo genere listo para Lulu o KDP. Automagica hace eso con LaTeX + scripts. El post cuenta el sistema y cómo lo usé para tipografiar tres Biblias históricas."

**Outline:**
1. El problema: self-publishing técnico sin diseñador profesional.
2. Automagica: LaTeX + scripts + Makefile + templates de cover.
3. El workflow: Markdown → LaTeX → PDF interior + PDF tapa.
4. El cruce con [[J-04]]: las tres Biblias como caso de uso (Reina-Valera 1865, Geneva 1564, y la tercera que esté en desarrollo).
5. Las trampas: fonts libres que tengan glifos antiguos, hyphenation para español antiguo, CMYK vs RGB en las tapas.
6. Cierre: si querés auto-publicar un libro técnico sin diseñador, este es el camino.

**Bibliografía:**
- [automagica en GitHub (upstream)](https://github.com/jorgearaya/automagica) — verificar el upstream.
- [LaTeX book class documentation](https://www.latex-project.org/help/books/).
- [memoir package en CTAN](https://www.ctan.org/pkg/memoir) — el paquete para libros.
- [Lulu printing specs](https://www.lulu.com/).
- [Amazon KDP print options](https://kdp.amazon.com/).

**Imágenes:**
- _Crear_: screenshot de un libro generado por automagica (~15 min).
- _Crear_: diagrama del pipeline Markdown → LaTeX → PDF → impresora (~30 min).

**Tags propuestos:** `['LaTeX', 'self-publishing', 'libros', 'automagica', 'Biblias', 'nerd lateral']`

**Estado actual:** fork + caso de uso real. Post fácil, complementa [[J-04]].

