### E-07 — dbaid: la herramienta que escribí porque no encontré ninguna

- **Archivo seed:** `dev/draft-dbaid.md`
- **Slug propuesto:** `dbaid-herramienta-personal`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-dbaid-herramienta-personal/index.md`
- **Serie:** E
- **Cross-links:** lleva a [[E-02]] (fixperm — el patrón "me lo escribo yo"), [[H-03]] (sistemas legacy donde dbaid sería útil)
- **Idioma:** es
- **Madurez:** bare-seed (archivo vacío)
- **Length target:** short (800-1200 palabras)

**Concepto:** *dbaid* (db-aid, asistente de base de datos) fue una utilidad chiquita que escribí porque ninguna de las herramientas existentes hacía lo que yo necesitaba para una migración / inspección / comparación de esquemas (revisar exactamente el caso al desempolvar el material). El post no es sobre la herramienta — es sobre el patrón: *cuándo conviene escribirte tu propia herramienta y cuándo no*.

**Hook:** "tengo una carpeta `bin/` con 30 scripts y herramientas que escribí porque no encontré la que necesitaba. La mayoría tienen 50 líneas. Una se llama *dbaid*. El post no es sobre dbaid — es sobre por qué la regla *no reinventes la rueda* es mala consejera el 30% del tiempo."

**Outline:**
1. Qué hacía dbaid exactamente (reconstruir del recuerdo y/o del código si lo encuentro).
2. Por qué no usé herramienta X (las opciones que existían en ese momento).
3. La economía honesta: 4 horas de escribir vs 4 horas semanales repitiendo el workflow manual. El break-even llega rápido.
4. La regla — cuándo escribirte la tuya:
   - el problema es muy específico de tu contexto;
   - las herramientas existentes son 10x más complejas de lo que necesitás;
   - vas a aprender el dominio escribiéndola.
5. Cuándo NO escribirla: cuando el dominio está bien resuelto y vos sólo no encontraste la herramienta correcta.
6. La trampa: el 80% de los `bin/` privados de la gente son re-implementaciones malas de cosas que ya existen. Esto es real y no me incluyo.
7. Cierre: el código de dbaid sigue (o no) en alguna cinta.

**Bibliografía:**
- [Mike Gancarz, *The Unix Philosophy*, Digital Press 1995](https://archive.org/details/unixphilosophy0000ganc) — la filosofía detrás del patrón.
- [Eric S. Raymond, *The Art of Unix Programming*, Addison-Wesley 2003](http://www.catb.org/~esr/writings/taoup/html/).
- [Brian Kernighan, *The Practice of Programming*](https://archive.org/details/practiceofprogra00kern), Addison-Wesley 1999.
- [Joel Spolsky, *In Defense of Not-Invented-Here Syndrome*, 2001](https://www.joelonsoftware.com/2001/10/14/in-defense-of-not-invented-here-syndrome/) — el contrapunto al "no reinventes la rueda".
- [The Pragmatic Programmer (1999)](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) — capítulo sobre construir herramientas.

**Imágenes:**
- _Crear_: ninguna — post corto y narrativo.
- _Opcional_: si encuentro el código, screenshot del help text original.

**Tags propuestos:** `['memoir', 'herramientas', 'NIH', 'Unix', 'dbaid']`

**Estado actual:** archivo vacío; necesita arqueología en backups antiguos para reconstruir el caso de uso real.

