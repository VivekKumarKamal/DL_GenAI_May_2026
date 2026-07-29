# Permeability (electromagnetism)

> **Query Topic**: magnetic susceptibility (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 137, Frequency: 11)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Permeability_(electromagnetism)

---

In electromagnetism , permeability is the measure of magnetization produced in a material in response to an applied magnetic field . Permeability is typically represented by the (italicized) Greek letter μ . It is the ratio of the magnetic induction $B$ to the magnetizing field $H$ in a material. The term was coined by Lord Kelvin in 1872, and is used alongside its electrostatic equivalent, permittivity , coined by Oliver Heaviside in 1885. The reciprocal of permeability is magnetic reluctivity. [ citation needed ]

In SI units, permeability is measured in henries per meter (H/m), or equivalently in newtons per ampere squared (N/A 2 ). The permeability constant μ 0 , also known as the magnetic constant or the permeability of free space, is the proportionality between magnetic induction and magnetizing force when forming a magnetic field in a classical vacuum .

A closely related property of materials is magnetic susceptibility , which is a dimensionless proportionality factor that indicates the degree of magnetization of a material in response to an applied magnetic field.

## Explanation

In the macroscopic formulation of electromagnetism , there appear two different kinds of magnetic field :

- the magnetizing field H which is generated around electric currents and displacement currents , and also emanates from the poles of magnets . The SI units of H are amperes per meter.

- the magnetic flux density B which acts back on the electrical domain, by curving the motion of charges and causing electromagnetic induction . The SI units of B are volt -seconds per square meter , a ratio equivalent to one tesla .

The concept of permeability arises since in many materials (and in vacuum), there is a simple relationship between H and B at any location or time, in that the two fields are precisely proportional to each other:

$\mathbf {B} =\mu \mathbf {H} ,$

where the proportionality factor μ is the permeability, which depends on the material. The permeability of vacuum (also known as permeability of free space) is a physical constant, denoted μ 0 . The SI units of μ are volt-seconds per ampere-meter, equivalently henry per meter. Typically μ would be a scalar, but for an anisotropic material, μ could be a second rank tensor .

However, inside strong magnetic materials (such as iron, or permanent magnets ), there is typically no simple relationship between H and B . The concept of permeability is then nonsensical or at least only applicable to special cases such as unsaturated magnetic cores . Not only do these materials have nonlinear magnetic behaviour, but often there is significant magnetic hysteresis , so there is not even a single-valued functional relationship between B and H . However, considering starting at a given value of B and H and slightly changing the fields, it is still possible to define an incremental permeability as:

$\Delta \mathbf {B} =\mu \,\Delta \mathbf {H} .$

assuming B and H are parallel.

In the microscopic formulation of electromagnetism , where there is no concept of an H field, the vacuum permeability μ 0 appears directly (in the SI Maxwell's equations) as a factor that relates total electric currents and time-varying electric fields to the B field they generate. In order to represent the magnetic response of a linear material with permeability μ , this instead appears as a magnetization M that arises in response to the B field: $\mathbf {M} =\left(\mu _{0}^{-1}-\mu ^{-1}\right)\mathbf {B}$ . The magnetization in turn is a contribution to the total electric current—the magnetization current .

## Relative permeability and magnetic susceptibility

Relative permeability, denoted by the symbol $\mu _{\mathrm {r} }$ , is the ratio of the permeability of a specific medium to the permeability of free space μ 0 :

$\mu _{\mathrm {r} }={\frac {\mu }{\mu _{0}}},$

where $\mu _{0}\approx$ 4 π × 10 −7 H/m is the magnetic permeability of free space . In terms of relative permeability, the magnetic susceptibility is

$\chi _{m}=\mu _{r}-1.$

The number χ m is a dimensionless quantity , sometimes called volumetric or bulk susceptibility, to distinguish it from χ p ( magnetic mass or specific susceptibility) and χ M ( molar or molar mass susceptibility).

## Diamagnetism

Diamagnetism is the property of an object which causes it to create a magnetic field in opposition of an externally applied magnetic field, thus causing a repulsive effect. Specifically, an external magnetic field alters the orbital velocity of electrons around their atom's nuclei, thus changing the magnetic dipole moment in the direction opposing the external field. Diamagnets are materials with a magnetic permeability less than μ 0 (a relative permeability less than 1).

Consequently, diamagnetism is a form of magnetism that a substance exhibits only in the presence of an externally applied magnetic field. It is generally a quite weak effect in most materials, although superconductors exhibit a strong effect.

## Paramagnetism

Paramagnetism is a form of magnetism which occurs only in the presence of an externally applied magnetic field. Paramagnetic materials are attracted to magnetic fields, hence have a relative magnetic permeability greater than one (or, equivalently, a positive magnetic susceptibility ).

The magnetic moment induced by the applied field is linear in the field strength, and it is rather weak . It typically requires a sensitive analytical balance to detect the effect. Unlike ferromagnets , paramagnets do not retain any magnetization in the absence of an externally applied magnetic field, because thermal motion causes the spins to become randomly oriented without it. Thus the total magnetization will drop to zero when the applied field is removed. Even in the presence of the field, there is only a small induced magnetization because only a small fraction of the spins will be oriented by the field. This fraction is proportional to the field strength and this explains the linear dependency. The attraction experienced by ferromagnets is non-linear and much stronger so that it is easily observed, for instance, in magnets on one's refrigerator.

## Gyromagnetism

For gyromagnetic media (see Faraday rotation ) the magnetic permeability response to an alternating electromagnetic field in the microwave frequency domain is treated as a non-diagonal tensor expressed by:

${\begin{aligned}\mathbf {B} (\omega )&={\begin{vmatrix}\mu _{1}&-i\mu _{2}&0\\i\mu _{2}&\mu _{1}&0\\0&0&\mu _{z}\end{vmatrix}}\mathbf {H} (\omega )\end{aligned}}.$

## Values for some common materials

The following table should be used with caution as the permeability of ferromagnetic materials varies greatly with field strength and specific composition and fabrication. For example, 4% electrical steel has an initial relative permeability (at or near 0 T) of 2,000 and a maximum of 38,000 at T = 1 and different range of values at different percent of Si and manufacturing process, and, indeed, the relative permeability of any material at a sufficiently high field strength trends toward 1 (at magnetic saturation).

A good magnetic core material must have high permeability.

For passive magnetic levitation a relative permeability below 1 is needed (corresponding to a negative susceptibility).

Permeability varies with a magnetic field. Values shown above are approximate and valid only at the magnetic fields shown. They are given for a zero frequency; in practice, the permeability is generally a function of the frequency. When the frequency is considered, the permeability can be complex , corresponding to the in-phase and out of phase response.

## Complex permeability

A useful tool for dealing with high frequency magnetic effects is the complex permeability. While at low frequencies in a linear material the magnetic field and the auxiliary magnetic field are simply proportional to each other through some scalar permeability, at high frequencies these quantities will react to each other with some lag time. These fields can be written as phasors , such that

$H=H_{0}e^{j\omega t}\qquad B=B_{0}e^{j\left(\omega t-\delta \right)}$

where $\delta$ is the phase delay of $B$ from $H$ .

Understanding permeability as the ratio of the magnetic flux density to the magnetic field, the ratio of the phasors can be written and simplified as

$\mu ={\frac {B}{H}}={\frac {B_{0}e^{j\left(\omega t-\delta \right)}}{H_{0}e^{j\omega t}}}={\frac {B_{0}}{H_{0}}}e^{-j\delta },$

so that the permeability becomes a complex number.

By Euler's formula , the complex permeability can be translated from polar to rectangular form,

$\mu ={\frac {B_{0}}{H_{0}}}\cos(\delta )-j{\frac {B_{0}}{H_{0}}}\sin(\delta )=\mu '-j\mu ''.$

The ratio of the imaginary to the real part of the complex permeability is called the loss tangent ,

$\tan(\delta )={\frac {\mu ''}{\mu '}},$

which provides a measure of how much power is lost in material versus how much is stored.
