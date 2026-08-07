### A1-09 — GnuCOBOL-lab: aprender RM/COBOL-85 desde un libro español de 1990 dentro de una VM Vagrant

- **Archivo seed (repo POC):** [github.com/CesarBallardini/GnuCOBOL-lab](https://github.com/CesarBallardini/GnuCOBOL-lab) — Shell, último push 2023-01-15
- **Slug propuesto:** `gnucobol-lab-rm-cobol-85`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-gnucobol-lab-rm-cobol-85/index.md`
- **Serie:** A1 — fuerte cruce con [[H-04]] (COBOL→GnuCOBOL migración) y [[H-02]] (RM/COBOL en GNU/Linux)
- **Cross-links:** depende conceptualmente de [[H-04]]; lleva a [[E-12]] (el patrón Vagrant+Ansible para aprender), [[K-02]] (laboratorios docentes), [[H-02]]
- **Idioma:** es
- **Madurez:** prosa-borrador (2026-07-15, generado por Claude; sin revisar por César) — base: **complete-poc**, VM Vagrant funciona, estructura capítulo-por-directorio del libro
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

**Estado actual:** **POC completo + prosa-borrador**. El repo en GitHub tiene todo el setup; el post se escribe esencialmente leyendo el README y agregando el ángulo nostálgico del libro.

Prosa escrita el 2026-07-15 (Claude, sin revisar por César), siguiendo el outline de 7 puntos ya existente. **Lo que quedó escrito:** el encuadre del libro español de 1990 como objeto didáctico, la tesis del isomorfismo libro↔repo, el argumento de por qué un dialecto muerto se estudia igual, la sub-historia de OpenCobolIDE como arqueología de paquetes, el inventario de lo que el libro enseña y los tutoriales modernos no, y el cierre sobre cuándo seguir un libro viejo en serio.

**Lo que quedó como hueco:** todo lo que sale del repo real y de la memoria de César. El draft asumía «se escribe leyendo el README», pero la prosa se generó **sin acceso al README ni al árbol del repo**, así que cada dato concreto del lab quedó pedido explícitamente: de dónde salió el libro y desde cuándo lo tiene, hasta qué capítulo llegó, qué construcciones de RM/COBOL-85 le rebotó GnuCOBOL de verdad, qué hace exactamente el rol de Ansible, cómo se llaman los directorios de capítulo, cuáles fueron los tres intentos de OpenCobolIDE y en qué orden, y por qué el último push es de enero de 2023. También quedan `[VERIFICAR:]` sobre los datos bibliográficos del libro (ISBN, edición, disponibilidad en archive.org), sobre las fechas/versiones de GnuCOBOL y Ubuntu 20.04, y sobre las afirmaciones de compatibilidad de dialectos (`-std=rm` y compañía) que hay que chequear contra el Programmer's Guide antes de publicar.

**Antes de publicar:** resolver los huecos con César, reemplazar los `[VERIFICAR:]` por datos chequeados contra las fuentes de la bibliografía, resolver `[[H-02]]`, `[[H-04]]`, `[[E-12]]` y `[[K-02]]` a URLs reales, y sacar las tres fotos/screenshots de la sección Imágenes.


---

## Borrador de prosa

Tengo un libro de COBOL de 1990, en español, y lo quiero seguir capítulo por capítulo, tipeando los listings a mano como si fuera 1992 y yo tuviera que entregar el práctico. El problema es aburridamente concreto: el dialecto que enseña el libro, RM/COBOL-85, no se compila más en ningún lado al que yo tenga acceso. No es que sea difícil: es que el producto no está. Un libro de texto cuyo compilador desapareció es, técnicamente, literatura.

La solución quedó en un repo: una VM Vagrant con GnuCOBOL adentro, provisionada con Ansible, y un directorio por cada capítulo del libro con los programas tipeados y compilando.[^repo] Este post cuenta ese lab, y de paso defiende una idea que en 2026 suena a excentricidad: seguir un libro viejo, entero y en orden, sigue siendo la mejor manera que conozco de aprender un lenguaje viejo.

### El libro

*Programación estructurada en RM/COBOL-85*, de García Pérez, Cerro Somolino y Diez Perla, publicado por McGraw-Hill en 1990.[^libro] Lo que lo hace raro no es el COBOL: es que sea un libro **en español** que enseña COBOL en serio, con nivel universitario, sin pedir disculpas y sin tratar al lector como si nunca hubiera visto una computadora. Esa combinación era escasa entonces y hoy es directamente inhallable. Los libros técnicos en español de esa época solían ser traducciones apuradas o manuales de producto; éste es un texto docente, con la progresión de un curso.

> 🕳️ **HUECO — necesita a César:** ¿de dónde salió tu ejemplar? ¿Lo compraste en su momento, lo heredaste, lo encontraste después? ¿Lo tenés en papel o es un PDF?

> 🕳️ **HUECO — necesita a César:** ¿lo usaste alguna vez «en serio» (cursada, trabajo, enseñando), o el lab es la primera vez que lo seguís en orden?

Buscar un equivalente moderno es un ejercicio deprimente. Lo que hay hoy sobre COBOL en español, cuando hay, es material de curso corto orientado a certificación o a «entrá al mainframe que pagan bien»: sintaxis suficiente para leer un programa ajeno, cero teoría de diseño de archivos, cero disciplina de estructuración. El libro del 90 hace lo contrario. Es un libro de *programación estructurada* que usa COBOL como vehículo, no un manual de COBOL que menciona la estructuración de pasada. El título dice el orden de las prioridades.

[VERIFICAR: datos bibliográficos completos del libro — ISBN, edición, cantidad de páginas, colección de McGraw-Hill; chequear también si hay algún ejemplar en archive.org o en catálogos de bibliotecas universitarias españolas/argentinas, y con qué modalidad (préstamo digital controlado vs. nada). El draft lo deja explícitamente como pendiente de verificación.]

### RM/COBOL-85 no es GnuCOBOL, y eso es parte del ejercicio

RM/COBOL fue un COBOL comercial, y el libro enseña *ese* dialecto: los ejemplos, las particularidades de entrada/salida y las extensiones fuera del estándar que el texto usa sin avisar, porque en 1990 no hacía falta avisar. El estudiante tenía el producto en el laboratorio de la facultad y listo.

GnuCOBOL es un compilador libre de COBOL, vivo y mantenido.[^gnucobol] No es RM/COBOL, pero tiene la virtud de tomarse en serio la compatibilidad con dialectos históricos: el Programmer's Guide documenta los estándares y dialectos que puede aceptar y cómo se seleccionan.[^gnucobol_guide] Ahí está el puente. Y la pregunta interesante del lab no es «¿anda?», es **dónde deja de andar**.

[VERIFICAR: cómo se selecciona exactamente el dialecto en GnuCOBOL 3.1.2 — nombre y valores de la opción de estándar (¿`-std=...`?), si existe un valor específico para RM/COBOL, y qué diferencias documenta el Programmer's Guide entre ese modo y el estándar COBOL 85. Chequear contra https://gnucobol.sourceforge.io/doc/gnucobol.html , no de memoria.]

> 🕳️ **HUECO — necesita a César:** cuando tipeaste los listings del libro, ¿qué te rebotó GnuCOBOL de verdad? Con una o dos construcciones concretas alcanza: ¿fueron extensiones de RM en la ENVIRONMENT DIVISION, el formato de fuente, ACCEPT/DISPLAY, algo de archivos indexados? Esto es lo que hace valioso el post frente a un tutorial genérico.

> 🕳️ **HUECO — necesita a César:** ¿tocaste los listings del libro para que compilen, o los dejaste como están y anotaste aparte lo que falla? Es una decisión editorial del repo y vale la pena explicarla.

### La VM: que el lab sea desechable

El setup es deliberadamente aburrido: Vagrant y VirtualBox levantan una VM Ubuntu 20.04, Ansible la provisiona e instala GnuCOBOL 3.1.2, y adentro está el árbol de capítulos.[^vagrant][^ansible]

La razón de la VM no es el aislamiento por el aislamiento. Es que un lab para aprender tiene que ser **desechable**. Cuando estás siguiendo un libro, la mitad de las veces rompés el entorno probando algo, y si romperlo cuesta caro dejás de probar. Con `vagrant destroy` y `vagrant up` volvés al estado inicial en minutos y no perdés nada. La VM convierte el miedo a romper en una operación de rutina, que es exactamente lo que necesita alguien que está estudiando.

El segundo motivo es la reproducibilidad hacia adelante. Ubuntu 20.04 y GnuCOBOL 3.1.2 son una foto de un momento, y esa foto está escrita en el `Vagrantfile` y en el playbook. Dentro de tres años, cuando la distro haya cambiado varias veces, el lab sigue describiendo con precisión qué necesitaba. Un `README` que dice «instalá GnuCOBOL» envejece; un playbook que lo instala, no.

> 🕳️ **HUECO — necesita a César:** ¿el playbook de Ansible compila GnuCOBOL desde fuente o lo instala del repositorio de Ubuntu? ¿Por qué elegiste 20.04 y no la LTS más nueva del momento?

> 🕳️ **HUECO — necesita a César:** ¿por qué VM y no un contenedor, que para un compilador de línea de comandos sería más liviano? Sospecho que la respuesta tiene que ver con OpenCobolIDE y el escritorio gráfico, pero no quiero ponerte palabras en la boca.

[VERIFICAR: fechas de release y estado de soporte de Ubuntu 20.04 (Focal) y de GnuCOBOL 3.1.2 al momento de armar el lab (último push del repo: 2023-01-15) y al momento de publicar el post. No afirmar versiones ni EOL sin chequear.]

### Un directorio por capítulo

La estructura del repo es un espejo del índice del libro: un directorio por capítulo, y adentro los programas de ese capítulo. Nada más.

Suena trivial y es la mejor decisión del lab. El isomorfismo libro↔repo hace que la navegación sea gratis: estás leyendo el capítulo 7, hacés `cd` al directorio 7, y ahí está lo que el capítulo 7 te pidió que hicieras. No hay que mantener un índice paralelo, no hay que recordar dónde guardaste aquel ejemplo de REDEFINES, no hay que inventar una taxonomía propia. El libro ya hizo el trabajo de ordenar el material —para eso es un libro de texto— y el repo se limita a no arruinarlo.

Es también una defensa contra la trampa clásica del autodidacta: saltear. Cuando el árbol de directorios tiene huecos, los huecos se ven. Un capítulo sin directorio es un capítulo que no hiciste, y está ahí mirándote cada vez que hacés `ls`.

> 🕳️ **HUECO — necesita a César:** ¿cómo se llaman los directorios de capítulo en el repo (`cap01/`, `07/`, con el título del capítulo)? ¿Hasta qué capítulo llegaste realmente? Si el árbol tiene huecos, decirlo en el post es más honesto —y más útil— que dar a entender que está completo.

### El desvío: instalar OpenCobolIDE

Acá el lab se me fue de las manos, en el buen sentido.

OpenCobolIDE es un IDE de escritorio para COBOL, escrito en Python con PyQt, hoy abandonado.[^ocide] La tentación era obvia: darle al estudiante un entorno gráfico en vez de `vi` y el compilador a mano. El problema es que un proyecto Python abandonado no se instala: se **excava**. Sus dependencias están clavadas a un intérprete y a versiones de librerías que las distribuciones actuales ya no traen, y cada año que pasa agrega una capa de sedimento.

Hubo tres intentos, contra distintas versiones de Ubuntu —Focal, Bionic y Xenial, entre 64 y 32 bits—, buscando la que todavía tuviera el Python y el PyQt de la época. Resultado: dos triunfos parciales y una rendición.

> 🕳️ **HUECO — necesita a César:** el detalle de los tres intentos. ¿Cuál fue cada uno (qué Ubuntu, qué arquitectura), qué significa exactamente «triunfo parcial» en cada caso —arrancaba pero no compilaba, compilaba pero el editor fallaba, otra cosa—, y en cuál te rendiste y por qué? Ésta es la mejor parte del post y no la puedo escribir yo.

> 🕳️ **HUECO — necesita a César:** ¿quedó algo de esos intentos en el repo (una rama, un playbook alternativo, un directorio), o fue todo trabajo tirado que sólo vive en tu memoria?

[VERIFICAR: la versión de Python y de PyQt que pide OpenCobolIDE, y desde cuándo está sin mantenimiento. El draft dice «Python 3.5/PyQt»; confirmarlo contra el repo (setup.py / requirements, fecha del último commit y del último release) antes de afirmarlo en el post.]

La moraleja del desvío es de arqueología de paquetes, no de COBOL: un IDE abandonado es más difícil de resucitar que un compilador de 1985. El compilador tiene un estándar detrás, implementaciones libres y gente que lo mantiene. El IDE tiene una cadena de dependencias del ecosistema Python de un año particular, y esa cadena no tiene a nadie cuidándola. La herramienta «moderna» y cómoda envejeció peor que el lenguaje «viejo». Es exactamente el argumento de [[H-04]] y [[H-02]] visto desde el otro lado del mostrador.

### Lo que el libro enseña y los tutoriales no

Después de tipear listings del 90 durante un rato, la lista de lo que se perdió por el camino se arma sola:

- **Las cuatro divisiones** —IDENTIFICATION, ENVIRONMENT, DATA, PROCEDURE— como una arquitectura obligatoria, no como boilerplate a copiar. El libro te hace pensar *qué va en cada una* y por qué el lenguaje te obliga a separar la descripción del entorno de la descripción de los datos, y ésta de la lógica.
- **Las cláusulas PIC** como un lenguaje de tipos declarativo y espacialmente explícito. Un `PIC S9(5)V99` dice el rango, el signo y la escala decimal, todo junto y sin ambigüedad. Un `float` de un tutorial moderno no dice ninguna de las tres cosas.
- **Archivos indexados** (ISAM) como estructura de datos de primera clase del lenguaje, no como una base de datos que se llama por red. El libro te enseña a diseñar el archivo antes de escribir el programa.
- **COPY libraries**: reuso de declaraciones de datos por inclusión textual, con todo lo bueno y lo malo que eso implica. Es el abuelo del `#include`, y verlo funcionar aclara qué problema estaban resolviendo.
- **REDEFINES**: mirar los mismos bytes con dos formas distintas. Es una `union` de C, con nombre autoexplicativo.

Ninguna de estas cosas aparece en un tutorial de tres horas, porque todas requieren que alguien te explique *el modelo mental*, no la sintaxis. Y explicar modelos mentales en orden, con ejercicios que se apoyan en el capítulo anterior, es precisamente lo que un libro de texto hace y un tutorial no.

[VERIFICAR: que las construcciones listadas (COPY, REDEFINES, archivos indexados, PIC) están efectivamente cubiertas en el libro y con qué alcance. Ajustar la lista contra el índice real antes de publicar; hoy está armada desde el Concepto del draft, no desde el libro en la mano.]

### Cuándo vale la pena seguir un libro viejo en serio

No siempre. Si querés aprender un lenguaje vivo, un libro de 1990 te va a enseñar cultura obsoleta con confianza injustificada, y eso es peor que no saber.

Vale la pena en dos casos. El primero: cuando el lenguaje que querés aprender también es viejo, y la mejor documentación de cómo se *pensaba* en ese lenguaje quedó congelada en los libros de su época. Nadie va a escribir un tratado nuevo de diseño de archivos indexados en COBOL; ya está escrito, en 1990, en español, y lo tengo acá.

El segundo: cuando querés la disciplina. Un libro tiene orden, tiene ejercicios que se acumulan y tiene un final. Un tutorial tiene tu atención y nada más. La diferencia se nota a los seis meses.

El lab no es más que la infraestructura mínima para que esa disciplina sea posible hoy: un compilador que acepta el dialecto —casi siempre—, una VM que puedo romper sin consecuencias, y un árbol de directorios que me recuerda hasta dónde llegué. El libro hace todo lo demás. [[E-12]] cuenta el patrón general —Vagrant y Ansible como andamio para aprender cualquier cosa— y [[K-02]] lo mira desde el ángulo docente.

> 🕳️ **HUECO — necesita a César:** el último push del repo es de enero de 2023. ¿Por qué se detuvo? ¿Terminaste lo que querías, te aburriste, se te cruzó otra cosa? Un cierre honesto sobre eso vale más que fingir que el lab está vivo.

> 🕳️ **HUECO — necesita a César:** ¿se lo recomendarías a alguien que empieza COBOL hoy, o es explícitamente un proyecto para vos y para nadie más? Tu respuesta cambia el tono de todo el cierre.

[^repo]: [CesarBallardini/GnuCOBOL-lab](https://github.com/CesarBallardini/GnuCOBOL-lab) — el repo del laboratorio.
[^libro]: García Pérez, Cerro Somolino, Diez Perla, *Programación estructurada en RM/COBOL-85*, McGraw-Hill, 1990. [VERIFICAR: completar ISBN y edición, y agregar link a archive.org o a un catálogo si existe alguna copia consultable, según la convención de la casa para libros sin versión libre.]
[^gnucobol]: [GnuCOBOL — sitio oficial](https://gnucobol.sourceforge.io/).
[^gnucobol_guide]: [GnuCOBOL Programmer's Guide](https://gnucobol.sourceforge.io/doc/gnucobol.html).
[^ocide]: [OpenCobolIDE](https://github.com/OpenCobolIDE/OpenCobolIDE) — repo abandonado.
[^vagrant]: [Documentación de Vagrant](https://developer.hashicorp.com/vagrant).
[^ansible]: [Documentación de Ansible](https://docs.ansible.com/).
