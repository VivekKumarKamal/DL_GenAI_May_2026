# Discrete dipole approximation codes

> **Query Topic**: inhomogeneous physical framework (Rank #2 Search Result)  
> **Source Queue**: train (Row ID: 511, Frequency: 5)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Discrete_dipole_approximation_codes

---

This is a list of software packages for calculating scattering and absorption of light using Discrete dipole approximation (DDA).
Most of the software applies to arbitrary-shaped inhomogeneous nonmagnetic particles and particle systems in free space or homogeneous dielectric host medium. The calculated quantities typically include the Mueller matrices, integral cross-sections (extinction, absorption, and scattering), internal fields and angle-resolved scattered fields (phase function). There are some published comparisons of existing DDA codes.


== General-purpose open-source software ==
These packages typically use regular grids (cubical or rectangular cuboid), conjugate gradient method to solve large systems of linear equations and FFT-acceleration of the matrix-vector products which uses convolution theorem. Complexity of this approach is almost linear in number of dipoles for both time and memory.


== Specialized software ==
These list include software that do not qualify for the previous section. The reasons may include the following: source code is not available, FFT acceleration is absent or reduced, the code focuses on specific applications not allowing easy calculation of standard scattering quantities.


== See also ==
Computational electromagnetics
Mie theory
Finite-difference time-domain method
Method of moments (electromagnetics)


== References ==
