---
layout: post
title: 'Cómo mover los posts Jekyll hacia el blog Hugo'
description: "Migración de posts Jekyll a posts Hugo"
tags: [Github Pages, Hugo, Jekyll, migración]
---


En el viejo blog Jekyll las entradas (posts) residen en el directorio: `_posts`

Simplemente necesitamos copiar lo archivos del viejo blog hacia la nueva ubicación.
Nos movemos al directorio donde reside el nuevo blog:

* Obtenemos una copia del viejo blog en Jekyll

```bash

git clone https://github.com/CesarBallardini/CesarBallardini.github.io
```

* copiamos los archivos:

```bash
cp CesarBallardini.github.io/_posts/* content/es/posts
```

Y con eso es suficiente.  Ahora cuando accedemos al blog Hugo están disponibles las antiguas entradas.

