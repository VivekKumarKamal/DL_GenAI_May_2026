# S-matrix

> **Query Topic**: relationship between the Wigner function and the density matrix operator (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 48, Frequency: 13)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/S-matrix

---

In physics , the S -matrix or scattering matrix is a matrix that relates the initial state and the final state of a physical system undergoing a scattering process . It is used in quantum mechanics , scattering theory and quantum field theory (QFT).

More formally, in the context of QFT, the S -matrix is defined as the unitary matrix connecting sets of asymptotically free particle states (the in-states and the out-states ) in the Hilbert space of physical states: a multi-particle state is said to be free (or non-interacting) if it transforms under Lorentz transformations as a tensor product , or direct product in physics parlance, of one-particle states as prescribed by equation (1) below. Asymptotically free then means that the state has this appearance in either the distant past or the distant future.

While the S -matrix may be defined for any background ( spacetime ) that is asymptotically solvable and has no event horizons , it has a simple form in the case of the Minkowski space . In this special case, the Hilbert space is a space of irreducible unitary representations of the inhomogeneous Lorentz group (the Poincaré group ); the S -matrix is the evolution operator between $t=-\infty$ (the distant past), and $t=+\infty$ (the distant future). It is defined only in the limit of zero energy density (or infinite particle separation distance).

It can be shown that if a quantum field theory in Minkowski space has a mass gap , the state in the asymptotic past and in the asymptotic future are both described by Fock spaces .

## History

The initial elements of S -matrix theory are found in Paul Dirac 's 1927 paper "Über die Quantenmechanik der Stoßvorgänge". The S -matrix was first properly introduced by John Archibald Wheeler in the 1937 paper "On the Mathematical Description of Light Nuclei by the Method of Resonating Group Structure". In this paper Wheeler introduced a scattering matrix – a unitary matrix of coefficients connecting "the asymptotic behaviour of an arbitrary particular solution [of the integral equations] with that of solutions of a standard form", but did not develop it fully.

In the 1940s, Werner Heisenberg independently developed and substantiated the idea of the S -matrix. Because of the problematic divergences present in quantum field theory at that time, Heisenberg was motivated to isolate the essential features of the theory that would not be affected by future changes as the theory developed. In doing so, he was led to introduce a unitary "characteristic" S -matrix.

Today, however, exact S -matrix results are important for conformal field theory , integrable systems , and several further areas of quantum field theory and string theory . S -matrices are not substitutes for a field-theoretic treatment, but rather, complement the end results of such.

## Motivation

In high-energy particle physics one is interested in computing the probability for different outcomes in scattering experiments. These experiments can be broken down into three stages:

- Making a collection of incoming particles collide (usually two kinds of particles with high energies).

- Allowing the incoming particles to interact. These interactions may change the types of particles present (e.g. if an electron and a positron annihilate they may produce two photons ).

- Measuring the resulting outgoing particles.

The process by which the incoming particles are transformed (through their interaction ) into the outgoing particles is called scattering . For particle physics, a physical theory of these processes must be able to compute the probability for different outgoing particles when different incoming particles collide with different energies.

The S -matrix in quantum field theory achieves exactly this. It is assumed that the small-energy-density approximation is valid in these cases.

## Use

The S -matrix is closely related to the transition probability amplitude in quantum mechanics and to cross sections of various interactions; the elements (individual numerical entries) in the S -matrix are known as scattering amplitudes . Poles of the S -matrix in the complex-energy plane are identified with bound states , virtual states or resonances . Branch cuts of the S -matrix in the complex-energy plane are associated to the opening of a scattering channel .

In the Hamiltonian approach to quantum field theory, the S -matrix may be calculated as a time-ordered exponential of the integrated Hamiltonian in the interaction picture ; it may also be expressed using Feynman's path integrals . In both cases, the perturbative calculation of the S -matrix leads to Feynman diagrams .

In scattering theory , the S -matrix is an operator mapping free particle in-states to free particle out-states ( scattering channels ) in the Heisenberg picture . This is very useful because often we cannot describe the interaction (at least, not the most interesting ones) exactly.

## In one-dimensional quantum mechanics

A simple prototype in which the S -matrix is 2-dimensional is considered first, for the purposes of illustration. In it, particles with sharp energy E scatter from a localized potential V according to the rules of 1-dimensional quantum mechanics. Already this simple model displays some features of more general cases, but is easier to handle.

Each energy E yields a matrix S = S ( E ) that depends on V . Thus, the total S -matrix could, figuratively speaking, be visualized, in a suitable basis, as a "continuous matrix" with every element zero except for 2 × 2 -blocks along the diagonal for a given V .

### Definition

Consider a localized one dimensional potential barrier V ( x ) , subjected to a beam of quantum particles with energy E . These particles are incident on the potential barrier from left to right.

The solutions of the Schrödinger equation outside the potential barrier are plane waves given by $\psi _{\rm {L}}(x)=Ae^{ikx}+Be^{-ikx}$ for the region to the left of the potential barrier, and $\psi _{\rm {R}}(x)=Ce^{ikx}+De^{-ikx}$ for the region to the right to the potential barrier, where $k={\sqrt {2mE/\hbar ^{2}}}$ is the wave vector . The time dependence is not needed in our overview and is hence omitted. The term with coefficient A represents the incoming wave, whereas term with coefficient C represents the outgoing wave. B stands for the reflecting wave. Since we set the incoming wave moving in the positive direction (coming from the left), D is zero and can be omitted.

The "scattering amplitude", i.e., the transition overlap of the outgoing waves with the incoming waves is a linear relation defining the S -matrix, ${\begin{pmatrix}B\\C\end{pmatrix}}={\begin{pmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{pmatrix}}{\begin{pmatrix}A\\D\end{pmatrix}}.$

The above relation can be written as $\Psi _{\rm {out}}=S\Psi _{\rm {in}}$ where $\Psi _{\rm {out}}={\begin{pmatrix}B\\C\end{pmatrix}},\quad \Psi _{\rm {in}}={\begin{pmatrix}A\\D\end{pmatrix}},\qquad S={\begin{pmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{pmatrix}}.$ The elements of S completely characterize the scattering properties of the potential barrier V ( x ) .

### Unitary property

The unitary property of the S -matrix is directly related to the conservation of the probability current in quantum mechanics .

The probability current density J of the wave function ψ ( x ) is defined as $J={\frac {\hbar }{2mi}}\left(\psi ^{*}{\frac {\partial \psi }{\partial x}}-\psi {\frac {\partial \psi ^{*}}{\partial x}}\right).$ The probability current density $J_{\rm {L}}(x)$ of $\psi _{\rm {L}}(x)$ to the left of the barrier is $J_{\rm {L}}(x)={\frac {\hbar k}{m}}\left(|A|^{2}-|B|^{2}\right),$ while the probability current density $J_{\rm {R}}(x)$ of $\psi _{\rm {R}}(x)$ to the right of the barrier is $J_{\rm {R}}(x)={\frac {\hbar k}{m}}\left(|C|^{2}-|D|^{2}\right).$ For conservation of the probability current, J L = J R . When combined with the relation $\Psi _{\text{out}}=S\Psi _{\text{in}}$ , this implies that the S -matrix is a unitary matrix . In the notation below, $\Psi _{\text{out}}^{\dagger }=(\,B^{*}\quad C^{*}\,)$ , and $\Psi _{\text{in}}^{\dagger }=(\,A^{*}\quad D^{*}\,)$ , so that $\Psi _{\text{out}}^{\dagger }\Psi _{\text{out}}^{\phantom {\dagger }}$ , represents the inner product of a vector with its dual co-vector, and $A^{*}$ , etc. is the complex conjugate of $A\in \mathbb {C}$ , etc., whose complex modulus is $\vert A\vert$ .

${\begin{aligned}&J_{\rm {L}}=J_{\rm {R}}\\&\vert A\vert ^{2}-\vert B\vert ^{2}=\vert C\vert ^{2}-\vert D\vert ^{2}\\&\vert B\vert ^{2}+\vert C\vert ^{2}=\vert A\vert ^{2}+\vert D\vert ^{2}\\&\Psi _{\text{out}}^{\dagger }\Psi _{\text{out}}=\Psi _{\text{in}}^{\dagger }\Psi _{\text{in}}\\&\Psi _{\text{in}}^{\dagger }S^{\dagger }S\Psi _{\text{in}}=\Psi _{\text{in}}^{\dagger }\Psi _{\text{in}}\\&\Longrightarrow S^{\dagger }S=I\\\end{aligned}}$

### Time-reversal symmetry

If the potential V ( x ) is real, then the system possesses time-reversal symmetry . Under this condition, if ψ ( x ) is a solution of the Schrödinger equation, then ψ *( x ) is also a solution.

The time-reversed solution is given by $\psi _{\rm {L}}^{*}(x)=A^{*}e^{-ikx}+B^{*}e^{ikx}$ for the region to the left to the potential barrier, and $\psi _{\rm {R}}^{*}(x)=C^{*}e^{-ikx}+D^{*}e^{ikx}$ for the region to the right to the potential barrier,
where the terms with coefficient B * , C * represent incoming wave, and terms with coefficient A * , D * represent outgoing wave.

They are again related by the S -matrix, ${\begin{pmatrix}A^{*}\\D^{*}\end{pmatrix}}={\begin{pmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{pmatrix}}{\begin{pmatrix}B^{*}\\C^{*}\end{pmatrix}}\,$ that is, $\Psi _{\rm {in}}^{*}=S\Psi _{\rm {out}}^{*}.$ Now, the relations $\Psi _{\rm {in}}^{*}=S\Psi _{\rm {out}}^{*},\quad \Psi _{\rm {out}}=S\Psi _{\rm {in}}$ together yield a condition $S^{*}S=I$ This condition, in conjunction with the unitarity relation, implies that the S -matrix is symmetric, as a result of time reversal symmetry, $S^{T}=S.$

By combining the symmetry and the unitarity, the S-matrix can be expressed in the form: ${\begin{pmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{pmatrix}}={\begin{pmatrix}e^{i\varphi }e^{i\delta }\cdot r&e^{i\varphi }{\sqrt {1-r^{2}}}\\e^{i\varphi }{\sqrt {1-r^{2}}}&-e^{i\varphi }e^{-i\delta }\cdot r\end{pmatrix}}=e^{i\varphi }{\begin{pmatrix}e^{i\delta }\cdot r&{\sqrt {1-r^{2}}}\\{\sqrt {1-r^{2}}}&-e^{-i\delta }\cdot r\end{pmatrix}}$ with $\delta ,\varphi \in [0;2\pi ]$ and $r\in [0;1]$ . So the S-matrix is determined by three real parameters.

#### Transfer matrix

The transfer matrix $M$ relates the plane waves $Ce^{ikx}$ and $De^{-ikx}$ on the right side of scattering potential to the plane waves $Ae^{ikx}$ and $Be^{-ikx}$ on the left side:

${\begin{pmatrix}C\\D\end{pmatrix}}={\begin{pmatrix}M_{11}&M_{12}\\M_{21}&M_{22}\end{pmatrix}}{\begin{pmatrix}A\\B\end{pmatrix}}$ and its components can be derived from the components of the S-matrix via: $M_{11}=1/S_{12}^{*}=1/S_{21}^{*}{,}\ M_{22}=M_{11}^{*}$ and $M_{12}=-S_{11}^{*}/S_{12}^{*}=S_{22}/S_{12}{,}\ M_{21}=M_{12}^{*}$ , whereby time-reversal symmetry is assumed.

In the case of time-reversal symmetry, the transfer matrix $\mathbf {M}$ can be expressed by three real parameters:

$M={\frac {1}{\sqrt {1-r^{2}}}}{\begin{pmatrix}e^{i\varphi }&-r\cdot e^{-i\delta }\\-r\cdot e^{i\delta }&e^{-i\varphi }\end{pmatrix}}$ with $\delta ,\varphi \in [0;2\pi ]$ and $r\in [0;1]$ (in case r = 1 there would be no connection between the left and the right side)

#### Finite square well

The one-dimensional, non-relativistic problem with time-reversal symmetry of a particle with mass m that approaches a (static) finite square well , has the potential function V with $V(x)={\begin{cases}-V_{0}&{\text{for}}~~|x|\leq a~~(V_{0}>0)\quad {\text{and}}\\[1ex]0&{\text{for}}~~|x|>a\end{cases}}$ The scattering can be solved by decomposing the wave packet of the free particle into plane waves $A_{k}\exp(ikx)$ with wave numbers $k>0$ for a plane wave coming (faraway) from the left side or likewise $D_{k}\exp(-ikx)$ (faraway) from the right side.

The S-matrix for the plane wave with wave number k has the solution: $S_{12}=S_{21}={\frac {\exp(-2ika)}{\cos(2la)-i\sin(2la){\frac {l^{2}+k^{2}}{2kl}}}}$ and $S_{11}=S_{12}\cdot i\sin(2la){\frac {l^{2}-k^{2}}{2kl}}$ ; hence $e^{i\delta }=\pm i$ and therefore $-e^{-i\delta }=e^{i\delta }$ and $S_{22}=S_{11}$ in this case.

Whereby $l={\sqrt {k^{2}+{\frac {2mV_{0}}{\hbar ^{2}}}}}$ is the (increased) wave number of the plane wave inside the square well, as the energy eigenvalue $E_{k}$ associated with the plane wave has to stay constant: $E_{k}={\frac {\hbar ^{2}k^{2}}{2m}}={\frac {\hbar ^{2}l^{2}}{2m}}-V_{0}$

The transmission is $T_{k}=|S_{21}|^{2}=|S_{12}|^{2}={\frac {1}{(\cos(2la))^{2}+(\sin(2la))^{2}{\frac {(l^{2}+k^{2})^{2}}{4k^{2}l^{2}}}}}={\frac {1}{1+(\sin(2la))^{2}{\frac {(l^{2}-k^{2})^{2}}{4k^{2}l^{2}}}}}$

In the case of $\sin(2la)=0$ then $\cos(2la)=\pm 1$ and therefore $S_{11}=S_{22}=0$ and $|S_{21}|=|S_{12}|=1$ i.e. a plane wave with wave number k passes the well without reflection if $k^{2}+{\frac {2mV_{0}}{\hbar ^{2}}}={\frac {n^{2}\pi ^{2}}{4a^{2}}}$ for a $n\in \mathbb {N}$

#### Finite square barrier

The square barrier is similar to the square well with the difference that $V(x)=+V_{0}>0$ for $|x|\leq a$ .

There are three different cases depending on the energy eigenvalue $E_{k}={\frac {\hbar ^{2}k^{2}}{2m}}$ of the plane waves (with wave numbers k resp. − k ) far away from the barrier:

- $E_{k}>V_{0}$ : In this case $l={\sqrt {k^{2}-{\frac {2mV_{0}}{\hbar ^{2}}}}}$ and the formulas for $S_{ij}$ have the same form as is in the square well case, and the transmission is $T_{k}=|S_{21}|^{2}=|S_{12}|^{2}={\frac {1}{1+(\sin(2la))^{2}{\frac {(l^{2}-k^{2})^{2}}{4k^{2}l^{2}}}}}$

- $E_{k}=V_{0}$ : In this case ${\sqrt {k^{2}-{\frac {2mV_{0}}{\hbar ^{2}}}}}=0$ and the wave function $\psi (x)$ has the property $\psi ''(x)=0$ inside the barrier and $S_{12}=S_{21}={\frac {\exp(-2ika)}{1-ika}}$ and $S_{11}=S_{22}={\frac {-ika\cdot \exp(-2ika)}{1-ika}}$ The transmission is: $T_{k}={\frac {1}{1+k^{2}a^{2}}}$ . This intermediate case is not singular, it's the limit ( $l\to 0$ resp. $\kappa \to 0$ ) from both sides.

$S_{12}=S_{21}={\frac {\exp(-2ika)}{1-ika}}$ and $S_{11}=S_{22}={\frac {-ika\cdot \exp(-2ika)}{1-ika}}$

- $E_{k}<V_{0}$ :In this case ${\sqrt {k^{2}-{\frac {2mV_{0}}{\hbar ^{2}}}}}$ is an imaginary number. So the wave function inside the barrier has the components $e^{\kappa x}$ and $e^{-\kappa x}$ with $\kappa ={\sqrt {{\frac {2mV_{0}}{\hbar ^{2}}}-k^{2}}}$ . The solution for the S-matrix is: $S_{12}=S_{21}={\frac {\exp(-2ika)}{\cosh(2\kappa a)-i\sinh(2\kappa a){\frac {k^{2}-{\kappa }^{2}}{2k\kappa }}}}$ and likewise: $S_{11}=-i{\frac {k^{2}+\kappa ^{2}}{2k\kappa }}\sinh(2\kappa a)\cdot S_{12}$ and also in this case $S_{22}=S_{11}$ . The transmission is $T_{k}=|S_{21}|^{2}=|S_{12}|^{2}={\frac {1}{1+(\sinh(2\kappa a))^{2}{\frac {(k^{2}+\kappa ^{2})^{2}}{4k^{2}\kappa ^{2}}}}}$ .

The solution for the S-matrix is: $S_{12}=S_{21}={\frac {\exp(-2ika)}{\cosh(2\kappa a)-i\sinh(2\kappa a){\frac {k^{2}-{\kappa }^{2}}{2k\kappa }}}}$

and likewise: $S_{11}=-i{\frac {k^{2}+\kappa ^{2}}{2k\kappa }}\sinh(2\kappa a)\cdot S_{12}$ and also in this case $S_{22}=S_{11}$ .

### Transmission coefficient and reflection coefficient

The transmission coefficient from the left of the potential barrier is, when D = 0 , $T_{\rm {L}}={\frac {|C|^{2}}{|A|^{2}}}=|S_{21}|^{2}.$

The reflection coefficient from the left of the potential barrier is, when D = 0 , $R_{\rm {L}}={\frac {|B|^{2}}{|A|^{2}}}=|S_{11}|^{2}.$

Similarly, the transmission coefficient from the right of the potential barrier is, when A = 0 , $T_{\rm {R}}={\frac {|B|^{2}}{|D|^{2}}}=|S_{12}|^{2}.$

The reflection coefficient from the right of the potential barrier is, when A = 0 , $R_{\rm {R}}={\frac {|C|^{2}}{|D|^{2}}}=|S_{22}|^{2}.$

The relations between the transmission and reflection coefficients are $T_{\rm {L}}+R_{\rm {L}}=1$ and $T_{\rm {R}}+R_{\rm {R}}=1.$ This identity is a consequence of the unitarity property of the S -matrix.

With time-reversal symmetry, the S-matrix is symmetric and hence $T_{\rm {L}}=|S_{21}|^{2}=|S_{12}|^{2}=T_{\rm {R}}$ and $R_{\rm {L}}=R_{\rm {R}}$ .

### Optical theorem in one dimension

In the case of free particles V ( x ) = 0 , the S -matrix is $S={\begin{pmatrix}0&1\\1&0\end{pmatrix}}.$ Whenever V ( x ) is different from zero, however, there is a departure of the S -matrix from the above form, to $S={\begin{pmatrix}2ir&1+2it\\1+2it&2ir^{*}{\frac {1+2it}{1-2it^{*}}}\end{pmatrix}}.$ This departure is parameterized by two complex functions of energy, r and t .
From unitarity there also follows a relationship between these two functions, $|r|^{2}+|t|^{2}=\operatorname {Im} (t).$

The analogue of this identity in three dimensions is known as the optical theorem .

## Definition in quantum field theory

### Interaction picture

A straightforward way to define the S -matrix begins with considering the interaction picture . Let the Hamiltonian H be split into the free part H 0 and the interaction V , H = H 0 + V . In this picture, the operators behave as free field operators and the state vectors have dynamics according to the interaction V . Let $\left|\Psi (t)\right\rangle$ denote a state that has evolved from a free initial state $\left|\Phi _{\rm {i}}\right\rangle .$ The S -matrix element is then defined as the projection of this state on the final state $\left\langle \Phi _{\rm {f}}\right|.$ Thus $S_{\rm {fi}}\equiv \lim _{t\rightarrow +\infty }\left\langle \Phi _{\rm {f}}|\Psi (t)\right\rangle \equiv \left\langle \Phi _{\rm {f}}\right|S\left|\Phi _{\rm {i}}\right\rangle ,$ where S is the S-operator . The great advantage of this definition is that the time-evolution operator U evolving a state in the interaction picture is formally known, $U(t,t_{0})=Te^{-i\int _{t_{0}}^{t}d\tau V(\tau )},$ where T denotes the time-ordered product . Expressed in this operator, $S_{\rm {fi}}=\lim _{t_{2}\rightarrow +\infty }\lim _{t_{1}\rightarrow -\infty }\left\langle \Phi _{\rm {f}}\right|U(t_{2},t_{1})\left|\Phi _{\rm {i}}\right\rangle ,$ from which $S=U(\infty ,-\infty ).$ Expanding using the knowledge about U gives a Dyson series , $S=\sum _{n=0}^{\infty }{\frac {(-i)^{n}}{n!}}\int _{-\infty }^{\infty }dt_{1}\cdots \int _{-\infty }^{\infty }dt_{n}T\left[V(t_{1})\cdots V(t_{n})\right],$ or, if V comes as a Hamiltonian density ${\mathcal {H}}$ , $S=\sum _{n=0}^{\infty }{\frac {(-i)^{n}}{n!}}\int _{-\infty }^{\infty }dx_{1}^{4}\cdots \int _{-\infty }^{\infty }dx_{n}^{4}T\left[{\mathcal {H}}(x_{1})\cdots {\mathcal {H}}(x_{n})\right].$

Being a special type of time-evolution operator, S is unitary. For any initial state and any final state one finds $S_{\rm {fi}}=\left\langle \Phi _{\rm {f}}|S|\Phi _{\rm {i}}\right\rangle =\left\langle \Phi _{\rm {f}}\left|\sum _{n=0}^{\infty }{\frac {(-i)^{n}}{n!}}\int _{-\infty }^{\infty }dx_{1}^{4}\cdots \int _{-\infty }^{\infty }dx_{n}^{4}T\left[{\mathcal {H}}(x_{1})\cdots {\mathcal {H}}(x_{n})\right]\right|\Phi _{\rm {i}}\right\rangle .$

This approach is somewhat naïve in that potential problems are swept under the carpet. This is intentional. The approach works in practice and some of the technical issues are addressed in the other sections.

### In and out states

Here a slightly more rigorous approach is taken in order to address potential problems that were disregarded in the interaction picture approach of above. The final outcome is, of course, the same as when taking the quicker route. For this, the notions of in and out states are needed. These will be developed in two ways, from vacuum, and from free particle states. Needless to say, the two approaches are equivalent, but they illuminate matters from different angles.

#### From vacuum

If a † ( k ) is a creation operator , its hermitian adjoint is an annihilation operator and destroys the vacuum, $a(k)\left|*,0\right\rangle =0.$

In Dirac notation , define $|*,0\rangle$ as a vacuum quantum state , i.e. a state without real particles. The asterisk signifies that not all vacua are necessarily equal, and certainly not equal to the Hilbert space zero state 0 . All vacuum states are assumed Poincaré invariant , invariance under translations, rotations and boosts, formally, $P^{\mu }|*,0\rangle =0,\quad M^{\mu \nu }|*,0\rangle =0$ where P μ is the generator of translation in space and time, and M μν is the generator of Lorentz transformations . Thus the description of the vacuum is independent of the frame of reference. Associated to the in and out states to be defined are the in and out field operators (aka fields ) Φ i and Φ o . Attention is here focused to the simplest case, that of a scalar theory in order to exemplify with the least possible cluttering of the notation. The in and out fields satisfy $(\Box ^{2}+m^{2})\phi _{\rm {i,o}}(x)=0,$ the free Klein–Gordon equation . These fields are postulated to have the same equal time commutation relations (ETCR) as the free fields, ${\begin{aligned}{[\phi _{\rm {i,o}}(x),\pi _{\rm {i,o}}(y)]}_{x_{0}=y_{0}}&=i\delta (\mathbf {x} -\mathbf {y} ),\\{[\phi _{\rm {i,o}}(x),\phi _{\rm {i,o}}(y)]}_{x_{0}=y_{0}}&={[\pi _{\rm {i,o}}(x),\pi _{\rm {i,o}}(y)]}_{x_{0}=y_{0}}=0,\end{aligned}}$ where π i , j is the field canonically conjugate to Φ i , j . Associated to the in and out fields are two sets of creation and annihilation operators, a † i ( k ) and a † f ( k ) , acting in the same Hilbert space , on two distinct complete sets ( Fock spaces ; initial space i , final space f ). These operators satisfy the usual commutation rules, ${\begin{aligned}{[a_{\rm {i,o}}(\mathbf {p} ),a_{\rm {i,o}}^{\dagger }(\mathbf {p} ')]}&=i\delta (\mathbf {p} -\mathbf {p'} ),\\{[a_{\rm {i,o}}(\mathbf {p} ),a_{\rm {i,o}}(\mathbf {p'} )]}&={[a_{\rm {i,o}}^{\dagger }(\mathbf {p} ),a_{\rm {i,o}}^{\dagger }(\mathbf {p'} )]}=0.\end{aligned}}$

The action of the creation operators on their respective vacua and states with a finite number of particles in the in and out states is given by ${\begin{aligned}\left|\mathrm {i} ,k_{1}\ldots k_{n}\right\rangle &=a_{i}^{\dagger }(k_{1})\cdots a_{\rm {i}}^{\dagger }(k_{n})\left|i,0\right\rangle ,\\\left|\mathrm {f} ,p_{1}\ldots p_{n}\right\rangle &=a_{\rm {f}}^{\dagger }(p_{1})\cdots a_{f}^{\dagger }(p_{n})\left|f,0\right\rangle ,\end{aligned}}$ where issues of normalization have been ignored. See the next section for a detailed account on how a general n -particle state is normalized. The initial and final spaces are defined by ${\mathcal {H}}_{\rm {i}}=\operatorname {span} \{\left|\mathrm {i} ,k_{1}\ldots k_{n}\right\rangle =a_{\rm {i}}^{\dagger }(k_{1})\cdots a_{\rm {i}}^{\dagger }(k_{n})\left|\mathrm {i} ,0\right\rangle \},$ ${\mathcal {H}}_{\rm {f}}=\operatorname {span} \{\left|\mathrm {f} ,p_{1}\ldots p_{n}\right\rangle =a_{\rm {f}}^{\dagger }(p_{1})\cdots a_{\rm {f}}^{\dagger }(p_{n})\left|\mathrm {f} ,0\right\rangle \}.$

The asymptotic states are assumed to have well defined Poincaré transformation properties, i.e. they are assumed to transform as a direct product of one-particle states. This is a characteristic of a non-interacting field. From this follows that the asymptotic states are all eigenstates of the momentum operator P μ , $P^{\mu }\left|\mathrm {i} ,k_{1}\ldots k_{m}\right\rangle =k_{1}^{\mu }+\cdots +k_{m}^{\mu }\left|\mathrm {i} ,k_{1}\ldots k_{m}\right\rangle ,\quad P^{\mu }\left|\mathrm {f} ,p_{1}\ldots p_{n}\right\rangle =p_{1}^{\mu }+\cdots +p_{n}^{\mu }\left|\mathrm {f} ,p_{1}\ldots p_{n}\right\rangle .$ In particular, they are eigenstates of the full Hamiltonian, $H=P^{0}.$

The vacuum is usually postulated to be stable and unique, $|\mathrm {i} ,0\rangle =|\mathrm {f} ,0\rangle =|*,0\rangle \equiv |0\rangle .$

The interaction is assumed adiabatically turned on and off.

#### Heisenberg picture

The Heisenberg picture is employed henceforth. In this picture, the states are time-independent. A Heisenberg state vector thus represents the complete spacetime history of a system of particles. The labeling of the in and out states refers to the asymptotic appearance. A state Ψ α , in is characterized by that as t → −∞ the particle content is that represented collectively by α . Likewise, a state Ψ β , out will have the particle content represented by β for t → +∞ . Using the assumption that the in and out states, as well as the interacting states, inhabit the same Hilbert space and assuming completeness of the normalized in and out states (postulate of asymptotic completeness ), the initial states can be expanded in a basis of final states (or vice versa). The explicit expression is given later after more notation and terminology has been introduced. The expansion coefficients are precisely the S -matrix elements to be defined below.

While the state vectors are constant in time in the Heisenberg picture, the physical states they represent are not . If a system is found to be in a state Ψ at time t = 0 , then it will be found in the state U ( τ )Ψ = e − iHτ Ψ at time t = τ . This is not (necessarily) the same Heisenberg state vector, but it is an equivalent state vector, meaning that it will, upon measurement, be found to be one of the final states from the expansion with nonzero coefficient. Letting τ vary one sees that the observed Ψ (not measured) is indeed the Schrödinger picture state vector. By repeating the measurement sufficiently many times and averaging, one may say that the same state vector is indeed found at time t = τ as at time t = 0 . This reflects the expansion above of an in state into out states.

#### From free particle states

For this viewpoint, one should consider how the archetypical scattering experiment is performed. The initial particles are prepared in well defined states where they are so far apart that they don't interact. They are somehow made to interact, and the final particles are registered when they are so far apart that they have ceased to interact. The idea is to look for states in the Heisenberg picture that in the distant past had the appearance of free particle states. This will be the in states. Likewise, an out state will be a state that in the distant future has the appearance of a free particle state.

The notation from the general reference for this section, Weinberg (2002) will be used. A general non-interacting multi-particle state is given by $\Psi _{p_{1}\sigma _{1}n_{1};p_{2}\sigma _{2}n_{2};\cdots },$ where

- p is momentum,

- σ is spin z-component or, in the massless case, helicity ,

- n is particle species.

These states are normalized as $\left(\Psi _{p_{1}'\sigma _{1}'n_{1}';p_{2}'\sigma _{2}'n_{2}';\cdots },\Psi _{p_{1}\sigma _{1}n_{1};p_{2}\sigma _{2}n_{2};\cdots }\right)=\delta ^{3}(\mathbf {p} _{1}'-\mathbf {p} _{1})\delta _{\sigma _{1}'\sigma _{1}}\delta _{n_{1}'n_{1}}\delta ^{3}(\mathbf {p} _{2}'-\mathbf {p} _{2})\delta _{\sigma _{2}'\sigma _{2}}\delta _{n_{2}'n_{2}}\cdots \quad \pm {\text{ permutations}}.$ Permutations work as such; if s ∈ S k is a permutation of k objects (for a k -particle state) such that $n_{s(i)}'=n_{i},\quad 1\leq i\leq k,$ then a nonzero term results. The sign is plus unless s involves an odd number of fermion transpositions, in which case it is minus. The notation is usually abbreviated letting one Greek letter stand for the whole collection describing the state. In abbreviated form the normalization becomes $\left(\Psi _{\alpha '},\Psi _{\alpha }\right)=\delta (\alpha '-\alpha ).$ When integrating over free-particle states one writes in this notation $d\alpha \cdots \equiv \sum _{n_{1}\sigma _{1}n_{2}\sigma _{2}\cdots }\int d^{3}p_{1}d^{3}p_{2}\cdots ,$ where the sum includes only terms such that no two terms are equal modulo a permutation of the particle type indices. The sets of states sought for are supposed to be complete . This is expressed as $\Psi =\int d\alpha \ \Psi _{\alpha }\left(\Psi _{\alpha },\Psi \right),$ which could be paraphrased as $\int d\alpha \ \left|\Psi _{\alpha }\right\rangle \left\langle \Psi _{\alpha }\right|=1,$ where for each fixed α , the right hand side is a projection operator onto the state α . Under an inhomogeneous Lorentz transformation (Λ, a ) , the field transforms according to the rule,

where W (Λ, p ) is the Wigner rotation and D ( j ) is the (2 j + 1) -dimensional representation of SO(3) . By putting Λ = 1, a = ( τ , 0, 0, 0) , for which U is exp( iHτ ) , in (1) , it immediately follows that $H\Psi =E_{\alpha }\Psi ,\quad E_{\alpha }=p_{1}^{0}+p_{2}^{0}+\cdots ,$ so the in and out states sought after are eigenstates of the full Hamiltonian that are necessarily non-interacting due to the absence of mixed particle energy terms. The discussion in the section above suggests that the in states Ψ + and the out states Ψ − should be such that $e^{-iH\tau }\int d\alpha g(\alpha )\Psi _{\alpha }^{\pm }=\int d\alpha e^{-iE_{\alpha }\tau }g(\alpha )\Psi _{\alpha }^{\pm }$ for large positive and negative τ has the appearance of the corresponding package, represented by g , of free-particle states, g assumed smooth and suitably localized in momentum. Wave packages are necessary, else the time evolution will yield only a phase factor indicating free particles, which cannot be the case. The right hand side follows from that the in and out states are eigenstates of the Hamiltonian per above. To formalize this requirement, assume that the full Hamiltonian H can be divided into two terms, a free-particle Hamiltonian H 0 and an interaction V , H = H 0 + V such that the eigenstates Φ γ of H 0 have the same appearance as the in- and out-states with respect to normalization and Lorentz transformation properties, $H_{0}\Phi _{\alpha }=E_{\alpha }\Phi _{\alpha },$ $(\Phi _{\alpha }',\Phi _{\alpha })=\delta (\alpha '-\alpha ).$

The in and out states are defined as eigenstates of the full Hamiltonian, $H\Psi _{\alpha }^{\pm }=E_{\alpha }\Psi _{\alpha }^{\pm },$ satisfying $e^{-iH\tau }\int d\alpha \ g(\alpha )\Psi _{\alpha }^{\pm }\rightarrow e^{-iH_{0}\tau }\int d\alpha \ g(\alpha )\Phi _{\alpha }.$ for τ → −∞ or τ → +∞ respectively. Define $\Omega (\tau )\equiv e^{+iH\tau }e^{-iH_{0}\tau },$ then $\Psi _{\alpha }^{\pm }=\Omega (\mp \infty )\Phi _{\alpha }.$ This last expression will work only using wave packages.From these definitions follow that the in and out states are normalized in the same way as the free-particle states, $(\Psi _{\beta }^{+},\Psi _{\alpha }^{+})=(\Phi _{\beta },\Phi _{\alpha })=(\Psi _{\beta }^{-},\Psi _{\alpha }^{-})=\delta (\beta -\alpha ),$ and the three sets are unitarily equivalent. Now rewrite the eigenvalue equation, $(E_{\alpha }-H_{0}\pm i\epsilon )\Psi _{\alpha }^{\pm }=\pm i\epsilon \Psi _{\alpha }^{\pm }+V\Psi _{\alpha }^{\pm },$ where the ± iε terms has been added to make the operator on the LHS invertible. Since the in and out states reduce to the free-particle states for V → 0 , put $i\epsilon \Psi _{\alpha }^{\pm }=i\epsilon \Phi _{\alpha }$ on the RHS to obtain $\Psi _{\alpha }^{\pm }=\Phi _{\alpha }+(E_{\alpha }-H_{0}\pm i\epsilon )^{-1}V\Psi _{\alpha }^{\pm }.$ Then use the completeness of the free-particle states, $V\Psi _{\alpha }^{\pm }=\int d\beta \ (\Phi _{\beta },V\Psi _{\alpha }^{\pm })\Phi _{\beta }\equiv \int d\beta \ T_{\beta \alpha }^{\pm }\Phi _{\beta },$ to finally obtain $\Psi _{\alpha }^{\pm }=\Phi _{\alpha }+\int d\beta \ {\frac {T_{\beta \alpha }^{\pm }\Phi _{\beta }}{E_{\alpha }-E_{\beta }\pm i\epsilon }}.$ Here H 0 has been replaced by its eigenvalue on the free-particle states. This is the Lippmann–Schwinger equation .

#### In states expressed as out states

The initial states can be expanded in a basis of final states (or vice versa). Using the completeness relation, $\Psi _{\alpha }^{-}=\int d\beta (\Psi _{\beta }^{+},\Psi _{\alpha }^{-})\Psi _{\beta }^{+}=\int d\beta |\Psi _{\beta }^{+}\rangle \langle \Psi _{\beta }^{+}|\Psi _{\alpha }^{-}\rangle =\sum _{n_{1}\sigma _{1}n_{2}\sigma _{2}\cdots }\int d^{3}p_{1}d^{3}p_{2}\cdots (\Psi _{\beta }^{+},\Psi _{\alpha }^{-})\Psi _{\beta }^{+},$ $\Psi _{\alpha }^{-}=\left|\mathrm {i} ,k_{1}\ldots k_{n}\right\rangle =C_{0}\left|\mathrm {f} ,0\right\rangle \ +\sum _{m=1}^{\infty }\int {d^{4}p_{1}\ldots d^{4}p_{m}C_{m}(p_{1}\ldots p_{m})\left|\mathrm {f} ,p_{1}\ldots p_{m}\right\rangle }~,$ where | C m | 2 is the probability that the interaction transforms $\left|\mathrm {i} ,k_{1}\ldots k_{n}\right\rangle =\Psi _{\alpha }^{-}$ into $\left|\mathrm {f} ,p_{1}\ldots p_{m}\right\rangle =\Psi _{\beta }^{+}.$ By the ordinary rules of quantum mechanics, $C_{m}(p_{1}\ldots p_{m})=\left\langle \mathrm {f} ,p_{1}\ldots p_{m}\right|\mathrm {i} ,k_{1}\ldots k_{n}\rangle =(\Psi _{\beta }^{+},\Psi _{\alpha }^{-})$ and one may write $\left|\mathrm {i} ,k_{1}\ldots k_{n}\right\rangle =C_{0}\left|\mathrm {f} ,0\right\rangle \ +\sum _{m=1}^{\infty }\int {d^{4}p_{1}\ldots d^{4}p_{m}\left|\mathrm {f} ,p_{1}\ldots p_{m}\right\rangle }\left\langle \mathrm {f} ,p_{1}\ldots p_{m}\right|\mathrm {i} ,k_{1}\ldots k_{n}\rangle ~.$ The expansion coefficients are precisely the S -matrix elements to be defined below.

### S -matrix

The S -matrix is now defined by $S_{\beta \alpha }=\langle \Psi _{\beta }^{-}|\Psi _{\alpha }^{+}\rangle =\langle \mathrm {f} ,\beta |\mathrm {i} ,\alpha \rangle ,\qquad |\mathrm {f} ,\beta \rangle \in {\mathcal {H}}_{\rm {f}},\quad |\mathrm {i} ,\alpha \rangle \in {\mathcal {H}}_{\rm {i}}.$

Here α and β are shorthands that represent the particle content but suppresses the individual labels. Associated to the S -matrix there is the S-operator S defined by $\langle \Phi _{\beta }|S|\Phi _{\alpha }\rangle \equiv S_{\beta \alpha },$ where the Φ γ are free particle states. This definition conforms with the direct approach used in the interaction picture. Also, due to unitary equivalence, $\langle \Psi _{\beta }^{+}|S|\Psi _{\alpha }^{+}\rangle =S_{\beta \alpha }=\langle \Psi _{\beta }^{-}|S|\Psi _{\alpha }^{-}\rangle .$

As a physical requirement, S must be a unitary operator . This is a statement of conservation of probability in quantum field theory. But $\langle \Psi _{\beta }^{-}|S|\Psi _{\alpha }^{-}\rangle =S_{\beta \alpha }=\langle \Psi _{\beta }^{-}|\Psi _{\alpha }^{+}\rangle .$ By completeness then, $S|\Psi _{\alpha }^{-}\rangle =|\Psi _{\alpha }^{+}\rangle ,$ so S is the unitary transformation from in-states to out states.
Lorentz invariance is another crucial requirement on the S -matrix. The S-operator represents the quantum canonical transformation of the initial in states to the final out states. Moreover, S leaves the vacuum state invariant and transforms in -space fields to out -space fields, $S\left|0\right\rangle =\left|0\right\rangle$ $\phi _{\mathrm {f} }=S\phi _{\mathrm {i} }S^{-1}~.$

In terms of creation and annihilation operators, this becomes $a_{\rm {f}}(p)=Sa_{\rm {i}}(p)S^{-1},a_{\rm {f}}^{\dagger }(p)=Sa_{\rm {i}}^{\dagger }(p)S^{-1},$ hence ${\begin{aligned}S|\mathrm {i} ,k_{1},k_{2},\ldots ,k_{n}\rangle &=Sa_{\rm {i}}^{\dagger }(k_{1})a_{\rm {i}}^{\dagger }(k_{2})\cdots a_{\rm {i}}^{\dagger }(k_{n})|0\rangle =Sa_{\rm {i}}^{\dagger }(k_{1})S^{-1}Sa_{\rm {i}}^{\dagger }(k_{2})S^{-1}\cdots Sa_{\rm {i}}^{\dagger }(k_{n})S^{-1}S|0\rangle \\[1ex]&=a_{\rm {o}}^{\dagger }(k_{1})a_{\rm {o}}^{\dagger }(k_{2})\cdots a_{\rm {o}}^{\dagger }(k_{n})S|0\rangle =a_{\rm {o}}^{\dagger }(k_{1})a_{\rm {o}}^{\dagger }(k_{2})\cdots a_{\rm {o}}^{\dagger }(k_{n})|0\rangle =|\mathrm {o} ,k_{1},k_{2},\ldots ,k_{n}\rangle .\end{aligned}}$ A similar expression holds when S operates to the left on an out state. This means that the S -matrix can be expressed as $S_{\beta \alpha }=\langle \mathrm {o} ,\beta |\mathrm {i} ,\alpha \rangle =\langle \mathrm {i} ,\beta |S|\mathrm {i} ,\alpha \rangle =\langle \mathrm {o} ,\beta |S|\mathrm {o} ,\alpha \rangle .$

If S describes an interaction correctly, these properties must be also true:

- If the system is made up with a single particle in momentum eigenstate | k ⟩ , then S | k ⟩ = | k ⟩ . This follows from the calculation above as a special case.

- The S -matrix element may be nonzero only where the output state has the same total momentum as the input state. This follows from the required Lorentz invariance of the S -matrix.

## Evolution operator U

Define a time-dependent creation and annihilation operator as follows, ${\begin{aligned}a^{\dagger }{\left(k,t\right)}&=U^{-1}(t)\,a_{\rm {i}}^{\dagger }{\left(k\right)}\,U{\left(t\right)}\\[1ex]a{\left(k,t\right)}&=U^{-1}(t)\,a_{\rm {i}}{\left(k\right)}\,U{\left(t\right)}\,,\end{aligned}}$ so, for the fields, $\phi _{\rm {f}}=U^{-1}(\infty )\phi _{\rm {i}}U(\infty )=S^{-1}\phi _{\rm {i}}S~,$ where $S=e^{i\alpha }\,U(\infty ).$

We allow for a phase difference, given by $e^{i\alpha }=\left\langle 0|U(\infty )|0\right\rangle ^{-1}~,$ because for S , $S\left|0\right\rangle =\left|0\right\rangle \Longrightarrow \left\langle 0|S|0\right\rangle =\left\langle 0|0\right\rangle =1~.$

Substituting the explicit expression for U , one has $S={\frac {1}{\left\langle 0|U(\infty )|0\right\rangle }}{\mathcal {T}}e^{-i\int {d\tau H_{\rm {int}}(\tau )}}~,$ where $H_{\rm {int}}$ is the interaction part of the Hamiltonian and ${\mathcal {T}}$ is the time ordering.

By inspection, it can be seen that this formula is not explicitly covariant.

## Dyson series

The most widely used expression for the S -matrix is the Dyson series. This expresses the S -matrix operator as the series : $S=\sum _{n=0}^{\infty }{\frac {(-i)^{n}}{n!}}\int \cdots \int d^{4}x_{1}d^{4}x_{2}\ldots d^{4}x_{n}T[{\mathcal {H}}_{\rm {int}}(x_{1}){\mathcal {H}}_{\rm {int}}(x_{2})\cdots {\mathcal {H}}_{\rm {int}}(x_{n})]$ where:

- $T[\cdots ]$ denotes time-ordering ,

- $\;{\mathcal {H}}_{\rm {int}}(x)$ denotes the interaction Hamiltonian density which describes the interactions in the theory.

## The not- S -matrix

Since the transformation of particles from black hole to Hawking radiation could not be described with an S -matrix, Stephen Hawking proposed a "not- S -matrix", for which he used the dollar sign ($), and which therefore was also called "dollar matrix".
