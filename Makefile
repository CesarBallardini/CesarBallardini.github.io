# Makefile del blog katra (Hugo + Ananke).
#
# Nada de esto toca git más allá de leer: no hay add, commit ni push. Publicar
# lo hace César a mano; `make publish-steps` imprime la secuencia.
#
# Variables que se pueden pasar en la línea de comandos:
#   POST=<bundle>   directorio del post, p. ej. 2026-10-21-un-lenguaje-que-solo-lee-el-llm
#   IDIOMA=es|en    idioma del post (por defecto es)
#   POSTS="a.md b.md"  archivos a revisar; por defecto, los index.md de posts
#                      modificados o nuevos según `git status`
#   FUTURE=1        `make build` con --buildFuture
#
# Ajustes propios de la máquina (por ejemplo la ruta de node) van en local.mk,
# que no se commitea.

SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:

-include local.mk

# Que los scripts escriban UTF-8 aunque la consola de Windows no lo sea.
export PYTHONIOENCODING := utf-8

HUGO   ?= hugo
PYTHON ?= uv run python
NODE   ?= node
NPM    ?= npm

IDIOMA ?= es
DATE   ?= $(shell date +%Y-%m-%d)
POST   ?=
SLUG   ?=
FUTURE ?=

CHECK_DIR := .check/site
BUNDLE    := content/$(IDIOMA)/posts/$(POST)
# El URL sale del nombre del bundle sin la fecha.
POST_SLUG  = $(shell echo '$(POST)' | sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}-//')
# hugo.exe necesita una ruta de Windows; en Linux o macOS, pwd alcanza.
PUBLIC_ABS := $(shell pwd -W 2>/dev/null || pwd)/public

CHANGED := $(shell git ls-files --modified --others --exclude-standard -- 'content/*/posts/*/index.md' 2>/dev/null)
POSTS   ?= $(if $(POST),$(BUNDLE)/index.md,$(CHANGED))

SPELL := $(NODE) .cspell/node_modules/cspell/bin.mjs -c .cspell/cli.json --no-progress

.PHONY: help setup spell-install serve serve-drafts serve-future new future drafts \
        build build-one files verify check check-site urls mermaid spell clean publish-steps

help: ## Esta ayuda
	@grep -hE '^[a-z-]+:.*## ' $(firstword $(MAKEFILE_LIST)) | sed -E 's/^([a-z-]+):.*## /\1:/' \
	  | awk '{ n = index($$0, ":"); printf "  \033[36m%-14s\033[0m %s\n", substr($$0, 1, n - 1), substr($$0, n + 1) }'

# --- Preparación -------------------------------------------------------------

setup: spell-install ## Después de clonar: el tema (submódulo) y el corrector
	git submodule update --init --recursive

spell-install: ## Instala cspell y el diccionario español en .cspell/node_modules
	cd .cspell && $(NPM) ci --no-audit --no-fund

# --- Escribir ----------------------------------------------------------------

serve: ## Servidor local con recarga (http://localhost:1313/). Nunca commitear lo que genera
	$(HUGO) server

serve-drafts: ## Igual, con borradores y posts con fecha futura
	$(HUGO) server -D --buildFuture

serve-future: ## Igual, con posts con fecha futura
	$(HUGO) server --buildFuture

new: ## Post nuevo: make new SLUG=mi-post [IDIOMA=en] [DATE=2026-11-01]
	@test -n "$(SLUG)" || { echo "Falta SLUG=..."; exit 1; }
	$(HUGO) new content/$(IDIOMA)/posts/$(DATE)-$(SLUG)/index.md

future: ## Posts que Hugo deja afuera sin avisar porque su fecha es futura
	$(HUGO) list future

drafts: ## Posts marcados como borrador
	$(HUGO) list drafts

# --- Construir ---------------------------------------------------------------

build: ## Reconstruye public/ con todo lo que hay en content/ [FUTURE=1]
	@if [ -n "$$($(HUGO) list future | tail -n +2)" ] && [ -z "$(FUTURE)" ]; then \
	  echo "Aviso: hay posts con fecha futura que no van a salir (make future; FUTURE=1 para incluirlos)."; fi
	$(HUGO) --cleanDestinationDir $(if $(FUTURE),--buildFuture)
	@$(MAKE) --no-print-directory verify

build-one: ## Reconstruye public/ con lo commiteado más un solo post: make build-one POST=<bundle>
	@test -n "$(POST)" || { echo "Falta POST=<bundle>"; exit 1; }
	@test -d "$(BUNDLE)" || { echo "No existe $(BUNDLE)"; exit 1; }
	T=$$(mktemp -d); trap 'rm -rf "$$T"' EXIT; \
	git archive HEAD | tar -x -C "$$T"; \
	cp -r themes/ananke/. "$$T/themes/ananke/"; \
	rm -rf "$$T/$(BUNDLE)"; cp -r "$(BUNDLE)" "$$T/content/$(IDIOMA)/posts/"; \
	$(HUGO) -s "$$T" -d "$(PUBLIC_ABS)" --cleanDestinationDir
	@$(MAKE) --no-print-directory verify

files: ## Qué publica el bundle de un post: make files POST=<bundle>
	@test -n "$(POST)" || { echo "Falta POST=<bundle>"; exit 1; }
	@find "public/$(if $(filter en,$(IDIOMA)),en/)posts/$(POST_SLUG)" -type f | sort

verify: ## Revisa public/: enlaces internos, notas al pie, livereload y localhost
	$(PYTHON) tools/check_site.py public

# --- Revisar antes de publicar -----------------------------------------------

check: future check-site mermaid spell ## Todas las revisiones locales (no consulta las URL externas)

check-site: ## Construye todo lo de content/ en .check/ y revisa enlaces y notas al pie
	$(HUGO) --buildFuture --cleanDestinationDir -d $(CHECK_DIR) --quiet
	$(PYTHON) tools/check_site.py $(CHECK_DIR)

urls: ## URL externas de POSTS (o POST=<bundle>): responden o no
	@test -n "$(strip $(POSTS))" || { echo "Nada que revisar: no hay posts cambiados (usar POST=<bundle>)"; exit 0; }
	$(PYTHON) tools/check_urls.py $(POSTS)

mermaid: ## Valida los diagramas mermaid de POSTS contra mermaid.ink
	@test -n "$(strip $(POSTS))" || { echo "Nada que revisar: no hay posts cambiados"; exit 0; }
	$(PYTHON) tools/check_mermaid.py $(POSTS)

spell: ## Ortografía de POSTS (o POST=<bundle>) con cspell, español e inglés
	@test -n "$(strip $(POSTS))" || { echo "Nada que revisar: no hay posts cambiados"; exit 0; }
	@test -d .cspell/node_modules || { echo "Falta el corrector: make spell-install"; exit 1; }
	$(SPELL) $(POSTS)

# --- Varios --------------------------------------------------------------------

clean: ## Borra cachés y la build de revisión. public/ no se toca
	rm -rf resources/_gen .hugo_build.lock .check

publish-steps: ## Imprime la secuencia para publicar (la corre César, a mano)
	@echo "make future                      # si lista algo que tiene que salir: make build FUTURE=1"
	@echo "make build                       # o, con otros posts sin terminar: make build-one POST=<bundle>"
	@echo "make check urls POST=<bundle>"
	@echo "git add content/$(IDIOMA)/posts/<bundle>/"
	@echo "git add -u public/ && git add public/"
	@echo "git status --short               # y git diff --cached --name-only: nada ajeno"
	@echo "git commit -- content/$(IDIOMA)/posts/<bundle>/ public/"
	@echo "git push origin master"
	@echo "Nunca volver a correr hugo después del git add de public/."
