"""Pide cada URL externa de los posts dados y avisa las que no responden.

Uso: check_urls.py content/es/posts/<bundle>/index.md [...]

No mira los bloques de código ni el código en línea. Un enlace a un repo propio
de GitHub da 404 hasta que se hace el push: es lo esperado, no un error del post.
"""

import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# Varios sitios rechazan el User-Agent por defecto de urllib.
UA = {"User-Agent": "Mozilla/5.0 (katra-blog link check; https://katra.ballardini.com.ar/)"}
CODE = re.compile(r"^```.*?^```|`[^`\n]+`", re.S | re.M)
URL = re.compile(r"https?://[^\s)\]>\"'«»]+")


def status(url: str) -> int | str:
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405, 501):
                return e.code
        except Exception as e:  # timeout, DNS, TLS
            return type(e).__name__
    return "?"


def main(files: list[str]) -> int:
    urls: dict[str, set[str]] = {}
    for f in files:
        text = CODE.sub("", Path(f).read_text(encoding="utf-8"))
        for u in URL.findall(text):
            urls.setdefault(u.rstrip(".,;:"), set()).add(f)
    with ThreadPoolExecutor(8) as pool:
        results = dict(zip(urls, pool.map(status, urls)))
    bad = {u: s for u, s in results.items() if not (isinstance(s, int) and s < 400)}
    for u, s in sorted(bad.items()):
        print(f"{s}  {u}")
    print(f"{len(urls)} URL, {len(bad)} sin responder")
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
