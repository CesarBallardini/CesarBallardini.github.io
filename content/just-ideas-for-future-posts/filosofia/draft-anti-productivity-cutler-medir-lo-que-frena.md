### C-13 — Anti-productivity: medí lo que te frena, no lo que producís (John Cutler)

- **Archivo seed:** _draft-rest.md bucket 6 (cosechado 2026-04-09)_
- **Slug propuesto:** `anti-productivity-cutler-medir-lo-que-frena`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-anti-productivity-cutler-medir-lo-que-frena/index.md`
- **Serie:** filosofia
- **Cross-links:** [[C-03]] (Tidy First), [[C-11]] (Goodhart), [[C-12]] (Forest/Desert)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** John Cutler escribió un artículo titulado *Anti-productivity* donde propone que en software no podemos medir productividad directamente, pero SÍ podemos medir *anti-productividad* — el tiempo perdido en fricciones, esperas, ambigüedades, retrabajos. Esta es la filosofía detrás del DX (Developer Experience) score que vende DX Inc. y que Kent Beck endorsa con reservas. El post discute la idea: en vez de "cuántos commits por desarrollador", medí "cuánto tiempo perdiste en CI esta semana".

**Hook:** "no podés medir cuánta agua pasa por el río, pero sí podés medir cuánto barro hay obstruyéndolo." Esa es la idea de John Cutler sobre productividad en software. Acá está cómo aplicarla.

**Outline:**

1. **Hook — el río y el barro.** La metáfora de Cutler; el planteo: la productividad no se deja mirar de frente, la fricción sí.
2. **Por qué el numerador no existe.** El problema real: en software no hay unidad de output. Líneas, commits, story points, features — todos son proxies del esfuerzo, no del valor. El numerador de la fracción está vacío.
3. **La inversión de Cutler.** Si no podés medir lo que producís, medí lo que te lo impide. El movimiento retórico y por qué es más honesto que el anterior.
4. **Qué es una fricción medible.** El catálogo concreto: esperas (CI, code review, aprobaciones), ambigüedad (no sé qué construir), retrabajo (lo construí mal), entorno (tarda en levantar). Todas tienen algo en común: el desarrollador las puede reportar sin mentir, porque no lo dejan mal parado a él.
5. **El aparato comercial: DX Inc., el DXI y las Core 4.** La idea tiene dueño y tiene precio. Distinguir los **dos** productos de DX: el DXI (14 drivers, sí encuadrado como anti-productividad por el propio Noda) y el Core 4 (Speed/Effectiveness/Quality/Impact, donde Speed = *diffs per engineer*, o sea el numerador vacío otra vez). La ironía de que la misma empresa venda las dos cosas es material del post, no una nota al pie.
6. **Beck endorsando con reservas — y cobrando.** La conversación con Noda: Beck abre con Goodhart, dice que le teme al mal uso, y sentencia que «vender el dashboard es mala praxis». Pero la conversación es **auspiciada y pagada por DX**, y él lo declara. El giro: usó el aviso pago para advertirle al sponsor.
7. **Accelerate como el antecedente que ya hizo este camino.** Las métricas de DORA miden el sistema de entrega, no a la persona. Cutler es el mismo movimiento, un paso más adentro. Aclarar que DORA hoy publica cinco métricas, no cuatro.
8. **La objeción seria: la anti-productividad también se Goodhartea.** [[C-11]]. Si medís tiempo de CI, alguien va a borrar tests. Si medís esperas de review, alguien va a aprobar sin leer. El barro también se puede maquillar.
9. **Cierre — qué haría yo el lunes.** La versión sin dashboard ni licencia: preguntar, anotar, mirar. Y la advertencia de [[C-12]]: la fricción que medís es la del bosque en el que estás.

**Bibliografía:** _(todas las URLs fetcheadas y verificadas el 2026-07-15)_

- **[Fuente primaria de Cutler]** John Cutler, [TBM 240: The Ultimate Guide to Developer Counter-Productivity](https://cutlefish.substack.com/p/tbm-240-the-ultimate-guide-to-developer) — *The Beautiful Mess*, 2023-09-02. **Ojo: el título real es «Counter-Productivity», no «Anti-productivity».** 26 familias de trabajo de apalancamiento negativo. Sin metáfora de río/barro. Backup: [Wayback 2026-03-28](http://web.archive.org/web/20260328152625/https://cutlefish.substack.com/p/tbm-240-the-ultimate-guide-to-developer). *(frágil)*
- John Cutler, [About — The Beautiful Mess](https://cutlefish.substack.com/about) — bio profesional propia (Amplitude, Medium desde 2015, Substack desde 2020). *(frágil)*
- **[Fuente primaria de Beck]** Kent Beck y Abi Noda, [Developer Productivity Metrics: Education Necessary](https://newsletter.kentbeck.com/p/developer-productivity-metrics-education) — 2025-01-29. **Conversación auspiciada y pagada por DX** (declarado en el post). Contiene: la cita de Cutler en boca de Noda, la Ley de Goodhart traída por Beck, «if you just sell the dashboard, that's malpractice», y el claim de los 13 minutos por punto de DXI. Backup: [Wayback 2026-04-12 (dominio viejo)](http://web.archive.org/web/20260412123620/https://tidyfirst.substack.com/p/developer-productivity-metrics-education). *(frágil)*
- Abi Noda, [Measuring developer productivity: A clear-eyed view](https://newsletter.getdx.com/p/developer-productivity-metrics-the) — newsletter de DX, 2025-02-05. Republicación de la misma conversación del lado del sponsor; útil para mostrar los dos encuadres del mismo material. *(frágil)*
- DX Inc., [DX Core 4 engineering metrics](https://getdx.com/dx-core-4/) + [Measuring developer productivity with the DX Core 4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/) — Speed / Effectiveness / Quality / Business Impact. *(frágil, sitio comercial)*
- DX Inc., [Developer Experience Index (DXI)](https://getdx.com/developer-experience-index/) — 14 drivers, score propietario. **Éste, y no Core 4, es el producto que Noda encuadra como anti-productividad.** *(frágil, sitio comercial)*
- Sergio De Simone, [DX Unveils New Framework for Measuring Developer Productivity](https://www.infoq.com/news/2025/01/dx-core-4-framework/) — InfoQ, 2025-01. Cobertura independiente; documenta *diffs per engineer* como instrumento de Speed. *(frágil)*
- [DORA's software delivery performance metrics](https://dora.dev/guides/dora-metrics/) — sitio oficial. **Hoy son cinco métricas, no cuatro.** *(estable)*
- Nicole Forsgren, Jez Humble y Gene Kim, *Accelerate: The Science of Lean Software and DevOps* — [IT Revolution](https://itrevolution.com/product/accelerate/), 2018-03-27, ISBN-13 9781942788331. Ficha en [Open Library](https://openlibrary.org/books/OL26833682M/Accelerate_The_Science_of_Lean_Software_and_DevOps). Sin copia en archive.org (búsqueda avanzada título+autor: 0 resultados). *(estable)*

_Descartadas:_ `medium.com/@johnpcutler/anti-productivity-…` (404 — no existe tal artículo en Medium); Paul Ingles, *Not Very Productive* (Medium, 2020-09-14) — cita a Cutler pero **no** al artículo de contra-productividad, sólo a un diagrama suyo en Twitter; no aporta.

**Imágenes:** _a definir_

**Tags propuestos:** `['John Cutler','productividad','metricas','DX','Beck','critica']`

**Estado actual:**

> ⚠️ **PREMISA EN DUDA (parcial) — 2026-07-15, pasada de fuentes.** El núcleo del Concepto **se sostiene**, pero un dato de su primera línea es falso y hay que corregirlo antes de escribir.
>
> **Lo que se cae:** el Concepto dice que «John Cutler escribió un artículo titulado *Anti-productivity*». **No existe tal artículo.** El artículo real es «TBM 240: The Ultimate Guide to Developer Counter-Productivity» (*The Beautiful Mess*, 2023-09-02), se llama **Counter**-Productivity, y **no usa la palabra «anti-productivity» ni una sola vez**. Verificado: búsqueda en el archivo de su Substack por «productivity» (sólo TBM 240, TBM 231 y TBM 243) y 404 en el Medium correspondiente. Quien lo rebautiza «Anti-productivity» es **Abi Noda al citarlo**. El término que da título a este post es, entonces, del vendedor, no del autor — lo cual, lejos de arruinar el post, le da un tema mejor (§5 y el nuevo párrafo de §3 ya lo aprovechan).
>
> **Lo que se sostiene, y mejor de lo esperado:**
> - «Beck endorsa con reservas» → **confirmado y con citas textuales**: Goodhart de entrada, «I am afraid of the misuse of this kind of information», «if you just sell the dashboard, that's malpractice», y la concesión tibia «I'm glad you're doing what you're doing».
> - «la filosofía detrás del DX score» → **confirmado en boca de Noda**, pero referido al **DXI**, no al Core 4: «that's the spirit of what we're trying to do with the developer experience index».
>
> **Lo que apareció y no estaba en el plan (y es lo mejor del hallazgo):** la conversación Beck × Noda es **publicidad paga** — «Thank you to DX for sponsoring this conversation. They paid me for my time & this space», declarado por Beck en el propio post. Y el Core 4 mide Speed con ***diffs per engineer***: la misma empresa que argumenta que no se puede medir productividad vende un tablero que cuenta commits por cabeza. Las dos cosas están incorporadas al borrador.
>
> **Correcciones de dato aplicadas a la prosa:** la entrevista es del **29 de enero de 2025**, no de enero de 2026; está en el newsletter de Kent Beck (`newsletter.kentbeck.com`, con `tidyfirst.substack.com` redirigiendo 301), no en «el newsletter de *Tidy First*» como cosa separada. La metáfora del río y el barro **no es de Cutler**: es glosa de César, y la prosa ahora lo dice explícitamente en vez de atribuirla. El Hook y el Concepto **no se tocaron** (son de César), pero ambos necesitan una pasada suya a la luz de esto: el Hook puede quedar tal cual si se presenta como metáfora propia, y el Concepto necesita cambiar «un artículo titulado *Anti-productivity*» por el título real.

_Historial:_ seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (9 secciones), se fijó `Length target: medium` y se escribió un borrador de prosa completo (~1500 palabras de prosa efectiva, sin contar marcas de verificación ni huecos) en la sección «Borrador de prosa» al pie. Queda en el piso del `Length target`: al cerrar los huecos con material de César, entra cómodo en el rango 1500-2200.

Lo que quedó **escrito**: el armazón argumental entero — el numerador vacío, la inversión de Cutler, el catálogo de fricciones, el encuadre comercial de DX Inc., la lectura de Beck endorsando con reservas, el paralelo con *Accelerate*, la objeción de Goodhart aplicada a la propia anti-productividad, y el cierre sin dashboard. Se sostiene solo como ensayo.

Lo que quedó como **hueco**:

- 7 huecos `🕳️` pidiendo a César lo que el post no puede inventar: si vivió el problema del numerador vacío en la STG o en el Ministerio de Cultura de Santa Fe (y con qué métrica lo midieron a él), la fricción más cara que recuerde de esos años, si alguna vez vio una métrica maquillada, qué le pasó al leer a Cutler, y el veredicto personal del cierre. Sin esos, es un ensayo correcto pero impersonal — todavía no es un post de katra.
- **Marcas de verificación pendientes: 11 → 1.** La pasada de fuentes del 2026-07-15 cerró diez con fuentes fetcheadas y verificadas (ver `**Bibliografía:**`, ahora con 9 entradas + descartes). El **riesgo de encuadre está resuelto**: la entrevista se leyó completa, Beck sí endorsa con reservas y sí hay vínculo comercial (es un post auspiciado), así que la §6 no se cae — al contrario, se fortalece.
- **La única marca que queda** es sobre *Accelerate*: no pude confirmar contra el texto del libro que encuadre explícitamente las métricas como propiedades del sistema y no del individuo. La ficha bibliográfica sí está verificada, y la página del editor habla de medir «the performance of their teams», pero eso es marketing del editor, no el libro. No hay copia en archive.org (0 resultados) para chequearlo online. **Necesita el libro en mano — cap. 2, «Measuring Performance».** Si César no lo tiene, la salida barata es bajar la afirmación a lo que sí está probado (DORA mide entrega, no personas, según `dora.dev`) y no ponerle al libro una tesis que no leímos.
- **Cross-link ganado:** la conversación Beck × Noda **arranca con la Ley de Goodhart**, traída por Beck. Eso conecta [[C-11]] con este post por la fuente misma, no por asociación nuestra — vale explotarlo en la §8.
- `**Imágenes:**` sigue en `_a definir_` — el candidato natural es un río con sedimento o un cauce obstruido (Wikimedia Commons, licencia clara, recorte 2.5:1).

---

## Borrador de prosa

Hace años que la industria del software intenta medir cuánto produce un programador, y hace años que fracasa. No fracasa por falta de ganas ni por falta de herramientas: fracasa porque el numerador de esa fracción no existe.

John Cutler dio vuelta el problema con un movimiento que a mí me pareció, la primera vez que lo leí, casi un truco de magia — de esos que una vez que te los explican son obvios y ya no podés dejar de verlos. Si no podés medir cuánta agua pasa por el río, medí cuánto barro hay obstruyéndolo. La metáfora es mía, no de él: Cutler no habla de ríos.[^cutler] Lo que dice, con menos poesía y más precisión, es que hay que dejar de medir productividad y empezar a mirar la **contra-productividad** — las actividades de apalancamiento nulo o negativo en las que se le va el día al que programa.

### El numerador que no existe

Pensá un segundo en qué significaría, en serio, medir la productividad de alguien que escribe software.

En una fábrica de tornillos es trivial: tornillos por hora. El numerador está ahí, es físico, lo contás. En software, ¿qué contás? ¿Líneas de código? Ya sabemos cómo termina eso: el que escribe mil líneas de basura le gana al que borra doscientas y deja el sistema mejor. ¿Commits? Contás la costumbre de apretar un botón, no el trabajo. ¿Story points? Son una estimación de esfuerzo que nosotros mismos inventamos, así que medir productividad en story points es medirte con la regla que vos dibujaste. ¿Features entregadas? Ahí ya estás midiendo el tamaño arbitrario con el que alguien cortó las tarjetas.

Todos esos números tienen el mismo defecto, y es un defecto de fondo, no de calibración: **son proxies del esfuerzo, no del valor**. Y el valor de un cambio de software no se conoce en el momento de escribirlo. A veces no se conoce nunca.

Así que la fracción está rota desde el vamos. No hay numerador. Y toda la industria de las métricas de productividad consiste, básicamente, en agarrar cualquier cosa que sí se pueda contar y hacer de cuenta que era eso.

> 🕳️ **HUECO — necesita a César:** ¿alguna vez te midieron a vos con una métrica de estas en el sector público (STG o Ministerio de Cultura de Santa Fe)? ¿Cuál era la métrica, quién la miraba, y qué terminó pasando con ella? Una o dos frases alcanzan.

### La inversión

Acá está el movimiento de Cutler, y es puramente lógico.

El valor producido es invisible, discutible y diferido. Pero el tiempo **perdido** no. El tiempo que esperaste a que terminara el pipeline de CI es un número. Los tres días que tu pull request estuvo esperando a que alguien lo mirara son un número. La semana que construiste la pantalla equivocada porque el requerimiento decía una cosa y el que lo pidió quería otra es un número. Los cuarenta minutos que tarda en levantar el entorno local cada mañana son un número.

Nada de eso es productividad. Todo eso es **lo contrario**: es el barro. Y el barro sí se deja contar.[^cutler]

Y Cutler lo cuenta en serio: su artículo es, literalmente, un catálogo de veintiséis familias de trabajo de apalancamiento negativo — trabajo reactivo no planificado, costos de arranque y cambio de contexto, trabajo administrativo que no agrega valor, sobrecarga de dependencias, reuniones inefectivas, búsqueda de consenso, workarounds, onboarding ineficiente, esperas, retrabajo, código sin liberar, deadlines artificiales, pérdida de conocimiento. Su tesis es explícita y va contra la medición individual: los factores personales «palidecen frente a los desafíos diarios y el entorno de los desarrolladores».[^cutler]

Lo que me convence de esta inversión no es que sea más fácil de medir. Es que es más **honesta**. Cuando la organización te pide que reportes tu productividad, te está pidiendo que te evalúes; nadie reporta bien ahí, porque reportar mal tiene consecuencias sobre tu sueldo. Cuando te pregunta cuánto tiempo perdiste esperando el CI, te está pidiendo que denuncies al sistema, no a vos. La respuesta sincera no te deja mal parado. Ese cambio de incentivo, para mí, es la mitad del valor de toda la idea.

Conviene aclarar una cosa de entrada, porque el post se apoya en ella. El artículo de Cutler no se llama *Anti-productivity*. Se llama **«TBM 240: The Ultimate Guide to Developer Counter-Productivity»**, salió el 2 de septiembre de 2023 en su newsletter *The Beautiful Mess*, y en ningún momento usa la palabra «anti-productividad».[^cutler] El que la usa —y el que le cambia el título al citarlo— es Abi Noda, CEO de DX, en la conversación con Beck que discutimos más abajo.[^beck_noda] O sea: «anti-productividad» no es la marca que Cutler le puso a su idea, es la que le puso el que la vende. No es un detalle menor para un post que trata justamente sobre quién nombra las cosas.

Cutler, para ubicarlo: escribe sobre desarrollo de producto desde 2015 —primero en Medium, desde 2020 en Substack— y pasó cuatro años en Amplitude, la empresa de analytics. No es académico ni vende una herramienta de medición: es un ensayista de la industria con público propio.[^cutler_about]

### El catálogo del barro

Cuando uno se sienta a hacer la lista, las fricciones caen en unas pocas familias, y todas son reconocibles a simple vista:

- **Esperas.** CI lento, code review parado, aprobaciones que dependen de una persona que está de vacaciones, ambientes de staging con cola.
- **Ambigüedad.** No sé qué hay que construir. No sé quién decide. Pregunté y no me contestaron.
- **Retrabajo.** Lo construí, estaba mal, lo hago de nuevo. La peor de todas, porque durante la primera vuelta tus métricas de output se veían **excelentes**.
- **Entorno.** El build local, las dependencias rotas, la máquina, el VPN, la burocracia de acceso.

Fijate una cosa: ninguna de estas cuatro es culpa del que las sufre. Todas son propiedades del sistema en el que trabaja. Por eso se pueden preguntar en voz alta sin que nadie se ponga a la defensiva — y por eso, si querés saber qué anda mal en un equipo, la pregunta «¿qué te frenó esta semana?» rinde diez veces más que cualquier dashboard.

> 🕳️ **HUECO — necesita a César:** de tus años en el sector público, ¿cuál fue la fricción más cara que recordás? ¿Era espera, ambigüedad, retrabajo o entorno? Contala en dos o tres frases, con el detalle concreto (qué había que esperar, cuánto tardaba).

> 🕳️ **HUECO — necesita a César:** ¿la fricción dominante en el Estado era técnica (CI, entornos, herramientas) o administrativa (aprobaciones, expedientes, firmas)? Esto importa para el post: si era administrativa, la idea de Cutler necesita una traducción y vale la pena decirlo.

### La idea tiene dueño y tiene precio

Ahora, la parte que hay que decir en voz alta antes de seguir entusiasmándose.

Esta idea no vive únicamente en un artículo de blog. La adoptó DX Inc., que vende medición de developer experience a empresas. Pero acá hay que hilar fino, porque DX vende **dos cosas distintas** y sólo una de ellas es anti-productividad.

Lo que sí es anti-productividad es el **DX Index (DXI)**: un score propietario compuesto por 14 «drivers» de eficiencia —velocidad de iteración local, deep work, proceso de release, confianza para hacer cambios— que la empresa correlaciona con tiempo ahorrado.[^dxi] Es el propio Noda quien lo dice, y lo dice citando a Cutler: «es el espíritu de lo que estamos tratando de hacer con el developer experience index. Estamos tratando de medir el desperdicio, porque si nos deshacemos de eso podemos ir más rápido — en vez de decirle a la gente que vaya más rápido».[^beck_noda] Ahí el Concepto de este post se sostiene: la anti-productividad **es** la filosofía declarada detrás del DX score.

Lo que **no** es anti-productividad es el otro producto de DX, el framework **Core 4**, anunciado en enero de 2025.[^dx] Sus cuatro dimensiones son Speed, Effectiveness, Quality e Impact — y Speed se mide con *diffs per engineer*, o sea commits por persona con otro nombre.[^dx_core4_infoq] Es exactamente el numerador vacío del principio de este post, servido de nuevo. La empresa que te explica que no se puede medir productividad te vende, en el mismo catálogo, un tablero que cuenta diffs por cabeza.

Eso no hace que la idea de Cutler sea falsa —las ideas buenas también se venden, y una idea no se vuelve mentira porque alguien le ponga precio—, pero sí obliga a leerla con la mano en el bolsillo. Y obliga a no confundir los dos productos, cosa que la prensa del sector confunde todo el tiempo.

Lo que a mí me interesa rescatar es la idea suelta, no el producto. La pregunta «¿qué te frenó esta semana?» no necesita licencia.

### Beck, que desconfía de todo, acepta esto

El dato que le da peso a la cosa es quién la avala. Kent Beck —históricamente escéptico de que a los programadores se los pueda medir— conversó con Abi Noda, CEO y cofundador de DX, en «Developer Productivity Metrics: Education Necessary», publicado en su newsletter el 29 de enero de 2025.[^beck_noda] Y sí: termina aceptando el enfoque **con reservas**. Las reservas son literales y son filosas.

Beck abre pidiendo lo que a esta altura debería ser ley: «Me gustaría adoptar una nueva resolución: que toda conversación sobre métricas tenga que empezar por la Ley de Goodhart» [[C-11]]. Después dice que le tiene miedo al mal uso: «Le tengo miedo al mal uso de este tipo de información». Y remata con la frase que debería ir en la portada de cualquier producto de estos: **«si te limitás a vender el dashboard, eso es mala praxis»**. Lo que concede es más tibio de lo que el marketing sugiere: «Me alegra que estés haciendo lo que estás haciendo. Creo que la autoconciencia es muy valiosa».[^beck_noda]

Esa última parte es la que importa, y es la que suele desaparecer cuando alguien cita esto en LinkedIn. No es un endorsement. Es un «sí, pero».

Y hay un dato más que no se puede omitir sin ser deshonesto, porque cambia cómo se lee todo lo anterior: **la conversación es publicidad paga**. El propio Beck lo declara arriba de todo, con todas las letras: «Gracias a DX por auspiciar esta conversación. Me pagaron por mi tiempo y por este espacio».[^beck_noda] Hay que decirlo en los dos sentidos, porque corta para los dos lados. Por un lado, un aval comprado vale menos que uno espontáneo, y quien cite a Beck avalando el DX score sin mencionar que DX le pagó está citando mal. Por el otro —y esto me parece lo más interesante— Beck usó el espacio que le pagaron para decirle al que le pagó que vender el dashboard es mala praxis. Es un aviso publicitario en el que el famoso contratado le advierte al sponsor. Eso habla bien de Beck y, curiosamente, también habla bien de DX por publicarlo.

### *Accelerate* ya había hecho este viaje

Nada de esto es completamente nuevo, y conviene reconocerlo. *Accelerate*, de Forsgren, Humble y Kim (IT Revolution, 2018), hizo el mismo movimiento hace años con las métricas de DORA.[^accelerate] Su hallazgo estructural no fue una métrica en particular sino **la unidad de medida**: no midieron personas, midieron el sistema de entrega. Las cuatro clásicas, con sus nombres canónicos: frecuencia de deploy, *change lead time* (tiempo desde el commit hasta producción), *change fail rate* y tiempo de recuperación ante un deploy fallido.[^dora] Ninguna de las cuatro tiene un nombre y apellido adentro.

Un detalle que conviene actualizar, porque el post lo va a leer alguien que fue a mirar: **hoy DORA ya no publica cuatro métricas, publica cinco**. Al catálogo se le sumó el *deployment rework rate* —la proporción de deploys no planificados que salen a raíz de un incidente en producción—, y las cinco están agrupadas en dos familias: throughput e inestabilidad.[^dora] «Las cuatro métricas de DORA» es, a esta altura, una expresión histórica.

Cutler, leído así, es *Accelerate* llevado un paso más adentro: DORA mide el sistema desde afuera, por sus salidas; la anti-productividad lo mide desde adentro, por dónde se traba.

[VERIFICAR: que *Accelerate* **en su propio texto** encuadre explícitamente las métricas como propiedades del sistema y no del individuo — es una afirmación central de este párrafo y no la pude verificar contra el libro. Lo que sí está verificado es la ficha (IT Revolution, 27-03-2018, ISBN 9781942788331) y que la página del editor describe el libro como medición de «the performance of their teams», en clave de equipo/organización. No hay copia en archive.org: la búsqueda avanzada por título+autor devuelve 0 resultados, así que no hay préstamo controlado al cual mandar al lector. Para cerrar esto hace falta el libro en mano — el capítulo 2 («Measuring Performance») es el lugar donde debería estar.]

### La trampa: el barro también se maquilla

Y acá viene la objeción que le pondría yo, y que el post tiene que hacerse a sí mismo si quiere ser honesto: la anti-productividad **también** es una métrica, y por lo tanto también obedece a Goodhart [[C-11]].

Si el tablero mide tiempo de CI, alguien va a borrar tests para que el pipeline corra más rápido. Si mide tiempo de espera en code review, alguien va a aprobar sin leer. Si mide retrabajo, va a bajar mágicamente la cantidad de cosas que se declaran retrabajo — se van a llamar «mejoras». En el momento en que la fricción reportada pasa a ser el objetivo, la fricción reportada deja de decir la verdad sobre la fricción real.

La única defensa que le veo es la misma de siempre, y es aburrida: estas mediciones sirven mientras sean **instrumentos de diagnóstico y no de evaluación**. En el segundo en que el número de fricción de tu equipo aparece en la revisión de desempeño de alguien, ese número murió y no te avisó.

> 🕳️ **HUECO — necesita a César:** ¿viste alguna vez, con tus ojos, una métrica maquillada por el equipo o por la jefatura? ¿Qué se medía y cómo la dieron vuelta? Sin nombres si hace falta, pero con el mecanismo concreto.

### Qué haría yo el lunes

La versión de esto que no necesita comprar nada cabe en tres pasos, y creo que es la única versión que sobrevive al contacto con un equipo real:

1. **Preguntar.** Una vez por semana, a cada uno: ¿qué te frenó? Sin formulario. Sin escala del uno al cinco.
2. **Anotar.** En un archivo de texto. Sin agregar, sin promediar, sin graficar. La anécdota cruda vale más que el promedio, porque el promedio te esconde justo el caso raro que te está comiendo el mes.
3. **Arreglar una.** Una sola, la que más se repite. Y volver a preguntar la semana que viene.

Eso no es un framework. Es prestar atención, con método. Y tiene una propiedad que ningún dashboard tiene: si la respuesta que te dan es «nada, todo bien», y sabés que es mentira, el problema que descubriste no era el CI. Era la confianza. Ninguna herramienta te iba a decir eso.

Un último recaudo, del lado de [[C-12]]: la fricción que medís es la fricción del bosque en el que estás parado. Un equipo en modo desierto —construyendo algo nuevo, sin usuarios, sin deuda— tiene fricciones que no se parecen en nada a las de un equipo en modo bosque, cuidando un sistema vivo con veinte años encima. Medir el barro está bien. Suponer que el barro de todos los ríos es el mismo, no.

> 🕳️ **HUECO — necesita a César:** ¿aplicaste alguna vez algo parecido a estos tres pasos, aunque no lo llamaras así? Y si no, ¿te parece que hubiera funcionado en los equipos que te tocaron, o el contexto lo hacía imposible?

> 🕳️ **HUECO — necesita a César:** el veredicto del cierre. ¿Comprás la idea de Cutler, la comprás con reservas como Beck, o te parece que es la misma trampa de siempre con mejor marketing? Una o dos frases con tu posición real.

> 🕳️ **HUECO — necesita a César:** ¿cómo llegaste a este artículo de Cutler y qué te hizo pararte a pensar? Sirve como apertura alternativa si el arranque del río queda demasiado abstracto.

[^cutler]: John Cutler, [TBM 240: The Ultimate Guide to Developer Counter-Productivity](https://cutlefish.substack.com/p/tbm-240-the-ultimate-guide-to-developer) — *The Beautiful Mess*, 2 de septiembre de 2023. El artículo enumera 26 familias de trabajo de apalancamiento nulo o negativo. No usa la expresión «anti-productivity» ni ninguna metáfora de río o barro. Copia de respaldo: [Wayback Machine, 28-03-2026](http://web.archive.org/web/20260328152625/https://cutlefish.substack.com/p/tbm-240-the-ultimate-guide-to-developer). *(frágil — Substack; backup verificado)*

[^cutler_about]: [About — The Beautiful Mess](https://cutlefish.substack.com/about) — bio propia de John Cutler: escribe sobre desarrollo de producto desde 2015, en Substack desde 2020, cuatro años en Amplitude. *(frágil — Substack)*

[^beck_noda]: Kent Beck y Abi Noda, [Developer Productivity Metrics: Education Necessary](https://newsletter.kentbeck.com/p/developer-productivity-metrics-education) — newsletter de Kent Beck, 29 de enero de 2025. **Conversación auspiciada**: el post declara «Thank you to DX for sponsoring this conversation. They paid me for my time & this space». El dominio `tidyfirst.substack.com` redirige (301) a `newsletter.kentbeck.com`. Copia de respaldo bajo el dominio viejo: [Wayback Machine, 12-04-2026](http://web.archive.org/web/20260412123620/https://tidyfirst.substack.com/p/developer-productivity-metrics-education). *(frágil — Substack; backup verificado)*

[^dx]: DX Inc., [DX Core 4 engineering metrics](https://getdx.com/dx-core-4/) y [Measuring developer productivity with the DX Core 4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/) — dimensiones Speed, Effectiveness, Quality y Business Impact; autores Abi Noda, Laura Tacho, Margaret-Anne Storey y Michaela Greiler. *(frágil — sitio comercial)*

[^dx_core4_infoq]: Sergio De Simone, [DX Unveils New Framework for Measuring Developer Productivity](https://www.infoq.com/news/2025/01/dx-core-4-framework/) — InfoQ, enero de 2025. Cobertura independiente del anuncio (6 de enero de 2025); es la fuente que documenta que Speed se instrumenta con *diffs per engineer* y que las dimensiones se diseñaron como «oppositional metrics». *(frágil — InfoQ)*

[^dxi]: DX Inc., [Developer Experience Index (DXI)](https://getdx.com/developer-experience-index/) — score propietario (™) compuesto por 14 drivers de eficiencia; la empresa lo comercializa correlacionando «developer friction against time savings». *(frágil — sitio comercial)*

[^dora]: [DORA's software delivery performance metrics](https://dora.dev/guides/dora-metrics/) — sitio oficial de DORA. Hoy documenta **cinco** métricas agrupadas en throughput (change lead time, deployment frequency, failed deployment recovery time) e inestabilidad (change fail rate, deployment rework rate). *(estable — dominio institucional del programa DORA)*

[^accelerate]: Nicole Forsgren, Jez Humble y Gene Kim, *Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations* — [IT Revolution](https://itrevolution.com/product/accelerate/), 27 de marzo de 2018. ISBN-13 9781942788331 (ISBN-10 1942788339); ficha corroborada en [Open Library](https://openlibrary.org/books/OL26833682M/Accelerate_The_Science_of_Lean_Software_and_DevOps). No existe copia en archive.org, ni siquiera en préstamo controlado. *(estable — Open Library / editorial)*
