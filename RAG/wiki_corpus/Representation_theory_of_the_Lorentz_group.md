# Representation theory of the Lorentz group

> **Query Topic**: Lorentz symmetry or Lorentz invariance in relativistic physics (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 7, Frequency: 15)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Representation_theory_of_the_Lorentz_group

---

The Lorentz group is a Lie group of symmetries of the spacetime of special relativity . This group can be realized as a collection of matrices , linear transformations , or unitary operators on some Hilbert space ; it has a variety of representations . This group is significant because special relativity together with quantum mechanics are the two physical theories that are most thoroughly established, and the conjunction of these two theories is the study of the infinite-dimensional unitary representations of the Lorentz group. These have both historical importance in mainstream physics, as well as connections to more speculative present-day theories.

The development of the representation theory has historically followed the development of the more general theory of representation theory of semisimple groups , largely due to Élie Cartan and Hermann Weyl , but the Lorentz group has also received special attention due to its importance in physics. Notable contributors are physicist E. P. Wigner and mathematician Valentine Bargmann with their Bargmann–Wigner program , one conclusion of which is, roughly, a classification of all unitary representations of the inhomogeneous Lorentz group amounts to a classification of all possible relativistic wave equations . The classification of the irreducible infinite-dimensional representations of the Lorentz group was established by Paul Dirac 's doctoral student in theoretical physics, Harish-Chandra , later turned mathematician, in 1947. Closely related work was published independently by Bargmann and Israel Gelfand together with Mark Naimark in the same year.

The full theory of the finite-dimensional representations of the Lie algebra of the Lorentz group is deduced using the general framework of the representation theory of semisimple Lie algebras . The finite-dimensional representations of the connected component ${\text{SO}}(3;1)^{+}$ of the full Lorentz group O(3; 1) are obtained by employing the Lie correspondence and the matrix exponential . The full finite-dimensional representation theory of the universal covering group (and also the spin group , a double cover) ${\text{SL}}(2,\mathbb {C} )$ of ${\text{SO}}(3;1)^{+}$ is obtained, and explicitly given in terms of action on a function space in representations of ${\text{SL}}(2,\mathbb {C} )$ and ${\mathfrak {sl}}(2,\mathbb {C} )$ . The representatives of time reversal and space inversion are given in space inversion and time reversal , completing the finite-dimensional theory for the full Lorentz group. The general properties of the ( m , n ) representations are outlined. Action on function spaces is considered, with the action on spherical harmonics and the Riemann P-functions appearing as examples. The infinite-dimensional case of irreducible unitary representations is realized for the ${\text{SL}}(2,\mathbb {C} )$ principal series and the complementary series . Finally, the Plancherel formula for ${\text{SL}}(2,\mathbb {C} )$ is given, and representations of SO(3, 1) are classified and realized for Lie algebras.

## Finite-dimensional representations

Representation theory of groups in general, and Lie groups in particular, is a very rich subject. The Lorentz group has some properties that makes it "agreeable" and others that make it "not very agreeable" within the context of representation theory; the group is simple and thus semisimple , but is not connected , and none of its components are simply connected . Furthermore, the Lorentz group is not compact .

For finite-dimensional representations, the presence of semisimplicity means that the Lorentz group can be dealt with the same way as other semisimple groups using a well-developed theory. In addition, all representations are built from the irreducible ones, since the Lie algebra possesses the complete reducibility property . But, the non-compactness of the Lorentz group, in combination with lack of simple connectedness, cannot be dealt with in all the aspects as in the simple framework that applies to simply connected, compact groups. Non-compactness implies, for a connected simple Lie group, that no nontrivial finite-dimensional unitary representations exist. Lack of simple connectedness gives rise to spin representations of the group. The non-connectedness means that, for representations of the full Lorentz group, time reversal and reversal of spatial orientation have to be dealt with separately.

### History

The development of the finite-dimensional representation theory of the Lorentz group mostly follows that of representation theory in general. Lie theory originated with Sophus Lie in 1873. By 1888 the classification of simple Lie algebras was essentially completed by Wilhelm Killing . In 1913 the theorem of highest weight for representations of simple Lie algebras, the path that will be followed here, was completed by Élie Cartan . Richard Brauer was during the period of 1935–38 largely responsible for the development of the Weyl-Brauer matrices describing how spin representations of the Lorentz Lie algebra can be embedded in Clifford algebras . The Lorentz group has also historically received special attention in representation theory due to its exceptional importance in physics (see History of infinite-dimensional unitary representations below). Mathematicians Hermann Weyl and Harish-Chandra and physicists Eugene Wigner and Valentine Bargmann made substantial contributions both to general representation theory and in particular to the Lorentz group. Physicist Paul Dirac was perhaps the first to manifestly knit everything together in a practical application of major lasting importance with the Dirac equation in 1928.

### Lie algebra

The irreducible representations of the Lie algebra of the Lorentz group can be derived by factoring that Lie algebra into a direct product of two subalgebras. Each subalgebra is isomorphic to ${\mathfrak {su}}(2)$ , and the irreducible representations of ${\mathfrak {su}}(2)$ are labeled by nonnegative half-integers. Consequently, the irreducible representations of the Lorentz group's Lie algebra are labeled by ordered pairs $(m,n)$ of nonnegative half-integers.

This section addresses the irreducible complex linear representations of the complexification ${\mathfrak {so}}(3;1)_{\mathbb {C} }$ of the Lie algebra ${\mathfrak {so}}(3;1)$ of the Lorentz group. A convenient basis for ${\mathfrak {so}}(3;1)$ is given by the three generators J i of rotations and the three generators K i of boosts . They are explicitly given in conventions and Lie algebra bases .

The Lie algebra is complexified , and the basis is changed to the components of its two ideals $\mathbf {A} ={\frac {\mathbf {J} +i\mathbf {K} }{2}},\quad \mathbf {B} ={\frac {\mathbf {J} -i\mathbf {K} }{2}}.$

The components of A = ( A 1 , A 2 , A 3 ) and B = ( B 1 , B 2 , B 3 ) separately satisfy the commutation relations of the Lie algebra ${\mathfrak {su}}(2)$ and, moreover, they commute with each other,

$\left[A_{i},A_{j}\right]=i\varepsilon _{ijk}A_{k},\quad \left[B_{i},B_{j}\right]=i\varepsilon _{ijk}B_{k},\quad \left[A_{i},B_{j}\right]=0,$

where i , j , k are indices which each take values 1, 2, 3 , and ε ijk is the three-dimensional Levi-Civita symbol . Let $\mathbf {A} _{\mathbb {C} }$ and $\mathbf {B} _{\mathbb {C} }$ denote the complex linear span of A and B respectively.

One has the isomorphisms

where ${\mathfrak {sl}}(2,\mathbb {C} )$ is the complexification of ${\mathfrak {su}}(2)\cong \mathbf {A} \cong \mathbf {B} .$

The utility of these isomorphisms comes from the fact that all irreducible representations of ${\mathfrak {su}}(2)$ , and hence all irreducible complex linear representations of ${\mathfrak {sl}}(2,\mathbb {C} ),$ are known. The irreducible complex linear representation of ${\mathfrak {sl}}(2,\mathbb {C} )$ is isomorphic to one of the highest weight representations . These are explicitly given in complex linear representations of ${\mathfrak {sl}}(2,\mathbb {C} ).$

#### Unitarian trick

The Lie algebra ${\mathfrak {sl}}(2,\mathbb {C} )\oplus {\mathfrak {sl}}(2,\mathbb {C} )$ is the Lie algebra of ${\text{SL}}(2,\mathbb {C} )\times {\text{SL}}(2,\mathbb {C} ).$ It contains the compact subgroup SU(2) × SU(2) with Lie algebra ${\mathfrak {su}}(2)\oplus {\mathfrak {su}}(2).$ The latter is a compact real form of ${\mathfrak {sl}}(2,\mathbb {C} )\oplus {\mathfrak {sl}}(2,\mathbb {C} ).$ Thus from the first statement of the unitarian trick, representations of SU(2) × SU(2) are in one-to-one correspondence with holomorphic representations of ${\text{SL}}(2,\mathbb {C} )\times {\text{SL}}(2,\mathbb {C} ).$

By compactness, the Peter–Weyl theorem applies to SU(2) × SU(2) , and hence orthonormality of irreducible characters may be appealed to. The irreducible unitary representations of SU(2) × SU(2) are precisely the tensor products of irreducible unitary representations of SU(2) .

By appeal to simple connectedness, the second statement of the unitarian trick is applied. The objects in the following list are in one-to-one correspondence:

- Holomorphic representations of ${\text{SL}}(2,\mathbb {C} )\times {\text{SL}}(2,\mathbb {C} )$

- Smooth representations of SU(2) × SU(2)

- Real linear representations of ${\mathfrak {su}}(2)\oplus {\mathfrak {su}}(2)$

- Complex linear representations of ${\mathfrak {sl}}(2,\mathbb {C} )\oplus {\mathfrak {sl}}(2,\mathbb {C} )$

Tensor products of representations appear at the Lie algebra level as either of

where Id is the identity operator. Here, the latter interpretation, which follows from (G6) , is intended. The highest weight representations of ${\mathfrak {sl}}(2,\mathbb {C} )$ are indexed by μ for μ = 0, 1/2, 1, ... . (The highest weights are actually 2 μ = 0, 1, 2, ... , but the notation here is adapted to that of ${\mathfrak {so}}(3;1).$ ) The tensor products of two such complex linear factors then form the irreducible complex linear representations of ${\mathfrak {sl}}(2,\mathbb {C} )\oplus {\mathfrak {sl}}(2,\mathbb {C} ).$

Finally, the $\mathbb {R}$ -linear representations of the real forms of the far left, ${\mathfrak {so}}(3;1)$ , and the far right, ${\mathfrak {sl}}(2,\mathbb {C} ),$ in (A1) are obtained from the $\mathbb {C}$ -linear representations of ${\mathfrak {sl}}(2,\mathbb {C} )\oplus {\mathfrak {sl}}(2,\mathbb {C} )$ characterized in the previous paragraph.

#### ( μ , ν )-representations of sl(2, C)

The complex linear representations of the complexification of ${\mathfrak {sl}}(2,\mathbb {C} ),{\mathfrak {sl}}(2,\mathbb {C} )_{\mathbb {C} },$ obtained via isomorphisms in (A1) , stand in one-to-one correspondence with the real linear representations of ${\mathfrak {sl}}(2,\mathbb {C} ).$ The set of all real linear irreducible representations of ${\mathfrak {sl}}(2,\mathbb {C} )$ are thus indexed by a pair ( μ , ν ) . The complex linear ones, corresponding precisely to the complexification of the real linear ${\mathfrak {su}}(2)$ representations, are of the form ( μ , 0) , while the conjugate linear ones are the (0, ν ) . All others are real linear only. The linearity properties follow from the canonical injection, the far right in (A1) , of ${\mathfrak {sl}}(2,\mathbb {C} )$ into its complexification. Representations on the form ( ν , ν ) or ( μ , ν ) ⊕ ( ν , μ ) are given by real matrices (the latter are not irreducible). Explicitly, the real linear ( μ , ν ) -representations of ${\mathfrak {sl}}(2,\mathbb {C} )$ are $\varphi _{\mu ,\nu }(X)=\left(\varphi _{\mu }\otimes {\overline {\varphi _{\nu }}}\right)(X)=\varphi _{\mu }(X)\otimes \operatorname {Id} _{\nu +1}+\operatorname {Id} _{\mu +1}\otimes {\overline {\varphi _{\nu }(X)}},\qquad X\in {\mathfrak {sl}}(2,\mathbb {C} )$ where ${\textstyle \varphi _{\mu },\mu =0,{\tfrac {1}{2}},1,{\tfrac {3}{2}},\ldots }$ are the complex linear irreducible representations of ${\mathfrak {sl}}(2,\mathbb {C} )$ and ${\overline {\varphi _{\nu }}},\nu =0,{\tfrac {1}{2}},1,{\tfrac {3}{2}},\ldots$ their complex conjugate representations. (The labeling is usually in the mathematics literature 0, 1, 2, ... , but half-integers are chosen here to conform with the labeling for the ${\mathfrak {so}}(3,1)$ Lie algebra.) Here the tensor product is interpreted in the former sense of (A0) . These representations are concretely realized below.

#### ( m , n )-representations of so(3; 1)

Via the displayed isomorphisms in (A1) and knowledge of the complex linear irreducible representations of ${\mathfrak {sl}}(2,\mathbb {C} )\oplus {\mathfrak {sl}}(2,\mathbb {C} )$ upon solving for J and K , all irreducible representations of ${\mathfrak {so}}(3;1)_{\mathbb {C} },$ and, by restriction, those of ${\mathfrak {so}}(3;1)$ are obtained. The representations of ${\mathfrak {so}}(3;1)$ obtained this way are real linear (and not complex or conjugate linear) because the algebra is not closed upon conjugation, but they are still irreducible. Since ${\mathfrak {so}}(3;1)$ is semisimple , all its representations can be built up as direct sums of the irreducible ones.

Thus the finite dimensional irreducible representations of the Lorentz algebra are classified by an ordered pair of half-integers m = μ and n = ν , conventionally written as one of $(m,n)\equiv \pi _{(m,n)}:{\mathfrak {so}}(3;1)\to {\mathfrak {gl}}(V),$ where V is a finite-dimensional vector space. These are, up to a similarity transformation , uniquely given by

where 1 n is the n -dimensional unit matrix and $\mathbf {J} ^{(n)}=\left(J_{1}^{(n)},J_{2}^{(n)},J_{3}^{(n)}\right)$ are the (2 n + 1) -dimensional irreducible representations of ${\mathfrak {so}}(3)\cong {\mathfrak {su}}(2)$ also termed spin matrices or angular momentum matrices . These are explicitly given as ${\begin{aligned}\left(J_{1}^{(j)}\right)_{a'a}&={\frac {1}{2}}\left({\sqrt {(j-a)(j+a+1)}}\delta _{a',a+1}+{\sqrt {(j+a)(j-a+1)}}\delta _{a',a-1}\right)\\\left(J_{2}^{(j)}\right)_{a'a}&={\frac {1}{2i}}\left({\sqrt {(j-a)(j+a+1)}}\delta _{a',a+1}-{\sqrt {(j+a)(j-a+1)}}\delta _{a',a-1}\right)\\\left(J_{3}^{(j)}\right)_{a'a}&=a\delta _{a',a}\end{aligned}}$ where δ denotes the Kronecker delta . In components, with − m ≤ a , a′ ≤ m , − n ≤ b , b′ ≤ n , the representations are given by ${\begin{aligned}\left(\pi _{(m,n)}\left(J_{i}\right)\right)_{a'b',ab}&=\delta _{b'b}\left(J_{i}^{(m)}\right)_{a'a}+\delta _{a'a}\left(J_{i}^{(n)}\right)_{b'b}\\\left(\pi _{(m,n)}\left(K_{i}\right)\right)_{a'b',ab}&=-i\left(\delta _{b'b}\left(J_{i}^{(m)}\right)_{a'a}-\delta _{a'a}\left(J_{i}^{(n)}\right)_{b'b}\right)\end{aligned}}$

#### Common representations

Representations of this Lie algebra are used in physics, since various physical quantities of interest are functions, or collections of functions, defined on spacetime that transform together under a representation of an appropriate dimension.

- The (0, 0) representation is the one-dimensional trivial representation and is carried by relativistic scalar field theories.

- Fermionic supersymmetry generators transform under one of the (0, ⁠ 1 / 2 ⁠ ) or ( ⁠ 1 / 2 ⁠ , 0) representations (Weyl spinors).

- The four-momentum of a particle (either massless or massive ) transforms under the ( ⁠ 1 / 2 ⁠ , ⁠ 1 / 2 ⁠ ) representation, a four-vector .

- A physical example of a (1,1) traceless symmetric tensor field is the traceless part of the energy–momentum tensor T μν .

Since complex conjugation exchanges ( m , n ) and ( n , m ) , the direct sum of representations ( m , n ) and ( n , m ) admits real matrix representatives and therefore has particular relevance to physics.

- ( ⁠ 1 / 2 ⁠ , 0) ⊕ (0, ⁠ 1 / 2 ⁠ ) is the Dirac spinor representation. See also Weyl spinors below.

- (1, ⁠ 1 / 2 ⁠ ) ⊕ ( ⁠ 1 / 2 ⁠ , 1) is the Rarita–Schwinger field representation.

- ( ⁠ 3 / 2 ⁠ , 0) ⊕ (0, ⁠ 3 / 2 ⁠ ) would be the symmetry of the hypothesized gravitino . It can be obtained from the (1, ⁠ 1 / 2 ⁠ ) ⊕ ( ⁠ 1 / 2 ⁠ , 1) representation.

- (1, 0) ⊕ (0, 1) is the representation of a parity -invariant 2-form field (a.k.a. curvature form ). The electromagnetic field tensor transforms under this representation.

### Group

The approach in this section is based on theorems that, in turn, are based on the fundamental Lie correspondence . The Lie correspondence is in essence a dictionary between connected Lie groups and Lie algebras. The link between them is the exponential mapping from the Lie algebra to the Lie group, denoted $\exp :{\mathfrak {g}}\to G.$

If $\pi :{\mathfrak {g}}\to {\mathfrak {gl}}(V)$ for some vector space V is a representation, a representation Π of the connected component of G is defined by

This definition applies whether the resulting representation is projective or not.

#### Surjectiveness of exponential map for SO(3, 1)

From a practical point of view, it is important whether the first formula in (G2) can be used for all elements of the group . It holds for all $X\in {\mathfrak {g}}$ , however, in the general case, e.g. for ${\text{SL}}(2,\mathbb {C} )$ , not all g ∈ G are in the image of exp .

But $\exp :{\mathfrak {so}}(3;1)\to {\text{SO}}(3;1)^{+}$ is surjective. One way to show this is to make use of the isomorphism ${\text{SO}}(3;1)^{+}\cong {\text{PGL}}(2,\mathbb {C} ),$ the latter being the Möbius group . It is a quotient of ${\text{GL}}(n,\mathbb {C} )$ (see the linked article). The quotient map is denoted with $p:{\text{GL}}(n,\mathbb {C} )\to {\text{PGL}}(2,\mathbb {C} ).$ The map $\exp :{\mathfrak {gl}}(n,\mathbb {C} )\to {\text{GL}}(n,\mathbb {C} )$ is onto. Apply (Lie) with π being the differential of p at the identity. Then

$\forall X\in {\mathfrak {gl}}(n,\mathbb {C} ):\quad p(\exp(iX))=\exp(i\pi (X)).$

Since the left hand side is surjective (both exp and p are), the right hand side is surjective and hence $\exp :{\mathfrak {pgl}}(2,\mathbb {C} )\to {\text{PGL}}(2,\mathbb {C} )$ is surjective. Finally, recycle the argument once more, but now with the known isomorphism between SO(3; 1) + and ${\text{PGL}}(2,\mathbb {C} )$ to find that exp is onto for the connected component of the Lorentz group.

#### Fundamental group

The Lorentz group is doubly connected , i. e. π 1 (SO(3; 1)) is a group with two equivalence classes of loops as its elements.

To exhibit the fundamental group of SO(3; 1) + , the topology of its covering group ${\text{SL}}(2,\mathbb {C} )$ is considered. By the polar decomposition theorem , any matrix $\lambda \in {\text{SL}}(2,\mathbb {C} )$ may be uniquely expressed as

$\lambda =ue^{h},$

where u is unitary with determinant one, hence in SU(2) , and h is Hermitian with trace zero. The trace and determinant conditions imply: ${\begin{aligned}h&={\begin{pmatrix}c&a-ib\\a+ib&-c\end{pmatrix}}&&(a,b,c)\in \mathbb {R} ^{3}\\[4pt]u&={\begin{pmatrix}d+ie&f+ig\\-f+ig&d-ie\end{pmatrix}}&&(d,e,f,g)\in \mathbb {R} ^{4}{\text{ subject to }}d^{2}+e^{2}+f^{2}+g^{2}=1.\end{aligned}}$

The manifestly continuous one-to-one map is a homeomorphism with continuous inverse given by (the locus of u is identified with $\mathbb {S} ^{3}\subset \mathbb {R} ^{4}$ )

${\begin{cases}\mathbb {R} ^{3}\times \mathbb {S} ^{3}\to {\text{SL}}(2,\mathbb {C} )\\(r,s)\mapsto u(s)e^{h(r)}\end{cases}}$

explicitly exhibiting that ${\text{SL}}(2,\mathbb {C} )$ is simply connected. But ${\text{SO}}(3;1)\cong {\text{SL}}(2,\mathbb {C} )/\{\pm I\},$ where $\{\pm I\}$ is the center of ${\text{SL}}(2,\mathbb {C} )$ . Identifying λ and − λ amounts to identifying u with − u , which in turn amounts to identifying antipodal points on $\mathbb {S} ^{3}.$ Thus topologically, ${\text{SO}}(3;1)\cong \mathbb {R} ^{3}\times (\mathbb {S} ^{3}/\mathbb {Z} _{2}),$

where last factor is not simply connected: Geometrically, it is seen (for visualization purposes, $\mathbb {S} ^{3}$ may be replaced by $\mathbb {S} ^{2}$ ) that a path from u to − u in $SU(2)\cong \mathbb {S} ^{3}$ is a loop in $\mathbb {S} ^{3}/\mathbb {Z} _{2}$ since u and − u are antipodal points, and that it is not contractible to a point. But a path from u to − u , thence to u again, a loop in $\mathbb {S} ^{3}$ and a double loop (considering p ( ue h ) = p (− ue h ) , where $p:{\text{SL}}(2,\mathbb {C} )\to {\text{SO}}(3;1)$ is the covering map) in $\mathbb {S} ^{3}/\mathbb {Z} _{2}$ that is contractible to a point (continuously move away from − u "upstairs" in $\mathbb {S} ^{3}$ and shrink the path there to the point u ). Thus π 1 (SO(3; 1)) is a group with two equivalence classes of loops as its elements, or put more simply, SO(3; 1) is doubly connected .

#### Projective representations

Since π 1 (SO(3; 1) + ) has two elements, some representations of the Lie algebra will yield projective representations . Once it is known whether a representation is projective, formula (G2) applies to all group elements and all representations, including the projective ones — with the understanding that the representative of a group element will depend on which element in the Lie algebra (the X in (G2) ) is used to represent the group element in the standard representation.

For the Lorentz group, the ( m , n ) -representation is projective when m + n is a half-integer. See § Spinors .

For a projective representation Π of SO(3; 1) + , it holds that

since any loop in SO(3; 1) + traversed twice, due to the double connectedness, is contractible to a point, so that its homotopy class is that of a constant map. It follows that Π is a double-valued function. It is not possible to consistently choose a sign to obtain a continuous representation of all of SO(3; 1) + , but this is possible locally around any point.

### Covering group SL(2, C)

Consider ${\mathfrak {sl}}(2,\mathbb {C} )$ as a real Lie algebra with basis

$\left({\frac {1}{2}}\sigma _{1},{\frac {1}{2}}\sigma _{2},{\frac {1}{2}}\sigma _{3},{\frac {i}{2}}\sigma _{1},{\frac {i}{2}}\sigma _{2},{\frac {i}{2}}\sigma _{3}\right)\equiv (j_{1},j_{2},j_{3},k_{1},k_{2},k_{3}),$

where the sigmas are the Pauli matrices . From the relations

is obtained

which are exactly on the form of the 3 -dimensional version of the commutation relations for ${\mathfrak {so}}(3;1)$ (see conventions and Lie algebra bases below). Thus, the map J i ↔ j i , K i ↔ k i , extended by linearity is an isomorphism. Since ${\text{SL}}(2,\mathbb {C} )$ is simply connected, it is the universal covering group of SO(3; 1) + .

#### A geometric view

Let p g ( t ), 0 ≤ t ≤ 1 be a path from 1 ∈ SO(3; 1) + to g ∈ SO(3; 1) + , denote its homotopy class by [ p g ] and let π g be the set of all such homotopy classes. Define the set

and endow it with the multiplication operation

where $p_{12}$ is the path multiplication of $p_{1}$ and $p_{2}$ :

$p_{12}(t)=(p_{1}*p_{2})(t)={\begin{cases}p_{1}(2t)&0\leqslant t\leqslant {\tfrac {1}{2}}\\p_{2}(2t-1)&{\tfrac {1}{2}}\leqslant t\leqslant 1\end{cases}}$

With this multiplication, G becomes a group isomorphic to ${\text{SL}}(2,\mathbb {C} ),$ the universal covering group of SO(3; 1) + . Since each π g has two elements, by the above construction, there is a 2:1 covering map p : G → SO(3; 1) + . According to covering group theory, the Lie algebras ${\mathfrak {so}}(3;1),{\mathfrak {sl}}(2,\mathbb {C} )$ and ${\mathfrak {g}}$ of G are all isomorphic. The covering map p : G → SO(3; 1) + is simply given by p ( g , [ p g ]) = g .

#### An algebraic view

For an algebraic view of the universal covering group, let ${\text{SL}}(2,\mathbb {C} )$ act on the set of all Hermitian 2 × 2 matrices ${\mathfrak {h}}$ by the operation

The action on ${\mathfrak {h}}$ is linear. An element of ${\mathfrak {h}}$ may be written in the form

The map P is a group homomorphism into ${\text{GL}}({\mathfrak {h}})\subset {\text{End}}({\mathfrak {h}}).$ Thus $\mathbf {P} :{\text{SL}}(2,\mathbb {C} )\to {\text{GL}}({\mathfrak {h}})$ is a 4-dimensional representation of ${\text{SL}}(2,\mathbb {C} )$ . Its kernel must in particular take the identity matrix to itself, A † IA = A † A = I and therefore A † = A −1 . Thus AX = XA for A in the kernel so, by Schur's lemma , A is a multiple of the identity, which must be ± I since det A = 1 . The space ${\mathfrak {h}}$ is mapped to Minkowski space M 4 , via

The action of P ( A ) on ${\mathfrak {h}}$ preserves determinants. The induced representation p of ${\text{SL}}(2,\mathbb {C} )$ on $\mathbb {R} ^{4},$ via the above isomorphism, given by

preserves the Lorentz inner product since $-\det X=\xi _{1}^{2}+\xi _{2}^{2}+\xi _{3}^{2}-\xi _{4}^{2}=x^{2}+y^{2}+z^{2}-t^{2}.$

This means that p ( A ) belongs to the full Lorentz group SO(3; 1) . By the main theorem of connectedness , since ${\text{SL}}(2,\mathbb {C} )$ is connected, its image under p in SO(3; 1) is connected, and hence is contained in SO(3; 1) + .

It can be shown that the Lie map of $\mathbf {p} :{\text{SL}}(2,\mathbb {C} )\to {\text{SO}}(3;1)^{+},$ is a Lie algebra isomorphism: $\pi :{\mathfrak {sl}}(2,\mathbb {C} )\to {\mathfrak {so}}(3;1).$ The map P is also onto.

Thus ${\text{SL}}(2,\mathbb {C} )$ , since it is simply connected, is the universal covering group of SO(3; 1) + , isomorphic to the group G of above.

#### Non-surjectiveness of exponential mapping for SL(2, C)

The exponential mapping $\exp :{\mathfrak {sl}}(2,\mathbb {C} )\to {\text{SL}}(2,\mathbb {C} )$ is not onto. The matrix

is in ${\text{SL}}(2,\mathbb {C} ),$ but there is no $Q\in {\mathfrak {sl}}(2,\mathbb {C} )$ such that q = exp( Q ) .

In general, if g is an element of a connected Lie group G with Lie algebra ${\mathfrak {g}},$ then, by (Lie) ,

The matrix q can be written

### Realization of representations of SL(2, C) and sl(2, C) and their Lie algebras

The complex linear representations of ${\mathfrak {sl}}(2,\mathbb {C} )$ and ${\text{SL}}(2,\mathbb {C} )$ are more straightforward to obtain than the ${\mathfrak {so}}(3;1)^{+}$ representations. The holomorphic group representations (meaning the corresponding Lie algebra representation is complex linear) are related to the complex linear Lie algebra representations by exponentiation. The real linear representations of ${\mathfrak {sl}}(2,\mathbb {C} )$ are exactly the ( μ , ν ) -representations. They can be exponentiated too. The ( μ , 0) -representations are complex linear and are (isomorphic to) the highest weight-representations. These are usually indexed with only one integer (but half-integers are used here).

The mathematical convention is used in this section for convenience. Lie algebra elements differ by a factor of i , and there is no factor of i in the exponential mapping compared to the physics convention used elsewhere. Let the basis of ${\mathfrak {sl}}(2,\mathbb {C} )$ be

This choice of basis and the notation is standard in the mathematical literature.

#### Complex linear representations

The irreducible holomorphic ( n + 1) -dimensional representations ${\text{SL}}(2,\mathbb {C} ),n\geqslant 2,$ can be realized on the space of homogeneous polynomial of degree n in 2 variables $\mathbf {P} _{n}^{2},$ the elements of which are

$P{\begin{pmatrix}z_{1}\\z_{2}\\\end{pmatrix}}=c_{n}z_{1}^{n}+c_{n-1}z_{1}^{n-1}z_{2}+\cdots +c_{0}z_{2}^{n},\quad c_{0},c_{1},\ldots ,c_{n}\in \mathbb {Z} .$

The action of ${\text{SL}}(2,\mathbb {C} )$ is given by

The associated ${\mathfrak {sl}}(2,\mathbb {C} )$ -action is, using (G6) and the definition above, for the basis elements of ${\mathfrak {sl}}(2,\mathbb {C} ),$

With a choice of basis for $P\in \mathbf {P} _{n}^{2}$ , these representations become matrix Lie algebras.

#### Real linear representations

The ( μ , ν ) -representations are realized on a space of polynomials $\mathbf {P} _{\mu ,\nu }^{2}$ in $z_{1},{\overline {z_{1}}},z_{2},{\overline {z_{2}}},$ homogeneous of degree μ in $z_{1},z_{2}$ and homogeneous of degree ν in ${\overline {z_{1}}},{\overline {z_{2}}}.$ The representations are given by

By employing (G6) again it is found that

In particular for the basis elements,

### Properties of the ( m , n ) representations

The ( m , n ) representations, defined above via (A1) (as restrictions to the real form ${\mathfrak {sl}}(3,1)$ ) of tensor products of irreducible complex linear representations π m = μ and π n = ν of ${\mathfrak {sl}}(2,\mathbb {C} ),$ are irreducible, and they are the only irreducible representations.

- Irreducibility follows from the unitarian trick and that a representation Π of SU(2) × SU(2) is irreducible if and only if Π = Π μ ⊗ Π ν , where Π μ , Π ν are irreducible representations of SU(2) .

- Uniqueness follows from that the Π m are the only irreducible representations of SU(2) , which is one of the conclusions of the theorem of the highest weight.

#### Casimir operators

For the Lorentz Lie algebra, the Casimir operators are central elements of the universal enveloping algebra , hence by Schur's lemma they act by scalars on each irreducible representation. For the finite-dimensional theory it is convenient to pass to the complexification and use the decomposition ${\mathfrak {so}}(3,1)_{\mathbb {C} }\cong \mathbf {A} _{\mathbb {C} }\oplus \mathbf {B} _{\mathbb {C} },$ where each of $\mathbf {A} _{\mathbb {C} }$ and $\mathbf {B} _{\mathbb {C} }$ is a copy of ${\mathfrak {sl}}(2,\mathbb {C} )$ (treated here as ${\mathfrak {su}}(2)_{\mathbb {C} }$ , as above , with the generators $A_{i}$ and $B_{i}$ , respectively).

With this normalization, quadratic Casimirs for the two factors may be taken as $\Omega _{A}=A_{1}^{2}+A_{2}^{2}+A_{3}^{2},\qquad \Omega _{B}=B_{1}^{2}+B_{2}^{2}+B_{3}^{2}.$ Equivalently, if $A_{\pm }=A_{1}\pm iA_{2}$ and $B_{\pm }=B_{1}\pm iB_{2}$ , then $\Omega _{A}=A_{3}^{2}+{\frac {1}{2}}(A_{+}A_{-}+A_{-}A_{+}),\qquad \Omega _{B}=B_{3}^{2}+{\frac {1}{2}}(B_{+}B_{-}+B_{-}B_{+}).$ Since the two factors commute, $\Omega _{A}$ and $\Omega _{B}$ are central in the universal enveloping algebra of ${\mathfrak {so}}(3,1)_{\mathbb {C} }$ . A convenient normalized choice of algebraically independent quadratic Casimir operators for the Lorentz algebra is therefore $C_{1}=2(\Omega _{A}+\Omega _{B}),\qquad C_{2}=\Omega _{A}-\Omega _{B}.$

In terms of the rotation and boost generators, this becomes $C_{1}=\mathbf {J} ^{2}-\mathbf {K} ^{2},\qquad C_{2}=i\,\mathbf {J} \cdot \mathbf {K} .$ If (m,n) denotes the irreducible representation obtained from the spin- m representation of ${\mathfrak {a}}$ and the spin- n representation of ${\mathfrak {b}}$ , then $\Omega _{A}\mapsto m(m+1),\qquad \Omega _{B}\mapsto n(n+1),$ and hence $C_{1}\mapsto 2{\bigl (}m(m+1)+n(n+1){\bigr )},\qquad C_{2}\mapsto m(m+1)-n(n+1).$ In particular, the conjugate pair (m,n) and (n,m) have the same value of $C_{1}$ but opposite values of $C_{2}$ ; when m=n , the second Casimir vanishes.

#### Dimension

The ( m , n ) representations are (2 m + 1)(2 n + 1) -dimensional. This follows easiest from counting the dimensions in any concrete realization, such as the one given in representations of ${\text{SL}}(2,\mathbb {C} )$ and ${\mathfrak {sl}}(2,\mathbb {C} )$ . For a Lie general algebra ${\mathfrak {g}}$ the Weyl dimension formula , $\dim \pi _{\rho }={\frac {\Pi _{\alpha \in R^{+}}\langle \alpha ,\rho +\delta \rangle }{\Pi _{\alpha \in R^{+}}\langle \alpha ,\delta \rangle }},$ applies, where R + is the set of positive roots, ρ is the highest weight, and δ is half the sum of the positive roots. The inner product $\langle \cdot ,\cdot \rangle$ is that of the Lie algebra ${\mathfrak {g}},$ invariant under the action of the Weyl group on ${\mathfrak {h}}\subset {\mathfrak {g}},$ the Cartan subalgebra . The roots (really elements of ${\mathfrak {h}}^{*}$ ) are via this inner product identified with elements of ${\mathfrak {h}}.$ For ${\mathfrak {sl}}(2,\mathbb {C} ),$ the formula reduces to dim π μ = 2 μ + 1 = 2 m + 1 , where the present notation must be taken into account . The highest weight is 2 μ . By taking tensor products, the result follows.

#### Faithfulness

If a (nontrivial) representation Π of a Lie group G is not faithful, then N = ker Π is a nontrivial normal subgroup. There are three relevant cases.

- N is non-discrete and abelian .

- N is non-discrete and non-abelian.

- N is discrete. In this case N ⊂ Z , where Z is the center of G .

In the case of SO(3; 1) + , the first case is excluded since SO(3; 1) + is semi-simple. The second case (and the first case) is excluded because SO(3; 1) + is simple. For the third case, SO(3; 1) + is isomorphic to the quotient ${\text{SL}}(2,\mathbb {C} )/\{\pm I\}.$ But $\{\pm I\}$ is the center of ${\text{SL}}(2,\mathbb {C} ).$ It follows that the center of SO(3; 1) + is trivial, and this excludes the third case. The conclusion is that every representation Π : SO(3; 1) + → GL( V ) and every projective representation Π : SO(3; 1) + → PGL( W ) for V , W finite-dimensional vector spaces are faithful.

By using the fundamental Lie correspondence, the statements and the reasoning above translate directly to Lie algebras with (abelian) nontrivial non-discrete normal subgroups replaced by (one-dimensional) nontrivial ideals in the Lie algebra, and the center of SO(3; 1) + replaced by the center of ${\mathfrak {sl}}(3;1)^{+}$ The center of any semisimple Lie algebra is trivial and ${\mathfrak {so}}(3;1)$ is semi-simple and simple, and hence has no non-trivial ideals.

A related fact is that if the corresponding representation of ${\text{SL}}(2,\mathbb {C} )$ is faithful, then the representation is projective. Conversely, if the representation is non-projective, then the corresponding ${\text{SL}}(2,\mathbb {C} )$ representation is not faithful, but is 2:1 .

#### Non-unitarity

The ( m , n ) Lie algebra representation is not Hermitian . Accordingly, the corresponding (projective) representation of the group is never unitary . This is due to the non-compactness of the Lorentz group. In fact, a connected simple non-compact Lie group cannot have any nontrivial unitary finite-dimensional representations. There is a topological proof of this. Let u : G → GL( V ) , where V is finite-dimensional, be a continuous unitary representation of the non-compact connected simple Lie group G . Then u ( G ) ⊂ U( V ) ⊂ GL( V ) where U( V ) is the compact subgroup of GL( V ) consisting of unitary transformations of V . The kernel of u is a normal subgroup of G . Since G is simple, ker u is either all of G , in which case u is trivial, or ker u is trivial, in which case u is faithful . In the latter case u is a diffeomorphism onto its image, u ( G ) ≅ G and u ( G ) is a Lie group. This would mean that u ( G ) is an embedded non-compact Lie subgroup of the compact group U( V ) . This is impossible with the subspace topology on u ( G ) ⊂ U( V ) since all embedded Lie subgroups of a Lie group are closed If u ( G ) were closed, it would be compact, and then G would be compact, contrary to assumption.

In the case of the Lorentz group, this can also be seen directly from the definitions. The representations of A and B used in the construction are Hermitian. This means that J is Hermitian, but K is anti-Hermitian . The non-unitarity is not a problem in quantum field theory, since the objects of concern are not required to have a Lorentz-invariant positive definite norm.

#### Restriction to SO(3)

The ( m , n ) representation is, however, unitary when restricted to the rotation subgroup SO(3) , but these representations are not irreducible as representations of SO(3). A Clebsch–Gordan decomposition can be applied showing that an ( m , n ) representation have SO(3) -invariant subspaces of highest weight (spin) m + n , m + n − 1, ..., | m − n | , where each possible highest weight (spin) occurs exactly once. A weight subspace of highest weight (spin) j is (2 j + 1) -dimensional. So for example, the ( ⁠ 1 / 2 ⁠ , ⁠ 1 / 2 ⁠ ) representation has spin 1 and spin 0 subspaces of dimension 3 and 1 respectively.

Since the angular momentum operator is given by J = A + B , the highest spin in quantum mechanics of the rotation sub-representation will be ( m + n )ℏ and the "usual" rules of addition of angular momenta and the formalism of 3-j symbols , 6-j symbols , etc. applies.

#### Spinors

It is the SO(3) -invariant subspaces of the irreducible representations that determine whether a representation has spin. From the above paragraph, it is seen that the ( m , n ) representation has spin if m + n is half-integer. The simplest are ( ⁠ 1 / 2 ⁠ , 0) and (0, ⁠ 1 / 2 ⁠ ) , the Weyl-spinors of dimension 2 . Then, for example, (0, ⁠ 3 / 2 ⁠ ) and (1, ⁠ 1 / 2 ⁠ ) are a spin representations of dimensions 2⋅ ⁠ 3 / 2 ⁠ + 1 = 4 and (2 + 1)(2⋅ ⁠ 1 / 2 ⁠ + 1) = 6 respectively. According to the above paragraph, there are subspaces with spin both ⁠ 3 / 2 ⁠ and ⁠ 1 / 2 ⁠ in the last two cases, so these representations cannot likely represent a single physical particle which must be well-behaved under SO(3) . It cannot be ruled out in general, however, that representations with multiple SO(3) subrepresentations with different spin can represent physical particles with well-defined spin. It may be that there is a suitable relativistic wave equation that projects out unphysical components , leaving only a single spin.

Construction of pure spin ⁠ n / 2 ⁠ representations for any n (under SO(3) ) from the irreducible representations involves taking tensor products of the Dirac-representation with a non-spin representation, extraction of a suitable subspace, and finally imposing differential constraints.

#### Dual representations

The following theorems are applied to examine whether the dual representation of an irreducible representation is isomorphic to the original representation:

- The set of weights of the dual representation of an irreducible representation of a semisimple Lie algebra is, including multiplicities, the negative of the set of weights for the original representation.

- Two irreducible representations are isomorphic if and only if they have the same highest weight .

- For each semisimple Lie algebra there exists a unique element w 0 of the Weyl group such that if μ is a dominant integral weight, then w 0 ⋅ (− μ ) is again a dominant integral weight.

- If $\pi _{\mu _{0}}$ is an irreducible representation with highest weight μ 0 , then $\pi _{\mu _{0}}^{*}$ has highest weight w 0 ⋅ (− μ ) .

Here, the elements of the Weyl group are considered as orthogonal transformations, acting by matrix multiplication, on the real vector space of roots . If − I is an element of the Weyl group of a semisimple Lie algebra, then w 0 = − I . In the case of ${\mathfrak {sl}}(2,\mathbb {C} ),$ the Weyl group is W = { I , − I } . It follows that each π μ , μ = 0, 1, ... is isomorphic to its dual $\pi _{\mu }^{*}.$ The root system of ${\mathfrak {sl}}(2,\mathbb {C} )\oplus {\mathfrak {sl}}(2,\mathbb {C} )$ is shown in the figure to the right. The Weyl group is generated by $\{w_{\gamma }\}$ where $w_{\gamma }$ is reflection in the plane orthogonal to γ as γ ranges over all roots. Inspection shows that w α ⋅ w β = − I so − I ∈ W . Using the fact that if π , σ are Lie algebra representations and π ≅ σ , then Π ≅ Σ , the conclusion for SO(3; 1) + is $\pi _{m,n}^{*}\cong \pi _{m,n},\quad \Pi _{m,n}^{*}\cong \Pi _{m,n},\quad 2m,2n\in \mathbf {N} .$

#### Complex conjugate representations

If π is a representation of a Lie algebra, then ${\overline {\pi }}$ is a representation, where the bar denotes entry-wise complex conjugation in the representative matrices. This follows from that complex conjugation commutes with addition and multiplication. In general, every irreducible representation π of ${\mathfrak {sl}}(n,\mathbb {C} )$ can be written uniquely as π = π + + π − , where $\pi ^{\pm }(X)={\frac {1}{2}}\left(\pi (X)\pm i\pi \left(i^{-1}X\right)\right),$ with $\pi ^{+}$ holomorphic (complex linear) and $\pi ^{-}$ anti-holomorphic (conjugate linear). For ${\mathfrak {sl}}(2,\mathbb {C} ),$ since $\pi _{\mu }$ is holomorphic, ${\overline {\pi _{\mu }}}$ is anti-holomorphic. Direct examination of the explicit expressions for $\pi _{\mu ,0}$ and $\pi _{0,\nu }$ in equation (S8) below shows that they are holomorphic and anti-holomorphic respectively. Closer examination of the expression (S8) also allows for identification of $\pi ^{+}$ and $\pi ^{-}$ for $\pi _{\mu ,\nu }$ as $\pi _{\mu ,\nu }^{+}=\pi _{\mu }^{\oplus _{\nu +1}},\qquad \pi _{\mu ,\nu }^{-}={\overline {\pi _{\nu }^{\oplus _{\mu +1}}}}.$

Using the above identities (interpreted as pointwise addition of functions), for SO(3; 1) + yields ${\begin{aligned}{\overline {\pi _{m,n}}}&={\overline {\pi _{m,n}^{+}+\pi _{m,n}^{-}}}={\overline {\pi _{m}^{\oplus _{2n+1}}}}+{\overline {{\overline {\pi _{n}}}^{\oplus _{2m+1}}}}\\&=\pi _{n}^{\oplus _{2m+1}}+{\overline {\pi _{m}}}^{\oplus _{2n+1}}=\pi _{n,m}^{+}+\pi _{n,m}^{-}=\pi _{n,m}\\&&&2m,2n\in \mathbb {N} \\{\overline {\Pi _{m,n}}}&=\Pi _{n,m}\end{aligned}}$ where the statement for the group representations follow from exp( X ) = exp( X ) . It follows that the irreducible representations ( m , n ) have real matrix representatives if and only if m = n . Reducible representations on the form ( m , n ) ⊕ ( n , m ) have real matrices too.

### Adjoint representation, Clifford algebra, and Dirac spinor representation

In general representation theory, if ( π , V ) is a representation of a Lie algebra ${\mathfrak {g}},$ then there is an associated representation of ${\mathfrak {g}},$ on End ( V ) , also denoted π , given by

Likewise, a representation (Π, V ) of a group G yields a representation Π on End( V ) of G , still denoted Π , given by

If π and Π are the standard representations on $\mathbb {R} ^{4}$ and if the action is restricted to ${\mathfrak {so}}(3,1)\subset {\text{End}}(\mathbb {R} ^{4}),$ then the two above representations are the adjoint representation of the Lie algebra and the adjoint representation of the group respectively. The corresponding representations (some $\mathbb {R} ^{n}$ or $\mathbb {C} ^{n}$ ) always exist for any matrix Lie group, and are paramount for investigation of the representation theory in general, and for any given Lie group in particular.

Applying this to the Lorentz group, if (Π, V ) is a projective representation, then direct calculation using (G5) shows that the induced representation on End( V ) is a proper representation, i.e. a representation without phase factors.

In quantum mechanics this means that if ( π , H ) or (Π, H ) is a representation acting on some Hilbert space H , then the corresponding induced representation acts on the set of linear operators on H . As an example, the induced representation of the projective spin ( ⁠ 1 / 2 ⁠ , 0) ⊕ (0, ⁠ 1 / 2 ⁠ ) representation on End( H ) is the non-projective 4-vector ( ⁠ 1 / 2 ⁠ , ⁠ 1 / 2 ⁠ ) representation.

For simplicity, consider only the "discrete part" of End( H ) , that is, given a basis for H , the set of constant matrices of various dimension, including possibly infinite dimensions. The induced 4-vector representation of above on this simplified End( H ) has an invariant 4-dimensional subspace that is spanned by the four gamma matrices . (The metric convention is different in the linked article.) In a corresponding way, the complete Clifford algebra of spacetime , ${\mathcal {Cl}}_{3,1}(\mathbb {R} ),$ whose complexification is ${\text{M}}(4,\mathbb {C} ),$ generated by the gamma matrices decomposes as a direct sum of representation spaces of a scalar irreducible representation (irrep), the (0, 0) , a pseudoscalar irrep, also the (0, 0) , but with parity inversion eigenvalue −1 , see the next section below, the already mentioned vector irrep, ( ⁠ 1 / 2 ⁠ , ⁠ 1 / 2 ⁠ ) , a pseudovector irrep, ( ⁠ 1 / 2 ⁠ , ⁠ 1 / 2 ⁠ ) with parity inversion eigenvalue +1 (not −1), and a tensor irrep, (1, 0) ⊕ (0, 1) . The dimensions add up to 1 + 1 + 4 + 4 + 6 = 16 . In other words,

where, as is customary , a representation is confused with its representation space.

#### ( ⁠ 1 / 2 ⁠ , 0) ⊕ (0, ⁠ 1 / 2 ⁠ ) spin representation

The six-dimensional representation space of the tensor (1, 0) ⊕ (0, 1) -representation inside ${\mathcal {Cl}}_{3,1}(\mathbb {R} )$ has two roles. The

where $\gamma ^{0},\ldots ,\gamma ^{3}\in {\mathcal {Cl}}_{3,1}(\mathbb {R} )$ are the gamma matrices, the sigmas, only 6 of which are non-zero due to antisymmetry of the bracket, span the tensor representation space. Moreover, they have the commutation relations of the Lorentz Lie algebra,

and hence constitute a representation (in addition to spanning a representation space) sitting inside ${\mathcal {Cl}}_{3,1}(\mathbb {R} ),$ the ( ⁠ 1 / 2 ⁠ , 0) ⊕ (0, ⁠ 1 / 2 ⁠ ) spin representation. For details, see Dirac spinor and Dirac algebra .

The conclusion is that every element of the complexified ${\mathcal {Cl}}_{3,1}(\mathbb {R} )$ in End( H ) (i.e. every complex 4 × 4 matrix) has well defined Lorentz transformation properties. In addition, it has a spin-representation of the Lorentz Lie algebra, which upon exponentiation becomes a spin representation of the group, acting on $\mathbb {C} ^{4},$ making it a space of Dirac spinors.

### Reducible representations

Other representations can be deduced from the irreducible ones, such as those obtained by taking direct sums, tensor products, and quotients of the irreducible representations. Other methods of obtaining representations include the restriction of a representation of a larger group containing the Lorentz group, e.g. ${\text{GL}}(n,\mathbb {R} )$ and the Poincaré group. These representations are in general not irreducible.

The Lorentz group and its Lie algebra have the complete reducibility property . This means that every representation reduces to a direct sum of irreducible representations.

### Space inversion and time reversal

The (possibly projective) ( m , n ) representation is irreducible as a representation SO(3; 1) + , the identity component of the Lorentz group, in physics terminology the proper orthochronous Lorentz group. If m = n it can be extended to a representation of all of O(3; 1) , the full Lorentz group, including space parity inversion and time reversal . The representations ( m , n ) ⊕ ( n , m ) can be extended likewise.

#### Space parity inversion

For space parity inversion, the adjoint action Ad P of P ∈ SO(3; 1) on ${\mathfrak {so}}(3;1)$ is considered, where P is the standard representative of space parity inversion, P = diag(1, −1, −1, −1) , given by

It is these properties of K and J under P that motivate the terms vector for K and pseudovector or axial vector for J . In a similar way, if π is any representation of ${\mathfrak {so}}(3;1)$ and Π is its associated group representation, then Π(SO(3; 1) + ) acts on the representation of π by the adjoint action, π ( X ) ↦ Π( g ) π ( X ) Π( g ) −1 for $X\in {\mathfrak {so}}(3;1),$ g ∈ SO(3; 1) + . If P is to be included in Π , then consistency with (F1) requires that

holds, where A and B are defined as in the first section. This can hold only if A i and B i have the same dimensions, i.e. only if m = n . When m ≠ n then ( m , n ) ⊕ ( n , m ) can be extended to an irreducible representation of SO(3; 1) + , the orthochronous Lorentz group. The parity reversal representative Π( P ) does not come automatically with the general construction of the ( m , n ) representations. It must be specified separately. The matrix β = i γ 0 (or a multiple of modulus −1 times it) may be used in the ( ⁠ 1 / 2 ⁠ , 0) ⊕ (0, ⁠ 1 / 2 ⁠ ) representation.

If parity is included with a minus sign (the 1×1 matrix [−1] ) in the (0,0) representation, it is called a pseudoscalar representation.

#### Time reversal

Time reversal T = diag(−1, 1, 1, 1) , acts similarly on ${\mathfrak {so}}(3;1)$ by

By explicitly including a representative for T , as well as one for P , a representation of the full Lorentz group O(3; 1) is obtained. A subtle problem appears however in application to physics, in particular quantum mechanics. When considering the full Poincaré group , four more generators, the P μ , in addition to the J i and K i generate the group. These are interpreted as generators of translations. The time-component P 0 is the Hamiltonian H . The operator T satisfies the relation

in analogy to the relations above with ${\mathfrak {so}}(3;1)$ replaced by the full Poincaré algebra . By just cancelling the i 's, the result THT −1 = − H would imply that for every state Ψ with positive energy E in a Hilbert space of quantum states with time-reversal invariance, there would be a state Π( T −1 )Ψ with negative energy − E . Such states do not exist. The operator Π( T ) is therefore chosen antilinear and antiunitary , so that it anticommutes with i , resulting in THT −1 = H , and its action on Hilbert space likewise becomes antilinear and antiunitary. It may be expressed as the composition of complex conjugation with multiplication by a unitary matrix. This is mathematically sound, see Wigner's theorem , but Π( T ) is then antiunitary rather than a complex-linear representation operator.

When constructing theories such as QED which is invariant under space parity and time reversal, Dirac spinors may be used, while theories that do not, such as the electroweak force , must be formulated in terms of Weyl spinors. The Dirac representation, ( ⁠ 1 / 2 ⁠ , 0) ⊕ (0, ⁠ 1 / 2 ⁠ ) , is usually taken to include both space parity and time inversions. Without space parity inversion, it is a reducible rather than irreducible representation.

The third discrete symmetry entering in the CPT theorem along with P and T , charge conjugation symmetry C , has nothing directly to do with Lorentz invariance.

## Action on function spaces

If V is a vector space of functions of a finite number of variables n , then the action on a scalar function $f\in V$ given by

produces another function Π f ∈ V . Here Π x is an n -dimensional representation, and Π is a possibly infinite-dimensional representation. A special case of this construction is when V is a space of functions defined on the a linear group G itself, viewed as a n -dimensional manifold embedded in $\mathbb {R} ^{m^{2}}$ (with m the dimension of the matrices). This is the setting in which the Peter–Weyl theorem and the Borel–Weil theorem are formulated. The former demonstrates the existence of a Fourier decomposition of functions on a compact group into characters of finite-dimensional representations. The latter theorem, providing more explicit representations, makes use of the unitarian trick to yield representations of complex non-compact groups, e.g. ${\text{SL}}(2,\mathbb {C} ).$

The following exemplifies action of the Lorentz group and the rotation subgroup on some function spaces.

### Euclidean rotations

The subgroup SO(3) of three-dimensional Euclidean rotations has an infinite-dimensional representation on the Hilbert space $L^{2}\left(\mathbb {S} ^{2}\right)=\operatorname {span} \left\{Y_{m}^{l},l\in \mathbb {N} ^{+},-l\leqslant m\leqslant l\right\},$

where $Y_{m}^{l}$ are the spherical harmonics . An arbitrary square integrable function f on the unit sphere can be expressed as

where the f lm are generalized Fourier coefficients .

The Lorentz group action restricts to that of SO(3) and is expressed as

where the D l are obtained from the representatives of odd dimension of the generators of rotation.

### Möbius group

The identity component of the Lorentz group is isomorphic to the Möbius group M . This group can be thought of as conformal mappings of either the complex plane or, via stereographic projection , the Riemann sphere . In this way, the Lorentz group itself can be thought of as acting conformally on the complex plane or on the Riemann sphere.

In the plane, a Möbius transformation characterized by the complex numbers a , b , c , d acts on the plane according to

and can be represented by complex matrices

since multiplication by a nonzero complex scalar does not change f . These are elements of ${\text{SL}}(2,\mathbb {C} )$ and are unique up to a sign (since ±Π f give the same f ), hence ${\text{SL}}(2,\mathbb {C} )/\{\pm I\}\cong {\text{SO}}(3;1)^{+}.$

### Riemann P-functions

The Riemann P-functions , solutions of Riemann's differential equation, are an example of a set of functions that transform among themselves under the action of the Lorentz group. The Riemann P-functions are expressed as

where the a , b , c , α , β , γ , α′ , β′ , γ′ are complex constants. The P-function on the right hand side can be expressed using standard hypergeometric functions . The connection is

The set of constants 0, ∞, 1 in the upper row on the left hand side are the regular singular points of the Gauss' hypergeometric equation . Its exponents , i. e. solutions of the indicial equation , for expansion around the singular point 0 are 0 and 1 − c ,corresponding to the two linearly independent solutions, and for expansion around the singular point 1 they are 0 and c − a − b . Similarly, the exponents for ∞ are a and b for the two solutions.

One has thus

where the condition (sometimes called Riemann's identity) $\alpha +\alpha '+\beta +\beta '+\gamma +\gamma '=1$ on the exponents of the solutions of Riemann's differential equation has been used to define γ ′ .

The first set of constants on the left hand side in (T1) , a , b , c denotes the regular singular points of Riemann's differential equation. The second set, α , β , γ , are the corresponding exponents at a , b , c for one of the two linearly independent solutions, and, accordingly, α′ , β′ , γ′ are exponents at a , b , c for the second solution.

Define an action of the Lorentz group on the set of all Riemann P-functions by first setting

where A , B , C , D are the entries in

for Λ = p ( λ ) ∈ SO(3; 1) + a Lorentz transformation.

Define

where P is a Riemann P-function. The resulting function is again a Riemann P-function. The effect of the Möbius transformation of the argument is that of shifting the poles to new locations, hence changing the critical points, but there is no change in the exponents of the differential equation the new function satisfies. The new function is expressed as

where

## Infinite-dimensional unitary representations

### History

The Lorentz group SO(3; 1) + and its double cover ${\text{SL}}(2,\mathbb {C} )$ also have infinite dimensional unitary representations, studied independently by Bargmann (1947) , Gelfand & Naimark (1947) and Harish-Chandra (1947) at the instigation of Paul Dirac . This trail of development begun with Dirac (1936) where he devised matrices U and B necessary for description of higher spin (compare Dirac matrices ), elaborated upon by Fierz (1939) , see also Fierz & Pauli (1939) , and proposed precursors of the Bargmann-Wigner equations . In Dirac (1945) he proposed a concrete infinite-dimensional representation space whose elements were called expansors as a generalization of tensors. These ideas were incorporated by Harish–Chandra and expanded with expinors as an infinite-dimensional generalization of spinors in his 1947 paper.

The Plancherel formula for these groups was first obtained by Gelfand and Naimark through involved calculations. The treatment was subsequently considerably simplified by Harish-Chandra (1951) and Gelfand & Graev (1953) , based on an analogue for ${\text{SL}}(2,\mathbb {C} )$ of the integration formula of Hermann Weyl for compact Lie groups . Elementary accounts of this approach can be found in Rühl (1970) and Knapp (2001) .

The theory of spherical functions for the Lorentz group, required for harmonic analysis on the hyperboloid model of 3-dimensional hyperbolic space sitting in Minkowski space is considerably easier than the general theory. It only involves representations from the spherical principal series and can be treated directly, because in radial coordinates the Laplacian on the hyperboloid is equivalent to the Laplacian on $\mathbb {R} .$ This theory is discussed in Takahashi (1963) , Helgason (1968) , Helgason (2000) and the posthumous text of Jorgenson & Lang (2008) .

### Principal series for SL(2, C)

The principal series , or unitary principal series , are the unitary representations induced from the one-dimensional representations of the lower triangular subgroup B of $G={\text{SL}}(2,\mathbb {C} ).$ Since the one-dimensional representations of B correspond to the representations of the diagonal matrices, with non-zero complex entries z and z −1 , they thus have the form $\chi _{\nu ,k}{\begin{pmatrix}z&0\\c&z^{-1}\end{pmatrix}}=r^{i\nu }e^{ik\theta },$ for k an integer, ν real and with z = re iθ . The representations are irreducible ; the only repetitions, i.e. isomorphisms of representations, occur when k is replaced by − k . By definition the representations are realized on L 2 sections of line bundles on $G/B=\mathbb {S} ^{2},$ which is isomorphic to the Riemann sphere . When k = 0 , these representations constitute the so-called spherical principal series .

The restriction of a principal series to the maximal compact subgroup K = SU(2) of G can also be realized as an induced representation of K using the identification G / B = K / T , where T = B ∩ K is the maximal torus in K consisting of diagonal matrices with | z | = 1 . It is the representation induced from the 1-dimensional representation z k T , and is independent of ν . By Frobenius reciprocity , on K they decompose as a direct sum of the irreducible representations of K with dimensions | k | + 2 m + 1 with m a non-negative integer.

Using the identification between the Riemann sphere minus a point and $\mathbb {C} ,$ the principal series can be defined directly on $L^{2}(\mathbb {C} )$ by the formula $\pi _{\nu ,k}{\begin{pmatrix}a&b\\c&d\end{pmatrix}}^{-1}f(z)=|cz+d|^{-2-i\nu }\left({cz+d \over |cz+d|}\right)^{-k}f\left({az+b \over cz+d}\right).$

Irreducibility can be checked in a variety of ways:

- The representation is already irreducible on B . This can be seen directly, but is also a special case of general results on irreducibility of induced representations due to François Bruhat and George Mackey , relying on the Bruhat decomposition G = B ∪ BsB where s is the Weyl group element ${\begin{pmatrix}0&-1\\1&0\end{pmatrix}}$ .

- The action of the Lie algebra ${\mathfrak {g}}$ of G can be computed on the algebraic direct sum of the irreducible subspaces of K can be computed explicitly and the it can be verified directly that the lowest-dimensional subspace generates this direct sum as a ${\mathfrak {g}}$ -module.

### Complementary series for SL(2, C)

The for 0 < t < 2 , the complementary series is defined on $L^{2}(\mathbb {C} )$ for the inner product $(f,g)_{t}=\iint {\frac {f(z){\overline {g(w)}}}{|z-w|^{2-t}}}\,dz\,dw,$ with the action given by $\pi _{t}{\begin{pmatrix}a&b\\c&d\end{pmatrix}}^{-1}f(z)=|cz+d|^{-2-t}f\left({az+b \over cz+d}\right).$

The representations in the complementary series are irreducible and pairwise non-isomorphic. As a representation of K , each is isomorphic to the Hilbert space direct sum of all the odd dimensional irreducible representations of K = SU(2) . Irreducibility can be proved by analyzing the action of ${\mathfrak {g}}$ on the algebraic sum of these subspaces or directly without using the Lie algebra.

### Plancherel theorem for SL(2, C)

The only irreducible unitary representations of ${\text{SL}}(2,\mathbb {C} )$ are the principal series, the complementary series and the trivial representation.
Since − I acts as (−1) k on the principal series and trivially on the remainder, these will give all the irreducible unitary representations of the Lorentz group, provided k is taken to be even.

To decompose the left regular representation of G on $L^{2}(G)$ only the principal series are required. This immediately yields the decomposition on the subrepresentations $L^{2}(G/\{\pm I\}),$ the left regular representation of the Lorentz group, and $L^{2}(G/K),$ the regular representation on 3-dimensional hyperbolic space. (The former only involves principal series representations with k even and the latter only those with k = 0 .)

The left and right regular representation λ and ρ are defined on $L^{2}(G)$ by ${\begin{aligned}(\lambda (g)f)(x)&=f\left(g^{-1}x\right)\\(\rho (g)f)(x)&=f(xg)\end{aligned}}$

Now if f is an element of C c ( G ) , the operator $\pi _{\nu ,k}(f)$ defined by $\pi _{\nu ,k}(f)=\int _{G}f(g)\pi (g)\,dg$ is Hilbert–Schmidt . Define a Hilbert space H by $H=\bigoplus _{k\geqslant 0}{\text{HS}}\left(L^{2}(\mathbb {C} )\right)\otimes L^{2}\left(\mathbb {R} ,c_{k}{\sqrt {\nu ^{2}+k^{2}}}d\nu \right),$ where $c_{k}={\begin{cases}{\frac {1}{4\pi ^{3/2}}}&k=0\\{\frac {1}{(2\pi )^{3/2}}}&k\neq 0\end{cases}}$ and ${\text{HS}}\left(L^{2}(\mathbb {C} )\right)$ denotes the Hilbert space of Hilbert–Schmidt operators on $L^{2}(\mathbb {C} ).$ Then the map U defined on C c ( G ) by $U(f)(\nu ,k)=\pi _{\nu ,k}(f)$ extends to a unitary of $L^{2}(G)$ onto H .

The map U satisfies the intertwining property $U(\lambda (x)\rho (y)f)(\nu ,k)=\pi _{\nu ,k}(x)^{-1}\pi _{\nu ,k}(f)\pi _{\nu ,k}(y).$

If f 1 , f 2 are in C c ( G ) then by unitarity $(f_{1},f_{2})=\sum _{k\geqslant 0}c_{k}^{2}\int _{-\infty }^{\infty }\operatorname {Tr} \left(\pi _{\nu ,k}(f_{1})\pi _{\nu ,k}(f_{2})^{*}\right)\left(\nu ^{2}+k^{2}\right)\,d\nu .$

Thus if $f=f_{1}*f_{2}^{*}$ denotes the convolution of $f_{1}$ and $f_{2}^{*},$ and $f_{2}^{*}(g)={\overline {f_{2}(g^{-1})}},$ then $f(1)=\sum _{k\geqslant 0}c_{k}^{2}\int _{-\infty }^{\infty }\operatorname {Tr} \left(\pi _{\nu ,k}(f)\right)\left(\nu ^{2}+k^{2}\right)\,d\nu .$

The last two displayed formulas are usually referred to as the Plancherel formula and the Fourier inversion formula respectively.

The Plancherel formula extends to all $f_{i}\in L^{2}(G).$ By a theorem of Jacques Dixmier and Paul Malliavin , every smooth compactly supported function on $G$ is a finite sum of convolutions of similar functions, the inversion formula holds for such f . It can be extended to much wider classes of functions satisfying mild differentiability conditions.

### Classification of representations of SO(3, 1)

The strategy followed in the classification of the irreducible infinite-dimensional representations is, in analogy to the finite-dimensional case, to assume they exist, and to investigate their properties. Thus first assume that an irreducible strongly continuous infinite-dimensional representation Π H on a Hilbert space H of SO(3; 1) + is at hand. Since SO(3) is a subgroup, Π H is a representation of it as well. Each irreducible subrepresentation of SO(3) is finite-dimensional, and the SO(3) representation is reducible into a direct sum of irreducible finite-dimensional unitary representations of SO(3) if Π H is unitary.

The steps are the following:

- Choose a suitable basis of common eigenvectors of J 2 and J 3 .

- Compute matrix elements of J 1 , J 2 , J 3 and K 1 , K 2 , K 3 .

- Enforce Lie algebra commutation relations.

- Require unitarity together with orthonormality of the basis.

#### Step 1

One suitable choice of basis and labeling is given by $\left|j_{0}\,j_{1};j\,m\right\rangle .$

If this were a finite-dimensional representation, then j 0 would correspond the lowest occurring eigenvalue j ( j + 1) of J 2 in the representation, equal to | m − n | , and j 1 would correspond to the highest occurring eigenvalue, equal to m + n . In the infinite-dimensional case, j 0 ≥ 0 retains this meaning, but j 1 does not. For simplicity, it is assumed that a given j occurs at most once in a given representation (this is the case for finite-dimensional representations), and it can be shown that the assumption is possible to avoid (with a slightly more complicated calculation) with the same results.

#### Step 2

The next step is to compute the matrix elements of the operators J 1 , J 2 , J 3 and K 1 , K 2 , K 3 forming the basis of the Lie algebra of ${\mathfrak {so}}(3;1).$ The matrix elements of $J_{\pm }=J_{1}\pm iJ_{2}$ and $J_{3}$ (the complexified Lie algebra is understood) are known from the representation theory of the rotation group, and are given by ${\begin{aligned}\left\langle j\,m\right|J_{+}\left|j\,m-1\right\rangle =\left\langle j\,m-1\right|J_{-}\left|j\,m\right\rangle &={\sqrt {(j+m)(j-m+1)}},\\\left\langle j\,m\right|J_{3}\left|j\,m\right\rangle &=m,\end{aligned}}$ where the labels j 0 and j 1 have been dropped since they are the same for all basis vectors in the representation.

Due to the commutation relations $[J_{i},K_{j}]=i\epsilon _{ijk}K_{k},$ the triple ( K 1 , K 2 , K 3 ) ≡ K is a vector operator and the Wigner–Eckart theorem applies for computation of matrix elements between the states represented by the chosen basis. The matrix elements of ${\begin{aligned}K_{0}^{(1)}&=K_{3},\\K_{\pm 1}^{(1)}&=\mp {\frac {1}{\sqrt {2}}}(K_{1}\pm iK_{2}),\end{aligned}}$

where the superscript (1) signifies that the defined quantities are the components of a spherical tensor operator of rank k = 1 (which explains the factor √ 2 as well) and the subscripts 0, ±1 are referred to as q in formulas below, are given by ${\begin{aligned}\left\langle j'm'\left|K_{0}^{(1)}\right|j\,m\right\rangle &=\left\langle j'\,m'\,k=1\,q=0|j\,m\right\rangle \left\langle j\left\|K^{(1)}\right\|j'\right\rangle ,\\\left\langle j'm'\left|K_{\pm 1}^{(1)}\right|j\,m\right\rangle &=\left\langle j'\,m'\,k=1\,q=\pm 1|j\,m\right\rangle \left\langle j\left\|K^{(1)}\right\|j'\right\rangle .\end{aligned}}$

Here, the first factors on the right-hand sides are Clebsch–Gordan coefficients for coupling j ′ with k to get j . The second factors are the reduced matrix elements . They do not depend on m , m ′ or q , but depend on j , j ′ and, of course, K .

#### Step 3

The next step is to demand that the Lie algebra relations hold, i.e. that $[K_{\pm },K_{3}]=\pm J_{\pm },\quad [K_{+},K_{-}]=-2J_{3}.$

This results in a set of equations for which the solutions are ${\begin{aligned}\left\langle j\left\|K^{(1)}\right\|j\right\rangle &=i{\frac {j_{1}j_{0}}{\sqrt {j(j+1)}}},\\\left\langle j\left\|K^{(1)}\right\|j-1\right\rangle &=-B_{j}\xi _{j}{\sqrt {j(2j-1)}},\\\left\langle j-1\left\|K^{(1)}\right\|j\right\rangle &=B_{j}\xi _{j}^{-1}{\sqrt {j(2j+1)}},\end{aligned}}$ where $B_{j}={\sqrt {\frac {(j^{2}-j_{0}^{2})(j^{2}-j_{1}^{2})}{j^{2}(4j^{2}-1)}}},\quad j_{0}=0,{\tfrac {1}{2}},1,\ldots \quad {\text{and}}\quad j_{1},\xi _{j}\in \mathbb {C} .$

#### Step 4

The imposition of the requirement of unitarity of the corresponding representation of the group restricts the possible values for the arbitrary complex numbers j 0 and ξ j . Unitarity of the group representation translates to the requirement of the Lie algebra representatives being Hermitian, meaning $K_{\pm }^{\dagger }=K_{\mp },\quad K_{3}^{\dagger }=K_{3}.$

This translates to ${\begin{aligned}\left\langle j\left\|K^{(1)}\right\|j\right\rangle &={\overline {\left\langle j\left\|K^{(1)}\right\|j\right\rangle }},\\\left\langle j\left\|K^{(1)}\right\|j-1\right\rangle &=-{\overline {\left\langle j-1\left\|K^{(1)}\right\|j\right\rangle }},\end{aligned}}$ leading to ${\begin{aligned}j_{0}\left(j_{1}+{\overline {j_{1}}}\right)&=0,\\\left|B_{j}\right|\left(\left|\xi _{j}\right|^{2}-e^{-2i\beta _{j}}\right)&=0,\end{aligned}}$ where β j is the angle of B j on polar form. For | B j | ≠ 0 follows $\left|\xi _{j}\right|^{2}=1$ and $\xi _{j}=1$ is chosen by convention. There are two possible cases:

- ${\underline {j_{1}+{\overline {j_{1}}}=0.}}$ In this case j 1 = − iν , ν real, $\left\langle j\left\|K^{(1)}\right\|j\right\rangle ={\frac {\nu j_{0}}{j(j+1)}}\quad {\text{and}}\quad B_{j}={\sqrt {\frac {(j^{2}-j_{0}^{2})(j^{2}+\nu ^{2})}{4j^{2}-1}}}$ This is the principal series . Its elements are denoted $(j_{0},\nu ),2j_{0}\in \mathbb {N} ,\nu \in \mathbb {R} .$

- ${\underline {j_{0}=0.}}$ It follows: $\left\langle j\left\|K^{(1)}\right\|j\right\rangle =0\quad {\text{and}}\quad B_{j}={\sqrt {\frac {j^{2}-\nu ^{2}}{4j^{2}-1}}}$ Since B 0 = B j 0 , B 2 j is real and positive for j = 1, 2, ... , leading to −1 ≤ ν ≤ 1 . This is complementary series . Its elements are denoted (0, ν ), −1 ≤ ν ≤ 1

This shows that the representations of above are all infinite-dimensional irreducible unitary representations.

## Explicit formulas

### Conventions and Lie algebra bases

The metric of choice is given by η = diag(−1, 1, 1, 1) , and the physics convention for Lie algebras and the exponential mapping is used. These choices are arbitrary, but once they are made, fixed. One possible choice of basis for the Lie algebra is, in the 4-vector representation, given by: ${\begin{aligned}J_{1}=J^{23}=-J^{32}&=i{\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}},&K_{1}=J^{01}=-J^{10}&=i{\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}},\\[8pt]J_{2}=J^{31}=-J^{13}&=i{\begin{pmatrix}0&0&0&0\\0&0&0&1\\0&0&0&0\\0&-1&0&0\end{pmatrix}},&K_{2}=J^{02}=-J^{20}&=i{\begin{pmatrix}0&0&1&0\\0&0&0&0\\1&0&0&0\\0&0&0&0\end{pmatrix}},\\[8pt]J_{3}=J^{12}=-J^{21}&=i{\begin{pmatrix}0&0&0&0\\0&0&-1&0\\0&1&0&0\\0&0&0&0\end{pmatrix}},&K_{3}=J^{03}=-J^{30}&=i{\begin{pmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&0\end{pmatrix}}.\\[8pt]\end{aligned}}$

The commutation relations of the Lie algebra ${\mathfrak {so}}(3;1)$ are: $\left[J^{\mu \nu },J^{\rho \sigma }\right]=i\left(\eta ^{\sigma \mu }J^{\rho \nu }+\eta ^{\nu \sigma }J^{\mu \rho }-\eta ^{\rho \mu }J^{\sigma \nu }-\eta ^{\nu \rho }J^{\mu \sigma }\right).$

In three-dimensional notation, these are $\left[J_{i},J_{j}\right]=i\epsilon _{ijk}J_{k},\quad \left[J_{i},K_{j}\right]=i\epsilon _{ijk}K_{k},\quad \left[K_{i},K_{j}\right]=-i\epsilon _{ijk}J_{k}.$

The choice of basis above satisfies the relations, but other choices are possible. The multiple use of the symbol J above and in the sequel should be observed.

For example, a typical boost and a typical rotation exponentiate as, $\exp(-i\xi K_{1})={\begin{pmatrix}\cosh \xi &\sinh \xi &0&0\\\sinh \xi &\cosh \xi &0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}},\qquad \exp(-i\theta J_{1})={\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&\cos \theta &-\sin \theta \\0&0&\sin \theta &\cos \theta \end{pmatrix}},$ symmetric and orthogonal, respectively.

### Weyl spinors

By taking, in turn, m = ⁠ 1 / 2 ⁠ , n = 0 and m = 0, n = ⁠ 1 / 2 ⁠ and by setting $J_{i}^{\left({\frac {1}{2}}\right)}={\frac {1}{2}}\sigma _{i}$ in the general expression (G1) , and by using the trivial relations 1 1 = 1 and J (0) = 0 , it follows

These are the left-handed and right-handed Weyl spinor representations. They act by matrix multiplication on 2-dimensional complex vector spaces (with a choice of basis) V L and V R , whose elements Ψ L and Ψ R are called left- and right-handed Weyl spinors respectively. Given $\left(\pi _{\left({\frac {1}{2}},0\right)},V_{\text{L}}\right)\quad {\text{and}}\quad \left(\pi _{\left(0,{\frac {1}{2}}\right)},V_{\text{R}}\right)$ their direct sum as representations is formed,

This is, up to a similarity transformation, the ( ⁠ 1 / 2 ⁠ ,0) ⊕ (0, ⁠ 1 / 2 ⁠ ) Dirac spinor representation of ${\mathfrak {so}}(3;1).$ It acts on the 4-component elements (Ψ L , Ψ R ) of ( V L ⊕ V R ) , by matrix multiplication. The representation may also be obtained in a more general and basis-independent way from the action of the corresponding Clifford algebra and its spin group on a spinor module. These expressions for Dirac spinors and Weyl spinors all extend by linearity of Lie algebras and representations to all of ${\mathfrak {so}}(3;1).$ Expressions for the group representations are obtained by exponentiation.

## Physics applications

Many of the representations, both finite-dimensional and infinite-dimensional, are important in theoretical physics. Representations appear in the description of fields in classical field theory , most importantly the electromagnetic field , and of particles in relativistic quantum mechanics , as well as of both particles and quantum fields in quantum field theory and of various objects in string theory and beyond. The representation theory also provides the theoretical ground for the concept of spin . The theory enters into general relativity in the sense that in small enough regions of spacetime, physics is that of special relativity.

The finite-dimensional irreducible non-unitary representations together with the irreducible infinite-dimensional unitary representations of the inhomogeneous Lorentz group , the Poincaré group , are the representations that have direct physical relevance.

Infinite-dimensional unitary representations of the Lorentz group appear by restriction of the irreducible infinite-dimensional unitary representations of the Poincaré group acting on the Hilbert spaces of relativistic quantum mechanics and quantum field theory . But these are also of mathematical interest and of potential direct physical relevance in other roles than that of a mere restriction. There were speculative theories — tensors and spinors have infinite counterparts in the expansors and the expinors of Dirac and Harish-Chandra, respectively — consistent with relativity and quantum mechanics, but they have found no proven physical application. Modern speculative theories potentially have similar ingredients to those below.

### Classical field theory

While the electromagnetic field together with the gravitational field are the only classical fields providing accurate descriptions of nature, other types of classical fields are important too. In the approach to quantum field theory (QFT) referred to as second quantization , the starting point is one or more classical fields, where e.g. the wave functions solving the Dirac equation are considered as classical fields prior to (second) quantization. While second quantization and the Lagrangian formalism associated with it is not a fundamental aspect of QFT, it is the case that so far all quantum field theories can be approached this way, including the Standard Model . The equations that describe the fields must be relativistically invariant, and their solutions (which will qualify as relativistic wave functions according to the definition below) must transform under some representation of the Lorentz group.

The action of the Lorentz group on the space of field configurations (a field configuration is the spacetime history of a particular solution, e.g. the electromagnetic field in all of space over all time is one field configuration) resembles the action on the Hilbert spaces of quantum mechanics, except that the commutator brackets are replaced by field theoretical Poisson brackets .

### Relativistic quantum mechanics

For the present purposes the following definition is made: A relativistic wave function is a set of n functions ψ α on spacetime which transforms under an arbitrary proper Lorentz transformation Λ as $\psi '^{\alpha }(x)=D{[\Lambda ]^{\alpha }}_{\beta }\psi ^{\beta }\left(\Lambda ^{-1}x\right),$ where D [Λ] is an n -dimensional matrix representative of Λ .

The most useful relativistic quantum mechanics one-particle theories (there are no fully consistent such theories) are the Klein–Gordon equation and the Dirac equation in their original setting. They are relativistically invariant and their solutions transform under the Lorentz group as Lorentz scalars and Dirac spinors respectively. The electromagnetic field is also a relativistic wave function according to this definition.

The infinite-dimensional representations may be used in the analysis of scattering.

### Quantum field theory

In quantum field theory , the demand for relativistic invariance enters, among other ways in that the S-matrix necessarily must be Poincaré invariant. This has the implication that there is one or more infinite-dimensional representation of the Lorentz group acting on Fock space . One way to guarantee the existence of such representations is the existence of a Lagrangian description (with modest requirements imposed, see the reference) of the system using the canonical formalism, from which a realization of the generators of the Lorentz group may be deduced.

The transformations of field operators illustrate the complementary role played by the finite-dimensional representations of the Lorentz group and the infinite-dimensional unitary representations of the Poincare group, witnessing the deep unity between mathematics and physics. For illustration, consider the definition an n -component field operator : A relativistic field operator is a set of n operator valued functions on spacetime which transforms under proper Poincaré transformations (Λ, a ) according to

$\Psi ^{\alpha }(x)\to \Psi '^{\alpha }(x)=U[\Lambda ,a]\Psi ^{\alpha }(x)U^{-1}\left[\Lambda ,a\right]=D{\left[\Lambda ^{-1}\right]^{\alpha }}_{\beta }\Psi ^{\beta }(\Lambda x+a)$

Here U [Λ, a] is the unitary operator representing (Λ, a) on the Hilbert space on which Ψ is defined and D is an n -dimensional representation of the Lorentz group. The transformation rule is the second Wightman axiom of quantum field theory.

By considerations of differential constraints that the field operator must be subjected to in order to describe a single particle with definite mass m and spin s (or helicity), it is deduced that

where a † , a are interpreted as creation and annihilation operators respectively. The creation operator a † transforms according to

$a^{\dagger }(\mathbf {p} ,\sigma )\rightarrow a'^{\dagger }\left(\mathbf {p} ,\sigma \right)=U[\Lambda ]a^{\dagger }(\mathbf {p} ,\sigma )U\left[\Lambda ^{-1}\right]=a^{\dagger }(\Lambda \mathbf {p} ,\rho )D^{(s)}{\left[R(\Lambda ,\mathbf {p} )^{-1}\right]^{\rho }}_{\sigma },$

and similarly for the annihilation operator. The point to be made is that the field operator transforms according to a finite-dimensional non-unitary representation of the Lorentz group, while the creation operator transforms under the infinite-dimensional unitary representation of the Poincare group characterized by the mass and spin ( m , s ) of the particle. The connection between the two are the wave functions , also called coefficient functions

$u^{\alpha }(\mathbf {p} ,\sigma )e^{ip\cdot x},\quad v^{\alpha }(\mathbf {p} ,\sigma )e^{-ip\cdot x}$

that carry both the indices ( x , α ) operated on by Lorentz transformations and the indices ( p , σ ) operated on by Poincaré transformations. This may be called the Lorentz–Poincaré connection. To exhibit the connection, subject both sides of equation (X1) to a Lorentz transformation resulting in for e.g. u ,

${D[\Lambda ]^{\alpha }}_{\alpha '}u^{\alpha '}(\mathbf {p} ,\lambda )={D^{(s)}[R(\Lambda ,\mathbf {p} )]^{\lambda '}}_{\lambda }u^{\alpha }\left(\Lambda \mathbf {p} ,\lambda '\right),$

where D is the non-unitary Lorentz group representative of Λ and D ( s ) is a unitary representative of the so-called Wigner rotation R associated to Λ and p that derives from the representation of the Poincaré group, and s is the spin of the particle.

All of the above formulas, including the definition of the field operator in terms of creation and annihilation operators, as well as the differential equations satisfied by the field operator for a particle with specified mass, spin and the ( m , n ) representation under which it is supposed to transform, and also that of the wave function, can be derived from group theoretical considerations alone once the frameworks of quantum mechanics and special relativity is given.

### Speculative theories

In theories in which spacetime can have more than D = 4 dimensions, the generalized Lorentz groups O( D − 1; 1) of the appropriate dimension take the place of O(3; 1) .

The requirement of Lorentz invariance takes on perhaps its most dramatic effect in string theory . Classical relativistic strings can be handled in the Lagrangian framework by using the Nambu–Goto action . This results in a relativistically invariant theory in any spacetime dimension. But as it turns out, the theory of open and closed bosonic strings (the simplest string theory) is impossible to quantize in such a way that the Lorentz group is represented on the space of states (a Hilbert space ) unless the dimension of spacetime is 26. The corresponding result for superstring theory is again deduced demanding Lorentz invariance, but now with supersymmetry . In these theories the Poincaré algebra is replaced by a supersymmetry algebra which is a Z 2 -graded Lie algebra extending the Poincaré algebra. The structure of such an algebra is to a large degree fixed by the demands of Lorentz invariance. In particular, the only possible dimension of spacetime in such theories is 10.

## Open problems

The classification and characterization of the representation theory of the Lorentz group was completed in 1947.

The irreducible infinite-dimensional unitary representations may have indirect relevance to physical reality in speculative modern theories since the (generalized) Lorentz group appears as the little group of the Poincaré group of spacelike vectors in higher spacetime dimension. The corresponding infinite-dimensional unitary representations of the (generalized) Poincaré group are the so-called tachyonic representations . Tachyons appear in the spectrum of bosonic strings and are associated with instability of the vacuum. Even though tachyons may not be realized in nature, these representations must be mathematically understood in order to understand string theory. This is so since tachyon states turn out to appear in superstring theories too in attempts to create realistic models.

One open problem is the completion of the Bargmann–Wigner programme for the isometry group SO( D − 2, 1) of the de Sitter spacetime dS D −2 . Ideally, the physical components of wave functions would be realized on the hyperboloid dS D −2 of radius μ > 0 embedded in $\mathbb {R} ^{D-2,1}$ and the corresponding O( D −2, 1) covariant wave equations of the infinite-dimensional unitary representation to be known.
