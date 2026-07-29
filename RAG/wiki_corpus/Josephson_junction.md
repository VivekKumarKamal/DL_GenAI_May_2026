# Josephson junction

> **Query Topic**: Josephson effect (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 310, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Josephson_junction

---

A Josephson junction is a nonlinear, dissipationless circuit element that uses the Josephson effect in superconductors to form a nonlinear inductor . It consists of a weak barrier (such as an insulator) separating two superconductors. Pairs of electrons tunnel through the barrier, producing an effective inductance that is dependent on the phase difference between the superconductors.

The Josephson junction is used as a circuit element in superconducting loops. In a circuit, the Josephson inductance and the junction capacitance can be used to form a nonlinear oscillator, similar to a LC circuit , with a current-dependent inductance. Circuits with Josephson junctions are used to make superconducting magnetometers known as SQUIDs , in classical logic gates for ultrafast computing, and in circuit quantum electrodynamics to create superconducting qubits .

## History

In 1962, British physicist Brian Josephson predicted the Josephson effect : that pairs of superconducting electrons known as Cooper pairs could tunnel through the gap between two superconducting layers, if they were weakly separated. In 1963, Phillip Anderson and John Rowell at Bell Labs constructed the first Josephson junction, using tin-oxide-lead junctions, to verify this effect. A thin film of tin was oxidized to form the barrier, and then a thin-film cross strip of lead formed the counter electrode.

In the 1960s, James Zimmerman , Arnold Silver , and colleagues working at a Ford lab on magnetic resonance realized that Josephson junction nonlinearity, combined with the flux quantization in superconducting loops, could be used to measure small changes in magnetic flux, and create a magnetometer with high levels of magnetic field sensitivity precision. They created the first such device using films of tin separated by plastic, with two Josephson junctions separated by a macroscopic gap. This was the first SQUID magnetometer.

In 1966, at IBM , Juri Matisoo demonstrated sub-nanosecond switching in a Josephson junction. This and subsequent results indicated that Josephson Junctions could be faster than any available transistor at the time. This began a superconducting supercomputer project at IBM, known as the Josephson signal processor, with intentions to use (Pb-In-Au)-oxide-(Pb-Bi) Josephson junctions as a basis for logic circuits to enable ultrafast computing. This project lasted from 1967 to September 1983. The initial attempt was shut down due to insufficient speed advantage compared to rapidly developing silicon technology, but some Japanese companies remained interested, since JJ-based technology avoided the problem of large semiconductor mainframes and power dissipation.

In 1980, Tony Leggett proposed using the phase of a Josephson junction as a macroscopic quantum coordinate. In 1987, John Clarke , Michel H. Devoret , and John M. Martinis used a Josephson junction-based circuit to demonstrating that a macroscopic system could have quantum mechanical properties (specifically, tunnelling and energy quantization ). They won the 2025 Nobel Prize in physics for their work.

In 1999, Yasunobu Nakamura and colleagues used Josephson junctions connected in a superconducting loop to show coherent quantum oscillations in a Josephson circuit, making this the first superconducting qubit . Superconducting qubits require the nonlinearity provided by Josephson junctions, since it allows the first two energy levels of the circuit to be addressed independently of all the others. All major superconducting qubit architectures use Josephson junctions.

## Theory

### Josephson equations

The Josephson effect arises when two superconductors are weakly coupled through a thin insulating barrier. Without any voltage applied, the two superconducting electrodes' electrical charge carriers, which are Cooper pairs , will cross the barrier as a supercurrent , ${\textstyle I_{J}}$ . This supercurrent is given by:

$I_{J}=I_{0}\sin(\varphi )$

Where ${\textstyle I_{0}}$ is the critical current and $\varphi$ is the phase difference between the two superconductor's wavefunctions. Because Cooper pairs tunnel phase-coherently, the supercurrent depends only on the phase difference. This is the first Josephson equation, known as the current-phase relation.

When a voltage is applied, the phase difference evolves in time. This is described by the second Josephson equation, the voltage-phase relation :

${\frac {d\varphi (t)}{dt}}={\frac {2e}{\hbar }}V={\frac {2\pi }{\Phi _{0}}}V$

The two Josephson equations can be used to derive the effective inductance.

$V(t)={\frac {\hbar }{2e}}{\frac {d\delta }{dt}}={\frac {\hbar }{2e}}\left({\frac {dI}{d\delta }}\right)^{-1}{\frac {dI}{dt}}$

By analogy with an inductor, ${\textstyle V(t)=L_{J}{\frac {dI}{dt}}}$ , so the effective inductance is:

$L_{J}={\frac {\hbar }{2e}}\left({\frac {dI}{d\delta }}\right)^{-1}={\frac {\Phi _{0}}{2\pi }}\left({\frac {dI}{d\delta }}\right)^{-1}$

Then, using the first Josephson equation:

${\frac {dI}{d\delta }}=I_{0}\cos(\delta )$

So the Josephson inductance is

$L_{J}={\frac {\Phi _{0}}{2\pi I_{0}\cos(\delta )}}$

The Josephson junction is both non-linear and non-dissipative. It is non-linear because its effective inductance depends on the superconducting phase difference $\delta$ , and it is (ideally) non-dissipative because it operates without resistance as long as the current remains below the critical value $I_{0}$ . However, at non-zero voltage, there is dissipation introduced by additional channels of loss. This is modeled as a shunt resistor in the RCSJ model.

### Energy stored in the junction

The potential energy of the junction is:

$U(\varphi )=-E_{J}\cos \varphi$

The Hamiltonian for this system is:

$H={\frac {Q^{2}}{2C}}-E_{J}\cos \phi$

Or equivalently:

$H=4E_{C}n^{2}-E_{J}\cos \phi$

where ${\textstyle E_{C}={\frac {e^{2}}{2C}}}$ is the charging energy and ${\textstyle n={\frac {Q}{2e}}}$ is the number of Cooper pairs.

### RCSJ equivalent circuit model

To study the dynamics of a Josephson junction, the model can be simplified by assuming that the normal conductance is constant. In this model, the Josephson junction is characterized by the Josephson inductance and the normal resistance R of the junction.

Similarly to a parallel plate capacitor , the Josephson junction design must have some capacitance because it consists of two electrodes separated by an insulator or weak link. It also may have some resistance , due to the dissipative current at finite voltage. Thus, the Josephson junction can be modeled as an ideal non-linear Josephson element in parallel with a normal resistor and capacitor. This is known as the resistively and capacitively-shunted junction (RCSJ) model. Alternatively, in the limit where capacitance is small, the resistively-shunted junction (RSJ) model is used.

In both models, the normal resistance will depend on bias voltage and temperature, $R_{N}=R(V,T)$ . It is thought that lower temperatures will make the resistance go to zero, because there will be fewer quasiparticles in the circuit. However, this in practice difficult, as there exist a non-negligible population of non-equilibrium quasiparticles, due to cosmic rays or other phenomena, that are not accounted for by temperature alone.

The main equation of the RCSJ model is:

${\frac {\hbar C}{2e}}\,{\frac {\partial ^{2}\varphi }{\partial t^{2}}}\;+\;{\frac {\hbar }{2eR}}\,{\frac {\partial \varphi }{\partial t}}\;+\;I_{c0}\sin(\varphi )\;=\;I$

This differential equation describes the dynamics of the Josephson junction when a bias current $I$ is applied.

### Tilted washboard potential

Rewriting the RCSJ model equation in dimensionless coordinates gives:

${\frac {\partial ^{2}\varphi }{\partial \tau ^{2}}}+{\frac {1}{Q}}\,{\frac {\partial \varphi }{\partial \tau }}+\sin(\varphi )={\frac {I}{I_{c0}}}\,.$

Where the dimensionless time variable $\tau =\omega _{p}t$ , with

$\omega _{p}={\sqrt {\frac {2eI_{0}}{\hbar C}}}\,.$

This is known as the Josephson plasma frequency of the junction. It represents the frequency of the Josephson junction oscillations in the untilted washboard potential.

When a current is applied to a Josephson junction, the RCSJ model can be used to describe its behavior. A current-biased Josephson junction exhibits an effective tilted washboard of potential energy. Although the bare Josephson junction resembles periodic wells with no tilt, the effective potential energy takes on an extra term in a current-biased circuit:

$U(\varphi )=-E_{J}\cos \varphi -{\frac {\hbar }{2e}}I\varphi$

where $I$ is the bias current.

This is of the form of a general tilted washboard potential, given by:

$U(x)=-Ax-B\cos(x)$

Their graphs are tilted cosine functions, with the degree of tilt given by the constant A. The Josephson junction acts like a damped nonlinear oscillator.

### Circuit quantization

In circuit quantization, flux and charge are treated as generalized coordinates. The quantization step promotes $\phi$ (dimensionless phase) and $n$ (Cooper pair number) to operators satisfying the commutation relations. This gives the quantum Hamiltonian for the Josephson junction, used in circuit quantum electrodynamics :

${\hat {H}}=4E_{C}{\hat {n}}^{2}-E_{J}\cos {\hat {\phi }}$

This forms the basic nonlinear element used in circuit quantum electrodynamics and in superconducting qubits .

## Types of Josephson junctions

### Superconductor-Insulator-Superconductor (SIS)

The superconductor-insulator-superconductor (SIS) tunnel junction, also called a superconducting tunnel junction , has two superconducting electrodes (S) separated by a thin insulating barrier (I). If the barrier is made of an insulating oxide, for example, aluminum oxide (Al 2 O 3 ), it would be about 1 nanometer thick; a thicker oxide barrier would block quantum tunneling. If a barrier is made of other, less perfect insulators, for example, from amorphous silicon, it may be several nanometers thick. SIS structures are widely used as Josephson junctions, but sometimes, when a supercurrent (zero-voltage current) isn't required, they are used for their nonlinear current-voltage characteristics. They are used in SQUIDs , Josephson voltage standards (in both cases, the application is of an analog type), and in superconducting digital circuits, for example in A/D and D/A converters, or in superconducting processors (in those cases, an application is digital, tunnel junctions assisting in creating logical 1 and 0 states), as well as in Quantum Computing , where they help form superconducting qubits .

In the vast majority of applications, the two electrodes (designated as "S" in the SIS abbreviation) are made of niobium (Nb), which has the highest superconducting transition temperature among elements in the Periodic Table. Clean Niobium superconducts below 9.2 K, which allows operation of a superconducting circuit containing SIS Nb-based junctions in liquid Helium, which has a boiling temperature of 4.2 K at normal pressure. Occasionally, when operational temperature must be much lower, as is the case in Quantum Computing (qubits), "S" layers can be made of aluminum (Al), which has a transition temperature into the superconducting state of 1.2 K. Aluminum is also used as a thin layer deposited over a niobium base electrode in order to create high-quality refractory (Nb-based) tunnel junctions (see below in the section "Fabrication"). The reason for using Al is that it forms a remarkably stable, uniform, pinhole-free oxide layer, which is ideal for creating a reliable tunnel barrier. It is not an accident that the first tunnel junctions created by Ivar Giaever were made of aluminum. Control of Al oxide thickness can be easily achieved by timing its oxidation in air or at a partial pressure of oxygen within a deposition system (see below in the "Fabrication" section).

### Superconductor-Normal-Superconductor (SNS)

The barrier is a thin normal metal, rather than an insulator. The normal metal may not be superconducting, or it may be a superconductor with a smaller critical temperature. Although for a SIS Josephson junction, the current-phase relationship is often close to being perfectly sinusoidal, the SNS junction current-phase relation has a ramp-like dependence.

SNS designs have higher critical currents and lower impedance than traditional SIS designs. Implementations of SNS junctions include SNS sandwiches, variable-thickness bridges, and ramp junctions. They are used in rapid single flux quantum logic circuits which encode digital information based on magnetic flux quanta since they have a non-hysteretic current–voltage dependence.

### Superconductor-constriction-Superconductor (ScS)

The barrier is a constriction or weak link, such as a microbridge of superconducting material. These junctions can carry larger critical currents than SIS junctions. ScS junctions may be used in cases where an all-superconducting junction would be preferable to introducing an insulator or non-superconducting metal to the device. ScS junctions have a sub-millimeter frequency range of around 500–1000 GHz.

Because of the non-negligible presence of non-equilibrium electrons (often called quasiparticles in this context), the dynamic behavior of ScS junctions is much more complicated than traditional resistive models.

### Phi Josephson junction

In traditional Josephson junctions, the ground state phase is zero. However, phi Josephson junctions instead have a non-zero Josephson phase in the ground state. In this case, the first Josephson equation (the current-phase relation) is modified, from ${\textstyle I=I_{0}\cos(\delta )}$ to:

$I=I_{0}\cos(\delta +\phi )$

Phi-junctions can be physically realized by breaking symmetries, such as by using an altermagnet .

#### Pi Josephson junction

Pi Josephson junctions are a kind of Phi Josephson junction with a 180 degree phase difference between them. The first Josephson equation (the current-phase relation) is modified in this case, from ${\textstyle I=I_{0}\cos(\delta )}$ to:

$I=I_{0}\cos(\delta +\pi )=-I_{0}\sin(\delta )$

Pi-junctions can be physically realized using a ferromagnetic barrier, which is usually magnetic but may be insulated. This architecture is often called a superconductor-ferromagnetic-superconductor (SFS) junction. In an SFS junction, the ground state energy oscillates between 0 and π as a function of the ferromagnet's thickness. Applications of the SFS Pi-junction include digital superconducting logic and memory.

### Long Josephson junction

Long Josephson junctions are Josephson junctions where at least one parameter exceeds the Josephson penetration depth $\lambda _{J}$ . The Josephson penetration depth describes how far an external magnetic field penetrates into a Josephson junction, and is given by:

$\lambda _{J}={\sqrt {\frac {\Phi _{0}}{2\pi \mu _{0}j_{c}\left(L+2\lambda _{L}\right)}}}$

where L is the length of the junction. In Josephson junctions with dimensions that exceed the penetration depth, the superconducting phase varies spatially, described by the sine-Gordon equation. These long Josephson junctions can support propagating flux quanta known as fluxons . They may be used as a Josephson transmission line or as a flux flow oscillator.

## Fabrication

### JJ fabrication in the 1960s - early 1980s: Shadow evaporation and the combination of photolithography and various layer depositions

When the field was young, starting in the early 1960s and all throughout the 1970s, single, large-area (on the order of mm 2 ) Josephson junctions were fabricated by evaporating superconducting electrodes (usually thin films of lead and lead alloys) through a set of changeable mechanical masks. This technique is called shadow evaporation , and it is currently of mostly historical interest. The tunnel barrier was formed by oxidizing the base electrode in air.

Later, fabrication of smaller junctions (typically tens of square microns in area) was performed by evaporating superconducting electrodes and interconnects through a series of photolithographic masks. Although these methods, borrowed from silicon technology, could produce fairly complex Josephson devices and circuits, the use of organic photoresist limited the materials used and the processing that could be performed. At the peak of its use, in the late 1970s and early 1980s, photolithography combined with various layer depositions produced Josephson junction circuits for the exploratory Josephson Signal Processor (JSP) at IBM, which were of considerable sophistication. In the IBM process in the early 1980s—which was the state-of-the-art at the time—the base electrode was made of niobium, and this niobium layer was oxidized to form an Nb oxide tunnel barrier in specialized RF oxidation chambers (simple air oxidation did not work for niobium). Then, with additional lithography performed on the base electrode, a lead-alloy counterelectrode and superconducting interconnects were deposited by vacuum evaporation. The results were far from being satisfactory: the quality of junction characteristics was relatively poor, and niobium oxide had a high dielectric constant, which was undesirable in digital applications. In addition, the chips thus produced suffered from unacceptable failure rates during thermal cycling.

### Whole-wafer process

In a method developed at Sperry Research by H. Kroger and colleagues in 1981, deposition of superconducting sandwich structure (future Josephson junctions) and patterning (creation of a desired superconducting circuit) were cleanly separated. This separation provided innumerable advantages, which will be described below. First, the entire substrate (usually a silicon wafer) is coated with a continuous tunneling structure: a trilayer consisting of a thin tunnel barrier sandwiched between two superconducting electrodes. This is typically done in a vacuum chamber, in situ, which allows good control and near-absolute cleanliness. Then the patterning of this sandwich structure is performed outside the deposition chamber, where the full arsenal of patterning techniques can be used, from state-of-the-art photolithography to various reactive ion etching and ion milling techniques, and, when necessary, additional layer depositions. All these techniques were initially developed as part of the toolbox of mighty silicon technology. Thus, the use of the whole-wafer process first proposed by Harry Kroger and his co-workers brought superconducting device fabrication into the realm of modern integrated circuit technology.

However, the junction structure used by Kroger and co-workers had serious shortcomings that, in essence, eliminated the advantages offered by the whole-wafer process. The tunnel barrier was formed from amorphous silicon, a-Si. The resulting Nb-(a-Si)-Nb junctions were hard to fabricate because of the difficulty of creating a suitable tunnel barrier from capricious a-Si. In addition, there was a detrimental interaction between the a-Si barrier layer and the top niobium electrode. As a result, the quality of the resulting Josephson junction current-voltage characteristic was poor.

However, a solution to these remaining problems was soon found. Shortly after Kroger at. al. publications, the whole-wafer processing method was significantly modified at AT&T Bell Labs by Gurvitch and co-workers, who combined the whole-wafer idea with the almost simultaneous important discovery made at Bell Labs—namely, the discovery of the benefits brought about by thin aluminum overlayers on the base (lower) niobium electrode.

Early in 1981, J. M. Rowell, M. Gurvitch, and J. Geerk (the latter visiting Bell Labs on a sabbatical from the National Laboratory in Karlsruhe, Germany) discovered that the quality of junction characteristics improved dramatically when the base niobium layer was covered with a thin layer of aluminum. Their first junctions were of the type Nb/Al-oxide/Ag (this structure is used in basic studies of a tunnel junction, where the second electrode must be a normal metal), and Nb/Al-oxide/PbBi (an alloy of Lead with small amounts of Bismuth). These junctions were prepared via sputtering of a base Nb/Al electrode—a thick (about 1500 nm) layer of Nb covered in situ with a thin (1 to 10 nm) layer of Al. This structure was then removed from a sputtering system and oxidized for a few minutes in room air. This exposure to air created a tunnel barrier, which, upon close examination, turned out to be composed entirely of aluminum oxide , even in samples where the overlayer thickness was extremely small, a few monolayers of aluminum. Then the oxidized base electrode was transferred to a different deposition chamber—a thermal evaporator—where it was masked using mechanical shadow masks and covered with Ag or PbBi counter-electrode. The whole process was decisively non-industrial; it created large-area (about 1 mm on a side) semi-soft (soft-metal counter-electrode) junctions, which were studied to understand the properties of an aluminum overlayer and to examine basic physics aspects of normal and Josephson tunneling in such junctions. It became apparent that a thin aluminum overlayer eliminated all the previous problems researchers had experienced with native niobium oxide, which was poisoning the base Nb electrode even when it was covered with a soft counter-electrode. The scientific interest in clean tunneling into famously stubborn niobium was satisfied. Yet, in addition to these scientific pursuits, the incredible near-ideal quality of Nb/Al-oxide-PbBi tunnel junctions was duly noted, and this remarkable quality pointed to the desirability of replacing the soft, non-technological PbBi counter-lectrode with the second niobium electrode, thus creating all-refractory Josephson tunnel junctions.

Soon after this Al overlayer breakthrough, M. Gurvitch, working with M.A. Washington and H.A. Huggins, developed a whole-wafer process that began with the deposition of Nb and Al layers, followed by their in situ (within the sputtering system) controlled oxidation, forming the Nb/Al-oxide base structure, which was then covered, also in situ, by the second blanket Nb electrode. The resulting wafer covered with a continuous Nb/Al-oxide/Nb trilayer structure was processed to form individual Josephson tunnel junctions using selective anodization and reactive ion etching. The results exceeded all expectations: the resulting junctions had nearly ideal BCS (Bardeen-Cooper-Schrieffer) characteristics, were uniform and reproducible, were completely immune to thermal cycling between the helium boiling temperature of 4.2 K and room temperature, and the tunnel barrier possessed a low dielectric constant of Al 2 O 3 , about four times lower than in niobium oxide, which was very important in envisioned applications in superconducting digital circuits.

By the Fall of 1983, all the parts of the puzzle were in place: the whole-wafer idea of Kroeger et al. was implemented on the Nb/Al-oxide/Nb structure (often called trilayer structure ), and technologically sound processing methods were developed that allowed delineation of individual junctions and construction of superconducting circuits containing these junctions. It turned out that the presence of aluminum oxide not only dramatically improved junction quality but also brought about important technological advantages during junction preparation.

From 1983 onward, Nb/Al-oxide/Nb Josephson junctions became the workhorse of superconducting electronics worldwide. Although this breakthrough did not stop IBM from already-decided closing of its Josephson Signal Processor project in September 1983, the methods developed at Bell Labs were picked up by a number of laboratories and companies around the world, notably they played a decisive role in obtaining government funding for Japanese superconductivity efforts, which were structured as part of their ambitious Fifth Generation Computer Systems (FGCS) project which lasted from 1982 to 1992. Indeed, Japanese researchers, picking up where IBM and Bell Labs left off, in a few years' time succeeded in demonstrating a small but viable superconducting processor based on Nb/Al-oxide/Nb junctions. In the U.S., a new company, HYPRES, Inc., was organized in Elmsford, NY, by Sadig Faris, who had previously been employed by IBM. The initial aim of HYPRES was to use new Nb/Al-oxide/Nb technology to commercialize superconducting electronics.

The principles laid down in the early 1980s have withstood the test of time; this technology is still used today, more than forty years later, to fabricate all superconducting circuits and devices, from SQUIDs and voltage standards to Josephson digital circuits and even some superconducting qubits.

In recent times, processes for making superconducting digital circuits have been developed to a high degree. This processing sophistication brings them into the mainstream of VLSI integrated circuit (IC) technology. And yet, Josephson junctions in these complex, multilayered circuits are still formed essentially the same way as in the original Bell Labs process developed by M. Gurvitch, M. A. Washington, and H. A. Huggins.

#### Sputtering deposition

Whole wafer processes use sputtering deposition. This is an alternative deposition technique, to reduce potential interactions between the evaporant and supporting material. In this method, the target material is bombarded with energetic ions . The ions can eject the target atoms into the gas phase. The sputter deposition method allows more complex alloys to be deposited, but sputter deposition rates are slow.

This is the preferred deposition method for Nb/Al-AlOx/Nb Josephson junctions.

### Etching

Usually a high-resolution lithography using an electron beam or focused ion beam etches the pattern on the device. Dry or wet etching can be used. Dry etching processes use physical etchants or reactive gases, while wet etching processes submerge the substrate in liquid etchants.

## Uses

### Superconducting qubits

Superconducting qubits using Josephson junctions are popular candidates for a quantum processor because superconductors inherently have very low dissipation, making long coherence times possible. These kinds of qubits are used by Google , IBM , Rigetti , and others to engineer quantum processors.

A superconducting qubit is essentially a nonlinear resonator formed from the Josephson inductance and its junction capacitance, which acts like a non-linear LC circuit . Since this oscillator is nonlinear, it is anharmonic , and allows the first two energy levels of the circuit to be addressed independently of the others. This is necessary because the system in principle has many energy levels, but the qubit's operating space includes only the two lowest states. In fact, In order to detect energy quantization at all, a circuit must include a non-linear element.

Almost all superconducting qubit architectures use Josephson junctions (with exceptions being topological qubits ). The standard implementation is a Josephson tunnel junction, but other architectures use constriction junctions.

### SQUIDs

A SQUID, or superconducting quantum interference device , consists of two Josephson junctions arranged in a loop, with magnetic flux threading through it. SQUIDs effectively act as a single flux-tunable Josephson junction, because the applied flux biases the phase across the junctions. Thus, the SQUID's critical current, and hence its effective inductance, can be tuned by the external magnetic flux.

### Logic circuits

Because Josephson junctions have a critical current, they can be fashioned into a binary logic circuit : when the current through the junction is less than the critical current, the voltage is zero, but once it exceeds the critical current , the voltage oscillates in time. Thus, Josephson junction switching between zero-voltage and finite-voltage states can be used in logic circuits.An example of applications in logic circuits is the rapid single flux quantum technology, which stores information in the form of magnetic flux quanta , transferred by single flux quantum voltage pulses produced by Josephson junctions.

Logic devices using Josephson junctions have ultra-high switching speeds, of around 10 picoseconds, and low power dissipation of around 1 μW. It is an active area of research because it may be able to overcome scaling limits in CMOS electronics. However, its level of integration remains significantly less than that of CMOS circuits.

### Voltage standard

Highly integrated arrays of Josephson junctions, containing more than 10,000 or even 100,000 junctions, can be used as a voltage standard. This voltage standard has achieved accuracy of 1 part per billion or better, allowing the volt to be referenced to the knowledge of just two fundamental physical constants, Planck's constant h and the elementary charge e. The junctions used are typically SIS or SNS. When they are SIS junctions, they are invariably made in the trilayer process with Nb/Al-oxide-Nb tunnel junctions (see the "Fabrication" section above).

### Demonstrating macroscopic quantum phenomena

A centimeter-wide superconducting circuit containing a Josephson junction was used by John Clarke , Michel H. Devoret , and John M. Martinis to demonstrate macroscopic quantum phenomena . In the device, billions of superconducting electrons in the circuit formed a collective macroscopic system described by a single quantum phase. By showing evidence of tunneling behavior in the junction, they were able to demonstrate quantum tunneling in a macroscopic object. This was the subject of the 2025 Nobel Prize in Physics .

### Ultra-low noise amplifiers

Josephson junctions are used in ultra-low noise amplifiers, like Josephson parametric amplifiers (JPAs) and traveling-wave parametric amplifiers (TWPAs), because they are largely dissipationless. Other non-linear elements such as semiconductors contribute to dissipation, even in low noise amplifiers like HEMTs . However, because there is no added noise when using a Josephson junction, superconducting amplifiers using Josephson junctions are able to operate near the quantum noise limit. This makes them useful for experiments that require extremely low noise, such as axion detection and readout of solid-state qubits.
