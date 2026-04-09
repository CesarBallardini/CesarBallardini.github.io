### A1-09 — GnuCOBOL-lab: aprender RM/COBOL-85 desde un libro español de 1990 dentro de una VM Vagrant

- **Archivo seed (repo POC):** [github.com/CesarBallardini/GnuCOBOL-lab](https://github.com/CesarBallardini/GnuCOBOL-lab) — Shell, último push 2023-01-15
- **Slug propuesto:** `gnucobol-lab-rm-cobol-85`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-gnucobol-lab-rm-cobol-85/index.md`
- **Serie:** A1 — fuerte cruce con [[H-04]] (COBOL→GnuCOBOL migración) y [[H-02]] (RM/COBOL en GNU/Linux)
- **Cross-links:** depende conceptualmente de [[H-04]]; lleva a [[E-12]] (el patrón Vagrant+Ansible para aprender), [[K-02]] (laboratorios docentes), [[H-02]]
- **Idioma:** es
- **Madurez:** **complete-poc** — VM Vagrant funciona, estructura capítulo-por-directorio del libro
- **Length target:** medium (1500-2200 palabras)

**Concepto:** *Programación estructurada en RM/COBOL-85* (García Pérez / Cerro Somolino / Diez Perla, McGraw-Hill 1990) es uno de los pocos libros en español que enseña COBOL serio a un público universitario. El problema en 2026 es que RM/COBOL-85 ya no existe como producto vivo accesible. La solución: una VM Vagrant + Ansible con GnuCOBOL 3.1.2 sobre Ubuntu 20.04, donde cada capítulo del libro es un directorio con los listings tipeados y compilando. Y el bonus: tres intentos de instalar el viejo OpenCobolIDE (abandonado) sobre Ubuntu Focal/Bionic/Xenial 64/32-bit, que es un buen paseo de arqueología de paquetes Python.

**Hook:** "tengo un libro de COBOL del 90 en español. Lo quiero seguir capítulo por capítulo. El problema: el dialecto del libro (RM/COBOL-85) no se compila más en ningún lado. La solución: una VM con GnuCOBOL, una Vagrantfile y la disciplina de tipear los listings. El post cuenta el lab y por qué seguir libros viejos sigue siendo, en 2026, la mejor manera de aprender un lenguaje viejo."

**Outline:**
1. El libro: García Pérez, Cerro Somolino, Diez Perla, McGraw-Hill 1990. Por qué importa que sea en español y por qué es difícil encontrar uno equivalente moderno.
2. RM/COBOL-85 vs GnuCOBOL: dialectos, compatibilidad real, qué *no* compila sin patches.
3. La VM: Vagrant + Virtualbox + Ansible + Ubuntu 20.04 + GnuCOBOL 3.1.2. El `Vagrantfile` mínimo.
4. La estructura capítulo-por-directorio. Por qué el isomorfismo libro↔repo ayuda al estudiante.
5. La aventura paralela: instalar OpenCobolIDE (abandonado, basado en Python 3.5/PyQt) en distintas versiones de Ubuntu. Tres intentos, dos triunfos parciales, una rendición.
6. Lo que el libro enseña que los tutoriales modernos no enseñan: PIC clauses, divisiones (IDENTIFICATION/ENVIRONMENT/DATA/PROCEDURE), archivos indexados ISAM, COPY libraries, REDEFINES.
7. Cierre: cuándo seguir un libro viejo en serio vale la pena.

**Bibliografía:**
- Repo del POC: [CesarBallardini/GnuCOBOL-lab](https://github.com/CesarBallardini/GnuCOBOL-lab).
- García Pérez, Cerro Somolino, Diez Perla, *Programación estructurada en RM/COBOL-85*, McGraw-Hill 1990 — verificar disponibilidad en bibliotecas o archive.org.
- [GnuCOBOL — sitio oficial](https://gnucobol.sourceforge.io/).
- [GnuCOBOL Programmer's Guide](https://gnucobol.sourceforge.io/doc/gnucobol.html).
- [OpenCobolIDE — repo abandonado](https://github.com/OpenCobolIDE/OpenCobolIDE) — para la sub-historia de instalación.
- [Vagrant docs](https://developer.hashicorp.com/vagrant) — para la VM base.
- [Ansible docs](https://docs.ansible.com/) — para la provisión.
- Cross-link [[H-02]] [[H-04]] para los ángulos de migración legacy.

**Imágenes:**
- _Crear_: foto de la tapa del libro de 1990 (~10 min, si lo tengo en papel).
- _Crear_: screenshot del REPL de GnuCOBOL compilando el primer capítulo (~10 min).
- _Crear_: árbol del repo mostrando un directorio por capítulo del libro (~10 min).

**Tags propuestos:** `['GnuCOBOL', 'RM COBOL', 'COBOL', 'Vagrant', 'libro', 'enseñanza', 'español']`

**Estado actual:** **POC completo**. El repo en GitHub tiene todo el setup; el post se escribe esencialmente leyendo el README y agregando el ángulo nostálgico del libro.

