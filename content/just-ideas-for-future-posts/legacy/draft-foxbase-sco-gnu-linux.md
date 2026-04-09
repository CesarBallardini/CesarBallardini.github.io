### H-03 — FoxBase para SCO migrado a GNU/Linux

- **Archivo seed:** `sysadmin/draft-sco-foxbase-en-gnu-linux.md`
- **Slug propuesto:** `foxbase-sco-gnu-linux`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-foxbase-sco-gnu-linux/index.md`
- **Serie:** H
- **Cross-links:** depende de [[H-01]] (Linux ABI); lleva a [[H-07]] (Trac en MinCultura — el ministerio donde corrió este FoxBase), [[H-06]] (la parábola)
- **Idioma:** es
- **Madurez:** seed (2 líneas)
- **Length target:** medium (1200-1800 palabras)

**Concepto:** FoxBase (el ancestro de FoxPro, Microsoft Visual FoxPro, etc.) tuvo una versión para Unix que vendía Fox Software antes de la compra por Microsoft. Es un binario más simple que RM/COBOL, pero los archivos `.dbf` con los que trabaja son lo verdaderamente interesante: el formato sigue siendo legible por casi cualquier herramienta moderna. El post cuenta la migración del binario (mismo patrón que [[H-02]]) pero también el sub-proyecto de migrar los DBF a PostgreSQL en paralelo.

**Hook:** "FoxBase es el padre de FoxPro. Funcionaba en SCO Unix en una época en que MS-DOS no tenía red. Cuando Microsoft compró Fox Software en 1992, dejó morir la versión Unix en 18 meses. Las empresas que la habían comprado se quedaron con sistemas que no se podían actualizar. Y esos sistemas, en muchos casos, siguieron andando. Veintidós años después me tocó mover uno."

**Outline:**
1. El árbol genealógico: dBase → FoxBase → FoxPro → Visual FoxPro → muerte oficial 2007. Cada paso es un cambio de empresa.
2. FoxBase para Unix — lo que la mayoría no sabe: existió, estuvo bien hecho, lo mató Microsoft.
3. La estrategia migración (mismo patrón que [[H-02]]): kernel Linux moderno + Linux ABI + binario de FoxBase intacto.
4. Lo más interesante NO es el binario — es el formato `.dbf`. Sigue siendo legible en 2026 con herramientas modernas (`dbfview`, GDAL para los espaciales, librerías Python).
5. El sub-proyecto paralelo: migrar los DBF a PostgreSQL para que el sistema *nuevo* (escrito desde cero, en paralelo, durante años) pudiera leer los datos sin involucrar a FoxBase.
6. La trampa: los códigos de carácter. FoxBase usaba CP850 / CP437; la migración a UTF-8 con tildes y eñes fue su propio infierno.
7. Cierre: la lección de portabilidad de formato — *el formato sobrevive al programa*. Si vas a apostar a algo, apostá al formato.

**Bibliografía:**
- [FoxBase — Wikipedia](https://en.wikipedia.org/wiki/FoxBASE).
- [Visual FoxPro end of life — Microsoft, 2007](https://learn.microsoft.com/en-us/previous-versions/visualstudio/foxpro/) — el anuncio.
- [dBase file format — Wikipedia](https://en.wikipedia.org/wiki/.dbf).
- [Especificación del formato DBF — devx.com](https://www.dbf2002.com/dbf-file-format.html) — referencia frágil.
- [GDAL — soporte para DBF](https://gdal.org/drivers/vector/shapefile.html) — leer dbf en Python moderno.
- [Python — `dbfread` library](https://dbfread.readthedocs.io/).
- [Joel Spolsky, *The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode*, 2003](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) — para la sección de codificación.

**Imágenes:**
- _Crear_: diagrama del árbol genealógico FoxBase → FoxPro → muerte (~30 min).
- _Crear_: side-by-side de un registro `.dbf` legible vs SQL equivalente en Postgres (~20 min).

**Tags propuestos:** `['legacy', 'FoxBase', 'SCO Unix', 'DBF', 'PostgreSQL', 'arqueologia']`

**Estado actual:** seed con dos líneas; cruza con [[H-07]] (Trac en MinCultura) por ser el mismo proyecto.

