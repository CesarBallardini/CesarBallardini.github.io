---
layout: post
title: ''
description: ''
tags: []
---


Mirar primero:

https://puppet.com/presentations/designing-puppet-rolesprofiles-pattern


Mirarlo de vuelta :)

Cómo se puede pensar en Ansible:
https://softwareengineering.stackexchange.com/questions/324705/what-is-the-equivalent-of-puppets-roles-profiles-pattern-in-ansible

Ansible has the concepts of roles and dependencies which can be used in conjunction to create a roles/profiles/components pattern as you do in Puppet. You could design your role as a component, as a profile or as a role. Probably you would need a naming convention structure to not get confused about the difference between them. If you want to build a webserver role (puppet pattern) you could have 5 roles (ansible roles), component-apache, component-mysql, profile-database, profile-webserver, role-webserver. The first 2 will be roles that installs and configure a generic apache/mysql software (you should find it at ansible-galaxy). The 2 profiles will add these 2 components as dependencies (in meta/) and specify what exactly your implementation is via vars or tasks (should I support virtualhost? My mysql profile will work as cluster?). In the end, you create the last role (ansible) which will work as a role (puppet pattern). It will add as dependencies your 2 profiles (profile-database, profile-webserver).

In the end, on your playbook, you just apply the role-webserver to the nodes specified.



el post que inició todo ese tema:
https://www.craigdunn.org/2012/05/239/

de ahi saqué: https://www.slideshare.net/PuppetLabs/roles-talk diapos

y video: https://www.youtube.com/watch?v=ZpHtOnlSGNY (pero no lo puedo ver en la oficina, no se porque:  "400. That’s an error. Your client has issued a malformed or illegal request. That’s all we know." )

Me resultó bastante mas esclarecedora la breve explicación sobre Ansible que la charla de Puppet, aunque es cierto que necesitás verla para saber de qué estamos hablando. Me quedan igualmente algunas dudas, tiro las primeras:

A nivel de componente: ¿los roles instanciarían variables, solamente las dejaría por default para garantizar una instalación funcional? Si quedan sin instanciar, la especificación vendría en el nivel de Perfil o del Rol?

A nivel de perfil: según el ejemplo en el nivel perfil tendrías algo como profile-database o profile-webserver, pero en esos caso podrían querer construirse desde distintos componentes. El ejemplo más claro profile-database, si hablamos de una base oracle, va a tener el componente principal y probablemente todas las variables distintas a un mysql ¿En ese caso el patrón sugiere un solo profile-database con toda la lógica para poder instanciarlo como uno u otro o habría en cambio un Perfil para cada uno?

Si en nuestro modelo tenemos aplicaciones de tal forma que tenemos un vínculo de n aplicaciones a m servidores. Pienso que habría un componente aplicacion-php que crearía usuarios necesarios, directorios, permisos, etc ¿se podría modelar así? Y las configuraciones de virtual-host o propiedades de php específicas dónde irían, en un Perfil? ¿qué Perfil?

César,

Me resultó bastante mas esclarecedora la breve explicación sobre Ansible que la charla de Puppet, aunque es cierto que necesitás verla para saber de qué estamos hablando. Me quedan igualmente algunas dudas, tiro las primeras:

A nivel de componente: ¿los roles instanciarían variables, solamente las dejaría por default para garantizar una instalación funcional?

Yo creo que algo así: en default/main.yml los parámetros (ej: ruta del binario o nombre del paquete) y en vars/main.yml los valores para dejar el componente en estado funcional.

Si quedan sin instanciar, la especificación vendría en el nivel de Perfil o del Rol?

No debería quedar nada sin instanciar (o está en default/ o en vars/ )



A nivel de perfil: según el ejemplo en el nivel perfil tendrías algo como profile-database o profile-webserver, pero en esos caso podrían querer construirse desde distintos componentes. El ejemplo más claro profile-database, si hablamos de una base oracle, va a tener el componente principal y probablemente todas las variables distintas a un mysql ¿En ese caso el patrón sugiere un solo profile-database con toda la lógica para poder instanciarlo como uno u otro o habría en cambio un Perfil para cada uno?

Esta respuesta te la debo, pero...


Bienvenido al proyecto DebOps (DevOps en Debian)

https://docs.debops.org/en/master/ docs
https://github.com/debops/debops código


La historia comienza aquí: https://github.com/debops/debops/blob/master/ansible/playbooks/site.yml

por ejemplo incluye a https://github.com/debops/debops/blob/master/ansible/playbooks/srv.yml
el cual meramente dice:

- import_playbook: srv/all.yml


y ese srv/all.yml es https://github.com/debops/debops/blob/master/ansible/playbooks/srv/all.yml
y allí se incluyen mysql, mariadb, postgresql, postfix, y todo lo que se te ocurra que sea un servicio que ofrece el nodo.

por ejemplo, https://github.com/debops/debops/blob/master/ansible/playbooks/srv/postgresql_server.yml es un link sombólico a ../service/postgresql_server.yml
el cual es https://github.com/debops/debops/blob/master/ansible/playbooks/service/postgresql_server.yml

el comienza con:

- name: Manage PostgreSQL server
  hosts: [ 'debops_service_postgresql_server', 'debops_postgresql_server' ]
  become: True

  environment: '{{ inventory__environment | d({})
                   | combine(inventory__group_environment | d({}))
                   | combine(inventory__host_environment  | d({})) }}'



O sea, los hosts de esos grupos son los únicos que se van a configurar con un servidor postgresql

La magia del combine se hace para mezclar las variables de diferentes variables:
https://github.com/debops/debops-playbooks/blob/master/docs/custom-environment.rst donde usa justo el ejemplo del proxy Web para el sistema

inventory__{|group_|host_}environment


La docs de PostgreSQL server es: http://debops.readthedocs.io/en/latest/ansible/roles/debops.postgresql_server/getting-started.html




Si un servidor postgres te parece medio alejado de lo que hacen normalmente en ASI, proba con http://debops.readthedocs.io/en/latest/ansible/roles/debops.gitlab/index.html

O más cercanos a lo que ahora estamos haciendo para entrega continua: http://debops.readthedocs.io/en/latest/ansible/roles/debops.php/index.html
O también: http://debops.readthedocs.io/en/latest/ansible/roles/debops.apache/index.html



Si en nuestro modelo tenemos aplicaciones de tal forma que tenemos un vínculo de n aplicaciones a m servidores. Pienso que habría un componente aplicacion-php que crearía usuarios necesarios, directorios, permisos, etc ¿se podría modelar así? Y las configuraciones de virtual-host o propiedades de php específicas dónde irían, en un Perfil? ¿qué Perfil?


Ahora puedo empezar a responder la pregunta que dejé colgada antes, y de paso esta que mencionás:

En Puppet con componente/perfil/rol la instalación se hace en cada nodo, el cual se clasifica con un ENC.

En Ansible lo que se instala es un site a través de un playbook, el site.yml
El playbook incluye todos los playbooks que hagan falta para crear la infraestructura completa.
Cada vez que agregas un nodo nuevo con características propias (esto va a pasar a menudo mientras booteamos toda la infra paso a paso incrementalmente), lo que se hace es clasificarlo en el inventario antes que nada, donde lo asignás a aeificios (red, gateway, proxy, mirror etc.) luego a ambiente (testing/prod/dev/capa) y a grupo de trabajo (webserver, database, etc), luego las cosas propias del host.  Ahora escribis un playbook que cuenta la historia de ese nodo desde que se conecta ansible hasta que esta listo para dar sus servicios a la infra.  Y eso se incorpora al site.yml

Rinse Repeat



Otro modelo de trabajo es el propuesto por Alessandro Franceschi , de example42.com. con quien incluso intercambiamos un par de email sobre el tema de organizar código puppet para infraestructuras generales, múltiples clientes, y cómo seguir la evolución del código puppet a lo largo del tiempo (donde dev/test/prod también se aplica a código puppet y es ortogonal con el dev/test/prod de los devs de apps)

En todos los casos, la herramienta de trabajo se transforma en un framework de expresión de infraestructura, mediante un cuidadoso uso de las estructuras de abstracción de código y de asignación de datos en hjerarquías o grafos de precedencias para aosciar parámetros de infra con programas que las implementan.

Uff. Es mucha palabrería que suena a sanata cuando no implementaste una o dos infras previamente.  Es un aprendizaje iterativo.  Primero trabajamos con recursos (paquetes/archivos/servicios), después queremos asociar recursos relacionados con un subsistema dado (sshd por ejemplo), después hay servicios que dependen y usan otros, y hay que orquestarlos (ej: postfix + amavis + spamassasin + rbl + buzones + webmail + ...) y después querés expresar ideas como escalabilidad (hay 5 servidores de X, quiero que haya 7).  Es necesario expresar cómo obtener una VM nueva, aprovisionarla en un ambiente dado, testear que tiene la funcionalidad solicitada, conectarla a las redes de trabajo, asegurar las reglas de firewall en los demás servidores, ruteo y facilidades (acceso desde el proxy, desde el mirror, monitoreo, backups, logs).

A medida que nos movemos por ese continuo de gestión de servicios (no de servidores) vamos haciéndonos las preguntas y transpiramos para conseguir, probar y depurar las respuestas.

Es explorar un territorio desconocido, sin mapas ni baqueanos.  Hay que ir despacio, sin detenerse.  Tomate tu tiempo.  En cualquier estadío que estemos, estamos mejor que antes.


Ale, esto lo tenés que leer después de 3 o 4 cerverzas y no sé lo que sale jajaja.

Andá al fondo del mail, parte de un proyecto en Puppet en el que buscaron cómo modelar una infraestructura definiendo roles y perfiles. Luego en el hilo que está enlazado tratan de tomar esos conceptos y ver cómo se pueden expresar en Ansible.

No es la única -ni definitiva- solución al problema de cómo organizar una infraestructura de uso general con Ansible pero creo que sirve al menos para orientar la discusión. El esquema de https://git.santafe.gov.ar/dpit/escrutinio2019 que planteó César responde a éste modelo, pero tenemos que verlo nosotros para sumar la experiencia de lo que logramos en estos meses.

Puede parecer quizás abstracto, pero ya comprobamos en la práctica que es necesaria una conceptualización para saber dónde va cada variable, qué tarea va en qué playbook o en qué rol, etc.

De hecho creo que ya tenemos algunas cuestiones para analizar que este modelo no aborda o resuelve:

Separar aprovisionamiento/creación de las tareas operativas/mantenimiento
Separar el inventario de los playbooks, ¿un inventario o muchos inventarios?



https://stackoverflow.com/questions/35926324/how-do-you-handle-server-dependencies-in-ansible-roles
el ejemplo de nginx_web / nginx_fileserver / nginx para una especie de "herencia del hombre pobre" en Ansible

https://github.com/kuleszaj/ansible-dependency-example
usa variables en el meta.yml para declarar una dependencia

https://groups.google.com/forum/#!topic/ansible-project/37bcs9dLH1g
Ansible Role dependencies After Role
My Role A starts an installer that always overrides the certificates. I also got a certificate deployment role Role B which should always be called after role A.

https://blog.eulinux.org/2016/01/ansible-conditional-role-dependencies.html
Ansible: Using conditional role dependencies
para que la distinción de master/slave no requiera un par de grupos en el inventario / esto vale cuando hacemos un role para instalar tanto server como client

Para leer https://www.craigdunn.org/2012/05/239/ debe buscarlo en:
http://web.archive.org/web/20131116063306/http://www.craigdunn.org/2012/05/239/

Mauro:

Mirá el readme de ese repositorio, eso lo armó césar en base a algunas cosas sobre la que él me iluminó y que charlamos juntos. Esa propuesta finalmente no se implementó porq no nos dieron bola, pero quedó la idea:

https://git.santafe.gov.ar/dpit/escrutinio2019/blob/master/README.md

En este enfoque (abajo hay referencias a la discusión) Hay 3 conceptos básicos: rol, perfil y componente. Nada nodo (vm para nosotros ahora) tiene un rol. Un "rol" se escribe en forma de playbook. Un playbook de "rol" consta de una secuencia de plays, donde cada play es un "perfil" ---> es lo que vos hiciste para el requerimiento sobre wildfly.


https://gitlab.com/respaldos_stg/dpit/escrutinio2019/-/blob/master/README.md :
# Inventarios

Se trabaja con múltiples inventarios.  El inventario forma parte de este repositorio Git.

Dentro del directorio `inventories/` hay un directorio para cada inventario.  En este momento están definidos los siguientes:

* development
* production
* staging
* testing

Cuando nos referimos a "inventario" estamos haciendo alusión a uno de esos subdirectorios de `inventories/`.

En un inventario dado hay tres elementos:
 * `hosts` es un archivo que lista los nodos de este inventario
 * `group_vars/` contiene un archivo de variables para cada grupo de nodos creado en el inventario
 * `host_vars/`contiene un archivo de variables para cada nodo del inventario

Los archivos de variables de grupo y de nodo pueden o no existir. si existe el
archivo `group_vars/all`, sus valores son aplicables a todos los nodos, sin importar si
pertenecen o no a algún grupo.

Los valores de las variables en estos archivos tienen la siguiente precedencia,
de mayor a menor:

 1. playbook
 2. nodo
 3. grupo
 4. all


Los directorios creados actualmente tienen esta forma:

```
├── inventories/
│   ├── development/
│   │   ├── group_vars/
│   │   ├── hosts
│   │   └── host_vars/
│   ├── production/
│   │   ├── group_vars/
│   │   ├── hosts
│   │   └── host_vars/
│   ├── staging/
│   │   ├── group_vars/
│   │   ├── hosts
│   │   └── host_vars/
│   └── testing/
│       ├── group_vars/
│       ├── hosts
│       └── host_vars/
```



# Estructura de este repositorio


```
.
├── .gitignore
├── README.md
├── TODO.md
├── requirements.txt
├── rol-cachebalancer-srv.yml
├── rol-cache-srv.yml
├── rol-dns-srv.yml
├── rol-file-srv.yml
├── rol-jenkinsjava-srv.yml
├── rol-jenkinsphp-srv.yml
├── rol-mysql-srv.yml
├── rol-tomcat-srv.yml
├── rol-webbalancer-srv.yml
├── rol-webphp-srv.yml
├── site-upgrade.yml
├── site.yml
├── inventories/
├── roles/
├── files/
└── templates/
```

Describimos brevemente los archivos y directorios del primer nivel:

El playbook de alto nivel para asegurar la instalaci{on de todas las VMs es `site.yml`.
Uno similar, que sirve para actualizar los programas a la última versión en cada VM es `site-upgrade.yml`.

`README.md` es este archivo que estás leyendo. `TODO.md` es una lista de asuntos por resolver (To Do List).

`.gitignore` es parte del repo Git, es la lista de excepciones con los archivos que no se desea almacenar en el repo.

Un nodo es una máquina virtual o física que forma parte de escrutinio2019.  Algunos de esos nodos están bajo
responsabilidad del Área ASI (Aplicaciones y Servicios de Internet).  Solamente nos ocuparemos de estos nodos.

Los nodos se describen en el Inventario, el cual se aloja dentro del directorio `inventories/`.
Más información en la sección "Inventario" más arriba.

Cada nodo pertenece a uno y sólo un "rol" que describe su función y relaciones con los demás nodos.  Para cada "rol" puede
haber más de un nodo que satisface ese "rol".

Una lista de cada "rol" identificado es la siguiente:

* `rol-cachebalancer-srv.yml`
* `rol-cache-srv.yml`
* `rol-dns-srv.yml`
* `rol-file-srv.yml`
* `rol-jenkinsjava-srv.yml`
* `rol-jenkinsphp-srv.yml`
* `rol-mysql-srv.yml`
* `rol-tomcat-srv.yml`
* `rol-webbalancer-srv.yml`
* `rol-webphp-srv.yml`

Un "rol" se escribe en forma de playbook.  Un playbook de "rol" consta de una secuencia de plays, donde cada play
es un "perfil".  Por ejemplo, los servidores de Glusterfs tienen un perfil/play para instalar Glusterfs y otro
perfil/play para instalar un servidor FTP.

El "perfil" describe un servicio o subsistema instalado en un "rol".

Un "perfil" necesita de "componentes" para proporcionar un servicio dado.

Por ejemplo:

 * componentes: apache 2.4 / php 7.1 (son "ansible roles" tomados de Ansible Galaxy o un repo Git propio)
 * perfil: webserver (incluye los dos componentes anteriores) (es un play dentro del playbook del "rol")
 * rol `rol-webphp-srv.yml`: servidor para aplicación "elecciones" y "api elecciones"
 * nodo: escphp1e, escphp2e, etc. implementan el "rol" `rol-webphp-srv.yml`

Los "Ansible roles" se alojan en el directorio `roles/`.  Este directorio está excluído del repo escrutinio2018.
Cada ansible role debe tener su propio repositorio Git donde se lo desarrolla de manera independiete a los fines
de lograr roles genéricos y reusables.

`requirements.txt` es la lista de roles Ansible con su versión correspondiente que son requisitos para
correr los playbooks de escrutinio2019. En las "Instrucciones de instalación" se describe cómo se utiliza este archivo.

Los directorios siguientes contienen los archivos y plantillas específicas para escrutinio, y que se utilizan en
los ansible roles genéricos, y en los playbooks específicos:

* `files/`
* `templates/`
