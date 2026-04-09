### G-20 — eCryptfs en 2026: por qué ya no, y cómo migrar tu HOME cifrado a LUKS

- **Archivo seed (repo POC):** [github.com/CesarBallardini/ubuntu18-encrypted-home](https://github.com/CesarBallardini/ubuntu18-encrypted-home) — sin lenguaje primario, último push 2019-11-18
- **Slug propuesto:** `ecryptfs-deprecado-migrar-luks`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-ecryptfs-deprecado-migrar-luks/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[H-01]] (legacy archeology), [[E-12]]
- **Idioma:** es
- **Madurez:** **partial-poc** — el tutorial de eCryptfs migration existe, otras secciones (LUKS, dm-crypt, fscrypt, VeraCrypt) son stubs
- **Length target:** medium (1500-2000 palabras)

**Concepto:** Ubuntu deprecó eCryptfs (encrypted home directories per-user) después de 18.04 Bionic. La gente que tenía notebooks viejas con HOMES eCryptfs se quedó con un sistema que no recibía soporte oficial. Mi repo tiene un tutorial para migrar de eCryptfs a no-cifrado (paso intermedio) sobre Bionic. El post lo amplía a 2026: por qué eCryptfs ya no, qué alternativas existen (LUKS, dm-crypt, fscrypt, VeraCrypt), y cómo elegir.

**Hook:** "tenías una notebook con Ubuntu 14.04 con HOME cifrado por eCryptfs. Después actualizaste a 18.04. Después intentaste actualizar a 20.04 y Ubuntu te dijo 'eCryptfs is deprecated'. Te quedaste atascado. Acá explico por qué pasó, qué alternativas tenés, y cómo migrar sin perder los datos."

**Outline:**
1. Qué era eCryptfs y por qué Ubuntu lo deprecó.
2. La situación de transición: notebooks viejas que no se pueden actualizar.
3. La migración intermedia: descifrar en Bionic, salvar los datos, migrar a una solución moderna.
4. Las alternativas modernas:
   - **LUKS / dm-crypt** — disco completo o partición, no per-user.
   - **fscrypt** — la respuesta nativa de ext4 para per-directory encryption.
   - **VeraCrypt** — el sucesor multiplataforma de TrueCrypt, contenedores cifrados.
5. Cómo elegir: por qué LUKS para casi todo el mundo en 2026.
6. Cierre.

**Bibliografía:**
- Repo del POC: [CesarBallardini/ubuntu18-encrypted-home](https://github.com/CesarBallardini/ubuntu18-encrypted-home).
- [eCryptfs — sitio histórico](https://www.ecryptfs.org/).
- [Ubuntu encryption deprecation announcement](https://ubuntu.com/blog/) — buscar el anuncio específico.
- [LUKS / cryptsetup docs](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/home).
- [fscrypt — kernel docs](https://www.kernel.org/doc/html/latest/filesystems/fscrypt.html).
- [VeraCrypt — sitio oficial](https://www.veracrypt.fr/).

**Imágenes:**
- _Crear_: tabla comparativa eCryptfs vs LUKS vs fscrypt vs VeraCrypt (~30 min).

**Tags propuestos:** `['eCryptfs', 'LUKS', 'fscrypt', 'VeraCrypt', 'cifrado', 'Ubuntu', 'migracion']`

**Estado actual:** **partial-poc**, eCryptfs migration guide existe, resto stub.

