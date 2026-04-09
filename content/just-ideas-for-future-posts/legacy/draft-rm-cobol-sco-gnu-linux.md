### H-02 — RM/COBOL bajo SCO Unix migrado a GNU/Linux: el binario que sobrevivió 25 años

- **Archivo seed:** `sysadmin/draft-rm-cobol-en-gnu-linux.md`
- **Slug propuesto:** `rm-cobol-sco-gnu-linux`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-rm-cobol-sco-gnu-linux/index.md`
- **Serie:** H
- **Cross-links:** depende de [[H-01]] (Linux ABI explicado); lleva a [[H-04]] (COBOL→GNU/COBOL como el camino "limpio"), [[H-06]] (la parábola del cohete)
- **Idioma:** es
- **Madurez:** seed (3 líneas en el seed)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** RM/COBOL (Ryan-McFarland, después Liant) es uno de esos COBOL comerciales que la mayoría de los desarrolladores nunca oyó nombrar. Lo encontré en una empresa que lo había instalado en SCO Unix en 1996 y lo seguía corriendo en 2018. La migración no fue "portar el COBOL" — fue migrar el sistema operativo de abajo, dejando los binarios RM/COBOL intactos sobre Linux ABI. El post explica los pasos exactos, los problemas con archivos indexados (ISAM) y por qué el resultado fue 100% transparente para los usuarios.

**Hook:** "RM/COBOL no es GNU/COBOL. RM/COBOL es Ryan-McFarland, después Liant, después Micro Focus. Es comercial, es propietario, no se compila — *es* un binario. Y en 2018 me tocó migrarlo de SCO Unix, una plataforma extinta, a Linux moderno, sin tocar una sola línea del COBOL original. Funcionó. Acá está cómo."

**Outline:**
1. Qué es RM/COBOL (y el chiste de los nombres: Ryan-McFarland → Liant → Micro Focus → otra adquisición).
2. El runtime: `runcobol` ejecuta los `.cob` precompilados, que son binarios opacos.
3. Por qué la migración "natural" (recompilar con GnuCOBOL) era inviable en este caso: dialecto, pragmas comerciales, librerías de terceros.
4. La estrategia elegida: dejar el sistema operativo de abajo cambiar (SCO → CentOS) y mantener los binarios RM/COBOL intactos sobre Linux ABI ([[H-01]]).
5. Los problemas concretos:
   - **archivos indexados ISAM** — RM/COBOL usa su propio formato; reverificar índices con `rmiutl`.
   - **layout de archivos en disco** — paths con `:` que SCO permitía y Linux no.
   - **terminales** — SCO usaba `ansicus`/`ansicfg`, Linux usa `terminfo`.
   - **printers** — el sistema de impresión cambió de `lp` SVR4 a CUPS.
6. La validación: cómo armé un set de tests "diferenciales" — corrí el sistema viejo y el nuevo en paralelo durante dos meses, comparando outputs.
7. Lo que aprendí: cuando el cliente dice "no toques nada que funciona", a veces tiene razón.
8. Cierre: este sistema sigue corriendo. Lo último que supe fue que la empresa quería sumarle una API REST. Eso lleva a [[H-04]].

**Bibliografía:**
- [Micro Focus RM/COBOL — página actual](https://www.microfocus.com/en-us/products/rm-cobol/overview) — donde fue a parar Liant.
- [GnuCOBOL — sitio oficial](https://gnucobol.sourceforge.io/) — la alternativa libre.
- [Liant Software — Wikipedia](https://en.wikipedia.org/wiki/Liant_Software) — historia corporativa.
- [SCO OpenServer — terminfo conversion](https://www.sco.com/) — recursos frágiles.
- [Mike Murphy & Frank Cohen, *Modernizing Legacy Systems*, Addison-Wesley 2003](https://www.oreilly.com/library/view/modernizing-legacy-systems/0321118847/) — el libro de referencia.
- [The Computerworld 1996 article on RM/COBOL](https://archive.org/search?query=rm+cobol+1996) — testimonio histórico.
- [GNU Cobol Programming Group on COBOL dialects](https://gnucobol.sourceforge.io/doc/) — diferencias entre dialectos.

**Imágenes:**
- _Crear_: diagrama de la migración — antes (SCO + RM/COBOL) y después (Linux + Linux ABI + RM/COBOL) (~30 min).
- _Crear_: tabla de los 4 problemas concretos y sus soluciones (~20 min).

**Tags propuestos:** `['legacy', 'RM COBOL', 'SCO Unix', 'Linux ABI', 'migracion', 'arqueologia']`

**Estado actual:** seed con tres líneas; el material existe en notas de migración del proyecto real.

