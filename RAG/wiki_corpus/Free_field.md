# Free field

> **Query Topic**: Peierls bracket in canonical quantization (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 141, Frequency: 16)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Free_field

---

In physics a free field is a field without interactions , which is described by the terms of motion and mass.

## Description

In classical physics , a free field is a field whose equations of motion are given by linear partial differential equations . Such linear PDE's have a unique solution for a given initial condition.

In quantum field theory , an operator valued distribution is a free field if it satisfies some linear partial differential equations such that the corresponding case of the same linear PDEs for a classical field (i.e. not an operator) would be the Euler–Lagrange equation for some quadratic Lagrangian . They are used to describe the non-interacting behavior of fields. We can differentiate distributions by defining their derivatives via differentiated test functions . See Schwartz distribution for more details. Since we are dealing not with ordinary distributions but operator valued distributions, it is understood these PDEs aren't constraints on states but instead a description of the relations among the smeared fields. Beside the PDEs, the operators also satisfy another relation, the commutation/anticommutation relations.

## Canonical commutation relation

Basically, commutator (for bosons )/ anticommutator (for fermions ) of two smeared fields is i times the Peierls bracket of the field with itself (which is really a distribution, not a function) for the PDEs smeared over both test functions. This has the form of a CCR/CAR algebra .

CCR/CAR algebras with infinitely many degrees of freedom have many inequivalent irreducible unitary representations. If the theory is defined over Minkowski space , we may choose the unitary irrep containing a vacuum state although that isn't always necessary.

## Example

### Equations

The following are equations of motion for different spin fields and particles.

#### Klein-Gordon Equation

Let ${\textstyle \phi }$ be a spin 0 field / particle. Then the equation of motion that describes its free motion is the Klein-Gordon equation. It is given by

$\partial ^{\mu }\partial _{\mu }\phi +m^{2}\phi =0$

#### Dirac Equation

The Dirac equation describes the free motion of a spin ${\textstyle {\frac {1}{2}}}$ field / particle. It is given by

$(i\gamma _{\mu }\partial ^{\mu }-m)\Psi =0$

#### Proca Equations

The Proca equations are a set of equations of motion that describe the free of motion of spin 1 fields / particles. They are given by $m^{2}A^{\rho }={\frac {1}{2}}\partial _{\sigma }(\partial ^{\sigma }A^{\rho }-\partial ^{\rho }A^{\sigma })$

or

$0={\frac {1}{2}}\partial _{\sigma }(\partial ^{\sigma }A^{\rho }-\partial ^{\rho }A^{\sigma })$

depending if the spin 1 field / particle, ${\textstyle A^{\mu }}$ , is massless or not.

### Operators on Free Fields

Let φ be an operator valued distribution and the (Klein–Gordon) PDE be

$\partial ^{\mu }\partial _{\mu }\phi +m^{2}\phi =0$ .

This is a bosonic field. Let's call the distribution given by the Peierls bracket Δ.

Then,

$\{\phi (x),\phi (y)\}=\Delta (x;y)$

where here, φ is a classical field and {,} is the Peierls bracket.

Then, the canonical commutation relation is

$[\phi [f],\phi [g]]=i\Delta [f,g]\,$ .

Note that Δ is a distribution over two arguments, and so, can be smeared as well.

Equivalently, we could have insisted that

${\mathcal {T}}\{[((\partial ^{\mu }\partial _{\mu }+m^{2})\phi )[f],\phi [g]]\}=-i\int d^{d}xf(x)g(x)$

where ${\mathcal {T}}$ is the time ordering operator and that if the supports of f and g are spacelike separated,

$[\phi [f],\phi [g]]=0$ .
