# Arduino LED and Switch Wiring Plan — IBM 370/145 Replica Panel

**Design document · 2026-08-02 · os370 panel replica project**

Electrical and firmware plan for the Arduino that drives the acrylic panel's lamps and reads its
buttons, toggles and rotary switches, connected over USB-C to a Raspberry Pi running Hercules with
MVS 3.8j Turnkey.

**Companion documents**
- [`2026-08-01-370-145-panel-inventory.md`](2026-08-01-370-145-panel-inventory.md) — what every
  lamp and switch *is*, and which are drivable. **Read that first; this document implements it.**
- [`2026-08-01-references.md`](2026-08-01-references.md) §9 — electronics prior art;
  §20 — why the 370/145 was chosen.

> ⚠️ **Dimensioned against provisional lamp counts.** The check-indicator banks have not yet been
> counted off the manual scan (inventory doc, [open question 1](2026-08-01-370-145-panel-inventory.md#8-open-questions)).
> Allocation is in **whole 8-bit registers with deliberate spare capacity**, so a recount changes
> only the bit-allocation tables — never the architecture or the parts list.

---

## 1. Design targets

| Target | Value | Rationale |
| --- | --- | --- |
| **LED outputs** | **208** (26 × 8) | ~160–190 estimated lamps + headroom |
| **Switch inputs** | **128** (16 × 8) | ~90 estimated inputs + headroom |
| **Refresh rate** | **1000 Hz, continuous** | Density modulation — see §2 |
| **Brightness levels** | **256 targets, floor at 16** | Below 16/255 the delta-sigma pulse rate drops under 62 Hz and flickers — see §2.2 |
| **End-to-end latency** | **≤ 10 ms** | Operation Blinkenlights measured ~1 s on a USB I/O board (unusable) vs **~1 ms** on an Arduino — references §5.1 |
| **Local autonomy** | LAMP TEST, TEST lamp, debounce | Must work with the Pi disconnected — §7 |

---

## 2. The refresh model: 1 kHz delta-sigma density modulation

### 2.1 Why this is the *correct* model, not a workaround

The 3145 used **incandescent** lamps. A filament has thermal mass, so when a displayed bit toggles
millions of times per second the lamp does not blink — it **glows at a brightness proportional to
the fraction of time that bit was 1**. That averaging is what produced the characteristic
blinkenlights shimmer.

Density-modulating an LED at 1 kHz, with the duty cycle set to the measured proportion of ones,
**reproduces that physics** rather than approximating it. This is a fidelity gain over the
static on/off drive originally considered, not a compromise.

It also falls out of the data situation for free. The Pi cannot send per-instruction state
(§8.2), so it must aggregate — and the natural aggregate *is* the per-bit duty cycle.

### 2.2 Use first-order delta-sigma, not fixed-window PWM

Per lamp, per frame:

```c
acc[i] += target[i];            // target 0..255
bool on = (acc[i] >= 256);
if (on) acc[i] -= 256;
```

Delta-sigma distributes the on-frames **evenly**. A lamp at 50 % alternates every frame — a 500 Hz
square wave, invisible. Naive fixed-window PWM would light it for 128 consecutive frames then dark
for 128, i.e. a visible 3.9 Hz blink at the same duty cycle.

**The low-end limit is real and must be respected.** With target `T`, the accumulator overflows
every `256/T` frames, so the pulse rate is:

```
f_pulse = 1000 × T / 256  Hz
```

| Target `T` | Duty | Pulse rate | Verdict |
| --- | --- | --- | --- |
| 255 | 100 % | steady | ✅ |
| 128 | 50 % | 500 Hz | ✅ |
| 32 | 12.5 % | 125 Hz | ✅ |
| **16** | **6.3 %** | **62.5 Hz** | ✅ **floor — use this** |
| 8 | 3.1 % | 31 Hz | ❌ visible flicker |
| 4 | 1.6 % | 15.6 Hz | ❌ obvious flicker |

**Rule: clamp any target below 16 to 0.** This is also physically accurate — a filament at 6 %
duty is visually dark, so the real machine had the same floor.

If finer low-end control is ever wanted, **raise the frame rate rather than adding bits**: at
2 kHz, `T = 8` gives 62.5 Hz.

### 2.3 Consequences

- **No global `OE` PWM.** Brightness is controlled by scaling targets in software. If a hardware
  dimmer is added later, run it at **≥ 20 kHz** so it does not beat against the 1 kHz frame rate.
- **No per-channel PWM hardware needed.** Plain shift registers suffice; the modulation is
  temporal and lives in firmware.
- **The frame must be isochronous.** Drive it from a hardware timer ISR, never from `loop()` —
  USB servicing jitter would modulate brightness. See §6.3.

---

## 3. Architecture

```
   Raspberry Pi 5                     Arduino Mega 2560               Panel
  ┌──────────────────┐              ┌───────────────────────┐
  │ Hercules + MVS   │              │ 1 kHz timer ISR:      │
  │ 3.8j TK5         │   USB-C      │  · delta-sigma × 208  │  SPI    ┌──────────────────┐
  │                  │◄────────────►│  · SPI frame          │────────►│ 26 × TPIC6B595   │──► 208 LEDs
  │ HDL sampling mod │  CDC, binary │  · switch capture     │  MOSI   │ open-drain sinks │
  │ + panel daemon   │  ~11 KB/s    │                       │         └──────────────────┘
  │ (duty-cycle agg) │              │  local: LAMP TEST,    │  SPI    ┌──────────────────┐
  └──────────────────┘              │  TEST lamp, debounce  │◄────────│ 16 × 74HC165     │◄── 128 switch lines
                                    └───────────────────────┘  MISO   └──────────────────┘
```

**Division of responsibility.** The Arduino owns the 1 kHz modulation, switch scanning, debounce,
and the behaviours that must survive a dead link (§7). *All* semantics — what a switch combination
means, which Hercules command to issue, how to compute a duty cycle — live on the Pi. This is the
split Operation Blinkenlights arrived at after abandoning its first architecture.

---

## 4. Output chain — LEDs

### 4.1 Driver: TPIC6B595

8-bit shift register with **open-drain DMOS power outputs** — replaces a 74HC595 + ULN2803 pair
with one part.

| Parameter | Value | Relevance |
| --- | --- | --- |
| Outputs | 8, open-drain, low-side | Sinks LED cathodes directly |
| Continuous current | 150 mA/channel | We need 10–15 mA. Vast margin |
| Package total | ~500 mA | 8 × 15 mA = 120 mA ✅ |
| Chaining | `SER OUT` → next `SER IN` | One SPI bus for all 26 |
| `G` (output enable) | Active low | Tie **low** (permanently enabled); brightness is temporal |
| `SRCLR` | Active low | Tie to **+5 V** |

**Rejected alternatives:** MAX7219 (internally multiplexed — beats against our 1 kHz frame and
forces an 8×8 matrix layout); TLC5940 (its per-channel PWM is redundant once delta-sigma is in
firmware); WS2812 (wrong colour rendition behind period legend caps, and its hard-timed one-wire
protocol fights USB servicing).

### 4.2 LED wiring

Open-drain sinks ⇒ **anodes to +5 V through a resistor, cathodes to the driver**:

```
        +5V  (dedicated panel rail — NOT the Pi's USB rail)
          │
         ┌┴┐
         │ │  R
         └┬┘
          │
         ─┴─   LED — diffused warm-white or amber
          ▽
          │
     ┌────┴──────────────┐
     │ TPIC6B595  DRAINn │
     └────┬──────────────┘
         GND
```

| LED type | Vf | R for 10 mA | Use |
| --- | --- | --- | --- |
| Amber | ~2.0 V | (5.0−2.0)/0.010 = 300 Ω → **330 Ω** | Closest to incandescent-behind-amber-cap |
| Warm white | ~3.0 V | (5.0−3.0)/0.010 = 200 Ω → **220 Ω** | Behind coloured legend caps |

**Choose the LED first, then the resistor. Buy one reel of one part number** — mixed bins give
visibly uneven brightness across a 200-lamp panel, and delta-sigma will not hide it.

**Use diffused, never water-clear.** Clear LEDs have a narrow beam and put a hot spot behind the
legend cap instead of lighting it evenly. Operation Blinkenlights used orange LEDs in modified
plastic casings for exactly this reason.

### 4.3 Bit allocation (208 outputs)

`U1` is nearest the MCU. **Chains fill back-to-front: transmit U26 first** — see §8.3.

**✅ Counted from the scan 2026-08-02** — see [inventory §3.0](2026-08-01-370-145-panel-inventory.md#30--verified-lamp-census--counted-from-the-scan-2026-08-02).
Allocation below is now based on **verified counts**, not estimates.

| Chip | Bits | Panel group | Positions | Lit | Spare |
| --- | --- | --- | --- | --- | --- |
| U1 | 0–7 | **System Indicators** — SYS, MAN, WAIT, TEST(A), LOAD | **5** | 5 | 3 |
| U2–U4 | 8–31 | **CPU Status** — 18-position row, 16 labelled, 2 amber | **18** | 16 | 6 |
| U5–U9 | 32–71 | **System Checks** — 2 rows × 18, 19 labelled, **all red** | **36** | 19 | 4 |
| U10–U12 | 72–95 | **Console File** — 18-position row: 6 red checks, CNTR MATCH, then Register `P(A) + 0–7` | **18** | 16 | 6 |
| U13–U17 | 96–135 | **Display Assembler Out** roller — 4 bytes × `P 0 1 2 3 │ 4 5 6 7` | **36** | 36 | 4 |
| U18–U22 | 136–175 | **A-Register Display** roller — identical structure | **36** | 36 | 4 |
| U23–U24 | 176–191 | **Backlit keys** | ~15 ❓ | ~15 | ~1 |
| U25–U26 | 192–207 | **Expansion** | 0 | 0 | 16 |
| | | **Total** | **≈ 164** | **≈ 143** | |

### 4.3a Lens colours — buy three, not one

IBM colour-codes the lenses, and the scan shows the code explicitly (`R` / `A` / unmarked):

| Colour | Count | Where |
| --- | --- | --- |
| **Red** | **19** | Every System Check indicator, and the 6 Console File check indicators — 25 red positions in total |
| **Amber** | **11** | TEST · TOD CLOCK INVLD · IMPL REQD · Console File Register `P` · **all 8 roller parity lamps** |
| **White** | **~110** | Everything else — the roller data bits, CPU Status, System Indicators |

This supersedes the single-reel advice in §4.2: **buy one reel per colour**, keep each reel
internally uniform, and match forward voltages within a colour so one resistor value serves each.

### 4.4 Roller lamp count and parity — resolved by visual count

> ⚠️ **This section previously stated the opposite and was wrong.** It claimed the roller banks
> had **no parity lamps** and were 32 lamps each, inferred from the PDF *text layer* (whose roller
> content tables list only `Byte 0…Byte 3`). Rendering the page at 430 dpi and looking at the
> **panel artwork** shows otherwise. **The text layer is not authoritative for artwork; the image
> is.** Corrected below.

**Each roller bank is 4 bytes of `P 0 1 2 3 │ 4 5 6 7` = 9 lamps per byte = 36 lamps per bank.
Two rollers = 72 lamps.** The `P` lamp of each byte is **amber**; the eight data lamps are white.
The vertical bar between bits 3 and 4 is a nibble separator, not a lamp.

Parity is therefore displayed in **three** places on this panel:

| Location | Parity lamps | Colour |
| --- | --- | --- |
| Display Assembler Out roller | 4 (one per byte) | Amber |
| A-Register Display roller | 4 (one per byte) | Amber |
| Console File Register | 1 | Amber |
| **Total** | **9** | |

Separately, `M-REG PARITY` and `M-REG COMP` appear as **red fault lamps** in the System Checks
bank, with a `PARITY CHECK` bracket spanning five positions. Those are error indicators, not live
data — and per §7.4 they must never be faked.

### 4.5 Does Hercules provide parity? No — but you can compute it honestly

**Hercules has no parity information, and cannot have any.** Parity is a *hardware storage
integrity* mechanism: real machines carried a check bit alongside each byte so a failing memory
chip or data path could be detected. Hercules keeps guest storage in ordinary host RAM. There is
no check bit, because there is no failing hardware to catch. **Parity is not architected** —
Principles of Operation does not define parity bits as program-visible state, which is exactly why
it is absent.

**But if you ever do fit parity lamps, they are legitimately drivable.** On a healthy machine the
stored parity bit *is by definition* the parity of the data — that is the entire point of the
mechanism. So:

```c
parity_lamp = odd_parity(displayed_byte);   // XOR of the 8 bits, inverted for odd parity
```

reproduces exactly what a non-faulty 3145 displayed. The **only** thing you cannot reproduce is a
parity *error*, which is the fault case — and per §7.4 you must never fake that anyway.

⚠️ IBM generally used **odd** parity; confirm the 3145's convention in the FE manual before
committing a legend.

**Storage protect key.** Display Assembler Out position 1, **byte 0 = 8 lamps** = bits 88–95.
The S/370 storage key is 7 bits (4-bit access-control key + fetch-protect + reference + change),
so 7 of those 8 carry real data. **Storage keys are architected** (`SSK`/`ISK` in Principles of
Operation) **and Hercules models them** — it must, or MVS would not boot. **Fully drivable.**

> Banks **U5–U11** (~50 lamps) are the ones that **cannot** be honestly driven — system checks and
> console file (inventory §7.2). They are wired identically to every other bank; the *policy*
> about what they display lives in firmware (§7.4).

---

## 5. Input chain — switches

### 5.1 Driver: 74HC165

Parallel-in / serial-out, chained on the same SPI clock as the output chain. **No internal
pull-ups** — every input needs an external one.

```
        +5V
         │
        ┌┴┐
        │ │ 10 kΩ pull-up
        └┬┘
         │
         ├────[ 1 kΩ ]────► 74HC165 input
         │
         ○  switch contact
         │
        GND
```

The 10 kΩ sets the idle state; the 1 kΩ series resistor protects against a wiring fault or ESD on
a long panel harness — mirroring the PiDP-11's 1 kΩ switch-sense limiting (references §9).

*Alternative:* MCP23017 (I²C, internal pull-ups, interrupt-on-change) — half the chip count, but
adds a second bus and is slower to scan. Prefer 74HC165 for one-bus uniformity.

### 5.2 Rotary switch encoding — two kinds, handled differently

#### Wheels A–H — the eight hex data/address wheels

**16-position hex-coded rotary switches** (BCD/hex output). **4 bits each → 32 lines.**

> Not 1-of-16 wafer switches — that would cost 128 lines for the wheels alone.
> Not quadrature encoders — they have no absolute position, so the panel would lose its setting at
> power-up, which the real machine never did.

⚠️ These switches usually output **complemented** (active-low) code. Verify against the datasheet
and invert in firmware — getting it backwards gives a wheel that reads `F` when it shows `0`.

#### Sourcing and cost — checked 2026-08-02

> ⚠️ **Prices and stock change constantly. Verify before ordering.** Figures below are what the
> distributors showed on 2026-08-02.
>
> *Link note: DigiKey and Newark return **403 to scripted requests** but load normally in a
> browser — see [references §19.3](2026-08-01-references.md#193-alive-but-bot-blocked--these-work-fine-in-a-browser).
> Do not read those 403s as dead links.*

**Option A — hex-coded rotary DIP switches (4 lines each, simplest firmware)**

| Part | Type | Price | Stock | Notes |
| --- | --- | --- | --- | --- |
| [Grayhill **94HBB16WT**](https://www.digikey.com/en/products/detail/grayhill-inc/94HBB16WT/1641991) (DigiKey GH7365-ND) | SMD gull-wing, **shaft actuator**, hex | **$6.63** @1 · $5.51 @10 · $5.07 @25 · **$4.53** @100 | ❌ **Out of stock, 12-week lead** | Gold contacts, 100 mA @ 50 VDC, 0.225″ above board, **10 000 mechanical cycles** |
| [Grayhill **94HAB16WT**](https://www.digikey.com/en/products/detail/grayhill-inc/94HAB16WT/726314) | SMD, **tool** actuator | ~**$4.15** @1 | ✅ ~5 693 in stock | Screwdriver-slot, not hand-turnable without a knob |
| [**CTS 221AMC16R**](https://www.digikey.com/en/product-highlight/c/cts-electrocomponents/221-series-rotary-dip-switch) | 10 × 10 mm, SMD or through-hole | ~**$1.74** @1000 | ✅ In stock — DigiKey lists it as a **direct substitute** for the 94HBB16WT | Best value of the coded parts |
| [Nidec **SD-1110**](https://www.digikey.com/en/products/detail/nidec-components/SD-1110/948376) | **Through-hole**, rotary with **shaft actuator**, hex | — | ✅ | **Through-hole + shaft is the friendliest of these for a panel build** |
| [NKK **FR02FR16P-R**](https://www.digikey.com/en/products/detail/nkk-switches/FR02FR16P-R/1165797) | SMD, tool actuator | — | ✅ | Alternative second source |

**8 wheels ≈ US$15–55** depending on part and quantity break.

**⚠️ Two honest caveats about Option A.** These are **board-adjustment** switches, not operator
controls. (1) **10 000 mechanical cycles** is a setup-adjustment rating — fine for a hobby panel,
but it is not a control designed to be dialled daily for years. (2) They are **~10 × 10 mm**,
whereas the real /145 wheels are large hand-turned knobs (see the scan). You will need a knob or
shaft extension and a careful panel-to-PCB alignment.

**Option B — panel-mount 1-of-16 rotary switch + diode encoding**

A proper hand-operated panel rotary switch, with **16 diodes per wheel** wiring the detents down to
4 binary lines. Keeps the 4-lines-per-wheel budget *and* gives an authentic feel and cycle life.

| Item | Qty | Approx. cost |
| --- | --- | --- |
| 16-position panel-mount rotary switch — [Mouser](https://www.mouser.com/c/electromechanical/switches/rotary-switches/?number+of+positions=16+Position) · [Newark](https://www.newark.com/c/switches-relays/switches/rotary-switches/rotary-switches?no-of-switch-positions=16-position) · [AliExpress](https://www.aliexpress.com/w/wholesale-16-position-rotary-switch.html) | 8 | ~$3 each (AliExpress) to ~$15–30 each (Mouser/Newark industrial) |
| 1N4148 diodes | 128 | ~$3 total |

**8 wheels ≈ US$27 (budget) to US$240 (industrial).**

**Recommendation: prototype with Option A** — buy **one** CTS 221AMC16R or Nidec SD-1110, confirm
the output polarity and that it reads cleanly through the 74HC165 chain, *then* decide. If the
finished panel is meant to be operated rather than displayed, go to **Option B** below for the
mechanical feel and cycle life.

#### Option B in detail — 1-of-16 panel switch + diode encoder

A proper hand-operated panel rotary switch has 16 individual position terminals. Wiring all 16 to
the input chain would cost **128 lines for the eight wheels alone** — the entire 74HC165 budget.
A **diode matrix** encodes each wheel down to 4 binary lines plus 1 validity line.

##### Circuit — one wheel

```
                                   +5 V
                                     │
        ┌────────────┬────────────┬──┴─────────┬────────────┬────────────┐
       ┌┴┐          ┌┴┐          ┌┴┐          ┌┴┐          ┌┴┐
       │ │10k       │ │10k       │ │10k       │ │10k       │ │10k
       └┬┘          └┬┘          └┬┘          └┬┘          └┬┘
        │            │            │            │            │
   b3 ──●──[1k]──►   │            │            │            │   ─► to 74HC165
   b2 ───────────────●──[1k]──►   │            │            │
   b1 ────────────────────────────●──[1k]──►   │            │
   b0 ─────────────────────────────────────────●──[1k]──►   │
  POS0 ──────────────────────────────────────────────────────●──[1k]──►
        │            │            │            │            │
        │  diode matrix: anode on the bit line, cathode to the switch terminal
        │            │            │            │            │
        └──▶|──┐     └──▶|──┐     └──▶|──┐     └──▶|──┐     └──▶|──┐
               │            │            │            │            │
            ┌──┴────────────┴────────────┴────────────┴────────────┴──┐
            │        1-of-16 rotary switch — position terminals        │
            │                                                          │
            │              pole (common) ──────────────────────► GND   │
            └──────────────────────────────────────────────────────────┘
```

When a position is selected, its terminal is grounded through the pole. Every diode hanging off
that terminal conducts, pulling its bit line down to ~0.7 V — comfortably below the 74HC `V_IL`
threshold of 1.5 V at 5 V. Unselected terminals float, so their diodes stay reverse-biased.

**The encoding is therefore active-low: a diode present ⇒ that bit reads 0 ⇒ invert in firmware.**
This matches the complemented output of the commercial coded switches in Option A, so **the
firmware is identical for both options.**

##### Diode matrix — which positions get diodes

`▷` = diode fitted from that bit line to that position terminal.

| Pos | Hex | b3 | b2 | b1 | b0 | POS0 | Diodes |
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: |
| 0 | `0` | · | · | · | · | **▷** | 1 |
| 1 | `1` | · | · | · | ▷ | · | 1 |
| 2 | `2` | · | · | ▷ | · | · | 1 |
| 3 | `3` | · | · | ▷ | ▷ | · | 2 |
| 4 | `4` | · | ▷ | · | · | · | 1 |
| 5 | `5` | · | ▷ | · | ▷ | · | 2 |
| 6 | `6` | · | ▷ | ▷ | · | · | 2 |
| 7 | `7` | · | ▷ | ▷ | ▷ | · | 3 |
| 8 | `8` | ▷ | · | · | · | · | 1 |
| 9 | `9` | ▷ | · | · | ▷ | · | 2 |
| 10 | `A` | ▷ | · | ▷ | · | · | 2 |
| 11 | `B` | ▷ | · | ▷ | ▷ | · | 3 |
| 12 | `C` | ▷ | ▷ | · | · | · | 2 |
| 13 | `D` | ▷ | ▷ | · | ▷ | · | 3 |
| 14 | `E` | ▷ | ▷ | ▷ | · | · | 3 |
| 15 | `F` | ▷ | ▷ | ▷ | ▷ | · | 4 |
| | **Total** | 8 | 8 | 8 | 8 | 1 | **33** |

**33 diodes per wheel × 8 wheels = 264 diodes.**

##### Why the POS0 line is not optional

Rotary switches are **break-before-make**: while you turn between detents, *no* terminal is
connected and every bit line floats high. That reads as `0000` — **indistinguishable from a genuine
position 0.** A wheel left slightly off-detent would silently report zero, and on the LOAD UNIT
wheels that means IPLing from the wrong device.

One diode from position 0 to a dedicated `POS0` line fixes it completely:

| Bit lines | POS0 | Meaning |
| --- | --- | --- |
| any bit low | high | positions 1–F — read the code |
| all high | **low** | **genuine position 0** |
| all high | high | **between detents — invalid, hold the last value** |

Cost: **1 diode and 1 input line per wheel.** A full `VALID` line (a diode from *every* position)
would also work but costs 16 diodes per wheel for no extra information — position 0 is the only
ambiguous code.

##### Firmware decode

```c
// raw bits, active low, as read from the 74HC165 chain
#define VAL_POS0  0x10          // bit 4 = POS0 line

uint8_t readWheel(uint8_t w) {
    uint8_t raw   = wheelBits[w];
    bool    isZero = !(raw & VAL_POS0);      // POS0 low  => genuine 0
    uint8_t v      = (~raw) & 0x0F;          // invert: diode fitted => bit set

    if (v == 0 && !isZero)
        return lastValid[w];                 // between detents — hold
    lastValid[w] = v;
    return v;
}
```

##### Parts, cost and budget impact

| Item | Qty | Note |
| --- | --- | --- |
| 16-position **non-shorting** panel rotary switch, 1 pole | 8 | Break-before-make. Confirm it is **1 pole × 16 positions**, not the common 4-pole × 3-position type |
| 1N4148 diode | **264** | ~$0.01–0.03 each ⇒ **≈$3–8 total** |
| 10 kΩ pull-up | 40 | 5 per wheel |
| 1 kΩ series | 40 | 5 per wheel |

**Input line budget: 5 lines × 8 wheels = 40** (up from 32). Revised total:

| Group | Lines |
| --- | --- |
| Wheels A–H (Option B, with POS0) | **40** |
| Mode rotaries, 1-of-N | 33 |
| Keys | 15 |
| Toggles | ~7 |
| Meter key switch, EPO | ~2 |
| **Total** | **≈ 97 of 128** — 31 spare ✅ |

Still fits the 16-chip 74HC165 chain. **No change to the architecture.**

##### Build note

264 hand-soldered diodes is tedious but trivial work, and it is the kind of thing that belongs on
the **wheel PCB** rather than flying leads — lay out the matrix as a regular 16 × 5 grid on the
board behind each wheel and it becomes 33 identical placements. Use **through-hole 1N4148** rather
than SMD; the assembly is far more forgiving and the parts cost is the same.

**What the wheels are for** (inventory §5.7). Same eight wheels, different meaning per operation:

| Wheels | Function | Firmware action |
| --- | --- | --- |
| **F, G, H** | **LOAD UNIT ADDRESS** — the IPL device | → `ipl <cuu>` (TK5 SYSRES is conventionally `148`) |
| **F, G, H** | **MAIN STORAGE ADDRESS** — store/display *and* address-compare | → storage display/alter, or breakpoint address |
| **A, B** | **DATA** — byte value for a manual store | → `store` operand |
| **H** | **WORD ADDRESS** — which register to display (`00` = GPR 1, `01` = GPR 2 …) | → `gpr` / `fpr` index |
| C, D | CF ADDRESS (service) | ignore |
| E–H | BYTE COUNT (service) | ignore |
| F, G, H | CONTROL STORAGE ADDRESS (service) | ignore |

#### Mode rotaries — 1-of-N, read directly

Irregular position counts and *named* positions, so one input line per position.

| Switch | What it selects | Positions | Lines | Feeds TEST? |
| --- | --- | --- | --- | --- |
| **RATE** | How the CPU runs: PROCESS / INSTRUCTION STEP (+ SINGLE CYCLE, HARD STOP service) | 4 | 4 | ✅ |
| **CHECK CONTROL** | Machine-check behaviour: PROCESS / STOP AFTER LOG (+ DISABLE, HARD STOP) | 4 | 4 | ✅ |
| **DIAGNOSTIC / CONSOLE FILE CONTROL** | Console-file & diagnostic modes: PROCESS/IMPL + service | ~8 ❓ | 8 | ✅ |
| **ADDRESS COMPARE** | *What kind* of access triggers a match: ANY(real) / DATA STORE / I/O / I-COUNTER / DATA COMPARE TRAP / ANY(logical) + service | ~12 ❓ | 12 | ❌ |
| **STORAGE SELECT** | Store/display target: MAIN STORAGE / LOCAL STORAGE (GPR+FPR) + service | ~8 ❓ | 8 | ❌ |
| | | | **~36** | |

**Three of the five feed the TEST lamp.** The fourth TEST input is not a rotary at all — it is the
**ADDRESS COMPARE CONTROL toggle** (SYNC/NORM · STOP · IMMED STOP). See §7.2.

1-of-N costs lines but is unambiguous, needs no decode table, and **detects a switch between
detents** (no line active = invalid). For a mode switch that gates CPU behaviour, that matters.

### 5.3 Bit allocation (128 inputs)

**✅ Counted from the scan 2026-08-02** — see [inventory §5.0](2026-08-01-370-145-panel-inventory.md#50--verified-switch-and-key-census--counted-from-the-scan-2026-08-02).

| Chip | Bits | Group | Lines |
| --- | --- | --- | --- |
| S1–S4 | 0–31 | **Rotary wheels A–H** — 4 bits each, hex-coded | **32** |
| S5–S9 | 32–71 | **Mode rotaries, 1-of-N** — ADDRESS COMPARE **9** · STORAGE SELECT **9** · RATE **3** · CHECK CONTROL **5** · DIAG/CF CONTROL **7** | **33** |
| S10 | 72–79 | **Toggles** — LAMP TEST, INTERVAL TIMER, TOD CLOCK, ADDRESS COMPARE CONTROL (3-pos ⇒ 2 lines), CF REG DISPLAY | ~7 ❓ |
| S11–S12 | 80–95 | **Keys** — 15 labelled (18 positions, 3 blank caps wired to nothing) | **15** |
| S13 | 96–103 | Use-meter key switch, EPO sense, spare | ~2 |
| S14–S16 | 104–127 | **Expansion** | 0 |
| | | **Total** | **≈ 89** (39 spare) |

**RATE has only 3 detents**, not 4 — `SINGLE CYCLE HARD STOP` is one position with a two-line
legend. That matches the manual's "the remaining position" (singular) and saves a line.

---

## 6. Microcontroller

### 6.1 Board: Arduino Mega 2560 — the build target

**Chosen because the UNO R4 Minima is not available in Argentina** (§11) while the Mega is
(29 210 ARS observed). It is also the board Operation Blinkenlights settled on after its USB I/O
board proved a thousand times too slow (references §5.1).

| Spec | Value | Why it matters here |
| --- | --- | --- |
| MCU | ATmega2560, 8-bit AVR | Mature, forgiving, universally documented |
| Clock | **16 MHz** | Delta-sigma costs ~13 % CPU — see [§6.4](#64-timing-budget) |
| **Operating voltage** | **5 V** | ✅ **No level shifters** — drives 74HC/TPIC directly |
| USB | **USB-B via an ATmega16U2 bridge** | ⚠️ **Not native.** Baud rate is a real bottleneck — [§6.5](#65-the-host-link-on-a-mega--baud-rate-is-real) |
| SRAM | 8 KB | 208 targets + 208 accumulators + buffers ≈ 900 B. Ample |
| Digital I/O | **54** (+16 analog) | We need **6**. Enormous room for expansion |
| Hardware UARTs | **4** | Enables the direct-to-Pi-GPIO option in [§6.6](#66-better-option-skip-usb-entirely) |

The 5 V logic level is the decisive advantage over a Teensy 4.1 (3.3 V, would need level shifters
on MOSI/SCK/latch/load — exactly what Operation Blinkenlights needed SparkFun converters for).
The **UNO R4 Minima remains a drop-in upgrade** if you can obtain one — see
[§6.7](#67-upgrading-to-a-uno-r4-minima-later).

### 6.2 Pin assignment — Arduino Mega 2560

| Signal | Pin | Dir | Notes |
| --- | --- | --- | --- |
| `SPI_MOSI` | **D51** | out | → U1 `SER IN` |
| `SPI_MISO` | **D50** | in | ← S1 `QH` |
| `SPI_SCK` | **D52** | out | → all `SRCK` **and** all `CLK` — shared by both chains |
| `SPI_SS` | **D53** | **out** | ⚠️ **Must be an output.** See the warning below |
| `LED_LATCH` (RCK) | **D8** | out | Rising edge latches shifted data to outputs |
| `SW_LOAD` (SH/LD) | **D9** | out | Low pulse captures all switch lines |
| `LINK_LED` | **D7** | out | Host-link health |
| `LED_G` | — | — | Tie **GND** (outputs always enabled; brightness is temporal, §2.3) |
| `LED_SRCLR` | — | — | Tie **+5 V** |
| `SW_CLKINH` | — | — | Tie **GND** |
| Last 74HC165 `SER` | — | — | Tie **GND** — surplus clocks shift in zeros, not noise (§6.3) |
| Host link | **USB-B** (`Serial`) | — | Via the 16U2 bridge — **set 500 000 baud**, §6.5 |
| *Host link, alternative* | **D18 TX / D19 RX** (`Serial1`) | — | Direct to the Pi's GPIO UART, §6.6 |

> ⚠️ **`SS` (D53) must be configured as an output**, even though nothing is connected to it.
> On AVR, if `SS` is left as an input and an external signal pulls it low, the SPI hardware
> silently switches to **slave mode** mid-transfer and the panel garbles. Put
> `pinMode(53, OUTPUT);` before `SPI.begin();` and never remove it. This trap does not exist on
> the R4.

**Pins used: 6 of 54.** The shift-register architecture means pin count is irrelevant — the spare
48 are available for hour meters, an EPO relay, a status display, or a second panel.

### 6.3 The 1 kHz frame — timer ISR

Run from **Timer1 in CTC mode**, never from `loop()`. Host-servicing jitter would otherwise
modulate the frame period and therefore the brightness.

```c
// Timer1 CTC @ 1000 Hz:  16 MHz / 8 prescaler / 2000 = 1000 Hz
TCCR1A = 0;
TCCR1B = _BV(WGM12) | _BV(CS11);   // CTC, prescaler 8
OCR1A  = 1999;                     // 2000 ticks = 1.000 ms exactly
TIMSK1 = _BV(OCIE1A);
```

```
ISR(TIMER1_COMPA_vect, ISR_NOBLOCK):        // ← NOBLOCK is mandatory, see §6.5
  1. SW_LOAD low → 1 µs → high              // 74HC165 captures switch state
  2. for i in 0..25:
        in[i] = SPI.transfer(frontBuffer[i]) // full duplex: lamps out, switches in
  3. LED_LATCH high → 1 µs → low             // TPIC6B595 outputs update atomically
  4. swap frontBuffer / backBuffer if the main loop has marked one ready
  5. if (frame % 5 == 0) flag switch data for main-loop processing   // 200 Hz debounce
```

**Delta-sigma runs in the main loop, not the ISR.** It fills `backBuffer` and sets a ready flag;
the ISR only shifts, latches and swaps. On a 16 MHz AVR this split is **not optional** — see
[§6.5](#65-the-host-link-on-a-mega--baud-rate-is-real).

**Order matters.** `SW_LOAD` must be pulsed *before* the transfer and `LED_LATCH` *after* it.
Reversed, you read switch state one frame stale.

**Chain-length mismatch is fine.** Shifting 26 bytes clocks the 16-chip input chain 208 times
although it holds only 128 stages; the **first 16 bytes received are the valid ones**, and the
remainder is discarded. Tie the last 74HC165's `SER` input to GND so the surplus shifts in as
zeros rather than floating.

### 6.4 Timing budget — Mega 2560 at 16 MHz

**In the ISR** (must finish well inside 1 ms, and ideally inside the UART's tolerance):

| Item | Cost | At 1 kHz |
| --- | --- | --- |
| SPI transfer, 26 B @ 8 MHz (`F_CPU/2`) | 26 µs | 2.6 % |
| Latch / load pulses | ~4 µs | 0.4 % |
| Buffer swap, housekeeping | ~5 µs | 0.5 % |
| **ISR total** | **≈ 35 µs** | **≈ 3.5 %** |

**In the main loop:**

| Item | Cost | At 1 kHz |
| --- | --- | --- |
| Delta-sigma, 208 lamps @ ~10 cycles each | ≈ 2 080 cycles ≈ **130 µs** | **13 %** |
| UART RX/TX ISR @ 500 000 baud | ~20 cycles/byte × 50 kB/s | ≈ 6 % |
| Protocol parse, CRC, debounce | — | ≈ 3 % |
| **Total CPU** | | **≈ 25 %** |

Roughly **75 % headroom**. Comfortable — but note the delta-sigma pass at 130 µs is **the reason it
cannot live in the ISR**: that is over three times the UART's tolerance for blocked interrupts.

*(For comparison, on a 48 MHz UNO R4 the same delta-sigma pass costs ~4 % and could safely sit
inside the ISR. That convenience is the main thing you give up.)*

### 6.5 The host link on a Mega — baud rate is real

**The ATmega2560 has no USB peripheral at all.** A second microcontroller, the **ATmega16U2**,
translates USB into an ordinary serial line:

```
   Pi ↔ USB ↔ [ ATmega16U2 bridge ] ↔ real UART at a real baud rate ↔ ATmega2560
```

So unlike a board with native USB, **the baud setting here is a genuine hardware bottleneck**, not
a cosmetic parameter. Practical ceiling through the bridge: **~46–50 kB/s** (460 800–500 000 baud,
both confirmed reliable in practice).

#### Does the protocol fit? Yes — but not at the Arduino default

| Baud | Bytes/s | Our load (214 B @ 50 Hz + 23 B @ 20 Hz ≈ **11.2 kB/s**) | Verdict |
| --- | --- | --- | --- |
| 115 200 *(Arduino default)* | 11 520 | **97 %** | ❌ **Unusable** — no headroom whatsoever |
| 250 000 | 25 000 | 45 % | ⚠️ Works, thin margin |
| **460 800** | 46 080 | 24 % | ✅ Confirmed reliable |
| **500 000** | 50 000 | **22 %** | ✅ **Recommended** |
| 1 000 000 | 100 000 | 11 % | ⚠️ Reported but not consistently confirmed through the 16U2 |

**Set 500 000 baud. The 115 200 default would fail.**

A useful AVR quirk: with `U2X=1` at 16 MHz, **250 000 / 500 000 / 1 000 000 baud are *exact*
divisors** (UBRR = 7 / 3 / 1). The familiar 115 200 is not — it lands on 117 647, a **2.1 % error**.
The fast rates are more accurate than the slow one.

If you must stay at 115 200, two levers recover the margin without touching the architecture:
- **Drop the frame rate to 20 Hz** → 4.3 kB/s → 37 % — the modulation is unaffected, only how often
  brightness targets refresh.
- **Pack brightness to 4 bits** (16 levels, which §2.2 already recommends) → 104 B/frame → 45 %.

#### ⚠️ The real gotcha: the 1 kHz ISR will eat incoming bytes

This is AVR-specific and it will bite silently.

The ATmega2560 USART has only a **two-level receive FIFO**. At 500 000 baud a byte arrives every
**20 µs**, so you have roughly **40 µs of slack** before bytes are lost. But the delta-sigma pass
costs ~10 cycles × 208 lamps ≈ **2 080 cycles ≈ 130 µs at 16 MHz** — over three times the tolerance.
A naive `ISR()` blocks interrupts for its whole duration and **would drop received bytes**.

Two fixes; apply **both**:

1. **`ISR(TIMER1_COMPA_vect, ISR_NOBLOCK)`** — re-enables global interrupts on entry so the USART
   RX interrupt can preempt. A one-word change.
2. **Double-buffer the frame.** Compute delta-sigma in the main loop into an inactive 26-byte
   buffer; the ISR only shifts out the active buffer and latches (~30–40 µs). Swap buffers at the
   frame boundary.

Both are already reflected in [§6.3](#63-the-1-khz-frame--timer-isr): the ISR is declared
`ISR_NOBLOCK` and delta-sigma runs in the main loop against a double buffer.

*(Neither would be needed on an R4 — the Cortex-M4's NVIC nests interrupts by priority as a matter
of course, and its native USB has 64-byte endpoint buffers.)*

### 6.6 Better option: skip USB entirely

The Mega has **4 hardware UARTs**. Connect **Serial1 (D18 TX / D19 RX)** straight to the Pi's GPIO
UART (**GPIO14/GPIO15**, header pins 8/10). This removes the 16U2, the USB stack and USB
enumeration from the path — lower and far more predictable latency.

```
   Mega D18 (TX, 5 V) ──[ 1k8 ]──┬── Pi GPIO15 (RXD, 3.3 V)
                                 │
                               [ 3k3 ]        ← divider: 5 V → ~3.2 V
                                 │
                                GND

   Mega D19 (RX) ◄────────────────── Pi GPIO14 (TXD, 3.3 V)
        (no shifting needed: AVR V_IH = 0.6 × 5 V = 3.0 V, and 3.3 V > 3.0 V)

   GND ──────────────────────────── GND      ← common ground, mandatory
```

**Only the Mega→Pi direction needs level shifting.** Pi→Mega works unshifted because 3.3 V clears
the AVR's 3.0 V logic-high threshold — though a proper bidirectional level shifter is tidier if you
have one.

On the Pi you must **free the UART**: `raspi-config` → *Interface Options* → *Serial Port* →
**disable** the login shell over serial, **enable** the serial port hardware. The port is then
`/dev/serial0`.

Trade-off: you lose USB convenience (no enumeration, no serial monitor over the same cable) and the
Arduino needs its own 5 V supply. In exchange the link is direct, deterministic, and comfortably
handles 500 000 baud or more.

### 6.7 Upgrading to a UNO R4 Minima later

The R4 is a **drop-in swap**. Nothing in the wiring, the BOM, the protocol or the panel changes —
only three things:

| Change | Detail |
| --- | --- |
| **Pin numbers** | `MOSI` D51→**D11**, `MISO` D50→**D12**, `SCK` D52→**D13**. No `SS` pin to worry about. `LED_LATCH` D8, `SW_LOAD` D9, `LINK_LED` D7 all unchanged |
| **Baud rate** | Becomes cosmetic — native USB moves 64-byte packets regardless |
| **ISR structure** | `ISR_NOBLOCK` and the double buffer become optional. Delta-sigma costs ~4 % at 48 MHz and could move back into the ISR. **Leave the double buffer in place anyway** — it costs nothing and keeps the frame isochronous |

What you gain: ~20× the link bandwidth, no ISR/UART contention to reason about, 32 KB SRAM instead
of 8 KB, and a USB-C connector.

What stays the same and matters most: **5 V logic on both**, so the TPIC6B595 and 74HC165 chains
need **no level shifters** either way. That is the property that made both boards candidates and a
Teensy 4.1 not.

| Criterion | Mega 2560 | UNO R4 Minima |
| --- | --- | --- |
| Available in Argentina | ✅ **Yes** (29 210 ARS obs.) | ❌ Not found locally |
| Host link | ⚠️ ~50 kB/s via 16U2 bridge | ✅ ~1 MB/s native USB |
| Interrupt behaviour | ⚠️ Needs `ISR_NOBLOCK` + double buffer | ✅ NVIC nests by priority |
| Headroom | 16 MHz, 8 KB | ✅ 48 MHz, 32 KB |
| Spare I/O | ✅ 48 pins spare | 8 pins spare |
| 5 V logic | ✅ | ✅ |

**Build with the Mega.** The protocol fits at 22 % link utilisation, both AVR pitfalls are solved
in §6.3 and §6.5, and it is the board you can actually buy. Treat the R4 as a future upgrade path,
not a compromise you are settling for.

---

## 7. What the Arduino owns locally

Must work with the USB cable unplugged.

### 7.1 LAMP TEST

IBM: *"All console indicators should light when the LAMP TEST toggle switch is operated to the
TEST position. The switch can be operated at any time without affecting system operation."*

Override at the delta-sigma stage: while the toggle reads TEST, force every `target[i] = 255`.
**Never route this through the Pi** — "at any time" includes when Hercules is not running.

### 7.2 The TEST lamp

A pure function of switches the Arduino already reads — no emulator round-trip, so it responds
instantly exactly as a hardwired lamp would:

```c
TEST = (RATE        != PROCESS)
    || (CHECK_CTRL  != PROCESS)
    || (DIAG_CF     != PROCESS_IMPL)
    || (ADDR_CMP_CTRL != SYNC_NORM);   // ← the toggle, not a rotary
```

### 7.3 Debounce

- **Momentary keys:** 5–20 ms; report a **press event**, not a level, so the Pi issues exactly one
  Hercules command per press.
- **Toggles and mode rotaries:** 20–50 ms **and** N consecutive equal reads. Wafer switches bounce
  badly and sweep through intermediate positions while turning.
- **1-of-N validity:** if zero or more than one line in a group is active, **hold the last valid
  position** and flag it. Never report a garbage position mid-rotation.

### 7.4 Undrivable-lamp policy

Banks U5–U11 (~50 lamps) report 3145 hardware conditions Hercules cannot produce. Make the policy
a **compile-time constant** so it is explicit and auditable:

| Mode | Behaviour |
| --- | --- |
| `DARK` *(default)* | Never light them. Strictly correct — a healthy machine shows no system checks |
| `STATIC` | Fixed plausible pattern. Clearly a prop |
| `SYNTHETIC` | **Only** for Display Assembler Out position 2 (SDBO), driven from **real** storage traffic supplied by the Pi |

**Never drive check or fault lamps from a random source.** A panel showing storage parity errors
during normal operation is not a replica, it is a false claim about machine state.

### 7.5 Link loss

No lamp frame for **2 seconds** → ramp all targets to 0 and go dark, leaving only `LINK_LED`.
A dark panel honestly reads as "powered off"; freezing a stale PSW display indefinitely is a lie.

---

## 8. Host protocol

### 8.1 Frames

Binary, fixed-length after the header, CRC-16/CCITT checked.

**Pi → Arduino (lamp brightness)**

| Offset | Bytes | Field |
| --- | --- | --- |
| 0 | 2 | Magic `0xA5 0x5A` |
| 2 | 1 | Type `0x01` |
| 3 | 1 | Length `208` |
| 4 | 208 | **Brightness 0–255 per lamp**, lamp 0 = U1 bit 0 |
| 212 | 2 | CRC-16 over bytes 2–211 |

**Arduino → Pi (switch state)**

| Offset | Bytes | Field |
| --- | --- | --- |
| 0 | 2 | Magic `0x5A 0xA5` |
| 2 | 1 | Type `0x81` |
| 3 | 1 | Length `17` |
| 4 | 16 | Switch bitmap, S1 first |
| 20 | 1 | Sequence counter |
| 21 | 2 | CRC-16 over bytes 2–20 |

Plus `0x02` ping / `0x82` pong carrying firmware version and compiled bank sizes, so a
firmware/host mismatch is detected rather than silently misdriving the panel.

**Note the payload is brightness, not bits.** Bandwidth is a non-issue (§8.2) and per-lamp duty
cycle is the whole point of §2.

### 8.2 Bandwidth budget — and the hard limit

| Direction | Frame | Rate | Throughput |
| --- | --- | --- | --- |
| Pi → Arduino | 214 B | 50 Hz | 10.7 KB/s = **85.6 kbit/s** |
| Arduino → Pi | 23 B | 20 Hz | 0.46 KB/s = **3.7 kbit/s** |
| **Total** | | | **≈ 11 KB/s ≈ 89 kbit/s** |

**On the UNO R4**, native full-speed USB CDC delivers on the order of **1 MB/s** in practice, so
this uses roughly **1 %** of the link, and the baud setting is cosmetic.

**On a Mega 2560 the link is ~20× narrower** — the ATmega16U2 bridge tops out near **50 kB/s**, so
the same load runs at **22 % utilisation at 500 000 baud** and **97 % (unusable) at the 115 200
default**. Set the baud rate explicitly. Full analysis, plus the AVR interrupt hazard that comes
with it, in [§6.5](#65-alternative-arduino-mega-2560--and-what-it-does-to-the-pi-link).

SPI side: 26 B × 1000 Hz = **26 KB/s = 208 kbit/s**, about 2.6 % of an 8 MHz bus — identical on
both boards.

**Send rates:** lamp frames **on change, capped at 50 Hz**; switch frames **on change, plus a
20 Hz heartbeat** so a dead link is detected inside the 2 s window of §7.5.

> ### ⚠️ You cannot stream per-instruction state. Not close.
>
> Hercules on a Pi 5 will run S/370 at roughly **20–60 MIPS** — *measure it, Hercules reports its
> own MIPS; treat this as an estimate.* Streaming a 3-byte instruction address per instruction at
> 30 MIPS would be **90 MB/s ≈ 720 Mbit/s**, against a practical USB CDC ceiling near 1 MB/s.
> That is **~90× over budget at best**, and worse under realistic CDC throughput.
>
> **All aggregation must happen inside the Pi.** The link carries duty cycles, never raw traffic.

### 8.3 Shift order — the classic bug

Shift-register chains fill **back to front**: the first byte transmitted lands in the **last**
chip. To load U1…U26 you must send **U26 first**. Define this in exactly one place and verify it
with the walking-bit test (§10 step 3). Getting it wrong scrambles the whole panel in a way that
looks like a wiring fault and will cost a day.

The input chain is the mirror image: the first byte received comes from the chip nearest MISO.

### 8.4 How the Pi computes duty cycle

1. An **HDL module** inside Hercules (references §7.2) snapshots PSW, registers and the selected
   storage word into shared memory on a **~1 kHz timer**. Cheap — one sample per ~30 000
   instructions.
2. The panel daemon accumulates **per-bit one-counts** over a 20–50 ms window.
3. `target = 255 × ones / samples`, clamped to 0 below 16 (§2.2).

**This is statistical sampling, not true integration — and it lands where the real machine did.**
High-order address bits change slowly and will show real structure; low-order bits change every
instruction and average to ~50 %, blurring to half brightness. **That is exactly what a real 3145
lamp bank looked like.**

---

## 9. Power

**The most likely source of trouble. Read before wiring.**

| Load | Current |
| --- | --- |
| 208 LEDs × 10 mA, all lit (**LAMP TEST**) | **2.08 A** |
| 26 × TPIC6B595 quiescent | ~30 mA |
| 16 × 74HC165 quiescent | ~10 mA |
| Arduino Mega 2560 | ~50 mA |
| **Worst case** | **≈ 2.15 A** |
| Typical (~30 % duty across the panel) | ≈ 0.7 A |

1. **Dedicated 5 V ≥ 4 A supply for the panel.** Never draw LED current through the Arduino's
   regulator or a Pi USB port — LAMP TEST would brown out the Pi, which is running your emulator
   and its filesystem.
2. **Common ground**, tied at exactly **one** point (star), or SPI has no reference.
3. **Decoupling: 100 nF across every chip's supply pins, plus 1000 µF bulk per LED bank.**
   Delta-sigma at 1 kHz means the panel current is *continuously switching* — this is a harsher
   supply environment than static drive, and inadequate bulk capacitance will glitch the shift
   registers.
4. **Do not back-feed the Arduino.** Power it from USB only (its own draw is trivial) *or* from
   the panel supply with the USB power line cut — never both. **USB-powered board + separately
   powered chains + common ground is the simple correct answer.**
5. **EPO:** sense it as an **input** and let the Pi shut down cleanly. Never wire it to anything
   that can cut power mid-write and corrupt the filesystem.

---

## 10. Bring-up and test plan

In order. Each step isolates one failure mode.

| # | Step | Pass criterion |
| --- | --- | --- |
| 1 | One TPIC6B595 on a breadboard, 8 LEDs, hand-clocked | Each LED lights individually |
| 2 | Same chip via `SPI.transfer()` + latch | Byte pattern appears correctly |
| 3 | **Chain all 26; walking-bit test**, one LED stepping 0→207 | Lit LED moves in expected physical order — **validates §8.3** |
| 4 | Full-on, measure rail under load | ≥ 4.75 V. If it sags, revisit §9 |
| 5 | **Delta-sigma sweep**: ramp one lamp 0→255 | Smooth, monotonic; **no flicker at or above target 16** |
| 6 | **Flicker floor check**: set targets 4, 8, 16, 32 | 4 and 8 visibly flicker; 16 and 32 do not. Confirms the §2.2 floor empirically |
| 7 | **Camera check**: photograph at 1/500 s and 1/2000 s | No banding or dark rows across the panel |
| 8 | One 74HC165, 8 switches, print raw byte | Bits track switches; verify pull-up polarity |
| 9 | Chain all 16, print 128 bits | Every physical switch maps to the expected bit |
| 10 | **Hex wheel decode**, turn each 0→F | Reads 0→F — **verify complement polarity** (§5.2) |
| 11 | **1-of-N validity**, turn a mode rotary slowly | Never reports an invalid or intermediate position |
| 12 | **LAMP TEST with USB unplugged** | All lamps light — proves §7.1 autonomy |
| 13 | **Latency**: toggle a switch, scope the Pi's response on a spare pin | ≤ 10 ms end to end |
| 14 | **Link loss**: unplug USB while running | Panel dark after ~2 s per §7.5 |
| 15 | **Frame jitter**: scope `LED_LATCH` | Period 1.000 ms ± < 1 % under USB load — confirms the ISR is not being starved |

---

## 11. Bill of materials (provisional)

> **Argentina column — read this first.**
> Prices marked **(obs.)** were observed on an Argentine retailer's site on **2026-08-02**.
> Everything else is an **estimate** derived from international price × typical local markup, and
> is flagged as such. **Argentine peso figures age extremely fast under inflation — re-check every
> ARS number before ordering.** I did *not* assume an ARS/USD rate; where a USD figure appears it
> is the international reference price, not a conversion. MercadoLibre blocks automated access, so
> its listings could not be priced here — check it manually, it is where most local hobbyists buy.

| Qty | Part | Purpose | Argentina — source and price |
| --- | --- | --- | --- |
| 1 | **Arduino Mega 2560** | Controller — 5 V logic, 16 MHz, 54 I/O, 4 UARTs (§6.1) | ✅ **Available locally.** [TodoMicro](https://www.todomicro.com.ar/): *Mega 2560 R3 + USB cable* **29 210 ARS (obs.)**. *(Optional future upgrade: UNO R4 Minima — **not found in local stock**, would need importing; see §6.7)* |
| 26 | TPIC6B595 | LED shift/sink drivers | ⚠️ **Unlikely locally.** TodoMicro search for 74HC595 returned **no bare-IC listing** — local hobby shops stock modules and kits, not logic ICs in quantity. Try [Elemon](https://www.elemon.com.ar/), [SyC Electrónica](https://www.sycelectronica.com.ar/), [Electrocomponentes](https://www.electrocomponentes.com.ar/) (distributors, not hobby shops); otherwise import. Int'l ref ≈ US$1 each |
| 16 | 74HC165 | Switch input shift registers | Same as above. Int'l ref ≈ US$0.50 each. Also on [MercadoLibre](https://electronica.mercadolibre.com.ar/componentes-electronicos/74hc165) — verify price manually |
| ~208 | LED, diffused — **~25 red, ~11 amber, ~110 white** (see §4.3a) | Panel lamps | ✅ **Readily available.** TodoMicro: *5 mm high-brightness, 100-pack* **5 919 ARS (obs.)**; *500-pack, 5 colours ×100* **6 537 ARS (obs.)**. ⚠️ Those are **high-brightness/straw-hat** — you want **diffused**; confirm before buying |
| ~208 | Resistor 330 Ω / 220 Ω | LED current limit — value follows the LED's Vf | ✅ Commodity. Est. **<3 000 ARS** for a 500-pack assortment |
| ~168 | Resistor 10 kΩ | Switch pull-ups (Option B: 40) | ✅ Commodity |
| ~168 | Resistor 1 kΩ | Switch input protection | ✅ Commodity |
| 42 | Capacitor 100 nF ceramic | Per-chip decoupling | ✅ Commodity, est. **<2 000 ARS** |
| ~4 | Capacitor 1000 µF electrolytic | Bulk, per LED bank | ✅ Commodity |
| **264** | **1N4148 diode** *(Option B only)* | Wheel encoder matrix — §5.2 | ✅ Commodity. Int'l ref ≈ US$3–8 for the lot; est. **<8 000 ARS** locally |
| 8 | Rotary switch for wheels A–H — **Option A** hex-coded *or* **Option B** 16-position non-shorting | Wheels A–H | ⚠️ **The hardest part to source locally.** Coded types (Grayhill/CTS/Nidec) are specialist — expect to import. Plain 16-position panel switches: check [MercadoLibre](https://listado.mercadolibre.com.ar/llave-rotativa-16-posiciones) and [Elemon](https://www.elemon.com.ar/). **Budget generously and order early** |
| 5 | Multi-position wafer rotary switch — **9, 9, 3, 5, 7** positions | ADDRESS COMPARE, STORAGE SELECT, RATE, CHECK CONTROL, DIAG/CF | ⚠️ Specific position counts are hard to source; a 12-position switch with a mechanical stop is the usual workaround. Check [Electrónica Liniers](https://www.electronicaliniers.com.ar/), [Nubbeo](https://www.nubbeo.com.ar/) |
| ~6 | Toggle switch (one 3-position) | LAMP TEST, INTERVAL TIMER, TOD CLOCK, ADDRESS COMPARE CONTROL, CF REG DISPLAY | ✅ Widely available, est. **1 500–3 000 ARS each** |
| 15 | Square momentary pushbutton | The keys — see the [3D-printed IBM inserts](https://www.printables.com/model/165377-ibm-system360-and-370-mainframe-computer-console-p), ≈ 25.5 × 25.1 mm | ✅ Tactile switches commodity; the **authentic square caps you 3D-print yourself** |
| 1 | 5 V ≥ 4 A regulated supply | Panel power | ✅ Common. Est. **15 000–30 000 ARS** |
| 1 | USB-C cable | Pi ↔ Arduino | ✅ Commodity |
| 2 | Hour meter *(optional)* | Customer / service use meters | ⚠️ Specialist; consider a small OLED instead |

#### Argentine suppliers — all verified reachable 2026-08-02

| Supplier | Type | Notes |
| --- | --- | --- |
| [TodoMicro](https://www.todomicro.com.ar/) | Hobby / maker retail | **The only one that returned live ARS prices to an automated query.** Strong on Arduino, LEDs, modules; weak on bare logic ICs |
| [MercadoLibre Argentina](https://electronica.mercadolibre.com.ar/componentes-electronicos/) | Marketplace | Where most local hobbyists actually buy. **Blocks automation — price it by hand** |
| [Elemon](https://www.elemon.com.ar/) | Distributor | One of the larger Argentine component distributors |
| [SyC — Semiconductores y Componentes](https://www.sycelectronica.com.ar/) | Distributor, wholesale + retail | Best bet for bare semiconductors |
| [Electrocomponentes S.A.](https://www.electrocomponentes.com.ar/) | Distributor, 40 yrs | Brand representation, instruments, tools |
| [Cika Electrónica](https://www.cika.com.ar/) | Distributor | Offices in Brazil, USA, Taiwan, Hong Kong — may help with imports |
| [Nubbeo](https://www.nubbeo.com.ar/) | Retail | General electronics |
| [Electrónica Liniers](https://www.electronicaliniers.com.ar/) | Retail | Switches, connectors, passives |
| [Puntotec](https://puntotec.com.ar/) | Retail | General |
| [Dinastía Tecnológica](https://dinastiatecnologica.com/) | Retail | General |

#### Honest sourcing assessment

**Three tiers, and only one is a problem:**

1. ✅ **Commodity — buy locally without thinking.** LEDs, resistors, capacitors, diodes, tactile
   switches, toggles, power supply, cable. Argentine retail carries all of it.
2. ⚠️ **Bare logic ICs (42 chips).** Argentine *hobby* shops sell modules and kits, not
   TPIC6B595/74HC165 in quantity — TodoMicro's 74HC595 search returned no bare-IC listing at all.
   The *distributors* above may stock them; otherwise import. This is 42 small parts, so shipping
   weight is negligible.
3. 🔴 **The rotary switches — the real constraint.** Coded hex switches are specialist parts
   unlikely to be on any Argentine shelf, and the exact position counts (9, 9, 3, 5, 7) are hard
   to source anywhere. **Start sourcing these first**; everything else can be bought in an
   afternoon.

**Practical route:** buy tier 1 locally, and place a single consolidated import order for the
42 ICs plus the 13 rotary switches. That is one shipment of small, light parts — the sensible way
to handle it given Argentine import friction.

---

## 12. Open questions

| # | Question | Blocks | Resolve via |
| --- | --- | --- | --- |
| 1 | ~~Exact lamp count per bank~~ **✅ RESOLVED 2026-08-02 by visual count** — 149 indicator positions across 7 banks; ~164 including backlit keys. Allocation in §4.3 is now built on verified numbers | — | Counted at 430–500 dpi from the [GA24-3554-0 scan](https://www.bitsavers.org/pdf/ibm/370/model145/GA24-3554-0_370_Model_145_Operating_Procedures_Sep70.pdf) pp. 8–13 |
| 2 | ~~Do the roller banks carry parity lamps?~~ **✅ RESOLVED — YES.** 36 lamps per bank (4 bytes × `P 0 1 2 3 │ 4 5 6 7`), 72 total, parity lamps amber (§4.4). **The earlier "no parity" answer was wrong** | — | Visual count; the text layer had misled the earlier reading |
| 3 | ~~Position counts for the mode rotaries~~ **✅ RESOLVED 2026-08-02** — ADDRESS COMPARE 9 · STORAGE SELECT 9 · **RATE 3** · CHECK CONTROL 5 · DIAG/CF CONTROL 7 = **33 lines** | — | Counted visually; detent legends transcribed in [inventory §5.0](2026-08-01-370-145-panel-inventory.md#50--verified-switch-and-key-census--counted-from-the-scan-2026-08-02) |
| 4 | **Key count ✅ RESOLVED** — 18 positions, **15 labelled**, 3 blank caps. **Still open: which keys are backlit.** POWER ON and START CONSOLE FILE are documented as two-colour (red→white); the rest is unknown | §4.3 U23–U24; two-colour needs 2 bits/key | Colour photographs of a real console |
| 5 | ~~Lamp pitch and panel dimensions~~ **DOWNGRADED 2026-08-02** — the replica carries the original's **proportions and layout, not its absolute dimensions**. Lamp pitch is now a **design choice** bounded below by LED size, not a fact to be discovered. Remaining input needed is one straight-on console photograph for the overall aspect ratio | PCB layout — but as a decision, not a blocker | [Inventory §7.5–§7.6](2026-08-01-370-145-panel-inventory.md#75-panel-scale-and-proportions) for the scale method and minimum-size analysis |
| 6 | **Hex-coded rotary switch** availability, price and output polarity | §5.2 | Datasheets — **buy one and test before committing to eight** |
| 7 | **Actual Hercules MIPS on the target Pi** | §8.4 sampling design | Run TK5 and read Hercules' MIPS display |

**Q1 is now the critical path** (it fixes both artwork and BOM). Q5 was downgraded on 2026-08-02 by
the proportions-not-dimensions decision. **Q2–Q4 affect final bit allocation but not the
architecture** — the topology and parts list stand regardless.

### 12.1 How many rotary switches are actually useful to Hercules?

**All 13 are readable; 11 of 13 drive real Hercules behaviour.** Rotary switches are *inputs*, and
inputs are the easy direction — the Arduino reads them regardless of whether Hercules has a
counterpart. The question is how many change what the emulator does.

| Rotary | Count | Useful? | What it drives |
| --- | --- | --- | --- |
| **Wheels F, G, H** | 3 | ✅ **Fully** | **LOAD UNIT ADDRESS** → `ipl <cuu>`; **MAIN STORAGE ADDRESS** → storage display/alter and breakpoint address. The most-used controls on the panel |
| **Wheels A, B** | 2 | ✅ **Fully** | **DATA** — the byte value for a manual store → `store` operand |
| **Wheel H** *(shared with above)* | — | ✅ **Fully** | **WORD ADDRESS** — selects which GPR/FPR to display → `gpr` / `fpr` index |
| **Wheels C, D, E** | 3 | ⚠️ **Partially** | Documented uses are CF ADDRESS and BYTE COUNT — both **service functions with no Hercules counterpart**. They *are* read, and C–E participate in the wider address groupings, so they are not wasted — but on their own they drive nothing |
| **RATE** | 1 | ✅ **Fully** | PROCESS → `start`; INSTRUCTION STEP → single-step per START press. **The cleanest one-to-one mapping on the panel.** Also feeds TEST |
| **ADDRESS COMPARE** | 1 | ✅ **Fully** | Selects *which kind* of access triggers a match: instruction fetch / data store / I/O / any-real / any-logical → genuinely different Hercules breakpoint semantics |
| **STORAGE SELECT** | 1 | ✅ **Fully** | MAIN STORAGE → `r`/`v`; LOCAL STORAGE → `gpr`/`fpr`. Decides what DISPLAY and STORE act on |
| **CHECK CONTROL** | 1 | ⚠️ **TEST lamp only** | Machine-check behaviour — Hercules has no machine checks. But it **feeds the TEST lamp** (§7.2), so it is not inert |
| **DIAGNOSTIC / CONSOLE FILE CONTROL** | 1 | ⚠️ **TEST lamp only** | Console-file and diagnostic modes — no counterpart. **Feeds the TEST lamp** |

**Tally: 8 of 13 rotaries drive Hercules commands directly; 2 more drive the TEST lamp locally;
3 (wheels C, D, E) have no independent function** but are still read and still turn.

This is a far better ratio than the lamps (§7.2), and it is the reason the /145 is satisfying to
*operate* rather than merely to look at: dial an address into F-G-H, press LOAD, and a real IPL
happens.

---

## 13. References

Every source consulted while writing this document. **All URLs HTTP-checked 2026-08-02 and
returned 200** unless noted. Broader source collection: [`2026-08-01-references.md`](2026-08-01-references.md).

### 13.1 IBM primary documentation — what the panel must do

| Reference | Used for |
| --- | --- |
| [GA24-3554-0 — *IBM System/370 Model 145 Operating Procedures*, Sep 1970](https://www.bitsavers.org/pdf/ibm/370/model145/GA24-3554-0_370_Model_145_Operating_Procedures_Sep70.pdf) | **The source of every lamp, switch and key in §4–§5.** Chapter "Console Indicators, Switches, and Keys" pp. 8–23. Has a real text layer. Basis for the parity finding in §4.4 (roller tables show `Byte 0–3` with no parity column; the only "parity" in the manual is `M-REG PARITY CHECK` in the System Check bank) |
| [SR20-4460-0 — *System/370 Operator's Reference Guide*, Jul 1974](https://www.bitsavers.org/pdf/ibm/370/SR20-4460-0_System_370_Operators_Reference_Guide_Jul74.pdf) | Confirmed **LOAD UNIT ADDRESS = wheels F, G, H** (§5.2); cross-model comparison establishing that the /145 is the only /370 displaying architected data on its own lamps; the /165–/168 CE parity/ROS/ALU check groups cited in §4.4 |
| [GA22-7000-0 — *System/370 Principles of Operation*, Jun 1970](https://www.bitsavers.org/pdf/ibm/370/princOps/GA22-7000-0_370_Principles_Of_Operation_Jun70.pdf) | "Operator Facilities" — the architected definition of reset, IPL, rate control, address compare. Storage-key architecture (`SSK`/`ISK`) behind the §4.3 storage-key claim; and the absence of any architected parity, per §4.5 |
| [SY24-3581-1 — *3145 Processing Unit Theory–Maintenance*, Oct 1971](https://bitsavers.org/pdf/ibm/370/fe/3145/SY24-3581-1_3145_Processing_Unit_Theory-Maintenance_Oct71.pdf) (57 MB) | Cited as the resolution path for open questions §12 Q2 and Q5 — panel layout, lamp wiring, CE-only indicators |
| [S124-0129-2 — *3145 Processing Unit Parts Catalog*, Oct 1975](https://bitsavers.org/pdf/ibm/370/fe/3145/S124-0129-2_3145_Processing_Unit_Parts_Catalog_Oct75.pdf) | Cited for lamp pitch and panel dimensions (§12 Q5) |

### 13.2 Component datasheets

| Reference | Used for |
| --- | --- |
| [TI TPIC6B595 product page](https://www.ti.com/product/TPIC6B595) · [datasheet (PDF)](https://www.ti.com/lit/ds/symlink/tpic6b595.pdf) | §4.1 — 8-bit shift register with open-drain DMOS outputs, 150 mA/channel, ~500 mA package, `G`/`SRCLR`/`SER OUT` behaviour |
| [TI SN74HC165 product page](https://www.ti.com/product/SN74HC165) · [datasheet (PDF)](https://www.ti.com/lit/ds/symlink/sn74hc165.pdf) | §5.1 — parallel-in/serial-out, `SH/LD` and `CLK INH` behaviour, **no internal pull-ups** |
| [Nexperia 74HC/HCT165 datasheet (PDF)](https://assets.nexperia.com/documents/data-sheet/74HC_HCT165.pdf) | Second-source confirmation of the same |

### 13.3 Microcontroller

| Reference | Used for |
| --- | --- |
| [**Arduino Mega 2560** — documentation](https://docs.arduino.cc/hardware/mega-2560/) | §6.1–§6.4 — ATmega2560, **16 MHz crystal**, **4 UARTs**, **54 digital I/O** (15 PWM), 16 analog inputs. The 4 UARTs are what make the direct-to-Pi-GPIO option in §6.6 possible |
| [Arduino Forum — max baud rate on the Mega 2560](https://forum.arduino.cc/t/maximum-baud-rate-on-arduino-mega-2560/464915) · [UNO/ATmega16U2 max serial throughput](https://forum.arduino.cc/t/uno-atmega16u2-maximum-serial-throughput/893662) | §6.5 — the practical ceiling through the **ATmega16U2 bridge**: 460 800 and 500 000 baud confirmed reliable, 1 Mbaud reported but not consistently. The basis for "set 500 000, never 115 200" |
| [Arduino UNO R4 Minima — documentation](https://docs.arduino.cc/hardware/uno-r4-minima) | §6.7 upgrade path — **"5 V only"**, Renesas RA4M1 Cortex-M4, 48 MHz, **USB-C native to the MCU**, 14 digital + 6 analog, 32 KB SRAM / 256 KB flash / 8 KB EEPROM |
| [UNO R4 Minima datasheet ABX00080 (PDF)](https://docs.arduino.cc/resources/datasheets/ABX00080-datasheet.pdf) | Electrical detail and pin mapping |
| [UNO R4 Minima cheat sheet](https://docs.arduino.cc/tutorials/uno-r4-minima/cheat-sheet) | SPI pin assignment (§6.2), timer and peripheral notes |
| [Arduino store — UNO R4 Minima](https://store.arduino.cc/products/uno-r4-minima) | Confirmed *"operating voltage is fixed at 5 V to be fully retro compatible with shields"* — the decisive point for **no level shifters** |
| [Renesas RA4M1 product page](https://www.renesas.com/en/products/ra4m1) | MCU peripherals — hardware timers for the §6.3 isochronous frame |

### 13.4 Modulation and perception

| Reference | Used for |
| --- | --- |
| [Delta-sigma modulation (Wikipedia)](https://en.wikipedia.org/wiki/Delta-sigma_modulation) | §2.2 — first-order accumulator/overflow formulation and why it distributes pulses evenly versus fixed-window PWM |
| [Flicker fusion threshold (Wikipedia)](https://en.wikipedia.org/wiki/Flicker_fusion_threshold) | §2.2 — basis for the 62.5 Hz floor and therefore the clamp at target 16 |
| [hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) | Reference implementation for careful LED timing and binary-code modulation; informed the isochronous-ISR requirement in §6.3 |

### 13.5 Prior art — replica panel electronics

| Reference | Used for |
| --- | --- |
| [Operation Blinkenlights — January 2012 archive](http://ibm360-console.blogspot.com/2012_01_01_archive.html) | **The latency figure in §1**: a Velleman K8061 USB I/O board gave ~1 s panel response versus **~1 ms** on an Arduino Mega 2560. Also the 74HC595/74HC597 chain topology (237 outputs, 183 inputs) and the orange-LEDs-in-modified-casings note in §4.2. *(HTTP-only site)* |
| [Operation Blinkenlights — "Emulator goes hardware"](https://ibm360-console.blogspot.com/2012/04/emulator-goes-hardware.html) | Why microarchitectural lamps forced an FPGA — the reasoning behind §7.4 |
| [PiDP-11 technical details](https://obsolescence.wixsite.com/obsolescence/pidp-11-technical-details) | Multiplexing scheme rejected in §2.1; **1 kΩ switch-sense limiting** adopted in §5.1; UDN2981 and 390 Ω precedent |
| [PiDP-10 technical details](https://obsolescence.wixsite.com/obsolescence/pidp-10-technical-details) | The same approach at larger lamp counts |
| [ETC CMU — "Driving a looooooot of LEDs"](https://www.etc.cmu.edu/projects/flux/?p=233) | TLC5940 + MIC5891 cost comparison behind the §4.1 driver rejection |
| [Hackaday.io — "My LED Matrix Needs a Little TLC"](https://hackaday.io/page/10259-my-led-matrix-needs-a-little-tlc) | TLC5940 practical experience |
| [JLCPCB — Arduino LED driver guide: 74HC595 and MAX7219](https://jlcpcb.com/blog/arduino-led-driver-tutorial) | Cascading and SPI practice; MAX7219 comparison in §4.1 |
| [ShiftRegisterLEDMatrixLib](https://github.com/michaelkamprath/ShiftRegisterLEDMatrixLib) | Existing shift-register LED library — a code starting point |
| [Printables — IBM S/360 and S/370 console pushbutton inserts](https://www.printables.com/model/165377-ibm-system360-and-370-mainframe-computer-console-p) | Key dimensions ≈ 25.5 × 25.1 × 18.8 mm (§11 BOM). *(403 to scripts, loads in a browser)* |

### 13.6 Hercules — what the host can supply

| Reference | Used for |
| --- | --- |
| [Hercules configuration file reference](https://hercules-390.github.io/html/hercconf.html) | `ARCHLVL` vs `CPUMODEL`; confirmation that `CPUMODEL` is *"a purely cosmetic value only"* and that `ARCHLVL S/370` is required for MVS 3.8j |
| [Hercules documentation set (v4)](https://hercules-390.github.io/html/) | Panel commands and operation — the command targets behind the §5.2 firmware actions |
| [Hercules User Reference Guide v3.12 (PDF)](https://hercdoc.glanzmann.org/V312/HerculesUserReference.pdf) | `ipl`, `iplc`, `sysreset`, `sysclear`, `restart`, `start`, `stop`, `store`, `psw`, `gpr`, `fpr`, `cr` |
| [README.HDL.md — Hercules Dynamic Loader](https://github.com/SDL-Hercules-390/hyperion/blob/master/readme/README.HDL.md) | The loadable-module mechanism behind the §8.4 sampling design |
| [SDL-Hercules-390/hyperion](https://github.com/SDL-Hercules-390/hyperion) | Source for the `EXTERNALGUI` path and storage-key implementation |

---

## 14. Change log

| Date | Change |
| --- | --- |
| 2026-08-02 | Initial plan. **1 kHz first-order delta-sigma density modulation** (emulating incandescent thermal averaging), TPIC6B595 output chain, 74HC165 input chain, **Arduino UNO R4 Minima** (USB-C, 5 V, 48 MHz), brightness-payload host protocol. |
| 2026-08-02 | **Parity resolved** (§4.4–§4.5): roller banks are **32 lamps each, 64 total, no parity lamps** — `GA24-3554-0` shows no parity column and reports parity only as the `M-REG PARITY CHECK` fault lamp. Hercules supplies no parity data and cannot, but computed odd parity is an honest substitute. Open question 2 closed. Added §13 References. |
| 2026-08-02 | Open question 5 downgraded — panel dimensions are now a design choice, not a discovery (see inventory §7.5–§7.6). Added §12.1: **8 of 13 rotary switches drive Hercules commands directly, 2 more drive the TEST lamp locally, 3 have no independent function.** |
| 2026-08-02 | **§6 rewritten around the Arduino Mega 2560 as the build target** — the UNO R4 is unavailable in Argentina. Mega pin assignment is now primary (**MOSI D51 / MISO D50 / SCK D52 / SS D53**, with the `SS`-as-output trap flagged); §6.3 ISR restructured to `ISR_NOBLOCK` + **double buffer, with delta-sigma moved to the main loop**; §6.4 timing rebudgeted for 16 MHz (ISR ≈35 µs, total CPU ≈25 %). New **§6.5** on the ATmega16U2 bridge making baud a real bottleneck (**500 000 required; the 115 200 default fails at 97 %**) and the AVR ISR/UART contention hazard; **§6.6** direct Serial1→Pi GPIO UART with level-shifting; **§6.7** R4 as a documented drop-in upgrade. BOM, power table and architecture diagram updated to match. |
| 2026-08-02 | **Option B fully specified** (§5.2): diode-matrix encoder circuit, the 16 × 5 diode table, firmware decode, and the **POS0 line** that distinguishes a genuine position 0 from a wheel sitting between detents — **33 diodes per wheel, 264 total**; wheel input lines rise to 40 (≈97 of 128 overall, still fits). Added an **Argentina sourcing column** to the BOM (§11) with 10 verified local suppliers and observed ARS prices where obtainable. |
| 2026-08-02 | **Keys and rotary positions counted. Open questions 3 and 4 (count portion) closed.** Mode rotaries = **33 positions** (RATE has only **3** detents, not 4). Keys = **18 positions, 15 labelled, 3 blank**. Verified input budget **≈89 of 128 lines**. Added rotary-switch **sourcing and pricing** to §5.2. |
| 2026-08-02 | **Lamps counted from the rendered scan. Open questions 1 and 2 closed.** ⚠️ **Parity correction: the roller banks DO carry parity lamps** — 36 per bank (`P 0 1 2 3 │ 4 5 6 7` × 4 bytes), 72 total, not 64. The previous "no parity" conclusion was drawn from the PDF text layer and was wrong. Bit allocation §4.3 rebuilt on verified counts (≈164 lamps). Added §4.3a: **IBM colour-codes the lenses — 25 red, 11 amber, ~110 white.** |
