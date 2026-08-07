### J-09 — "Look both ways before crossing a one-way street" — la paradoja de Doug Linder

- **Archivo seed:** _draft-rest.md bucket 6 (cosechado 2026-04-09)_
- **Slug propuesto:** `doug-linder-cruzar-calle-una-via`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-doug-linder-cruzar-calle-una-via/index.md`
- **Serie:** nerd
- **Cross-links:** [[K-23]] (citas interesantes), [[J-03]] (MindForth)
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César)
- **Length target:** 1600–1900 palabras (ensayo corto lateral, una cita desempacada)

**Concepto:** La cita "A good programmer is someone who always looks both ways before crossing a one-way street" — atribuida a Doug Linder — captura en una línea la actitud del buen programador frente al riesgo. Las flechas oficiales del lenguaje, framework o sistema no son garantía de que nada vendrá del otro lado. El post desempaca la cita, busca su origen real (es difícil de rastrear), y discute las situaciones en programación donde "mirar la dirección equivocada" salva el día.

**Hook:** "un buen programador es alguien que siempre mira para los dos lados antes de cruzar una calle de una sola vía". Doug Linder. Probablemente. La frase es perfecta. Vamos a ver de dónde sale y por qué es verdad.

**Outline:**

1. **El hook** — la frase, y el «probablemente» pegado a la atribución. Dos párrafos.
2. **Quién carajo es Doug Linder** — el rastreo que no llega a ningún lado: colecciones de citas, Bartleby, el Jargon File, los `.signature` de Usenet. La frase es huérfana y circula igual.
3. **La traducción también es un problema** — «one-way street» acá es «calle de mano única». Detalle menor que sirve: la metáfora depende de una señal de tránsito, y las señales de tránsito son promesas de terceros.
4. **Qué dice la frase, en serio** — la flecha pintada en el asfalto es un contrato, no una ley física. El buen programador desconfía del contrato sin dejar de usarlo.
5. **El catálogo de calles de mano única** — el valor que «nunca» es nulo, el campo que «siempre» viene bien formado, el `switch` exhaustivo, el orden de llegada garantizado, la API que «no falla», el reloj monótono, la migración irreversible. Cada una con su patología.
6. **El costo de mirar** — mirar para los dos lados no es gratis: paranoia, código defensivo, ruido. El buen programador no mira siempre todo; sabe qué flechas son concreto y cuáles son pintura fresca.
7. **Vos también pintás flechas** — la mitad incómoda: cada contrato que documentás es una calle de mano única para el que venga después.
8. **Cierre meta** — aplicar la cita a la cita misma. Cross-links a [[K-23]] y [[J-03]].

**Bibliografía:**

_La cita no tiene fuente primaria localizable (rastreo 2026-07-16). Lo único que existe son sitios agregadores de citas que la reproducen sin decir de dónde salió. Se listan como evidencia del fenómeno, no como fuente que respalde la atribución._

- [Goodreads — cita atribuida a Doug Linder](https://www.goodreads.com/quotes/8899857-a-good-programmer-is-someone-who-always-looks-both-ways) — el propio sitio aclara que las citas «are added by the Goodreads community and are not verified». Sin fuente primaria. **frágil (sin fuente primaria).**
- [QuoteFancy](https://quotefancy.com/quote/1716739/Doug-Linder-A-good-programmer-is-someone-who-always-looks-both-ways-before-crossing-a-one), [AZQuotes](https://www.azquotes.com/quote/669637), [defprogramming](https://www.defprogramming.com/quotes-by/doug-linder/), [TheySaidSo](https://theysaidso.com/quote/doug-linder-a-good-programmer-is-someone-who-always-looks-both-ways-before-cross) — agregadores; todos repiten nombre + frase sin fecha ni fuente. **frágil (sin fuente primaria).**
- IEEE Computer Society (cuenta oficial en X, 2025) la difundió atribuyéndola a «Doug Linder, computer scientist» — pero el rótulo «computer scientist» tampoco viene con ninguna fuente; parece heredado de los agregadores. Que una institución seria la reproduzca no la vuelve verificable. **frágil.**
- **The Jargon File** (URL canónica http://catb.org/jargon/) — candidato **descartado**: se descargó el texto completo (versión 2.1.1 y el glosario actual) y se buscó «one-way street», «looks both ways» y «Linder»: cero coincidencias. La frase **no está** en el Jargon File. **estable** (ausencia verificada 2026-07-16).
- **Bartleby.com** (https://www.bartleby.com/) — candidato **descartado**: la búsqueda no encontró la cita en el sitio. **frágil** (ausencia, no hay entrada localizable).
- **Quote Investigator** (https://quoteinvestigator.com/) — el sitio dedicado a rastrear orígenes de citas **no tiene ninguna investigación** sobre esta frase (búsqueda «Nothing found»). Ni el sitio que existe para esto la ha rastreado. **estable** (ausencia verificada).
- **Douglas O. Linder** — [Wikipedia](https://en.wikipedia.org/wiki/Doug_Linder): el único «Doug Linder» público e identificable es un profesor de Derecho de la Universidad de Missouri–Kansas City, creador del sitio *Famous Trials*. Nada lo vincula con la programación ni con esta frase; casi con certeza es coincidencia de apellido, no el autor. **estable.**
- [[E-25]] Jargon File (post propio sobre el tema)

**Imágenes:** _a definir_

**Tags propuestos:** `['cita','Doug Linder','programador','risk','nerd lateral']`

**Estado actual:** seed cosechado de `draft-rest.md` el 2026-04-09. El 2026-07-15 se le construyó el outline (8 puntos) y se escribió el borrador de prosa completo (~1750 palabras) al final del archivo.

Lo que quedó **escrito y cerrado**: el encuadre de la cita, la sección sobre la traducción rioplatense, el catálogo de «calles de mano única» en programación (nulos, formatos, exhaustividad, orden de llegada, APIs que no fallan, relojes, migraciones), la sección sobre el costo de mirar, el giro de «vos también pintás flechas» y el cierre meta. Todo eso es argumentación técnica y no depende de datos externos.

Lo que quedó como **hueco (necesita a César)** — 7 marcadores:

1. Dónde y cuándo vio la frase por primera vez.
2. Si tuvo `.signature` con citas y cuáles rotaba.
3. Un caso concreto de «esto nunca puede pasar» que pasó (bug real).
4. Un caso del sector público (STG / Min. Cultura Santa Fe) donde el dato garantizado por contrato no cumplía.
5. Su regla personal para decidir cuándo validar y cuándo confiar.
6. Alguna vez que él pintó la flecha: un contrato que documentó como garantizado y no lo era.
7. Postura sobre `assert` vs. validación en producción.

Lo que quedó como **`[VERIFICAR:]`** — 7 marcadores. Los importantes:

- **La atribución es el tema del post, no un detalle a resolver.** La bibliografía dice explícitamente «origen incierto». El borrador **no afirma en ningún momento** quién es Doug Linder, en qué año dijo la frase, ni de qué colección salió: todo eso queda marcado. Si el rastreo previo a publicar encuentra algo firme, la sección 2 se reescribe con el dato; si no encuentra nada, la sección 2 funciona igual (mejor, incluso) contando el fracaso del rastreo.
- Falta chequear: la redacción textual en inglés de la frase, si Bartleby.com efectivamente la lista y bajo qué entrada, si aparece en el Jargon File (ver [[E-25]]), y si existe una persona pública identificable llamada Doug Linder asociada a la cita.
- El Hook del draft dice «Vamos a ver de dónde sale» — **esa promesa probablemente no se pueda cumplir**. La prosa la reformula: el post cuenta la búsqueda y su fracaso, no el hallazgo. Si César quiere sostener el Hook original, hace falta investigación real primero.
- Nada de lo que circula por memoria sobre el origen de la frase (foros, listas de citas de programación, atribuciones cruzadas) entró al texto: no está en la bibliografía.

El 2026-07-16 se investigó la atribución de la cita; ver nota. **Hallazgo:** la frase es huérfana — no existe fuente primaria localizable. Está atribuida a «Doug Linder» sólo en sitios agregadores (Goodreads, QuoteFancy, AZQuotes, defprogramming, TheySaidSo, e incluso un tuit de IEEE Computer Society), ninguno con fecha ni fuente; no aparece en el Jargon File (verificado descargando el texto), no aparece en Bartleby, y Quote Investigator no la ha investigado. El único «Doug Linder» público identificable es un profesor de Derecho (UMKC, *Famous Trials*) sin relación con la programación: casi con seguridad una coincidencia de apellido, no el autor. Es decir: el «probablemente» del Hook queda confirmado como la lectura correcta, y la premisa del post (cita perfecta sin autor comprobable) se sostiene. Se rehízo la bibliografía en consecuencia y **se resolvieron 6 de 7 marcadores `[VERIFICAR:]`**; queda sin resolver el de la «quote file» del MIT (no se halló ninguna fuente que confirme que sea una cosa concreta y rastreable — se deja el marcador verbatim).

Antes de publicar: completar los 7 huecos (necesitan a César) y decidir imágenes (siguen `_a definir_`).

---

## Borrador de prosa

> ⚠️ **Curiosidad nerd lateral — esto no es ciencia de la computación**

«A good programmer is someone who always looks both ways before crossing a one-way street.» Un buen programador es alguien que siempre mira para los dos lados antes de cruzar una calle de una sola mano. La frase es perfecta: dice todo lo que tiene que decir en catorce palabras, tiene el chiste adentro, y el chiste es también el argumento. Se la suele atribuir a un tal Doug Linder.

Probablemente.

Y ese «probablemente» resultó ser, para mi sorpresa, la parte más interesante del asunto. Yo quería escribir un post sobre lo que la frase significa. Terminé escribiendo dos: uno sobre la frase, y otro —más corto, más incómodo— sobre el hecho de que nadie parece saber de dónde salió.

### ¿Quién es Doug Linder?

No lo sé. Y todo indica que el resto tampoco.

El nombre viene pegado a la cita como si fuera obvio, con esa naturalidad de las cosas que se repiten mucho. Aparece en listas de citas de programación, en firmas de mails, en slides de charlas, en el pie de páginas de proyectos. Siempre igual, siempre sin fecha, siempre sin fuente. Nunca «Doug Linder, en tal libro, página tal». Nunca «Doug Linder, entrevistado en tal revista». Solamente el nombre, colgado de la frase como una etiqueta de precio.

Busqué. El único «Doug Linder» público e identificable que aparece es Douglas O. Linder, profesor de Derecho en la Universidad de Missouri–Kansas City y autor del monumental sitio *Famous Trials*. Su biografía no menciona la programación por ningún lado, y nada —salvo el apellido— lo conecta con esta frase: casi con certeza es una coincidencia de nombre, no el autor[^identidad]. Dicho de otro modo: no hay ningún programador público identificable llamado Doug Linder al que rastrear la cita.

Los lugares donde uno esperaría encontrarla no ayudan demasiado. Bartleby.com, que es de las colecciones de citas más viejas de la web, es candidato natural[^bartleby]. El Jargon File —el diccionario de la cultura hacker que ya me da para un post entero ([[E-25]])— es otro candidato, porque históricamente fue el lugar donde el folklore del gremio se depositaba y quedaba[^jargon]. También circula la idea de que salió de alguna *quote file* del MIT, esos archivos de citas que se acumulaban en máquinas compartidas y que la gente leía por el placer de leerlas.

Busqué en Bartleby y la cita no está: no aparece ni bajo «Linder» ni bajo el texto de la frase.

El Jargon File tampoco: descargué el texto completo (la vieja versión 2.1.1 y el glosario actual en catb.org) y busqué «one-way street», «looks both ways» y «Linder». Cero resultados. La frase no está ahí, contra lo que sugeriría la memoria.

[VERIFICAR: la existencia y el contenido de la «quote file» del MIT mencionada en la bibliografía del draft — si es una cosa concreta y rastreable o una leyenda de segunda mano.]

La redacción más difundida —la que reproducen Goodreads, QuoteFancy y AZQuotes— es «A good programmer is someone who always looks both ways before crossing a one-way street». Circula también una variante sin el «always» («a good programmer is someone who looks both ways…»); fijo la primera como canónica por ser la mayoritaria.

Lo que sí puedo decirte, sin verificar nada, es cómo viajan estas frases. Alguien la escribe en algún lado. Otro la pone en su `.signature` —ese bloque de cuatro líneas al pie de cada mail y cada posteo de Usenet, que era el único espacio de expresión personal que te daba el protocolo—. De ahí salta a un archivo de citas. De ahí a una lista de «las 50 mejores frases sobre programación». Y para cuando llega a una slide, el nombre ya viene soldado a la frase y nadie recuerda quién soldó a quién.

> 🕳️ **HUECO — necesita a César:** ¿Dónde y cuándo viste vos esta frase por primera vez? (¿un `.signature`, un libro, una charla, un canal de IRC?)

> 🕳️ **HUECO — necesita a César:** ¿Tuviste `.signature` con citas rotativas en tu época de Usenet/mailing lists? ¿Cuáles usabas?

### Un paréntesis de traducción

Acá una calle de una sola vía es una calle de mano única. «De una mano», directamente. Y la traducción importa un poquito más de lo que parece, porque la metáfora entera se apoya en una señal de tránsito.

La flecha pintada en el asfalto no es una ley de la física. Es una convención, sostenida por un municipio, respetada por la mayoría de la gente la mayor parte del tiempo. La flecha no impide que un auto venga de contramano: solamente hace que sea *ilegal* que venga de contramano. Y si el auto viene igual, la ilegalidad no te salva. Te atropella un auto que no tenía derecho a estar ahí, y estás igual de atropellado.

Eso es la frase entera, en realidad. Todo lo demás son ejemplos.

### El catálogo de calles de mano única

Tu trabajo está lleno de flechas pintadas en el asfalto. Van algunas:

**El valor que nunca es nulo.** El campo está declarado no-nulo. La base tiene la restricción. La documentación lo dice. Y sin embargo ahí está, en el log de producción, a las tres de la mañana. Vino por una migración vieja, por un `INSERT` hecho a mano en un incidente anterior, por un import que corrió con las validaciones apagadas «solo por esta vez».

**El campo que siempre viene bien formado.** El proveedor te garantiza que el CUIT viene con once dígitos, sin guiones. Y viene con once dígitos sin guiones durante cuatro años. Hasta que del otro lado cambian de sistema, o entra un operador nuevo, o alguien exporta desde una planilla y el cero de la izquierda se evapora.

**El `switch` exhaustivo.** Cubriste todos los casos del enum. Todos. El `default` tiene un comentario que dice «no puede pasar». Y un día alguien agrega un valor al enum, y ese `default` que no podía pasar se convierte en el camino que toma el 3% de tu tráfico, en silencio, sin romper nada visible durante meses.

**El orden de llegada.** Los mensajes llegan en orden. Salvo que haya reintentos. O dos consumidores. O un reparto entre particiones que alguien tocó para mejorar el throughput y no avisó.

**La API que no falla.** El endpoint interno «siempre responde». Es del equipo de al lado, está en la misma red, tiene tres nueves de disponibilidad. Tres nueves son ocho horas y media por año de calle de contramano.

**El reloj.** El tiempo avanza para adelante. Salvo cuando el NTP corrige un salto, o la VM se suspende, o el horario cambia, o dos máquinas del cluster no coinciden en qué hora es y tu lógica de «el más reciente gana» empieza a elegir al más viejo.

**La migración irreversible.** El script de migración es de una sola mano por definición: se corre para adelante y no vuelve. Por eso mismo es la calle donde más caro sale no mirar.

> 🕳️ **HUECO — necesita a César:** ¿Cuál es tu caso favorito de «esto nunca puede pasar» que después pasó? Un bug concreto, con el «nunca» explícito en el código o en la doc.

> 🕳️ **HUECO — necesita a César:** ¿Algún caso en la STG o en el Ministerio de Cultura de Santa Fe donde el dato que otro organismo garantizaba por contrato/convenio no cumplía en la práctica? (Sin nombres propios si no corresponde.)

### El costo de mirar

Ahora la parte que la frase, por ser una frase, no dice.

Mirar para los dos lados no es gratis. Si mirás para los dos lados en *todas* las calles, no llegás nunca a ningún lado. La versión programática de eso es código que valida tres veces lo mismo, que envuelve cada llamada en un `try` que traga la excepción y sigue, que chequea nulos en variables que acaba de crear dos líneas más arriba. Ese código no es prudente: es ruidoso. Y el ruido tiene un costo propio, porque entierra las validaciones que sí importan bajo una pila de validaciones ceremoniales, y hace que el lector deje de distinguir cuál es cuál.

Un colega que valida todo por igual me está diciendo, en el fondo, que no sabe qué puede fallar. La paranoia uniforme es indistinguible de la ignorancia.

Así que la frase, leída literalmente, es mala. Leída bien, dice otra cosa: el buen programador es el que sabe **cuáles** flechas son concreto y cuáles son pintura fresca. Sabe que el tipo de dato que le da el compilador es concreto, y que el comentario que dice «ordenado por fecha» es pintura. Sabe que el `NOT NULL` de la base es concreto, y que el `NOT NULL` del docstring es pintura. Esa clasificación no está escrita en ningún lado, no la da ninguna herramienta, y es —creo yo— la mayor parte de lo que llamamos experiencia.

> 🕳️ **HUECO — necesita a César:** ¿Cuál es tu regla propia para decidir cuándo validar y cuándo confiar? Aunque sea una heurística sucia de una frase.

> 🕳️ **HUECO — necesita a César:** ¿Sos de poner `assert` o de validar y manejar el error en producción? ¿Cambió tu postura con los años?

### Vos también pintás flechas

Y ahora la mitad incómoda, que es la que casi nunca se comenta cuando se cita la frase.

La frase te pone siempre en el rol del peatón. Prudente, atento, sobreviviente. Pero vos también sos el municipio. Cada vez que escribís «este método nunca devuelve nulo», cada vez que documentás un formato, cada vez que declarás una precondición, estás pintando una flecha en el asfalto para alguien que va a cruzar dentro de tres años y que no te va a poder preguntar nada.

La pregunta honesta no es cuántas veces te mintió una flecha ajena. Es cuántas veces mintió una tuya. Yo diría que el número no es cero para nadie que haya escrito software más de un rato.

> 🕳️ **HUECO — necesita a César:** ¿Te acordás de una flecha que hayas pintado vos? Un contrato que documentaste como garantizado y que después no era cierto, y qué pasó cuando alguien lo cruzó confiando.

### Cierre

Así que tenemos una frase sin autor comprobable sobre la conveniencia de desconfiar de las garantías nominales. Que es, hay que decirlo, bastante gracioso.

La cita viene con una flecha pintada al lado: «Doug Linder». La flecha dice que hay un autor, que ese autor es él, que alguien lo verificó alguna vez. Y yo la crucé sin mirar durante años, como todo el mundo, porque la frase es buena y el nombre no molestaba. Recién cuando me senté a escribir esto miré para el otro lado, y del otro lado no venía nada. Ni un auto. Ni una fuente. Nada.

No es un motivo para dejar de usarla. Las frases huérfanas también sirven; el gremio está lleno de sabiduría anónima que funciona igual sin apellido, y el Jargon File es prueba de eso ([[E-25]]). Pero sí es un motivo para citarla como corresponde: «una frase que se le atribuye a Doug Linder», con el «se le atribuye» adentro, que es exactamente el tipo de precaución que la frase misma recomienda.

Mirá para los dos lados antes de cruzar una calle de mano única. Incluso —sobre todo— cuando la calle es una cita. Sobre citas que resultan ser menos firmes de lo que parecen tengo más para decir en [[K-23]], y sobre el género «el nombre viaja más lejos que la fuente» hay un caso extremo en [[J-03]].

[^bartleby]: Bartleby.com — colección de citas y textos de referencia en línea (<https://www.bartleby.com/>). La búsqueda del 2026-07-16 **no encontró** esta cita en el sitio; frágil como fuente, no hay entrada localizable.

[^jargon]: The Jargon File — diccionario de la cultura hacker, en su URL canónica <http://catb.org/jargon/>. Verificado el 2026-07-16 descargando el texto completo (versión 2.1.1 y glosario actual): la frase **no aparece** en ninguna de las dos. Estable.

[^identidad]: El único Doug Linder público e identificable es Douglas O. Linder, profesor de Derecho en la Universidad de Missouri–Kansas City y creador del sitio *Famous Trials* — ver [Wikipedia](https://en.wikipedia.org/wiki/Doug_Linder). No hay conexión con la programación; la coincidencia es sólo de apellido. Estable.
