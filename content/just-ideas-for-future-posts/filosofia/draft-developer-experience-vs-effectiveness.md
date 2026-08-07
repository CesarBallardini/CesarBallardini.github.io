### C-16 — Developer Experience vs Effectiveness: por qué Beck rechaza la palabra "experiencia"

- **Archivo seed:** _draft-rest.md bucket 6 (cosechado 2026-04-09)_
- **Slug propuesto:** `developer-experience-vs-effectiveness`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-developer-experience-vs-effectiveness/index.md`
- **Serie:** filosofia
- **Cross-links:** [[C-03]] (Tidy First), [[C-13]] (anti-productivity), [[C-14]] (XP)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1600–2000 palabras (ensayo corto de opinión, una sola tesis)

**Concepto:** En la conversación con Abi Noda, Kent Beck "flinches" cuando aparece la frase "developer experience" — no porque esté mal medir la experiencia, sino porque la palabra invita al malentendido de que el objetivo es "hacer felices" a los desarrolladores. Beck cuenta una anécdota del entrenador de fútbol de su hijo: "estamos acá para divertirnos. ¿Sabés qué es divertido? Ganar. Si para ganar tenés que practicar más, eso ya no es 'happy-clappy fun', es algo mejor". Por eso DX llama a su métrica "effectiveness", no "developer happiness". El post discute la distinción y por qué importa.

**Hook:** "no me hagas feliz". Lo dijo Kent Beck cuando le hablaron de developer experience. La meta no es la felicidad del programador — es la efectividad. Y eso es muy distinto. Acá lo desarrolla.

**Outline:**
1. La escena: aparece «developer experience» en la conversación y Beck se retrae. El hook — la objeción es a la palabra, no a la medición.
2. Por qué la palabra importa: «experiencia» es un sustantivo de estado interno, y lo que se mide de un estado interno tiende a ser el reporte del estado (satisfacción, felicidad), no la causa.
3. La anécdota del entrenador de fútbol del hijo de Beck: «estamos acá para divertirnos; ¿sabés qué es divertido? Ganar». La diversión como consecuencia, no como objetivo.
4. La distinción operativa: *happiness* como métrica terminal vs *effectiveness* como métrica instrumental. Por qué DX eligió la segunda palabra.
5. El argumento fuerte a favor de Beck: si el objetivo declarado es la felicidad, Goodhart te come — se optimiza el reporte, no el trabajo ([[C-11]]). Y la felicidad es más barata de comprar que la efectividad (perks vs arreglar el CI).
6. El contraargumento honesto: la investigación de satisfacción del desarrollador existe y no es humo; el comentario de Peggy Story en el hilo. La satisfacción como *señal* diagnóstica sin ser *objetivo*.
7. Qué cambia en la práctica cuando pedís efectividad en vez de felicidad: qué preguntás en la encuesta, qué arreglás primero, qué no comprás.
8. Cierre: la efectividad como forma adulta del cuidado. Enlace a [[C-13]] (medir lo que frena) y [[C-14]] (XP: las prácticas eran para poder trabajar, no para pasarla bien).

**Bibliografía:** _(pasada de fuentes 2026-07-15 — todas las URLs de abajo fueron fetcheadas y verificadas)_

**Fuente primaria — la conversación**
- Kent Beck y Abi Noda, [«Developer Productivity Metrics: Education Necessary»](https://newsletter.kentbeck.com/p/developer-productivity-metrics-education), newsletter *Tidy First*, **29 de enero de 2025** — `frágil` (Substack). Backup: [Wayback 2026-04-12](http://web.archive.org/web/20260412123620/https://tidyfirst.substack.com/p/developer-productivity-metrics-education). **Ojo: `tidyfirst.substack.com` redirige 301 a `newsletter.kentbeck.com`.** Contiene las tres citas load-bearing del post: el «flinch», la anécdota del entrenador y el pasaje de «effectiveness».
- Abi Noda, [«Measuring developer productivity: A clear-eyed view»](https://newsletter.getdx.com/p/developer-productivity-metrics-the), newsletter *Engineering Enablement* (DX), **5 de febrero de 2025** — `frágil`. Backup: [Wayback 2026-04-19](http://web.archive.org/web/20260419074227/https://newsletter.getdx.com/p/developer-productivity-metrics-the). Es la misma conversación republicada con otro título; sirve de segunda copia.
- **Corrección de fecha:** la bibliografía original decía «Jan 2026». Es **enero de 2025**. Un año de diferencia.

**El encuadre «effectiveness» (reemplaza a la entrada fantasma «GitHub developer happiness vs DX effectiveness framing»)**
- Abi Noda, [«Introducing the DX Core 4»](https://newsletter.getdx.com/p/introducing-the-dx-core-4), 10 de diciembre de 2024 — `frágil`. Las cuatro dimensiones y la definición del DXI.
- DX, [«Guide to the DX Core 4»](https://docs.getdx.com/dx-core-4/) — `frágil` (doc de producto, cambia sin aviso). *Effectiveness* = «Developer experience & friction», medida con DXI.
- **No existe un documento de GitHub.** Lo de «GitHub says it should be called developer happiness» es una frase de Noda *dentro de la misma conversación*, reportando de segunda mano una opinión de GitHub. No hay paper ni post de GitHub que buscar: la entrada bibliográfica original apuntaba a algo que nunca existió como documento.

**Margaret-Anne «Peggy» Storey (el nombre correcto de «Peggy Story»)**
- [Sitio personal de Margaret-Anne Storey](https://www.margaretstorey.com/) — `frágil` (dominio personal). Fuente preferida sobre Wikipedia, per convenciones de la casa.
- DX, [«An inside look at SPACE with Dr. Margaret-Anne Storey»](https://getdx.com/podcast/space-framework/) — `frágil`. Confirma el apodo «Peggy» y su rol de Chief Scientist en DX.
- M.-A. Storey et al., «Towards a Theory of Software Developer Job Satisfaction and Perceived Productivity», *IEEE Transactions on Software Engineering*, vol. 47, n.º 10, pp. 2125–2142, 2021. DOI [10.1109/TSE.2019.2944354](https://doi.org/10.1109/TSE.2019.2944354) — `estable` (DOI verificado vía Crossref; IEEE Xplore no se deja fetchear). Mirror libre: [preprint en Microsoft Research](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/12/storey-tse-2019.pdf) — `estable`. Glosa de la autora: [su blog, 2020-06-01](https://www.margaretstorey.com/blog/2020/06/01/developer-productivity-satisfaction-theory/) — `frágil`.
- N. Forsgren, M.-A. Storey, C. Maddila, T. Zimmermann, B. Houck y J. Butler, «The SPACE of Developer Productivity», *ACM Queue*, vol. 19, n.º 1, pp. 20–48, 2021. DOI [10.1145/3454122.3454124](https://doi.org/10.1145/3454122.3454124) — `estable` (DOI verificado vía Crossref; `queue.acm.org` devuelve **HTTP 403** al fetch automatizado, y la página de Microsoft Research **no** ofrece PDF libre — sólo BibTeX. No encontré mirror de texto libre legítimo).

**Contexto XP**
- Kent Beck, *Extreme Programming Explained: Embrace Change*, 1.ª ed., Addison-Wesley, 1999, ISBN 0201616416 — [Internet Archive, préstamo digital controlado](https://archive.org/details/extremeprogrammi00beck) — `estable`. El ejemplar de archive.org es la **7.ª impresión, fechada 2000**; el copyright de la 1.ª ed. es 1999.

**Imágenes:** _a definir_

**Tags propuestos:** `['Kent Beck','developer experience','effectiveness','DX','cultura']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09; expandido a prosa el 2026-07-15 (generado por Claude, sin revisar por César). **Pasada de fuentes 2026-07-15: la fuente primaria apareció completa.** El seed borrado ya no hace falta — la conversación Beck × Noda está publicada y fetcheada, y las tres citas load-bearing (el «flinch», el entrenador, el pasaje de «effectiveness») quedaron verificadas al pie de la letra. Los 8 `[VERIFICAR:]` están resueltos.

⚠️ **PREMISA EN DUDA (parcial):** el Concepto dice que Beck se retrae «no porque esté mal medir la experiencia, sino porque la palabra invita al malentendido de que el objetivo es hacer felices a los desarrolladores». La fuente sostiene esa mitad, pero **antepone otra razón que el draft ignora**: «I kind of flinch at "developer experience" **because it isn't just about the developer**». El reclamo principal de Beck es que la palabra recorta el foco al desarrollador y deja afuera el producto y el negocio — lo de las reuniones de «hagamos felices a los devs» viene *después*, como ilustración. El Hook («no me hagas feliz») sigue funcionando y la tesis del post se sostiene, pero tal como está el Concepto le atribuye a Beck un argumento más angosto que el que hizo. **Decisión de César**: o se ensancha el Concepto para incluir «no es sólo sobre el desarrollador», o se aclara en el post que se está tomando deliberadamente sólo una de las dos objeciones.

⚠️ **La sección 6 decía lo contrario de lo que dice la fuente.** «Peggy Story» es **Margaret-Anne «Peggy» Storey** (UVic + Chief Scientist de DX, coautora de SPACE). Su comentario **no** era una defensa de la satisfacción como señal diagnóstica, como suponía el borrador: era una objeción de *naming* —que el índice debía llamarse «developer experience» y no ir bajo «effectiveness»—, reportada de segunda mano por Noda. La sección quedó reescrita sobre lo que la fuente sí sostiene, y encima mejoró: la ironía de que la científica jefe de DX le discutiera el nombre a su propio CEO es mejor material que el que había. La sección 6 **no** hay que cortarla.

Qué quedó escrito: el outline completo (8 puntos) y un borrador de ~1.750 palabras que sostiene la tesis de punta a punta — la objeción de Beck a la palabra «experiencia», la anécdota del entrenador, la distinción happiness/effectiveness, el argumento Goodhart y el contraargumento de la investigación de satisfacción.

Qué se resolvió en la pasada de fuentes (2026-07-15):
- ~~El seed original ya no está~~ → **no importa**: la conversación está publicada en dos lados (Tidy First y Engineering Enablement), fetcheada y con backup de Wayback. Todas las comillas de Beck ahora salen de la fuente, no del campo Concepto.
- ~~«Peggy Story»~~ → **Margaret-Anne «Peggy» Storey**, identificada y sourceada (sitio propio, rol en DX, paper de TSE, SPACE). Ver la advertencia de arriba: lo que dijo no es lo que el borrador creía.
- ~~«GitHub developer happiness vs DX effectiveness framing»~~ → **no existe tal documento**. Es una frase de Noda dentro de la misma entrevista. La entrada bibliográfica original apuntaba al vacío.
- Fecha de la entrevista: era **enero de 2025**, no enero de 2026.
- Anécdota del entrenador: **no es fútbol y no es «su hijo»** — Beck dice «one of my kids' sports teams», sin deporte ni cuál de sus hijos.
- 1.ª ed. de *Extreme Programming Explained*: **1999** (el ejemplar de archive.org es 7.ª impresión, 2000). «Décadas» era correcto; ahora dice «un cuarto de siglo».

Qué quedó como hueco:
- **Ningún `[VERIFICAR:]` pendiente.** Lo único que no se pudo conseguir es un mirror de texto libre de SPACE (ACM Queue devuelve 403 y Microsoft Research sólo ofrece BibTeX); queda el DOI, verificado vía Crossref, que alcanza para citar.
- 6 huecos de experiencia vivida de César (todos del sector público santafesino: encuestas de clima, fricciones reales de su equipo, si alguna vez le compraron una perk en vez de arreglarle una herramienta). Sin esos, el post es un comentario de lectura y no un post de katra.

---

## Borrador de prosa

Hay un momento en la conversación entre Kent Beck y Abi Noda en el que Beck se incomoda. No con una idea: con una palabra. Aparece la frase «developer experience» y Beck se retrae. La frase textual es suya: «I kind of flinch at "developer experience" because it isn't just about the developer. I've been to meetings where it's like "Oh, the developers aren't happy, we want to make developers happy"»[^beck_noda]. Y la objeción no es la que uno esperaría.

> ⚠️ **Nota de sourcing (2026-07-15):** la cita se recuperó y el verbo «flinch» es correcto. Pero el motivo que Beck da *primero* no es el que sostiene el Concepto de este draft: dice que se retrae porque la cosa «isn't just about the developer» —es decir, porque el foco en el desarrollador deja afuera al producto y al negocio—, y *recién después* aparece la queja por las reuniones de «hagamos felices a los devs». Las dos razones están en el texto; el draft usa sólo la segunda. Al reescribir, incorporar la primera o el post le está poniendo a Beck un argumento más angosto que el que hizo. Beck no está diciendo que medir la experiencia de los programadores sea una pavada, ni que las encuestas internas sean humo. Está diciendo algo más fino y más molesto: que la palabra «experiencia» abre una puerta por la que se cuela un malentendido carísimo.

El malentendido es este: que el objetivo del asunto es hacer felices a los programadores. Beck lo rechaza sin diplomacia. No me hagas feliz —viene a decir—, hacéme efectivo. Y esas dos cosas, que en el folleto de cualquier plataforma interna parecen sinónimos, no lo son ni un poco.

### La palabra elegida

Empecemos por lo que a mí me parece el dato más elocuente, y es un dato de marketing, no de filosofía. La empresa de Abi Noda se llama DX —por *developer experience*, literalmente— y sin embargo a su métrica no la llamó *developer happiness*. La llamó **effectiveness**[^dx_core4]. Y no es una lectura mía: en la misma conversación Noda lo dice con todas las letras, y cuenta que se lo discutieron de los dos lados. «A lot of people ask why developer experience index is under effectiveness — even folks like Peggy Ann Story were like, "No that should be called developer experience." GitHub says it should be called developer happiness. But it needs to be called effectiveness because that's what we're actually measuring — not developer happiness but effectiveness»[^beck_noda]. Es decir: la gente que vive de vender medición de experiencia de desarrollador eligió deliberadamente no medir la felicidad del desarrollador.

> ⚠️ **Nota de sourcing (2026-07-15):** el encuadre se verificó, pero es más torcido —y más interesante— que lo que dice el borrador. En el framework DX Core 4, *effectiveness* es una de las cuatro dimensiones (speed, effectiveness, quality, impact) y se mide con el **DXI (Developer Experience Index)**, un índice de 14 ítems Likert; la documentación de DX define lo que effectiveness mide como «Developer experience & friction»[^dx_core4] [^dx_docs]. O sea: DX no borró la palabra «experiencia» — la dejó en el nombre del índice y le puso «effectiveness» al *nivel de arriba*. La tesis del post sigue en pie (eligieron no decir «happiness»), pero la frase «no la llamó developer happiness, la llamó effectiveness» necesita esta precisión: lo que renombraron fue la dimensión, no el índice. Y la objeción de Storey era exactamente contra ese renombre. Eso no es una casualidad de naming. Es una decisión defensiva, tomada por alguien que ya vio lo que pasa cuando el nombre de la métrica invita al comprador a entenderla mal.

Porque «experiencia» es un sustantivo de estado interno. Y con los estados internos pasa una cosa incómoda: lo único que podés medir de un estado interno es *el reporte del estado*. No la causa. Cuando ponés «experiencia» en el título del tablero, la pregunta que termina bajando al equipo es «¿cómo te sentís?», y la respuesta a esa pregunta se puede mejorar sin tocar una sola línea del problema que la produjo. La efectividad, en cambio, es un sustantivo de relación con el mundo: sos efectivo *respecto de algo*, y ese algo es externo a vos y por lo tanto discutible, verificable, mejorable.

### El entrenador

Beck ilustra la distinción con una anécdota doméstica, y me parece la mejor parte de toda la conversación. La cita textual es esta: «I remember one of my kids' sports teams, the coach said, "We're here to have fun. You know what's fun? Winning. If that means we have to practice extra hard or do more drills so you're more capable of winning, and you don't like doing more drills — well, we're aimed at a higher level of joy than whether you have happy-clappy fun today."»[^beck_noda]

La expresión que hay que conservar en la traducción es *happy-clappy fun* —diversión de aplaudir y sonreír—, y el remate: apuntamos a *un nivel más alto de alegría*, no a que hoy la pases bien.

> ⚠️ **Nota de sourcing (2026-07-15):** dos detalles del borrador estaban mal y quedaron corregidos arriba. (1) **No es fútbol**: Beck dice «one of my kids' sports teams», sin nombrar el deporte — el post no puede decir «fútbol». (2) **No es «su hijo»**: dice «my kids», sin especificar cuál ni el género. La formulación entrecomillada del borrador («y si para ganar hay que practicar más, entonces practicamos más») era una paráfrasis del campo Concepto, no la cita: el original agrega la cláusula clave «and you don't like doing more drills», que es justamente donde el argumento muerde.

Lo que hace el entrenador es un movimiento lógico que vale la pena mirar despacio, porque es exactamente el movimiento de Beck. No niega la diversión: la ratifica como propósito. Lo que hace es negarle el lugar de *objetivo operativo*. La diversión pasa a ser una consecuencia, y el objetivo operativo pasa a ser ganar. Y entonces —esto es lo lindo— aparece una consecuencia que ninguna cantidad de buena onda hubiera producido: entrenar más. Un objetivo de felicidad jamás te lleva a entrenar más. Un objetivo de victoria sí, y encima te devuelve la felicidad por el camino largo, que es el único por el que llega en serio.

Traducido a un equipo de software: si el objetivo declarado es que la pases bien, nadie va a proponer arreglar el build de veinte minutos, porque arreglar el build es aburrido, es una semana de trabajo sin gloria y no lo nota ningún usuario. Si el objetivo declarado es que el equipo sea efectivo, arreglar el build es lo primero de la lista. Y del otro lado de esa semana, casualmente, hay gente más contenta.

### Por qué la felicidad es la métrica peligrosa

Acá está, para mí, el núcleo del argumento, y conecta directo con la Ley de Goodhart [[C-11]]: en el momento en que la felicidad del programador se vuelve el objetivo declarado de la organización, deja de ser una buena medida de nada.

Pensá en el incentivo. La felicidad reportada es **barata de comprar**. Es muchísimo más barato poner una máquina de café buena, una tarde libre por mes, un Slack con emojis y una encuesta trimestral con carita sonriente, que rehacer el pipeline de CI, pagar la deuda técnica de un módulo que nadie quiere tocar, o —lo más caro de todo— cambiarle el proceso de aprobación a un área que no depende de vos. Las dos cosas suben el puntaje de una encuesta de experiencia. Una sola de las dos hace que el equipo entregue mejor software. Si la organización mide felicidad, el gerente racional compra la máquina de café. No porque sea cínico: porque le pediste eso.

La efectividad no se deja comprar así. Podés maquillarla —hay maneras, y [[C-13]] es justamente el post sobre eso— pero es sustancialmente más difícil de simular, porque apunta a fricciones concretas y nombrables: cuánto tardás en tener un entorno andando, cuánto tarda un PR en mergear, cuántas veces por semana te frena una espera que no depende de vos. Esas cosas o están o no están. No se arreglan con una pizza.

> 🕳️ **HUECO — necesita a César:** ¿Te tocó alguna vez el caso «máquina de café en vez de arreglar la herramienta» en el sector público santafesino? Si sí: ¿qué era la perk y qué era lo que realmente frenaba al equipo?

> 🕳️ **HUECO — necesita a César:** ¿En la STG o en Cultura hubo encuestas de clima laboral / satisfacción del personal? ¿Preguntaban por herramientas y fricciones, o sólo por «cómo te sentís en tu área»?

> 🕳️ **HUECO — necesita a César:** Nombrá una fricción concreta de tu trabajo en Cultura que, si te la hubieran arreglado, te habría cambiado la semana. Una sola, con nombre y apellido (una espera, una aprobación, una máquina, un trámite).

### El contraargumento honesto

Sería deshonesto de mi parte dejar el post acá, porque el argumento de Beck tiene un flanco. La investigación sobre satisfacción del desarrollador existe, es seria, y no dice que la satisfacción sea decorativa.

Y quien objetó el nombre «effectiveness» no era un rando de LinkedIn: era **Margaret-Anne Storey** —«Peggy»—, profesora de Ciencias de la Computación en la Universidad de Victoria, Canada Research Chair en aspectos humanos y sociales de la ingeniería de software, coautora del framework SPACE y, dato que le pone sabor al asunto, **Chief Scientist de la propia DX**[^storey_site] [^storey_dx]. Es decir: la científica jefe de la empresa le dijo a su CEO que a esa métrica había que llamarla «developer experience», y el CEO le dijo que no[^beck_noda].

Storey tiene con qué respaldar la objeción. Su paper con Zimmermann, Bird, Czerwonka, Murphy y Kalliamvakou en *IEEE Transactions on Software Engineering* encontró una relación **bidireccional** entre satisfacción laboral y productividad percibida del desarrollador: no es que la satisfacción sea un subproducto de trabajar bien, es que se alimentan mutuamente[^storey_tse]. Y en SPACE, la primera dimensión —la S— es literalmente *satisfaction and well-being*[^space]. La posición de Storey no es «hagamos felices a los devs»; es que la satisfacción es una variable con poder explicativo propio, no un termómetro decorativo.

> ⚠️ **Nota de sourcing (2026-07-15) — ACÁ EL BORRADOR DECÍA LO CONTRARIO:** el borrador afirmaba que «en el hilo de la conversación aparece un comentario de Peggy Story que va justamente por ese lado» (el de la satisfacción como señal diagnóstica). **Eso no es lo que dice la fuente.** El único comentario de Storey en la conversación es una objeción de *naming* —que el índice debería llamarse «developer experience» y no ir bajo «effectiveness»—, reportada de segunda mano por Noda, no una defensa de la satisfacción como diagnóstico. Además el nombre estaba mal transcripto en dos niveles: la fuente escribe «Peggy Ann Story» y la persona real es **Margaret-Anne Storey**. La sección quedó reescrita sobre lo que la fuente sí sostiene (la objeción de naming + la investigación propia de Storey, que sí existe y es seria). No hace falta cortar la sección 6 del outline: hay material verificado de sobra, pero el argumento ahora corre por otro carril que el que imaginaba el borrador.

Y creo que la síntesis está disponible sin traicionar a Beck. La distinción no es entre gente que se preocupa por los programadores y gente que no. Es entre tratar la satisfacción como **objetivo terminal** o como **señal diagnóstica**. Como señal, es utilísima y no la reemplaza nada: una encuesta bien hecha te dice dónde duele antes de que el dolor aparezca en las métricas de entrega, y te lo dice en el idioma de las personas que hacen el trabajo, que suelen saber perfectamente qué está roto. Lo que Beck rechaza no es escuchar eso. Es *apuntarle*. Un termómetro es un gran instrumento y un pésimo objetivo: si tu meta es que el termómetro marque menos, lo metés en la heladera.

> 🕳️ **HUECO — necesita a César:** ¿Estás de acuerdo con Beck acá, o te parece que en un contexto de trabajo real —sobre todo estatal, con sueldos y carrera fijos— la felicidad SÍ tiene que ser un objetivo declarado porque no hay otra palanca? Dos o tres frases con tu postura.

### Qué cambia en la práctica

Si tomás la palabra en serio, cambian tres cosas chiquitas y concretas.

Cambia **qué preguntás**. «¿Estás conforme con tus herramientas?» es una pregunta de experiencia y la respuesta no te sirve para nada. «¿Cuántas veces esta semana esperaste más de una hora por algo que no dependía de vos?» es una pregunta de efectividad, y la respuesta viene con un ticket adentro.

Cambia **qué arreglás primero**. La cola se ordena por fricción removida, no por incomodidad reportada. A veces coinciden. Cuando no coinciden, gana la fricción.

Y cambia **qué no comprás**. Ninguna perk, ningún dashboard, ningún onboarding con globos entra en el presupuesto de efectividad. Beck es durísimo con eso en otro tramo de la conversación —vender el tablero sin acompañar el trabajo es malpractice [[C-15]]— y la lógica es la misma: el instrumento no es el trabajo.

### Cierre

Me gusta este argumento porque es lo contrario de lo que parece. Suena a jefe rancio diciendo «acá se viene a trabajar». Y es exactamente al revés: es la posición que se toma en serio el malestar del programador, tanto que se niega a comprarlo barato. Decirle a alguien «te quiero efectivo» es decirle «voy a ir a pelearme con las cosas que te frenan», que cuesta plata y capital político. Decirle «te quiero feliz» sale una pizza.

Es la misma estructura que XP [[C-14]], si lo pensás: aquellas prácticas —pair programming, tests primero, integración continua— nunca se vendieron como formas de pasarla bien. Se vendieron como formas de poder trabajar sin romper todo, y la consecuencia lateral, la que aparece cuando el código deja de darte miedo, es que el trabajo se vuelve disfrutable. Beck viene diciendo lo mismo desde hace un cuarto de siglo: la 1.ª edición de *Extreme Programming Explained: Embrace Change* es de 1999[^xp_explained]. Sólo que ahora se lo tiene que decir a una industria que le puso a la cosa un nombre que invita a olvidarlo.

No me hagas feliz. Sacame las piedras del camino. La alegría la pongo yo.

> 🕳️ **HUECO — necesita a César:** El cierre necesita una línea tuya, no de Beck. ¿Cuál es tu versión de «sacame las piedras del camino»? ¿Qué le pedirías hoy a una organización si te dieran un solo pedido?

> 🕳️ **HUECO — necesita a César:** ¿Querés que el post mencione tu propia experiencia armando herramientas para otros (MerLinux, el workflow de Trac en Cultura)? Si sí: ¿eso lo hiciste para que el equipo la pasara mejor o para que pudiera trabajar? ¿Lo pensaste en esos términos en su momento?

[^beck_noda]: Kent Beck y Abi Noda, [«Developer Productivity Metrics: Education Necessary»](https://newsletter.kentbeck.com/p/developer-productivity-metrics-education), newsletter *Tidy First* (Kent Beck), 29 de enero de 2025. Republicado por Abi Noda como [«Measuring developer productivity: A clear-eyed view»](https://newsletter.getdx.com/p/developer-productivity-metrics-the), newsletter *Engineering Enablement* (DX), 5 de febrero de 2025 — mismo contenido, título distinto. Backup en Wayback: [snapshot 2026-04-12 de la versión Tidy First](http://web.archive.org/web/20260412123620/https://tidyfirst.substack.com/p/developer-productivity-metrics-education) y [snapshot 2026-04-19 de la versión DX](http://web.archive.org/web/20260419074227/https://newsletter.getdx.com/p/developer-productivity-metrics-the).

[^dx_core4]: Abi Noda, [«Introducing the DX Core 4»](https://newsletter.getdx.com/p/introducing-the-dx-core-4), newsletter *Engineering Enablement*, 10 de diciembre de 2024. Define las cuatro dimensiones (speed, effectiveness, quality, impact) y el DXI como «an aggregated score from 14 standardized Likert-scale survey items».

[^dx_docs]: DX, [«Guide to the DX Core 4»](https://docs.getdx.com/dx-core-4/), documentación de producto. La dimensión *Effectiveness* mide «Developer experience & friction» y se instrumenta con el DXI, que la propia doc reconoce «survey-based by design».

[^storey_site]: [Sitio personal de Margaret-Anne Storey](https://www.margaretstorey.com/) — profesora de Ciencias de la Computación en la University of Victoria y Canada Research Chair in Human and Social Aspects of Software Engineering.

[^storey_dx]: DX, [«An inside look at SPACE with Dr. Margaret-Anne Storey»](https://getdx.com/podcast/space-framework/) — la presenta como Chief Scientist de DX y confirma el apodo: «This week's guest is Dr. Margaret-Anne Storey, who goes by the name Peggy».

[^storey_tse]: M.-A. Storey, T. Zimmermann, C. Bird, J. Czerwonka, B. Murphy y E. Kalliamvakou, «Towards a Theory of Software Developer Job Satisfaction and Perceived Productivity», *IEEE Transactions on Software Engineering*, vol. 47, n.º 10, pp. 2125–2142, 2021. DOI: [10.1109/TSE.2019.2944354](https://doi.org/10.1109/TSE.2019.2944354). Texto completo libre: [preprint en Microsoft Research](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/12/storey-tse-2019.pdf). Comentario de la propia autora: [«A Theory of Developer Satisfaction and Perceived Productivity»](https://www.margaretstorey.com/blog/2020/06/01/developer-productivity-satisfaction-theory/).

[^space]: N. Forsgren, M.-A. Storey, C. Maddila, T. Zimmermann, B. Houck y J. Butler, «The SPACE of Developer Productivity: There's more to it than you think», *ACM Queue*, vol. 19, n.º 1, pp. 20–48, 2021. DOI: [10.1145/3454122.3454124](https://doi.org/10.1145/3454122.3454124). La dimensión «S» es *satisfaction and well-being*.

[^xp_explained]: Kent Beck, *Extreme Programming Explained: Embrace Change*, 1.ª ed., Addison-Wesley, Reading, MA, 1999. ISBN 0201616416. Copia en préstamo digital controlado: [Internet Archive](https://archive.org/details/extremeprogrammi00beck) — ojo, ese ejemplar es la 7.ª impresión, fechada 2000 por archive.org; el copyright de la 1.ª edición es 1999. (La 2.ª edición, de 2004, es la coescrita con Cynthia Andres: no confundirlas.)
