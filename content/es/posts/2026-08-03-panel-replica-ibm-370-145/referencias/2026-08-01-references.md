# IBM System/370 Replica Panel — Reference Collection

**Date:** 2026-08-01
**Project:** Acrylic replica of an IBM System/370 operator control panel, driven by an Arduino
(LEDs out / switches, buttons and rotary switches in) over USB from a Raspberry Pi running the
Hercules emulator with MVS Turnkey.

---

## 0. How to use this document

The sections below are ordered by the order you will actually need them:

1. **[§1 Choosing which panel to replicate](#1-design-decision-which-370-panel-to-replicate)** — decide the target model first; everything downstream depends on it.
2. **[§2 Panel artwork and pixel-accurate drawings](#2-panel-artwork-and-pixel-accurate-drawings-for-laser-cutting)** — the vector/graphic sources for the laser cutter.
3. **[§3 Primary IBM documentation](#3-primary-ibm-documentation-bitsavers-and-friends)** — authoritative panel layouts, lamp and switch semantics, dimensions.
4. **[§4 Photographs, museums and archives](#4-photographs-museums-and-archives)** — ground truth for colours, textures, proportions.
5. **[§5 Existing replica and DIY panel projects](#5-existing-replica-and-diy-front-panel-projects)** — prior art; read before designing anything.
6. **[§6 Mechanical parts](#6-mechanical-parts-buttons-lens-caps-switches)** — buttons, lens caps, switches, rotary switches.
7. **[§7 Hercules emulator](#7-hercules-emulator-software-documentation-and-control-interfaces)** — software and the interfaces the Arduino will talk to.
8. **[§8 MVS references](#8-mvs-references-emphasis-on-mvs-turnkey)** — MVS 3.8j and the Turnkey distributions.
9. **[§9 Electronics](#9-electronics-arduino--raspberry-pi-leds-switches-usb)** — LED driving, switch scanning, USB serial.
10. **[§10 Laser cutting acrylic](#10-laser-cutting-acrylic-file-preparation-and-vendors)** — file prep and vendor requirements.
11. **[§11 Books](#11-books)**, **[§12 Magazines and trade press](#12-magazines-trade-press-and-periodical-archives)**, **[§13 YouTube](#13-youtube-channels-and-videos)**, **[§14 Blogs, forums, mailing lists and communities](#14-blogs-forums-mailing-lists-and-communities)**.
12. **[§15 Master reference index](#15-master-reference-index)** — every link in one flat table with a one-line description.
13. **[§16 Gaps in the public record](#16-gaps-in-the-public-record-what-you-will-have-to-originate)** — what nobody has published, so you know what you must originate.
14. **[§17 The IBM 3033 / 303X console](#17-the-ibm-3033--303x-console-lights-switches-buttons)** — what the 3033 operator interface actually is, and why it is *not* a lamp panel.
15. **[§18 IBM mainframe hardware timeline, 1952–2026](#18-ibm-mainframe-hardware-timeline-19522026)** — every generation with announce / withdrawal / end-of-service dates and supported operating systems.
16. **[§19 Link health and archive policy](#19-link-health-and-archive-policy)** — which of these links are dead, which are bot-blocked, and the Wayback replacement for each.
17. **[§20 Which panel best matches the signals Hercules can supply?](#20-which-panel-best-matches-the-signals-hercules-can-actually-supply)** — **the key engineering answer**, proved lamp-by-lamp from the /145 manual. If you read only one section, read this one and [§1](#1-design-decision-which-370-panel-to-replicate).

**Archive warning — verified 2026-08-01.** Every URL in this document was checked with an HTTP
request on that date. **Two important sites are completely offline:** `hercules-390.org` and
`wotho.ethz.ch/tk4-`. Several archives (Yahoo Groups via narkive) return 503, and one wiki is
permanently gone. Working replacements and Wayback Machine snapshots are given inline and
collected in **[§19](#19-link-health-and-archive-policy)**. Mirror anything you depend on
*locally* before you start designing.

---

## 1. Design decision: which /370 panel to replicate?

This matters more than any other choice, so it goes first.

- **MVS Turnkey (TK4- / TK5) *defaults* to reporting itself as an IBM 3033 — but that is one line
  of configuration, not a constraint.** Hercules' `CPUMODEL` statement is, in IBM's own
  documentation's words, "a purely cosmetic value only": it sets the 4-hex-digit machine type
  returned by the `STIDP` instruction and nothing else. **Hercules makes no attempt to emulate the
  behaviour or features of any particular CPU model.** Only `ARCHLVL` (S/370 vs ESA/390 vs
  z/Architecture) changes actual behaviour. So you can edit the Turnkey `.cnf` to say
  `CPUMODEL 0145` and MVS will report a 370/145 — with zero behavioural difference. See
  [§7.2](#72-operating-modes-and-external-control--this-is-the-critical-section-for-your-arduino-link).
  **Practical consequence: your choice of which panel to build is completely independent of what
  Hercules reports.** Build the /145 panel and set `CPUMODEL 0145`.
- **Do not replicate the 3033's own console.** The 3033's operator interface (the **3036 console**)
  is an L-shaped desk with two 3277 CRT workstations and service processors — a *display* console,
  **not** a lamp-and-roller panel. If you replicate a 3033 faithfully you get screens, not
  blinkenlights. Full detail in **[§17](#17-the-ibm-3033--303x-console-lights-switches-buttons)**.
- **Five /370 models have a hardware control panel: the /135, /145, /155, /165 and /168.**
  ⚠️ **Corrected:** the **/158** does **not** — per `SR20-4460`, "The Model 158 display console
  does not have LOAD UNIT dials or a LOAD key"; it IPLs by pointing a **light pen** at screen
  frames. The **/115 and /125** likewise use a "Display Operating Console". Do not build those three.
  (An earlier draft of this document wrongly grouped the /168 with the /158 — the /168 genuinely
  has LOAD UNIT switches, a LOAD key, ENABLE SYSTEM CLEAR, and MANUAL and LOAD lights.)
- **The /145 (3145) is the target — and it is the only defensible one.** It is the **only /370
  whose lamp banks actually display architected data** (storage contents, registers, and the next
  instruction address when stopped). On the /135 and /155 that data goes to the **printer-keyboard**
  instead; on the /165 it goes to a **CRT**. See
  [§20.8](#208-per-model-survey-which-370s-actually-have-a-lamp-panel) for the primary-source
  evidence. It is also by far the best documented model on Bitsavers.
- **The /165 panel is the most spectacular** (more rollers, far more lamps) but it is a hybrid:
  the lamps are status and microarchitecture, while general registers and storage are displayed on
  an attached CRT via MCAR/MCDR. Most of its extra lamps are undrivable.

**Honest caveat about signal fidelity:** Hercules is an *architecture* emulator, not a
*microarchitecture* emulator. It can give you PSW, instruction address, CPU state (running /
wait / manual / stopped), load light, interrupt/IPL state, register contents, device activity and
MIPS. It **cannot** give you the microcode-level, ALU-level and SDR/local-storage-level signals
that the real roller positions displayed — those come from the gate-level machine. Prior art that
solved this properly (Operation Blinkenlights, Lawrence Wilkinson's 360/30) had to build an
FPGA gate-level CPU. Plan your roller positions accordingly: some will be driven with real data,
some will be decorative or synthesised. See §5 and §7.

---

## 2. Panel artwork and pixel-accurate drawings (for laser cutting)

There is **no** publicly published, ready-to-cut DXF/SVG of a System/370 panel. What exists is
high-quality *illustration* work you can trace, plus primary manuals with dimensioned drawings.
Expect to redraw the panel yourself in Inkscape / KiCad / FreeCAD / QCAD from these.

| Reference | Content |
| --- | --- |
| [ibm360.com — S/360 Front Panels](https://www.ibm360.com/home/s360-front-panels) | The single best artwork source. Recreated, high-accuracy front panel illustrations for S/360 Models 20, 22, 25, 30, 40, 44, 50, 65, 67, 75, 85, 91/95/195 and the 9020 variants. Explicitly "recreated to have much more accurate detail" than earlier efforts. Licensed **CC BY-NC-SA 4.0** — note the **NonCommercial** clause. No download links published; images are embedded on the page, so contact the site owner (Chris Bigos) before deriving cutting files. |
| [ibm360.info — S/360 Front Panels](https://www.ibm360.info/home/s360-front-panels) | Same project under its `.info` domain. Also referenced as `files.ibm360.info`, a file server holding actual front panel **photographs** and scanned Field Engineering documents. Chris Bigos supplied the IBM 7201-02 FE manuals to the Operation Blinkenlights project (§5). |
| [John Savard — Quadibloc, "Front Panels" index](http://www.quadibloc.com/comp/panint.htm) | The original hand-drawn panel diagrams that inspired ibm360.com. Covers S/360 **and** S/370 models — including a diagram of the **System/370 Model 165** front panel. HTTP-only site (does not answer on HTTPS); open in a browser rather than a fetch tool. |
| [Quadibloc — The System/360 Saga Part II: Extending the Range](http://www.quadibloc.com/comp/pan05.htm) | Panel diagrams and commentary for the mid-range models. |
| [Quadibloc — The System/360 Saga Part III: The Case of the Bashful Computer](http://www.quadibloc.com/comp/pan06.htm) | Continues into the later models; contains the S/370 Model 165 panel diagram (lower half of the page's diagram). |
| [Ken Shirriff — "Iconic consoles of the IBM System/360 mainframes, 55 years old"](http://www.righto.com/2019/04/iconic-consoles-of-ibm-system360.html) | The best single explanatory article on how these panels are *organised*: what the roller (drum) displays are and how they let one row of lamps show several different functions; how many rollers each model had (Model 30 = 0, 40 = 2, 50 = 4, 65 = 6); flat silkscreened panels (Model 30) vs. individually-socketed bulbs (upper models); why the Model 75 has 64 data toggle switches. Many high-resolution photographs. Read this before drawing anything. |

**Practical approach for getting to a cut file:**
1. Pick the model (§1).
2. Pull the *dimensioned* drawings from the FE / Operating Procedures manuals (§3).
3. Pull the highest-resolution straight-on photographs you can find (§4) and rectify them
   (perspective-correct) in GIMP/Photoshop.
4. Trace to vector in Inkscape, cross-checking against the manual dimensions — the photo gives you
   proportions and the manual gives you absolute sizes.
5. Verify lamp pitch and pushbutton pitch against the 3D-printed button inserts in §6, whose
   dimensions were taken from real IBM parts (≈25.5 × 25.1 × 18.8 mm).

---

## 3. Primary IBM documentation (Bitsavers and friends)

Bitsavers is the authoritative free archive of scanned IBM manuals. Root for /370:
**<https://bitsavers.org/pdf/ibm/370/>** (mirrors: `bitsavers.trailing-edge.com`,
`bitsavers.informatik.uni-stuttgart.de`).

### 3.1 The two most important documents

| Reference | Content |
| --- | --- |
| [SR20-4460-0 — System/370 Operator's Reference Guide, Jul 1974](https://www.bitsavers.org/pdf/ibm/370/SR20-4460-0_System_370_Operators_Reference_Guide_Jul74.pdf) | **The definitive cross-model description of the /370 operator control panel.** Describes every switch, key, rotary control and indicator: LOAD, LOAD UNIT address rotary switches, SYSTEM RESET, PSW RESTART, INTERRUPT, STOP/START, RATE (PROCESS / INSN STEP), STORE/DISPLAY, ADDRESS COMPARE, IMPL, CHECK RESET, power controls, and the meaning of the MANUAL / WAIT / SYSTEM / LOAD / TEST indicators. This is the document that tells you *what each light and switch must do* in your replica. |
| [SR20-4460-2 — System/370 Operator's Reference Guide, Dec 1976](https://bitsavers.trailing-edge.com/pdf/ibm/370/SR20-4460-2_System_370_Operators_Reference_Guide_Dec76.pdf) | Later, larger (13 MB) revision of the above, covering more models. Use both — the later edition adds models, the earlier one is sometimes clearer on the early machines. |
| [Full text (OCR) of SR20-4460-0 on archive.org](https://archive.org/stream/bitsavers_ibm370SR20torsReferenceGuideJul74_5912360/SR20-4460-0_System_370_Operators_Reference_Guide_Jul74_djvu.txt) | Searchable plain-text version of the July 1974 guide — handy for grepping switch names and lamp labels when you are building the silkscreen legend list. |

### 3.2 Model 145 (3145) — recommended target

| Reference | Content |
| --- | --- |
| [GA24-3554-0 — System/370 Model 145 Operating Procedures, Sep 1970](https://www.bitsavers.org/pdf/ibm/370/model145/GA24-3554-0_370_Model_145_Operating_Procedures_Sep70.pdf) | Operator-level procedures with **console panel figures**: IPL procedure using the LOAD UNIT ADDRESS rotary switches (positions F, G, H), RATE switch settings including INSN STEP, display/store operations. 2.8 MB. |
| [GC38-0015-2 — 370/145 Operating Procedures, Sep 1972](https://bitsavers.org/pdf/ibm/370/model145/GC38-0015-2_370_145_Operating_Procedures_sep72.pdf) | Later revision, 5.4 MB. |
| [SY24-3581-1 — 3145 Processing Unit Theory–Maintenance, Oct 1971](https://bitsavers.org/pdf/ibm/370/fe/3145/SY24-3581-1_3145_Processing_Unit_Theory-Maintenance_Oct71.pdf) | **57 MB Field Engineering manual — the goldmine.** FE theory/maintenance manuals contain panel layout drawings, indicator assignments, lamp driver circuits and the wiring behind the console. This is where to look for exact lamp positions and what each lamp is wired to. |
| [SY24-3581-4 — 3145 Processor Theory Maintenance](https://bitsavers.org/pdf/ibm/370/fe/3145/SY24-3581-4_3145_Processor_Theory_Maintenance.pdf) | Later revision, 14 MB. |
| [S124-0129-2 — 3145 Processing Unit Parts Catalog, Oct 1975](https://bitsavers.org/pdf/ibm/370/fe/3145/S124-0129-2_3145_Processing_Unit_Parts_Catalog_Oct75.pdf) | **Exploded parts drawings with IBM part numbers**, 14 MB. Use this for the *physical* geometry of pushbutton assemblies, lamp holders, roller assemblies, bezels and the panel casting. Invaluable for a mechanically faithful replica. |
| [S229-2239-1 — 370/145 Reference Summary, Sep 1972](https://bitsavers.org/pdf/ibm/370/fe/3145/S229-2239-1_370-145_Reference_Summary_Sep72.pdf) | Condensed FE reference card set; quick lookup for panel indicators and console printer info. |
| [SR25-5608-0 — System/370 Model 145 Installation Instructions, Jul 1971](https://bitsavers.org/pdf/ibm/370/fe/3145/SR25-5608-0_System_370_Model_145_Installation_Instructions_Jul71.pdf) | Installation-level drawings; useful for enclosure proportions. |
| [GA24-3557-3 — 370 Model 145 Functional Characteristics, Aug 1972](https://bitsavers.org/pdf/ibm/370/funcChar/GA24-3557-3_IBM_370_Model_145_Functional_Characteristics_Aug72.pdf) | Architecture and machine behaviour; contains the "System Control Panel" section describing the operator control / operator intervention / customer engineer sections of the panel. |
| [GA24-3557-1 — 370/145 Functional Characteristics, Oct 1970](http://bitsavers.trailing-edge.com/pdf/ibm/370/funcChar/GA24-3557-1_370-145_funcChar_Oct70.pdf) | Earlier edition of the same. |
| [GC20-1734-2 — A Guide to the IBM System/370 Model 145, Aug 1972](https://www.bitsavers.org/pdf/ibm/370/systemGuide/GC20-1734-2_370-145_Guide_Aug72.pdf) | Marketing/overview guide with system photographs including the console. |
| [G520-2398-2 — 370/145 Facts Folder, Aug 1972](http://bitsavers.informatik.uni-stuttgart.de/pdf/ibm/370/facts_folder/G520-2398-2_370-145_Facts_Folder_197208.pdf) | Short glossy sales folder — good clean product photography. |
| [IBM 370/145 Product Announcement (ed-thelen.org)](https://ed-thelen.org/comp-hist/IBM-ProdAnn/370-145.pdf) | Original announcement material with photos. |

### 3.3 Models 155 / 158 / 165 / 168 (larger panels)

| Reference | Content |
| --- | --- |
| [GA22-6942-1 — System/370 Model 155 Functional Characteristics, Jan 1971](http://www.bitsavers.org/pdf/ibm/370/funcChar/GA22-6942-1_370-155_funcChar_Jan71.pdf) | Contains the **System Control Panel** chapter: commonly used indicators, switches and keys, split into operator control and operator intervention sections. The /155 panel is the archetypal big /370 panel. |
| [Same document, alternate mirror (sharktastica.co.uk)](https://sharktastica.co.uk/resources/docs/pdf/IBM_GA22-6942-1_3155-func-chars_1971_bitsavers.pdf) | Mirror in case Bitsavers is slow. |
| [GC20-1754-2 — A Guide to the System/370 Model 158, 3rd ed., Aug 1975](https://bitsavers.org/pdf/ibm/370/model158/GC20-1754-2_A_Guide_to_the_System_370_Model_158_3rd_ed_197508.pdf) | 8.4 MB overview guide with console photography for the /158. |
| [GC20-1730-0 — A Guide to the IBM System/370 (Model 165), Nov 1970](https://bitsavers.org/pdf/ibm/370/systemGuide/GC20-1730-0_370-165_Guide_Nov70.pdf) | Model 165 guide — the /165 has the largest, most impressive panel of the early /370 line. |
| [SY33-1059-1 — 3125 Processing Unit General Information, Oct 1973](https://bitsavers.org/pdf/ibm/370/fe/3125/SY33-1059-1_3125_Processing_Unit_General_Information_Oct73.pdf) | FE manual for the smaller 3125; useful as a comparison of how IBM documented console assemblies. |

### 3.4 Architecture and physical planning

| Reference | Content |
| --- | --- |
| [GA22-7000-0 — IBM System/370 Principles of Operation, Jun 1970](https://www.bitsavers.org/pdf/ibm/370/princOps/GA22-7000-0_370_Principles_Of_Operation_Jun70.pdf) | The architecture bible. Chapter on **"Operator Facilities"** defines, at architecture level, the manual controls every /370 must have: system reset, initial program load, alter/display, rate control, address compare, plus the *architected* meaning of the wait, manual, system, test and load indicators. If you want your panel to behave correctly rather than merely look correct, this is mandatory reading. |
| [GX20-1850-7 — System/370 Reference Summary ("green card"), Feb 1989](http://www.bitsavers.org/pdf/ibm/370/referenceCard/GX20-1850-7_System_370_Reference_Summary_Feb89.pdf) | The famous fold-out reference card: PSW format, instruction formats, condition codes. You will want the PSW bit layout when deciding which LEDs display which PSW field. |
| [GC22-7004-14 — System/370 Installation Manual — Physical Planning, Jun 1985](https://bitsavers.trailing-edge.com/pdf/ibm/370/fe/GC22-7004-14_370_Installation_Manual_Physical_Planning_Jun85.pdf) | **Dimensioned floor-plan and cabinet drawings** for /370 units, including the 3145. Use for overall enclosure proportions if you build a cabinet around the acrylic panel. |
| [Mark Smotherman — "The IBM 360/370 Architecture for Mainframe Computers" (Appendix F, CPSC 464)](https://mark.people.clemson.edu/464/appF.pdf) | Concise academic summary of the 360/370 architecture — a fast way to get oriented before tackling Principles of Operation. |
| [Mark Smotherman — Computer Architecture History index](https://mark.people.clemson.edu/hist.html) | Large curated collection of IBM mainframe architecture history pages (ACS, Future System, Model 91, I/O history). Good background and further citations. |
| [Wikipedia — IBM System/370](https://en.wikipedia.org/wiki/IBM_System/370) | Orientation and model-by-model links. |
| [Wikipedia — IBM System/370 Model 145](https://en.wikipedia.org/wiki/IBM_System/370_Model_145) · [Model 148](https://en.wikipedia.org/wiki/IBM_System/370_Model_148) · [Model 155](https://en.wikipedia.org/wiki/IBM_System/370_Model_155) · [Model 165](https://en.wikipedia.org/wiki/IBM_System/370_Model_165) · [Model 168](https://en.wikipedia.org/wiki/IBM_System/370_Model_168) · [Model 115](https://en.wikipedia.org/wiki/IBM_System/370_Model_115) · [Model 135](https://en.wikipedia.org/wiki/IBM_System/370_Model_135) | Per-model specs, dates and console photographs. The /145 was the first IBM machine with semiconductor main memory. **Note:** there is **no** `IBM_System/370_Model_158` article (verified 404 on 2026-08-01) — the /158 is covered inside the main [IBM System/370](https://en.wikipedia.org/wiki/IBM_System/370) article and, in far more depth, in the Bitsavers [/158 guide](https://bitsavers.org/pdf/ibm/370/model158/GC20-1754-2_A_Guide_to_the_System_370_Model_158_3rd_ed_197508.pdf) listed in §3.3. |
| [Wikipedia — Green card (IBM/360)](https://en.wikipedia.org/wiki/Green_card_(IBM/360)) | History of the reference card; useful if you want a period-correct accessory. |

---

## 4. Photographs, museums and archives

| Reference | Content |
| --- | --- |
| [Wikimedia Commons — Category:IBM System/370](https://commons.wikimedia.org/wiki/Category:IBM_System/370) | Freely licensed photographs and document scans of /370 hardware. Check licences, but these are the safest images to work from legally. |
| [Wikimedia Commons — Category:IBM System/360 Model 30](https://commons.wikimedia.org/wiki/Category:IBM_System/360_Model_30) | Comparable /360 console imagery. |
| [Computing History (UK) — IBM System 370 Control Panel](https://www.computinghistory.org.uk/det/31058/IBM-System-370-Control-Panel/) | Museum catalogue entry for a surviving physical /370 control panel — photographs of the real object. |
| [Rhode Island Computer Museum — IBM 370 Front Panel](https://www.ricomputermuseum.org/collections-gallery/interesting_computer_items/ibm-370-panel) | RICM holds an IBM 370 front panel in its "Interesting Items" collection. The page is navigation-heavy; contact the museum directly — museums holding a physical panel are the best possible source for accurate measurements. |
| [Computer History Museum — IBM System/370 Model 158 (cat. 102646258)](https://www.computerhistory.org/collections/catalog/102646258) | CHM catalogue entry: Model 158 promotional brochure with console photographs. |
| [Computer History Museum — 370 Model 145 Functional Characteristics (cat. 102665279)](https://www.computerhistory.org/collections/catalog/102665279) | CHM catalogue record for the /145 functional characteristics manual. |
| [Ed Thelen — IBM System 360 Model 30](https://ed-thelen.org/comp-hist/ibm-360-30.html) | Long-running vintage computing site with detailed /360 machine pages and photographs. |
| [Stanford InfoLab — IBM 360 display and Stanford Big Iron](http://infolab.stanford.edu/pub/voy/museum/pictures/display/3-1.htm) | Historic photographs of a /360 installation. |
| [Flickr — `ibm360` tag](https://www.flickr.com/photos/tags/ibm360/) | Community photographs; several straight-on, high-resolution console shots suitable for tracing. |
| [Flickr — Lawrence Wilkinson, "IBM System 360/30 on FPGA"](https://www.flickr.com/photos/carrierdetect/4718559358) | Photographs from the 360/30 FPGA project including its panel recreation. |
| [Wikimedia Commons — File:IBM system 360.JPG](https://commons.wikimedia.org/wiki/File:IBM_system_360.JPG) | Freely licensed /360 system photograph. |
| [Wikimedia Commons — File:System 370 Reference Summary.jpg](https://commons.wikimedia.org/wiki/File:System_370_Reference_Summary.jpg) | Scan of the /370 reference summary card. |
| [Hacker News — "Control Panel Of IBM 360 Mainframe"](https://news.ycombinator.com/item?id=3196037) | Discussion thread with additional photo links and first-hand operator recollections about what the lights actually did. |

---

## 5. Existing replica and DIY front panel projects

**Read this section before you design anything.** These are people who have already solved most
of your problems.

### 5.1 Operation Blinkenlights — the closest prior art to your project

| Reference | Content |
| --- | --- |
| [Operation Blinkenlights (blog)](http://ibm360-console.blogspot.com/) | **The single most relevant project in existence.** A real IBM System/360 Model 65 console panel (235 indicator lamps, toggle switches, pushbuttons, rotary controls, potentiometers) restored and driven from a **modified Hercules emulator**. Documents the whole journey chronologically from November 2011. |
| [Operation Blinkenlights — January 2012 archive](http://ibm360-console.blogspot.com/2012_01_01_archive.html) | The electronics phase: initially a **Velleman K8061 USB interface** feeding **74HC595 (output) and 74HC597 (input) shift register** chains handling **183 digital inputs, 237 digital outputs, 5 analog inputs, 1 analog output**; incandescent bulbs replaced with orange LEDs in modified plastic casings. Later migrated to an **Arduino Mega 2560 + Ethernet shield**, which cut panel response time from ~1 second to ~1 millisecond. *This is directly transferable to your Arduino design — including the warning that a naive USB approach is far too slow.* |
| [Operation Blinkenlights — "Emulator goes hardware"](https://ibm360-console.blogspot.com/2012/04/emulator-goes-hardware.html) | Why they moved from software emulation to a **Xilinx XUPV5-LX110T FPGA**: Hercules alone cannot produce the microarchitectural signals the panel's rollers display. Custom PCB with SparkFun 4-way level shifters, 50-pin ribbon cable and HD50 connector to the panel. |
| [Operation Blinkenlights — "Source code of FPGA implementation"](http://ibm360-console.blogspot.com/2012/04/source-code-of-fpga-implementation.html) | Release of `pcie360_0_1_20120413.zip` — VHDL implementation, incomplete but functional for elementary console operations. |
| [VAXBARN — Operation Blinkenlights project page](https://vaxbarn.com/projects/ibm-360-panel) | **Live.** The hosting collector's project page for the same effort, with additional photographs and status. |
| ~~`vaxbarn.com/component/content/article/390-ibm-360-65`~~ — **404 (site restructured).** Start from the live [VAXBARN home](https://vaxbarn.com/) or the [Wayback index for this host](https://web.archive.org/web/*/vaxbarn.com/*) | Background on the Model 65 hardware behind the panel. |
| ~~`vaxbarn.com/cat/360`~~ — **404.** Use the [Wayback snapshot, 2025-11-19](http://web.archive.org/web/20251119204040/https://vaxbarn.com/cat/360) | All the site's IBM 360 material, as it stood in November 2025. |
| ~~`http://ibm360-console.wikispaces.com/`~~ — **permanently dead** (Wikispaces shut down in 2018) and, critically, **the Internet Archive has essentially nothing**: a CDX query returns only a 302 on the root, `favicon.ico`, `robots.txt` and one **402-paywalled** file entry (`7201 Control Field Listings.pdf`). [CDX query for yourself](http://web.archive.org/cdx/search/cdx?url=ibm360-console.wikispaces.com*&output=text&fl=timestamp,original,statuscode&collapse=urlkey) | The project's wiki, which held the microarchitecture documentation and the **modified Hercules source code**. **This material appears to be lost.** If you want it, ask on the [Hercules groups.io list](https://groups.io/g/hercules-390) or contact the [VAXBARN](https://vaxbarn.com/projects/ibm-360-panel) owner directly — do not assume the Wayback Machine has it. |

### 5.2 Using a real S/360 or S/370 panel with Hercules — the mailing-list thread

| Reference | Content |
| --- | --- |
| [hercules-390 list — "Using an IBM S/360 or S/370 Operator Panel as a Hardware Interface to the Hercules Emulator"](https://hercules-390.yahoogroups.narkive.com/0TRePf7v/using-an-ibm-s-360-or-s-370-operator-panel-as-a-hardware-interface-to-the-hercules-emulator) — **narkive returned HTTP 503 on 2026-08-01, and the Internet Archive has *no* snapshot of this specific thread.** Fallbacks: retry narkive later (503 is transient overload, not deletion); browse the [Wayback index of the whole narkive host](https://web.archive.org/web/*/hercules-390.yahoogroups.narkive.com/*), which *does* hold hundreds of other threads from 2021–2024; or re-ask on the live [groups.io/g/hercules-390](https://groups.io/g/hercules-390) | Hercules mailing-list thread on exactly your question — someone interfacing a System 360/65 to Hercules to control it like HercGUI does. Core advice from the Hercules developers: you need a driver for each lamp, and the practical route is to **take the information Hercules already publishes (the same data HercGUI consumes) and use it to drive custom hardware**. |

### 5.3 The PiDP family — the model for how to build and sell a replica panel

Oscar Vermeulen's PiDP kits are the best-executed Raspberry-Pi-plus-replica-panel projects in
existence. Even though they are DEC rather than IBM, the **construction technique, panel
lamination method, multiplexing scheme and business model are all directly applicable.**

| Reference | Content |
| --- | --- |
| [PiDP-11 building instructions (obsolescence.dev)](https://obsolescence.dev/pidp-11-building-instructions.html) | Full build guide for the PDP-11/70 replica. |
| [PiDP-11 Technical Details](https://obsolescence.wixsite.com/obsolescence/pidp-11-technical-details) | **The electrical design you should copy.** Multiplexing: 6 `ledRow` pins supply + to each row of 12 LEDs, 12 `column` pins drive the cathodes, 3 `row` pins sink the switch matrix and are flipped to input-with-pullup for scanning. Rows cycle ~60 Hz so the eye sees the whole panel lit. A **UDN2981** high-side driver buffers the row pins because the Pi GPIO cannot supply the current. **390 Ω** resistors limit LED current; **1 kΩ** resistors limit current during switch sensing. PCB designed in **KiCad** with freerouter. |
| [PiDP-10 Technical Details](https://obsolescence.wixsite.com/obsolescence/pidp-10-technical-details) | Same approach scaled up to the PDP-10 panel, which has far more lamps — closer to your /370 lamp count. |
| [PiDP-11 User Manual (PDF)](https://obsolescence.dev/pidp11/PiDP-11_Manual.pdf) | Complete manual: assembly, wiring, software, troubleshooting. **Live.** |
| ~~`http://pidp.net/pidp11/PiDP-11_Manual.odt`~~ (the editable ODT source referenced from the technical-details page) — **returns HTTP 406.** Use the [Wayback snapshot, 2024-11-09](http://web.archive.org/web/20241109013654/https://pidp.net/pidp11/PiDP-11_Manual.odt) | The manual in editable OpenDocument form — useful if you want to fork the document structure for your own build guide. |
| [PiDP-11 on Hackaday.io](https://hackaday.io/project/8069-pidp-11) | Project log with design iterations and photographs. |
| [PiDP-11 build logs (Hackaday.io, page 2)](https://hackaday.io/project/8069/logs?sort=newest&page=2) | Earlier logs covering panel artwork and manufacturing decisions. |
| [Hackster.io — "PiDP-11: A Pi-Based Replica of the PDP-11/70"](https://www.hackster.io/obsolescence/pidp-11-a-pi-based-replica-of-the-pdp-11-70-1dcda9) | Project overview and parts list. |
| [Kieran Healy — "Building a PDP-11/70 Kit"](https://kieranhealy.org/blog/archives/2021/10/09/building-a-pdp-11/70-kit/) | Independent build write-up with excellent photographs of the finished acrylic panel — good reference for what a well-made replica panel looks like up close. |
| [Lanny Cox — "Building the PiDP-8"](https://lannycox.com/2020/04/22/building-the-pidp-8/) | Another independent build log. |
| [Google Group `pidp-11` — "Show us your kits"](https://groups.google.com/g/pidp-11/c/E-RMRVQ15NQ/m/3S6ln4ANEwAJ) | Gallery thread of completed builds — many variations on panel finishing and lighting. |
| [Google Group `pidp-8` — PIDP-11 thread](https://groups.google.com/g/pidp-8/c/uFkciMFuHHg) | Community discussion of panel construction. |
| [Makery — "Raspberry Pi replica of the legendary 1960s PDP-8"](https://www.makery.info/en/2015/04/06/une-replique-raspberry-pi-du-mythique-pdp-8-des-annees-60/) | Press coverage of the PiDP-8, explaining the concept and reception. |
| [Hackaday — SIMH tag](https://hackaday.com/tag/simh/) | Rolling coverage of simulator-plus-panel projects. |

**Key manufacturing insight from the PiDP-11:** the panel is made by **laminating a polycarbonate
sheet to an acrylic panel, with the silkscreen graphics sandwiched between them**, then laser
cutting the switch openings through the assembly. The graphics being in the middle stops them
fading or being scratched off. Design files were produced by **tracing original artwork from a real
PDP-11/40 panel**. Adopt this method.

### 5.4 BlinkenBone — a general framework for driving real panels from simulators

| Reference | Content |
| --- | --- |
| [BlinkenBone on GitHub (j-hoppe/BlinkenBone)](https://github.com/j-hoppe/BlinkenBone) | Jörg Hoppe's architecture for connecting simulators of vintage computers to "Blinkenlight panels" — either real physical panels fitted with modern micro-Linux controllers, or photorealistic Java panel simulations. **The client/server protocol design is worth stealing even though the target is SimH/DEC rather than Hercules/IBM.** |
| [BlinkenBone — gpio.c (PDP-15 blinkenlight server)](https://github.com/j-hoppe/BlinkenBone/blob/master/projects/07.3_blinkenlight_server_pdp15/gpio.c) | Concrete, readable example of a GPIO-level panel server: multiplexing, timing, switch scanning. |
| [BlinkenBone releases](https://github.com/j-hoppe/BlinkenBone/releases) | Prebuilt distributions. |
| [retrocmp.com — BlinkenBone project root](http://www.retrocmp.com/projects/blinkenbone) | Main documentation hub. |
| [retrocmp.com — download and run simulated panels](https://www.retrocmp.com/projects/blinkenbone/176-blinkenbone-download-and-run-simulated-panels-for-free) | Runnable "distributions" bundling SimH, disk images, PDF docs, the Java panel and startup scripts. Useful as a model for how to ship your own project. |
| [retrocmp.com — UniBone / BlinkenBone Panels](https://www.retrocmp.com/projects/unibone/354-unibone-blinkenbone-panels) | Hardware for driving real panels (BeagleBone Black + BlinkenCape + BlinkenBoard). |
| [classiccmp cctalk — "Photorealistic frontpanels for DEC PDP simulations under SimH"](https://classiccmp.org/pipermail/cctalk/2018-March/038873.html) | Announcement and discussion. |
| [alt.folklore.computers — "Simulated PDP-11 Blinkenlight front panel for SimH"](https://groups.google.com/g/alt.folklore.computers/c/VIw6tJKZx_c) | Original discussion thread. |
| [simh mailing list — "Frontpanels"](https://www.mail-archive.com/simh@trailing-edge.com/msg07173.html) | Design discussion on simulator front-panel APIs — the same problem you face with Hercules. |

### 5.5 Gate-level IBM recreations (if you want real microarchitecture signals)

| Reference | Content |
| --- | --- |
| [Lawrence Wilkinson — IBM 360/30 Saga](https://www.ljw.me.uk/ibm360/Saga.html) | The story of building a gate-level IBM System/360 Model 30 in VHDL, transcribed **directly from the gate designs in IBM service manuals using the exact same signal names**, plus rebuilding and hand-debugging the microcode from printed listings. Includes a VGA output that exactly mimics the Model 30 front panel, down to microcode-state indicator lights. This is the reference for anyone who wants panel lights that are genuinely correct. |
| [Lawrence Wilkinson — IBM System 360 Model 30 VHDL files](https://www.ljw.me.uk/ibm360/vhdl/) | The complete VHDL source, plus compiled bitstreams for the Digilent Spartan-3 board and a newer Digilent Zybo Z7-20 version. |
| [Adafruit blog — "Obtaining an IBM System/360 Front Panel"](https://blog.adafruit.com/2019/06/28/obtaining-an-ibm-system-360-front-panel-vintagecomputing-retrocomputing-ibm/) | Coverage of CuriousMarc acquiring a real /360 Model 50 panel — with photographs and links. Notes that replicas exist for the IMSAI 8080 and PDP-11 but the IBM 360 has yet to get the same treatment. *That gap is your project.* |
| [Hackaday — System/360 tag](https://hackaday.com/tag/system-360/) | Rolling coverage of /360 panel and restoration projects. |
| [Hackaday — Mainframe tag](https://hackaday.com/tag/mainframe/page/2/) | Broader mainframe project coverage. |
| [altair-duino group — "IBM System/360 or 370 Front Panel?"](https://groups.google.com/g/altair-duino/c/D1k26Spm6zE) | Discussion in the Altair-Duino community (a successful Arduino-driven replica panel product) about doing the same for an IBM panel. Relevant because the Altair-Duino is *literally* an Arduino driving a replica front panel — study its architecture. |
| [Whirlpool forums — "IBM s360 still lives — 50 years on"](https://forums.whirlpool.net.au/archive/2245918) | Long enthusiast thread with links to emulation and panel projects. |

---

## 6. Mechanical parts: buttons, lens caps, switches

| Reference | Content |
| --- | --- |
| [Printables — "IBM System/360 and /370 mainframe computer console pushbutton insert" by 1944GPW](https://www.printables.com/model/165377-ibm-system360-and-370-mainframe-computer-console-p) — *returns 403 to scripts (Cloudflare bot protection) but **works normally in a browser**; if it ever does go down, the [Wayback snapshot, 2024-08-13](http://web.archive.org/web/20240813122756/https://www.printables.com/model/165377-ibm-system360-and-370-mainframe-computer-console-p) has the page* | **3D-printable replicas of the actual IBM console pushbutton inserts.** 16 STL files: START, STOP, LOAD, DISPLAY, RESET, SYSTEM RESET, CHECK RESET, LOG OUT, PSW RESTART, STORE, POWER ON, POWER OFF, INTERRUPT, a blank insert, and a curved sanding block for finishing. Individual inserts ≈ **25.5 × 25.1 × 18.8 mm** — use this as your authoritative pushbutton pitch. Includes a **parametric OpenSCAD script** so you can change legends and fonts. Tested in PLA (excellent) and ABS (good, may need scaling). 100 % infill recommended for translucent variants. Licensed **CC BY**. Originally posted to Thingiverse, December 2017. |
| [Cults3D — same model, mirror](https://cults3d.com/en/3d-model/gadget/ibm-system-360-and-370-mainframe-computer-console-pushbutton-insert) | Alternate download host with the same description and finishing instructions (sanding, painting the text, polishing). |

For the rest of the mechanical bill of materials, work from the **3145 Parts Catalog**
(§3.2) — it gives IBM part numbers and exploded views for lamp holders, roller assemblies,
toggle switches and rotary switches, which you can then match to modern equivalents.

---

## 7. Hercules emulator: software, documentation and control interfaces

### 7.1 The emulator itself

| Reference | Content |
| --- | --- |
| ~~`http://www.hercules-390.org/`~~ — **OFFLINE as of 2026-08-01** (connection fails on every variant). Use [the Wayback snapshot, 2026-05-02](http://web.archive.org/web/20260502060042/http://www.hercules-390.org/) | The original project site. It is *gone*, not merely slow — every link you find pointing at `hercules-390.org` needs a replacement. The live successors are the two GitHub-hosted resources below. |
| [**`github.com/hercules-390/hyperion`** — the original Hercules 4.0 "Hyperion" repository](https://github.com/hercules-390/hyperion) | **Live (verified 2026-08-01).** The original project's own repo, 8 871 commits, 293 stars, licensed under the **Q Public Licence**, OSI-certified open source. Its README calls Hyperion "the official development version of the Hercules emulator", containing "the latest bleeding edge changes". This is the upstream lineage of the emulator; the SDL repo below is the fork that most people build today. Also the place to read the `EXTERNALGUI` code path (see issue [#150](https://github.com/hercules-390/hyperion/issues/150)). |
| [**`hercules-390.github.io/html/`** — the Hercules 4.0 documentation set](https://hercules-390.github.io/html/) | **Live (verified 2026-08-01).** The GitHub-hosted replacement for the dead `hercules-390.org` documentation. How-to style with worked examples. Chapters: **Hercules Operation** (command-line parameters, **panel commands**, keyboard use, and the **Hercules Automatic Operator**), **Configuration File** (system config and I/O device definition — see [hercconf.html](https://hercules-390.github.io/html/hercconf.html)), Creating Emulated DASD, Compressed DASD Files, System Messages, FAQ, **Telnet/tn3270 Console How-To**, TCP/IP networking, Hercules-REXX integration, Shared Device Server, Technical Support. It also links the downloadable V4.00 PDF manual set on `hercdoc.glanzmann.org`. **Note:** this set does *not* document an external-GUI wire protocol or an HTTP API — confirming that the protocol lives only in the source. |
| [SDL Hercules 4.x "Hyperion" on GitHub](https://github.com/SDL-Hercules-390/hyperion) | **The actively maintained fork — build this one.** Full source; builds cleanly on Raspberry Pi OS. |
| [Hyperion README](https://github.com/sdl-hercules-390/hyperion/blob/master/README.md) | Build instructions, feature summary, platform notes. |
| [SDL Hercules HTML documentation](https://sdl-hercules-390.github.io/html/) | The SDL fork's documentation set. |
| [Wikipedia — Hercules (emulator)](https://en.wikipedia.org/wiki/Hercules_(emulator)) | Overview, history, licensing (QPL), and which IBM architectures are emulated. |
| [Michael Dickinson — "Obtaining the Hercules emulator, so many options"](https://mdickinson.dyndns.org/hercules/obtaining.php) | Clear comparison of the several Hercules forks and builds (Hercules 3.x, SDL Hyperion 4.x, Hercules-390 variants) and which to pick. Read before you `git clone` anything. |

### 7.2 Operating modes and external control — *this is the critical section for your Arduino link*

| Reference | Content |
| --- | --- |
| [Hercules: Installation and Operation](https://sdl-hercules-390.github.io/html/hercinst.html) | **The key document.** Documents the three operating modes and their flags: **Panel mode** (default, `hercules`), **command-line mode** (`herclin`), and **NoUI/daemon mode** (`--NoUI` / `-n`, replacing the deprecated `--daemon`). Crucially it documents `--externalgui` / `-e`, which "indicates Hercules is to be controlled by an External GUI". Also documents `-f/--config`, `-o/--output` (logfile), `-r/--rcfile` (run-commands file executed at startup), `-v/--verbose`, the `http` command for the built-in HTTP server, the `sh` panel command, and the **HAO (Hercules Automatic Operator)** facility. |
| [README.DAEMON.md (Hyperion)](https://github.com/SDL-Hercules-390/hyperion/blob/master/readme/README.DAEMON.md) | Explains "No-UI" mode in detail — how to run Hercules headless with stdin from `/dev/null` and all output to a logfile, and it stresses that **you must supply some other means of issuing commands**. Recommends the built-in HTTP server via `HTTP PORT`, `HTTP ROOT`, `HTTP START` configuration statements, reachable at e.g. `http://127.0.0.1:8181`, through which you can view registers, device information and issue commands. |
| [Hercules: Configuration File](https://sdl-hercules-390.github.io/html/hercconf.html) — also at [hercules-390.github.io/html/hercconf.html](https://hercules-390.github.io/html/hercconf.html) | **Settles the "3033 vs 370/145" question.** Documents `ARCHLVL` (formerly `ARCHMODE`) — S/370, ESA/390, ESAME, z/Architecture — which is the **only** statement here that changes behaviour. `CPUMODEL` takes a 4-hex-digit machine type stored by `STIDP`, and the manual states outright that Hercules "makes no attempt to emulate all aspects of, or features of, a given CPU model. The CPUMODEL statement defines a purely cosmetic value only." `CPUSERIAL` (6 hex digits, default `000001`) and `CPUVERID` (2 hex digits) likewise only feed `STIDP`; `MODEL`, `PLANT` and `MANUFACTURER` (defaults `EMULATOR`, `ZZ`, `HRC`) only feed `STSI`. **Change `CPUMODEL` freely — the emulation is identical.** |
| [Hercules User Reference Guide (PDF, v3.12)](https://hercdoc.glanzmann.org/V312/HerculesUserReference.pdf) | The full command reference. Contains the panel commands you will map to physical buttons: `ipl` / `iplc` (IPL normal / IPL clear from device `xxxx`), `sysreset` (SYSTEM RESET manual operation), `sysclear` (SYSTEM CLEAR RESET), `restart` (PSW restart), `start`, `stop`, `store`, and the display commands `psw`, `gpr`, `fpr`, `cr`, `ar`, `pr`, plus real/virtual storage display and alter. **This is your button-to-command mapping table.** |
| [Hercules User Reference Guide (v3.06)](https://hercdoc.glanzmann.org/V306/HerculesUserReference.pdf) · [(v3.05)](https://hercdoc.glanzmann.org/V305/HerculesUserReference.pdf) · [(v3.08)](https://hercdoc.glanzmann.org/V308/HerculesUserReference.pdf) | Thomas Glanzmann's archive of every version of the reference guide — useful when a command's behaviour changed between releases. |
| [Hercules User Reference Guide (hercules-390.org PDF)](http://www.hercules-390.org/HerculesUserReference.pdf) | Original-site copy of the same. |
| [Hercules console commands grouped by functionality (manualzz)](https://manualzz.com/doc/o/kscmd/hercules-user-reference-guide---the-hercules-system-370--esa-hercules-console-commands--grouped-by-functionality-) | Browsable HTML rendering of the command list, grouped by function — convenient while designing the panel mapping. |
| [Hercules Version 2: Installation and Operation (BSP GmbH mirror)](https://bsp-gmbh.pocnet.net/turnkey/cookbook/hercules/hercinst.html) | Older but well-written installation/operation document, hosted alongside the Turnkey cookbook. |
| [README.HDL.md — Hercules Dynamic Loader](https://github.com/SDL-Hercules-390/hyperion/blob/master/readme/README.HDL.md) | How to write **loadable modules** for Hercules. If you want the cleanest integration — a module that pushes panel state to the Arduino from inside Hercules rather than scraping output — this is the mechanism. |
| [README.EXTPKG.md — external packages](https://github.com/sdl-hercules-390/hyperion/blob/master/readme/README.EXTPKG.md) | How Hyperion consumes external packages (SoftFloat, decNumber, telnet, crypto). Relevant if you build a custom Hercules. |
| [README.S37X.md — S/370 extensions](https://github.com/sdl-hercules-390/hyperion/blob/master/readme/README.S37X.md) | S/370 instruction extension support. |
| [README.HERCLOGO.md](https://github.com/SDL-Hercules-390/hyperion/blob/master/readme/README.HERCLOGO.md) | Customising the 3270 logo screen — cosmetic, but part of making the whole thing feel period-correct. |
| [hercules-390 issue #150 — `"extgui" not declared in logmsg.c`](https://github.com/hercules-390/hyperion/issues/150) | Bug report that incidentally shows where the `EXTERNALGUI` / `extgui` conditional compilation lives in the source. **A useful entry point for reading the external-GUI code path yourself** — the protocol is defined in the source, not in a published spec. |
| [hercules-390 list — "Hercules Console commands via command line"](https://hercules-390.yahoogroups.narkive.com/clmlCchf/hercules-console-commands-via-command-line) | Mailing-list thread on driving Hercules commands programmatically from outside. |

**Practical note on the Pi↔Hercules link:** there is no formally published external-GUI protocol
document. Your realistic options, in increasing order of effort and fidelity:
(a) poll the **built-in HTTP server**; (b) drive `herclin` / a command pipe and parse the message
stream; (c) run with `--externalgui` and consume the tagged status lines that HercGUI consumes
(read the `EXTERNALGUI`-guarded code in Hyperion to learn the format); (d) write an **HDL module**
that publishes panel state directly. Option (d) is the clean one, and matches what Operation
Blinkenlights did by patching Hercules.

### 7.3 Existing Hercules GUIs — study these, they already solve "get panel data out"

| Reference | Content |
| --- | --- |
| [HercGUI (softdevlabs.com)](http://www.softdevlabs.com/hercgui.html) | "Fish's" Windows GUI for Hercules — the original consumer of the external-GUI interface. It displays exactly the data a physical panel needs: PSW, registers, CPU state, load/wait indicators, MIPS, device status. Note the site is HTTP-only. |
| [Jason — graphical front end to Hercules](http://ollydbg.de/Jason/index.htm) | A Java front end giving a view of the virtual devices attached to the emulator. Operation Blinkenlights used Jason on an LCD panel *beside* the real console panel to show the rest of the /360 environment — a pattern worth copying (physical panel for CPU state, small LCD for devices). |
| [HerculesStudio manual page](https://www.systutorials.com/docs/linux/man/1-HerculesStudio/) | Qt-based cross-platform Hercules GUI; its source is a good example of parsing Hercules output on Linux. |
| [hrdplex-gui (GitHub, haynieresearch)](https://github.com/haynieresearch/hrdplex-gui) | Another GUI front end to Hercules — a further worked example of the same integration problem. |
| [Hercules WinGUI FAQ (Volker Bandke, moshix mirror)](https://moshix.dynu.net/bandke/hercules/wingui/hercgui-faq.html) | FAQ covering how the Windows GUI talks to Hercules and what it can and cannot show. |

---

## 8. MVS references (emphasis on MVS Turnkey)

MVS 3.8j is the last release of OS/VS2 MVS placed in the public domain, which is why every hobby
mainframe runs it. A "**Turnkey**" (Tur(n)key) system is a prepackaged, pre-generated MVS 3.8j with
Hercules, DASD volumes, configuration and a large body of add-on software already installed — so
you IPL and you are running, instead of spending weeks doing a SYSGEN.

### 8.1 Turnkey distributions — the main line of descent

**TK3 (Volker Bandke) → TK4- (Jürgen Winkelmann) → TK5 (Rob Prins).**

| Reference | Content |
| --- | --- |
| [**MVS Tur(n)key 5 — Rob Prins (prince-webdesign.nl/tk5)**](https://www.prince-webdesign.nl/tk5) | **The current recommended distribution.** MVS 3.8j Turnkey 5, "fully restructured but still based upon TK3, TK4- and TK4ROB". Reduced to **15 DASD volumes** (down from 28 in TK4-), ready to run in minutes on Windows, Linux or macOS, with a large set of utilities and bonus MVS programs. This is what you should install on the Raspberry Pi. |
| [TK5 Introduction and User Manual (PDF)](https://www.prince-webdesign.nl/images/downloads/TK5-Introduction-and-User-Manual.pdf) | The official TK5 manual: installation, starting and stopping the system, logging on, the supplied subsystems and utilities, and how the Hercules configuration is laid out. **Read this to learn which Hercules config file you will be modifying for your panel integration.** |
| [Prince Webdesign — "An update on MVS Turnkey 4"](https://www.prince-webdesign.nl/index.php/software/update-on-mvs-turnkey-4) | Rob Prins's TK4ROB work — the bridge between TK4- and TK5, explaining what changed and why. |
| ~~`https://wotho.ethz.ch/tk4-/`~~ — **OFFLINE as of 2026-08-01.** Use the **live mirror → [`https://wotho.pebble-beach.ch/tk4-/`](https://wotho.pebble-beach.ch/tk4-/)** (verified 200), or the [Wayback snapshot, 2023-03-23](http://web.archive.org/web/20230323192244/https://wotho.ethz.ch/tk4-/) | **MVS 3.8j Tur(n)key TK4- by Jürgen Winkelmann (ETH Zürich)** — the previous long-standing standard, still very widely used and very well documented. MVS 3.8j on an emulated **IBM 3033** under Hercules. The ETH Zürich home has gone offline; the `pebble-beach.ch` mirror is the working download site. Note the emulated-3033 default — see [§1](#1-design-decision-which-370-panel-to-replicate), it is only a `CPUMODEL` line. |
| [H390-MVS list — "MVS 3.8j Tur(n)key TK4- System — Update 08 Available"](https://h390-mvs.yahoogroups.narkive.com/0W13Msef/mvs-3-8j-tur-n-key-tk4-system-update-08-available) — *narkive returns 503; read the live successor list at [groups.io/g/H390-MVS](https://groups.io/g/H390-MVS)* | Release notes for TK4- Update 8, the last major update — describes what is in the distribution. |
| [H390-MVS list — "MVS 3.8j Tur(n)key TK4- System Available"](https://h390-mvs.yahoogroups.narkive.com/uYfnOiuq/mvs-3-8j-tur-n-key-tk4-system-available) — **Wayback copy (2025-06-04) works:** [archived version](http://web.archive.org/web/20250604125220/https://h390-mvs.yahoogroups.narkive.com/uYfnOiuq/mvs-3-8j-tur-n-key-tk4-system-available) | The original TK4- announcement, explaining its relationship to Volker Bandke's TK3. |
| [H390-MVS list — TK4- Update 05 announcement](https://h390-mvs.yahoogroups.narkive.com/lLvuySRO/mvs-3-8j-tur-n-key-tk4-system-update-05-available) — *narkive 503; try [groups.io/g/H390-MVS](https://groups.io/g/H390-MVS) or the [Wayback index for this host](https://web.archive.org/web/*/h390-mvs.yahoogroups.narkive.com/*)* | Intermediate release notes. |
| [H390-MVS on groups.io — "MVS TK4 or CE" thread](https://groups.io/g/H390-MVS/topic/mvs_tk4_or_ce/88376808) | **Live.** Current community discussion comparing TK4-, TK5 and MVS/CE, and where people post working mirror links when a primary site goes down. |
| [tk4 CREDITS.md (mainframed/tk4 on GitHub)](https://github.com/mainframed/tk4/blob/main/CREDITS.md) | Credits file documenting the full TK3 → TK4- lineage and everyone who contributed components — a good map of who built what. |
| [**The MVS Tur(n)key New Users Cookbook** (Volker Bandke, BSP GmbH mirror)](https://bsp-gmbh.pocnet.net/turnkey/cookbook/) | Volker Bandke's classic introduction for new Turnkey users, by the creator of TK3. Still the friendliest starting point for someone who has never used MVS. |

### 8.2 Turnkey in containers (handy for the Raspberry Pi)

| Reference | Content |
| --- | --- |
| [tk5-hercules (joergschultzelutter)](https://github.com/joergschultzelutter/tk5-hercules) | Port of skunklabz' `tk4-hercules` Dockerfile to MVS 3.8j Turnkey 5.2, running on Alpine Linux. |
| [docker-ubuntu-hercules-mvs (RattyDAVE)](https://github.com/RattyDAVE/docker-ubuntu-hercules-mvs) | Ubuntu + Hercules + MVS container. |
| [rattydave/docker-ubuntu-hercules-mvs on Docker Hub](https://hub.docker.com/r/rattydave/docker-ubuntu-hercules-mvs) | Prebuilt image. |
| [mvs38j (skissane)](https://github.com/skissane/mvs38j) | Run MVS 3.8J inside Docker. |

*Caveat:* containers simplify deployment but add a layer between Hercules and your serial port.
For the panel project a **native install on the Pi** is simpler.

### 8.3 MVS 3.8j itself — sources, SYSGEN and learning

| Reference | Content |
| --- | --- |
| [CBT Tape — MVS 3.8j page](https://www.cbttape.org/mvs38.htm) | The CBT Tape is the canonical public collection of MVS freeware and public-domain software; this page is the reference index for MVS 3.8j distributions and materials. |
| [Michael Dickinson — "Available distributions of MVS3.8J I am aware of"](https://mdickinson.dyndns.org/hercules/obtaining_an_os/obtaining_mvs38j.php) | Comparison table of every MVS 3.8j distribution (TK3, TK4-, TK5, MVS/CE, MVS/380 and others) with pros and cons. **Read this before choosing.** |
| [Jay Moseley — Installing MVS 3.8j](https://www.jaymoseley.com/hercules/installMVS/iMVSintroV8.htm) | The famous hands-on guide to generating a working MVS 3.8j **from scratch**, starting from the IBM MVS 3.7 starter system. You do not need this for a Turnkey system, but it is the best explanation of how MVS is actually put together. |
| [Jay Moseley — Hercules / MVS site root](https://www.jaymoseley.com/hercules/) | Also hosts the widely used **TSO tutorial** based on MVS 3.8 and an **MVS FAQ**. |
| [MVS/380](https://en.wikipedia.org/wiki/MVS) *(see project sites via Awesome-Mainframes)* | A patched MVS 3.8 + Hercules combination that allows access to 31-bit address space — an alternative to plain 3.8j if you want more memory. Linked from the Awesome-Mainframes list below. |

### 8.4 MVS tutorials, walkthroughs and getting-started blogs

| Reference | Content |
| --- | --- |
| [Awesome-Mainframes (FuzzyMainframes on GitHub)](https://github.com/FuzzyMainframes/Awesome-Mainframes) | **Start here.** A curated "awesome list" of mainframe resources: emulators, operating systems, Turnkey distributions, tutorials, utilities, communities, videos. The single best index of everything in this section. |
| [Awesome-Mainframes README (direct)](https://github.com/FuzzyMainframes/Awesome-Mainframes/blob/master/README.md) | The list content itself. |
| [Supratim Sanyal — "MVS 3.8 Operating System on IBM 3033 Mainframe: Virtualization on Linux Using Hercules and MVS 3.8J TK4-"](https://supratim-sanyal.blogspot.com/2020/01/mvs-38-operating-system-on-ibm-3033.html) | Detailed, screenshot-heavy Linux walkthrough of installing and running TK4-. Closest thing to a Raspberry-Pi-ready recipe. |
| [Bradrico Rigg — "Run your own mainframe using Hercules mainframe emulator and MVS 3.8j tk4"](https://bradricorigg.medium.com/run-your-own-mainframe-using-hercules-mainframe-emulator-and-mvs-3-8j-tk4-55fa7c982553) | Step-by-step Medium tutorial. |
| [Bradley Rigg — same tutorial, alternate posting](https://bradrigg456.medium.com/run-your-own-mainframe-using-hercules-mainframe-emulator-and-mvs-3-8j-tk4-e8a85ebecd62) | Mirror. |
| [Mike Slinn — "IBM MVS on the Hercules Mainframe emulator"](https://www.mslinn.com/mainframe/2000-hercules.html) | Setup notes and background. |
| [Monadical — "Starting and Running Your First Program on a Mainframe"](https://monadical.com/posts/how-to-run-programs-on-a-mainframe.html) | Beginner-friendly first-JCL-job walkthrough. |
| [Kevin Durant — "MOM Pt. 001: Setting up my own Mainframe!"](https://kevindurant.be/2019/03/17/mom-part-1-setting-up-my-own-mainframe/) | Blog series on building a home mainframe environment. |
| [Dan's Notes — "Emulate your own mainframe computer with MVS-TK5"](https://www.maccormac.net/emulate-your-own-mainframe/) | Focused specifically on TK5. |
| [LowEndBox — "Run a $8 Million Mainframe at Home for FREE!"](https://lowendbox.com/blog/run-a-8-million-mainframe-at-home-for-free/) | Light introduction aimed at people with small VPS/SBC hardware — relevant to Raspberry Pi sizing. |
| [Hendro's Workshop — "Look Ma! My $5 Pi Zero Thinks It is a Mainframe"](https://www.suhendro.com/2016/10/look-ma-my-5-pi-zero-thinks-it-is-a-mainframe/) | **Running Hercules + MVS on a Raspberry Pi Zero.** Directly relevant performance data point: if a Pi Zero can do it, a modern Pi has ample headroom for Hercules plus your serial panel driver. |
| [RS DesignSpark — "My Raspberry Pi Thinks It's a Mainframe!"](https://www.rs-online.com/designspark/my-raspberry-pi-thinks-it-s-a-mainframe) | Another Pi + Hercules build write-up. |
| [AskWoody — "IBM System/370 on a… Raspberry Pi"](https://www.askwoody.com/forums/topic/ibm-system-370-on-a-raspberry-pi/) | Forum thread on the same combination, with troubleshooting. |
| [Vito Rallo — "I Built a Mac App to Run an IBM Mainframe… Hercules and TK5 natively on Apple Silicon"](https://medium.com/@vito.rallo/i-built-a-mac-app-to-run-an-ibm-mainframe-running-hercules-and-tk5-natively-on-a-apple-silicon-b625fed07962) | Example of wrapping Hercules + TK5 in a purpose-built launcher app — a useful model for the launcher you will write on the Pi. |
| [moshix/mvs on GitHub](https://github.com/moshix/mvs) | "Useful mainframe stuff" — scripts, tools and MVS material from moshix. |
| [mvs_submit_job (GroupTheorist12)](https://github.com/GroupTheorist12/mvs_submit_job) | Submitting jobs to MVS programmatically — useful if the panel should be able to trigger jobs. |
| [Quora — "Can IBM System 360/370/390 programs be run on a PC, a Mac or a Raspberry Pi?"](https://www.quora.com/Can-IBM-System-360-370-390-programs-be-run-on-a-PC-a-Mac-or-a-Raspberry-Pi) | General orientation answer on the emulation landscape. |

---

## 9. Electronics: Arduino ↔ Raspberry Pi, LEDs, switches, USB

Your panel will need on the order of **150–250 LEDs** and **100+ switch inputs** depending on
model. That rules out one-pin-per-device.

| Reference | Content |
| --- | --- |
| [PiDP-11 Technical Details](https://obsolescence.wixsite.com/obsolescence/pidp-11-technical-details) | (Repeated from §5.3 because it is the most directly applicable electrical reference.) Row/column multiplexing at ~60 Hz, UDN2981 high-side driver, 390 Ω LED current limiting, 1 kΩ switch-sense limiting, interleaved switch scanning, KiCad. |
| [Operation Blinkenlights — January 2012 archive](http://ibm360-console.blogspot.com/2012_01_01_archive.html) | (Repeated from §5.1.) The **74HC595 / 74HC597 shift-register chain** approach for 237 outputs and 183 inputs, and the measured latency difference between the Velleman USB board (~1 s) and an Arduino Mega 2560 (~1 ms). |
| [JLCPCB — "Arduino LED Driver Guide: 74HC595 and MAX7219 for LED Matrix"](https://jlcpcb.com/blog/arduino-led-driver-tutorial) | Practical tutorial on both approaches: cascading modules, brightness control, wiring diagrams, optimised SPI code. |
| [ETC CMU — "Driving a looooooot of LEDs"](https://www.etc.cmu.edu/projects/flux/?p=233) | Cost/architecture comparison for large LED counts: **TLC5940** (16-channel constant-current sink) for columns plus **MIC5891** (8-bit serial latched source driver) for rows. Notes ~$27.60 in driver chips for a 24×24 bi-colour matrix versus ~$94.50 using MAX7221s. Directly relevant to keeping a 250-LED panel affordable. |
| [Hackaday.io — J.B. Langston, "My LED Matrix Needs a Little TLC"](https://hackaday.io/page/10259-my-led-matrix-needs-a-little-tlc) | Build log using TLC5940s for a large matrix, with the gotchas. |
| [Arduino Forum — "16x8 LED matrix driver IC"](https://forum.arduino.cc/t/16x8-led-matrix-driver-ic/135578) | Discussion comparing MAX7219, HT16K33 and discrete shift registers. |
| [Arduino Forum — "Red LED matrix with TLC5940"](https://forum.arduino.cc/t/red-led-matrix-with-tlc5940/136053) | Practical TLC5940 wiring and code issues. |
| [Arduino Forum — "MAX7219 LED Matrix"](https://forum.arduino.cc/t/max7219-led-matrix/275606) | MAX7219 daisy-chaining in practice. |
| [ShiftRegisterLEDMatrixLib (michaelkamprath, GitHub)](https://github.com/michaelkamprath/ShiftRegisterLEDMatrixLib) | Arduino library for LED matrices driven by shift registers for both rows and columns — a ready-made software base for the panel driver. |
| [DigiKey Maker.io — MAX7219 8×8 LED Matrix Module Arduino Interfacing](https://www.digikey.com/es/maker/projects/max7219-8x8-led-matrix-module-arduino-interfacing/3bfeffd9a5b148a5869688ecf40e952d) | Clean reference wiring and code (Spanish-language DigiKey page). |
| [PCBSync — MAX7219 LED Matrix Arduino complete guide](https://pcbsync.com/max7219-led-matrix-arduino/) | Another complete MAX7219 walkthrough. |
| [neonaut — "LED Matrixes — 1088AS, 2088RGB, Colorduino"](https://neonaut.neocities.org/blog/2018/led-matrixes-1088as-2088rgb-colorduino) | Comparison of matrix modules and driving methods. |
| [Instructables — "Magic Hercules: Driver for Digital LEDs"](https://www.instructables.com/Magic-Hercules-Driver-for-Digital-LEDs/) | *(Name collision — unrelated to the Hercules emulator.)* An SPI-to-NZR converter module for addressable LEDs, 3.3 V tolerant. Relevant only if you choose addressable (WS2812-style) LEDs instead of a multiplexed matrix. |
| [Arduino Project Hub — Magic Hercules driver](https://create.arduino.cc/projecthub/p-kard/magic-hercules-driver-for-digital-leds-be361c) | Same project on Project Hub. |
| [hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) | The reference implementation for high-quality LED matrix driving direct from Raspberry Pi GPIO, with careful timing. Worth reading for its timing/PWM technique even though your matrix is monochrome and Arduino-driven. |
| [2dom/PxMatrix](https://github.com/2dom/PxMatrix) | Adafruit-GFX-compatible LED matrix panel driver — another timing reference. |
| [vitorleal/matrix-led-python](https://github.com/vitorleal/matrix-led-python) | Python module for driving a matrix from the Raspberry Pi — relevant if you decide to move some driving to the Pi side. |
| [GitHub topic — led-panels](https://github.com/topics/led-panels) | Broad index of current LED-panel projects and libraries. |

**Architecture recommendation based on the prior art:** an **Arduino Mega 2560** (or a Teensy, for
more RAM and speed) running a tight multiplexing loop, with **74HC595 chains for LED columns**,
a **UDN2981 / TPIC6B595-class driver for rows**, and **74HC597 or MCP23017 chains for switch
input**; USB CDC serial to the Pi at 115200 baud or higher, with a compact binary frame protocol
(magic byte + lamp bitmap + checksum outbound, switch bitmap inbound). Keep the Arduino dumb: it
should own only multiplexing and debouncing, and all semantics should live on the Pi. This is
exactly the split Operation Blinkenlights arrived at after abandoning the slow USB-board approach.

---

## 10. Laser cutting acrylic: file preparation and vendors

| Reference | Content |
| --- | --- |
| [PlaqueMaker — Laser Cutting File Guidelines & Design Requirements](https://www.plaquemaker.com/pages/resources-content/laser-cutting-file-guidelines) | Accepted vector formats (PDF, AI, EPS from Adobe; CDR from CorelDRAW; DXF/DWG compatible with AutoCAD 2014 or earlier); requirement that artwork be **vector only**; cut lines at minimum stroke thickness. |
| [Laser Cutting Experts AU — "Acrylic Laser Cutting: Thickness, Finishes & Design Rules (2025 Guide)"](https://www.lasercuttingexperts.com.au/acrylic-laser-cutting-thickness-finishes-design-rules-2025-guide) | **Convert all fonts to outlines/curves before export.** Use stencil-safe fonts or add bridges for closed letters (A, O, P, R, B). Avoid hairline serifs. **For reverse-engraved panels viewed through the face, mirror the artwork**, and put engraving lines on a clearly named etch layer in the DXF. Directly applicable to an IBM panel legend. |
| [Xometry — "Extruded and Cast Acrylic: How to Laser Engrave and Cut Acrylic"](https://www.xometry.com/resources/sheet/cast-acrylic-cutting/) | **Cast acrylic engraves more cleanly (frosted white result); extruded acrylic gives smoother flame-polished cut edges.** Choose per surface: cast for the engraved legend, extruded if edge quality dominates. |
| [LCSC — Front Panel Design Specifications](https://www.lcsc.com/faqs/front-panels/front-panels-design-specifications) | Manufacturer spec sheet with concrete minimums: **text line width > 0.25 mm for bottom (second-surface) printing, > 0.15 mm for front printing.** Use these numbers when sizing the tiny IBM legends. |
| [Nova Display — Submission Guidelines for Acrylic Laser Cutting and Engraving](https://www.novadisplay.com/nova-display-resources/customer-support-pages/submit-artwork-and-specs/submission-guidelines/submission-guidelines-for-laser-cutting-and-engraving/) | Artwork submission checklist from a commercial shop — a good template for what your cutting company will ask for. |
| [Ponoko — "Mounting And Protecting Custom PCBs With Laser Cut Faceplates, Panels And Enclosures"](https://www.ponoko.com/blog/design-ideas/mounting-and-protecting-custom-pcbs-with-laser-cut-faceplates-panels-and-enclosures/) | How to design a laser-cut faceplate that mounts over a PCB — exactly your LED/switch PCB behind an acrylic panel problem. Ponoko is also a practical low-volume vendor. |
| [Inventables — Black and Clear Reverse Laserable Acrylic Sheet](https://www.inventables.com/products/black-and-clear-reverse-laserable-acrylic-sheet) | Two-layer "reverse laserable" acrylic: engrave from the back through a black layer to reveal clear, then backlight. **This is the single easiest way to get crisp backlit legends and lamp windows on a replica panel** — consider it for the lamp-legend strips. |
| [Canal Plastics Center — laser cutting service](https://www.canalplastic.com/pages/laser-cutting) | Established acrylic supplier and cutting service. |
| [PlaqueMaker / vectorsfile / Vecty free template libraries](https://vectorsfile.com/) · [Vecty acrylic templates](https://vecty.co/laser-cut/acrylic) | Free laser-cut vector template libraries — useful for reference geometry and file structure conventions, not for IBM artwork. |

**Recommended panel construction**, combining the PiDP-11 method with the above:
polycarbonate face sheet → printed graphics layer → acrylic backing, laminated, then laser cut for
switch and pushbutton openings; lamp legends done as second-surface engraving on reverse-laserable
acrylic so they can be backlit. Ask your cutter for **cast acrylic** for engraved parts.

---

## 11. Books

Every entry below carries a link. Where a **free-to-read or borrowable** copy exists on the
Internet Archive it is given first and marked **[IA free]** (no account needed) or
**[IA borrow]** (free Internet Archive account, 1-hour/14-day loan).

### 11.1 History of the machines

| Book | Where to read it | Content |
| --- | --- | --- |
| **Pugh, Johnson & Palmer — *IBM's 360 and Early 370 Systems*** (MIT Press, 1991, xx + 810 pp., ISBN 9780262517201) | **[IA borrow](https://archive.org/details/ibms360early370s0000pugh)** · [MIT Press](https://direct.mit.edu/books/monograph/4262/IBM-s-360-and-Early-370-Systems) · [Google Books preview](https://books.google.com/books/about/IBM_s_360_and_Early_370_Systems.html?id=MFGj_PT_clIC) · [print/used](https://www.amazon.com/IBMs-Early-Systems-History-Computing/dp/0262517205) · [all editions](https://www.goodreads.com/work/editions/1444979-ibm-s-360-and-early-370-systems-history-of-computing) | **The definitive history.** Covers ~1960–1975 from IBM's own records, published reports and interviews with 100+ participants: hybrid circuits, the unified-product-line decision, memory and storage development, software support, integrated circuits, terminal-oriented systems. Essential for understanding *why* the panels look the way they do; contains photographs and engineering detail found nowhere online. |
| **Pugh — *Memories That Shaped an Industry: Decisions Leading to IBM System/360*** (MIT Press, 1984) | **[IA borrow](https://archive.org/details/memoriesthatshap0000pugh)** | The prequel: how IBM arrived at the S/360 decision, with deep coverage of the core-memory and circuit technology that dictated what a 1964-era console could physically display. |
| **Pugh — *Building IBM: Shaping an Industry and Its Technology*** (MIT Press, 1995) | **[IA borrow](https://archive.org/details/buildingibmshapi0000pugh)** | Company-wide history from the tabulator era through the 1990s — the wider context for the whole [timeline in §18](#18-ibm-mainframe-hardware-timeline-19522026). |
| **Melinda Varian — *VM and the VM Community: Past, Present, and Future*** (SHARE 89, Sessions 9059–9061, August 1997; earlier versions 1989, 1990, 1991) | **[Free PDF, leeandmelindavarian.com](https://www.leeandmelindavarian.com/Melinda/25paper.pdf)** | **The definitive insider history of IBM virtual machines**, written by Melinda Varian of Princeton's Office of Computing and Information Technology and marking VM's 25th anniversary. Traces the line from **CP-40** and **CP-67/CMS** on the **System/360 Model 67** through **VM/370** and beyond, covering the Cambridge Scientific Center, the people who built it, IBM's competing TSS/360 effort, and how the *user community* (SHARE, VMSHARE) drove the product — a rare history that is technical, primary-source and readable at once. **Relevance to this project:** the /370's virtual-storage architecture is the thing MVS 3.8j and Hercules both rest on, and this paper explains where it came from and why the Model 67 mattered. Freely downloadable, ~3,700 lines of text. Copyright Melinda W. Varian; redistribution permission granted to SHARE only, so link to it rather than rehosting it. |
| **Brooks — *The Mythical Man-Month*** (1975; 1995 anniversary ed.) | **[IA free, 1995 ed.](https://archive.org/details/MythicalManMonth)** · [IA borrow, 1975 ed.](https://archive.org/details/mythicalmanmonth00broo) | Written by the manager of OS/360 *about* OS/360. Not a hardware book, but the single best explanation of why the software you will run (MVS's ancestor) turned out the way it did. |
| **Reviews of Pugh et al.** | [Academia.edu](https://www.academia.edu/109239689/IBMs_360_and_Early_370_Systems_ByEmerson_W_Pugh_Lyle_R_Johnson_and_John_H_Palmer_Cambridge_Mass_MIT_Press_1991_xx_810_pp_Charts_illustrations_appendixes_notes_references_and_index_37_50) · [ResearchGate](https://www.researchgate.net/publication/274770131_IBM's_360_and_Early_370_Systems_By_Emerson_W_Pugh_Lyle_R_Johnson_and_John_H_Palmer_Cambridge_Mass_MIT_Press_1991_xx_810_pp_Charts_illustrations_appendixes_notes_references_and_index_3750) | Scholarly assessments of the book's reliability. *(Both hosts return 403 to scripts but load in a browser.)* |

### 11.2 Period IBM books, brochures and manuals on archive.org

| Book / document | Where to read it | Content |
| --- | --- | --- |
| **IBM System/370 Model 155 brochure (IBM, 1971)** | **[IA free](https://archive.org/details/TNM_IBM_System-370_Model_155_-_IBM_1971_20170907_0205)** | Original IBM sales brochure for the /155. **Directly useful for your panel** — period product photography of exactly the machine class you are replicating. |
| **IBM *Introduction to Virtual Storage in System/370*** (IBM, 1972) | **[IA borrow](https://archive.org/details/ibmintroductiont0000vari)** | IBM's own explanation of the virtual-storage machinery that the /370 added over the /360 — the architecture MVS depends on. |
| **Rindfleisch — *Debugging System 360/370 Programs Using OS and VS Storage Dumps*** (1976) | **[IA borrow](https://archive.org/details/debuggingsystem30000rind)** | Period debugging practice; teaches you to read a PSW and registers the way an operator standing at the panel would. |
| **IBM *Principles of Operation: Type 701 and Associated Equipment*** (1953) | **[IA free](https://archive.org/details/type-701-and-associated-equipment)** | The earliest entry in the [§18 timeline](#18-ibm-mainframe-hardware-timeline-19522026) — IBM's first production stored-program computer, in IBM's own words. |
| **IBM 1401 Data Processing System brochure (1959)** | **[IA free, searchable](https://archive.org/details/ibm-1401-brochure-searchable)** | Original brochure for the machine that made IBM the dominant vendor before the /360. |
| **IBM System/360 Bibliography (A22-6822-4, 1965)** | **[IA free](https://archive.org/details/bitsavers_ibm360biblSystem360BibliographyAug65_4444592)** | IBM's own index of every S/360 publication — **use it to discover manual order numbers you did not know existed**, then look them up on Bitsavers. |
| **IBM System/360–System/370 Bibliography (GA22-6822-16, 1971)** | **[IA free](https://archive.org/details/bitsavers_ibm360biblystem360System370BibliographyJul71_14748928)** | The /370-era successor to the above. The fastest route to a complete list of /370 FE and operator manuals. |
| **IBM System/360 Debugging and Programming Cards (1970)** | **[IA free](https://archive.org/details/System_360_Debugging_and_Programming_Cards_)** | The pocket reference cards operators actually carried. |
| **IBM System/390 brochure (GU20-0082)** | **[IA free](https://archive.org/details/bitsavers_ibm390broctem390Brochure_6157275)** · [IBM System/390, 1990](https://archive.org/details/ibm-system-390-1990) | Later-generation IBM marketing material, for the §18 timeline. |
| **Hoskins — *IBM ES/9000: A Business Perspective*** (1992) | **[IA borrow](https://archive.org/details/ibmes9000busines00hosk)** | Contemporary account of the ES/9000 generation. |
| **IBM System/390 Technical Insights (1995)** | **[IA free](https://archive.org/details/ibm-system-390-technical-insights)** | Technical overview of the S/390 generation. |

### 11.3 MVS, JCL and TSO — the software you will actually run

| Book | Where to read it | Content |
| --- | --- | --- |
| **Johnson — *MVS: Concepts and Facilities*** (1989) | **[IA borrow](https://archive.org/details/mvsconceptsfacil0000john)** | The standard conceptual introduction to MVS internals. Start here after the Turnkey cookbook. |
| **Zamir — *The MVS JCL Primer*** (1995) | **[IA borrow](https://archive.org/details/mvsjclprimer0000zami)** | Gentle introduction to Job Control Language, which is how you get anything done on MVS 3.8j. |
| **Brown — *System/390 Job Control Language*** (1998) | **[IA borrow](https://archive.org/details/system390jobcont00brow)** | A fuller JCL text. |
| **Menendez & Lowe — *Murach's OS/390 and z/OS JCL*** (2002) | **[IA borrow](https://archive.org/details/murachsos390zosj0000mene)** | Modern, very readable JCL training and reference; most of it applies unchanged to MVS 3.8j. |
| **Carathanassis — *Expert MVS/XA JCL*** (1989) | **[IA borrow](https://archive.org/details/expertmvsxajcl0000cara)** | Advanced JCL. |
| **IBM — *MVS/390 JCL User's Guide*** (1996) | **[IA borrow](https://archive.org/details/mvsos390jclusersgu00inte)** | IBM's own JCL user's guide. |
| **Lowe — *MVS TSO: Concepts, Commands, SPF, CLIST*** (1984) | **[IA borrow](https://archive.org/details/mvstsoconceptsco0000lowe)** · [*MVS TSO*, 1991](https://archive.org/details/mvstso0000lowe) | TSO is the interactive interface you will log into under Turnkey. The 1984 edition is contemporary with MVS 3.8j. |
| **Bosler — *MVS TSO/ISPF*** (1993) | **[IA borrow](https://archive.org/details/mvstsoispfguidef00bosl)** | ISPF panels and editor — the environment TK4-/TK5 drop you into. |
| **Yuen — *Essential Concepts of Operating Systems: Using IBM Mainframe Examples*** (1986) | **[IA borrow](https://archive.org/details/essentialconcept0000yuen)** | OS theory taught entirely through IBM mainframe examples — bridges general CS knowledge to MVS. |
| **Bamberg & others — *MVS and UNIX: A Survival Handbook*** (1998) | **[IA borrow](https://archive.org/details/mvsunixsurvivalh0000bamb)** | Useful if you come from Linux (as you will, on the Raspberry Pi) and need the mental mapping. |
| **IBM System/370 Assists for MVS (GA22-7079-1, 1981)** | **[IA free](https://archive.org/details/bitsavers_ibm370MVSG0AssistsforMVSOct81_1165870)** | Hardware assists the /370 provides specifically for MVS. |
| **IBM Virtual Machine Facility/370 — CMS Command and Macro Reference (GC20-1818-3, 1981)** | **[IA free](https://archive.org/details/bitsavers_ibm370VM37BMVirtualMachineFacility370CMSCommandand_19758590)** | VM/370 reference, if you ever run VM instead of MVS under Hercules. |

### 11.4 Free book-length works already cited elsewhere in this document

| Work | Link | Content |
| --- | --- | --- |
| **IBM System/370 Principles of Operation** (GA22-7000-0, 1970) | [Bitsavers PDF](https://www.bitsavers.org/pdf/ibm/370/princOps/GA22-7000-0_370_Principles_Of_Operation_Jun70.pdf) | The primary architecture text — its **"Operator Facilities"** chapter is the specification your panel must satisfy. Keep it on your desk. Full entry in [§3.4](#34-architecture-and-physical-planning). |
| **The MVS Tur(n)key New Users Cookbook** (Volker Bandke) | [bsp-gmbh.pocnet.net mirror](https://bsp-gmbh.pocnet.net/turnkey/cookbook/) | Book-length free tutorial; the standard MVS 3.8j onboarding text, by the creator of TK3. Full entry in [§8.1](#81-turnkey-distributions--the-main-line-of-descent). |
| **Jay Moseley — Installing MVS 3.8j** | [jaymoseley.com](https://www.jaymoseley.com/hercules/installMVS/iMVSintroV8.htm) | Book-length free work on generating MVS from the IBM 3.7 starter system. Full entry in [§8.3](#83-mvs-38j-itself--sources-sysgen-and-learning). |
| **IBM Mainframe Operating Systems: Timeline and Brief Explanation** | [PDF on jaymoseley.com](https://www.jaymoseley.com/hercules/downloads/pdf/$OSTL33.pdf) | Compact chronology of every IBM mainframe OS and how they descend from one another — the companion to [§18](#18-ibm-mainframe-hardware-timeline-19522026). |

*Also worth acquiring if you find them second-hand:* any IBM **Field Engineering Theory of
Operation** or **Maintenance Library** binder for a 3145/3155/3165 — the physical binders often
contain fold-out panel drawings that scan poorly and are therefore missing or illegible in the
Bitsavers PDFs. Search [eBay](https://www.ebay.com/sch/i.html?_nkw=IBM+3145+field+engineering+manual) and
the [VCF Marketplace](https://forum.vcfed.org/index.php?forums/vintage-computer-marketplace.60/).

---

## 12. Magazines, trade press and periodical archives

| Reference | Content |
| --- | --- |
| [Datapro Reports 70C-491-05 — IBM System/370 Model 145](http://bitsavers.informatik.uni-stuttgart.de/pdf//datapro/datapro_reports_70s-90s/IBM/70C-491-05_7010_IBM_System_370_Model_145.pdf) | **Datapro Reports** were the industry's independent equipment evaluations. This one covers the /145 in detail: configuration, pricing, performance, and — importantly for you — the operator interface, with photographs. |
| [Datapro Reports 70C-491-04 — IBM System/370 Models 155 & 165](https://bitsavers.trailing-edge.com/pdf/datapro/datapro_reports_70s-90s/IBM/70C-491-04_7007_IBM_System_370_Model_155_165.pdf) | The same treatment for the /155 and /165 — the big-panel machines. |
| [Bitsavers Datapro archive (root)](https://bitsavers.org/pdf/datapro/) | The whole Datapro Reports collection, 1970s–1990s. Browse for any /370 model you settle on. |
| [Bitsavers `magazines` archive](https://bitsavers.org/magazines/) | Scanned computing periodicals — *Datamation*, *Computerworld* and others from the /370 era, containing IBM advertising with large, clean console photography. **IBM's own period advertisements are an underrated source of straight-on, well-lit panel images.** |
| [Internet Archive — computer magazine collections](https://archive.org/details/computermagazines) | Large searchable magazine archive; search for "System/370" to surface contemporary coverage and ads. |
| [IT History Society — IBM System/370 Model 155](https://www.ithistory.org/db/hardware/ibm/ibm-system370-model-155) | Database entry with specifications, dates and press references. |
| [Hackaday](https://hackaday.com/) (see model-specific tags in §5) | The de facto trade press for this kind of project. Following the [System/360](https://hackaday.com/tag/system-360/), [mainframe](https://hackaday.com/tag/mainframe/page/2/), [SIMH](https://hackaday.com/tag/simh/) and [I/O](https://hackaday.com/tag/io/) tags will surface new replica work as it appears — and is where you should publish your own build. |

---

## 13. YouTube channels and videos

| Channel / video | Link | Content |
| --- | --- | --- |
| **moshix** | [youtube.com/c/moshix](https://www.youtube.com/c/moshix) · [channel by ID](https://www.youtube.com/channel/UCR1ajTWGiUtiAv8X-hpBY7w) — *note: the `@moshix` handle URL 404s; use either link here* | **The single most useful channel for the software half of your project.** Hundreds of videos on IBM mainframes (plus DEC and Cray): Assembly, REXX, PL/I, Go, bash, Python, C. Includes the long practical series **"IBM's MVS 3.8 on Linux for newcomers"**, which walks from "I have never logged into a mainframe" to submitting a COBOL job on an emulated IBM 3033 under Hercules; **M14** covers adding a DASD device to MVS; **M24** covers running KICKS (CICS) on MVS 3.8. |
| **moshix — code and scripts** | [github.com/moshix/mvs](https://github.com/moshix/mvs) | The companion repository to the videos: MVS utilities, install scripts and mainframe tooling. |
| **moshix — Hercules/Bandke mirror** | [moshix.dynu.net/bandke/hercules/wingui/hercgui-faq.html](https://moshix.dynu.net/bandke/hercules/wingui/hercgui-faq.html) | Moshix hosts a mirror of Volker Bandke's Hercules material, including the WinGUI FAQ. |
| **CuriousMarc** | [youtube.com/channel/UC3bosUr3WlKYm4sBaLs-Adw](https://www.youtube.com/channel/UC3bosUr3WlKYm4sBaLs-Adw) | Restorations of exceptional vintage electronics, early computers, space hardware, mechanical calculators and Teletypes. **Marc acquired a real IBM System/360 Model 50 front panel with 250+ blinkenlights** and has documented working with it — including running it as a retro clock. The best channel for seeing how these panels are physically constructed and re-lit. |
| **CuriousMarc — companion site** | [curiousmarc.com/computing](https://www.curiousmarc.com/computing) | Written detail, schematics and part sourcing behind the videos. Often has the wiring diagrams the video only shows briefly. |
| **CuriousMarc — "IBM System/360 Front Panel"** | [youtube.com/watch?v=WS-WtjwAAO0](https://www.youtube.com/watch?v=WS-WtjwAAO0) | Walkthrough of a real /360 panel — lamps, buttons, rollers, wiring. **Watch this before designing the mechanics.** |
| **CuriousMarc — "Restoring an IBM I/O Tester from the 1960s"** | [youtube.com/watch?v=Z8PdWIZFVEk](https://www.youtube.com/watch?v=Z8PdWIZFVEk) | Restoring 1960s IBM panel hardware contemporaneous with the /360; excellent detail on IBM lamp assemblies and pushbutton construction. |
| **Hackaday write-up of the I/O Tester restoration** | [hackaday.com/2021/12/19/restoring-a-vintage-ibm-i-o-tester/](https://hackaday.com/2021/12/19/restoring-a-vintage-ibm-i-o-tester/) · [duino4projects mirror](https://duino4projects.com/restoring-a-vintage-ibm-i-o-tester/) | The written version, with stills you can pause over. |
| **"IBM 360 console blinkenlights"** | [youtube.com/watch?v=NU7kSAUSRUo](https://www.youtube.com/watch?v=NU7kSAUSRUo) | The Operation Blinkenlights panel running. **Study this for LED brightness and refresh rate** — it shows what a driven /360 panel actually looks like in motion, which still photos cannot convey. |
| **"IBM System/360 Front Panel" (Adafruit coverage)** | [blog.adafruit.com](https://blog.adafruit.com/2019/06/28/obtaining-an-ibm-system-360-front-panel-vintagecomputing-retrocomputing-ibm/) | Adafruit's post about the panel acquisition, with embedded video and further links. |
| **Usagi Electric** (David Lovett) | [youtube.com/@UsagiElectric](https://www.youtube.com/@UsagiElectric) | Restoration of very early computers, including a tube-based Bendix G-15 for a museum. Deep, patient coverage of period-correct electronics, lamp drivers and panel construction technique. |
| **Ken Shirriff** — appears frequently on CuriousMarc's restorations | [righto.com](http://www.righto.com/) *(blog, not a channel — see [§14](#14-blogs-forums-mailing-lists-and-communities))* · [the console article](http://www.righto.com/2019/04/iconic-consoles-of-ibm-system360.html) | The written counterpart to those videos: the definitive explanation of how /360 and /370 roller displays and lamp banks are organised. |
| **Computer History Museum — video collections** | [computerhistory.org/collections](https://www.computerhistory.org/collections/) · [CHM Revolution: Mainframes](https://www.computerhistory.org/revolution/mainframe-computers/7/161) | Oral histories and archival footage of S/360-era machines in operation, including operators using the consoles. |
| **PiDP-11 project videos** | [hackaday.io/project/8069-pidp-11](https://hackaday.io/project/8069-pidp-11) | The PiDP-11 logs embed videos of the finished panel multiplexing — the closest visual reference for what your Arduino-driven panel should look like when working. |

---

## 14. Blogs, forums, mailing lists and communities

Every entry links to a live destination unless explicitly marked otherwise.

### 14.1 Where to ask questions (live, active)

| Community | Link | Content |
| --- | --- | --- |
| **Hercules on groups.io** | [groups.io/g/hercules-390](https://groups.io/g/hercules-390) | **Where the Hercules community lives today**, after Yahoo Groups closed. The right place to ask how to get panel state out of Hercules, and where the developers who wrote the `EXTERNALGUI` code can be reached. |
| **H390-MVS on groups.io** | [groups.io/g/H390-MVS](https://groups.io/g/H390-MVS) · [example thread: "MVS TK4 or CE"](https://groups.io/g/H390-MVS/topic/mvs_tk4_or_ce/88376808) | The MVS-on-Hercules list. Turnkey release announcements, MVS troubleshooting, and where working mirror links get posted when a primary site (like `wotho.ethz.ch`) goes down. |
| **Google Group: pidp-11** | [groups.google.com/g/pidp-11](https://groups.google.com/g/pidp-11) · [completed-builds gallery thread](https://groups.google.com/g/pidp-11/c/E-RMRVQ15NQ/m/3S6ln4ANEwAJ) | Hundreds of people who have each built a Raspberry-Pi-driven replica front panel. **Ask your acrylic lamination, LED multiplexing and switch-debounce questions here** — this is where the practical expertise actually is. |
| **Google Group: pidp-8** | [groups.google.com/g/pidp-8](https://groups.google.com/g/pidp-8) · [panel construction thread](https://groups.google.com/g/pidp-8/c/uFkciMFuHHg) | The older sibling community; same expertise, longer archive. |
| **Google Group: altair-duino** | [groups.google.com/g/altair-duino](https://groups.google.com/g/altair-duino) · [thread: "IBM System/360 or 370 Front Panel?"](https://groups.google.com/g/altair-duino/c/D1k26Spm6zE) | Community around the **Arduino-driven** Altair 8800 replica — the closest existing commercial product to what you are building, and a linked thread specifically about doing an IBM panel. |
| **classiccmp — cctalk mailing list** | [classiccmp.org/pipermail/cctalk/](https://classiccmp.org/pipermail/cctalk/) · [front-panel thread example](https://classiccmp.org/pipermail/cctalk/2018-March/038873.html) | The classic-computing mailing list. Front-panel, simulator and restoration threads appear constantly, and people here own real hardware you may be able to measure. |
| **SimH mailing list archive** | [mail-archive.com/simh@trailing-edge.com/](https://www.mail-archive.com/simh@trailing-edge.com/) · [the "Frontpanels" design thread](https://www.mail-archive.com/simh@trailing-edge.com/msg07173.html) | Design discussion on how a simulator should expose front-panel state — the same architectural problem you face with Hercules. |
| **Vintage Computer Federation forums** | [forum.vcfed.org](https://forum.vcfed.org/) · [marketplace](https://forum.vcfed.org/index.php?forums/vintage-computer-marketplace.60/) | Large restoration community; the marketplace is a realistic source for real IBM lamp assemblies, switches and FE manuals. |
| **Reddit — r/mainframe** | [reddit.com/r/mainframe](https://www.reddit.com/r/mainframe/) | MVS, JCL and z/OS questions; a mix of hobbyists and working mainframe staff. |
| **Reddit — r/retrobattlestations** | [reddit.com/r/retrobattlestations](https://www.reddit.com/r/retrobattlestations/) | Where to post the finished panel and get build feedback. |
| **Hacker News — "Control Panel Of IBM 360 Mainframe"** | [news.ycombinator.com/item?id=3196037](https://news.ycombinator.com/item?id=3196037) | First-hand recollections from people who **operated** these machines — what the lights actually did in practice, which no manual records. |
| **Hacker News — "A Guide to the IBM 3033 Processor Complex (1979)"** | [news.ycombinator.com/item?id=24195600](https://news.ycombinator.com/item?id=24195600) | Discussion of the 3033 manual, with operator anecdotes about the 3036 console. See [§17](#17-the-ibm-3033--303x-console-lights-switches-buttons). |
| **alt.folklore.computers** | [groups.google.com/g/alt.folklore.computers](https://groups.google.com/g/alt.folklore.computers) · [simulated PDP-11 panel thread](https://groups.google.com/g/alt.folklore.computers/c/VIw6tJKZx_c) | Long-running Usenet group; deep institutional memory about these machines. |

### 14.2 Blogs and personal archives (live)

| Site | Link | Content |
| --- | --- | --- |
| **Ken Shirriff — righto.com** | [righto.com](http://www.righto.com/) · [the /360 console article](http://www.righto.com/2019/04/iconic-consoles-of-ibm-system360.html) | The best technical writing on vintage IBM hardware anywhere. A masterclass in reverse-engineering old hardware from its manuals — which is exactly the skill this project needs. |
| **Operation Blinkenlights** | [ibm360-console.blogspot.com](http://ibm360-console.blogspot.com/) · [electronics phase](http://ibm360-console.blogspot.com/2012_01_01_archive.html) · [FPGA phase](https://ibm360-console.blogspot.com/2012/04/emulator-goes-hardware.html) · [source release](http://ibm360-console.blogspot.com/2012/04/source-code-of-fpga-implementation.html) | **The project blog most similar to yours.** Read it end to end before you buy any components. See [§5.1](#51-operation-blinkenlights--the-closest-prior-art-to-your-project). |
| **VAXBARN** | [vaxbarn.com](https://vaxbarn.com/) · [Operation Blinkenlights project page](https://vaxbarn.com/projects/ibm-360-panel) | Collector site hosting the Operation Blinkenlights panel; broad vintage-hardware coverage. *(Note: `vaxbarn.com/cat/360` now 404s — see [§19](#19-link-health-and-archive-policy).)* |
| **obsolescence.dev** (Oscar Vermeulen) | [obsolescence.dev](https://obsolescence.dev/) · [PiDP-11 technical details](https://obsolescence.wixsite.com/obsolescence/pidp-11-technical-details) · [PiDP-10 technical details](https://obsolescence.wixsite.com/obsolescence/pidp-10-technical-details) | The PiDP project home — build guides, the multiplexing design you should copy, and ordering. |
| **retrocmp.com** (Jörg Hoppe) | [retrocmp.com](https://www.retrocmp.com/) · [BlinkenBone root](http://www.retrocmp.com/projects/blinkenbone) · [UniBone BlinkenBone panels](https://www.retrocmp.com/projects/unibone/354-unibone-blinkenbone-panels) | The BlinkenBone architecture for connecting simulators to real panels, plus the hardware to do it. |
| **Lawrence Wilkinson — ljw.me.uk** | [ljw.me.uk/ibm360/Saga.html](https://www.ljw.me.uk/ibm360/Saga.html) · [VHDL source](https://www.ljw.me.uk/ibm360/vhdl/) | The gate-level IBM 360/30 in VHDL, with a front-panel recreation accurate down to microcode-state lights. |
| **Mark Smotherman — Clemson** | [mark.people.clemson.edu](https://mark.people.clemson.edu/) · [architecture history index](https://mark.people.clemson.edu/hist.html) · [360/370 architecture appendix (PDF)](https://mark.people.clemson.edu/464/appF.pdf) | Academic archive of IBM mainframe architecture history — ACS, Future System, Model 91, I/O history. |
| **Ed Thelen — computer history** | [ed-thelen.org/comp-hist/](https://ed-thelen.org/comp-hist/) · [IBM 360/30 page](https://ed-thelen.org/comp-hist/ibm-360-30.html) · [370/145 product announcement](https://ed-thelen.org/comp-hist/IBM-ProdAnn/370-145.pdf) | Long-running archive of machine descriptions, original product announcements and restoration accounts. |
| **Jay Moseley** | [jaymoseley.com/hercules/](https://www.jaymoseley.com/hercules/) · [installing MVS 3.8j](https://www.jaymoseley.com/hercules/installMVS/iMVSintroV8.htm) · [OS timeline PDF](https://www.jaymoseley.com/hercules/downloads/pdf/$OSTL33.pdf) | MVS installation from the starter system, the TSO tutorial, the MVS FAQ, and the IBM operating-system timeline. |
| **Michael Dickinson — Hercules pages** | [mdickinson.dyndns.org/hercules/](https://mdickinson.dyndns.org/hercules/) · [choosing a Hercules build](https://mdickinson.dyndns.org/hercules/obtaining.php) · [choosing an MVS distribution](https://mdickinson.dyndns.org/hercules/obtaining_an_os/obtaining_mvs38j.php) | The clearest comparison of the competing Hercules forks and MVS 3.8j distributions. *(Dynamic-DNS host — mirror it locally.)* |
| **CBT Tape** | [cbttape.org](https://www.cbttape.org/) · [MVS 3.8j index](https://www.cbttape.org/mvs38.htm) | The canonical public-domain MVS freeware collection and community hub. |
| **Supratim Sanyal's blog** | [supratim-sanyal.blogspot.com — MVS 3.8 on Hercules](https://supratim-sanyal.blogspot.com/2020/01/mvs-38-operating-system-on-ibm-3033.html) | Screenshot-heavy Linux walkthrough of a TK4- installation. |
| **Kevin Durant's blog — "MOM" series** | [kevindurant.be — setting up my own mainframe](https://kevindurant.be/2019/03/17/mom-part-1-setting-up-my-own-mainframe/) | Multi-part home-mainframe build series. |
| **Dan's Notes** | [maccormac.net — emulate your own mainframe](https://www.maccormac.net/emulate-your-own-mainframe/) | TK5-specific getting-started guide. |
| **Hendro's Workshop** | [suhendro.com — Pi Zero as a mainframe](https://www.suhendro.com/2016/10/look-ma-my-5-pi-zero-thinks-it-is-a-mainframe/) | Hercules + MVS on a Raspberry Pi Zero — the performance data point that proves your Pi has ample headroom. |
| **JWT Audio — Retro Computing** | [jwtaudio.com/other-interests/retro-computing](https://www.jwtaudio.com/other-interests/retro-computing) | Hobbyist site with panel and restoration material. |
| **Hackaday** | [hackaday.com](https://hackaday.com/) · [System/360 tag](https://hackaday.com/tag/system-360/) · [mainframe tag](https://hackaday.com/tag/mainframe/page/2/) · [SIMH tag](https://hackaday.com/tag/simh/) · [I/O tag](https://hackaday.com/tag/io/) | The de facto trade press for projects like yours. Follow these tags to catch new replica work — and **publish your build here** when it runs. |
| **Adafruit blog** | [blog.adafruit.com — obtaining an IBM System/360 front panel](https://blog.adafruit.com/2019/06/28/obtaining-an-ibm-system-360-front-panel-vintagecomputing-retrocomputing-ibm/) | Notes that replicas exist for the IMSAI 8080 and PDP-11 but the IBM 360/370 has never had the same treatment. That gap is your project. |
| **duino4projects** | [duino4projects.com — IBM I/O Tester restoration](https://duino4projects.com/restoring-a-vintage-ibm-i-o-tester/) | Arduino-community write-up of the CuriousMarc restoration. |
| **Chris Bigos — ibm360.com / ibm360.info** | [ibm360.com](https://www.ibm360.com/home/s360-front-panels) · [ibm360.info](https://www.ibm360.info/home/s360-front-panels) | The recreated front-panel artwork and scanned FE documents. **Contact the owner here about licensing before deriving cutting files** (CC BY-NC-SA). |

### 14.3 Archives of dead communities (read-only, partly broken)

| Archive | Link | Status and content |
| --- | --- | --- |
| **hercules-390 Yahoo Group (via narkive)** | [hercules-390.yahoogroups.narkive.com](https://hercules-390.yahoogroups.narkive.com/) · [Wayback index for the host](https://web.archive.org/web/*/hercules-390.yahoogroups.narkive.com/*) | **Returned HTTP 503 on 2026-08-01.** Yahoo Groups itself is gone; narkive is a third-party mirror that is frequently overloaded. The Wayback Machine holds hundreds of individual threads from 2021–2024 — but **not** the operator-panel thread from [§5.2](#52-using-a-real-s360-or-s370-panel-with-hercules--the-mailing-list-thread). Retry narkive later, or re-ask on [groups.io](https://groups.io/g/hercules-390). |
| **H390-MVS Yahoo Group (via narkive)** | [h390-mvs.yahoogroups.narkive.com](https://h390-mvs.yahoogroups.narkive.com/) · [archived TK4- announcement](http://web.archive.org/web/20250604125220/https://h390-mvs.yahoogroups.narkive.com/uYfnOiuq/mvs-3-8j-tur-n-key-tk4-system-available) | **503 on 2026-08-01.** The Turnkey release announcements live here. The Wayback copy of the original TK4- announcement works. |
| **Operation Blinkenlights wiki** | ~~`ibm360-console.wikispaces.com`~~ — [CDX query showing what survives](http://web.archive.org/cdx/search/cdx?url=ibm360-console.wikispaces.com*&output=text&fl=timestamp,original,statuscode&collapse=urlkey) | **Permanently dead and essentially unarchived.** Wikispaces shut down in 2018; the Internet Archive holds only a root redirect, a favicon, `robots.txt` and one paywalled file entry. **The modified Hercules source that lived here appears to be lost** — ask on [groups.io/g/hercules-390](https://groups.io/g/hercules-390) or contact [VAXBARN](https://vaxbarn.com/projects/ibm-360-panel). |
| **hercules-390.org** | ~~`http://www.hercules-390.org/`~~ — [Wayback, 2026-05-02](http://web.archive.org/web/20260502060042/http://www.hercules-390.org/) · live replacements: [docs](https://hercules-390.github.io/html/), [code](https://github.com/hercules-390/hyperion) | **Offline as of 2026-08-01.** The GitHub Pages documentation and the GitHub repository have taken over both functions. |

---

## 15. Master reference index

Every source cited above, in one flat list, with a one-line note on its content.

### Panel artwork and drawings
| # | Reference | What it contains |
| --- | --- | --- |
| 1 | <https://www.ibm360.com/home/s360-front-panels> | Highest-accuracy recreated S/360 front panel illustrations (Models 20–195, 9020); CC BY-NC-SA 4.0. |
| 2 | <https://www.ibm360.info/home/s360-front-panels> | Same project, `.info` domain; also hosts scanned FE documents and real panel photographs. |
| 3 | <http://www.quadibloc.com/comp/panint.htm> | John Savard's front-panel diagram index, S/360 **and** S/370 (incl. Model 165). HTTP only. |
| 4 | <http://www.quadibloc.com/comp/pan05.htm> | Quadibloc S/360 Saga Part II — mid-range panel diagrams. |
| 5 | <http://www.quadibloc.com/comp/pan06.htm> | Quadibloc S/360 Saga Part III — includes the S/370 Model 165 panel diagram. |
| 6 | <http://www.righto.com/2019/04/iconic-consoles-of-ibm-system360.html> | Ken Shirriff: how roller displays, lamp rows and switch banks are organised across models; many hi-res photos. |

### Primary IBM documentation
| # | Reference | What it contains |
| --- | --- | --- |
| 7 | <https://bitsavers.org/pdf/ibm/370/> | Bitsavers /370 root directory — browse for any manual. |
| 8 | <https://www.bitsavers.org/pdf/ibm/370/SR20-4460-0_System_370_Operators_Reference_Guide_Jul74.pdf> | **Definitive description of every /370 panel switch, key and indicator.** |
| 9 | <https://bitsavers.trailing-edge.com/pdf/ibm/370/SR20-4460-2_System_370_Operators_Reference_Guide_Dec76.pdf> | Later, larger edition of the Operator's Reference Guide covering more models. |
| 10 | <https://archive.org/stream/bitsavers_ibm370SR20torsReferenceGuideJul74_5912360/SR20-4460-0_System_370_Operators_Reference_Guide_Jul74_djvu.txt> | Searchable OCR text of the 1974 Operator's Reference Guide. |
| 11 | <https://www.bitsavers.org/pdf/ibm/370/model145/GA24-3554-0_370_Model_145_Operating_Procedures_Sep70.pdf> | /145 operating procedures with console panel figures; IPL via LOAD UNIT rotary switches. |
| 12 | <https://bitsavers.org/pdf/ibm/370/model145/GC38-0015-2_370_145_Operating_Procedures_sep72.pdf> | Later /145 operating procedures. |
| 13 | <https://bitsavers.org/pdf/ibm/370/fe/3145/SY24-3581-1_3145_Processing_Unit_Theory-Maintenance_Oct71.pdf> | **57 MB FE theory/maintenance manual — panel layouts, indicator assignments, lamp circuits.** |
| 14 | <https://bitsavers.org/pdf/ibm/370/fe/3145/SY24-3581-4_3145_Processor_Theory_Maintenance.pdf> | Later revision of the same FE manual. |
| 15 | <https://bitsavers.org/pdf/ibm/370/fe/3145/S124-0129-2_3145_Processing_Unit_Parts_Catalog_Oct75.pdf> | **Exploded parts drawings with IBM part numbers** — pushbuttons, lamp holders, rollers, bezels. |
| 16 | <https://bitsavers.org/pdf/ibm/370/fe/3145/S229-2239-1_370-145_Reference_Summary_Sep72.pdf> | FE quick-reference card set for the /145. |
| 17 | <https://bitsavers.org/pdf/ibm/370/fe/3145/SR25-5608-0_System_370_Model_145_Installation_Instructions_Jul71.pdf> | /145 installation drawings. |
| 18 | <https://bitsavers.org/pdf/ibm/370/funcChar/GA24-3557-3_IBM_370_Model_145_Functional_Characteristics_Aug72.pdf> | /145 architecture + "System Control Panel" section. |
| 19 | <http://bitsavers.trailing-edge.com/pdf/ibm/370/funcChar/GA24-3557-1_370-145_funcChar_Oct70.pdf> | Earlier edition of the above. |
| 20 | <http://www.bitsavers.org/pdf/ibm/370/funcChar/GA22-6942-1_370-155_funcChar_Jan71.pdf> | /155 functional characteristics with the System Control Panel chapter. |
| 21 | <https://sharktastica.co.uk/resources/docs/pdf/IBM_GA22-6942-1_3155-func-chars_1971_bitsavers.pdf> | Mirror of the /155 functional characteristics. |
| 22 | <https://bitsavers.org/pdf/ibm/370/model158/GC20-1754-2_A_Guide_to_the_System_370_Model_158_3rd_ed_197508.pdf> | /158 guide with console photography. |
| 23 | <https://www.bitsavers.org/pdf/ibm/370/systemGuide/GC20-1734-2_370-145_Guide_Aug72.pdf> | /145 overview guide with system photographs. |
| 24 | <https://bitsavers.org/pdf/ibm/370/systemGuide/GC20-1730-0_370-165_Guide_Nov70.pdf> | /165 guide — the largest early /370 panel. |
| 25 | <https://www.bitsavers.org/pdf/ibm/370/princOps/GA22-7000-0_370_Principles_Of_Operation_Jun70.pdf> | **Principles of Operation** — architected "Operator Facilities": resets, IPL, rate control, address compare, indicator semantics. |
| 26 | <http://www.bitsavers.org/pdf/ibm/370/referenceCard/GX20-1850-7_System_370_Reference_Summary_Feb89.pdf> | The "green card": PSW layout, instruction formats, condition codes. |
| 27 | <https://bitsavers.trailing-edge.com/pdf/ibm/370/fe/GC22-7004-14_370_Installation_Manual_Physical_Planning_Jun85.pdf> | Dimensioned cabinet and floor-plan drawings for /370 units. |
| 28 | <https://bitsavers.org/pdf/ibm/370/fe/3125/SY33-1059-1_3125_Processing_Unit_General_Information_Oct73.pdf> | 3125 FE general information — comparison of console documentation style. |
| 29 | <http://bitsavers.informatik.uni-stuttgart.de/pdf/ibm/370/facts_folder/G520-2398-2_370-145_Facts_Folder_197208.pdf> | /145 sales facts folder with clean product photography. |
| 30 | <https://ed-thelen.org/comp-hist/IBM-ProdAnn/370-145.pdf> | Original /145 product announcement with photos. |
| 31 | <https://mark.people.clemson.edu/464/appF.pdf> | Smotherman, "The IBM 360/370 Architecture for Mainframe Computers" — concise architecture summary. |
| 32 | <https://mark.people.clemson.edu/hist.html> | Smotherman's computer architecture history index. |
| 33 | <https://en.wikipedia.org/wiki/IBM_System/370> (+ Model [115](https://en.wikipedia.org/wiki/IBM_System/370_Model_115), [135](https://en.wikipedia.org/wiki/IBM_System/370_Model_135), [145](https://en.wikipedia.org/wiki/IBM_System/370_Model_145), [155](https://en.wikipedia.org/wiki/IBM_System/370_Model_155), [158](https://en.wikipedia.org/wiki/IBM_System/370_Model_158), [165](https://en.wikipedia.org/wiki/IBM_System/370_Model_165), [168](https://en.wikipedia.org/wiki/IBM_System/370_Model_168)) | Per-model specs, dates, console photographs. |

### Photographs, museums, archives
| # | Reference | What it contains |
| --- | --- | --- |
| 34 | <https://commons.wikimedia.org/wiki/Category:IBM_System/370> | Freely licensed /370 photographs and scans. |
| 35 | <https://commons.wikimedia.org/wiki/Category:IBM_System/360_Model_30> | Freely licensed /360 Model 30 imagery. |
| 36 | <https://www.computinghistory.org.uk/det/31058/IBM-System-370-Control-Panel/> | UK museum catalogue entry for a surviving physical /370 control panel. |
| 37 | <https://www.ricomputermuseum.org/collections-gallery/interesting_computer_items/ibm-370-panel> | RICM holds an IBM 370 front panel — contact them for measurements. |
| 38 | <https://www.computerhistory.org/collections/catalog/102646258> | CHM: /370 Model 158 brochure with console photography. |
| 39 | <https://www.computerhistory.org/collections/catalog/102665279> | CHM: /370 Model 145 Functional Characteristics record. |
| 40 | <https://ed-thelen.org/comp-hist/ibm-360-30.html> | Ed Thelen's /360 Model 30 page with photographs. |
| 41 | <http://infolab.stanford.edu/pub/voy/museum/pictures/display/3-1.htm> | Stanford historic /360 installation photographs. |
| 42 | <https://www.flickr.com/photos/tags/ibm360/> | Community /360 photographs, several usable for tracing. |
| 43 | <https://www.flickr.com/photos/carrierdetect/4718559358> | Lawrence Wilkinson's 360/30-on-FPGA photographs. |
| 44 | <https://commons.wikimedia.org/wiki/File:IBM_system_360.JPG> | Freely licensed /360 system photograph. |
| 45 | <https://commons.wikimedia.org/wiki/File:System_370_Reference_Summary.jpg> | Scan of the /370 reference summary card. |
| 46 | <https://news.ycombinator.com/item?id=3196037> | HN thread with photo links and operator recollections. |

### Replica and DIY panel projects
| # | Reference | What it contains |
| --- | --- | --- |
| 47 | <http://ibm360-console.blogspot.com/> | **Operation Blinkenlights** — real /360 Model 65 panel driven by a modified Hercules. Closest prior art. |
| 48 | <http://ibm360-console.blogspot.com/2012_01_01_archive.html> | Its electronics: Velleman K8061 → 74HC595/74HC597 chains (237 out / 183 in) → Arduino Mega 2560; latency 1 s → 1 ms. |
| 49 | <https://ibm360-console.blogspot.com/2012/04/emulator-goes-hardware.html> | Move to a Xilinx XUPV5-LX110T FPGA; level shifters, 50-pin ribbon, HD50 connector. |
| 50 | <http://ibm360-console.blogspot.com/2012/04/source-code-of-fpga-implementation.html> | VHDL source release (`pcie360_0_1_20120413.zip`). |
| 51 | <https://vaxbarn.com/projects/ibm-360-panel> | VAXBARN's page for the same project. |
| 52 | <https://www.vaxbarn.com/component/content/article/390-ibm-360-65?catid=8&Itemid=103> | Background on the /360 Model 65. |
| 53 | <https://vaxbarn.com/cat/360> | VAXBARN's IBM 360 material. |
| 54 | <https://web.archive.org/web/*/ibm360-console.wikispaces.com/*> | Wayback copies of the project wiki holding the **modified Hercules source**. |
| 55 | <https://hercules-390.yahoogroups.narkive.com/0TRePf7v/using-an-ibm-s-360-or-s-370-operator-panel-as-a-hardware-interface-to-the-hercules-emulator> | Hercules list thread: how to drive a real S/360-S/370 panel from Hercules. |
| 56 | <https://obsolescence.dev/pidp-11-building-instructions.html> | PiDP-11 full build guide. |
| 57 | <https://obsolescence.wixsite.com/obsolescence/pidp-11-technical-details> | **PiDP-11 electrical design** — multiplexing, UDN2981, 390 Ω / 1 kΩ, switch scanning, KiCad. |
| 58 | <https://obsolescence.wixsite.com/obsolescence/pidp-10-technical-details> | Same approach scaled to the larger PDP-10 panel. |
| 59 | <https://obsolescence.dev/pidp11/PiDP-11_Manual.pdf> | PiDP-11 user manual. |
| 60 | <https://hackaday.io/project/8069-pidp-11> | PiDP-11 Hackaday.io project log. |
| 61 | <https://hackaday.io/project/8069/logs?sort=newest&page=2> | Earlier PiDP-11 logs on artwork and manufacturing. |
| 62 | <https://www.hackster.io/obsolescence/pidp-11-a-pi-based-replica-of-the-pdp-11-70-1dcda9> | PiDP-11 overview and parts list. |
| 63 | <https://kieranhealy.org/blog/archives/2021/10/09/building-a-pdp-11/70-kit/> | Independent PiDP-11 build with excellent close-up acrylic panel photos. |
| 64 | <https://lannycox.com/2020/04/22/building-the-pidp-8/> | Independent PiDP-8 build log. |
| 65 | <https://groups.google.com/g/pidp-11/c/E-RMRVQ15NQ/m/3S6ln4ANEwAJ> | Gallery of completed PiDP-11 builds. |
| 66 | <https://groups.google.com/g/pidp-8/c/uFkciMFuHHg> | PiDP community panel-construction discussion. |
| 67 | <https://www.makery.info/en/2015/04/06/une-replique-raspberry-pi-du-mythique-pdp-8-des-annees-60/> | Press coverage of the PiDP-8 concept. |
| 68 | <https://github.com/ashlin4010/pdp-11.40-front-panel> | PDP-11/40 front panel project — panel artwork traced from original PDP-11/40 artwork. |
| 69 | <https://github.com/j-hoppe/BlinkenBone> | **BlinkenBone** — framework connecting simulators to real or simulated blinkenlight panels. |
| 70 | <https://github.com/j-hoppe/BlinkenBone/blob/master/projects/07.3_blinkenlight_server_pdp15/gpio.c> | Readable GPIO panel-server implementation (multiplexing, timing, scanning). |
| 71 | <https://github.com/j-hoppe/BlinkenBone/releases> | BlinkenBone prebuilt releases. |
| 72 | <http://www.retrocmp.com/projects/blinkenbone> | BlinkenBone documentation root. |
| 73 | <https://www.retrocmp.com/projects/blinkenbone/176-blinkenbone-download-and-run-simulated-panels-for-free> | Runnable simulated-panel distributions — a packaging model to copy. |
| 74 | <https://www.retrocmp.com/projects/unibone/354-unibone-blinkenbone-panels> | Hardware (BeagleBone + BlinkenCape + BlinkenBoard) for driving real panels. |
| 75 | <https://classiccmp.org/pipermail/cctalk/2018-March/038873.html> | cctalk announcement of photorealistic SimH front panels. |
| 76 | <https://groups.google.com/g/alt.folklore.computers/c/VIw6tJKZx_c> | Original discussion of the simulated PDP-11 blinkenlight panel. |
| 77 | <https://www.mail-archive.com/simh@trailing-edge.com/msg07173.html> | SimH list design discussion on simulator front-panel APIs. |
| 78 | <https://www.ljw.me.uk/ibm360/Saga.html> | **Lawrence Wilkinson's gate-level IBM 360/30 in VHDL**, transcribed from IBM service manuals; VGA panel recreation with microcode-state lights. |
| 79 | <https://www.ljw.me.uk/ibm360/vhdl/> | The complete 360/30 VHDL source and Spartan-3 / Zybo Z7-20 bitstreams. |
| 80 | <https://blog.adafruit.com/2019/06/28/obtaining-an-ibm-system-360-front-panel-vintagecomputing-retrocomputing-ibm/> | Adafruit on CuriousMarc acquiring a real /360 Model 50 panel; notes the IBM replica gap. |
| 81 | <https://hackaday.com/tag/system-360/> | Hackaday's System/360 coverage. |
| 82 | <https://hackaday.com/tag/mainframe/page/2/> | Hackaday's mainframe coverage. |
| 83 | <https://hackaday.com/tag/simh/> | Hackaday's simulator/panel coverage. |
| 84 | <https://groups.google.com/g/altair-duino/c/D1k26Spm6zE> | Altair-Duino community discussing an IBM /360 or /370 panel — an Arduino-driven replica panel community. |
| 85 | <https://forums.whirlpool.net.au/archive/2245918> | Long enthusiast thread on /360 survival and emulation. |

### Mechanical parts
| # | Reference | What it contains |
| --- | --- | --- |
| 86 | <https://www.printables.com/model/165377-ibm-system360-and-370-mainframe-computer-console-p> | **16 STL pushbutton inserts** for real IBM /360-/370 consoles (START, STOP, LOAD, PSW RESTART, …), ≈25.5 × 25.1 × 18.8 mm, parametric OpenSCAD source, CC BY. |
| 87 | <https://cults3d.com/en/3d-model/gadget/ibm-system-360-and-370-mainframe-computer-console-pushbutton-insert> | Same model with printing and finishing instructions (PLA/ABS, 100 % infill, sanding, painting the legend). |

### Hercules emulator
| # | Reference | What it contains |
| --- | --- | --- |
| 88 | <http://www.hercules-390.org/> | Original Hercules project site. |
| 89 | <https://github.com/SDL-Hercules-390/hyperion> | **SDL Hercules 4.x Hyperion — the actively maintained fork.** |
| 90 | <https://github.com/sdl-hercules-390/hyperion/blob/master/README.md> | Build instructions and feature summary. |
| 91 | <https://sdl-hercules-390.github.io/html/> | Current HTML documentation set. |
| 92 | <https://sdl-hercules-390.github.io/html/hercinst.html> | **Installation & Operation — panel / external-GUI / NoUI modes, `--externalgui`, `--NoUI`, `-r` rcfile, HAO, `sh`.** |
| 93 | <https://github.com/SDL-Hercules-390/hyperion/blob/master/readme/README.DAEMON.md> | Headless operation; HTTP server (`HTTP PORT` / `ROOT` / `START`) as the external control channel. |
| 94 | <https://sdl-hercules-390.github.io/html/hercconf.html> | Configuration statements, including CPU model identification. |
| 95 | <https://hercdoc.glanzmann.org/V312/HerculesUserReference.pdf> | **Full command reference — `ipl`, `iplc`, `sysreset`, `sysclear`, `restart`, `start`, `stop`, `store`, `psw`, `gpr`, `cr`, …** Your button-to-command map. |
| 96 | <https://hercdoc.glanzmann.org/V306/HerculesUserReference.pdf> · <https://hercdoc.glanzmann.org/V305/HerculesUserReference.pdf> · <https://hercdoc.glanzmann.org/V308/HerculesUserReference.pdf> | Archived reference guides for older Hercules versions. |
| 97 | <http://www.hercules-390.org/HerculesUserReference.pdf> | Original-site copy of the reference guide. |
| 98 | <https://manualzz.com/doc/o/kscmd/hercules-user-reference-guide---the-hercules-system-370--esa-hercules-console-commands--grouped-by-functionality-> | Browsable HTML list of Hercules console commands grouped by function. |
| 99 | <https://bsp-gmbh.pocnet.net/turnkey/cookbook/hercules/hercinst.html> | Hercules v2 installation/operation document (Turnkey cookbook mirror). |
| 100 | <https://github.com/SDL-Hercules-390/hyperion/blob/master/readme/README.HDL.md> | **Hercules Dynamic Loader** — how to write a loadable module; the clean way to publish panel state. |
| 101 | <https://github.com/sdl-hercules-390/hyperion/blob/master/readme/README.EXTPKG.md> | External package handling when building Hercules. |
| 102 | <https://github.com/sdl-hercules-390/hyperion/blob/master/readme/README.S37X.md> | S/370 instruction extension support. |
| 103 | <https://github.com/SDL-Hercules-390/hyperion/blob/master/readme/README.HERCLOGO.md> | Customising the 3270 logo screen. |
| 104 | <https://github.com/hercules-390/hyperion/issues/150> | Shows where `EXTERNALGUI` / `extgui` lives in the source — entry point for reading the protocol. |
| 105 | <https://hercules-390.yahoogroups.narkive.com/clmlCchf/hercules-console-commands-via-command-line> | Driving Hercules commands programmatically from outside. |
| 106 | <http://www.softdevlabs.com/hercgui.html> | **HercGUI** — the original external-GUI client; displays exactly the data a physical panel needs. HTTP only. |
| 107 | <http://ollydbg.de/Jason/index.htm> | **Jason** — Java front end showing virtual devices; used beside the real panel in Operation Blinkenlights. |
| 108 | <https://www.systutorials.com/docs/linux/man/1-HerculesStudio/> | HerculesStudio (Qt GUI) man page — Linux example of parsing Hercules output. |
| 109 | <https://github.com/haynieresearch/hrdplex-gui> | Another Hercules GUI front end. |
| 110 | <https://moshix.dynu.net/bandke/hercules/wingui/hercgui-faq.html> | Hercules WinGUI FAQ — what the GUI can and cannot show. |
| 111 | <https://en.wikipedia.org/wiki/Hercules_(emulator)> | Overview, history, QPL licensing, emulated architectures. |
| 112 | <https://mdickinson.dyndns.org/hercules/obtaining.php> | Comparison of the Hercules forks — read before cloning. |

### MVS and MVS Turnkey
| # | Reference | What it contains |
| --- | --- | --- |
| 113 | <https://www.prince-webdesign.nl/tk5> | **MVS Tur(n)key 5 (Rob Prins) — the current recommended distribution.** 15 DASD volumes, ready in minutes. |
| 114 | <https://www.prince-webdesign.nl/images/downloads/TK5-Introduction-and-User-Manual.pdf> | **TK5 Introduction and User Manual** — installation, operation, supplied software, Hercules config layout. |
| 115 | <https://www.prince-webdesign.nl/index.php/software/update-on-mvs-turnkey-4> | TK4ROB — the bridge from TK4- to TK5. |
| 116 | <https://wotho.ethz.ch/tk4-/> | **MVS 3.8j Tur(n)key TK4- (Jürgen Winkelmann, ETH Zürich)** — the previous standard; MVS 3.8j on an emulated IBM 3033. |
| 117 | <https://h390-mvs.yahoogroups.narkive.com/0W13Msef/mvs-3-8j-tur-n-key-tk4-system-update-08-available> | TK4- Update 8 release notes. |
| 118 | <https://h390-mvs.yahoogroups.narkive.com/uYfnOiuq/mvs-3-8j-tur-n-key-tk4-system-available> | Original TK4- announcement and its relationship to TK3. |
| 119 | <https://h390-mvs.yahoogroups.narkive.com/lLvuySRO/mvs-3-8j-tur-n-key-tk4-system-update-05-available> | TK4- Update 5 release notes. |
| 120 | <https://github.com/mainframed/tk4/blob/main/CREDITS.md> | TK3 → TK4- lineage and contributor credits. |
| 121 | <https://bsp-gmbh.pocnet.net/turnkey/cookbook/> | **The MVS Tur(n)key New Users Cookbook** (Volker Bandke) — the standard onboarding text. |
| 122 | <https://github.com/joergschultzelutter/tk5-hercules> | TK5 in Docker on Alpine Linux. |
| 123 | <https://github.com/RattyDAVE/docker-ubuntu-hercules-mvs> | Ubuntu + Hercules + MVS container. |
| 124 | <https://hub.docker.com/r/rattydave/docker-ubuntu-hercules-mvs> | Prebuilt image of the above. |
| 125 | <https://github.com/skissane/mvs38j> | MVS 3.8J in Docker. |
| 126 | <https://www.cbttape.org/mvs38.htm> | CBT Tape's MVS 3.8j reference index. |
| 127 | <https://mdickinson.dyndns.org/hercules/obtaining_an_os/obtaining_mvs38j.php> | Comparison of every MVS 3.8j distribution (TK3/TK4-/TK5/MVS-CE/MVS-380). |
| 128 | <https://www.jaymoseley.com/hercules/installMVS/iMVSintroV8.htm> | Jay Moseley's build-MVS-from-the-3.7-starter-system guide. |
| 129 | <https://www.jaymoseley.com/hercules/> | Jay Moseley's Hercules/MVS hub — also the TSO tutorial and MVS FAQ. |
| 130 | <https://github.com/FuzzyMainframes/Awesome-Mainframes> | **Curated index of all mainframe resources** — emulators, OSes, Turnkey distributions, tutorials, communities. |
| 131 | <https://github.com/FuzzyMainframes/Awesome-Mainframes/blob/master/README.md> | The list content itself. |
| 132 | <https://supratim-sanyal.blogspot.com/2020/01/mvs-38-operating-system-on-ibm-3033.html> | Detailed Linux walkthrough of TK4- installation. |
| 133 | <https://bradricorigg.medium.com/run-your-own-mainframe-using-hercules-mainframe-emulator-and-mvs-3-8j-tk4-55fa7c982553> | Step-by-step TK4- tutorial. |
| 134 | <https://bradrigg456.medium.com/run-your-own-mainframe-using-hercules-mainframe-emulator-and-mvs-3-8j-tk4-e8a85ebecd62> | Mirror of the above. |
| 135 | <https://www.mslinn.com/mainframe/2000-hercules.html> | MVS-on-Hercules setup notes. |
| 136 | <https://monadical.com/posts/how-to-run-programs-on-a-mainframe.html> | Beginner's first-JCL-job walkthrough. |
| 137 | <https://kevindurant.be/2019/03/17/mom-part-1-setting-up-my-own-mainframe/> | Blog series on building a home mainframe. |
| 138 | <https://www.maccormac.net/emulate-your-own-mainframe/> | TK5-specific getting-started guide. |
| 139 | <https://lowendbox.com/blog/run-a-8-million-mainframe-at-home-for-free/> | Introduction aimed at small/low-power hosts. |
| 140 | <https://www.suhendro.com/2016/10/look-ma-my-5-pi-zero-thinks-it-is-a-mainframe/> | **Hercules + MVS on a Raspberry Pi Zero** — performance data point for Pi sizing. |
| 141 | <https://www.rs-online.com/designspark/my-raspberry-pi-thinks-it-s-a-mainframe> | Another Pi + Hercules build write-up. |
| 142 | <https://www.askwoody.com/forums/topic/ibm-system-370-on-a-raspberry-pi/> | Forum thread on /370 emulation on the Pi. |
| 143 | <https://medium.com/@vito.rallo/i-built-a-mac-app-to-run-an-ibm-mainframe-running-hercules-and-tk5-natively-on-a-apple-silicon-b625fed07962> | Wrapping Hercules + TK5 in a launcher app — model for your Pi launcher. |
| 144 | <https://github.com/moshix/mvs> | moshix's collection of mainframe scripts and tools. |
| 145 | <https://github.com/GroupTheorist12/mvs_submit_job> | Submitting MVS jobs programmatically. |
| 146 | <https://www.quora.com/Can-IBM-System-360-370-390-programs-be-run-on-a-PC-a-Mac-or-a-Raspberry-Pi> | Orientation on the emulation landscape. |

### Electronics
| # | Reference | What it contains |
| --- | --- | --- |
| 147 | <https://jlcpcb.com/blog/arduino-led-driver-tutorial> | 74HC595 vs MAX7219 for Arduino LED matrices — cascading, brightness, SPI code. |
| 148 | <https://www.etc.cmu.edu/projects/flux/?p=233> | Driving very large LED counts: TLC5940 sinks + MIC5891 sources; cost comparison vs MAX7221. |
| 149 | <https://hackaday.io/page/10259-my-led-matrix-needs-a-little-tlc> | TLC5940 large-matrix build log and gotchas. |
| 150 | <https://forum.arduino.cc/t/16x8-led-matrix-driver-ic/135578> | Comparison of MAX7219 / HT16K33 / shift registers. |
| 151 | <https://forum.arduino.cc/t/red-led-matrix-with-tlc5940/136053> | Practical TLC5940 wiring and code. |
| 152 | <https://forum.arduino.cc/t/max7219-led-matrix/275606> | MAX7219 daisy-chaining in practice. |
| 153 | <https://github.com/michaelkamprath/ShiftRegisterLEDMatrixLib> | Arduino library for shift-register-driven LED matrices — ready-made driver base. |
| 154 | <https://www.digikey.com/es/maker/projects/max7219-8x8-led-matrix-module-arduino-interfacing/3bfeffd9a5b148a5869688ecf40e952d> | DigiKey MAX7219 reference wiring and code. |
| 155 | <https://pcbsync.com/max7219-led-matrix-arduino/> | Complete MAX7219 walkthrough. |
| 156 | <https://neonaut.neocities.org/blog/2018/led-matrixes-1088as-2088rgb-colorduino> | Comparison of matrix modules and driving methods. |
| 157 | <https://www.instructables.com/Magic-Hercules-Driver-for-Digital-LEDs/> | SPI→NZR converter for addressable LEDs (**unrelated to the Hercules emulator** — name collision). |
| 158 | <https://create.arduino.cc/projecthub/p-kard/magic-hercules-driver-for-digital-leds-be361c> | Same module on Arduino Project Hub. |
| 159 | <https://github.com/hzeller/rpi-rgb-led-matrix> | Reference-quality LED matrix timing/PWM from Raspberry Pi GPIO. |
| 160 | <https://github.com/2dom/PxMatrix> | Adafruit-GFX-compatible LED matrix panel driver. |
| 161 | <https://github.com/vitorleal/matrix-led-python> | Python matrix driver for the Raspberry Pi. |
| 162 | <https://github.com/topics/led-panels> | Index of current LED-panel projects and libraries. |

### Laser cutting and panel manufacture
| # | Reference | What it contains |
| --- | --- | --- |
| 163 | <https://www.plaquemaker.com/pages/resources-content/laser-cutting-file-guidelines> | Accepted vector formats (PDF/AI/EPS/CDR/DXF/DWG ≤ AutoCAD 2014); vector-only requirement; minimum stroke. |
| 164 | <https://www.lasercuttingexperts.com.au/acrylic-laser-cutting-thickness-finishes-design-rules-2025-guide> | Fonts to outlines; stencil-safe fonts and bridges; **mirror artwork for reverse engraving**; named etch layer in DXF. |
| 165 | <https://www.xometry.com/resources/sheet/cast-acrylic-cutting/> | Cast acrylic engraves cleanly; extruded acrylic cuts with smoother flame-polished edges. |
| 166 | <https://www.lcsc.com/faqs/front-panels/front-panels-design-specifications> | Concrete minimums: text line width > 0.25 mm second-surface, > 0.15 mm front-surface. |
| 167 | <https://www.novadisplay.com/nova-display-resources/customer-support-pages/submit-artwork-and-specs/submission-guidelines/submission-guidelines-for-laser-cutting-and-engraving/> | Commercial shop's artwork submission checklist. |
| 168 | <https://www.ponoko.com/blog/design-ideas/mounting-and-protecting-custom-pcbs-with-laser-cut-faceplates-panels-and-enclosures/> | Designing a laser-cut faceplate that mounts over a PCB. |
| 169 | <https://www.inventables.com/products/black-and-clear-reverse-laserable-acrylic-sheet> | **Reverse-laserable two-layer acrylic** — engrave from behind, backlight the legend. |
| 170 | <https://www.canalplastic.com/pages/laser-cutting> | Acrylic supplier and cutting service. |
| 171 | <https://vectorsfile.com/> · <https://vecty.co/laser-cut/acrylic> | Free laser-cut vector template libraries (file conventions, not IBM artwork). |

### Books, magazines, video, community
| # | Reference | What it contains |
| --- | --- | --- |
| 172 | <https://direct.mit.edu/books/monograph/4262/IBM-s-360-and-Early-370-Systems> | **Pugh, Johnson & Palmer, *IBM's 360 and Early 370 Systems*** (MIT Press, 1991) — the definitive 810-page history. |
| 173 | <https://archive.org/details/ibms360early370s0000pugh> | Borrowable scan of the same book. |
| 174 | <https://books.google.com/books/about/IBM_s_360_and_Early_370_Systems.html?id=MFGj_PT_clIC> | Google Books entry with previewable content. |
| 175 | <https://www.amazon.com/IBMs-Early-Systems-History-Computing/dp/0262517205> | Print edition, ISBN 9780262517201. |
| 176 | <https://www.goodreads.com/work/editions/1444979-ibm-s-360-and-early-370-systems-history-of-computing> | All editions and ISBNs for second-hand hunting. |
| 177 | <https://www.academia.edu/109239689/> · <https://www.researchgate.net/publication/274770131_> | Scholarly reviews of the Pugh book. |
| 178 | <http://bitsavers.informatik.uni-stuttgart.de/pdf//datapro/datapro_reports_70s-90s/IBM/70C-491-05_7010_IBM_System_370_Model_145.pdf> | **Datapro Report on the /145** — independent evaluation with operator-interface photos. |
| 179 | <https://bitsavers.trailing-edge.com/pdf/datapro/datapro_reports_70s-90s/IBM/70C-491-04_7007_IBM_System_370_Model_155_165.pdf> | Datapro Report on the /155 and /165. |
| 180 | <https://bitsavers.org/pdf/datapro/> | The full Datapro Reports archive. |
| 181 | <https://bitsavers.org/magazines/> | Scanned period computing magazines — IBM ads with clean console photography. |
| 182 | <https://archive.org/details/computermagazines> | Internet Archive's searchable computer magazine collection. |
| 183 | <https://www.ithistory.org/db/hardware/ibm/ibm-system370-model-155> | IT History Society database entry for the /155. |
| 184 | <https://www.youtube.com/@moshix> · <https://www.youtube.com/channel/UCR1ajTWGiUtiAv8X-hpBY7w> | **moshix** — the essential channel for MVS 3.8j / Hercules, incl. "MVS 3.8 on Linux for newcomers". |
| 185 | <https://www.youtube.com/channel/UC3bosUr3WlKYm4sBaLs-Adw> | **CuriousMarc** — restorations of 1960s IBM hardware; owns a real /360 Model 50 panel with 250+ lamps. |
| 186 | <https://www.curiousmarc.com/computing> | CuriousMarc's written companion site with schematics and part sourcing. |
| 187 | <https://www.youtube.com/watch?v=WS-WtjwAAO0> | Video walkthrough of a real IBM System/360 front panel. |
| 188 | <https://www.youtube.com/watch?v=Z8PdWIZFVEk> | Restoring a 1960s IBM I/O Tester — IBM lamp and pushbutton construction in detail. |
| 189 | <https://hackaday.com/2021/12/19/restoring-a-vintage-ibm-i-o-tester/> | Written coverage of the same restoration. |
| 190 | <https://www.youtube.com/watch?v=NU7kSAUSRUo> | The Operation Blinkenlights /360 panel running — LED brightness/refresh reference. |
| 191 | <https://www.youtube.com/@UsagiElectric> | **Usagi Electric** — very early computer restoration; period-correct electronics technique. |
| 192 | <http://www.righto.com/> | **Ken Shirriff's blog** — the best technical writing on vintage IBM hardware. |
| 193 | <https://vaxbarn.com/> | VAXBARN collector site. |
| 194 | <https://obsolescence.dev/> | Oscar Vermeulen's PiDP project home. |
| 195 | <https://groups.google.com/g/pidp-11> · <https://groups.google.com/g/pidp-8> | **The communities to ask acrylic and multiplexing questions in.** |
| 196 | <https://groups.google.com/g/altair-duino> | Arduino-driven Altair 8800 replica community. |
| 197 | <https://groups.io/g/hercules-390> | **Where the Hercules community lives today** — ask panel-integration questions here. |
| 198 | <https://hercules-390.yahoogroups.narkive.com/> | Archive of the old Hercules Yahoo Group. |
| 199 | <https://h390-mvs.yahoogroups.narkive.com/> | Archive of the old MVS-on-Hercules Yahoo Group. |
| 200 | <https://classiccmp.org/pipermail/cctalk/> | The classic computing mailing list archive. |
| 201 | <https://mark.people.clemson.edu/> | Mark Smotherman's mainframe architecture history archive. |
| 202 | <https://ed-thelen.org/comp-hist/> | Ed Thelen's computer history archive. |
| 203 | <https://www.cbttape.org/> | CBT Tape — canonical MVS freeware collection. |
| 204 | <https://www.reddit.com/r/mainframe/> · <https://www.reddit.com/r/retrobattlestations/> | Communities for MVS questions and replica-build feedback. |
| 205 | <https://www.jwtaudio.com/other-interests/retro-computing> | Hobbyist retro computing site with panel material. |
| 206 | <https://duino4projects.com/restoring-a-vintage-ibm-i-o-tester/> | Arduino-community write-up of the IBM I/O Tester restoration. |
| 207 | <https://web.archive.org/> | **The Wayback Machine** — required for the dead Wikispaces wiki, the Yahoo Groups archives and any HTTP-only site that goes offline. |

---

## 16. Gaps in the public record (what you will have to originate)

Being explicit about this so you plan for it:

1. **There is no published cut-ready DXF/SVG of any System/370 panel.** You will produce the first
   one. Budget real time for tracing and dimensional cross-checking.
2. **The best S/370-specific panel artwork (Quadibloc) is hand-drawn and low resolution**; the
   best high-accuracy artwork (ibm360.com) is **System/360**, is **CC BY-NC** (non-commercial),
   and has no published download. If your project is ever to be sold as a kit, contact
   Chris Bigos at ibm360.com/ibm360.info about licensing before you build on it.
3. **No documented external-GUI wire protocol for Hercules.** The format is defined only in the
   `EXTERNALGUI`-guarded source. You will either read the source, or go the HDL-module route, or
   parse the HTTP interface.
4. **Hercules cannot supply microarchitecture-level roller data.** Decide early which roller
   positions are real and which are decorative, and be upfront about it in your documentation.
5. **Several key sources are already lost or offline.** Verified 2026-08-01: `hercules-390.org`
   is **offline**, `wotho.ethz.ch/tk4-` is **offline**, the Operation Blinkenlights wiki is
   **dead and essentially unarchived**, and the narkive Yahoo Groups mirrors return 503.
   Quadibloc and softdevlabs are HTTP-only. **Mirror everything you rely on locally, now.**
   Full status table in [§19](#19-link-health-and-archive-policy).

---

## 17. The IBM 3033 / 303X console: lights, switches, buttons

This section exists because **MVS Turnkey defaults to reporting an IBM 3033**, and it is worth
knowing exactly what that machine's operator interface was before deciding it is not what you
want to build.

### 17.1 The short answer

**The 3033 has no blinkenlights panel.** It is the generation where IBM moved operator control
off a hardwired lamp-and-switch panel and onto a **CRT display driven by a service processor**.
If you replicate a 3033 faithfully, you build a desk with two green-screen terminals on it.

This is why [§1](#1-design-decision-which-370-panel-to-replicate) recommends targeting a
**370/145** instead (the /135, /155 and /165 also have lamp panels, but only the /145 displays
architected data *on those lamps* — see [§20.7](#207-where-the-operator-visible-data-goes-by-model)) —
and why that costs you nothing, since
`CPUMODEL` is [purely cosmetic in Hercules](#72-operating-modes-and-external-control--this-is-the-critical-section-for-your-arduino-link).

### 17.2 What the 3033 operator interface actually consists of

| Element | Detail |
| --- | --- |
| **The console** | The **IBM 3036 Processor Complex Console**, announced 25 March 1977 alongside the 3033 and standard on the 3031, 3032 and 3033. |
| **Physical form** | An **L-shaped desk** with **two workstations**. |
| **Each workstation** | One **service processor**, one **IBM 3277 display station**, and **two 33FD diskette drives**. |
| **The two diskettes** | One is used for **logging hardware errors**; the other **contains the microcode**. |
| **Redundancy** | One service processor is the **master**, the other a **backup**; they can **automatically switch roles** when needed. |
| **Dual operation** | The two display stations can work **in parallel**, so more than one operator task can proceed at once. |
| **Hard switches that do exist** | The console control head carries the **TOD (Time Of Day)** and **EPO (Emergency Power Off)** switches. These, plus power controls, are essentially the only physical operator switches left. |
| **How operator functions are performed** | IPL, system reset, PSW restart, store/display, address compare and rate control are issued **through the display console via the service processor**, as commands and screens — not as dedicated lamps, toggles and rotary switches. |

### 17.3 Why this happened

The 303X generation introduced the **service processor** as an intermediary between the operator
and the CPU. Once a small computer sits between the two, there is no reason to run hundreds of
wires from the CPU's internal registers out to physical lamps: the service processor can read
machine state and *draw* it. This is the direct ancestor of the modern
**HMC (Hardware Management Console)** — and, not coincidentally, the Hercules documentation
describes its own control panel as "roughly equivalent to the HMC on an IBM S/390 mainframe".

**The historical irony worth noting in your project write-up:** Hercules' text panel is
architecturally a 3033-style console, and your acrylic panel will be a 370/145-style console.
You are deliberately going *backwards* one generation — from the service-processor console to
the hardwired lamp panel — which is exactly the interesting part.

### 17.4 Sources for the 3033 and 303X

| Reference | Content |
| --- | --- |
| [GC20-1859-4 — A Guide to the IBM 3033 Processor Complex, Apr 1979](https://www.bitsavers.org/pdf/ibm/3033/GC20-1859-4_3033_ProcessorComplex_Apr79.pdf) | **The primary source, 9.8 MB.** The definitive IBM description of the 3033 and the 3036 console. ⚠️ **This scan has no OCR text layer** — it is page images only, so it cannot be searched or text-extracted. You must page through it visually. The console chapter is where the 3036 layout, workstation contents and operator procedures are documented. |
| [GA22-7060-3 — IBM 3033 Functional Characteristics, Jan 1979](https://bitsavers.org/pdf/ibm/3033/GA22-7060-3_3033_FuncChar_Jan79.pdf) | 3.3 MB. Architecture and machine behaviour, including the operator-facilities section — the 3033 equivalent of the "System Control Panel" chapters in the /145 and /155 manuals. |
| [8271600 — 3033 Processor Complex Installation Instructions, Apr 1982](https://www.bitsavers.org/pdf/ibm/3033/8271600_3033_Processor_Complex_Installation_Instructions_Apr82.pdf) | 7.9 MB. Physical installation, including console placement and cabling — useful for the 3036 desk's dimensions. |
| [Bitsavers /3033 directory](https://www.bitsavers.org/pdf/ibm/3033/) | The complete 3033 holdings — **only these three files.** Note there is **no** FE theory/maintenance manual or parts catalog for the 3033 on Bitsavers, unlike the 3145. This is a second, independent reason to target the /145: the documentation simply is not there for the 3033. |
| [Wikipedia — IBM 303X](https://en.wikipedia.org/wiki/IBM_303X) | 3031 / 3032 / 3033 specifications, dates and the 3036 console description. **3033:** announced 25 March 1977, first shipped 17 March 1978, 60 ns cycle, 64 KB cache, up to 16 MB main storage. **3031 and 3032:** announced 6 October 1977. **All three withdrawn 5 February 1985.** OS support: MVS, OS/VS2 SVS, OS/VS1, VM/370, ACP (the 3031 also supported TSS/370 and DOS/VS). |
| [Wikipedia — IBM 30XX mainframe lines](https://en.wikipedia.org/wiki/IBM_30XX_mainframe_lines) | Overview tying the 303X and 308X families together. |
| [Datapro 70C-491-02 — IBM 3083 product description](https://bitsavers.org/pdf/datapro/datapro_reports_70s-90s/IBM/70C-491-02_8205_IBM_3083.pdf) | Independent evaluation of the follow-on 308X generation, with console coverage. |
| [Hacker News — "A Guide to the IBM 3033 Processor Complex (1979)"](https://news.ycombinator.com/item?id=24195600) | Discussion thread with operator recollections of using the 3036 console in production. |
| [Bob Thomas — "The IBM 3033 mainframe system (nicknamed *The Big One*)"](https://www.linkedin.com/posts/bobthomasesmpubs_mainframe-history-the-ibm-3033-mainframe-activity-7075562789234229248--nE-) | Popular history post with 61 comments, many from people who ran these machines. Anecdotal but a good source of operator detail. |
| [Kent State — System 370 Model 303X page](https://www.cs.kent.edu/~rothstei/10051/history/IBM-370_files/ComputerHistory1.html) | Course page summarising the 303X within the /370 line. |

> **Honest limitation:** the two large 3033 PDFs on Bitsavers are **image-only scans without a
> text layer**, so the detail in §17.2 above is assembled from Wikipedia, IBM's own announcement
> material and secondary summaries rather than transcribed from the manuals. If you need the
> exact 3036 console layout — for instance to confirm whether any indicator lamps remained on the
> processor frame itself — **you must open `GC20-1859-4` and look at the console chapter's
> figures yourself.** Do not treat this section as a substitute for that.

---

## 18. IBM mainframe hardware timeline, 1952–2026

Announce date, end of life, operating systems, and a source link for each generation.

### 18.1 Read this first — what the date columns mean

IBM tracks four distinct dates, and conflating them is the usual source of error:

| Term | Meaning |
| --- | --- |
| **ANN** | **Announcement** of the product. |
| **GA** | **General availability** — when you could actually get one. |
| **HW WDFM** | **Hardware withdrawal from marketing** — IBM stops selling it. |
| **LIC WDFM** | **Licensed Internal Code withdrawal from marketing.** |
| **EOS** | **End of service** — unsupported from this date. |

These definitions are IBM's own, from the *Mainframe Life Cycle History* legend.

**Source discipline used below:** rows from 2000 onward are taken **directly from IBM's own
published life-cycle document** (primary source). Rows before 2000 are from Wikipedia and
contemporary trade press, because IBM's life-cycle document *starts at the year 2000* — it
explicitly covers "the mainframe product life cycle since the introduction of z/Architecture
technology in 2000". **Pre-2000 withdrawal and end-of-service dates are therefore
less reliable and are marked as such.** Where a cell is blank, IBM has not published the date
(usually because it has not happened yet).

### 18.2 The primary source you should bookmark

| Reference | Content |
| --- | --- |
| [**IBM Mainframe Life Cycle History** — landing page (IBM support node 6354755)](https://www.ibm.com/support/pages/node/6354755) · also at [ibm.com/support/pages/ibm-mainframe-life-cycle-history](https://www.ibm.com/support/pages/ibm-mainframe-life-cycle-history) | **The authoritative, IBM-published, continuously updated source** for ANN / GA / HW WDFM / LIC WDFM / EOS for every z-generation machine, plus the z/OS support matrix showing which OS release runs on which server. IBM refreshes it every few months — **always check for a newer version than the one cited here.** *(The IBM site returns 403 to scripted fetches; it downloads normally in a browser, and `curl` with a browser User-Agent works.)* |
| [IBM Mainframe Life Cycle History **V3.1**, 19 November 2025 (PDF)](https://www.ibm.com/support/pages/system/files/inline-files/IBM%20Mainframe%20Life%20Cycle%20History%20V3.1%20-%20November%2019,%202025.pdf) | The edition all figures in §18.4 are taken from. 17 pages. Author: Disha Prashar, IBM Canada. |
| [V3.0, 8 April 2025 (PDF)](https://www.ibm.com/support/pages/system/files/inline-files/IBM%20Mainframe%20Life%20Cycle%20History%20V3.0%20-%20April%208,%202025.pdf) · [V2.14, 10 October 2023 (PDF)](https://www.ibm.com/support/pages/system/files/inline-files/IBM%20Mainframe%20Life%20Cycle%20History%20V2.14%20-%20October%2010%202023_0.pdf) | Earlier editions — useful because IBM sometimes *revises* planned dates, so the older editions show what was previously planned. ⚠️ **These two returned 403 even with a browser User-Agent on 2026-08-01** (V3.1 downloaded fine). Reach them by clicking through from the [landing page](https://www.ibm.com/support/pages/node/6354755) in a real browser. |
| [IBM — "History and Evolution of IBM Mainframes" (SHARE session 17217, 2015)](https://share.confex.com/share/125/webprogram/Handout/Session17217/History%20and%20Evolution%20of%20IBM%20Mainframes%202015-08-04.pdf) | An IBM-authored conference presentation citing **IBM Archives** as its source, covering the whole line from the 1950s. Fills the pre-2000 gap with IBM-sourced material. *(Host was unreachable on 2026-08-01 — try again, or use [the Wayback Machine](https://web.archive.org/web/*/share.confex.com/share/125/webprogram/Handout/Session17217/*).)* |
| [Computer Museum UK — "A Brief History of the IBM ES/9000, System/390 and zSeries 1990–" (PDF)](https://www.computermuseum.org.uk/fixed_pages/sys390.pdf) | Independent, well-referenced history bridging 1990 to the zSeries era. |
| [Jay Moseley — "IBM Mainframe Operating Systems: Timeline and Brief Explanation" (PDF)](https://www.jaymoseley.com/hercules/downloads/pdf/$OSTL33.pdf) | The operating-system counterpart to this hardware timeline. |
| [Wikipedia — History of IBM mainframe operating systems](https://en.wikipedia.org/wiki/History_of_IBM_mainframe_operating_systems) | Well-cited overview of how OS/360 → OS/VS2 → MVS → MVS/XA → MVS/ESA → OS/390 → z/OS descend from one another. |
| [Wikipedia — IBM mainframe](https://en.wikipedia.org/wiki/IBM_mainframe) | Top-level index of every generation, with links to per-machine articles. |

### 18.3 Pre-z/Architecture: 1952 – 1999

⚠️ **Dates in this table are from secondary sources** (Wikipedia, Datapro, contemporary trade
press). Announcement dates are generally reliable; **withdrawal dates are patchier and
end-of-service dates are mostly unrecorded** for this era. Verify anything load-bearing against
[IBM Archives](https://www.ibm.com/history) or the original announcement letter.

| Generation | Announced | Withdrawn / end of life | Operating systems | Source |
| --- | --- | --- | --- | --- |
| **IBM 701** "Defense Calculator" | Unveiled **7 April 1953** | Superseded by the 704 (1954) | None — bare machine, then user-written monitors. IBM's own [*Principles of Operation: Type 701*](https://archive.org/details/type-701-and-associated-equipment) (1953) is the manual. | [Wikipedia — IBM 700/7000 series](https://en.wikipedia.org/wiki/IBM_700/7000_series) |
| **IBM 700/7000 series** (702, 704, 705, 709, 7090, 7040, 7070, 7080, 7094) | **1953–1962** by model | Displaced by S/360 from 1965; most withdrawn late 1960s | SOS (SHARE Operating System), FMS (FORTRAN Monitor System), **IBSYS**; 7090/7094 were the scientific workhorses | [Wikipedia — IBM 700/7000 series](https://en.wikipedia.org/wiki/IBM_700/7000_series) |
| **IBM 1401 / 1400 series** | **5 October 1959** | **Withdrawn 1971** | No OS initially; 1401 Symbolic Programming System, tape monitors. The machine that made IBM dominant pre-S/360. | [Wikipedia — IBM 1400 series](https://en.wikipedia.org/wiki/IBM_1400_series) · [Columbia — The IBM 1401](https://www.columbia.edu/cu/computinghistory/1401.html) · [ibm-1401.info](https://ibm-1401.info/1401GuidePosterV9.html) · [1959 brochure](https://archive.org/details/ibm-1401-brochure-searchable) |
| **IBM 1410 / 7010** | 1960 / 1962 | Late 1960s | Tape and disk operating systems for the 1410 | [Wikipedia — IBM 1410](https://en.wikipedia.org/wiki/IBM_1410) |
| **System/360** (Models 20, 22, 25, 30, 40, 44, 50, 65, 67, 75, 85, 91, 95, 195) | **7 April 1964**; delivered from 1965 | Line delivered 1965–1978; superseded by S/370 from 1970 | **BOS/360, BPS, TOS/360, DOS/360, OS/360 (PCP, MFT, MVT)**; on the Model 67: **TSS/360** and **CP-67/CMS** (the ancestor of VM) | [Wikipedia — IBM System/360](https://en.wikipedia.org/wiki/IBM_System/360) · [CHM "This Day in History"](https://www.computerhistory.org/tdih/april/7/) · [ETHW](https://ethw.org/IBM_System/360) · [IEEE Spectrum](https://spectrum.ieee.org/building-the-system360-mainframe-nearly-destroyed-ibm) · [CHM Revolution](https://www.computerhistory.org/revolution/mainframe-computers/7/161) |
| **System/370** (115, 125, 135, 138, 145, 148, 155, 158, 165, 168) | **30 June 1970** | Superseded by 303X from 1977; individual models withdrawn late 1970s–early 1980s | **DOS/VS, OS/VS1, OS/VS2 SVS, OS/VS2 MVS** (release 3.8j is what you will run), **VM/370**, TSS/370, ACP | [Wikipedia — IBM System/370](https://en.wikipedia.org/wiki/IBM_System/370) · [Principles of Operation, 1970](https://www.bitsavers.org/pdf/ibm/370/princOps/GA22-7000-0_370_Principles_Of_Operation_Jun70.pdf) — **this is the generation your panel replicates** |
| **303X** — **3033** | **25 March 1977**; first shipped **17 March 1978** | **Withdrawn 5 February 1985** | MVS, OS/VS2 SVS, OS/VS1, VM/370, ACP | [Wikipedia — IBM 303X](https://en.wikipedia.org/wiki/IBM_303X) · [§17](#17-the-ibm-3033--303x-console-lights-switches-buttons) |
| **303X** — **3031 and 3032** | **6 October 1977** | **Withdrawn 5 February 1985** | As 3033; the 3031 also ran **TSS/370** and **DOS/VS** | [Wikipedia — IBM 303X](https://en.wikipedia.org/wiki/IBM_303X) |
| **4300 series** (4331, 4341, later 4361, 4381) | **30 January 1979** | **4341 withdrawn 11 February 1986** | **DOS/VSE**, VM/370, VM/SP, MVS | [Wikipedia — IBM 4300](https://en.wikipedia.org/wiki/IBM_4300) · [Datapro 70C-491-08](https://www.bitsavers.org/pdf/datapro/datapro_reports_70s-90s/IBM/70C-491-08_8109_IBM_4300.pdf) |
| **308X** — **3081** | **12 November 1980** | **Withdrawn 4 August 1987** | MVS/SP, **MVS/XA** (31-bit addressing arrives here), VM/SP, VM/XA, DOS/VSE | [Wikipedia — IBM 308X](https://en.wikipedia.org/wiki/IBM_308X) |
| **3090** (Models 200, 400, later 600E etc.) | **12 February 1985** | **Models 200/400 withdrawn 5 May 1989** | MVS/XA, **MVS/ESA**, VM/XA, VM/ESA, VSE/SP | [Wikipedia — IBM 3090](https://en.wikipedia.org/wiki/IBM_3090) · [Datapro 70C-504MK-70](http://bitsavers.informatik.uni-stuttgart.de/pdf/datapro/datapro_reports_70s-90s/IBM/70C-504MK-70_8504_IBM_3090.pdf) |
| **ES/9000 and System/390 (ESA/390 architecture)** | **5 September 1990** — both announced the same day | ES/9000 models withdrawn through the late 1990s | **MVS/ESA**, VM/ESA, VSE/ESA | [Wikipedia — IBM System/390](https://en.wikipedia.org/wiki/IBM_System/390) · [Computer Museum UK history PDF](https://www.computermuseum.org.uk/fixed_pages/sys390.pdf) · [IBM ES/9000 9221 withdrawal notice](https://www.ibm.com/support/pages/node/7094086) |
| **S/390 Parallel Enterprise Server (9672)** — the CMOS transition | Unveiled and shipping **September 1994**; generations G1–G6 through 1999 | Superseded by zSeries from 2000 | MVS/ESA, **OS/390**, VM/ESA, VSE/ESA, TPF; later **Linux/390** | [Wikipedia — IBM System/390](https://en.wikipedia.org/wiki/IBM_System/390) · [IBM 9672-R25 withdrawal notice](https://www.ibm.com/support/pages/node/7093198) · [IBM S/390 Parallel Transaction Server announcement](https://www.ibm.com/common/ssi/cgi-bin/ssialias?infotype=DD&subtype=SM&htmlfid=872/ENUS9672-_h01) |
| **IBM Multiprise 2000 / 3000** | 1996 / 1999 | Superseded by zSeries | OS/390, VM/ESA, VSE/ESA | [Wikipedia — IBM Multiprise](https://en.wikipedia.org/wiki/IBM_Multiprise) |

### 18.4 z/Architecture era: 2000 – 2026 — **IBM primary source**

Every date in this table is transcribed from **IBM Mainframe Life Cycle History V3.1
(19 November 2025)**. Blank cells mean IBM has not published that date. Operating systems for the
whole era are **z/OS, z/VM, z/VSE (now z/TPF and Linux on Z), z/TPF and Linux on IBM Z**; the
z/OS-release-to-server matrix is in §18.5.

| Machine type / model | Family | Announced | GA | HW withdrawal | LIC withdrawal | End of service |
| --- | --- | --- | --- | --- | --- | --- |
| 2064 1nn | **z900 G1** | 3 Oct 2000 | 18 Dec 2000 | 30 Jun 2006 | — | 31 Dec 2014 |
| 2066 | **z800** | 19 Feb 2002 | 29 Mar 2002 | 31 Dec 2005 | — | 31 Dec 2014 |
| 2064 2nn | **z900 G2** | 30 Apr 2002 | 15 May 2002 | 30 Jun 2006 | — | 31 Dec 2014 |
| 2084 | **z990** | 13 May 2003 | 16 Jun 2003 | 30 Jun 2008 | — | 31 Dec 2014 |
| 2086 A04 | **z890** | 7 Apr 2004 | 28 May 2004 | 31 Dec 2007 | — | 31 Oct 2016 |
| 2094 Snn | **z9 EC** | 26 Jul 2005 | 16 Sep 2005 | 30 Jun 2010 | — | 31 Oct 2017 |
| 2096 R07/S07 | **z9 BC** | 27 Apr 2006 | 26 May 2006 | 30 Jun 2010 | — | 31 Jan 2019 |
| 2097 Enn | **z10 EC** | 26 Feb 2008 | 26 Feb 2008 | 30 Jun 2012 | 30 Jun 2013 | 31 Dec 2019 |
| 2098 E10 | **z10 BC** | 21 Oct 2008 | 28 Oct 2008 | 30 Jun 2012 | 30 Jun 2013 | 31 Dec 2019 |
| 2817 Mnn | **z196** | 22 Jul 2010 | 10 Sep 2010 | 30 Jun 2014 | 30 Jun 2015 | 31 Dec 2021 |
| 2818 Mnn | **z114** | 12 Jul 2011 | 9 Sep 2011 | 30 Jun 2014 | 30 Jun 2015 | 31 Dec 2022 |
| 2827 Hnn | **zEC12** | 28 Aug 2012 | 19 Sep 2012 | 31 Dec 2016 | 31 Dec 2017 | 31 Dec 2023 |
| 2828 Hnn | **zBC12** | 23 Jul 2013 | 20 Sep 2013 | 31 Dec 2016 | 31 Dec 2017 | 31 Dec 2023 |
| 2964 Nnn | **z13** | 14 Jan 2015 | 9 Mar 2015 | 30 Jun 2019 | 30 Jun 2020 | 31 Dec 2024 |
| 2965 Nnn | **z13s** | 16 Feb 2016 | 10 Mar 2016 | 30 Jun 2019 | 30 Jun 2020 | 31 Dec 2024 |
| 3906 M0n | **z14** | 17 Jul 2017 | 13 Sep 2017 | 30 Jun 2021 | — | 30 Jun 2022 |
| 3907 ZR1 | **z14 ZR1** | 10 Apr 2018 | 31 May 2018 | 30 Sep 2021 | — | 30 Sep 2022 |
| 8561 T01 | **z15** | 12 Sep 2019 | 23 Sep 2019 | 31 Dec 2023 | — | 31 Dec 2024 |
| 8562 T02 | **z15 T02** | 14 Apr 2020 | 15 May 2020 | 30 Jun 2024 | — | 30 Jun 2025 |
| 3931 A01 | **z16** | 5 Apr 2022 | 31 May 2022 | 31 Dec 2025 | — | 31 Dec 2026 |
| 3932 A02 | **z16 A02** | 4 Apr 2023 | 17 May 2023 | — | — | — |
| **9175 ME1** | **z17** | **8 Apr 2025** | **18 Jun 2025** | — | — | — |

**The current machine** as of this document's date is the **IBM z17 (machine type 9175, model
ME1)**, announced 8 April 2025 and generally available 18 June 2025. The corresponding Linux-only
line is **LinuxONE 5 (9175-ML1)**; the previous generation was **LinuxONE 4 (3931-LA1)** and
**LinuxONE III (8561-LT1)**.

IBM's own averages across this era: **0.1 years** from announcement to GA, **4.0 years** from GA
to hardware withdrawal, and **7.6 years** from hardware withdrawal to end of service — so a
typical z machine is supported for roughly **11–12 years** after GA.

### 18.5 z/OS release support by machine — **IBM primary source**

Also from Life Cycle History V3.1. `(*)` marks dates IBM labels as *planned* and therefore subject
to change.

| z/OS release | GA | Withdrawn from marketing | End of service | Extended defect support |
| --- | --- | --- | --- | --- |
| **z/OS V2.3** | Sep 2017 | Jan 2020 | Sep 2022 | Sep 2025 (*) |
| **z/OS V2.4** | Sep 2019 | Jan 2022 | Sep 2024 | Sep 2027 (*) |
| **z/OS V2.5** | Sep 2021 | Jan 2024 | Sep 2026 (*) | Sep 2029 (*) |
| **z/OS 3.1** | Sep 2023 | Jan 2026 (*) | Sep 2028 (*) | Sep 2031 (*) |
| **z/OS 3.2** | Sep 2025 | Jan 2028 (*) | Sep 2030 (*) | Sep 2033 (*) |

Server support, per the same document: z/OS V2.3 and V2.4 run on zEC12/zBC12 through z16;
**z/OS V2.5, 3.1 and 3.2 run on the z17**; z/OS 3.2 requires z15 or later.

### 18.6 Where your project sits on this timeline

- **The panel you are building** replicates the **System/370** generation — announced 30 June
  1970, the generation whose consoles still had rollers, lamp banks and rotary switches.
- **The operating system you will run**, MVS 3.8j, is **OS/VS2 MVS Release 3.8**, a genuine
  1970s System/370 operating system — which is precisely why it is in the public domain and why
  the hobby community can use it at all.
- **The emulator** implements S/370, ESA/390 and z/Architecture, so it spans the entire timeline
  from 1970 to the present.
- **The gap you are closing** is that between 1977 (the 303X, when IBM took the lamps away) and
  today: no IBM machine built since has had a blinkenlights operator panel, and no one has yet
  published a faithful replica of one.

---

## 19. Link health and archive policy

**Every URL in this document was HTTP-checked on 2026-08-01.** Of 228 unique URLs, the results
below are the only ones that did not return `200 OK`. Everything not listed here was live.

### 19.1 Genuinely dead — use the replacement

| Dead URL | Status | What to use instead |
| --- | --- | --- |
| `http://www.hercules-390.org/` | **Offline** (connection fails on `http`, `https`, `www` and bare host) | Docs → [hercules-390.github.io/html/](https://hercules-390.github.io/html/) · Code → [github.com/hercules-390/hyperion](https://github.com/hercules-390/hyperion) · Archive → [Wayback 2026-05-02](http://web.archive.org/web/20260502060042/http://www.hercules-390.org/) |
| `http://www.hercules-390.org/HerculesUserReference.pdf` | **Offline** | [Wayback 2025-12-05](http://web.archive.org/web/20251205060137/http://www.hercules-390.org/HerculesUserReference.pdf) · or the live [hercdoc.glanzmann.org V3.12 copy](https://hercdoc.glanzmann.org/V312/HerculesUserReference.pdf) |
| `https://wotho.ethz.ch/tk4-/` | **Offline** | **Live mirror → [wotho.pebble-beach.ch/tk4-/](https://wotho.pebble-beach.ch/tk4-/)** · Archive → [Wayback 2023-03-23](http://web.archive.org/web/20230323192244/https://wotho.ethz.ch/tk4-/) |
| `http://ibm360-console.wikispaces.com/` | **Permanently dead** (Wikispaces closed 2018) | **Nothing usable exists.** The [CDX query](http://web.archive.org/cdx/search/cdx?url=ibm360-console.wikispaces.com*&output=text&fl=timestamp,original,statuscode&collapse=urlkey) returns only a root 302, a favicon, `robots.txt` and one 402-paywalled file. Ask on [groups.io/g/hercules-390](https://groups.io/g/hercules-390). |
| `https://vaxbarn.com/cat/360` | **404** (site restructured) | [Wayback 2025-11-19](http://web.archive.org/web/20251119204040/https://vaxbarn.com/cat/360) · or start from [vaxbarn.com](https://vaxbarn.com/) |
| `https://www.vaxbarn.com/component/content/article/390-ibm-360-65?...` | **404** | [Wayback index for the host](https://web.archive.org/web/*/vaxbarn.com/*) |
| `https://www.ithistory.org/db/hardware/ibm/ibm-system370-model-155` | **404** | [Wayback 2025-10-02](http://web.archive.org/web/20251002163523/https://www.ithistory.org/db/hardware/ibm/ibm-system370-model-155) · site root [ithistory.org](https://www.ithistory.org/) is live |
| `https://www.youtube.com/@moshix` | **404** (handle changed) | [youtube.com/c/moshix](https://www.youtube.com/c/moshix) · [channel by ID](https://www.youtube.com/channel/UCR1ajTWGiUtiAv8X-hpBY7w) |
| `https://en.wikipedia.org/wiki/IBM_System/370_Model_158` | **404** (article does not exist) | [IBM System/370](https://en.wikipedia.org/wiki/IBM_System/370) · [Model 148](https://en.wikipedia.org/wiki/IBM_System/370_Model_148) · the Bitsavers [/158 guide](https://bitsavers.org/pdf/ibm/370/model158/GC20-1754-2_A_Guide_to_the_System_370_Model_158_3rd_ed_197508.pdf) |
| `http://pidp.net/pidp11/PiDP-11_Manual.odt` | **406** | [Wayback 2024-11-09](http://web.archive.org/web/20241109013654/https://pidp.net/pidp11/PiDP-11_Manual.odt) · or the live [PDF version](https://obsolescence.dev/pidp11/PiDP-11_Manual.pdf) |
| `https://share.confex.com/.../History and Evolution of IBM Mainframes...pdf` | **DNS failure** on 2026-08-01 | [Wayback index](https://web.archive.org/web/*/share.confex.com/share/125/webprogram/Handout/Session17217/*) — retry the live host first, it may be transient |

### 19.2 Overloaded, not deleted — retry or use the successor

| URL | Status | Note |
| --- | --- | --- |
| `hercules-390.yahoogroups.narkive.com` (host and all threads) | **503** | narkive is a third-party mirror that overloads. **503 is transient, not deletion.** The [Wayback host index](https://web.archive.org/web/*/hercules-390.yahoogroups.narkive.com/*) holds many threads from 2021–2024 — but **not** the operator-panel thread. Live successor: [groups.io/g/hercules-390](https://groups.io/g/hercules-390). |
| `h390-mvs.yahoogroups.narkive.com` (host and all threads) | **503** | Same situation. The [TK4- announcement is archived](http://web.archive.org/web/20250604125220/https://h390-mvs.yahoogroups.narkive.com/uYfnOiuq/mvs-3-8j-tur-n-key-tk4-system-available). Live successor: [groups.io/g/H390-MVS](https://groups.io/g/H390-MVS). |

### 19.3 Alive but bot-blocked — **these work fine in a browser**

Do **not** mistake these for dead links. They return `403` only to automated requests:

[printables.com](https://www.printables.com/model/165377-ibm-system360-and-370-mainframe-computer-console-p) ·
[blog.adafruit.com](https://blog.adafruit.com/2019/06/28/obtaining-an-ibm-system-360-front-panel-vintagecomputing-retrocomputing-ibm/) ·
[direct.mit.edu](https://direct.mit.edu/books/monograph/4262/IBM-s-360-and-Early-370-Systems) ·
[duino4projects.com](https://duino4projects.com/restoring-a-vintage-ibm-i-o-tester/) ·
[manualzz.com](https://manualzz.com/doc/o/kscmd/hercules-user-reference-guide---the-hercules-system-370--esa-hercules-console-commands--grouped-by-functionality-) ·
[askwoody.com](https://www.askwoody.com/forums/topic/ibm-system-370-on-a-raspberry-pi/) ·
[digikey.com](https://www.digikey.com/es/maker/projects/max7219-8x8-led-matrix-module-arduino-interfacing/3bfeffd9a5b148a5869688ecf40e952d) ·
[novadisplay.com](https://www.novadisplay.com/nova-display-resources/customer-support-pages/submit-artwork-and-specs/submission-guidelines/submission-guidelines-for-laser-cutting-and-engraving/) ·
[researchgate.net](https://www.researchgate.net/publication/274770131_IBM's_360_and_Early_370_Systems_By_Emerson_W_Pugh_Lyle_R_Johnson_and_John_H_Palmer_Cambridge_Mass_MIT_Press_1991_xx_810_pp_Charts_illustrations_appendixes_notes_references_and_index_3750) ·
[ibm.com support pages](https://www.ibm.com/support/pages/ibm-mainframe-life-cycle-history)
(the IBM PDFs download correctly with a browser User-Agent).

### 19.4 HTTP-only — alive, but will not load over HTTPS

These returned `200` over plain HTTP and refuse connections on port 443. Browsers handle them
fine; automated tools that force HTTPS will fail:

[quadibloc.com/comp/panint.htm](http://www.quadibloc.com/comp/panint.htm)
([Wayback](http://web.archive.org/web/20260515082049/http://quadibloc.com/comp/panint.htm)) ·
[quadibloc.com/comp/pan05.htm](http://www.quadibloc.com/comp/pan05.htm) ·
[quadibloc.com/comp/pan06.htm](http://www.quadibloc.com/comp/pan06.htm) ·
[softdevlabs.com/hercgui.html](http://www.softdevlabs.com/hercgui.html)
([Wayback](http://web.archive.org/web/20260422210041/http://softdevlabs.com/hercgui.html)) ·
[ollydbg.de/Jason/index.htm](http://ollydbg.de/Jason/index.htm) ·
[retrocmp.com/projects/blinkenbone](http://www.retrocmp.com/projects/blinkenbone) ·
[ibm360-console.blogspot.com](http://ibm360-console.blogspot.com/) ·
[righto.com](http://www.righto.com/)

**Because Quadibloc is the only substantial source of S/370-specific panel diagrams and is
HTTP-only on a personal domain, mirror it locally today.**

### 19.5 How to find a replacement yourself

When any link here dies, in this order:

1. **Wayback availability API** — returns the closest snapshot as JSON:
   `https://archive.org/wayback/available?url=EXAMPLE.COM/page`
2. **Wayback CDX API** — lists *every* capture, so you can tell "never archived" from
   "archived under a different URL":
   `http://web.archive.org/cdx/search/cdx?url=EXAMPLE.COM*&output=text&fl=timestamp,original,statuscode&collapse=urlkey`
3. **Try `http://` instead of `https://`**, and the bare host without `www` — several sites here
   are alive only on one of those.
4. **Look for a community mirror.** `wotho.pebble-beach.ch` was found this way; when a primary
   Turnkey or Hercules site dies, someone posts a mirror on
   [groups.io/g/H390-MVS](https://groups.io/g/H390-MVS) within days.
5. **Check Bitsavers' mirrors** if a manual URL fails. These four were verified live on
   2026-08-01 and carry the same tree, so you can swap the hostname and keep the path:
   [`bitsavers.org`](https://bitsavers.org/pdf/ibm/370/) ·
   [`bitsavers.trailing-edge.com`](https://bitsavers.trailing-edge.com/pdf/ibm/370/) ·
   [`bitsavers.informatik.uni-stuttgart.de`](http://bitsavers.informatik.uni-stuttgart.de/pdf/ibm/370/) ·
   [`ftpmirror.your.org/pub/misc/bitsavers/`](http://ftpmirror.your.org/pub/misc/bitsavers/pdf/ibm/370/).
   ⚠️ **`bitsavers.computerhistory.org` no longer resolves** — if a search engine hands you a URL
   on that host, rewrite it to `bitsavers.org` and it will work.

---

## 20. Which panel best matches the signals Hercules can actually supply?

**Answer: the IBM System/370 Model 145 (3145).** Not as a compromise — it is genuinely the best
*technical* match, and this section proves it from IBM's own manual rather than by inference.

**Source for everything below:**
[GA24-3554-0, *IBM System/370 Model 145 Operating Procedures*, September 1970](https://www.bitsavers.org/pdf/ibm/370/model145/GA24-3554-0_370_Model_145_Operating_Procedures_Sep70.pdf),
chapter "Console Indicators, Switches, and Keys" (pages 8–23). **This PDF has a real text layer**
— unlike the 3033 manuals — so you can search it and copy exact legend text for your silkscreen.

### 20.1 The selection principle

A /370 panel lamp is fed by one of two kinds of signal:

- **Architected state** — PSW, instruction address, condition code, storage contents, registers,
  CPU running/stopped/wait, IPL in progress. **Defined by the architecture**, therefore present in
  *any* correct S/370 implementation, therefore **available in Hercules.**
- **Microarchitectural state** — the 3145's own M, B, Z, D and C registers, storage data bus-out,
  MCKA, the microcode sequencer. **Specific to how IBM built that particular machine.** Hercules
  has no such registers, so these signals **do not exist** and cannot be produced.

So the question "which panel matches Hercules?" reduces to: **which /370 panel has the highest
proportion of architected lamps to microarchitectural lamps?** The answer is the low- and
mid-range models, and the /145 is the best-documented of them.

### 20.2 Why the /145 wins — the decisive detail

The /145 has **only two roller switches** (compared with four on a /360 Model 50 and six on a
Model 65), and — this is the key finding — **IBM's own manual marks most of their positions
"for service use":**

| Roller | Positions | Verdict |
| --- | --- | --- |
| **A-REGISTER DISPLAY** | Position **1** = *Storage or External Register*, selected by the STORAGE SELECT switch. **Positions 2–8 are footnoted "for service use"** (TI/TA/TT/TE, S/P/T/L, System Register, channel words). | **Position 1 is fully drivable** from Hercules storage and register display. And the manual states: *"When the CPU is in a soft-stopped state (MANUAL indicator on), the indicators display the next instruction address."* — **that is the PSW instruction address, directly available.** |
| **DISPLAY ASSEMBLER OUT** | Position 1 = M-Register bytes 1–3 + protect stack key; position 2 = Storage Data Bus-Out / selected channel. **Positions 3–8 are footnoted "for service use"** (C, MB2/MB3/N2/N3, B, Z, D registers, MCKA). | **Positions 3–8 are pure 3145 microarchitecture — not drivable.** Wire them to a static or decorative pattern and document that honestly. |

**In other words, on a /145 the operator-relevant roller content is roughly two positions out of
sixteen, and both of those are architected.** On a /165 or /168 you would be building far more
lamps whose content Hercules cannot supply.

### 20.3 The /145's five system indicators — all drivable

The manual gives the exact logic. Every one of these can be computed from state Hercules exposes:

| Lamp | IBM's definition | How you drive it |
| --- | --- | --- |
| **SYSTEM** | "on when CPU operations are in progress and either use meter is running" | Hercules CPU is started and executing. |
| **MANUAL** | "on when the CPU clock is stopped or the system is in a soft-stop state. All pending interrupts are handled. **Manual store/display operations are possible only when the MANUAL indicator is on**" | Hercules CPU stopped (`stop` command / stopped state). Also gates your panel's store/display functions — enforce this in firmware. |
| **WAIT** | "on when the system is in a wait state (CPU clock running but no instruction processing taking place)" | **PSW wait bit.** Directly available. |
| **TEST** | "on when any of the following switches are not in the process or normal position: 1. RATE, 2. CHECK CONTROL, 3. DIAGNOSTIC/CONSOLE FILE CONTROL, 4. ADDRESS COMPARE CONTROL" | **Needs no emulator data at all** — it is a pure OR of four of your own switch positions. **Compute it in the Arduino.** A lovely piece of authenticity you get for free. |
| **LOAD** | "on when the Initial Program Load (IPL) is in progress. It turns on when the LOAD key is pressed and turns off when the initial PSW is loaded successfully" | Set on when you issue `ipl`, clear when Hercules reports the CPU running from the loaded PSW. |

### 20.4 The /145's switches are almost all *inputs* — which is the easy direction

Inputs are trivially handled by the Arduino and need nothing from Hercules. The /145 is unusually
input-heavy, which works in your favour:

| Control | IBM's function | Maps to |
| --- | --- | --- |
| **Rotary switches A–H** (eight hex thumbwheels) | **A,B** = DATA (value for manual store) · **C,D** = CF ADDRESS · **E,F,G,H** = BYTE COUNT · **F,G,H** = MAIN STORAGE ADDRESS (for store/display **and address compare**) · **H** = WORD ADDRESS (to display General-Purpose and Floating-Point registers) · **LOAD UNIT ADDRESS** (the IPL device) · STORE/DISPLAY ADDRESS · BYTE/X-LATE REGS | Read the wheels, compose the address/data, and issue the matching Hercules command. **LOAD UNIT feeds `ipl xxxx` directly.** |
| **RATE switch** — PROCESS / INSTRUCTION STEP (+ SINGLE CYCLE, HARD STOP for service) | "INSTRUCTION STEP: One complete machine language instruction (including all pending interrupts allowed by the system mask) is executed for each operation of the START key. The machine enters the soft-stop state" | PROCESS → `start`; INSTRUCTION STEP → Hercules single-step per START press. **A near-perfect one-to-one mapping.** |
| **ADDRESS COMPARE** + **ADDRESS COMPARE CONTROL** | Stop or trap when a storage address matches the FGH wheels | Hercules **breakpoint** (`b` command). Genuinely equivalent. |
| **STORAGE SELECT** (incl. **LOCAL STORAGE** position) | "used for manual store and display of General-Purpose and Floating-Point registers" | Selects whether display/store targets main storage (`r`/`v`) or registers (`gpr`/`fpr`). |
| **CHECK CONTROL** — PROCESS / STOP AFTER LOG (+ DISABLE, HARD STOP) | Action on a machine check | No Hercules equivalent for real machine checks. Wire it into the **TEST** lamp logic (§20.3) and leave it functionally inert — which is *correct*, since a healthy machine never exercises it. |
| **DIAGNOSTIC/CONSOLE FILE CONTROL** — PROCESS/IMPL + service positions | Console file and diagnostic functions | Same: feeds the TEST lamp, otherwise inert. |
| **LAMP TEST** key | "All console indicators should light when the LAMP TEST key is operated… can be operated at any time without affecting system operation" | **Implement this — it is one line of Arduino code and it is the single most satisfying authentic detail on the whole panel.** |
| **Use meters** (customer / service) + key switch | Two direct-reading meters recording CPU operating time, selected by a key switch | Drive from Hercules' CPU-busy time, or fit real hour meters. Pure output, easy. |
| **Emergency Pull switch (EPO)** | Emergency power off | Decorative, or genuinely cut power to the panel. **Do not wire it to anything that can corrupt the Pi's filesystem.** |

### 20.5 What you cannot drive — be honest about it in your documentation

| Not drivable | Why |
| --- | --- |
| DISPLAY ASSEMBLER OUT positions 3–8 (C, MB2/MB3/N2/N3, B, Z, D registers, MCKA) | 3145 microarchitecture. No Hercules counterpart exists. |
| A-REGISTER DISPLAY positions 2–8 (TI/TA/TT/TE, S/P/T/L, System Register, channel words) | Same. |
| **System Check indicators** and **Console File indicators** | Real 3145 hardware fault detection and the console diskette file. Hercules has no failing hardware to report. |
| CPU Status indicators such as **CLOCK STOP**, **LOG PRES** | Microarchitectural / RAS state. |

**Recommended treatment:** drive the architected lamps for real; put the service-use roller
positions on a slow, plausible pseudo-random "activity" pattern derived from real instruction
throughput so the panel *looks* alive; and **say plainly in your README which is which.** Anyone
who knows these machines will ask, and an honest answer is far better received than a vague one.

### 20.6 Is there a better choice than the /145?

**No — and the reason is stronger than "best documented".** See the per-model survey in §20.8:
the /145 is the **only** System/370 whose lamp banks display architected data. Every other
lamp-panel /370 sends registers, PSW and storage somewhere else — the printer-keyboard on the
/135 and /155, a CRT on the /165. Choosing any of them would mean building a large lamp array
that structurally *cannot* show the data Hercules provides.

An earlier draft suggested the /115, /125 or /138 as higher-ratio alternatives. **That advice was
wrong and is withdrawn:** the /115 and /125 use a Display Operating Console, not lamps.

### 20.7 Where the operator-visible data goes, by model

This is the single most useful table in this document for the build decision.

| Model | Panel type | Where registers / PSW / storage are displayed | Verdict |
| --- | --- | --- | --- |
| **/115, /125** | **Display Operating Console** (CRT) | Screen | ❌ Not a lamp panel |
| **/135** | Lamp panel | **Printer-keyboard** — "Press ALTER/DISPLAY at console-printer keyboard… Type 2-character mnemonic" | ⚠️ Lamps are status only |
| **/145** | **Lamp panel** | **The panel's own A-Register lamp bank** — position 1 = "Storage or External Register" per STORAGE SELECT; and "when the CPU is in a soft-stopped state (MANUAL indicator on), the indicators display the next instruction address" | ✅ **The target** |
| **/155** | Lamp panel | **Printer-keyboard** — the manual states flatly: *"Display operations are performed through the PR-KB."* | ⚠️ Lamps are status only |
| **/158** | **Display console** | Screen frames, light pen. *"The Model 158 display console does not have LOAD UNIT dials or a LOAD key."* | ❌ Not a lamp panel |
| **/165** | Lamp panel **+ CRT** | **CRT** — "Set CRT MODE SELECT to CE and MANUAL ENTRY SELECT to MCAR… See eight bytes of storage displayed at MCDR on the CRT" | ⚠️ Big lamp array, but data goes to the tube |
| **/168** | Lamp panel **+ CRT** | **CRT** — "Set CRT MODE SELECT to CE… Set MANUAL ENTRY SELECT to MCAR… The contents of the addressed general register are displayed on the CRT in the right half of the MCDR" | ⚠️ Largest lamp array of the line, but the architected data goes to the tube — same limitation as the /165, at roughly twice the build cost |
| **3033 / 303X** | **3036 display console** | Screen, via service processor | ❌ See [§17](#17-the-ibm-3033--303x-console-lights-switches-buttons) |

### 20.8 Per-model survey: which /370s actually have a lamp panel?

**Source:** [SR20-4460-0, *System/370 Operator's Reference Guide*, July 1974](https://www.bitsavers.org/pdf/ibm/370/SR20-4460-0_System_370_Operators_Reference_Guide_Jul74.pdf),
section 3, which gives per-model power-on, IPL and alter/display procedures for the /115, /125,
/135, /145, /155, /158, /165 and /168. This scan has a text layer and was transcribed directly.
The per-model procedures are the giveaway: a machine whose IPL procedure says *"dial the address
into LOAD UNIT switches"* has a lamp panel; one that says *"select 4 under O-OPERATOR FUNCTIONS…
with the light pen"* does not.

Evidence quoted from that guide:

- **/145** — "Select IPL input device address on rotary switches"; store/display through the
  panel's own switches and lamp banks, with the PR-KB offered as the *easier* alternative
  ("Use the alter/display function of the PR-KB… whenever possible").
- **/135** — "Press LAMP TEST to check lamps"; "Select IPL input device address on rotary switches
  C through E (LOAD UNIT ADDRESS)"; "Press LOAD". But display is via the console-printer keyboard.
- **/155** — "Dial the address of the IPL device into LOAD UNIT switches FGH. Press the LOAD key.
  The LOAD indicator turns on." Display: **"Display operations are performed through the PR-KB."**
- **/165** — "Set LOAD UNIT switches to residence volume address. Hold SYSTEM CLEAR; press LOAD.
  Manual light goes off, LOAD light comes on"; RATE switch with INSN STEP. Register display via
  the CRT at MCAR/MCDR.
- **/158** — "Insert the IMPL diskette in the console file"; "The system is IMPLed in **display
  mode**"; "Exit from the configuration frame by selecting MANUAL with the **light pen**";
  display via "'3 ALTER/DISPLAY' under FRAME CONTROL". And elsewhere in the guide:
  **"The Model 158 display console does not have LOAD UNIT dials or a LOAD key."**
- **/168** — **has a real control panel:** "Set LOAD UNIT switches to SYSRES volume address";
  "Press ENABLE SYSTEM CLEAR and LOAD simultaneously… Manual light goes off, LOAD light comes on";
  "Press STOP. Manual light comes on"; "Set STORAGE SELECT to GEN PUR". **But** register display
  goes to the CRT: "Set CRT MODE SELECT to CE… MANUAL ENTRY SELECT to MCAR… displayed on the CRT
  in the right half of the MCDR. Use 00 to 0F for 16 general registers."
  ⚠️ **Do not be misled** by the guide's separate "Model 168 Display Console Display Areas" section
  — that documents the **OS/VS2 operator message console** (source: GC38-0260 *OS/VS2 Display
  Consoles*), which is the operating system's 3277-class message screen, **not** the CPU control
  panel. The two are different devices, and conflating them is easy.
- **/115, /125** — the guide has a "Display Operating Console – Model 115 and Model 125" section.

**Conclusion: the /145 is not a compromise pick. It is the only System/370 that can do what this
project needs.**

### 20.9 Sources for this section

| Reference | Content |
| --- | --- |
| [GA24-3554-0 — 370/145 Operating Procedures (Sep 1970)](https://www.bitsavers.org/pdf/ibm/370/model145/GA24-3554-0_370_Model_145_Operating_Procedures_Sep70.pdf) | **The source of every quotation above.** Text-searchable. Chapter "Console Indicators, Switches, and Keys" pp. 8–23 contains: System Check Indicators (8), CPU Status Indicators (9), Console File Indicators (10), **System Indicators (11)**, **Display Assembler Out Roller Switch (12)**, **A-Register Display Roller Switch (13)**, Toggle Switches (14), **Address Compare Switch (15)**, Storage Select Switch (16), **Rate Switch (17)**, Check Control Switch (18), Diagnostic/Console File Control Switch (19), **Rotary Switches A through H (20)**, Use Meters (21), Keys (22). Later chapters cover IMPL (38), **IPL (39)**, Instruction Step (39), Set IC (39), Clear Storage (40), Data Compare Trap (40), **Manual Store/Display Operations (41)**. |
| [SR20-4460-0 — System/370 Operator's Reference Guide (Jul 1974)](https://www.bitsavers.org/pdf/ibm/370/SR20-4460-0_System_370_Operators_Reference_Guide_Jul74.pdf) | Cross-model confirmation that these controls are common to the /370 line, not /145 quirks. Also text-searchable. |
| [GA22-7000-0 — System/370 Principles of Operation, "Operator Facilities"](https://www.bitsavers.org/pdf/ibm/370/princOps/GA22-7000-0_370_Principles_Of_Operation_Jun70.pdf) | The *architected* definition of these facilities — which is precisely why Hercules can supply them. |
| [Hercules command reference (V3.12 PDF)](https://hercdoc.glanzmann.org/V312/HerculesUserReference.pdf) | The other half of every mapping in §20.4: `ipl`, `iplc`, `sysreset`, `sysclear`, `restart`, `start`, `stop`, `store`, `psw`, `gpr`, `fpr`, `cr`, `ar`, `pr`, plus storage display/alter and breakpoints. |
| [Hercules configuration reference](https://hercules-390.github.io/html/hercconf.html) | Set `CPUMODEL 0145` so the machine also *reports* itself as a /145 — see [§1](#1-design-decision-which-370-panel-to-replicate). |
| [Ken Shirriff — iconic consoles](http://www.righto.com/2019/04/iconic-consoles-of-ibm-system360.html) | Confirms the general rule that roller count scales with model size (Model 30 = 0, 40 = 2, 50 = 4, 65 = 6) — the reason a smaller machine means a higher drivable-lamp ratio. |
