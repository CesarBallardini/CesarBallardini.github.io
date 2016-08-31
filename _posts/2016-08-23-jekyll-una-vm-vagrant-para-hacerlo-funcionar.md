---
layout: post
title: 'Jekyll: una VM Vagrant para hacerlo funcionar'
description: "Una VM es un buen lugar para tener una visualización previa de lo que publicaremos."
tags: [blog, jekyll, vagrant, Vagrantfile, virtualbox, ansible, rvm, ruby, bundle]
---

Vamos a usar Vagrant para instalar Jekyll 3.x en una máquina virtual con Virtualbox, para editar y generar nuestro sitio, sin interferir con el sistema de escritorio que usemos para nuestro trabajo cotidiano.

Si no tienes instalado el combo vagrant + virtualbox, te recomiendo que lo hagas de acuerdo a las instrucciones en FIXME.

El ```Vagrantfile``` nos permite crear una VM liviana con Ubuntu 14.04 Trusty de 32 bits, con poca memoria, más que suficiente para nuestras necesidades.  El aprovisionamiento se hace en dos etapas: 1. los paquetes esenciales del sistema operativo; 2. ansible.  

El sistema operativo es todo lo necesario para que se puedan instalar paquetes, se aproveche un archivo de _swap_ por si nos quedamos cortos con la RAM asignada, y la VM queda actualizada en sus paquetes.

El ansible lo instalamos en la VM.  Esto es discutible.  Como pretendo que esta VM corra, se instale y se configure sin importar el software del equipo host, no puedo asegurar que ansible funciona o siquiera es instalable en el host.  Lo instalamos en la VM y hacemos que sea su propia máquina de control ansible. Cómo correr ansible para que ejecute todas las instalaciones es algo que documentamos en ```provision/ansible-setup.sh``` que es un _oneliner_. Todas las rutas de los archivos serán relativas a la ubicación del ```Vagrantfile```.

Luego hay que correr el playbook que instala las dependencias de Jekyll y el propio Jekyll.

Otro playbook se ocupa de hacer el deploy del sitio estático, y de subirlo a Github.

Vamos a ver cada una de estas cosas en detalle.

## ```Vagrantfile```
 
El ```Vagrantfile``` simplemente descarga un _box_ estándar de Ubuntu, le asigna una dirección IP y tamaño de memoria adecuado a las necesidades.  Se crea un directorio ```www/``` en el host, que se mapea dentro de la VM para que sea el lugar donde se aloje el contenido del Web server.

También se invocan cuatro scripts para el aprovisionamiento:

 * ```provision/os-setup.sh``` instala lo esencial del sistema operativo para que funcione en la locación de instalación (_proxies_, fuentes de paquetes Debian, _swap_, _hostname_, etc.)
 * ```provision/ansible-setup.sh``` (instala ansible)
 * ```provision/ansible-playbook-install.sh``` (instala roles y el playbook a usar)
 * ```provision/ansible-setup.sh``` (corre ansible para instalar Jekyll)

```ruby
VAGRANTFILE_API_VERSION = "2"
arch= "i386" ; bits="32" ; distro="trusty"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define "github-pages"+bits do |base|
    base.vm.box = "ubuntu/"+distro+bits
    base.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/"+distro+"-server-cloudimg-"+arch+"-vagrant-disk1.box"
    base.vm.hostname = "jk.dev"
    base.vm.provision "shell", path: "provision/os-setup.sh", privileged: true
    base.vm.provision "shell", path: "provision/ansible-setup.sh", privileged: true
    base.vm.provision "shell", path: "provision/ansible-playbook-install.sh", privileged: false
    base.vm.provision "shell", path: "provision/ansible-run.sh", privileged: false
    base.vm.network "forwarded_port", guest: 4000, host: 4000
    base.vm.network "private_network", ip: "192.168.33.10"
    base.vm.synced_folder "www/", "/srv/www", create: true
    base.ssh.forward_agent = true
    base.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--nictype1", "Am79C973"]
      vb.customize ["modifyvm", :id, "--nictype2", "Am79C973"]
      vb.customize ["modifyvm", :id, "--memory", 512]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
      vb.gui = false
      vb.name = "Jekyll Blog Vagrant "+arch+" arch"
      vb.memory = "512"
    end
  end
end
```

## El aprovisionamiento del sistema operativo básico

No hay mucho más que comentar en el código siguiente.  *Use the source, Luke!*

Creamos un directorio ```provision/``` donde residirá todo el código de aprovisionamiento en shell, y un directorio ```provision/ansible/``` donde estarán roles, configuración y playbooks de ansible.

```bash
mkdir -p provision/ansible
```

El ```provision/os-setup.sh``` será el siguiente:

```bash
#!/bin/bash
#
##
# provision/os-setup.sh
# instala lo necesario a nivel de sistema operativo
#

##
# Parametros de la VM
#
# vm_hostname: nombre de host dentro de la VM
vm_hostname=jk.dev

# vm_swapfilesize: si esta vacio no se crea area de swap en la VM
vm_swapfilesize=2G

##
# TODO: poner en configuracion de la ubicacion de trabajo
# Estos sources son para instalaciones con acceso a un mirror interno:
# si se hace un noop, se usan los que vienen configurados en la VM desde el vagrant box usado
#
aseguro_sources_list() {
  wget http://mirror.EXAMPLE.COM/listas/sources.list.14.04 -O /etc/apt/sources.list
  : 
}

############################################
##
# no hay mas que modificar desde esta linea hacia abajo
##

distro=`lsb_release -d | awk '{print $2}'`
release=`lsb_release -d | awk '{print $3}'`

aseguro_config_apt() {
  aseguro_sources_list
  apt-get    update
}

actualizo_paquetes_sistema() {
  apt-get    update
  apt-get -y upgrade
  apt-get -y autoremove
  apt-get -y dist-upgrade
  apt-get -y --force-yes autoremove
  apt-get -y autoclean
}

aseguro_un_minimo_espacio_de_swap() {
  vm_swapfilesize=$1

  if [ -n "${vm_swapfilesize}" ]
  then
    fallocate -l ${vm_swapfilesize} /swapfile
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile
    # swapon -s  # verificar que el swap funciona
    echo '/swapfile   none    swap    sw    0   0' >> /etc/fstab
  fi
}


mejoras_en_performance() {
  sysctl vm.swappiness=10
  echo 'vm.swappiness=10' > /etc/sysctl.conf

  sysctl vm.vfs_cache_pressure=50
  echo 'vm.vfs_cache_pressure = 50' > /etc/sysctl.conf
}

set_hostname() {
  echo '127.0.0.1   '$1 >> /etc/hosts
}

instalo_keyring() {
  [ $release == "Debian" ] && apt-get install -y debian-keyring
  [ $release == "Ubuntu" ] && apt-get install -y --force-yes ubuntu-keyring ubuntu-extras-keyring
}

instalo_paquetes_esenciales() {
  apt-get install -y --force-yes debconf-utils
  apt-get install -y --force-yes python-software-properties build-essential
  apt-get install -y --force-yes git
}

###################################
##
# main
#
aseguro_config_apt
aseguro_un_minimo_espacio_de_swap ${vm_swapfilesize}
mejoras_en_performance
set_hostname ${vmhostname}

instalo_keyring
instalo_paquetes_esenciales
actualizo_paquetes_sistema
# EOF
```


## Instalación de Ansible

Este _script_ corre con privilegios de *root* y se ocupa de instalar la fuente de paquetes en Ubuntu (FIXME para otros S.O.) necesarios para instalar la versión estable más moderna de ansible.

```bash
#!/bin/bash
#
##
# provision/ansible-setup.sh
# instala lo necesario para que funcione ansible
#

apt-get install -y python-software-properties build-essential
apt-add-repository -y ppa:ansible/ansible
apt-get update
apt-get install ansible -y
```

## Instalación de Jekyll y sus dependencias

Vamos a usar playbooks de ansible para realizar la instalación de Jekyll y sus dependencias.

El primer paso es asegurar la configuración de ansible, la cual requiere un archivo de inventario, y uno de configuración global.

El inventario se denomina jk.inventory y su contenido es un grupo denominado jk, donde sólo reside la identificación de la VM (jk.dev) con una conexión local, para evitar el uso de SSH:

```ini
[jk]
jk.dev  ansible_connection=local
```

El archivo de configuración de ansible se denomina ```ansible.cfg```, y se instala localmente en el directorio de trabajo, para que se use en lugar del archivo global a nivel de sistema.  En nuestro caso está casi vacío de contenido y sólo tiene las líneas:

```ini
[defaults]
roles_path    = ./roles

[privilege_escalation]
[paramiko_connection]
[ssh_connection]
[accelerate]
[selinux]
```

Para ejecutar ansible usaremos el mandato ```provision/ansible-run.sh```:

```bash
cd /vagrant/provision/ansible
time ansible-playbook -vv -i jk.inventory instala-jekyll.yml
```

## Cómo crear el playbook de instalación de Jekyll

Primero debemos instalar los roles necesarios desde Ansible Galaxy:

```bash
cd /vagrant/provision/ansible/roles/
ansible-galaxy install rvm_io.rvm1-ruby
ansible-galaxy install igor_mukhin.jekyll
```

Nuestro playbook de instalación será: ```instala-jekyll.yml```

```yaml
- hosts: jk
  vars:
    jekyll_version: 3.2.1

  roles:
    - {role: rvm_io.rvm1-ruby, rvm1_gpg_key_server: 'hkp://keyserver.ubuntu.com:80' }
    - {role: igor_mukhin.jekyll, tags: jekyll, become: true }
```


Nota: Un problema de permisos en la creación de symlinks en roles/rvm_io.rvm1-ruby/tasks/rubies.yml se resuelve usando privilegios de administrador en el task, que debería quedar (cerca de la línea 54):

```yaml
- name: Symlink ruby related binaries on the system path
  file:
    state: 'link'
    src: '{{ rvm1_install_path }}/wrappers/default/{{ item }}'
    dest: '{{ rvm1_symlink_to }}/{{ item }}'
    owner: 'root'
    group: 'root'
  when: not '--user-install' in rvm1_install_flags
  with_items: '{{ rvm1_symlink_binaries }}'
  become: yes
```

Todos estos pasos los englobaremos en un script bash para que corra al momento del aprovisionamiento, ```provision/ansible-playbook-install.sh``` es:

```bash
#!/bin/bash
#
##
# provision/ansible-playbook-install.sh
# instala roles, playbboks y variables
#

##
# playbook de instalacion de software
#
cat > /vagrant/provision/ansible/instala-jekyll.yml <<!EOF
- hosts: jk
  vars:
    jekyll_version: 3.2.1

  roles:
    - {role: rvm_io.rvm1-ruby, rvm1_gpg_key_server: 'hkp://keyserver.ubuntu.com:80' }
    - {role: igor_mukhin.jekyll, tags: jekyll, become: true }

!EOF

##
# instalo roles
#

mkdir -p /vagrant/provision/ansible/roles/
cd /vagrant/provision/ansible/

ansible-galaxy install rvm_io.rvm1-ruby
ansible-galaxy install igor_mukhin.jekyll

##
# emparcho rvm_io.rvm1-ruby, sino da problema de permisos al crear los symlinks
#
[ -z "$( sed -n -e "63p"  /vagrant/provision/ansible/roles/rvm_io.rvm1-ruby/tasks/rubies.yml )" ] \
  && sed -i '63i\ \ become: yes' /vagrant/provision/ansible/roles/rvm_io.rvm1-ruby/tasks/rubies.yml
```

