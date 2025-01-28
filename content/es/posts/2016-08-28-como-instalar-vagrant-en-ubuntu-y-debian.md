---
layout: post
title: 'Cómo instalar Vagrant en Ubuntu y Debian'
description: "Instalación de Vagrant, Virtualbox, plugins, y entorno sobre variantes GNU/Linux Debian y Ubuntu"
tags: [vagrant, virtualbox, Debian, Ubuntu, instalacion]
---

Vagrant es un programa que aprovecha una plataforma de virtualización para proporcionar un _workflow_ simple de gestión del
ciclo de vida de las máquinas virtuales.

Como sistema de virtualización utilizaremos Virtualbox.  Su principal ventaja es que es muy sencillo de poner en funcionamiento
y además corre en diferentes sistemas operativos anfitrión, como Mac OS X, GNU/Linux y Ms Windows.

La instalación se puede hacer de diversas maneras: con paquetes del sistema operativo anfitrión (en caso que existan como en GNU/Linux),
también se puede instalar a partir de los fuentes de cada proyecto, pues se trata de sistemas de software libre.  En la primer manera tenemos el
problema de que la versión que está empaquetada no siempre es la última estable.  En el segundo caso, es muy engorroso instalar toda
la cadena de compilador y entorno de desarrollo, luego clonar los repositorios fuentes, y compilar e instalar manualmente; incluso aunque de
esta manera tengamos la versión del «último grito de la moda», cuando salga una nueva, vamos a tener que rehacer todo el procedimiento.

Aquí vamos a dar las instrucciones para realizar la instalación utilizando los paquetes binarios disponibles para la descarga en cada proyecto.  El motivo es que
de esta manera podemos instalar la última versión estable provista por el dueño del proyecto, y será simple su actualización futura.  El único inconveniente
de este proceder puede ser si el dueño del proyecto no proporciona versiones binarias para las versiones de sistema operativo que necesitamos usar, y ése no es el caso con Debian y Ubuntu.

La opción de usar la instalación mediante el sistema de gestión de paquetes de tu sistema operativo GNU/Linux es buena.  En particular es muy simple, por ejemplo en Debian o Ubuntu
simplemente uno escribe:

```bash
  apt-get install virtualbox dkms vagrant
```

Si las versiones que consigues de esa manera alcanzan en tu trabajo, por favor, no sigas leyendo este artículo.  Si necesitas las versiones actuales
de cada paquete, entonces la instalación desde el gestor de paquetes tal vez no alcance, sigue leyendo.

Vamos a instalar entonces primero Virtualbox, luego Vagrant y a continuación algunos plugins muy útiles de Vagrant.


## Instalación de Virtualbox

Debemos buscar paquete apropiado a arquitectura y cpu en [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

Son dos:
1. VirtualBox platform package
2. Oracle VM VirtualBox Extension Pack

Al momento de escribir esto la versión estable es la 5.1.4, pero la versión de Vagrant no la admite, así que vamos a instalar la versión 5.0.26, tomada desde
[https://www.virtualbox.org/wiki/Download_Old_Builds_5_0](https://www.virtualbox.org/wiki/Download_Old_Builds_5_0)

La instalación en sistemas GNU/Linux está documentada en [https://www.virtualbox.org/wiki/Linux_Downloads](https://www.virtualbox.org/wiki/Linux_Downloads)

La instalación para sistemas MS Windows es un programa ejecutable que se debe descargar y hacer funcionar en el sistema anfitrión.

Los pasos a seguir para instalar Virtualbox son:

1. Agregar una fuente de paquetes .deb en APT.
2. Instalar la clave pública de Oracle con la cual están firmados digitalmente los paquetes de ese repositorio del punto anterior.
3. Actualizar la lista de paquetes conocida por APT.
4. Instalar el paquete .deb de virtualbox.
5. Instalar el paquete `dkms` en Debian y Ubuntu para que cuando se actualiza de manera rutinaria el núcleo del sistema operativo, se hagan las compilaciones de módulos de Virtualbox necesarias, de manera automática.

Luego procedemos a instalar el Oracle VM VirtualBox Extension Pack.

1. Descargamos el archivo del Extension Pack.
2. Usamos `VBoxManage` para instalar el pack dentro del Virtualbox.

Para evitar errores y acciones manuales, escribí un _script_ en Bash que automatiza todas estas tareas.  Sólo hace falta proporcionarle el valor de las versiones que se buscan, y lo demás se realiza sin tropiezos.  Las variables de marras son:

```bash
VB_MayorVersion=5.0
VB_MinorVersion=26
VB_EXTPACK_ReleaseNumber=108824
```
y sus valores se obtienen de la página [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads) antes mencionada. Por ejemplo, el enlace de descarga de las extensiones apunta a un archivo de nombre `Oracle_VM_VirtualBox_Extension_Pack-5.0.26-108824.vbox-extpack` y de allí se obtiene el `108824` mencionado en la variable `VB_EXTPACK_ReleaseNumber`.



## Instalación de Vagrant

De igual manera que en el caso de Virtualbox, accedemos a la página de descargas de Vagrant en
[https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html)  y buscamos el paquete apropiado a la arquitectura y cpu.

Al momento de escribir esto, la última versión estable es la 1.8.1.

A diferencia de Virtualbox, no vamos a instalar una fuente de paquetes de APT, sino solamente descargar el archivo del paquete .deb de vagrant y luego
lo instalaremos con `dpkg -i`.

Al igual que en el caso de Virtualbox, a los fines de evitar errores, en el _script_ hay una sección que hace estas tareas, y sólo hay que proporcionarle
la versión de vagrant en una variable, como se muestra a continuación:

```bash
VAG_Version=1.8.1
```

## Instalación de plugins en Vagrant

Los plugins son mecanismos de extensión que posee Vagrant para incorporar comportamiento adicional.

Una lista de los actualmente disponibles se puede encontrar en [https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Plugins](https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Plugins).

Los dos plugins que vamos a instalar son:

* vagrant-vbguest actualiza las _guest additions_ de VirtualBox si es necesario
* vagrant-proxyconf configura la VM para que use las variables de entorno de proxy del anfitrión. Esto es fundamental si tu acceso a Internet es mediante un proxy corporativo.

La forma de instalar plugins es muy simple, en nuestro caso:

```bash
  vagrant plugin install vagrant-vbguest vagrant-proxyconf
```

En el caso de `vagrant-proxyconf` vamos a agregar a la configuración global de la cuenta de usuario que utilizamos lo siguiente en `~/.vagrant.d/Vagrantfile`:

```ruby
Vagrant.configure("2") do |config|
  puts "proxyconf..."
  if Vagrant.has_plugin?("vagrant-proxyconf")
    puts "find proxyconf plugin !"
    if ENV["http_proxy"]
      puts "http_proxy: " + ENV["http_proxy"]
      config.proxy.http     = ENV["http_proxy"]
    end
    if ENV["https_proxy"]
      puts "https_proxy: " + ENV["https_proxy"]
      config.proxy.https    = ENV["https_proxy"]
    end
    if ENV["no_proxy"]
      config.proxy.no_proxy = ENV["no_proxy"]
    end
  end
end
```

## El script completo de instalación

Para lograr un entorno de Vagrant + Virtualbox repetible en diferentes estaciones de trabajo donde nos
toque desempeñarnos, resulta más adecuado si en lugar de correr los mandatos manualmente, los englobamos
en un pequeño programa en Bash.

Se puede ver en el código que se intentó realizar un control de errores
en las acciones, informando cuando alguna no se puede llevar a cabo.

Además hay un rudimento de idempotencia, pues antes de realizar una acción (descargar un archivo, instalar un paquetes)
se trata de verificar si ya fue realizada con anterioridad, para evitar repetirla innecesariamente.

El control de errores y la idempotencia agrega «ruido» a las simples instrucciones de instalación, lo cual hace que
ya no sean tan fáciles de leer.  En otra oportunidad veremos cómo usar una herramienta más apropiada a las instalaciones,
llamada Ansible, la cual incorpora de fábrica estas importantes características.

A continuación, toma un momento para revisar el programa y si necesitas virtualización hecha simple, hazlo correr.

```bash
#!/bin/bash

# buscar paquete apropiado a arquitectura y cpu en https://www.vagrantup.com/downloads.html
#
VAG_Version=1.8.1


# buscar paquete apropiado a arquitectura+cpu y que sea admitido por Vagrant en https://www.virtualbox.org/wiki/Downloads
# son dos:
#    1. VirtualBox platform package
#    2. VirtualBox Oracle VM VirtualBox Extension Pack
#

##
# info de la version del Virtualbox
VB_MayorVersion=5.0
VB_MinorVersion=26

##
# release number del Oracle Virtualbox Extension Pack
VB_EXTPACK_ReleaseNumber=108824

#######################################
##
# no hay mas cambios desde esta linea hacia abajo
#

##
# la distro donde se van a instalar los paquetes Virtualbox y Vagrant:
distro=`lsb_release -d | awk '{print $2}'`
release=`lsb_release -d | awk '{print $3}'`
codename=`lsb_release -c | awk '{print $2}'`
arch=`arch`


error() {
  echo $* >&2
  exit 1
}


oracle_pubkey() {
  if [ $codename == "trusty" -o $codename == "wheezy" ] ; then echo oracle_vbox.asc      ; return 0; fi
  if [ $codename == "xenial" -o $codename == "jessie" ] ; then echo oracle_vbox_2016.asc ; return 0; fi

  error "no se puede determinar cual es la clave de APT de Oracle para distro:"${distro}" y codename: "${codename}
}


instalo_virtualbox() {

  # verifico si no esta ya instalado
  dpkg -l  virtualbox-${VB_MayorVersion} >/dev/null ; VB_INSTALADO=$?
  if [ 0 -ne "${VB_INSTALADO}" ] ; then
    Oracle_pubkey_filename=`oracle_pubkey`

    # fuente de paquetes de Oracle para Virtualbox
    sudo bash -c "echo 'deb http://download.virtualbox.org/virtualbox/debian '${codename}' contrib' > /etc/apt/sources.list.d/virtualbox.list"

    # The Oracle public key for apt-secure:
    wget -q https://www.virtualbox.org/download/${Oracle_pubkey_filename} -O- | sudo apt-key add -

    # actualizo lista de paquetes
    sudo apt-get update

    # instalo Virtualbox y dkms to ensure that the VirtualBox host kernel modules (vboxdrv, vboxnetflt and vboxnetadp) are properly updated if the Linux kernel version changes during the next apt-get upgrade.
    sudo apt-get install -y --force-yes virtualbox-${VB_MayorVersion} dkms ; ret=$?
    [ 0 -eq "$ret" ] || error "no se pudo instalar dkms y "virtualbox-${VB_MayorVersion}

  fi
}


instalo_oracle_extension_pack() {

  VB_BASE_URL=http://download.virtualbox.org/virtualbox/${VB_MayorVersion}.${VB_MinorVersion}
  VB_EXTPACK_FILENAME=Oracle_VM_VirtualBox_Extension_Pack-${VB_MayorVersion}.${VB_MinorVersion}-${VB_EXTPACK_ReleaseNumber}.vbox-extpack

  # verifico si no esta ya instalado
  if [ 0 -eq `sudo VBoxManage list extpacks | awk '/Extension Packs:/ {print $3} '` ] ; then
    [ -r ${VB_EXTPACK_FILENAME} ] || wget -q ${VB_BASE_URL}/${VB_EXTPACK_FILENAME} ; ret=$?
    [ 0 -eq "$ret" ] || error "no se pudo descargar el extension pack: "${VB_BASE_URL}/${VB_EXTPACK_FILENAME}

    # instalo el Extension Pack
    sudo VBoxManage extpack install ${VB_EXTPACK_FILENAME} 2>/dev/null ; ret=$?
    [ 0 -eq "$ret" ] || error "no se pudo instalar el extension pack: "${VB_EXTPACK_FILENAME}

    #sudo VBoxManage list extpacks
    #sudo VBoxManage extpack uninstall "Oracle VM VirtualBox Extension Pack"
  fi

}


instalo_vagrant() {
  VAG_BASE_URL=https://releases.hashicorp.com/vagrant/${VAG_Version}
  VAG_PKG_NAME=vagrant_${VAG_Version}_${arch}.deb

  # verifico si no esta ya instalado
  dpkg -l vagrant >/dev/null ; VAG_INSTALADO=$?
  if [ 0 -ne "${VAG_INSTALADO}" ] ; then

    [ -r ${VAG_PKG_NAME} ] || wget -q ${VAG_BASE_URL}/${VAG_PKG_NAME} ; ret=$?
    [ 0 -eq "$ret" ] || error "no se pudo descargar vagrant: "${VAG_BASE_URL}/${VAG_PKG_NAME}

    sudo dpkg -i ${VAG_PKG_NAME} ; ret=$?
    [ 0 -eq "$ret" ] || error "no se pudo instalar "${VAG_PKG_NAME}
  fi

}


instalo_vagrant_proxyconf() {
  vagrant plugin install vagrant-proxyconf

  cat > ~/.vagrant.d/Vagrantfile << !EOF
Vagrant.configure("2") do |config|
  puts "proxyconf..."
  if Vagrant.has_plugin?("vagrant-proxyconf")
    puts "find proxyconf plugin !"
    if ENV["http_proxy"]
      puts "http_proxy: " + ENV["http_proxy"]
      config.proxy.http     = ENV["http_proxy"]
    end
    if ENV["https_proxy"]
      puts "https_proxy: " + ENV["https_proxy"]
      config.proxy.https    = ENV["https_proxy"]
    end
    if ENV["no_proxy"]
      config.proxy.no_proxy = ENV["no_proxy"]
    end
  end
end
!EOF
}


instalo_vagrant_plugins() {
  mkdir -p ~/.vagrant.d/

  instalo_vagrant_proxyconf
  vagrant plugin install vagrant-share
  vagrant plugin install vagrant-vbguest
}


##
# main
#
instalo_virtualbox
instalo_oracle_extension_pack

instalo_vagrant
instalo_vagrant_plugins

##
# luego se puede verificar la instalación con:
#
# vagrant init ubuntu/trusty32; vagrant up # para crear una VM de prueba
# vagrant ssh     # para conectarte a la VM recién creada

```

## Obtener el código fuente desde Github

Se creó un repo en Github: [https://github.com/CesarBallardini/instala-virtualbox-vagrant](https://github.com/CesarBallardini/instala-virtualbox-vagrant)

Para obtener este código fuente, debes clonar el repositorio mediante SSH o HTTPS:

```bash
  git clone git@github.com:CesarBallardini/instala-virtualbox-vagrant.git     # SSH
  git clone https://github.com/CesarBallardini/instala-virtualbox-vagrant.git # HTTPS
```


## Para crear inicialmente este proyecto

Para subir el código de este proyecto, simplemente hay que hacer:

* editar el `.gitignore` para evitar el directorio privado y el de vagrant:

```
provision/private/
.vagrant
```
* inicializar el repo git, agregar los cambios relevantes, crear el commit inicial:

```bash
  git init
  git add .
  git commit -m "instrucciones de instalacion y Vagrantfile para probarlas"
```
* crear un repo en Github, ene ste caso se creó el `instala-virtualbox-vagrant`
* poner el repo de github como origin y subir los cambios:

```bash
  git remote add origin https://github.com/CesarBallardini/instala-virtualbox-vagrant.git
  git push -u origin master
```
