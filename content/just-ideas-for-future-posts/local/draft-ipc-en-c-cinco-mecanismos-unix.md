### I-06 — IPC en C: el recorrido honesto por los cinco mecanismos clásicos de Unix

- **Archivo seed:** _histórico (eliminado 2026-04-09): `ipc.c` — un archivo C vacío de 0 bytes que vivía en la raíz de `just-ideas-for-future-posts/`, dejado el 2025-02-03 como placeholder físico para acordarme de escribir este post. La idea ya está absorbida en este entry, así que el archivo placeholder fue eliminado del repo._
- **Slug propuesto:** `ipc-en-c-cinco-mecanismos-unix`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-ipc-en-c-cinco-mecanismos-unix/index.md`
- **Serie:** I — encaja por el ángulo "aprendí Unix peleándome con C en estas latitudes" (memoria del cómputo local de los 90)
- **Cross-links:** lleva a [[E-02]] (fixperm: el otro post de "aprendí Unix escribiendo C", mismo período), [[H-01]] (Linux ABI: cuando IPC se complica entre familias de kernels distintos), [[A1-03]] (Forth, otra "vista cruda" del sistema), [[I-03]] (Spectrum/MicroHobby: la cultura de tipear listings en C que llegaba en revistas)
- **Idioma:** es
- **Madurez:** concepto confirmado por el autor el 2026-04-08, placeholder físico (`ipc.c`) eliminado el 2026-04-09 después de absorberlo aquí
- **Length target:** medium (1500-2200 palabras)

**Concepto:** Unix tiene cinco maneras canónicas de hacer IPC entre procesos: pipes anónimos, named pipes (FIFOs), signals, shared memory (System V o POSIX) y sockets (Unix-domain o TCP). Las aprendí en distinto orden, en distintos años, con distintos motivos prácticos detrás de cada una. El post es un memoir técnico que recorre las cinco con un ejemplo mínimo en C, una anécdota personal de cuándo y por qué la usé en serio, y la lección estructural que cada una le dejó a las herramientas modernas que uso hoy (D-Bus, Redis pub/sub, gRPC, NATS, ZeroMQ — todas son envoltorios elegantes de los mismos cinco primitivos).

**Hook:** "tenía un archivo en mi carpeta de drafts que se llamaba `ipc.c`. Estaba vacío. Lo dejé ahí en febrero del 2025 para acordarme: tengo que escribir el post sobre cuándo aprendí IPC en Unix. Pipes primero. Signals después. Shared memory peleándomela un buen rato. Sockets Unix-domain mucho más tarde. Cada uno con su año, su anécdota y su moraleja. Acá está el post que el archivo vacío me debía. (El archivo `ipc.c` ya no existe — lo borré cuando este entry quedó listo.)"

**Outline:**
1. **Pipes anónimos** — el primero, el más simple, el más usado. `pipe(2)`, `popen(3)`. La idea de "el output de uno es el input del otro" sin pasar por disco. Por qué `cat foo | grep bar` funciona y qué pasa por debajo.
2. **FIFOs (named pipes)** — los pipes con nombre. `mkfifo(3)`. Cuándo te das cuenta de que "todo es un archivo" en Unix es verdad y por qué importa: dos procesos sin relación de parentesco pueden comunicarse a través de un nodo en el filesystem. La anécdota de cuándo lo usé bien por primera vez.
3. **Signals** — el mecanismo menos amigable. `signal(2)`, `sigaction(2)`. La trampa de los handlers no re-entrantes. La regla de oro que aprendí a los golpes: en un signal handler solo se hace `write()` y se setean variables `volatile sig_atomic_t`. Todo lo demás es bug latente.
4. **Shared memory (System V)** — `shmget`, `shmat`, `shmdt`, `shmctl`. La primera vez que usé `shmget` y entendí *de verdad* que dos procesos podían escribir al mismo segmento y que la sincronización era *mi* problema. La introducción a los semáforos como complemento obligatorio. La transición a POSIX shared memory (`shm_open`) años después.
5. **Sockets Unix-domain** — el descubrimiento tardío. `socket(AF_UNIX, ...)`. Por qué son hoy la primera elección para IPC local: tienen el modelo familiar de sockets, sin la latencia de TCP, con permisos de filesystem y con `SCM_RIGHTS` para pasar file descriptors entre procesos (la magia que hace funcionar a `dbus`, `systemd`, `wayland`).
6. **Lo que sobrevive de cada una en las herramientas modernas**:
   - **D-Bus** = signals + sockets Unix-domain bien empaquetados.
   - **Redis pub/sub** = shared memory conceptual, distribuida por red.
   - **gRPC** = sockets bien empaquetados con un schema compiler.
   - **systemd journal** = shared memory ring-buffer con sockets para readers.
   - **ZeroMQ / NATS** = el patrón pub/sub abstraído del transporte.
7. **La lección estructural** — aprender los cinco primitivos en C te hace mejor diseñador de sistemas distribuidos modernos. No porque vayas a usar `shmget` en producción, sino porque entendés *qué problema resuelve cada abstracción* y por qué eligieron resolverlo así.
8. **Cierre** — el archivo `ipc.c` ya no necesita estar vacío. Acá está el código compilable que reúne los cinco ejemplos en un solo binario didáctico (compilable con `cc ipc.c -o ipc`, sin dependencias). Lo subo al repo y lo enlazo desde el post.

**Bibliografía:**
- [W Richard Stevens, *UNIX Network Programming, Volume 2: Interprocess Communications*, 2nd ed Prentice Hall 1998](http://www.kohala.com/start/unpv22e/unpv22e.html) — la biblia. Si tenés que comprar un solo libro de IPC, este.
- [W Richard Stevens & Stephen A Rago, *Advanced Programming in the UNIX Environment*, 3rd ed Addison-Wesley 2013](https://www.apuebook.com/) — para el contexto Unix general.
- [Beej Jorgensen, *Beej's Guide to Unix IPC*](https://beej.us/guide/bgipc/) — la introducción libre y didáctica, todo lo esencial en una página HTML.
- [Beej Jorgensen, *Beej's Guide to Network Programming*](https://beej.us/guide/bgnet/) — el companion sobre sockets, igual de bueno.
- [Linux man pages — *sysvipc(7)*](https://man7.org/linux/man-pages/man7/sysvipc.7.html) — overview oficial de System V IPC.
- [Linux man pages — *shm_overview(7)*](https://man7.org/linux/man-pages/man7/shm_overview.7.html) — POSIX shared memory.
- [Linux man pages — *signal(7)*](https://man7.org/linux/man-pages/man7/signal.7.html) — el infierno de los signals, oficial.
- [Linux man pages — *unix(7)*](https://man7.org/linux/man-pages/man7/unix.7.html) — sockets Unix-domain.
- [Wikipedia — Inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) — overview general.
- [Brian Kernighan & Dennis Ritchie, *The C Programming Language*, 2nd ed Prentice Hall 1988](https://archive.org/details/the-c-programming-language) — referencia canónica de C, capítulo 7 y 8 para system calls.
- [Michael Kerrisk, *The Linux Programming Interface*, No Starch 2010](https://man7.org/tlpi/) — la biblia moderna del Linux/Unix programming, incluye los cinco mecanismos con la profundidad correcta.
- [Eric S Raymond, *The Art of Unix Programming*, Addison-Wesley 2003 — capítulo sobre IPC](http://www.catb.org/~esr/writings/taoup/html/ch07s02.html) — el ángulo filosófico ("simple text streams over complex IPC").

**Imágenes:**
- _Crear_: tabla comparativa de los 5 mecanismos IPC (latencia típica, persistencia, semántica de fallo, cuándo usar cada uno, mecanismo moderno equivalente) (~45 min) — esta tabla es probablemente lo más útil del post.
- _Crear_: cinco diagramitos pequeños (uno por mecanismo) mostrando dos procesos comunicándose (~1 hora).
- _Opcional_: árbol de decisión "qué IPC usar para tu caso" (~30 min).

**Tags propuestos:** `['IPC', 'C', 'Unix', 'pipes', 'sockets', 'shared memory', 'signals', 'memoir', 'systems']`

**Estado actual:** seed físico (`ipc.c`, archivo `.c` vacío de 0 bytes en la raíz de `just-ideas-for-future-posts/`, fechado 2025-02-03). **Concepto confirmado por el autor el 2026-04-08**: el archivo es un recordatorio físico para escribir este memoir técnico. Acción a hacer junto con la publicación del post: rellenar el archivo `ipc.c` con el código compilable que reúne los cinco ejemplos didácticos, y enlazarlo desde el post como descarga directa.

