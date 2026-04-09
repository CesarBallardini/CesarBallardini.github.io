### G-23 — OpenGrok bajo Tomcat con Ansible: indexar código fuente de proyectos legacy

- **Archivo seed:** `github.com/CesarBallardini/opengrok_role` (fork, HTML, Apr 2021)
- **Slug propuesto:** `opengrok-ansible-legacy-code-search`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-opengrok-ansible-legacy-code-search/index.md`
- **Serie:** G — con puente fuerte a la Serie H (archeología de sistemas legacy)
- **Cross-links:** lleva a [[H-02]] (RM COBOL), [[H-04]] (COBOL→GnuCOBOL), [[H-07]] (FoxBase→PG), [[G-01]] (Ansible roles/profiles)
- **Idioma:** es
- **Madurez:** fork de un role Ansible funcional
- **Length target:** medium (1200-1600 palabras)

**Concepto:** OpenGrok es un motor de búsqueda/indexación de código fuente desarrollado originalmente en Sun para indexar el código de Solaris. Corre como webapp en Tomcat. Indexa repositorios Git/SVN/Mercurial y te da búsquedas tipo `grep -r` pero con UI web, navegación por símbolos, cross-references. Para quien administra proyectos legacy con millones de líneas (ver Serie H), OpenGrok es la herramienta correcta. El post explica cómo montarlo con el role Ansible que forkeé, y por qué en 2026 sigue siendo la mejor respuesta para este caso de uso (ni Sourcegraph free ni GitHub Code Search cubren proyectos cerrados en SVN local).

**Hook:** "tenés que buscar todas las llamadas a una función en un proyecto COBOL de 800.000 líneas. Tu editor se cuelga. `grep -r` funciona pero es ciego a la semántica. GitHub Code Search no ve tu repo privado en SVN. ¿Qué usabas en 2008 en este caso? OpenGrok. ¿Qué seguís usando en 2026? OpenGrok. El post explica por qué."

**Outline:**
1. Qué es OpenGrok (historia Sun, hoy Oracle).
2. Por qué para proyectos legacy: soporta SVN, CVS, Perforce, Mercurial. Indexa símbolos. Corre on-prem.
3. El role Ansible: Tomcat + OpenGrok + cron para re-indexar + nginx reverse proxy.
4. La configuración mínima: path del repo, frecuencia de reindex, autenticación HTTP.
5. Lo que no hace bien: performance en proyectos > 10GB, búsquedas en lenguajes no soportados por el parser.
6. Las alternativas modernas que consideré y descarté para el caso legacy: Sourcegraph (demasiado heavy, licencia cambió), GitHub Code Search (no ve repos no-git), livegrep (no hace símbolos).
7. Cierre: el role Ansible está en mi fork, funciona.

**Bibliografía:**
- [OpenGrok — sitio oficial](https://oracle.github.io/opengrok/).
- [OpenGrok en GitHub](https://github.com/oracle/opengrok).
- [Apache Tomcat documentation](https://tomcat.apache.org/tomcat-9.0-doc/index.html).
- [Sourcegraph — sitio oficial (para comparación)](https://sourcegraph.com/).
- [livegrep](https://livegrep.com/) — alternativa ligera.

**Imágenes:**
- _Crear_: screenshot de la UI de OpenGrok buscando un símbolo en un proyecto legacy (~15 min).
- _Crear_: diagrama de la pila Ansible role: Tomcat + OpenGrok + nginx (~30 min).

**Tags propuestos:** `['OpenGrok', 'Ansible', 'Tomcat', 'code search', 'legacy', 'Subversion', 'sysadmin']`

**Estado actual:** fork del role funcional, material listo para escribir.

