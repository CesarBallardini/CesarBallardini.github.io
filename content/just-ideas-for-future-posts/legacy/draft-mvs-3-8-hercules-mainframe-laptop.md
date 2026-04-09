### H-10 — IBM MVS 3.8j sobre Hercules: corriendo un mainframe IBM en mi notebook

- **Archivo seed (repo POC):** [github.com/CesarBallardini/mvs-on-hercules](https://github.com/CesarBallardini/mvs-on-hercules) — Ruby, último push 2022-02-07
- **Slug propuesto:** `mvs-3-8-hercules-mainframe-laptop`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-mvs-3-8-hercules-mainframe-laptop/index.md`
- **Serie:** H — flagship mainframe; cruza con [[D-03]] (Turing) y [[A1-08]] (KL1, otra "máquina de otra época")
- **Cross-links:** lleva a [[H-11]] (s390x Linux), [[H-12]] (prtspool), [[H-04]] (COBOL→GnuCOBOL); cruza con [[H-06]] (parábola)
- **Idioma:** es
- **Madurez:** **complete-poc** — README extremadamente rico con bibliografía
- **Length target:** long (2500-3500 palabras), o mini-serie de 3-4 posts

**Concepto:** **Hercules** es un emulador open-source de mainframes IBM (System/370, ESA/390, z/Architecture) que corre en cualquier Linux. **MVS 3.8j Tur(n)key 4-** es una distribución completa de MVS (la generación que precedió a OS/390 y z/OS), empaquetada por la comunidad para correr en Hercules — y, por una rareza histórica, *legalmente distribuible* porque IBM la liberó. El resultado: podés tener un mainframe IBM 3033-clase completo, con TSO, JCL, ISPF y compiladores COBOL/Fortran/PL-I, corriendo en una VM Vagrant en tu notebook. Mi POC arma todo eso con Vagrant + Hercules + MVS 3.8j Tur(n)key 4- + Docker o VirtualBox como provider, y deja el sistema arrancado y listo para hacer LOGON con HERC01-4 / IBMUSER.

**Hook:** "tengo un mainframe IBM en mi notebook. No es metáfora. Es MVS 3.8j corriendo sobre Hercules, con TSO, JCL, ISPF y compiladores COBOL. Hago `vagrant up`, espero un par de minutos, hago LOGON con IBMUSER, y veo el prompt READY. Es 2026 y estoy operando un mainframe que IBM lanzó en los 70."

**Outline:**
1. Hercules en 30 segundos: emulador open-source de System/370/390/zArch, escrito en C, mantenido desde 1999 por Roger Bowler y comunidad.
2. MVS 3.8j en 30 segundos: la última versión de MVS que IBM liberó (verificar matiz legal exacto).
3. Tur(n)key 4-: la distribución comunitaria que empaqueta MVS 3.8j + RAKF + parches + utilidades.
4. Mi POC `mvs-on-hercules`: Vagrant + Ubuntu + Hercules + Tur(n)key 4-. Provider Docker o VirtualBox.
5. El primer LOGON: cómo conectarse al mainframe (3270 emulator: c3270, x3270, tn3270 protocol).
6. Las cuentas predefinidas: HERC01-4 (admin), IBMUSER (super-user).
7. Lo que se puede hacer en sesión TSO: JCL submit, ISPF (editor full-screen), compilar un COBOL.
8. La conexión con [[H-04]] (compilar contra el compilador *real* de IBM en vez de GnuCOBOL).
9. La sub-historia del print spooling — cross [[H-12]].
10. Cierre: la sensación honesta de "estoy operando un cacharro de los 70 y funciona perfecto".

**Bibliografía:**
- Repo del POC: [CesarBallardini/mvs-on-hercules](https://github.com/CesarBallardini/mvs-on-hercules) — README muy rico, reusar bibliografía.
- [Hercules — sitio oficial](http://www.hercules-390.org/).
- [Hercules SDL fork mantenido](https://github.com/SDL-Hercules-390/hyperion).
- [Tur(n)key 4- en wotho.ethz.ch](https://wotho.ethz.ch/tk4-/).
- [MVS 3.8j — Wikipedia](https://en.wikipedia.org/wiki/MVS).
- *Running your own mainframe on Linux for fun and profit*, Vintage Computer Festival Berlin 2018 — buscar la charla específica en YouTube.
- *My Own Mainframe* blog series — verificar URL.
- [Mike Murach, *Murach's Mainframe COBOL*, Murach 2004](https://www.murach.com/) — referencia COBOL/JCL.
- [c3270 / x3270 — IBM 3270 emulator](http://x3270.bgp.nu/).

**Imágenes:**
- _Crear_: screenshot del logon TSO con prompt READY (~10 min — la imagen mítica).
- _Crear_: screenshot de ISPF en sesión 3270 (~10 min).
- _Crear_: diagrama de la pila Vagrant → Ubuntu host → Hercules → MVS 3.8j → TSO (~45 min).

**Tags propuestos:** `['MVS', 'Hercules', 'mainframe', 'IBM', 'TSO', 'JCL', 'ISPF', 'Vagrant', 'arqueologia']`

**Estado actual:** **POC completo y replicable**. README muy rico — puede dar varios posts si se desdobla en mini-serie.

