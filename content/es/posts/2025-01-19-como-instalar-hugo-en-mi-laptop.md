---
layout: post
title: 'Cómo instalar Hugo en mi laptop'
description: "Instalación de Hugo en una laptop con MS Windows 11"
tags: [MS Windows 11, Hugo, Jekyll, instalacion]
---

## 1. Instalamos Hugo

* https://gohugo.io/installation/windows/#chocolatey

La forma simple en una laptop con MS Windows 11 es mediante Chocolatey.
Con permisos de administrador, ejecuta:


```bash
choco install hugo-extended
```

Eso instala un solo archivo binario con el programa ejecutable.  Para ver la versión,
en una terminal de usuario normal, ejecuta:

```Powershell
hugo version
```

En mi caso, eso da:

```text
hugo v0.141.0-e7bd51698e5c3778a86003018702b1a7dcb9559a+extended windows/amd64 BuildDate=2025-01-16T13:11:18Z VendorInfo=gohugoio
```
## 2. Creamos un blog

Usaremos la Quick Start Guide: https://gohugo.io/getting-started/quick-start/

```bash
cd ~/cesar/blog/
hugo new site katra
cd katra/

git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo "theme = 'ananke'" >> hugo.toml

# Correr con alguno de los siguientes:
hugo server
hugo server --buildDrafts
hugo server --buildDrafts --disableFastRender
```

## 3. Agregar una página

```bash
hugo new content content/posts/my-first-post.md
```

Abre `content/posts/my-first-post.md` y escribe algo de contenido.


## 4. Preparamos espacio para posts en inglés, además de castellano

```bash
mkdir -p content/{es,en}/posts/
touch content/{es,en}/posts/.gitkeep
mkdir -p layouts/{es,en}/_default

mv content/posts/my-first-post.md content/es/posts/my-first-post.md
rmdir content/posts/
```

## 5. Configuración

El archivo de configuración es `hugo.toml`.  Lo dejaremos así:

```toml
baseURL = 'https://katra.ballardini.com.ar/'
copyright = 'César Ballardini'
defaultContentLanguage = "es"
enableRobotsTXT = true
resourceDir = "./resources"
sectionPagesMenu = "main"
theme = "ananke"
#theme = ["github.com/theNewDynamic/gohugo-theme-ananke"]
timeZone = 'America/Buenos_Aires'
title = 'katra'


[frontmatter]
  date = [':filename', ':default']

[languages.es]
contentDir = "content/es"
languageCode = 'es-AR'
weight = 1
title = "katra"
read_more_copy = "Leer más..."

[languages.en]
contentDir = "content/en"
languageCode = 'en-US'
weight = 2
title = "katra.en"
read_more_copy = "Read more about this entry"

[pagination]
pagerSize = 3 # this is set low for demonstrating with dummy content. Set to a higher number

[services.googleAnalytics]
id = ''

[sitemap]
changefreq = "monthly"
priority = 0.5
filename = "sitemap.xml"



[params]
author = "César Ballardini"
date_format = "02 de January de 2006"
favicon = ""
recent_posts_number = 3
show_reading_time = true
site_logo = ""
text_color = ""

# choose a background color from any on this page: https://tachyons.io/docs/themes/skins/ and preface it with "bg-"
background_color_class = "bg-black"

# choose fitting and alignment styles for the featured image using Tachyons classes such as "cover|contain" for fitting and "bg-top|bg-center|bg-bottom" for alignment, or add any other class space-separated to customize further
featured_image_class = "cover bg-top"

# choose a color dimming class for the page or site header from any on this page: https://tachyons.io/docs/themes/skins/, preface it with "bg-" and add the value such as "-X0" where X is in [1,9]
cover_dimming_class = "bg-black-60"

[params.ananke.social.share]
networks = [
  "email",
  "linkedin",
  "x-twitter",
  "github",
]

[params.ananke.social.follow]
networks = [
  "linkedin",
  "x-twitter",
  "github",
]

[params.ananke.social.email]
username = "cesar.ballardini@gmail.com"

[params.ananke.social.linkedin]
username = "cesarballardini"

[params.ananke.social.x-twitter]
username = "cesarballardini"
# https://x.com/cesarballardini

[params.ananke.social.github]
username = "Cesar.Ballardini"
# https://github.com/CesarBallardini

[params.ananke.social.facebook]
username = "cesar.ballardini"
# profilelink = "https://www.facebook.com/cesar.ballardini"

```

* Subtítulo para las entradas en: `content/es/posts/_index.md`

```yaml
---
title: 'Entradas'
description: 'el espíritu y la tecnología de la información'
---
```

* El formato de la fecha de las entradas se obtiene de la configuración y se asigna en: `archetypes/default.md`

```markdown
+++
date = '{{ time.Now.Format .params.dateFormat }}'
draft = false
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
+++
```

* favicon

Elegir uno, en mi caso fue https://favicon.io/emoji-favicons/slightly-smiling-face/

Descargarlo y copiarlo dentro de `public/`
