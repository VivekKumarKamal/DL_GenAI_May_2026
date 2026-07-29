# Projective space

> **Query Topic**: statements accurately describes the dimension of an object in a CW complex (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 207, Frequency: 15)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Projective_space

---

In mathematics , the concept of a projective space originated from the visual effect of perspective , where parallel lines seem to meet at infinity . A projective space may thus be viewed as the extension of a Euclidean space , or, more generally, an affine space with points at infinity , in such a way that there is one point at infinity of each direction of parallel lines .

This definition of a projective space has the disadvantage of not being isotropic , having two different sorts of points, which must be considered separately in proofs. Therefore, other definitions are generally preferred. There are two classes of definitions. In synthetic geometry , point and line are primitive entities that are related by the incidence relation "a point is on a line" or "a line passes through a point", which is subject to the axioms of projective geometry . For some such set of axioms, the projective spaces that are defined have been shown to be equivalent to those resulting from the following definition, which is more often encountered in modern textbooks.

Using linear algebra , a projective space of dimension n is defined as the set of the vector lines (that is, vector subspaces of dimension one) in a vector space V of dimension n + 1 . Equivalently, it is the quotient set of V \ {0} by the equivalence relation "being on the same vector line". As a vector line intersects the unit sphere of V in two antipodal points , projective spaces can be equivalently defined as spheres in which antipodal points are identified. A projective space of dimension 1 is a projective line , and a projective space of dimension 2 is a projective plane .

Projective spaces are widely used in geometry , allowing for simpler statements and simpler proofs. For example, in affine geometry , two distinct lines in a plane intersect in at most one point, while, in projective geometry , they intersect in exactly one point. Also, there is only one class of conic sections , which can be distinguished only by their intersections with the line at infinity: two intersection points for hyperbolas ; one for the parabola , which is tangent to the line at infinity; and no real intersection point of ellipses .

In topology , and more specifically in manifold theory , projective spaces play a fundamental role, being typical examples of non-orientable manifolds .

## Motivation

As outlined above, projective spaces were introduced for formalizing statements like "two coplanar lines intersect in exactly one point, and this point is at infinity if the lines are parallel ". Such statements are suggested by the study of perspective , which may be considered as a central projection of the three dimensional space onto a plane (see Pinhole camera model ). More precisely, the entrance pupil of a camera or of the eye of an observer is the center of projection , and the image is formed on the projection plane .

Mathematically, the center of projection is a point O of the space (the intersection of the axes in the figure); the projection plane ( P 2 , in blue on the figure) is a plane not passing through O , which is often chosen to be the plane of equation z = 1 , when Cartesian coordinates are considered. Then, the central projection maps a point P to the intersection of the line OP with the projection plane. Such an intersection exists if and only if the point P does not belong to the plane ( P 1 , in green on the figure) that passes through O and is parallel to P 2 .

It follows that the lines passing through O split in two disjoint subsets: the lines that are not contained in P 1 , which are in one to one correspondence with the points of P 2 , and those contained in P 1 , which are in one to one correspondence with the directions of parallel lines in P 2 . This suggests to define the points (called here projective points for clarity) of the projective plane as the lines passing through O . A projective line in this plane consists of all projective points (which are lines) contained in a plane passing through O . As the intersection of two planes passing through O is a line passing through O , the intersection of two distinct projective lines consists of a single projective point. The plane P 1 defines a projective line which is called the line at infinity of P 2 . By identifying each point of P 2 with the corresponding projective point, one can thus say that the projective plane is the disjoint union of P 2 and the (projective) line at infinity.

As an affine space with a distinguished point O may be identified with its associated vector space (see Affine space § Vector spaces as affine spaces ), the preceding construction is generally done by starting from a vector space and is called projectivization . Also, the construction can be done by starting with a vector space of any positive dimension.

So, a projective space of dimension n can be defined as the set of vector lines (vector subspaces of dimension one) in a vector space of dimension n + 1 . A projective space can also be defined as the elements of any set that is in natural correspondence with this set of vector lines.

This set can be the set of equivalence classes under the equivalence relation between vectors defined by "one vector is the product of the other by a nonzero scalar". In other words, this amounts to defining a projective space as the set of vector lines in which the zero vector has been removed.

A third equivalent definition is to define a projective space of dimension n as the set of pairs of antipodal points in a sphere of dimension n (in a space of dimension n + 1 ).

## Definition

Given a vector space V over a field K , the projective space P ( V ) is the set of equivalence classes of V \ {0} under the equivalence relation ~ defined by x ~ y if there is a nonzero element λ of K such that x = λy . If V is a topological vector space , the quotient space P ( V ) is a topological space , endowed with the quotient topology of the subspace topology of V \ {0} . This is the case when K is the field R of the real numbers or the field C of the complex numbers . If V is finite dimensional, the dimension of P ( V ) is the dimension of V minus one.

In the common case where V = K n +1 , the projective space P ( V ) is denoted P n ( K ) (as well as K P n or P n ( K ) , although this notation may be confused with exponentiation). The space P n ( K ) is often called the projective space of dimension n over K , or the projective n -space , since all projective spaces of dimension n are isomorphic to it (because every K vector space of dimension n + 1 is isomorphic to K n +1 ).

The elements of a projective space P ( V ) are commonly called points . If a basis of V has been chosen, and, in particular if V = K n +1 , the projective coordinates of a point P are the coordinates on the basis of any element of the corresponding equivalence class. These coordinates are commonly denoted [ x 0 : ... : x n ] , the colons and the brackets being used for distinguishing from usual coordinates, and emphasizing that this is an equivalence class, which is defined up to the multiplication by a non zero constant. That is, if [ x 0 : ... : x n ] are projective coordinates of a point, then [ λx 0 : ... : λx n ] are also projective coordinates of the same point, for any nonzero λ in K . Also, the above definition implies that [ x 0 : ... : x n ] are projective coordinates of a point if and only if at least one of the coordinates is nonzero.

If K is the field of real or complex numbers, a projective space is called a real projective space or a complex projective space , respectively. If n is one or two, a projective space of dimension n is called a projective line or a projective plane , respectively. The complex projective line is also called the Riemann sphere .

All these definitions extend naturally to the case where K is a division ring ; see, for example, Quaternionic projective space . The notation PG( n , K ) is sometimes used for P n ( K ) . If K is a finite field with q elements, P n ( K ) is often denoted PG( n , q ) (see PG(3,2) ).

## Related concepts

### Subspace

Let P ( V ) be a projective space, where V is a vector space over a field K , and $p:V\setminus \{0\}\to \mathbf {P} (V)$ be the canonical map that maps a nonzero vector v to its equivalence class, which is the vector line containing v .

Every linear subspace W of V is a union of lines. It follows that p ( W ) is a projective space, which can be identified with P ( W ) .

A projective subspace is thus a projective space that is obtained by restricting to a linear subspace the equivalence relation that defines P ( V ) .

If p ( v ) and p ( w ) are two different points of P ( V ) , the vectors v and w are linearly independent . It follows that:

- There is exactly one projective line that passes through two different points of P ( V ) , and

- A subset of P ( V ) is a projective subspace if and only if, given any two different points, it contains the whole projective line passing through these points.

In synthetic geometry , where projective lines are primitive objects, the first property is an axiom, and the second one is the definition of a projective subspace.

### Span

Every intersection of projective subspaces is a projective subspace. It follows that for every subset S of a projective space, there is a smallest projective subspace containing S , the intersection of all projective subspaces containing S . This projective subspace is called the projective span of S , and S is a spanning set for it.

A set S of points is projectively independent if its span is not the span of any proper subset of S . If S is a spanning set of a projective space P , then there is a subset of S that spans P and is projectively independent (this results from the similar theorem for vector spaces). If the dimension of P is n , such an independent spanning set has n + 1 elements.

Contrarily to the cases of vector spaces and affine spaces , an independent spanning set does not suffice for defining coordinates. One needs one more point, see next section.

### Frame

A projective frame or projective basis is an ordered set of points in a projective space that allows defining coordinates. More precisely, in an n -dimensional projective space, a projective frame is a tuple of n + 2 points such that any n + 1 of them are independent; that is, they are not contained in a hyperplane .

If V is an ( n + 1) -dimensional vector space, and p is the canonical projection from V to P ( V ) , then ( p ( e 0 ), ..., p ( e n +1 )) is a projective frame if and only if ( e 0 , ..., e n ) is a basis of V and the coefficients of e n +1 on this basis are all nonzero. By rescaling the first n vectors, any frame can be rewritten as ( p ( e ′ 0 ), ..., p( e ′ n +1 )) such that e ′ n +1 = e ′ 0 + ... + e ′ n ; this representation is unique up to the multiplication of all e ′ i with a common nonzero factor.

The projective coordinates or homogeneous coordinates of a point p ( v ) on a frame ( p ( e 0 ), ..., p ( e n +1 )) with e n +1 = e 0 + ... + e n are the coordinates of v on the basis ( e 0 , ..., e n ) . They are only defined up to scaling with a common nonzero factor.

The canonical frame of the projective space P n ( K ) consists of images by p of the elements of the canonical basis of K n +1 (that is, the tuples with only one nonzero entry, equal to 1), and the image by p of their sum.

### Projective geometry

In mathematics , projective geometry is the study of geometric properties that are invariant with respect to projective transformations . This means that, compared to elementary Euclidean geometry , projective geometry has a different setting ( projective space ) and a selective set of basic geometric concepts. The basic intuitions are that projective space has more points than Euclidean space , for a given dimension, and that geometric transformations are permitted that transform the extra points (called " points at infinity ") to Euclidean points, and vice versa.

Properties meaningful for projective geometry are respected by this new idea of transformation, which is more radical in its effects than can be expressed by a transformation matrix and translations (the affine transformations ). The first issue for geometers is what kind of geometry is adequate for a novel situation. Unlike in Euclidean geometry , the concept of an angle does not apply in projective geometry, because no measure of angles is invariant with respect to projective transformations, as is seen in perspective drawing from a changing perspective. One source for projective geometry was indeed the theory of perspective. Another difference from elementary geometry is the way in which parallel lines can be said to meet in a point at infinity , once the concept is translated into projective geometry's terms. Again this notion has an intuitive basis, such as railway tracks meeting at the horizon in a perspective drawing. See Projective plane for the basics of projective geometry in two dimensions.

While the ideas were available earlier, projective geometry was mainly a development of the 19th century. This included the theory of complex projective space , the coordinates used ( homogeneous coordinates ) being complex numbers. Several major types of more abstract mathematics (including invariant theory , the Italian school of algebraic geometry , and Felix Klein 's Erlangen programme resulting in the study of the classical groups ) were motivated by projective geometry. It was also a subject with many practitioners for its own sake, as synthetic geometry . Another topic that developed from axiomatic studies of projective geometry is finite geometry .

The topic of projective geometry is itself now divided into many research subtopics, two examples of which are projective algebraic geometry (the study of projective varieties ) and projective differential geometry (the study of differential invariants of the projective transformations).

### Projective transformation

In projective geometry , a homography is an isomorphism of projective spaces, induced by an isomorphism of the vector spaces from which the projective spaces derive. It is a bijection that maps lines to lines, and thus a collineation . In general, some collineations are not homographies, but the fundamental theorem of projective geometry asserts that is not so in the case of real projective spaces of dimension at least two. Synonyms include projectivity, projective transformation, and projective collineation.

Historically, homographies (and projective spaces) have been introduced to study perspective and projections in Euclidean geometry , and the term homography , which, etymologically, roughly means "similar drawing", dates from this time. At the end of the 19th century, formal definitions of projective spaces were introduced, which extended Euclidean and affine spaces by the addition of new points called points at infinity . The term "projective transformation" originated in these abstract constructions. These constructions divide into two classes that have been shown to be equivalent. A projective space may be constructed as the set of the lines of a vector space over a given field (the above definition is based on this version); this construction facilitates the definition of projective coordinates and allows using the tools of linear algebra for the study of homographies. The alternative approach consists in defining the projective space through a set of axioms, which do not involve explicitly any field ( incidence geometry , see also synthetic geometry ); in this context, collineations are easier to define than homographies, and homographies are defined as specific collineations, thus called "projective collineations".

For sake of simplicity, unless otherwise stated, the projective spaces considered in this article are supposed to be defined over a (commutative) field . Equivalently Pappus's hexagon theorem and Desargues's theorem are supposed to be true. A large part of the results remain true, or may be generalized to projective geometries for which these theorems do not hold.

## Topology

A projective space is a topological space , as endowed with the quotient topology of the topology of a finite dimensional real vector space.

Let S be the unit sphere in a normed vector space V , and consider the function $\pi :S\to \mathbf {P} (V)$ that maps a point of S to the vector line passing through it. This function is continuous and surjective. The inverse image of every point of P ( V ) consist of two antipodal points . As spheres are compact spaces , it follows that:

For every point P of S , the restriction of π to a neighborhood of P is a homeomorphism onto its image, provided that the neighborhood is small enough for not containing any pair of antipodal points. This shows that a projective space is a manifold. A simple atlas can be provided, as follows.

As soon as a basis has been chosen for V , any vector can be identified with its coordinates on the basis, and any point of P ( V ) may be identified with its homogeneous coordinates . For i = 0, ..., n , the set $U_{i}=\{[x_{0}:\cdots :x_{n}],x_{i}\neq 0\}$ is an open subset of P ( V ) , and $\mathbf {P} (V)=\bigcup _{i=0}^{n}U_{i}$ since every point of P ( V ) has at least one nonzero coordinate.

To each U i is associated a chart , which is the homeomorphisms ${\begin{aligned}\mathbb {\varphi } _{i}:R^{n}&\to U_{i}\\(y_{0},\dots ,{\widehat {y_{i}}},\dots ,y_{n})&\mapsto [y_{0}:\cdots :y_{i-1}:1:y_{i+1}:\cdots :y_{n}],\end{aligned}}$ such that $\varphi _{i}^{-1}\left([x_{0}:\cdots :x_{n}]\right)=\left({\frac {x_{0}}{x_{i}}},\dots ,{\widehat {\frac {x_{i}}{x_{i}}}},\dots ,{\frac {x_{n}}{x_{i}}}\right),$ where hats means that the corresponding term is missing.

These charts form an atlas , and, as the transition maps are analytic functions , it results that projective spaces are analytic manifolds .

For example, in the case of n = 1 , that is of a projective line, there are only two U i , which can each be identified to a copy of the real line . In both lines, the intersection of the two charts is the set of nonzero real numbers, and the transition map is $x\mapsto {\frac {1}{x}}$ in both directions. The image represents the projective line as a circle where antipodal points are identified, and shows the two homeomorphisms of a real line to the projective line; as antipodal points are identified, the image of each line is represented as an open half circle, which can be identified with the projective line with a single point removed.

### CW complex structure

Real projective spaces have a simple CW complex structure, as P n ( R ) can be obtained from P n −1 ( R ) by attaching an n -cell with the quotient projection S n −1 → P n −1 ( R ) as the attaching map.

## Algebraic geometry

Originally, algebraic geometry was the study of common zeros of sets of multivariate polynomials . These common zeros, called algebraic varieties belong to an affine space . It appeared soon, that in the case of real coefficients, one must consider all the complex zeros for having accurate results. For example, the fundamental theorem of algebra asserts that a univariate square-free polynomial of degree n has exactly n complex roots. In the multivariate case, the consideration of complex zeros is also needed, but not sufficient: one must also consider zeros at infinity . For example, Bézout's theorem asserts that the intersection of two plane algebraic curves of respective degrees d and e consists of exactly de points if one consider complex points in the projective plane, and if one counts the points with their multiplicity. Another example is the genus–degree formula that allows computing the genus of a plane algebraic curve from its singularities in the complex projective plane .

So a projective variety is the set of points in a projective space, whose homogeneous coordinates are common zeros of a set of homogeneous polynomials .

Any affine variety can be completed , in a unique way, into a projective variety by adding its points at infinity , which consists of homogenizing the defining polynomials, and removing the components that are contained in the hyperplane at infinity, by saturating with respect to the homogenizing variable.

An important property of projective spaces and projective varieties is that the image of a projective variety under a morphism of algebraic varieties is closed for Zariski topology (that is, it is an algebraic set ). This is a generalization to every ground field of the compactness of the real and complex projective space.

A projective space is itself a projective variety, being the set of zeros of the zero polynomial.

### Scheme theory

Scheme theory, introduced by Alexander Grothendieck during the second half of 20th century, allows defining a generalization of algebraic varieties, called schemes , by gluing together smaller pieces called affine schemes , similarly as manifolds can be built by gluing together open sets of R n . The Proj construction is the construction of the scheme of a projective space, and, more generally of any projective variety, by gluing together affine schemes. In the case of projective spaces, one can take for these affine schemes the affine schemes associated to the charts (affine spaces) of the above description of a projective space as a manifold.

## Synthetic geometry

In synthetic geometry , a projective space S can be defined axiomatically as a set P (the set of points), together with a set L of subsets of P (the set of lines), satisfying these axioms:

- Each two distinct points p and q are in exactly one line.

- Veblen 's axiom: If a , b , c , d are distinct points and the lines through ab and cd meet, then so do the lines through ac and bd .

- Any line has at least 3 points on it.

The last axiom eliminates reducible cases that can be written as a disjoint union of projective spaces together with 2-point lines joining any two points in distinct projective spaces. More abstractly, it can be defined as an incidence structure ( P , L , I ) consisting of a set P of points, a set L of lines, and an incidence relation I that states which points lie on which lines.

The structures defined by these axioms are more general than those obtained from the vector space construction given above. If the (projective) dimension is at least three then, by the Veblen–Young theorem , there is no difference. However, for dimension two, there are examples that satisfy these axioms that can not be constructed from vector spaces (or even modules over division rings). These examples do not satisfy the theorem of Desargues and are known as non-Desarguesian planes . In dimension one, any set with at least three elements satisfies the axioms, so it is usual to assume additional structure for projective lines defined axiomatically.

It is possible to avoid the troublesome cases in low dimensions by adding or modifying axioms that define a projective space. Coxeter (1969 , p. 231) gives such an extension due to Bachmann. To ensure that the dimension is at least two, replace the three point per line axiom above by:

- There exist four points, no three of which are collinear.

To avoid the non-Desarguesian planes, include Pappus's theorem as an axiom;

- If the six vertices of a hexagon lie alternately on two lines, the three points of intersection of pairs of opposite sides are collinear.

And, to ensure that the vector space is defined over a field that does not have even characteristic include Fano's axiom ;

- The three diagonal points of a complete quadrangle are never collinear.

A subspace of the projective space is a subset X , such that any line containing two points of X is a subset of X (that is, completely contained in X ). The full space and the empty space are always subspaces.

The geometric dimension of the space is said to be n if that is the largest number for which there is a strictly ascending chain of subspaces of this form: $\varnothing =X_{-1}\subset X_{0}\subset \cdots X_{n}=P.$

A subspace X i in such a chain is said to have (geometric) dimension i . Subspaces of dimension 0 are called points , those of dimension 1 are called lines and so on. If the full space has dimension n then any subspace of dimension n − 1 is called a hyperplane .

Projective spaces admit an equivalent formulation in terms of lattice theory. There is a bijective correspondence between projective spaces and geomodular lattices, namely, subdirectly irreducible , compactly generated , complemented , modular lattices .

### Classification

- Dimension 0 (no lines): The space is a single point.

- Dimension 1 (exactly one line): All points lie on the unique line.

- Dimension 2: There are at least 2 lines, and any two lines meet. A projective space for n = 2 is equivalent to a projective plane . These are much harder to classify, as not all of them are isomorphic with a PG( d , K ) . The Desarguesian planes (those that are isomorphic with a PG(2, K )) satisfy Desargues's theorem and are projective planes over division rings, but there are many non-Desarguesian planes .

- Dimension at least 3: Two non-intersecting lines exist. Veblen & Young (1965) proved the Veblen–Young theorem , to the effect that every projective space of dimension n ≥ 3 is isomorphic with a PG( n , K ) , the n -dimensional projective space over some division ring K .

### Finite projective spaces and planes

A finite projective space is a projective space where P is a finite set of points. In any finite projective space, each line contains the same number of points and the order of the space is defined as one less than this common number. For finite projective spaces of dimension at least three, Wedderburn's theorem implies that the division ring over which the projective space is defined must be a finite field , GF( q ) , whose order (that is, number of elements) is q (a prime power). A finite projective space defined over such a finite field has q + 1 points on a line, so the two concepts of order coincide. Notationally, PG( n , GF( q )) is usually written as PG( n , q ) .

All finite fields of the same order are isomorphic, so, up to isomorphism, there is only one finite projective space for each dimension greater than or equal to three, over a given finite field. However, in dimension two there are non-Desarguesian planes. Up to isomorphism there are

finite projective planes of orders 2, 3, 4, ..., 10, respectively. The numbers beyond this are very difficult to calculate and are not determined except for some zero values due to the Bruck–Ryser theorem .

The smallest projective plane is the Fano plane , PG(2, 2) with 7 points and 7 lines. The smallest 3-dimensional projective space is PG(3, 2) , with 15 points, 35 lines and 15 planes.

## Morphisms

Injective linear maps T ∈ L ( V , W ) between two vector spaces V and W over the same field K induce mappings of the corresponding projective spaces P ( V ) → P ( W ) via:

where v is a non-zero element of V and [...] denotes the equivalence classes of a vector under the defining identification of the respective projective spaces. Since members of the equivalence class differ by a scalar factor, and linear maps preserve scalar factors, this induced map is well-defined . (If T is not injective, it has a null space larger than {0} ; in this case the meaning of the class of T ( v ) is problematic if v is non-zero and in the null space. In this case one obtains a so-called rational map , see also Birational geometry .)

Two linear maps S and T in L ( V , W ) induce the same map between P ( V ) and P ( W ) if and only if they differ by a scalar multiple, that is if T = λS for some λ ≠ 0 . Thus if one identifies the scalar multiples of the identity map with the underlying field K , the set of K -linear morphisms from P ( V ) to P ( W ) is simply P ( L ( V , W )) .

The automorphisms P ( V ) → P ( V ) can be described more concretely. (We deal only with automorphisms preserving the base field K ). Using the notion of sheaves generated by global sections , it can be shown that any algebraic (not necessarily linear) automorphism must be linear, i.e., coming from a (linear) automorphism of the vector space V . The latter form the group GL( V ) . By identifying maps that differ by a scalar, one concludes that

the quotient group of GL( V ) modulo the matrices that are scalar multiples of the identity. (These matrices form the center of Aut( V ) .) The groups PGL are called projective linear groups . The automorphisms of the complex projective line P 1 ( C ) are called Möbius transformations .

## Dual projective space

When the construction above is applied to the dual space V ∗ rather than V , one obtains the dual projective space, which can be canonically identified with the space of hyperplanes through the origin of V . That is, if V is n -dimensional, then P ( V ∗ ) is the Grassmannian of n − 1 planes in V .

In algebraic geometry, this construction allows for greater flexibility in the construction of projective bundles. One would like to be able to associate a projective space to every quasi-coherent sheaf E over a scheme Y , not just the locally free ones. [ clarification needed ] See EGA II , Chap. II, par. 4 for more details.

## Generalizations

The projective space, being the "space" of all one-dimensional linear subspaces of a given vector space V is generalized to Grassmannian manifold , which is parametrizing higher-dimensional subspaces (of some fixed dimension) of V .

More generally flag manifold is the space of flags, i.e., chains of linear subspaces of V .

Even more generally, moduli spaces parametrize objects such as elliptic curves of a given kind.

Generalizing to associative rings (rather than only fields) yields, for example, the projective line over a ring .

Patching projective spaces together yields projective space bundles .

Severi–Brauer varieties are algebraic varieties over a field K , which become isomorphic to projective spaces after an extension of the base field K .

Another generalization of projective spaces are weighted projective spaces ; these are themselves special cases of toric varieties .
