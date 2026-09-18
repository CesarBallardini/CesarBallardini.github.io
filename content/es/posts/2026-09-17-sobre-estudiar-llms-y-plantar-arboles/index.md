---
title: 'Sobre estudiar LLMs y plantar árboles'
description: '¿Qué hay detrás de un LLM?'
tags: ['IA', 'inteligencia artificial', 'LLM', 'plan de estudio', 'pedagogia']
featured_image: hero-tocon-y-roble.jpg
page_css: ['tables.css']
---

Hace un tiempo leí una frase «el mejor momento para plantar un árbol fue hace veinte años; el segundo mejor momento es ahora».  

Hay muchas ofertas de trabajo relacionadas con la Inteligencia Artificial. ¿Cuándo es un buen momento para estudiar IA? Se parece a plantar un árbol.  Si querés disfrutar de la sombra (presentarte a las ofertas de trabajo) entonces hace años deberías haber estudiado IA. Este post es sobre un árbol que acabo de plantar: un [plan de estudio para aprender cómo funcionan los modelos de lenguaje grandes](https://katra.ballardini.com.ar/llm-for-dummies-study-plan/), desde cero.

## El árbol

[*LLM for Dummies*](https://katra.ballardini.com.ar/llm-for-dummies-study-plan/) es un curso armado como libro, en inglés. Arranca en álgebra de nivel universitario inicial y termina en construir, entrenar, operar y mejorar un modelo de lenguaje de código abierto. Son 24 capítulos repartidos en seis partes:

| Parte | Tema | Capítulos |
| --- | --- | --- |
| I | Fundamentos matemáticos: álgebra, cálculo, álgebra lineal, probabilidad, optimización | 1–5 |
| II | Programación y herramientas: Python, el stack científico, GPUs | 6–7 |
| III | Machine learning y deep learning, hasta backpropagation a mano | 8–10 |
| IV | Transformers y LLMs: tokens, embeddings, un LLM desde cero, preentrenamiento, entrenamiento distribuido | 11–16 |
| V | Post-entrenamiento: fine-tuning, alineamiento (RLHF, DPO), modelos de razonamiento | 17–19 |
| VI | Evaluación, inferencia, operación, un proyecto final y el hábito de leer papers | 20–24 |

Todos los capítulos tienen la misma forma: qué se aprende, los temas en orden, los recursos (con un «empezá por acá» marcado en cada grupo), un **hito** práctico que produce un resultado verificable, y una estimación de tiempo. El hito es el mecanismo de control: si ya sabés un tema, podés hojear el capítulo y usar el hito como diagnóstico.

Los recursos son gratuitos o baratos, y cada uno está enlazado a su página oficial: cursos del MIT OpenCourseWare, Stanford, Harvard, Khan Academy, fast.ai, Hugging Face, los videos de Karpathy, y libros que sus autores publican libres, como *Mathematics for Machine Learning*, *Deep Learning* de Goodfellow, Bengio y Courville, o *Understanding Deep Learning* de Prince.

Si no querés recorrerlo de punta a punta, hay [seis rutas de aprendizaje](https://katra.ballardini.com.ar/llm-for-dummies-study-plan/learning-paths/), cada una parte de un objetivo: entender cómo funciona un LLM por dentro, preentrenar un modelo, mejorar un modelo existente, servirlo y operarlo en producción, o construir una aplicación usando modelos de uso libre. Cada ruta nombra los capítulos en orden, lo que asume de antes y el hito que prueba que llegaste. Para quien arranca de cero está la Ruta 0, que es la base de todas las demás.

## Cuánto tarda en crecer

Acá es donde entra la frase. La estimación total del plan es de **24 a 36 meses a 10 horas por semana**, o de 12 a 18 meses a 20 horas por semana. La Parte I, la matemática, se lleva una buena porción de ese tiempo, porque todo lo que viene después se apoya en ella.

Dos o tres años es mucho. Es el tipo de número que invita a pensar «tendría que haber empezado antes». Hace quince años —o veinte, o treinta— no existía nada de esto para estudiar: el paper que presentó la arquitectura Transformer es de 2017. Lo que sí existía era la matemática de la Parte I:  si fuiste a la universidad vas a tener una buena base para empezar o repasar.  Por otro lado, una tecnología tan nueva, que requiere tanta potencia de cálculo y energía es una garantía de que es muy poco probable que encuentres buenos maestros en tu ciudad.  Vas a tener que estudiar por tu cuenta, y vas a tener que usar material de las universidades y empresas de primer nivel.

La sugerencia del propio plan para la primera semana es modesta a propósito: ver la charla de una hora de Karpathy, [*Intro to Large Language Models*](https://www.youtube.com/watch?v=zjkBMFhNj_g), para tener el panorama; empezar álgebra en Khan Academy y Python en CS50P, entre media hora y una hora por día cada uno; y al final de la semana fijar un presupuesto de horas semanal. Un horario fijo se sostiene mejor, a lo largo de meses de esfuerzo, que sesiones largas e irregulares.

## Dónde está

- La guía de estudio: <https://katra.ballardini.com.ar/llm-for-dummies-study-plan/>
- El plan completo en un solo archivo ([`STUDY_PLAN.md`](https://github.com/CesarBallardini/llm-for-dummies-study-plan/blob/main/STUDY_PLAN.md)): <https://github.com/CesarBallardini/llm-for-dummies-study-plan>

Está publicado bajo licencia MIT, que cubre el texto del plan y el código de los hitos. Los cursos, libros, papers y videos enlazados conservan la licencia de sus autores.

Hace muchos años mi enfoque cuando tenía que estudiar algo completamente nuevo era sencillo:

- Buscar cursos en alguna universidad relacionados con el tema que deseaba aprender
- Conseguir el plan de estudios de las materias
- Buscar la bibliografía del plan de estudios
- Sacar los libros de la biblioteca
- Cuaderno y lápiz, estudiar los libros y hacer los ejercicios

La llegada de los buscadores de Internet me permitió encontrar universidades lejos de mi casa.  Ahora las IA generativas son más poderosas a la hora de encontrar material: he usado Claude de Anthropic con Opus 5 para encontrar el material, clasificarlo, ordenarlo en capítulos y secciones.

Como en la foto de cabecera[^img_hero], el roble pequeño brota al lado del viejo tocón, podemos usar la IA para aprender IA.

Nos encontramos al final del curso, tomando unos mates a la sombra.

[^img_hero]: Imagen de [Tree stump with oak sapling at Myrstigen 1](https://commons.wikimedia.org/wiki/File:Tree_stump_with_oak_sapling_at_Myrstigen_1.jpg) — CC BY-SA 4.0 — W.carter, 2022. Sendero Myrstigen, Brastad, municipio de Lysekil, Suecia. Recortada a 2.5:1 para hero landscape.
