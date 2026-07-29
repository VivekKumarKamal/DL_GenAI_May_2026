# Point reflection

> **Query Topic**: How many crystallographic point groups are there in three-dimensional space (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 270, Frequency: 18)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Point_reflection

---

In geometry , a point reflection (also called a point inversion or central inversion ) is a geometric transformation of affine space in which every point is reflected across a designated inversion center , which remains fixed . In Euclidean or pseudo-Euclidean spaces , a point reflection is an isometry (preserves distance ). In the Euclidean plane , a point reflection is the same as a half-turn rotation (180° or π radians ), while in three-dimensional Euclidean space a point reflection is an improper rotation which preserves distances but reverses orientation . A point reflection is an involution : applying it twice is the identity transformation .

An object that is invariant under a point reflection is said to possess point symmetry (also called inversion symmetry or central symmetry ). A point group including a point reflection among its symmetries is called centrosymmetric . Inversion symmetry is found in many crystal structures and molecules , and has a major effect upon their physical properties.

## Terminology

The term reflection is loose, and considered by some an abuse of language, with inversion preferred; however, point reflection is widely used. Such maps are involutions , meaning that they have order 2 – they are their own inverse: applying them twice yields the identity map – which is also true of other maps called reflections . More narrowly, a reflection refers to a reflection in a hyperplane ( $n-1$ dimensional affine subspace – a point on the line , a line in the plane , a plane in 3-space), with the hyperplane being fixed, but more broadly reflection is applied to any involution of Euclidean space, and the fixed set (an affine space of dimension k , where $1\leq k\leq n-1$ ) is called the mirror . In dimension 1 these coincide, as a point is a hyperplane in the line.

In terms of linear algebra, assuming the origin is fixed, involutions are exactly the diagonalizable maps with all eigenvalues either 1 or −1. Reflection in a hyperplane has a single − 1 eigenvalue (and multiplicity $n-1$ on the 1 eigenvalue), while point reflection has only the −1 eigenvalue (with multiplicity n ).

The term inversion should not be confused with inversive geometry , where inversion is defined with respect to a circle.

## Examples

In two dimensions, a point reflection is the same as a rotation of 180 degrees. In three dimensions, a point reflection can be described as a 180-degree rotation composed with reflection across the plane of rotation, perpendicular to the axis of rotation. In dimension n , point reflections are orientation -preserving if n is even, and orientation-reversing if n is odd.

## Formula

Given a vector a in the Euclidean space R n , the formula for the reflection of a across the point p is

$\mathrm {Ref} _{\mathbf {p} }(\mathbf {a} )=2\mathbf {p} -\mathbf {a} .$

In the case where p is the origin, point reflection is simply the negation of the vector a .

In Euclidean geometry , the inversion of a point X with respect to a point P is a point X * such that P is the midpoint of the line segment with endpoints X and X *. In other words, the vector from X to P is the same as the vector from P to X *.

The formula for the inversion in P is

x * = 2 p − x

where p , x and x * are the position vectors of P , X and X * respectively.

This mapping is an isometric involutive affine transformation which has exactly one fixed point , which is P .

## Point reflection as a special case of uniform scaling or homothety

When the inversion point P coincides with the origin, point reflection is equivalent to a special case of uniform scaling : uniform scaling with scale factor equal to −1. This is an example of linear transformation .

When P does not coincide with the origin, point reflection is equivalent to a special case of homothetic transformation : homothety with homothetic center coinciding with P, and scale factor −1. (This is an example of non-linear affine transformation .)

## Point reflection group

The composition of two point reflections is a translation . Specifically, point reflection at p followed by point reflection at q is translation by the vector 2( q − p ).

The set consisting of all point reflections and translations is Lie subgroup of the Euclidean group . It is a semidirect product of R n with a cyclic group of order 2, the latter acting on R n by negation. It is precisely the subgroup of the Euclidean group that fixes the line at infinity pointwise.

In the case n = 1, the point reflection group is the full isometry group of the line.

## Point reflections in mathematics

- Point reflection across the center of a sphere yields the antipodal map .

- A symmetric space is a Riemannian manifold with an isometric reflection across each point. Symmetric spaces play an important role in the study of Lie groups and Riemannian geometry .

## Point reflection in analytic geometry

Given the point $P(x,y)$ and its reflection $P'(x',y')$ with respect to the point $C(x_{c},y_{c})$ , the latter is the midpoint of the segment ${\overline {PP'}}$ ;

${\begin{cases}x_{c}={\frac {x+x'}{2}}\\y_{c}={\frac {y+y'}{2}}\end{cases}}$

Hence, the equations to find the coordinates of the reflected point are

${\begin{cases}x'=2x_{c}-x\\y'=2y_{c}-y\end{cases}}$

Particular is the case in which the point C has coordinates $(0,0)$ (see the paragraph below )

${\begin{cases}x'=-x\\y'=-y\end{cases}}$

## Properties

In even-dimensional Euclidean space , say 2 N -dimensional space, the inversion in a point P is equivalent to N rotations over angles π in each plane of an arbitrary set of N mutually orthogonal planes intersecting at P . These rotations are mutually commutative. Therefore, inversion in a point in even-dimensional space is an orientation-preserving isometry or direct isometry .

In odd-dimensional Euclidean space , say (2 N + 1)-dimensional space, it is equivalent to N rotations over π in each plane of an arbitrary set of N mutually orthogonal planes intersecting at P , combined with the reflection in the 2 N -dimensional subspace spanned by these rotation planes. Therefore, it reverses rather than preserves orientation , it is an indirect isometry .

Geometrically in 3D it amounts to rotation about an axis through P by an angle of 180°, combined with reflection in the plane through P which is perpendicular to the axis; the result does not depend on the orientation (in the other sense) of the axis. Notations for the type of operation, or the type of group it generates, are ${\overline {1}}$ , C i , S 2 , and 1 × . The group type is one of the three symmetry group types in 3D without any pure rotational symmetry , see cyclic symmetries with n = 1.

The following point groups in three dimensions contain inversion:

- C n h and D n h for even n

- S 2 n and D n d for odd n

- T h , O h , and I h

Closely related to inverse in a point is reflection in respect to a plane , which can be thought of as an "inversion in a plane".

## Inversion centers in crystals and molecules

Inversion symmetry plays a major role in the properties of materials, as also do other symmetry operations.

Some molecules contain an inversion center when a point exists through which all atoms can reflect while retaining symmetry. In many cases they can be considered as polyhedra, categorized by their coordination number and bond angles. For example, four-coordinate polyhedra are classified as tetrahedra , while five-coordinate environments can be square pyramidal or trigonal bipyramidal depending on the bonding angles. Six-coordinate octahedra are an example of centrosymmetric polyhedra, as the central atom acts as an inversion center through which the six bonded atoms retain symmetry. Tetrahedra, on the other hand, are non-centrosymmetric as an inversion through the central atom would result in a reversal of the polyhedron. Polyhedra with an odd (versus even) coordination number are not centrosymmtric. Polyhedra containing inversion centers are known as centrosymmetric, while those without are non-centrosymmetric. The presence or absence of an inversion center has a strong influence on the optical properties; for instance molecules without inversion symmetry have a dipole moment and can directly interact with photons, while those with inversion have no dipole moment and only interact via Raman scattering . The later is named after C. V. Raman who was awarded the 1930 Nobel Prize in Physics for his discovery.

In addition, in crystallography , the presence of inversion centers for periodic structures distinguishes between centrosymmetric and non-centrosymmetric compounds. All crystalline compounds come from a repetition of an atomic building block known as a unit cell, and these unit cells define which polyhedra form and in what order. In many materials such as oxides these polyhedra can link together via corner-, edge- or face sharing, depending on which atoms share common bonds and also the valence. In other cases such as for metals and alloys the structures are better considered as arrangements of close-packed atoms. Crystals which do not have inversion symmetry also display the piezoelectric effect . The presence or absence of inversion symmetry also has numerous consequences for the properties of solids, as does the mathematical relationships between the different crystal symmetries.

Real polyhedra in crystals often lack the uniformity anticipated in their bonding geometry. Common irregularities found in crystallography include distortions and disorder. Distortion involves the warping of polyhedra due to nonuniform bonding lengths, often due to differing electrostatic interactions between heteroatoms or electronic effects such as Jahn–Teller distortions . For instance, a titanium center will likely bond evenly to six oxygens in an octahedra, but distortion would occur if one of the oxygens were replaced with a more electronegative fluorine. Distortions will not change the inherent geometry of the polyhedra—a distorted octahedron is still classified as an octahedron, but strong enough distortions can have an effect on the centrosymmetry of a compound. Disorder involves a split occupancy over two or more sites, in which an atom will occupy one crystallographic position in a certain percentage of polyhedra and the other in the remaining positions. Disorder can influence the centrosymmetry of certain polyhedra as well, depending on whether or not the occupancy is split over an already-present inversion center.

Centrosymmetry applies to the crystal structure as a whole, not just individual polyhedra. Crystals are classified into thirty-two crystallographic point groups which describe how the different polyhedra arrange themselves in space in the bulk structure. Of these thirty-two point groups, eleven are centrosymmetric. The presence of noncentrosymmetric polyhedra does not guarantee that the point group will be the same—two non-centrosymmetric shapes can be oriented in space in a manner which contains an inversion center between the two. Two tetrahedra facing each other can have an inversion center in the middle, because the orientation allows for each atom to have a reflected pair. The inverse is also true, as multiple centrosymmetric polyhedra can be arranged to form a noncentrosymmetric point group.

## Inversion with respect to the origin

Inversion with respect to the origin corresponds to additive inversion of the position vector, and also to scalar multiplication by − 1. The operation commutes with every other linear transformation , but not with translation : it is in the center of the general linear group . "Inversion" without indicating "in a point", "in a line" or "in a plane", means this inversion; in physics 3-dimensional reflection through the origin is also called a parity transformation .

In mathematics, reflection through the origin refers to the point reflection of Euclidean space R n across the origin of the Cartesian coordinate system . Reflection through the origin is an orthogonal transformation corresponding to scalar multiplication by $-1$ , and can also be written as $-I$ , where $I$ is the identity matrix . In three dimensions, this sends $(x,y,z)\mapsto (-x,-y,-z)$ , and so forth.

### Representations

As a scalar matrix , it is represented in every basis by a matrix with $-1$ on the diagonal, and, together with the identity, is the center of the orthogonal group $O(n)$ .

It is a product of n orthogonal reflections (reflection through the axes of any orthogonal basis ); note that orthogonal reflections commute.

In 2 dimensions, it is in fact rotation by 180 degrees, and in dimension $2n$ , it is rotation by 180 degrees in n orthogonal planes; note again that rotations in orthogonal planes commute.

### Properties

It has determinant $(-1)^{n}$ (from the representation by a matrix or as a product of reflections). Thus it is orientation-preserving in even dimension, thus an element of the special orthogonal group SO(2 n ), and it is orientation-reversing in odd dimension, thus not an element of SO(2 n + 1) and instead providing a splitting of the map $O(2n+1)\to \pm 1$ , showing that $O(2n+1)=SO(2n+1)\times \{\pm I\}$ as an internal direct product .

- Together with the identity, it forms the center of the orthogonal group .

- It preserves every quadratic form, meaning $Q(-v)=Q(v)$ , and thus is an element of every indefinite orthogonal group as well.

- It equals the identity if and only if the characteristic is 2.

- It is the longest element of the Coxeter group of signed permutations .

Analogously, it is a longest element of the orthogonal group, with respect to the generating set of reflections: elements of the orthogonal group all have length at most n with respect to the generating set of reflections, and reflection through the origin has length n, though it is not unique in this: other maximal combinations of rotations (and possibly reflections) also have maximal length.

### Geometry

In SO(2 r ), reflection through the origin is the farthest point from the identity element with respect to the usual metric. In O(2 r + 1), reflection through the origin is not in SO(2 r +1) (it is in the non-identity component), and there is no natural sense in which it is a "farther point" than any other point in the non-identity component, but it does provide a base point in the other component.

### Clifford algebras and spin groups

It should not be confused with the element $-1\in \mathrm {Spin} (n)$ in the spin group . This is particularly confusing for even spin groups, as $-I\in SO(2n)$ , and thus in $\operatorname {Spin} (n)$ there is both $-1$ and 2 lifts of $-I$ .

Reflection through the identity extends to an automorphism of a Clifford algebra , called the main involution or grade involution.

Reflection through the identity lifts to a pseudoscalar .
