### H-11 — Linux Ubuntu para s390x sobre Hercules: instalando arquitectura IBM Z emulada en mi laptop

- **Archivo seed (repo POC):** [github.com/CesarBallardini/s390x-on-hercules](https://github.com/CesarBallardini/s390x-on-hercules) — Shell, 1 star, último push 2021-09-08
- **Slug propuesto:** `linux-s390x-hercules`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-linux-s390x-hercules/index.md`
- **Serie:** H — pareja conceptual con [[H-10]]
- **Cross-links:** depende de [[H-10]]; lleva a [[H-12]]
- **Idioma:** es
- **Madurez:** **complete-poc** — instalación documentada paso a paso con tiempos
- **Length target:** medium (1500-2200 palabras)

**Concepto:** mientras [[H-10]] corre MVS 3.8j (un sistema operativo IBM clásico) en Hercules, este POC corre **Linux Ubuntu 18.04 para s390x** (la arquitectura moderna de IBM Z) en el mismo emulador. Los binarios que ejecutás dicen `Vendor ID: IBM/S390` en `lscpu` con feature flags `esan3 zarch stfle msa ldisp eimm dfp edat etf3eh highgprs sie`. Tarda ~3 horas instalarlo. La red se configura por CTC (Channel-to-Channel) con relay SSH. Es probablemente la única manera honesta de jugar con un Linux s390x si no trabajás en un banco.

**Hook:** "Linux corre en muchas arquitecturas. Una de ellas es **s390x** — la arquitectura de los mainframes IBM Z modernos. Casi nadie tiene acceso a un mainframe real. Pero podés emular uno con Hercules e instalar Ubuntu para s390x adentro. Tarda 3 horas. Funciona. `lscpu` te dice 'Vendor ID: IBM/S390'."

**Outline:**
1. Por qué s390x importa: la arquitectura del mundo bancario, una de las pocas arquitecturas Linux soportadas que casi nadie usa en su laptop.
2. Hercules como emulador (cross [[H-10]]).
3. Conseguir el instalador Ubuntu 18.04 s390x (Canonical lo publica oficialmente).
4. La red por CTC: por qué CTC y no Ethernet.
5. El relay SSH para acceder al instalador desde el host.
6. La instalación: 3 horas, pantallas en orden, gotchas conocidas.
7. Después del primer boot: `arch`, `lscpu`, ver los feature flags de IBM Z.
8. Lo que sí funciona, lo que no.
9. Cierre: la sensación de tener una notebook que reporta "IBM/S390" en `lscpu`.

**Bibliografía:**
- Repo del POC: [CesarBallardini/s390x-on-hercules](https://github.com/CesarBallardini/s390x-on-hercules).
- [Hercules — sitio oficial](http://www.hercules-390.org/).
- [Ubuntu for s390x — port page](https://help.ubuntu.com/community/Installation/Ports).
- [Canonical — Ubuntu on IBM Z and LinuxONE](https://ubuntu.com/ibm).
- [IBM z/Architecture Principles of Operation (SA22-7832)](https://www.ibm.com/docs/en/zos).
- [Wikipedia — Linux on IBM Z](https://en.wikipedia.org/wiki/Linux_on_IBM_Z).

**Imágenes:**
- _Crear_: screenshot de `lscpu` mostrando "IBM/S390" y los flags (~5 min — imagen mítica).
- _Crear_: diagrama del CTC Channel-to-Channel networking (~30 min).

**Tags propuestos:** `['s390x', 'Hercules', 'IBM Z', 'Linux', 'Ubuntu', 'mainframe', 'arqueologia']`

**Estado actual:** **complete-poc**.

