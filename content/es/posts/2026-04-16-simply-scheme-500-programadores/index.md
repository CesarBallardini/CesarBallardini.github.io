---
layout: post
title: 'Simply Scheme: el libro que no quería 500 programadores mediocres'
description: 'Brian Harvey escribió, en el prefacio de su libro de 1994: la disciplina junta a 500 programadores mediocres; las ideas grandes necesitan unos pocos. Treinta años después, la apuesta sigue en pie.'
tags: ['libros', 'Scheme', 'pedagogia', 'Berkeley', 'Brian Harvey']
---

> _«Computer programs have become too large and complex to encompass in a human mind. Therefore, the job of computer science education is to teach people how to discipline their work in such a way that 500 mediocre programmers can join together and produce a program that correctly meets its specification.»_

Así arranca, casi al pasar, el prefacio de _Simply Scheme: Introducing Computer Science_ (Brian Harvey y Matthew Wright, MIT Press, 1994).[^ss] No es una crítica ajena — es la caricatura que los propios autores hacen de lo que ellos llaman la **vista conservadora** de la educación en ciencias de la computación. La escriben para después voltearla.[^preface]

Porque dos frases más adelante viene la otra versión, la que ellos sí sostienen:

> _«...the job of computer science education is to teach people how to expand their minds so that the programs can fit, by learning to think in a vocabulary of larger, more powerful, more flexible ideas than the obvious ones.»_

Ahí está el post entero en dos citas. Una dice: la complejidad del software le gana a la mente individual, así que hay que sumar cuerpos y disciplina hasta compensar. La otra dice: la complejidad del software le gana a la mente individual, así que hay que agrandar la mente. Quinientos programadores mediocres coordinados por proceso, o un puñado que piense en ideas más grandes. Mismo problema, dos apuestas completamente distintas sobre dónde poner el esfuerzo.

Harvey y Wright apostaron por la segunda. Y lo interesante — lo que treinta años después sigue vigente — es que no la reservaron para una élite ya seleccionada.

## Un curso para los que no iban a ser programadores

Durante casi dos décadas, el curso CS 3 — _Introduction to Symbolic Programming_ — de la Universidad de California en Berkeley usó _Simply Scheme_ como libro de texto.[^cs3] La mayoría de los alumnos no eran de la carrera de informática: cursaban CS 3 porque necesitaban un curso de razonamiento cuantitativo, no porque quisieran programar. También lo tomaban los futuros informáticos que llegaban sin experiencia previa — alrededor del diez por ciento de los ingresantes a CS (Computer Science), según el propio Harvey.

Ahí está la primera subversión del libro. La vista conservadora asume, sin decirlo, que las ideas grandes son para los que ya se sabe que van a ser programadores, y que al resto — la masa, los 500 — les alcanza con la disciplina y el proceso. Harvey apostó lo contrario: si las ideas potentes se enseñan bien, no hace falta preseleccionar a nadie. Cualquiera puede aprender a pensar así.

## Un prólogo a SICP

Si conocés SICP — _Structure and Interpretation of Computer Programs_, el libro de Abelson y Sussman, con Julie Sussman[^sicp] — _Simply Scheme_ es el libro que te lleva hasta la puerta de entrada. Harvey y Wright lo dicen sin ambigüedad: «Our book is a prequel; it's meant to teach you what you need to know in order to read that book successfully.»[^preface]

No es casualidad que Hal Abelson, coautor de SICP, haya escrito el prólogo de _Simply Scheme_.[^foreword] Ahí Abelson nombra la misma trampa que Harvey caricaturiza en su propio prefacio, sólo que con otras palabras: «This book points the way out of the trap. It emphasizes programming as a way to express ideas, rather than just a way to get computers to perform tasks.» La trampa es creer que programar es dar instrucciones a una máquina — la tarea que, en el fondo, cualquiera de los 500 puede hacer si sigue el proceso. La salida es entender que programar es pensar con rigor sobre ideas — la tarea para la que hace falta una mente expandida, no un manual de disciplina.

El dato que más me llamó la atención: _Simply Scheme_ cubre, en 26 capítulos y siete partes, el material equivalente a las primeras cien páginas de SICP.[^whatsnext] No es que sea más fácil — es que va más lento, con más ejemplos, más repetición y más paciencia. Donde SICP asume que ya sabés qué es una función, _Simply Scheme_ te lo enseña. Donde SICP te tira a la pileta con recursión en el capítulo 1, Harvey espera hasta la Parte IV.

Y eso no es una concesión. Es el mismo argumento del prefacio, llevado a la práctica: si el objetivo es agrandar la mente en vez de disciplinarla, hay que dar tiempo.

## La interacción como método, no como lujo

El prefacio también cita explícitamente a Dijkstra, que en 1989 propuso que los alumnos de CS no tocaran una computadora.[^dijkstra] Harvey se planta en la posición exactamente opuesta: sentaba a sus alumnos frente al intérprete de Scheme desde el primer día. Escribí una expresión, mirá el resultado. Para la vista conservadora esto sería ruido — mejor razonar en el papel antes de ensuciarse con la máquina. Para la vista radical es el método: las ideas grandes se aprenden probándolas, no memorizándolas.

## Tres decisiones que construyen una mente expandida

"Expandir la mente" suena lindo en un prefacio, pero Harvey y Wright lo bajan a decisiones concretas de diseño del libro. Son las que, para mí, explican por qué esto no es sólo retórica: son las prácticas puntuales que separan pensar en ideas grandes de simplemente acumular sintaxis.

**Funciones de orden superior antes que recursión.** En casi todos los cursos introductorios, la recursión aparece temprano y las funciones de orden superior tarde — si aparecen. Harvey invierte el orden. Su argumento: si se enseña recursión primero, el alumno construye un modelo mental incorrecto donde "la función se llama a sí misma" implica "volver atrás", como un loop. Enseñar `map`, `filter` y `accumulate` primero construye la intuición de que las funciones son valores como cualquier otro.

**Cero mutación.** En todo el libro no hay un solo `set!`. No hay variables que cambien de valor. Harvey se ahorra así el modelo de evaluación por entornos — la parte más difícil de SICP — y trabaja todo el libro con el modelo de sustitución puro. La única excepción es `vector-set!` cerca del final, presentado como una concesión al mundo real.

**Programación simbólica.** En vez de arrancar con números y aritmética, _Simply Scheme_ arranca con palabras y oraciones. `(first 'hello)` devuelve `h`. `(butfirst 'hello)` devuelve `ello`. `(sentence 'I 'love 'Scheme)` devuelve `(I love Scheme)`. Manipular texto es más interesante que sumar enteros, y lo interesante es lo que mantiene a la gente programando.

Ninguna de las tres es una restricción — al revés de lo que haría la vista conservadora, que restringe para contener el daño. Las tres son apuestas a que, si entendés estas ideas primero, después podés cargar con más complejidad en la cabeza sin que se te desarme el modelo mental. Eso es, literalmente, "expandir la mente para que los programas entren".

## Leerlo hoy

Berkeley ya no usa Scheme para su curso introductorio: CS 61A pasó a Python en 2011 y CS 3 fue reemplazado por CS 10, _The Beauty and Joy of Computing_, que usa Snap! — un lenguaje visual con funciones de orden superior creado por el propio Harvey.[^snap] El mundo se movió.

Pero la elección entre las dos vistas no se resolvió — se volvió invisible. La mayoría de los cursos introductorios de hoy enseñan Python con `for` loops y variables mutables desde el día uno, sin declarar que están tomando partido. Es la vista conservadora de 1994, sin la caricatura de los "500 mediocres" que la hacía incómoda de defender en voz alta. Los alumnos de esos cursos salen sabiendo escribir un loop. Muchos no salen sabiendo qué es una función de orden superior, ni por qué esa idea importa.

Y ahí está la apuesta que sigue abierta treinta años después: si necesitás resolver algo grande, ¿sumás gente disciplinada hasta que el proceso compense lo que a cada uno individualmente le falta, o invertís en que cada mente individual pueda cargar con más? Harvey no eligió la primera opción ni la reservó para unos pocos elegidos de antemano — apostó a que enseñarle a _cualquiera_ a pensar en ideas grandes salía más barato, y era más honesto, que reclutar 500 personas para que la disciplina hiciera el trabajo que las ideas no estaban haciendo.

_Simply Scheme_ está disponible gratis, completo, en la web de Harvey.[^ss] Se puede leer en una semana. Si alguna vez quisiste entender SICP pero te rebotó, empezá por acá. Y si enseñás a programar — o simplemente programás y no querés ser uno de los 500 — leelo como lo que es: un manifiesto contra la idea de que la complejidad se resuelve con más gente y más proceso, en vez de con mejores ideas.

[^ss]: Brian Harvey & Matthew Wright, [_Simply Scheme: Introducing Computer Science_](https://people.eecs.berkeley.edu/~bh/ss-toc2.html), MIT Press, 2.ª ed. 1999. Texto completo disponible en la web de Harvey para uso personal.

[^preface]: [Prefacio de _Simply Scheme_](https://people.eecs.berkeley.edu/~bh/ssch0/preface.html), donde Harvey y Wright contraponen la "vista conservadora" y la "vista radical" de la educación en ciencias de la computación.

[^cs3]: [CS 3: Introduction to Symbolic Programming](https://people.eecs.berkeley.edu/~bh/cs3.html) — página del curso en Berkeley.

[^sicp]: Harold Abelson & Gerald Jay Sussman, con Julie Sussman, [_Structure and Interpretation of Computer Programs_](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html), MIT Press, 2.ª ed. 1996.

[^foreword]: [Prólogo de _Simply Scheme_](https://people.eecs.berkeley.edu/~bh/ssch0/foreword.html), escrito por Hal Abelson, coautor de SICP.

[^whatsnext]: [Capítulo 26: What's Next?](https://people.eecs.berkeley.edu/~bh/ssch26/preview.html) — donde Harvey conecta _Simply Scheme_ con SICP y estima la cobertura.

[^dijkstra]: Edsger W. Dijkstra, «On the Cruelty of Really Teaching Computing Science», publicado dentro de Peter J. Denning (ed.), [«A Debate on Teaching Computing Science»](https://doi.org/10.1145/76380.76381), _Communications of the ACM_ 32, n.º 12 (1989), pp. 1397–1414. Texto de Dijkstra disponible como [EWD 1036](https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html) en el archivo EWD de UT Austin. Harvey lo cita en el prefacio para marcar su desacuerdo.

[^snap]: [Snap!](https://snap.berkeley.edu/) — _Build Your Own Blocks_, lenguaje visual creado por Brian Harvey y Jens Mönig. Berkeley lo usa en CS 10 como sucesor de CS 3.
