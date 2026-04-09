### G-19 — Apps GUI legadas en VMs: Enterprise Architect Lite y Visual Paradigm sobre Wine + Vagrant

- **Archivo seed (repo POC):** [github.com/CesarBallardini/enterprise-architect-lite](https://github.com/CesarBallardini/enterprise-architect-lite) — Shell, 2022-06-21 — más [github.com/CesarBallardini/visual-paradigm-community](https://github.com/CesarBallardini/visual-paradigm-community)
- **Slug propuesto:** `apps-gui-legadas-vms-wine`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-apps-gui-legadas-vms-wine/index.md`
- **Serie:** G
- **Cross-links:** complementa [[G-18]] (mismo problema, otra solución)
- **Idioma:** es
- **Madurez:** **complete-poc** ambos
- **Length target:** short (800-1200 palabras)

**Concepto:** mientras [[G-18]] resuelve el problema del display en Docker, este post resuelve el problema *adyacente*: cuando la app es Windows-only, propietaria, o requiere un toolkit que no funciona en Linux nativo. Solución: una VM Vagrant con Wine encima, donde corre Enterprise Architect Lite (`.eap` viewer) o Visual Paradigm Community Edition. La técnica es vieja pero sigue siendo la respuesta correcta para muchas apps "viejas pero útiles".

**Hook:** "necesitás abrir un `.eap` (Enterprise Architect) que un colega te pasó. EA no tiene cliente Linux. No querés instalar Wine en tu host. Solución: una VM Vagrant Ubuntu con Wine pre-configurado, EA Lite ya instalado. `vagrant up`, abrís el archivo, listo. Acá lo armé para EA Lite y Visual Paradigm."

**Outline:**
1. Por qué a veces VMs son la respuesta: Wine no siempre funciona en tu host, dependencias propietarias, cuestiones de licencia.
2. El patrón: VM Vagrant Ubuntu + Wine + la app.
3. Caso EA Lite: descargar el instalador, correrlo dentro de Wine, exponer el filesystem del host para abrir archivos `.eap`.
4. Caso Visual Paradigm Community: similar pero con instalación nativa Linux (no requiere Wine).
5. La trampa de los archivos: cómo compartir el filesystem entre host y VM (synced folders).
6. Cierre.

**Bibliografía:**
- Repos: [enterprise-architect-lite](https://github.com/CesarBallardini/enterprise-architect-lite), [visual-paradigm-community](https://github.com/CesarBallardini/visual-paradigm-community).
- [Sparx Systems Enterprise Architect](https://sparxsystems.com/).
- [Visual Paradigm Community](https://www.visual-paradigm.com/download/community.jsp).
- [Wine — sitio oficial](https://www.winehq.org/).

**Imágenes:**
- _Crear_: screenshot de EA Lite abriendo un `.eap` desde adentro de la VM (~10 min).

**Tags propuestos:** `['Vagrant', 'Wine', 'Enterprise Architect', 'Visual Paradigm', 'GUI', 'Windows apps']`

**Estado actual:** **complete-poc** ambos.

