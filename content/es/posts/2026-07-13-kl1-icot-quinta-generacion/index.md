---
title: 'Resucitando KL1: el lenguaje del proyecto japonés de Quinta Generación, treinta años después'
description: 'Japón apostó 850 millones de dólares a un lenguaje de programación lógica concurrente y a hardware paralelo dedicado. El proyecto cerró en 1992. Empaqueté su compilador en un Vagrant moderno para hacerlo correr hoy — esta es la arqueología de esa reconstrucción.'
featured_image: 'hero-icot-kl1.jpg'
tags: ['KL1', 'KLIC', 'ICOT', 'Prolog concurrente', 'Japon', 'Vagrant', 'Debian']
---

Entre 1982 y 1992, en la misma época en que las vidrieras electrónicas de Tokio ya anunciaban audio, video y calculadoras a los gritos[^img_hero], Japón gastó el equivalente a 850 millones de dólares en el *Fifth Generation Computer Systems Project* (5GCS): una apuesta estatal a redefinir la computación alrededor de la **programación lógica concurrente**, corriendo sobre hardware paralelo diseñado específicamente para eso. El lenguaje central del proyecto se llamaba **KL1** — *Kernel Language 1*. El proyecto se cerró en 1992 sin haber producido la "máquina que piensa" que prometía. Pero el código sobrevivió. Hace unos años lo recompilé en una laptop moderna y lo hice correr. Esta es la historia de esa reconstrucción.

## ICOT y la apuesta de los 850 millones

A principios de los 80, el gobierno japonés miraba con preocupación cómo Estados Unidos discutía Lisp y las máquinas Symbolics, mientras la industria de semiconductores japonesa dominaba la manufactura pero no el diseño de sistemas inteligentes. La respuesta fue el *Institute for New Generation Computer Technology* (**ICOT**), un instituto central financiado por el gobierno y los fabricantes japoneses (Fujitsu, Hitachi, NEC, Toshiba, Matsushita, Mitsubishi, Oki, Sharp), con un mandato de diez años y una meta declarada: construir sistemas de inferencia masivamente paralelos, con un lenguaje de programación lógica como interfaz nativa entre el programador y el hardware.

La apuesta técnica central fue **no** seguir el camino Lisp/von Neumann. En cambio, ICOT eligió la **programación lógica** — el paradigma de Prolog — como base, y le agregó **concurrencia** como primitiva del lenguaje, no como biblioteca. La idea: si el hardware iba a ser masivamente paralelo, el lenguaje tenía que expresar paralelismo de forma nativa desde la sintaxis misma de los programas.

## KL1 como lenguaje: de Prolog a las guardas

KL1 no nace de cero. Desciende de una línea de lenguajes de programación lógica concurrente: Prolog clásico → *Concurrent Prolog* (Shapiro) → **GHC** (*Guarded Horn Clauses*, Kazunori Ueda, 1985)[^ghc] → KL1, la síntesis final de ICOT.

La idea que lo diferencia de Prolog es la **guarda**. En Prolog, cuando hay varias cláusulas que podrían aplicar, el motor las prueba en orden y hace backtracking si una falla. En KL1 (y en GHC, su antecesor directo), cada cláusula tiene una guarda — una condición que se evalúa *antes* de comprometerse con esa cláusula — y una vez que una guarda tiene éxito, esa elección es **definitiva**: no hay backtracking. Esto se llama *committed choice*, y es lo que hace que el modelo sea naturalmente concurrente: distintos objetivos pueden evaluar sus guardas en paralelo, sin necesidad de coordinarse entre sí hasta que uno se compromete.

El ejemplo más chico que existe para ver esto es casi vergonzosamente simple — es el que trae la traducción al KL1 del libro de Huntbach y Ringwood, *Agent-Oriented Programming*[^huntbach]:

```prolog
:- module main.

main :- not(0, X), io:outstream([print(X), nl]).

not(In, Out):- In = 0 | Out = 1.
not(In, Out):- In = 1 | Out = 0.
```

Las dos cláusulas de **not/2** tienen guardas mutuamente excluyentes (`In = 0` y `In = 1`, antes de la barra `|`). El motor evalúa ambas guardas, sólo una puede tener éxito para un valor concreto de `In`, y esa cláusula se compromete sin mirar atrás. No parece gran cosa para invertir un bit — pero esa misma mecánica, escalada, es la que permite que miles de procesos KL1 corriendo en paralelo se sincronicen únicamente a través de la unificación de variables compartidas, sin locks, sin semáforos, sin un scheduler explícito escrito a mano.

## Por qué "fracasó" — y por qué esa palabra es injusta

El 5GCS terminó en 1992 sin las máquinas que piensan que prometía en 1982. En la narrativa popular de la época, eso se leyó como un fracaso rotundo — el libro alarmista de Feigenbaum y McCorduck, *The Fifth Generation*[^feigenbaum], escrito en pleno auge del proyecto, hoy es más un documento de época que una referencia técnica.

Pero mirado en retrospectiva por el propio Kazunori Ueda —el diseñador de GHC y una de las figuras centrales del proyecto— la historia es más matizada. En su balance de 2018[^ueda2018], Ueda argumenta que el 5GCS produjo un cuerpo de trabajo técnico enorme sobre programación lógica concurrente, sistemas paralelos y modelos de computación declarativa, incluso si el objetivo declarado (IA fuerte sobre hardware dedicado) no se cumplió. Parte de ese trabajo influyó, indirectamente, en ideas que sí sobrevivieron con otros nombres: el modelo de actores, la sincronización por paso de mensajes sin estado compartido. Joe Armstrong, el creador de Erlang, dedica una sección de *A History of Erlang*[^armstrong] a reconocer la línea de investigación en programación lógica concurrente japonesa como parte del paisaje intelectual del que Erlang emerge, aunque su camino directo fuera otro (Prolog vía Ericsson, no KL1 vía ICOT).

Y el trabajo de ingeniería sobrevivió literalmente, no sólo en espíritu: **KLIC**, la implementación portable de KL1 en C, se siguió manteniendo después del cierre formal de ICOT[^chikayama1996], y hoy —treinta años después— se puede *bajar, compilar y correr*.

## KLIC: la implementación que sobrevivió

KLIC[^chikayama1996] es un compilador de KL1 a C, escrito por Takashi Chikayama y su equipo, pensado para correr sobre Unix genérico en vez de sobre las máquinas PIM (*Parallel Inference Machine*) dedicadas del proyecto original. Es, en otras palabras, la puerta de entrada a KL1 para cualquiera que no tenga una PIM en el garage.

Hubo un paquete Debian de KLIC hasta 2006. Sus binarios eran de 32 bits (`i386`). Después de eso, nada — el paquete quedó huérfano, y con cada ciclo de vida de Debian se volvió más difícil de instalar en un sistema moderno.

## El POC: reconstruir el paquete Debian de 2006 en 2020

Mi repo `kl1c`[^repo] hace exactamente esa reconstrucción, y el proceso resultó ser una lección de arqueología de software más interesante de lo que esperaba.

El punto de partida es literal: el snapshot congelado de `snapshot.debian.org` correspondiente al 6 de noviembre de 2006 — el último día en que ese paquete existió en el archivo activo de Debian. De ahí se bajan los tres artefactos de un paquete fuente Debian clásico: el `.dsc` (metadata + checksums), el `.diff.gz` (el parche de empaquetado de Debian sobre el código original) y el `.orig.tar.gz` (el tarball upstream de KLIC 3.003). `dpkg-source -x` reconstruye el árbol de fuentes completo a partir de esos tres archivos, tal como lo hubiera visto un desarrollador Debian en 2006.

A partir de ahí, nada compila limpio. Dos problemas concretos, cada uno una pequeña cápsula de por qué el software viejo se rompe:

**El `Configure` de KLIC —un script interactivo estilo años 90 que autodetecta funciones de la libc— dejó de confiar en su propia autodetección.** El script prueba si el sistema tiene `bcmp`/`bcopy`/`bzero`/`strchr` (las funciones BSD clásicas) o sus equivalentes POSIX modernos (`memcmp`/`memcpy`/`memset`/`index`), compilando pequeños programas de prueba al vuelo. En un Ubuntu de 2016, esa detección para `bcmp`, `bzero` y `strchr` specíficamente falla — no importa demasiado por qué; lo que importa es que la respuesta correcta ya se sabe de antemano. El parche del repo simplemente **hardcodea** la respuesta (`USEBCMP="#define"`, etc.) en vez de confiar en una detección que ya no es confiable treinta años después.

**El instalador interactivo no sabía que las rutas de librerías multiarch existen.** KLIC se instala vía un script `expect` que simula un usuario respondiendo a los prompts del instalador original. Ese instalador de los 90 no conocía el layout `/usr/lib/i386-linux-gnu/` — la convención *multiarch* que Debian introdujo bastante después, para poder tener librerías de distintas arquitecturas conviviendo en el mismo sistema. El parche le agrega al script `expect` la respuesta específica que apunta ahí.

Con esos dos parches (más uno tercero encadenado en `debian/rules`) y un `debian/compat` fijado en 5 (para que `debhelper` no se queje), `debuild -us -uc -d` produce paquetes `.deb` frescos — sin firmar, sin verificación estricta de dependencias, pero funcionales. Todo esto corre dentro de una VM Vagrant con el box `ubuntu/trusty32`: Ubuntu 14.04 "Trusty Tahr", 32 bits. La elección de 32 bits no es casual — los binarios originales de 2006 eran `i386`, y reconstruir en la misma arquitectura evita tener que portear código C de los 90 a un modelo de punteros de 64 bits, que para un compilador con su propio runtime y representación de términos etiquetados es un problema bastante más profundo que un parche de tres líneas.

## "Hello, concurrent world" en KL1

Con los paquetes instalados, el ejemplo que más me gusta correr no es **not/2** — ya lo vimos, es el más chico posible — sino la criba de Eratóstenes concurrente, un clásico de los lenguajes de programación lógica concurrente porque muestra el patrón real: procesos que se comunican exclusivamente a través de streams (listas cuya cola todavía no está instanciada):

```prolog
gen(N0,Max,Ns0) :- N0=<Max | Ns0=[N0|Ns1], N1:=N0+1, gen(N1,Max,Ns1).
gen(N0,Max,Ns0) :- N0 >Max | Ns0=[].

sift([],     Zs0) :- Zs0=[].
sift([P|Xs1],Zs0) :- Zs0=[P|Zs1], filter(P,Xs1,Ys), sift(Ys,Zs1).

filter(_,[],     Ys0) :-               Ys0=[].
filter(P,[X|Xs1],Ys0) :- X mod P=\=0 | Ys0=[X|Ys1], filter(P,Xs1,Ys1).
filter(P,[X|Xs1],Ys0) :- X mod P=:=0 |              filter(P,Xs1,Ys0).
```

**gen/3** genera la lista de números desde 2 hasta el máximo. **sift/2** toma esa lista, separa el primer número (que es primo por construcción) y arma un **filter/3** que descarta sus múltiplos del resto del stream, encadenándose recursivamente con el siguiente **sift/2**. El resultado es, literalmente, una tubería de procesos concurrentes — uno por cada primo encontrado hasta el momento — cada uno filtrando el stream que le llega del anterior. Nadie escribió un scheduler. Nadie coordinó explícitamente nada. La sincronización entera sale de que cada proceso sólo puede avanzar cuando la cola del stream que está leyendo deja de ser una variable libre y pasa a estar instanciada por quien la produce.

Es la misma idea que **not/2** mostraba en miniatura, escalada a un problema real: guardas + streams + committed choice alcanzan para expresar concurrencia sin que el programador tenga que pensar en threads.

## El eco de Dijkstra

Hay una conexión que no armé yo — la señala el propio README del repo, citando el trabajo de Dijkstra sobre **comandos guardados**[^ewd472]. La guarda de KL1 no es una invención aislada de ICOT: es un descendiente directo de la idea de Dijkstra de 1975 de que el no-determinismo controlado por guardas —condiciones que se evalúan antes de comprometerse con una rama de ejecución— es una forma más honesta de expresar programas concurrentes que el flujo de control secuencial disfrazado de paralelo. GHC y KL1 tomaron esa idea, la aplicaron a cláusulas de Horn, y construyeron todo un paradigma de programación lógica concurrente encima. Es uno de esos hilos que conecta un paper de fundamentos teóricos con un proyecto de 850 millones de dólares al otro lado del mundo, quince años después.

## Por qué vale la pena resucitar esto

Un proyecto cerrado en 1992, con un paquete Debian huérfano desde 2006, es exactamente el tipo de software que uno esperaría que esté perdido para siempre. No lo está. Los archivos de ICOT siguen preservados (con algunos mirrors muertos y otros vivos)[^icot], el código de KLIC sigue compilando con los parches correctos, y el lenguaje que Japón diseñó para las máquinas que iban a pensar corre hoy, sin ironía, dentro de una VM de 32 bits en una laptop cualquiera. Si alguna vez pensaste que un proyecto "fracasado" es sinónimo de código perdido, esto es la prueba de que no necesariamente: alcanza con sentarse tres tardes, tres parches, y las ganas de ver correr algo que el mundo dejó de mantener hace veinte años.

[^ghc]: Kazunori Ueda, *[Guarded Horn Clauses](https://www.ueda.info.waseda.ac.jp/~ueda/pub/GHCthesis.pdf)*, tesis de maestría, Universidad de Tokio, marzo de 1986 — el paper fundacional de GHC, la síntesis inmediatamente anterior a KL1.

[^huntbach]: Matthew M Huntbach & Graem A Ringwood, *Agent-Oriented Programming: From Prolog to Guarded Definite Clauses*, Lecture Notes in Artificial Intelligence 1630, Springer, 1999. [DOI 10.1007/3-540-47938-4](https://doi.org/10.1007/3-540-47938-4) — referencia canónica. La copia en archive.org que circulaba hasta hace poco ya no está disponible (item marcado `dark`); hay una copia de texto completo en [theswissbay.ch](https://theswissbay.ch/pdf/Gentoomen%20Library/Artificial%20Intelligence/General/Agent-Oriented%20Programming%20-%20From%20Prolog%20to%20Guarded%20Definite%20Clauses%20-%20Matthew%20M.%20Huntbach.pdf) (mirror personal, verificar antes de que se caiga).

[^feigenbaum]: Edward A Feigenbaum & Pamela McCorduck, *The Fifth Generation: Artificial Intelligence and Japan's Computer Challenge to the World*, Addison-Wesley, 1983. [Préstamo digital controlado en archive.org](https://archive.org/details/fifthgenerationa00feig).

[^ueda2018]: Kazunori Ueda, [*Logic/Constraint Programming and Concurrency: The Hard-Won Lessons of the Fifth Generation Computer Project*](https://doi.org/10.1016/j.scico.2017.06.002), *Science of Computer Programming*, vol. 164 (2018), pp. 3-17. El balance retrospectivo del propio diseñador de GHC.

[^armstrong]: Joe Armstrong, [*A History of Erlang*](https://doi.org/10.1145/1238844.1238850), *Proceedings of the Third ACM SIGPLAN Conference on History of Programming Languages* (HOPL III), 2007.

[^chikayama1996]: Takashi Chikayama, *KLIC: A Portable Parallel Implementation of a Concurrent Logic Programming Language*, en *Parallel Symbolic Languages and Systems* (PSLS 1995), Lecture Notes in Computer Science, Springer, 1996. [DOI 10.1007/BFb0023068](https://doi.org/10.1007/BFb0023068) — el paper que describe la implementación exacta que este proyecto empaqueta; copia incluida en el repo del POC.

[^ewd472]: Edsger W Dijkstra, [*Guarded commands, non-determinacy and formal derivation of programs*](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html), EWD472, 1975 (publicado en *Communications of the ACM* 18(8), 1975). El origen de la idea de "guarda" que GHC y KL1 heredan.

[^icot]: El archivo de software libre de ICOT (*ICOT Free Software*, ifs) está preservado por Kazunori Ueda en Waseda: [ueda.info.waseda.ac.jp/software.html](https://www.ueda.info.waseda.ac.jp/software.html) ([backup en Wayback Machine](https://web.archive.org/web/20251201151637/https://www.ueda.info.waseda.ac.jp/software.html)). El dominio original `icot.or.jp` está caído; [snapshot de 2008 en Wayback Machine](https://web.archive.org/web/20081231075254/http://www.icot.or.jp:80/ARCHIVE/HomePage-E.html).

[^repo]: César Ballardini, [*kl1c*](https://github.com/CesarBallardini/kl1c), repositorio en GitHub. Contiene el `Vagrantfile`, los parches de empaquetado, los paquetes `.deb` reconstruidos, y una colección de programas de ejemplo en KL1.

[^img_hero]: Imagen de portada: [*Akihabara 1976*](https://commons.wikimedia.org/wiki/File:Akihabara_1976.jpg) — fotografía de John Lloyd, 1976, vía Wikimedia Commons — CC BY 2.0. Recortada a 2.5:1 para hero landscape. No es una foto de ICOT ni de una PIM (no hay fotos de acceso público de ninguna de las dos) — es el barrio electrónico de Tokio, unos años antes del arranque del proyecto, para ambientar la época y el lugar.
