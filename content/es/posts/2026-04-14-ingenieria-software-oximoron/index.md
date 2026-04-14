---
layout: post
title: '¿El término "Ingeniería de software" es un oxímoron?'
description: 'La pregunta que Alan Kay dejó en el apéndice de un manual en 2002.'
featured_image: hero-alan-kay.jpg
tags: ['filosofia', 'Alan Kay', 'ingenieria alternativa', 'OOPSLA', 'profesion', 'Dijkstra']
---

Ingeniería. Ingeniero. _Engine_. Máquina. Vamos a hacer una pregunta tonta y peligrosa: ¿qué máquina construye un ingeniero de software? Si te sale rápido, sospechá. Yo llevo treinta años metido en el software y todavía no tengo una respuesta que me convenza.[^img_kay]

Lo interesante no es que la pregunta sea difícil. Lo interesante es que la pregunta no la inventó un crítico externo de la disciplina, ni un filósofo decidido a molestar, ni un estudiante con ganas de quedar bien en un seminario. La escribió Alan Kay, el tipo que acuñó _object-oriented_, en un apéndice de un manual técnico que casi nadie lee. La dejó ahí, como quien deja una bomba en el cajón de una mesa de luz, y siguió escribiendo software.

## Las ingenierías clásicas se organizan alrededor de una máquina

El sustantivo _ingeniería_ se siente robusto porque evoca algo muy específico. Las ingenierías que le dieron al nombre su prestigio —la civil, la mecánica, la eléctrica, la química— están todas organizadas alrededor de un objeto físico. El ingeniero civil diseña y supervisa la construcción de un puente: el puente es la cosa. El ingeniero mecánico diseña un motor, una caja reductora, una prensa: el motor es la cosa. El ingeniero eléctrico diseña una red de distribución, un transformador, un circuito: el circuito es la cosa.

Ese objeto físico cumple una función doble. Por un lado, ancla el vocabulario técnico: cuando dos ingenieros civiles discuten sobre momentos flectores, los dos están pensando en el mismo puente. Por otro lado, ancla la responsabilidad civil. Si el puente se cae, hay un colegio profesional, una matrícula, una firma en un plano y un juicio posible. La palabra _ingeniero_, en las disciplinas clásicas, no es un adjetivo que se agrega al currículum: es un contrato con la sociedad que tiene consecuencias jurídicas. La etimología no está de adorno: _engineer_ viene de _engine_, y _engine_ es esa máquina concreta que alguien firmó y que puede matarte si la firmó mal.

## Las "ingenierías alternativas"

Con esa imagen en la cabeza, la lista de disciplinas que usan la palabra _ingeniería_ con un adjetivo adelante se vuelve divertida. Ingeniería industrial, ingeniería ambiental, ingeniería financiera, ingeniería social. Y, por supuesto, _ingeniería de software_. El patrón es el mismo que en las "medicinas alternativas": el adjetivo cambia el sustantivo sin pedir permiso. Medicina china, medicina ayurvédica, medicina basada en ondas cósmicas. _Medicina_ hace el trabajo pesado — importa el prestigio — y el adjetivo pone la condición.

No estoy acusando a nadie de impostor. La ingeniería industrial tiene su historia y su cuerpo de conocimiento. La ingeniería financiera modela cosas que valen la pena modelar. Lo que pasa es que, cuando se comparan con las clásicas, a todas les falta _la máquina_: el objeto físico que ancla el vocabulario y la responsabilidad. Un ingeniero financiero no firma un puente. Un ingeniero industrial firma procesos, que son invisibles hasta que fallan y nadie sabe bien quién los firmó. Y un ingeniero de software firma… ¿qué, exactamente?

Una respuesta honesta empieza por reconocer que cuando le ponemos el adjetivo _alternativa_ a la palabra _ingeniería_, estamos pidiéndole al sustantivo que nos preste el prestigio sin pagar los costos. Y eso, como todo préstamo no pagado, genera deuda.

## La pregunta que dejó Alan Kay en 2002

En octubre de 2002, Alan Kay publicó el borrador 0.1 del manual de Croquet, un sistema de colaboración 3D hecho sobre Squeak que casi no sobrevivió a su propio entusiasmo.[^croquet] El manual tenía un apéndice B titulado, literalmente, _Is "Software Engineering" an Oxymoron?_.[^kay-croquet] No era un ensayo independiente: era una reflexión dentro de un documento técnico, escondida al final.

La pregunta de Kay es honesta, no retórica. No dice "la ingeniería de software es una farsa". Dice algo más sutil: si tomamos en serio la etimología —_engineer_ viene de _engine_— y miramos lo que construye nuestra disciplina, ¿a cuál objeto le estamos poniendo nuestra firma?

Importa que la pregunta la escriba Kay y no un crítico externo. Kay no está afuera tirando piedras. Kay es uno de los que fundó la disciplina: Sketchpad de Sutherland estaba en su genealogía, Smalltalk fue su criatura, el Dynabook fue su visión, el PARC fue su casa. El mismo tipo había dicho cinco años antes, en OOPSLA 1997, en una keynote titulada _The Computer Revolution Hasn't Happened Yet_.[^kay-oopsla] Cuando alguien con ese currículum, con cuarenta años de ver a la disciplina desde adentro, pregunta si el nombre con que la bautizamos es un oxímoron, no está despreciando el campo: está preocupado. La preocupación honesta del que labura en algo y no ve cerrar la ecuación.

## Tres respuestas que circulan

**"El software _es_ la máquina."** La más directa: ¿qué máquina construye un ingeniero de software? El programa mismo. El código es la máquina, ejecutándose sobre una CPU genérica. El problema con esta respuesta es la indirección. Lo que el desarrollador escribe no es la máquina: es una receta para una receta. El compilador (o el intérprete, o el JIT) decide cómo transformar el código fuente en instrucciones reales para una CPU concreta, sobre un sistema operativo concreto, sobre un kernel que puede interrumpir el proceso en cualquier instante. El plano del ingeniero civil _es_ el puente que se construye; el código del desarrollador está a tres o cuatro capas de la cosa que efectivamente corre. Y la cosa que corre se modifica todos los martes — no hay un _as-built_ que certificar, porque nunca termina de construirse.

**"Ingeniería es aplicar conocimiento científico a un problema práctico."** Esta es la posición de Mary Shaw en su artículo de 1990:[^shaw] el software ya tiene ciencia (teoría de computabilidad, lógica, análisis de algoritmos), ya tiene práctica (sistemas que funcionan), y por lo tanto tiene derecho a llamarse ingeniería. Es una respuesta defendible y sofisticada. Pero es blanda: pierde el lado de _responsabilidad civil_ de la palabra. Un farmacéutico también aplica conocimiento científico a un problema práctico, y no por eso se llama ingeniero farmacéutico. La ciencia-aplicada-a-problemas-prácticos es condición necesaria, no suficiente.

**"El software es matemática aplicada."** Esta es, aproximadamente, la posición de Dijkstra, visible en los EWD y especialmente en EWD 1305, _Answers to questions from students of Software Engineering_.[^ewd1305] Para Dijkstra el problema no era la ingeniería en sí: era pretender hacerla con el rigor rebajado del apuro comercial. Su propuesta implícita era abandonar la palabra _ingeniería_ y aceptar que el software es una rama de la matemática aplicada. Es la respuesta más honesta de las tres: acepta el oxímoron y lo resuelve renunciando al sustantivo equivocado. También es la menos popular, porque nadie quiere poner "matemático aplicado" en LinkedIn.

## Por qué no es un debate académico

Uno podría pensar que todo esto es filosofía de café, y en parte lo es. Pero tiene consecuencias prácticas. Las ingenierías clásicas tienen códigos de ética profesional ligados a colegios que pueden expulsarte, matrícula obligatoria para firmar ciertos trabajos, responsabilidad civil objetiva, seguro obligatorio, y controles previos a la habilitación. Ninguna de esas cosas existe, en sentido fuerte, para el software.

El _Software Engineering Code of Ethics_ de ACM/IEEE-CS, publicado en 1999,[^ethics] es un documento valioso, pero no tiene fuerza vinculante: nadie pierde la matrícula por violarlo, porque en la inmensa mayoría de las jurisdicciones no hay matrícula que perder. Hubo intentos de regular la profesión, y todos terminaron diluidos. Texas ofreció entre 2013 y 2019 una licencia PE específica para _Software Engineering_; NCEES la discontinuó por falta de candidatos —en cinco administraciones del examen se anotaron 81 personas en total—.[^texas-pe] Alberta, que sí restringía el uso del título _software engineer_ por la ley de su colegio profesional, perdió en noviembre de 2023 una causa contra Getty Images y Jobber; en julio de 2024 la legislatura provincial sacó el título de la ley regulada.[^alberta-pe] El intento siempre choca con la misma pregunta: ¿cuál es exactamente el software que debe regularse? ¿El código de la computadora del auto? ¿El de la tablet? ¿El del sitio de comidas a domicilio?

Tom DeMarco —coautor de _Peopleware_, autor del libro de métricas _Controlling Software Projects_ (1982)— publicó en IEEE Software en 2009 un texto donde se renuncia a sí mismo.[^demarco] El DeMarco joven había escrito la frase más citada del campo, _"You can't control what you can't measure"_; el DeMarco de 2009 corre el dial de la incomodidad un click más allá. La conclusión no es "medí lo correcto" —ese sería el consejo blando—, es algo peor: el reflejo de control te _selecciona_ los proyectos equivocados, los de bajo retorno donde efectivamente se puede medir y controlar todo. Los proyectos que valen la pena —los que cambian el negocio, los que transforman a una empresa— son por definición experimentales: su construcción tal vez no, pero su concepción sí. La distinción que cierra el artículo es la que más sirve acá: una cosa es _to engineer software_ (verbo), que tiene todo el sentido del mundo; otra cosa es _software engineering_ (sustantivo), que terminó denotando un combo específico —procesos definidos, walkthroughs, matrices de trazabilidad, métricas, planificación rigurosa, estándares de código— que persigue consistencia y predictibilidad. Que el autor del libro de métricas más influyente firme esa renuncia es lo que le da peso.

Mientras tanto, en los contratos seguimos firmando "Ingeniero de Software" y en las licencias del producto seguimos repartiendo "AS IS, WITHOUT WARRANTY OF ANY KIND". El sustantivo de la portada dice una cosa, la letra chica dice exactamente la opuesta. En ninguna otra ingeniería pasa eso.

## Una aspiración, no una credencial

En 2021, en GOTO, Kay volvió sobre el asunto con una charla titulada _Aspiring to Learn The Engineering of Software_.[^kay-goto] El título es cuidadoso: _aspiring to learn_. No dice que el software ya sea una ingeniería. No dice que no vaya a serlo nunca. Dice algo más útil: es una aspiración. Hay prácticas —el testing sistemático, la verificación formal, la disciplina del diseño, la honestidad con las trade-offs— que se parecen más al trabajo del ingeniero civil que a la improvisación del artista. Y hay prácticas —firmar antes de pensar, copiar de Stack Overflow a ciegas, desplegar porque la consola da verde— que no se parecen a ninguna disciplina.

La posición que me quedó después de treinta años de hacer esto es modesta. _Ingeniería de software_ no es un oxímoron, pero tampoco es todavía una descripción: es una aspiración. Sigo escribiendo software, sigo firmando contratos que usan la palabra _ingeniero_, y sigo poniendo "desarrollador" en el CV cuando tengo que ser honesto. Voy a poner _ingeniero_ en el CV con todas las letras el día que encuentre la máquina que estoy firmando. Kay no la encontró en cuarenta años. ¿Qué podría pretender yo en treinta? Por ahora aspiro a aprender la ingeniería del software, como dice el título de su charla, y tomo _ingeniería_ como objetivo, no como credencial.

[^croquet]: [Croquet Project](https://en.wikipedia.org/wiki/Croquet_Project) en Wikipedia — contexto del sistema 3D colaborativo donde apareció el apéndice.

[^kay-croquet]: Alan Kay et al., _Croquet: The User Manual_, draft 0.1, octubre 2002. Apéndice B: _Is "Software Engineering" an Oxymoron?_. [Copia en Wayback Machine](http://web.archive.org/web/20030407181600/www.opencroquet.org/downloads/Croquet0.1.pdf).

[^kay-oopsla]: Alan Kay, [_The Computer Revolution Hasn't Happened Yet_](https://www.youtube.com/watch?v=oKg1hTOQXoY), keynote en OOPSLA 1997.

[^shaw]: Mary Shaw, [_Prospects for an Engineering Discipline of Software_ (PDF)](https://people.cs.vt.edu/~kafura/CS6604/Papers/Prospects-Engineering-Discipline-Software.pdf), IEEE Software vol 7 n.º 6, noviembre 1990, pp. 15–24 — [DOI 10.1109/52.60586](https://doi.org/10.1109/52.60586). Página de [Mary Shaw](https://en.wikipedia.org/wiki/Mary_Shaw_(computer_scientist)) en Wikipedia.

[^ewd1305]: Edsger W Dijkstra, EWD 1305 — _Answers to questions from students of Software Engineering_, Austin, noviembre 2000. [Transcripción HTML](https://www.cs.utexas.edu/~EWD/transcriptions/EWD13xx/EWD1305.html) y [escaneo PDF del manuscrito original](https://www.cs.utexas.edu/~EWD/ewd13xx/EWD1305.PDF) en el archivo EWD de UT Austin.

[^ethics]: [Software Engineering Code of Ethics](https://www.acm.org/code-of-ethics/software-engineering-code) — ACM/IEEE-CS, 1999.

[^texas-pe]: [_NCEES discontinuing PE Software Engineering exam_](https://ncees.org/ncees-discontinuing-pe-software-engineering-exam/) — anuncio oficial de NCEES (2018); el examen se administró por última vez en abril de 2019. Detalle de números bajos en [_NCEES Ends Software Engineering PE Exam_](https://www.nspe.org/career-growth/pe-magazine/may-2018/ncees-ends-software-engineering-pe-exam) (NSPE, mayo 2018) y en la [página de la Texas Board of Professional Engineers](https://pels.texas.gov/software.html).

[^alberta-pe]: [_Court sides with tech companies in 'software engineer' terminology dispute_](https://edmontonjournal.com/news/politics/court-sides-with-tech-companies-in-software-engineer-terminology-dispute) — Edmonton Journal, 11 de noviembre de 2023, sobre el fallo a favor de Getty Images y Jobber. Cierre del caso y enmienda legislativa (Bill 7) en el [comunicado de APEGA del 3 de julio de 2024](https://www.apega.ca/news/2024/07/03/apega-legal-action-concludes-key-clarifications-on-title-protection-provided).

[^demarco]: Tom DeMarco, _Software Engineering: An Idea Whose Time Has Come and Gone?_, IEEE Software, vol 26 n.º 4, julio-agosto 2009, pp. 95–96 (editorial corto). [DOI 10.1109/MS.2009.101](https://doi.org/10.1109/MS.2009.101) — [copia en PDF](https://www.cs.uni.edu/~wallingf/teaching/172/resources/demarco-on-se.pdf) en una página de curso de la University of Northern Iowa. [Comentario en InfoQ](https://www.infoq.com/news/2009/08/demarco-software-engineering-/) que reproduce los pasajes clave.

[^kay-goto]: Alan Kay, [_Aspiring to Learn The Engineering of Software_](https://www.youtube.com/watch?v=D43PlUr1x_E), GOTO 2021.

[^img_kay]: Imagen de [Alan Kay and the prototype of Dynabook, pt. 5](https://commons.wikimedia.org/wiki/File:Alan_Kay_and_the_prototype_of_Dynabook,_pt._5_(3010032738).jpg) — CC-BY 2.0 — autor: Marcin Wichary, 5 de noviembre de 2008. Recortada a 2.5:1 para hero landscape.
