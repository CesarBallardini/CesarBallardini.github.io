---
layout: post
title: 'Vagrant: ¿Qué es eso?'
description: "Descripción del problema que resuelve Vagrant"
tags: [vagrant, virtualbox]
---

## Introducción

Vagrant[^ref1] es una herramienta que simplifica el _workflow_ y reduce la carga necesaria para crear, correr y operar máquinas virtuales (VM) en tu computadora.

La interfaz de gestión es mediante mandatos en modo CLI (_Command Line Interface_). Admite las soluciones principales de virtualización: VirtualBox, VMWare, KVM, Hyper-V. Trabaja con las herramientas de gestión de configuración más populares: Ansible, Chef, Puppet, Salt.

Además facilita la distribución de entornos virtuales, lo cual permite que los agentes de la organización tengan un acceso simple, sin complicaciones a entornos patrón, por ejemplo: entornos de desarrollo de un framework Web, entornos de testing repetibles, etc.

Hay un único mandato que se necesita para levantar una o más VMs que trabajan en concierto:

```bash
vagrant up
```

No importa si las VM se crearán sobre VirtualBox o sobre VMWare, si es una única VM o son tres, si se va correr dentro de la VM un GNU/Linux o un MS Windows, tampoco importa si tendrá Symfony o Django.  Con ese solo mandato, la VM estará encendida y respondiendo en un tiempo que va desde segundos a minutos.


## Lo que Vagrant automatiza para nosotros

Cuando se da el mandato enunciado unos párrafos más arriba, lo que Vagrant hace es:

1. Lee el archivo de configuración de la infraestructura que va a crear (`Vagrantfile`)
2. Descarga la plantilla (_box_) de la imagen que va a crear (VM)
3. Inicia la VM
4. Configura los recursos de la VM: RAM, cantidad de CPUs, directorios compartidos y configuración de red
5. Si es apropiado, realiza la instalación del software solicitado para la VM

La VM está ahora operativa, y podemos ingresar mediante SSH con el mandato:

```bash
vagrant ssh
```

## Mandatos usuales Vagrant

Las operaciones fundamentales son las siguientes:

```bash
vagrant up      # levanta la VM, creándola si es la primera vez que se ejecuta
vagrant ssh     # ingresa para SSH a la VM
vagrant halt    # detiene la ejecución de la VM (queda lista para otro vagrant up)
vagrant destroy # detiene la VM y elimina la imagen de la VM (desaparece completamente)
```

## Virtualización

El problema que resuelve la virtualización es el del aislamiento de sistemas: el sistema instalado en mi computadora no necesita ser modificado para correr una aplicación Web.

Dentro de la VM puede existir otra versión de sistema operativo, por ejemplo tal vez mi computadora tiene instalado Ubuntu GNU/Linux, y en la VM estoy trabajando con un servidor Debian.  Además la pesadilla del desarrollador es el _dependency hell_[^ref4]: cuando diferentes aplicaciones en las cuales está trabajando requieren diferentes versiones incompatibles de una biblioteca en particular.  O diferentes versiones de PHP, etc.

El aislamiento que proporciona la virtualización permite que en la computadora se instale una versión de PHP, y en la VM otro completamente diferente, sin que haya interferencias.

Algunos de los mecanismos de virtualización, por ejemplo Virtualbox, trabajan sobre diferentes sistemas operativos anfitrión, como Mac, GNU/Linux y Ms Windows.  Otros, basados en contenedores como LXC, trabajan sobre diferentes versiones de GNU/Linux.

## Vagrant

Vagrant se apoya en un mecanismo de virtualización dado y proporciona mandatos y configuraciones que abstraen el detalle de cómo producir una VM operativa sobre ese dado mecanismo de virtualización.

## Desventajas

1. Eficiencia de la estación de trabajo.  Las máquinas de los desarrolladores ejecutan las VM con una penalidad en la performance, y por ello deben ser de suficientes recursos en RAM y CPU para que sean usadas con eficacia.  Las estaciones de los sysadmin deben ser de mejores prestaciones aún, pues la tarea de crear las VM y sus verificaciones es muy demandante.
2. El directorio compartido que crea Virtualbox tiene una pésima performance, para mejorar este aspecto se debe usar NFS.  Pero esta mejora no está disponible cuando el anfitrión es un MS Windows.  Entonces no toda combinación de partes es factible.
3. Algunas combinaciones de sistema operativo en el anfitrión y plataforma de virtualización no son funcionales.

## Ventajas

1. Simple _workflow_ para obtener VMs correctamente configuradas: no hay que lidiar con el sistema de virtualización.
2. Corto tiempo hasta que el entorno de trabajo está operativo, en el orden de minutos.
3. El desarrollador puede cambiarse de estación de trabajo hacia otra, o cambiar su sistema operativo, sin tener que reinstalar nada de software.  Sólo debe asegurarse que tiene instalado Virtualbox y Vagrant.
4. El desarrollador ya no es responsable de instalar software del lado server.
5. Todo el mundo usa exactamente el mismo software del lado server.
6. A las VMs que usan los desarrolladores, las preparan los ingenieros de operaciones.
7. Cada desarrollador puede crear, destruir y recrear los entornos virtuales en minutos.
8. Vagrant facilita la actualización del software de server que se usa en las estaciones de los desarrolladores.
9. El acceso a los recursos del sistema, como los puertos de red, está restringido, de manera predeterminada.
10. La seguridad de todos los equipos usados para desarrollo se puede gestionar globalmente, porque es un sysadmin el que preparó las VM y las reglas de acceso a la computadora del desarrollador.
11. Se puede lograr un mapeo casi 1:1 entre los entornos de desarrollo, testing y producción.
12. Los entornos virtuales se crean para cada proyecto: todo proyecto corre aislado de los demás proyectos.
13. Cada proyecto puede elegir usar paquetes de manera arbitraria: un proyecto puede usar Debian + PHP5.4 + Symfony2.8 y otro CentOS + Ruby2.3 + Rails4.
14. Se usa un único _workflow_, sin importar la plataforma de virtualización, el sistema operativo de la VM, el lenguaje de programación, _framework_, o software del lado server.
15. Los desarrolladores no necesitan una conexión de red para hacer su trabajo.
16. Vagrant es Open Source y Free Software[^ref2] [^ref3].
17. Vagrant funciona en las plataformas de sistema operativo más populares: GNU/Linux, Mac OS X y MS Windows.
18. Vagrant dispone de una documentación clara y bien detallada.
19. La funcionalidad de Vagrant puede extenderse mediante _plugins_.
20. Es ideal para la presentación en cursos y capacitaciones.  El instructor puede asegurarse el entorno que usarán los alumnos, es fácil para los alumnos entrar en carrera, sin necesidad de saber cómo instalar todo el software requerido.


[^ref1]: [http://www.vagrantup.com/](http://www.vagrantup.com/) Sede Web del proyecto.

[^ref2]: [https://github.com/mitchellh/vagrant](https://github.com/mitchellh/vagrant) Código fuente en Github.

[^ref3]: [https://github.com/mitchellh/vagrant/blob/master/LICENSE](https://github.com/mitchellh/vagrant/blob/master/LICENSE) Licencia MIT empleada.

[^ref4]: [https://en.wikipedia.org/wiki/Dependency_hell](https://en.wikipedia.org/wiki/Dependency_hell)

