"""Revisa un sitio ya construido: enlaces internos, notas al pie y restos de `hugo server`.

Uso: check_site.py DIR

- Enlaces internos: cada href="/..." tiene que existir como archivo o como
  directorio con index.html. Atrapa el bundle con fecha en el URL y el `.md`
  que quedó en un enlace.
- Notas al pie, página por página: definidas contra referenciadas, y un `[^`
  suelto, que es una definición que quedó pegada a otra línea.
- livereload y localhost: rastros de una build de `hugo server`.
"""

import re
import sys
import urllib.parse
from pathlib import Path

# El post de 2016 sobre Jekyll cita una configuración que menciona localhost:4000.
LOCALHOST_OK = {"posts/jekyll-hpstr-como-eliminar-el-ejemplo/index.html"}
# Las notas al pie se revisan sólo en la página de cada post: los listados
# (inicio, tags, paginación) muestran resúmenes con referencias cuya definición
# está en el post.
POST_PAGE = re.compile(r"^(en/)?posts/(?!page/)[^/]+/index\.html$")


def main(root: Path) -> int:
    pages = sorted(root.rglob("*.html"))
    if not pages:
        print(f"{root}: no hay páginas; ¿se construyó?")
        return 1
    problems = []
    for page in pages:
        rel = page.relative_to(root).as_posix()
        text = page.read_text(encoding="utf-8", errors="replace")
        for href in re.findall(r'href="?(/[^"\s>#?]*)', text):
            target = root / urllib.parse.unquote(href.lstrip("/"))
            if not (target.is_file() or (target / "index.html").is_file()):
                problems.append(f"{rel}: enlace roto {href}")
        if POST_PAGE.match(rel):
            defs = set(re.findall(r'id="?fn:([^"\s>]+)', text))
            refs = set(re.findall(r'href="?#fn:([^"\s>]+)', text))
            problems += [f"{rel}: nota definida y nunca referenciada [^{n}]" for n in sorted(defs - refs)]
            problems += [f"{rel}: nota referenciada y nunca definida [^{n}]" for n in sorted(refs - defs)]
            if "[^" in text:
                problems.append(f"{rel}: `[^` suelto ({text.count('[^')})")
        if "livereload" in text:
            problems.append(f"{rel}: script de livereload (build de hugo server)")
        if "localhost:" in text and rel not in LOCALHOST_OK:
            problems.append(f"{rel}: menciona localhost: (¿build de hugo server?)")
    for p in problems:
        print(p)
    print(f"{len(pages)} páginas, {len(problems)} problemas")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(Path(sys.argv[1])))
