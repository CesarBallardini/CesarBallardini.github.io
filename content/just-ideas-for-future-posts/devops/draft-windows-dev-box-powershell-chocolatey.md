### G-31 — Windows dev box setup scripts: automatizar la laptop corporativa con PowerShell + Chocolatey

- **Archivo seed:** `github.com/CesarBallardini/windows-dev-box-setup-scripts` (fork, PowerShell, Sep 2022)
- **Slug propuesto:** `windows-dev-box-powershell-chocolatey`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-windows-dev-box-powershell-chocolatey/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-07]] (Docker en Windows), [[G-08]] (ansible-devops-workstation — el primo Linux), [[E-04]] (entorno Python)
- **Idioma:** es
- **Madurez:** fork de los scripts de Microsoft (repo original abandonado), adaptación parcial
- **Length target:** medium (1000-1500 palabras)

**Concepto:** Microsoft publicó hace años un set de scripts PowerShell para automatizar el setup de una "dev box" en Windows — Chocolatey + Scoop + winget + configuraciones + herramientas. Lo forkeé para adaptarlo a mi workflow. El post explica cómo automatizar el setup de una laptop Windows para desarrollo (contraparte de [[G-08]] que es para Linux) y por qué en 2026 la respuesta razonable incluye WSL2 + winget + dotfiles en git.

**Hook:** "te dieron una laptop Windows nueva para trabajo. Tenés que instalar 30 cosas. Lo hacés a mano. En 2 horas ya perdiste la mitad del día. O: corrés un script PowerShell y en 20 minutos está todo. El post es sobre el script y sobre por qué en Windows la automatización de dev box importa *más* que en Linux, no menos."

**Outline:**
1. El escenario: nueva laptop corporativa con Windows, no tenés admin pleno pero sí PowerShell.
2. Las herramientas: winget (oficial), Chocolatey (histórico), Scoop (alternativa).
3. Lo que instalo: Git, VSCode, WSL2, Python, Node, Docker Desktop o alternativa, clientes SSH, terminal Alacritty/WezTerm.
4. La parte de configuración: dotfiles en git, PowerShell profile, perfiles de Windows Terminal.
5. La integración con WSL2: dónde empieza Windows y dónde Linux.
6. Cierre: el fork adaptado está en mi GitHub.

**Bibliografía:**
- [Microsoft — winget documentation](https://learn.microsoft.com/en-us/windows/package-manager/winget/).
- [Chocolatey](https://chocolatey.org/).
- [Scoop](https://scoop.sh/).
- [Microsoft Sandbox / DevBox original project](https://github.com/Microsoft/windows-dev-box-setup-scripts).

**Imágenes:**
- _Crear_: tabla winget vs Chocolatey vs Scoop (~30 min).
- _Crear_: diagrama del flujo de setup (~30 min).

**Tags propuestos:** `['Windows', 'PowerShell', 'Chocolatey', 'winget', 'Scoop', 'devenv']`

**Estado actual:** fork funcional con mis adaptaciones parciales; el post sale natural.

