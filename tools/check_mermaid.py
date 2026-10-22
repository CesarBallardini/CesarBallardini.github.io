"""Valida cada bloque ```mermaid de los posts dados contra mermaid.ink.

Uso: check_mermaid.py content/es/posts/<bundle>/index.md [...]

Si el post tiene `mermaid_html_labels: true`, manda la misma configuración que
usa el sitio (securityLevel antiscript + htmlLabels). Un 400 o 404 es un error
de sintaxis que de otro modo aparecería recién en la página publicada.
"""

import base64
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# mermaid.ink contesta 403 al User-Agent por defecto de urllib.
UA = {"User-Agent": "katra-blog-check/1.0 (https://katra.ballardini.com.ar/)"}
HTML_LABELS = {"theme": "neutral", "securityLevel": "antiscript", "flowchart": {"htmlLabels": True}}


def check(code: str, html_labels: bool) -> int:
    payload = json.dumps({"code": code, "mermaid": HTML_LABELS}) if html_labels else code
    url = "https://mermaid.ink/svg/" + base64.urlsafe_b64encode(payload.encode()).decode()
    # Un 5xx es mermaid.ink caído o saturado, no un error del diagrama: reintentar.
    for wait in (0, 5, 15):
        time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if e.code < 500:
                return e.code
            status = e.code
    return status


def main(files: list[str]) -> int:
    total = bad = unknown = 0
    for f in files:
        text = Path(f).read_text(encoding="utf-8").replace("\r\n", "\n")
        html_labels = re.search(r"^mermaid_html_labels:\s*true\s*$", text, re.M) is not None
        for n, code in enumerate(re.findall(r"^```mermaid\n(.*?)\n```", text, re.S | re.M), 1):
            total += 1
            s = check(code, html_labels)
            if s >= 500:
                unknown += 1
                print(f"{s}  {f}  diagrama {n}: mermaid.ink no respondió, sin validar")
            elif s != 200:
                bad += 1
                print(f"{s}  {f}  diagrama {n}: {code.splitlines()[0]}")
    print(f"{total} diagramas, {bad} con error, {unknown} sin validar")
    return 1 if bad or unknown else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
