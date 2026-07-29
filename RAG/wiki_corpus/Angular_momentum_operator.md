# Angular momentum operator

> **Query Topic**: Heisenberg uncertainty principle and how does it relate to angular momentum in quantum mechanics (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 17, Frequency: 12)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Angular_momentum_operator

---

In quantum mechanics , the angular momentum operator is one of several related operators analogous to classical angular momentum . The angular momentum operator plays a central role in the theory of atomic and molecular physics and other quantum problems involving rotational symmetry . Being an observable, its eigenfunctions represent the distinguishable physical states of a system's angular momentum, and the corresponding eigenvalues the observable experimental values. When applied to a mathematical representation of the state of a system, yields the same state multiplied by its angular momentum value if the state is an eigenstate (as per the eigenstates/eigenvalues equation). In both classical and quantum mechanical systems, angular momentum (together with linear momentum and energy ) is one of the three fundamental properties of motion.

There are several angular momentum operators: total angular momentum (usually denoted J ), orbital angular momentum (usually denoted L ), and spin angular momentum ( spin for short, usually denoted S ). The term angular momentum operator can (confusingly) refer to either the total or the orbital angular momentum. Total angular momentum is always conserved , see Noether's theorem .

## Overview

In quantum mechanics, angular momentum can refer to one of three different, but related things.

### Orbital angular momentum

The classical definition of angular momentum is $\mathbf {L} =\mathbf {r} \times \mathbf {p}$ . The quantum-mechanical counterparts of these objects share the same relationship: $\mathbf {L} =\mathbf {r} \times \mathbf {p}$ where r is the quantum position operator , p is the quantum momentum operator , × is cross product , and L is the orbital angular momentum operator . L (just like p and r ) is a vector operator (a vector whose components are operators), i.e. $\mathbf {L} =\left(L_{x},L_{y},L_{z}\right)$ where L x , L y , L z are three different quantum-mechanical operators.

In the special case of a single particle with no electric charge and no spin , the orbital angular momentum operator can be written in the position basis as: $\mathbf {L} =-i\hbar (\mathbf {r} \times \nabla )$ where ∇ is the vector differential operator, del .

### Spin angular momentum

There is another type of angular momentum, called spin angular momentum (more often shortened to spin ), represented by the spin operator $\mathbf {S} =\left(S_{x},S_{y},S_{z}\right)$ . Spin is often depicted as a particle literally spinning around an axis, but this is only a metaphor: the closest classical analog is based on wave circulation. All elementary particles have a characteristic spin ( scalar bosons have zero spin). For example, electrons always have "spin 1/2" while photons always have "spin 1" (details below ).

### Total angular momentum

Finally, there is total angular momentum $\mathbf {J} =\left(J_{x},J_{y},J_{z}\right)$ , which combines both the spin and orbital angular momentum of a particle or system: $\mathbf {J} =\mathbf {L} +\mathbf {S} .$

Conservation of angular momentum states that J for a closed system, or J for the whole universe, is conserved. However, L and S are not generally conserved. For example, the spin–orbit interaction allows angular momentum to transfer back and forth between L and S , with the total J remaining constant.

## Commutation relations

### Commutation relations between components

The orbital angular momentum operator is a vector operator, meaning it can be written in terms of its vector components $\mathbf {L} =\left(L_{x},L_{y},L_{z}\right)$ . The components have the following commutation relations with each other: $\left[L_{x},L_{y}\right]=i\hbar L_{z},\;\;\left[L_{y},L_{z}\right]=i\hbar L_{x},\;\;\left[L_{z},L_{x}\right]=i\hbar L_{y},$

where [ , ] denotes the commutator $[X,Y]\equiv XY-YX.$

This can be written as $\left[L_{l},L_{m}\right]=i\hbar \sum _{n=1}^{3}\varepsilon _{lmn}L_{n},$ where l , m , n are the component indices (1 for x , 2 for y , 3 for z ), and ε lmn denotes the Levi-Civita symbol . Alternatively Einstein's summation convention can be used to write this as: [ citation needed ] $\left[L_{l},L_{m}\right]=i\hbar \varepsilon _{lmn}L_{n}.$

A compact expression as one vector equation is also possible: $\mathbf {L} \times \mathbf {L} =i\hbar \mathbf {L}$

The commutation relations can be proved as a direct consequence of the canonical commutation relations $[x_{l},p_{m}]=i\hbar \delta _{lm}$ , where δ lm is the Kronecker delta .

There is an analogous relationship in classical physics: $\left\{L_{i},L_{j}\right\}=\varepsilon _{ijk}L_{k}$ where L n is a component of the classical angular momentum operator, and $\{,\}$ is the Poisson bracket .

The same commutation relations apply for the other angular momentum operators (spin and total angular momentum): $\left[S_{l},S_{m}\right]=i\hbar \sum _{n=1}^{3}\varepsilon _{lmn}S_{n},\quad \left[J_{l},J_{m}\right]=i\hbar \sum _{n=1}^{3}\varepsilon _{lmn}J_{n}.$

These can be assumed to hold in analogy with L . Alternatively, they can be derived as discussed below .

These commutation relations mean that L has the mathematical structure of a Lie algebra , and the ε lmn are its structure constants . In this case, the Lie algebra is SU(2) or SO(3) in physics notation ( $\operatorname {su} (2)$ or $\operatorname {so} (3)$ respectively in mathematics notation), i.e. Lie algebra associated with rotations in three dimensions. The same is true of J and S . The reason is discussed below . These commutation relations are relevant for measurement and uncertainty, as discussed further below.

In molecules the total angular momentum F is the sum of the rovibronic (orbital) angular momentum N , the electron spin angular momentum S , and the nuclear spin angular momentum I . For electronic singlet states the rovibronic angular momentum is denoted J rather than N . As explained by Van Vleck, the components of the molecular rovibronic angular momentum referred to molecule-fixed axes have different commutation relations from those given above which are for the components about space-fixed axes.

### Commutation relations involving vector magnitude

Like any vector, the square of a magnitude can be defined for the orbital angular momentum operator, $L^{2}\equiv L_{x}^{2}+L_{y}^{2}+L_{z}^{2}.$

$L^{2}$ is another quantum operator . It commutes with the components of $\mathbf {L}$ , $\left[L^{2},L_{x}\right]=\left[L^{2},L_{y}\right]=\left[L^{2},L_{z}\right]=0.$

One way to prove that these operators commute is to start from the [ L ℓ , L m ] commutation relations in the previous section:

${\begin{aligned}\left[L^{2},L_{x}\right]&=\left[L_{x}^{2},L_{x}\right]+\left[L_{y}^{2},L_{x}\right]+\left[L_{z}^{2},L_{x}\right]\\&=L_{y}\left[L_{y},L_{x}\right]+\left[L_{y},L_{x}\right]L_{y}+L_{z}\left[L_{z},L_{x}\right]+\left[L_{z},L_{x}\right]L_{z}\\&=L_{y}\left(-i\hbar L_{z}\right)+\left(-i\hbar L_{z}\right)L_{y}+L_{z}\left(i\hbar L_{y}\right)+\left(i\hbar L_{y}\right)L_{z}\\&=0\end{aligned}}$

Mathematically, $L^{2}$ is a Casimir invariant of the Lie algebra SO(3) spanned by $\mathbf {L}$ .

As above, there is an analogous relationship in classical physics: $\left\{L^{2},L_{x}\right\}=\left\{L^{2},L_{y}\right\}=\left\{L^{2},L_{z}\right\}=0$ where $L_{i}$ is a component of the classical angular momentum operator, and $\{,\}$ is the Poisson bracket .

Returning to the quantum case, the same commutation relations apply to the other angular momentum operators (spin and total angular momentum), as well, ${\begin{aligned}\left[S^{2},S_{i}\right]&=0,\\\left[J^{2},J_{i}\right]&=0.\end{aligned}}$

### Uncertainty principle

In general, in quantum mechanics, when two observable operators do not commute, they are called complementary observables . Two complementary observables cannot be measured simultaneously; instead they satisfy an uncertainty principle . The more accurately one observable is known, the less accurately the other one can be known. Just as there is an uncertainty principle relating position and momentum, there are uncertainty principles for angular momentum.

The Robertson–Schrödinger relation gives the following uncertainty principle: $\sigma _{L_{x}}\sigma _{L_{y}}\geq {\frac {\hbar }{2}}\left|\langle L_{z}\rangle \right|.$ where $\sigma _{X}$ is the standard deviation in the measured values of X and $\langle X\rangle$ denotes the expectation value of X . This inequality is also true if x, y, z are rearranged, or if L is replaced by J or S .

Therefore, two orthogonal components of angular momentum (for example L x and L y ) are complementary and cannot be simultaneously known or measured, except in special cases such as $L_{x}=L_{y}=L_{z}=0$ .

It is, however, possible to simultaneously measure or specify L 2 and any one component of L ; for example, L 2 and L z . This is often useful, and the values are characterized by the azimuthal quantum number ( l ) and the magnetic quantum number ( m ). In this case the quantum state of the system is a simultaneous eigenstate of the operators L 2 and L z , but not of L x or L y . The eigenvalues are related to l and m , as shown in the table below.

## Quantization

In quantum mechanics , angular momentum is quantized – that is, it cannot vary continuously, but only in "quantum leaps" between certain allowed values. For any system, the following restrictions on measurement results apply, where $\hbar$ is reduced Planck constant :

### Derivation using ladder operators

A common way to derive the quantization rules above is the method of ladder operators . The ladder operators for the total angular momentum $\mathbf {J} =\left(J_{x},J_{y},J_{z}\right)$ are defined as: ${\begin{aligned}J_{+}&\equiv J_{x}+iJ_{y},\\J_{-}&\equiv J_{x}-iJ_{y}\end{aligned}}$

Suppose $|\psi \rangle$ is a simultaneous eigenstate of $J^{2}$ and $J_{z}$ (i.e., a state with a definite value for $J^{2}$ and a definite value for $J_{z}$ ). Then using the commutation relations for the components of $\mathbf {J}$ , one can prove that each of the states $J_{+}|\psi \rangle$ and $J_{-}|\psi \rangle$ is either zero or a simultaneous eigenstate of $J^{2}$ and $J_{z}$ , with the same value as $|\psi \rangle$ for $J^{2}$ but with values for $J_{z}$ that are increased or decreased by $\hbar$ respectively. The result is zero when the use of a ladder operator would otherwise result in a state with a value for $J_{z}$ that is outside the allowable range. Using the ladder operators in this way, the possible values and quantum numbers for $J^{2}$ and $J_{z}$ can be found.

Let $\psi ({J^{2}}'J_{z}')$ be a state function for the system with eigenvalue ${J^{2}}'$ for $J^{2}$ and eigenvalue $J_{z}'$ for $J_{z}$ .

From $J^{2}=J_{x}^{2}+J_{y}^{2}+J_{z}^{2}$ is obtained, $J_{x}^{2}+J_{y}^{2}=J^{2}-J_{z}^{2}.$ Applying both sides of the above equation to $\psi ({J^{2}}'J_{z}')$ , $(J_{x}^{2}+J_{y}^{2})\;\psi ({J^{2}}'J_{z}')=({J^{2}}'-J_{z}'^{2})\;\psi ({J^{2}}'J_{z}').$ Since $J_{x}$ and $J_{y}$ are real observables, ${J^{2}}'-J_{z}'^{2}$ is not negative and ${\textstyle |J_{z}'|\leq {\sqrt {{J^{2}}'}}}$ . Thus $J_{z}'$ has an upper and lower bound.

Two of the commutation relations for the components of $\mathbf {J}$ are, $[J_{y},J_{z}]=i\hbar J_{x},\;\;[J_{z},J_{x}]=i\hbar J_{y}.$ They can be combined to obtain two equations, which are written together using $\pm$ signs in the following, $J_{z}(J_{x}\pm iJ_{y})=(J_{x}\pm iJ_{y})(J_{z}\pm \hbar ),$ where one of the equations uses the $+$ signs and the other uses the $-$ signs.
Applying both sides of the above to $\psi ({J^{2}}'J_{z}')$ , ${\begin{aligned}J_{z}(J_{x}\pm iJ_{y})\;\psi ({J^{2}}'J_{z}')&=(J_{x}\pm iJ_{y})(J_{z}\pm \hbar )\;\psi ({J^{2}}'J_{z}')\\&=(J_{z}'\pm \hbar )(J_{x}\pm iJ_{y})\;\psi ({J^{2}}'J_{z}')\;.\\\end{aligned}}$ The above shows that $(J_{x}\pm iJ_{y})\;\psi ({J^{2}}'J_{z}')$ are two eigenfunctions of $J_{z}$ with respective eigenvalues ${J_{z}}'\pm \hbar$ , unless one of the functions is zero, in which case it is not an eigenfunction. For the functions that are not zero, $\psi ({J^{2}}'J_{z}'\pm \hbar )=(J_{x}\pm iJ_{y})\;\psi ({J^{2}}'J_{z}').$ Further eigenfunctions of $J_{z}$ and corresponding eigenvalues can be found by repeatedly applying $J_{x}\pm iJ_{y}$ as long as the magnitude of the resulting eigenvalue is $\leq {\sqrt {{J^{2}}'}}$ .
Since the eigenvalues of $J_{z}$ are bounded, let $J_{z}^{0}$ be the lowest eigenvalue and $J_{z}^{1}$ be the highest. Then $(J_{x}-iJ_{y})\;\psi ({J^{2}}'J_{z}^{0})=0$ and $(J_{x}+iJ_{y})\;\psi ({J^{2}}'J_{z}^{1})=0,$ since there are no states where the eigenvalue of $J_{z}$ is $<J_{z}^{0}$ or $>J_{z}^{1}$ . By applying $(J_{x}+iJ_{y})$ to the first equation, $(J_{x}-iJ_{y})$ to the second, using $J_{x}^{2}+J_{y}^{2}=J^{2}-J_{z}^{2}$ , and using also $J_{+}J_{-}=J_{x}^{2}+J_{y}^{2}-i[J_{x},J_{y}]=J_{x}^{2}+J_{y}^{2}+J_{z}$ , it can be shown that ${J^{2}}'-(J_{z}^{0})^{2}+\hbar J_{z}^{0}=0$ and ${J^{2}}'-(J_{z}^{1})^{2}-\hbar J_{z}^{1}=0.$ Subtracting the first equation from the second and rearranging, $(J_{z}^{1}+J_{z}^{0})(J_{z}^{0}-J_{z}^{1}-\hbar )=0.$ Since $J_{z}^{1}\geq J_{z}^{0}$ , the second factor is negative. Then the first factor must be zero and thus $J_{z}^{0}=-J_{z}^{1}$ .

The difference $J_{z}^{1}-J_{z}^{0}$ comes from successive application of $J_{x}-iJ_{y}$ or $J_{x}+iJ_{y}$ which lower or raise the eigenvalue of $J_{z}$ by $\hbar$ so that, $J_{z}^{1}-J_{z}^{0}=0,\hbar ,2\hbar ,\dots$ Let $J_{z}^{1}-J_{z}^{0}=2j\hbar ,$ where $j=0,{\tfrac {1}{2}},1,{\tfrac {3}{2}},\dots \;.$ Then using $J_{z}^{0}=-J_{z}^{1}$ and the above, $J_{z}^{0}=-j\hbar$ and $J_{z}^{1}=j\hbar ,$ and the allowable eigenvalues of $J_{z}$ are $J_{z}'=-j\hbar ,-j\hbar +\hbar ,-j\hbar +2\hbar ,\dots ,j\hbar .$ Expressing $J_{z}'$ in terms of a quantum number $m_{j}\;$ , and substituting $J_{z}^{0}=-j\hbar$ into ${J^{2}}'-(J_{z}^{0})^{2}+\hbar J_{z}^{0}=0$ from above,

${\begin{aligned}J_{z}'&=m_{j}\hbar &m_{j}&=-j,-j+1,-j+2,\dots ,j\\{J^{2}}'&=j(j+1)\hbar ^{2}&j&=0,{\tfrac {1}{2}},1,{\tfrac {3}{2}},\dots \;.\end{aligned}}$

Since $\mathbf {S}$ and $\mathbf {L}$ have the same commutation relations as $\mathbf {J}$ , the same ladder analysis can be applied to them, except that for $\mathbf {L}$ there is a further restriction on the quantum numbers that they must be integers.

In the Schroedinger representation, the z component of the orbital angular momentum operator can be expressed in spherical coordinates as, $L_{z}=-i\hbar {\frac {\partial }{\partial \phi }}.$ For $L_{z}$ and eigenfunction $\psi$ with eigenvalue $L_{z}'$ , $-i\hbar {\frac {\partial }{\partial \phi }}\psi =L_{z}'\psi .$ Solving for $\psi$ , $\psi =Ae^{iL_{z}'\phi /\hbar },$ where $A$ is independent of $\phi$ . Since $\psi$ is required to be single valued, and adding $2\pi$ to $\phi$ results in a coordinate for the same point in space, ${\begin{aligned}Ae^{iL_{z}'(\phi +2\pi )/\hbar }&=Ae^{iL_{z}'\phi /\hbar },\\e^{iL_{z}'2\pi /\hbar }&=1.\end{aligned}}$ Solving for the eigenvalue $L_{z}'$ , $L_{z}'=m_{l}\hbar \;,$ where $m_{l}$ is an integer. From the above and the relation $m_{\ell }=-\ell ,(-\ell +1),\ldots ,(\ell -1),\ell \ \$ , it follows that $\ell$ is also an integer. This shows that the quantum numbers $m_{\ell }$ and $\ell$ for the orbital angular momentum $\mathbf {L}$ are restricted to integers, unlike the quantum numbers for the total angular momentum $\mathbf {J}$ and spin $\mathbf {S}$ , which can have half-integer values.

### Visual interpretation

Since the angular momenta are quantum operators, they cannot be drawn as vectors like in classical mechanics. Nevertheless, it is common to depict them heuristically in this way. Depicted on the right is a set of states with quantum numbers $\ell =2$ , and $m_{\ell }=-2,-1,0,1,2$ for the five cones from bottom to top. Since $|L|={\sqrt {L^{2}}}=\hbar {\sqrt {6}}$ , the vectors are all shown with length $\hbar {\sqrt {6}}$ . The rings represent the fact that $L_{z}$ is known with certainty, but $L_{x}$ and $L_{y}$ are unknown; therefore every classical vector with the appropriate length and z -component is drawn, forming a cone. The expected value of the angular momentum for a given ensemble of systems in the quantum state characterized by $\ell$ and $m_{\ell }$ could be somewhere on this cone while it cannot be defined for a single system (since the components of $L$ do not commute with each other).

### Quantization in macroscopic systems

The quantization rules are widely thought to be true even for macroscopic systems, like the angular momentum L of a spinning tire. However they have no observable effect so this has not been tested. For example, if $L_{z}/\hbar$ is roughly 100000000, it makes essentially no difference whether the precise value is an integer like 100000000 or 100000001, or a non-integer like 100000000.2—the discrete steps are currently too small to measure. For most intents and purposes, the assortment of all the possible values of angular momentum is effectively continuous at macroscopic scales.

## Angular momentum as the generator of rotations

The most general and fundamental definition of angular momentum is as the generator of rotations. More specifically, let $R({\hat {n}},\phi )$ be a rotation operator , which rotates any quantum state about axis ${\hat {n}}$ by angle $\phi$ . As $\phi \rightarrow 0$ , the operator $R({\hat {n}},\phi )$ approaches the identity operator , because a rotation of 0° maps all states to themselves. Then the angular momentum operator $J_{\hat {n}}$ about axis ${\hat {n}}$ is defined as: $J_{\hat {n}}\equiv i\hbar \lim _{\phi \rightarrow 0}{\frac {R\left({\hat {n}},\phi \right)-1}{\phi }}=\left.i\hbar {\frac {\partial R\left({\hat {n}},\phi \right)}{\partial \phi }}\right|_{\phi =0}$

where 1 is the identity operator . Also notice that R is an additive morphism : $R\left({\hat {n}},\phi _{1}+\phi _{2}\right)=R\left({\hat {n}},\phi _{1}\right)R\left({\hat {n}},\phi _{2}\right)$ ; as a consequence $R\left({\hat {n}},\phi \right)=\exp \left(-{\frac {i\phi J_{\hat {n}}}{\hbar }}\right)$ where exp is matrix exponential . The existence of the generator is guaranteed by the Stone's theorem on one-parameter unitary groups .

In simpler terms, the total angular momentum operator characterizes how a quantum system is changed when it is rotated. The relationship between angular momentum operators and rotation operators is the same as the relationship between Lie algebras and Lie groups in mathematics, as discussed further below.

Just as J is the generator for rotation operators , L and S are generators for modified partial rotation operators. The operator $R_{\text{spatial}}\left({\hat {n}},\phi \right)=\exp \left(-{\frac {i\phi L_{\hat {n}}}{\hbar }}\right),$ rotates the position (in space) of all particles and fields, without rotating the internal (spin) state of any particle. Likewise, the operator $R_{\text{internal}}\left({\hat {n}},\phi \right)=\exp \left(-{\frac {i\phi S_{\hat {n}}}{\hbar }}\right),$ rotates the internal (spin) state of all particles, without moving any particles or fields in space. The relation J = L + S comes from: $R\left({\hat {n}},\phi \right)=R_{\text{internal}}\left({\hat {n}},\phi \right)R_{\text{spatial}}\left({\hat {n}},\phi \right)$

i.e. if the positions are rotated, and then the internal states are rotated, then altogether the complete system has been rotated.

### SU(2), SO(3), and 360° rotations

Although one might expect $R\left({\hat {n}},360^{\circ }\right)=1$ (a rotation of 360° is the identity operator), this is not assumed in quantum mechanics, and it turns out it is often not true: When the total angular momentum quantum number is a half-integer (1/2, 3/2, etc.), $R\left({\hat {n}},360^{\circ }\right)=-1$ , and when it is an integer, $R\left({\hat {n}},360^{\circ }\right)=+1$ . Mathematically, the structure of rotations in the universe is not SO(3) , the group of three-dimensional rotations in classical mechanics. Instead, it is SU(2) , which is identical to SO(3) for small rotations, but where a 360° rotation is mathematically distinguished from a rotation of 0°. (A rotation of 720° is, however, the same as a rotation of 0°.)

On the other hand, $R_{\text{spatial}}\left({\hat {n}},360^{\circ }\right)=+1$ in all circumstances, because a 360° rotation of a spatial configuration is the same as no rotation at all. (This is different from a 360° rotation of the internal (spin) state of the particle, which might or might not be the same as no rotation at all.) In other words, the $R_{\text{spatial}}$ operators carry the structure of SO(3) , while $R$ and $R_{\text{internal}}$ carry the structure of SU(2) .

From the equation $+1=R_{\text{spatial}}\left({\hat {z}},360^{\circ }\right)=\exp \left(-2\pi iL_{z}/\hbar \right)$ , one picks an eigenstate $L_{z}|\psi \rangle =m\hbar |\psi \rangle$ and draws $e^{-2\pi im}=1$ which is to say that the orbital angular momentum quantum numbers can only be integers, not half-integers.

### Connection to representation theory

Starting with a certain quantum state $|\psi _{0}\rangle$ , consider the set of states $R\left({\hat {n}},\phi \right)\left|\psi _{0}\right\rangle$ for all possible ${\hat {n}}$ and $\phi$ , i.e. the set of states that come about from rotating the starting state in every possible way. The linear span of that set is a vector space , and therefore the manner in which the rotation operators map one state onto another is a representation of the group of rotation operators.

From the relation between J and rotation operators,

(The Lie algebras of SU(2) and SO(3) are identical.)

The ladder operator derivation above is a method for classifying the representations of the Lie algebra SU(2).

### Connection to commutation relations

Classical rotations do not commute with each other: For example, rotating 1° about the x -axis then 1° about the y -axis gives a slightly different overall rotation than rotating 1° about the y -axis then 1° about the x -axis. By carefully analyzing this noncommutativity, the commutation relations of the angular momentum operators can be derived.

(This same calculational procedure is one way to answer the mathematical question "What is the Lie algebra of the Lie groups SO(3) or SU(2) ?")

## Conservation of angular momentum

The Hamiltonian H represents the energy and dynamics of the system. In a spherically symmetric situation, the Hamiltonian is invariant under rotations: $RHR^{-1}=H$ where R is a rotation operator . As a consequence, $[H,R]=0$ , and then $[H,\mathbf {J} ]=\mathbf {0}$ due to the relationship between J and R . By the Ehrenfest theorem , it follows that J is conserved.

To summarize, if H is rotationally-invariant (The Hamiltonian function defined on an inner product space is said to have rotational invariance if its value does not change when arbitrary rotations are applied to its coordinates.), then total angular momentum J is conserved. This is an example of Noether's theorem .

If H is just the Hamiltonian for one particle, the total angular momentum of that one particle is conserved when the particle is in a central potential (i.e., when the potential energy function depends only on $\left|\mathbf {r} \right|$ ). Alternatively, H may be the Hamiltonian of all particles and fields in the universe, and then H is always rotationally-invariant, as the fundamental laws of physics of the universe are the same regardless of orientation. This is the basis for saying conservation of angular momentum is a general principle of physics.

For a particle without spin, J = L , so orbital angular momentum is conserved in the same circumstances. When the spin is nonzero, the spin–orbit interaction allows angular momentum to transfer from L to S or back. Therefore, L is not, on its own, conserved.

## Angular momentum coupling

Often, two or more sorts of angular momentum interact with each other, so that angular momentum can transfer from one to the other. For example, in spin–orbit coupling , angular momentum can transfer between L and S , but only the total J = L + S is conserved. In another example, in an atom with two electrons, each has its own angular momentum J 1 and J 2 , but only the total J = J 1 + J 2 is conserved.

In these situations, it is often useful to know the relationship between, on the one hand, states where $\left(J_{1}\right)_{z},\left(J_{1}\right)^{2},\left(J_{2}\right)_{z},\left(J_{2}\right)^{2}$ all have definite values, and on the other hand, states where $\left(J_{1}\right)^{2},\left(J_{2}\right)^{2},J^{2},J_{z}$ all have definite values, as the latter four are usually conserved (constants of motion). The procedure to go back and forth between these bases is to use Clebsch–Gordan coefficients .

One important result in this field is that a relationship between the quantum numbers for $\left(J_{1}\right)^{2},\left(J_{2}\right)^{2},J^{2}$ : $j\in \left\{\left|j_{1}-j_{2}\right|,\left(\left|j_{1}-j_{2}\right|+1\right),\ldots ,\left(j_{1}+j_{2}\right)\right\}.$

For an atom or molecule with J = L + S , the term symbol gives the quantum numbers associated with the operators $L^{2},S^{2},J^{2}$ .

## Orbital angular momentum in spherical coordinates

Angular momentum operators usually occur when solving a problem with spherical symmetry in spherical coordinates . The angular momentum in the spatial representation is ${\begin{aligned}\mathbf {L} &=i\hbar \left({\frac {\hat {\boldsymbol {\theta }}}{\sin(\theta )}}{\frac {\partial }{\partial \phi }}-{\hat {\boldsymbol {\phi }}}{\frac {\partial }{\partial \theta }}\right)\\&=i\hbar \left({\hat {\mathbf {x} }}\left(\sin(\phi ){\frac {\partial }{\partial \theta }}+\cot(\theta )\cos(\phi ){\frac {\partial }{\partial \phi }}\right)+{\hat {\mathbf {y} }}\left(-\cos(\phi ){\frac {\partial }{\partial \theta }}+\cot(\theta )\sin(\phi ){\frac {\partial }{\partial \phi }}\right)-{\hat {\mathbf {z} }}{\frac {\partial }{\partial \phi }}\right)\\L_{+}&=\hbar e^{i\phi }\left({\frac {\partial }{\partial \theta }}+i\cot(\theta ){\frac {\partial }{\partial \phi }}\right),\\L_{-}&=\hbar e^{-i\phi }\left(-{\frac {\partial }{\partial \theta }}+i\cot(\theta ){\frac {\partial }{\partial \phi }}\right),\\L^{2}&=-\hbar ^{2}\left({\frac {1}{\sin(\theta )}}{\frac {\partial }{\partial \theta }}\left(\sin(\theta ){\frac {\partial }{\partial \theta }}\right)+{\frac {1}{\sin ^{2}(\theta )}}{\frac {\partial ^{2}}{\partial \phi ^{2}}}\right),\\L_{z}&=-i\hbar {\frac {\partial }{\partial \phi }}.\end{aligned}}$

In spherical coordinates the angular part of the Laplace operator can be expressed by the angular momentum. This leads to the relation $\Delta ={\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}\,{\frac {\partial }{\partial r}}\right)-{\frac {L^{2}}{\hbar ^{2}r^{2}}}.$

When solving to find eigenstates of the operator $L^{2}$ , we obtain the following ${\begin{aligned}L^{2}\left|\ell ,m\right\rangle &=\hbar ^{2}\ell (\ell +1)\left|\ell ,m\right\rangle \\L_{z}\left|\ell ,m\right\rangle &=\hbar m\left|\ell ,m\right\rangle \end{aligned}}$ where $\left\langle \theta ,\phi |\ell ,m\right\rangle =Y_{\ell ,m}(\theta ,\phi )$ are the spherical harmonics .
