### H-06 — La parábola del diámetro de los cohetes (la mejor metáfora del legacy que existe)

- **Archivo seed:** _histórico (eliminado 2026-04-09): `misc/draft-diametro-de-los-cohetes-trasbordador.md` tenía 3 líneas de esqueleto ("los cohetes se fabricaron lejos del lanzamiento / los llevaron por tren / los túneles se hicieron teniendo en cuenta el ancho de dos caballos"). La parábola entera ya está absorbida en este entry._
- **Slug propuesto:** `parabola-diametro-cohetes`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-parabola-diametro-cohetes/index.md`
- **Serie:** H — el corazón conceptual de la serie
- **Cross-links:** referido por casi toda la serie H ([[H-01]] [[H-02]] [[H-03]] [[H-04]] [[H-07]]); también por [[C-01]] (oxímoron) y [[B-06]] (teoría imperativa)
- **Idioma:** es
- **Madurez:** sin seed, pero la cuento de memoria
- **Length target:** short (800-1200 palabras) — el formato corto le va mejor

**Concepto:** la parábola del diámetro de los cohetes (a veces atribuida a una explicación de por qué los Solid Rocket Boosters del Space Shuttle medían 4 pies 8.5 pulgadas) es la metáfora perfecta del software legacy: cada decisión de diseño contemporánea está condicionada por una restricción anterior, que está condicionada por otra anterior, que se remonta a una decisión que ya nadie recuerda. *Roman horse asses* es el final de la cadena, casi siempre. El post cuenta la parábola, discute si la versión histórica es exacta (no del todo), y muestra por qué el principio sigue siendo cierto incluso cuando la anécdota se exagera.

**Hook:** "los Solid Rocket Boosters del Space Shuttle medían 4 pies 8.5 pulgadas de ancho. ¿Por qué? Porque viajaban en tren desde la fábrica en Utah hasta Florida. ¿Por qué los túneles de tren de EE.UU. tenían ese ancho? Porque el ancho de vía es el del Reino Unido, que es el del primer tranvía a vapor, que es el del carro pre-tranvía, que es el del carro romano, que es el ancho de la grupa de dos caballos. Resultado: la NASA, en 1980, estaba diseñando cohetes con la medida del culo de dos caballos romanos. Y vos, en 2026, estás todavía soportando un parámetro de 256 caracteres porque alguien en 1989 pensó que eso era suficiente."

**Outline:**
1. La parábola completa, narrada con cuidado.
2. La verdad histórica vs el mito: Snopes y los historiadores ferroviarios coinciden en que la versión es *parcialmente* cierta (el ancho estándar de vía sí viene de tradiciones pre-modernas; la conexión causal directa con los carros romanos está exagerada).
3. Por qué la verdad histórica importa poco: la *idea* es exacta aunque el ejemplo sea aproximado.
4. Tres ejemplos de software donde funciona la misma cadena:
   - **El año 2038 problem** — porque alguien en 1969 decidió que los timestamps Unix serían int32.
   - **El límite de 64K segments en x86** — porque Intel en 1978 quería retrocompatibilidad con el 8080.
   - **Los `\r\n` de los archivos en Windows** — porque CP/M, porque la teletype, porque el papel.
5. La conclusión correcta: el legacy no es un *defecto*, es la *evidencia material* de las decisiones que hicieron posible que algo siguiera existiendo. Reescribirlo desde cero es perder esa evidencia.
6. La conclusión incorrecta (la que la gente saca): "entonces hay que limpiarlo". No. La parábola dice exactamente lo contrario. La parábola dice: respetá la cadena.
7. Cierre: cita de Joel Spolsky sobre por qué nunca se debe reescribir.

**Bibliografía:**
- [Snopes — *Did NASA Engineers Design the Space Shuttle Booster Rockets to Be a Specific Size Because of Roman Chariots?*](https://www.snopes.com/fact-check/railroad-gauge-chariots/) — el fact-check.
- [Bill Bryson, *At Home: A Short History of Private Life*, Doubleday 2010](https://www.penguinrandomhouse.com/books/95237/at-home-by-bill-bryson/) — versión para público general.
- [George W. Hilton, *American Narrow Gauge Railroads*, Stanford University Press 1997](https://www.sup.org/books/title/?id=2353) — el libro académico sobre ancho de vía.
- [Joel Spolsky, *Things You Should Never Do, Part I*, 2000](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — el ensayo canónico.
- [Year 2038 problem — Wikipedia](https://en.wikipedia.org/wiki/Year_2038_problem).
- [x86 memory segmentation — Wikipedia](https://en.wikipedia.org/wiki/X86_memory_segmentation).
- [Tom Peters, *Excellence Isn't About Avoiding Mistakes*](https://tompeters.com/) — perspectiva adicional sobre legacy como activo.
- [Jevons paradox y *the cost of legacy* — papers IEEE](https://ieeexplore.ieee.org/) — buscar papers serios sobre el costo del legacy.

**Imágenes:**
- _Crear_: línea de tiempo visual: caballo romano → carro → tranvía → tren → vagón de carga → SRB de la NASA (~1 hora — esta imagen es la *piéce de résistance* del post).
- _Wikimedia_: foto del SRB siendo transportado en tren — disponible en commons.
- _Wikimedia_: foto de un carro romano reconstruido — disponible.

**Tags propuestos:** `['legacy', 'parabola', 'historia', 'cohetes', 'NASA', 'sistemas', 'metafora']`

**Estado actual:** sin seed; la parábola está clara en mi cabeza, sólo hay que sentarse a escribirla con precisión histórica.

