# Gauss's law for gravity

> **Query Topic**: Gauss's law (Rank #2 Search Result)
> **Source Queue**: train (Row ID: 59, Frequency: 11)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Gauss's_law_for_gravity

---

In physics, Gauss's law for gravity, also known as Gauss's flux theorem for gravity, is a law of physics that is equivalent to Newton's law of universal gravitation. It is named after Carl Friedrich Gauss. It states that the flux (surface integral) of the gravitational field over any closed surface is proportional to the mass enclosed.  Gauss's law for gravity is often more convenient to work from than Newton's law.
The form of Gauss's law for gravity is mathematically similar to Gauss's law for electrostatics, one of Maxwell's equations. Gauss's law for gravity has the same mathematical relation to Newton's law that Gauss's law for electrostatics bears to Coulomb's law.  This is because both Newton's law and Coulomb's law describe inverse-square interaction in a 3-dimensional space.


== Qualitative statement of the law ==

The gravitational field g (also called gravitational acceleration) is a vector field – a vector at each point of space (and time). It is defined so that the gravitational force experienced by a particle is equal to the mass of the particle multiplied by the gravitational field at that point.
Gravitational flux is a surface integral of the gravitational field over a closed surface, analogous to how magnetic flux is a surface integral of the magnetic field.
Gauss's law for gravity states:

The gravitational flux through any closed surface is proportional to the enclosed mass.


== Integral form ==
The integral form of Gauss's law for gravity states:

where

 
  
    
      
        
          ∂
          V
        
      
    
    {\displaystyle \scriptstyle \partial V}
  
  (also written 
  
    
      
        
          ∮
          
            ∂
            V
          
        
      
    
    {\displaystyle \oint _{\partial V}}
  
) denotes a surface integral over a closed surface,
∂V is any closed surface (the boundary of an arbitrary volume V),
dA is a vector, whose magnitude is the area of an infinitesimal piece of the surface ∂V, and whose direction is the outward-pointing surface normal (see surface integral for more details),
g is the gravitational field,
G is the universal gravitational constant, and
M is the total mass enclosed within the surface ∂V.
The left-hand side of this equation is called the flux of the gravitational field. Note that according to the law it is always negative (or zero), and never positive. This can be contrasted with Gauss's law for electricity, where the flux can be either positive or negative. The difference is because charge can be either positive or negative, while mass can only be positive.


== Differential form ==
The differential form of Gauss's law for gravity states

where 
  
    
      
        ∇
        ⋅
      
    
    {\displaystyle \nabla \cdot }
  
 denotes the divergence, g is the gravitational field, G is the universal gravitational constant, and ρ is the mass density at each point.


=== Relation to the integral form ===
The two forms of Gauss's law for gravity are mathematically equivalent. The divergence theorem states:

  
    
      
        
          ∮
          
            ∂
            V
          
        
        
          g
        
        ⋅
        d
        
          A
        
        =
        
          ∫
          
            V
          
        
        ∇
        ⋅
        
          g
        
        
        d
        V
      
    
    {\displaystyle \oint _{\partial V}\mathbf {g} \cdot d\mathbf {A} =\int _{V}\nabla \cdot \mathbf {g} \,dV}
  

where V is a closed region bounded by a simple closed oriented surface ∂V and dV is an infinitesimal piece of the volume V (see volume integral for more details). The gravitational field g must be a continuously differentiable vector field defined on a neighborhood of V.
Given also that

  
    
      
        M
        =
        
          ∫
          
            V
          
        
        ρ
         
        d
        V
      
    
    {\displaystyle M=\int _{V}\rho \ dV}
  

we can apply the divergence theorem to the integral form of Gauss's law for gravity, which becomes:

  
    
      
        
          ∫
          
            V
          
        
        ∇
        ⋅
        
          g
        
         
        d
        V
        =
        −
        4
        π
        G
        
          ∫
          
            V
          
        
        ρ
         
        d
        V
      
    
    {\displaystyle \int _{V}\nabla \cdot \mathbf {g} \ dV=-4\pi G\int _{V}\rho \ dV}
  

which can be rewritten:

  
    
      
        
          ∫
          
            V
          
        
        (
        ∇
        ⋅
        
          g
        
        )
         
        d
        V
        =
        
          ∫
          
            V
          
        
        (
        −
        4
        π
        G
        ρ
        )
         
        d
        V
        .
      
    
    {\displaystyle \int _{V}(\nabla \cdot \mathbf {g} )\ dV=\int _{V}(-4\pi G\rho )\ dV.}
  

This has to hold simultaneously for every possible volume V; the only way this can happen is if the integrands are equal. Hence we arrive at

  
    
      
        ∇
        ⋅
        
          g
        
        =
        −
        4
        π
        G
        ρ
        ,
      
    
    {\displaystyle \nabla \cdot \mathbf {g} =-4\pi G\rho ,}
  

which is the differential form of Gauss's law for gravity.
It is possible to derive the integral form from the differential form using the reverse of this method.
Although the two forms are equivalent, one or the other might be more convenient to use in a particular computation.


== Relation to Newton's law ==


=== Deriving Gauss's law from Newton's law ===
Gauss's law for gravity can be derived from Newton's law of universal gravitation, which states that the gravitational field due to a point mass is:

  
    
      
        
          g
        
        (
        
          r
        
        )
        =
        −
        
          
            
              G
              M
            
            
              r
              
                2
              
            
          
        
        
          
            e
            
              r
            
          
        
      
    
    {\displaystyle \mathbf {g} (\mathbf {r} )=-{\frac {GM}{r^{2}}}\mathbf {e_{r}} }
  

where

er is the radial unit vector,
r is the radius, |r|.
M is the mass of the particle, which is assumed to be a point mass located at the origin.
A proof using vector calculus is shown in the box below. It is mathematically identical to the proof of Gauss's law (in electrostatics) starting from Coulomb's law.


=== Deriving Newton's law from Gauss's law and irrotationality ===
It is impossible to mathematically prove Newton's law from Gauss's law alone, because Gauss's law specifies the divergence of g but does not contain any information regarding the curl of g (see Helmholtz decomposition). In addition to Gauss's law, the assumption is used that g is irrotational (has zero curl), as gravity is a conservative force:

  
    
      
        ∇
        ×
        
          g
        
        =
        0
      
    
    {\displaystyle \nabla \times \mathbf {g} =0}
  

Even these are not enough: Boundary conditions on g are also necessary to prove Newton's law, such as the assumption that the field is zero infinitely far from a mass.
The proof of Newton's law from these assumptions is as follows:


== Poisson's equation and gravitational potential ==
Since the gravitational field has zero curl (equivalently, gravity is a conservative force) as mentioned above, it can be written as the gradient of a scalar potential, called the gravitational potential:

  
    
      
        
          g
        
        =
        −
        ∇
        ϕ
        .
      
    
    {\displaystyle \mathbf {g} =-\nabla \phi .}
  

Then the differential form of Gauss's law for gravity becomes Poisson's equation:

  
    
      
        
          ∇
          
            2
          
        
        ϕ
        =
        4
        π
        G
        ρ
        .
      
    
    {\displaystyle \nabla ^{2}\phi =4\pi G\rho .}
  

This provides an alternate means of calculating the gravitational potential and gravitational field. Although computing g via Poisson's equation is mathematically equivalent to computing g directly from Gauss's law, one or the other approach may be an easier computation in a given situation.
In radially symmetric systems, the gravitational potential is a function of only one variable (namely, 
  
    
      
        r
        =
        
          |
        
        
          r
        
        
          |
        
      
    
    {\displaystyle r=|\mathbf {r} |}
  
), and Poisson's equation becomes (see Del in cylindrical and spherical coordinates):

  
    
      
        
          
            1
            
              r
              
                2
              
            
          
        
        
          
            ∂
            
              ∂
              r
            
          
        
        
          (
          
            
              r
              
                2
              
            
            
            
              
                
                  ∂
                  ϕ
                
                
                  ∂
                  r
                
              
            
          
          )
        
        =
        4
        π
        G
        ρ
        (
        r
        )
      
    
    {\displaystyle {\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}\,{\frac {\partial \phi }{\partial r}}\right)=4\pi G\rho (r)}
  

while the gravitational field is:

  
    
      
        
          g
        
        (
        
          r
        
        )
        =
        −
        
          
            e
            
              r
            
          
        
        
          
            
              ∂
              ϕ
            
            
              ∂
              r
            
          
        
        .
      
    
    {\displaystyle \mathbf {g} (\mathbf {r} )=-\mathbf {e_{r}} {\frac {\partial \phi }{\partial r}}.}
  

When solving the equation it should be taken into account that in the case of finite densities ∂ϕ/∂r has to be continuous at boundaries (discontinuities of the density), and zero for r = 0.


== Applications ==
Gauss's law can be used to easily derive the gravitational field in certain cases where a direct application of Newton's law would be more difficult (but not impossible). See the article Gaussian surface for more details on how these derivations are done. Three such applications are as follows:


=== Bouguer plate ===

We can conclude (by using a "Gaussian pillbox") that for an infinite, flat plate (Bouguer plate) of any finite thickness, the gravitational field outside the plate is perpendicular to the plate, towards it, with magnitude 2πG times the mass per unit area, independent of the distance to the plate (see also gravity anomalies).
More generally, for a mass distribution with the density depending on one Cartesian coordinate z only, gravity for any z is 2πG times the difference in mass per unit area on either side of this z value.
In particular, a parallel combination of two parallel infinite plates of equal mass per unit area produces no gravitational field between them.


=== Cylindrically symmetric mass distribution ===
In the case of an infinite uniform (in z) cylindrically symmetric mass distribution we can conclude (by using a cylindrical Gaussian surface) that the field strength at a distance r from the center is inward with a magnitude of 2G/r times the total mass per unit length at a smaller distance (from the axis), regardless of any masses at a larger distance.
For example, inside an infinite uniform hollow cylinder, the field is zero.


=== Spherically symmetric mass distribution ===

In the case of a spherically symmetric mass distribution we can conclude (by using a spherical Gaussian surface) that the field strength at a distance r from the center is inward with a magnitude of G/r2 times only the total mass within a smaller distance than r. All the mass at a greater distance than r from the center has no resultant effect.
For example, a hollow sphere does not produce any net gravity inside. The gravitational field inside is the same as if the hollow sphere were not there (i.e. the resultant field is that of all masses not including the sphere, which can be inside and outside the sphere).
Although this follows in one or two lines of algebra from Gauss's law for gravity, it took Isaac Newton several pages of cumbersome calculus to derive it directly using his law of gravity; see the article shell theorem for this direct derivation.


== Derivation from Lagrangian ==

The Lagrangian density for Newtonian gravity is

  
    
      
        
          
            L
          
        
        (
        
          x
        
        ,
        t
        )
        =
        −
        ρ
        (
        
          x
        
        ,
        t
        )
        ϕ
        (
        
          x
        
        ,
        t
        )
        −
        
          
            1
            
              8
              π
              G
            
          
        
        (
        ∇
        ϕ
        (
        
          x
        
        ,
        t
        )
        
          )
          
            2
          
        
      
    
    {\displaystyle {\mathcal {L}}(\mathbf {x} ,t)=-\rho (\mathbf {x} ,t)\phi (\mathbf {x} ,t)-{1 \over 8\pi G}(\nabla \phi (\mathbf {x} ,t))^{2}}
  

Applying Hamilton's principle to this Lagrangian, the result is Gauss's law for gravity:

  
    
      
        4
        π
        G
        ρ
        (
        
          x
        
        ,
        t
        )
        =
        
          ∇
          
            2
          
        
        ϕ
        (
        
          x
        
        ,
        t
        )
        .
      
    
    {\displaystyle 4\pi G\rho (\mathbf {x} ,t)=\nabla ^{2}\phi (\mathbf {x} ,t).}
  

See Lagrangian (field theory) for details.


== See also ==


== References ==


== Further reading ==
For usage of the term "Gauss's law for gravity" see, for example, Moody, M. V.; Paik, H. J. (1 March 1993). "Gauss's law test of gravity at short range". Physical Review Letters. 70 (9): 1195–1198. Bibcode:1993PhRvL..70.1195M. doi:10.1103/PhysRevLett.70.1195. PMID 10054315.
