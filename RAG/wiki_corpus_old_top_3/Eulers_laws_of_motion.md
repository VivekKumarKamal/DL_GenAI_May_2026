# Euler's laws of motion

> **Query Topic**: Newton's laws of motion (Rank #2 Search Result)
> **Source Queue**: train (Row ID: 25, Frequency: 16)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Euler's_laws_of_motion

---

In classical mechanics, Euler's laws of motion are equations of motion which extend Newton's laws of motion for point particle to rigid body motion. They were formulated by Leonhard Euler about 50 years after Isaac Newton formulated his laws.


== Overview ==


=== Euler's first law ===
Euler's first law states that the rate of change of linear momentum p of a rigid body is equal to the resultant of all the external forces Fext acting on the body:

  
    
      
        
          
            F
          
          
            ext
          
        
        =
        
          
            
              d
              
                p
              
            
            
              d
              t
            
          
        
        .
      
    
    {\displaystyle \mathbf {F} _{\text{ext}}={\frac {d\mathbf {p} }{dt}}.}
  

Internal forces between the particles that make up a body do not contribute to changing the momentum of the body as there is an equal and opposite force resulting in no net effect.
The linear momentum of a rigid body is the product of the mass of the body and the velocity of its center of mass vcm.


=== Euler's second law ===

Euler's second law states that the rate of change of angular momentum L about a point that is fixed in an inertial reference frame (often the center of mass of the body), is equal to the sum of the external moments of force (torques) acting on that body M about that point: 

  
    
      
        
          M
        
        =
        
          
            
              d
              
                L
              
            
            
              d
              t
            
          
        
        .
      
    
    {\displaystyle \mathbf {M} ={d\mathbf {L}  \over dt}.}
  

Note that the above formula holds only if both M and L are computed with respect to a fixed inertial frame or a frame parallel to the inertial frame but fixed on the center of mass.
For rigid bodies translating and rotating in only two dimensions, this can be expressed as:

  
    
      
        
          M
        
        =
        
          
            r
          
          
            
              c
              m
            
          
        
        ×
        
          
            a
          
          
            
              c
              m
            
          
        
        m
        +
        I
        
          α
        
        ,
      
    
    {\displaystyle \mathbf {M} =\mathbf {r} _{\rm {cm}}\times \mathbf {a} _{\rm {cm}}m+I{\boldsymbol {\alpha }},}
  

where:

rcm is the position vector of the center of mass of the body with respect to the point about which moments are summed,
acm is the linear acceleration of the center of mass of the body,
m is the mass of the body,
α is the angular acceleration of the body, and
I is the moment of inertia of the body about its center of mass.
See also Euler's equations (rigid body dynamics).


== Explanation and derivation ==
The distribution of internal forces in a deformable body are not necessarily equal throughout, i.e. the stresses vary from one point to the next. This variation of internal forces throughout the body is governed by Newton's second law of motion of conservation of linear momentum and angular momentum, which for their simplest use are applied to a mass particle but are extended in continuum mechanics to a body of continuously distributed mass. For continuous bodies these laws are called Euler's laws of motion.
The total body force applied to a continuous body with mass m, mass density ρ, and volume V, is the volume integral integrated over the volume of the body:

  
    
      
        
          
            F
          
          
            B
          
        
        =
        
          ∫
          
            V
          
        
        
          b
        
        
        d
        m
        =
        
          ∫
          
            V
          
        
        
          b
        
        ρ
        
        d
        V
      
    
    {\displaystyle \mathbf {F} _{B}=\int _{V}\mathbf {b} \,dm=\int _{V}\mathbf {b} \rho \,dV}
  

where b is the force acting on the body per unit mass (dimensions of acceleration, misleadingly called the "body force"), and dm = ρ dV is an infinitesimal mass element of the body.
Body forces and contact forces acting on the body lead to corresponding moments (torques) of those forces relative to a given point. Thus, the total applied torque M about the origin is given by

  
    
      
        
          M
        
        =
        
          
            M
          
          
            B
          
        
        +
        
          
            M
          
          
            C
          
        
      
    
    {\displaystyle \mathbf {M} =\mathbf {M} _{B}+\mathbf {M} _{C}}
  

where MB and MC respectively indicate the moments caused by the body and contact forces.
Thus, the sum of all applied forces and torques (with respect to the origin of the coordinate system) acting on the body can be given as the sum of a volume and surface integral:

  
    
      
        
          F
        
        =
        
          ∫
          
            V
          
        
        
          a
        
        
        d
        m
        =
        
          ∫
          
            V
          
        
        
          a
        
        ρ
        
        d
        V
        =
        
          ∫
          
            S
          
        
        
          t
        
        
        d
        S
        +
        
          ∫
          
            V
          
        
        
          b
        
        ρ
        
        d
        V
      
    
    {\displaystyle \mathbf {F} =\int _{V}\mathbf {a} \,dm=\int _{V}\mathbf {a} \rho \,dV=\int _{S}\mathbf {t} \,dS+\int _{V}\mathbf {b} \rho \,dV}
  

  
    
      
        
          M
        
        =
        
          
            M
          
          
            B
          
        
        +
        
          
            M
          
          
            C
          
        
        =
        
          ∫
          
            S
          
        
        
          r
        
        ×
        
          t
        
        
        d
        S
        +
        
          ∫
          
            V
          
        
        
          r
        
        ×
        
          b
        
        ρ
        
        d
        V
        .
      
    
    {\displaystyle \mathbf {M} =\mathbf {M} _{B}+\mathbf {M} _{C}=\int _{S}\mathbf {r} \times \mathbf {t} \,dS+\int _{V}\mathbf {r} \times \mathbf {b} \rho \,dV.}
  

where t = t(n) is called the surface traction, integrated over the surface of the body, in turn n denotes a unit vector normal and directed outwards to the surface S.
Let the coordinate system (x1, x2, x3) be an inertial frame of reference, r be the position vector of a point particle in the continuous body with respect to the origin of the coordinate system, and v = ⁠dr/dt⁠ be the velocity vector of that point.
Euler's first axiom or law (law of balance of linear momentum or balance of forces) states that in an inertial frame the time rate of change of linear momentum p of an arbitrary portion of a continuous body is equal to the total applied force F acting on that portion, and it is expressed as

  
    
      
        
          
            
              
                
                  
                    
                      d
                      
                        p
                      
                    
                    
                      d
                      t
                    
                  
                
              
              
                
                =
                
                  F
                
              
            
            
              
                
                  
                    d
                    
                      d
                      t
                    
                  
                
                
                  ∫
                  
                    V
                  
                
                ρ
                
                  v
                
                
                d
                V
              
              
                
                =
                
                  ∫
                  
                    S
                  
                
                
                  t
                
                
                d
                S
                +
                
                  ∫
                  
                    V
                  
                
                
                  b
                
                ρ
                
                d
                V
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\frac {d\mathbf {p} }{dt}}&=\mathbf {F} \\{\frac {d}{dt}}\int _{V}\rho \mathbf {v} \,dV&=\int _{S}\mathbf {t} \,dS+\int _{V}\mathbf {b} \rho \,dV.\end{aligned}}}
  

Euler's second axiom or law (law of balance of angular momentum or balance of torques) states that in an inertial frame the time rate of change of angular momentum L of an arbitrary portion of a continuous body is equal to the total applied torque M acting on that portion, and it is expressed as

  
    
      
        
          
            
              
                
                  
                    
                      d
                      
                        L
                      
                    
                    
                      d
                      t
                    
                  
                
              
              
                
                =
                
                  M
                
              
            
            
              
                
                  
                    d
                    
                      d
                      t
                    
                  
                
                
                  ∫
                  
                    V
                  
                
                
                  r
                
                ×
                ρ
                
                  v
                
                
                d
                V
              
              
                
                =
                
                  ∫
                  
                    S
                  
                
                
                  r
                
                ×
                
                  t
                
                
                d
                S
                +
                
                  ∫
                  
                    V
                  
                
                
                  r
                
                ×
                
                  b
                
                ρ
                
                d
                V
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\frac {d\mathbf {L} }{dt}}&=\mathbf {M} \\{\frac {d}{dt}}\int _{V}\mathbf {r} \times \rho \mathbf {v} \,dV&=\int _{S}\mathbf {r} \times \mathbf {t} \,dS+\int _{V}\mathbf {r} \times \mathbf {b} \rho \,dV.\end{aligned}}}
  

where 
  
    
      
        
          v
        
      
    
    {\displaystyle \mathbf {v} }
  
 is the velocity, 
  
    
      
        V
      
    
    {\displaystyle V}
  
 the volume, and the derivatives of p and L are material derivatives.


== See also ==
List of topics named after Leonhard Euler
Euler's laws of rigid body rotations
Newton–Euler equations of motion with 6 components, combining Euler's two laws into one equation.


== References ==
