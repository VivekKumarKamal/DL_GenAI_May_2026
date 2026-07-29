# Symmetry of diatomic molecules

> **Query Topic**: permutation-inversion groups (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 360, Frequency: 17)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Symmetry_of_diatomic_molecules

---

Molecular symmetry in physics and chemistry describes the symmetry present in molecules and the classification of molecules according to their symmetry. Molecular symmetry is a fundamental concept in the application of quantum mechanics in physics and chemistry, for example, it can be used to predict or explain many of a molecule's properties, such as its dipole moment and its allowed spectroscopic transitions (based on selection rules ), without doing the exact rigorous calculations (which, in some cases, may not even be possible). To do this it is necessary to classify the states of the molecule using the irreducible representations from the character table of the symmetry group of the molecule. Among all the molecular symmetries, diatomic molecules show some distinct features and are relatively easier to analyze.

## Symmetry and group theory

The physical laws governing a system is generally written as a relation (equations, differential equations, integral equations etc.). An operation on the ingredients of this relation, which keeps the form of the relations invariant is called a symmetry transformation or a symmetry of the system.

- These symmetry operations can involve external or internal co-ordinates; giving rise to geometrical or internal symmetries.

- These symmetry operations can be global or local; giving rise to global or gauge symmetries.

- These symmetry operations can be discrete or continuous.

Symmetry is a fundamentally important concept in quantum mechanics. It can predict conserved quantities and provide quantum numbers. It can predict degeneracies of eigenstates and gives insights about the matrix elements of the Hamiltonian without calculating them. Rather than looking into individual symmetries, it is sometimes more convenient to look into the general relations between the symmetries. It turns out that Group theory is the most efficient way of doing this.

### Groups

A group is a mathematical structure (usually denoted in the form ( G ,*)) consisting of a set G and a binary operation $'*'$ (sometimes loosely called 'multiplication'), satisfying the following properties:

- closure : For every pair of elements $x,y\in G$ , the product $x*y\in G$ .

- associativity : For every x and y and z in G , both ( x * y )* z and x *( y * z ) result with the same element in G (in symbols, $(x*y)*z=x*(y*z)\forall x,y,z\in G$ ).

- existence of identity : There must be an element (say e ) in G such that product any element of G with e make no change to the element (in symbols, $x*e=e*x=x;\forall x\in G$ ).

- existence of inverse : For each element ( x ) in G , there must be an element y in G such that product of x and y is the identity element e (in symbols, for each $x\in G$ ${\text{ }}\exists {\text{ }}y\in G$ such that $x*y=y*x=e$ ).

- In addition to the above four, if it so happens that $\forall x,y\in G$ , $x*y=y*x$ , i.e., the operation in commutative, then the group is called an abelian group . Otherwise it is called a non-abelian group .

### Groups, symmetry and conservation

The set of all symmetry transformations of a Hamiltonian has the structure of a group, with group multiplication equivalent to applying the transformations one after the other. The group elements can be represented as matrices, so that the group operation becomes the ordinary matrix multiplication. In quantum mechanics, the evolution of an arbitrary superposition of states are given by unitary operators, so each of the elements of the symmetry groups are unitary operators. Now any unitary operator can be expressed as the exponential of some Hermitian operator . So, the corresponding Hermitian operators are the ' generators ' of the symmetry group . These unitary transformations act on the Hamiltonian operator in some Hilbert space in a way that the Hamiltonian remains invariant under the transformations. In other words, the symmetry operators commute with the Hamiltonian. If $U$ represents the unitary symmetry operator and acts on the Hamiltonian $H$ , then;

These operators have the above-mentioned properties of a group:

- The symmetry operations are closed under multiplication.

- Application of symmetry transformations are associative.

- There is always a trivial transformation, where nothing is done to the original co-ordinates. This is the identity element of the group.

- And as long as an inverse transformation exists, it is a symmetry transformation, i.e. it leaves the Hamiltonian invariant. Thus the inverse is part of this set.

So, by the symmetry of a system, we mean a set of operators, each of which commutes with the Hamiltonian, and they form a symmetry group . This group may be abelian or non-abelian. Depending upon which one it is, the properties of the system changes (for example, if the group is abelian, there would be no degeneracy ). Corresponding to every different kind of symmetry in a system, we can find a symmetry group associated with it.

It follows that the generator $T$ of the symmetry group also commutes with the Hamiltonian. Now, it follows that:

Some specific examples can be systems having rotational , translational invariance etc. For a rotationally invariant system, the symmetry group of the Hamiltonian is the general rotation group. Now, if (say) the system is invariant about any rotation about Z-axis (i.e., the system has axial symmetry ), then the symmetry group of the Hamiltonian is the group of rotation about the symmetry axis. Now, this group is generated by the Z-component of the orbital angular momentum, ${L}_{z}$ (general group element $R(\alpha )={{e}^{\frac {-i\alpha {{L}_{z}}}{\hbar }}}$ ). Thus, ${L}_{z}$ commutes with $H$ for this system and Z-component of the angular momentum is conserved. Similarly, translation symmetry gives rise to conservation of linear momentum, inversion symmetry gives rise to parity conservation and so on.

## Geometrical symmetries

### Symmetry operations, point groups and permutation-inversion groups

A molecule at equilibrium in a certain electronic state usually has some geometrical symmetry. This symmetry is described by a certain point group which consists of operations (called symmetry operations) that produce a spatial orientation of the molecule that is indistinguishable from the starting configuration. There are five types of point group symmetry operation : identity, rotation, reflection, inversion and improper rotation or rotation-reflection. Common to all symmetry operations is that the geometrical center-point of the molecule does not change its position; hence the name point group . One can determine the elements of the point group for a particular molecule by considering the geometrical symmetry of its molecular model. However, when one uses a point group, the elements are not to be interpreted in the same way. Instead the elements rotate and/or reflect the vibronic (vibration-electronic) coordinates and these elements commute with the vibronic Hamiltonian. The point group is used to classify by symmetry the vibronic eigenstates. The symmetry classification of the rotational levels, the eigenstates of the full (rovibronic nuclear spin) Hamiltonian, requires the use of the appropriate permutation-inversion group as introduced by Longuet-Higgins . See the Section Inversion symmetry and nuclear permutation symmetry below. The elements of permutation-inversion groups commute with the full molecular Hamiltonian . In addition to point groups, there exists another kind of group important in crystallography , where translation in 3-D also needs to be taken care of. They are known as space groups .

### Basic point group symmetry operations

The five basic symmetry operations mentioned above are:

- Identity operation E (from German Einheit , meaning "unity") leaves the molecule unchanged. It forms the identity element in the symmetry group. Though its inclusion seems to be trivial, it is important also because even for the most asymmetric molecule, this symmetry is present. The corresponding symmetry element is the entire molecule itself.

- Inversion i inverts the molecule about its center of inversion (if it has any). The center of inversion is the symmetry element in this case. There may or may not be an atom at this center. A molecule may or may not have a center of inversion. For example, the benzene molecule, a cube, and spheres do have a center of inversion, whereas a tetrahedron does not.

- Reflection σ produces a mirror image geometry of the molecule about a certain plane. The mirror plane bisects the molecule and must include its center of geometry. The plane of symmetry is the symmetry element in this case. A symmetry plane parallel to the principal axis (defined below) is called vertical ( σ v ), and one perpendicular to it – horizontal ( σ h ). A third type of symmetry plane exists: If a vertical symmetry plane additionally bisects the angle between two 2-fold rotation axes perpendicular to the principal axis, the plane is called dihedral (σ d ).

- n -fold rotation C n about an n -fold axis of symmetry produces molecular orientations indistinguishable from the initial for each rotation of 360°/ n (clockwise and counter-clockwise). It is denoted by C n . The axis of symmetry is the symmetry element in this case. A molecule can have more than one symmetry axis; the one with the highest n is called the principal axis and by convention is assigned the z axis in a Cartesian coordinate system.

- n -fold rotation–reflection , or improper rotation , S n about an n -fold axis of improper rotation is composed of two successive geometry transformations: first, a rotation through 360°/ n about the axis of that rotation, and second, reflection through a plane perpendicular (and through the molecular center of geometry) to that axis. This axis is the symmetry element in this case. It is abbreviated S n .

All other symmetry present in a specific molecule are a combination of these 5 operations.

### Schoenflies notation

The Schoenflies (or Schönflies ) notation , named after the German mathematician Arthur Moritz Schoenflies , is one of two conventions commonly used to describe point groups. This notation is used in spectroscopy and is used here to specify a molecular point group.

## Point groups for diatomic molecules

There are two point groups for diatomic molecules: ${{C}_{\infty v}}$ for heteronuclear diatomics, and ${{D}_{\infty h}}$ for homonuclear diatomics.

- ${{C}_{\infty v}}$ :

The group ${{C}_{\infty v}}$ , contains rotations $C(\phi )$ through any angle $\phi$ about the axis of symmetry and an infinite number of reflections ${{\sigma }_{v}}$ through the planes containing the inter-nuclear axis (or the vertical axis, that is reason of the subscript ' v ').In the group ${{C}_{\infty v}}$ all planes of symmetry are equivalent, so that all reflections ${{\sigma }_{v}}$ form a single class with a continuous series of elements; the axis of symmetry is bilateral, so that there is a continuous series of classes, each containing two elements $C(\pm \phi )$ . Note that this group is non-abelian and there exists an infinite number of irreducible representations in the group. The character table of the group is as follows:

- ${{D}_{\infty h}}$ :

In addition to axial reflection symmetry, homonuclear diatomic molecules are symmetric with respect to inversion or reflection through any axis in the plane passing through the point of symmetry and perpendicular to the inter-nuclear axis.

The classes of the group ${{D}_{\infty h}}$ can be obtained from those of the group ${{C}_{\infty v}}$ using the relation between the two groups: ${{D}_{\infty h}}={{C}_{\infty v}}\times {{C}_{i}}$ . Like ${{C}_{\infty v}}$ , ${{D}_{\infty h}}$ is non-abelian and there are an infinite number of irreducible representations in the group. The character table of this group is as follows:

### Summary examples

## Complete set of commuting operators

Unlike a single atom, the Hamiltonian of a diatomic molecule doesn't commute with ${{L}^{2}}$ . So the quantum number $l$ is no longer a good quantum number . The internuclear axis chooses a specific direction in space and the potential is no longer spherically symmetric. Instead, ${{L}_{z}}$ and ${{J}_{z}}$ commutes with the Hamiltonian $H$ (taking the arbitrary internuclear axis as the Z axis). But ${{L}_{x}},{{L}_{y}}$ do not commute with $H$ due to the fact that the electronic Hamiltonian of a diatomic molecule is invariant under rotations about the internuclear line (the Z axis), but not under rotations about the X or Y axes. Again, ${{S}^{2}}$ and ${{S}_{z}}$ act on a different Hilbert space, so they commute with $H$ in this case also. The electronic Hamiltonian for a diatomic molecule is also invariant under reflections in all planes containing the internuclear line. The ( X-Z ) plane is such a plane, and reflection of the coordinates of the electrons in this plane corresponds to the operation ${{y}_{i}}\to -{{y}_{i}}$ . If ${{A}_{y}}$ is the operator that performs this reflection, then $[{{A}_{y}},H]=0$ . So the Complete Set of Commuting Operators (CSCO) for a general heteronuclear diatomic molecule is $\{H,{\text{ }}{{J}_{z}},{{L}_{z}},{{S}^{2}},{{S}_{z}},A\}$ ; where $A$ is an operator that inverts only one of the two spatial co-ordinates ( x or y).

In the special case of a homonuclear diatomic molecule, there is an extra symmetry since in addition to the axis of symmetry provided by the internuclear axis, there is a centre of symmetry at the midpoint of the distance between the two nuclei (the symmetry discussed in this paragraph only depends on the two nuclear charges being the same. The two nuclei can therefore have different mass, that is they can be two isotopes of the same species such as the proton and the deuteron, or ${{O}^{16}}$ and ${{O}^{18}}$ , and so on). Choosing this point as the origin of the coordinates, the Hamiltonian is invariant under an inversion of the coordinates of all electrons with respect to that origin, namely in the operation ${{\vec {r}}_{i}}\to -{{\vec {r}}_{i}}$ . Thus the parity operator $\Pi$ . Thus the CSCO for a homonuclear diatomic molecule is $\left\{H,{\text{ }}{{J}_{z}},{{L}_{z}},{{S}^{2}},{{S}_{z}},A,{\text{ }}\Pi \right\}$ .

## Molecular term symbol, Λ-doubling

Molecular term symbol is a shorthand expression of the group representation and angular momenta that characterize the state of a molecule. It is the equivalent of the term symbol for the atomic case. We already know the CSCO of the most general diatomic molecule. So, the good quantum numbers can sufficiently describe the state of the diatomic molecule. Here, the symmetry is explicitly stated in the nomenclature.

### Angular momentum

Here, the system is not spherically symmetric. So, $[H,L^{2}]\neq 0$ , and the state cannot be depicted in terms of $l$ as an eigenstate of the Hamiltonian is not an eigenstate of $L^{2}$ anymore (in contrast to the atomic term symbol, where the states were written as $^{2S+1}L_{J}$ ). But, as $[H,L_{z}]=0$ , the eigenvalues corresponding to $L_{z}$ can still be used. If $L_{z}|\Psi \rangle =M_{L}\hbar |\Psi \rangle ;\quad M_{L}=0,\pm 1,\pm 2,\dots ,$ then $L_{z}|\Psi \rangle =\pm \Lambda \hbar |\Psi \rangle ;\quad \Lambda =0,1,2,\dots ,$ where $\Lambda =|M_{L}|$ is the absolute value (in a.u.) of the projection of the total electronic angular momentum on the internuclear axis; $\Lambda$ can be used as a term symbol. By analogy with the spectroscopic notation S, P, D, F, ... used for atoms, it is customary to associate code letters with the values of $\Lambda$ according to the correspondence ${\begin{array}{rcccc}{\text{value of}}\ \Lambda \colon &0&1&2&3&\dots \\&\updownarrow &\updownarrow &\updownarrow &\updownarrow \\{\text{code letter:}}&\Sigma &\Pi &\Delta &\Phi &\dots \end{array}}$

For the individual electrons, the notation and the correspondence used are $\lambda =|m_{l}|$ and ${\begin{array}{rcccc}{\text{value of}}\ \lambda \colon &0&1&2&3&\dots \\&\updownarrow &\updownarrow &\updownarrow &\updownarrow \\{\text{code letter:}}&\sigma &\pi &\delta &\phi &\dots \end{array}}$

### Axial symmetry

Again, $[A_{y},H]=0$ , and in addition $A_{y}L_{z}=-L_{z}A_{y}$ , since $L_{z}=-i\hbar \left(x{\frac {\partial }{\partial y}}-y{\frac {\partial }{\partial x}}\right).$ It follows immediately that if $\Lambda \neq 0,$ the action of the operator $A_{y}$ on an eigenstate corresponding to the eigenvalue $\Lambda \hbar$ of $L_{z}$ converts this state into another one, corresponding to the eigenvalue $-\Lambda \hbar$ , and that both eigenstates have the same energy. The electronic terms such that $\Lambda \neq 0$ (that is, the terms $\Pi ,\Delta ,\Phi ,\dots$ ) are thus doubly degenerate, each value of the energy corresponding to two states which differ by the direction of the projection of the orbital angular momentum along the molecular axis. This twofold degeneracy is actually only approximate, and it is possible to show that the interaction between the electronic and rotational motions leads to a splitting of the terms with $\Lambda \neq 0$ into two nearby levels, which is called ${\boldsymbol {\Lambda }}$ -doubling .

$\Lambda =0$ corresponds to the $\Sigma$ states. These states are non-degenerate, so that the states of a $\Sigma$ term can only be multiplied by a constant in a reflection through a plane containing the molecular axis. When $\Lambda =0$ , simultaneous eigenfunctions of $H$ , $L_{z}$ and $A_{y}$ can be constructed. Since $A_{y}^{2}=1$ , the eigenfunctions of $A_{y}$ have eigenvalues $\pm 1$ . So to completely specify $\Sigma$ states of diatomic molecules, $\Sigma ^{+}$ states, which are left unchanged upon reflection in a plane containing the nuclei, need to be distinguished from $\Sigma ^{-}$ states, which change sign upon reflection.

### Inversion symmetry and nuclear permutation symmetry

Homonuclear diatomic molecules have a center of symmetry at their midpoint. Choosing this point (which is the nuclear center of mass) as the origin of the coordinates, the electronic Hamiltonian is invariant under the point group operation i of inversion of the coordinates of all electrons at that origin. This operation is not the parity operation P (or E*); the parity operation involves the inversion of nuclear and electronic spatial coordinates at the molecular center of mass. Electronic states either remain unchanged by the operation i , or they are changed in sign by i . The former are denoted by the subscript g and are called gerade, while the latter are denoted by the subscript u and are called ungerade. The subscripts g or u are therefore added to the term symbol, so that for homonuclear diatomic molecules electronic states can have the symmetries $\Sigma _{g}^{+},\Sigma _{g}^{-},\Sigma _{u}^{+},\Sigma _{u}^{-},{{\Pi }_{g}},{{\Pi }_{u}}$ ,......according to the irreducible representations of the ${{D}_{\infty h}}$ point group.

The complete Hamiltonian of a diatomic molecule (as for all molecules) commutes with the parity operation P or E* and rovibronic (rotation-vibration-electronic) energy levels (often called rotational levels) can be given the parity symmetry label + or - . The complete Hamiltonian of a homonuclear diatomic molecule also commutes with the operation
of permuting (or exchanging) the coordinates of the two (identical) nuclei and rotational levels 
gain the additional label s or a depending on whether the total wavefunction is
unchanged (symmetric) or changed in sign (antisymmetric) by the permutation operation. Thus, the rotational levels of heteronuclear diatomic molecules are labelled + or - , whereas those of homonuclear diatomic
molecules are labelled +s , +a , -s or -a . The rovibronic nuclear spin states are classified using the appropriate permutation-inversion group.

The complete Hamiltonian of a homonuclear diatomic molecule (as for all centro-symmetric molecules)
does not commute with the point group inversion operation i because of the effect of the nuclear hyperfine Hamiltonian. The nuclear hyperfine Hamiltonian can mix the rotational levels of g and u vibronic states (called ortho - para mixing) and give
rise to ortho - para transitions

### Spin and total angular momentum

If S denotes the resultant of the individual electron spins, $s(s+1){{\hbar }^{2}}$ are the eigenvalues of S and as in the case of atoms, each electronic term of the molecule is also characterised by the value of S . If spin-orbit coupling is neglected, there is a degeneracy of order $2s+1$ associated with each $s$ for a given $\Lambda$ . Just as for atoms, the quantity $2s+1$ is called the multiplicity of the term and.is written as a (left) superscript, so that the term symbol is written as ${}^{2s+1}\Lambda$ . For example, the symbol ${}^{3}\Pi$ denotes a term such that $\Lambda =1$ and $s=1$ . It is worth noting that the ground state (often labelled by the symbol $X$ ) of most diatomic molecules is such that $s=0$ and exhibits maximum symmetry. Thus, in most cases it is a ${}^{1}{{\Sigma }^{+}}$ state (written as $X{}^{1}{{\Sigma }^{+}}$ , excited states are written with $A,B,C,...$ in front) for a heteronuclear molecule and a ${}^{1}\Sigma _{g}^{+}$ state (written as $X{}^{1}\Sigma _{g}^{+}$ ) for a homonuclear molecule.

Spin–orbit coupling lifts the degeneracy of the electronic states. This is because the z -component of spin interacts with the z -component of the orbital angular momentum, generating a total electronic angular momentum along the molecule axis J z . This is characterized by the quantum number ${{M}_{J}}$ , where ${{M}_{J}}={{M}_{S}}+{{M}_{L}}$ . Again, positive and negative values of ${{M}_{J}}$ are degenerate, so the pairs ( M L , M S ) and (− M L , − M S ) are degenerate. These pairs are grouped together with the quantum number $\Omega$ , which is defined as the sum of the pair of values ( M L , M S ) for which M L is positive: $\Omega =\Lambda +{{M}_{S}}$

### Molecular term symbol

So, the overall molecular term symbol for the most general diatomic molecule is given by ${}^{2S+1}\!\Lambda _{\Omega ,{\text{(g/u)}}}^{(+/-)},$ where

S is the total spin quantum number,

$\Lambda$ is the projection of the orbital angular momentum along the internuclear axis,

$\Omega$ is the projection of the total angular momentum along the internuclear axis,

u/g is the effect of the point group operation i ,

+/− is the reflection symmetry along an arbitrary plane containing the internuclear axis.

## von Neumann-Wigner non-crossing rule

### Effect of symmetry on the matrix elements of the Hamiltonian

The electronic terms or potential curves ${{E}_{S}}(R)$ of a diatomic molecule depend only on the internuclear distance $R$ , and it is important to investigate the behaviour of these potential curves as R varies. It is of considerable interest to examine the intersection of the curves representing the different terms.

Let ${{E}_{1}}(R)$ and ${{E}_{2}}(R)$ two different electronic potential curves. If they intersect at some point, then the functions ${{E}_{1}}(R)$ and ${{E}_{2}}(R)$ will have neighbouring values near this point. To decide whether such an intersection can occur, it is convenient to put the problem as follows. Suppose at some internuclear distance ${R}_{c}$ the values ${{E}_{1}}({{R}_{C}})$ and ${{E}_{2}}({{R}_{C}})$ are close, but distinct (as shown in the figure). Then it is to be examined whether or ${{E}_{1}}(R)$ and ${{E}_{2}}(R)$ can be made to intersect by the modification ${{R}_{C}}\to {{R}_{C}}+\Delta R$ . The energies $E_{1}^{(0)}={{E}_{1}}({{R}_{C}})$ and $E_{2}^{(0)}={{E}_{2}}({{R}_{C}})$ are eigenvalues of the Hamiltonian ${{H}_{0}}=H({{R}_{C}})$ . The corresponding orthonormal electronic eigenstates will be denoted by $\left|\Phi _{1}^{(0)}\right\rangle$ and $\left|\Phi _{2}^{(0)}\right\rangle$ and are assumed to be real.
The Hamiltonian now becomes $H\equiv H({{R}_{C}}+\Delta R)={{H}_{0}}+H'$ , where $H'={\frac {\partial {{H}_{0}}}{\partial {{R}_{C}}}}\Delta R$ is the small perturbation operator (though it is a degenerate case, so ordinary method of perturbation won't work). setting $H_{ij}^{'}=\left\langle \Phi _{i}^{(0)}|H'|\Phi _{j}^{(0)}\right\rangle ;i,j=1,2$ , it can be deduced that in order for ${{E}_{1}}(R)$ and ${{E}_{2}}(R)$ to be equal at the point ${{R}_{C}}+\Delta R$ the following two conditions are required to be fulfilled:

However, we have at our disposal only one arbitrary parameter $\Delta R$ giving the perturbation $H'$ . Hence the

two conditions involving more than one parameter cannot in general be simultaneously satisfied (the initial assumption that $\left|\Phi _{1}^{(0)}\right\rangle$ and $\left|\Phi _{2}^{(0)}\right\rangle$ real, implies that $H_{12}^{'}$ is also real). So, two case can arise:

- The matrix element $H_{12}^{'}$ vanishes identically. It is then possible to satisfy the first condition independently. Therefore, it is possible for the crossing to occur if, for a certain value of $\Delta R$ (i.e., for a certain value of $R$ ) the first equation is satisfied. As the perturbation operator $H'$ (or $H$ ) commutes with the symmetry operators of the molecule, this case will happen if the two electronic states $\left|\Phi _{1}^{(0)}\right\rangle$ and $\left|\Phi _{2}^{(0)}\right\rangle$ have different point group symmetries (for example if they correspond to two electronic terms having different values of $\Lambda$ , different electronic parities g and u , different multiplicities, or for example are the two terms ${{\Sigma }^{+}}$ and ${{\Sigma }^{-}}$ ) as it can be shown that, for a scalar quantity whose operator commutes with the angular momentum and inversion operators, only the matrix elements for transitions between states of the same angular momentum and parity are non-zero and the proof remains valid, in essentially the same form, for the general case of an arbitrary symmetry operator.

- If the electronic states $\left|\Phi _{1}^{(0)}\right\rangle$ and $\left|\Phi _{2}^{(0)}\right\rangle$ have the same point group symmetry, then $H_{12}^{'}$ can be, and will in general be, non-zero. Except for accidental crossing which would occur if, by coincidence, the two equations were satisfied at the same value of $R$ , it is in general impossible to find a single value of $\Delta R$ (i.e., a single value of $R$ ) for which the two conditions are satisfied simultaneously.

Thus, in a diatomic molecule, only terms of different symmetry can intersect, while the intersection of terms of like symmetry is forbidden. This is, in general, true for any case in quantum mechanics where the Hamiltonian contains some parameter and its eigenvalues are consequently functions of that parameter. This general rule is known as von Neumann - Wigner non-crossing rule.

This general symmetry principle has important consequences is molecular spectra.
In fact, in the applications of valence bond method in case of diatomic molecules, three main correspondence between the atomic and the molecular orbitals are taken care of:

- Molecular orbitals having a given value of $\lambda$ (the component of the orbital angular momentum along the internuclear axis) must connect with atomic orbitals having the same value of $\lambda$ (i.e. the same value of $\left|m\right|$ ).

- The electronic parity of the wave function ( g or u ) must be preserved as $R$ varies from $0$ to $\infty$ .

- The von Neumann-Wigner non-crossing rule must be obeyed, so that energy curves corresponding to orbitals having the same symmetry do not cross as $R$ varies from $0$ to $\infty$ .

Thus, von Neumann-Wigner non-crossing rule also acts as a starting point for valence bond theory.

## Observable consequences

Symmetry in diatomic molecules manifests itself directly by influencing the molecular spectra of the molecule. The effect of symmetry on different types of spectra in diatomic molecules are:

### Rotational spectrum

In the electric dipole approximation the transition amplitude for emission or absorption of radiation can be shown to be proportional to the vibronic matrix element of the component of the electric dipole operator $D$ along the molecular axis. This is the permanent electric dipole moment.
In homonuclear diatomic molecules, the permanent electric dipole moment vanishes and there is no pure rotation spectrum (but see N.B. below).
Heteronuclear diatomic molecules possess a permanent electric dipole moment and exhibit spectra corresponding to rotational transitions, without change in the vibronic state. For $\Lambda =0$ , the selection rules for a rotational transition are: ${\begin{aligned}&\Delta \Im =\pm 1\\&\Delta {{M}_{\Im }}=0,\pm 1\\\end{aligned}}$ . For $\Lambda \neq 0$ , the selection rules become: ${\begin{aligned}&\Delta \Im =0,\pm 1\\&\Delta {{M}_{\Im }}=0,\pm 1\\\end{aligned}}$ .This is due to the fact that although the photon absorbed or emitted carries one unit of angular momentum, the nuclear rotation can change, with no change in $\Im$ , if the electronic angular momentum makes an equal and opposite change. Symmetry considerations require that the electric dipole moment of a diatomic molecule is directed along the internuclear line, and this leads to the additional selection rule $\Delta \Lambda =0$ .The pure rotational spectrum of a diatomic molecule consists of lines in the far infra-red or the microwave region, the frequencies of these lines given by:

$\hbar {{\omega }_{\Im +1,\Im }}={{E}_{r}}(\Im +1)-{{E}_{r}}(\Im )=2B(\Im +1)$ ; where $B={\frac {{\hbar }^{2}}{2\mu R_{0}^{2}}}$ , and $\Im \geq \Lambda$

- N.B. In exceptional circumstances the hyperfine Hamiltonian can mix the rotational levels of g and u vibronic states of homonuclear diatomic molecules giving rise to pure rotational ( ortho - para ) transitions in a homonuclear diatomic molecule.

### Vibrational spectrum

The transition matrix elements for pure vibrational transition are ${{\mu }_{v,v'}}=\left\langle v'|\mu |v\right\rangle$ , where $\mu$ is the dipole moment of the diatomic molecule in the electronic state $\alpha$ . Because the dipole moment depends on the bond length $R$ , its variation with displacement of the nuclei from equilibrium can be expressed as: $\mu ={{\mu }_{0}}+{{({\frac {d\mu }{dx}})}_{0}}x+{\frac {1}{2}}{{({\frac {{{d}^{2}}\mu }{d{{x}^{2}}}})}_{0}}{{x}^{2}}+.......$ ; where ${{\mu }_{0}}$ is the dipole moment when the displacement is zero. The transition matrix elements are, therefore: $\left\langle v'|\mu |v\right\rangle ={{\mu }_{0}}\left\langle v'|v\right\rangle +{{({\frac {d\mu }{dx}})}_{0}}\left\langle v'|x|v\right\rangle +{\frac {1}{2}}{{({\frac {{{d}^{2}}\mu }{d{{x}^{2}}}})}_{0}}\left\langle v'|{{x}^{2}}|v\right\rangle +.......={{({\frac {d\mu }{dx}})}_{0}}\left\langle v'|x|v\right\rangle +{\frac {1}{2}}{{({\frac {{{d}^{2}}\mu }{d{{x}^{2}}}})}_{0}}\left\langle v'|{{x}^{2}}|v\right\rangle +.......$ using orthogonality of the states. So, the transition matrix is non-zero only if the molecular dipole moment varies with displacement, for otherwise the derivatives of $\mu$ would be zero. The gross selection rule for the vibrational transitions of diatomic molecules is then: To show a vibrational spectrum, a diatomic molecule must have a dipole moment that varies with extension. So, homonuclear diatomic molecules do not undergo electric-dipole vibrational transitions. So, a homonuclear diatomic molecule doesn't show purely vibrational spectra.

For small displacements, the electric dipole moment of a molecule can be expected to vary linearly with the extension of the bond. This would be the case for a heteronuclear molecule in which the partial charges on the two atoms were independent of the internuclear distance. In such cases (known as harmonic approximation), the quadratic and higher terms in the expansion can be ignored and ${{\mu }_{v,v'}}=\left\langle v'|\mu |v\right\rangle ={{({\frac {d\mu }{dx}})}_{0}}\left\langle v'|x|v\right\rangle$ . Now, the matrix elements can be expressed in position basis in terms of the harmonic oscillator wavefunctions: Hermite polynomials. Using the property of Hermite polynomials: $2(\alpha x){{H}_{v}}(\alpha x)=2v{{H}_{v-1}}(\alpha x)+{{H}_{v+1}}(\alpha x)$ , it is evident that $x\left|v\right\rangle$ which is proportional to $x{{H}_{v}}(\alpha x)$ , produces two terms, one proportional to $\left|v+1\right\rangle$ and the other to $\left|v-1\right\rangle$ . So, the only non-zero contributions to ${{\mu }_{v,v'}}$ comes from $v'=v\pm 1$ . So, the selection rule for heteronuclear diatomic molecules is: $\Delta v=\pm 1$

- Conclusion: Homonuclear diatomic molecules show no pure vibrational spectral lines, and the vibrational spectral lines of heteronuclear diatomic molecules are governed by the above-mentioned selection rule.

### Rovibrational spectrum

Homonuclear diatomic molecules show neither pure vibrational nor pure rotational spectra. However, as the absorption of a photon requires the molecule to take up one unit of angular momentum , vibrational transitions are accompanied by a change in rotational state, which is subject to the same selection rules as for the pure rotational spectrum. For a molecule in a $\Sigma$ state, the transitions between two vibration-rotation (or rovibrational ) levels $(v,\Im )$ and $(v',\Im ')$ , with vibrational quantum numbers $v$ and $v'=v+1$ , fall into two sets according to whether $\Delta \Im =+1$ or $\Delta \Im =-1$ . The set corresponding to $\Delta \Im =+1$ is called the R branch . The corresponding frequencies are given by: $\hbar {{\omega }^{R}}=E(v+1,\Im +1)-E(v,\Im )=2B(\Im +1)+\hbar {{\omega }_{0}};{\text{ }}\Im =0,1,2,......$

The set corresponding to $\Delta \Im =-1$ is called the P branch . The corresponding frequencies are given by: $\hbar {{\omega }^{P}}=E(v+1,\Im -1)-E(v,\Im )=-2B\Im +\hbar {{\omega }_{0}};{\text{ }}\Im =1,2,3,......$

Both branches make up what is called a rotational-vibrational band or a rovibrational band . These bands are in the infra-red part of the spectrum.

If the molecule is not in a $\Sigma$ state, so that $\Lambda \neq 0$ , transitions with $\Delta \Im =0$ are allowed. This gives rise to a further branch of the vibrational-rotational spectrum, called the Q branch . The frequencies ${{\omega }^{Q}}$ corresponding to the lines in this branch are given by a quadratic function of $\Im$ if ${{B}_{v}}$ and ${{B}_{v+1}}$ are unequal, and reduce to the single frequency: $\hbar {{\omega }^{Q}}=E(v+1,\Im )-E(v,\Im )=\hbar {{\omega }_{0}}$ if ${{B}_{v+1}}={{B}_{v}}$ .

For a heteronuclear diatomic molecule, this selection rule has two consequences:

- Both the vibrational and rotational quantum numbers must change. The Q-branch is therefore forbidden.

- The energy change of rotation can be either subtracted from or added to the energy change of vibration, giving the P- and R- branches of the spectrum, respectively.

Homonuclear diatomic molecules also show this kind of spectra. The selection rules, however, are a bit different.

- Conclusion: Both homo- and hetero-nuclear diatomic molecules show rovibrational spectra. A Q-branch is absent in the spectra of heteronuclear diatomic molecules.

## A special example: Hydrogen molecule ion

An explicit implication of symmetry on the molecular structure can be shown in case of the simplest bi-nuclear system: a hydrogen molecule ion or a di-hydrogen cation, ${\text{H}}_{2}^{+}$ . A natural trial wave function for the ${\text{H}}_{2}^{+}$ is determined by first considering the lowest-energy state of the system when the two protons are widely separated. Then there are clearly two possible states: the electron is attached either to one of the protons, forming a hydrogen atom in the ground state , or the electron is attached to the other proton, again in the ground state of a hydrogen atom (as depicted in the picture).

The trial states in the position basis (or the ' wave functions ') are then:

$\left\langle \mathbf {r} |\mathbf {1} \right\rangle ={\frac {1}{\sqrt {\pi a_{0}^{3}}}}{{e}^{-{\frac {\left|\mathbf {r} -{\frac {\mathbf {R} }{2}}\right|}{{a}_{0}}}}}$ and $\left\langle \mathbf {r} |\mathbf {2} \right\rangle ={\frac {1}{\sqrt {\pi a_{0}^{3}}}}{{e}^{-{\frac {\left|\mathbf {r} +{\frac {\mathbf {R} }{2}}\right|}{{a}_{0}}}}}$

The analysis of ${\text{H}}_{2}^{+}$ using variational method starts assuming these forms. Again, this is only one possible combination of states. There can be other combination of states also, for example, the electron is in an excited state of the hydrogen atom. The corresponding Hamiltonian of the system is:

$H={\frac {{\mathbf {p} }^{2}}{2{{m}_{e}}}}-{\frac {{e}^{2}}{\left|\mathbf {r} -\mathbf {R} /2\right|}}-{\frac {{e}^{2}}{\left|\mathbf {r} +\mathbf {R} /2\right|}}+{\frac {{e}^{2}}{R}}$

Clearly, using the states $\left|1\right\rangle$ and $\left|2\right\rangle$ as basis will introduce off-diagonal elements in the Hamiltonian. Here, because of the relative simplicity of the ${\text{H}}_{2}^{+}$ ion, the matrix elements can actually be calculated. The electronic Hamiltonian of ${\text{H}}_{2}^{+}$ commutes with the point group inversion symmetry operation i . Using its symmetry properties, we can relate the diagonal and off-diagonal elements of the Hamiltonian as:

Because ${{H}_{11}}={{H}_{22}}$ as well as ${{H}_{12}}={{H}_{21}}$ , the linear combination of $\left|1\right\rangle$ and $\left|2\right\rangle$ that diagonalizes the Hamiltonian is $\left|\pm \right\rangle ={\frac {1}{\sqrt {2\pm 2\left\langle 1|2\right\rangle }}}(\left|1\right\rangle \pm \left|2\right\rangle )$ (after normalization). Now as $[H,$ i $]=0$ for ${\text{H}}_{2}^{+}$ , the states $\left|\pm \right\rangle$ are also eigenstates of i . It turns out that $\left|+\right\rangle$ and $\left|-\right\rangle$ are the eigenstates of i with eigenvalues +1 and -1 (in other words, the wave functions $\left\langle \mathbf {r} |+\right\rangle$ and $\left\langle \mathbf {r} |-\right\rangle$ are gerade (symmetric) and ungerade (unsymmetric), respectively). The corresponding expectation value of the energies are ${{E}_{\pm }}={\frac {1}{1\pm \left\langle 1|2\right\rangle }}({{H}_{11}}\pm {{H}_{12}})$ .

From the graph, we see that only ${{E}_{+}}$ has a minimum corresponding to a separation of 1.3 Å and a total energy ${{E}_{+}}=-15.4{\text{ eV}}$ , which is less than the initial energy of the system, $-13.6{\text{ eV}}$ . Thus, only the gerade state stabilizes the ion with a binding energy of $1.8{\text{ eV}}$ . As a result, the ground state of ${\text{H}}_{2}^{+}$ is ${{X}^{2}}\Sigma _{g}^{+}$ and this state $\left(\left|+\right\rangle \right)$ is called a bonding molecular orbital.

Thus, symmetry plays an explicit role in the formation of ${\text{H}}_{2}^{+}$ .
