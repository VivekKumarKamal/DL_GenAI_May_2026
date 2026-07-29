# Probability amplitude

> **Query Topic**: significance of probability amplitudes in quantum mechanics (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 15, Frequency: 15)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Probability_amplitude

---

In quantum mechanics , a probability amplitude is a complex number used for describing the behaviour of systems. The square modulus of this quantity at a point in space represents a probability density at that point.

Probability amplitudes provide a relationship between the quantum state of a system and the results of observations of that system, a link that was first proposed by Max Born , in 1926. Interpretation of values of a wave function as the probability amplitude is a pillar of the Copenhagen interpretation of quantum mechanics. In fact, the properties of the space of wave functions were being used to make physical predictions (such as emissions from atoms being at certain discrete energies) before any physical interpretation of a particular function was offered. Born was awarded half of the 1954 Nobel Prize in Physics for this understanding, and the probability thus calculated is sometimes called the "Born probability".

These probabilistic concepts, namely the probability density and quantum measurements , were vigorously contested at the time by the original physicists working on the theory, such as Schrödinger and Einstein . It is the source of the mysterious consequences and philosophical difficulties in the interpretations of quantum mechanics —topics that continue to be debated even today.

## Physical overview

Neglecting some technical complexities, the problem of quantum measurement is the behaviour of a quantum state, for which the value of the observable Q to be measured is uncertain . Such a state is thought to be a coherent superposition of the observable's eigenstates , states on which the value of the observable is uniquely defined, for different possible values of the observable.

When a measurement of Q is made, the system (under the Copenhagen interpretation ) jumps to one of the eigenstates , returning the eigenvalue belonging to that eigenstate. The system may always be described by a linear combination or superposition of these eigenstates with unequal "weights" . Intuitively it is clear that eigenstates with heavier "weights" are more "likely" to be produced. Indeed, which of the above eigenstates the system jumps to is given by a probabilistic law: the probability of the system jumping to the state is proportional to the absolute value of the corresponding numerical weight squared. These numerical weights are called probability amplitudes, and this relationship used to calculate probabilities from given pure quantum states (such as wave functions) is called the Born rule .

Clearly, the sum of the probabilities, which equals the sum of the absolute squares of the probability amplitudes, must equal 1. This is the normalization requirement.

If the system is known to be in some eigenstate of Q (e.g. after an observation of the corresponding eigenvalue of Q ) the probability of observing that eigenvalue becomes equal to 1 (certain) for all subsequent measurements of Q (so long as no other important forces act between the measurements). In other words, the probability amplitudes are zero for all the other eigenstates, and remain zero for the future measurements. If the set of eigenstates to which the system can jump upon measurement of Q is the same as the set of eigenstates for measurement of R , then subsequent measurements of either Q or R always produce the same values with probability of 1, no matter the order in which they are applied. The probability amplitudes are unaffected by either measurement, and the observables are said to commute .

By contrast, if the eigenstates of Q and R are different, then measurement of R produces a jump to a state that is not an eigenstate of Q . Therefore, if the system is known to be in some eigenstate of Q (all probability amplitudes zero except for one eigenstate), then when R is observed the probability amplitudes are changed. A second, subsequent observation of Q no longer certainly produces the eigenvalue corresponding to the starting state. In other words, the probability amplitudes for the second measurement of Q depend on whether it comes before or after a measurement of R , and the two observables do not commute .

## Mathematical formulation

In a formal setup, the state of an isolated physical system in quantum mechanics is represented, at a fixed time $t$ , by a state vector | Ψ ⟩ belonging to a separable complex Hilbert space . Using bra–ket notation the relation between state vector and "position basis " $\{|x\rangle \}$ of the Hilbert space can be written as

$\psi (x)=\langle x|\Psi \rangle$ .

Its relation with an observable can be elucidated by generalizing the quantum state $\psi$ to a measurable function and its domain of definition to a given σ -finite measure space $(X,{\mathcal {A}},\mu )$ . This allows for a refinement of Lebesgue's decomposition theorem , decomposing μ into three mutually singular parts

$\mu =\mu _{\mathrm {ac} }+\mu _{\mathrm {sc} }+\mu _{\mathrm {pp} }$

where μ ac is absolutely continuous with respect to the Lebesgue measure, μ sc is singular with respect to the Lebesgue measure and atomless, and μ pp is a pure point measure.

### Continuous amplitudes

A usual presentation of the probability amplitude is that of a wave function $\psi$ belonging to the L 2 space of ( equivalence classes of) square integrable functions , i.e., $\psi$ belongs to L 2 ( X ) if and only if

$\|\psi \|^{2}=\int _{X}|\psi (x)|^{2}\,dx<\infty$ .

If the norm is equal to 1 and $|\psi (x)|^{2}\in \mathbb {R} _{\geq 0}$ such that

$\int _{X}|\psi (x)|^{2}\,dx\equiv \int _{X}\,d\mu _{ac}(x)=1$ ,

then $|\psi (x)|^{2}$ is the probability density function for a measurement of the particle's position at a given time, defined as the Radon–Nikodym derivative with respect to the Lebesgue measure (e.g. on the set R of all real numbers ). As probability is a dimensionless quantity, | ψ ( x ) | 2 must have the inverse dimension of the variable of integration x . For example, the above amplitude has dimension [L −1/2 ], where L represents length .

Whereas a Hilbert space is separable if and only if it admits a countable orthonormal basis, the range of a continuous random variable $x$ is an uncountable set (i.e. the probability that the system is "at position $x$ " will always be zero ). As such, eigenstates of an observable need not necessarily be measurable functions belonging to L 2 ( X ) (see normalization condition below). A typical example is the position operator ${\hat {\mathrm {x} }}$ defined as

$\langle x|{\hat {\mathrm {x} }}|\Psi \rangle ={\hat {\mathrm {x} }}\langle x|\Psi \rangle =x_{0}\psi (x),\quad x\in \mathbb {R} ,$

whose eigenfunctions are Dirac delta functions

$\psi (x)=\delta (x-x_{0})$

which clearly do not belong to L 2 ( X ) . By replacing the state space by a suitable rigged Hilbert space , however, the rigorous notion of eigenstates from spectral theorem as well as spectral decomposition is preserved.

### Discrete amplitudes

Let $\mu _{pp}$ be atomic (i.e. the set $A\subset X$ in ${\mathcal {A}}$ is an atom ); specifying the measure of any discrete variable x ∈ A equal to 1 . The amplitudes are composed of state vector | Ψ ⟩ indexed by A ; its components are denoted by ψ ( x ) for uniformity with the previous case. If the ℓ 2 -norm of | Ψ ⟩ is equal to 1, then | ψ ( x ) | 2 is a probability mass function .

A convenient configuration space X is such that each point x produces some unique value of the observable Q . For discrete X it means that all elements of the standard basis are eigenvectors of Q . Then $\psi (x)$ is the probability amplitude for the eigenstate | x ⟩ . If it corresponds to a non- degenerate eigenvalue of Q , then $|\psi (x)|^{2}$ gives the probability of the corresponding value of Q for the initial state | Ψ ⟩ .

| ψ ( x ) | = 1 if and only if | x ⟩ is the same quantum state as | Ψ ⟩ . ψ ( x ) = 0 if and only if | x ⟩ and | Ψ ⟩ are orthogonal . Otherwise the modulus of ψ ( x ) is between 0 and 1.

A discrete probability amplitude may be considered as a fundamental frequency in the probability frequency domain ( spherical harmonics ) for the purposes of simplifying M-theory transformation calculations. [ citation needed ] Discrete dynamical variables are used in such problems as a particle in an idealized reflective box and quantum harmonic oscillator . [ clarification needed ]

### Examples

An example of the discrete case is a quantum system that can be in two possible states , e.g. the polarization of a photon . When the polarization is measured, it could be the horizontal state $|H\rangle$ or the vertical state $|V\rangle$ . Until its polarization is measured the photon can be in a superposition of both these states, so its state $|\psi \rangle$ could be written as

$|\psi \rangle =\alpha |H\rangle +\beta |V\rangle$ ,

with $\alpha$ and $\beta$ the probability amplitudes for the states $|H\rangle$ and $|V\rangle$ respectively. When the photon's polarization is measured, the resulting state is either horizontal or vertical. But in a random experiment, the probability of being horizontally polarized is $|\alpha |^{2}$ , and the probability of being vertically polarized is $|\beta |^{2}$ .

Hence, a photon in a state ${\textstyle |\psi \rangle ={\sqrt {\frac {1}{3}}}|H\rangle -i{\sqrt {\frac {2}{3}}}|V\rangle }$ would have a probability of ${\textstyle {\frac {1}{3}}}$ to come out horizontally polarized, and a probability of ${\textstyle {\frac {2}{3}}}$ to come out vertically polarized when an ensemble of measurements are made. The order of such results, is, however, completely random.

Another example is quantum spin. If a spin-measuring apparatus is pointing along the z-axis and is therefore able to measure the z-component of the spin ( ${\textstyle \sigma _{z}}$ ), the following must be true for the measurement of spin "up" and "down":

$\sigma _{z}|u\rangle =(+1)|u\rangle$

$\sigma _{z}|d\rangle =(-1)|d\rangle$

If one assumes that system is prepared, so that +1 is registered in ${\textstyle \sigma _{x}}$ and then the apparatus is rotated to measure ${\textstyle \sigma _{z}}$ , the following holds:

${\begin{aligned}\langle r|u\rangle &=\left({\frac {1}{\sqrt {2}}}\langle u|+{\frac {1}{\sqrt {2}}}\langle d|\right)\cdot |u\rangle \\&=\left({\frac {1}{\sqrt {2}}}{\begin{pmatrix}1\\0\end{pmatrix}}+{\frac {1}{\sqrt {2}}}{\begin{pmatrix}0\\1\end{pmatrix}}\right)\cdot {\begin{pmatrix}1\\0\end{pmatrix}}\\&={\frac {1}{\sqrt {2}}}\end{aligned}}$

The probability amplitude of measuring spin up is given by ${\textstyle \langle r|u\rangle }$ , since the system had the initial state ${\textstyle |r\rangle }$ . The probability of measuring ${\textstyle |u\rangle }$ is given by

$P(|u\rangle )=\langle r|u\rangle \langle u|r\rangle =\left({\frac {1}{\sqrt {2}}}\right)^{2}={\frac {1}{2}}$

Which agrees with experiment.

## Normalization

In the example above, the measurement must give either | H ⟩ or | V ⟩ , so the total probability of measuring | H ⟩ or | V ⟩ must be 1. This leads to a constraint that α 2 + β 2 = 1 ; more generally the sum of the squared moduli of the probability amplitudes of all the possible states is equal to one . If to understand "all the possible states" as an orthonormal basis , that makes sense in the discrete case, then this condition is the same as the norm-1 condition explained above .

One can always divide any non-zero element of a Hilbert space by its norm and obtain a normalized state vector. Not every wave function belongs to the Hilbert space L 2 ( X ) , though. Wave functions that fulfill this constraint are called normalizable .

The Schrödinger equation , describing states of quantum particles, has solutions that describe a system and determine precisely how the state changes with time . Suppose a wave function ψ ( x , t ) gives a description of the particle (position x at a given time t ). A wave function is square integrable if

$\int |\psi (\mathbf {x} ,t)|^{2}\,\mathrm {d\mathbf {x} } =a^{2}<\infty .$

After normalization the wave function still represents the same state and is therefore equal by definition to

$\psi (\mathbf {x} ,t):={\frac {\psi (\mathbf {x} ,t)}{a}}.$

Under the standard Copenhagen interpretation , the normalized wavefunction gives probability amplitudes for the position of the particle. Hence, ρ ( x ) = | ψ ( x , t ) | 2 is a probability density function and the probability that the particle is in the volume V at fixed time t is given by

$P_{\mathbf {x} \in V}(t)=\int _{V}|\psi (\mathbf {x} ,t)|^{2}\,\mathrm {d\mathbf {x} } =\int _{V}\rho (\mathbf {x} )\,\mathrm {d\mathbf {x} } .$

The probability density function does not vary with time as the evolution of the wave function is dictated by the Schrödinger equation and is therefore entirely deterministic. This is key to understanding the importance of this interpretation: for a given particle constant mass , initial ψ ( x , t 0 ) and potential , the Schrödinger equation fully determines subsequent wavefunctions. The above then gives probabilities of locations of the particle at all subsequent times.

## In the context of the double-slit experiment

Probability amplitudes have special significance because they act in quantum mechanics as the equivalent of conventional probabilities, with many analogous laws, as described above. For example, in the classic double-slit experiment , electrons are fired randomly at two slits, and the probability distribution of detecting electrons at all parts on a large screen placed behind the slits, is questioned. An intuitive answer is that P (through either slit) = P (through first slit) + P (through second slit) , where P (event) is the probability of that event. This is obvious if one assumes that an electron passes through either slit. When no measurement apparatus that determines through which slit the electrons travel is installed, the observed probability distribution on the screen reflects the interference pattern that is common with light waves. If one assumes the above law to be true, then this pattern cannot be explained. The particles cannot be said to go through either slit and the simple explanation does not work. The correct explanation is, however, by the association of probability amplitudes to each event. The complex amplitudes which represent the electron passing each slit ( ψ first and ψ second ) follow the law of precisely the form expected: ψ total = ψ first + ψ second . This is the principle of quantum superposition . The probability, which is the modulus squared of the probability amplitude, then, follows the interference pattern under the requirement that amplitudes are complex: $P=\left|\psi _{\text{first}}+\psi _{\text{second}}\right|^{2}=\left|\psi _{\text{first}}\right|^{2}+\left|\psi _{\text{second}}\right|^{2}+2\left|\psi _{\text{first}}\right|\left|\psi _{\text{second}}\right|\cos(\varphi _{1}-\varphi _{2}).$ Here, $\varphi _{1}$ and $\varphi _{2}$ are the arguments of ψ first and ψ second respectively. A purely real formulation has too few dimensions to describe the system's state when superposition is taken into account. That is, without the arguments of the amplitudes, we cannot describe the phase-dependent interference. The crucial term ${\textstyle 2\left|\psi _{\text{first}}\right|\left|\psi _{\text{second}}\right|\cos(\varphi _{1}-\varphi _{2})}$ is called the "interference term", and this would be missing if we had added the probabilities.

However, one may choose to devise an experiment in which the experimenter observes which slit each electron goes through. Then, due to wavefunction collapse , the interference pattern is not observed on the screen.

One may go further in devising an experiment in which the experimenter gets rid of this "which-path information" by a "quantum eraser" . Then, according to the Copenhagen interpretation , the case A applies again and the interference pattern is restored.

## Conservation of probabilities and the continuity equation

Intuitively, since a normalised wave function stays normalised while evolving according to the wave equation, there will be a relationship between the change in the probability density of the particle's position and the change in the amplitude at these positions.

Define the probability current (or flux) j as

$\mathbf {j} ={\hbar \over m}{1 \over {2i}}\left(\psi ^{*}\nabla \psi -\psi \nabla \psi ^{*}\right)={\hbar \over m}\operatorname {Im} \left(\psi ^{*}\nabla \psi \right),$

measured in units of (probability)/(area × time).

Then the current satisfies the equation

$\nabla \cdot \mathbf {j} +{\partial \over \partial t}|\psi |^{2}=0.$

The probability density is $\rho =|\psi |^{2}$ , this equation is exactly the continuity equation , appearing in many situations in physics where we need to describe the local conservation of quantities. The best example is in classical electrodynamics, where j corresponds to current density corresponding to electric charge, and the density is the charge-density. The corresponding continuity equation describes the local conservation of charges .

## Composite systems

For two quantum systems with spaces L 2 ( X 1 ) and L 2 ( X 2 ) and given states | Ψ 1 ⟩ and | Ψ 2 ⟩ respectively, their combined state | Ψ 1 ⟩ ⊗ | Ψ 2 ⟩ can be expressed as ψ 1 ( x 1 ) ψ 2 ( x 2 ) a function on X 1 × X 2 , that gives the product of respective probability measures . In other words, amplitudes of a non- entangled composite state are products of original amplitudes, and respective observables on the systems 1 and 2 behave on these states as independent random variables . This strengthens the probabilistic interpretation explicated above .

## Amplitudes in operators

The concept of amplitudes is also used in the context of scattering theory , notably in the form of S-matrices . Whereas moduli of vector components squared, for a given vector, give a fixed probability distribution, moduli of matrix elements squared are interpreted as transition probabilities just as in a random process. Like a finite-dimensional unit vector specifies a finite probability distribution, a finite-dimensional unitary matrix specifies transition probabilities between a finite number of states.

The "transitional" interpretation may be applied to L 2 s on non-discrete spaces as well. [ clarification needed ]
