# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository status

**There is no code in this repository yet.** It contains research and design documents only:
`2026-08-01-references.md` (sources, ~320 verified links),
`2026-08-01-370-145-panel-inventory.md` (build spec — every lamp, switch and key on the 3145
console with its Hercules mapping), `2026-08-02-arduino-wiring-plan.md` (electrical and firmware
plan: 1 kHz delta-sigma LED drive, TPIC6B595/74HC165 chains, Arduino UNO R4 Minima), and
`.claude/settings.local.json`.

There is therefore **no build, lint, test, or run command to document**. Do not invent one, and do
not add a section describing one until the corresponding tooling actually exists. When code does
arrive it will span three separate toolchains — Arduino/PlatformIO firmware, Raspberry Pi host
software, and CAD/vector files for the acrylic panel — so record each one's commands separately as
it lands.

Despite the `github/` path, **this directory is not a git repository** (`git rev-parse` fails).
Do not assume git history exists or that `git` commands will work here.

## What this project is

A physical replica of an **IBM System/370 operator control panel**:

- Laser-cut acrylic front panel mimicking the real console.
- An **Arduino** drives the LEDs and reads buttons, toggle switches and rotary switches.
- The Arduino connects over **USB** to a **Raspberry Pi**.
- The Pi runs the **Hercules** emulator with **MVS Turnkey** (TK4-/TK5) inside.

The goal is maximum fidelity to the real machine — all lights, buttons and switches.

## Design decisions already settled (do not re-litigate these)

These were established by reading IBM's primary manuals. Re-deriving them wastes effort, and
guessing at them produces wrong answers.

**Target machine: the IBM System/370 Model 145 (3145).** Three reasons, in priority order:

1. **Hercules' `CPUMODEL` is purely cosmetic.** IBM's own configuration documentation states it
   "defines a purely cosmetic value only" — it sets the machine type reported by the `STIDP`
   instruction and nothing else. Only `ARCHLVL` changes actual behaviour. MVS Turnkey's default
   of "IBM 3033" is therefore one line in the `.cnf` file, not a constraint: set `CPUMODEL 0145`
   and the emulation is byte-identical. **The panel choice is fully independent of what Hercules
   reports.**
2. **The /145 has the best drivable-lamp ratio.** It has only two roller switches, and
   `GA24-3554-0` footnotes A-REGISTER DISPLAY positions 2–8 and DISPLAY ASSEMBLER OUT positions
   3–8 as "for service use" — 3145 microarchitecture with no Hercules counterpart. The /155, /165
   and /168 have many more lamps that cannot be driven.
3. **Best documentation on Bitsavers** — operating procedures *and* a 57 MB FE theory/maintenance
   manual *and* a parts catalog. By contrast the 3033 has only three files and no FE manual at all.

**Do not replicate the 3033's own console.** It is the 3036: an L-shaped desk with two 3277 CRT
workstations and service processors. Replicating it faithfully yields green screens, not
blinkenlights.

**Hercules is an architecture emulator, not a microarchitecture emulator.** Available: PSW,
instruction address, CPU running/stopped/wait state, IPL state, registers, storage, device
activity, MIPS. Not available: ALU, microcode, local-storage and bus-level signals that the real
roller positions displayed. Some roller positions will necessarily be decorative — say so
explicitly in any user-facing documentation rather than implying full fidelity.

**Useful consequence:** the TEST lamp is defined as on whenever RATE, CHECK CONTROL,
DIAGNOSTIC/CONSOLE FILE CONTROL or ADDRESS COMPARE CONTROL is off-normal. That is a pure OR of the
panel's own switch positions — compute it in the Arduino, no emulator data required.

## Navigating the reference document

`2026-08-01-references.md` has 21 top-level sections and ~321 verified URLs. Rather than reading
it end to end, jump to what you need:

| Need | Section |
| --- | --- |
| Which panel to build and why | §1, and §20 for the lamp-by-lamp proof |
| Vector artwork to trace for the laser cutter | §2 |
| IBM primary manuals (panel layouts, switch semantics, dimensions) | §3 |
| Prior art — read before designing anything | §5 (Operation Blinkenlights, PiDP, BlinkenBone) |
| Hercules control interfaces | §7 |
| MVS Turnkey | §8 |
| LED driving and switch scanning electronics | §9 |
| Acrylic laser-cutting file requirements | §10 |
| What the 3033 console actually was | §17 |
| IBM hardware timeline 1952–2026 | §18 |
| Which links are dead and their replacements | §19 |

Each section entry carries a one-line description of the source's content. §16 lists what is
*not* publicly available and must be originated.

## Link rot — verified 2026-08-01

Two important sites are **completely offline**. If you find references to them, substitute:

- `hercules-390.org` → docs at <https://hercules-390.github.io/html/>, code at
  <https://github.com/hercules-390/hyperion>
- `wotho.ethz.ch/tk4-` (TK4- home) → live mirror <https://wotho.pebble-beach.ch/tk4-/>

The Operation Blinkenlights wiki, which held that project's modified Hercules source, is dead
**and essentially unarchived** — a CDX query returns only a redirect, a favicon and a paywalled
entry. Do not send the user to the Wayback Machine for it; that material appears lost.

Several sources are **HTTP-only** (quadibloc.com, softdevlabs.com, retrocmp.com) and will fail any
tool that forces HTTPS — they work fine in a browser. Others (printables.com, ibm.com, direct.mit.edu,
digikey.com) return 403 to scripts but load normally in a browser. Neither category is dead.

§19.5 documents the Wayback availability and CDX APIs for finding replacements, plus the four live
Bitsavers mirrors. Note that `bitsavers.computerhistory.org` no longer resolves — rewrite such URLs
to `bitsavers.org`.

## Environment notes for this machine

- `python` and `python3` are **Windows Store stubs that do not execute**. Use `uv` (installed) to
  get a real interpreter, or avoid Python.
- `pdftotext`, `jq`, `curl` and `uv` are all available and work.
- Many Bitsavers PDFs have a real text layer and can be extracted with `pdftotext -layout`
  (`GA24-3554-0` and `SR20-4460-0` both do). **The IBM 3033 manuals are image-only scans** and
  cannot be text-extracted — they require visual inspection.
- IBM's PDFs on `ibm.com` need a browser User-Agent on `curl`; some still return 403 and must be
  reached by clicking through the landing page.

## Working conventions

When adding sources to the reference document, follow the established pattern: every entry carries
a **live-checked URL and a short description of what the source actually contains** — not just a
title. Bare links without explanation are not useful to this project.

Link-check before claiming a source is dead, and distinguish the four failure modes the document
already separates: genuinely dead, transiently overloaded (503), bot-blocked (403 but live), and
HTTP-only. Conflating them sends the user chasing archives for pages that load fine in a browser.
