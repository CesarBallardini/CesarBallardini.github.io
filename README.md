# katra

[![Deploy static content to Pages](https://github.com/CesarBallardini/CesarBallardini.github.io/actions/workflows/static.yml/badge.svg)](https://github.com/CesarBallardini/CesarBallardini.github.io/actions/workflows/static.yml)

Blog personal de César Ballardini — **<https://katra.ballardini.com.ar/>**

## Por qué "katra"

En Star Trek, la *katra* es la esencia viviente de una persona: todo lo que fue, todo lo que aprendió, todo lo que pensó, transferible a otra mente. Un blog es más o menos eso — un lugar donde depositar lo que uno sabe, lo que aprendió, lo que le llamó la atención, para que sobreviva fuera de la cabeza de uno. Cada post es un pedacito de katra. La historia completa está en [¿Por qué katra?](https://katra.ballardini.com.ar/posts/por-que-katra/).

## Qué vas a encontrar

Contenido mayormente en castellano (es-AR), con una sección en inglés que traduce algunos posts (no un espejo 1:1). Los temas rondan alrededor de la arqueología de lenguajes de programación, la familia Lisp, filosofía de la ingeniería de software, pioneros del cómputo, arquitectura como CS (IaC/deploy), sistemas legacy, memoria local de la computación (Argentina/LATAM), curiosidades nerd laterales, y vida y trabajo en general.

## Stack técnico

- **[Hugo](https://gohugo.io/)** como generador estático.
- Tema **[Ananke](https://github.com/theNewDynamic/gohugo-theme-ananke)**, incluido como submódulo git en `themes/ananke`.
- Deploy a GitHub Pages vía GitHub Actions (`.github/workflows/static.yml`) en cada push a `master` — no hay build de Hugo en CI, el directorio `public/` se commitea directamente.

## Desarrollo local

```bash
git clone --recursive https://github.com/CesarBallardini/CesarBallardini.github.io.git
cd CesarBallardini.github.io

hugo server          # servidor local con recarga en vivo (http://localhost:1313/)
hugo server -D       # incluye posts en borrador
hugo                 # build a ./public/
```

### Publicar el blog

No hay build de Hugo en CI — el directorio `public/` se commitea directamente, y GitHub Actions sólo lo sube a Pages tal cual está en el repo. Así que publicar es:

```bash
hugo --cleanDestinationDir   # rebuild limpio, elimina archivos huérfanos de builds previos
git add -u public/ public/**
git add public/              # si hay posts nuevos (archivos sin trackear)
git commit -m "..."
git push
```

- **Nunca commitear un build de `hugo server`** — reescribe el `baseURL` al puerto local y lo mete en cada canonical/og:url/RSS/sitemap. Siempre rebuildear con `hugo --cleanDestinationDir` (o `rm -rf public && hugo`) antes de commitear.
- **Verificar antes de commitear**: `grep -rl "localhost:" public/ | wc -l` tiene que dar `0`.
- Si se corrió `hugo` de nuevo después de un `git add public/`, el rebuild pisa lo que estaba staged — re-stagear con `git add -u public/` (más los archivos nuevos) antes del commit.

Los detalles completos de arquitectura, convenciones de contenido y el sistema de planificación editorial están en [`CLAUDE.md`](CLAUDE.md).
