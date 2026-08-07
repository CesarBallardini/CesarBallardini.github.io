### A1-13 — Masterminds of Programming: roster completo de las 17 entrevistas

- **Archivo seed:** _draft-rest.md bucket 4 (cosechado 2026-04-09)_
- **Slug propuesto:** `masterminds-roster-completo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-masterminds-roster-completo/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[E-09]] (Masterminds reseña), [[A1-14]]..[[A1-NN]] (entradas por lenguaje individual)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium-long (2000-2600 palabras) — fijado el 2026-07-15: es un índice anotado de 17 entradas, necesita aire para agrupar y comentar, pero no es un ensayo

**Concepto:** Listado completo de las 17 entrevistas del libro *Masterminds of Programming* (Biancuzzi & Warden, O'Reilly 2009): APL (Falkoff), BASIC (Kurtz), FORTH (Moore), ML (Milner), SQL (Chamberlin), AWK (Aho/Weinberger/Kernighan), PostScript (Geschke/Warnock), C++ (Stroustrup), Eiffel (Meyer), Objective-C (Cox/Love), Perl (Larry Wall), Haskell (SPJ/Hudak/Wadler/Hughes), Python (van Rossum), Lua (de Figueiredo/Ierusalimschy), Java (Gosling), UML (Booch/Jacobson/Rumbaugh), Delphi/C# (Hejlsberg). Este post es el índice anotado para usar como hoja de ruta del libro.

**Hook:** 17 lenguajes. 17 cabezas. 1 libro. Esta es la hoja de ruta para leerlo en orden y no perderse.

**Outline:**

1. **Hook — 17 lenguajes, 17 cabezas, 1 libro.** Qué es este post: la hoja de ruta, no la reseña. La reseña subjetiva es [[E-09]].
2. **Cómo está armado el libro.** Un capítulo por lenguaje, formato Q&A largo. Por qué eso cambia cómo se lee: no hay narrador, hay transcripción.
3. **El roster completo.** Tabla de las 17 entrevistas con lenguaje y entrevistados, en el orden del libro.
4. **El problema del orden.** Por qué leerlo de la primera a la última página es la peor opción, y cuatro rutas alternativas.
5. **Grupo 1 — los que empezaron como notación o como pedagogía:** APL, BASIC, FORTH, ML.
6. **Grupo 2 — los que se te metieron en el trabajo sin que los eligieras:** SQL, AWK, PostScript.
7. **Grupo 3 — la pelea por los objetos:** C++, Eiffel, Objective-C.
8. **Grupo 4 — los lenguajes de la gente:** Perl, Python, Lua.
9. **Grupo 5 — la teoría que bajó a producción:** Haskell.
10. **Grupo 6 — los que tuvieron dueño:** Java, Delphi/C#, y UML como el intruso que no es un lenguaje de programación.
11. **Las ausencias.** Qué falta en el roster y qué dice eso del libro y de su fecha.
12. **Plan de lectura concreto.** Dónde bajarlo y cómo repartir 17 entrevistas sin abandonar en la cuarta.
13. **Cierre — el hilo que atraviesa las 17.**

**Bibliografía:** _(pasada de fuentes 2026-07-15 — todas las URLs de abajo fueron fetcheadas y verificadas)_

**La fuente primaria**

- [[tr-23]] Biancuzzi, F. & Warden, S. (eds.), *Masterminds of Programming: Conversations with the Creators of Major Programming Languages*, O'Reilly Media, 1.ª ed. marzo 2009, 496 pp., ISBN 978-0-596-51517-1. Prólogo de Sir Tony Hoare. — **estable**
- **Ítem CDL (el que se enlaza):** <https://archive.org/details/mastermindsofpro0000unse> — préstamo digital controlado. — **estable**
- **Ítem de descarga libre (subida de usuario «usege», 2015):** <https://archive.org/details/MastermindsOfProgramming> — PDF/ePub/texto completo. Copia con copyright vigente subida por un tercero; **no** es una edición liberada por O'Reilly. Es la fuente sobre la que se verificó el índice. — **estable** (pero de legalidad dudosa: ver nota en el borrador)
- **Texto completo (donde se verificó el índice, el prefacio y la página de créditos):** <https://archive.org/stream/MastermindsOfProgramming/Masterminds%20of%20Programming_djvu.txt> — **estable**

**Confirmación independiente del roster**

- Reseña de ACCU (Association of C and C++ Users): <https://accu.org/bookreviews/2024/bruntlett_2025/> — confirma los 17 lenguajes y su orden, el prólogo de Hoare, ~26 pp./capítulo y ~15 pp. de biografías. — **frágil** → backup: <http://web.archive.org/web/20251027215603/https://accu.org/bookreviews/2024/bruntlett_2025/>

**Para las afirmaciones técnicas del post (fuentes de los propios autores)**

- Stroustrup, B., «A History of C++: 1979–1991», HOPL-2 (ACM), marzo 1993: <https://www.stroustrup.com/hopl2.pdf> — respalda «Simula para organizar + C para la eficiencia» con la primera oración del paper. — **frágil** (sitio personal) → backup: <http://web.archive.org/web/20260703213554/https://www.stroustrup.com/hopl2.pdf>
- Cox, B. L., «The object oriented pre-compiler: programming Smalltalk 80 methods in C language», *ACM SIGPLAN Notices* 18(1), 1983, pp. 15-22. DOI: <https://doi.org/10.1145/948093.948095> — respalda «Smalltalk sobre C». ACM DL da 403; metadatos verificados vía Crossref: <https://api.crossref.org/works/10.1145/948093.948095>. — **estable** (DOI)
- Gordon, M., «From LCF to HOL: a short history», en *Proof, Language, and Interaction*, MIT Press, 2000, ISBN 0262161885. Archivo del autor en Cambridge: <https://www.cl.cam.ac.uk/archive/mjcg/papers/HolHistory.html> · PDF: <https://www.cl.cam.ac.uk/archive/mjcg/papers/HolHistory.pdf> — respalda ML como «Meta Language» de LCF, y LCF como sistema de Milner en Stanford, 1972. — **estable** (dominio institucional) → backup del HTML: <http://web.archive.org/web/20260206100221/https://www.cl.cam.ac.uk/archive/mjcg/papers/HolHistory.html>

**Pista para el capítulo de Objective-C, si se quiere profundizar (no usada en el borrador)**

- Cox, B. J., Naroff, S. & Hsu, H., «The origins of Objective-C at PPI/Stepstone and its evolution at NeXT», *Proceedings of the ACM on Programming Languages*, vol. 4, n.º HOPL (2020), pp. 1-74. DOI: <https://doi.org/10.1145/3386332> — **CC BY 4.0** según Crossref (<https://api.crossref.org/works/10.1145/3386332>), pero el PDF en ACM DL devuelve 403 a fetch automatizado y **no se pudo leer en esta pasada**: no se citó ninguna afirmación suya. Historia de Objective-C escrita por el propio Cox; candidato fuerte para [[A1-NN]]. — **estable** (DOI)

**Descartadas en esta pasada**

- `oreilly.com/library/view/masterminds-of-programming/9780596801670/` y `oreilly.com/pub/pr/2277` (gacetilla de prensa) — HTTP 403 a fetch automatizado; no verificables.
- `library.villanova.edu/Find/Record/2211750/TOC` — devuelve «Verifying your access…», sin contenido real.
- Sitios de PDFs piratas (dokumen.pub, epdf.pub, bookey) que aparecen alto en las búsquedas — descartados por principio.
- `amturing.acm.org` (página de Milner) — HTTP 403; se reemplazó por el archivo de Gordon en Cambridge, que además es mejor fuente (Gordon trabajó en LCF con Milner).

**Imágenes:** _a definir_

**Tags propuestos:** `['libros','Masterminds','lenguajes','roster','historia']`

**Estado actual:**

⚠️ **PREMISA EN DUDA — el orden del roster estaba mal, y con él se cayó una sección entera.** (Pasada de fuentes, 2026-07-15.) El `**Concepto:**` de este draft lista los 17 lenguajes en un orden que **no es el del libro**: el `Concepto` arranca por APL/BASIC/FORTH, y el libro arranca por **C++ y Python**. La *nómina* del `Concepto` es correcta —los 17 lenguajes y sus entrevistados están todos bien, salvo que el capítulo 13 se titula «C#» y no «Delphi/C#»—, pero el *orden* no. El `Concepto` y el `Hook` no se tocaron (son de César), pero queda anotado que el orden del `Concepto` no es citable como orden del libro.

Consecuencia grande: la sección «El problema del orden» del borrador se apoyaba en «la primera entrevista del libro es APL, la segunda es BASIC» para argumentar que el libro se abandona porque empieza cuesta arriba. **Eso es falso** y el argumento no se sostiene. Se reescribió el tramo (el libro abre por C++ y Python como rampa de entrada deliberada; el escalón duro llega en los capítulos 3-5 y 8-9), con nota de corrección visible en el cuerpo. **César: ese párrafo de reemplazo es de Claude y necesita tu voz y tu criterio.** El `Hook` («17 lenguajes, 17 cabezas, 1 libro, esta es la hoja de ruta») sobrevive intacto: el post sigue siendo exactamente lo que dice ser.

✅ **Resuelto el conflicto Erlang/Clojure que bloqueaba este draft y [[E-09]].** El índice real del libro **no tiene Erlang ni Clojure**: Joe Armstrong y Rich Hickey **no** fueron entrevistados. La tabla de este draft (corregida de orden) es la buena; **la nota equivocada está en [[E-09]]** y hay que arreglarla cuando se trabaje ese draft. Control cruzado que cierra la cuestión: el prefacio dice «27 great designers» y la suma de entrevistados del roster verificado da exactamente 27 — no sobra lugar para dos entrevistados más.

**Fuentes de la pasada:** el índice, el prefacio y la página de créditos se verificaron sobre el texto completo del ítem de archive.org, y se confirmaron de manera **independiente** contra la reseña de ACCU (mismos 17 lenguajes, mismo orden, mismo prólogo de Hoare). Las afirmaciones técnicas del post ahora se apoyan en fuentes de los propios autores: Stroustrup (su paper de HOPL-2, en su sitio) para «Simula + C», Cox (SIGPLAN Notices 1983, vía DOI) para «Smalltalk sobre C», y Gordon (archivo de Cambridge) para ML como «Meta Language» de LCF. Ver `**Bibliografía:**`, con flags de bitrot y backups de Wayback para las frágiles.

**De 17 marcas `[VERIFICAR:]` quedan 2**, las dos honestas:

- **La ventana temporal de las entrevistas.** El libro no la declara (busqué en el prefacio y en el texto completo); las páginas de O'Reilly que podrían tenerla dan 403. Pendiente: Wayback sobre la gacetilla, o posts de Biancuzzi de 2008-2009.
- **Las fechas de vida de Ritchie/Kay/McCarthy**, si se quiere argumentar las ausencias por quién estaba entrevistable en 2008-2009. No las verifiqué, así que no las escribí.

**Hallazgo lateral con consecuencia editorial:** hay **dos** ítems de archive.org, no uno. El que anotaba el seed (`MastermindsOfProgramming`) es una subida de un usuario particular de 2015 con el PDF a descarga libre — un O'Reilly de 2009 con copyright vigente, no una edición liberada. El legítimo es `mastermindsofpro0000unse`, en préstamo digital controlado. El borrador ahora hace la distinción y enlaza el de CDL; **queda un hueco nuevo para César** decidiendo si enlazar o no la copia libre.

Datos de edición confirmados para el frontmatter y las citas: O'Reilly, 1.ª edición **marzo de 2009**, **496 pp.**, ISBN **978-0-596-51517-1**, prólogo de **Sir Tony Hoare**, cierre con *Afterword* + ~15 pp. de *Contributors* + índice.

---

_Historial:_ seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (13 secciones), se fijó `Length target: medium-long (2000-2600 palabras)` y se escribió un borrador de prosa completo (~2150 palabras de prosa efectiva, sin contar marcas de verificación ni huecos) en la sección «Borrador de prosa» al pie.

Lo que quedó **escrito**: el encuadre entero (este post es la hoja de ruta, [[E-09]] es la reseña), la explicación del formato Q&A y por qué cambia la lectura, la tabla del roster, el argumento contra leerlo en orden de tapa a tapa, los seis agrupamientos temáticos con su justificación, la sección de ausencias, el plan de lectura y el cierre. El armazón se sostiene solo: es un post de servicio y la estructura es el 80% del trabajo.

Lo que quedó como **hueco**:

- 8 huecos `🕳️` pidiendo a César lo que sólo puede poner él: cuándo y cómo consiguió el libro, cuáles entrevistas leyó y cuáles no, qué le dejó la de Chamberlin después de años de SQL, su opinión sobre Perl, si el caso Lua le resuena con algo real del sector público de Santa Fe, cuál es la ruta de lectura que él realmente recomienda, cómo lo leyó de verdad, y el veredicto del cierre. Sin eso el post es una tabla de contenidos con comentarios — útil, pero no es katra.
- _(superado por la pasada de fuentes del 2026-07-15: de estas 17 marcas quedan 2 — ver arriba)_ 17 marcas `[VERIFICAR:]` sobre datos que la bibliografía listada **no** respalda: el orden real de los capítulos del libro, la nómina exacta de entrevistados por capítulo (el Concepto los trae por apellido y los nombres de pila de la tabla están completados de memoria), el caso de Objective-C («Cox/Love»), si Waldemar Celes aparece en el capítulo de Lua, si los cuatro de Haskell están en un solo capítulo, si el libro trae prólogo o material editorial además de las entrevistas, la fecha de las entrevistas frente a la de publicación, el origen de ML como metalenguaje de LCF, la caracterización C++/Simula vs Objective-C/Smalltalk, y el estado legal y la URL exacta del ítem de archive.org. Tres marcas más cuelgan de lo mismo: las afirmaciones «ninguna mujer entre los 17», «única entrevista latinoamericana» y la lista de ausencias (C, Ruby, JavaScript) sólo se sostienen si el roster de la tabla es correcto y completo — son fuertes y equivocarse ahí sería feo.
- ✅ _(RESUELTO el 2026-07-15: no hay ni Erlang ni Clojure en el libro; el que está mal es [[E-09]] — ver arriba)_ ⚠️ **Conflicto interno del plan, hay que resolverlo antes de escribir cualquiera de los dos posts:** el `**Concepto:**` de este draft lista 17 entrevistas y **no** incluye Erlang ni Clojure, pero el draft de [[E-09]] afirma en su outline que Joe Armstrong (Erlang) y Rich Hickey (Clojure) fueron entrevistados — y a la vez, más abajo, que Hickey *no* está en el libro. Los dos drafts no pueden tener razón. Hay que abrir el índice real del libro y corregir el que esté mal. La prosa de este borrador deja el punto marcado y no lo resuelve por su cuenta.
- `**Imágenes:**` sigue en `_a definir_`. Para un post-índice el candidato natural es una imagen propia (la tabla del roster renderizada, o una foto de la tapa) más que Wikimedia; decidir antes de correr `hugo new`.
- El post lleva tabla markdown → acordarse de `page_css: ['tables.css']` en el frontmatter al publicar.

---

## Borrador de prosa

17 lenguajes. 17 cabezas. 1 libro.

*Masterminds of Programming*[^masterminds] hace una sola cosa, y la hace 17 veces: sienta a los creadores de un lenguaje de programación y les pregunta qué hicieron, por qué, y qué harían distinto. No es un libro de historia escrito por un historiador. Son las transcripciones, con los tipos hablando.

Este post no es la reseña —esa la escribí aparte, en [[E-09]], y ahí cuento cuáles me sacudieron y por qué—. Este post es la hoja de ruta: el roster completo, agrupado, con una idea de en qué orden meterle mano. Porque el libro tiene un problema logístico que nadie te avisa, y es que 17 entrevistas largas leídas de corrido, en el orden en que vienen, te funden.

### El formato importa más de lo que parece

Un capítulo, un lenguaje, una conversación. Pregunta, respuesta, pregunta, respuesta, durante unas 26 páginas por capítulo.[^accu]

No son las 17 entrevistas y nada más: el libro abre con un **prólogo de Sir Tony Hoare** y un prefacio de los editores, y cierra con un *Afterword*, una sección de *Contributors* con las biografías de los entrevistados —unas 15 páginas— y el índice.[^masterminds] [^accu] Entre capítulo y capítulo, en cambio, no hay texto editorial que hilvane: los editores presentan y se corren.

En el prefacio, Biancuzzi cuenta que fueron **27 diseñadores** los que los guiaron: «Shane and I had the great privilege to let 27 great designers guide us through our journey».[^masterminds] El número cierra exacto con la tabla de acá abajo (1+1+1+1+1+3+2+4+1+1+2+1+1+3+1+2+1 = 27), y sirve de control cruzado: si el roster tuviera un entrevistado de más o de menos, no daría 27.

Eso cambia dos cosas.

La primera: **no hay narrador que te acomode la conclusión.** En un libro de historia de la computación, el autor te dice «y así fue como X se equivocó». Acá el tipo habla, y si se contradice, se contradice, y vos te arreglás. Es más trabajo de lectura y es mucho más honesto.

La segunda: **los capítulos son independientes.** No hay hilo argumental que se rompa si salteás. Esto es exactamente lo que habilita todo lo que sigue: podés leerlo en el orden que se te cante sin perderte nada.

### El roster

Estas son las 17, **en el orden real del libro**, con los entrevistados de cada una:[^masterminds] [^accu]

| # | Lenguaje | Entrevistado/s |
|---|---|---|
| 1 | C++ | Bjarne Stroustrup |
| 2 | Python | Guido van Rossum |
| 3 | APL | Adin D. Falkoff |
| 4 | Forth | Charles H. Moore |
| 5 | BASIC | Thomas E. Kurtz |
| 6 | AWK | Alfred Aho, Peter Weinberger, Brian Kernighan |
| 7 | Lua | Luiz Henrique de Figueiredo, Roberto Ierusalimschy |
| 8 | Haskell | Simon Peyton Jones, Paul Hudak, Philip Wadler, John Hughes |
| 9 | ML | Robin Milner |
| 10 | SQL | Don Chamberlin |
| 11 | Objective-C | Brad Cox, Tom Love |
| 12 | Java | James Gosling |
| 13 | C# | Anders Hejlsberg |
| 14 | UML | Ivar Jacobson, James Rumbaugh, Grady Booch |
| 15 | Perl | Larry Wall |
| 16 | PostScript | Charles Geschke, John Warnock |
| 17 | Eiffel | Bertrand Meyer |

> **Nota de corrección (pasada de fuentes):** esta tabla **cambió** respecto del borrador anterior. El borrador asumía que el orden en que el `Concepto` de este draft lista los lenguajes era el orden del libro, y **no lo es**. El índice real —verificado en el texto completo de archive.org[^masterminds] y confirmado de manera independiente por la reseña de ACCU[^accu]— arranca por C++ y Python, no por APL y BASIC. La nómina de entrevistados del `Concepto` sí era correcta en los 17 casos; lo que estaba mal era el orden. También: el capítulo 13 se titula **«C#» a secas**, no «Delphi/C#» — Hejlsberg es presentado como inventor de Delphi, pero el capítulo está catalogado bajo C#. Ningún capítulo cubre más de un lenguaje.

Los nombres completos quedan confirmados contra el índice: Falkoff aparece como **Adin D. Falkoff**, Moore como **Charles H. Moore** (no «Chuck» en el libro), Kurtz como **Thomas E. Kurtz**, Aho como **Alfred Aho**. «Love» es efectivamente **Tom Love**, y comparte el capítulo de Objective-C con Brad Cox. Geschke y Warnock comparten el de PostScript.

El capítulo de Lua entrevista sólo a **de Figueiredo e Ierusalimschy**: Waldemar Celes, el tercer autor del lenguaje, **no** figura entre los entrevistados.[^masterminds]

**Resuelto — la contradicción Erlang/Clojure:** el borrador anterior dejaba anotado que en otro lado yo tenía escrito que Joe Armstrong (Erlang) y Rich Hickey (Clojure) aparecían en el libro. **No aparecen.** El índice real no tiene ni Erlang ni Clojure, y el conteo de 27 diseñadores del prefacio cierra sin ellos. La tabla de este post es la correcta; la nota equivocada es la de [[E-09]], que hay que corregir cuando se trabaje ese draft.

> 🕳️ **HUECO — necesita a César:** ¿tenés el libro en papel, en PDF, o lo leíste desde archive.org? ¿Cómo llegaste a él — te lo recomendaron, lo encontraste solo, lo compraste cuando salió? Dos frases; es lo que le da carne al arranque.

> 🕳️ **HUECO — necesita a César:** ¿lo leíste entero o leíste algunas? Si no lo leíste entero, decilo — un post que dice «leí nueve de las diecisiete» es infinitamente más creíble que uno que finge haberlas leído todas.

### El problema del orden

> ⚠️ **Nota de corrección (pasada de fuentes) — este tramo cambió de argumento.** El borrador decía: «La primera entrevista del libro es APL. La segunda es BASIC. Si arrancás por ahí, arrancás por dos lenguajes que la mayoría de los lectores de hoy no tocó nunca». **Es falso.** El libro arranca por C++ y Python. El argumento original —que el libro se abandona porque empieza cuesta arriba— no se sostiene contra el índice real, así que lo reescribo. César: revisá este párrafo, porque el reemplazo es mío y el tono es tuyo.

Los editores no fueron tontos con el orden. El libro **abre por C++ y Python**: los dos lenguajes con más chances de que el lector los tenga abiertos en otra ventana. Es una rampa de entrada deliberada, y funciona.

El problema aparece después. A partir del capítulo 3 el libro se va a APL, Forth y BASIC —tres lenguajes que la mayoría de los lectores de hoy no tocó nunca, contados por gente que trabajaba en un mundo de computación que ya no existe—, y en el 8 y el 9 pega el doble golpe de Haskell y ML. Es fascinante, pero es un tercer y cuarto escalón cuesta arriba, y ahí es donde el libro se abandona: no en la primera página, sino en la cincuenta.

Y el problema de fondo no es el orden, es el volumen: 17 conversaciones largas leídas de corrido se te licúan, empieces por donde empieces.

Te propongo cuatro rutas.

**Ruta «lo que ya usás».** Empezá por el lenguaje que tenés abierto en otra ventana. Python, SQL, Java, C++. La entrevista te va a explicar por qué esa cosa que te molesta todos los días es como es, y esa es la mejor droga de entrada que tiene el libro.

**Ruta «lo que nunca vas a usar».** Exactamente al revés: APL, FORTH, ML. Sin nada en juego, sin opinión previa, leés las ideas puras. Es la ruta del que ya sabe que quiere el libro entero.

**Ruta cronológica.** Por edad del lenguaje, no por orden del capítulo. Ves cómo cada generación reacciona contra la anterior. Cuesta más armarla y rinde como ninguna.

**Ruta «los arrepentimientos».** Buscar en cada entrevista el momento en que el tipo dice alguna versión de «no anticipé que se usara así». Aparece en casi todas. Es el hilo real del libro y volvemos a él al final.

> 🕳️ **HUECO — necesita a César:** de estas cuatro rutas, ¿cuál usaste vos, o cuál usarías? Y si tenés una quinta que a mí no se me ocurrió, esa es la que va. El post tiene que recomendar una, no cuatro.

### Grupo 1 — los que empezaron como notación o como pedagogía

**APL** (Falkoff), **BASIC** (Kurtz), **FORTH** (Moore), **ML** (Milner).

Lo que junta a estos cuatro no es la época: es que ninguno nació para «hacer software» en el sentido industrial. APL nació como una notación para pensar y enseñar [[A1-14]]. BASIC nació para que estudiantes que no eran de computación pudieran usar la máquina de Dartmouth [[A1-15]]. FORTH nació porque un tipo quería una herramienta a su medida y se la hizo [[A1-03]]. ML nació como el metalenguaje de un demostrador de teoremas — o sea, ni siquiera nació para que la gente programara en él.

Cuatro lenguajes que aparecieron como efecto secundario de otra intención. Y los cuatro terminaron teniendo más descendencia que muchos que se diseñaron a propósito.

Lo de ML no es leyenda: está documentado por Mike Gordon, que trabajó en LCF con Milner. **LCF** —«Logic for Computable Functions»— fue un verificador de demostraciones que Milner desarrolló en Stanford en 1972. Para que los usuarios pudieran extender y personalizar las tácticas de demostración, «Milner, ably assisted by Morris and Newey, designed the programming language ML (an abbreviation for "Meta Language")».[^gordon] O sea: el nombre del lenguaje *es* la palabra metalenguaje, abreviada. Y Gordon subraya que «the needs of theorem proving very strongly influenced the design of the first version of ML» — el tipado fuerte y las excepciones entraron porque el demostrador los necesitaba, no porque alguien estuviera diseñando un lenguaje de propósito general.[^gordon]

Detalle que el borrador no tenía: Milner no lo hizo solo. Morris y Newey estuvieron ahí.

### Grupo 2 — los que se te metieron en el trabajo sin que los eligieras

**SQL** (Chamberlin), **AWK** (Aho, Weinberger, Kernighan), **PostScript** (Geschke, Warnock).

Nadie eligió aprender SQL [[A1-16]]. Te tocó. Nadie decidió que su carrera pasara por AWK; apareció un archivo de texto que había que cortar y ahí estaba. Y PostScript es el caso extremo: es un lenguaje de programación completo, con pila y todo, y millones de personas lo ejecutaron miles de millones de veces sin enterarse jamás de que existía, cada vez que apretaron Imprimir.

Este grupo es el más subestimado del libro, y es donde vive la mejor pregunta que tiene: ¿qué se siente inventar algo que todo el mundo usa y nadie nombra?

> 🕳️ **HUECO — necesita a César:** de estos tres, SQL es el que seguro te cruzó en serio. ¿Hubo algo en la entrevista a Chamberlin que te haya cambiado la opinión sobre SQL después de años de usarlo? ¿O te confirmó lo que ya pensabas?

### Grupo 3 — la pelea por los objetos

**C++** (Stroustrup), **Eiffel** (Meyer), **Objective-C** (Cox, Love).

Tres respuestas distintas a la misma pregunta de la misma época: cómo le metemos objetos a esto sin tirar todo abajo. C++ los pegó sobre C con obsesión por no pagar lo que no usás. Objective-C los pegó sobre C también, pero copiando a Smalltalk en vez de a Simula. Eiffel dijo «no pego nada sobre nada» y se hizo entero, con contratos incluidos.

Leídas seguidas, estas tres son un debate. Y el capítulo de C++ es, para mí, donde el formato Q&A rinde más: Stroustrup contestando por decisiones que le criticaron durante treinta años.

Confirmado: el capítulo 11 es entrevista doble, **Brad Cox y Tom Love**, los dos en el mismo capítulo.[^masterminds]

Y la caracterización no hace falta ponérsela en boca a nadie de la entrevista, porque cada uno la dejó escrita por su cuenta, antes. Stroustrup abre su historia de C++ con esta frase: «C++ was designed to provide Simula's facilities for program organization together with C's efficiency and flexibility for systems programming».[^hopl2] Es literal: Simula para organizar, C para que no duela. Y del lado de Cox, el título de su paper de 1983 dice solo casi todo — «The object oriented pre-compiler: programming Smalltalk 80 methods in C language».[^cox83] Smalltalk sobre C, un precompilador de por medio.

Así que el paralelismo del párrafo de arriba se sostiene con fuentes de los propios autores, no con folklore.

### Grupo 4 — los lenguajes de la gente

**Perl** (Larry Wall), **Python** (van Rossum), **Lua** (de Figueiredo, Ierusalimschy).

Tres lenguajes con filosofías explícitas y opuestas sobre cómo tratar al programador. Perl te da todas las maneras de hacerlo y confía en vos [[A1-17]]. Python te da una y te la hace obvia. Lua te da casi nada y te deja construir el resto — y por eso terminó embebido en todos lados [[A1-19]].

Larry Wall es lingüista de formación, y su entrevista es la más rara del libro porque no habla como ingeniero. Y la de Lua tiene un valor extra que en Argentina se siente distinto: es la única entrevista del roster a gente de América Latina, laburando en América Latina, con presupuesto de América Latina, y el lenguaje les salió mejor que a medio Silicon Valley.

La afirmación «única entrevista a gente de América Latina» queda en pie: con el roster de 17 ya verificado contra el índice real y el conflicto Erlang/Clojure resuelto, los únicos dos entrevistados latinoamericanos del libro son de Figueiredo e Ierusalimschy, los dos de Lua.[^masterminds]

> 🕳️ **HUECO — necesita a César:** ¿usaste Perl en serio en algún momento? Perl es el lenguaje que separa generaciones de sysadmins, y si lo usaste tenés una opinión fuerte al respecto. ¿Cuál es?

> 🕳️ **HUECO — necesita a César:** lo de Lua y el presupuesto latinoamericano — ¿te resuena con algo de tu experiencia en el sector público de Santa Fe? No inventé nada acá, pero si tenés un paralelo real (hacer algo bueno con poca plata y sin permiso de nadie), es el mejor lugar del post para meterlo.

### Grupo 5 — la teoría que bajó a producción

**Haskell** (Peyton Jones, Hudak, Wadler, Hughes).

Este capítulo es distinto a todos: cuatro personas [[A1-18]]. No es un creador con su lenguaje, es un comité que se juntó a propósito, y eso ya te dice todo sobre la naturaleza del bicho.

Confirmado: el capítulo 8 es uno solo y entrevista a los cuatro —Simon Peyton Jones, Paul Hudak, Philip Wadler y John Hughes—, no son secciones separadas.[^masterminds] Es el capítulo con más entrevistados del libro; el de UML, con tres, viene segundo.

Es la entrevista más densa del libro y la que más recompensa. Si venís de lenguajes imperativos, es la que te va a costar. Leela igual, y leela con tiempo.

### Grupo 6 — los que tuvieron dueño

**Java** (Gosling), **C#** (Hejlsberg), **UML** (Jacobson, Rumbaugh, Booch).

(El capítulo se llama **C#**, no «Delphi/C#» como decía mi seed: el libro presenta a Hejlsberg como inventor de Delphi, pero cataloga el capítulo bajo C#.[^masterminds] En el libro van seguidos: Java es el 12, C# el 13, UML el 14.)

Acá el diseño no es una conversación entre el creador y el problema: hay una empresa en el medio [[A1-20]] [[A1-21]]. Gosling en Sun, Hejlsberg en Borland y después en Microsoft, y los tres de UML fabricando un estándar que se volvió una industria de certificaciones.

UML es el intruso: no es un lenguaje de programación. Que esté en un libro que se llama *Masterminds of Programming* es una decisión editorial rara, y creo que es defendible por lo que muestra — la ambición de que la notación reemplazara al código, y lo que pasó con esa ambición.

Bonus: Gosling dice cosas sobre la herencia que no te esperás del inventor de Java. Le dediqué un post entero [[C-10]].

### Las ausencias

Un roster también se define por quién no está.

No hay Smalltalk, o sea no hay Alan Kay. No hay Lisp de McCarthy. No hay JavaScript, no hay Ruby, no hay C de Ritchie. Y no hay ninguna mujer en las 17.

Esa última no es un detalle de trivia: es un dato sobre el libro y sobre cómo se armó el canon del que salió el libro.

Las dos afirmaciones quedan verificadas contra el índice real y la lista de *Contributors*:[^masterminds] [^accu] entre los 17 capítulos no hay Smalltalk, ni Lisp, ni C, ni Ruby, ni JavaScript; y los 27 entrevistados son 27 varones. Ninguna mujer en el roster.

Sobre la fecha: el libro es de **O'Reilly, primera edición marzo de 2009**, ISBN 978-0-596-51517-1.[^masterminds] Eso acota las ausencias con justicia — para 2009 tanto Ruby como JavaScript ya eran ineludibles, así que la ausencia no se explica por «el lenguaje todavía no importaba».

[VERIFICAR: si querés apoyar el argumento de las ausencias en quién estaba vivo y entrevistable en 2008-2009 (Ritchie, Kay, McCarthy), hay que chequear cada fecha contra una fuente. En esta pasada no las verifiqué y por eso no las escribo.]

[VERIFICAR: la ventana temporal en que se hicieron las entrevistas. Busqué en el prefacio y en el texto completo del ítem de archive.org y **el libro no la declara**: el prefacio habla de «our journey» y de los 27 diseñadores, pero no fecha las conversaciones ni dice cuánto duró el proyecto. La página de catálogo de O'Reilly (`oreilly.com/library/view/masterminds-of-programming/9780596801670/`) y su gacetilla de prensa (`oreilly.com/pub/pr/2277`) devuelven **HTTP 403** a fetch automatizado y no se pudieron revisar. Pendiente: probar la gacetilla vía Wayback, o buscar entrevistas/posts de Biancuzzi de 2008-2009 contando el proceso.]

### Plan de lectura

El libro está en archive.org, y acá hay que hacer una distinción que importa.[^archive_cdl] [^archive_free]

Hay **dos ítems distintos**. Uno es el de la propia Internet Archive en modalidad de **préstamo digital controlado**: lo pedís prestado, lo leés, se te vence. Es el camino legítimo y es el que enlazo.[^archive_cdl] El otro es una subida de un usuario particular (cuenta «usege», enero de 2015) con el PDF y el ePub a descarga libre y sin restricción.[^archive_free] Existe, resuelve, y no voy a fingir que no lo vi —de hecho es de donde salió el índice que verifiqué para este post—, pero es un libro de O'Reilly de 2009 con copyright vigente subido por un tercero: no es una edición liberada por la editorial, es una copia que quedó ahí. Que esté accesible no lo hace legal.

Si lo vas a leer en serio, compralo o pedilo prestado por CDL.

> 🕳️ **HUECO — necesita a César:** decidí vos cómo tratar esto en el post publicado. Yo dejo los dos ítems documentados y la distinción hecha, pero enlazar o no la copia libre es una decisión tuya, no mía.

Mi propuesta, y es la parte útil de este post: **una entrevista por semana, en el orden que vos armes con alguna de las cuatro rutas.** Diecisiete semanas, cuatro meses. Suena lento y es exactamente el punto: estos capítulos no son artículos, son conversaciones largas, y leídos de a dos por noche se te mezclan todos y no te queda nada.

> 🕳️ **HUECO — necesita a César:** ¿esto es lo que hiciste vos, o me lo estoy inventando como consejo razonable? Si lo leíste de otra manera —de un tirón, salteado, abandonado y retomado años después— contá esa, que es la verdadera.

### El hilo

Si tuviera que decir qué tienen en común las 17, diría esto: en casi todas, en algún momento, el tipo dice alguna versión de **«no anticipé que se usara así»**.

No es humildad de entrevista. Es el hecho central del oficio. Diseñás una herramienta con una intención, la soltás al mundo, y el mundo la usa para otra cosa. Y ahí ya no es tuya.

Ese es el libro. El roster es la excusa.

> 🕳️ **HUECO — necesita a César:** el cierre necesita tu veredicto. Después de leer las que leíste, ¿el libro te dejó más admiración por estos tipos o menos? Y la pregunta que de verdad cierra el post: ¿alguna vez te pasó a vos, en chiquito — que algo que hiciste terminara usándose para algo que no habías previsto?

---

[^masterminds]: Federico Biancuzzi & Shane Warden (eds.), *Masterminds of Programming: Conversations with the Creators of Major Programming Languages*, O'Reilly Media, primera edición marzo de 2009, 496 pp., ISBN 978-0-596-51517-1. Prólogo de Sir Tony Hoare. Índice, prefacio y datos de edición verificados sobre el [texto completo del ítem de archive.org](https://archive.org/stream/MastermindsOfProgramming/Masterminds%20of%20Programming_djvu.txt) — ver [[tr-23]] en el plan editorial.
[^archive_cdl]: [*Masterminds of programming* en Internet Archive](https://archive.org/details/mastermindsofpro0000unse) — ítem en **préstamo digital controlado** (hay que pedirlo prestado para leerlo). O'Reilly, 2009, ISBN 0596515170 / 9780596515171.
[^archive_free]: [*Masterminds Of Programming* en Internet Archive](https://archive.org/details/MastermindsOfProgramming) — subida de usuario («usege», 3 de enero de 2015), PDF/ePub/texto completo a descarga libre. **Copia de un libro con copyright vigente subida por un tercero, no una edición liberada por O'Reilly.** Es la fuente sobre la que se verificó el índice de este post.
[^accu]: [Reseña de *Masterminds of Programming*](https://accu.org/bookreviews/2024/bruntlett_2025/) — ACCU (Association of C and C++ Users). Confirma de manera independiente los 17 lenguajes y su orden, el prólogo de Tony Hoare, las ~26 páginas por capítulo y las ~15 páginas de biografías de los entrevistados. Backup: [Wayback, 2025-10-27](http://web.archive.org/web/20251027215603/https://accu.org/bookreviews/2024/bruntlett_2025/).
[^hopl2]: Bjarne Stroustrup, [«A History of C++: 1979–1991»](https://www.stroustrup.com/hopl2.pdf) — ACM History of Programming Languages Conference (HOPL-2), marzo de 1993; PDF en el sitio del propio autor. La cita («C++ was designed to provide Simula's facilities for program organization together with C's efficiency and flexibility for systems programming») es la primera oración de la Introducción. Backup: [Wayback, 2026-07-03](http://web.archive.org/web/20260703213554/https://www.stroustrup.com/hopl2.pdf).
[^cox83]: Brad L. Cox, «The object oriented pre-compiler: programming Smalltalk 80 methods in C language», *ACM SIGPLAN Notices*, vol. 18, n.º 1 (1983), pp. 15-22. DOI: [10.1145/948093.948095](https://doi.org/10.1145/948093.948095). El texto en ACM DL está detrás de paywall y devuelve HTTP 403 a fetch automatizado; los datos bibliográficos se verificaron vía [Crossref](https://api.crossref.org/works/10.1145/948093.948095).
[^gordon]: Mike Gordon, [«From LCF to HOL: a short history»](https://www.cl.cam.ac.uk/archive/mjcg/papers/HolHistory.html) — archivo del propio autor en el Computer Laboratory de Cambridge ([PDF](https://www.cl.cam.ac.uk/archive/mjcg/papers/HolHistory.pdf)). Publicado en G. Plotkin, C. Stirling & M. Tofte (eds.), *Proof, Language, and Interaction*, MIT Press, 2000, ISBN 0262161885. Backup del HTML: [Wayback, 2026-02-06](http://web.archive.org/web/20260206100221/https://www.cl.cam.ac.uk/archive/mjcg/papers/HolHistory.html).
