# Uncertainty principle

> **Query Topic**: relationship between the Wigner function and the density matrix operator (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 48, Frequency: 13)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Uncertainty_principle

---

The uncertainty principle , also known as Heisenberg's indeterminacy principle , is a fundamental concept in quantum mechanics . It states that there is a limit to the precision with which certain pairs of physical properties, such as position and momentum , can be simultaneously known. In other words, the more accurately one property is measured, the less accurately the other property can be known.

More formally, the uncertainty principle is any of a variety of mathematical inequalities asserting a fundamental limit to the product of the accuracy of certain related pairs of measurements on a quantum system, such as position , x , and momentum, p . Such paired-variables are known as complementary variables or canonically conjugate variables .

First introduced in 1927 by German physicist Werner Heisenberg , the formal inequality relating the standard deviation of position σ x and the standard deviation of momentum σ p was derived by Earle Hesse Kennard later that year and by Hermann Weyl in 1928:

$\sigma _{x}\sigma _{p}\geq {\frac {\hbar }{2}}$

where $\hbar ={\frac {h}{2\pi }}$ is the reduced Planck constant .

The quintessentially quantum mechanical uncertainty principle comes in many forms other than position–momentum. The energy–time relationship is widely used to relate quantum state lifetime to measured energy widths but its formal derivation is fraught with confusing issues about the nature of time. The basic principle has been extended in numerous directions; it must be considered in many kinds of fundamental physical measurements.

## Position–momentum

It is vital to illustrate how the principle applies to relatively intelligible physical situations since it is indiscernible on the macroscopic scales that humans experience. Two alternative frameworks for quantum physics offer different explanations for the uncertainty principle. The wave mechanics picture of the uncertainty principle is more visually intuitive, but the more abstract matrix mechanics picture formulates it in a way that generalizes more easily. The effect of Heisenberg uncertainity principle is significant only for motion of microscopic objects and is negligible for that of macroscopic objects .

Mathematically, in wave mechanics, the uncertainty relation between position and momentum arises because the expressions of the wavefunction in the two corresponding orthonormal bases in Hilbert space are Fourier transforms of one another (i.e., position and momentum are conjugate variables ). A nonzero function and its Fourier transform cannot both be sharply localized at the same time. A similar tradeoff between the variances of Fourier conjugates arises in all systems underlain by Fourier analysis, for example in sound waves: A pure tone is a sharp spike at a single frequency, while its Fourier transform gives the shape of the sound wave in the time domain, which is a completely delocalized sine wave. In quantum mechanics, the two key points are that the position of the particle takes the form of a matter wave, and momentum is its Fourier conjugate, assured by the de Broglie relation p = ħk , where k is the wavenumber .

In matrix mechanics , the mathematical formulation of quantum mechanics , any pair of non- commuting self-adjoint operators representing observables are subject to similar uncertainty limits. An eigenstate of an observable represents the state of the wavefunction for a certain measurement value (the eigenvalue). For example, if a measurement of an observable A is performed, then the system is in a particular eigenstate Ψ of that observable. However, the particular eigenstate of the observable A need not be an eigenstate of another observable B : If so, then it does not have a unique associated measurement for it, as the system is not in an eigenstate of that observable.

### Visualization

The uncertainty principle can be visualized using the position- and momentum-space wavefunctions for one spinless particle with mass in one dimension.

The more localized the position-space wavefunction, the more likely the particle is to be found with the position coordinates in that region, and correspondingly the momentum-space wavefunction is less localized so the possible momentum components the particle could have are more widespread. Conversely, the more localized the momentum-space wavefunction, the more likely the particle is to be found with those values of momentum components in that region, and correspondingly the less localized the position-space wavefunction, so the position coordinates the particle could occupy are more widespread. These wavefunctions are Fourier transforms of each other: mathematically, the uncertainty principle expresses the relationship between conjugate variables in the transform.

### Wave mechanics interpretation

According to the de Broglie hypothesis , every object in the universe is associated with a wave . Thus every object, from an elementary particle to atoms, molecules and on up to planets and beyond are subject to the uncertainty principle.

The time-independent wave function of a single-moded plane wave of wavenumber k 0 or momentum p 0 is $\psi (x)\propto e^{ik_{0}x}=e^{ip_{0}x/\hbar }~.$

The Born rule states that this should be interpreted as a probability density amplitude function in the sense that the probability of finding the particle between a and b is $\operatorname {P} [a\leq X\leq b]=\int _{a}^{b}|\psi (x)|^{2}\,\mathrm {d} x~.$

In the case of the single-mode plane wave, $|\psi (x)|^{2}$ is 1 if $X=x$ and 0 otherwise. In other words, the particle position is extremely uncertain in the sense that it could be essentially anywhere along the wave packet.

On the other hand, consider a wave function that is a sum of many waves , which we may write as $\psi (x)\propto \sum _{n}A_{n}e^{ip_{n}x/\hbar }~,$ where A n represents the relative contribution of the mode p n to the overall total. The figures to the right show how with the addition of many plane waves, the wave packet can become more localized. We may take this a step further to the continuum limit , where the wave function is an integral over all possible modes $\psi (x)={\frac {1}{\sqrt {2\pi \hbar }}}\int _{-\infty }^{\infty }\varphi (p)\cdot e^{ipx/\hbar }\,dp~,$ with $\varphi (p)$ representing the amplitude of these modes and is called the wave function in momentum space . In mathematical terms, we say that $\varphi (p)$ is the Fourier transform of $\psi (x)$ and that x and p are conjugate variables . Adding together all of these plane waves comes at a cost, namely the momentum has become less precise, having become a mixture of waves of many different momenta.

One way to quantify the precision of the position and momentum is the standard deviation σ . Since $|\psi (x)|^{2}$ is a probability density function for position, we calculate its standard deviation.

The precision of the position is improved, i.e. reduced σ x , by using many plane waves, thereby weakening the precision of the momentum, i.e. increased σ p . Another way of stating this is that σ x and σ p have an inverse relationship or are at least bounded from below. This is the uncertainty principle, the exact limit of which is the Kennard bound.

### Proof of the Kennard inequality using wave mechanics

We are interested in the variances of position and momentum, defined as $\sigma _{x}^{2}=\int _{-\infty }^{\infty }x^{2}\cdot |\psi (x)|^{2}\,dx-\left(\int _{-\infty }^{\infty }x\cdot |\psi (x)|^{2}\,dx\right)^{2}$ $\sigma _{p}^{2}=\int _{-\infty }^{\infty }p^{2}\cdot |\varphi (p)|^{2}\,dp-\left(\int _{-\infty }^{\infty }p\cdot |\varphi (p)|^{2}\,dp\right)^{2}~.$

Without loss of generality , we will assume that the means vanish, which just amounts to a shift of the origin of our coordinates. (A more general proof that does not make this assumption is given below.) This gives us the simpler form $\sigma _{x}^{2}=\int _{-\infty }^{\infty }x^{2}\cdot |\psi (x)|^{2}\,dx$ $\sigma _{p}^{2}=\int _{-\infty }^{\infty }p^{2}\cdot |\varphi (p)|^{2}\,dp~.$

The function $f(x)=x\cdot \psi (x)$ can be interpreted as a vector in a function space . We can define an inner product for a pair of functions u ( x ) and v ( x ) in this vector space: $\langle u\mid v\rangle =\int _{-\infty }^{\infty }u^{*}(x)\cdot v(x)\,dx,$ where the asterisk denotes the complex conjugate .

With this inner product defined, we note that the variance for position can be written as $\sigma _{x}^{2}=\int _{-\infty }^{\infty }|f(x)|^{2}\,dx=\langle f\mid f\rangle ~.$

We can repeat this for momentum by interpreting the function ${\tilde {g}}(p)=p\cdot \varphi (p)$ as a vector, but we can also take advantage of the fact that $\psi (x)$ and $\varphi (p)$ are Fourier transforms of each other. We evaluate the inverse Fourier transform through integration by parts : ${\begin{aligned}g(x)&={\frac {1}{\sqrt {2\pi \hbar }}}\cdot \int _{-\infty }^{\infty }{\tilde {g}}(p)\cdot e^{ipx/\hbar }\,dp\\&={\frac {1}{\sqrt {2\pi \hbar }}}\int _{-\infty }^{\infty }p\cdot \varphi (p)\cdot e^{ipx/\hbar }\,dp\\&={\frac {1}{2\pi \hbar }}\int _{-\infty }^{\infty }\left[p\cdot \int _{-\infty }^{\infty }\psi (\chi )e^{-ip\chi /\hbar }\,d\chi \right]\cdot e^{ipx/\hbar }\,dp\\&={\frac {i}{2\pi }}\int _{-\infty }^{\infty }\left[{\cancel {\left.\psi (\chi )e^{-ip\chi /\hbar }\right|_{-\infty }^{\infty }}}-\int _{-\infty }^{\infty }{\frac {d\psi (\chi )}{d\chi }}e^{-ip\chi /\hbar }\,d\chi \right]\cdot e^{ipx/\hbar }\,dp\\&=-i\int _{-\infty }^{\infty }{\frac {d\psi (\chi )}{d\chi }}\left[{\frac {1}{2\pi }}\int _{-\infty }^{\infty }\,e^{ip(x-\chi )/\hbar }\,dp\right]\,d\chi \\&=-i\int _{-\infty }^{\infty }{\frac {d\psi (\chi )}{d\chi }}\left[\delta \left({\frac {x-\chi }{\hbar }}\right)\right]\,d\chi \\&=-i\hbar \int _{-\infty }^{\infty }{\frac {d\psi (\chi )}{d\chi }}\left[\delta \left(x-\chi \right)\right]\,d\chi \\&=-i\hbar {\frac {d\psi (x)}{dx}}\\&=\left(-i\hbar {\frac {d}{dx}}\right)\cdot \psi (x),\end{aligned}}$ where $v={\frac {\hbar }{-ip}}e^{-ip\chi /\hbar }$ in the integration by parts, the cancelled term vanishes because the wave function vanishes at both infinities and $|e^{-ip\chi /\hbar }|=1$ , and then use the Dirac delta function which is valid because ${\dfrac {d\psi (\chi )}{d\chi }}$ does not depend on p .

The term ${\textstyle -i\hbar {\frac {d}{dx}}}$ is called the momentum operator in position space. Applying Plancherel's theorem , we see that the variance for momentum can be written as $\sigma _{p}^{2}=\int _{-\infty }^{\infty }|{\tilde {g}}(p)|^{2}\,dp=\int _{-\infty }^{\infty }|g(x)|^{2}\,dx=\langle g\mid g\rangle .$

The Cauchy–Schwarz inequality asserts that $\sigma _{x}^{2}\sigma _{p}^{2}=\langle f\mid f\rangle \cdot \langle g\mid g\rangle \geq |\langle f\mid g\rangle |^{2}~.$

The modulus squared of any complex number z can be expressed as $|z|^{2}={\Big (}{\text{Re}}(z){\Big )}^{2}+{\Big (}{\text{Im}}(z){\Big )}^{2}\geq {\Big (}{\text{Im}}(z){\Big )}^{2}=\left({\frac {z-z^{\ast }}{2i}}\right)^{2}.$ we let $z=\langle f|g\rangle$ and $z^{*}=\langle g\mid f\rangle$ and substitute these into the equation above to get $|\langle f\mid g\rangle |^{2}\geq \left({\frac {\langle f\mid g\rangle -\langle g\mid f\rangle }{2i}}\right)^{2}~.$

All that remains is to evaluate these inner products.

${\begin{aligned}\langle f\mid g\rangle -\langle g\mid f\rangle &=\int _{-\infty }^{\infty }\psi ^{*}(x)\,x\cdot \left(-i\hbar {\frac {d}{dx}}\right)\,\psi (x)\,dx-\int _{-\infty }^{\infty }\psi ^{*}(x)\,\left(-i\hbar {\frac {d}{dx}}\right)\cdot x\,\psi (x)\,dx\\&=i\hbar \cdot \int _{-\infty }^{\infty }\psi ^{*}(x)\left[\left(-x\cdot {\frac {d\psi (x)}{dx}}\right)+{\frac {d(x\psi (x))}{dx}}\right]\,dx\\&=i\hbar \cdot \int _{-\infty }^{\infty }\psi ^{*}(x)\left[\left(-x\cdot {\frac {d\psi (x)}{dx}}\right)+\psi (x)+\left(x\cdot {\frac {d\psi (x)}{dx}}\right)\right]\,dx\\&=i\hbar \cdot \int _{-\infty }^{\infty }\psi ^{*}(x)\psi (x)\,dx\\&=i\hbar \cdot \int _{-\infty }^{\infty }|\psi (x)|^{2}\,dx\\&=i\hbar \end{aligned}}$

Plugging this into the above inequalities, we get $\sigma _{x}^{2}\sigma _{p}^{2}\geq |\langle f\mid g\rangle |^{2}\geq \left({\frac {\langle f\mid g\rangle -\langle g\mid f\rangle }{2i}}\right)^{2}=\left({\frac {i\hbar }{2i}}\right)^{2}={\frac {\hbar ^{2}}{4}}$ and taking the square root $\sigma _{x}\sigma _{p}\geq {\frac {\hbar }{2}}~.$

with equality if and only if p and x are linearly dependent. Note that the only physics involved in this proof was that $\psi (x)$ and $\varphi (p)$ are wave functions for position and momentum, which are Fourier transforms of each other. A similar result would hold for any pair of conjugate variables.

### Matrix mechanics interpretation

In matrix mechanics, observables such as position and momentum are represented by self-adjoint operators. When considering pairs of observables, an important quantity is the commutator . For a pair of operators Â and ${\hat {B}}$ , one defines their commutator as $[{\hat {A}},{\hat {B}}]={\hat {A}}{\hat {B}}-{\hat {B}}{\hat {A}}.$ In the case of position and momentum, the commutator is the canonical commutation relation $[{\hat {x}},{\hat {p}}]=i\hbar .$

The physical meaning of the non-commutativity can be understood by considering the effect of the commutator on position and momentum eigenstates . Let $|\psi \rangle$ be a right eigenstate of position with a constant eigenvalue x 0 . By definition, this means that ${\hat {x}}|\psi \rangle =x_{0}|\psi \rangle .$ Applying the commutator to $|\psi \rangle$ yields $[{\hat {x}},{\hat {p}}]|\psi \rangle =({\hat {x}}{\hat {p}}-{\hat {p}}{\hat {x}})|\psi \rangle =({\hat {x}}-x_{0}{\hat {I}}){\hat {p}}\,|\psi \rangle =i\hbar |\psi \rangle ,$ where Î is the identity operator .

Suppose, for the sake of proof by contradiction , that $|\psi \rangle$ is also a right eigenstate of momentum, with constant eigenvalue p 0 . If this were true, then one could write $({\hat {x}}-x_{0}{\hat {I}}){\hat {p}}\,|\psi \rangle =({\hat {x}}-x_{0}{\hat {I}})p_{0}\,|\psi \rangle =(x_{0}{\hat {I}}-x_{0}{\hat {I}})p_{0}\,|\psi \rangle =0.$ On the other hand, the above canonical commutation relation requires that $[{\hat {x}},{\hat {p}}]|\psi \rangle =i\hbar |\psi \rangle \neq 0.$ This implies that no quantum state can simultaneously be both a position and a momentum eigenstate.

When a state is measured, it is projected onto an eigenstate in the basis of the relevant observable. For example, if a particle's position is measured, then the state amounts to a position eigenstate. This means that the state is not a momentum eigenstate, however, but rather it can be represented as a sum of multiple momentum basis eigenstates. In other words, the momentum must be less precise. This precision may be quantified by the standard deviations, $\sigma _{x}={\sqrt {\langle {\hat {x}}^{2}\rangle -\langle {\hat {x}}\rangle ^{2}}}$ $\sigma _{p}={\sqrt {\langle {\hat {p}}^{2}\rangle -\langle {\hat {p}}\rangle ^{2}}}.$

As in the wave mechanics interpretation above, one sees a tradeoff between the respective precisions of the two, quantified by the uncertainty principle.

### Quantum harmonic oscillator stationary states

Consider a one-dimensional quantum harmonic oscillator . It is possible to express the position and momentum operators in terms of the creation and annihilation operators : ${\hat {x}}={\sqrt {\frac {\hbar }{2m\omega }}}(a+a^{\dagger })$ ${\hat {p}}=i{\sqrt {\frac {m\omega \hbar }{2}}}(a^{\dagger }-a).$

Using the standard rules for creation and annihilation operators on the energy eigenstates, $a^{\dagger }|n\rangle ={\sqrt {n+1}}|n+1\rangle$ $a|n\rangle ={\sqrt {n}}|n-1\rangle ,$ the variances may be computed directly, $\sigma _{x}^{2}={\frac {\hbar }{m\omega }}\left(n+{\frac {1}{2}}\right)$ $\sigma _{p}^{2}=\hbar m\omega \left(n+{\frac {1}{2}}\right)\,.$ The product of these standard deviations is then $\sigma _{x}\sigma _{p}=\hbar \left(n+{\frac {1}{2}}\right)\geq {\frac {\hbar }{2}}.~$

In particular, the above Kennard bound is saturated for the ground state n =0 , for which the probability density is just the normal distribution .

### Quantum harmonic oscillators with Gaussian initial condition

In a quantum harmonic oscillator of characteristic angular frequency ω , place a state that is offset from the bottom of the potential by some displacement x 0 as $\psi (x)=\left({\frac {m\Omega }{\pi \hbar }}\right)^{1/4}\exp {\left(-{\frac {m\Omega (x-x_{0})^{2}}{2\hbar }}\right)},$ where Ω describes the width of the initial state but need not be the same as ω . Through integration over the propagator , we can solve for the full time -dependent solution. After many cancelations, the probability densities reduce to $|\Psi (x,t)|^{2}\sim {\mathcal {N}}\left(x_{0}\cos {(\omega t)},{\frac {\hbar }{2m\Omega }}\left(\cos ^{2}(\omega t)+{\frac {\Omega ^{2}}{\omega ^{2}}}\sin ^{2}{(\omega t)}\right)\right)$ $|\Phi (p,t)|^{2}\sim {\mathcal {N}}\left(-mx_{0}\omega \sin(\omega t),{\frac {\hbar m\Omega }{2}}\left(\cos ^{2}{(\omega t)}+{\frac {\omega ^{2}}{\Omega ^{2}}}\sin ^{2}{(\omega t)}\right)\right),$ where we have used the notation ${\mathcal {N}}(\mu ,\sigma ^{2})$ to denote a normal distribution of mean μ and variance σ 2 . Copying the variances above and applying trigonometric identities , we can write the product of the standard deviations as ${\begin{aligned}\sigma _{x}\sigma _{p}&={\frac {\hbar }{2}}{\sqrt {\left(\cos ^{2}{(\omega t)}+{\frac {\Omega ^{2}}{\omega ^{2}}}\sin ^{2}{(\omega t)}\right)\left(\cos ^{2}{(\omega t)}+{\frac {\omega ^{2}}{\Omega ^{2}}}\sin ^{2}{(\omega t)}\right)}}\\&={\frac {\hbar }{4}}{\sqrt {3+{\frac {1}{2}}\left({\frac {\Omega ^{2}}{\omega ^{2}}}+{\frac {\omega ^{2}}{\Omega ^{2}}}\right)-\left({\frac {1}{2}}\left({\frac {\Omega ^{2}}{\omega ^{2}}}+{\frac {\omega ^{2}}{\Omega ^{2}}}\right)-1\right)\cos {(4\omega t)}}}\end{aligned}}$

From the relations ${\frac {\Omega ^{2}}{\omega ^{2}}}+{\frac {\omega ^{2}}{\Omega ^{2}}}\geq 2,\quad |\cos(4\omega t)|\leq 1,$ we can conclude the following (the right most equality holds only when Ω = ω ): $\sigma _{x}\sigma _{p}\geq {\frac {\hbar }{4}}{\sqrt {3+{\frac {1}{2}}\left({\frac {\Omega ^{2}}{\omega ^{2}}}+{\frac {\omega ^{2}}{\Omega ^{2}}}\right)-\left({\frac {1}{2}}\left({\frac {\Omega ^{2}}{\omega ^{2}}}+{\frac {\omega ^{2}}{\Omega ^{2}}}\right)-1\right)}}={\frac {\hbar }{2}}.$

### Coherent states

A coherent state is a right eigenstate of the annihilation operator , ${\hat {a}}|\alpha \rangle =\alpha |\alpha \rangle ,$ which may be represented in terms of Fock states as $|\alpha \rangle =e^{-{|\alpha |^{2} \over 2}}\sum _{n=0}^{\infty }{\alpha ^{n} \over {\sqrt {n!}}}|n\rangle$

In the picture where the coherent state is a massive particle in a quantum harmonic oscillator, the position and momentum operators may be expressed in terms of the annihilation operators in the same formulas above and used to calculate the variances, $\sigma _{x}^{2}={\frac {\hbar }{2m\omega }},$ $\sigma _{p}^{2}={\frac {\hbar m\omega }{2}}.$ Therefore, every coherent state saturates the Kennard bound $\sigma _{x}\sigma _{p}={\sqrt {\frac {\hbar }{2m\omega }}}\,{\sqrt {\frac {\hbar m\omega }{2}}}={\frac {\hbar }{2}}.$ with position and momentum each contributing an amount ${\textstyle {\sqrt {\hbar /2}}}$ in a "balanced" way. Moreover, every squeezed coherent state also saturates the Kennard bound although the individual contributions of position and momentum need not be balanced in general.

### Particle in a box

Consider a particle in a one-dimensional box of length $L$ . The eigenfunctions in position and momentum space are $\psi _{n}(x,t)={\begin{cases}A\sin(k_{n}x)\mathrm {e} ^{-\mathrm {i} \omega _{n}t},&0<x<L,\\0,&{\text{otherwise,}}\end{cases}}$ and $\varphi _{n}(p,t)={\sqrt {\frac {\pi L}{\hbar }}}\,\,{\frac {n\left(1-(-1)^{n}e^{-ikL}\right)e^{-i\omega _{n}t}}{\pi ^{2}n^{2}-k^{2}L^{2}}},$ where ${\textstyle \omega _{n}={\frac {\pi ^{2}\hbar n^{2}}{8L^{2}m}}}$ and we have used the de Broglie relation $p=\hbar k$ . The variances of $x$ and $p$ can be calculated explicitly: $\sigma _{x}^{2}={\frac {L^{2}}{12}}\left(1-{\frac {6}{n^{2}\pi ^{2}}}\right)$ $\sigma _{p}^{2}=\left({\frac {\hbar n\pi }{L}}\right)^{2}.$

The product of the standard deviations is therefore $\sigma _{x}\sigma _{p}={\frac {\hbar }{2}}{\sqrt {{\frac {n^{2}\pi ^{2}}{3}}-2}}.$ For all $n=1,\,2,\,3,\,\ldots$ , the quantity ${\textstyle {\sqrt {{\frac {n^{2}\pi ^{2}}{3}}-2}}}$ is greater than 1, so the uncertainty principle is never violated. For numerical concreteness, the smallest value occurs when $n=1$ , in which case $\sigma _{x}\sigma _{p}={\frac {\hbar }{2}}{\sqrt {{\frac {\pi ^{2}}{3}}-2}}\approx 0.568\hbar >{\frac {\hbar }{2}}.$

### Constant momentum

Assume a particle initially has a momentum space wave function described by a normal distribution around some constant momentum p 0 according to $\varphi (p)=\left({\frac {x_{0}}{\hbar {\sqrt {\pi }}}}\right)^{1/2}\exp \left({\frac {-x_{0}^{2}(p-p_{0})^{2}}{2\hbar ^{2}}}\right),$ where we have introduced a reference scale ${\textstyle x_{0}={\sqrt {\hbar /m\omega _{0}}}}$ , with $\omega _{0}>0$ describing the width of the distribution—cf. nondimensionalization . If the state is allowed to evolve in free space, then the time-dependent momentum and position space wave functions are $\Phi (p,t)=\left({\frac {x_{0}}{\hbar {\sqrt {\pi }}}}\right)^{1/2}\exp \left({\frac {-x_{0}^{2}(p-p_{0})^{2}}{2\hbar ^{2}}}-{\frac {ip^{2}t}{2m\hbar }}\right),$ $\Psi (x,t)=\left({\frac {1}{x_{0}{\sqrt {\pi }}}}\right)^{1/2}{\frac {e^{-x_{0}^{2}p_{0}^{2}/2\hbar ^{2}}}{\sqrt {1+i\omega _{0}t}}}\,\exp \left(-{\frac {(x-ix_{0}^{2}p_{0}/\hbar )^{2}}{2x_{0}^{2}(1+i\omega _{0}t)}}\right).$

Since $\langle p(t)\rangle =p_{0}$ and $\sigma _{p}(t)=\hbar /({\sqrt {2}}x_{0})$ , this can be interpreted as a particle moving along with constant momentum at arbitrarily high precision. On the other hand, the standard deviation of the position is $\sigma _{x}={\frac {x_{0}}{\sqrt {2}}}{\sqrt {1+\omega _{0}^{2}t^{2}}}$ such that the uncertainty product can only increase with time as $\sigma _{x}(t)\sigma _{p}(t)={\frac {\hbar }{2}}{\sqrt {1+\omega _{0}^{2}t^{2}}}$

## Mathematical formalism

Starting with Kennard's derivation of position-momentum uncertainty, Howard Percy Robertson developed a formulation for arbitrary Hermitian operators ${\hat {\mathcal {O}}}$ expressed in terms of their standard deviation $\sigma _{\mathcal {O}}={\sqrt {\langle {\hat {\mathcal {O}}}^{2}\rangle -\langle {\hat {\mathcal {O}}}\rangle ^{2}}},$ where the brackets $\langle {\hat {\mathcal {O}}}\rangle$ indicate an expectation value of the observable represented by operator ${\hat {\mathcal {O}}}$ . For a pair of operators ${\hat {A}}$ and ${\hat {B}}$ , define their commutator as $[{\hat {A}},{\hat {B}}]={\hat {A}}{\hat {B}}-{\hat {B}}{\hat {A}},$ and the Robertson uncertainty relation is given by $\sigma _{A}\sigma _{B}\geq \left|{\frac {1}{2i}}\langle [{\hat {A}},{\hat {B}}]\rangle \right|={\frac {1}{2}}\left|\langle [{\hat {A}},{\hat {B}}]\rangle \right|.$

Erwin Schrödinger showed how to allow for correlation between the operators, giving a stronger inequality, known as the Robertson–Schrödinger uncertainty relation ,

$\sigma _{A}^{2}\sigma _{B}^{2}\geq \left|{\frac {1}{2}}\langle \{{\hat {A}},{\hat {B}}\}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle \right|^{2}+\left|{\frac {1}{2i}}\langle [{\hat {A}},{\hat {B}}]\rangle \right|^{2},$

where the anticommutator, $\{{\hat {A}},{\hat {B}}\}={\hat {A}}{\hat {B}}+{\hat {B}}{\hat {A}}$ is used.

The derivation shown here incorporates and builds off of those shown in Robertson, Schrödinger and standard textbooks such as Griffiths. For any Hermitian operator ${\hat {A}}$ , based upon the definition of variance , we have $\sigma _{A}^{2}=\langle ({\hat {A}}-\langle {\hat {A}}\rangle )\Psi |({\hat {A}}-\langle {\hat {A}}\rangle )\Psi \rangle .$ we let $|f\rangle =|({\hat {A}}-\langle {\hat {A}}\rangle )\Psi \rangle$ and thus $\sigma _{A}^{2}=\langle f\mid f\rangle \,.$

Similarly, for any other Hermitian operator ${\hat {B}}$ in the same state $\sigma _{B}^{2}=\langle ({\hat {B}}-\langle {\hat {B}}\rangle )\Psi |({\hat {B}}-\langle {\hat {B}}\rangle )\Psi \rangle =\langle g\mid g\rangle$ for $|g\rangle =|({\hat {B}}-\langle {\hat {B}}\rangle )\Psi \rangle .$

The product of the two deviations can thus be expressed as

In order to relate the two vectors $|f\rangle$ and $|g\rangle$ , we use the Cauchy–Schwarz inequality which is defined as $\langle f\mid f\rangle \langle g\mid g\rangle \geq |\langle f\mid g\rangle |^{2},$ and thus Equation ( 1 ) can be written as

Since $\langle f\mid g\rangle$ is in general a complex number, we use the fact that the modulus squared of any complex number $z$ is defined as $|z|^{2}=zz^{*}$ , where $z^{*}$ is the complex conjugate of $z$ . The modulus squared can also be expressed as

we let $z=\langle f\mid g\rangle$ and $z^{*}=\langle g\mid f\rangle$ and substitute these into the equation above to get

The inner product $\langle f\mid g\rangle$ is written out explicitly as $\langle f\mid g\rangle =\langle ({\hat {A}}-\langle {\hat {A}}\rangle )\Psi |({\hat {B}}-\langle {\hat {B}}\rangle )\Psi \rangle ,$ and using the fact that ${\hat {A}}$ and ${\hat {B}}$ are Hermitian operators, we find ${\begin{aligned}\langle f\mid g\rangle &=\langle \Psi |({\hat {A}}-\langle {\hat {A}}\rangle )({\hat {B}}-\langle {\hat {B}}\rangle )\Psi \rangle \\[4pt]&=\langle \Psi \mid ({\hat {A}}{\hat {B}}-{\hat {A}}\langle {\hat {B}}\rangle -{\hat {B}}\langle {\hat {A}}\rangle +\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle )\Psi \rangle \\[4pt]&=\langle \Psi \mid {\hat {A}}{\hat {B}}\Psi \rangle -\langle \Psi \mid {\hat {A}}\langle {\hat {B}}\rangle \Psi \rangle -\langle \Psi \mid {\hat {B}}\langle {\hat {A}}\rangle \Psi \rangle +\langle \Psi \mid \langle {\hat {A}}\rangle \langle {\hat {B}}\rangle \Psi \rangle \\[4pt]&=\langle {\hat {A}}{\hat {B}}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle +\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle \\[4pt]&=\langle {\hat {A}}{\hat {B}}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle .\end{aligned}}$

Similarly it can be shown that $\langle g\mid f\rangle =\langle {\hat {B}}{\hat {A}}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle .$

Thus, we have $\langle f\mid g\rangle -\langle g\mid f\rangle =\langle {\hat {A}}{\hat {B}}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle -\langle {\hat {B}}{\hat {A}}\rangle +\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle =\langle [{\hat {A}},{\hat {B}}]\rangle$ and $\langle f\mid g\rangle +\langle g\mid f\rangle =\langle {\hat {A}}{\hat {B}}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle +\langle {\hat {B}}{\hat {A}}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle =\langle \{{\hat {A}},{\hat {B}}\}\rangle -2\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle .$

We now substitute the above two equations above back into Eq. ( 4 ) and get $|\langle f\mid g\rangle |^{2}={\Big (}{\frac {1}{2}}\langle \{{\hat {A}},{\hat {B}}\}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle {\Big )}^{2}+{\Big (}{\frac {1}{2i}}\langle [{\hat {A}},{\hat {B}}]\rangle {\Big )}^{2}\,.$

Substituting the above into Equation ( 2 ) we get the Schrödinger uncertainty relation $\sigma _{A}\sigma _{B}\geq {\sqrt {{\Big (}{\frac {1}{2}}\langle \{{\hat {A}},{\hat {B}}\}\rangle -\langle {\hat {A}}\rangle \langle {\hat {B}}\rangle {\Big )}^{2}+{\Big (}{\frac {1}{2i}}\langle [{\hat {A}},{\hat {B}}]\rangle {\Big )}^{2}}}.$

This proof has an issue related to the domains of the operators involved. For the proof to make sense, the vector ${\hat {B}}|\Psi \rangle$ has to be in the domain of the unbounded operator ${\hat {A}}$ , which is not always the case. In fact, the Robertson uncertainty relation is false if ${\hat {A}}$ is an angle variable and ${\hat {B}}$ is the derivative with respect to this variable. In this example, the commutator is a nonzero constant—just as in the Heisenberg uncertainty relation—and yet there are states where the product of the uncertainties is zero. (See the counterexample section below.) This issue can be overcome by using a variational method for the proof, or by working with an exponentiated version of the canonical commutation relations.

Note that in the general form of the Robertson–Schrödinger uncertainty relation, there is no need to assume that the operators ${\hat {A}}$ and ${\hat {B}}$ are self-adjoint operators . It suffices to assume that they are merely symmetric operators . (The distinction between these two notions is generally glossed over in the physics literature, where the term Hermitian is used for either or both classes of operators. See Chapter 9 of Hall's book for a detailed discussion of this important but technical distinction.)

### Phase space

In the phase space formulation of quantum mechanics, the Robertson–Schrödinger relation follows from a positivity condition on a real star-square function. Given a Wigner function $W(x,p)$ with star product ★ and a function f , the following is generally true: $\langle f^{*}\star f\rangle =\int (f^{*}\star f)\,W(x,p)\,dx\,dp\geq 0~.$

Choosing $f=a+bx+cp$ , we arrive at $\langle f^{*}\star f\rangle ={\begin{bmatrix}a^{*}&b^{*}&c^{*}\end{bmatrix}}{\begin{bmatrix}1&\langle x\rangle &\langle p\rangle \\\langle x\rangle &\langle x\star x\rangle &\langle x\star p\rangle \\\langle p\rangle &\langle p\star x\rangle &\langle p\star p\rangle \end{bmatrix}}{\begin{bmatrix}a\\b\\c\end{bmatrix}}\geq 0~.$

Since this positivity condition is true for all a , b , and c , it follows that all the eigenvalues of the matrix are non-negative.

The non-negative eigenvalues then imply a corresponding non-negativity condition on the determinant , $\det {\begin{bmatrix}1&\langle x\rangle &\langle p\rangle \\\langle x\rangle &\langle x\star x\rangle &\langle x\star p\rangle \\\langle p\rangle &\langle p\star x\rangle &\langle p\star p\rangle \end{bmatrix}}=\det {\begin{bmatrix}1&\langle x\rangle &\langle p\rangle \\\langle x\rangle &\langle x^{2}\rangle &\left\langle xp+{\frac {i\hbar }{2}}\right\rangle \\\langle p\rangle &\left\langle xp-{\frac {i\hbar }{2}}\right\rangle &\langle p^{2}\rangle \end{bmatrix}}\geq 0~,$ or, explicitly, after algebraic manipulation, $\sigma _{x}^{2}\sigma _{p}^{2}=\left(\langle x^{2}\rangle -\langle x\rangle ^{2}\right)\left(\langle p^{2}\rangle -\langle p\rangle ^{2}\right)\geq \left(\langle xp\rangle -\langle x\rangle \langle p\rangle \right)^{2}+{\frac {\hbar ^{2}}{4}}~.$

### Examples

Since the Robertson and Schrödinger relations are for general operators, the relations can be applied to any two observables to obtain specific uncertainty relations. A few of the most common relations found in the literature are given below.

- Position–linear momentum uncertainty relation : for the position and linear momentum operators, the canonical commutation relation $[{\hat {x}},{\hat {p}}]=i\hbar$ implies the Kennard inequality from above: $\sigma _{x}\sigma _{p}\geq {\frac {\hbar }{2}}.$

- Angular momentum uncertainty relation : For two orthogonal components of the total angular momentum operator of an object: $\sigma _{J_{i}}\sigma _{J_{j}}\geq {\frac {\hbar }{2}}{\big |}\langle J_{k}\rangle {\big |},$ where i , j , k are distinct, and J i denotes angular momentum along the x i axis. This relation implies that unless all three components vanish together, only a single component of a system's angular momentum can be defined with arbitrary precision, normally the component parallel to an external (magnetic or electric) field. Moreover, for $[J_{x},J_{y}]=i\hbar \varepsilon _{xyz}J_{z}$ , a choice ${\hat {A}}=J_{x}$ , ${\hat {B}}=J_{y}$ , in angular momentum multiplets, ψ = | j , m ⟩, bounds the Casimir invariant (angular momentum squared, $\langle J_{x}^{2}+J_{y}^{2}+J_{z}^{2}\rangle$ ) from below and thus yields useful constraints such as j ( j + 1) ≥ m ( m + 1) , and hence j ≥ m , among others.

- For the number of electrons in a superconductor and the phase of its Ginzburg–Landau order parameter $\Delta N\,\Delta \varphi \geq 1.$

### Limitations

The derivation of the Robertson inequality for operators ${\hat {A}}$ and ${\hat {B}}$ requires ${\hat {A}}{\hat {B}}\psi$ and ${\hat {B}}{\hat {A}}\psi$ to be defined. There are quantum systems where these conditions are not valid. One example is a quantum particle on a ring , where the wave function depends on an angular variable $\theta$ in the interval $[0,2\pi ]$ . Define "position" and "momentum" operators ${\hat {A}}$ and ${\hat {B}}$ by ${\hat {A}}\psi (\theta )=\theta \psi (\theta ),\quad \theta \in [0,2\pi ],$ and ${\hat {B}}\psi =-i\hbar {\frac {d\psi }{d\theta }},$ with periodic boundary conditions on ${\hat {B}}$ . The definition of ${\hat {A}}$ depends the $\theta$ range from 0 to $2\pi$ . These operators satisfy the usual commutation relations for position and momentum operators, $[{\hat {A}},{\hat {B}}]=i\hbar$ . More precisely, ${\hat {A}}{\hat {B}}\psi -{\hat {B}}{\hat {A}}\psi =i\hbar \psi$ whenever both ${\hat {A}}{\hat {B}}\psi$ and ${\hat {B}}{\hat {A}}\psi$ are defined, and the space of such $\psi$ is a dense subspace of the quantum Hilbert space.

Now let $\psi$ be any of the eigenstates of ${\hat {B}}$ , which are given by $\psi (\theta )=e^{2\pi in\theta }$ . These states are normalizable, unlike the eigenstates of the momentum operator on the line. Also the operator ${\hat {A}}$ is bounded, since $\theta$ ranges over a bounded interval. Thus, in the state $\psi$ , the uncertainty of $B$ is zero and the uncertainty of $A$ is finite, so that $\sigma _{A}\sigma _{B}=0.$ The Robertson uncertainty principle does not apply in this case: $\psi$ is not in the domain of the operator ${\hat {B}}{\hat {A}}$ , since multiplication by $\theta$ disrupts the periodic boundary conditions imposed on ${\hat {B}}$ .

For the usual position and momentum operators ${\hat {X}}$ and ${\hat {P}}$ on the real line, no such counterexamples can occur. As long as $\sigma _{x}$ and $\sigma _{p}$ are defined in the state $\psi$ , the Heisenberg uncertainty principle holds, even if $\psi$ fails to be in the domain of ${\hat {X}}{\hat {P}}$ or of ${\hat {P}}{\hat {X}}$ .

### Mixed states

The Robertson–Schrödinger uncertainty can be improved noting that it must hold for all components $\varrho _{k}$ in any decomposition of the density matrix given as $\varrho =\sum _{k}p_{k}\varrho _{k}.$ Here, for the probabilities $p_{k}\geq 0$ and $\sum _{k}p_{k}=1$ hold. Then, using the relation $\sum _{k}a_{k}\sum _{k}b_{k}\geq \left(\sum _{k}{\sqrt {a_{k}b_{k}}}\right)^{2}$ for $a_{k},b_{k}\geq 0$ ,
it follows that $\sigma _{A}^{2}\sigma _{B}^{2}\geq \left[\sum _{k}p_{k}L(\varrho _{k})\right]^{2},$ where the function in the bound is defined $L(\varrho )={\sqrt {\left|{\frac {1}{2}}\operatorname {tr} (\rho \{A,B\})-\operatorname {tr} (\rho A)\operatorname {tr} (\rho B)\right|^{2}+\left|{\frac {1}{2i}}\operatorname {tr} (\rho [A,B])\right|^{2}}}.$ The above relation very often has a bound larger than that of the original Robertson–Schrödinger uncertainty relation. Thus, we need to calculate the bound of the Robertson–Schrödinger uncertainty for the mixed components of the quantum state rather than for the quantum state, and compute an average of their square roots. The following expression is stronger than the Robertson–Schrödinger uncertainty relation $\sigma _{A}^{2}\sigma _{B}^{2}\geq \left[\max _{p_{k},\varrho _{k}}\sum _{k}p_{k}L(\varrho _{k})\right]^{2},$ where on the right-hand side there is a concave roof over the decompositions of the density matrix.
The improved relation above is saturated by all single-qubit quantum states.

With similar arguments, one can derive a relation with a convex roof on the right-hand side $\sigma _{A}^{2}F_{Q}[\varrho ,B]\geq 4\left[\min _{p_{k},\Psi _{k}}\sum _{k}p_{k}L(\vert \Psi _{k}\rangle \langle \Psi _{k}\vert )\right]^{2}$ where $F_{Q}[\varrho ,B]$ denotes the quantum Fisher information and the density matrix is decomposed to pure states as $\varrho =\sum _{k}p_{k}\vert \Psi _{k}\rangle \langle \Psi _{k}\vert .$ The derivation takes advantage of the fact that the quantum Fisher information is the convex roof of the variance times four.

A simpler inequality follows without a convex roof $\sigma _{A}^{2}F_{Q}[\varrho ,B]\geq \vert \langle i[A,B]\rangle \vert ^{2},$ which is stronger than the Heisenberg uncertainty relation, since for the quantum Fisher information we have $F_{Q}[\varrho ,B]\leq 4\sigma _{B},$ while for pure states the equality holds.

### The Maccone–Pati uncertainty relations

The Robertson–Schrödinger uncertainty relation can be trivial if the state of the system is chosen to be eigenstate of one of the observable. The stronger uncertainty relations proved by Lorenzo Maccone and Arun K. Pati give non-trivial bounds on the sum of the variances for two incompatible observables. (Earlier works on uncertainty relations formulated as the sum of variances include, e.g., Ref. due to Yichen Huang.) For two non-commuting observables $A$ and $B$ the first stronger uncertainty relation is given by $\sigma _{A}^{2}+\sigma _{B}^{2}\geq \pm i\langle \Psi \mid [A,B]|\Psi \rangle +\mid \langle \Psi \mid (A\pm iB)\mid {\bar {\Psi }}\rangle |^{2},$ where $\sigma _{A}^{2}=\langle \Psi |A^{2}|\Psi \rangle -\langle \Psi \mid A\mid \Psi \rangle ^{2}$ , $\sigma _{B}^{2}=\langle \Psi |B^{2}|\Psi \rangle -\langle \Psi \mid B\mid \Psi \rangle ^{2}$ , $|{\bar {\Psi }}\rangle$ is a normalized vector that is orthogonal to the state of the system $|\Psi \rangle$ and one should choose the sign of $\pm i\langle \Psi \mid [A,B]\mid \Psi \rangle$ to make this real quantity a positive number.

The second stronger uncertainty relation is given by $\sigma _{A}^{2}+\sigma _{B}^{2}\geq {\frac {1}{2}}|\langle {\bar {\Psi }}_{A+B}\mid (A+B)\mid \Psi \rangle |^{2}$ where $|{\bar {\Psi }}_{A+B}\rangle$ is a state orthogonal to $|\Psi \rangle$ .
The form of $|{\bar {\Psi }}_{A+B}\rangle$ implies that the right-hand side of the new uncertainty relation is nonzero unless $|\Psi \rangle$ is an eigenstate of $(A+B)$ . One may note that $|\Psi \rangle$ can be an eigenstate of $(A+B)$ without being an eigenstate of either $A$ or $B$ . However, when $|\Psi \rangle$ is an eigenstate of one of the two observables the Heisenberg–Schrödinger uncertainty relation becomes trivial. But the lower bound in the new relation is nonzero unless $|\Psi \rangle$ is an eigenstate of both.

## Energy–time

An energy–time uncertainty relation like $\Delta E\Delta t\gtrsim \hbar /2,$ has a long, controversial history; the meaning of $\Delta t$ and $\Delta E$ varies and different formulations have different arenas of validity. However, one well-known application is both well established and experimentally verified: the connection between the life-time of a resonance state, $\tau _{\sqrt {1/2}}$ and its energy width $\Delta E$ : $\tau _{\sqrt {1/2}}\Delta E=\pi \hbar /4.$ In particle-physics, widths from experimental fits to the Breit–Wigner energy distribution are used to characterize the lifetime of quasi-stable or decaying states.

An informal, heuristic meaning of the principle is the following: A state that only exists for a short time cannot have a definite energy. To have a definite energy, the frequency of the state must be defined accurately, and this requires the state to hang around for many cycles, the reciprocal of the required accuracy. For example, in spectroscopy , excited states have a finite lifetime. By the time–energy uncertainty principle, they do not have a definite energy, and, each time they decay, the energy they release is slightly different. The average energy of the outgoing photon has a peak at the theoretical energy of the state, but the distribution has a finite width called the natural linewidth . Fast-decaying states have a broad linewidth, while slow-decaying states have a narrow linewidth. The same linewidth effect also makes it difficult to specify the rest mass of unstable, fast-decaying particles in particle physics . The faster the particle decays (the shorter its lifetime), the less certain is its mass (the larger the particle's width ).

### Time in quantum mechanics

The concept of "time" in quantum mechanics offers many challenges. There is no quantum theory of time measurement; relativity is both fundamental to time and difficult to include in quantum mechanics. While position and momentum are associated with a single particle, time is a system property: it has no operator needed for the Robertson–Schrödinger relation. The mathematical treatment of stable and unstable quantum systems differ. These factors combine to make energy–time uncertainty principles controversial.

Three notions of "time" can be distinguished: external, intrinsic, and observable. External or laboratory time is seen by the experimenter; intrinsic time is inferred by changes in dynamic variables, like the hands of a clock or the motion of a free particle ; observable time concerns time as an observable, the measurement of time-separated events.

An external-time energy–time uncertainty principle might say that measuring the energy of a quantum system to an accuracy $\Delta E$ requires a time interval $\Delta t>h/\Delta E$ . However, Yakir Aharonov and David Bohm have shown that, in some quantum systems, energy can be measured accurately within an arbitrarily short time: external-time uncertainty principles are not universal.

Intrinsic time is the basis for several formulations of energy–time uncertainty relations, including the Mandelstam–Tamm relation discussed in the next section. A physical system with an intrinsic time closely matching the external laboratory time is called a "clock".

Observable time, measuring time between two events, remains a challenge for quantum theories; some progress has been made using positive operator-valued measure concepts.

### Mandelstam–Tamm

In 1945, Leonid Mandelstam and Igor Tamm derived a non-relativistic time–energy uncertainty relation as follows. From Heisenberg mechanics, the generalized Ehrenfest theorem for an observable B without explicit time dependence, represented by a self-adjoint operator ${\hat {B}}$ relates time dependence of the average value of ${\hat {B}}$ to the average of its commutator with the Hamiltonian:

${\frac {d\langle {\hat {B}}\rangle }{dt}}={\frac {i}{\hbar }}\langle [{\hat {H}},{\hat {B}}]\rangle .$

The value of $\langle [{\hat {H}},{\hat {B}}]\rangle$ is then substituted in the Robertson uncertainty relation for the energy operator ${\hat {H}}$ and ${\hat {B}}$ : $\sigma _{H}\sigma _{B}\geq \left|{\frac {1}{2i}}\langle [{\hat {H}},{\hat {B}}]\rangle \right|,$ giving $\sigma _{H}{\frac {\sigma _{B}}{\left|{\frac {d\langle {\hat {B}}\rangle }{dt}}\right|}}\geq {\frac {\hbar }{2}}$ (whenever the denominator is nonzero).
While this is a universal result, it depends upon the observable chosen and that the deviations $\sigma _{H}$ and $\sigma _{B}$ are computed for a particular state.
Identifying $\Delta E\equiv \sigma _{E}$ and the characteristic time $\tau _{B}\equiv {\frac {\sigma _{B}}{\left|{\frac {d\langle {\hat {B}}\rangle }{dt}}\right|}}$ gives an energy–time relationship $\Delta E\tau _{B}\geq {\frac {\hbar }{2}}.$ Although $\tau _{B}$ has the dimension of time, it is different from the time parameter t that enters the Schrödinger equation . This $\tau _{B}$ can be interpreted as time for which the expectation value of the observable, $\langle {\hat {B}}\rangle ,$ changes by an amount equal to one standard deviation. Examples:

- The time a free quantum particle passes a point in space is more uncertain as the energy of the state is more precisely controlled: $\Delta T=\hbar /2\Delta E.$ Since the time spread is related to the particle position spread and the energy spread is related to the momentum spread, this relation is directly related to position–momentum uncertainty.

- A Delta particle , a quasistable composite of quarks related to protons and neutrons, has a lifetime of 10 −23 s, so its measured mass equivalent to energy , 1232 MeV/ c 2 , varies by ±120 MeV/ c 2 ; this variation is intrinsic and not caused by measurement errors.

- Two energy states $\psi _{1,2}$ with energies $E_{1,2},$ superimposed to create a composite state

$\Psi (x,t)=a\psi _{1}(x)e^{-iE_{1}t/h}+b\psi _{2}(x)e^{-iE_{2}t/h}.$

The probability amplitude of this state has a time-dependent interference term:

$|\Psi (x,t)|^{2}=a^{2}|\psi _{1}(x)|^{2}+b^{2}|\psi _{2}(x)|^{2}+2ab\cos({\frac {E_{2}-E_{1}}{\hbar }}t).$

The oscillation period varies inversely with the energy difference: $\tau =2\pi \hbar /(E_{2}-E_{1})$ .

Each example has a different meaning for the time uncertainty, according to the observable and state used.

### Quantum field theory

Some formulations of quantum field theory uses temporary electron–positron pairs in its calculations called virtual particles . The mass-energy and lifetime of these particles are related by the energy–time uncertainty relation. The energy of a quantum systems is not known with enough precision to limit their behavior to a single, simple history. Thus the influence of all histories must be incorporated into quantum calculations, including those with much greater or much less energy than the mean of the measured/calculated energy distribution.

The energy–time uncertainty principle does not temporarily violate conservation of energy ; it does not imply that energy can be "borrowed" from the universe as long as it is "returned" within a short amount of time. The energy of the universe is not an exactly known parameter at all times. When events transpire at very short time intervals, there is uncertainty in the energy of these events.

## Harmonic analysis

In the context of harmonic analysis the uncertainty principle implies that one cannot at the same time localize the value of a function and its Fourier transform. To wit, the following inequality holds, $\left(\int _{-\infty }^{\infty }x^{2}|f(x)|^{2}\,dx\right)\left(\int _{-\infty }^{\infty }\xi ^{2}|{\hat {f}}(\xi )|^{2}\,d\xi \right)\geq {\frac {\|f\|_{2}^{4}}{16\pi ^{2}}}.$

Further mathematical uncertainty inequalities, including the above entropic uncertainty , hold between a function f and its Fourier transform ƒ̂ : $H_{x}+H_{\xi }\geq \log(e/2)$

### Signal processing

In the context of time–frequency analysis uncertainty principles are referred to as the Gabor limit , after Dennis Gabor , or sometimes the Heisenberg–Gabor limit . The basic result, which follows from "Benedicks's theorem", below, is that a function cannot be both time limited and band limited (a function and its Fourier transform cannot both have bounded domain)—see bandlimited versus timelimited . More accurately, the time-bandwidth or duration-bandwidth product satisfies $\sigma _{t}\sigma _{f}\geq {\frac {1}{4\pi }}\approx 0.08{\text{ cycles}},$ where $\sigma _{t}$ and $\sigma _{f}$ are the standard deviations of the time and frequency energy concentrations respectively. The minimum is attained for a Gaussian -shaped pulse ( Gabor wavelet ) [For the un-squared Gaussian (i.e. signal amplitude) and its un-squared Fourier transform magnitude $\sigma _{t}\sigma _{f}=1/2\pi$ ; squaring reduces each $\sigma$ by a factor ${\sqrt {2}}$ .] Another common measure is the product of the time and frequency full width at half maximum (of the power/energy), which for the Gaussian equals $2\ln 2/\pi \approx 0.44$ (see bandwidth-limited pulse ).

Stated differently, one cannot simultaneously sharply localize a signal f in both the time domain and frequency domain .

When applied to filters , the result implies that one cannot simultaneously achieve a high temporal resolution and high frequency resolution at the same time; a concrete example are the resolution issues of the short-time Fourier transform —if one uses a wide window, one achieves good frequency resolution at the cost of temporal resolution, while a narrow window has the opposite trade-off.

Alternate theorems give more precise quantitative results, and, in time–frequency analysis, rather than interpreting the (1-dimensional) time and frequency domains separately, one instead interprets the limit as a lower limit on the support of a function in the (2-dimensional) time–frequency plane. In practice, the Gabor limit limits the simultaneous time–frequency resolution one can achieve without interference; it is possible to achieve higher resolution, but at the cost of different components of the signal interfering with each other.

As a result, in order to analyze signals where the transients are important, the wavelet transform is often used instead of the Fourier.

### Discrete Fourier transform

Let $\left\{\mathbf {x_{n}} \right\}:=x_{0},x_{1},\ldots ,x_{N-1}$ be a sequence of N complex numbers and $\left\{\mathbf {X_{k}} \right\}:=X_{0},X_{1},\ldots ,X_{N-1},$ be its discrete Fourier transform .

Denote by $\|x\|_{0}$ the number of non-zero elements in the time sequence $x_{0},x_{1},\ldots ,x_{N-1}$ and by $\|X\|_{0}$ the number of non-zero elements in the frequency sequence $X_{0},X_{1},\ldots ,X_{N-1}$ . Then, $\|x\|_{0}\cdot \|X\|_{0}\geq N.$

This inequality is sharp , with equality achieved when x or X is a Dirac mass, or more generally when x is a nonzero multiple of a Dirac comb supported on a subgroup of the integers modulo N (in which case X is also a Dirac comb supported on a complementary subgroup, and vice versa).

More generally, if T and W are subsets of the integers modulo N , let $L_{T},R_{W}:\ell ^{2}(\mathbb {Z} /N\mathbb {Z} )\to \ell ^{2}(\mathbb {Z} /N\mathbb {Z} )$ denote the time-limiting operator and band-limiting operators , respectively. Then $\|L_{T}R_{W}\|^{2}\leq {\frac {|T||W|}{|G|}}$ where the norm is the operator norm of operators on the Hilbert space $\ell ^{2}(\mathbb {Z} /N\mathbb {Z} )$ of functions on the integers modulo N . This inequality has implications for signal reconstruction .

When N is a prime number , a stronger inequality holds: $\|x\|_{0}+\|X\|_{0}\geq N+1.$ Discovered by Terence Tao , this inequality is also sharp.

### Benedicks's theorem

Amrein–Berthier and Benedicks's theorem intuitively says that the set of points where f is non-zero and the set of points where ƒ̂ is non-zero cannot both be small.

Specifically, it is impossible for a function f in L 2 ( R ) and its Fourier transform ƒ̂ to both be supported on sets of finite Lebesgue measure . A more quantitative version is $\|f\|_{L^{2}(\mathbf {R} ^{d})}\leq Ce^{C|S||\Sigma |}{\bigl (}\|f\|_{L^{2}(S^{c})}+\|{\hat {f}}\|_{L^{2}(\Sigma ^{c})}{\bigr )}~.$

One expects that the factor Ce C | S | | Σ | may be replaced by Ce C ( | S | | Σ | ) 1/ d , which is only known if either S or Σ is convex.

### Hardy's uncertainty principle

The mathematician G. H. Hardy formulated the following uncertainty principle: it is not possible for f and ƒ̂ to both be "very rapidly decreasing". Specifically, if f in $L^{2}(\mathbb {R} )$ is such that $|f(x)|\leq C(1+|x|)^{N}e^{-a\pi x^{2}}$ and $|{\hat {f}}(\xi )|\leq C(1+|\xi |)^{N}e^{-b\pi \xi ^{2}}$ ( $C>0,N$ an integer),
then, if ab > 1, f = 0 , while if ab = 1 , then there is a polynomial P of degree ≤ N such that $f(x)=P(x)e^{-a\pi x^{2}}.$

This was later improved as follows: if $f\in L^{2}(\mathbb {R} ^{d})$ is such that $\int _{\mathbb {R} ^{d}}\int _{\mathbb {R} ^{d}}|f(x)||{\hat {f}}(\xi )|{\frac {e^{\pi |\langle x,\xi \rangle |}}{(1+|x|+|\xi |)^{N}}}\,dx\,d\xi <+\infty ~,$ then $f(x)=P(x)e^{-\pi \langle Ax,x\rangle }~,$ where P is a polynomial of degree ( N − d )/2 and A is a real d × d positive definite matrix.

This result was stated in Beurling's complete works without proof and proved in Hörmander (the case $d=1,N=0$ ) and Bonami, Demange, and Jaming for the general case. Note that Hörmander–Beurling's version implies the case ab > 1 in Hardy's Theorem while the version by Bonami–Demange–Jaming covers the full strength of Hardy's Theorem. A different proof of Beurling's theorem based on Liouville's theorem appeared in ref.

A full description of the case ab < 1 as well as the following extension to Schwartz class distributions appears in ref.

Theorem — If a tempered distribution $f\in {\mathcal {S}}'(\mathbb {R} ^{d})$ is such that $e^{\pi |x|^{2}}f\in {\mathcal {S}}'(\mathbb {R} ^{d})$ and $e^{\pi |\xi |^{2}}{\hat {f}}\in {\mathcal {S}}'(\mathbb {R} ^{d})~,$ then $f(x)=P(x)e^{-\pi \langle Ax,x\rangle }~,$ for some convenient polynomial P and real positive definite matrix A of type d × d .

## Additional uncertainty relations

### Heisenberg limit

In quantum metrology , and especially interferometry , the Heisenberg limit is the optimal rate at which the accuracy of a measurement can scale with the energy used in the measurement. Typically, this is the measurement of a phase (applied to one arm of a beam-splitter ) and the energy is given by the number of photons used in an interferometer . Although some claim to have broken the Heisenberg limit, this reflects disagreement on the definition of the scaling resource. Suitably defined, the Heisenberg limit is a consequence of the basic principles of quantum mechanics and cannot be beaten, although the weak Heisenberg limit can be beaten.

### Systematic and statistical errors

The inequalities above focus on the statistical imprecision of observables as quantified by the standard deviation $\sigma$ . Heisenberg's original version, however, was dealing with the systematic error , a disturbance of the quantum system produced by the measuring apparatus, i.e., an observer effect.

If we let $\varepsilon _{A}$ represent the error (i.e., inaccuracy ) of a measurement of an observable A and $\eta _{B}$ the disturbance produced on a subsequent measurement of the conjugate variable B by the former measurement of A , then the inequality proposed by Masanao Ozawa − encompassing both systematic and statistical errors - holds:

$\varepsilon _{A}\,\eta _{B}+\varepsilon _{A}\,\sigma _{B}+\sigma _{A}\,\eta _{B}\,\geq \,{\frac {1}{2}}\,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

Heisenberg's uncertainty principle, as originally described in the 1927 formulation, mentions only the first term of Ozawa inequality, regarding the systematic error . Using the notation above to describe the error/disturbance effect of sequential measurements (first A , then B ), it could be written as

$\varepsilon _{A}\,\eta _{B}\,\geq \,{\frac {1}{2}}\,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

The formal derivation of the Heisenberg relation is possible but far from intuitive. It was not proposed by Heisenberg, but formulated in a mathematically consistent way only in recent years. Also, it must be stressed that the Heisenberg formulation is not taking into account the intrinsic statistical errors $\sigma _{A}$ and $\sigma _{B}$ . There is increasing experimental evidence that the total quantum uncertainty cannot be described by the Heisenberg term alone, but requires the presence of all the three terms of the Ozawa inequality.

Using the same formalism, it is also possible to introduce the other kind of physical situation, often confused with the previous one, namely the case of simultaneous measurements ( A and B at the same time):

$\varepsilon _{A}\,\varepsilon _{B}\,\geq \,{\frac {1}{2}}\,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

The two simultaneous measurements on A and B are necessarily unsharp or weak .

It is also possible to derive an uncertainty relation that, as the Ozawa's one, combines both the statistical and systematic error components, but keeps a form very close to the Heisenberg original inequality. By adding Robertson

$\sigma _{A}\,\sigma _{B}\,\geq \,{\frac {1}{2}}\,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

and Ozawa relations we obtain $\varepsilon _{A}\eta _{B}+\varepsilon _{A}\,\sigma _{B}+\sigma _{A}\,\eta _{B}+\sigma _{A}\sigma _{B}\geq \left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|.$ The four terms can be written as: $(\varepsilon _{A}+\sigma _{A})\,(\eta _{B}+\sigma _{B})\,\geq \,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|.$ Defining: ${\bar {\varepsilon }}_{A}\,\equiv \,(\varepsilon _{A}+\sigma _{A})$ as the inaccuracy in the measured values of the variable A and ${\bar {\eta }}_{B}\,\equiv \,(\eta _{B}+\sigma _{B})$ as the resulting fluctuation in the conjugate variable B , Kazuo Fujikawa established an uncertainty relation similar to the Heisenberg original one, but valid both for systematic and statistical errors :

${\bar {\varepsilon }}_{A}\,{\bar {\eta }}_{B}\,\geq \,\left|{\Bigl \langle }{\bigl [}{\hat {A}},{\hat {B}}{\bigr ]}{\Bigr \rangle }\right|$

### Quantum entropic uncertainty principle

For many distributions, the standard deviation is not a particularly natural way of quantifying the structure. For example, uncertainty relations in which one of the observables is an angle has little physical meaning for fluctuations larger than one period. Other examples include highly bimodal distributions , or unimodal distributions with divergent variance.

A solution that overcomes these issues is an uncertainty based on entropic uncertainty instead of the product of variances. While formulating the many-worlds interpretation of quantum mechanics in 1957, Hugh Everett III conjectured a stronger extension of the uncertainty principle based on entropic certainty. This conjecture, also studied by I. I. Hirschman and proven in 1975 by W. Beckner and by Iwo Bialynicki-Birula and Jerzy Mycielski is that, for two normalized, dimensionless Fourier transform pairs f ( a ) and g ( b ) where

$f(a)=\int _{-\infty }^{\infty }g(b)\ e^{2\pi iab}\,db$ and $\,\,\,g(b)=\int _{-\infty }^{\infty }f(a)\ e^{-2\pi iab}\,da$

the Shannon information entropies $H_{a}=-\int _{-\infty }^{\infty }|f(a)|^{2}\log |f(a)|^{2}\,da,$ and $H_{b}=-\int _{-\infty }^{\infty }|g(b)|^{2}\log |g(b)|^{2}\,db$ are subject to the following constraint,

$H_{a}+H_{b}\geq \log(e/2)$

where the logarithms may be in any base.

The probability distribution functions associated with the position wave function ψ ( x ) and the momentum wave function φ ( x ) have dimensions of inverse length and momentum respectively, but the entropies may be rendered dimensionless by $H_{x}=-\int |\psi (x)|^{2}\ln \left(x_{0}\,|\psi (x)|^{2}\right)dx=-\left\langle \ln \left(x_{0}\,\left|\psi (x)\right|^{2}\right)\right\rangle$ $H_{p}=-\int |\varphi (p)|^{2}\ln(p_{0}\,|\varphi (p)|^{2})\,dp=-\left\langle \ln(p_{0}\left|\varphi (p)\right|^{2})\right\rangle$ where x 0 and p 0 are some arbitrarily chosen length and momentum respectively, which render the arguments of the logarithms dimensionless. Note that the entropies will be functions of these chosen parameters. Due to the Fourier transform relation between the position wave function ψ ( x ) and the momentum wavefunction φ ( p ) , the above constraint can be written for the corresponding entropies as

$H_{x}+H_{p}\geq \log \left({\frac {e\,h}{2\,x_{0}\,p_{0}}}\right)$

where h is the Planck constant .

Depending on one's choice of the x 0 p 0 product, the expression may be written in many ways. If x 0 p 0 is chosen to be h , then $H_{x}+H_{p}\geq \log \left({\frac {e}{2}}\right)$

If, instead, x 0 p 0 is chosen to be $\hbar$ , then $H_{x}+H_{p}\geq \log(e\,\pi )$

If x 0 and p 0 are chosen to be unity in whatever system of units are being used, then $H_{x}+H_{p}\geq \log \left({\frac {e\,h}{2}}\right)$ where h is interpreted as a dimensionless number equal to the value of the Planck constant in the chosen system of units. Note that these inequalities can be extended to multimode quantum states, or wavefunctions in more than one spatial dimension.

The quantum entropic uncertainty principle is more restrictive than the Heisenberg uncertainty principle. From the inverse logarithmic Sobolev inequalities $H_{x}\leq {\frac {1}{2}}\log(2e\pi \sigma _{x}^{2}/x_{0}^{2})~,$ $H_{p}\leq {\frac {1}{2}}\log(2e\pi \sigma _{p}^{2}/p_{0}^{2})~,$ (equivalently, from the fact that normal distributions maximize the entropy of all such with a given variance), it readily follows that this entropic uncertainty principle is stronger than the one based on standard deviations , because $\sigma _{x}\sigma _{p}\geq {\frac {\hbar }{2}}\exp \left(H_{x}+H_{p}-\log \left({\frac {e\,h}{2\,x_{0}\,p_{0}}}\right)\right)\geq {\frac {\hbar }{2}}~.$

In other words, the Heisenberg uncertainty principle, is a consequence of the quantum entropic uncertainty principle, but not vice versa. A few remarks on these inequalities. First, the choice of base e is a matter of popular convention in physics. The logarithm can alternatively be in any base, provided that it be consistent on both sides of the inequality. Second, recall the Shannon entropy has been used, not the quantum von Neumann entropy . Finally, the normal distribution saturates the inequality, and it is the only distribution with this property, because it is the maximum entropy probability distribution among those with fixed variance (cf. here for proof).

A measurement apparatus will have a finite resolution set by the discretization of its possible outputs into bins, with the probability of lying within one of the bins given by the Born rule. We will consider the most common experimental situation, in which the bins are of uniform size. Let δx be a measure of the spatial resolution. We take the zeroth bin to be centered near the origin, with possibly some small constant offset c . The probability of lying within the jth interval of width δx is $\operatorname {P} [x_{j}]=\int _{(j-1/2)\delta x-c}^{(j+1/2)\delta x-c}|\psi (x)|^{2}\,dx$

To account for this discretization, we can define the Shannon entropy of the wave function for a given measurement apparatus as $H_{x}=-\sum _{j=-\infty }^{\infty }\operatorname {P} [x_{j}]\ln \operatorname {P} [x_{j}].$

Under the above definition, the entropic uncertainty relation is $H_{x}+H_{p}>\ln \left({\frac {e}{2}}\right)-\ln \left({\frac {\delta x\delta p}{h}}\right).$

Here we note that δx δp / h is a typical infinitesimal phase space volume used in the calculation of a partition function . The inequality is also strict and not saturated. Efforts to improve this bound are an active area of research.

### Uncertainty relation with three angular momentum components

For a particle of total angular momentum $j$ the following uncertainty relation holds $\sigma _{J_{x}}^{2}+\sigma _{J_{y}}^{2}+\sigma _{J_{z}}^{2}\geq j,$ where $J_{l}$ are angular momentum components. The relation can be derived from $\langle J_{x}^{2}+J_{y}^{2}+J_{z}^{2}\rangle =j(j+1),$ and $\langle J_{x}\rangle ^{2}+\langle J_{y}\rangle ^{2}+\langle J_{z}\rangle ^{2}\leq j.$ The relation can be strengthened as $\sigma _{J_{x}}^{2}+\sigma _{J_{y}}^{2}+F_{Q}[\varrho ,J_{z}]/4\geq j,$ where $F_{Q}[\varrho ,J_{z}]$ is the quantum Fisher information.

## History

In 1925 Heisenberg published the Umdeutung (reinterpretation) paper where he showed that central aspect of quantum theory was the non- commutativity : the theory implied that the relative order of position and momentum measurement was significant. Working with Max Born and Pascual Jordan , he continued to develop matrix mechanics , that would become the first modern quantum mechanics formulation.

In March 1926, working in Bohr's institute, Heisenberg realized that the non- commutativity implies the uncertainty principle. Writing to Wolfgang Pauli in February 1927, he worked out the basic concepts.

In his celebrated 1927 paper " Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik " ("On the Perceptual Content of Quantum Theoretical Kinematics and Mechanics"), Heisenberg established this expression as the minimum amount of unavoidable momentum disturbance caused by any position measurement, but he did not give a precise definition for the uncertainties Δx and Δ p . Instead, he gave some plausible estimates in each case separately. His paper gave an analysis in terms of a microscope that Bohr showed was incorrect; Heisenberg included an addendum to the publication.

In his 1930 Chicago lecture he refined his principle:

Later work broadened the concept. Any two variables that do not commute cannot be measured simultaneously—the more precisely one is known, the less precisely the other can be known. Heisenberg wrote:

It can be expressed in its simplest form as follows: One can never know with perfect accuracy both of those two important factors which determine the movement of one of the smallest particles—its position and its velocity. It is impossible to determine accurately both the position and the direction and speed of a particle at the same instant .

Kennard in 1927 first proved the modern inequality:

where ħ = ⁠ h / 2 π ⁠ , and σ x , σ p are the standard deviations of position and momentum. (Heisenberg only proved relation ( A2 ) for the special case of Gaussian states. ) In 1929 Robertson generalized the inequality to all observables and in 1930 Schrödinger extended the form to allow non-zero covariance of the operators; this result is referred to as Robertson-Schrödinger inequality.

### Terminology and translation

Throughout the main body of his original 1927 paper, written in German, Heisenberg used the word "Ungenauigkeit", (Eng: Imprecision)
to describe the basic theoretical principle. Only in the endnote did he switch to the word "Unsicherheit" (Eng: Uncertainty). Later on, he always used "Unbestimmtheit" (Eng: Indefiniteness). When the English-language version of Heisenberg's textbook, The Physical Principles of the Quantum Theory , was published in 1930, however, only the English word "uncertainty" was used, and it became the term in the English language.

### Heisenberg's microscope

The principle is quite counter-intuitive, so the early students of quantum theory had to be reassured that naive measurements to violate it were bound always to be unworkable. One way in which Heisenberg originally illustrated the intrinsic impossibility of violating the uncertainty principle is by using the observer effect of an imaginary microscope as a measuring device.

He imagines an experimenter trying to measure the position and momentum of an electron by shooting a photon at it.

- Problem 1 – If the photon has a short wavelength , and therefore, a large momentum, the position can be measured accurately. But the photon scatters in a random direction, transferring a large and uncertain amount of momentum to the electron. If the photon has a long wavelength and low momentum, the collision does not disturb the electron's momentum very much, but the scattering will reveal its position only vaguely.

- Problem 2 – If a large aperture is used for the microscope, the electron's location can be well resolved (see Rayleigh criterion ); but by the principle of conservation of momentum , the transverse momentum of the incoming photon affects the electron's beamline momentum and hence, the new momentum of the electron resolves poorly. If a small aperture is used, the accuracy of both resolutions is the other way around.

The combination of these trade-offs implies that no matter what photon wavelength and aperture size are used, the product of the uncertainty in measured position and measured momentum is greater than or equal to a lower limit, which is (up to a small numerical factor) equal to the Planck constant . Heisenberg did not care to formulate the uncertainty principle as an exact limit, and preferred to use it instead, as a heuristic quantitative statement, correct up to small numerical factors, which makes the radically new noncommutativity of quantum mechanics inevitable.

### Intrinsic quantum uncertainty

Historically, the uncertainty principle has been confused with a related effect in physics , called the observer effect , which notes that measurements of certain systems cannot be made without affecting the system, that is, without changing something in a system. Heisenberg used such an observer effect at the quantum level (see below) as a physical "explanation" of quantum uncertainty. It has since become clearer, however, that the uncertainty principle is inherent in the properties of all wave-like systems , and that it arises in quantum mechanics simply due to the matter wave nature of all quantum objects. Thus, the uncertainty principle actually states a fundamental property of quantum systems and is not a statement about the observational success of current technology.

## Critical reactions

The Copenhagen interpretation of quantum mechanics and Heisenberg's uncertainty principle were, in fact, initially seen as twin targets by detractors. According to the Copenhagen interpretation of quantum mechanics, there is no fundamental reality that the quantum state describes, just a prescription for calculating experimental results. There is no way to say what the state of a system fundamentally is, only what the result of observations might be.

Albert Einstein believed that randomness is a reflection of our ignorance of some fundamental property of reality, while Niels Bohr believed that the probability distributions are fundamental and irreducible, and depend on which measurements we choose to perform. Einstein and Bohr debated the uncertainty principle for many years.

### Ideal detached observer

Wolfgang Pauli called Einstein's fundamental objection to the uncertainty principle "the ideal of the detached observer" (phrase translated from the German):

"Like the moon has a definite position," Einstein said to me last winter, "whether or not we look at the moon, the same must also hold for the atomic objects, as there is no sharp distinction possible between these and macroscopic objects. Observation cannot create an element of reality like a position, there must be something contained in the complete description of physical reality which corresponds to the possibility of observing a position, already before the observation has been actually made." I hope, that I quoted Einstein correctly; it is always difficult to quote somebody out of memory with whom one does not agree. It is precisely this kind of postulate which I call the ideal of the detached observer.

— Letter from Pauli to Niels Bohr, February 15, 1955

### Einstein's slit

The first of Einstein's thought experiments challenging the uncertainty principle went as follows:

Consider a particle passing through a slit of width d . The slit introduces an uncertainty in momentum of approximately ⁠ h / d ⁠ because the particle passes through the wall. But let us determine the momentum of the particle by measuring the recoil of the wall. In doing so, we find the momentum of the particle to arbitrary accuracy by conservation of momentum.

Bohr's response was that the wall is quantum mechanical as well, and that to measure the recoil to accuracy Δ p , the momentum of the wall must be known to this accuracy before the particle passes through. This introduces an uncertainty in the position of the wall and therefore the position of the slit equal to ⁠ h / Δ p ⁠ , and if the wall's momentum is known precisely enough to measure the recoil, the slit's position is uncertain enough to disallow a position measurement.

A similar analysis with particles diffracting through multiple slits is given by Richard Feynman .

### Einstein's box

Bohr was present when Einstein proposed the thought experiment which has become known as Einstein's box . Einstein argued that "Heisenberg's uncertainty equation implied that the uncertainty in time was related to the uncertainty in energy, the product of the two being related to the Planck constant." Consider, he said, an ideal box, lined with mirrors so that it can contain light indefinitely. The box could be weighed before a clockwork mechanism opened an ideal shutter at a chosen instant to allow one single photon to escape. "We now know, explained Einstein, precisely the time at which the photon left the box." "Now, weigh the box again. The change of mass tells the energy of the emitted light. In this manner, said Einstein, one could measure the energy emitted and the time it was released with any desired precision, in contradiction to the uncertainty principle."

Bohr spent a sleepless night considering this argument, and eventually realized that it was flawed. He pointed out that if the box were to be weighed, say by a spring and a pointer on a scale, "since the box must move vertically with a change in its weight, there will be uncertainty in its vertical velocity and therefore an uncertainty in its height above the table. ... Furthermore, the uncertainty about the elevation above the Earth's surface will result in an uncertainty in the rate of the clock", because of Einstein's own theory of gravity's effect on time . "Through this chain of uncertainties, Bohr showed that Einstein's light box experiment could not simultaneously measure exactly both the energy of the photon and the time of its escape."

### EPR paradox for entangled particles

In 1935, Einstein, Boris Podolsky and Nathan Rosen published an analysis of spatially separated entangled particles (EPR paradox). According to EPR, one could measure the position of one of the entangled particles and the momentum of the second particle, and from those measurements deduce the position and momentum of both particles to any precision, violating the uncertainty principle. In order to avoid such possibility, the measurement of one particle must modify the probability distribution of the other particle instantaneously, possibly violating the principle of locality .

In 1964, John Stewart Bell showed that this assumption can be falsified, since it would imply a certain inequality between the probabilities of different experiments. Experimental results confirm the predictions of quantum mechanics, ruling out EPR's basic assumption of local hidden variables .

### Popper's criticism

Science philosopher Karl Popper approached the problem of indeterminacy as a logician and metaphysical realist . He disagreed with the application of the uncertainty relations to individual particles rather than to ensembles of identically prepared particles, referring to them as "statistical scatter relations". In this statistical interpretation, a particular measurement may be made to arbitrary precision without invalidating the quantum theory.

In 1934, Popper published Zur Kritik der Ungenauigkeitsrelationen ("Critique of the Uncertainty Relations") in Naturwissenschaften , and in the same year Logik der Forschung (translated and updated by the author as The Logic of Scientific Discovery in 1959 ), outlining his arguments for the statistical interpretation. In 1982, he further developed his theory in Quantum theory and the schism in Physics , writing:

[Heisenberg's] formulae are, beyond all doubt, derivable statistical formulae of the quantum theory. But they have been habitually misinterpreted by those quantum theorists who said that these formulae can be interpreted as determining some upper limit to the precision of our measurements . [original emphasis]

Popper proposed an experiment to falsify the uncertainty relations, although he later withdrew his initial version after discussions with Carl Friedrich von Weizsäcker , Heisenberg, and Einstein; Popper sent his paper to Einstein and it may have influenced the formulation of the EPR paradox.

### Free will

Some scientists, including Arthur Compton and Martin Heisenberg , have suggested that the uncertainty principle, or at least the general probabilistic nature of quantum mechanics, could be evidence for the two-stage model of free will. One critique, however, is that apart from the basic role of quantum mechanics as a foundation for chemistry, nontrivial biological mechanisms requiring quantum mechanics are unlikely, due to the rapid decoherence time of quantum systems at room temperature. Proponents of this theory commonly say that this decoherence is overcome by both screening and decoherence-free subspaces found in biological cells.

### Thermodynamics

There is reason to believe that violating the uncertainty principle also strongly implies the violation of the second law of thermodynamics . See Gibbs paradox .

### Rejection of the principle

Uncertainty principles relate quantum particles – electrons for example – to classical concepts – position and momentum. This presumes quantum particles have position and momentum. Edwin C. Kemble pointed out [ clarification needed ] in 1937 that such properties cannot be experimentally verified and assuming they exist gives rise to many contradictions; similarly Rudolf Haag notes that position in quantum mechanics is an attribute of an interaction, say between an electron and a detector, not an intrinsic property. From this point of view the uncertainty principle is not a fundamental quantum property but a concept "carried over from the language of our ancestors", as Kemble says.

## Applications

Since the uncertainty principle is such a basic result in quantum mechanics, typical experiments in quantum mechanics routinely observe aspects of it. All forms of spectroscopy , including particle physics use the relationship to relate measured energy line-width to the lifetime of quantum states. Certain experiments, however, may deliberately test a particular form of the uncertainty principle as part of their main research program. These include, for example, tests of number–phase uncertainty relations in superconducting or quantum optics systems.

Applications dependent on the uncertainty principle for their operation include extremely low-noise technology such as that required in gravitational wave interferometers . Such an interferometer measures distances between mirrors detect gravitational waves . For a mirror of mass $m$ observed for $\tau$ seconds will be limited by quantum uncertainty in an amount $\Delta z_{\textrm {QL}}={\sqrt {2\hbar \tau /m}}.$ For a mirror of mass 1 × 10 5 gm measured over 2 × 10 −3 s will be limited in accuracy to 6 × 10 −18 cm .
