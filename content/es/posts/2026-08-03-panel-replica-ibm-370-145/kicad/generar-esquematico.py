#!/usr/bin/env python3
"""
Genera el esquemático de la unidad repetida del panel réplica del IBM 370/145.

Emite dos archivos KiCad 10:
  · os370-panel.kicad_sym        biblioteca de símbolos propia
  · unidad-repetida.kicad_sch    el esquemático

Se generan por programa y no a mano para poder iterar: el formato de KiCad son
S-expressions con coordenadas absolutas, y moverlas a mano es tedioso y frágil.

Pinouts, con su procedencia:
  · TPIC6B595 — hoja de datos de Texas Instruments SLIS032A (jul 1995, rev may 2005),
    paquete N/DW de 20 pines, vista superior.
  · 74HC165  — verificado contra la biblioteca 74xx.kicad_sym que distribuye KiCad.

Uso:
    uv run python generar-esquematico.py
    kicad-cli sch export svg --output . unidad-repetida.kicad_sch
"""

import uuid as _uuid

def U():
    return str(_uuid.uuid4())


GRID = 1.27


def g(v):
    """Ajusta a la grilla de conexión de 1,27 mm.

    KiCad marca endpoint_off_grid en cualquier extremo que no caiga en la grilla,
    y una vez que un origen queda fuera todo lo que cuelga de él hereda el error."""
    return round(round(v / GRID) * GRID, 4)

# ─────────────────────────────────────────────────────────────────────────────
# Pinouts
# ─────────────────────────────────────────────────────────────────────────────
# (número, nombre, tipo eléctrico, lado)   lado: L izquierda, R derecha
TPIC = [
    ("2",  "VCC",      "power_in",     "L"),
    ("3",  "SER_IN",   "input",        "L"),
    ("13", "SRCK",     "input",        "L"),
    ("12", "RCK",      "input",        "L"),
    ("8",  "~{SRCLR}", "input",        "L"),
    ("9",  "~{G}",     "input",        "L"),
    ("10", "GND",      "power_in",     "L"),
    ("4",  "DRAIN0",   "open_collector", "R"),
    ("5",  "DRAIN1",   "open_collector", "R"),
    ("6",  "DRAIN2",   "open_collector", "R"),
    ("7",  "DRAIN3",   "open_collector", "R"),
    ("14", "DRAIN4",   "open_collector", "R"),
    ("15", "DRAIN5",   "open_collector", "R"),
    ("16", "DRAIN6",   "open_collector", "R"),
    ("17", "DRAIN7",   "open_collector", "R"),
    ("18", "SER_OUT",  "output",       "R"),
]

HC165 = [
    ("16", "VCC",   "power_in", "L"),
    ("10", "DS",    "input",    "L"),
    ("2",  "CP",    "input",    "L"),
    ("15", "~{CE}", "input",    "L"),
    ("1",  "~{PL}", "input",    "L"),
    ("8",  "GND",   "power_in", "L"),
    ("11", "D0",    "input",    "R"),
    ("12", "D1",    "input",    "R"),
    ("13", "D2",    "input",    "R"),
    ("14", "D3",    "input",    "R"),
    ("3",  "D4",    "input",    "R"),
    ("4",  "D5",    "input",    "R"),
    ("5",  "D6",    "input",    "R"),
    ("6",  "D7",    "input",    "R"),
    ("9",  "Q7",    "output",   "R"),
]

FONT = "(effects (font (size 1.27 1.27)))"


def ic_symbol(lib, name, pins, w, datasheet, descr):
    """Símbolo rectangular con pines a ambos lados."""
    L = [p for p in pins if p[3] == "L"]
    R = [p for p in pins if p[3] == "R"]
    rows = max(len(L), len(R))
    h = (rows + 1) * 2.54
    hw, hh = w / 2, h / 2
    s = [f'\t\t(symbol "{lib}:{name}"',
         '\t\t\t(pin_names (offset 0.508))',
         '\t\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)',
         f'\t\t\t(property "Reference" "U" (at {-hw} {hh+1.5} 0) {FONT})',
         f'\t\t\t(property "Value" "{name}" (at {-hw} {-hh-2.5} 0) '
         f'(effects (font (size 1.27 1.27)) (justify left)))',
         f'\t\t\t(property "Footprint" "" (at 0 0 0) '
         f'(effects (font (size 1.27 1.27)) (hide yes)))',
         f'\t\t\t(property "Datasheet" "{datasheet}" (at 0 0 0) '
         f'(effects (font (size 1.27 1.27)) (hide yes)))',
         f'\t\t\t(property "Description" "{descr}" (at 0 0 0) '
         f'(effects (font (size 1.27 1.27)) (hide yes)))',
         f'\t\t\t(symbol "{name}_0_1"',
         f'\t\t\t\t(rectangle (start {-hw} {hh}) (end {hw} {-hh})',
         '\t\t\t\t\t(stroke (width 0.254) (type default))',
         '\t\t\t\t\t(fill (type background)))',
         '\t\t\t)',
         f'\t\t\t(symbol "{name}_1_1"']
    for i, (num, nm, typ, _) in enumerate(L):
        y = hh - 2.54 * (i + 1)
        s.append(f'\t\t\t\t(pin {typ} line (at {-hw-2.54} {y} 0) (length 2.54)'
                 f' (name "{nm}" {FONT}) (number "{num}" {FONT}))')
    for i, (num, nm, typ, _) in enumerate(R):
        y = hh - 2.54 * (i + 1)
        s.append(f'\t\t\t\t(pin {typ} line (at {hw+2.54} {y} 180) (length 2.54)'
                 f' (name "{nm}" {FONT}) (number "{num}" {FONT}))')
    s += ['\t\t\t)', '\t\t)']
    return "\n".join(s)


def passive_symbols(lib):
    """R, LED, llave y símbolos de alimentación — geometría mínima pero legible."""
    P = []
    # ── Resistencia: rectángulo vertical, pines arriba y abajo
    P.append(f'''\t\t(symbol "{lib}:R"
\t\t\t(pin_numbers (hide yes)) (pin_names (offset 0) (hide yes))
\t\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)
\t\t\t(property "Reference" "R" (at 2.54 0 90) {FONT})
\t\t\t(property "Value" "R" (at -2.54 0 90) {FONT})
\t\t\t(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
\t\t\t(symbol "R_0_1"
\t\t\t\t(rectangle (start -1.016 2.54) (end 1.016 -2.54)
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t)
\t\t\t(symbol "R_1_1"
\t\t\t\t(pin passive line (at 0 5.08 270) (length 2.54) (name "~" {FONT}) (number "1" {FONT}))
\t\t\t\t(pin passive line (at 0 -5.08 90) (length 2.54) (name "~" {FONT}) (number "2" {FONT}))
\t\t\t)
\t\t)''')
    # ── LED: triángulo + barra + dos flechas de emisión
    P.append(f'''\t\t(symbol "{lib}:LED"
\t\t\t(pin_numbers (hide yes)) (pin_names (offset 1.016) (hide yes))
\t\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)
\t\t\t(property "Reference" "D" (at 0 3.556 0) {FONT})
\t\t\t(property "Value" "LED" (at 0 -3.81 0) {FONT})
\t\t\t(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
\t\t\t(symbol "LED_0_1"
\t\t\t\t(polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27))
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t\t(polyline (pts (xy -1.27 0) (xy 1.27 0))
\t\t\t\t\t(stroke (width 0) (type default)) (fill (type none)))
\t\t\t\t(polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27) (xy -1.27 0) (xy 1.27 -1.27))
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t\t(polyline (pts (xy -1.27 -2.032) (xy -0.508 -3.048))
\t\t\t\t\t(stroke (width 0.152) (type default)) (fill (type none)))
\t\t\t\t(polyline (pts (xy 0.254 -2.032) (xy 1.016 -3.048))
\t\t\t\t\t(stroke (width 0.152) (type default)) (fill (type none)))
\t\t\t)
\t\t\t(symbol "LED_1_1"
\t\t\t\t(pin passive line (at -3.81 0 0) (length 2.54) (name "K" {FONT}) (number "1" {FONT}))
\t\t\t\t(pin passive line (at 3.81 0 180) (length 2.54) (name "A" {FONT}) (number "2" {FONT}))
\t\t\t)
\t\t)''')
    # ── Llave SPST
    P.append(f'''\t\t(symbol "{lib}:SW"
\t\t\t(pin_numbers (hide yes)) (pin_names (offset 0) (hide yes))
\t\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)
\t\t\t(property "Reference" "SW" (at 0 3.556 0) {FONT})
\t\t\t(property "Value" "SW" (at 0 -3.81 0) {FONT})
\t\t\t(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
\t\t\t(symbol "SW_0_1"
\t\t\t\t(circle (center -2.032 0) (radius 0.508)
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t\t(circle (center 2.032 0) (radius 0.508)
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t\t(polyline (pts (xy -1.524 0.254) (xy 1.778 1.778))
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t)
\t\t\t(symbol "SW_1_1"
\t\t\t\t(pin passive line (at -5.08 0 0) (length 2.54) (name "1" {FONT}) (number "1" {FONT}))
\t\t\t\t(pin passive line (at 5.08 0 180) (length 2.54) (name "2" {FONT}) (number "2" {FONT}))
\t\t\t)
\t\t)''')
    # ── +5V
    P.append(f'''\t\t(symbol "{lib}:+5V"
\t\t\t(power) (pin_numbers (hide yes)) (pin_names (offset 0) (hide yes))
\t\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)
\t\t\t(property "Reference" "#PWR" (at 0 -2.54 0) (effects (font (size 1.27 1.27)) (hide yes)))
\t\t\t(property "Value" "+5V" (at 0 3.556 0) {FONT})
\t\t\t(symbol "+5V_0_1"
\t\t\t\t(polyline (pts (xy -0.762 1.27) (xy 0 2.54) (xy 0.762 1.27))
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t\t(polyline (pts (xy 0 0) (xy 0 2.54))
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t)
\t\t\t(symbol "+5V_1_1"
\t\t\t\t(pin power_in line (at 0 0 90) (length 0) (name "+5V" {FONT}) (number "1" {FONT}))
\t\t\t)
\t\t)''')
    # ── GND
    P.append(f'''\t\t(symbol "{lib}:GND"
\t\t\t(power) (pin_numbers (hide yes)) (pin_names (offset 0) (hide yes))
\t\t\t(exclude_from_sim no) (in_bom yes) (on_board yes)
\t\t\t(property "Reference" "#PWR" (at 0 2.54 0) (effects (font (size 1.27 1.27)) (hide yes)))
\t\t\t(property "Value" "GND" (at 0 -3.81 0) {FONT})
\t\t\t(symbol "GND_0_1"
\t\t\t\t(polyline (pts (xy -1.905 -1.27) (xy 1.905 -1.27) (xy 0 -2.921) (xy -1.905 -1.27))
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t\t(polyline (pts (xy 0 0) (xy 0 -1.27))
\t\t\t\t\t(stroke (width 0.254) (type default)) (fill (type none)))
\t\t\t)
\t\t\t(symbol "GND_1_1"
\t\t\t\t(pin power_in line (at 0 0 270) (length 0) (name "GND" {FONT}) (number "1" {FONT}))
\t\t\t)
\t\t)''')
    return P


# ─────────────────────────────────────────────────────────────────────────────
LIB = "os370"
DS_TPIC = "https://www.ti.com/lit/ds/symlink/tpic6b595.pdf"
DS_165 = "https://assets.nexperia.com/documents/data-sheet/74HC_HCT165.pdf"

symbols = [
    ic_symbol(LIB, "TPIC6B595", TPIC, 25.4, DS_TPIC,
              "Registro de desplazamiento 8 bits con salidas DMOS open-drain 150 mA"),
    ic_symbol(LIB, "74HC165", HC165, 25.4, DS_165,
              "Registro de desplazamiento 8 bits, entrada paralelo / salida serie"),
] + passive_symbols(LIB)

with open("os370-panel.kicad_sym", "w", encoding="utf-8") as f:
    f.write("(kicad_symbol_lib\n\t(version 20241209)\n\t(generator \"os370\")\n"
            "\t(generator_version \"10.0\")\n")
    for s in symbols:
        f.write(s.replace("\n\t\t", "\n\t")[1:] + "\n")
    f.write(")\n")

# ─────────────────────────────────────────────────────────────────────────────
# Esquemático
# ─────────────────────────────────────────────────────────────────────────────
ROOT = U()
out = ["(kicad_sch", '\t(version 20250114)', '\t(generator "os370")',
       '\t(generator_version "10.0")', f'\t(uuid "{ROOT}")', '\t(paper "A3")',
       '\t(title_block',
       '\t\t(title "Panel réplica IBM System/370-145 — unidad repetida")',
       '\t\t(date "2026-08-02")', '\t\t(rev "A")',
       '\t\t(company "katra.ballardini.com.ar")',
       '\t\t(comment 1 "Etapa de salida: 1 de 26 TPIC6B595 — 8 LEDs")',
       '\t\t(comment 2 "Etapa de entrada: 1 de 16 74HC165 — 8 llaves")',
       '\t\t(comment 3 "El panel completo son 26 y 16 de estas etapas encadenadas")',
       '\t\t(comment 4 "Pinouts: TI SLIS032A y biblioteca 74xx de KiCad")',
       '\t)', '\t(lib_symbols']
for s in symbols:
    out.append(s)
out.append('\t)')

refs = {}


def place(lib_name, ref, val, x, y, mirror=None, hide_val=False, rot=0, lado=False,
          lbl_dx=0.0):
    """Coloca un símbolo.

    `lado=True` pone referencia y valor a los costados en vez de arriba y
    abajo: es lo que corresponde a un componente vertical, porque encima y
    debajo tiene sus propios cables.

    Las referencias de los símbolos de alimentación (#PWR…) NO se dibujan:
    son automáticas y sólo ensucian la hoja.
    """
    x, y = g(x), g(y)
    # KiCad suma la rotación del símbolo al ángulo del rótulo. Con el símbolo
    # acostado hay que restarla, o el texto sale escrito de costado.
    ang = (360 - rot) % 360
    n = refs.get(ref[0], 0) + 1
    refs[ref[0]] = n
    u = U()
    m = f'\t\t(mirror {mirror})\n' if mirror else ''
    vis = '(hide yes) ' if hide_val else ''
    oculto = '(hide yes) ' if ref.startswith('#') else ''
    if lib_name == "+5V":
        # El símbolo apunta hacia arriba: su rótulo va ARRIBA. Debajo está el
        # cable que baja al componente, y el texto ahí tapa la conexión.
        rx, ry_, vx, vy = x, y - 8.89, x + lbl_dx, y - 5.72
    elif lib_name == "GND":
        rx, ry_, vx, vy = x, y + 8.89, x, y + 5.72
    elif lado:
        rx, ry_, vx, vy = x + 5.72, y, x - 5.72, y
    else:
        rx, ry_, vx, vy = x, y - 4.45, x, y + 4.45
    out.append(f'''\t(symbol
\t\t(lib_id "{LIB}:{lib_name}")
\t\t(at {x} {y} {rot})
{m}\t\t(unit 1)
\t\t(exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
\t\t(uuid "{u}")
\t\t(property "Reference" "{ref}" (at {rx} {ry_} {ang}) (effects (font (size 1.0 1.0)) {oculto}))
\t\t(property "Value" "{val}" (at {vx} {vy} {ang}) (effects (font (size 1.0 1.0)) {vis}))
\t\t(instances (project "" (path "/{ROOT}" (reference "{ref}") (unit 1))))
\t)''')


def wire(x1, y1, x2, y2):
    x1, y1, x2, y2 = g(x1), g(y1), g(x2), g(y2)
    out.append(f'\t(wire (pts (xy {x1} {y1}) (xy {x2} {y2}))'
               f' (stroke (width 0) (type default)) (uuid "{U()}"))')


def label(txt, x, y, rot=0, justify="left bottom"):
    x, y = g(x), g(y)
    out.append(f'\t(label "{txt}" (at {x} {y} {rot})'
               f' (effects (font (size 1.27 1.27)) (justify {justify})) (uuid "{U()}"))')


def text(txt, x, y, size=2.0):
    out.append(f'\t(text "{txt}" (at {x} {y} 0)'
               f' (effects (font (size {size} {size})) (justify left)) (uuid "{U()}"))')


# ── Bloque 1: etapa de salida ────────────────────────────────────────────────
# ── Etapa de salida ─────────────────────────────────────────────────────────
# Los pines del integrado estan a 2,54 mm, pero un LED mide ~7,6 mm de alto y
# una resistencia ~10 mm.  Si se cuelga la cadena directamente del pin, cada
# componente se dibuja encima del siguiente.  Por eso las salidas se ABANICAN
# a un paso de 12,7 mm, con los tramos verticales escalonados en X para que
# tampoco se superpongan entre si.
PASO = 13.97
text("ETAPA DE SALIDA — 1 de 26.  Encadenar SER OUT -> SER IN del siguiente.", 20, 20, 2.5)

FILA0_OUT = 39.37
UX, UY = 55.88, g(FILA0_OUT + 3.5 * PASO)   # centrado sobre el abanico.
# g() es obligatorio: 3,5 x PASO cae en media grilla y desalinea todos los pines.
place("TPIC6B595", "U1", "TPIC6B595", UX, UY)

hw = 25.4 / 2
hh = (9 + 1) * 2.54 / 2
left_pins = [p for p in TPIC if p[3] == "L"]
right_pins = [p for p in TPIC if p[3] == "R"]

for i, (num, nm, _, _) in enumerate(left_pins):
    y = UY - (hh - 2.54 * (i + 1))
    x = UX - hw - 2.54
    wire(x, y, x - 7.62, y)
    nice = {"~{SRCLR}": "+5V", "~{G}": "GND"}.get(nm)
    label(nm.replace("~{", "").replace("}", "") if not nice else nice,
          x - 7.62, y, 180, "right bottom")

LEDX, RX = 116.84, 143.51
n_out = 0
for i, (num, nm, _, _) in enumerate(right_pins):
    y = UY - (hh - 2.54 * (i + 1))
    x = UX + hw + 2.54
    if nm == "SER_OUT":
        wire(x, y, x + 38.1, y)
        label("SER_IN_U2", x + 38.1, y, 0, "left bottom")
        continue
    fila = FILA0_OUT + n_out * PASO
    xv = x + 5.08 + n_out * 1.27          # tramo vertical escalonado
    wire(x, y, xv, y)
    wire(xv, y, xv, fila)
    wire(xv, fila, LEDX - 3.81, fila)
    place("LED", f"D{n_out+1}", "LED", LEDX, fila, hide_val=True)
    wire(LEDX + 3.81, fila, RX - 5.08, fila)
    place("R", f"R{n_out+1}", "330R", RX, fila, rot=90)
    wire(RX + 5.08, fila, RX + 11.43, fila)
    wire(RX + 11.43, fila, RX + 11.43, fila - 3.81)
    place("+5V", f"#PWR0{n_out+1}", "+5V", RX + 11.43, fila - 3.81)
    n_out += 1

text("R = 330 ohm (ambar Vf~2.0V) / 220 ohm (blanco calido Vf~3.0V) a 10 mA.", 20, 140, 1.8)
text("Medir el Vf del lote comprado.  G a GND: salidas siempre habilitadas —", 20, 145, 1.8)
text("el brillo es temporal (delta-sigma 1 kHz).", 20, 150, 1.8)

# ── Etapa de entrada ────────────────────────────────────────────────────────
text("ETAPA DE ENTRADA — 1 de 16.", 20, 158, 2.5)
# El titulo va en dos lineas: el pull-up de la primera fila sube hasta y~151
# y una linea larga a esta altura le queda cruzada por el cable.
text("Encadenar Q7 -> DS del siguiente.", 20, 164, 1.8)

FILA0_IN = 168.91
VX, VY = 55.88, g(FILA0_IN + 3.5 * PASO)
place("74HC165", "U2", "74HC165", VX, VY)

hh2 = (9 + 1) * 2.54 / 2
lp2 = [p for p in HC165 if p[3] == "L"]
rp2 = [p for p in HC165 if p[3] == "R"]

for i, (num, nm, _, _) in enumerate(lp2):
    y = VY - (hh2 - 2.54 * (i + 1))
    x = VX - hw - 2.54
    wire(x, y, x - 7.62, y)
    nice = {"~{CE}": "GND", "DS": "Q7_ANT"}.get(nm, nm.replace("~{", "").replace("}", ""))
    label(nice, x - 7.62, y, 180, "right bottom")

R1KX, NODOX, SWX2, GNDX = 116.84, 138.43, 229.87, 255.27
n_in = 0
for i, (num, nm, _, _) in enumerate(rp2):
    y = VY - (hh2 - 2.54 * (i + 1))
    x = VX + hw + 2.54
    if nm == "Q7":
        wire(x, y, x + 38.1, y)
        label("Q7_A_MISO", x + 38.1, y, 0, "left bottom")
        continue
    fila = FILA0_IN + n_in * PASO
    xv = x + 5.08 + n_in * 1.27
    wire(x, y, xv, y)
    wire(xv, y, xv, fila)
    wire(xv, fila, R1KX - 5.08, fila)
    place("R", f"R{20+n_in}", "1k", R1KX, fila, rot=90)
    wire(R1KX + 5.08, fila, NODOX, fila)
    # pull-up 10k hacia +5V
    # El pull-up mide 17,78 mm de alto y el paso de fila es 13,97: alineados en
    # una columna se pisan. Se escalonan en X, con paso suficiente para que el
    # rótulo +5V de una fila no caiga sobre la referencia de la fila de arriba.
    pux = g(NODOX + n_in * 8.89)
    wire(NODOX, fila, pux, fila)
    wire(pux, fila, pux, fila - 5.08)
    place("R", f"R{30+n_in}", "10k", pux, fila - 10.16, lado=True)
    wire(pux, fila - 15.24, pux, fila - 17.78)
    # El rótulo va corrido a la derecha: centrado cae sobre la referencia de la
    # resistencia de la columna anterior, a 3,17 mm fijos por el escalonado.
    place("+5V", f"#PWR1{n_in}", "+5V", pux, fila - 17.78, lbl_dx=5.08)
    # llave a masa
    wire(pux, fila, SWX2 - 5.08, fila)
    place("SW", f"SW{n_in+1}", "SW", SWX2, fila, hide_val=True)
    wire(SWX2 + 5.08, fila, GNDX, fila)
    place("GND", f"#PWR2{n_in}", "GND", GNDX, fila)
    n_in += 1

text("10k fija el estado en reposo; 1k en serie protege el mazo largo (ESD / falla de cableado).", 20, 278, 1.8)


text("CONEXION AL ARDUINO MEGA 2560", 288, 22, 2.5)
notas = [
    "D51 MOSI   -> SER_IN de U1 (primer TPIC6B595)",
    "D50 MISO   <- Q7 del primer 74HC165",
    "D52 SCK    -> SRCK de todos los TPIC  Y  CP de todos los HC165  (bus compartido)",
    "D53 SS     -> DEBE ser salida.  pinMode(53, OUTPUT) antes de SPI.begin()",
    "             Si queda como entrada y algo la baja, el SPI pasa a modo esclavo",
    "             en silencio y el panel se ensucia.",
    "D8  LATCH  -> RCK de todos los TPIC   (flanco de subida, DESPUES de la trama)",
    "D9  LOAD   -> ~PL de todos los HC165  (pulso bajo, ANTES de la trama)",
    "",
    "Atados fijos:   ~G -> GND      ~SRCLR -> +5V      ~CE -> GND",
    "                SER del ultimo HC165 -> GND",
    "",
    "ENLACE CON LA RASPBERRY PI 5 — opcion recomendada: UART directo, sin USB",
    "",
    "   Mega D18 (TX, 5V) --[1k8]--+-- Pi GPIO15 (RXD, 3.3V)",
    "                              |",
    "                            [3k3]     divisor 5V -> ~3.2V",
    "                              |",
    "                             GND",
    "",
    "   Mega D19 (RX) <---------- Pi GPIO14 (TXD)   directo: 3.3V supera el VIH del AVR",
    "",
    "ALIMENTACION",
    "   Fuente 5V >= 4A dedicada al panel.  LAMP TEST = 208 LEDs x 10 mA = 2.08 A.",
    "   NUNCA sacar la corriente de los LEDs del regulador del Arduino ni del USB de la Pi.",
    "   Masa comun unida en UN solo punto (estrella).",
    "   100 nF por cada integrado + 1000 uF de bulk por banco de LEDs.",
]
for i, n in enumerate(notas):
    text(n, 288, 32 + i * 5.5, 1.7)

out.append('\t(sheet_instances (path "/" (page "1")))')
out.append(")")

with open("unidad-repetida.kicad_sch", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

print("generado: os370-panel.kicad_sym  y  unidad-repetida.kicad_sch")
