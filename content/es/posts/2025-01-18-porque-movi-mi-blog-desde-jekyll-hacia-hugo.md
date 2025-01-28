---
layout: post
title: 'Porqué moví el Blog desde Jekyll hacia Hugo'
description: "Instalación de Hugo en una laptop con MS Windows 11"
tags: [Hugo, Jekyll, Blog]
---

El intento de Blog usando Jekyll tuvo poco éxito desde el punto de vista de la cantidad de posts.

En 2016 cambié de trabajo.  En la nueva posición los sysadmin no utilizaban Vagrant, Virtualbox, ni
automatizaban más allá de algunos scripts en Bash.  Cuando se sucedieron más de tres consultas
acerca de cómo instalar y usar esos programas, la idea de evitar la repetición me llevó a escribir esas viejas entradas.

Ahora en cambio mi motivación es anotar detalles de la historia y el folklore de la programación a lo largo de
los años.  Se trata de un conocimiento tribal que me gustaría dejar plasmado en un solo lugar, para beneficio
de los interesados y para evitarme, otra vez, la repetición.

Cuando quise crear posts adicionales en el Blog usando Jekyll, me encontré con su GitHub repo en https://github.com/jekyll/jekyll con commits antiguos, lo cual me hizo buscar cuál es el estado actual en el desarrollo de Jekyll.

Encontré:
* https://www.bridgetownrb.com/future/rip-jekyll/
* https://www.theregister.com/2021/09/14/future_of_jekyll_project_engine/


“Jekyll is in frozen mode and permanent hiatus. RIP Jekyll 2009-2018.” (la fuente fue un mensaje en un canal Slack,
la política de eliminación de mensajes antiguos provocó la pérdida del original)


Hace unos años que Github me avisa sobre problemas de seguridad en las dependencias Ruby de Jekyll.

La gran ventaja para mí de un generador de sitios estático  que puede servirse desde
Github Pages está en la muy baja carga de trabajo administrativo
que requiere: no hay base de datos, no hay web server, ni reverse proxy.  No hay que configurar,
ni mantener, ni actualizar esas piezas de software.

Las Github Pages toman un repositorio y generan el sitio estático.  De vez en cuando es necesario
obtener el repositorio y actualizar las dependencias para evitar las vulnerabilidades.

Es cierto que podría tener una instalación de Jekyll en mi laptop y generar el sitio allí para
luego subirlo al repositorio de las Github Pages.  Pero es un trabajo adicional, y la verdad,
instalar un entorno Ruby sólo para esa aplicación no me hace ninguna gracia.  De hecho, hace unos años
utilicé Vagrant+Virtualbox para no inundar de dependencias mi sistema.

Existen muchas alternativas para generadores de sitios estáticos.  Mi criterio de selección es simple:

* debe poder servirse desde Github Pages (no quiero un virtual server para el blog)
* deseable que una Github Action lo genere desde el propio repositorio al realizar merges en master.
* no quiero instalar un entorno de lenguaje de programación (Ruby, Python, Javascript, etc.) con su
package manager, el paquete del programa, más todas sus dependencias.
* deseable que la migración desde Jekyll sea lo más indolora posible

El ganador ha sido Hugo (https://gohugo.io/), escrito en Go Lang, y eso permite descargar sólo un ejecutable
para el sistema operativo y no hace falta más nada.   Hugo es un derivado de Jekyll, por lo tanto
los posts comparten el formato y características.  En otro post veremos lo simple que fue la conversión.

Entonces, paso a paso, lo que haremos será:

1. [Instalar Hugo en la laptop, crear un sitio inicial y configurarlo.](/posts/como-instalar-hugo-en-mi-laptop/)
2. [Migrar los posts antiguos escritos para Jekyll.](/posts/como-mover-los-posts-jekyll-hacia-hugo.md)
3. Generar el sitio estático para el blog.
4. Publicar el blog en Github Pages
5. Crear esta serie de posts para explicar cómo hacer estas tareas
