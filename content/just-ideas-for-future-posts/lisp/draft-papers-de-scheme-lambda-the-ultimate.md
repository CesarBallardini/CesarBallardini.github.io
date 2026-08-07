### A2-02 — Los papers de Scheme: lambda the ultimate

- **Archivo seed:** `dev/draft-scheme-papers.md`
- **Slug propuesto:** `papers-de-scheme-lambda-the-ultimate`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-papers-de-scheme-lambda-the-ultimate.md`
- **Serie:** A2
- **Cross-links:** depende de [[tr-14]] (Lambda the Ultimate classics); lleva a [[A2-01]] (SICP), [[B-04]] (tail calls), [[B-05]] (trampolines), [[C-05]] (revolución del cómputo)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** la serie de papers que Sussman y Steele escribieron sobre Scheme entre 1975 y 1980 ("Lambda the Ultimate ___") cambiaron lo que entendíamos por "lenguaje de programación". El post es una lectura guiada para alguien que nunca leyó un paper técnico antes.

**Hook:** "cuatro papers, todos con el título *Lambda the Ultimate algo*, y el primero arranca con: 'descubrimos por accidente que con lambda podés construir todo lo que un compilador necesita'. Eso es *Lambda the Ultimate Imperative*. Y sí, vamos a leerlo."

**Outline:** (corregido 2026-07-15 — los puntos 4 y 5 del outline original eran **el mismo paper**; ver Estado actual)
1. La serie *Lambda Papers* de Steele y Sussman. Por qué los escribieron, qué pasaba en el MIT en ese momento. Arranca en el AI Memo 349 (dic. 1975).
2. *LAMBDA: The Ultimate Imperative* (AI Memo 353, mar. 1976) — cómo lambda subsume goto, asignación, loops.
3. *LAMBDA: The Ultimate Declarative* (AI Memo 379, nov. 1976) — la otra cara: lambda como operador de renombre; anuncia el compilador.
4. *LAMBDA: The Ultimate GOTO* = *Debunking the "Expensive Procedure Call" Myth* (AI Memo 443, oct. 1977) — **un solo paper con tres títulos**: por qué tail calls son saltos y por qué deben ser cheap.
5. *RABBIT* (Steele, MS thesis, AI-TR-474, may. 1978) — el primer compilador "real" de Scheme; CPS como representación intermedia.
6. *LAMBDA: The Ultimate Opcode* (AI Memo 514, mar. 1979) — el cuarto «Ultimate», que el borrador no tenía. Cierra el arco: de la semántica al silicio.
7. Cierre: por qué leer estos papers todavía vale la pena en 2026.

**Bibliografía:** (revisada y verificada 2026-07-15. `dspace.mit.edu` responde **HTTP 405** a fetch automatizado y `web.archive.org` está bloqueado para el agente, así que cada handle de DSpace se verificó contra el **endpoint OAI-PMH del MIT** —`https://dspace.mit.edu/oai/request?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:dspace.mit.edu:1721.1/<n>`—, que devuelve título, autor, fecha e identificador reales. Eso detectó dos citas erróneas del borrador. Flags de bitrot: `estable` / `frágil`.)

*Los papers de la serie (todos DSpace del MIT — `estable`):*
- [Sussman & Steele, *SCHEME: An Interpreter for Extended Lambda Calculus*, AI Memo 349, diciembre 1975](https://dspace.mit.edu/handle/1721.1/5794) — `AIM-349`. **Agregado**: es el arranque de la serie y faltaba. `estable`
- [Steele & Sussman, *LAMBDA: The Ultimate Imperative*, AI Memo 353, marzo 1976](https://dspace.mit.edu/handle/1721.1/5790) — `AIM-353`. Handle confirmado por OAI. Abstract citado textual en el post. `estable`
- [Steele, *LAMBDA: The Ultimate Declarative*, AI Memo 379, noviembre 1976](https://dspace.mit.edu/handle/1721.1/6091) — `AIM-379`. **URL CORREGIDA**: el borrador citaba `1721.1/5789`, que según OAI es `AIM-351`, *A State Space Model for Sensorimotor Control and Learning*, de Marc Raibert — otro paper, otro autor, otro tema. El handle correcto es `1721.1/6091`. `estable`
- [Steele, *Debunking the "Expensive Procedure Call" Myth, or, Procedure Call Implementations Considered Harmful, or, Lambda: The Ultimate GOTO*, AI Memo 443, octubre 1977](https://dspace.mit.edu/handle/1721.1/5753) — `AIM-443`. **HALLAZGO PRINCIPAL**: «el paper del mito» y «Lambda: The Ultimate GOTO» son **el mismo trabajo**, no dos. Título completo confirmado por OAI, por Crossref y por wikisource. `estable`
- [Steele & Sussman, *Design of LISP-based Processors … or LAMBDA: The Ultimate Opcode*, AI Memo 514, marzo 1979](https://dspace.mit.edu/handle/1721.1/5731) — `AIM-514`. **Agregado**: es el cuarto paper «LAMBDA: The Ultimate ___» y faltaba por completo. `estable`
- [Steele, *RABBIT: A Compiler for SCHEME*, AI-TR-474, mayo 1978](https://dspace.mit.edu/handle/1721.1/6913) — `AITR-474`. Handle y fecha confirmados por OAI. `estable`

*Versión publicada (para citar con DOI):*
- Steele, «Debunking the "expensive procedure call" myth…», *Proceedings of the 1977 Annual Conference (ACM '77)*, ACM Press, 1977. DOI [10.1145/800179.810196](https://doi.org/10.1145/800179.810196) — verificado vía `https://api.crossref.org/works/10.1145/800179.810196` porque la ACM DL bloquea fetch. `estable`

*Correcciones al aparato del borrador:*
- [Steele, *The Definition and Implementation of a Computer Programming Language Based on Constraints*, AI-TR-595, agosto 1980](https://dspace.mit.edu/handle/1721.1/6933) — `AITR-595`. **AUTOR Y AÑO CORREGIDOS**: el borrador lo citaba como «tesis doctoral de Sussman de 1973» y lo usaba como *antecedente* de los Lambda Papers. OAI dice que es de **Steele** y de **1980** — o sea, es posterior a toda la serie y no puede ser su antecedente. `estable`
- [Sussman, *A Computational Model of Skill Acquisition*, AI-TR-297, agosto 1973](https://dspace.mit.edu/handle/1721.1/6894) — `AITR-297`. **Agregado**: ésta sí es la tesis doctoral de Sussman de 1973, pero es sobre HACKER y aprendizaje de habilidades, no sobre definición de lenguajes; no sirve como el antecedente que el borrador quería. `estable`

*Índices y bibliotecas curadas:*
- [*The Lambda Papers* — research.scheme.org](https://research.scheme.org/lambda-papers/) — índice de la serie completa (9 entradas) con memo, fecha y abstract. Es la fuente que fija el **alcance** de la serie. `frágil` → backup Wayback: [snapshot 2026-02-01](http://web.archive.org/web/20260201181527/https://research.scheme.org/lambda-papers/)
- [SCHEME family — Software Preservation Group, Computer History Museum](https://softwarepreservation.computerhistory.org/LISP/scheme_family.html) — cronología independiente; corrobora memo/mes/año de toda la serie. Segunda fuente para el alcance. `estable`
- [readscheme.org — mirror en GitHub](https://github.com/scheme-and-computer-science/library.readscheme.org) — bibliografía curada de research sobre Scheme (orig. Jim Bender). Verificado. `estable`
- [Lambda the Ultimate — classic papers](http://lambda-the-ultimate.org/classic/papers.html) — **NO VERIFICADA**: el servidor cortó la conexión en todos los intentos (`ECONNRESET`, socket cerrado). La API de Wayback informa snapshot 200 del 2026-04-25 pero no pude abrirlo (web.archive.org bloqueado para el agente). Confirmar a mano antes de publicar; si sigue caída, `[[tr-14]]` necesita otra fuente. `frágil`
- [[tr-14]] — Lambda the Ultimate, classic papers. Ver la advertencia de arriba: la URL del recurso está sin verificar.

*Abstracts (fuente secundaria de contraste, usada para verificar por duplicado):*
- [*Lambda: The Ultimate GOTO* — Wikisource](https://en.wikisource.org/wiki/Lambda:_The_Ultimate_GOTO) — transcripción; su abstract coincide con el registro OAI. Útil porque DSpace bloquea el fetch del PDF. `estable`

**Imágenes:**
- _Crear_: screenshot de la portada del primer Lambda Paper (PDF) (5 min).
- _Crear_: opcional, un timeline simple SVG de los papers en orden (~30 min).

**Tags propuestos:** `['Scheme', 'Lambda Papers', 'Sussman', 'Steele', 'lambda calculus', 'historia']`

**Estado actual:** **pasada de fuentes hecha 2026-07-15** (agente; sin revisar por César). La prosa del borrador previo tenía **tres errores de hecho verificables**, ahora corregidos. Bibliografía reescrita: 6 fuentes agregadas, 1 URL corregida, 1 cita corregida en autor y año, 1 marcada como no verificable.

> ⚠️ **PREMISA EN DUDA — el Hook se sostiene, pero el cuerpo del post no contaba los mismos cuatro papers.**
>
> El Hook dice «cuatro papers, todos con el título *Lambda the Ultimate algo*, entre 1975 y 1980». Dos fuentes independientes (el índice [*The Lambda Papers*](https://research.scheme.org/lambda-papers/) de research.scheme.org y el [Software Preservation Group del Computer History Museum](https://softwarepreservation.computerhistory.org/LISP/scheme_family.html)) coinciden: los papers titulados «LAMBDA: The Ultimate ___» son **exactamente cuatro** — Imperative (353, 1976), Declarative (379, 1976), **GOTO (443, 1977)** y **Opcode (514, 1979)**. **El conteo del Hook es correcto.** El rango de años no del todo: los cuatro «Ultimate» van de 1976 a 1979; se llega a «1975-1980» sólo si se cuenta el memo 349 (dic. 1975) como arranque y la publicación del 514 en CACM (1980) como cierre. Decisión de César: ajustar el rango o explicitar qué se cuenta.
>
> **El problema real estaba en el cuerpo**, que armaba un cuarteto distinto y equivocado (Imperative, Declarative, GOTO, Debunking, RABBIT — cinco, y con dos de ellos siendo el mismo trabajo). Corregido en la prosa y en el outline.
>
> **Además, la frase que el Hook presenta como apertura del Memo 353 no existe.** El abstract real (ahora citado textual en el post, verificado por duplicado vía OAI del MIT y research.scheme.org) no habla de accidente, ni de descubrimiento, ni de compiladores; y dice explícitamente lo contrario del «descubrimos»: «Some of these models … are already well known, and appear in the work of Landin, Reynolds, and others», y que el paper «is partly tutorial in intent». No toqué el Hook (es de César), pero **hay que reescribirlo o dejar de presentar esa frase como cita** antes de publicar.

**Los tres errores de hecho corregidos:**

1. **«Debunking the Expensive Procedure Call Myth» y «Lambda: The Ultimate GOTO» son el MISMO paper** (AI Memo 443, oct. 1977). El borrador los trataba como dos trabajos distintos, con una sección entera («Acá hay dos piezas») construida sobre esa confusión, y marcaba al GOTO como «la única afirmación del posteo sin fuente listada» — cuando en realidad ya estaba en la bibliografía bajo el otro título. Confirmado por tres fuentes: registro OAI del MIT, Crossref (DOI 10.1145/800179.810196) y wikisource.
2. **La URL del Memo 379 apuntaba a otro paper.** El borrador citaba `dspace.mit.edu/handle/1721.1/5789` para *LAMBDA: The Ultimate Declarative*; ese handle es `AIM-351`, *A State Space Model for Sensorimotor Control and Learning*, de **Marc Raibert**. El handle correcto es `1721.1/6091`.
3. **El «antecedente de Sussman de 1973» no es de Sussman ni de 1973.** *The Definition and Implementation of a Computer Programming Language Based on Constraints* (handle `1721.1/6933`) es `AITR-595`, de **Guy Steele**, de **agosto de 1980** — posterior a toda la serie, así que no puede ser su antecedente. Párrafo eliminado y reemplazado por el contexto que sí se sostiene (memo 349, ACTORS de Hewitt, MacLISP, todo citado del abstract). La tesis real de Sussman de 1973 (*A Computational Model of Skill Acquisition*, `AITR-297`) queda en bibliografía como aclaración, pero no sirve para lo que el párrafo quería.

**Marcas:** de las 8 `[VERIFICAR:]` del cuerpo quedan **3**, todas por la misma causa técnica: **`dspace.mit.edu` responde HTTP 405 a fetch automatizado y `web.archive.org` está bloqueado para el agente**, así que se pudieron leer los *abstracts* (vía el endpoint OAI-PMH del MIT, que sí responde) pero **no el cuerpo de ningún PDF**. Las tres pendientes son: (a) la máquina PDP-10 —no aparece en ningún abstract; MacLISP sí está confirmado—; (b) qué mide concretamente el Memo 443 —el abstract menciona «an existing implementation» sin nombrarla ni dar números—; (c) sobre qué máquina corre RABBIT y qué emite —el abstract confirma CPS como representación intermedia pero no menciona máquina destino—. Las tres se resuelven bajando tres PDF a mano.

**6 huecos 🕳️ intactos.** El post es una lectura guiada en primera persona y necesita a César para: cuándo y por dónde llegó a los Lambda Papers, si los leyó en papel o en pantalla, cuál le resultó más difícil, qué pasó cuando intentó leer RABBIT, y qué recuerda de la primera vez que leyó un paper técnico. Nota: dos huecos preguntan «de los cuatro, ¿cuál…?» — ahora que el cuarteto cambió (entra Opcode, y GOTO/Debunking se fusionan), puede que la pregunta haya que reformularla.

**Pendiente al publicar:** resolver `[[tr-14]]`, `[[A2-01]]`, `[[B-04]]`, `[[B-05]]` y `[[C-05]]` a URLs reales.

---

## Borrador de prosa

Hay cuatro papers del MIT que llevan casi el mismo título. *LAMBDA: The Ultimate Imperative* (AI Memo 353, marzo de 1976)[^imperative]. *LAMBDA: The Ultimate Declarative* (AI Memo 379, noviembre de 1976)[^declarative]. *LAMBDA: The Ultimate GOTO* (AI Memo 443, octubre de 1977)[^goto]. Y *LAMBDA: The Ultimate Opcode* (AI Memo 514, marzo de 1979)[^opcode]. Alrededor de ellos hay una cola de trabajos que siguen tirando del mismo hilo. Se los conoce como los *Lambda Papers*, los escribieron Gerald Sussman y Guy Steele, y lo que sostienen —los cuatro, con distinta ropa— es una sola idea: que casi todo lo que creías que era una construcción del lenguaje de programación es, en realidad, una función.

No es una metáfora. Es un argumento técnico, escrito con la prolijidad de un memo de laboratorio, y se puede leer. Eso es lo que quiero hacer acá: leerlos juntos. No resumirlos —leerlos. Porque si nunca abriste un paper técnico, estos son un lugar sorprendentemente amable para empezar, y quiero mostrarte por qué.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste vos a los Lambda Papers? ¿Fue por SICP, por alguien que te los pasó, por el blog Lambda the Ultimate, o buscando otra cosa? Una o dos frases con el año aproximado.

### Qué es un «AI Memo», y por qué eso importa antes de leer

Los trabajos que nos importan no salieron en una revista. Salieron como **AI Memos** del MIT Artificial Intelligence Laboratory: *LAMBDA: The Ultimate Imperative* es el AI Memo 353, de marzo de 1976[^imperative]; *LAMBDA: The Ultimate Declarative* es el 379, de noviembre del mismo año[^declarative]; *LAMBDA: The Ultimate GOTO* es el 443, de octubre de 1977[^goto]; *LAMBDA: The Ultimate Opcode* es el 514, de marzo de 1979[^opcode]. Y el que los precede a todos: *SCHEME: An Interpreter for Extended Lambda Calculus*, AI Memo 349, de diciembre de 1975[^scheme349], donde el lenguaje aparece por primera vez.

Aparte de la serie, pero central para el argumento, está *RABBIT: A Compiler for SCHEME*, el AI-TR-474 de mayo de 1978, que es la tesis de maestría de Steele[^rabbit].

Una aclaración de catálogo que conviene hacer temprano, porque es una fuente de confusión real: **el AI Memo 443 es un solo trabajo con tres títulos encadenados**. Su título completo en el catálogo del MIT es *Debunking the "Expensive Procedure Call" Myth, or, Procedure Call Implementations Considered Harmful, or, Lambda: The Ultimate GOTO*[^goto]. Es decir: «el paper del mito» y «el Ultimate GOTO» **son el mismo paper**, no dos. Se lo cita de las dos maneras según el gusto de quien cite, y eso hace parecer que la serie tiene un trabajo más de los que tiene.

Un AI Memo era literalmente eso: un memo interno. Se escribía para los colegas del pasillo, no para un comité de revisión anónimo de otro continente. Y se nota. El tono es directo, hay chistes, hay código de verdad, y hay párrafos donde el autor te cuenta qué probó y qué no le funcionó. Un paper de conferencia moderno esconde todo eso; un AI Memo de los setenta te lo deja adelante. Por eso son buenos como primer paper: no tenés que aprender a decodificar la retórica académica antes de acceder al contenido.

Todos están abiertos en DSpace, el repositorio del MIT. No hay paywall, no hay que pedirle el PDF a nadie por mail. Los bajás y los leés.

> 🕳️ **HUECO — necesita a César:** ¿los leíste en pantalla o los imprimiste? Si los imprimiste, ¿guardás todavía esa pila de hojas? (Serviría como foto para el post, aunque sea de un rincón de la biblioteca.)

### 1976: qué estaba pasando en ese pasillo

El contexto mínimo, y sólo el que puedo sostener: el memo 349 es de diciembre de 1975, el 353 de marzo de 1976, el 379 de noviembre de 1976, el 443 de octubre de 1977, la tesis RABBIT de mayo de 1978, y el 514 de marzo de 1979. Es decir, seis trabajos en poco más de tres años, del mismo laboratorio, tirando del mismo hilo. Eso no es una serie de papers: es una obsesión con fechas.

El arranque real está en el 349, *SCHEME: An Interpreter for Extended Lambda Calculus*[^scheme349], y su abstract dice de dónde vino la idea con todas las letras: «Inspired by ACTORS, we have implemented an interpreter for a LISP-like language, SCHEME, based on the lambda calculus, but extended for side effects, multiprocessing, and process synchronization». Los ACTORS son los de Carl Hewitt, y el laboratorio era el mismo. El interpreter estaba escrito en MacLISP: el propio memo 349 cierra con la implementación completa y anotada sobre MacLISP. El hilo de los actors sigue vivo tres memos después: el abstract del 379 dice que su visión de LAMBDA «complements Hewitt's actors theory nicely»[^declarative].

Así que los Lambda Papers no le caen del cielo a nadie; son la continuación de una línea de trabajo que arranca en un interprete de juguete con propósito declaradamente tutorial.

[VERIFICAR: la máquina concreta sobre la que corría todo esto (se suele decir PDP-10) no aparece en los abstracts del 349, 353, 379, 443 ni AITR-474 —que son los que pude leer vía el endpoint OAI de DSpace y research.scheme.org—. MacLISP sí está confirmado por el abstract del 349. Para el PDP-10: buscar en el cuerpo del PDF del memo 349 (sección de implementación), que no pude abrir porque dspace.mit.edu responde HTTP 405 a fetch automatizado.]

<!-- NOTA DE FUENTES (2026-07-15): la marca sobre el alcance de la serie se resolvió. Dos fuentes independientes —el índice de The Lambda Papers de research.scheme.org y el Software Preservation Group del Computer History Museum— coinciden en el catálogo: los papers titulados «LAMBDA: The Ultimate ___» son exactamente CUATRO (Imperative 1976, Declarative 1976, GOTO 1977, Opcode 1979), y el rango real es 1976-1979 (1975-1979 si se cuenta el memo 349 como arranque de la serie; hasta 1980 si se cuenta la publicación del 514 en CACM). El conteo de «cuatro» del Hook se sostiene; el rango «1975 y 1980» es defendible sólo si se explicita qué se cuenta. Ver PREMISA EN DUDA en Estado actual. -->

Se cayó de acá un párrafo del borrador anterior que afirmaba que el antecedente era «la tesis doctoral de Sussman de 1973, *The Definition and Implementation of a Computer Programming Language Based on Constraints*». **Eso era falso en autor y en fecha** y se eliminó: el registro de DSpace de ese trabajo (handle 1721.1/6933) dice que es de **Guy Lewis Steele Jr.**, es el **AITR-595**, y es de **agosto de 1980**[^constraints] — o sea, es la tesis doctoral de *Steele*, y es **posterior** a todos los Lambda Papers, no anterior. La tesis doctoral de Sussman de 1973 existe, pero es *A Computational Model of Skill Acquisition* (AITR-297, agosto de 1973)[^sussman73], sobre HACKER y aprendizaje de habilidades — no sobre definición de lenguajes, y por lo tanto no sirve como el antecedente que el párrafo quería.

### *LAMBDA: The Ultimate Imperative* (AI Memo 353, marzo de 1976)

El que más shock produce. El título ya es la tesis: lambda —la función anónima, la construcción más «declarativa» que hay— es el mecanismo imperativo definitivo. Steele y Sussman muestran que las construcciones que un lenguaje imperativo trata como primitivas irreducibles se pueden expresar como aplicaciones de funciones. No como una traducción torpe, sino de manera directa y sistemática.

La lista no hace falta reconstruirla de memoria, porque el abstract la enumera[^imperative]:

> «We demonstrate how to model the following common programming constructs in terms of an applicative order language similar to LISP: Simple Recursion, Iteration, Compound Statements and Expressions, GO TO and Assignment, Continuation-Passing, Escape Expressions, Fluid Variables, Call by Name, Call by Need, and Call by Reference.»

Y sigue con la parte que a mí me parece la más elegante del abstract entero, porque es donde se ve el ascetismo del método:

> «The models require only (possibly self-referent) lambda application, conditionals, and (rarely) assignment. No complex data structures such as stacks are used. The models are transparent, involving only local syntactic transformations.»

Sin stacks. Sin estructuras de datos complejas. Sólo transformaciones sintácticas locales. Ese es todo el aparato.

Vale marcar una honestidad del propio paper que suele perderse cuando se lo mitifica: los autores **no** dicen haber descubierto todo esto. El abstract aclara que «Some of these models, such as those for GO TO and assignment, are already well known, and appear in the work of Landin, Reynolds, and others», que lo nuevo son los modelos «for escape expressions, fluid variables, and call by need with side effects», y que el paper «is partly tutorial in intent, gathering all the models together for purposes of context». Es, en parte, una recopilación declarada.

La consecuencia es la que hace que el paper importe cincuenta años después: si todas esas construcciones son azúcar sintáctico sobre lambda, entonces la pregunta «¿qué primitivas necesita un lenguaje?» tiene una respuesta mucho más chica de lo que suponíamos. Y si el lenguaje es más chico, el compilador tiene menos casos especiales que tratar. La economía conceptual se convierte en economía de ingeniería. Sobre esa idea —que un lenguaje se hace grande creciendo desde un núcleo mínimo, no acumulando features— ya escribí en [[C-05]].

<!-- NOTA DE FUENTES (2026-07-15): marca resuelta en cuanto a la búsqueda. El abstract real del Memo 353 está ahora citado textual más arriba (verificado por duplicado: endpoint OAI de dspace.mit.edu y research.scheme.org). La frase que el Hook pone entre comillas —«descubrimos por accidente que con lambda podés construir todo lo que un compilador necesita»— NO aparece en el abstract ni se le parece: el abstract no habla de accidente ni de descubrimiento, y de hecho dice lo contrario (que varios modelos «are already well known ... Landin, Reynolds»), y tampoco menciona compiladores (eso es el 379). El Hook es de César y no se toca acá, pero hay que reescribirlo antes de publicar o dejar de presentarlo como cita. Ver PREMISA EN DUDA en Estado actual. -->

No pude verificar el cuerpo del PDF: `dspace.mit.edu` responde HTTP 405 a fetch automatizado, así que todo lo citado acá viene del registro OAI del MIT y del índice de research.scheme.org, que coinciden palabra por palabra.

### *LAMBDA: The Ultimate Declarative* (AI Memo 379, noviembre de 1976)

Si el 353 dice «lambda es lo imperativo», el 379 dice «lambda es lo declarativo». Y no es una contradicción: es el punto. La misma construcción sirve para las dos cosas, y el hecho de que sirva para las dos es lo que la vuelve fundacional en vez de meramente conveniente.

El abstract se presenta a sí mismo como «a sequel to *LAMBDA: The Ultimate Imperative*», y el aporte que anuncia es un cambio de lente: «a new view of LAMBDA as a renaming operator is presented and contrasted with the usual functional view taken by LISP»[^declarative]. Lambda no como «función» sino como **operador de renombre**. Combinada con «the view of function invocation as a kind of generalized GOTO», esa lente es la que produce las consecuencias.

Este es también el paper donde el interés se corre desde «qué se puede expresar» hacia «cómo se compila». El 353 es un argumento sobre semántica; el 379 empieza a mirar la máquina: el abstract dedica la mitad de su extensión a enumerar «specific techniques for use by an optimizing compiler». Es la bisagra de la serie.

Y la conexión con RABBIT no hay que inferirla, porque el abstract del 379 la deja escrita como promesa, en 1976:

> «Such a compiler is to be built in the near future as a testing ground for these ideas.»

Ese compilador es RABBIT. El 379 anuncia la tesis que Steele va a defender un año y medio después.

> 🕳️ **HUECO — necesita a César:** de los cuatro, ¿cuál te costó más? Y ¿qué hiciste cuando te trabaste — lo abandonaste, buscaste ayuda, lo releíste meses después?

### El *GOTO* y el mito del procedure call caro (AI Memo 443, octubre de 1977)

Acá el borrador anterior tenía **dos piezas, y eran una sola**. Lo corrijo porque el error es instructivo: *LAMBDA: The Ultimate GOTO* y *Debunking the «Expensive Procedure Call» Myth* son **el mismo trabajo**, el AI Memo 443 de octubre de 1977. El título completo, tal como lo registra el catálogo del MIT, es *Debunking the "Expensive Procedure Call" Myth, or, Procedure Call Implementations Considered Harmful, or, Lambda: The Ultimate GOTO*[^goto]. Tres títulos apilados con «or,», que es exactamente el tipo de chiste que un AI Memo se permitía y un paper de revista no. Una versión salió además en las actas de la ACM National Conference de 1977[^goto_acm].

El «mito» que desarma es una creencia de la época —que llamar a un procedimiento es caro, y que por lo tanto un programador serio evita los procedimientos y escribe ciclos a mano. El abstract lo ataca de frente:

> «Folklore states that `GOTO` statements are "cheap", while procedure calls are "expensive". This myth is largely a result of poorly designed language implementations.»

Steele muestra que eso no es una verdad sobre el cómputo sino un artefacto de cómo estaban implementados los compiladores de entonces. Y de ahí sale la idea que le da el tercer título: una llamada en posición de cola no es una llamada, es un salto. Un `goto` con argumentos. Si es un salto, no tiene por qué costar lo que cuesta una llamada —no hay que empujar nada en el stack, porque no hay a dónde volver.

El abstract cierra con una frase que vale por todo el paper: «The difficulty with the `GOTO` statement and the procedure call is characterized as a conflict between abstract programming concepts and concrete language constructs.»

Es un movimiento retórico que vale la pena mirar aparte del contenido. El paper no dice «acá va mi lenguaje nuevo, es lindo». Dice: «lo que ustedes creen que es una ley de la naturaleza es en realidad un bug de sus herramientas». Eso es mucho más difícil de escribir, y mucho más efectivo. Y es la justificación de ingeniería de por qué Scheme exige eliminación de llamadas de cola: si el argumento de que la llamada es cara se cae, entonces no hay excusa para no hacerla barata.

De ese hilo —qué es una tail call, y cómo se vive sin stack— salen [[B-04]] y [[B-05]], que lo tratan en detalle.

[VERIFICAR: qué mide concretamente el Memo 443 — si hay benchmarks, sobre qué máquina y qué compiladores. El abstract (leído completo vía el registro OAI del MIT y wikisource) dice sólo que «Both theoretical ideas and an existing implementation are discussed which debunk this myth», sin nombrar la implementación ni dar un solo número; es plausible que «an existing implementation» sea RABBIT, pero el abstract no lo dice y NO hay que afirmarlo sin leer el cuerpo. Para resolverlo hace falta el PDF (AIM-443.pdf en DSpace), que no pude abrir: dspace.mit.edu responde HTTP 405 a fetch automatizado y web.archive.org está bloqueado para mí. Bajarlo a mano. No inventar números; o se citan los del paper o no se citan.]

### RABBIT (AI-TR-474, mayo de 1978)

Y después está la prueba. *RABBIT: A Compiler for SCHEME*, la tesis de maestría de Steele[^rabbit]. Los papers anteriores son argumentos; RABBIT es el argumento ejecutándose — el compilador que el 379 había prometido dos años antes. Si lambda realmente subsume las construcciones imperativas, entonces un compilador que trate todo como lambda tiene que poder generar código decente.

El abstract confirma que ese es literalmente el diseño: el compilador «knows relatively little about specific data manipulation primitives such as arithmetic operators, but concentrates on general issues of environment and control», y en vez de conocer muchas construcciones «handles only a small basis set which reflects the semantics of lambda-calculus». Todo lo demás —«sequencing, assignment, looping, `GOTO`, as well as many standard LISP constructs such as `AND`, `OR`, and `COND`»— entra como macros sobre esa base aplicativa. El Memo 353 en forma de software.

Y el resultado que hacía falta para cerrar el argumento: «A small number of optimization techniques, coupled with the treatment of function calls as `GOTO` statements, serve to produce code as good as that produced by more traditional compilers»[^rabbit].

Sobre el continuation-passing style: sí, y el abstract es explícito. La representación intermedia de RABBIT no son triples sino **un subconjunto del propio Scheme**, escrito «in the so-called continuation-passing style», elegido de modo que «all temporary quantities are made manifest as variables, and no control stack is needed to evaluate it». De ahí la frase con la que Steele cierra, que es una provocación de ingeniería: «an applicative language like SCHEME is a better candidate for an UNCOL than the more imperative candidates proposed to date».

Es también el más denso de todos: es una tesis, no un memo de veinte páginas. Y es donde la lectura deja de ser cómoda.

[VERIFICAR: sobre qué máquina corre RABBIT y qué genera exactamente como salida. El abstract (verificado vía OAI del MIT y research.scheme.org) NO menciona máquina destino ni lenguaje de salida — sólo la representación intermedia en CPS. Se dice comúnmente que emite MacLISP, y el memo 349 confirma que el interpreter original era MacLISP, pero eso NO es evidencia sobre RABBIT. Hace falta el cuerpo del PDF AITR-474 (DSpace bloquea fetch: HTTP 405). No afirmar la máquina de memoria.]

> 🕳️ **HUECO — necesita a César:** ¿llegaste a leer RABBIT entero, o lo hojeaste? Si lo abandonaste, decilo — es más útil para el lector que fingir que lo terminaste.

### Cómo leer estos papers en 2026

El consejo práctico, que es lo que quiero dejarte:

**Leelos en orden, pero no linealmente.** Primero el título y el abstract de los cuatro, de corrido, en veinte minutos. Vas a tener el mapa antes de entrar en ninguna página.

**Aceptá no entender el código la primera vez.** El Lisp de 1976 no es el Scheme que ves hoy. Hay sintaxis que ya no existe. No te trabes ahí: el argumento vive en la prosa, y el código es la evidencia.

**Leé el paper del mito primero si querés un enganche rápido.** Es el más corto de espíritu y el que tiene un adversario claro. Un paper con un adversario se lee solo.

**Usá las bibliotecas curadas.** El índice *The Lambda Papers* de research.scheme.org[^lambdapapers] es el más útil de todos: tiene la serie completa en orden, con número de memo, fecha y abstract de cada uno. El Software Preservation Group del Computer History Museum tiene la misma cronología con contexto histórico[^chm]. El mirror de readscheme.org en GitHub[^readscheme] es una bibliografía más amplia de research sobre Scheme. Y la sección de classic papers de Lambda the Ultimate[^ltu] es la referencia clásica, aunque hoy responde de manera intermitente. Si sos de perderte en enlaces, esos son tu piso firme.

> 🕳️ **HUECO — necesita a César:** ¿te acordás de la primera vez que intentaste leer *cualquier* paper técnico, sin saber que los papers se leen salteados? Ese recuerdo es el corazón emocional del post — necesito el detalle concreto (qué paper, dónde estabas, qué te pasó).

Y la razón de fondo por la que todavía vale la pena. Estos cuatro trabajos no envejecieron porque no son sobre Scheme. Son sobre qué es un lenguaje de programación —y esa pregunta no se resolvió. Cada vez que un lenguaje nuevo descubre las closures, o el pattern matching, o que las corrutinas se pueden hacer con continuaciones, está redescubriendo algo que está escrito, con todas las letras y en inglés claro, en un memo interno de un laboratorio de Cambridge de hace cincuenta años. Leerlos no es arqueología. Es enterarse antes.

Si querés empezar por otro lado —por el libro en vez del paper— [[A2-01]] es el camino: SICP es el mismo grupo de gente contándolo en 700 páginas y con clases grabadas.

> 🕳️ **HUECO — necesita a César:** ¿hay algún lenguaje o herramienta actual con el que trabajaste donde hayas dicho «esto ya lo leí en los Lambda Papers»? Un ejemplo concreto cerraría el post mucho mejor que la generalidad.

[^scheme349]: Gerald Jay Sussman y Guy Lewis Steele Jr., [*SCHEME: An Interpreter for Extended Lambda Calculus*](https://dspace.mit.edu/handle/1721.1/5794) — MIT AI Memo 349, diciembre de 1975. Handle `1721.1/5794`, identificador `AIM-349`.
[^imperative]: Guy Lewis Steele Jr. y Gerald Jay Sussman, [*LAMBDA: The Ultimate Imperative*](https://dspace.mit.edu/handle/1721.1/5790) — MIT AI Memo 353, marzo de 1976. Handle `1721.1/5790`, identificador `AIM-353`.
[^declarative]: Guy Lewis Steele Jr., [*LAMBDA: The Ultimate Declarative*](https://dspace.mit.edu/handle/1721.1/6091) — MIT AI Memo 379, noviembre de 1976. Handle `1721.1/6091`, identificador `AIM-379`. **Ojo:** el borrador anterior citaba el handle `1721.1/5789`, que es un item distinto (`AIM-351`, *A State Space Model for Sensorimotor Control and Learning*, de Marc Raibert). Corregido.
[^goto]: Guy Lewis Steele Jr., [*Debunking the "Expensive Procedure Call" Myth, or, Procedure Call Implementations Considered Harmful, or, Lambda: The Ultimate GOTO*](https://dspace.mit.edu/handle/1721.1/5753) — MIT AI Memo 443, octubre de 1977. Handle `1721.1/5753`, identificador `AIM-443`. Título completo según el registro del MIT: los tres títulos son del mismo trabajo.
[^goto_acm]: Guy Lewis Steele Jr., «Debunking the "expensive procedure call" myth or, procedure call implementations considered harmful or, LAMBDA: The Ultimate GOTO» — *Proceedings of the 1977 Annual Conference (ACM '77)*, ACM Press, 1977. DOI: [10.1145/800179.810196](https://doi.org/10.1145/800179.810196). Metadatos verificados vía la API de Crossref; la página de la ACM Digital Library bloquea fetch automatizado.
[^opcode]: Guy Lewis Steele Jr. y Gerald Jay Sussman, [*Design of LISP-based Processors, or SCHEME: A Dielectric LISP, or Finite Memories Considered Harmful, or LAMBDA: The Ultimate Opcode*](https://dspace.mit.edu/handle/1721.1/5731) — MIT AI Memo 514, marzo de 1979. Handle `1721.1/5731`, identificador `AIM-514`. El cuarto y último de los papers titulados «LAMBDA: The Ultimate ___».
[^rabbit]: Guy Lewis Steele Jr., [*RABBIT: A Compiler for SCHEME*](https://dspace.mit.edu/handle/1721.1/6913) — MIT AI-TR-474, mayo de 1978. Handle `1721.1/6913`, identificador `AITR-474`. Tesis de maestría.
[^constraints]: Guy Lewis Steele Jr., [*The Definition and Implementation of a Computer Programming Language Based on Constraints*](https://dspace.mit.edu/handle/1721.1/6933) — MIT AI-TR-595, agosto de 1980. Handle `1721.1/6933`, identificador `AITR-595`. Tesis doctoral **de Steele**, no de Sussman, y de 1980, no de 1973 (el borrador anterior se equivocaba en ambas cosas).
[^sussman73]: Gerald Jay Sussman, [*A Computational Model of Skill Acquisition*](https://dspace.mit.edu/handle/1721.1/6894) — MIT AI-TR-297, agosto de 1973. Handle `1721.1/6894`, identificador `AITR-297`. Es la verdadera tesis doctoral de Sussman de 1973 (sobre HACKER), y no trata sobre definición de lenguajes.
[^lambdapapers]: [*The Lambda Papers* — research.scheme.org](https://research.scheme.org/lambda-papers/). Índice de la serie completa con memo, fecha y abstract de cada trabajo. Backup en Wayback: [snapshot del 2026-02-01](http://web.archive.org/web/20260201181527/https://research.scheme.org/lambda-papers/).
[^chm]: [SCHEME family — Software Preservation Group, Computer History Museum](https://softwarepreservation.computerhistory.org/LISP/scheme_family.html). Cronología independiente de los AI Memos de Scheme; corrobora memo, mes y año de toda la serie.
[^readscheme]: [readscheme.org — mirror en GitHub](https://github.com/scheme-and-computer-science/library.readscheme.org). Bibliografía curada de research sobre Scheme, originalmente mantenida por Jim Bender.
[^ltu]: [Lambda the Ultimate — classic papers](http://lambda-the-ultimate.org/classic/papers.html). **No verificada:** el sitio cortó la conexión (`ECONNRESET` / socket cerrado) en todos los intentos del 2026-07-15; la API de Wayback informa un snapshot con status 200 del 2026-04-25, pero no pude abrirlo para confirmar el contenido. Backup declarado: `http://web.archive.org/web/20260425041048/http://lambda-the-ultimate.org/classic/papers.html`. Confirmar a mano antes de publicar.

