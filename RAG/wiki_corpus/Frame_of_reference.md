# Frame of reference

> **Query Topic**: linear frame dragging (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 204, Frequency: 11)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Frame_of_reference

---

In physics and astronomy , a frame of reference (or reference frame ) is an abstract coordinate system , whose origin , orientation , and scale have been specified in physical space . It is based on a set of reference points , defined as geometric points whose position is identified both mathematically (with numerical coordinate values) and physically (signaled by conventional markers). An important special case is that of an inertial reference frame , a stationary or uniformly moving frame.

For n dimensions, n + 1 reference points are sufficient to fully define a reference frame. Using rectangular Cartesian coordinates , a reference frame may be defined with a reference point at the origin and a reference point at one unit distance from the origin along each of the n coordinate axes . [ citation needed ]

In Einsteinian relativity , reference frames are used to specify the relationship between a moving observer and the phenomenon under observation. In this context, the term often becomes observational frame of reference (or observational reference frame ), which implies that the observer is at rest in the frame, although not necessarily located at its origin . A relativistic reference frame includes (or implies) the coordinate time , which does not equate across different reference frames moving relatively to each other. The situation thus differs from Galilean relativity , in which all possible coordinate times are essentially equivalent. [ citation needed ]

## Definition

The need to distinguish between the various meanings of "frame of reference" has led to a variety of terms. For example, sometimes the type of coordinate system is attached as a modifier, as in Cartesian frame of reference . Sometimes the state of motion is emphasized, as in rotating frame of reference . Sometimes the way it transforms to frames considered as related is emphasized as in Galilean frame of reference . Sometimes frames are distinguished by the scale of their observations, as in macroscopic and microscopic frames of reference .

In this article, the term observational frame of reference is used when emphasis is upon the state of motion rather than upon the coordinate choice or the character of the observations or observational apparatus. In this sense, an observational frame of reference allows study of the effect of motion upon an entire family of coordinate systems that could be attached to this frame. On the other hand, a coordinate system may be employed for many purposes where the state of motion is not the primary concern. For example, a coordinate system may be adopted to take advantage of the symmetry of a system. In a still broader perspective, the formulation of many problems in physics employs generalized coordinates , normal modes or eigenvectors , which are only indirectly related to space and time. It seems useful to divorce the various aspects of a reference frame for the discussion below. We therefore take observational frames of reference, coordinate systems, and observational equipment as independent concepts, separated as below:

- An observational frame (such as an inertial frame or non-inertial frame of reference ) is a physical concept related to state of motion.

- A coordinate system is a mathematical concept, amounting to a choice of language used to describe observations. Consequently, an observer in an observational frame of reference can choose to employ any coordinate system (Cartesian, polar, curvilinear, generalized, ...) to describe observations made from that frame of reference. A change in the choice of this coordinate system does not change an observer's state of motion, and so does not entail a change in the observer's observational frame of reference. This viewpoint can be found elsewhere as well. Which is not to dispute that some coordinate systems may be a better choice for some observations than are others.

- Choice of what to measure and with what observational apparatus is a matter separate from the observer's state of motion and choice of coordinate system.

## Coordinate systems

Although the term "coordinate system" is often used (particularly by physicists) in a nontechnical sense, the term "coordinate system" does have a precise meaning in mathematics, and sometimes that is what the physicist means as well.

A coordinate system in mathematics is a facet of geometry or of algebra , in particular, a property of manifolds (for example, in physics, configuration spaces or phase spaces ). The coordinates of a point r in an n -dimensional space are simply an ordered set of n numbers:

$\mathbf {r} =[x^{1},\ x^{2},\ \dots ,\ x^{n}].$

In a general Banach space , these numbers could be (for example) coefficients in a functional expansion like a Fourier series . In a physical problem, they could be spacetime coordinates or normal mode amplitudes. In a robot design , they could be angles of relative rotations, linear displacements, or deformations of joints . Here we will suppose these coordinates can be related to a Cartesian coordinate system by a set of functions:

$x^{j}=x^{j}(x,\ y,\ z,\ \dots ),\quad j=1,\ \dots ,\ n,$

where x , y , z , etc. are the n Cartesian coordinates of the point. Given these functions, coordinate surfaces are defined by the relations:

$x^{j}(x,y,z,\dots )=\mathrm {constant} ,\quad j=1,\ \dots ,\ n.$

The intersection of these surfaces define coordinate lines . At any selected point, tangents to the intersecting coordinate lines at that point define a set of basis vectors { e 1 , e 2 , ..., e n } at that point. That is:

$\mathbf {e} _{i}(\mathbf {r} )=\lim _{\epsilon \rightarrow 0}{\frac {\mathbf {r} \left(x^{1},\ \dots ,\ x^{i}+\epsilon ,\ \dots ,\ x^{n}\right)-\mathbf {r} \left(x^{1},\ \dots ,\ x^{i},\ \dots ,\ x^{n}\right)}{\epsilon }},\quad i=1,\ \dots ,\ n,$

which can be normalized to be of unit length. For more detail see curvilinear coordinates .

Coordinate surfaces, coordinate lines, and basis vectors are components of a coordinate system . If the basis vectors are orthogonal at every point, the coordinate system is an orthogonal coordinate system .

An important aspect of a coordinate system is its metric tensor g ik , which determines the arc length ds in the coordinate system in terms of its coordinates:

$(ds)^{2}=g_{ik}\ dx^{i}\ dx^{k},$

where repeated indices are summed over.

As is apparent from these remarks, a coordinate system is a mathematical construct , part of an axiomatic system . There is no necessary connection between coordinate systems and physical motion (or any other aspect of reality). However, coordinate systems can include time as a coordinate, and can be used to describe motion. Thus, Lorentz transformations and Galilean transformations may be viewed as coordinate transformations .

## Observational frame of reference

An observational frame of reference , often referred to as a physical frame of reference , a frame of reference , or simply a frame , is a physical concept related to an observer and the observer's state of motion. Here we adopt the view expressed by Kumar and Barve: an observational frame of reference is characterized only by its state of motion . However, there is lack of unanimity on this point. In special relativity , the distinction is sometimes made between an observer and a frame . According to this view, a frame is an observer plus a coordinate lattice constructed to be an orthonormal right-handed set of spacelike vectors perpendicular to a timelike vector. See Doran. This restricted view is not used here, and is not universally adopted even in discussions of relativity. In general relativity the use of general coordinate systems is common (see, for example, the Schwarzschild solution for the gravitational field outside an isolated sphere ).

There are two types of observational reference frame: inertial and non-inertial . An inertial frame of reference is defined as one in which all laws of physics take on their simplest form. In special relativity these frames are related by Lorentz transformations , which are parametrized by rapidity . In Newtonian mechanics, a more restricted definition requires only that Newton's first law holds true; that is, a Newtonian inertial frame is one in which a free particle travels in a straight line at constant speed , or is at rest. These frames are related by Galilean transformations . These relativistic and Newtonian transformations are expressed in spaces of general dimension in terms of representations of the Poincaré group and of the Galilean group .

In contrast to the inertial frame, a non-inertial frame of reference is one in which fictitious forces must be invoked to explain observations. An example is an observational frame of reference centered at a point on the Earth's surface. This frame of reference orbits around the center of the Earth, which introduces the fictitious forces known as the Coriolis force , centrifugal force , and gravitational force . (All of these forces including gravity disappear in a truly inertial reference frame, which is one of free-fall.)

## Measurement apparatus

A further aspect of a frame of reference is the role of the measurement apparatus (for example, clocks and rods) attached to the frame (see Norton quote above). This question is not addressed in this article, and is of particular interest in quantum mechanics , where the relation between observer and measurement is still under discussion (see measurement problem ).

In physics experiments, the frame of reference in which the laboratory measurement devices are at rest is usually referred to as the laboratory frame or simply "lab frame." An example would be the frame in which the detectors for a particle accelerator are at rest. The lab frame in some experiments is an inertial frame, but it is not required to be (for example the laboratory on the surface of the Earth in many physics experiments is not inertial). In particle physics experiments, it is often useful to transform energies and momenta of particles from the lab frame where they are measured, to the center of momentum frame "COM frame" in which calculations are sometimes simplified, since potentially all kinetic energy still present in the COM frame may be used for making new particles.

In this connection it may be noted that the clocks and rods often used to describe observers' measurement equipment in thought, in practice are replaced by a much more complicated and indirect metrology that is connected to the nature of the vacuum , and uses atomic clocks that operate according to the Standard Model and that must be corrected for gravitational time dilation . (See second , meter and kilogram ).

In fact, Einstein felt that clocks and rods were merely expedient measuring devices and they should be replaced by more fundamental entities based upon, for example, atoms and molecules.

## Generalization

The discussion is taken beyond simple space-time coordinate systems by Brading and Castellani. Extension to coordinate systems using generalized coordinates underlies the Hamiltonian and Lagrangian formulations of quantum field theory , classical relativistic mechanics , and quantum gravity .

## Instances

- International Terrestrial Reference Frame

- International Celestial Reference Frame

- In fluid mechanics, Lagrangian and Eulerian specification of the flow field

- Frame fields in general relativity

- Moving frame in mathematics
