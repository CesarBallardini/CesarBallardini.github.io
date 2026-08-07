### C-15 — "Vender solo el dashboard es malpractice" — Beck sobre métricas sin acompañamiento

- **Archivo seed:** _draft-rest.md bucket 6 (cosechado 2026-04-09)_
- **Slug propuesto:** `vender-dashboards-malpractice`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-vender-dashboards-malpractice/index.md`
- **Serie:** filosofia
- **Cross-links:** [[C-11]] (Goodhart), [[C-12]] (Forest/Desert), [[C-13]] (anti-productivity)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1600-1800 palabras (ensayo de opinión con una analogía central y su desarme)

**Concepto:** En el podcast con Abi Noda (CEO de DX, vendedor de dashboards de productividad de software), Kent Beck dice una frase fuerte: "yo iría tan lejos como decir que si solo vendés el dashboard, eso es malpractice". El argumento: cualquier sistema de métricas necesita educación, contexto, interpretación. Vender un dashboard "y arreglátelas" es como vender un análisis de sangre sin médico que lo interprete. El post discute la analogía médica, qué tipo de "consultoría con dashboard" es honesta, y cómo evitar caer en la trampa.

**Hook:** "si solo vendés el dashboard, eso es malpractice." Lo dijo Kent Beck en una conversación con el CEO de la empresa que vende dashboards de productividad. La conversación fue civilizada. El post discute por qué tenía razón.

**Outline:**

1. **El hook**: la frase de Beck dicha en la cara del vendedor, y por qué la conversación no explotó.
2. **La analogía médica tal como la trajeron ellos**: el análisis de lípidos. Un número sin médico no es diagnóstico.
3. **Dónde la analogía funciona**: instrumento ≠ interpretación; el valor está en el acompañamiento, no en el gráfico.
4. **Dónde la analogía se rompe** (la parte que me interesa): el análisis de sangre mide algo que existía antes del análisis; la métrica de productividad *crea* aquello que mide. Puente a Goodhart [[C-11]].
5. **El modelo de negocio como problema epistemológico**: quien vende el instrumento no puede ser el único que enseña a leerlo.
6. **Qué sería una consultoría honesta con dashboard**: cuatro criterios prácticos.
7. **Por qué compramos dashboards igual**: la demanda de legibilidad desde arriba, no la oferta. Puente a [[C-12]] y [[C-13]].
8. **Cierre**: «malpractice» es una palabra de profesión, y ahí está el verdadero filo de la frase.

**Bibliografía:**

_Fuente primaria (verificada por fetch el 2026-07-15):_

- **Kent Beck & Abi Noda, «Developer Productivity Metrics: Education Necessary», 29 de enero de 2025** — el original, en el newsletter propio de Beck: <https://newsletter.kentbeck.com/p/developer-productivity-metrics-education> — **frágil** (newsletter personal / Substack). Es **texto (transcripción editada de una conversación), no podcast ni video**. Ojo: `tidyfirst.substack.com` ahora redirige 301 a `newsletter.kentbeck.com`. Backup Wayback de la URL vieja (snapshot 2026-04-12): <http://web.archive.org/web/20260412123620/https://tidyfirst.substack.com/p/developer-productivity-metrics-education> — **estable**. (La URL nueva de kentbeck.com todavía no tiene snapshot; conviene pedir uno antes de publicar.)
- **Repost de la misma conversación por Abi Noda, «Engineering Enablement» newsletter de DX, 5 de febrero de 2025**: <https://newsletter.getdx.com/p/developer-productivity-metrics-the> — **frágil**. Útil como confirmación cruzada: el vendedor republicó la crítica en su propio newsletter.
- **DX — página institucional «About»**: <https://getdx.com/about/> — **frágil**. Ahí DX se describe a sí misma como «the world's leading developer intelligence platform» y lista a Abi Noda como **«CEO, Co-Founder»**. La home (<https://getdx.com/>) usa otra fórmula: «engineering intelligence platform designed by researchers».

_Autoderivación en medicina (para el movimiento 5):_

- **Stark Law / Physician Self-Referral Law — 42 U.S.C. § 1395nn.** Descripción oficial en HHS Office of Inspector General, «Fraud & Abuse Laws»: <https://oig.hhs.gov/compliance/physician-education/fraud-abuse-laws/> — **estable** (dominio institucional .gov). Prohíbe que un médico derive a un paciente a una entidad con la que él (o un familiar directo) tiene una relación financiera, para «designated health services» pagados por Medicare/Medicaid, salvo excepción aplicable.
- **Huttinger, R. & Aeddula, N. R., «Stark Law», StatPearls**, StatPearls Publishing / NCBI Bookshelf (National Library of Medicine, NIH), última actualización 6 de octubre de 2022: <https://www.ncbi.nlm.nih.gov/books/NBK559074/> — **estable**. Dato de oro para el post: la ley **nació aplicándose específicamente a la derivación a laboratorios clínicos** y recién después se extendió a «designated health services». La analogía del post cae justo sobre el caso original de la norma.
- _Rechazada:_ <https://www.cms.gov/medicare/regulations-guidance/physician-self-referral> (la página canónica de CMS) devuelve **HTTP 403** a fetch automatizado. Existe y es la fuente canónica, pero no la pude abrir; por eso se cita OIG + StatPearls, que sí abrieron.

_Colegiación de informáticos en Argentina (para el cierre):_

- **Fundación Vía Libre, «Profesionales informáticos, en puja por la colegiación», 21 de septiembre de 2007**: <https://www.vialibre.org.ar/profesionales-informaticos-en-puja-por-la-colegiacion/> — **frágil**; backup Wayback (snapshot 2026-03-07): <http://web.archive.org/web/20260307092440/https://www.vialibre.org.ar/profesionales-informaticos-en-puja-por-la-colegiacion/> — **estable**. Es una republicación de una nota de *La Capital* de Rosario (19/09/2007) sobre **un proyecto de colegiación obligatoria en la provincia de Santa Fe** — o sea, la provincia de César. Federico Heinz (Vía Libre) citado en contra: «En Córdoba tenemos matriculación obligatoria desde hace 20 años y ninguno de esos beneficios existió», y el argumento de que la informática es una ciencia *transversal* (como la matemática), no *vertical* (como la medicina o la arquitectura) — que es exactamente el eje del último movimiento del post.
- _Rechazadas (404 en vivo, contenido no verificable):_ `vialibre.org.ar/2006/12/14/sobre-la-matriculacion-obligatoria-en-informatica/` y `vialibre.org.ar/2007/11/01/pablo-sametband-contra-matriculacion/`. Ambas aparecen en buscadores pero devuelven **404**. La primera tiene snapshot de Wayback (2020-08-09) pero no pude leer su contenido desde acá, así que **no se cita**.

_Contexto (no citas primarias):_

- Goodhart aparece explícitamente en la propia entrevista: Beck abre con «I would like to adopt a new resolution that any conversation about metrics has to start with Goodhart's Law». Munición directa para el puente a [[C-11]].

**Imágenes:** _a definir_

**Tags propuestos:** `['Kent Beck','dashboards','metricas','malpractice','consultoria','critica']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le agregó outline numerado (8 movimientos) y un borrador de prosa completo (~1750 palabras) en la sección **Borrador de prosa** al pie.

Lo que quedó escrito: el desarme de la analogía médica (funciona como crítica al «te vendo el número y arreglate», se rompe en el punto de que el colesterol existe sin el análisis y la métrica de productividad no), el argumento del conflicto de interés estructural del vendedor-intérprete, los cuatro criterios de consultoría honesta, y el cierre sobre «malpractice» como palabra de profesión colegiada.

Lo que quedó como hueco (6 `🕳️`): toda la experiencia vivida de César con métricas y tableros — si le vendieron o le pidieron uno alguna vez, si él mismo construyó tableros para otros, el episodio del sector público santafesino, la opinión propia sobre si el problema está en la oferta o en la demanda, la posición sobre colegiación, y la anécdota de cierre. **Los 6 huecos siguen intactos**: ninguna pasada de fuentes los puede contestar.

---

### Pasada de fuentes — 2026-07-15 (Claude, sin revisar por César)

Se leyó la fuente primaria completa. **La entrevista existe, la cita es real y la premisa central del post se sostiene.** Detalle abajo.

**⚠️ PREMISA EN DUDA: la conversación estaba patrocinada por DX.** Beck lo declara arriba de todo: «Thank you to DX for sponsoring this conversation. They paid me for my time & this space», y presenta el texto como «a sponsored conversation with Abi Noda, CEO of DX». Esto no toca la cita ni el argumento, pero **desarma el asombro del Hook y del Concepto**: el post se maravilla de que «la conversación no explotó» y de que Beck «se lo dijo en la cara al tipo», cuando en realidad DX le pagó a Beck para tener esa conversación en ese espacio. La cordialidad estaba comprada. Ahora bien: esto **no hunde el post, lo mejora** — el propio movimiento 5 (el vendedor-intérprete y su conflicto de interés) queda ilustrado por la fuente misma, que es un crítico cobrando del vendedor al que critica. Ya se incorporó a la prosa en dos lugares (un párrafo nuevo tras el hook y otro al final del movimiento 5) y en el cierre (Noda republicó la crítica entera en el newsletter de DX una semana después: no hay consecuencia, sólo contenido). **César tiene que decidir si el Hook sobrevive tal cual**, porque hoy promete un coraje que la fuente no respalda.

**⚠️ Error de hecho en el Concepto (no lo toqué, es de César):** dice «En el podcast con Abi Noda». **No es un podcast**: es un texto, una transcripción editada publicada en el newsletter de Beck. Tampoco es de enero de 2026 —como decía la bibliografía del seed— sino del **29 de enero de 2025**. Hay que corregir el Concepto antes de escribir.

**`[VERIFICAR:]` resueltos (4 de 5):**

1. `[^beck_quote]` — **resuelto**. Cita textual fijada: «I would go so far as to say if you just sell the dashboard, that's malpractice». El seed decía *only* donde el original dice *just*. Formato (texto) y fecha (29-01-2025) confirmados. Hay link citable.
2. `[^dx]` — **resuelto**. Abi Noda es **CEO y cofundador**, las dos cosas, según la propia página About de DX. DX se describe como «developer intelligence platform», no como dashboard — lo que le da la razón al matiz del post: Beck ataca el empaquetado.
3. `[^lipids]` — **resuelto, y a favor del post**. **La analogía de los lípidos la trae Noda**, no Beck, justo después de la frase de malpractice. El segundo y el tercer movimiento quedan en pie sin reescritura. Este era el `[VERIFICAR:]` del que dependía el tercer movimiento.
4. `[^self_referral]` — **resuelto en lo esencial**: la norma existe, se llama **Stark Law** (42 U.S.C. § 1395nn), y —regalo para el post— **nació regulando específicamente la derivación a laboratorios clínicos**. La analogía del post cae sobre el caso fundacional de la norma. Queda un `[VERIFICAR:]` acotado: Stark es derecho estadounidense y sólo alcanza Medicare/Medicaid, mientras el post afirma «en cualquier sistema medianamente sano». O se acota la frase, o falta buscar el equivalente argentino (no lo busqué).

**`[VERIFICAR:]` que siguen abiertos (3):**

- `[^colegiacion]` — **parcial**. Encontré y leí una entrada real de vialibre.org.ar (21-09-2007) donde Federico Heinz argumenta contra la colegiación obligatoria, y —hallazgo afortunado— la nota es sobre **un proyecto de la provincia de Santa Fe**. Alcanza para decir «Vía Libre argumentó en contra»; no alcanza para atribuirle una posición institucional formal. Dos entradas más del sitio que aparecen en buscadores dan **404**.
- `[^self_referral]` — el alcance jurisdiccional (ver arriba).
- `[^repost]` — menor: confirmar el título exacto del repost de Noda y si editó el texto.

**Munición nueva que salió de la fuente y conviene usar:**

- Beck abre la conversación pidiendo que **toda charla sobre métricas empiece por Goodhart**: «I would like to adopt a new resolution that any conversation about metrics has to start with Goodhart's Law». Puente directo y citable a [[C-11]].
- El contraste **transversal/vertical** de Heinz (la informática es como la matemática, no como la medicina) choca de frente con la analogía médica del post. Es el mejor material para el último movimiento y no estaba en el borrador.

Pendiente adicional: definir imágenes (hay candidatas anotadas en las notas de armado, ninguna con licencia verificada todavía) y resolver `[[C-11]]`, `[[C-12]]`, `[[C-13]]` al publicar.

---

## Borrador de prosa

«Yo iría tan lejos como decir que si solo vendés el dashboard, eso es malpractice».[^beck_quote]

La frase es de Kent Beck. La dijo en una conversación con Abi Noda, que es CEO y cofundador de DX, que es una empresa que vende métricas de productividad de software.[^dx] O sea: se lo dijo en la cara al tipo cuyo producto es exactamente eso. Y la conversación no explotó: siguió siendo civilizada, incluso cordial. Noda no se puso a la defensiva, y unas líneas después aparece la analogía que le da al asunto su forma definitiva: la del análisis de lípidos.[^lipids]

Ahora, antes de seguir, un dato que cambia el color de todo lo anterior: **la conversación estaba patrocinada por DX**. Beck lo aclara arriba de todo, con todas las letras: DX le pagó por su tiempo y por ese espacio.[^sponsored] Así que la cordialidad no es un milagro de la buena fe: es, en parte, el clima que se compra. Lo cual —ya vas a ver— no debilita el argumento de Beck. Lo vuelve un ejemplo de sí mismo.

Voy a contarte por qué creo que Beck tenía razón, y también dónde creo que la analogía que usaron se queda corta —que es, para mí, la parte interesante.

### El análisis de sangre

La analogía es esta. Te hacés un perfil lipídico. Te llega un papel con números: colesterol total, HDL, LDL, triglicéridos. Al costado, los rangos de referencia. Si tu LDL está fuera de rango, el papel te lo marca.

Ahora bien: nadie sostiene con seriedad que ese papel sea el acto médico. El papel es un instrumento. El acto médico es lo que pasa cuando alguien que estudió años mira ese número *junto con* tu edad, tu historia familiar, tu presión, lo que comés, si fumás, qué medicación tomás, y decide si eso significa «cambiá la dieta», «hacemos otro control en seis meses» o «empezamos estatinas hoy». El número solo no dice ninguna de esas tres cosas. El número solo, entregado sin nadie que lo lea, produce dos resultados posibles: pánico o indiferencia. Casi nunca produce una buena decisión.

Vender el laboratorio sin el médico —o peor, vender el laboratorio *diciendo* que reemplaza al médico— sería, efectivamente, mala praxis. Ahí la analogía de Noda hace su trabajo, y hace falta reconocer que la trajo él, no un crítico externo.

El paralelo con las métricas de ingeniería es directo. Un tablero te dice que el lead time del equipo B subió de tres días a nueve. ¿Y? Puede ser que el equipo B esté en problemas. Puede ser que el equipo B haya empezado a tocar el módulo de facturación, que es un pantano, y que nueve días sea heroico. Puede ser que se fueron dos personas. Puede ser que cambiaron cómo etiquetan los tickets. El número, solo, no distingue entre «hay un problema» y «hay un contexto». Un gerente con el tablero abierto y sin nadie que lo ayude a leerlo va a hacer lo que hace cualquiera frente a un número rojo: apretar hasta que se ponga verde.

Y ahí está el punto de Beck: si vos vendés el instrumento y te desentendés de la interpretación, sabiendo que el instrumento sin interpretación produce ese comportamiento, no sos neutral. Sos parte de lo que pasa después.

> 🕳️ **HUECO — necesita a César:** ¿Alguna vez te vendieron, te pidieron o te impusieron un tablero de métricas de equipo? ¿Cuál era la métrica estrella y qué terminó pasando con ella? Una o dos frases alcanzan para abrir el post con esto en vez de con la cita.

### Donde la analogía se rompe

Hasta acá vengo acompañando. Pero la analogía médica tiene una costura, y me parece que es la costura más importante de todo el asunto.

Tu colesterol existe independientemente del análisis. Si el laboratorio cierra, tu LDL sigue siendo el que es. El instrumento *observa* algo que ya estaba ahí, y lo observa —dentro de su error de medición— sin modificarlo. Podés discutir el rango de referencia, podés discutir si la medición es útil; no podés discutir que hay una magnitud física ahí afuera, en tu sangre, esperando ser medida.

Las métricas de productividad de software no son así. El lead time, los pull requests por semana, el deployment frequency: nada de eso preexiste al tablero de la misma manera. En el momento en que el número se vuelve visible para quien decide los aumentos, deja de ser una observación y pasa a ser un incentivo. La gente —gente razonable, no gente tramposa— empieza a partir los pull requests en pedazos más chicos. Empieza a abrir tickets que antes no abría. Empieza a mover trabajo hacia lo que el tablero cuenta y a sacarlo de lo que el tablero no ve, que casualmente es donde vive casi todo el trabajo valioso: mentorear a alguien, borrar código, decir «esto no hay que construirlo».

Esto es Goodhart, obviamente, y le dediqué un post entero [[C-11]]. Pero acá el punto es más específico: **la analogía médica le concede al dashboard más objetividad de la que tiene**. Un análisis de lípidos mal interpretado te da una mala decisión sobre un cuerpo que sigue siendo el mismo. Un dashboard mal interpretado *reconfigura el cuerpo*. A los seis meses el equipo ya no es el equipo que era cuando compraste el tablero: es un equipo optimizado para el tablero.

Lo cual, si querés, hace la frase de Beck todavía más fuerte que lo que él mismo dijo. Si el instrumento fuera inocuo como una centrífuga, vender el instrumento solo sería negligencia. Si el instrumento deforma lo que mide, vender el instrumento solo es algo más parecido a soltar un reactivo en el organismo y facturar la observación.

### El problema del vendedor-intérprete

Está la parte incómoda, que Beck señala con la palabra que eligió. Si el dashboard sin acompañamiento es mala praxis, la conclusión obvia es «bueno, vendé el dashboard *con* acompañamiento». Y eso es, más o menos, lo que vende toda consultora seria de este rubro.

Pero fijate el círculo. El médico que interpreta tu análisis no cobra por el análisis. Es más: en cualquier sistema medianamente sano, la relación entre el que indica el estudio y el laboratorio que lo cobra está regulada precisamente porque sabemos qué pasa cuando no lo está. Se llama autoderivación, y en medicina hay literatura y hay normas al respecto.[^self_referral]

En el negocio de las métricas de ingeniería no hay ninguna separación equivalente. La misma empresa te vende el instrumento, te enseña a leerlo, y te dice si el resultado justifica renovar la licencia. Un intérprete cuyo ingreso depende de que sigas creyendo en el instrumento no es un intérprete independiente. No hace falta postular mala fe: alcanza con la deriva normal de cualquiera que mira su producto todos los días.

Así que la versión más dura del argumento de Beck no es «vendé también la educación». Es: **el que vende el tablero no puede ser el único que te enseña a leerlo, por la misma razón por la que no querés que el laboratorio te indique los estudios**.

Y acá vuelve el detalle del patrocinio, que es lo que más me gusta de todo este asunto. La crítica más filosa que se le hizo públicamente a la industria de las métricas se publicó en un espacio pagado por una empresa de métricas. Beck lo declaró —hay que decirlo, lo declaró arriba de todo, que es más de lo que hace casi nadie—, pero la estructura sigue siendo la que él mismo denuncia: el intérprete cobrando del vendedor. No es hipocresía; es que no hay afuera. No existe el lugar independiente desde el cual decir esto, porque la profesión nunca lo construyó. Que es, exactamente, adonde va a parar el final del post.

> 🕳️ **HUECO — necesita a César:** ¿Te tocó alguna vez estar del lado del que *construye* el tablero para otro (un jefe, un cliente, una dirección)? Si sí: ¿te pidieron alguna vez que la métrica mostrara algo en particular, o te autocensuraste al elegir qué mostrar?

> 🕳️ **HUECO — necesita a César:** En el sector público santafesino (STG / Ministerio de Cultura) — ¿hubo alguna vez un pedido de «indicadores de gestión» sobre el trabajo del área de sistemas? ¿Quién los pedía, qué querían ver, y qué se terminó reportando? Este es el mejor contraejemplo posible, porque ahí el que pide la métrica ni siquiera es el que la va a interpretar.

### Qué sería una consultoría honesta con dashboard

No estoy en contra de medir. Estoy en contra de que medir se venda como pensar. Si tuviera que escribir los criterios de lo que compraría, serían estos cuatro:

1. **El acompañamiento no es un extra facturable, es el producto.** Si el tablero se puede comprar solo, se va a comprar solo. Beck tiene razón en atacar el empaquetado, no el software.
2. **El instrumento viene con su propia lista de fallas.** Cualquier estudio médico serio publica su sensibilidad, su especificidad y sus falsos positivos. Un dashboard de productividad debería venir con un documento que diga, con nombre y apellido, qué comportamiento perverso induce cada métrica que muestra. Si el vendedor no puede escribir ese documento, no entiende su propio producto.
3. **El número no le llega a quien decide sueldos.** El día que el tablero entra a la revisión de desempeño, murió como instrumento de diagnóstico y nació como instrumento de disciplina. No hay curso de interpretación que arregle eso.
4. **Hay una fecha de vencimiento.** Toda métrica se agota: sirve mientras nadie la optimiza. Una consultoría honesta te dice cuándo dejar de mirar la que te vendió.

Ninguno de los cuatro es sobre el software. Los cuatro son sobre la relación. Que es exactamente el punto de Beck.

### Por qué los compramos igual

Queda una pregunta que la frase de Beck no responde, y es la que me parece más honesta de todas: si es tan obvio que el número solo no dice nada, ¿por qué se venden tantos?

Mi sospecha es que el problema no está en la oferta. Está en la demanda de legibilidad. Una organización de cierto tamaño tiene, arriba, gente que tiene que decidir sobre un trabajo que no puede ver, no puede evaluar y no puede hacer. El dashboard no le vende información: le vende la posibilidad de decidir sin entender. Eso es un producto valiosísimo y la industria hace bien en cobrarlo caro. Es la misma dinámica que discutí en [[C-12]] cuando hablé de qué le pasa a un bosque cuando lo administra alguien que solo puede contar árboles, y la que está atrás de casi toda la maquinaria de productividad que critiqué en [[C-13]].

Con lo cual la mala praxis, si querés, es compartida. El que vende el tablero solo comete la que dice Beck. El que lo compra para no tener que aprender qué hace su gente comete otra, más silenciosa, y no hay colegio profesional que se la reproche.

> 🕳️ **HUECO — necesita a César:** ¿Compartís esta tesis de que la demanda manda? ¿O te parece que estoy siendo demasiado indulgente con los vendedores? Esta sección es la opinión propia del post y necesita ser tuya, no mía.

### La palabra

Termino con lo que a mí me parece el verdadero filo de la frase, y que es fácil pasar por alto.

Beck no dijo «es una macana». No dijo «es poco ético», que es lo que uno dice para no comprometerse. Dijo **malpractice**. Y esa es una palabra de profesión: mala praxis solo se le puede imputar a alguien que pertenece a un cuerpo que definió un estándar de cuidado, que tiene una matrícula que se puede perder, y que respalda a sus miembros cuando se niegan a hacer algo que el cliente pide. El médico que no te da la receta que le exigís tiene un colegio atrás.

Nosotros no tenemos nada de eso. Usar «malpractice» para hablar de software es, en el mejor de los casos, una aspiración: pedir prestada la gravedad de una profesión que sí construyó esas instituciones, sin haber construido las nuestras. Y en el peor, es admitir el problema en la misma frase en que se lo denuncia. Beck puede decirle a Noda que vender el dashboard solo es mala praxis, y Noda puede escucharlo con toda cordialidad —como efectivamente lo escuchó— y seguir vendiendo, porque no hay ninguna consecuencia. La palabra no tiene dónde apoyarse.

La prueba está a la vista: una semana después, Noda republicó la conversación entera —acusación de mala praxis incluida— en el newsletter de su propia empresa.[^repost] Y hace bien. Cuando una imputación de mala praxis no tiene un colegio atrás, no es una imputación: es contenido. Se absorbe, se republica, y hasta funciona como prueba de que uno es de los que aceptan la crítica.

Es un debate viejo en Argentina, el de la colegiación de los informáticos, y tiene sus propios costos que no son menores.[^colegiacion]

> 🕳️ **HUECO — necesita a César:** ¿Cuál es tu posición sobre la colegiación profesional de los informáticos? Vía Libre argumentó en contra en su momento; el cierre del post depende de dónde parás vos. Dos frases.

> 🕳️ **HUECO — necesita a César:** ¿Hay algún momento de tu carrera en que te hubiera gustado tener un colegio atrás para poder decir «esto no lo hago»? Si hay uno, ese es el cierre real del post y la cita de Beck pasa a ser la excusa para contarlo.

---

**Notas de armado (no van al post):**

- **Imágenes:** idea para el hero — un papel de análisis clínico de lípidos con los rangos de referencia al costado, o una centrífuga de laboratorio. Buscar en Wikimedia Commons (dominio público / CC), recortar a 2.5:1 con Pillow. Alternativa: un gráfico de líneas antiguo, tipo gráfico de control industrial. Recordar la footnote `[^img_hero]` con atribución y referenciarla inline.
  - Pasada de sourcing 2026-07-15: abrí [`Category:Blood tests`](https://commons.wikimedia.org/wiki/Category:Blood_tests) en Commons — tiene varias planillas de resultados reales (`CMP report.JPG`, `Résultat d'une prise de sang.jpg`, `Результаты анализа крови.jpg`, `Complete blood count and differential.jpg`), que es exactamente el género que pide el post. **No verifiqué las licencias de ninguna todavía** — hay que abrir la ficha de cada archivo antes de usarla.
  - Descartada: [`File:Blood-centrifugation-scheme.png`](https://commons.wikimedia.org/wiki/File:Blood-centrifugation-scheme.png) (CC BY 3.0, autor KnuteKnudsen) — licencia sana pero es **retrato, 397×530 px**: no da para un hero 2.5:1 ni recortándola.
- **Corrección de formato (pasada 2026-07-15):** la fuente **no es un podcast ni un video**, es texto. Cualquier mención a «el episodio», «escuchar» o «la entrevista grabada» tiene que salir del post. La fecha es **enero de 2025**, no enero de 2026.

[^beck_quote]: [«Developer Productivity Metrics: Education Necessary»](https://newsletter.kentbeck.com/p/developer-productivity-metrics-education) — Kent Beck y Abi Noda, 29 de enero de 2025. La frase textual es: «I would go so far as to say if you just sell the dashboard, that's malpractice». Traducción propia. **Nota de sourcing:** la reconstrucción del seed decía *«if you **only** sell the dashboard»*; el original dice *«if you **just** sell the dashboard»*. Ya corregido. El formato es **texto** —una transcripción editada publicada en el newsletter de Beck—, no un podcast ni un video: hay que sacar del post cualquier referencia a «el episodio» o a «escuchar». La fecha real es **enero de 2025**, no enero de 2026 como decía la bibliografía del seed.

[^dx]: [DX — About](https://getdx.com/about/). DX se describe a sí misma como «the world's leading developer intelligence platform» (en la home, como «engineering intelligence platform designed by researchers»), y lista a **Abi Noda como «CEO, Co-Founder»** — o sea, las dos cosas. Confirmado también dentro de la propia entrevista, donde Beck lo presenta como «Abi Noda, CEO of DX». Punto a favor del matiz del post: DX **no** se vende a sí misma como «un dashboard» sino como plataforma de inteligencia sobre ingeniería; el reproche de Beck apunta al empaquetado, no al software.

[^lipids]: **La analogía es de Noda.** Confirmado en la transcripción: tras la frase de Beck sobre malpractice, Noda responde «Yeah, it's like getting a lipid test but not being able to meet with a physician who can properly interpret it». O sea: el vendedor mismo concede que el número necesita médico, que es exactamente lo que el post necesitaba. El segundo y el tercer movimiento quedan en pie tal como están escritos.

[^self_referral]: La norma existe y tiene nombre: **Stark Law** o *Physician Self-Referral Law*, 42 U.S.C. § 1395nn. Prohíbe que un médico derive pacientes a una entidad con la que tiene una relación financiera, para prestaciones pagadas por Medicare/Medicaid. Ver [HHS Office of Inspector General, «Fraud & Abuse Laws»](https://oig.hhs.gov/compliance/physician-education/fraud-abuse-laws/) y [Huttinger, R. & Aeddula, N. R., «Stark Law», StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK559074/) (NCBI Bookshelf / NIH, act. 6-10-2022). **Detalle que le viene perfecto al post:** la ley empezó regulando exactamente la derivación a **laboratorios clínicos**, y sólo después se extendió al resto de las prestaciones. La analogía del post cae sobre el caso fundacional de la norma. [VERIFICAR: Stark es **derecho estadounidense y sólo alcanza a Medicare/Medicaid**; el párrafo del post dice «en cualquier sistema medianamente sano», lo cual es más ancho que lo que la fuente sostiene. O se acota la frase a «en Estados Unidos, por ejemplo…», o hace falta buscar el equivalente argentino (¿ley de ejercicio de la medicina, códigos de ética del COMRA, normativa provincial de Santa Fe?). No busqué normativa argentina en esta pasada.]

[^colegiacion]: [«Profesionales informáticos, en puja por la colegiación»](https://www.vialibre.org.ar/profesionales-informaticos-en-puja-por-la-colegiacion/) — Fundación Vía Libre, 21 de septiembre de 2007 ([backup Wayback](http://web.archive.org/web/20260307092440/https://www.vialibre.org.ar/profesionales-informaticos-en-puja-por-la-colegiacion/)). Republica una nota de *La Capital* de Rosario (19-09-2007) sobre un proyecto de colegiación obligatoria **en la provincia de Santa Fe**. Federico Heinz, de Vía Libre, argumenta en contra: «En Córdoba tenemos matriculación obligatoria desde hace 20 años y ninguno de esos beneficios existió», y sostiene que la informática es una ciencia *transversal* —como la matemática— y no *vertical* como la medicina o la arquitectura. Ese contraste transversal/vertical choca de frente con la analogía médica del post, y es probablemente el mejor material del cierre. [VERIFICAR: lo que abrí es una **republicación periodística con Heinz citado**, no un documento institucional de posición de Vía Libre. Si el post va a decir «Vía Libre argumentó en contra», con esto alcanza; si va a decir «la posición institucional de Vía Libre es X», falta el documento. Busqué además dos entradas más de vialibre.org.ar que aparecen en buscadores (`2006/12/14/sobre-la-matriculacion-obligatoria-en-informatica` y `2007/11/01/pablo-sametband-contra-matriculacion`) y **las dos devuelven 404**; la primera tiene snapshot de Wayback de 2020 que no pude leer. Probar el buscador interno del sitio o escribirle a la Fundación.]

[^repost]: [«Developer productivity metrics: a clear-eyed view»](https://newsletter.getdx.com/p/developer-productivity-metrics-the) — Abi Noda, newsletter «Engineering Enablement» de DX, 5 de febrero de 2025. Es la misma conversación, republicada por el propio Noda en el canal de DX una semana después del original de Beck (29-01-2025). [VERIFICAR: confirmar el título exacto con el que Noda la republicó y si el texto está editado respecto del original de Beck; abrí la página y confirmé que es la misma conversación, la misma cita de malpractice y la misma respuesta de los lípidos, pero no la comparé párrafo por párrafo.]

[^sponsored]: La conversación fue **patrocinada por DX**. Beck lo declara arriba de todo, en el original: «Thank you to DX for sponsoring this conversation. They paid me for my time & this space», y presenta el texto como «a sponsored conversation with Abi Noda, CEO of DX».

