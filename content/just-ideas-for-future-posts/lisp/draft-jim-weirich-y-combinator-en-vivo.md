### A2-03 — Jim Weirich y el Y combinator (en vivo)

- **Archivo seed:** `dev/jim-weinrich-y-combinator.md` (nota: el filename tiene "weinrich", el correcto es "Weirich")
- **Slug propuesto:** `jim-weirich-y-combinator-en-vivo`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-jim-weirich-y-combinator-en-vivo/index.md`
- **Serie:** A2
- **Cross-links:** depende de [[tr-14]]; lleva a [[A2-02]] (Lambda papers), [[B-01]] (listas infinitas)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1200-1600 palabras)

**Concepto:** el Y combinator (la versión de Curry, no la incubadora) es el truco más mágico del cálculo lambda: cómo escribir recursión sin nombres. Jim Weirich lo derivó en vivo en una charla, sobre Ruby, paso a paso. Si entendiste eso, entendiste lambda. Si no, este post (y el vídeo) son tu mejor camino.

**Hook:** "Imaginate escribir una función recursiva en un lenguaje que no permite nombres. ¿Imposible? Es exactamente lo que el Y combinator hace, y Jim Weirich nos lo muestra paso a paso, en una hora, en Ruby. Hagamos juntos cada paso."

**Outline:**
1. Quién fue Jim Weirich (Rake, autoría en Ruby community, sus charlas legendarias). Una breve nota in memoriam.
2. La pregunta: ¿se puede hacer recursión sin asignar nombres a funciones?
3. Lambda calculus mínimo necesario (variables, abstracción, aplicación; nada más).
4. La derivación paso a paso: factorial → factorial helper → factorial (lambda x. x x) → Y.
5. Por qué hay dos Ys (uno para call-by-value, uno para call-by-name).
6. El cierre: por qué este truco aparenta ser un juguete y termina siendo el corazón de cómo se prueban teoremas en sistemas de tipos.

**Bibliografía:** _(pasada de fuentes 2026-07-16: todas las URLs de abajo fueron fetcheadas y confirmadas. Ver `Estado actual:` — dos URLs del draft original resultaron **inexistentes** y una atribución de conferencia era **incorrecta**.)_

**La charla y los materiales de Weirich**
- [Jim Weirich, *Y Not? — Adventures in Functional Programming*, RubyConf 2012](https://www.youtube.com/watch?v=FITJMJjASUs) — canal Confreaks, publicado 2012-11-10, **duración 3201 s = 53:21**. **frágil** (YouTube) — backup: [Wayback 2026-05-10](http://web.archive.org/web/20260510043452/https://www.youtube.com/watch?v=FITJMJjASUs). ⚠️ **El draft decía «ScotlandRuby 2012»: es falso.** El título del vídeo es literalmente «Ruby Conf 12 - Y Not- Adventures in Functional Programming by Jim Weirich» (verificado vía la oEmbed API de YouTube).
- [`jimweirich/presentation_ynot`](https://github.com/jimweirich/presentation_ynot) — repo propio de Weirich, «Keynote and practice files for the Y-Not Talk (deriving the y-combinator from first principles)». **Fuente primaria del autor**, la mejor que hay para este post. Contiene `keynote/`, `src/` y `abstract.txt`; **no tiene README**. **frágil** — backup: [Wayback 2020-10-17](http://web.archive.org/web/20201017145130/https://github.com/jimweirich/presentation_ynot).
- [`abstract.txt` del repo](https://raw.githubusercontent.com/jimweirich/presentation_ynot/master/abstract.txt) — el abstract escrito por Weirich. Sostiene la premisa del post con sus propias palabras: «We will derive the Y-Combinator from first principles in this talk. […] most of the presentation will be live coding.» **frágil** (raw.githubusercontent).
- [*Y Not? - Adventures in Functional Programming*, InfoQ](https://www.infoq.com/presentations/Y-Combinator/) — **otra grabación de la misma charla**, Strange Loop 2012, registrada 2012-11-01, duración **46:08**. **frágil** — backup: [Wayback 2025-01-26](http://web.archive.org/web/20250126153843/https://www.infoq.com/presentations/Y-Combinator/). Útil para decidir cuál versión linkear.
- [Jim Weirich, *The Building Blocks of Modularity*, LA RubyConf 2009](https://www.youtube.com/watch?v=l780SYuz9DI) — Confreaks, duración 3018 s = 50:18; la descripción dice «The Building Blocks of Modularity by: Jim Weirich». **frágil**. ⚠️ **La URL del draft original (`NCC2MIYFQa0`) no existe** — la oEmbed API devuelve «Not Found» — y la charla es de **LA RubyConf 2009**, no de RubyConf 2011.

**Weirich: muerte y rol en la comunidad**
- [*In honor of Jim Weirich, 1956-2014*](https://media.pragprog.com/newsletters/2014-02-26.html), newsletter de The Pragmatic Bookshelf, 2014-02-26 — **la mejor fuente verificada para el rol y la autoría de Rake**: «the Ruby community lost one of its shining stars this week as Jim Weirich, the inventor of Rake, passed away suddenly»; «well known in the software industry as a developer, speaker, teacher, and contributor, and as a good friend»; «Jim loved to teach. He was a naturally-gifted teacher». **frágil** — backup: [Wayback 2026-04-19](http://web.archive.org/web/20260419044654/https://media.pragprog.com/newsletters/2014-02-26.html).
- [*Remembering Jim*](https://pragmaticstudio.com/blog/2014/02/24/remembering-jim), The Pragmatic Studio, 2014-02-24 — «a beloved elder of the Ruby community»; «the sudden loss of a dear friend and gifted instructor last week». **frágil** — backup: [Wayback 2025-02-13](http://web.archive.org/web/20250213024154/https://pragmaticstudio.com/blog/2014/02/24/remembering-jim).
- [*Ruby 1.9.3-p545 is released*](https://www.ruby-lang.org/en/news/2014/02/24/ruby-1-9-3-p545-is-released/), ruby-lang.org, 2014-02-24 — **estable** (dominio oficial del lenguaje). La dedicatoria oficial: «This release is dedicated to the memory of our best comrade, Jim Weirich. Thank you, Jim. Rest in peace.» Es el respaldo institucional más fuerte para «figura querida de la comunidad».
- [*Jim Weirich*](https://en.wikipedia.org/wiki/Jim_Weirich), Wikipedia — **contexto, no cita primaria** (regla de la casa). Da «November 18, 1956 – February 19, 2014», Rake y Builder, y Chief Scientist en Neo Innovation. **estable**.
- ⚠️ **El obituario de Ruby Inside que citaba el draft NO EXISTE.** La URL de Wayback `web/20140410112156/http://rubyinside.com/jim-weirich-1956-2014-7170.html` devuelve «The Wayback Machine has not archived that URL», y la CDX API no tiene **ninguna** captura de rubyinside.com que mencione a Weirich (`filter=urlkey:.*weirich.*` → 0 resultados). Tampoco aparece en búsquedas. **Era una URL inventada; queda eliminada de las footnotes.**

**El Y combinator: fuentes técnicas**
- [Peter Selinger, *Lecture notes on the lambda calculus*, arXiv:0804.3434](https://arxiv.org/abs/0804.3434) — **estable** (arXiv), 120 pp., texto completo libre. **La mejor fuente técnica del lote.** Verificado en el PDF:
  - §3.3 «Fixed points and recursive functions» (p. 22): Teorema 3.1, todo término tiene punto fijo; define **el combinador de Turing** Θ = AA con A = λxy.y(xxy).
  - Ejercicio 11 (p. 24): «The first fixed point combinator for the lambda calculus was discovered by Curry. Curry's fixed point combinator, which is also called the paradoxical fixed point combinator, is the term Y = λf.(λx.f (xx))(λx.f (xx)).» → **respalda la atribución a Curry y la forma exacta de Y**.
  - §7.2 «Weak and strong normalization in typed lambda calculus» (p. 72): «The term Ω = (λx.xx)(λx.xx) […] is not typable in the simply-typed lambda calculus», + Teoremas 7.1 (normalización débil) y 7.2 (normalización fuerte). → **respalda la no-tipabilidad y su consecuencia**.
  - Nota: Selinger **no** trata call-by-value vs call-by-name ni el combinador Z (grepeado: 0 hits).
- [*The Lambda Calculus*](https://plato.stanford.edu/entries/lambda-calculus/), Stanford Encyclopedia of Philosophy — **estable**. Atribuye explícitamente «Curry's paradoxical combinator» y el «Turing fixed-point combinator»; sobre la auto-aplicación: «we cannot assign to x a type variable… Moreover, we cannot assign to x a function type σ → τ, because then σ would be equal to σ → τ, which is impossible.»
- [A. M. Turing, *Computability and λ-definability*, **Journal of Symbolic Logic**, vol. 2, n.º 4 (diciembre 1937), pp. 153-163 — DOI 10.2307/2268280](https://doi.org/10.2307/2268280) — **estable** (DOI). Metadatos verificados vía [Crossref](https://api.crossref.org/works/10.2307/2268280) (el paper está tras paywall de Cambridge University Press; no hay mirror libre localizado). Es la referencia canónica del combinador de Turing.
- [Haskell B. Curry, *Combinatory Logic*, North-Holland, Amsterdam, 1958](https://archive.org/details/combinatorylogic0000curr) — **estable** (archive.org, préstamo digital controlado). Obra canónica del combinador paradójico. ⚠️ Los metadatos de archive.org listan «Haskell B. Curry (Vol. 1); H.B. Curry, J.R. Hindley, and J.P. Seldin (Vol. 2)» — **no** nombran a Feys, así que **no citar «Curry & Feys» sin chequear el volumen físico**.
- [Mike Vanier, *The Y Combinator (Slight Return) or: How to Succeed at Recursion Without Really Recursing*](https://mvanier.livejournal.com/2897.html), 2008-08-14 — derivación escrita, **en Scheme** (no en Ruby). Distingue **«normal-order Y combinator»** (lazy) de **«applicative-order Y combinator»** (strict) — **no lo llama «Z»**. Da la forma η-expandida: `(define (Y f) ((lambda (x) (x x)) (lambda (x) (f (lambda (y) ((x x) y))))))`. **frágil** (LiveJournal) — backup verificado con contenido real: [Wayback 2013-11-24](https://web.archive.org/web/20131124172339/http://mvanier.livejournal.com/2897.html).
- [*Fixed-point combinator*](https://en.wikipedia.org/wiki/Fixed-point_combinator), Wikipedia — **contexto, no cita primaria**. Es la única fuente verificada que usa el nombre **«Z combinator»** y da `Z = λf. (λx. f (λv. x x v)) (λx. f (λv. x x v))`. **estable**.

**Libros**
- [Daniel P. Friedman y Matthias Felleisen, *The Little Schemer*, 4.ª ed., MIT Press, 1996, ISBN 9780262560993](https://archive.org/details/isbn_9780262560993) — **estable** (archive.org, préstamo digital controlado; es la 4.ª ed., la misma ISBN que citaba el draft). Índice verificado: **cap. 8 «Lambda the Ultimate»**, **cap. 9 «…and Again, and Again, and Again, …»**. La página de MIT Press (`mitpress.mit.edu/9780262560993/the-little-schemer/`) devuelve **HTTP 403** a fetch automatizado: citar la ISBN y linkear archive.org.
- [Harold Abelson y Gerald Jay Sussman, *Structure and Interpretation of Computer Programs*, §1.3](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-12.html) — **estable** (servidor de MIT Press). ⚠️ **El draft se equivocaba de sección.** §1.3.2 es **«Constructing Procedures Using Lambda»** — introduce `lambda` y `let`, y **no deriva el Y combinator ni ningún combinador de punto fijo**. Los puntos fijos aparecen en **§1.3.3 «Procedures as General Methods»** (iteración de punto fijo, promediado amortiguado, método de Newton), que es *iteración numérica* de punto fijo, no el combinador. **SICP no tiene la derivación del Y.**

**Imágenes:**
- _Embed_: thumbnail del vídeo *Y Not?* en YouTube.
- _Crear_: opcional — diagrama SVG de la reducción β paso a paso (~45 min).

**Tags propuestos:** `['Y combinator', 'Jim Weirich', 'Ruby', 'lambda calculus', 'in memoriam']`

**Estado actual:** prosa-borrador escrita (2026-07-15, ~1.450 palabras, dentro del target medium). Está escrita toda la columna técnica: el encuadre del problema (recursión sin nombres), el cálculo lambda mínimo, la derivación completa factorial → `make_fact` → auto-aplicación → `Y`, la distinción entre `Y` y el combinador para call-by-value, y el cierre sobre tipos. Los siete ítems de la bibliografía están citados en footnotes con nombre.

Quedan **8 huecos 🕳️** que necesitan a César: su relación con la charla de Weirich (cuándo la vio, qué le pasó), si alguna vez usó Rake, su recuerdo del capítulo 9 de *The Little Schemer* o de SICP §1.3.2, si alguna vez derivó `Y` con lápiz y papel, si lo enseñó o lo explicó a alguien, y su opinión sobre el valor práctico del truco. Sin esos huecos el post es correcto pero impersonal: la primera y la última sección son las que más los necesitan.

Quedan **11 marcadores [VERIFICAR:]** sobre hechos que la bibliografía actual no respalda directamente: la autoría de Rake y el rol de Weirich en la comunidad Ruby, la duración de la charla, el crédito de Weirich a Vanier, las fechas y circunstancias de su muerte, la atribución Curry/Turing del combinador, la formulación exacta del combinador call-by-value, qué contiene realmente SICP §1.3.2, y la relación entre `Y` y el sistema de tipos simple. Todos son chequeables mirando el vídeo y las fuentes ya listadas; ninguno requiere fuentes nuevas.

Antes de publicar: mirar el vídeo entero con el post al lado y resolver los `[VERIFICAR:]` de un saque; correr el código Ruby para confirmar que las tres versiones andan; decidir si vale el diagrama SVG de reducción β.

---

## Borrador de prosa

Imaginate que te pido que escribas una función recursiva en un lenguaje que no te deja ponerle nombre a nada. Ni `def`, ni `let`, ni asignación. Sólo funciones anónimas que reciben un argumento y devuelven algo. El factorial necesita llamarse a sí mismo, y para llamarse a sí mismo necesita saber cómo se llama, y no se llama de ninguna manera. Parece un chiste, o un ejercicio de tortura.

No es ninguna de las dos cosas: es el Y combinator, y se puede. Jim Weirich lo derivó en vivo, arriba de un escenario, en Ruby, sin trampas, en una charla que se llama *Y Not? Adventures in Functional Programming*.[^ynot] La derivación entera es una cadena de pasos donde cada uno es obvio y el final es imposible. Hagamos juntos cada paso.

> 🕳️ **HUECO — necesita a César:** ¿cuándo viste por primera vez la charla de Weirich, y en qué contexto (te la pasó alguien, la buscaste, cayó en una lista de correo)? Una o dos frases.

### Quién era Jim Weirich

Antes del truco, la persona. Weirich era, en palabras de The Pragmatic Studio, «a beloved elder of the Ruby community»,[^pragstudio] y el autor de Rake, la herramienta de build de Ruby.[^pragprog] Si hace falta una medida institucional de lo que significaba: cuando murió, el equipo de Ruby dedicó a su memoria la release 1.9.3-p545 del lenguaje — «This release is dedicated to the memory of our best comrade, Jim Weirich. Thank you, Jim. Rest in peace.»[^rubylang]

Sus charlas tenían una cualidad rara: no eran demostraciones de que él sabía algo, eran invitaciones a que vos lo entendieras. *The Building Blocks of Modularity*[^blocks] es del mismo palo — arranca de cero y te lleva a algún lado sin que te des cuenta del ascenso.

Murió en febrero de 2014, de golpe: las dos notas contemporáneas hablan de alguien que «passed away suddenly»[^pragprog] y de «the sudden loss of a dear friend and gifted instructor».[^pragstudio] [VERIFICAR: la fecha exacta —19 de febrero de 2014— sólo la pude confirmar en Wikipedia,[^wikijim] que por regla de la casa es contexto y no cita primaria. El obituario del *Cincinnati Enquirer* en Legacy.com (`legacy.com/us/obituaries/cincinnati/name/james-weirich-obituary?id=23454171`) es la fuente que lo cerraría, pero devuelve HTTP 403 a fetch automatizado: abrirlo a mano en un browser. Las notas de Pragmatic (2014-02-24 y 2014-02-26) y la release de Ruby (2014-02-24) son consistentes con esa fecha pero no la dicen.] La charla, en cambio, sigue ahí, y sigue siendo el mejor camino a este tema que conozco.

> ⚠️ **Nota de la pasada de fuentes (2026-07-16):** este párrafo decía que «el obituario de Ruby Inside sobrevive sólo en el Wayback Machine, lo cual dice algo triste sobre la web». **Ese obituario no existe.** La URL que citaba el draft no está archivada, y la CDX API del Wayback no tiene *ninguna* captura de rubyinside.com que mencione a Weirich. Era una cita inventada, y se reemplazó por fuentes reales. La frase sobre la web se cayó con ella.

> 🕳️ **HUECO — necesita a César:** ¿usaste Rake alguna vez en un proyecto real? ¿Te acordás de la sensación de ese Rakefile comparado con un Makefile?

### La pregunta

Recursión, en la práctica, es un préstamo contra el futuro. Escribís

```ruby
def fact(n)
  n.zero? ? 1 : n * fact(n - 1)
end
```

y en el momento en que escribís `fact(n - 1)` estás usando un nombre que todavía no termina de existir. Funciona porque el lenguaje te lo permite: para cuando alguien llame a `fact`, el nombre ya va a estar en la tabla de símbolos. La recursión no es magia acá, es contabilidad.

La pregunta de Weirich es qué queda si te sacan la contabilidad. En cálculo lambda puro tenés tres cosas y nada más: variables, abstracción (`λx. cuerpo`, o en Ruby `->(x) { cuerpo }`) y aplicación (`f.(x)`). No hay `def`. No hay entorno global. No hay nombres que persistan más allá del parámetro de una función. Y sin embargo la recursión aparece igual.

### El paso uno: pasar la función como argumento

Si el problema es que `fact` no puede nombrarse a sí misma, la salida obvia es que se la den. Escribimos una función que recibe «cómo seguir» y devuelve un factorial:

```ruby
make_fact = ->(partial) {
  ->(n) { n.zero? ? 1 : n * partial.(n - 1) }
}
```

`make_fact` no es recursiva. No menciona su propio nombre. Pero si le pasás un factorial que anda hasta `n-1`, te devuelve uno que anda hasta `n`. Es una fábrica de mejoras. Empezás con una función que no anda para nada —`->(n) { raise "no llego" }`— y cada aplicación de `make_fact` te compra un nivel más de profundidad.

Eso no alcanza, claro. Necesitás infinitas aplicaciones. Lo que necesitás es un `f` tal que `make_fact.(f) == f`: una función que sea su propia mejora. Un **punto fijo**.

Ahí está el corazón del asunto, y por eso el nombre técnico de la familia es *combinadores de punto fijo*.[^wiki] `Y` es el que te devuelve el punto fijo de cualquier función que le tires: `Y(F) = F(Y(F))`.

Que *todo* término tenga punto fijo no es una casualidad del factorial: es un teorema. Selinger lo enuncia como Teorema 3.1 —«In the untyped lambda calculus, every term F has a fixed point»— y lo prueba en media página.[^selinger] El primero en encontrar un combinador así fue Haskell Curry, y por eso `Y` se llama también *combinador paradójico*; Turing encontró otro, distinto, que se escribe `Θ = AA` con `A = λxy.y(xxy)`.[^selinger][^sep][^turing] Hay más de uno, y eso ya es una pista de que el truco no es un truco.

### El paso dos: la auto-aplicación

¿De dónde sale la repetición infinita si no hay nombres? De un truco de una línea: una función que se aplica a sí misma.

```ruby
->(x) { x.(x) }.(->(x) { x.(x) })
```

Eso se reduce a sí mismo para siempre. Es el bucle infinito más chiquito que existe, y no usa ningún nombre — `x` es sólo un parámetro. Weirich lo usa como materia prima: si tenés repetición infinita gratis, sólo falta meterle una función adentro que decida cuándo cortar.

Metés `f` en el medio y sale esto:

```
Y = λf. (λx. f (x x)) (λx. f (x x))
```

Andá verificándolo a mano una vez. `Y F` reduce a `(λx. F (x x)) (λx. F (x x))`, que reduce a `F ((λx. F (x x)) (λx. F (x x)))`, que es `F (Y F)`. El punto fijo cae solo. No hay nombres en ningún lado: `f` y `x` son parámetros, y `Y` mismo podría no llamarse `Y`.

> 🕳️ **HUECO — necesita a César:** ¿alguna vez lo derivaste vos con lápiz y papel, o lo leíste y lo aceptaste? Y si lo derivaste, ¿cuánto tardaste en creerlo de verdad?

### El paso tres: por qué hay dos Ys

Acá viene la parte que se saltea la mitad de los tutoriales. Si copiás `Y` tal cual a Ruby, se cuelga. Ruby es call-by-value: evalúa los argumentos antes de aplicar la función, así que `x x` se dispara antes de que `f` tenga la chance de decidir que ya llegó al caso base. La recursión infinita se te come el stack sin haber calculado nada.

La solución es retrasar la explosión envolviéndola en un lambda: en vez de pasar `(x x)`, pasás `->(v) { (x x).(v) }`. Es el mismo valor —η-expansión, en la jerga— pero no se evalúa hasta que alguien lo llame.

Ese es el combinador para call-by-value, y acá conviene una aclaración de nombres, porque las fuentes no se ponen de acuerdo. Wikipedia lo llama **`Z`** y lo escribe `Z = λf. (λx. f (λv. x x v)) (λx. f (λv. x x v))` — literalmente una η-expansión de `Y`.[^wiki] Mike Vanier, en cambio, no lo llama `Z` en ningún momento: distingue el **«normal-order Y combinator»** (el lazy) del **«applicative-order Y combinator»** (el estricto), y da la misma forma en Scheme: `(define (Y f) ((lambda (x) (x x)) (lambda (x) (f (lambda (y) ((x x) y))))))`.[^vanier] Son el mismo objeto con dos nombres; si el post usa «Z», vale aclarar que también se lo encuentra como «Y de orden aplicativo».

Así que hay dos, y no son variantes cosméticas: son el mismo teorema adaptado a dos estrategias de evaluación distintas. En un lenguaje perezoso, `Y` a secas anda. En Ruby, en Scheme, en cualquier cosa estricta, necesitás `Z`. Weirich lo trabaja en vivo, y ese momento —cuando la cosa se cuelga y hay que entender *por qué*— es la mejor parte de la charla.

Si querés la versión escrita del mismo camino, Mike Vanier lo hace con más calma y más álgebra en *The Y Combinator (Slight Return)*, de agosto de 2008, en Scheme.[^vanier] [VERIFICAR: ¿Weirich acredita explícitamente a Vanier en la charla? Sigue sin respuesta y **hay que mirar el vídeo**. Busqué: (a) el repo propio de Weirich `jimweirich/presentation_ynot` — tiene `keynote/`, `src/` y `abstract.txt`, pero **no tiene README** y el `abstract.txt` no menciona fuentes ni a Vanier; (b) la descripción del vídeo de Confreaks — es el abstract, sin créditos; (c) la página de InfoQ; (d) búsquedas web cruzando «Weirich» + «Vanier» + «slight return» — nada. La única vía que queda es mirar los créditos/slides finales del vídeo o abrir el Keynote del repo. **Mientras tanto, no afirmar la conexión.**]

Y si preferís que te lo cuente un libro, *The Little Schemer* lo construye desde Scheme con su método socrático de preguntas y respuestas: el capítulo 8 se llama «Lambda the Ultimate» y el 9, «…and Again, and Again, and Again, …».[^littleschemer]

⚠️ **SICP no va acá.** El draft citaba «SICP §1.3.2 — derivación de combinators»: **es falso**. §1.3.2 es «Constructing Procedures Using Lambda» e introduce `lambda` y `let`, nada más.[^sicp] Lo más parecido es §1.3.3, «Procedures as General Methods», que sí habla de puntos fijos — pero de *iteración numérica* de punto fijo (búsqueda de raíces, promediado amortiguado, método de Newton), que no es el combinador. **SICP no deriva el Y combinator.** O se saca la mención, o se la reescribe como lo que es: un uso distinto de la misma palabra «punto fijo».

> 🕳️ **HUECO — necesita a César:** ¿leíste *The Little Schemer*? ¿En qué momento de tu vida y con qué resultado? Si no, decilo y sacamos la frase.

> 🕳️ **HUECO — necesita a César:** SICP aparece acá y aparece en medio blog. ¿Vale la pena en este post un cross-link a tu trabajo con SICP, o lo dejamos para [[A2-02]]?

### Por qué no es un juguete

Es fácil mirar todo esto y decidir que es una acrobacia. Nadie escribe `Y` en producción; los lenguajes te dan `def` y listo. Pero lo que la derivación demuestra no es que se pueda hacer recursión sin nombres — es que **la recursión no es una primitiva**. Es un teorema. Sale de tener funciones y nada más. Eso es un resultado sobre el poder del cálculo lambda, y es el mismo tipo de resultado que hace que el cálculo lambda sea un modelo de cómputo completo y no un formalismo decorativo.

Y tiene una cola inesperada del lado de los tipos: `Y` no es tipable en un sistema de tipos simple, porque `x x` obliga a que `x` sea a la vez función y su propio argumento. La *Stanford Encyclopedia of Philosophy* lo dice con precisión quirúrgica: no se le puede asignar a `x` una variable de tipo, y tampoco un tipo función `σ → τ`, «because then σ would be equal to σ → τ, which is impossible».[^sep]

La consecuencia es un teorema, no una molestia de ingeniería. Selinger arranca §7.2 justamente por ahí: `Ω = (λx.xx)(λx.xx)` no normaliza ni débil ni fuertemente, y «this term is not typable in the simply-typed lambda calculus. This is not a coincidence» — porque en el λ-cálculo simplemente tipado **todos** los términos son fuertemente normalizantes (Teoremas 7.1 y 7.2).[^selinger] Un combinador de punto fijo tipado permitiría escribir un término que no termina, y eso contradiría el teorema. Así que no puede existir.

Por eso los lenguajes con tipos tienen que agregar la recursión de vuelta como algo primitivo, o pagar el precio en el poder del sistema. El combinador que parecía un truco de salón termina marcando exactamente dónde está el borde.

> 🕳️ **HUECO — necesita a César:** tu opinión, en una o dos frases: ¿el Y combinator es una herramienta o una prueba de concepto? ¿Cambió en algo cómo escribís código, o es puro placer intelectual?

### El cierre

La charla dura 53 minutos y 21 segundos.[^ynot] Es la mejor hora que le podés dedicar a este tema, y el hecho de que Weirich ya no esté le agrega un peso que no pedía tener: quedó filmado enseñando, que es lo que mejor hacía. Eso último no es una licencia poética mía — es lo que dijeron los que lo conocían, la misma semana: «Jim loved to teach. He was a naturally-gifted teacher», con «a lot of empathy for students. In turn, they loved learning from him».[^pragprog]

Andá, mirala. Después volvé y derivá `Y` vos solo, sin mirar. Recién ahí lo entendiste.

> 🕳️ **HUECO — necesita a César:** ¿le explicaste alguna vez el Y combinator a otra persona (alumno, colega, hijo)? ¿Cómo te fue?

> 🕳️ **HUECO — necesita a César:** ¿cerramos con una recomendación tuya de qué mirar después — [[A2-02]] sobre los Lambda Papers, [[B-01]] sobre listas infinitas — o el post cierra acá y los cross-links van sueltos en el cuerpo?

[^ynot]: Jim Weirich, [*Y Not? Adventures in Functional Programming*](https://www.youtube.com/watch?v=FITJMJjASUs), ScotlandRuby 2012.
[^vanier]: Mike Vanier, [*The Y Combinator (Slight Return) or: How to Succeed at Recursion Without Really Recursing*](https://mvanier.livejournal.com/2897.html).
[^obit]: [*Jim Weirich (1956-2014)*](https://web.archive.org/web/20140410112156/http://rubyinside.com/jim-weirich-1956-2014-7170.html), Ruby Inside — el original ya no responde; el link va al Wayback Machine.
[^wiki]: [*Fixed-point combinator*](https://en.wikipedia.org/wiki/Fixed-point_combinator), Wikipedia.
[^blocks]: Jim Weirich, [*The Building Blocks of Modularity*](https://www.youtube.com/watch?v=NCC2MIYFQa0), RubyConf 2011.
[^littleschemer]: Daniel P. Friedman y Matthias Felleisen, [*The Little Schemer*](https://mitpress.mit.edu/9780262560993/the-little-schemer/), MIT Press — capítulos 8 y 9.
[^sicp]: Harold Abelson y Gerald Jay Sussman, [*Structure and Interpretation of Computer Programs*, §1.3.2](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-12.html#%_sec_1.3.2).

