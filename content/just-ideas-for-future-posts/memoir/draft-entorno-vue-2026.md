### E-05 — Mi entorno de Vue.js 3 en 2026

- **Archivo seed:** `dev/draft-vuejs3-dev-environment.md`
- **Slug propuesto:** `entorno-vue-2026`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-entorno-vue-2026/index.md`
- **Serie:** E
- **Cross-links:** lleva a [[E-04]] (Python env, mismo formato), [[E-06]] (Ollama)
- **Idioma:** es
- **Madurez:** bare-seed (archivo vacío)
- **Length target:** medium (1500-2000 palabras)

**Concepto:** complemento natural de [[E-04]] pero para el lado frontend. Vue 3 + Vite + script setup + TypeScript + Pinia + Vue Router. Y la pregunta filosófica que abre el post: ¿por qué Vue y no React, en 2026? Respuesta corta: porque Composition API es honesta y la documentación oficial es completa.

**Hook:** "en 2024 intenté volver a React. Duré dos semanas. Volví a Vue 3 con Composition API y *script setup* y la productividad volvió. No es ideología, es ergonomía. El post explica el setup completo en 2026 y por qué cada pieza está donde está."

**Outline:**
1. Por qué Vue y no React, sin pelea: dos posiciones honestas para dos tipos de proyectos.
2. El stack: Vue 3 + Vite + `<script setup>` + TypeScript + Pinia + Vue Router + VueUse.
3. `<script setup>` — la parte que cambia todo. Comparación con Options API y con Composition API "explícita".
4. Pinia vs Vuex — por qué Pinia ganó.
5. ESLint + Prettier (todavía) o Biome (experimento) — el frontend está atrasado en consolidación de tooling respecto a Python/ruff.
6. Vitest para testing. Cypress / Playwright para e2e — cuándo cada uno.
7. El template starter que uso: `pnpm create vue` con qué opciones marcadas.
8. Lo que no uso: Nuxt (excepto cuando hace falta SSR), Quasar, Vuetify (depende del proyecto).
9. Cierre: el archivo `vite.config.ts` mínimo y por qué cada plugin está ahí.

**Bibliografía:**
- [Vue.js 3 — guía oficial](https://vuejs.org/guide/introduction.html) — la mejor doc de framework frontend que existe.
- [Vite — documentación](https://vitejs.dev/).
- [Pinia — store oficial de Vue](https://pinia.vuejs.org/).
- [VueUse — colección de composables](https://vueuse.org/).
- [Vitest](https://vitest.dev/).
- [Evan You, *State of Vue 2024*](https://blog.vuejs.org/) — keynote anuales.
- [Anthony Fu, *On Reka and Building Tools*](https://antfu.me/posts/) — el blog del mantainer principal de muchas herramientas Vue.
- [Vue.js Argentina meetup](https://www.meetup.com/vuejs-argentina/) — comunidad local, frágil pero existente.

**Imágenes:**
- _Crear_: diagrama del stack con flechas de qué llama qué (~30 min).
- _Crear_: tabla comparativa Vue/React en 6 dimensiones honestas (~30 min) — esto puede ser controvertido, escribirlo con cuidado.

**Tags propuestos:** `['Vue', 'Vite', 'TypeScript', 'Pinia', 'devenv', 'frontend']`

**Estado actual:** archivo vacío; el contenido existe en mis dotfiles y en proyectos reales, sólo hay que sentarse a escribirlo.

