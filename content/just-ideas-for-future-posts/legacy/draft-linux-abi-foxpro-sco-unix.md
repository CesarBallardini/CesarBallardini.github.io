### H-01 — Linux ABI: cómo correr FoxPro para SCO Unix en un kernel actual

- **Archivo seed:** `sysadmin/draft-dvd-live-linux-abi.md` (frontmatter ya completado, draft=true)
- **Slug propuesto:** `linux-abi-foxpro-sco-unix`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-linux-abi-foxpro-sco-unix/index.md`
- **Serie:** H — primer eslabón de la cadena legacy
- **Cross-links:** lleva a [[H-02]] (RM COBOL, otro binario SCO en Linux), [[H-03]] (FoxBase, mismo problema con sintaxis distinta), [[H-06]] (la parábola del cohete), [[A1-08]] (los lenguajes "raros" de los 80)
- **Idioma:** es
- **Madurez:** seed-with-frontmatter (título y tags ya escritos en el seed)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** durante años el kernel de Linux tuvo *Linux ABI*, un módulo que permitía cargar y ejecutar binarios compilados para SCO Unix (entre otros). Esto significaba que podías tener una empresa con FoxPro/Xbase++ corriendo desde 1992 en una máquina SCO, y un día migrar el hardware a un Linux moderno *sin recompilar*. El binario seguía funcionando. El post cuenta cómo se monta eso, los hacks que requiere, y la lección de fondo: a veces emular es más barato que portar.

**Hook:** "tenés un sistema escrito en FoxPro para SCO Unix en 1994. Funciona. Lo escribió alguien que ya no está. El código no se puede portar — son 200 mil líneas y nadie sabe cómo testearlas. La empresa lo necesita. ¿Qué hacés? Respuesta: lo corrés en un kernel Linux moderno con Linux ABI, y nadie se entera. Vamos a ver cómo."

**Outline:**
1. El problema: software escrito para un Unix comercial extinto, sin código fuente accesible o sin recursos para portarlo.
2. Qué es Linux ABI / *Personality* — el subsistema del kernel que permite ejecutar binarios COFF/ELF de otros Unixes (SCO, SVR4, Solaris x86, BSDi).
3. La historia: ABI iBCS / iBCS2 / Linux ABI. Cuándo entró al kernel, cuándo se volvió bitrot, qué pasó en 2008-2010 con la limpieza de Andrew Morton.
4. La receta práctica:
   - kernel con `CONFIG_BINFMT_COFF` y módulos `abi-*`.
   - libs compartidas de SCO copiadas en `/lib/abi/`.
   - el binario ejecutado directamente. *Funciona*.
5. El DVD live que armé para hacer esto sin tener que instalar nada — basado en Knoppix derivado, con todas las libs precargadas.
6. Lo que no funciona: drivers de hardware específicos de SCO (controladores SCSI exóticos), syscalls que cambiaron de semántica entre SCO y Linux, threading.
7. Por qué esto es la *opción correcta* en el 80% de los casos. Y por qué la opinión de "eso es legacy, hay que reescribir" es casi siempre del que no tiene que pagar la cuenta.
8. Cierre: en 2026, ¿sigue siendo viable? Sí, con el kernel < 2.6.22 o con qemu-user-static. La opción real moderna se llama Docker + qemu-user, y abre [[H-03]].

**Bibliografía:**
- [Linux iBCS — Andrew Tridgell et al, archivo histórico](https://sourceforge.net/projects/linux-abi/) — proyecto oficial.
- [Linux Kernel — *Personality* system call](https://man7.org/linux/man-pages/man2/personality.2.html).
- [Christoph Hellwig, *Removing iBCS2 support from the Linux kernel*, LKML 2008](https://lwn.net/Articles/268467/) — el momento histórico.
- [SCO OpenServer — Wikipedia](https://en.wikipedia.org/wiki/SCO_OpenServer).
- [iBCS2 — Wikipedia](https://en.wikipedia.org/wiki/Intel_Binary_Compatibility_Standard).
- [FoxPro for Unix — historia en archive.org](https://web.archive.org/web/2000*/foxpro+sco) — recursos frágiles, verificar.
- [Joel Spolsky, *Things You Should Never Do, Part I*, 2000](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — el ensayo canónico contra "rewrite from scratch".
- [Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall 2004](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — el libro que define "legacy".

**Imágenes:**
- _Crear_: diagrama de capas — kernel Linux + Linux ABI + libs SCO + binario FoxPro (~45 min).
- _Crear_: foto del DVD físico si todavía tengo el grabado original (~10 min).

**Tags propuestos:** `['legacy', 'Linux ABI', 'FoxPro', 'SCO Unix', 'kernel', 'iBCS2', 'arqueologia']`

**Estado actual:** seed con frontmatter completo y una línea de prosa; el material técnico está en mis notas de instalación.

