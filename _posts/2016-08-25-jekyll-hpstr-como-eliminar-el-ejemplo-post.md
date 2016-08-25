---
layout: post
title: 'Jekyll HPSTR: Cómo eliminar el ejemplo y poner tu propio contenido'
description: "Cómo vamos a escribir contenido en nuestro blog."
tags: [blog, jekyll, theme, tema, hpstr, github]
---

Nuevamente comenzamos revisando las [instrucciones](https://mmistakes.github.io/hpstr-jekyll-theme/theme-setup/) del tema HPSTR en 

Entonces, dentro de la VM:

```bash
cd /vagrant/www/CesarBallardini.github.io/
```
Eliminamos los directorios:

* `theme-setup/`
* `about/`

Mantenemos los directorios siguientes:

* `assets/` (traducir _back_ en `js/plugins/jquery.dlmenu.js`, y en `js/sripts/.min.js`)
* `images/` (dejo sólo las imágenes `apple-touch-icon-114x114-precomposed.png`, `apple-touch-icon-144x144-precomposed.png`, `apple-touch-icon-72x72-precomposed.png`, `apple-touch-icon-precomposed.png`, `twitter-card-summary-large-image.jpg`; agrego `cesarballardini.jpg`)
* `_data/` (comento los enlaces en `_navigation.yml`)
* `_includes/` (`navigation.html` traducir mensajes, `read-more.html` arreglar fechas)
* `_layouts/` (`post.html` arreglar fechas)
* `_posts/` (elimino los archivos con los posts de ejemplo)
* `_sass/` (atribución de entradas pasar a castellano en `_page.scss`)


Los siguientes, los mantenemos pero hay que personalizarlos:

* ```about/``` (elimino el directorio, lo voy a transformar en `acerca-de-mi/index.md`)
* ```posts/``` (traducir title y description en `index.html`)
* ```tags/```   (traducir title y description en `index.html`)
* ```feed.xml```
* ```index.html``` (elimino la referencia a la imagen de fondo; corrijo el link hacia _About_ y arreglo fechas)

Edito el archivo de configuración global ```_config.yml``` y queda:

```yaml
title:            katra
description:      el espíritu y la tecnología de la información
disqus_shortname: 
reading_time:     true
words_per_minute: 200
# Your site's domain goes here (eg: https://mmistakes.github.io, http://yourdomain.com, etc)
# When testing locally leave blank or use http://localhost:4000
#url: http://ballardini.com.ar/blog
#url: http://CesarBallardini.github.io
url:

# Owner/author information
owner:
  name:           César Ballardini
  avatar:         cesarballardini.jpg
  bio:            "Soy un programador de alma inquieta. Las computadoras te incitan a programar, y una vez que empiezas, no se puede detener."
  email:          cesar@ballardini.com.ar
  # Social networking links used in footer. Update and remove as you like.
  twitter:        CesarBallardini
  facebook:       
  github:         CesarBallardini
  stackexchange:  
  linkedin:       CesarBallardini
  instagram:      
  flickr:         
  tumblr:         
  # google plus id, include the '+', eg +mmistakes
  google_plus:

# Background image to be tiled on all pages
background: 

# Analytics and webmaster tools stuff goes here
google_analytics:   
google_verify:      
# https://ssl.bing.com/webmaster/configure/verify/ownership Option 2 content= goes here
bing_verify:         

# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
timezone:    America/Buenos_Aires
future:      true
highlighter: rouge
markdown:    kramdown
gems:
  - jekyll-sitemap
  - jekyll-paginate
  - jekyll-gist
  - jekyll-feed
sass:
  sass_dir: _sass
  style: compressed

# https://github.com/mojombo/jekyll/wiki/Permalinks
permalink:   /:categories/:title/

# Amount of post to show on home page
paginate: 5

kramdown:
  input: GFM
  auto_ids: true
  footnote_nr: 1
  entity_output: as_char
  toc_levels: 1..6
  enable_coderay: false

include: 
  - .htaccess
exclude: 
  - "*.less"
  - "*.sublime-project"
  - "*.sublime-workspace"
  - .asset-cache
  - .bundle
  - .jekyll-assets-cache
  - .sass-cache
  - CHANGELOG
  - Capfile
  - Gemfile
  - Gruntfile.js
  - LICENSE
  - README
  - Rakefile
  - config
  - gulpfile.js
  - lib
  - log
  - node_modules
  - package.json
  - spec
  - tmp
```


