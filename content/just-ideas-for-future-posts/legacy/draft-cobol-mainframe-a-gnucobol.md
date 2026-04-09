### H-04 — Migrar COBOL de mainframe a GnuCOBOL en GNU/Linux

- **Archivo seed:** `dev/draft-migracion-sistema-cobol.md`
- **Slug propuesto:** `cobol-mainframe-a-gnucobol`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-cobol-mainframe-a-gnucobol/index.md`
- **Serie:** H — el caso "limpio" en contraste con [[H-01]] [[H-02]] [[H-03]]
- **Cross-links:** depende de [[H-02]] (RM/COBOL: la opción de NO migrar el COBOL); lleva a [[H-06]] (la parábola)
- **Idioma:** es
- **Madurez:** seed (2 líneas)
- **Length target:** long (2500-3500 palabras) — es el más técnico de la serie H

**Concepto:** la otra estrategia legacy. En lugar de mantener el binario y cambiar el SO debajo (como [[H-01]] [[H-02]] [[H-03]]), acá hicimos al revés: tomamos código COBOL escrito originalmente para un mainframe (IBM o similar) y lo recompilamos con GnuCOBOL en GNU/Linux. La parte interesante no es el compilador — son los miles de pequeños incompatibilidades: dialecto, JCL, archivos indexados VSAM, copybooks, codificación EBCDIC, sistema de printer.

**Hook:** "podés *no* migrar el COBOL y mantener el binario (ver [[H-02]]). O podés migrarlo de verdad, recompilando contra GnuCOBOL. Las dos son válidas. La segunda es más cara, más arriesgada, y a veces es la única opción razonable. El post cuenta cuándo elegir cuál y cómo se ve el camino limpio cuando lo elegís."

**Outline:**
1. La encrucijada: emular vs portar. Cómo decidir.
2. GnuCOBOL — historia corta. OpenCOBOL → GnuCOBOL, mantenimiento por Roger While y comunidad.
3. Compatibilidad de dialectos — IBM ANSI vs Micro Focus vs RM vs MF/Fujitsu. GnuCOBOL soporta muchos pero no todos.
4. Los problemas reales que se enfrentan al portar:
   - **JCL → shell scripts** — el control de jobs no se traduce automático.
   - **VSAM → ISAM/Berkeley DB/files planos** — qué hace GnuCOBOL.
   - **Copybooks** — convertir las copias de IBM EBCDIC packed-decimal.
   - **EBCDIC → ASCII/UTF-8** — el infierno encoding.
   - **`PERFORM ... THRU`** — semántica vs `goto`, cómo testear.
   - **`SORT`** — el verbo SORT puede llamar a un sort externo en GnuCOBOL.
5. La estrategia testing: corrida en paralelo (regression testing diferencial) sobre data real.
6. La parte deportiva: GnuCOBOL es lento comparado con un compilador comercial. ¿Importa? Sí, pero no tanto como te dicen.
7. Lo que se gana: salir del lock-in de mainframe, ahorrar licencias caras (CPU MIPS, no es chiste), poder usar git, tests modernos, deploy de [[G-05]].
8. Lo que se pierde: la confianza ciega en el sistema viejo. El sistema nuevo está en bajo escrutinio durante años.
9. Cierre: cuándo SÍ portar y cuándo dejarlo en emulación. Mi heurística personal en 3 reglas.

**Bibliografía:**
- [GnuCOBOL — sitio oficial](https://gnucobol.sourceforge.io/).
- [GnuCOBOL — Programmer's Guide](https://gnucobol.sourceforge.io/doc/gnucobol.html).
- [COBOL — Wikipedia](https://en.wikipedia.org/wiki/COBOL).
- [Carol Woodward, *Beginning COBOL for Programmers*, Apress 2014](https://link.springer.com/book/10.1007/978-1-4302-6253-4).
- [Michael Coughlan, *Beginning COBOL*, Apress 2014](https://link.springer.com/book/10.1007/978-1-4842-0396-0).
- [Mike Murphy & Frank Cohen, *Modernizing Legacy Systems*, Addison-Wesley 2003](https://www.oreilly.com/library/view/modernizing-legacy-systems/0321118847/).
- [IBM, *Enterprise COBOL Programming Guide*](https://www.ibm.com/docs/en/cobol-zos) — la referencia mainframe.
- [Reuters, *Banks scramble to find COBOL programmers as state computer systems crash during pandemic*, 2020](https://www.reuters.com/article/us-health-coronavirus-usa-cobol-idUSKBN21J7Q4) — el artículo que recordó al mundo que COBOL existe.
- [Hacker News thread sobre el post de Reuters](https://news.ycombinator.com/item?id=22790990).

**Imágenes:**
- _Crear_: tabla de equivalencias dialecto IBM ↔ GnuCOBOL para los 10 verbos más comunes (~1 hora).
- _Crear_: diagrama del flujo de testing diferencial (~30 min).
- _Crear_: gráfico de "qué se mantuvo idéntico vs qué cambió" en una migración real (~30 min).

**Tags propuestos:** `['legacy', 'COBOL', 'GnuCOBOL', 'mainframe', 'migracion', 'EBCDIC', 'arqueologia']`

**Estado actual:** seed con dos líneas; este es el post más exigente de la serie H y necesita material concreto de un proyecto real.

