### E-11 — De Jekyll a Hugo: cómo migré mi blog y por qué (con 2 anécdotas de Vagrant + Windows 11)

- **Archivo seed (repo POC):** [github.com/CesarBallardini/jekyll-vagrant](https://github.com/CesarBallardini/jekyll-vagrant) — Shell, último push 2023-04-21
- **Slug propuesto:** `jekyll-a-hugo-migracion-blog`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-jekyll-a-hugo-migracion-blog/index.md`
- **Serie:** E
- **Cross-links:** lleva a [[E-12]] (patrón Vagrant+Ansible), [[G-19]] (Vagrant en Windows 11 — la anécdota del Ctrl-C); también referencia al blog mismo (este blog, katra)
- **Idioma:** es
- **Madurez:** seed-físico (el repo `jekyll-vagrant` es la time-capsule del blog *anterior*, antes de la migración a Hugo)
- **Length target:** medium (1500-2200 palabras)

**Concepto:** este blog (katra) está en Hugo desde hace un tiempo. Antes estaba en Jekyll, y antes de eso era... otra cosa. La migración no fue por moda — fue por dolor: Jekyll es Ruby, las dependencias son frágiles, las builds son lentas, y mantener un entorno de desarrollo Jekyll en Windows 11 requería una VM Vagrant con un script `vagrant-ssh.sh` para hacer Ctrl-C funcionar. Hugo es un binario Go autocontenido, build de un blog medio en menos de un segundo, sin dependencias externas. El post cuenta el dolor del setup viejo, el momento de la decisión, qué me tomó migrar, y los dos errores que tuve que corregir después.

**Hook:** "este blog estaba en Jekyll. Funcionaba. Pero cada vez que quería editar un post tenía que arrancar una VM Vagrant porque Jekyll en Windows 11 era un infierno de gemas, Bundler y locks. Migré a Hugo: un binario Go que cabe en 30 MB, sin Ruby, sin gemas, sin VMs. La migración me llevó dos tardes. No me arrepiento ni un poco. Acá cuento por qué."

**Outline:**
1. Qué tenía antes: Jekyll + GitHub Pages + el repo `jekyll-vagrant` con una VM Ubuntu.
2. Por qué la VM era necesaria: Jekyll/Bundler en Windows + Ruby + gems con extensiones C nativas + la imposibilidad práctica de mantener un Gemfile.lock estable. La VM aislaba todo eso.
3. La anécdota del Ctrl-C: en Windows 11, `vagrant ssh` no propaga bien los signals al proceso remoto. Mi solución fue un script `vagrant-ssh.sh` que usa `vagrant ssh-config` para sacar los parámetros y abrir directamente con `ssh` nativo.
4. El día que se rompió Jekyll por un cambio de gem y dije "no más".
5. La decisión Hugo: por qué Hugo y no Eleventy, Astro, Zola, etc. La razón principal: *binario único, cero dependencias*.
6. La migración: convertir layouts Jekyll a Hugo (mismo concepto, sintaxis distinta), migrar frontmatter (YAML compatible), revisar URLs (la trampa: el comportamiento de slugs y tags no es idéntico), elegir tema (Ananke para no diseñar nada).
7. Lo que se rompió: tags con puntos (regla `AGENTS.md` documentada en el plan, ver [Convenciones](#convenciones-de-la-casa)), URLs con prefijo `/es/` (no necesario), unsafe HTML en algunos posts.
8. Lo que se ganó: build en menos de 1 segundo, *cero* dependencias para editar.
9. Cierre: la VM Vagrant de Jekyll sigue siendo útil como time-capsule. Y a alguien, en algún momento, va a salvarle el día.

**Bibliografía:**
- Repo del POC histórico: [CesarBallardini/jekyll-vagrant](https://github.com/CesarBallardini/jekyll-vagrant) — el setup pre-Hugo.
- Repo del blog actual: [CesarBallardini/CesarBallardini.github.io](https://github.com/CesarBallardini/CesarBallardini.github.io).
- [Hugo — sitio oficial](https://gohugo.io/).
- [Jekyll — sitio oficial](https://jekyllrb.com/).
- [Ananke — Hugo theme](https://github.com/theNewDynamic/gohugo-theme-ananke).
- [Bjorn Stierand, *Migrating from Jekyll to Hugo*](https://bjornstierand.com/blog/2020/migrating-from-jekyll-to-hugo/) — referencia para checklist de migración.
- [Vagrant docs — `ssh` command](https://developer.hashicorp.com/vagrant/docs/cli/ssh).

**Imágenes:**
- _Crear_: gráfico de tiempo de build Jekyll vs Hugo (~10 min — un solo número, pero contundente).
- _Crear_: el script `vagrant-ssh.sh` en una caja con explicación inline (~15 min).
- _Crear_: foto del CSS antes/después si la apariencia cambió (~10 min).

**Tags propuestos:** `['Hugo', 'Jekyll', 'blog', 'migracion', 'Vagrant', 'Windows', 'memoir']`

**Estado actual:** la migración ya pasó, la time-capsule Jekyll sigue en GitHub. El post es 100% retrospectivo, baja fricción de redacción.

