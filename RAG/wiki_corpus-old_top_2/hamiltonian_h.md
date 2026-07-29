# Hamiltonian mechanics

> **Query Topic**: Hamiltonian H (Rank #1 Search Result)  
> **Source Queue**: train (Row ID: 10, Frequency: 13)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Hamiltonian_mechanics

---

In physics, Hamiltonian mechanics is a reformulation of Lagrangian mechanics that emerged in 1833. Introduced by Sir William Rowan Hamilton, Hamiltonian mechanics replaces (generalized) velocities 
  
    
      
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\dot {q}}^{i}}
  
 used in Lagrangian mechanics with (generalized) momenta. Both theories provide interpretations of classical mechanics and describe the same physical phenomena.
Hamiltonian mechanics has a close relationship with geometry (notably, symplectic geometry and Poisson structures) and serves as a link between classical and quantum mechanics.


== Overview ==


=== Phase space coordinates (p, q) and Hamiltonian H ===
Let 
  
    
      
        (
        M
        ,
        
          
            L
          
        
        )
      
    
    {\displaystyle (M,{\mathcal {L}})}
  
 be a mechanical system with  configuration space 
  
    
      
        M
      
    
    {\displaystyle M}
  
 and smooth Lagrangian 
  
    
      
        
          
            L
          
        
        .
      
    
    {\displaystyle {\mathcal {L}}.}
  
 Select a standard coordinate system 
  
    
      
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        )
      
    
    {\displaystyle ({\boldsymbol {q}},{\boldsymbol {\dot {q}}})}
  
 on the tangent bundle 
  
    
      
        T
        M
        .
      
    
    {\displaystyle TM.}
  
 The quantities 
  
    
      
        
          
            p
            
              i
            
          
          (
          
            q
          
          ,
          
            
              
                q
                ˙
              
            
          
          ,
          t
          )
           
          
            
              
                
                  =
                
                
                  def
                
              
            
          
           
          
            ∂
            
              
                L
              
            
          
          
            /
          
          
            ∂
            
              
                
                  
                    q
                    ˙
                  
                
              
              
                i
              
            
          
        
      
    
    {\displaystyle \textstyle p_{i}({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)~{\stackrel {\text{def}}{=}}~{\partial {\mathcal {L}}}/{\partial {\dot {q}}^{i}}}
  
 are called momenta. (Also generalized momenta, conjugate momenta, and canonical momenta). For a time instant 
  
    
      
        t
        ,
      
    
    {\displaystyle t,}
  
 the Legendre transformation of 
  
    
      
        
          
            L
          
        
      
    
    {\displaystyle {\mathcal {L}}}
  
 is defined as the map 
  
    
      
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        )
        →
        
          (
          
            
              p
            
            ,
            
              q
            
          
          )
        
      
    
    {\displaystyle ({\boldsymbol {q}},{\boldsymbol {\dot {q}}})\to \left({\boldsymbol {p}},{\boldsymbol {q}}\right)}
  
 which is assumed to have a smooth inverse 
  
    
      
        (
        
          p
        
        ,
        
          q
        
        )
        →
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        )
        .
      
    
    {\displaystyle ({\boldsymbol {p}},{\boldsymbol {q}})\to ({\boldsymbol {q}},{\boldsymbol {\dot {q}}}).}
  
 For a system with 
  
    
      
        n
      
    
    {\displaystyle n}
  
 degrees of freedom, the Lagrangian mechanics defines the energy function

  
    
      
        
          E
          
            
              L
            
          
        
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        ,
        t
        )
        
        
          
            
              
                =
              
              
                def
              
            
          
        
        
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                
                  
                    
                      q
                      ˙
                    
                  
                
                
                  i
                
              
            
          
        
        −
        
          
            L
          
        
        .
      
    
    {\displaystyle E_{\mathcal {L}}({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)\,{\stackrel {\text{def}}{=}}\,\sum _{i=1}^{n}{\dot {q}}^{i}{\frac {\partial {\mathcal {L}}}{\partial {\dot {q}}^{i}}}-{\mathcal {L}}.}
  

The Legendre transform of 
  
    
      
        
          
            L
          
        
      
    
    {\displaystyle {\mathcal {L}}}
  
 turns 
  
    
      
        
          E
          
            
              L
            
          
        
      
    
    {\displaystyle E_{\mathcal {L}}}
  
 into a function 
  
    
      
        
          
            H
          
        
        (
        
          p
        
        ,
        
          q
        
        ,
        t
        )
      
    
    {\displaystyle {\mathcal {H}}({\boldsymbol {p}},{\boldsymbol {q}},t)}
  
 known as the Hamiltonian. The Hamiltonian satisfies

  
    
      
        
          
            H
          
        
        
          
            (
            
              
                
                  
                    ∂
                    
                      
                        L
                      
                    
                  
                  
                    ∂
                    
                      
                        
                          q
                          ˙
                        
                      
                    
                  
                
              
              ,
              
                q
              
              ,
              t
            
            )
          
        
        =
        
          E
          
            
              L
            
          
        
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        ,
        t
        )
      
    
    {\displaystyle {\mathcal {H}}{\left({\frac {\partial {\mathcal {L}}}{\partial {\boldsymbol {\dot {q}}}}},{\boldsymbol {q}},t\right)}=E_{\mathcal {L}}({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)}
  

which implies that

  
    
      
        
          
            H
          
        
        (
        
          p
        
        ,
        
          q
        
        ,
        t
        )
        =
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          p
          
            i
          
        
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
        −
        
          
            L
          
        
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        ,
        t
        )
        ,
      
    
    {\displaystyle {\mathcal {H}}({\boldsymbol {p}},{\boldsymbol {q}},t)=\sum _{i=1}^{n}p_{i}{\dot {q}}^{i}-{\mathcal {L}}({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t),}
  

where the velocities 
  
    
      
        
          
            
              q
              ˙
            
          
        
        =
        (
        
          
            
              
                q
                ˙
              
            
          
          
            1
          
        
        ,
        …
        ,
        
          
            
              
                q
                ˙
              
            
          
          
            n
          
        
        )
      
    
    {\displaystyle {\boldsymbol {\dot {q}}}=({\dot {q}}^{1},\ldots ,{\dot {q}}^{n})}
  
 are found from the (
  
    
      
        n
      
    
    {\displaystyle n}
  
-dimensional) equation 
  
    
      
        
          
            p
          
          =
          
            ∂
            
              
                L
              
            
          
          
            /
          
          
            ∂
            
              
                
                  q
                  ˙
                
              
            
          
        
      
    
    {\displaystyle \textstyle {\boldsymbol {p}}={\partial {\mathcal {L}}}/{\partial {\boldsymbol {\dot {q}}}}}
  
 which, by assumption, is uniquely solvable for ⁠
  
    
      
        
          
            
              q
              ˙
            
          
        
      
    
    {\displaystyle {\boldsymbol {\dot {q}}}}
  
⁠. The (
  
    
      
        2
        n
      
    
    {\displaystyle 2n}
  
-dimensional) pair 
  
    
      
        (
        
          p
        
        ,
        
          q
        
        )
      
    
    {\displaystyle ({\boldsymbol {p}},{\boldsymbol {q}})}
  
 is called phase space coordinates. (Also canonical coordinates).


=== From Euler–Lagrange equation to Hamilton's equations ===
In phase space coordinates ⁠
  
    
      
        (
        
          p
        
        ,
        
          q
        
        )
      
    
    {\displaystyle ({\boldsymbol {p}},{\boldsymbol {q}})}
  
⁠, the (
  
    
      
        n
      
    
    {\displaystyle n}
  
-dimensional) Euler–Lagrange equation

  
    
      
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                q
              
            
          
        
        −
        
          
            d
            
              d
              t
            
          
        
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                
                  
                    q
                    ˙
                  
                
              
            
          
        
        =
        0
      
    
    {\displaystyle {\frac {\partial {\mathcal {L}}}{\partial {\boldsymbol {q}}}}-{\frac {d}{dt}}{\frac {\partial {\mathcal {L}}}{\partial {\dot {\boldsymbol {q}}}}}=0}
  

becomes Hamilton's equations in 
  
    
      
        2
        n
      
    
    {\displaystyle 2n}
  
 dimensions


=== From stationary action principle to Hamilton's equations ===
Let 
  
    
      
        
          
            P
          
        
        (
        a
        ,
        b
        ,
        
          
            x
          
          
            a
          
        
        ,
        
          
            x
          
          
            b
          
        
        )
      
    
    {\displaystyle {\mathcal {P}}(a,b,{\boldsymbol {x}}_{a},{\boldsymbol {x}}_{b})}
  
 be the set of smooth paths 
  
    
      
        
          q
        
        :
        [
        a
        ,
        b
        ]
        →
        M
      
    
    {\displaystyle {\boldsymbol {q}}:[a,b]\to M}
  
 for which 
  
    
      
        
          q
        
        (
        a
        )
        =
        
          
            x
          
          
            a
          
        
      
    
    {\displaystyle {\boldsymbol {q}}(a)={\boldsymbol {x}}_{a}}
  
 and 
  
    
      
        
          q
        
        (
        b
        )
        =
        
          
            x
          
          
            b
          
        
        .
      
    
    {\displaystyle {\boldsymbol {q}}(b)={\boldsymbol {x}}_{b}.}
  
 The action functional 
  
    
      
        
          
            S
          
        
        :
        
          
            P
          
        
        (
        a
        ,
        b
        ,
        
          
            x
          
          
            a
          
        
        ,
        
          
            x
          
          
            b
          
        
        )
        →
        
          R
        
      
    
    {\displaystyle {\mathcal {S}}:{\mathcal {P}}(a,b,{\boldsymbol {x}}_{a},{\boldsymbol {x}}_{b})\to \mathbb {R} }
  
 is defined via

  
    
      
        
          
            S
          
        
        [
        
          q
        
        ]
        =
        
          ∫
          
            a
          
          
            b
          
        
        
          
            L
          
        
        (
        t
        ,
        
          q
        
        (
        t
        )
        ,
        
          
            
              q
              ˙
            
          
        
        (
        t
        )
        )
        
        d
        t
        =
        
          ∫
          
            a
          
          
            b
          
        
        
          (
          
            
              ∑
              
                i
                =
                1
              
              
                n
              
            
            
              p
              
                i
              
            
            
              
                
                  
                    q
                    ˙
                  
                
              
              
                i
              
            
            −
            
              
                H
              
            
            (
            
              p
            
            ,
            
              q
            
            ,
            t
            )
          
          )
        
        
        d
        t
        ,
      
    
    {\displaystyle {\mathcal {S}}[{\boldsymbol {q}}]=\int _{a}^{b}{\mathcal {L}}(t,{\boldsymbol {q}}(t),{\dot {\boldsymbol {q}}}(t))\,dt=\int _{a}^{b}\left(\sum _{i=1}^{n}p_{i}{\dot {q}}^{i}-{\mathcal {H}}({\boldsymbol {p}},{\boldsymbol {q}},t)\right)\,dt,}
  

where ⁠
  
    
      
        
          q
        
        =
        
          q
        
        (
        t
        )
      
    
    {\displaystyle {\boldsymbol {q}}={\boldsymbol {q}}(t)}
  
⁠, and 
  
    
      
        
          p
        
        =
        ∂
        
          
            L
          
        
        
          /
        
        ∂
        
          
            
              q
              ˙
            
          
        
      
    
    {\displaystyle {\boldsymbol {p}}=\partial {\mathcal {L}}/\partial {\boldsymbol {\dot {q}}}}
  
 (see above). A path 
  
    
      
        
          q
        
        ∈
        
          
            P
          
        
        (
        a
        ,
        b
        ,
        
          
            x
          
          
            a
          
        
        ,
        
          
            x
          
          
            b
          
        
        )
      
    
    {\displaystyle {\boldsymbol {q}}\in {\mathcal {P}}(a,b,{\boldsymbol {x}}_{a},{\boldsymbol {x}}_{b})}
  
 is a stationary point of 
  
    
      
        
          
            S
          
        
      
    
    {\displaystyle {\mathcal {S}}}
  
 (and hence is an equation of motion) if and only if the path 
  
    
      
        (
        
          p
        
        (
        t
        )
        ,
        
          q
        
        (
        t
        )
        )
      
    
    {\displaystyle ({\boldsymbol {p}}(t),{\boldsymbol {q}}(t))}
  
 in phase space coordinates obeys the Hamilton equations.


=== Basic physical interpretation ===
A simple interpretation of Hamiltonian mechanics comes from its application on a one-dimensional system consisting of one nonrelativistic particle of mass m. The value 
  
    
      
        H
        (
        p
        ,
        q
        )
      
    
    {\displaystyle H(p,q)}
  
 of the Hamiltonian is the total energy of the system, in this case the sum of kinetic and potential energy, traditionally denoted T and V, respectively. Here p is the momentum mv and q is the space coordinate. Then

  
    
      
        
          
            H
          
        
        =
        T
        +
        V
        ,
        
        T
        =
        
          
            
              p
              
                2
              
            
            
              2
              m
            
          
        
        ,
        
        V
        =
        V
        (
        q
        )
      
    
    {\displaystyle {\mathcal {H}}=T+V,\qquad T={\frac {p^{2}}{2m}},\qquad V=V(q)}
  

T is a function of p alone, while V is a function of q alone (i.e., T and V are scleronomic).
In this example, the time derivative of q is the velocity, and so the first Hamilton equation means that the particle's velocity equals the derivative of its kinetic energy with respect to its momentum.  The time derivative of the momentum p equals the Newtonian force, and so the second Hamilton equation means that the force equals the negative gradient of potential energy.


== Example ==

A spherical pendulum consists of a mass m moving without friction on the surface of a sphere. The only forces acting on the mass are the reaction from the sphere and gravity. Spherical coordinates are used to describe the position of the mass in terms of (r, θ, φ), where r is fixed, r = ℓ.
The Lagrangian for this system is

  
    
      
        L
        =
        
          
            1
            2
          
        
        m
        
          ℓ
          
            2
          
        
        
          (
          
            
              
                
                  
                    θ
                    ˙
                  
                
              
              
                2
              
            
            +
            
              sin
              
                2
              
            
            ⁡
            θ
             
            
              
                
                  
                    φ
                    ˙
                  
                
              
              
                2
              
            
          
          )
        
        +
        m
        g
        ℓ
        cos
        ⁡
        θ
        .
      
    
    {\displaystyle L={\frac {1}{2}}m\ell ^{2}\left({\dot {\theta }}^{2}+\sin ^{2}\theta \ {\dot {\varphi }}^{2}\right)+mg\ell \cos \theta .}
  

Thus the Hamiltonian is

  
    
      
        H
        =
        
          P
          
            θ
          
        
        
          
            
              θ
              ˙
            
          
        
        +
        
          P
          
            φ
          
        
        
          
            
              φ
              ˙
            
          
        
        −
        L
      
    
    {\displaystyle H=P_{\theta }{\dot {\theta }}+P_{\varphi }{\dot {\varphi }}-L}
  

where

  
    
      
        
          P
          
            θ
          
        
        =
        
          
            
              ∂
              L
            
            
              ∂
              
                
                  
                    θ
                    ˙
                  
                
              
            
          
        
        =
        m
        
          ℓ
          
            2
          
        
        
          
            
              θ
              ˙
            
          
        
      
    
    {\displaystyle P_{\theta }={\frac {\partial L}{\partial {\dot {\theta }}}}=m\ell ^{2}{\dot {\theta }}}
  

and

  
    
      
        
          P
          
            φ
          
        
        =
        
          
            
              ∂
              L
            
            
              ∂
              
                
                  
                    φ
                    ˙
                  
                
              
            
          
        
        =
        m
        
          ℓ
          
            2
          
        
        
          sin
          
            2
          
        
        
        θ
        
        
          
            
              φ
              ˙
            
          
        
        .
      
    
    {\displaystyle P_{\varphi }={\frac {\partial L}{\partial {\dot {\varphi }}}}=m\ell ^{2}\sin ^{2}\!\theta \,{\dot {\varphi }}.}
  

In terms of coordinates and momenta, the Hamiltonian reads

  
    
      
        
          
            
              
                H
              
              
                
                =
                
                  
                    
                      
                        
                          
                            [
                          
                        
                        
                          
                            
                              1
                              2
                            
                          
                        
                        m
                        
                          ℓ
                          
                            2
                          
                        
                        
                          
                            
                              
                                θ
                                ˙
                              
                            
                          
                          
                            2
                          
                        
                        +
                        
                          
                            
                              1
                              2
                            
                          
                        
                        m
                        
                          ℓ
                          
                            2
                          
                        
                        
                          sin
                          
                            2
                          
                        
                        
                        θ
                        
                        
                          
                            
                              
                                φ
                                ˙
                              
                            
                          
                          
                            2
                          
                        
                        
                          
                            ]
                          
                        
                      
                      ⏟
                    
                  
                  
                    T
                  
                
                +
                
                  
                    
                      
                        
                          
                            [
                          
                        
                        −
                        m
                        g
                        ℓ
                        cos
                        ⁡
                        θ
                        
                          
                            ]
                          
                        
                      
                      ⏟
                    
                  
                  
                    V
                  
                
              
            
            
              
              
                
                =
                
                  
                    
                      P
                      
                        θ
                      
                      
                        2
                      
                    
                    
                      2
                      m
                      
                        ℓ
                        
                          2
                        
                      
                    
                  
                
                +
                
                  
                    
                      P
                      
                        φ
                      
                      
                        2
                      
                    
                    
                      2
                      m
                      
                        ℓ
                        
                          2
                        
                      
                      
                        sin
                        
                          2
                        
                      
                      ⁡
                      θ
                    
                  
                
                −
                m
                g
                ℓ
                cos
                ⁡
                θ
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}H&=\underbrace {{\Bigl [}{\tfrac {1}{2}}m\ell ^{2}{\dot {\theta }}^{2}+{\tfrac {1}{2}}m\ell ^{2}\sin ^{2}\!\theta \,{\dot {\varphi }}^{2}{\Bigr ]}} _{T}+\underbrace {{\Bigl [}-mg\ell \cos \theta {\Bigr ]}} _{V}\\[2ex]&={\frac {P_{\theta }^{2}}{2m\ell ^{2}}}+{\frac {P_{\varphi }^{2}}{2m\ell ^{2}\sin ^{2}\theta }}-mg\ell \cos \theta .\end{aligned}}}
  

Hamilton's equations give the time evolution of coordinates and conjugate momenta in four first-order differential equations,

  
    
      
        
          
            
              
                
                  
                    
                      θ
                      ˙
                    
                  
                
              
              
                
                =
                
                  
                    
                      P
                      
                        θ
                      
                    
                    
                      m
                      
                        ℓ
                        
                          2
                        
                      
                    
                  
                
              
            
            
              
                
                  
                    
                      φ
                      ˙
                    
                  
                
              
              
                
                =
                
                  
                    
                      P
                      
                        φ
                      
                    
                    
                      m
                      
                        ℓ
                        
                          2
                        
                      
                      
                        sin
                        
                          2
                        
                      
                      ⁡
                      θ
                    
                  
                
              
            
            
              
                
                  
                    
                      
                        P
                        
                          θ
                        
                      
                      ˙
                    
                  
                
              
              
                
                =
                
                  
                    
                      P
                      
                        φ
                      
                      
                        2
                      
                    
                    
                      m
                      
                        ℓ
                        
                          2
                        
                      
                      
                        sin
                        
                          3
                        
                      
                      ⁡
                      θ
                    
                  
                
                cos
                ⁡
                θ
                −
                m
                g
                ℓ
                sin
                ⁡
                θ
              
            
            
              
                
                  
                    
                      
                        P
                        
                          φ
                        
                      
                      ˙
                    
                  
                
              
              
                
                =
                0.
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\dot {\theta }}&={P_{\theta } \over m\ell ^{2}}\\[6pt]{\dot {\varphi }}&={P_{\varphi } \over m\ell ^{2}\sin ^{2}\theta }\\[6pt]{\dot {P_{\theta }}}&={P_{\varphi }^{2} \over m\ell ^{2}\sin ^{3}\theta }\cos \theta -mg\ell \sin \theta \\[6pt]{\dot {P_{\varphi }}}&=0.\end{aligned}}}
  

Momentum ⁠
  
    
      
        
          P
          
            φ
          
        
      
    
    {\displaystyle P_{\varphi }}
  
⁠, which corresponds to the vertical component of angular momentum ⁠
  
    
      
        
          L
          
            z
          
        
        =
        ℓ
        sin
        ⁡
        θ
        ×
        m
        ℓ
        sin
        ⁡
        θ
        
        
          
            
              φ
              ˙
            
          
        
      
    
    {\displaystyle L_{z}=\ell \sin \theta \times m\ell \sin \theta \,{\dot {\varphi }}}
  
⁠, is a constant of motion. That is a consequence of the rotational symmetry of the system around the vertical axis. Being absent from the Hamiltonian, azimuth 
  
    
      
        φ
      
    
    {\displaystyle \varphi }
  
 is a cyclic coordinate, which implies conservation of its conjugate momentum.


== Deriving Hamilton's equations ==
Hamilton's equations can be derived by a calculation with the Lagrangian ⁠
  
    
      
        
          
            L
          
        
      
    
    {\displaystyle {\mathcal {L}}}
  
⁠, generalized positions qi, and generalized velocities ⋅qi, where ⁠
  
    
      
        i
        =
        1
        ,
        …
        ,
        n
      
    
    {\displaystyle i=1,\ldots ,n}
  
⁠. Here we work off-shell, meaning ⁠
  
    
      
        
          q
          
            i
          
        
      
    
    {\displaystyle q^{i}}
  
⁠, ⁠
  
    
      
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\dot {q}}^{i}}
  
⁠, ⁠
  
    
      
        t
      
    
    {\displaystyle t}
  
⁠ are independent coordinates in phase space, not constrained to follow any equations of motion (in particular, 
  
    
      
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\dot {q}}^{i}}
  
 is not a derivative of ⁠
  
    
      
        
          q
          
            i
          
        
      
    
    {\displaystyle q^{i}}
  
⁠). The total differential of the Lagrangian is:

  
    
      
        
          d
        
        
          
            L
          
        
        =
        
          ∑
          
            i
          
        
        
          (
          
            
              
                
                  ∂
                  
                    
                      L
                    
                  
                
                
                  ∂
                  
                    q
                    
                      i
                    
                  
                
              
            
            
              d
            
            
              q
              
                i
              
            
            +
            
              
                
                  ∂
                  
                    
                      L
                    
                  
                
                
                  ∂
                  
                    
                      
                        
                          q
                          ˙
                        
                      
                    
                    
                      i
                    
                  
                
              
            
            
            
              d
            
            
              
                
                  
                    q
                    ˙
                  
                
              
              
                i
              
            
          
          )
        
        +
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              t
            
          
        
        
        
          d
        
        t
         
        .
      
    
    {\displaystyle \mathrm {d} {\mathcal {L}}=\sum _{i}\left({\frac {\partial {\mathcal {L}}}{\partial q^{i}}}\mathrm {d} q^{i}+{\frac {\partial {\mathcal {L}}}{\partial {\dot {q}}^{i}}}\,\mathrm {d} {\dot {q}}^{i}\right)+{\frac {\partial {\mathcal {L}}}{\partial t}}\,\mathrm {d} t\ .}
  

The generalized momentum coordinates were defined as ⁠
  
    
      
        
          p
          
            i
          
        
        =
        ∂
        
          
            L
          
        
        
          /
        
        ∂
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
      
    
    {\displaystyle p_{i}=\partial {\mathcal {L}}/\partial {\dot {q}}^{i}}
  
⁠, so we may rewrite the equation as:

  
    
      
        
          
            
              
                
                  d
                
                
                  
                    L
                  
                
                =
              
              
                
                
                  ∑
                  
                    i
                  
                
                
                  (
                  
                    
                      
                        
                          ∂
                          
                            
                              L
                            
                          
                        
                        
                          ∂
                          
                            q
                            
                              i
                            
                          
                        
                      
                    
                    
                    
                      d
                    
                    
                      q
                      
                        i
                      
                    
                    +
                    
                      p
                      
                        i
                      
                    
                    
                      d
                    
                    
                      
                        
                          
                            q
                            ˙
                          
                        
                      
                      
                        i
                      
                    
                  
                  )
                
                +
                
                  
                    
                      ∂
                      
                        
                          L
                        
                      
                    
                    
                      ∂
                      t
                    
                  
                
                
                  d
                
                t
              
            
            
              
                =
              
              
                
                
                  ∑
                  
                    i
                  
                
                
                  (
                  
                    
                      
                        
                          ∂
                          
                            
                              L
                            
                          
                        
                        
                          ∂
                          
                            q
                            
                              i
                            
                          
                        
                      
                    
                    
                    
                      d
                    
                    
                      q
                      
                        i
                      
                    
                    +
                    
                      d
                    
                    (
                    
                      p
                      
                        i
                      
                    
                    
                      
                        
                          
                            q
                            ˙
                          
                        
                      
                      
                        i
                      
                    
                    )
                    −
                    
                      
                        
                          
                            q
                            ˙
                          
                        
                      
                      
                        i
                      
                    
                    
                    
                      d
                    
                    
                      p
                      
                        i
                      
                    
                  
                  )
                
                +
                
                  
                    
                      ∂
                      
                        
                          L
                        
                      
                    
                    
                      ∂
                      t
                    
                  
                
                
                
                  d
                
                t
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\mathrm {d} {\mathcal {L}}=&\sum _{i}\left({\frac {\partial {\mathcal {L}}}{\partial q^{i}}}\,\mathrm {d} q^{i}+p_{i}\mathrm {d} {\dot {q}}^{i}\right)+{\frac {\partial {\mathcal {L}}}{\partial t}}\mathrm {d} t\\=&\sum _{i}\left({\frac {\partial {\mathcal {L}}}{\partial q^{i}}}\,\mathrm {d} q^{i}+\mathrm {d} (p_{i}{\dot {q}}^{i})-{\dot {q}}^{i}\,\mathrm {d} p_{i}\right)+{\frac {\partial {\mathcal {L}}}{\partial t}}\,\mathrm {d} t\,.\end{aligned}}}
  

After rearranging, one obtains:

  
    
      
        
          d
        
        
        
          (
          
            
              ∑
              
                i
              
            
            
              p
              
                i
              
            
            
              
                
                  
                    q
                    ˙
                  
                
              
              
                i
              
            
            −
            
              
                L
              
            
          
          )
        
        =
        
          ∑
          
            i
          
        
        
          (
          
            −
            
              
                
                  ∂
                  
                    
                      L
                    
                  
                
                
                  ∂
                  
                    q
                    
                      i
                    
                  
                
              
            
            
            
              d
            
            
              q
              
                i
              
            
            +
            
              
                
                  
                    q
                    ˙
                  
                
              
              
                i
              
            
            
              d
            
            
              p
              
                i
              
            
          
          )
        
        −
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              t
            
          
        
        
        
          d
        
        t
         
        .
      
    
    {\displaystyle \mathrm {d} \!\left(\sum _{i}p_{i}{\dot {q}}^{i}-{\mathcal {L}}\right)=\sum _{i}\left(-{\frac {\partial {\mathcal {L}}}{\partial q^{i}}}\,\mathrm {d} q^{i}+{\dot {q}}^{i}\mathrm {d} p_{i}\right)-{\frac {\partial {\mathcal {L}}}{\partial t}}\,\mathrm {d} t\ .}
  

The term in parentheses on the left-hand side is just the Hamiltonian 
  
    
      
        
          
            H
          
        
        =
        ∑
        
          p
          
            i
          
        
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
        −
        
          
            L
          
        
      
    
    {\textstyle {\mathcal {H}}=\sum p_{i}{\dot {q}}^{i}-{\mathcal {L}}}
  
 defined previously, therefore:

  
    
      
        
          d
        
        
          
            H
          
        
        =
        
          ∑
          
            i
          
        
        
          (
          
            −
            
              
                
                  ∂
                  
                    
                      L
                    
                  
                
                
                  ∂
                  
                    q
                    
                      i
                    
                  
                
              
            
            
            
              d
            
            
              q
              
                i
              
            
            +
            
              
                
                  
                    q
                    ˙
                  
                
              
              
                i
              
            
            
            
              d
            
            
              p
              
                i
              
            
          
          )
        
        −
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              t
            
          
        
        
        
          d
        
        t
         
        .
      
    
    {\displaystyle \mathrm {d} {\mathcal {H}}=\sum _{i}\left(-{\frac {\partial {\mathcal {L}}}{\partial q^{i}}}\,\mathrm {d} q^{i}+{\dot {q}}^{i}\,\mathrm {d} p_{i}\right)-{\frac {\partial {\mathcal {L}}}{\partial t}}\,\mathrm {d} t\ .}
  

One may also calculate the total differential of the Hamiltonian 
  
    
      
        
          
            H
          
        
      
    
    {\displaystyle {\mathcal {H}}}
  
 with respect to coordinates ⁠
  
    
      
        
          q
          
            i
          
        
      
    
    {\displaystyle q^{i}}
  
⁠, ⁠
  
    
      
        
          p
          
            i
          
        
      
    
    {\displaystyle p_{i}}
  
⁠, ⁠
  
    
      
        t
      
    
    {\displaystyle t}
  
⁠ instead of ⁠
  
    
      
        
          q
          
            i
          
        
      
    
    {\displaystyle q^{i}}
  
⁠, ⁠
  
    
      
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\dot {q}}^{i}}
  
⁠, ⁠
  
    
      
        t
      
    
    {\displaystyle t}
  
⁠, yielding:

  
    
      
        
          d
        
        
          
            H
          
        
        =
        
          ∑
          
            i
          
        
        
          (
          
            
              
                
                  ∂
                  
                    
                      H
                    
                  
                
                
                  ∂
                  
                    q
                    
                      i
                    
                  
                
              
            
            
              d
            
            
              q
              
                i
              
            
            +
            
              
                
                  ∂
                  
                    
                      H
                    
                  
                
                
                  ∂
                  
                    p
                    
                      i
                    
                  
                
              
            
            
              d
            
            
              p
              
                i
              
            
          
          )
        
        +
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              t
            
          
        
        
        
          d
        
        t
         
        .
      
    
    {\displaystyle \mathrm {d} {\mathcal {H}}=\sum _{i}\left({\frac {\partial {\mathcal {H}}}{\partial q^{i}}}\mathrm {d} q^{i}+{\frac {\partial {\mathcal {H}}}{\partial p_{i}}}\mathrm {d} p_{i}\right)+{\frac {\partial {\mathcal {H}}}{\partial t}}\,\mathrm {d} t\ .}
  

One may now equate these two expressions for ⁠
  
    
      
        d
        
          
            H
          
        
      
    
    {\displaystyle d{\mathcal {H}}}
  
⁠, one in terms of ⁠
  
    
      
        
          
            L
          
        
      
    
    {\displaystyle {\mathcal {L}}}
  
⁠, the other in terms of ⁠
  
    
      
        
          
            H
          
        
      
    
    {\displaystyle {\mathcal {H}}}
  
⁠:

  
    
      
        
          ∑
          
            i
          
        
        
          (
          
            −
            
              
                
                  ∂
                  
                    
                      L
                    
                  
                
                
                  ∂
                  
                    q
                    
                      i
                    
                  
                
              
            
            
              d
            
            
              q
              
                i
              
            
            +
            
              
                
                  
                    q
                    ˙
                  
                
              
              
                i
              
            
            
              d
            
            
              p
              
                i
              
            
          
          )
        
        −
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              t
            
          
        
        
        
          d
        
        t
         
        =
         
        
          ∑
          
            i
          
        
        
          (
          
            
              
                
                  ∂
                  
                    
                      H
                    
                  
                
                
                  ∂
                  
                    q
                    
                      i
                    
                  
                
              
            
            
              d
            
            
              q
              
                i
              
            
            +
            
              
                
                  ∂
                  
                    
                      H
                    
                  
                
                
                  ∂
                  
                    p
                    
                      i
                    
                  
                
              
            
            
              d
            
            
              p
              
                i
              
            
          
          )
        
        +
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              t
            
          
        
        
        
          d
        
        t
         
        .
      
    
    {\displaystyle \sum _{i}\left(-{\frac {\partial {\mathcal {L}}}{\partial q^{i}}}\mathrm {d} q^{i}+{\dot {q}}^{i}\mathrm {d} p_{i}\right)-{\frac {\partial {\mathcal {L}}}{\partial t}}\,\mathrm {d} t\ =\ \sum _{i}\left({\frac {\partial {\mathcal {H}}}{\partial q^{i}}}\mathrm {d} q^{i}+{\frac {\partial {\mathcal {H}}}{\partial p_{i}}}\mathrm {d} p_{i}\right)+{\frac {\partial {\mathcal {H}}}{\partial t}}\,\mathrm {d} t\ .}
  

Since these calculations are off-shell, one can equate the respective coefficients of ⁠
  
    
      
        
          d
        
        
          q
          
            i
          
        
      
    
    {\displaystyle \mathrm {d} q^{i}}
  
⁠, ⁠
  
    
      
        
          d
        
        
          p
          
            i
          
        
      
    
    {\displaystyle \mathrm {d} p_{i}}
  
⁠, ⁠
  
    
      
        
          d
        
        t
      
    
    {\displaystyle \mathrm {d} t}
  
⁠ on the two sides:

  
    
      
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
        =
        −
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
        
        ,
        
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              
                p
                
                  i
                
              
            
          
        
        =
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
        
        ,
        
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              t
            
          
        
        =
        −
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              t
            
          
        
         
        .
      
    
    {\displaystyle {\frac {\partial {\mathcal {H}}}{\partial q^{i}}}=-{\frac {\partial {\mathcal {L}}}{\partial q^{i}}}\quad ,\quad {\frac {\partial {\mathcal {H}}}{\partial p_{i}}}={\dot {q}}^{i}\quad ,\quad {\frac {\partial {\mathcal {H}}}{\partial t}}=-{\partial {\mathcal {L}} \over \partial t}\ .}
  

On-shell, one substitutes parametric functions 
  
    
      
        
          q
          
            i
          
        
        =
        
          q
          
            i
          
        
        (
        t
        )
      
    
    {\displaystyle q^{i}=q^{i}(t)}
  
 which define a trajectory in phase space with velocities ⁠
  
    
      
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
        =
        
          
            
              d
              
                d
                t
              
            
          
        
        
          q
          
            i
          
        
        (
        t
        )
      
    
    {\displaystyle {\dot {q}}^{i}={\tfrac {d}{dt}}q^{i}(t)}
  
⁠, obeying Lagrange's equations:

  
    
      
        
          
            
              d
            
            
              
                d
              
              t
            
          
        
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                
                  
                    
                      q
                      ˙
                    
                  
                
                
                  i
                
              
            
          
        
        −
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
        =
        0
         
        .
      
    
    {\displaystyle {\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial {\mathcal {L}}}{\partial {\dot {q}}^{i}}}-{\frac {\partial {\mathcal {L}}}{\partial q^{i}}}=0\ .}
  

Rearranging and writing in terms of the on-shell 
  
    
      
        
          p
          
            i
          
        
        =
        
          p
          
            i
          
        
        (
        t
        )
      
    
    {\displaystyle p_{i}=p_{i}(t)}
  
 gives:

  
    
      
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
        =
        
          
            
              
                p
                ˙
              
            
          
          
            i
          
        
         
        .
      
    
    {\displaystyle {\frac {\partial {\mathcal {L}}}{\partial q^{i}}}={\dot {p}}_{i}\ .}
  

Thus Lagrange's equations are equivalent to Hamilton's equations:

  
    
      
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
        =
        −
        
          
            
              
                p
                ˙
              
            
          
          
            i
          
        
        
        ,
        
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              
                p
                
                  i
                
              
            
          
        
        =
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
        
        ,
        
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              t
            
          
        
        =
        −
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              t
            
          
        
        
        .
      
    
    {\displaystyle {\frac {\partial {\mathcal {H}}}{\partial q^{i}}}=-{\dot {p}}_{i}\quad ,\quad {\frac {\partial {\mathcal {H}}}{\partial p_{i}}}={\dot {q}}^{i}\quad ,\quad {\frac {\partial {\mathcal {H}}}{\partial t}}=-{\frac {\partial {\mathcal {L}}}{\partial t}}\,.}
  

In the case of time-independent 
  
    
      
        
          
            H
          
        
      
    
    {\displaystyle {\mathcal {H}}}
  
 and ⁠
  
    
      
        
          
            L
          
        
      
    
    {\displaystyle {\mathcal {L}}}
  
⁠, i.e. ⁠
  
    
      
        ∂
        
          
            H
          
        
        
          /
        
        ∂
        t
        =
        −
        ∂
        
          
            L
          
        
        
          /
        
        ∂
        t
        =
        0
      
    
    {\displaystyle \partial {\mathcal {H}}/\partial t=-\partial {\mathcal {L}}/\partial t=0}
  
⁠, Hamilton's equations consist of 2n first-order differential equations, while Lagrange's equations consist of n second-order equations. Hamilton's equations usually do not reduce the difficulty of finding explicit solutions, but important theoretical results can be derived from them, because coordinates and momenta are independent variables with nearly symmetric roles.
Hamilton's equations have another advantage over Lagrange's equations: if a system has a symmetry, so that some coordinate 
  
    
      
        
          q
          
            i
          
        
      
    
    {\displaystyle q_{i}}
  
 does not occur in the Hamiltonian (i.e. a cyclic coordinate), the corresponding momentum coordinate 
  
    
      
        
          p
          
            i
          
        
      
    
    {\displaystyle p_{i}}
  
 is conserved along each trajectory, and that coordinate can be reduced to a constant in the other equations of the set. This effectively reduces the problem from n coordinates to (n − 1) coordinates: this is the basis of symplectic reduction in geometry. In the Lagrangian framework, the conservation of momentum also follows immediately, however all the generalized velocities 
  
    
      
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\dot {q}}_{i}}
  
 still occur in the Lagrangian, and a system of equations in n coordinates still has to be solved.
The Lagrangian and Hamiltonian approaches provide the groundwork for deeper results in classical mechanics, and suggest analogous formulations in quantum mechanics: the path integral formulation and the Schrödinger equation.


== Properties of the Hamiltonian ==
The value of the Hamiltonian 
  
    
      
        
          
            H
          
        
      
    
    {\displaystyle {\mathcal {H}}}
  
 is the total energy of the system if and only if the energy function 
  
    
      
        
          E
          
            
              L
            
          
        
      
    
    {\displaystyle E_{\mathcal {L}}}
  
 has the same property. (See definition of ⁠
  
    
      
        
          
            H
          
        
      
    
    {\displaystyle {\mathcal {H}}}
  
⁠).

  
    
      
        
          
            
              d
              
                
                  H
                
              
            
            
              d
              t
            
          
        
        =
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              t
            
          
        
      
    
    {\displaystyle {\frac {d{\mathcal {H}}}{dt}}={\frac {\partial {\mathcal {H}}}{\partial t}}}
  
 when ⁠
  
    
      
        
          p
        
        (
        t
        )
      
    
    {\displaystyle \mathbf {p} (t)}
  
⁠, ⁠
  
    
      
        
          q
        
        (
        t
        )
      
    
    {\displaystyle \mathbf {q} (t)}
  
⁠ form a solution of Hamilton's equations. Indeed, 
  
    
      
        
          
            
              d
              
                
                  H
                
              
            
            
              d
              t
            
          
        
        =
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              
                p
              
            
          
        
        ⋅
        
          
            
              p
              ˙
            
          
        
        +
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              
                q
              
            
          
        
        ⋅
        
          
            
              q
              ˙
            
          
        
        +
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              t
            
          
        
        ,
      
    
    {\textstyle {\frac {d{\mathcal {H}}}{dt}}={\frac {\partial {\mathcal {H}}}{\partial {\boldsymbol {p}}}}\cdot {\dot {\boldsymbol {p}}}+{\frac {\partial {\mathcal {H}}}{\partial {\boldsymbol {q}}}}\cdot {\dot {\boldsymbol {q}}}+{\frac {\partial {\mathcal {H}}}{\partial t}},}
  
 and everything but the final term cancels out.

  
    
      
        
          
            H
          
        
      
    
    {\displaystyle {\mathcal {H}}}
  
 does not change under point transformations, i.e. smooth changes 
  
    
      
        
          q
        
        ↔
        
          
            q
            ′
          
        
      
    
    {\displaystyle {\boldsymbol {q}}\leftrightarrow {\boldsymbol {q'}}}
  
 of space coordinates. (Follows from the invariance of the energy function 
  
    
      
        
          E
          
            
              L
            
          
        
      
    
    {\displaystyle E_{\mathcal {L}}}
  
 under point transformations. The invariance of 
  
    
      
        
          E
          
            
              L
            
          
        
      
    
    {\displaystyle E_{\mathcal {L}}}
  
 can be established directly).

  
    
      
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              t
            
          
        
        =
        −
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              t
            
          
        
        .
      
    
    {\displaystyle {\frac {\partial {\mathcal {H}}}{\partial t}}=-{\frac {\partial {\mathcal {L}}}{\partial t}}.}
  
 (See § Deriving Hamilton's equations).
⁠
  
    
      
        −
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
        =
        
          
            
              
                p
                ˙
              
            
          
          
            i
          
        
        =
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
      
    
    {\displaystyle -{\frac {\partial {\mathcal {H}}}{\partial q^{i}}}={\dot {p}}_{i}={\frac {\partial {\mathcal {L}}}{\partial q^{i}}}}
  
⁠. (Compare Hamilton's and Euler–Lagrange equations or see § Deriving Hamilton's equations).

  
    
      
        
          
            
              ∂
              
                
                  H
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
        =
        0
      
    
    {\displaystyle {\frac {\partial {\mathcal {H}}}{\partial q^{i}}}=0}
  
 if and only if ⁠
  
    
      
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                q
                
                  i
                
              
            
          
        
        =
        0
      
    
    {\displaystyle {\frac {\partial {\mathcal {L}}}{\partial q^{i}}}=0}
  
⁠.A coordinate for which the last equation holds is called cyclic (or ignorable). Every cyclic coordinate 
  
    
      
        
          q
          
            i
          
        
      
    
    {\displaystyle q^{i}}
  
 reduces the number of degrees of freedom by ⁠
  
    
      
        1
      
    
    {\displaystyle 1}
  
⁠, causes the corresponding momentum 
  
    
      
        
          p
          
            i
          
        
      
    
    {\displaystyle p_{i}}
  
 to be conserved, and makes Hamilton's equations easier to solve.


== Hamiltonian as the total system energy ==
In its application to a given system, the Hamiltonian is often taken to be

  
    
      
        
          
            H
          
        
        =
        T
        +
        V
      
    
    {\displaystyle {\mathcal {H}}=T+V}
  

where 
  
    
      
        T
      
    
    {\displaystyle T}
  
 is the kinetic energy and 
  
    
      
        V
      
    
    {\displaystyle V}
  
 is the potential energy. Using this relation can be simpler than first calculating the Lagrangian, and then deriving the Hamiltonian from the Lagrangian. However, the relation is not true for all systems.
The relation holds true for nonrelativistic systems when all of the following conditions are satisfied

  
    
      
        
          
            
              ∂
              V
              (
              
                q
              
              ,
              
                
                  
                    q
                    ˙
                  
                
              
              ,
              t
              )
            
            
              ∂
              
                
                  
                    
                      q
                      ˙
                    
                  
                
                
                  i
                
              
            
          
        
        =
        0
        
        ,
        
        ∀
        i
      
    
    {\displaystyle {\frac {\partial V({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)}{\partial {\dot {q}}_{i}}}=0\;,\quad \forall i}
  

  
    
      
        
          
            
              ∂
              T
              (
              
                q
              
              ,
              
                
                  
                    q
                    ˙
                  
                
              
              ,
              t
              )
            
            
              ∂
              t
            
          
        
        =
        0
      
    
    {\displaystyle {\frac {\partial T({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)}{\partial t}}=0}
  

  
    
      
        T
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        )
        =
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        
          ∑
          
            j
            =
            1
          
          
            n
          
        
        
          
            (
          
        
        
          c
          
            i
            j
          
        
        (
        
          q
        
        )
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
        
          
            
              
                q
                ˙
              
            
          
          
            j
          
        
        
          
            )
          
        
      
    
    {\displaystyle T({\boldsymbol {q}},{\boldsymbol {\dot {q}}})=\sum _{i=1}^{n}\sum _{j=1}^{n}{\biggl (}c_{ij}({\boldsymbol {q}}){\dot {q}}_{i}{\dot {q}}_{j}{\biggr )}}
  

where 
  
    
      
        t
      
    
    {\displaystyle t}
  
 is time, 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is the number of degrees of freedom of the system, and each 
  
    
      
        
          c
          
            i
            j
          
        
        (
        
          q
        
        )
      
    
    {\displaystyle c_{ij}({\boldsymbol {q}})}
  
 is an arbitrary scalar function of 
  
    
      
        
          q
        
      
    
    {\displaystyle {\boldsymbol {q}}}
  
.
In words, this means that the relation 
  
    
      
        
          
            H
          
        
        =
        T
        +
        V
      
    
    {\displaystyle {\mathcal {H}}=T+V}
  
 holds true if 
  
    
      
        T
      
    
    {\displaystyle T}
  
 does not contain time as an explicit variable (it is scleronomic), 
  
    
      
        V
      
    
    {\displaystyle V}
  
 does not contain generalised velocity as an explicit variable, and each term of 
  
    
      
        T
      
    
    {\displaystyle T}
  
 is quadratic in generalised velocity.


=== Proof ===
Preliminary to this proof, it is important to address an ambiguity in the related mathematical notation. While a change of variables can be used to equate

  
    
      
        
          
            L
          
        
        (
        
          p
        
        ,
        
          q
        
        ,
        t
        )
        =
        
          
            L
          
        
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        ,
        t
        )
      
    
    {\displaystyle {\mathcal {L}}({\boldsymbol {p}},{\boldsymbol {q}},t)={\mathcal {L}}({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)}
  
,
it is important to note that

  
    
      
        
          
            
              ∂
              
                
                  L
                
              
              (
              
                q
              
              ,
              
                
                  
                    q
                    ˙
                  
                
              
              ,
              t
              )
            
            
              ∂
              
                
                  
                    
                      q
                      ˙
                    
                  
                
                
                  i
                
              
            
          
        
        ≠
        
          
            
              ∂
              
                
                  L
                
              
              (
              
                p
              
              ,
              
                q
              
              ,
              t
              )
            
            
              ∂
              
                
                  
                    
                      q
                      ˙
                    
                  
                
                
                  i
                
              
            
          
        
      
    
    {\displaystyle {\frac {\partial {\mathcal {L}}({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)}{\partial {\dot {q}}_{i}}}\neq {\frac {\partial {\mathcal {L}}({\boldsymbol {p}},{\boldsymbol {q}},t)}{\partial {\dot {q}}_{i}}}}
  
.
In this case, the right hand side always evaluates to 0. To perform a change of variables inside of a partial derivative, the multivariable chain rule should be used. Hence, to avoid ambiguity, the function arguments of any term inside of a partial derivative should be stated.
Additionally, this proof uses the notation 
  
    
      
        f
        (
        a
        ,
        b
        ,
        c
        )
        =
        f
        (
        a
        ,
        b
        )
      
    
    {\displaystyle f(a,b,c)=f(a,b)}
  
 to imply that 
  
    
      
        
          
            
              ∂
              f
              (
              a
              ,
              b
              ,
              c
              )
            
            
              ∂
              c
            
          
        
        =
        0
      
    
    {\displaystyle {\frac {\partial f(a,b,c)}{\partial c}}=0}
  
.


=== Application to systems of point masses ===
For a system of point masses, the requirement for 
  
    
      
        T
      
    
    {\displaystyle T}
  
 to be quadratic in generalised velocity is always satisfied for the case where 
  
    
      
        T
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        ,
        t
        )
        =
        T
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        )
      
    
    {\displaystyle T({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)=T({\boldsymbol {q}},{\boldsymbol {\dot {q}}})}
  
, which is a requirement for 
  
    
      
        
          
            H
          
        
        =
        T
        +
        V
      
    
    {\displaystyle {\mathcal {H}}=T+V}
  
 anyway.


=== Conservation of energy ===
If the conditions for 
  
    
      
        
          
            H
          
        
        =
        T
        +
        V
      
    
    {\displaystyle {\mathcal {H}}=T+V}
  
 are satisfied, then conservation of the Hamiltonian implies conservation of energy. This requires the additional condition that 
  
    
      
        V
      
    
    {\displaystyle V}
  
 does not contain time as an explicit variable.

  
    
      
        
          
            
              ∂
              V
              (
              
                q
              
              ,
              
                
                  
                    q
                    ˙
                  
                
              
              ,
              t
              )
            
            
              ∂
              t
            
          
        
        =
        0
      
    
    {\displaystyle {\frac {\partial V({\boldsymbol {q}},{\boldsymbol {\dot {q}}},t)}{\partial t}}=0}
  

In summary, the requirements for 
  
    
      
        
          
            H
          
        
        =
        T
        +
        V
        =
        
          constant of time
        
      
    
    {\displaystyle {\mathcal {H}}=T+V={\text{constant of time}}}
  
 to be satisfied for a nonrelativistic system are

  
    
      
        V
        =
        V
        (
        
          q
        
        )
      
    
    {\displaystyle V=V({\boldsymbol {q}})}
  

  
    
      
        T
        =
        T
        (
        
          q
        
        ,
        
          
            
              q
              ˙
            
          
        
        )
      
    
    {\displaystyle T=T({\boldsymbol {q}},{\boldsymbol {\dot {q}}})}
  

  
    
      
        T
      
    
    {\displaystyle T}
  
 is a homogeneous quadratic function in 
  
    
      
        
          
            
              q
              ˙
            
          
        
      
    
    {\displaystyle {\boldsymbol {\dot {q}}}}
  

Regarding extensions to the Euler-Lagrange formulation which use dissipation functions (See Lagrangian mechanics § Extensions to include non-conservative forces), e.g. the Rayleigh dissipation function, energy is not conserved when a dissipation function has effect. It is possible to explain the link between this and the former requirements by relating the extended and conventional Euler-Lagrange equations: grouping the extended terms into the potential function produces a velocity dependent potential. Hence, the requirements are not satisfied when a dissipation function has effect.


== Hamiltonian of a charged particle in an electromagnetic field ==
A sufficient illustration of Hamiltonian mechanics is given by the Hamiltonian of a charged particle in an electromagnetic field. In Cartesian coordinates the Lagrangian of a non-relativistic classical particle in an electromagnetic field is (in SI Units):

  
    
      
        
          
            L
          
        
        =
        
          ∑
          
            i
          
        
        
          
            
              1
              2
            
          
        
        m
        
          
            
              
                x
                ˙
              
            
          
          
            i
          
          
            2
          
        
        +
        
          ∑
          
            i
          
        
        q
        
          
            
              
                x
                ˙
              
            
          
          
            i
          
        
        
          A
          
            i
          
        
        −
        q
        φ
        ,
      
    
    {\displaystyle {\mathcal {L}}=\sum _{i}{\tfrac {1}{2}}m{\dot {x}}_{i}^{2}+\sum _{i}q{\dot {x}}_{i}A_{i}-q\varphi ,}
  

where q is the electric charge of the particle, φ is the electric scalar potential, and the Ai are the components of the magnetic vector potential that may all explicitly depend on 
  
    
      
        
          x
          
            i
          
        
      
    
    {\displaystyle x_{i}}
  
 and ⁠
  
    
      
        t
      
    
    {\displaystyle t}
  
⁠.
This Lagrangian, combined with Euler–Lagrange equation, produces the Lorentz force law

  
    
      
        m
        
          
            
              
                x
              
              ¨
            
          
        
        =
        q
        
          E
        
        +
        q
        
          
            
              
                x
              
              ˙
            
          
        
        ×
        
          B
        
        
        ,
      
    
    {\displaystyle m{\ddot {\mathbf {x} }}=q\mathbf {E} +q{\dot {\mathbf {x} }}\times \mathbf {B} \,,}
  

and is called minimal coupling.
The canonical momenta are given by:

  
    
      
        
          p
          
            i
          
        
        =
        
          
            
              ∂
              
                
                  L
                
              
            
            
              ∂
              
                
                  
                    
                      x
                      ˙
                    
                  
                
                
                  i
                
              
            
          
        
        =
        m
        
          
            
              
                x
                ˙
              
            
          
          
            i
          
        
        +
        q
        
          A
          
            i
          
        
        .
      
    
    {\displaystyle p_{i}={\frac {\partial {\mathcal {L}}}{\partial {\dot {x}}_{i}}}=m{\dot {x}}_{i}+qA_{i}.}
  

The Hamiltonian, as the Legendre transformation of the Lagrangian, is therefore:

  
    
      
        
          
            H
          
        
        =
        
          ∑
          
            i
          
        
        
          
            
              
                x
                ˙
              
            
          
          
            i
          
        
        
          p
          
            i
          
        
        −
        
          
            L
          
        
        =
        
          ∑
          
            i
          
        
        
          
            
              
                (
                
                  
                    p
                    
                      i
                    
                  
                  −
                  q
                  
                    A
                    
                      i
                    
                  
                
                )
              
              
                2
              
            
            
              2
              m
            
          
        
        +
        q
        φ
        .
      
    
    {\displaystyle {\mathcal {H}}=\sum _{i}{\dot {x}}_{i}p_{i}-{\mathcal {L}}=\sum _{i}{\frac {\left(p_{i}-qA_{i}\right)^{2}}{2m}}+q\varphi .}
  

This equation is used frequently in quantum mechanics.
Under gauge transformation:

  
    
      
        
          A
        
        →
        
          A
        
        +
        ∇
        f
        
        ,
        
        φ
        →
        φ
        −
        
          
            
              f
              ˙
            
          
        
        
        ,
      
    
    {\displaystyle \mathbf {A} \rightarrow \mathbf {A} +\nabla f\,,\quad \varphi \rightarrow \varphi -{\dot {f}}\,,}
  

where f(r, t) is any scalar function of space and time. The aforementioned Lagrangian, the canonical momenta, and the Hamiltonian transform like:

  
    
      
        L
        →
        
          L
          ′
        
        =
        L
        +
        q
        
          
            
              d
              f
            
            
              d
              t
            
          
        
        
        ,
        
        
          p
        
        →
        
          
            p
            ′
          
        
        =
        
          p
        
        +
        q
        ∇
        f
        
        ,
        
        H
        →
        
          H
          ′
        
        =
        H
        −
        q
        
          
            
              ∂
              f
            
            
              ∂
              t
            
          
        
        
        ,
      
    
    {\displaystyle L\rightarrow L'=L+q{\frac {df}{dt}}\,,\quad \mathbf {p} \rightarrow \mathbf {p'} =\mathbf {p} +q\nabla f\,,\quad H\rightarrow H'=H-q{\frac {\partial f}{\partial t}}\,,}
  

which still produces the same Hamilton's equation:

  
    
      
        
          
            
              
                
                  
                    
                    
                      
                        
                          ∂
                          
                            H
                            ′
                          
                        
                        
                          ∂
                          
                            
                              x
                              
                                i
                              
                            
                          
                        
                      
                    
                    |
                  
                  
                    
                      p
                      
                        i
                      
                      ′
                    
                  
                
              
              
                
                =
                
                  
                    
                    
                      
                        ∂
                        
                          ∂
                          
                            
                              x
                              
                                i
                              
                            
                          
                        
                      
                    
                    |
                  
                  
                    
                      p
                      
                        i
                      
                      ′
                    
                  
                
                (
                
                  
                    
                      
                        x
                        ˙
                      
                    
                  
                  
                    i
                  
                
                
                  p
                  
                    i
                  
                  ′
                
                −
                
                  L
                  ′
                
                )
                =
                −
                
                  
                    
                    
                      
                        
                          ∂
                          
                            L
                            ′
                          
                        
                        
                          ∂
                          
                            
                              x
                              
                                i
                              
                            
                          
                        
                      
                    
                    |
                  
                  
                    
                      p
                      
                        i
                      
                      ′
                    
                  
                
              
            
            
              
              
                
                =
                −
                
                  
                    
                    
                      
                        
                          ∂
                          L
                        
                        
                          ∂
                          
                            
                              x
                              
                                i
                              
                            
                          
                        
                      
                    
                    |
                  
                  
                    
                      p
                      
                        i
                      
                      ′
                    
                  
                
                −
                q
                
                  
                    
                    
                      
                        ∂
                        
                          ∂
                          
                            
                              x
                              
                                i
                              
                            
                          
                        
                      
                    
                    |
                  
                  
                    
                      p
                      
                        i
                      
                      ′
                    
                  
                
                
                  
                    
                      d
                      f
                    
                    
                      d
                      t
                    
                  
                
              
            
            
              
              
                
                =
                −
                
                  
                    d
                    
                      d
                      t
                    
                  
                
                
                  (
                  
                    
                      
                        
                        
                          
                            
                              ∂
                              L
                            
                            
                              ∂
                              
                                
                                  
                                    
                                      
                                        x
                                        ˙
                                      
                                    
                                  
                                  
                                    i
                                  
                                
                              
                            
                          
                        
                        |
                      
                      
                        
                          p
                          
                            i
                          
                          ′
                        
                      
                    
                    +
                    q
                    
                      
                        
                        
                          
                            
                              ∂
                              f
                            
                            
                              ∂
                              
                                
                                  x
                                  
                                    i
                                  
                                
                              
                            
                          
                        
                        |
                      
                      
                        
                          p
                          
                            i
                          
                          ′
                        
                      
                    
                  
                  )
                
              
            
            
              
              
                
                =
                −
                
                  
                    
                      
                        p
                        ˙
                      
                    
                  
                  
                    i
                  
                  ′
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\left.{\frac {\partial H'}{\partial {x_{i}}}}\right|_{p'_{i}}&=\left.{\frac {\partial }{\partial {x_{i}}}}\right|_{p'_{i}}({\dot {x}}_{i}p'_{i}-L')=-\left.{\frac {\partial L'}{\partial {x_{i}}}}\right|_{p'_{i}}\\&=-\left.{\frac {\partial L}{\partial {x_{i}}}}\right|_{p'_{i}}-q\left.{\frac {\partial }{\partial {x_{i}}}}\right|_{p'_{i}}{\frac {df}{dt}}\\&=-{\frac {d}{dt}}\left(\left.{\frac {\partial L}{\partial {{\dot {x}}_{i}}}}\right|_{p'_{i}}+q\left.{\frac {\partial f}{\partial {x_{i}}}}\right|_{p'_{i}}\right)\\&=-{\dot {p}}'_{i}\end{aligned}}}
  

In quantum mechanics, the wave function will also undergo a local U(1) group transformation during the Gauge Transformation, which implies that all physical results must be invariant under local U(1) transformations.


== From symplectic geometry to Hamilton's equations ==


=== Geometry of Hamiltonian systems ===
The Hamiltonian can induce a symplectic structure on a smooth even-dimensional manifold M2n in several equivalent ways, the best known being the following:
As a closed nondegenerate symplectic 2-form ω. According to Darboux's theorem, in a small neighbourhood around any point on M there exist suitable local coordinates 
  
    
      
        
          p
          
            1
          
        
        ,
        ⋯
        ,
        
          p
          
            n
          
        
        ,
         
        
          q
          
            1
          
        
        ,
        ⋯
        ,
        
          q
          
            n
          
        
      
    
    {\displaystyle p_{1},\cdots ,p_{n},\ q_{1},\cdots ,q_{n}}
  
 (canonical or symplectic coordinates) in which the symplectic form becomes: 

  
    
      
        ω
        =
        
          ∑
          
            i
            =
            1
          
          
            n
          
        
        d
        
          p
          
            i
          
        
        ∧
        d
        
          q
          
            i
          
        
        
        .
      
    
    {\displaystyle \omega =\sum _{i=1}^{n}dp_{i}\wedge dq_{i}\,.}
  

The form 
  
    
      
        ω
      
    
    {\displaystyle \omega }
  
 induces a natural isomorphism of the tangent space with the cotangent space: ⁠
  
    
      
        
          T
          
            x
          
        
        M
        ≅
        
          T
          
            x
          
          
            ∗
          
        
        M
      
    
    {\displaystyle T_{x}M\cong T_{x}^{*}M}
  
⁠. This is done by mapping a vector 
  
    
      
        ξ
        ∈
        
          T
          
            x
          
        
        M
      
    
    {\displaystyle \xi \in T_{x}M}
  
 to the 1-form ⁠
  
    
      
        
          ω
          
            ξ
          
        
        ∈
        
          T
          
            x
          
          
            ∗
          
        
        M
      
    
    {\displaystyle \omega _{\xi }\in T_{x}^{*}M}
  
⁠, where 
  
    
      
        
          ω
          
            ξ
          
        
        (
        η
        )
        =
        ω
        (
        η
        ,
        ξ
        )
      
    
    {\displaystyle \omega _{\xi }(\eta )=\omega (\eta ,\xi )}
  
 for all ⁠
  
    
      
        η
        ∈
        
          T
          
            x
          
        
        M
      
    
    {\displaystyle \eta \in T_{x}M}
  
⁠. Due to the bilinearity and non-degeneracy of ⁠
  
    
      
        ω
      
    
    {\displaystyle \omega }
  
⁠, and the fact that ⁠
  
    
      
        dim
        ⁡
        
          T
          
            x
          
        
        M
        =
        dim
        ⁡
        
          T
          
            x
          
          
            ∗
          
        
        M
      
    
    {\displaystyle \dim T_{x}M=\dim T_{x}^{*}M}
  
⁠, the mapping 
  
    
      
        ξ
        →
        
          ω
          
            ξ
          
        
      
    
    {\displaystyle \xi \to \omega _{\xi }}
  
 is indeed a linear isomorphism. This isomorphism is natural in that it does not change with change of coordinates on 
  
    
      
        M
        .
      
    
    {\displaystyle M.}
  
 Repeating over all ⁠
  
    
      
        x
        ∈
        M
      
    
    {\displaystyle x\in M}
  
⁠, we end up with an isomorphism 
  
    
      
        
          J
          
            −
            1
          
        
        :
        
          Vect
        
        (
        M
        )
        →
        
          Ω
          
            1
          
        
        (
        M
        )
      
    
    {\displaystyle J^{-1}:{\text{Vect}}(M)\to \Omega ^{1}(M)}
  
 between the infinite-dimensional space of smooth vector fields and that of smooth 1-forms. For every 
  
    
      
        f
        ,
        g
        ∈
        
          C
          
            ∞
          
        
        (
        M
        ,
        
          R
        
        )
      
    
    {\displaystyle f,g\in C^{\infty }(M,\mathbb {R} )}
  
 and ⁠
  
    
      
        ξ
        ,
        η
        ∈
        
          Vect
        
        (
        M
        )
      
    
    {\displaystyle \xi ,\eta \in {\text{Vect}}(M)}
  
⁠,

  
    
      
        
          J
          
            −
            1
          
        
        (
        f
        ξ
        +
        g
        η
        )
        =
        f
        
          J
          
            −
            1
          
        
        (
        ξ
        )
        +
        g
        
          J
          
            −
            1
          
        
        (
        η
        )
        .
      
    
    {\displaystyle J^{-1}(f\xi +g\eta )=fJ^{-1}(\xi )+gJ^{-1}(\eta ).}
  

(In algebraic terms, one would say that the 
  
    
      
        
          C
          
            ∞
          
        
        (
        M
        ,
        
          R
        
        )
      
    
    {\displaystyle C^{\infty }(M,\mathbb {R} )}
  
-modules 
  
    
      
        
          Vect
        
        (
        M
        )
      
    
    {\displaystyle {\text{Vect}}(M)}
  
 and 
  
    
      
        
          Ω
          
            1
          
        
        (
        M
        )
      
    
    {\displaystyle \Omega ^{1}(M)}
  
 are isomorphic). If ⁠
  
    
      
        H
        ∈
        
          C
          
            ∞
          
        
        (
        M
        ×
        
          
            R
          
          
            t
          
        
        ,
        
          R
        
        )
      
    
    {\displaystyle H\in C^{\infty }(M\times \mathbb {R} _{t},\mathbb {R} )}
  
⁠, then, for every fixed ⁠
  
    
      
        t
        ∈
        
          
            R
          
          
            t
          
        
      
    
    {\displaystyle t\in \mathbb {R} _{t}}
  
⁠, ⁠
  
    
      
        d
        H
        ∈
        
          Ω
          
            1
          
        
        (
        M
        )
      
    
    {\displaystyle dH\in \Omega ^{1}(M)}
  
⁠, and ⁠
  
    
      
        J
        (
        d
        H
        )
        ∈
        
          Vect
        
        (
        M
        )
      
    
    {\displaystyle J(dH)\in {\text{Vect}}(M)}
  
⁠. 
  
    
      
        J
        (
        d
        H
        )
      
    
    {\displaystyle J(dH)}
  
 is known as a Hamiltonian vector field. The respective differential equation on 
  
    
      
        M
      
    
    {\displaystyle M}
  

  
    
      
        
          
            
              x
              ˙
            
          
        
        =
        J
        (
        d
        H
        )
        (
        x
        )
      
    
    {\displaystyle {\dot {x}}=J(dH)(x)}
  

is called Hamilton's equation. Here 
  
    
      
        x
        =
        x
        (
        t
        )
      
    
    {\displaystyle x=x(t)}
  
 and 
  
    
      
        J
        (
        d
        H
        )
        (
        x
        )
        ∈
        
          T
          
            x
          
        
        M
      
    
    {\displaystyle J(dH)(x)\in T_{x}M}
  
 is the (time-dependent) value of the vector field 
  
    
      
        J
        (
        d
        H
        )
      
    
    {\displaystyle J(dH)}
  
 at ⁠
  
    
      
        x
        ∈
        M
      
    
    {\displaystyle x\in M}
  
⁠.
A Hamiltonian system may be understood as a fiber bundle E over time R, with the fiber Et being the position space at time t ∈ R. The Lagrangian is thus a function on the jet bundle J over E; taking the fiberwise Legendre transform of the Lagrangian produces a function on the dual bundle over time whose fiber at t is the cotangent space T∗Et, which comes equipped with a natural symplectic form, and this latter function is the Hamiltonian. The correspondence between Lagrangian and Hamiltonian mechanics is achieved with the tautological one-form.
Any smooth real-valued function H on a symplectic manifold can be used to define a Hamiltonian system. The function H is known as "the Hamiltonian" or "the energy function." The symplectic manifold is then called the phase space. The Hamiltonian induces a special vector field on the symplectic manifold, known as the Hamiltonian vector field.
The Hamiltonian vector field induces a Hamiltonian flow on the manifold. This is a one-parameter family of transformations of the manifold (the parameter of the curves is commonly called "the time"); in other words, an isotopy of symplectomorphisms, starting with the identity. By Liouville's theorem, each symplectomorphism preserves the volume form on the phase space. The collection of symplectomorphisms induced by the Hamiltonian flow is commonly called "the Hamiltonian mechanics" of the Hamiltonian system.
The symplectic structure induces a Poisson bracket. The Poisson bracket gives the space of functions on the manifold the structure of a Lie algebra.
If F and G are smooth functions on M then the smooth function ω(J(dF), J(dG)) is properly defined; it is called a Poisson bracket of functions F and G and is denoted {F, G}. The Poisson bracket has the following properties:

bilinearity
antisymmetry
Leibniz rule: 
  
    
      
        {
        
          F
          
            1
          
        
        ⋅
        
          F
          
            2
          
        
        ,
        G
        }
        =
        
          F
          
            1
          
        
        {
        
          F
          
            2
          
        
        ,
        G
        }
        +
        
          F
          
            2
          
        
        {
        
          F
          
            1
          
        
        ,
        G
        }
      
    
    {\displaystyle \{F_{1}\cdot F_{2},G\}=F_{1}\{F_{2},G\}+F_{2}\{F_{1},G\}}
  

Jacobi identity: 
  
    
      
        {
        {
        H
        ,
        F
        }
        ,
        G
        }
        +
        {
        {
        F
        ,
        G
        }
        ,
        H
        }
        +
        {
        {
        G
        ,
        H
        }
        ,
        F
        }
        ≡
        0
      
    
    {\displaystyle \{\{H,F\},G\}+\{\{F,G\},H\}+\{\{G,H\},F\}\equiv 0}
  

non-degeneracy: if the point x on M is not critical for F then a smooth function G exists such that ⁠
  
    
      
        {
        F
        ,
        G
        }
        (
        x
        )
        ≠
        0
      
    
    {\displaystyle \{F,G\}(x)\neq 0}
  
⁠.
Given a function f

  
    
      
        
          
            
              d
            
            
              
                d
              
              t
            
          
        
        f
        =
        
          
            ∂
            
              ∂
              t
            
          
        
        f
        +
        
          {
          
            f
            ,
            
              
                H
              
            
          
          }
        
        ,
      
    
    {\displaystyle {\frac {\mathrm {d} }{\mathrm {d} t}}f={\frac {\partial }{\partial t}}f+\left\{f,{\mathcal {H}}\right\},}
  

if there is a probability distribution ρ, then (since the phase space velocity 
  
    
      
        (
        
          
            
              
                p
                ˙
              
            
          
          
            i
          
        
        ,
        
          
            
              
                q
                ˙
              
            
          
          
            i
          
        
        )
      
    
    {\displaystyle ({\dot {p}}_{i},{\dot {q}}_{i})}
  
 has zero divergence and probability is conserved) its convective derivative can be shown to be zero and so

  
    
      
        
          
            ∂
            
              ∂
              t
            
          
        
        ρ
        =
        −
        
          {
          
            ρ
            ,
            
              
                H
              
            
          
          }
        
      
    
    {\displaystyle {\frac {\partial }{\partial t}}\rho =-\left\{\rho ,{\mathcal {H}}\right\}}
  

This is called Liouville's theorem. Every smooth function G over the symplectic manifold generates a one-parameter family of symplectomorphisms and if {G, H} = 0, then G is conserved and the symplectomorphisms are symmetry transformations.
A Hamiltonian may have multiple conserved quantities Gi. If the symplectic manifold has dimension 2n and there are n functionally independent conserved quantities Gi which are in involution (i.e., {Gi, Gj} = 0), then the Hamiltonian is Liouville integrable. The Liouville–Arnold theorem says that, locally, any Liouville integrable Hamiltonian can be transformed via a symplectomorphism into a new Hamiltonian with the conserved quantities Gi as coordinates; the new coordinates are called action–angle coordinates. The transformed Hamiltonian depends only on the Gi, and hence the equations of motion have the simple form

  
    
      
        
          
            
              
                G
                ˙
              
            
          
          
            i
          
        
        =
        0
        
        ,
        
        
          
            
              
                φ
                ˙
              
            
          
          
            i
          
        
        =
        
          F
          
            i
          
        
        (
        G
        )
      
    
    {\displaystyle {\dot {G}}_{i}=0\quad ,\quad {\dot {\varphi }}_{i}=F_{i}(G)}
  

for some function F. There is an entire field focusing on small deviations from integrable systems governed by the KAM theorem.
The integrability of Hamiltonian vector fields is an open question. In general, Hamiltonian systems are chaotic; concepts of measure, completeness, integrability and stability are poorly defined.


=== Riemannian manifolds ===
An important special case consists of those Hamiltonians that are quadratic forms, that is, Hamiltonians that can be written as

  
    
      
        
          
            H
          
        
        (
        q
        ,
        p
        )
        =
        
          
            
              1
              2
            
          
        
        ⟨
        p
        ,
        p
        
          ⟩
          
            q
          
        
      
    
    {\displaystyle {\mathcal {H}}(q,p)={\tfrac {1}{2}}\langle p,p\rangle _{q}}
  

where ⟨ , ⟩q is a smoothly varying inner product on the fibers T∗qQ, the cotangent space to the point q in the configuration space, sometimes called a cometric. This Hamiltonian consists entirely of the kinetic term.
If one considers a Riemannian manifold or a pseudo-Riemannian manifold, the Riemannian metric induces a linear isomorphism between the tangent and cotangent bundles. (See Musical isomorphism). Using this isomorphism, one can define a cometric. (In coordinates, the matrix defining the cometric is the inverse of the matrix defining the metric.) The solutions to the Hamilton–Jacobi equations for this Hamiltonian are then the same as the geodesics on the manifold. In particular, the Hamiltonian flow in this case is the same thing as the geodesic flow. The existence of such solutions, and the completeness of the set of solutions, are discussed in detail in the article on geodesics. See also Geodesics as Hamiltonian flows.


=== Sub-Riemannian manifolds ===
When the cometric is degenerate, then it is not invertible. In this case, one does not have a Riemannian manifold, as one does not have a metric. However, the Hamiltonian still exists. In the case where the cometric is degenerate at every point q of the configuration space manifold Q, so that the rank of the cometric is less than the dimension of the manifold Q, one has a sub-Riemannian manifold.
The Hamiltonian in this case is known as a sub-Riemannian Hamiltonian. Every such Hamiltonian uniquely determines the cometric, and vice versa. This implies that every sub-Riemannian manifold is uniquely determined by its sub-Riemannian Hamiltonian, and that the converse is true: every sub-Riemannian manifold has a unique sub-Riemannian Hamiltonian. The existence of sub-Riemannian geodesics is given by the Chow–Rashevskii theorem.
The continuous, real-valued Heisenberg group provides a simple example of a sub-Riemannian manifold. For the Heisenberg group, the Hamiltonian is given by

  
    
      
        
          
            H
          
        
        
          (
          
            x
            ,
            y
            ,
            z
            ,
            
              p
              
                x
              
            
            ,
            
              p
              
                y
              
            
            ,
            
              p
              
                z
              
            
          
          )
        
        =
        
          
            
              1
              2
            
          
        
        
          (
          
            
              p
              
                x
              
              
                2
              
            
            +
            
              p
              
                y
              
              
                2
              
            
          
          )
        
        .
      
    
    {\displaystyle {\mathcal {H}}\left(x,y,z,p_{x},p_{y},p_{z}\right)={\tfrac {1}{2}}\left(p_{x}^{2}+p_{y}^{2}\right).}
  

pz is not involved in the Hamiltonian.


=== Poisson algebras ===
Hamiltonian systems can be generalized in various ways. Instead of simply looking at the algebra of smooth functions over a symplectic manifold, Hamiltonian mechanics can be formulated on general commutative unital real Poisson algebras. A state is a continuous linear functional on the Poisson algebra (equipped with some suitable topology) such that for any element A of the algebra, A2 maps to a nonnegative real number.
A further generalization is given by Nambu dynamics.


=== Generalization to quantum mechanics through Poisson bracket ===
Hamilton's equations above work well for classical mechanics, but not for quantum mechanics, since the differential equations discussed assume that one can specify the exact position and momentum of the particle simultaneously at any point in time. However, the equations can be further generalized to then be extended to apply to quantum mechanics as well as to classical mechanics, through the deformation of the Poisson algebra over p and q to the algebra of Moyal brackets.
Specifically, the more general form of the Hamilton's equation reads

  
    
      
        
          
            
              
                d
              
              f
            
            
              
                d
              
              t
            
          
        
        =
        
          {
          
            f
            ,
            
              
                H
              
            
          
          }
        
        +
        
          
            
              ∂
              f
            
            
              ∂
              t
            
          
        
        ,
      
    
    {\displaystyle {\frac {\mathrm {d} f}{\mathrm {d} t}}=\left\{f,{\mathcal {H}}\right\}+{\frac {\partial f}{\partial t}},}
  

where f is some function of p and q, and H is the Hamiltonian. To find out the rules for evaluating a Poisson bracket without resorting to differential equations, see Lie algebra; a Poisson bracket is the name for the Lie bracket in a Poisson algebra. These Poisson brackets can then be extended to Moyal brackets comporting to an inequivalent Lie algebra, as proven by Hilbrand J. Groenewold, and thereby describe quantum mechanical diffusion in phase space (See Phase space formulation and Wigner–Weyl transform). This more algebraic approach not only permits ultimately extending probability distributions in phase space to Wigner quasi-probability distributions, but, at the mere Poisson bracket classical setting, also provides more power in helping analyze the relevant conserved quantities in a system.


== See also ==


== References ==


== Further reading ==


== External links ==

Binney, James J., Classical Mechanics (lecture notes) (PDF), University of Oxford, retrieved 27 October 2010
Tong, David, Classical Dynamics (Cambridge lecture notes), University of Cambridge, retrieved 27 October 2010
Hamilton, William Rowan, On a General Method in Dynamics, Trinity College Dublin
Malham, Simon J.A. (2016), An introduction to Lagrangian and Hamiltonian mechanics (lecture notes) (PDF)
Morin, David (2008), Introduction to Classical Mechanics (Additional material: The Hamiltonian method) (PDF)
