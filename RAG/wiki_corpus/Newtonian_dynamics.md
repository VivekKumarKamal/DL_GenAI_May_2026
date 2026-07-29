# Newtonian dynamics

> **Query Topic**: Modified Newtonian Dynamics (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 47, Frequency: 31)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Newtonian_dynamics

---

In physics, Newtonian dynamics (also known as Newtonian mechanics ) is the study of the dynamics of a particle or a small body according to Newton's laws of motion .

## Mathematical generalizations

Typically, the Newtonian dynamics occurs in a three-dimensional Euclidean space , which is flat. However, in mathematics Newton's laws of motion can be generalized to multidimensional and curved spaces. Often the term Newtonian dynamics is narrowed to Newton's second law $\displaystyle m\,\mathbf {a} =\mathbf {F}$ .

## Newton's second law in a multidimensional space

Consider $\displaystyle N$ particles with masses $\displaystyle m_{1},\,\ldots ,\,m_{N}$ in the regular three-dimensional Euclidean space . Let $\displaystyle \mathbf {r} _{1},\,\ldots ,\,\mathbf {r} _{N}$ be their radius-vectors in some inertial coordinate system. Then the motion of these particles is governed by Newton's second law applied to each of them

The three-dimensional radius-vectors $\displaystyle \mathbf {r} _{1},\,\ldots ,\,\mathbf {r} _{N}$ can be built into a single $\displaystyle n=3N$ -dimensional radius-vector. Similarly, three-dimensional velocity vectors $\displaystyle \mathbf {v} _{1},\,\ldots ,\,\mathbf {v} _{N}$ can be built into a single $\displaystyle n=3N$ -dimensional velocity vector:

In terms of the multidimensional vectors ( 2 ) the equations ( 1 ) are written as

i.e. they take the form of Newton's second law applied to a single particle with the unit mass $\displaystyle m=1$ .

Definition . The equations ( 3 ) are called the
equations of a Newtonian dynamical system in a flat multidimensional Euclidean space , which is called the configuration space of this system. Its points are marked by the radius-vector $\displaystyle \mathbf {r}$ . The space whose points are marked by the pair of vectors $\displaystyle (\mathbf {r} ,\mathbf {v} )$ is called the phase space of the dynamical system ( 3 ).

## Euclidean structure

The configuration space and the phase space of the dynamical system ( 3 ) both are Euclidean spaces, i. e. they are equipped with a Euclidean structure. The Euclidean structure of them is defined so that the kinetic energy of the single multidimensional particle with the unit mass $\displaystyle m=1$ is equal to the sum of kinetic energies of the three-dimensional particles with the masses $\displaystyle m_{1},\,\ldots ,\,m_{N}$ :

## Constraints and internal coordinates

In some cases the motion of the particles with the masses $\displaystyle m_{1},\,\ldots ,\,m_{N}$ can be constrained. Typical constraints look like scalar equations of the form

Constraints of the form ( 5 ) are called holonomic and scleronomic . In terms of the radius-vector $\displaystyle \mathbf {r}$ of the Newtonian dynamical system ( 3 ) they are written as

Each such constraint reduces by one the number of degrees of freedom of the Newtonian dynamical system ( 3 ). Therefore, the constrained system has $\displaystyle n=3\,N-K$ degrees of freedom.

Definition . The constraint equations ( 6 ) define an $\displaystyle n$ -dimensional manifold $\displaystyle M$ within the configuration space of the Newtonian dynamical system ( 3 ). This manifold $\displaystyle M$ is called the configuration space of the constrained system. Its tangent bundle $\displaystyle TM$ is called the phase space of the constrained system.

Let $\displaystyle q^{1},\,\ldots ,\,q^{n}$ be the internal coordinates of a point of $\displaystyle M$ . Their usage is typical for the Lagrangian mechanics . The radius-vector $\displaystyle \mathbf {r}$ is expressed as some definite function of $\displaystyle q^{1},\,\ldots ,\,q^{n}$ :

The vector-function ( 7 ) resolves the constraint equations ( 6 ) in the sense that upon substituting ( 7 ) into ( 6 ) the equations ( 6 ) are fulfilled identically in $\displaystyle q^{1},\,\ldots ,\,q^{n}$ .

## Internal presentation of the velocity vector

The velocity vector of the constrained Newtonian dynamical system is expressed in terms of the partial derivatives of the vector-function
( 7 ):

The quantities $\displaystyle {\dot {q}}^{1},\,\ldots ,\,{\dot {q}}^{n}$ are called internal components of the velocity vector. Sometimes they are denoted with the use of a separate symbol

and then treated as independent variables. The quantities

are used as internal coordinates of a point of the phase space $\displaystyle TM$ of the constrained Newtonian dynamical system.

## Embedding and the induced Riemannian metric

Geometrically, the vector-function ( 7 ) implements an embedding of the configuration space $\displaystyle M$ of the constrained Newtonian dynamical system into the $\displaystyle 3\,N$ -dimensional flat configuration space of the unconstrained 
Newtonian dynamical system ( 3 ). Due to this embedding the Euclidean structure of the ambient space induces the Riemannian metric onto the manifold $\displaystyle M$ . The components of the metric tensor of this induced metric are given by the formula

where $\displaystyle (\ ,\ )$ is the scalar product associated with the Euclidean structure ( 4 ).

## Kinetic energy of a constrained Newtonian dynamical system

Since the Euclidean structure of an unconstrained system of $\displaystyle N$ particles is introduced through their kinetic energy, the induced Riemannian structure on the configuration space $\displaystyle N$ of a constrained system preserves this relation to the kinetic energy:

The formula ( 12 ) is derived by substituting ( 8 ) into ( 4 ) and taking into account ( 11 ).

## Constraint forces

For a constrained Newtonian dynamical system the constraints described by the equations ( 6 ) are usually implemented by some mechanical framework. This framework produces some auxiliary forces including the force that maintains the system within its configuration manifold $\displaystyle M$ . Such a maintaining force is perpendicular to $\displaystyle M$ . It is called the normal force . The force $\displaystyle \mathbf {F}$ from ( 6 ) is subdivided into two components

The first component in ( 13 ) is tangent to the configuration manifold $\displaystyle M$ . The second component is perpendicular to $\displaystyle M$ . In coincides with the normal force $\displaystyle \mathbf {N}$ . Like the velocity vector ( 8 ), the tangent force $\displaystyle \mathbf {F} _{\parallel }$ has its internal presentation

The quantities $F^{1},\,\ldots ,\,F^{n}$ in ( 14 ) are called the internal components of the force vector.

## Newton's second law in a curved space

The Newtonian dynamical system ( 3 ) constrained to the configuration manifold $\displaystyle M$ by the constraint equations ( 6 ) is described by the differential equations

where $\Gamma _{ij}^{s}$ are Christoffel symbols of the metric connection produced by the Riemannian metric ( 11 ).

## Relation to Lagrange equations

Mechanical systems with constraints are usually described by Lagrange equations :

where $T=T(q^{1},\ldots ,q^{n},w^{1},\ldots ,w^{n})$ is the kinetic energy the constrained dynamical system given by the formula ( 12 ). The quantities $Q_{1},\,\ldots ,\,Q_{n}$ in 
( 16 ) are the inner covariant components of the tangent force vector $\mathbf {F} _{\parallel }$ (see ( 13 ) and ( 14 )). They are produced from the inner contravariant components $F^{1},\,\ldots ,\,F^{n}$ of the vector $\mathbf {F} _{\parallel }$ by means of the standard index lowering procedure using the metric ( 11 ):

The equations ( 16 ) are equivalent to the equations ( 15 ). However, the metric ( 11 ) and
other geometric features of the configuration manifold $\displaystyle M$ are not explicit in ( 16 ). The metric ( 11 ) can be recovered from the kinetic energy $\displaystyle T$ by means of the formula
