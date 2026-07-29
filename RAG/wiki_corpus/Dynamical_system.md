# Dynamical system

> **Query Topic**: mathematical function is commonly used to characterize linear time-invariant systems (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 131, Frequency: 2)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Dynamical_system

---

In mathematics , physics , engineering and systems theory , a dynamical system is the description of how a system evolves in time.
The study of dynamical systems is the focus of dynamical systems theory . It has applications to a wide variety of fields such as mathematics, physics, biology , chemistry , engineering , economics , history , and medicine . Dynamical systems are a fundamental part of chaos theory , logistic map dynamics, bifurcation theory , the self-assembly and self-organization processes, and the edge of chaos concept.

For example, an astronomer can experimentally record the positions of how the planets move in the sky, and this can be considered a complete enough description of a dynamical system. In the case of planets there is also enough knowledge to codify this information as a set of differential equations with initial conditions , or as a map from the present state to a future state in a predefined state space with a time parameter t , 
or as an orbit in phase space .

## Overview

The concept of a dynamical system has its origins in Newtonian mechanics and more precisely in celestial mechanics . There, as in other natural sciences and engineering disciplines, there is some need to predict the evolution of the system, but maybe also pose other questions such as stability, qualitative or long term behaviour, dependence on parameters, existence of periodic, stochastic or chaotic behaviour. The relation from one state and another is either explicit such as a function in the parameter t predicting position and velocity of a particle or implicit such as a differential equation , difference equation or other time scale . Some times it may not be possible to define such a description, there may not even be a differential equation predicting stock price , or it maybe impossible to build one but still talk stock prices can be considered a dynamical system based on experimental data changing over time.

Important properties are existence and uniqueness of solutions, integrability (i.e. the existence of conserved quantities), the possibility to solve the system and be able to compute the state at any point in time. Other properties are whether the system is discrete , continuous , differentiable , smooth , deterministic , ergodic , stochastic or chaotic .

If the system can be solved, then, given an initial point, it is possible to determine all its future positions, a collection of points known as a trajectory or orbit .

Before the advent of computers , finding an orbit required sophisticated mathematical techniques and could be accomplished only for a small class of dynamical systems. Numerical methods implemented on electronic computing machines have simplified the task of determining the orbits of a dynamical system.

For simple dynamical systems, knowing the trajectory is often sufficient, but most dynamical systems are too complicated to be understood in terms of individual trajectories. The difficulties arise because:

- The systems studied may only be known approximately—the parameters of the system may not be known precisely or terms may be missing from the equations. The approximations used bring into question the validity or relevance of numerical solutions. To address these questions several notions of stability have been introduced in the study of dynamical systems, such as Lyapunov stability or structural stability . The stability of the dynamical system implies that there is a class of models or initial conditions for which the trajectories would be equivalent. The operation for comparing orbits to establish their equivalence changes with the different notions of stability.

- The type of trajectory may be more important than one particular trajectory. Some trajectories may be periodic, whereas others may wander through many different states of the system. Applications often require enumerating these classes or maintaining the system within one class. Classifying all possible trajectories has led to the qualitative study of dynamical systems, that is, properties that do not change under coordinate changes. Linear dynamical systems and systems that have two numbers describing a state are examples of dynamical systems where the possible classes of orbits are understood.

- The behavior of trajectories as a function of a parameter may be what is needed for an application. As a parameter is varied, the dynamical systems may have bifurcation points where the qualitative behavior of the dynamical system changes. For example, it may go from having only periodic motions to apparently erratic behavior, as in the transition to turbulence of a fluid .

- The trajectories of the system may appear erratic, as if random. In these cases it may be necessary to compute averages using one very long trajectory or many different trajectories. The averages are well defined for ergodic systems and a more detailed understanding has been worked out for hyperbolic systems . Understanding the probabilistic aspects of dynamical systems has helped establish the foundations of statistical mechanics and of chaos .

## Examples

Simple examples include the mathematical models that describe the swinging of a clock pendulum , the flow of water in a pipe , the random motion of particles in the air , and the number of fish each springtime in a lake .

- Three body problem : Approximate trajectories of three identical bodies located at the vertices of a scalene triangle and having zero initial velocities.

- Arnold cat map : picture showing how the linear map stretches the unit square and how its pieces are rearranged when the modulo operation is performed. The lines with the arrows show the direction of the contracting and expanding eigenspaces

- Baker's map : Example of a measure that is invariant under the action of the (unrotated) baker's map: an invariant measure . Applying the baker's map to this image always results in exactly the same image.

- Billiards : A particle moving inside the Bunimovich stadium, a well-known chaotic billiard.

- Outer billiards : defined relative to a pentagon

- Bouncing ball dynamics : The motion is not quite parabolic due to air resistance .

- Bifurcation diagram for a Circle map . Black regions correspond to Arnold tongues .

- The recursive application of a Complex quadratic polynomial as a complex plane map gives a Dynamical system. Here there is a Dynamical plane with a Julia set and critical orbit.

- Motion of the double compound pendulum (from numerical integration of the equations of motion)

- Dyadic transformation xy plot where x = x 0 ∈ [0, 1] is rational and y = x n for all n

- The Lorenz attractor arises in the study of the Lorenz oscillator , a dynamical system.

- An example of a Kármán vortex street , an emergent phenomenon from Fluid dynamics .

- The Kicked Rotor , a famous chaotic system

- Orbital resonance in Saturn's rings .

- The chaotic rotation of Hyperion . The Solar System as a whole is full of examples of dynamical systems from Celestial mechanics

Other classical examples include:

- Hénon map

- Irrational rotation

- Kaplan–Yorke map

- Lorenz system

- Quadratic map simulation system

- Rössler map

- Swinging Atwood's machine

- Tent map

Any mathematical map can be treated as the definition of a dynamical system for example:

- List of chaotic maps

## History

Many people regard French mathematician Henri Poincaré as the founder of dynamical systems. Poincaré published two now classical monographs, "New Methods of Celestial Mechanics" (1892–1899) and "Lectures on Celestial Mechanics" (1905–1910). In them, he successfully applied the results of their research to the problem of the motion of three bodies and studied in detail the behavior of solutions (frequency, stability, asymptotic, and so on). These papers included the Poincaré recurrence theorem , which states that certain systems will, after a sufficiently long but finite time, return to a state very close to the initial state.

Aleksandr Lyapunov developed many important approximation methods. His methods, which he developed in 1899, make it possible to define the stability of sets of ordinary differential equations. He created the modern theory of the stability of a dynamical system.

In 1913, George David Birkhoff proved Poincaré's " Last Geometric Theorem ", a special case of the three-body problem , a result that made him world-famous. In 1927, he published his Dynamical Systems .

Birkhoff's most durable result has been his 1931 discovery of what is now called the ergodic theorem .
Combining insights from physics on the ergodic hypothesis with measure theory , this theorem solved, at least in principle, a fundamental problem of statistical mechanics . The ergodic theorem has also had repercussions for dynamics.

Stephen Smale made significant advances as well. His first contribution was the Smale horseshoe that jumpstarted significant research in dynamical systems. He also outlined a research program carried out by many others.

Oleksandr Mykolaiovych Sharkovsky developed Sharkovsky's theorem on the periods of discrete dynamical systems in 1964. One of the implications of the theorem is that if a discrete dynamical system on the real line has a periodic point of period 3, then it must have periodic points of every other period.

In the late 20th century, the dynamical system perspective to partial differential equations started gaining popularity. Palestinian mechanical engineer Ali H. Nayfeh applied nonlinear dynamics in mechanical and engineering systems. His pioneering work in applied nonlinear dynamics has been influential in the construction and maintenance of machines and structures that are common in daily life, such as ships , cranes , bridges , buildings , skyscrapers , jet engines , rocket engines , aircraft and spacecraft .

## Generalizations

The most general definition unifies several concepts in mathematics such as ordinary differential equations and ergodic theory , physics such as phase space , quantum state and thermodynamic state , engineering such as system theory , control theory and even information theory .

### Mathematical intuition

From a mathematics perspective in the most general case the state space X is treated as a generic set of abstract algebra . This space X
has a semi-group structure on it (i.e. where only associativity is required) and there is most often a natural choice for an Identity element, which is typically attached to the origin of the chosen reference frame . This semi-group can be intuitively interpreted as the time coordinate t. Time in fact has an addition operation and an origin, the identity, like a group. 
The action of the semi-group on X is a set of maps from X to itself parametric in the time t, and this is intuitively the time evolution.

### Generalizing the state space

It is possible to allow different choices of the state space such as a function space (e.g. the pressure, temperature and velocity of a gas in a rocket are a function in the space of solutions of some fluid dynamics PDEs and they may vary over time), a quantum state space (e.g. the state of an atom can be described by a set of functions in an hilbert space and a set of probabilities for these), or a manifold (e.g. the state of a black hole can be described by a metric tensor on a Riemann manifold and its position will be a vector in the same manifold). Other choices can be a phase space , a Configuration space or even a discrete space (e.g. the set of prime numbers or a finite field ).

### Time as a multidimensional manifold

Time can be generalized too as a generic set of continuous parameters, for example the control parameters of a robot can be a manifold .
There is no need that time has a direction, that is smooth or even that it has whatsoever meaning similar to the intuition of time , in fact it can be generalized to even more general algebraic objects.

A general class of systems are defined over multiple independent variables and are therefore called multidimensional systems . Such systems are useful for modeling, and for example in image processing . [ citation needed ]

Time typically is considered often an external parameter as in classical and quantum mechanics , and this is typically called time domain representation, and it goes hand in hand with the Hamiltonian mechanics formulation. This is not necessarily always the case: general relativity for example is frame independent, and gravity has an influence over time too, and in quantum electrodynamics the use of the Lagrangian mechanics formulation is more common where time and space are on same footing. In both cases the literature still talks about dynamical systems.

### Discrete dynamical system

Time can also be a discrete parameter. When time is generalized to the multi-dimensional case, i.e. as a general set of control or external parameters, this space can be interpreted as a Lattice , i.e. as the discrete points of a manifold or the tics of a stock price . Discrete Time events therefore can be counted by integers, for example like the measurements of the position of the planets in the sky, but this can vastly differ from the intuition of time as a clock that has equispaced time events. One of the tasks is typically to extract some mathematical model from the data.

### Not deterministic

The evolution rule of the dynamical system is a function that describes what future states follow from the current state. Often the function is deterministic , that is, for a given time interval only one future state follows from the current state. However, some systems are not deterministic they may allow multiple future states (i.e. the maps are generalized into multivalued functions and not uniquely defined everywhere) and the system can be subject to a bifurcation .

### Stochastic

Some systems are also stochastic , either in the input parameters such as an oscillator with a random force , or in the initial conditions, or in the predicted variables as in a Stochastic differential equation . In that random events also affect the evolution of the state variables, and this includes stochastic jump processes which are not continuous, a prototype example of a stochastic dynamical system are stock prices .

### Chaotic and Quantum systems

Lastly, there are chaotic systems (i.e. typically deterministic but not predictable) such as:

- complex dynamics

- Hyperbolic dynamics

- multiplicative chaos

- non-deterministic chaos

And quantum systems (i.e. deterministic until they are measured), or quantum chaotic systems.

## Formal definition

Assume that X is a non empty set with elements called states.
Assume a general transformation: $T:X\to X$

It is possible to interpret X as a state space and T as the evolution between states. Adding different structures on T and on X allows to model different properties of the dynamical system.

It is possible to model time evolution: ${\hat {T}}$ can be a semigroup with one parameter $t$ called time that will also belong to a semi-group such as $N(t>0)$ in the discrete time case, $R^{+}(t>0)$ in the continuous time case.

A semigroup structure introduces associativity ${\hat {T_{1}}}({\hat {T_{2}}}{\hat {T_{3}}})=({\hat {T_{1}}}{\hat {T_{2}}}){\hat {T_{3}}}$ which implies a composition law between different time evolutions: ${\hat {T}}(t_{1}+t_{2})={\hat {T}}(t_{1}){\hat {T}}(t_{2})$ this is also ultimately a homomorphism .

It is possible to define an origin of time $t=0$ adding an identity to the semi-group ${\hat {T}}(0)=\mathbf {1}$ and it is finally possible also to model reversible time evolution: T can be a group such as $\mathbf {Z}$ or $R$ , and being a group this in fact has a definition of inverse transformations: $\exists !{\hat {T}}^{-1}:{\hat {T}}^{-1}={\hat {T}}(-t),{\hat {T}}(-t){\hat {T}}(t)=\mathbf {1}$

More commonly there are multiple classes of definitions for a dynamical system: a first one is motivated by ordinary differential equations and is geometrical in flavor, there is an additional differentiability structure; a second one is motivated by ergodic theory and is measure theoretical in flavor, there is an additional topological structure and a last one which is motivated by Category theory and is more abstract in flavour.

## Geometrical definition

In the geometrical definition, a dynamical system is the tuple $\langle {\mathcal {T}},{\mathcal {M}},f\rangle$ . ${\mathcal {T}}$ is the domain for time – there are many choices, usually the reals or the integers, possibly restricted to be non-negative. ${\mathcal {M}}$ is a manifold , and typically, but not always, f is an evolution rule t → f t (with $t\in {\mathcal {T}}$ ) such that f t is a diffeomorphism of the manifold to itself.

Typically there is some extra structure on the manifold:

- To be locally a Banach space , this allows to use standard techniques of functional analysis .

- A symplectic structure which is the typical case for a phase space

- A Euclidean Space such as configuration space due to holonomic constraints

- A discrete structure like a graph .

- A set of diffeomorphisms such as coordinate transformations

- A metric tensor like in a Riemann manifold

### Real dynamical system

A real dynamical system , real-time dynamical system , continuous time dynamical system , or flow is a tuple ( T , M , Φ) with T an open interval in the real numbers R , M a manifold typically but not necessarily locally homeomorphic to a Banach space , and Φ a continuous function .

Being locally homeomorphic to a Banach space allows to use theorems of existence and uniqueness of solutions for differential equations, and linear operators, and this makes it analogous the classical definition based on a system of differential equations.

#### Differentiability

If Φ is continuously differentiable the system is called a differentiable dynamical system . The function f is therefore a "smooth" mapping of the time-domain ${\mathcal {T}}$ into the space of diffeomorphisms of the manifold to itself. In other terms, f ( t ) is a diffeomorphism , for every time t in the domain ${\mathcal {T}}$ The manifold M is then typically locally diffeomorphic to a Banach space .

#### Dimensionality

If the manifold M is locally diffeomorphic to R n , the dynamical system is finite-dimensional ; if not, the dynamical system is infinite-dimensional . [ clarification needed ]

#### Flows

When T is taken to be the reals, the dynamical system is called global or a flow ; and if T is restricted to the non-negative reals, then the dynamical system is a semi-flow . [ clarification needed ]

#### Classical definition

The modern geometrical definition assumes a map that provides an explicit description of the dynamical system, this is motivated by ergodic theory , by partial differential equations and by mathematical techniques that go beyond differential equations. An explicit description is often not available, the classical geometrical definition is implicit, rooted in classical mechanics, and based on a standard set of ordinary differential equations and a finite set of degrees of freedom :

${\frac {dx_{i}}{dt}}=u_{i}(x_{1},...,x_{n},t);(i=1,...,n)$ There can be different regularity conditions to the functions $u_{i}$ such as being differentiable or analytic .

This definition implies the existence and uniqueness of solutions of such equations.

#### Lagrangian Dynamical system

It is also possible to cast the geometrical definition in terms of a variational principle :

$\Phi (\gamma )=\int _{t_{0}}^{t_{1}}L(\gamma ,{\dot {\gamma }})dt$ where ${\dot {\gamma }}\in TM_{\gamma (t)}$ is called velocity vector.

#### Hamiltonian Dynamical system

Dually to the Lagrangian it is possible to use a Hamiltonian formulation which includes a Symplectic or Poisson manifold structure on the phase space .

#### Non integrable systems

To be complete there are also systems that are typically not integrable systems such as dissipative systems , nonholonomic systems and systems that have a contact manifold structure for example systems that have a no slip boundary condition (i.e. some constraint on the velocity on the boundary).

### Algebraic dynamical systems

An important class of systems from a mathematical perspective is when the map $f$ is algebraic or in general when the map is implicitly defined by a set of algebraic equations and the manifold ${\mathcal {M}}$ is ideally defined on a generic field .

### Discrete dynamical system

A discrete-time dynamical system is a tuple ( T , M , Φ), where M is a manifold locally diffeomorphic to a Banach space , and Φ is a function. T can be taken to be the integers or the non negative integers. The manifold itself can be a graph or made discrete for example with a discrete topology .

## Measure theoretical definition

A dynamical system may be defined formally as the triplet ( T , ${\mathfrak {M}}$ , Φ), where Φ is a measure-preserving transformation of a measure space ${\mathfrak {M}}$ , Φ is also the action of a semigroup T as the general case. Here the Measure space ${\mathfrak {M}}$ is defined by the triplet ( X , Σ, μ ), where X is a set , Σ is a sigma-algebra on X and μ is a finite measure on the measurable space ( X , Σ). Often ${\mathfrak {M}}$ is a probability space , i.e. a measure space where the total measure of the full space is 1, in other words with a finite and normalized probability measure .

A map Φ: X → X is said to be Σ-measurable if and only if, for every σ in Σ, one has $\Phi ^{-1}\sigma \in \Sigma$ . A map Φ is said to preserve the measure if and only if, for every σ in Σ, one has $\mu (\Phi ^{-1}\sigma )=\mu (\sigma )$ . Combining the above, a map Φ is said to be a measure-preserving transformation of X , if it is a map from X to itself, it is Σ-measurable, and is measure-preserving.

The triplet 
( T , ${\mathfrak {M}}$ , Φ), with ${\mathfrak {M}}=$ ( X , Σ, μ ) for such a Φ, is then defined to be a measure-preserving dynamical system .

### Conventions

There are two conventions for the definition of the maps:

- Physics and continuous time convention: The map Φ embodies the time evolution of the dynamical system, it is possible to interpret it for discrete time evolution as Φ= $\Phi _{n}$ parametrized by $n\in \mathbb {Z} ^{+}$ or for a continuous time evolution as Φ= $\Phi _{t}$ where $t\in \mathbb {R} ^{+}$ , in the general case each map is different. Assuming an initial time $t_{0}$ and a state vector ${\vec {\mathbb {x} }}(t)\in X$ , the map can be seen as a time translation map ${\vec {\mathbb {x} }}(t+t_{0})={\hat {\Phi }}(t)[{\vec {\mathbb {x} }}(t_{0})]$ . In the discrete case this means that the total map ${\hat {\Phi }}_{n}=\Phi _{n}\circ \Phi _{n-1}\circ \dots \circ \Phi _{1}\circ \Phi _{0}$ can be seen as composition of individual maps. This convention is also related to the study of limit points and Cauchy sequences .

- Mathematics and discrete convention: all maps are defined as the evolution of the state for one time step to the next one, i.e. from $t_{n}\to t_{n+1}$ , or in the continuous case from $t\to t+\delta t$ . The maps ${\hat {\Phi }}_{n}:x\in X,x_{n}\to x_{n+1}$ are the same map $\Phi$ for all time steps $t_{n}$ , this can be interpreted also as an iteration over the map ${\hat {\Phi }}_{n}=\Phi ^{n}=\Phi \circ \Phi \circ \dots \circ \Phi$ . This convention is also related to the study of fixed points , and recursion .

In the language of representation theory : time evolution in the state space X is the induced representation of time translation in the semigroup T, and the map Φ is the group action that induces the representation on X, i.e. there is a homomorphism beteeen the time group T and the state space X where $T(t_{0}+t)=T(t)\circ T(t_{0})$ . In the language of quantum mechanics the infinitesimal generator of time translation $t\to t+\delta t$ is the derivative in time ${\partial }_{t}$ , and also the time evolution operator.

### Examples

- Permutations

- Group actions

- Bernoulli scheme

### Relation to geometric definition

The measure theoretical definition assumes the existence of a measure-preserving transformation, in physical terminology the measure is a probability density function over the phase space . The intuition comes from Hamiltonian systems which are volume preserving. The fact that the energy is an integral of motion induces volume conservation on the phase space, or incompressibility of the flow , extra integrals of motions induce further foliations on the phase space. [ citation needed ] . 
Another intuition comes from permutations which are "incompressible". One can interpret the set of all possible permutations of a set as the automorphism group induced by the conservation of number of elements of the set.

Many different invariant measures can be associated to any one evolution rule, in the same manner as multiple probability densities can induce the same macro-state . If the dynamical system is given by a system of differential equations the appropriate measure must be determined, the symmetries are not explicit and it may not even be possible to define a probability measure in certain patological cases. This makes it difficult to develop ergodic theory starting from differential equations, so it becomes convenient to have a dynamical systems-motivated definition within ergodic theory that side-steps the choice of measure and assumes the choice has been made.

A simple construction (sometimes called the Krylov–Bogolyubov theorem ) shows that for a large class of systems it is always possible to construct a measure so as to make the evolution rule of the dynamical system a measure-preserving transformation. In the construction a given measure of the state space is summed for all future points of a trajectory, assuring the invariance.

Some systems have a natural measure, such as the Liouville measure in Hamiltonian systems , chosen over other invariant measures, such as the measures supported on periodic orbits of the Hamiltonian system. For chaotic dissipative systems the choice of invariant measure is technically more challenging. The measure needs to be supported on the attractor , but attractors have zero Lebesgue measure and the invariant measures must be singular with respect to the Lebesgue measure . For dissipative systems typically a small region of phase space shrinks under time evolution, for chaotic systems a small region of phase space instead typically grows and expands at least to a full finite region of the phase space

For hyperbolic dynamical systems, the Sinai–Ruelle–Bowen measures appear to be the natural choice. [ citation needed ] They are constructed on the geometrical structure of stable and unstable manifolds of the dynamical system [ citation needed ] ; they behave physically under small perturbations [ citation needed ] ; and they explain many of the observed statistics of hyperbolic systems [ citation needed ] . [ clarification needed ]

### Topological dynamical system

A topological dynamical system is a dynamical system ( T , X , Φ) on a locally compact and/or Hausdorff topological space X . Φ is a topological isomorphism and therefore a homeomorphism .

Topological dynamics is typically done from a global perspective, i.e. considering all possible initial conditions and outcomes (e.g. equilibrium points , periodic orbits , attractors or chaos ), the statistics and the groupings of the trajectories, the long term behaviour in time of the system, the homeomorphisms (i.e. continuous deformations) of the trajectories. Typically the trajectories are differentiable , and the systems are also flows .

#### Compactification

It is often useful to study the continuous extension Φ* of Φ to the one-point compactification X* of X . Even after losing the differential structure of the original system, there are compactness arguments to analyze the new system ( R , X* , Φ*). This is similar in spirit to Projective geometry where all limit points to infinity are the same point.
Another more general technique is to use Stone–Čech compactification . which is similar in spirit to affine geometry where all limit points at infinity are considered different.

#### Relevance

In compact dynamical systems the limit set of any orbit is non-empty , compact and simply connected .

## Definition with Category theory

### Categories vs semi-groups

A category X of mathematical objects has a semigroup G of homomorphisms acting on it (topological spaces have continuous maps, sets have arbitrary maps, groups, rings fields or algebras have homomorphisms, measure spaces have measurable maps). We can view each of these categories as a dynamical system. One can even include the category of dynamical systems with suitable homomorphisms. But this viewpoint is not a very useful in itself.

### Definition with monoids

In the context of category theory, categories are always defined together with an Identity map, therefore these definitions are based on monoids instead of semi-groups.

A dynamical system [ citation needed ] is a tuple ( T , X , Φ) where T is a monoid , [ citation needed ] written additively, X is a non-empty set and Φ is a function : $\Phi :U\subseteq (T\times X)\to X$ with: $\mathrm {proj} _{2}(U)=X$ (where $\mathrm {proj} _{2}$ is the 2nd projection map [ citation needed ] ) and for any x in X : $\Phi (0,x)=x$ $\Phi (t_{2},\Phi (t_{1},x))=\Phi (t_{2}+t_{1},x),$ for $\,t_{1},\,t_{2}+t_{1}\in I(x)$ and $\ t_{2}\in I(\Phi (t_{1},x))$ , where we have defined the set $I(x):=\{t\in T:(t,x)\in U\}$ for any x in X .

In particular, in the case that $U=T\times X$ we have for every x in X that $I(x)=T$ and thus that Φ defines a monoid action of T on X .

The function Φ( t , x ) is called the evolution function of the dynamical system: it associates to every point x in the set X a unique image, depending on the variable t , called the evolution parameter . X is called phase space or state space , while the variable x represents an initial state of the system.

We often write: $\Phi _{x}(t)\equiv \Phi (t,x)$ $\Phi ^{t}(x)\equiv \Phi (t,x)$ if we take one of the variables as constant. The function $\Phi _{x}:I(x)\to X$ is called the flow through x and its graph is called the trajectory through x . The set $\gamma _{x}\equiv \{\Phi (t,x):t\in I(x)\}$ is called the orbit through x .
The orbit through x is the image of the flow through x .

A subset S of the state space X is called Φ- invariant if for all x in S and all t in T $\Phi (t,x)\in S.$ Thus, in particular, if S is Φ- invariant , $I(x)=T$ for all x in S . That is, the flow through x must be defined for all time for every element of S .

## Construction of dynamical systems

The concept of evolution in time is central to the theory of dynamical systems as seen in the previous sections: the basic reason for this fact is that the starting motivation of the theory was the study of time behavior of classical mechanical systems . But a system of ordinary differential equations must be solved before it becomes a dynamic system. For example, consider an initial value problem such as the following: ${\dot {\boldsymbol {x}}}={\boldsymbol {v}}(t,{\boldsymbol {x}})$ ${\boldsymbol {x}}|_{t=0}={\boldsymbol {x}}_{0}$ where

- ${\dot {\boldsymbol {x}}}$ represents the velocity of the material point x

- M is a finite dimensional manifold

- v : T × M → TM is a vector field in R n or C n and represents the change of velocity induced by the known forces acting on the given material point in the phase space M . The change is not a vector in the phase space M , but is instead in the tangent space TM .

There is no need for higher order derivatives in the equation, nor for the parameter t in v ( t , x ), because these can be eliminated by considering systems of higher dimensions.

Depending on the properties of this vector field, the mechanical system is called

- autonomous , when v ( t , x ) = v ( x )

- homogeneous when v ( t , 0 ) = 0 for all t

The solution can be found using standard ODE techniques and is denoted as the evolution function already introduced above ${\boldsymbol {x}}(t)=\Phi (t,{\boldsymbol {x}}_{0})$

The dynamical system is then ( T , M , Φ).

Some formal manipulation of the system of differential equations shown above gives a more general form of equations a dynamical system must satisfy ${\dot {\boldsymbol {x}}}-{\boldsymbol {v}}(t,{\boldsymbol {x}})=0\qquad \Leftrightarrow \qquad {\mathfrak {G}}\left(t,\Phi (t,{\boldsymbol {x}}_{0})\right)=0$ where ${\mathfrak {G}}:{{(T\times M)}^{M}}\to \mathbf {C}$ is a functional from the set of evolution functions to the field of the complex numbers.

This equation is useful when modeling mechanical systems with complicated constraints.

Many of the concepts in dynamical systems can be extended to infinite-dimensional manifolds—those that are locally Banach spaces —in which case the differential equations are partial differential equations .

## Discrete dynamical systems

A discrete dynamical system is when either time or space or both are discrete. Typically for both space and time, there is a finite or countable sets of points and bounded maps and operators, that can be manipulated on a computer given some general assumptions on the boundaries .

### Mathematical definition

In the general context of mathematics , it is possible to define the dynamical system as a general discrete map as in the Formal definition .
A generic sequence is already per se a discrete dynamical system. Recursion and interation of maps is another such case. A prototype of this is the Logistic map .

### Empirical definition

From an empirical perspective, all dynamical systems derived from temporal data
are discrete, Gauss for example proved that with the measurement of 3 positions and times of Ceres in the sky is possible to fully determine the orbit, therefore be able to compute any possible position and velocity of the asteroid in the past or the future and therefore fully characterize the dynamical system. Typical tasks with experimental data are to derive a mathematical model.

### Examples

- Fibonacci Rabbits : Population model with infinite resources that generates the Fibonacci numbers .

- Logistic map A generic map applied to itself recursively makes a dynamical system

- Discrete example of predator prey model

- PageRank is an example of discrete dynamical system that predicts the future probability of a user o visit a page

### Applied mathematics and physics

In the context of applied mathematics such as physics , biology or engineering , the starting point is typically a finite difference equation such as the most simple possible one here: $y_{t+1}=ax_{t}+b$

More generally this can be generalized into a generic discrete map from a n-dimensional manifold to itself: $y_{t+1}^{i}=f_{t}^{i}(x_{1},..,x_{n}),i=1,...,n$

In the context of Hamiltonian flows , motion itself can be considered a canonical transformation (i.e. ultimately a map ) and therefore a discrete set of these in a discrete time interval $\Delta t$ is again a shape of characterization of the full discrete dynamical system.

There are also cases of dense orbits, where in essence the state phase space is not compact , and unbounded operators , like in quantum mechanics , where the evolution maps are not compact .

An example of this is a weather forecast of Earth where the data points are separated in space from each other.
The system can be put on a lattice , and formulas can be used to compute and predict certain variables, like in the case of the discretization of Navier–Stokes equations .

### Cascades

Discrete dynamical systems are often also called cascades, when the concept of passing over information from one step to the next is predominant. Typical examples are avalanches and also period doubling cascades. When T is taken to be the integers, it is a cascade or a map . If T is restricted to the non-negative integers the system is called a semi-cascade . [ clarification needed ]

### Cellular Automaton

A cellular automaton is a tuple ( T , M , Φ), with T a lattice such as the integers or a higher-dimensional integer grid , M is a set of functions from an integer lattice (again, with one or more dimensions) to a finite set, and Φ a (locally defined) evolution function. As such cellular automata are dynamical systems. The lattice in M represents the "space" lattice, while the one in T represents the "time" lattice. [ clarification needed ]

### Other notable examples

- Symbolic dynamics

- Finite state automata

- Turing machines

- Arithmetic dynamics

- Graph dynamical system

- By its discrete nature graph theory and in general any form of discrete mathematics can be seen in the lense of discrete dynamical systems

- Same apply to any form of finite mathematics , finite geometry , finite groups or countable mathematical structures such as coxeter groups

Some of these are separate subfields in their own right such as number theory or network theory .

## Linear dynamical systems

Linear dynamical systems are at the heart of any system engineering and system theory curriculum. Historically linear systems up to the 1970s reflected most of system theory as a whole (i.e. before the widespread availability of computers).
They include the basic features of any dynamical system, such as attenuation saturation and oscillation , and at least locally they can approximate also any non linear systems.

Linear dynamical systems can be solved in terms of simple functions such as exponentials and simple trigonometric functions (i.e. complex exponentials), and the behavior of all orbits can be classified.

In a linear system the phase space is the N -dimensional Euclidean space, so any point in phase space can be represented by a vector with N numbers. N dimensional Linear dynamical systems are also not chaotic

The analysis of linear systems is also simplified and possible because they satisfy a superposition principle : if u ( t ) and w ( t ) satisfy a linear differential equation that describe a system, then so will a linear combination $\alpha u(t)+\beta w(t)$ .
With superposition is possible to generate new solutions from known ones, therefore is just necessary to classify the fundamental solutions to know all of them.

### Flows

For a flow , the vector field v( x ) is an affine function of the position in the phase space, that is, ${\dot {x}}=v(x)=Ax+b,$ with A a matrix, b a vector of numbers and x the position vector. The solution to this system can be found by using the superposition principle (linearity).
The case b ≠ 0 with A = 0 is just a straight line in the direction of b : $\Phi ^{t}(x_{1})=x_{1}+bt.$

When b is zero and A ≠ 0 the origin is an equilibrium (or singular) point of the flow, that is, if x 0 = 0, then the orbit remains there.
For other initial conditions, the equation of motion is given by the exponential of a matrix : for an initial point x 0 , $\Phi ^{t}(x_{0})=e^{tA}x_{0}.$

When b = 0, the eigenvalues of A determine the structure of the phase space. From the eigenvalues and the eigenvectors of A it is possible to determine if an initial point will converge or diverge to the equilibrium point at the origin.

The distance between two different initial conditions in the case A ≠ 0 will change exponentially in most cases, either converging exponentially fast towards a point, or diverging exponentially fast. Linear systems display sensitive dependence on initial conditions in the case of divergence. For nonlinear systems this is one of the (necessary but not sufficient) conditions for chaotic behavior .

### Maps

A discrete-time , affine dynamical system has the form of a matrix difference equation : $x_{n+1}=Ax_{n}+b,$ with A a matrix and b a vector. As in the continuous case, the change of coordinates x → x + (1 − A ) –1 b removes the term b from the equation. In the new coordinate system , the origin is a fixed point of the map and the solutions are of the linear system A n x 0 .
The solutions for the map are no longer curves, but points that hop in the phase space. The orbits are organized in curves, or fibers, which are collections of points that map into themselves under the action of the map.

As in the continuous case, the eigenvalues and eigenvectors of A determine the structure of phase space. For example, if u 1 is an eigenvector of A , with a real eigenvalue smaller than one, then the straight lines given by the points along α u 1 , with α ∈ R , is an invariant curve of the map. Points in this straight line run into the fixed point.

There are also many other discrete dynamical systems such as Chaotic maps .

### Local dynamics

The qualitative properties of dynamical systems do not change under a smooth change of coordinates (this is sometimes taken as a definition of qualitative): a singular point of the vector field (a point where v ( x ) = 0) will remain a singular point under smooth transformations; a periodic orbit is a loop in phase space and smooth deformations of the phase space cannot alter it being a loop. It is in the neighborhood of singular points and periodic orbits that the structure of a phase space of a dynamical system can be well understood. In the qualitative study of dynamical systems, the approach is to show that there is a change of coordinates (usually unspecified, but computable) that makes the dynamical system as simple as possible.

### Rectification

A flow in most small patches of the phase space can be made very simple. If y is a point where the vector field v ( y ) ≠ 0, then there is a change of coordinates for a region around y where the vector field becomes a series of parallel vectors of the same magnitude. This is known as the rectification theorem.

The rectification theorem says that away from singular points the dynamics of a point in a small patch is a straight line. The patch can sometimes be enlarged by stitching several patches together, and when this works out in the whole phase space M the dynamical system is integrable . In most cases the patch cannot be extended to the entire phase space. There may be singular points in the vector field (where v ( x ) = 0); or the patches may become smaller and smaller as some point is approached. The more subtle reason is a global constraint, where the trajectory starts out in a patch, and after visiting a series of other patches comes back to the original one. If the next time the orbit loops around phase space in a different way, then it is impossible to rectify the vector field in the whole series of patches.

### Near periodic orbits

In general, in the neighborhood of a periodic orbit the rectification theorem cannot be used. Poincaré developed an approach that transforms the analysis near a periodic orbit to the analysis of a map. Pick a point x 0 in the orbit γ and consider the points in phase space in that neighborhood that are perpendicular to v ( x 0 ). These points are a Poincaré section S ( γ , x 0 ), of the orbit. The flow now defines a map, the Poincaré map F : S → S , for points starting in S and returning to S . Not all these points will take the same amount of time to come back, but the times will be close to the time it takes x 0 .

The intersection of the periodic orbit with the Poincaré section is a fixed point of the Poincaré map F . By a translation, the point can be assumed to be at x = 0. The Taylor series of the map is F ( x ) = J · x + O( x 2 ), so a change of coordinates h can only be expected to simplify F to its linear part $h^{-1}\circ F\circ h(x)=J\cdot x.$

This is known as the conjugation equation. Finding conditions for this equation to hold has been one of the major tasks of research in dynamical systems. Poincaré first approached it assuming all functions to be analytic and in the process discovered the non-resonant condition. If λ 1 , ..., λ ν are the eigenvalues of J they will be resonant if one eigenvalue is an integer linear combination of two or more of the others. As terms of the form λ i – Σ (multiples of other eigenvalues) occurs in the denominator of the terms for the function h , the non-resonant condition is also known as the small divisor problem.

### Conjugation results

The results on the existence of a solution to the conjugation equation depend on the eigenvalues of J and the degree of smoothness required from h . As J does not need to have any special symmetries, its eigenvalues will typically be complex numbers. When the eigenvalues of J are not in the unit circle, the dynamics near the fixed point x 0 of F is called hyperbolic and when the eigenvalues are on the unit circle and complex, the dynamics is called elliptic .

In the hyperbolic case, the Hartman–Grobman theorem gives the conditions for the existence of a continuous function that maps the neighborhood of the fixed point of the map to the linear map J · x . The hyperbolic case is also structurally stable . Small changes in the vector field will only produce small changes in the Poincaré map and these small changes will reflect in small changes in the position of the eigenvalues of J in the complex plane, implying that the map is still hyperbolic.

The Kolmogorov–Arnold–Moser (KAM) theorem gives the behavior near an elliptic point.

## Bifurcation theory

When the evolution map Φ t (or the vector field it is derived from) depends on a parameter μ, the structure of the phase space will also depend on this parameter. Small changes may produce no qualitative changes in the phase space until a special value μ 0 is reached. At this point the phase space changes qualitatively and the dynamical system is said to have gone through a bifurcation.

Bifurcation theory considers a structure in phase space (typically a fixed point , a periodic orbit, or an invariant torus ) and studies its behavior as a function of the parameter μ . At the bifurcation point the structure may change its stability, split into new structures, or merge with other structures. By using Taylor series approximations of the maps and an understanding of the differences that may be eliminated by a change of coordinates, it is possible to catalog the bifurcations of dynamical systems.

The bifurcations of a hyperbolic fixed point x 0 of a system family F μ can be characterized by the eigenvalues of the first derivative of the system DF μ ( x 0 ) computed at the bifurcation point. For a map, the bifurcation will occur when there are eigenvalues of DF μ on the unit circle. For a flow, it will occur when there are eigenvalues on the imaginary axis. For more information, see the main article on Bifurcation theory .

Some bifurcations can lead to very complicated structures in phase space. For example, the Ruelle–Takens scenario describes how a periodic orbit bifurcates into a torus and the torus into a strange attractor . In another example, Feigenbaum period-doubling describes how a stable periodic orbit goes through a series of period-doubling bifurcations .

## Ergodic systems

In many dynamical systems, it is possible to choose the coordinates of the system so that the volume (really a ν-dimensional volume) in phase space is invariant. This happens for mechanical systems derived from Newton's laws as long as the coordinates are the position and the momentum and the volume is measured in units of (position) × (momentum). The flow takes points of a subset A into the points Φ t ( A ) and invariance of the phase space means that $\mathrm {vol} (A)=\mathrm {vol} (\Phi ^{t}(A)).$ In the Hamiltonian formalism , given a coordinate it is possible to derive the appropriate (generalized) momentum such that the associated volume is preserved by the flow. The volume is said to be computed by the Liouville measure .

In a Hamiltonian system, not all possible configurations of position and momentum can be reached from an initial condition. Because of energy conservation, only the states with the same energy as the initial condition are accessible. The states with the same energy form an energy shell Ω, a sub-manifold of the phase space. The volume of the energy shell, computed using the Liouville measure, is preserved under evolution.

For systems where the volume is preserved by the flow, Poincaré discovered the recurrence theorem : Assume the phase space has a finite Liouville volume and let F be a phase space volume-preserving map and A a subset of the phase space. Then almost every point of A returns to A infinitely often. The Poincaré recurrence theorem was used by Zermelo to object to Boltzmann 's derivation of the increase in entropy in a dynamical system of colliding atoms.

One of the questions raised by Boltzmann's work was the possible equality between time averages and space averages, what he called the ergodic hypothesis . The hypothesis states that the length of time a typical trajectory spends in a region A is vol( A )/vol(Ω).

The ergodic hypothesis turned out not to be the essential property needed for the development of statistical mechanics and a series of other ergodic-like properties were introduced to capture the relevant aspects of physical systems. Koopman approached the study of ergodic systems by the use of functional analysis . An observable a is a function that to each point of the phase space associates a number (say instantaneous pressure, or average height). The value of an observable can be computed at another time by using the evolution function φ t . This introduces an operator U t , the transfer operator , $(U^{t}a)(x)=a(\Phi ^{-t}(x)).$

By studying the spectral properties of the linear operator U it becomes possible to classify the ergodic properties of Φ t . In using the Koopman approach of considering the action of the flow on an observable function, the finite-dimensional nonlinear problem involving Φ t gets mapped into an infinite-dimensional linear problem involving U .

The Liouville measure restricted to the energy surface Ω is the basis for the averages computed in equilibrium statistical mechanics . An average in time along a trajectory is equivalent to an average in space computed with the Boltzmann factor exp(−β H ) . This idea has been generalized by Sinai, Bowen, and Ruelle (SRB) to a larger class of dynamical systems that includes dissipative systems. SRB measures replace the Boltzmann factor and they are defined on attractors of chaotic systems.

## Nonlinear dynamical systems and chaos

### Chaotic systems

Simple nonlinear dynamical systems, including piecewise linear systems, can exhibit strongly unpredictable behavior, which might seem to be random, despite the fact that they are fundamentally deterministic. This unpredictable behavior has been called chaos . Hyperbolic systems are precisely defined dynamical systems that exhibit the properties ascribed to chaotic systems. In hyperbolic systems the tangent spaces perpendicular to an orbit can be decomposed into a combination of two parts: one with the points that converge towards the orbit (the stable manifold ) and another of the points that diverge from the orbit (the unstable manifold ).

This branch of mathematics deals with the long-term qualitative behavior of dynamical systems. Here, the focus is not on finding precise solutions to the equations defining the dynamical system (which is often hopeless), but rather to answer questions like "Will the system settle down to a steady state in the long term, and if so, what are the possible attractors ?" or "Does the long-term behavior of the system depend on its initial condition?"

The chaotic behavior of complex systems is not the issue. Meteorology has been known for years to involve complex—even chaotic—behavior. Chaos theory has been so surprising because chaos can be found within almost trivial systems. The Pomeau–Manneville scenario of the logistic map and the Fermi–Pasta–Ulam–Tsingou problem arose with just second-degree polynomials; the horseshoe map is piecewise linear.

### Solutions of finite duration

For non-linear autonomous ODEs it is possible under some conditions to develop solutions of finite duration, meaning here that in these solutions the system will reach the value zero at some time, called an ending time, and then stay there forever after. This can occur only when system trajectories are not uniquely determined forwards and backwards in time by the dynamics, thus solutions of finite duration imply a form of "backwards-in-time unpredictability" closely related to the forwards-in-time unpredictability of chaos. This behavior cannot happen for Lipschitz continuous differential equations according to the proof of the Picard-Lindelof theorem . These solutions are non-Lipschitz functions at their ending times and cannot be analytical functions on the whole real line.

As example, the equation: $y'=-{\text{sgn}}(y){\sqrt {|y|}},\,\,y(0)=1$ Admits the finite duration solution: $y(t)={\frac {1}{4}}\left(1-{\frac {t}{2}}+\left|1-{\frac {t}{2}}\right|\right)^{2}$ that is zero for $t\geq 2$ and is not Lipschitz continuous at its ending time $t=2.$

## Algebraic dynamical system

Algebraic dynamical systems can be considered as a special algebraic case of the classical geometric definition. This is based on an algebraic time evolution map as the group action or implicitly as a system of algebraic equations instead of ODEs . From a measure theoretic perspective , the manifold is a measure space , a variety , an algebraic group , and a topological group : the focus is then on symmetries, and ergodic theory behavior. These systems are often studied with methods from abstract algebra , algebraic geometry and Galois theory .

In the context of Algebraic quantum field theory the measure space can be a C*-algebra , namely observables are not just algebras of functions but an operator algebra , and this is treated together with a global gauge group (i.e. a group of constraints that leaves the observable invariant).

In the context of machine learning the neural network itself (e.g. Recursive neural network , diffusion models ) can be treated as a set of algebraic equations (often these are finite approximations such as gradient descent , there is a concept of time step , evolution dynamics across the network, and eventually there is a separate set of algebraic constraints such as enforcing unwanted behaviors.

In the context of geometry and number theory , typically one studies the iterations of a rational map over specific number fields , this area is called Algebraic Dynamics, it studies things such as the rational points of algebraic curves, and is deeply connected to Arithmetic dynamics

One such examples is the Poncelet map , where a point is moving in successive steps between two given conics , and the equations are algebraic (i.e. tangents and intersections). Another example can be a billiard with a border that is an algebraic curve , such as an elliptic billiard, in this case the dynamics is defined by reflections.

Note that algebraic curves are differentiable almost every where (a part from a finite number of points), therefore one can study them with analytic methods. In these two examples, the continuous dynamics is piecewise linear, the important events are typically discrete, albeit may be still an infinite or even measurable set (such as an ergodic trajectory in the billiard), the important events are when an algebraic equation applies (such as a reflection on a border). These systems can therefore be studied as discrete dynamical systems too.

## Effective Dynamics

Effective dynamics is the coarse-graining of equations of motion that describe a system at a certain scale, or a specific behaviour, typically getting rid of certain degrees of freedom . Instead of solving the microstate , i.e. the exact interactions for all atoms, molecules, or neural network nodes, effective dynamics models an "effective" force, energy or set of parameters and equations that describe the aggregate effect.

Typically effective dynamics arises from simplifying or specializing complex non linear phenomena, a major way to achieve this is with ensemble averages and this links it deeply with Ergodic theory and the Renormalization group . Key aspect of effective dynamics is the concept of emergence , such as: linear behaviour emergence from non linear equations as in solitons or linear emergence from ensemble averages , emergence of order and degrees of freedom in phase transitions such as in the Landau theory , emergence of prime number patterns in percolation dynamics.

Examples of these approaches are Effective Field Theories,Reynolds Averaged Navier-Stokes (RANS), disordered quantum systems, thermodynamics and Phase transitions.

## Category theory for dynamical systems

In the period between 2000 and 2020, category theory has been applied to system theory (e.g. to open systems and subsystems) and to dynamical systems. The motivation is to study common properties across dynamical systems, topological dynamical systems (i.e. with compact state space), and measure preserving dynamical systems (e.g. hamiltonian systems). It is also possible to draw an analogy between group representation theory (such as irreducible representations ) and ergodic decomposition i.e. that every invariant (i.e. conservative ) measure is a mixture of ergodic ones, in an analogous fashion to the central limit theorem . Ultimately this can be compared to the fundamental theorem of arithmetic and to prime number decomposition.
