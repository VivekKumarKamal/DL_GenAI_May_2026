# Gauss's law for magnetism

> **Query Topic**: Gauss's law (Rank #2 Search Result)  
> **Source Queue**: train (Row ID: 59, Frequency: 11)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Gauss's_law_for_magnetism

---

In physics, Gauss's law for magnetism is one of the four Maxwell's equations that underlie classical electrodynamics. It states that the magnetic field B has divergence equal to zero, in other words, that it is a solenoidal vector field. It is equivalent to the statement that magnetic monopoles do not exist. Rather than "magnetic charges", the basic entity for magnetism is the magnetic dipole. (If monopoles were ever found, the law would have to be modified, as elaborated below.)
Gauss's law for magnetism can be written in two forms, a differential form and an integral form. These forms are equivalent due to the divergence theorem.
The name "Gauss's law for magnetism" is not universally used. The law is also called "Absence of free magnetic poles".  It is also referred to as the "transversality requirement" because for plane waves it requires that the polarization be transverse to the direction of propagation. 


== Differential form ==
The differential form for Gauss's law for magnetism is:

where ∇ · denotes divergence, and B is the magnetic field.


== Integral form ==

The integral form of Gauss's law for magnetism states:

where S is any closed surface (see image right), 
  
    
      
        
          Φ
          
            B
          
        
      
    
    {\displaystyle \Phi _{B}}
  
 is the magnetic flux through S, and dS is a vector, whose magnitude is the area of an infinitesimal piece of the surface S, and whose direction is the outward-pointing surface normal (see surface integral for more details).
Gauss's law for magnetism thus states that the net magnetic flux through a closed surface equals zero.
The integral and differential forms of Gauss's law for magnetism are mathematically equivalent, due to the divergence theorem. That said, one or the other might be more convenient to use in a particular computation.
The law in this form states that for each volume element in space, there are exactly the same number of "magnetic field lines" entering and exiting the volume. No total "magnetic charge" can build up in any point in space. For example, the south pole of the magnet is exactly as strong as the north pole, and free-floating south poles without accompanying north poles (magnetic monopoles) are not allowed. In contrast, this is not true for other fields such as electric fields or gravitational fields, where total electric charge or mass can build up in a volume of space.


== Vector potential ==

Due to the Helmholtz decomposition theorem, Gauss's law for magnetism is equivalent to the following statement:

The vector field A is called the magnetic vector potential.
Note that there is more than one possible A which satisfies this equation for a given B field. In fact, there are infinitely many: any field of the form ∇ϕ can be added onto A to get an alternative choice for A, by the identity (see Vector calculus identities):

  
    
      
        ∇
        ×
        
          A
        
        =
        ∇
        ×
        (
        
          A
        
        +
        ∇
        ϕ
        )
      
    
    {\displaystyle \nabla \times \mathbf {A} =\nabla \times (\mathbf {A} +\nabla \phi )}
  

since the curl of a gradient is the zero vector field:

  
    
      
        ∇
        ×
        ∇
        ϕ
        =
        
          0
        
      
    
    {\displaystyle \nabla \times \nabla \phi ={\boldsymbol {0}}}
  

This arbitrariness in A is called gauge freedom.


== Field lines ==

The magnetic field B can be depicted via field lines (also called flux lines) – that is, a set of curves whose direction corresponds to the direction of B, and whose areal density is proportional to the magnitude of B. Gauss's law for magnetism is equivalent to the statement that the field lines have neither a beginning nor an end: Each one either forms a closed loop, winds around forever without ever quite joining back up to itself exactly, or extends to infinity.


== Incorporating magnetic monopoles ==

If magnetic monopoles were to be discovered, then Gauss's law for magnetism would state the divergence of B would be proportional to the magnetic charge density ρm, analogous to Gauss's law for electric field. For zero net magnetic charge density (ρm = 0), the original form of Gauss's magnetism law is the result.
The modified formula for use with the SI is not standard and depends on the choice of defining equation for the magnetic charge and current; in one variation, magnetic charge has units of webers, in another it has units of ampere-meters.

where μ0 is the vacuum permeability.
So far, examples of magnetic monopoles are disputed in extensive search, although certain papers report examples matching that behavior.


== History ==
This idea of the nonexistence of the  magnetic monopoles originated in 1269 by Petrus Peregrinus de Maricourt. His work heavily influenced William Gilbert, whose 1600 work De Magnete spread the idea further. In the early 1800s Michael Faraday reintroduced this law, and it subsequently made its way into James Clerk Maxwell's electromagnetic field equations.


== Numerical computation ==
In numerical computation, the numerical solution may not satisfy Gauss's law for magnetism due to the discretization errors of the numerical methods. However, in many cases, e.g., for magnetohydrodynamics, it is important to preserve Gauss's law for magnetism precisely (up to the machine precision). Violation of Gauss's law for magnetism on the discrete level will introduce a strong non-physical force. In view of energy conservation, violation of this condition leads to a non-conservative energy integral, and the error is proportional to the divergence of the magnetic field.
There are various ways to preserve Gauss's law for magnetism in numerical methods, including the divergence-cleaning techniques, the constrained transport method, potential-based formulations and de Rham complex based finite element methods where stable and structure-preserving algorithms are constructed on unstructured meshes with finite element differential forms.


== See also ==
Magnetic moment
Vector calculus
Integral
Flux
Gaussian surface
Faraday's law of induction
Ampère's circuital law
Lorenz gauge condition


== References ==


== External links ==
 Media related to Gauss's law for magnetism at Wikimedia Commons
