# Vector (mathematics and physics)

> **Query Topic**: geometric quantization in mathematical physics (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 241, Frequency: 8)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)

---

In mathematics and physics , a vector is a generalization of a single number . It may denote a vector quantity , i.e., physical quantity that cannot be expressed by a single scalar quantity . The term may also be used to refer to elements of vector spaces , that can be added together and multiplied ("scaled") by scalars . In some contexts, vectors are tuples , which are finite sequences (of numbers or other objects) of a fixed length.

Historically, vectors were introduced in geometry and physics (typically in mechanics ) for quantities that have both a magnitude and a direction, such as displacements , forces and velocity . Such quantities are represented by geometric vectors in the same way as distances , masses and time are represented by real numbers .

Both geometric vectors and tuples can be added and scaled, and these vector operations led to the concept of a vector space, which is a set equipped with a vector addition and a scalar multiplication that satisfy some axioms generalizing the main properties of operations on the above sorts of vectors. A vector space formed by geometric vectors is called a Euclidean vector space , and a vector space formed by tuples is called a coordinate vector space .

Many vector spaces are considered in mathematics, such as extension fields , polynomial rings , algebras and function spaces . The term vector is generally not used for elements of these vector spaces, and is generally reserved for geometric vectors, tuples, and elements of unspecified vector spaces (for example, when discussing general properties of vector spaces).

## Vectors in Euclidean geometry

In mathematics , physics , and engineering , a Euclidean vector or simply a vector (sometimes called a geometric vector or spatial vector ) is a geometric object that has magnitude (or length ) and direction . Euclidean vectors can be added and scaled to form a vector space . A vector quantity is a vector-valued physical quantity , including units of measurement and possibly a support , formulated as a directed line segment . A vector is frequently depicted graphically as an arrow connecting an initial point A with a terminal point B , and denoted by ${\textstyle {\stackrel {\longrightarrow }{AB}}.}$

A vector is what is needed to "carry" the point A to the point B ; the Latin word vector means 'carrier'. It was first used by 18th century astronomers investigating planetary revolution around the Sun. The magnitude of the vector is the distance between the two points, and the direction refers to the direction of displacement from A to B . Many algebraic operations on real numbers such as addition , subtraction , multiplication , and negation have close analogues for vectors, operations which obey the familiar algebraic laws of commutativity , associativity , and distributivity . These operations and associated laws qualify Euclidean vectors as an example of the more generalized concept of vectors defined simply as elements of a vector space .

Vectors play an important role in physics : the velocity and acceleration of a moving object and the forces acting on it can all be described with vectors. Many other physical quantities can be usefully thought of as vectors. Although most of them do not represent distances (except, for example, position or displacement ), their magnitude and direction can still be represented by the length and direction of an arrow. The mathematical representation of a physical vector depends on the coordinate system used to describe it. Other vector-like mathematical objects that describe physical quantities , such as pseudovectors and tensors , transform in a similar way under changes of the coordinate system.

## Vector quantities

In the natural sciences , a vector quantity (also known as a vector physical quantity, physical vector, or simply vector) is a vector-valued physical quantity . It is typically formulated as the product of a unit of measurement and a vector numerical value ( unitless ), often a Euclidean vector with magnitude and direction .
For example, a position vector in physical space may be expressed as three Cartesian coordinates with SI unit of meters .

In physics and engineering , particularly in mechanics , a physical vector may be endowed with additional structure compared to a geometrical vector. A bound vector is defined as the combination of an ordinary vector quantity and a point of application or point of action . Bound vector quantities are formulated as a directed line segment , with a definite initial point besides the magnitude and direction of the main vector. For example, a force on the Euclidean plane has two Cartesian components in SI unit of newtons (describing the magnitude and direction of the force) and an accompanying two-dimensional position vector in meters (describing the point of application of the force), for a total of four numbers on the plane (and six in space). A simpler example of a bound vector is the translation vector from an initial point to an end point; in this case, the bound vector is an ordered pair of points in the same position space, with all coordinates having the same quantity dimension and unit (length and meters). A sliding vector is the combination of an ordinary vector quantity and a line of application or line of action , over which the vector quantity can be translated (without rotations).
A free vector is a vector quantity having an undefined point or region of application; it can be freely translated with no consequences; a displacement vector is a prototypical example of free vector.

Aside from the notion of units and support, physical vector quantities may also differ from Euclidean vectors in terms of metric .
For example, an event in spacetime may be represented as a position four-vector , with coherent derived unit of meters: it includes a position Euclidean vector and a timelike component, t ⋅ c 0 (involving the speed of light ).
In that case, the Minkowski metric is adopted instead of the Euclidean metric .

Vector quantities are a generalization of scalar quantities and can be further generalized as tensor quantities . Individual vectors may be ordered in a sequence over time (a time series ), such as position vectors discretizing a trajectory .
A vector may also result from the evaluation , at a particular instant, of a continuous vector-valued function (e.g., the pendulum equation ).
In the natural sciences, the term "vector quantity" also encompasses vector fields defined over a two- or three-dimensional region of space, such as wind velocity over Earth's surface. Pseudo vectors and bivectors are also admitted as physical vector quantities.

## Vector spaces

In mathematics , a vector space (also called a linear space) is a set whose elements, often called vectors , can be added together and multiplied ("scaled") by numbers called scalars . The operations of vector addition and scalar multiplication must satisfy certain requirements, called vector axioms . Real vector spaces and complex vector spaces are kinds of vector spaces based on different kinds of scalars: real numbers and complex numbers . Scalars can also be, more generally, elements of any field .

Vector spaces generalize Euclidean vectors , which allow modeling of physical quantities (such as forces and velocity ) that have not only a magnitude , but also a direction . The concept of vector spaces is fundamental for linear algebra , together with the concept of matrices , which allows computing in vector spaces. This provides a concise and synthetic way for manipulating and studying systems of linear equations .

Vector spaces are characterized by their dimension , which, roughly speaking, specifies the number of independent directions in the space. This means that for two vector spaces over a given field and with the same dimension, the properties that depend only on the vector-space structure are exactly the same (that is, the vector spaces are isomorphic ). A vector space is finite-dimensional if its dimension is a natural number . Otherwise, it is infinite-dimensional , and its dimension is an infinite cardinal . Finite-dimensional vector spaces occur naturally in geometry and related areas. Infinite-dimensional vector spaces occur in many areas of mathematics. For example, polynomial rings are countably infinite-dimensional vector spaces, and many function spaces have the cardinality of the continuum as a dimension.

Many vector spaces that are considered in mathematics are also endowed with other structures . This is the case of algebras , which include field extensions , polynomial rings, associative algebras and Lie algebras . This is also the case of topological vector spaces , which include function spaces, inner product spaces , normed spaces , Hilbert spaces and Banach spaces .

## Vectors in algebra

Every algebra over a field is a vector space, but elements of an algebra are generally not called vectors. However, in some cases, they are called vectors , mainly due to historical reasons.

- Vector quaternion , a quaternion with a zero real part

- Multivector or p -vector , an element of the exterior algebra of a vector space.

- Spinors , also called spin vectors , have been introduced for extending the notion of rotation vector . In fact, rotation vectors represent well rotations locally , but not globally, because a closed loop in the space of rotation vectors may induce a curve in the space of rotations that is not a loop. Also, the manifold of rotation vectors is orientable , while the manifold of rotations is not. Spinors are elements of a vector subspace of some Clifford algebra .

- Witt vector , an infinite sequence of elements of a commutative ring, which belongs to an algebra over this ring , and has been introduced for handling carry propagation in the operations on p-adic numbers .

## Data represented by vectors

The set $\mathbb {R} ^{n}$ of tuples of n real numbers has a natural structure of vector space defined by component-wise addition and scalar multiplication . It is common to call these tuples vectors , even in contexts where vector-space operations do not apply. More generally, when some data can be represented naturally by vectors, they are often called vectors even when addition and scalar multiplication of vectors are not valid operations on these data. [ disputed – discuss ] Here are some examples.

- Rotation vector , a Euclidean vector whose direction is that of the axis of a rotation and magnitude is the angle of the rotation.

- Burgers vector , a vector that represents the magnitude and direction of the lattice distortion of dislocation in a crystal lattice

- Interval vector , in musical set theory, an array that expresses the intervallic content of a pitch-class set

- Probability vector , in statistics, a vector with non-negative entries that sum to one.

- Random vector or multivariate random variable , in statistics , a set of real -valued random variables that may be correlated . However, a random vector may also refer to a random variable that takes its values in a vector space.

- Logical vector , a vector of 0s and 1s ( Booleans ).

## Vectors in calculus

Calculus serves as a foundational mathematical tool in the realm of vectors, offering a framework for the analysis and manipulation of vector quantities in diverse scientific disciplines, notably physics and engineering . Vector-valued functions, where the output is a vector, are scrutinized using calculus to derive essential insights into motion within three-dimensional space. Vector calculus extends traditional calculus principles to vector fields, introducing operations like gradient , divergence , and curl , which find applications in physics and engineering contexts. Line integrals , crucial for calculating work along a path within force fields, and surface integrals , employed to determine quantities like flux , illustrate the practical utility of calculus in vector analysis. Volume integrals , essential for computations involving scalar or vector fields over three-dimensional regions, contribute to understanding mass distribution , charge density , and fluid flow rates. [ citation needed ]
