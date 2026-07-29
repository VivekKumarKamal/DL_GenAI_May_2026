# Projective Hilbert space

> **Query Topic**: Hilbert space in quantum mechanics (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 65, Frequency: 11)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Projective_Hilbert_space

---

In mathematics and the foundations of quantum mechanics , the projective Hilbert space or ray space $\mathbf {P} (H)$ of a complex Hilbert space $H$ is the set of equivalence classes $[v]$ of non-zero vectors $v\in H$ , for the equivalence relation $\sim$ on $H$ given by

$w\sim v$ if and only if $v=\lambda w$ for some non-zero complex number $\lambda$ .

This is the usual construction of projectivization , applied to a complex Hilbert space. In quantum mechanics, the equivalence classes $[v]$ are also referred to as rays or projective rays . Each such projective ray is a copy of the nonzero complex numbers, which is topologically a two-dimensional plane after one point has been removed.

## Overview

The physical significance of the projective Hilbert space is that in quantum theory , the wave functions $\psi$ and $\lambda \psi$ represent the same physical state , for any $\lambda \neq 0$ . The Born rule demands that if the system is physical and measurable, its wave function has unit norm , $\langle \psi |\psi \rangle =1$ , in which case it is called a normalized wave function . The unit norm constraint does not completely determine $\psi$ within the ray, since $\psi$ could be multiplied by any $\lambda$ with absolute value 1 (the circle group $U(1)$ action) and retain its normalization. Such a $\lambda$ can be written as $\lambda =e^{i\phi }$ with $\phi$ called the global phase .

Rays that differ by such a $\lambda$ correspond to the same state (cf. quantum state (algebraic definition) , given a C*-algebra of observables and a representation on $H$ ). No measurement can recover the phase of a ray; it is not observable. One says that $U(1)$ is a gauge group of the first kind.

If $H$ is an irreducible representation of the algebra of observables then the rays induce pure states . Convex linear combinations of rays naturally give rise to density matrix which (still in case of an irreducible representation) correspond to mixed states.

In the case $H$ is finite-dimensional, i.e., $H=H_{n}$ , the Hilbert space reduces to a finite-dimensional inner product space and the set of projective rays may be treated as a complex projective space ; it is a homogeneous space for a unitary group $\mathrm {U} (n)$ . That is,

$\mathbf {P} (H_{n})=\mathbb {C} \mathbf {P} ^{n-1}$ ,

which carries a Kähler metric , called the Fubini–Study metric , derived from the Hilbert space's norm.

As such, the projectivization of, e.g., two-dimensional complex Hilbert space (the space describing one qubit ) is the complex projective line $\mathbb {C} \mathbf {P} ^{1}$ . This is known as the Bloch sphere or, equivalently, the Riemann sphere . See Hopf fibration for details of the projectivization construction in this case.

## Product

The Cartesian product of projective Hilbert spaces is not a projective space. The Segre mapping is an embedding of the Cartesian product of two projective spaces into the projective space associated to the tensor product of the two Hilbert spaces, given by $\mathbf {P} (H)\times \mathbf {P} (H')\to \mathbf {P} (H\otimes H'),([x],[y])\mapsto [x\otimes y]$ . In quantum theory, it describes how to make states of the composite system from states of its constituents. It is only an embedding , not a surjection; most of the tensor product space does not lie in its image and represents entangled states .
