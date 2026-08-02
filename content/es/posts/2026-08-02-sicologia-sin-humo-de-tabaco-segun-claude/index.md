---
title: 'Sicología sin humo de tabaco en el trasero, según Claude'
description: 'Le hice a Claude las mismas cuatro preguntas que le había hecho a ChatGPT sobre qué queda de la sicología. Contestó distinto.'
featured_image: hero-claude-logo.jpg
tags: ['IA', 'ChatGPT', 'Claude', 'psicologia', 'crisis de replicacion', 'epistemologia', 'nerd lateral']
---

⚠️ *Curiosidad nerd lateral — esto no es ciencia de la computación. Es el apéndice de otro post.*

Este post es la cola de [«Sicología sin humo de tabaco en el trasero, según ChatGPT»](/posts/sicologia-sin-humo-de-tabaco-segun-chatgpt/). Ahí conté que en octubre de 2025 le hice a ChatGPT cuatro prompts encadenados para que le sacara a la sicología todo concepto sin instrumento, que cumplió las cuatro veces sin discutirme nada.

Al escribir aquel post quedó una pregunta obvia dando vueltas: **¿y si le hago los mismos cuatro prompts a otro modelo?**

Eso es lo que sigue. Mismos prompts, mismo orden, sin tocarles una coma. Las respuestas son de Claude, de Anthropic, del 2 de agosto de 2026, con acceso a búsqueda web para verificar lo que afirmaba.[^img_hero] Van tal como salieron.

**Leé primero la advertencia del final.** Es la parte que hace que esto sirva como evidencia y no como publicidad, y si me la salteás vas a sacar la conclusión equivocada.

## Ronda 1

> **Prompt:** Si eliminamos a Freud y sus discípulos, y a carl Jung y sus discípulos, ¿que queda del aparato de la psicología? No puedes usar a ningún autor que se base en los anteriores

Queda casi toda la psicología que hoy se enseña como ciencia, y por una razón que conviene decir antes que la lista: **nunca vino de ahí**. Wundt monta el laboratorio de Leipzig en 1879, antes de que Freud publicara nada relevante. La psicofísica alemana, el conductismo, la psicometría, la revolución cognitiva y la neuropsicología de lesiones crecieron en paralelo, y varias de ellas explícitamente en contra.

Pero tu regla —«ningún autor que se base en los anteriores»— es más filosa de lo que parece, y es más interesante mirar qué **sí** se lleva puesto:

- **John Bowlby cae.** Era psicoanalista, formado en la Sociedad Psicoanalítica Británica, y construyó la teoría del apego desde adentro de esa tradición, aunque después la peleara con etología y datos. Y el apego es, con Ainsworth y la Situación Extraña, una de las áreas **mejor replicadas** de la psicología del desarrollo. Tu filtro elimina un cuerpo empírico fuerte por su genealogía.
- **Erik Erikson cae** entero, y con él buena parte del vocabulario del desarrollo psicosocial.
- **Carl Rogers cae**, aunque a casi nadie se le ocurre ponerlo en esa lista. Reconocía a Otto Rank —discípulo directo de Freud— como su influencia temprana decisiva, por vía de Jessie Taft y el círculo rankiano de Filadelfia.[^rank]
- Y hay un caso límite del que conviene no abusar: Watson y Skinner **se definieron en contra** del introspeccionismo y del psicoanálisis. Si «basarse en» incluye «reaccionar contra», el filtro se come todo. Yo lo leería en sentido estricto —dependencia teórica positiva, no polémica— y dejaría el conductismo en pie.

Resumen: sobrevive el aparato empírico completo. Lo que se pierde no es sólo «la psicología profunda»: se pierde también una zona con buenos datos, el apego, por parentesco y no por mérito. Eso ya dice algo sobre el filtro.

## Ronda 2

> **Prompt:** Elimina también los conceptos e ideas que no pueden someterse a experimentación basada en neurociencias

Acá te voy a discutir el pedido, porque este filtro no hace lo que parece que hace.

Tiene tres problemas, y son distintos entre sí:

1. **Confunde mecanismo con evidencia.** Que no sepamos por qué circuito funciona un tratamiento no dice nada sobre si funciona. La eficacia clínica se establece con ensayos controlados aleatorizados y medidas de resultado, no con imágenes. Aplicado literalmente, tu filtro borra intervenciones con eficacia demostrada y conserva correlatos anatómicos sin consecuencia clínica.
2. **El dominio de referencia es más estrecho de lo que te conviene.** Lo que pedís —que el concepto produzca resultados contrastables contra estudios de neurociencia— es un buen criterio: exige que la afirmación pueda chocar contra algo que no sea la propia teoría. Mi objeción no es al criterio, es a que **la neurociencia no es el único lugar contra el cual una afirmación puede chocar y perder.** La conducta medida, la psicometría y el ensayo clínico también lo son. Un aprendizaje que se mide en ensayos hasta criterio, una prueba con validez predictiva sobre resultados de vida, un tratamiento que gana o pierde contra placebo: los tres hacen contacto con el mundo y los tres pueden salir mal, sin pasar por el cerebro. Con tu recorte, esas tres cosas caen junto con el arquetipo, y no pertenecen a la misma categoría.
3. **Lo más importante: neurotesteable ≠ testeado con fiabilidad.** La literatura de neuroimagen es, precisamente, una de las que peor sobrevivió a la revisión de la última década. Corrección estadística mal calibrada en los paquetes de análisis estándar;[^eklund] el mismo dataset entregado a setenta equipos independientes que produjeron resultados discrepantes;[^botvinik] cálculos que muestran que los estudios de asociación cerebro-conducta necesitan miles de sujetos, cuando el estudio típico tenía decenas.[^marek] Tu filtro no está seleccionando por dureza. Está seleccionando por **aspecto** de dureza.

Lo que te propongo entonces no es reemplazar tu criterio sino **ampliarle el dominio de referencia y ponerle exigencias de calidad**: que la afirmación se pueda contrastar contra *algún* dominio independiente de la teoría que la postula —neurociencia, conducta, psicometría o clínica—, y que la contrastación se haga con preregistro, potencia estadística adecuada, tamaño de efecto informado y al menos una replicación independiente. Ese filtro es más barato que el tuyo, más duro, y ordena el campo de otra manera: deja adentro cosas conductuales sin neuroimagen y deja afuera cosas con neuroimagen preciosa.

## Ronda 3

> **Prompt:** Ten en cuenta the big Five

Los Big Five aguantan, sí, pero **no por donde vos y yo veníamos mirando**, y ese detalle es el que hace interesante el ejercicio.

Aguantan por razones psicométricas y de genética conductual: la estructura de cinco factores reaparece en muestras grandes y en varios idiomas, los rasgos predicen resultados de vida con validez modesta pero estable, y los estudios de gemelos dan heredabilidades sustanciales. Nada de eso necesita un scanner.

La parte **neuro** de los Big Five —«extraversión ↔ estriado ventral», «neuroticismo ↔ amígdala hiperreactiva»— es justamente la más floja del paquete: son en buena medida estudios de muestra chica, del tipo que la revisión de reproducibilidad de la última década dejó peor parado. Si aplicás tu filtro con rigor, te quedás con lo peor del constructo y tirás lo mejor.

Y un asterisco que hay que poner, porque es reciente y es grande: la estructura de cinco factores **no se sostiene igual fuera del mundo WEIRD**.[^weird] Un trabajo publicado en *Science Advances* en 2019 analizó 29 encuestas cara a cara con casi 95.000 respondentes en 23 países de ingresos bajos y medios y encontró que los ítems habituales no miden lo que dicen medir en esas poblaciones —aunque los mismos ítems administrados por internet, con respondentes autoseleccionados de los mismos países, sí funcionaban.[^laajaj] Eso no destruye el modelo; sí destruye la frase «consistencia intercultural» dicha sin condiciones.

Conclusión que me parece la buena: los Big Five son el mejor ejemplo disponible de un constructo que **pasa el filtro correcto y sería mal juzgado por el tuyo**.

## Ronda 4

> **Prompt:** Indica como la crisis de replicación afecta a este núcleo de psicología que has definido, y compara con cómo afecta a todas las áreas de la psicología que has dejado afuera

Esta es la pregunta que da vuelta el ejercicio, así que la contesto sin adornos: **la crisis no golpeó más fuerte afuera del núcleo que definimos. En varios frentes golpeó más fuerte adentro.**

No te puedo dar una columna de «nivel de evidencia» con emojis. Te puedo dar estudios:

- **El marco general.** El Reproducibility Project de la Open Science Collaboration intentó replicar 100 estudios de tres revistas de primera línea: 97% de los originales tenían resultado significativo, 36% de las réplicas también, y los tamaños de efecto quedaron en la mitad.[^osc]
- **Neuroimagen — el supuesto refugio.** Eklund, Nichols y Knutsson mostraron que la corrección para inferencia por clusters, tal como venía implementada en los paquetes habituales, inflaba los falsos positivos.[^eklund] Botvinik-Nezer y colegas le dieron el mismo dataset a 70 equipos con nueve hipótesis idénticas: no hubo dos equipos que eligieran el mismo pipeline, y las conclusiones variaron.[^botvinik] Marek y colegas calcularon que los estudios de asociación cerebro-conducta necesitan miles de sujetos para ser reproducibles.[^marek]
- **Psicopatología biológica — el peor caso, no el mejor.** Border y colegas examinaron los 18 genes candidatos más estudiados para depresión en muestras grandes y no encontraron soporte para ninguno; concluyen que la literatura previa era en su mayoría falsos positivos.[^border] La revisión paraguas de Moncrieff y colegas no halló evidencia consistente de la asociación entre serotonina y depresión — con la aclaración necesaria de que ese trabajo recibió críticas metodológicas serias en la misma revista, así que no es un veredicto cerrado.[^moncrieff]
- **Cognición experimental.** Sí, *ego depletion* cayó: replicación multi-laboratorio preregistrada, 23 laboratorios, 2.141 participantes, sin efecto.[^hagger] Ese punto de la respuesta anterior está bien.

Y del otro lado, el de las áreas excluidas, hay que hacer una distinción que se suele saltear:

- El psicoanálisis como **teoría** tiene un problema anterior a la replicación: en su mayor parte no generó afirmaciones contrastables, así que no hay nada que replicar. Ojo, que esto no es unánime: Popper lo tomó como su ejemplo canónico de teoría no falsable, pero Grünbaum sostuvo lo contrario —que Freud sí hace afirmaciones contrastables y que el problema es que fallan—.[^popper] La segunda posición es más dura con Freud, no más blanda.
- La terapia **psicodinámica** de hoy es otra cosa y sí se somete a ensayos. Un meta-análisis de equivalencia la encontró comparable a tratamientos con eficacia establecida; recibió una crítica metodológica publicada, y en la respuesta los propios autores conceden que en algunos estudios «igualmente inefectivos» habría sido una descripción más exacta.[^steinert] Ese matiz vale más que cualquier tabla.

La conclusión que saco es incómoda para el ejercicio entero, incluida mi propia respuesta anterior: **usar la neurociencia como dominio de referencia privilegiado no garantiza replicabilidad**. Un estudio de neuroimagen produce números, y los números producen tablas, y las tablas producen convicción — pero un estudio con veinticinco sujetos y veinte grados de libertad en el pipeline de análisis es menos reproducible que un cuestionario de personalidad bien validado, por más caro que haya sido el equipo. Tu criterio era correcto en la forma —pedir contrastabilidad— y quedó corto en el alcance.

## La advertencia, que es la parte importante

Esto **no prueba que un modelo sea mejor que otro**, y si el post se leyera así estaría haciendo exactamente lo que critica.

Tres razones, y conviene dejarlas escritas:

**El contexto no era el mismo.** Los prompts de octubre de 2025 se hicieron en una conversación normal, sin pedirle a nadie que discutiera nada. Estas respuestas se escribieron dentro de un pedido que ya buscaba el contraste, sabiendo que el desacuerdo era el producto. Es una ventaja enorme y no es mérito.

**Hubo acceso a verificar.** Cada estudio citado acá se buscó y se abrió. Un modelo contestando de memoria, sin herramientas, no está jugando el mismo juego — y la conversación original fue exactamente eso.

**El modo de falla no desaparece; cambia de forma.** Un modelo que discute la premisa puede equivocarse con la misma seguridad con la que el otro asentía, y suena todavía más convincente porque suena crítico. La confianza calibrada de mentira se puede simular igual de bien en tono escéptico que en tono complaciente.

Dicho de otro modo: la diferencia visible entre las dos columnas no es «un modelo honesto contra uno adulón». Es **lo que pasa cuando alguien pide acuerdo contra lo que pasa cuando alguien pide pelea**. Los dos resultados son, en buena medida, lo que se pidió.

Si algo hay que llevarse de los dos posts, es que el que verifica sigue siendo el lector.

[^img_hero]: Símbolo de Claude, [`Claude AI symbol.svg`](https://commons.wikimedia.org/wiki/File:Claude_AI_symbol.svg) — obra de Anthropic, liberada bajo [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.es) (dedicación al dominio público), vía Wikimedia Commons. Compuesto sobre fondo liso en formato 2.5:1 para el hero, igual que el logotipo del post hermano.
[^rank]: Roy José deCarvalho, [«Otto Rank, the Rankian circle in Philadelphia, and the origins of Carl Rogers' person-centered psychotherapy»](https://pubmed.ncbi.nlm.nih.gov/11623737/), *History of Psychology* 2(2):132-148, 1999.
[^eklund]: Anders Eklund, Thomas E. Nichols y Hans Knutsson, [«Cluster failure: Why fMRI inferences for spatial extent have inflated false-positive rates»](https://www.pnas.org/doi/10.1073/pnas.1602413113), *PNAS* 113(28):7900-7905, 2016. Corresponde leerlo junto con [la corrección publicada](https://www.pnas.org/doi/10.1073/pnas.1612033113) y [la re-evaluación posterior](https://www.pnas.org/doi/10.1073/pnas.1614502114).
[^botvinik]: Rotem Botvinik-Nezer et al., [«Variability in the analysis of a single neuroimaging dataset by many teams»](https://www.nature.com/articles/s41586-020-2314-9), *Nature* 582(7810):84-88, 2020.
[^marek]: Scott Marek et al., «Reproducible brain-wide association studies require thousands of individuals», *Nature* 603(7902):654-660, 2022, DOI [10.1038/s41586-022-04492-9](https://doi.org/10.1038/s41586-022-04492-9).
[^osc]: Open Science Collaboration, [«Estimating the reproducibility of psychological science»](https://doi.org/10.1126/science.aac4716), *Science* 349(6251):aac4716, 2015.
[^border]: Richard Border et al., [«No Support for Historical Candidate Gene or Candidate Gene-by-Interaction Hypotheses for Major Depression Across Multiple Large Samples»](https://doi.org/10.1176/appi.ajp.2018.18070881), *American Journal of Psychiatry* 176(5):376-387, 2019.
[^moncrieff]: Joanna Moncrieff et al., [«The serotonin theory of depression: a systematic umbrella review of the evidence»](https://pubmed.ncbi.nlm.nih.gov/35854107/), *Molecular Psychiatry*, 2022. Las críticas: [réplica en la misma revista](https://www.nature.com/articles/s41380-023-02093-0) y [respuesta del King's College London](https://www.kcl.ac.uk/news/a-response-to-the-serotonin-theory-of-depression-a-systematic-umbrella-review-of-the-evidence).
[^hagger]: Martin S. Hagger et al., [«A Multilab Preregistered Replication of the Ego-Depletion Effect»](https://journals.sagepub.com/doi/10.1177/1745691616652873), *Perspectives on Psychological Science* 11(4):546-573, 2016.
[^weird]: *Nota del editor, no de la respuesta original.* **WEIRD** es el acrónimo de *Western, Educated, Industrialized, Rich, Democratic*, acuñado por Joseph Henrich, Steven J. Heine y Ara Norenzayan en [«The weirdest people in the world?»](https://henrich.fas.harvard.edu/publications/weirdest-people-world), *Behavioral and Brain Sciences* 33(2-3):61-83, 2010. Mostraron que el 96% de los sujetos de la investigación psicológica salía de países occidentales industrializados —el 68% sólo de Estados Unidos— y en buena medida de estudiantes universitarios; y que esas poblaciones, lejos de ser un punto de partida neutro, están en el extremo de la distribución en muchas medidas. De ahí el juego de palabras del título: el sujeto más estudiado es también el más raro.
[^laajaj]: Rachid Laajaj et al., [«Challenges to capture the big five personality traits in non-WEIRD populations»](https://doi.org/10.1126/sciadv.aaw5226), *Science Advances* 5(7):eaaw5226, 2019. [Texto libre en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6620089/).
[^popper]: Karl Popper, *Conjectures and Refutations: The Growth of Scientific Knowledge*, Routledge & Kegan Paul, Londres, 1963, y Adolf Grünbaum, *The Foundations of Psychoanalysis: A Philosophical Critique*, University of California Press, Berkeley, 1984.
[^steinert]: Christiane Steinert et al., [«Psychodynamic Therapy: As Efficacious as Other Empirically Supported Treatments?»](https://doi.org/10.1176/appi.ajp.2017.17010057), *American Journal of Psychiatry* 174(10):943-953, 2017, y la [respuesta a Cristea et al.](https://psychiatryonline.org/doi/10.1176/appi.ajp.2017.17050592r) en la misma revista.
