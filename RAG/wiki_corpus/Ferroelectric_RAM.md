# Ferroelectric RAM

> **Query Topic**: main advantage of ferroelectric memristors (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 362, Frequency: 17)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Ferroelectric_RAM

---

Ferroelectric RAM ( FeRAM , F-RAM or FRAM ) is a random-access memory similar in construction to DRAM but using a ferroelectric layer instead of a dielectric layer to achieve non-volatility. FeRAM is an alternative non-volatile random-access memory technology that offers the same functionality as flash memory . An FeRAM chip contains a thin film of ferroelectric material , often lead zirconate titanate , commonly referred to as PZT. The atoms in the PZT layer change polarity in an electric field, thereby producing a power-efficient binary switch. However, the most important aspect of the PZT is that it is not affected by power disruption or magnetic interference, making FeRAM a reliable nonvolatile memory .

FeRAM's advantages over Flash include: lower power usage, faster write speeds and a much greater maximum read/write endurance (about 10 10 to 10 15 cycles). FeRAMs have data retention times of more than 10 years at +85 °C (and decades at lower temperatures). The primary disadvantages of FeRAM are much lower storage densities than flash devices, storage capacity limitations and higher cost. Like DRAM, FeRAM's read process is destructive, necessitating a write-after-read architecture.

## History

Ferroelectric RAM was proposed by MIT graduate student Dudley Allen Buck in his master's thesis, Ferroelectrics for Digital Information Storage and Switching, published in 1952.

In 1955, Bell Telephone Laboratories was experimenting with ferroelectric-crystal memories. Following the introduction of metal–oxide–semiconductor (MOS) dynamic random-access memory ( DRAM ) chips in the early 1970s, development of FeRAM began in the late 1980s. Work was done in 1991 at NASA 's Jet Propulsion Laboratory (JPL) on improving methods of read out, including a novel method of non-destructive readout using pulses of UV radiation.

FeRAM was commercialized in the mid-1990s. In 1994, video game company Sega used FeRAM chips to store saved games in Sonic the Hedgehog 3 , which shipped several million game cartridges that year. In 1996, Samsung Electronics introduced a 4 Mb FeRAM chip fabricated using NMOS logic . In 1998, Hyundai Electronics (now SK Hynix ) also commercialized FeRAM technology. The earliest known commercial product to use FeRAM is Sony 's PlayStation 2 Memory Card (8 MB) , released in 2000. The Memory Card's microcontroller (MCU) manufactured by Toshiba contained 32 kb (4 kB ) embedded FeRAM fabricated using a 500 nm complementary MOS (CMOS) process.

In 1999 Fujitsu began producing standalone FeRAMs, as well as specialized chips (e.g. chips for smart cards ) with embedded FeRAMs for Ramtron. In 2010 Ramtron switched to Texas Instruments and IBM.

In 2024–2025 ferroelectric RAM research was driven by HfO₂-based materials for CMOS compatibility, scalability to <10 nm, and integration into advanced nodes (22–28 nm). Cycle counts exceeded 10¹², with reduced power requirements.

Prototypes offered 9–16 Mb arrays with 10¹² endurance and 5–7 ns read/write.

## Vendors

Ramtron is a fabless semiconductor company . One major licensee is Fujitsu , which operates one of the largest semiconductor foundry production lines with FeRAM capability. In 2012 Ramtron was acquired by Cypress Semiconductor .

FeRAM research projects were reported at Samsung , Matsushita , Oki , Toshiba , Infineon , Hynix , Symetrix, Cambridge University , University of Toronto , and the Interuniversity Microelectronics Centre (IMEC, Belgium ).

## Description

Conventional DRAM consists of a grid of small capacitors and their associated wiring and signaling transistors . Each storage element, a cell , consists of one capacitor and one transistor, a so-called "1T-1C" device.

The 1T-1C storage cell design in a FeRAM is similar in construction to the storage cell in DRAM, in that both cell types include one capacitor and one access transistor. In a DRAM cell capacitor, a linear dielectric is used, whereas in a FeRAM cell capacitor the dielectric structure includes ferroelectric material , typically lead zirconate titanate (PZT).

A ferroelectric material has a nonlinear relationship between the applied electric field and the apparently stored charge. Specifically, the ferroelectric characteristic has the form of a hysteresis loop, which is very similar in shape to the hysteresis loop of ferromagnetic materials. The dielectric constant of a ferroelectric is typically much higher than that of a linear dielectric because of the effects of semi-permanent electric dipoles formed in the crystal structure of the ferroelectric material. When an external electric field is applied across a dielectric, the dipoles tend to align themselves with the field direction, produced by small shifts in the positions of atoms and shifts in the distributions of electronic charge in the crystal structure. After the charge is removed, the dipoles retain their polarization state. Binary "0"s and "1"s are stored as one of two possible electric polarizations in each data storage cell 2021 2027 Global And Regional Ferroelectric Ram Industry Status And Prospects Professional Market – Market Reports World .

In terms of operation, FeRAM is similar to DRAM. Writing is accomplished by applying a field across the ferroelectric layer by charging the plates on either side of it, forcing the atoms inside into the "up" or "down" orientation (depending on the polarity of the charge), thereby storing a "1" or "0" Introduction to DRAM (Dynamic Random-Access Memory) - Technical Articles . Reading operation is also similar to DRAM Ferroelectric RAM: FRAM Technology Operation » Electronics Notes . The transistor forces the cell into a particular state, say "0". If the cell already held a "0", nothing will happen in the output lines. If the cell held a "1", the re-orientation of the atoms in the film will cause a brief pulse of current in the output as they push electrons out of the metal on the "down" side Ferroelectric RAM: FRAM Technology Operation » Electronics Notes . The presence of this pulse means the cell held a "1". Since this process overwrites the cell, reading FeRAM is a destructive process, and requires the cell to be re-written.

In general, the operation of FeRAM is similar to ferrite core memory , one of the primary forms of computer memory in the 1960s Computer Memory Technology: From Ferrite Rings to FRAM . However, compared to core memory, FeRAM requires far less power to flip the state of the polarity and does so much faster.

## Features and properties

### Density

The main determinant of a memory system's cost is the density of the components used to make it up. Smaller components, and fewer of them, means that more cells can be packed onto a single chip, which in turn means more can be produced at once from a single silicon wafer. This improves yield, which is directly related to cost.

The lower limit to this scaling process is an important point of comparison. In general, the technology that scales to the smallest cell size will end up being the least expensive per bit . In terms of construction, FeRAM and DRAM are similar, and can in general be built on similar lines at similar sizes. In both cases, the lower limit seems to be defined by the amount of charge needed to trigger the sense amplifiers. For DRAM, this appears to be a problem at around 55 nm, at which point the charge stored in the capacitor is too small to be detected.

An additional limitation on size is that materials tend to stop being ferroelectric when they are too small. (This effect is related to the ferroelectric's "depolarization field".) There is ongoing research on addressing the problem of stabilizing ferroelectric materials; one approach, for example, uses molecular adsorbates.

### Power consumption

The key advantage to FeRAM over DRAM is what happens between the read and write cycles. In DRAM, the charge deposited on the metal plates leaks across the insulating layer and the control transistor, and disappears. In order for a DRAM to store data for anything other than a very short time, every cell must be periodically read and then re-written, a process known as refresh . Each cell must be refreshed many times every second (typically 16 times per second ) and this requires a continuous supply of power. In contrast, FeRAM only requires power when actually reading or writing a cell FRAM Can Lower Power and Increase Performance in MCU-Based Systems .

Another non-volatile memory type is flash , and like FeRAM it does not require a refresh process. Flash works by pushing electrons across a high-quality insulating barrier where they get "stuck" on one terminal of a transistor . This process requires high voltages, which are built up in a charge pump over time. This means that FeRAM could be expected to be lower power than flash, at least for writing, as the write power in FeRAM is only marginally higher than reading FRAM - Smart IC Memory from Texas Instruments . For a "mostly-read" device the difference might be slight, but for devices with more balanced read and write the difference could be expected to be much higher.

### Reliability

Data reliability is guaranteed in F-RAM even in a high magnetic field environment compared to MRAM . Cypress Semiconductor's F-RAM devices are immune to the strong magnetic fields and do not show any failures under the maximum available magnetic field strengths (3,700 gauss for horizontal insertion and 2,000 gauss for vertical insertion) FRAM - Smart IC Memory from Texas Instruments . [ dubious – discuss ] In addition, the F-RAM devices allow rewriting with a different data pattern after exposure to the magnetic fields.

### Speed

DRAM speed is limited by the rate at which the charge stored in the cells can be drained (for reading) or stored (for writing). In general, this ends up being defined by the capability of the control transistors, the capacitance of the lines carrying power to the cells, and the heat that power generates.

FeRAM is based on the physical movement of atoms in response to an external field, which is extremely fast, averaging about 1 ns. In theory, this means that FeRAM could be much faster than DRAM. However, since power has to flow into the cell for reading and writing, the electrical and switching delays would likely be similar to DRAM overall. It does seem reasonable to suggest that FeRAM would require less charge than DRAM, because DRAMs need to hold the charge, whereas FeRAM would have been written to before the charge would have drained. However, there is a delay in writing because the charge has to flow through the control transistor, which limits current somewhat Ferroelectric Memories: The Middle Ground .

In comparison to flash, the advantages are much more obvious. Whereas the read operation is likely to be similar in speed, the charge pump used for writing requires a considerable time to "build up" current, a process that FeRAM does not need. Flash memories commonly need a millisecond or more to complete a write, whereas current FeRAMs may complete a write in less than 150 ns.

On the other hand, FeRAM has its own reliability issues, including imprint and fatigue. Imprint is the preferential polarization state from previous writes to that state, and fatigue is the increase of minimum writing voltage due to loss of polarization after extensive cycling.

The theoretical speed of FeRAM is not entirely clear. Existing 350 nm devices have read times on the order of 50–60 ns. Although slow compared to modern DRAMs, which can be found with times on the order of 20 ns, common 350 nm DRAMs operated with a read time of about 35 ns, so FeRAM speed appears to be comparable given the same fabrication technology.

### Additional metrics

## Applications

- Datalogger in portable/implantable medical devices, as FeRAM consumes less energy compared to other non-volatile memories such as EEPROM

- Feram's energy-efficient and reliable data retention, makes them an ideal choice for IoT devices such as wearable electronics, sensors, and actuators .

- FeRAM is used in wearables, smart meters, and medical monitors .

- FRAM holds significant promise in the automotive industry, with one of its main benefits being its rapid write capability Infineon Welcomes New Devices to Fleet of Automotive Ferroelectric RAM - News .

- They are often integrated into RFID tags to provide fast writes, low power consumption, and high endurance, enabling secure and frequent data updates for applications such as supply chain tracking, access control, and smart cards Reasons to Choose FeRAM-embedded RFIDs｜RAMXEED .

## Market

FeRAM remains a relatively small part of the overall semiconductor market Ramtron . In 2005, worldwide semiconductor sales were US$235 billion (according to the Gartner Group ), with the flash memory market accounting for US$18.6 billion (according to IC Insights). The 2005 annual sales of Ramtron, perhaps the largest FeRAM vendor, were reported to be US$32.7 million. The much larger sales of flash memory compared to the alternative NVRAMs support a much larger research and development effort. Flash memory is produced using semiconductor linewidths of 30 nm at Samsung (2007) while FeRAMs are produced in linewidths of 350 nm at Fujitsu and 130 nm at Texas Instruments (2007) Introduction to FRAM (Ferroelectric RAM) including Its History . Flash memory cells can store multiple bits per cell (currently 4 in the highest density NAND flash devices), and the number of bits per flash cell is projected to increase to 8 as a result of innovations in flash cell design A Guide to NAND Flash Memory: Comparing SLC, MLC, TLC, and QLC . As a consequence, the areal bit densities of flash memory are much higher than those of FeRAM, and thus the cost per bit of flash memory is orders of magnitude lower than that of FeRAM.

The density of FeRAM arrays might be increased by improvements in FeRAM foundry process technology and cell structures, such as the development of vertical capacitor structures (in the same way as DRAM) to reduce the area of the cell footprint. However, reducing the cell size may cause the data signal to become too weak to be detectable. In 2005, Ramtron reported significant sales of its FeRAM products in a variety of sectors including (but not limited to) electricity meters , automotive (e.g. black boxes , smart air bags ), business machines (e.g. printers, RAID disk controllers), instrumentation, medical equipment, industrial microcontrollers, and radio frequency identification tags. The other emerging NVRAMs, such as MRAM, may seek to enter similar niche markets in competition with FeRAM.

Texas Instruments proved it to be possible to embed FeRAM cells using two additional masking steps during conventional CMOS semiconductor manufacture. Flash typically requires nine masks. This makes possible for example, the integration of FeRAM onto microcontrollers, where a simplified process would reduce costs. However, the materials used to make FeRAMs are not commonly used in CMOS integrated circuit manufacturing. Both the PZT ferroelectric layer and the noble metals used for electrodes raise CMOS process compatibility and contamination issues. Texas Instruments has incorporated an amount of FRAM memory into its MSP430 microcontrollers in its new FRAM series.

### Capacity timeline

As of 2021 different vendors were selling chips with no more than 16Mb of memory in storage size (density).
