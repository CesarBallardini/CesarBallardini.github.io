#!/usr/bin/env python3
"""
Genera el esquemático de la matriz de diodos de UNA rueda hexadecimal.

Codifica los 16 detentes de una llave rotativa común en 4 líneas binarias
más una línea POS0 de validez: 33 diodos por rueda, 264 para las ocho.

Topología:
  · El polo común de la llave va a masa.
  · Cada terminal de posición sube por su propia línea vertical.
  · Cinco rieles horizontales (b3 b2 b1 b0 POS0) cruzan por arriba.
  · Donde el bit vale 1 se monta un diodo: ánodo al riel, cátodo al terminal.
  · Cada riel lleva pull-up de 10k a +5V y 1k en serie hacia el 74HC165.

Al seleccionar una posición su terminal queda a masa, los diodos que cuelgan
de él conducen y bajan sus rieles a ~0,7 V — por debajo del VIL de 1,5 V del
74HC a 5 V. Los terminales no seleccionados flotan y sus diodos quedan en
inversa. El código leído es el COMPLEMENTO del valor: hay que invertirlo en
firmware.

Los cruces entre líneas verticales y rieles NO se conectan: en KiCad dos
cables que se cruzan sin junction no forman nodo.

Uso:
    uv run python generar-matriz-diodos.py
    kicad-cli sch export pdf --output matriz-diodos.pdf matriz-diodos.kicad_sch
"""

import uuid as _uuid

GRID = 1.27


def g(v):
    return round(round(v / GRID) * GRID, 4)


def U():
    return str(_uuid.uuid4())


FONT = "(effects (font (size 1.27 1.27)))"
LIB = "os370m"

# ── Símbolos ────────────────────────────────────────────────────────────────
# Llave rotativa 1 de 16: polo + 16 terminales de posición.
def sw16():
    h = 18 * 2.54
    hh, hw = h / 2, 10.16
    s = [f'\t\t(symbol "{LIB}:SW_ROT16"',
         '\t\t\t(pin_names (offset 0.508))',
         '\t\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)',
         f'\t\t\t(property "Reference" "SW" (at {-hw} {hh+2} 0) {FONT})',
         f'\t\t\t(property "Value" "Rotativa 16 pos" (at {-hw} {-hh-3} 0) '
         f'(effects (font (size 1.27 1.27)) (justify left)))',
         '\t\t\t(symbol "SW_ROT16_0_1"',
         f'\t\t\t\t(rectangle (start {-hw} {hh}) (end {hw} {-hh})',
         '\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type background)))',
         '\t\t\t)',
         '\t\t\t(symbol "SW_ROT16_1_1"',
         f'\t\t\t\t(pin passive line (at {-hw-2.54} {hh-2.54} 0) (length 2.54)'
         f' (name "POLO" {FONT}) (number "C" {FONT}))']
    for i in range(16):
        y = hh - 2.54 * (i + 2)
        s.append(f'\t\t\t\t(pin passive line (at {hw+2.54} {y} 180) (length 2.54)'
                 f' (name "P{i:X}" {FONT}) (number "{i}" {FONT}))')
    s += ['\t\t\t)', '\t\t)']
    return "\n".join(s)


def small(name, ref, graphic, pins):
    return (f'\t\t(symbol "{LIB}:{name}"\n'
            '\t\t\t(pin_numbers (hide yes)) (pin_names (offset 0) (hide yes))\n'
            '\t\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)\n'
            f'\t\t\t(property "Reference" "{ref}" (at 0 3.556 0) {FONT})\n'
            f'\t\t\t(property "Value" "{name}" (at 0 -3.81 0) {FONT})\n'
            f'\t\t\t(symbol "{name}_0_1"\n{graphic}\n\t\t\t)\n'
            f'\t\t\t(symbol "{name}_1_1"\n{pins}\n\t\t\t)\n\t\t)')


SYMS = [
    sw16(),
    small("R", "R",
          '\t\t\t\t(rectangle (start -1.016 2.54) (end 1.016 -2.54)\n'
          '\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))',
          f'\t\t\t\t(pin passive line (at 0 5.08 270) (length 2.54) (name "~" {FONT}) (number "1" {FONT}))\n'
          f'\t\t\t\t(pin passive line (at 0 -5.08 90) (length 2.54) (name "~" {FONT}) (number "2" {FONT}))'),
    # Diodo: cátodo abajo (hacia el terminal de posición), ánodo arriba (al riel)
    small("D", "D",
          '\t\t\t\t(polyline (pts (xy -1.27 -1.27) (xy 1.27 -1.27))\n'
          '\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))\n'
          '\t\t\t\t(polyline (pts (xy -1.27 1.27) (xy 1.27 1.27) (xy 0 -1.27) (xy -1.27 1.27))\n'
          '\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type outline)))',
          f'\t\t\t\t(pin passive line (at 0 3.81 270) (length 2.54) (name "A" {FONT}) (number "1" {FONT}))\n'
          f'\t\t\t\t(pin passive line (at 0 -3.81 90) (length 2.54) (name "K" {FONT}) (number "2" {FONT}))'),
    small("+5V", "#PWR",
          '\t\t\t\t(polyline (pts (xy -0.762 1.27) (xy 0 2.54) (xy 0.762 1.27))\n'
          '\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))\n'
          '\t\t\t\t(polyline (pts (xy 0 0) (xy 0 2.54))\n'
          '\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))',
          f'\t\t\t\t(pin power_in line (at 0 0 90) (length 0) (name "+5V" {FONT}) (number "1" {FONT}))'),
    small("GND", "#PWR",
          '\t\t\t\t(polyline (pts (xy -1.905 -1.27) (xy 1.905 -1.27) (xy 0 -2.921) (xy -1.905 -1.27))\n'
          '\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))\n'
          '\t\t\t\t(polyline (pts (xy 0 0) (xy 0 -1.27))\n'
          '\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))',
          f'\t\t\t\t(pin power_in line (at 0 0 270) (length 0) (name "GND" {FONT}) (number "1" {FONT}))'),
]

with open("os370-matriz.kicad_sym", "w", encoding="utf-8") as f:
    f.write('(kicad_symbol_lib\n\t(version 20241209)\n\t(generator "os370")\n'
            '\t(generator_version "10.0")\n')
    for s in SYMS:
        f.write(s.replace("\n\t\t", "\n\t")[1:] + "\n")
    f.write(")\n")

# ── Esquemático ─────────────────────────────────────────────────────────────
ROOT = U()
out = ["(kicad_sch", '\t(version 20250114)', '\t(generator "os370")',
       '\t(generator_version "10.0")', f'\t(uuid "{ROOT}")', '\t(paper "A3")',
       '\t(title_block',
       '\t\t(title "Matriz de diodos — una rueda hexadecimal A..H")',
       '\t\t(date "2026-08-02")', '\t\t(rev "A")',
       '\t\t(company "katra.ballardini.com.ar")',
       '\t\t(comment 1 "16 detentes -> 4 lineas binarias + 1 de validez POS0")',
       '\t\t(comment 2 "33 diodos por rueda · 264 para las ocho ruedas")',
       '\t\t(comment 3 "El codigo leido es el COMPLEMENTO: invertir en firmware")',
       '\t\t(comment 4 "Cruces sin punto de union NO conectan")',
       '\t)', '\t(lib_symbols']
out += SYMS
out.append('\t)')

refs = {}


def place(lib_name, ref, val, x, y, rot=0, hide_val=False):
    x, y = g(x), g(y)
    vis = '(hide yes) ' if hide_val else ''
    out.append(f'''\t(symbol
\t\t(lib_id "{LIB}:{lib_name}")
\t\t(at {x} {y} {rot})
\t\t(unit 1)
\t\t(exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
\t\t(uuid "{U()}")
\t\t(property "Reference" "{ref}" (at {x + 4.5} {y - 1.5} 0) (effects (font (size 1.0 1.0)) {'(hide yes) ' if ref.startswith('#') else ''}))
\t\t(property "Value" "{val}" (at {x + 4.5} {y + 1.5} 0) (effects (font (size 1.0 1.0)) {vis}))
\t\t(instances (project "" (path "/{ROOT}" (reference "{ref}") (unit 1))))
\t)''')


def wire(x1, y1, x2, y2):
    x1, y1, x2, y2 = g(x1), g(y1), g(x2), g(y2)
    out.append(f'\t(wire (pts (xy {x1} {y1}) (xy {x2} {y2}))'
               f' (stroke (width 0) (type default)) (uuid "{U()}"))')


def junction(x, y):
    out.append(f'\t(junction (at {g(x)} {g(y)}) (diameter 0) (color 0 0 0 0)'
               f' (uuid "{U()}"))')


def label(txt, x, y, rot=0, justify="left bottom"):
    out.append(f'\t(label "{txt}" (at {g(x)} {g(y)} {rot})'
               f' (effects (font (size 1.27 1.27)) (justify {justify})) (uuid "{U()}"))')


def text(txt, x, y, size=1.7):
    out.append(f'\t(text "{txt}" (at {g(x)} {g(y)} 0)'
               f' (effects (font (size {size} {size})) (justify left)) (uuid "{U()}"))')


# Geometría
SWX, SWY = 40.64, 132.08          # centro de la llave
hh = 18 * 2.54 / 2
POSX0 = SWX + 10.16 + 2.54        # x del primer pin de posición
COLX = 88.9                       # x de la primera columna vertical
DCOL = 15.24                      # separación entre columnas de posición
RAILY = [30.48, 43.18, 55.88, 68.58, 81.28]   # b3 b2 b1 b0 POS0
RAILN = ["b3", "b2", "b1", "b0", "POS0"]

place("SW_ROT16", "SW1", "Rotativa 16 pos", SWX, SWY)

# polo común a masa
px, py = SWX - 10.16 - 2.54, SWY - hh + 2.54
wire(px, py, px - 7.62, py)
wire(px - 7.62, py, px - 7.62, py + 15.24)
place("GND", "#PWR01", "GND", px - 7.62, py + 15.24)
text("POLO COMUN", px - 18, py - 4, 1.5)

# rieles horizontales + acondicionamiento de cada línea
RAILX1 = COLX - 20.32
RAILX2 = COLX + 15 * DCOL + 10.16
for i, (ry, rn) in enumerate(zip(RAILY, RAILN)):
    pux = RAILX1 - 6.35 - i * 8.89      # escalonado: si van alineados se pisan
    wire(pux, ry, RAILX2, ry)
    # pull-up 10k a +5V, cada uno en su propia columna
    wire(pux, ry, pux, ry - 5.08)
    place("R", f"R{10+i}", "10k", pux, ry - 10.16)
    wire(pux, ry - 15.24, pux, ry - 17.78)
    place("+5V", f"#PWR1{i}", "+5V", pux, ry - 17.78)
    # 1k en serie hacia el 74HC165 (a la derecha)
    wire(RAILX2, ry, RAILX2 + 7.62, ry)
    place("R", f"R{20+i}", "1k", RAILX2 + 12.7, ry, rot=90)
    wire(RAILX2 + 17.78, ry, RAILX2 + 25.4, ry)
    label(f"{rn}_A_74HC165", RAILX2 + 25.4, ry, 0, "left bottom")
    text(rn, pux - 12.7, ry + 0.6, 1.8)

# columnas: una por posición, con sus diodos
nd = 0
for pos in range(16):
    x = COLX + pos * DCOL
    ypin = SWY - hh + 2.54 * (pos + 2)
    # del pin de la llave hacia la derecha, y luego sube
    wire(POSX0, ypin, x, ypin)
    # bits en 1 -> diodo; POS0 sólo en la posición 0
    bits = [(0, (pos >> 3) & 1), (1, (pos >> 2) & 1),
            (2, (pos >> 1) & 1), (3, pos & 1), (4, 1 if pos == 0 else 0)]
    activos = [ri for ri, on in bits if on]
    if not activos:
        continue
    # La columna sube en TRAMOS que terminan en cada cátodo: un pin en el
    # medio de un cable no forma nodo en KiCad, tiene que ser un extremo.
    catodos = sorted((RAILY[ri] + 12.7 for ri in activos), reverse=True)
    prev = ypin
    for k, cy in enumerate(catodos):
        wire(x, prev, x, cy)
        if k < len(catodos) - 1:
            junction(x, cy)          # el tramo sigue: hace falta el punto
        prev = cy
    for ri in activos:
        ry = RAILY[ri]
        place("D", f"D{nd+1}", "1N4148", x, ry + 8.89, hide_val=True)
        wire(x, ry + 5.08, x, ry)    # ánodo al riel
        junction(x, ry)
        nd += 1
    # marcas de posición
    text(f"{pos:X}", x - 1.27, RAILY[0] - 7.62, 2.0)

text("POSICION (hex)", COLX - 42, RAILY[0] - 7.62, 2.0)

# ── Notas ───────────────────────────────────────────────────────────────────
# Van DEBAJO del diagrama y en dos columnas. El dibujo ocupa hasta y~155 y
# todo el ancho de la hoja, asi que cualquier bloque puesto arriba o a la
# derecha se le superpone y el texto queda ilegible.
NY0 = 168.0
NDY = 4.2
COL_A, COL_B = 18.0, 218.0

col_izq = [
    "MATRIZ DE DIODOS - UNA RUEDA",
    "",
    "16 detentes -> 4 lineas binarias (b3..b0)",
    "mas 1 linea de validez (POS0).",
    "33 diodos por rueda · 264 para las ocho.",
    "",
    "COMO FUNCIONA",
    "  El polo comun va a masa.  Al elegir una",
    "  posicion su terminal queda a masa y todos",
    "  los diodos que cuelgan de el conducen,",
    "  bajando sus rieles a ~0,7 V — por debajo",
    "  del VIL de 1,5 V del 74HC a 5 V.",
    "",
    "  Los terminales no elegidos flotan y sus",
    "  diodos quedan polarizados en inversa.",
    "",
    "  Se monta diodo donde el bit vale 1.  Como",
    "  el diodo BAJA la linea, el codigo leido es",
    "  el COMPLEMENTO del valor:",
    "",
    "        val = (~leido) & 0x0F",
    "",
    "NOTAS DE DIBUJO",
    "  Los cruces sin punto de union NO conectan.",
    "  Pull-up 10k por riel.",
    "  1k en serie protege el mazo largo.",
]

col_der = [
    "POR QUE LA LINEA POS0 NO ES OPCIONAL",
    "",
    "  Las rotativas son break-before-make:",
    "  mientras se gira, entre un detente y el",
    "  siguiente NINGUN terminal esta conectado",
    "  y las cuatro lineas flotan altas.",
    "",
    "  Eso se lee igual que una posicion 0",
    "  legitima.  Con POS0 se distinguen:",
    "",
    "   algun bit bajo + POS0 alto",
    "        -> posiciones 1..F, leer el codigo",
    "",
    "   todas altas    + POS0 BAJO",
    "        -> posicion 0 legitima",
    "",
    "   todas altas    + POS0 alto",
    "        -> ENTRE DETENTES: descartar y",
    "           conservar el ultimo valor valido",
    "",
    "  Sin POS0 una rueda a medio girar informa",
    "  cero en silencio.  En las ruedas F G H,",
    "  que son LOAD UNIT ADDRESS, eso significa",
    "  arrancar del dispositivo equivocado.",
    "",
    "  Cuesta 1 diodo y 1 linea por rueda.",
]

for i, n in enumerate(col_izq):
    text(n, COL_A, NY0 + i * NDY, 1.7)
for i, n in enumerate(col_der):
    text(n, COL_B, NY0 + i * NDY, 1.7)

out.append('\t(sheet_instances (path "/" (page "1")))')
out.append(")")

with open("matriz-diodos.kicad_sch", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

print(f"generado: matriz-diodos.kicad_sch con {nd} diodos (esperados 33)")
