### G-30 — Packer + OpenVPN: construir AMIs reproducibles para bastión VPN

- **Archivo seed:** `github.com/CesarBallardini/packer-openvpn` (own, Shell, Oct 2016) + `github.com/CesarBallardini/packer-templates` (fork PowerShell, Sep 2016)
- **Slug propuesto:** `packer-openvpn-ami-reproducible`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-packer-openvpn-ami-reproducible/index.md`
- **Serie:** G
- **Cross-links:** lleva a [[G-17]] (Partman + Preseed con Packer), [[G-02]] (infra determinística)
- **Idioma:** es
- **Madurez:** **viejo (2016)**, funcional en su momento, hoy seguro desactualizado
- **Length target:** short (800-1200 palabras)

**Concepto:** *Packer* (de HashiCorp) construye imágenes de máquina virtual de manera reproducible a partir de un template declarativo. El post usa dos forks viejos (2016): uno mío con un template Packer para construir una AMI de OpenVPN, otro fork de templates genéricos. El post es un memoir técnico honesto sobre esa etapa: "cómo se sentía hacer IaC en 2016, antes de que fuera normal".

**Hook:** "en 2016 armé un template Packer que construía una AMI de Amazon con OpenVPN preinstalado, configurado, listo para `terraform apply` y quedar ejecutándose. Hoy suena a cosa de rutina. En 2016 era artesanía. El post es el memoir de esa etapa, y el honor que le debemos a Mitchell Hashimoto por haber inventado Packer, Vagrant y Terraform en la misma década."

**Outline:**
1. Qué era Packer en 2016 y por qué fue una revolución.
2. El template OpenVPN: provisioner shell + Ansible + cleanup.
3. El workflow: `packer build` → AMI nueva → `terraform apply` → bastion corriendo.
4. Lo que envejeció mal: versiones de OpenVPN, la fixture de Amazon Linux 1, los plugins de Packer que cambiaron API.
5. Lo que sobrevive: la filosofía "imagen declarativa reproducible" es el corazón de todo el IaC moderno.
6. Cierre: el repo sigue pero no corre. Es arqueología.

**Bibliografía:**
- [Packer — sitio oficial](https://www.packer.io/).
- [HashiCorp — historia de Packer + Vagrant + Terraform](https://www.hashicorp.com/).
- [Mitchell Hashimoto — blog posts históricos](https://mitchellh.com/).
- [OpenVPN — sitio oficial](https://openvpn.net/).

**Imágenes:**
- _Crear_: diagrama del workflow packer build → AMI → terraform (~30 min).

**Tags propuestos:** `['Packer', 'OpenVPN', 'HashiCorp', 'AMI', 'IaC', 'historia']`

**Estado actual:** **fork viejo 2016**, el post sería un memoir histórico más que un tutorial operativo.

