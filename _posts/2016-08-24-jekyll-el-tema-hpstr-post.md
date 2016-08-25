---
layout: post
title: 'Jekyll: El tema HPSTR'
description: "El tema HPSTR en el blog."
tags: [blog, jekyll, theme, tema, hpstr]
---

HPSTR es un tema de Jekyll que usa SCSS y requiere Jekyll 3.x.

Los pasos de instalación están descriptos en [las instrucciones de instalación de este tema](https://mmistakes.github.io/hpstr-jekyll-theme/theme-setup/) y los voy a adaptar al entorno de VM que hemos construído antes.

Luego de levantar nuestra VM con Jekyll instalado, nos conectamos a nuestra cuenta en Github y hacemos un fork del [repo del tema](https://github.com/mmistakes/hpstr-jekyll-theme/) en Github.

Para crear un sitio Web en Github, las instrucciones están muy claras en el tutorial de [github-pages](http://jmcglone.com/guides/github-pages/).

Vamos a tratar primero el caso inicial, cuando por primera vez creamos nuestro blog. Yo voy a referir mi cuenta en Github, que es ```CesarBallardini```, así que en el resto de esta serie sobre cómo tener funcionando tu blog jekyll + HPSTR, vas a tener que cambiar este nombre de cuenta por el tuyo. Así también sucederá con mi nombre y apellido, y dirección de correo electrónico. 

Debemos crear el repo ```CesarBallardini.github.io```, completamente vacío: sin ```.gitignore``` ni ```README.md```.

Clonamos el repo inicial: 

```bash
cd /vagrant/www/
git clone https://github.com/CesarBallardini/CesarBallardini.github.io
cd CesarBallardini.github.io/
```

En la VM configuramos Git, sólo para este repo:

```bash
git config user.email "cesar@ballardini.com.ar"
git config user.name "Cesar Ballardini"
```

Cargamos el tema HPSTR desde el repo propio:

```bash
git remote add hipster https://github.com/CesarBallardini/hpstr-jekyll-theme.git
git fetch hipster master
git merge hipster/master -m "incorporo HPSTR al repo de jekyll"
```

Ahora tenemos dos alternativas: verlo localmente, para tener una visualización previa de cómo va a quedar el blog, y la otra posibilidad es subirlo a Github para hacerlo público.

## Localmente desde la VM

Para verlo localmente, usaremos el programa jekyll, ya instalado en la VM, nos aseguramos de instalar las gemas requeridas como dependencias:

```bash
bundle install
```

Y lo publicamos localmente:
```bash
bundle exec jekyll build
bundle exec jekyll serve --host 192.168.33.10 --incremental
```
Queda accesible en [http://192.168.33.10:4000/](http://192.168.33.10:4000/) en nuestro navegador (que es el IP configurado en el ```Vagrantfile``` en FIXME).

## Publicado en Github

Por otro lado. lo podemos publicar en Github (aquí nos solicitará nuestro nombre de usuario y contraseña en Github):

La primera vez desconecto el _tracking_ de la rama aguas arriba:

```bash
git branch --unset-upstream
```
Y ahora hago el push hacia Github:

```bash
git push origin master
```

Y accederlo desde allí en: [http://cesarballardini.github.io/](http://cesarballardini.github.io/)

