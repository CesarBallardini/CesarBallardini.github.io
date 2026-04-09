### A2-02 — Los papers de Scheme: lambda the ultimate

- **Archivo seed:** `dev/draft-scheme-papers.md`
- **Slug propuesto:** `papers-de-scheme-lambda-the-ultimate`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-papers-de-scheme-lambda-the-ultimate.md`
- **Serie:** A2
- **Cross-links:** depende de [[tr-14]] (Lambda the Ultimate classics); lleva a [[A2-01]] (SICP), [[B-04]] (tail calls), [[B-05]] (trampolines), [[C-05]] (revolución del cómputo)
- **Idioma:** es
- **Madurez:** bare-seed
- **Length target:** medium (1500-2000 palabras)

**Concepto:** la serie de papers que Sussman y Steele escribieron sobre Scheme entre 1975 y 1980 ("Lambda the Ultimate ___") cambiaron lo que entendíamos por "lenguaje de programación". El post es una lectura guiada para alguien que nunca leyó un paper técnico antes.

**Hook:** "cuatro papers, todos con el título *Lambda the Ultimate algo*, y el primero arranca con: 'descubrimos por accidente que con lambda podés construir todo lo que un compilador necesita'. Eso es *Lambda the Ultimate Imperative*. Y sí, vamos a leerlo."

**Outline:**
1. La serie *Lambda Papers* de Steele y Sussman (1975-1980). Por qué los escribieron, qué pasaba en el MIT en ese momento.
2. *Lambda: The Ultimate Imperative* (1976) — cómo lambda subsume goto, asignación, loops.
3. *Lambda: The Ultimate Declarative* (1976) — la otra cara: lambda como mecanismo declarativo.
4. *Lambda: The Ultimate GOTO* (1977) — por qué tail calls son saltos.
5. *Debunking the "Expensive Procedure Call" Myth* (1977) — el paper que justifica por qué tail calls deben ser cheap.
6. *RABBIT* (Steele, MS thesis 1978) — el primer compilador "real" de Scheme.
7. Cierre: por qué leer estos papers todavía vale la pena en 2026.

**Bibliografía:**
- [[tr-14]] — Lambda the Ultimate, classic papers.
- [Sussman & Steele, *Lambda: The Ultimate Imperative*, MIT AI Memo 353, 1976](https://dspace.mit.edu/handle/1721.1/5790).
- [Steele, *Lambda: The Ultimate Declarative*, MIT AI Memo 379, 1976](https://dspace.mit.edu/handle/1721.1/5789).
- [Steele, *Debunking the "Expensive Procedure Call" Myth*, MIT AI Memo 443, 1977](https://dspace.mit.edu/handle/1721.1/5753).
- [Steele, *RABBIT: A Compiler for Scheme*, MIT AI-TR-474, 1978](https://dspace.mit.edu/handle/1721.1/6913).
- [Lambda the Ultimate (the blog) — papers section](http://lambda-the-ultimate.org/classic/papers.html).
- [Sussman, *The Definition and Implementation of a Computer Programming Language Based on Constraints*, MIT 1973](https://dspace.mit.edu/handle/1721.1/6933) — antecedente.
- [readscheme.org en GitHub (mirror)](https://github.com/scheme-and-computer-science/library.readscheme.org) — biblioteca curada de recursos Scheme.

**Imágenes:**
- _Crear_: screenshot de la portada del primer Lambda Paper (PDF) (5 min).
- _Crear_: opcional, un timeline simple SVG de los papers en orden (~30 min).

**Tags propuestos:** `['Scheme', 'Lambda Papers', 'Sussman', 'Steele', 'lambda calculus', 'historia']`

**Estado actual:** sólo título.

