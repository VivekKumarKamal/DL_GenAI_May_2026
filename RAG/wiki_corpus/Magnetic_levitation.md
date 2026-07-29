# Magnetic levitation

> **Query Topic**: Earnshaw's theorem state (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 361, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Magnetic_levitation

---

Magnetic levitation ( maglev ) or magnetic suspension is a method by which an object is suspended with no support other than magnetic fields . Magnetic force is used to counteract the effects of the gravitational force and any other forces.

The two primary issues involved in magnetic levitation are (a) lifting forces – providing an upward force sufficient to counteract gravity, and (b) stability – ensuring that the system does not spontaneously slide or flip into a configuration where the lift is neutralized.

Magnetic levitation is used for maglev trains, contactless melting , magnetic bearings , and for product display purposes.

## Lift

Magnetic materials and systems are able to attract or repel each other with a force dependent on the magnetic field and the area of the magnets. For example, the simplest example of lift would be a simple dipole magnet positioned in the magnetic fields of another dipole magnet, oriented with like poles facing each other, so that the force between magnets repels the two magnets.

Essentially all types of magnets have been used to generate lift for magnetic levitation: permanent magnets , electromagnets , ferromagnetism , diamagnetism , superconducting magnets , and magnetism due to induced currents in conductors.

To calculate the amount of lift, a magnetic pressure can be defined. For example, the magnetic pressure of a magnetic field on a superconductor can be calculated by:

$P_{\text{mag}}={\frac {B^{2}}{2\mu _{0}}}$

where $P_{\text{mag}}$ is the force per unit area in pascals , $B$ is the magnetic field just above the superconductor in teslas , and $\mu _{0}$ = 4π × 10 −7 N·A −2 is the permeability of the vacuum.

## Stability

Earnshaw's theorem proves that using only paramagnetic materials (such as ferromagnetic iron) it is impossible for a static system to stably levitate against gravity.

For example, the simplest example of lift with two simple dipole magnets repelling is highly unstable, since the top magnet can slide sideways or flip over, and it turns out that no configuration of magnets can produce stability.

However, servomechanisms (spinning/rotation), the use of diamagnetic materials, superconduction , or systems involving eddy currents allow stability to be achieved.

In some cases the lifting force is provided by magnetic repulsion, but stability is provided by a mechanical support bearing little load. This is termed pseudo-levitation .

### Static stability

Static stability means that any small displacement away from a stable equilibrium causes a net force to push it back to the equilibrium point.

Earnshaw's theorem proved conclusively that it is not possible to levitate stably using only static, macroscopic, paramagnetic fields. The forces acting on any paramagnetic object in any combinations of gravitational , electrostatic , and magnetostatic fields will make the object's position, at best, unstable along at least one axis, and it can be in unstable equilibrium along all axes. However, several possibilities exist to make levitation viable, for example, the use of electronic stabilization or diamagnetic materials (since relative magnetic permeability is less than one ); it can be shown that diamagnetic materials are stable along at least one axis, and can be stable along all axes. Conductors can have a relative permeability to alternating magnetic fields of below one, so some configurations using simple AC-driven electromagnets are self stable.

### Dynamic stability

When a levitation system uses negative feedback to maintain its equilibrium by damping out any oscillations that may occur, it has achieved dynamic stability.

For the case of a static magnetic field, the magnetic force is a conservative force and therefore can exhibit no built-in damping. In practice many of the levitation schemes are marginally stable and, when non-idealities of physical systems are considered, result in negative damping. This negative damping gives rise to exponentially growing oscillations around the magnetic field's unstable equilibrium point, inevitably causing the levitating object to be ejected from the magnetic field.

Dynamic stability on the other hand, can be achieved by spinning a permanent magnet having poles slightly off the rotation plane (called tilt) in constant speed within a range which can hold another dipole magnet in the air.

For the magnetic levitation scheme to be stable, negative feedback from an external control system can be also used to add damping to the system. This can be accomplished in a number of ways:

- external mechanical damping (in the support), such as dashpots , air drag , etc.

- eddy current damping (conductive metal influenced by field)

- tuned mass dampers in the levitated object

- electromagnets controlled by electronics

## Methods

For successful levitation and control of all 6 axes (degrees of freedom; 3 translational and 3 rotational) a combination of permanent magnets and electromagnets or diamagnets or superconductors as well as attractive and repulsive fields can be used. From Earnshaw's theorem at least one stable axis must be present for the system to levitate successfully, but the other axes can be stabilized using ferromagnetism.

The primary ones used in maglev trains are servo-stabilized electromagnetic suspension (EMS), electrodynamic suspension (EDS).

### Mechanical constraint (pseudo-levitation)

With a small amount of mechanical constraint for stability, achieving pseudo-levitation is a relatively straightforward process.

If two magnets are mechanically constrained along a single axis, for example, and arranged to repel each other strongly, this will act to levitate one of the magnets above the other.

Another geometry is where the magnets are attracted, but prevented from touching by a tensile member, such as a string or cable.

Another example is the Zippe-type centrifuge where a cylinder is suspended under an attractive magnet, and stabilized by a needle bearing from below.

Another configuration consists of an array of permanent magnets installed in a ferromagnetic U-shaped profile and coupled with a ferromagnetic rail. The magnetic flux crosses the rail in a direction transversal to the first axis and creates a closed-loop on the U-shaped profile. This configuration generates a stable equilibrium along the first axis that maintains the rail centered on the flux crossing point (minimum magnetic reluctance ) and allows to bear a load magnetically. On the other axis, the system is constrained and centered by mechanical means, such as wheels.

### Servomechanisms

The attraction from a fixed-strength magnet decreases with increased distance, and increases at closer distances. This is unstable. For a stable system, the opposite is needed: variations from a stable position should push it back to the target position.

Stable magnetic levitation can be achieved by measuring the position and speed of the object being levitated, and using a feedback loop which continuously adjusts one or more electromagnets to correct the object's motion, thus forming a servomechanism .

Many systems use magnetic attraction pulling upward against gravity for these kinds of systems as this gives some inherent lateral stability, but some use a combination of magnetic attraction and magnetic repulsion to push upward.

Either system represents examples of ElectroMagnetic Suspension (EMS). For a very simple example, some tabletop levitation demonstrations use this principle, and the object cuts a beam of light or Hall effect sensor method is used to measure the position of the object. The electromagnet is above the object being levitated; the electromagnet is turned off whenever the object gets too close, and turned back on when it falls further away. Such a simple system is not very robust; far more effective control systems exist, but this illustrates the basic idea.

EMS magnetic levitation trains are based on this kind of levitation: The train wraps around the track, and is pulled upward from below. The servo controls keep it safely at a constant distance from the track.

### Induced currents

These schemes work due to repulsion due to Lenz's law . When a conductor is presented with a time-varying magnetic field, electrical currents are set up in the conductor which create a magnetic field that causes a repulsive effect.

These kinds of systems typically show an inherent stability, although extra damping is sometimes required.

#### Relative motion between conductors and magnets

If one moves a base made of a very good electrical conductor such as copper , aluminium , or silver close to a magnet, an ( eddy ) current will be induced in the conductor that will oppose the changes in the field and create an opposite field that will repel the magnet ( Lenz's law ). At a sufficiently high rate of movement, a suspended magnet will levitate on the metal, or vice versa with suspended metal. Litz wire made of wire thinner than the skin depth for the frequencies seen by the metal works much more efficiently than solid conductors. Figure-8 coils can be used to keep something aligned.

An especially technologically interesting case of this comes when one uses a Halbach array instead of a single-pole permanent magnet, as this almost doubles the field strength, which in turn almost doubles the strength of the eddy currents. The net effect is to more than triple the lift force. Using two opposed Halbach arrays increases the field even further.

Halbach arrays are also well-suited to magnetic levitation and stabilisation of gyroscopes and spindles of electric motors and generators .

#### Oscillating electromagnetic fields

A conductor can be levitated above an electromagnet (or vice versa) with an alternating current flowing through it. This causes any regular conductor to behave like a diamagnet, due to the eddy currents generated in the conductor. Since the eddy currents create their own fields which oppose the magnetic field, the conductive object is repelled from the electromagnet, and most of the field lines of the magnetic field will no longer penetrate the conductive object.

This effect requires non-ferromagnetic but highly conductive materials like aluminium or copper, as the ferromagnetic ones are also strongly attracted to the electromagnet (although at high frequencies the field can still be expelled) and tend to have a higher resistivity giving lower eddy currents. Again, litz wire gives the best results.

The effect can be used for stunts such as levitating a telephone book by concealing an aluminium plate within it.

At high frequencies (a few tens of kilohertz or so) and kilowatt powers small quantities of metals can be levitated and melted using levitation melting without the risk of the metal being contaminated by the crucible.

One source of oscillating magnetic field that is used is the linear induction motor . This can be used to levitate as well as provide propulsion.

### Diamagnetically stabilized levitation

Earnshaw's theorem does not apply to diamagnets . These behave in the opposite manner to normal magnets owing to their relative permeability of μ r < 1 (i.e. negative magnetic susceptibility ). Diamagnetic levitation can be inherently stable.

A permanent magnet can be stably suspended by various configurations of strong permanent magnets and strong diamagnets. When using superconducting magnets, the levitation of a permanent magnet can even be stabilized by the small diamagnetism of water in human fingers.

### Diamagnetic levitation

Diamagnetism is the property of an object which causes it to create a magnetic field in opposition to an externally applied magnetic field, thus causing the material to be repelled by magnetic fields. Diamagnetic materials cause lines of magnetic flux to curve away from the material. Specifically, an external magnetic field alters the orbital velocity of electrons around their nuclei, thus changing the magnetic dipole moment .

According to Lenz's law, this opposes the external field. Diamagnets are materials with a magnetic permeability less than μ 0 (a relative permeability less than 1). Consequently, diamagnetism is a form of magnetism that is only exhibited by a substance in the presence of an externally applied magnetic field. It is generally quite a weak effect in most materials, although superconductors exhibit a strong effect.

#### Direct diamagnetic levitation

A substance that is diamagnetic repels a magnetic field. All materials have diamagnetic properties, but the effect is very weak, and is usually overcome by the object's paramagnetic or ferromagnetic properties, which act in the opposite manner. Any material in which the diamagnetic component is stronger will be repelled by a magnet.

Diamagnetic levitation can be used to levitate very light pieces of pyrolytic graphite or bismuth above a moderately strong permanent magnet. As water is predominantly diamagnetic, this technique has been used to levitate water droplets and even live animals, such as a grasshopper, frog and a mouse. However, the magnetic fields required for this are very high, typically in the range of 16 teslas , and therefore create significant problems if ferromagnetic materials are nearby. Operation of this electromagnet used in the frog levitation experiment required 4 MW (4000000 watts) of power.

The minimum criterion for diamagnetic levitation is $B{\frac {dB}{dz}}=\mu _{0}\,\rho \,{\frac {g}{\chi }}$ , where:

- $\chi$ is the magnetic susceptibility

- $\rho$ is the density of the material

- $g$ is the local gravitational acceleration (−9.8 m / s 2 on Earth)

- $\mu _{0}$ is the permeability of free space

- $B$ is the magnetic field

- ${\frac {dB}{dz}}$ is the rate of change of the magnetic field along the vertical axis.

Assuming ideal conditions along the z -direction of solenoid magnet:

- Water levitates at $B{\frac {dB}{dz}}\approx 1400\ \mathrm {T^{2}/m}$

- Graphite levitates at $B{\frac {dB}{dz}}\approx 375\ \mathrm {T^{2}/m} .$

### Superconductors

Superconductors may be considered perfect diamagnets , and completely expel magnetic fields due to the Meissner effect when the superconductivity initially forms; thus superconducting levitation can be considered a particular instance of diamagnetic levitation. In a type-II superconductor , the levitation of the magnet is further stabilized due to flux pinning within the superconductor; this tends to stop the superconductor from moving with respect to the magnetic field, even if the levitated system is inverted.

These principles are exploited by EDS (Electrodynamic Suspension), superconducting bearings , flywheels , etc.

A very strong magnetic field is required to levitate a train. The SCMaglev trains have superconducting magnetic coils, but the SCMaglev levitation is not due to the Meissner effect.

### Rotational stabilization

A magnet or properly assembled array of magnets can be stably levitated against gravity when gyroscopically stabilized by spinning it in a properly sized toroidal field created by either, a single magnet, or base of an array of magnets forming a ring and having the necessary toroidal field profile. However, this only works while the rate of precession is between both upper and lower critical thresholds—the region of stability is quite narrow both spatially and in the required rate of precession. [ citation needed ]

The first discovery of this phenomenon was by Roy M. Harrigan , a Vermont inventor who patented a levitation device in 1983 based upon it. [ better source needed ] Several devices using rotational stabilization (such as the popular Levitron branded levitating top toy) have been developed citing this patent. Non-commercial devices [ specify ] have been created for university research laboratories, generally using magnets too powerful for safe public interaction. [ citation needed ]

### Strong focusing

Earnshaw's theory strictly only applies to static fields. Alternating magnetic fields, even purely alternating attractive fields, can induce stability and confine a trajectory through a magnetic field to give a levitation effect.

This is used in particle accelerators to confine and lift charged particles, and has been proposed for maglev trains as well.

## Uses

Known uses of magnetic levitation include maglev trains, contactless melting , magnetic bearings , and for product display purposes. Moreover, recently magnetic levitation has been approached in the field of microbotics .

### Maglev transportation

Maglev , or magnetic levitation , is a system of transportation that suspends, guides and propels vehicles, predominantly trains, using magnetic levitation from a very large number of magnets for lift and propulsion. This method has the potential to be faster, quieter and smoother than wheeled mass transit systems. The technology has the potential to exceed 6,400 km/h (4,000 mi/h) if deployed in an evacuated tunnel. If not deployed in an evacuated tube the power needed for levitation is usually not a particularly large percentage and most of the power needed is used to overcome air drag , as with any other high speed train.

The highest recorded speed of a maglev train is 603 kilometers per hour (374.69 mph), achieved in Japan on 21 April 2015; 28.2 km/h faster than the conventional TGV speed record. Maglev trains exist and are planned across the world. Notable projects in Asia include Central Japan Railway Company's superconducting maglev train and Shanghai's maglev train , the oldest commercial maglev still in operation. Elsewhere, various projects have been considered across Europe and Northeast Maglev aims to overhaul North America's Northeast Corridor with JR Central's SCMaglev technology.

### Magnetic bearings

- Magnetic bearings

- Flywheels

- Centrifuges

- Magnetic ring spinning

### Levitation melting

Electromagnetic levitation (EML), patented by Muck in 1923, is one of the oldest levitation techniques used for containerless experiments. The technique levitates objects using electromagnets . A typical EML coil has reversed winding of upper and lower sections energized by a radio frequency power supply.

### Microbotics

In the field of microbotics , strategies which exploit magnetic levitation have been investigated. In particular, it has been demonstrated that through such a technique, control of multiple microscale-sized agents within a defined workspace can be achieved. Several research studies report the realization of different custom setups to properly obtain the desired control of microrobots. In Philips laboratories in Hamburg a custom clinical scale system, integrating both permanent magnets and electromagnets , was used to perform magnetic levitation and 3D navigation of a single magnetic object. Another research group integrated a higher number of electromagnets, thus more magnetic degrees of freedom , to achieve 3D independent control of multiple objects through magnetic levitation.

#### DM3 System

Microrobot involving magnetic levitation has been studied by SRI International (Stanford Research Institute) for many years. This small-scale multi-agent robotic system is called the Diamagnetic Micro Manipulation or the DM3 system. The DM3 contains a microrobot built with magnets that levitate and move on the surface of a PCB driving platform. The microrobot in this system was built with an array of NdFeB magnets shown in figure File:Microrobot Magnet Disposition.png . The dimension of magnets varies between different versions, while typically in the range of 1.4 -2 mm square shape with a lower height. The poles of magnets were positioned as a checkerboard array to fit the magnetic field generated by the PCB platform. The robot can be built in different size depending on the size of the array. Prototypes tested in SRI papers are mainly 2*2, 3*3, and 5*5 squares.

The driving platform PCB was built with multiple layers of wire traces like a voice coil actuation. Shown in figure there are four layers of wires in the PCB which represents two sets placed perpendicular to each other that stand for X and Y direction movement. From top to bottom, the order comes in XYXY that cross each other evenly and same axis were interlaced to control actuation. Since the force created by every layer must be the same on the circuit, deeper layers need higher current to transmit the same magnetic force to the robots on top. Set of currents with 0.25A, 0.33A, 0.5A, and 0.7A were used at SRI. One square of the above 4-layer system acts as a zone on the driving platform. This enables the circuit to control multiple robots in the same zone easily, but each robot cannot move separately. However, the platform can be divided into multiple zones which enable the separate control of robots in different zones.

Finally, a thin layer of pyrolytic graphite (500 um) acts as diamagnetic layer, placed on the top to provide stable levitation. Thin copper (15 um) placed above the graphite was used in earlier versions of the system for eddy current damping.

The basic system for 1DOF movement consists of two serpentine traces, individually actuated. Figure shows the schematic of the trace paths and a 3x3 magnet microrobot on top. On position number 1, the magnets are in their equilibrium position where the magnetic flux density is the highest, in between two opposite currents from the same trace path.

On moving from 1 to 2, the first trace path is turned off while the second is turned on. This causes the magnets to move to their new equilibrium, toward the higher magnetic flux density.

Repeating this procedure with opposite currents on the same trace paths, a movement in the desired direction is produced.

To find the velocity, the forces on the microrobot must be analyzed (fig. ). The microrobot is supposed to levitate and so no friction forced is produced, other than the air drag which is also not considered.

The force produced by the interaction of the magnetic moments of the microrobot and the flux density of the serpentine traces is:

$F=\nabla ({\overrightarrow {m}}\cdot {\overrightarrow {B}})$

The magnetic moment vector, given the orientation requirement for the diamagnetic levitation, is:

${\overrightarrow {m}}={\bigl (}{\begin{smallmatrix}0&0&{\frac {B_{r}V_{m}}{\mu _{0}}}\\\end{smallmatrix}}{\bigr )}$

Meanwhile, the contribution to the B field by the 2 closest traces is:

${\vec {B}}={\vec {B}}_{1}+{\vec {B}}_{2}=\ \mu _{0}{\frac {{\vec {I_{1}}}\times {\vec {r}}_{1}}{2\pi \left|{\vec {r}}_{1}\right|^{2}}}+\mu _{0}{\frac {{\vec {I_{2}}}\times {\vec {r}}_{2}}{2\pi \left|{\vec {r}}_{2}\right|^{2}}}$

Since for this approximation ${\overrightarrow {m}}\cdot {\overrightarrow {B}}$ is not dependent on y or z, their derivatives are zero and only force in the x direction is produced:

$F_{x}={\frac {B_{r}V_{m}I}{2\pi }}{\frac {\partial }{\partial x}}\left({\frac {x-\Delta x_{0}}{(x-\Delta x_{0})^{2}+d^{2}}}+{\frac {x+\Delta x_{0}}{(x+\Delta x_{0})^{2}+d^{2}}}\right)$

This is the only force applied on the magnet, and it can be equated to the robot's mass multiplied by its acceleration. This equation can be integrated to find the velocity of the microrobot:

$F_{x}=mv{\frac {dv}{dx}}$

${\frac {B_{r}V_{m}I}{2\pi m}}\left({\frac {2\Delta x_{0}}{4\Delta x_{0}^{2}+d^{2}}}\right)={\frac {1}{2}}v_{max}^{2}$

Introducing the relation between magnet volume, mass, and density $V_{m}={\frac {m}{\rho _{m}}}$ in the previous equation cancels out the mass, which means that if more magnets are added (N number of magnets), force will increase linearly:

$v_{max}={\sqrt {N{\frac {B_{r}I}{\pi \rho _{m}}}\left({\frac {2\Delta x_{0}}{4\Delta x_{0}^{2}+d^{2}}}\right)}}$

This is the expression for the robot speed as a function of the current.

For a second DOF, more traces must be added. Two more intertwined serpentine traces must be added below the existing ones, rotated 90 degrees, to generate forces in the Y direction. Intensity on these traces will have to be higher to account for the higher distance.

Diamagnetically levitated milli- and micro-robots can be controlled and moved with near-zero noise in their force, and they can be made intrinsically stable. In this way there is highly optimized control that uses zone or area control.

Diamagnetic levitation can produce two effects on a micro robot. The first is reducing the sliding friction and the second is fully levitating the micro robot. The fully levitation system will be the focus. To produce passive levitation a diamagnetic layer (such as graphite) must exist in the presence of a ferromagnet (such as NdFeB). Diamagnetic materials are characterized by having negative susceptibility, induced magnetic moment opposite to the external magnetic field. For that reason, they are repelled by an external magnetic field and tend to move toward the field minimum. This repulsive force is a result of the diamagnets having a magnetization direction antiparallel to the external magnetic fields.

The magnetizations of diamagnetic materials vary with an applied magnetic field which can be given as:

$M=\chi _{p}H$

Where $H$ is the magnetic field strength and $\chi _{p}$ is the dimensionless susceptibility. For an object with volume $V_{p}$ , the induced magnetic moment m can be given by:

${\overrightarrow {m}}=\chi _{p}{\frac {V_{p}}{\mu _{0}}}{\overrightarrow {B}}$

The magnetic force acting on the object is there for described as:

$F_{m}={\frac {\chi _{p}V_{p}}{\mu _{0}}}\nabla ({\overrightarrow {B}}\cdot {\overrightarrow {B}})$

If the object has density $\rho _{p}$ and is levitating in a medium with density $\rho _{m}$ and magnetic susceptibility $\chi _{m}$ the total energy of the object, with a magnetic and gravitational term, is:

$E={\frac {\chi _{p}-\chi _{m}}{2\mu _{0}}}V_{p}({\overrightarrow {B}}\cdot {\overrightarrow {B}})+(\rho _{p}-\rho _{m})V_{p}gz$

Such that the resulting force becomes:

$\sum F={\frac {\chi _{p}-\chi _{m}}{2\mu _{0}}}V_{p}\nabla ({\overrightarrow {B}}\cdot {\overrightarrow {B}})+(\rho _{p}-\rho _{m})V_{p}g{\overrightarrow {k}}$

The necessary condition for stability is:

$\chi _{p}-\chi _{m}<0$

To calculate the whole diamagnetic force acting on the levitated materials, each single dipole of the diamagnetic material must be considered. The diamagnetic force for the entire volume can be expressed as:

$F_{m}={\frac {\chi _{p}}{\mu _{0}}}\iiint _{V_{p}}\nabla ({\overrightarrow {B}}\cdot {\overrightarrow {B}})dv$

The diamagnetic repulsion force is proportional to the magnetic susceptibility of diamagnetic materials. To counteract gravity in the magnetic field, materials with strong diamagnetism and lightweight properties are preferred.

## Historical beliefs

Legends of magnetic levitation were common in ancient and medieval times, and their spread from the Roman world to the Middle East and later to India has been documented by the classical scholar Dunstan Lowe. The earliest known source is Pliny the Elder (first century AD), who described architectural plans for an iron statue that was to be suspended by lodestone from the vault of a temple in Alexandria. Many subsequent reports described levitating statues, relics or other objects of symbolic importance, and versions of the legend have appeared in diverse religious traditions, including Christianity, Islam, Buddhism, and Hinduism. In some cases they were interpreted as divine miracles, while in others they were described as natural phenomena falsely purported to be miraculous; one example of the latter comes from St Augustine, who refers to a magnetically suspended statue in his book The City of God ( c. 410 AD ). Another common feature of these legends, according to Lowe, is an explanation of the object's disappearance, often involving its destruction by non-believers in acts of impiety. Although the phenomenon itself is now understood to be physically impossible, as was first recognized by Samuel Earnshaw in 1842, stories of magnetic levitation have persisted to modern times, one prominent example being the legend of the suspended monument in the Konark Sun Temple in Eastern India.

## History

- 1839 Earnshaw's theorem showed electrostatic levitation cannot be stable; later theorem was extended to magnetostatic levitation by others

- 1913 Emile Bachelet awarded a patent in March 1912 for his "levitating transmitting apparatus" (patent no. 1,020,942) for electromagnetic suspension system

- 1933 Superdiamagnetism Walther Meissner and Robert Ochsenfeld (the Meissner effect )

- 1934 Hermann Kemper "monorail vehicle with no wheels attached." Reich Patent number 643316

- 1939 Braunbeck 's extension showed that magnetic levitation is possible with diamagnetic materials

- 1939 Bedford, Peer, and Tonks aluminum plate placed on two concentric cylindrical coils shows 6-axis stable levitation.

- 1961 James R. Powell and BNL colleague Gordon Danby electrodynamic levitation using superconducting magnets and "Null flux" figure-8 coils

- 1970s Spin stabilized magnetic levitation Roy M. Harrigan

- 1974 Magnetic river Eric Laithwaite and others

- 1979 transrapid train carried passengers

- 1981 First single-tether magnetic levitation system exhibited publicly ( Tom Shannon , Compass of Love, collection Musee d'Art Moderne de la Ville de Paris)

- 1984 Low-speed maglev shuttle in Birmingham Eric Laithwaite and others

- 1997 Diamagnetically levitated live frog Andre Geim

- 1999 Inductrack permanent magnet electrodynamic levitation (General Atomics)

- 2000 The first man-loading HTS maglev test vehicle "Century" in the world was successfully developed in China.

- 2024 The first passive maglev train was unveiled and demonstrated in Verona, Italy .
