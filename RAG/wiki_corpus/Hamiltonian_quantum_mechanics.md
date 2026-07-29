# Hamiltonian (quantum mechanics)

> **Query Topic**: Hamiltonian H (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 48, Frequency: 13)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Hamiltonian_(quantum_mechanics)

---

In quantum mechanics , the Hamiltonian of a system is an operator corresponding to the total energy of that system, including both kinetic energy and potential energy . Its spectrum , the system's energy spectrum or its set of energy eigenvalues , is the set of possible outcomes obtainable from a measurement of the system's total energy. Due to its close relation to the energy spectrum and time-evolution of a system, it is of fundamental importance in most formulations of quantum theory .

The Hamiltonian is named after William Rowan Hamilton , who developed a revolutionary reformulation of Newtonian mechanics , known as Hamiltonian mechanics , which was historically important to the development of quantum physics. Similar to vector notation , it is typically denoted by ${\hat {H}}$ , where the hat indicates that it is an operator. It can also be written as $H$ or ${\check {H}}$ .

## Introduction

The Hamiltonian of a system represents the total energy of the system; that is, the sum of the kinetic and potential energies of all particles associated with the system. The Hamiltonian takes different forms and can be simplified in some cases by taking into account the concrete characteristics of the system under analysis, such as single or several particles in the system, interaction between particles, kind of potential energy, time varying potential or time independent one.

## Schrödinger Hamiltonian

### One particle

By analogy with classical mechanics , the Hamiltonian is commonly expressed as the sum of operators corresponding to the kinetic and potential energies of a system in the form ${\hat {H}}={\hat {T}}+{\hat {V}},$ where ${\hat {V}}=V=V(\mathbf {r} ,t),$ is the potential energy operator and ${\hat {T}}={\frac {\mathbf {\hat {p}} \cdot \mathbf {\hat {p}} }{2m}}={\frac {{\hat {p}}^{2}}{2m}}=-{\frac {\hbar ^{2}}{2m}}\nabla ^{2},$ is the kinetic energy operator in which $m$ is the mass of the particle, the dot denotes the dot product of vectors, and ${\hat {p}}=-i\hbar \nabla ,$ is the momentum operator where a $\nabla$ is the del operator . The dot product of $\nabla$ with itself is the Laplacian $\nabla ^{2}$ . In three dimensions using Cartesian coordinates the Laplace operator is $\nabla ^{2}={\frac {\partial ^{2}}{{\partial x}^{2}}}+{\frac {\partial ^{2}}{{\partial y}^{2}}}+{\frac {\partial ^{2}}{{\partial z}^{2}}}$

Although this is not the technical definition of the Hamiltonian in classical mechanics , it is the form it most commonly takes. Combining these yields the form used in the Schrödinger equation : ${\begin{aligned}{\hat {H}}&={\hat {T}}+{\hat {V}}\\[6pt]&={\frac {\mathbf {\hat {p}} \cdot \mathbf {\hat {p}} }{2m}}+V(\mathbf {r} ,t)\\[6pt]&=-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}+V(\mathbf {r} ,t)\end{aligned}}$ which allows one to apply the Hamiltonian to systems described by a wave function $\Psi (\mathbf {r} ,t)$ . This is the approach commonly taken in introductory treatments of quantum mechanics, using the formalism of Schrödinger's wave mechanics.

One can also make substitutions to certain variables to fit specific cases, such as some involving electromagnetic fields.

#### Expectation value

It can be shown that the expectation value of the Hamiltonian which gives the energy expectation value will always be greater than or equal to the minimum potential of the system.

Consider computing the expectation value of kinetic energy: ${\begin{aligned}T&=-{\frac {\hbar ^{2}}{2m}}\int _{-\infty }^{+\infty }\psi ^{*}{\frac {d^{2}\psi }{dx^{2}}}\,dx\\[1ex]&=-{\frac {\hbar ^{2}}{2m}}\left({\left[\psi '(x)\psi ^{*}(x)\right]}_{-\infty }^{+\infty }-\int _{-\infty }^{+\infty }{\frac {d\psi }{dx}}{\frac {d\psi ^{*}}{dx}}\,dx\right)\\[1ex]&={\frac {\hbar ^{2}}{2m}}\int _{-\infty }^{+\infty }\left|{\frac {d\psi }{dx}}\right|^{2}\,dx\geq 0\end{aligned}}$

Hence the expectation value of kinetic energy is always non-negative. This result can be used to calculate the expectation value of the total energy which is given for a normalized wavefunction as: $E=T+\langle V(x)\rangle =T+\int _{-\infty }^{+\infty }V(x)|\psi (x)|^{2}\,dx\geq V_{\text{min}}(x)\int _{-\infty }^{+\infty }|\psi (x)|^{2}\,dx\geq V_{\text{min}}(x)$ which complete the proof. Similarly, the condition can be generalized to any higher dimensions using the divergence theorem .

### Many particles

The formalism can be extended to $N$ particles: ${\hat {H}}=\sum _{n=1}^{N}{\hat {T}}_{n}+{\hat {V}}$ where ${\hat {V}}=V(\mathbf {r} _{1},\mathbf {r} _{2},\ldots ,\mathbf {r} _{N},t),$ is the potential energy function, now a function of the spatial configuration of the system and time (a particular set of spatial positions at some instant of time defines a configuration) and ${\hat {T}}_{n}={\frac {\mathbf {\hat {p}} _{n}\cdot \mathbf {\hat {p}} _{n}}{2m_{n}}}=-{\frac {\hbar ^{2}}{2m_{n}}}\nabla _{n}^{2}$ is the kinetic energy operator of particle $n$ , $\nabla _{n}$ is the gradient for particle $n$ , and $\nabla _{n}^{2}$ is the Laplacian for particle n : $\nabla _{n}^{2}={\frac {\partial ^{2}}{\partial x_{n}^{2}}}+{\frac {\partial ^{2}}{\partial y_{n}^{2}}}+{\frac {\partial ^{2}}{\partial z_{n}^{2}}},$

Combining these yields the Schrödinger Hamiltonian for the $N$ -particle case: ${\begin{aligned}{\hat {H}}&=\sum _{n=1}^{N}{\hat {T}}_{n}+{\hat {V}}\\[6pt]&=\sum _{n=1}^{N}{\frac {\mathbf {\hat {p}} _{n}\cdot \mathbf {\hat {p}} _{n}}{2m_{n}}}+V(\mathbf {r} _{1},\mathbf {r} _{2},\ldots ,\mathbf {r} _{N},t)\\[6pt]&=-{\frac {\hbar ^{2}}{2}}\sum _{n=1}^{N}{\frac {1}{m_{n}}}\nabla _{n}^{2}+V(\mathbf {r} _{1},\mathbf {r} _{2},\ldots ,\mathbf {r} _{N},t)\end{aligned}}$

However, complications can arise in the many-body problem . Since the potential energy depends on the spatial arrangement of the particles, the kinetic energy will also depend on the spatial configuration to conserve energy. The motion due to any one particle will vary due to the motion of all the other particles in the system. For this reason cross terms for kinetic energy may appear in the Hamiltonian; a mix of the gradients for two particles: $-{\frac {\hbar ^{2}}{2M}}\nabla _{i}\cdot \nabla _{j}$ where $M$ denotes the mass of the collection of particles resulting in this extra kinetic energy. Terms of this form are known as mass polarization terms , and appear in the Hamiltonian of many-electron atoms (see below).

For $N$ interacting particles, i.e. particles which interact mutually and constitute a many-body situation, the potential energy function $V$ is not simply a sum of the separate potentials (and certainly not a product, as this is dimensionally incorrect). The potential energy function can only be written as above: a function of all the spatial positions of each particle.

For non-interacting particles, i.e. particles which do not interact mutually and move independently, the potential of the system is the sum of the separate potential energy for each particle, that is $V=\sum _{i=1}^{N}V(\mathbf {r} _{i},t)=V(\mathbf {r} _{1},t)+V(\mathbf {r} _{2},t)+\cdots +V(\mathbf {r} _{N},t)$

The general form of the Hamiltonian in this case is: ${\begin{aligned}{\hat {H}}&=-{\frac {\hbar ^{2}}{2}}\sum _{i=1}^{N}{\frac {1}{m_{i}}}\nabla _{i}^{2}+\sum _{i=1}^{N}V_{i}\\[6pt]&=\sum _{i=1}^{N}\left(-{\frac {\hbar ^{2}}{2m_{i}}}\nabla _{i}^{2}+V_{i}\right)\\[6pt]&=\sum _{i=1}^{N}{\hat {H}}_{i}\end{aligned}}$ where the sum is taken over all particles and their corresponding potentials; the result is that the Hamiltonian of the system is the sum of the separate Hamiltonians for each particle. This is an idealized situation—in practice the particles are almost always influenced by some potential, and there are many-body interactions. One illustrative example of a two-body interaction where this form would not apply is for electrostatic potentials due to charged particles, because they interact with each other by Coulomb interaction (electrostatic force), as shown below.

## Schrödinger equation

The Hamiltonian generates the time evolution of quantum states. If $\left|\psi (t)\right\rangle$ is the state of the system at time $t$ , then $H\left|\psi (t)\right\rangle =i\hbar {d \over \ dt}\left|\psi (t)\right\rangle .$

This equation is the Schrödinger equation . It takes the same form as the Hamilton–Jacobi equation , which is one of the reasons $H$ is also called the Hamiltonian. Given the state at some initial time ( $t=0$ ), we can solve it to obtain the state at any subsequent time. In particular, if $H$ is independent of time, then $\left|\psi (t)\right\rangle =e^{-iHt/\hbar }\left|\psi (0)\right\rangle .$

The exponential operator on the right hand side of the Schrödinger equation is usually defined by the corresponding power series in $H$ . One might notice that taking polynomials or power series of unbounded operators that are not defined everywhere may not make mathematical sense. Rigorously, to take functions of unbounded operators, a functional calculus is required. In the case of the exponential function, the continuous , or just the holomorphic functional calculus suffices. We note again, however, that for common calculations the physicists' formulation is quite sufficient.

By the *- homomorphism property of the functional calculus, the operator $U=e^{-iHt/\hbar }$ is a unitary operator . It is the time evolution operator or propagator of a closed quantum system. If the Hamiltonian is time-independent, $\{U(t)\}$ form a one parameter unitary group (more than a semigroup ); this gives rise to the physical principle of detailed balance .

## Dirac formalism

However, in the more general formalism of Dirac , the Hamiltonian is typically implemented as an operator on a Hilbert space in the following way:

The eigenkets of $H$ , denoted $\left|a\right\rangle$ , provide an orthonormal basis for the Hilbert space. The spectrum of allowed energy levels of the system is given by the set of eigenvalues, denoted $\{E_{a}\}$ , solving the equation: $H\left|a\right\rangle =E_{a}\left|a\right\rangle .$

Since $H$ is a Hermitian operator , the energy is always a real number .

From a mathematically rigorous point of view, care must be taken with the above assumptions. Operators on infinite-dimensional Hilbert spaces need not have eigenvalues (the set of eigenvalues does not necessarily coincide with the spectrum of an operator ). However, all routine quantum mechanical calculations can be done using the physical formulation. [ clarification needed ]

## Expressions for the Hamiltonian

Following are expressions for the Hamiltonian in a number of situations. Typical ways to classify the expressions are the number of particles, number of dimensions, and the nature of the potential energy function—importantly space and time dependence. Masses are denoted by $m$ , and charges by $q$ .

### Free particle

The particle is not bound by any potential energy, so the potential is zero and this Hamiltonian is the simplest. For one dimension: ${\hat {H}}=-{\frac {\hbar ^{2}}{2m}}{\frac {\partial ^{2}}{\partial x^{2}}}$ and in higher dimensions: ${\hat {H}}=-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}$

### Constant-potential well

For a particle in a region of constant potential $V=V_{0}$ (no dependence on space or time), in one dimension, the Hamiltonian is: ${\hat {H}}=-{\frac {\hbar ^{2}}{2m}}{\frac {\partial ^{2}}{\partial x^{2}}}+V_{0}$ in three dimensions ${\hat {H}}=-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}+V_{0}$

This applies to the elementary " particle in a box " problem, and step potentials .

### Simple harmonic oscillator

For a simple harmonic oscillator in one dimension, the potential varies with position (but not time), according to: $V={\frac {k}{2}}x^{2}={\frac {m\omega ^{2}}{2}}x^{2}$ where the angular frequency $\omega$ , effective spring constant $k$ , and mass $m$ of the oscillator satisfy: $\omega ^{2}={\frac {k}{m}}$ so the Hamiltonian is: ${\hat {H}}=-{\frac {\hbar ^{2}}{2m}}{\frac {\partial ^{2}}{\partial x^{2}}}+{\frac {m\omega ^{2}}{2}}x^{2}$

For three dimensions, this becomes ${\hat {H}}=-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}+{\frac {m\omega ^{2}}{2}}r^{2}$ where the three-dimensional position vector $\mathbf {r}$ using Cartesian coordinates is $(x,y,z)$ , its magnitude is $r^{2}=\mathbf {r} \cdot \mathbf {r} =|\mathbf {r} |^{2}=x^{2}+y^{2}+z^{2}$

Writing the Hamiltonian out in full shows it is simply the sum of the one-dimensional Hamiltonians in each direction: ${\begin{aligned}{\hat {H}}&=-{\frac {\hbar ^{2}}{2m}}\left({\frac {\partial ^{2}}{\partial x^{2}}}+{\frac {\partial ^{2}}{\partial y^{2}}}+{\frac {\partial ^{2}}{\partial z^{2}}}\right)+{\frac {m\omega ^{2}}{2}}\left(x^{2}+y^{2}+z^{2}\right)\\[6pt]&=\left(-{\frac {\hbar ^{2}}{2m}}{\frac {\partial ^{2}}{\partial x^{2}}}+{\frac {m\omega ^{2}}{2}}x^{2}\right)+\left(-{\frac {\hbar ^{2}}{2m}}{\frac {\partial ^{2}}{\partial y^{2}}}+{\frac {m\omega ^{2}}{2}}y^{2}\right)+\left(-{\frac {\hbar ^{2}}{2m}}{\frac {\partial ^{2}}{\partial z^{2}}}+{\frac {m\omega ^{2}}{2}}z^{2}\right)\end{aligned}}$

### Rigid rotor

For a rigid rotor —i.e., system of particles which can rotate freely about any axes, not bound in any potential (such as free molecules with negligible vibrational degrees of freedom , say due to double or triple chemical bonds ), the Hamiltonian is: ${\hat {H}}=-{\frac {\hbar ^{2}}{2I_{xx}}}{\hat {J}}_{x}^{2}-{\frac {\hbar ^{2}}{2I_{yy}}}{\hat {J}}_{y}^{2}-{\frac {\hbar ^{2}}{2I_{zz}}}{\hat {J}}_{z}^{2}$ where $I_{xx}$ , $I_{yy}$ , and $I_{zz}$ are the moment of inertia components (technically the diagonal elements of the moment of inertia tensor ), and ${\hat {J}}_{x}$ , ${\hat {J}}_{y}$ , and ${\hat {J}}_{z}$ are the total angular momentum operators (components), about the $x$ , $y$ , and $z$ axes respectively.

### Electrostatic (Coulomb) potential

The Coulomb potential energy for two point charges $q_{1}$ and $q_{2}$ (i.e., those that have no spatial extent independently), in three dimensions, is (in SI units —rather than Gaussian units which are frequently used in electromagnetism ): $V={\frac {q_{1}q_{2}}{4\pi \varepsilon _{0}|\mathbf {r} |}}$

However, this is only the potential for one point charge due to another. If there are many charged particles, each charge has a potential energy due to every other point charge (except itself). For $N$ charges, the potential energy of charge $q_{j}$ due to all other charges is (see also Electrostatic potential energy stored in a configuration of discrete point charges ): $V_{j}={\frac {1}{2}}\sum _{i\neq j}q_{i}\phi (\mathbf {r} _{i})={\frac {1}{8\pi \varepsilon _{0}}}\sum _{i\neq j}{\frac {q_{i}q_{j}}{|\mathbf {r} _{i}-\mathbf {r} _{j}|}}$ where $\phi (\mathbf {r} _{i})$ is the electrostatic potential of charge $q_{j}$ at $\mathbf {r} _{i}$ . The total potential of the system is then the sum over $j$ : $V={\frac {1}{8\pi \varepsilon _{0}}}\sum _{j=1}^{N}\sum _{i\neq j}{\frac {q_{i}q_{j}}{|\mathbf {r} _{i}-\mathbf {r} _{j}|}}$ so the Hamiltonian is: ${\begin{aligned}{\hat {H}}&=-{\frac {\hbar ^{2}}{2}}\sum _{j=1}^{N}{\frac {1}{m_{j}}}\nabla _{j}^{2}+{\frac {1}{8\pi \varepsilon _{0}}}\sum _{j=1}^{N}\sum _{i\neq j}{\frac {q_{i}q_{j}}{|\mathbf {r} _{i}-\mathbf {r} _{j}|}}\\&=\sum _{j=1}^{N}\left(-{\frac {\hbar ^{2}}{2m_{j}}}\nabla _{j}^{2}+{\frac {1}{8\pi \varepsilon _{0}}}\sum _{i\neq j}{\frac {q_{i}q_{j}}{|\mathbf {r} _{i}-\mathbf {r} _{j}|}}\right)\\\end{aligned}}$

### Electric dipole in an electric field

For an electric dipole moment $\mathbf {d}$ constituting charges of magnitude $q$ , in a uniform, electrostatic field (time-independent) $\mathbf {E}$ , positioned in one place, the potential is: $V=-\mathbf {\hat {d}} \cdot \mathbf {E}$ the dipole moment itself is the operator $\mathbf {\hat {d}} =q\mathbf {\hat {r}}$

Since the particle is stationary, there is no translational kinetic energy of the dipole, so the Hamiltonian of the dipole is just the potential energy: ${\hat {H}}=-\mathbf {\hat {d}} \cdot \mathbf {E} =-q\mathbf {\hat {r}} \cdot \mathbf {E}$

### Magnetic dipole in a magnetic field

For a magnetic dipole moment ${\boldsymbol {\mu }}$ in a uniform, magnetostatic field (time-independent) $\mathbf {B}$ , positioned in one place, the potential is: $V=-{\boldsymbol {\mu }}\cdot \mathbf {B}$

Since the particle is stationary, there is no translational kinetic energy of the dipole, so the Hamiltonian of the dipole is just the potential energy: ${\hat {H}}=-{\boldsymbol {\mu }}\cdot \mathbf {B}$

For a spin- 1 ⁄ 2 particle, the corresponding spin magnetic moment is: ${\boldsymbol {\mu }}_{S}={\frac {g_{s}e}{2m}}\mathbf {S}$ where $g_{s}$ is the "spin g-factor " (not to be confused with the gyromagnetic ratio ), $e$ is the electron charge, $\mathbf {S}$ is the spin operator vector, whose components are the Pauli matrices , hence ${\hat {H}}={\frac {g_{s}e}{2m}}\mathbf {S} \cdot \mathbf {B}$

### Charged particle in an electromagnetic field

For a particle with mass $m$ and charge $q$ in an electromagnetic field, described by the scalar potential $\phi$ and vector potential $\mathbf {A}$ , there are two parts to the Hamiltonian to substitute for. The canonical momentum operator $\mathbf {\hat {p}}$ , which includes a contribution from the $\mathbf {A}$ field and fulfils the canonical commutation relation , must be quantized; $\mathbf {\hat {p}} =m{\dot {\mathbf {r} }}+q\mathbf {A} ,$ where $m{\dot {\mathbf {r} }}$ is the kinetic momentum . The quantization prescription reads $\mathbf {\hat {p}} =-i\hbar \nabla ,$ so the corresponding kinetic energy operator is ${\hat {T}}={\frac {1}{2}}m{\dot {\mathbf {r} }}\cdot {\dot {\mathbf {r} }}={\frac {1}{2m}}\left(\mathbf {\hat {p}} -q\mathbf {A} \right)^{2}$ and the potential energy, which is due to the $\phi$ field, is given by ${\hat {V}}=q\phi .$

Casting all of these into the Hamiltonian gives ${\hat {H}}={\frac {1}{2m}}\left(-i\hbar \nabla -q\mathbf {A} \right)^{2}+q\phi .$

## Energy eigenket degeneracy, symmetry, and conservation laws

In many systems, two or more energy eigenstates have the same energy. A simple example of this is a free particle, whose energy eigenstates have wavefunctions that are propagating plane waves. The energy of each of these plane waves is inversely proportional to the square of its wavelength . A wave propagating in the $x$ direction is a different state from one propagating in the $y$ direction, but if they have the same wavelength, then their energies will be the same. When this happens, the states are said to be degenerate .

It turns out that degeneracy occurs whenever a nontrivial unitary operator $U$ commutes with the Hamiltonian. To see this, suppose that $|a\rangle$ is an energy eigenket. Then $U|a\rangle$ is an energy eigenket with the same eigenvalue, since $UH|a\rangle =UE_{a}|a\rangle =E_{a}(U|a\rangle )=H\;(U|a\rangle ).$

Since $U$ is nontrivial, at least one pair of $|a\rangle$ and $U|a\rangle$ must represent distinct states. Therefore, $H$ has at least one pair of degenerate energy eigenkets. In the case of the free particle, the unitary operator which produces the symmetry is the rotation operator , which rotates the wavefunctions by some angle while otherwise preserving their shape.

The existence of a symmetry operator implies the existence of a conserved observable. Let $G$ be the Hermitian generator of $U$ : $U=I-i\varepsilon G+O(\varepsilon ^{2})$

It is straightforward to show that if $U$ commutes with $H$ , then so does $G$ : $[H,G]=0$

Therefore, ${\frac {\partial }{\partial t}}\langle \psi (t)|G|\psi (t)\rangle ={\frac {1}{i\hbar }}\langle \psi (t)|[G,H]|\psi (t)\rangle =0.$

In obtaining this result, we have used the Schrödinger equation, as well as its dual , $\langle \psi (t)|H=-i\hbar {d \over \ dt}\langle \psi (t)|.$

Thus, the expected value of the observable $G$ is conserved for any state of the system. In the case of the free particle, the conserved quantity is the angular momentum .

## Hamilton's equations

Hamilton 's equations in classical Hamiltonian mechanics have a direct analogy in quantum mechanics. Suppose we have a set of basis states $\left\{\left|n\right\rangle \right\}$ , which need not necessarily be eigenstates of the energy. For simplicity, we assume that they are discrete, and that they are orthonormal, i.e., $\langle n'|n\rangle =\delta _{nn'}$

Note that these basis states are assumed to be independent of time. We will assume that the Hamiltonian is also independent of time.

The instantaneous state of the system at time $t$ , $\left|\psi \left(t\right)\right\rangle$ , can be expanded in terms of these basis states: $|\psi (t)\rangle =\sum _{n}a_{n}(t)|n\rangle$ where $a_{n}(t)=\langle n|\psi (t)\rangle .$

The coefficients $a_{n}(t)$ are complex variables. We can treat them as coordinates which specify the state of the system, like the position and momentum coordinates which specify a classical system. Like classical coordinates, they are generally not constant in time, and their time dependence gives rise to the time dependence of the system as a whole.

The expectation value of the Hamiltonian of this state, which is also the mean energy, is $\langle H(t)\rangle \mathrel {\stackrel {\mathrm {def} }{=}} \langle \psi (t)|H|\psi (t)\rangle =\sum _{nn'}a_{n'}^{*}a_{n}\langle n'|H|n\rangle$ where the last step was obtained by expanding $\left|\psi \left(t\right)\right\rangle$ in terms of the basis states.

Each $a_{n}(t)$ actually corresponds to two independent degrees of freedom, since the variable has a real part and an imaginary part. We now perform the following trick: instead of using the real and imaginary parts as the independent variables, we use $a_{n}(t)$ and its complex conjugate $a_{n}^{*}(t)$ . With this choice of independent variables, we can calculate the partial derivative ${\frac {\partial \langle H\rangle }{\partial a_{n'}^{*}}}=\sum _{n}a_{n}\langle n'|H|n\rangle =\langle n'|H|\psi \rangle$

By applying the Schrödinger equation and using the orthonormality of the basis states, this further reduces to ${\frac {\partial \langle H\rangle }{\partial a_{n'}^{*}}}=i\hbar {\frac {\partial a_{n'}}{\partial t}}$

Similarly, one can show that ${\frac {\partial \langle H\rangle }{\partial a_{n}}}=-i\hbar {\frac {\partial a_{n}^{*}}{\partial t}}$

If we define "conjugate momentum" variables $\pi _{n}$ by $\pi _{n}(t)=i\hbar a_{n}^{*}(t)$ then the above equations become ${\frac {\partial \langle H\rangle }{\partial \pi _{n}}}={\frac {\partial a_{n}}{\partial t}},\quad {\frac {\partial \langle H\rangle }{\partial a_{n}}}=-{\frac {\partial \pi _{n}}{\partial t}}$ which is precisely the form of Hamilton's equations, with the $a_{n}$ s as the generalized coordinates, the $\pi _{n}$ s as the conjugate momenta, and $\langle H\rangle$ taking the place of the classical Hamiltonian.
