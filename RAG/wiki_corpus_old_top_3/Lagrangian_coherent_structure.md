# Lagrangian coherent structure

> **Query Topic**: coherent turbulent structures (Rank #2 Search Result)
> **Source Queue**: train (Row ID: 195, Frequency: 12)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Lagrangian_coherent_structure

---

Lagrangian coherent structures (LCSs) are distinguished surfaces of trajectories in a dynamical system that exert a major influence on nearby trajectories over a time interval of interest. The type of this influence may vary, but it invariably creates a coherent trajectory pattern for which the underlying LCS serves as a theoretical centerpiece. In observations of tracer patterns in nature, one readily identifies coherent features, but it is often the underlying structure creating these features that is of interest.
As illustrated on the right, individual tracer trajectories forming coherent patterns are generally sensitive with respect to changes in their initial conditions and the system parameters. In contrast, the LCSs creating these trajectory patterns turn out to be robust and provide a simplified skeleton of the overall dynamics of the system. The robustness of this skeleton makes LCSs ideal tools for model validation, model comparison and benchmarking. LCSs can also be used for now-casting and even short-term forecasting of pattern evolution in complex dynamical systems.
Physical phenomena governed by LCSs include floating debris, oil spills, surface drifters and chlorophyll patterns in the ocean; clouds of volcanic ash and spores in the atmosphere; and coherent crowd patterns formed by humans and animals. It has been used by underwater glider for efficient ocean navigation, and is hypothesized to be used by albatross for foraging.
While LCSs generally exist in any dynamical system, their role in creating coherent patterns is perhaps most readily observable in fluid flows.


== General definitions ==


=== Material surfaces ===

On a phase space 
  
    
      
        
          
            P
          
        
      
    
    {\displaystyle {\mathcal {P}}}
  
 and over a time interval 
  
    
      
        
          
            I
          
        
        =
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle {\mathcal {I}}=[t_{0},t_{1}]}
  
 , consider a non-autonomous dynamical system defined through the flow map 
  
    
      
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
        :
        
          x
          
            0
          
        
        ↦
        x
        (
        t
        ,
        
          t
          
            0
          
        
        ,
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle F_{t_{0}}^{t}\colon x_{0}\mapsto x(t,t_{0},x_{0})}
  
, mapping initial conditions 
  
    
      
        
          x
          
            0
          
        
        ∈
        
          
            P
          
        
      
    
    {\displaystyle x_{0}\in {\mathcal {P}}}
  
 into their position 
  
    
      
        x
        (
        t
        ,
        
          t
          
            0
          
        
        ,
        
          x
          
            0
          
        
        )
        ∈
        
          
            P
          
        
      
    
    {\displaystyle x(t,t_{0},x_{0})\in {\mathcal {P}}}
  
 for any time 
  
    
      
        t
        ∈
        
          
            I
          
        
      
    
    {\displaystyle t\in {\mathcal {I}}}
  
. If the flow map 
  
    
      
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle F_{t_{0}}^{t}}
  
 is a diffeomorphism for any choice of 
  
    
      
        t
        ∈
        
          
            I
          
        
      
    
    {\displaystyle t\in {\mathcal {I}}}
  
, then for any smooth set 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{0})}
  
 of initial conditions in 
  
    
      
        
          
            P
          
        
      
    
    {\displaystyle {\mathcal {P}}}
  
, the set

  
    
      
        
          
            M
          
        
        =
        {
        (
        x
        ,
        t
        )
        ∈
        
          
            P
          
        
        ×
        
          
            I
          
        
        
        :
        [
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
        
          ]
          
            −
            1
          
        
        (
        x
        )
        ∈
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
        }
      
    
    {\displaystyle {\mathcal {M}}=\{(x,t)\in {\mathcal {P}}\times {\mathcal {I}}\,\colon [F_{t_{0}}^{t}]^{-1}(x)\in {\mathcal {M}}(t_{0})\}}
  

is an invariant manifold in the extended phase space 
  
    
      
        
          
            P
          
        
        ×
        
          
            I
          
        
      
    
    {\displaystyle {\mathcal {P}}\times {\mathcal {I}}}
  
. Borrowing terminology from fluid dynamics, we refer to the evolving time slice 
  
    
      
        
          
            M
          
        
        (
        t
        )
        =
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
        (
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
        )
      
    
    {\displaystyle {\mathcal {M}}(t)=F_{t_{0}}^{t}({\mathcal {M}}(t_{0}))}
  
 of the manifold 
  
    
      
        
          
            M
          
        
      
    
    {\displaystyle {\mathcal {M}}}
  
 as a material surface (see Fig. 1). Since any choice of the initial condition set 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{0})}
  
 yields an invariant manifold 
  
    
      
        
          
            M
          
        
        ∈
        
          
            P
          
        
        ×
        
          
            I
          
        
      
    
    {\displaystyle {\mathcal {M}}\in {\mathcal {P}}\times {\mathcal {I}}}
  
, invariant manifolds and their associated material surfaces are abundant and generally undistinguished in the extended phase space. Only few of them will act as cores of coherent trajectory patterns.


=== LCSs as exceptional material surfaces ===

In order to create a coherent pattern, a material surface 
  
    
      
        
          
            M
          
        
        (
        t
        )
      
    
    {\displaystyle {\mathcal {M}}(t)}
  
 should exert a sustained and consistent action on nearby trajectories throughout the time interval 
  
    
      
        
          
            I
          
        
      
    
    {\displaystyle {\mathcal {I}}}
  
. Examples of such action are attraction, repulsion, or shear. In principle, any well-defined mathematical property qualifies that creates coherent patterns out of randomly selected nearby initial conditions.
Most such properties can be expressed by strict inequalities. For instance, we call a material surface 
  
    
      
        
          
            M
          
        
        (
        t
        )
      
    
    {\displaystyle {\mathcal {M}}(t)}
  
 attracting over the interval 
  
    
      
        
          
            I
          
        
      
    
    {\displaystyle {\mathcal {I}}}
  
 if all small enough initial perturbations to 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{0})}
  
 are carried by the flow into even smaller final perturbations to 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            1
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{1})}
  
. In classical dynamical systems theory, invariant manifolds satisfying such an attraction property over infinite times are called attractors. They are not only special, but even locally unique in the phase space: no continuous family of attractors may exist.
In contrast, in dynamical systems defined over a finite time interval 
  
    
      
        
          
            I
          
        
      
    
    {\displaystyle {\mathcal {I}}}
  
, strict inequalities do not define exceptional (i.e., locally unique) material surfaces. This follows from the continuity of the flow map 
  
    
      
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle F_{t_{0}}^{t}}
  
 over 
  
    
      
        
          
            I
          
        
      
    
    {\displaystyle {\mathcal {I}}}
  
. For instance, if a material surface 
  
    
      
        
          
            M
          
        
        (
        t
        )
      
    
    {\displaystyle {\mathcal {M}}(t)}
  
 attracts all nearby trajectories over the time interval 
  
    
      
        
          
            I
          
        
      
    
    {\displaystyle {\mathcal {I}}}
  
, then so will any sufficiently close other material surface.
Thus, attracting, repelling and shearing material surfaces are necessarily stacked on each other, i.e., occur in continuous families. This leads to the idea of seeking LCSs in finite-time dynamical systems as exceptional material surfaces that exhibit a coherence-inducing property more strongly than any of the neighboring material surfaces. Such LCSs, defined as extrema (or more generally, stationary surfaces) for a finite-time coherence property, will indeed serve as observed centerpieces of trajectory patterns. Examples of attracting, repelling and shearing LCSs are in a direct numerical simulation of 2D turbulence are shown in Fig.2a.


=== LCSs vs. classical invariant manifolds ===
Classical invariant manifolds are invariant sets in the phase space 
  
    
      
        
          
            P
          
        
      
    
    {\displaystyle {\mathcal {P}}}
  
 of an autonomous dynamical system. In contrast,
LCSs are only required to be invariant in the extended phase space. This means that even if the underlying dynamical system is autonomous, the LCSs of the system over the interval 
  
    
      
        I
      
    
    {\displaystyle I}
  
 will generally be time-dependent, acting as the evolving skeletons of observed coherent trajectory patterns. Figure 2b shows the difference between an attracting LCS and a classic unstable manifold of a saddle point, for evolving times, in an autonomous dynamical system.


=== Objectivity of LCSs ===
Assume that the phase space of the underlying dynamical system is the material configuration space of a continuum, such as a fluid or a deformable body. For instance, for a dynamical system generated by an unsteady velocity field

  
    
      
        v
        =
        v
        (
        x
        ,
        t
        )
        ,
        
        x
        ∈
        U
        ⊂
        
          
            R
          
          
            3
          
        
        ,
      
    
    {\displaystyle v=v(x,t),\qquad x\in U\subset \mathbb {R} ^{3},}
  

the open set 
  
    
      
        U
      
    
    {\displaystyle U}
  
 of possible particle positions is a material configuration space. In this space, LCSs are material surfaces, formed by trajectories. Whether or not a material trajectory is contained in an LCS is a property that is independent of the choice of coordinates, and hence cannot depend of the observer. As a consequence, LCSs are subject to the basic objectivity (material frame-indifference) requirement of continuum mechanics. The objectivity of LCSs requires them to be invariant with respect to all possible observer changes, i.e., linear coordinate changes of the form

  
    
      
        x
        =
        Q
        (
        t
        )
        y
        +
        b
        (
        t
        )
        ,
      
    
    {\displaystyle x=Q(t)y+b(t),}
  

where 
  
    
      
        y
        ∈
        
          
            R
          
          
            3
          
        
      
    
    {\displaystyle y\in \mathbb {R} ^{3}}
  
 is the vector of the transformed coordinates; 
  
    
      
        Q
        (
        t
        )
      
    
    {\displaystyle Q(t)}
  
 is an arbitrary 
  
    
      
        3
        ×
        3
      
    
    {\displaystyle 3\times 3}
  
 proper orthogonal matrix representing time-dependent rotations; and 
  
    
      
        b
        (
        t
        )
      
    
    {\displaystyle b(t)}
  
 is an arbitrary 
  
    
      
        3
      
    
    {\displaystyle 3}
  
-dimensional vector representing time-dependent translations. As a consequence, any self-consistent LCS definition or criterion should be expressible in terms of quantities that are frame-invariant. For instance, the strain rate 
  
    
      
        S
        (
        x
        ,
        t
        )
      
    
    {\displaystyle S(x,t)}
  
 and the spin tensor 
  
    
      
        W
        (
        x
        ,
        t
        )
      
    
    {\displaystyle W(x,t)}
  
 defined as

  
    
      
        S
        (
        x
        ,
        t
        )
        =
        
          
            1
            2
          
        
        
          (
          
            ∇
            v
            (
            x
            ,
            t
            )
            +
            (
            ∇
            v
            (
            x
            ,
            t
            )
            
              )
              
                T
              
            
          
          )
        
        ,
        
        W
        (
        x
        ,
        t
        )
        =
        
          
            1
            2
          
        
        
          (
          
            ∇
            v
            (
            x
            ,
            t
            )
            −
            (
            ∇
            v
            (
            x
            ,
            t
            )
            
              )
              
                T
              
            
          
          )
        
        ,
      
    
    {\displaystyle S(x,t)={\frac {1}{2}}\left(\nabla v(x,t)+(\nabla v(x,t))^{T}\right),\qquad W(x,t)={\frac {1}{2}}\left(\nabla v(x,t)-(\nabla v(x,t))^{T}\right),}
  

transform under Euclidean changes of frame into the quantities

  
    
      
        
          
            
              S
              ~
            
          
        
        (
        y
        ,
        t
        )
        =
        Q
        (
        t
        
          )
          
            T
          
        
        S
        (
        x
        ,
        t
        )
        Q
        (
        t
        )
        ,
        
        
          
            
              W
              ~
            
          
        
        (
        y
        ,
        t
        )
        =
        Q
        (
        t
        
          )
          
            T
          
        
        W
        (
        x
        ,
        t
        )
        Q
        (
        t
        )
        −
        Q
        (
        t
        
          )
          
            T
          
        
        
          
            
              Q
              ˙
            
          
        
        (
        t
        )
        .
      
    
    {\displaystyle {\tilde {S}}(y,t)=Q(t)^{T}S(x,t)Q(t),\qquad {\tilde {W}}(y,t)=Q(t)^{T}W(x,t)Q(t)-Q(t)^{T}{\dot {Q}}(t).}
  

A Euclidean frame change is, therefore, equivalent to a similarity transform for 
  
    
      
        S
        (
        x
        ,
        t
        )
      
    
    {\displaystyle S(x,t)}
  
, and hence an LCS approach depending only on the eigenvalues and eigenvectors of 
  
    
      
        S
        (
        x
        ,
        t
        )
      
    
    {\displaystyle S(x,t)}
  
 is automatically frame-invariant. In contrast, an LCS approach depending on the eigenvalues of 
  
    
      
        W
        (
        x
        ,
        t
        )
      
    
    {\displaystyle W(x,t)}
  
 is generally not frame-invariant.
A number of frame-dependent quantities, such as 
  
    
      
        ∇
        v
        (
        x
        ,
        t
        )
      
    
    {\displaystyle \nabla v(x,t)}
  
, 
  
    
      
        
          W
        
        (
        y
        ,
        t
        )
      
    
    {\displaystyle {W}(y,t)}
  
, 
  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle \nabla F_{t_{0}}^{t}}
  
, as well as the averages or eigenvalues of these quantities, are routinely used in heuristic LCS detection. While such quantities may effectively mark features of the instantaneous velocity field 
  
    
      
        v
        (
        x
        ,
        t
        )
      
    
    {\displaystyle v(x,t)}
  
, the ability of these quantities to capture material mixing, transport, and coherence is limited and a priori unknown in any given frame. As an example, consider the linear unsteady fluid particle motion

  
    
      
        
          
            
              x
              ˙
            
          
        
        =
        v
        (
        x
        ,
        t
        )
        =
        
          
            (
            
              
                
                  sin
                  ⁡
                  
                    4
                    t
                  
                
                
                  2
                  +
                  cos
                  ⁡
                  
                    4
                    t
                  
                
              
              
                
                  −
                  2
                  +
                  cos
                  ⁡
                  
                    4
                    t
                  
                
                
                  −
                  sin
                  ⁡
                  
                    4
                    t
                  
                
              
            
            )
          
        
        x
        ,
      
    
    {\displaystyle {\dot {x}}=v(x,t)={\begin{pmatrix}\sin {4t}&2+\cos {4t}\\-2+\cos {4t}&-\sin {4t}\end{pmatrix}}x,}
  

which is an exact solution of the two-dimensional Navier–Stokes equations. The (frame-dependent) Okubo-Weiss criterion classifies the whole domain in this flow as elliptic (vortical) because 
  
    
      
        q
        =
        
          
            1
            2
          
        
        (
        
          
            |
            S
            |
          
          
            2
          
        
        −
        
          
            |
            W
            |
          
          
            2
          
        
        )
        <
        0
      
    
    {\displaystyle q={\frac {1}{2}}({\vert S\vert }^{2}-{\vert W\vert }^{2})<0}
  
 holds, with 
  
    
      
        |
        
        ⋅
        
        |
      
    
    {\displaystyle \vert \,\cdot \,\vert }
  
 referring to the Euclidean matrix norm. As seen in Fig. 3, however, trajectories grow exponentially along a rotating line and shrink exponentially along another rotating line. In material terms, therefore, the flow is hyperbolic (saddle-type) in any frame.

Since Newton's equation for particle motion and the Navier–Stokes equations for fluid motion are well known to be frame-dependent, it might first seem counterintuitive to require frame-invariance for LCSs, which are composed of solutions of these frame-dependent equations. Recall, however, that the Newton and Navier–Stokes equations represent objective physical principles for material particle trajectories. As long as correctly transformed from one frame to the other, these equations generate physically the same material trajectories in the new frame. In fact, we decide how to transform the equations of motion from an 
  
    
      
        x
      
    
    {\displaystyle x}
  
-frame to a 
  
    
      
        y
      
    
    {\displaystyle y}
  
-frame through a coordinate change 
  
    
      
        x
        =
        Q
        (
        t
        )
        y
        +
        b
        (
        t
        )
      
    
    {\displaystyle x=Q(t)y+b(t)}
  
 precisely by upholding that trajectories are mapped into trajectories, i.e., by requiring 
  
    
      
        x
        (
        t
        )
        =
        Q
        (
        t
        )
        y
        (
        t
        )
        +
        b
        (
        t
        )
      
    
    {\displaystyle x(t)=Q(t)y(t)+b(t)}
  
 to hold for all times. Temporal differentiation of this identity and substitution into the original equation in the 
  
    
      
        x
      
    
    {\displaystyle x}
  
-frame then yields the transformed equation in the 
  
    
      
        y
      
    
    {\displaystyle y}
  
-frame. While this process adds new terms (inertial forces) to the equations of motion, these inertial terms arise precisely to ensure the invariance of material trajectories. Fully composed of material trajectories, LCSs remain invariant in the transformed equation of motion defined in the 
  
    
      
        y
      
    
    {\displaystyle y}
  
-frame of reference. Consequently, any self-consistent LCS definition or detection method must also be frame-invariant.


== Hyperbolic LCSs ==

Motivated by the above discussion, the simplest way to define an attracting LCS is by requiring it to be a locally strongest attracting material surface in the extended phase space 
  
    
      
        
          
            P
          
        
        ×
        
          
            I
          
        
      
    
    {\displaystyle {\mathcal {P}}\times {\mathcal {I}}}
  
 (see. Fig. 4) . Similarly, a repelling LCS can be defined as a locally strongest repelling material surface. Attracting and repelling LCSs together are usually referred to as hyperbolic LCSs, as they provide a finite-time generalization of the classic concept of normally hyperbolic invariant manifolds in dynamical systems.


=== Diagnostic approach: Finite-time Lyapunov exponent (FTLE) ridges ===
Heuristically, one may seek initial positions 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{0})}
  
 of repelling LCSs as set of initial conditions at which infinitesimal perturbations to trajectories starting from 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{0})}
  
 grow locally at the highest rate relative to trajectories starting off of 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{0})}
  
. The heuristic element here is that instead of constructing a highly repelling material surface, one simply seeks points of large particle separation. Such a separation may well be due to strong shear along the set of points so identified; this set is not at all guaranteed to exert any normal repulsion on nearby trajectories.
The growth of an infinitesimal perturbation 
  
    
      
        
          ξ
        
        (
        t
        )
      
    
    {\displaystyle {\xi }(t)}
  
 along a trajectory 
  
    
      
        x
        (
        t
        ,
        
          t
          
            0
          
        
        ,
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle x(t,t_{0},x_{0})}
  
 is governed by the flow map gradient 
  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle \nabla F_{t_{0}}^{t}}
  
. Let 
  
    
      
        ϵ
        
          ξ
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle \epsilon {\xi }(t_{0})}
  
 be a small perturbation to the initial condition 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x_{0}}
  
, with 
  
    
      
        0
        <
        ϵ
        ≪
        1
      
    
    {\displaystyle 0<\epsilon \ll 1}
  
, and with 
  
    
      
        ξ
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle \xi (t_{0})}
  
 denoting an arbitrary unit vector in 
  
    
      
        
          
            R
          
          
            n
          
        
      
    
    {\displaystyle \mathbb {R} ^{n}}
  
. This perturbation generally grows along the trajectory 
  
    
      
        x
        (
        t
        ,
        
          t
          
            0
          
        
        ,
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle x(t,t_{0},x_{0})}
  
 into the perturbation vector 
  
    
      
        
          
            ξ
          
          
            ϵ
          
        
        (
        
          t
          
            1
          
        
        ;
        
          x
          
            0
          
        
        )
        =
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
        ϵ
        
          ξ
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle {\xi }_{\epsilon }(t_{1};x_{0})=\nabla F_{t_{0}}^{t_{1}}(x_{0})\epsilon {\xi }(t_{0})}
  
. Then the maximum relative stretching of infinitesimal perturbations at the point 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x_{0}}
  
 can be computed as

  
    
      
        
          
            
              
                
                  δ
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    
                      t
                      
                        1
                      
                    
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
              
                
                =
                
                  lim
                  
                    ϵ
                    →
                    0
                  
                
                
                  
                    1
                    ϵ
                  
                
                
                  max
                  
                    
                      |
                      
                        ξ
                        (
                        
                          t
                          
                            0
                          
                        
                        )
                      
                      |
                    
                    =
                    1
                  
                
                
                  |
                  
                    
                      ξ
                      
                        ϵ
                      
                    
                    (
                    
                      t
                      
                        1
                      
                    
                    ;
                    
                      x
                      
                        0
                      
                    
                    )
                  
                  |
                
              
            
            
              
              
                
                =
                
                  max
                  
                    
                      |
                      
                        ξ
                        (
                        
                          t
                          
                            0
                          
                        
                        )
                      
                      |
                    
                    =
                    1
                  
                
                
                  
                    
                      ⟨
                      
                        ∇
                        
                          F
                          
                            
                              t
                              
                                0
                              
                            
                          
                          
                            
                              t
                              
                                1
                              
                            
                          
                        
                        (
                        
                          x
                          
                            0
                          
                        
                        )
                        ξ
                        (
                        
                          t
                          
                            0
                          
                        
                        )
                        ,
                        ∇
                        
                          F
                          
                            
                              t
                              
                                0
                              
                            
                          
                          
                            
                              t
                              
                                1
                              
                            
                          
                        
                        (
                        
                          x
                          
                            0
                          
                        
                        )
                        ξ
                        (
                        
                          t
                          
                            0
                          
                        
                        )
                      
                      ⟩
                    
                  
                
              
            
            
              
              
                
                =
                
                  max
                  
                    
                      |
                      
                        ξ
                        (
                        
                          t
                          
                            0
                          
                        
                        )
                      
                      |
                    
                    =
                    1
                  
                
                
                  
                    
                      ⟨
                      
                        ξ
                        (
                        
                          t
                          
                            0
                          
                        
                        )
                        ,
                        
                          C
                          
                            
                              t
                              
                                0
                              
                            
                          
                          
                            
                              t
                              
                                1
                              
                            
                          
                        
                        (
                        
                          x
                          
                            0
                          
                        
                        )
                        ξ
                        (
                        
                          t
                          
                            0
                          
                        
                        )
                      
                      ⟩
                    
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\delta _{t_{0}}^{t_{1}}(x_{0})&=\lim _{\epsilon \to 0}{\frac {1}{\epsilon }}\max _{\left|\xi (t_{0})\right|=1}\left|\xi _{\epsilon }(t_{1};x_{0})\right|\\&=\max _{\left|\xi (t_{0})\right|=1}{\sqrt {\left\langle \nabla F_{t_{0}}^{t_{1}}(x_{0})\xi (t_{0}),\nabla F_{t_{0}}^{t_{1}}(x_{0})\xi (t_{0})\right\rangle }}\\&=\max _{\left|\xi (t_{0})\right|=1}{\sqrt {\left\langle \xi (t_{0}),C_{t_{0}}^{t_{1}}(x_{0})\xi (t_{0})\right\rangle }}\\\end{aligned}}}
  

where 
  
    
      
        
          C
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        =
        
          
            [
            
              ∇
              
                F
                
                  
                    t
                    
                      0
                    
                  
                
                
                  
                    t
                    
                      1
                    
                  
                
              
            
            ]
          
          
            T
          
        
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle C_{t_{0}}^{t_{1}}=\left[\nabla F_{t_{0}}^{t_{1}}\right]^{T}\nabla F_{t_{0}}^{t_{1}}}
  
 denotes the right Cauchy–Green strain tensor. One then concludes that the maximum relative stretching experienced along a trajectory starting from 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x_{0}}
  
 is just 
  
    
      
        
          δ
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
        =
        
          
            
              λ
              
                n
              
            
            (
            
              x
              
                0
              
            
            )
          
        
      
    
    {\displaystyle \delta _{t_{0}}^{t_{1}}(x_{0})={\sqrt {\lambda _{n}(x_{0})}}}
  
. As this relative stretching tends to grow rapidly, it is more convenient to work with its growth exponent 
  
    
      
        (
        log
        ⁡
        
          
            δ
            
              
                t
                
                  0
                
              
            
            
              
                t
                
                  1
                
              
            
          
        
        )
        
          /
        
        (
        
          t
          
            1
          
        
        −
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle (\log {\delta _{t_{0}}^{t_{1}}})/(t_{1}-t_{0})}
  
, which is then precisely the finite-time Lyapunov exponent (FTLE)

  
    
      
        
          
            F
            T
            L
            E
          
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
        =
        
          
            1
            
              2
              (
              
                t
                
                  1
                
              
              −
              
                t
                
                  0
                
              
              )
            
          
        
        log
        ⁡
        
          λ
          
            n
          
        
        (
        
          x
          
            0
          
        
        )
        .
      
    
    {\displaystyle \mathrm {FTLE} _{t_{0}}^{t_{1}}(x_{0})={\frac {1}{2(t_{1}-t_{0})}}\log \lambda _{n}(x_{0}).}
  

Therefore, one expects hyperbolic LCSs to appear as codimension-one local maximizing surfaces (or ridges) of the FTLE field.
This expectation turns out to be justified in the majority of cases: time 
  
    
      
        
          t
          
            0
          
        
      
    
    {\displaystyle t_{0}}
  
 positions of repelling LCSs are marked by ridges of 
  
    
      
        
          
            F
            T
            L
            E
          
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \mathrm {FTLE} _{t_{0}}^{t_{1}}(x_{0})}
  
. By applying the same argument in backward time,
we obtain that time 
  
    
      
        
          t
          
            1
          
        
      
    
    {\displaystyle t_{1}}
  
 positions of attracting LCSs are marked by ridges of the backward FTLE field 
  
    
      
        
          
            F
            T
            L
            E
          
          
            
              t
              
                1
              
            
          
          
            
              t
              
                0
              
            
          
        
      
    
    {\displaystyle \mathrm {FTLE} _{t_{1}}^{t_{0}}}
  
.
The classic way of computing Lyapunov exponents is solving a linear differential equation for the linearized flow map 
  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \nabla F_{t_{0}}^{t}(x_{0})}
  
. A more expedient approach is to compute the FTLE field from a simple finite-difference approximation to the deformation gradient.
For example, in a three-dimensional flow, we launch a trajectory 
  
    
      
        x
        (
        t
        ;
        
          t
          
            0
          
        
        ,
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle x(t;t_{0},x_{0})}
  
 from any element 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x_{0}}
  
 of a grid of initial conditions. Using the coordinate representation 
  
    
      
        x
        =
        (
        
          x
          
            1
          
        
        ,
        
          x
          
            2
          
        
        ,
        
          x
          
            3
          
        
        )
      
    
    {\displaystyle x=(x^{1},x^{2},x^{3})}
  
 for the evolving trajectory 
  
    
      
        x
        (
        t
        ;
        
          t
          
            0
          
        
        ,
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle x(t;t_{0},x_{0})}
  
, we approximate the gradient of the flow map as

  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
        (
        
          x
          
            0
          
        
        )
        ≈
        
          
            (
            
              
                
                  
                    
                      
                        
                          x
                          
                            1
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            1
                          
                        
                        )
                        −
                        
                          x
                          
                            1
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            1
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              1
                            
                          
                        
                        |
                      
                    
                  
                
                
                  
                    
                      
                        
                          x
                          
                            1
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            2
                          
                        
                        )
                        −
                        
                          x
                          
                            1
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            2
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              2
                            
                          
                        
                        |
                      
                    
                  
                
                
                  
                    
                      
                        
                          x
                          
                            1
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            3
                          
                        
                        )
                        −
                        
                          x
                          
                            1
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            3
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              3
                            
                          
                        
                        |
                      
                    
                  
                
              
              
                
                  
                    
                      
                        
                          x
                          
                            2
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            1
                          
                        
                        )
                        −
                        
                          x
                          
                            2
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            1
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              1
                            
                          
                        
                        |
                      
                    
                  
                
                
                  
                    
                      
                        
                          x
                          
                            2
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            2
                          
                        
                        )
                        −
                        
                          x
                          
                            2
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            2
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              2
                            
                          
                        
                        |
                      
                    
                  
                
                
                  
                    
                      
                        
                          x
                          
                            2
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            3
                          
                        
                        )
                        −
                        
                          x
                          
                            2
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            3
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              3
                            
                          
                        
                        |
                      
                    
                  
                
              
              
                
                  
                    
                      
                        
                          x
                          
                            3
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            1
                          
                        
                        )
                        −
                        
                          x
                          
                            3
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            1
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              1
                            
                          
                        
                        |
                      
                    
                  
                
                
                  
                    
                      
                        
                          x
                          
                            3
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            2
                          
                        
                        )
                        −
                        
                          x
                          
                            3
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            2
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              2
                            
                          
                        
                        |
                      
                    
                  
                
                
                  
                    
                      
                        
                          x
                          
                            3
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        +
                        
                          δ
                          
                            3
                          
                        
                        )
                        −
                        
                          x
                          
                            3
                          
                        
                        (
                        t
                        ;
                        
                          t
                          
                            0
                          
                        
                        ,
                        
                          x
                          
                            0
                          
                        
                        −
                        
                          δ
                          
                            3
                          
                        
                        )
                      
                      
                        |
                        
                          2
                          
                            δ
                            
                              3
                            
                          
                        
                        |
                      
                    
                  
                
              
            
            )
          
        
        ,
      
    
    {\displaystyle \nabla F_{t_{0}}^{t}(x_{0})\approx {\begin{pmatrix}{\frac {x^{1}(t;t_{0},x_{0}+\delta _{1})-x^{1}(t;t_{0},x_{0}-\delta _{1})}{\left|2\delta _{1}\right|}}&{\frac {x^{1}(t;t_{0},x_{0}+\delta _{2})-x^{1}(t;t_{0},x_{0}-\delta _{2})}{\left|2\delta _{2}\right|}}&{\frac {x^{1}(t;t_{0},x_{0}+\delta _{3})-x^{1}(t;t_{0},x_{0}-\delta _{3})}{\left|2\delta _{3}\right|}}\\{\frac {x^{2}(t;t_{0},x_{0}+\delta _{1})-x^{2}(t;t_{0},x_{0}-\delta _{1})}{\left|2\delta _{1}\right|}}&{\frac {x^{2}(t;t_{0},x_{0}+\delta _{2})-x^{2}(t;t_{0},x_{0}-\delta _{2})}{\left|2\delta _{2}\right|}}&{\frac {x^{2}(t;t_{0},x_{0}+\delta _{3})-x^{2}(t;t_{0},x_{0}-\delta _{3})}{\left|2\delta _{3}\right|}}\\{\frac {x^{3}(t;t_{0},x_{0}+\delta _{1})-x^{3}(t;t_{0},x_{0}-\delta _{1})}{\left|2\delta _{1}\right|}}&{\frac {x^{3}(t;t_{0},x_{0}+\delta _{2})-x^{3}(t;t_{0},x_{0}-\delta _{2})}{\left|2\delta _{2}\right|}}&{\frac {x^{3}(t;t_{0},x_{0}+\delta _{3})-x^{3}(t;t_{0},x_{0}-\delta _{3})}{\left|2\delta _{3}\right|}}\end{pmatrix}},}
  

with a small vector 
  
    
      
        
          δ
          
            i
          
        
      
    
    {\displaystyle \delta _{i}}
  
 pointing in the 
  
    
      
        
          x
          
            i
          
        
      
    
    {\displaystyle x^{i}}
  
 coordinate direction. For two-dimensional flows, only the first 
  
    
      
        2
        ×
        2
      
    
    {\displaystyle 2\times 2}
  
 minor matrix of the above matrix is relevant.


==== Issues with inferring hyperbolic LCSs from FTLE ridges ====
FTLE ridges have proven to be a simple and efficient tool for the visualize hyperbolic LCSs in a number of physical problems, yielding intriguing images of initial positions of hyperbolic LCSs in different applications (see, e.g., Figs. 5a-b). However, FTLE ridges obtained over sliding time windows 
  
    
      
        [
        
          t
          
            0
          
        
        +
        T
        ,
        
          t
          
            1
          
        
        +
        T
        ]
      
    
    {\displaystyle [t_{0}+T,t_{1}+T]}
  
 do not form material surfaces. Thus, ridges of 
  
    
      
        
          
            F
            T
            L
            E
          
          
            
              t
              
                0
              
            
            +
            T
          
          
            
              t
              
                1
              
            
            +
            T
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \mathrm {FTLE} _{t_{0}+T}^{t_{1}+T}(x_{0})}
  
 under varying 
  
    
      
        T
      
    
    {\displaystyle T}
  
 cannot be used to define Lagrangian objects, such as hyperbolic LCSs. Indeed, a locally strongest repelling material surface over 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
 will generally not play the same role over 
  
    
      
        [
        
          t
          
            0
          
        
        +
        T
        ,
        
          t
          
            1
          
        
        +
        T
        ]
      
    
    {\displaystyle [t_{0}+T,t_{1}+T]}
  
 and hence its evolving position at time 
  
    
      
        
          t
          
            0
          
        
        +
        T
      
    
    {\displaystyle t_{0}+T}
  
 will not be a ridge for 
  
    
      
        
          
            F
            T
            L
            E
          
          
            
              t
              
                0
              
            
            +
            T
          
          
            
              t
              
                1
              
            
            +
            T
          
        
      
    
    {\displaystyle \mathrm {FTLE} _{t_{0}+T}^{t_{1}+T}}
  
. Nonetheless, evolving second-derivative FTLE ridges computed over sliding intervals of the form 
  
    
      
        [
        
          t
          
            0
          
        
        +
        T
        ,
        
          t
          
            1
          
        
        +
        T
        ]
      
    
    {\displaystyle [t_{0}+T,t_{1}+T]}
  
 have been identified by some authors broadly with LCSs. In support of this identification, it is also often argued that the material flux over such sliding-window FTLE ridges should necessarily be small.
The "FTLE ridge=LCS" identification, however, suffers form the following conceptual and mathematical problems:

Second-derivative FTLE ridges are necessarily straight lines and hence do not exist in physical problems.
FTLE ridges computed over sliding time windows 
  
    
      
        [
        
          t
          
            0
          
        
        +
        T
        ,
        
          t
          
            1
          
        
        +
        T
        ]
      
    
    {\displaystyle [t_{0}+T,t_{1}+T]}
  
 with a varying 
  
    
      
        T
      
    
    {\displaystyle T}
  
 are generally not Lagrangian and the flux through them is generally not small.
In particular, a broadly referenced material flux formula for FTLE ridges is incorrect, even for straight FTLE ridges
FTLE ridges mark hyperbolic LCS positions, but also highlight surfaces of high shear. A convoluted mixture of both types of surfaces often arises in applications (see Fig. 6 for an example).
There are several other types LCSs (elliptic and parabolic) beyond the hyperbolic LCSs highlighted by FTLE ridges


=== Local variational approach: Shrink and stretch surfaces ===
The local variational theory of hyperbolic LCSs builds on their original definition as strongest repelling or repelling material surfaces in the flow over the time interval 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
. At an initial point 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x_{0}}
  
 , let 
  
    
      
        
          n
          
            0
          
        
      
    
    {\displaystyle n_{0}}
  

denote a unit normal to an initial material surface 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{0})}
  
 (cf. Fig. 7). By the invariance of material lines, the tangent space 
  
    
      
        
          T
          
            
              x
              
                0
              
            
          
        
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle T_{x_{0}}{\mathcal {M}}(t_{0})}
  
 is mapped into the tangent space of 
  
    
      
        
          T
          
            
              x
              
                1
              
            
          
        
        
          
            M
          
        
        (
        
          t
          
            1
          
        
        )
      
    
    {\displaystyle T_{x_{1}}{\mathcal {M}}(t_{1})}
  

by the linearized flow map 
  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \nabla F_{t_{0}}^{t_{1}}(x_{0})}
  
. At the same time, the image of the normal 
  
    
      
        
          n
          
            0
          
        
      
    
    {\displaystyle n_{0}}
  
 normal under 
  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \nabla F_{t_{0}}^{t_{1}}(x_{0})}
  
 generally does not remain normal to 
  
    
      
        
          
            M
          
        
        (
        
          t
          
            1
          
        
        )
      
    
    {\displaystyle {\mathcal {M}}(t_{1})}
  
.
Therefore, in addition to a normal component of length 
  
    
      
        
          ρ
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
            ,
          
        
        
          n
          
            0
          
        
        )
      
    
    {\displaystyle \rho _{t_{0}}^{t_{1}}(x_{0,}n_{0})}
  
, the advected normal also develops a tangential component of length 
  
    
      
        
          σ
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        ,
        
          n
          
            0
          
        
        )
      
    
    {\displaystyle \sigma _{t_{0}}^{t_{1}}(x_{0},n_{0})}
  
 (cf. Fig. 7).

If 
  
    
      
        
          ρ
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        ,
        
          n
          
            0
          
        
        )
        >
        1
      
    
    {\displaystyle \rho _{t_{0}}^{t_{1}}(x_{0},n_{0})>1}
  
, then the evolving material surface 
  
    
      
        
          
            M
          
        
        (
        t
        )
      
    
    {\displaystyle {\mathcal {M}}(t)}
  
 strictly repels nearby trajectories by the end of the time interval 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
. Similarly, 
  
    
      
        
          ρ
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        ,
        
          n
          
            0
          
        
        )
        <
        1
      
    
    {\displaystyle \rho _{t_{0}}^{t_{1}}(x_{0},n_{0})<1}
  

signals that 
  
    
      
        
          
            M
          
        
        (
        t
        )
      
    
    {\displaystyle {\mathcal {M}}(t)}
  
 strictly attracts nearby trajectories along its normal directions. A repelling (attracting) LCS over the interval 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
 can be defined as a material surface 
  
    
      
        
          
            M
          
        
        (
        t
        )
      
    
    {\displaystyle {\mathcal {M}}(t)}
  
 whose net repulsion 
  
    
      
        
          ρ
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        ,
        
          n
          
            0
          
        
        )
      
    
    {\displaystyle \rho _{t_{0}}^{t_{1}}(x_{0},n_{0})}
  
 is pointwise maximal (minimal) with respect to perturbations
of the initial normal vector field 
  
    
      
        
          n
          
            0
          
        
      
    
    {\displaystyle n_{0}}
  
. As earlier, we refer to repelling and attracting LCSs collectively as hyperbolic LCSs.
Solving these local extremum principles for hyperbolic LCSs in two and three dimensions yields unit normal vector fields to which hyperbolic LCSs should everywhere be tangent. The existence of such normal surfaces also requires a Frobenius-type integrability condition in the three-dimensional case. All these results can be summarized as follows:

Repelling LCSs are obtained as most repelling shrink lines, starting from local maxima of 
  
    
      
        
          λ
          
            2
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \lambda _{2}(x_{0})}
  
. Attracting LCSs are obtained as most attracting stretch lines, starting from local minima of 
  
    
      
        
          λ
          
            1
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \lambda _{1}(x_{0})}
  
. These starting points serve are initial positions of exceptional saddle-type trajectories in the flow. An example of the local variational computation of a repelling LCS is shown in FIg. 8. The computational algorithm is available in LCS Tool.

In 3D flows, instead of solving the Frobenius PDE (see table above) for hyperbolic LCSs, an easier approach is to construct intersections of hyperbolic LCSs with select 2D planes, and fit a surface numerically to a large number of such intersection curves. Let us denote the unit normal of a 2D plane 
  
    
      
        Π
      
    
    {\displaystyle \Pi }
  
 by 
  
    
      
        
          n
          
            Π
          
        
      
    
    {\displaystyle n_{\Pi }}
  
. The intersection curve of a 2D repelling LCS surface with the plane 
  
    
      
        Π
      
    
    {\displaystyle \Pi }
  
 is normal to both 
  
    
      
        
          n
          
            Π
          
        
      
    
    {\displaystyle n_{\Pi }}
  
 and to the unit normal 
  
    
      
        
          ξ
          
            3
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \xi _{3}(x_{0})}
  
 of the LCS. As a consequence, an intersection curve 
  
    
      
        
          x
          
            0
          
        
        (
        s
        )
      
    
    {\displaystyle x_{0}(s)}
  
 satisfies the ODE

  
    
      
        
          x
          
            0
          
          
            ′
          
        
        =
        
          ξ
          
            3
          
        
        (
        
          x
          
            0
          
        
        )
        ×
        
          n
          
            Π
          
        
        ,
      
    
    {\displaystyle x_{0}^{\prime }=\xi _{3}(x_{0})\times n_{\Pi },}
  

whose trajectories we refer to as reduced shrink lines. (Strictly speaking, this equation is not an ordinary differential equation, given that its right-hand side is not a vector field, but a direction field, which is generally not globally orientable). Intersections of hyperbolic LCSs with 
  
    
      
        Π
      
    
    {\displaystyle \Pi }
  
 are fastest contracting reduced shrink lines. Determining such shrink lines in a smooth family of nearby 
  
    
      
        Π
      
    
    {\displaystyle \Pi }
  
 planes, then fitting a surface to the curve family so obtained yields a numerical approximation of a 2D repelling LCS.


=== Global variational approach: Shrink- and stretchlines as null-geodesics ===
A general material surface experiences shear and strain in its deformation, both of which depend continuously on initial conditions by the continuity of the map 
  
    
      
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle F_{t_{0}}^{t}}
  
.
The averaged strain and shear within a strip of 
  
    
      
        
          
            O
          
        
        (
        ϵ
        )
      
    
    {\displaystyle {\mathcal {O}}(\epsilon )}
  
-close material lines, therefore, typically show 
  
    
      
        
          
            O
          
        
        (
        ϵ
        )
      
    
    {\displaystyle {\mathcal {O}}(\epsilon )}
  
 variation within such a strip.
The two-dimensional geodesic theory of LCSs seeks exceptionally coherent locations where this general trend fails, resulting in an order of magnitude smaller variability in shear or strain than what is normally expected across an 
  
    
      
        
          
            O
          
        
        (
        ϵ
        )
      
    
    {\displaystyle {\mathcal {O}}(\epsilon )}
  
 strip. Specifically, the geodesic theory searches for LCSs as special material lines around which 
  
    
      
        
          
            O
          
        
        (
        ϵ
        )
      
    
    {\displaystyle {\mathcal {O}}(\epsilon )}
  
 material strips show no 
  
    
      
        
          
            O
          
        
        (
        ϵ
        )
      
    
    {\displaystyle {\mathcal {O}}(\epsilon )}
  
 variability either in the material-line
averaged shear (Shearless LCSs) or in the material-line averaged strain (Strainless or Elliptic LCSs). Such LCSs turn out to be null-geodesics of appropriate metric tensors defined by the deformation field—hence the name of this theory.
Shearless LCSs are found to be null-geodesics of a Lorentzian metric tensor 
  
    
      
        
          D
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle D_{t_{0}}^{t_{1}}}
  
 defined as

  
    
      
        
          D
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
        =
        
          
            1
            2
          
        
        
          [
          
            
              C
              
                
                  t
                  
                    0
                  
                
              
              
                
                  t
                  
                    1
                  
                
              
            
            (
            
              x
              
                0
              
            
            )
            Ω
            −
            Ω
            
              C
              
                
                  t
                  
                    0
                  
                
              
              
                
                  t
                  
                    1
                  
                
              
            
            (
            
              x
              
                0
              
            
            )
          
          ]
        
        ,
        
        Ω
        =
        
          
            (
            
              
                
                  0
                
                
                  −
                  1
                
              
              
                
                  1
                
                
                  0
                
              
            
            )
          
        
        .
      
    
    {\displaystyle D_{t_{0}}^{t_{1}}(x_{0})={\frac {1}{2}}\left[C_{t_{0}}^{t_{1}}(x_{0})\Omega -\Omega C_{t_{0}}^{t_{1}}(x_{0})\right],\qquad \Omega ={\begin{pmatrix}0&-1\\1&0\\\end{pmatrix}}.}
  

Such null-geodesics can be proven to be tensorlines of the Cauchy–Green strain tensor, i.e., are tangent to the direction field formed by the strain eigenvector fields 
  
    
      
        
          ξ
          
            i
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \xi _{i}(x_{0})}
  
. Specifically, repelling LCSs are trajectories of 
  
    
      
        
          x
          
            0
          
          
            ′
          
        
        =
        
          ξ
          
            1
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle x_{0}^{\prime }=\xi _{1}(x_{0})}
  
 starting from local maxima of the 
  
    
      
        
          λ
          
            2
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \lambda _{2}(x_{0})}
  
 eigenvalue field. Similarly, attracting LCSs are trajectories of 
  
    
      
        
          x
          
            0
          
          
            ′
          
        
        =
        
          ξ
          
            2
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle x_{0}^{\prime }=\xi _{2}(x_{0})}
  
 starting from local minims of the 
  
    
      
        
          λ
          
            1
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \lambda _{1}(x_{0})}
  
 eigenvalue field. This agrees with the conclusion of the local variational theory of LCSs. The geodesic approach, however, also sheds more light on the robustness of hyperbolic LCSs: hyperbolic LCSs only prevail as stationary curves of the averaged shear functional under variations that leave their endpoints fixed. This is to be contrasted with parabolic LCSs (see below), which are also shearless LCSs but prevail as stationary curves to the shear functional even under arbitrary variations. As a consequence, individual trajectories are objective, and statements about the coherent structures they form should also be objective.
A sample application is shown in Fig. 9, where the sudden appearance of a hyperbolic core (strongest attracting part of a stretchline) within the oil spill caused the notable Tiger-Tail instability in the shape of the oil spill.


== Elliptic LCSs ==
Elliptc LCSs are closed and nested material surfaces that act as building blocks of the Lagrangian equivalents of vortices, i.e., rotation-dominated regions of trajectories that generally traverse the phase space without substantial stretching or folding. They mimic the behavior of Kolmogorov–Arnold–Moser (KAM) tori that form elliptic regions in Hamiltonian systems. There coherence can be approached either through their homogeneous material rotation or through their homogeneous stretching properties.


=== Rotational coherence from the polar rotation angle (PRA) ===
As a simplest approach to rotational coherence, one may define an elliptic LCS as a tubular material surface along which small material volumes complete the same net rotation over the time intervall 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
 of interest.
A challenge in that in each material volume element, all individual material fibers (tangent vectors to trajectories) perform different rotations.
To obtain a well-defined bulk rotation for each material element, one may employ the unique left and right polar decompositions of the flow gradient in the form

  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        =
        
          R
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        
          U
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        =
        
          V
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        
          R
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        ,
      
    
    {\displaystyle \nabla F_{t_{0}}^{t_{1}}=R_{t_{0}}^{t_{1}}U_{t_{0}}^{t_{1}}=V_{t_{0}}^{t_{1}}R_{t_{0}}^{t_{1}},}
  

where the proper orthogonal tensor 
  
    
      
        
          R
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle R_{t_{0}}^{t_{1}}}
  
 is called the rotation tensor and the symmetric, positive definite tensors 
  
    
      
        
          U
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        ,
        
          V
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle U_{t_{0}}^{t_{1}},V_{t_{0}}^{t_{1}}}
  
 are called the left stretch tensor and right stretch tensor, respectively.
Since the Cauchy–Green strain tensor can be written as

  
    
      
        
          C
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        =
        [
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        
          ]
          
            T
          
        
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        =
        
          U
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        
          U
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        =
        
          V
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        
          V
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        ,
      
    
    {\displaystyle C_{t_{0}}^{t_{1}}=[\nabla F_{t_{0}}^{t_{1}}]^{T}\nabla F_{t_{0}}^{t_{1}}=U_{t_{0}}^{t_{1}}U_{t_{0}}^{t_{1}}=V_{t_{0}}^{t_{1}}V_{t_{0}}^{t_{1}},}
  

the local material straining described by the eigenvalues and eigenvectors of 
  
    
      
        
          C
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle C_{t_{0}}^{t_{1}}}
  
 are fully captured by the singular values and singular vectors of the stretch tensors. The remaining factor in the deformation gradient is represented by 
  
    
      
        
          R
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle R_{t_{0}}^{t_{1}}}
  
, interpreted as the bulk solid-body rotation component of volume elements. In planar motions, this rotation is defined relative to the normal of the plane. In three dimensions, the rotation is defined relative to the axis defined by the eigenvector of 
  
    
      
        
          R
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle R_{t_{0}}^{t_{1}}}
  
 corresponding to its unit eigenvalue. In higher-dimensional flows, the rotation tensor cannot be viewed as a rotation about a single axis.

In two and three dimensions, therefore, there exists a polar rotation angle (PRA) 
  
    
      
        
          θ
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \theta _{t_{0}}^{t_{1}}(x_{0})}
  
 that characterises the material rotation generated by 
  
    
      
        
          R
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle R_{t_{0}}^{t_{1}}}
  
 for a volume element centered at the initial condition 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x_{0}}
  
. This PRA is well-defined up to multiples of 
  
    
      
        2
        π
      
    
    {\displaystyle 2\pi }
  
. For two-dimensional flows, the PRA can be computed from the invariants of 
  
    
      
        
          C
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle C_{t_{0}}^{t_{1}}}
  
 using the formulas

  
    
      
        
          
            
              
                cos
                ⁡
                
                  θ
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    
                      t
                      
                        1
                      
                    
                  
                
              
              
                
                =
                
                  
                    
                      ⟨
                      
                        ξ
                        
                          i
                        
                      
                      ,
                      ∇
                      
                        F
                        
                          
                            t
                            
                              0
                            
                          
                        
                        
                          
                            t
                            
                              1
                            
                          
                        
                      
                      
                        ξ
                        
                          i
                        
                      
                      ⟩
                    
                    
                      
                        λ
                        
                          i
                        
                      
                    
                  
                
                ,
                
                i
                =
                1
                
                
                o
                r
                
                
                
                2
                ,
              
            
            
              
                sin
                ⁡
                
                  θ
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    
                      t
                      
                        1
                      
                    
                  
                
              
              
                
                =
                
                  
                    (
                    
                      −
                      1
                    
                    )
                  
                  
                    j
                  
                
                
                  
                    
                      ⟨
                      
                        ξ
                        
                          i
                        
                      
                      ,
                      ∇
                      
                        F
                        
                          
                            t
                            
                              0
                            
                          
                        
                        
                          
                            t
                            
                              1
                            
                          
                        
                      
                      
                        ξ
                        
                          j
                        
                      
                      ⟩
                    
                    
                      
                        λ
                        
                          j
                        
                      
                    
                  
                
                ,
                
                (
                i
                ,
                j
                )
                =
                (
                1
                ,
                2
                )
                
                
                o
                r
                
                
                (
                2
                ,
                1
                )
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\cos \theta _{t_{0}}^{t_{1}}&={\frac {\langle \xi _{i},\nabla F_{t_{0}}^{t_{1}}\xi _{i}\rangle }{\sqrt {\lambda _{i}}}},\quad i=1\,\,or\,\,\,2,\\\sin \theta _{t_{0}}^{t_{1}}&=\left(-1\right)^{j}{\frac {\langle \xi _{i},\nabla F_{t_{0}}^{t_{1}}\xi _{j}\rangle }{\sqrt {\lambda _{j}}}},\qquad (i,j)=(1,2)\,\,or\,\,(2,1),\\\end{aligned}}}
  

which yield a four-quadrant version of the PRA via the formula

  
    
      
        
          θ
          
            
              t
              
                0
              
            
          
          
            t
          
        
        =
        
          [
          
            1
            −
            
              
                s
                i
                g
                n
                
              
            
            
              (
              
                sin
                ⁡
                
                  θ
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    t
                  
                
              
              )
            
          
          ]
        
        π
        +
        
          
            s
            i
            g
            n
            
          
        
        
          (
          
            sin
            ⁡
            
              θ
              
                
                  t
                  
                    0
                  
                
              
              
                t
              
            
          
          )
        
        
          cos
          
            −
            1
          
        
        ⁡
        
          (
          
            cos
            ⁡
            
              θ
              
                
                  t
                  
                    0
                  
                
              
              
                t
              
            
          
          )
        
        .
      
    
    {\displaystyle \theta _{t_{0}}^{t}=\left[1-{\rm {sign\,}}\left(\sin \theta _{t_{0}}^{t}\right)\right]\pi +{\rm {sign\,}}\left(\sin \theta _{t_{0}}^{t}\right)\cos ^{-1}\left(\cos \theta _{t_{0}}^{t}\right).}
  

For three-dimensional flows, the PRA can again be computed from the invariants of 
  
    
      
        
          C
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle C_{t_{0}}^{t_{1}}}
  
 from the formulas

  
    
      
        
          
            
              
                cos
                ⁡
                
                  θ
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    t
                  
                
              
              
                
                =
                
                  
                    1
                    2
                  
                
                
                  (
                  
                    
                      ∑
                      
                        i
                        =
                        1
                      
                      
                        3
                      
                    
                    
                      
                        
                          ⟨
                          
                            
                              ξ
                              
                                i
                              
                            
                            ,
                            ∇
                            
                              F
                              
                                
                                  t
                                  
                                    0
                                  
                                
                              
                              
                                
                                  t
                                  
                                    1
                                  
                                
                              
                            
                            
                              ξ
                              
                                i
                              
                            
                          
                          ⟩
                        
                        
                          
                            λ
                            
                              i
                            
                          
                        
                      
                    
                    −
                    1
                  
                  )
                
                ,
              
            
            
              
                sin
                ⁡
                
                  θ
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    t
                  
                
              
              
                
                =
                
                  
                    
                      
                        ⟨
                        
                          
                            ξ
                            
                              i
                            
                          
                          ,
                          ∇
                          
                            F
                            
                              
                                t
                                
                                  0
                                
                              
                            
                            
                              
                                t
                                
                                  1
                                
                              
                            
                          
                          
                            ξ
                            
                              j
                            
                          
                        
                        ⟩
                      
                      −
                      
                        ⟨
                        
                          
                            ξ
                            
                              j
                            
                          
                          ,
                          ∇
                          
                            F
                            
                              
                                t
                                
                                  0
                                
                              
                            
                            
                              
                                t
                                
                                  1
                                
                              
                            
                          
                          
                            ξ
                            
                              i
                            
                          
                        
                        ⟩
                      
                    
                    
                      2
                      
                        ϵ
                        
                          i
                          j
                          k
                        
                      
                      
                        e
                        
                          k
                        
                      
                    
                  
                
                ,
                
                i
                ≠
                j
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\cos \theta _{t_{0}}^{t}&={\frac {1}{2}}\left(\sum _{i=1}^{3}{\frac {\left\langle \xi _{i},\nabla F_{t_{0}}^{t_{1}}\xi _{i}\right\rangle }{\sqrt {\lambda _{i}}}}-1\right),\\\sin \theta _{t_{0}}^{t}&={\frac {\left\langle \xi _{i},\nabla F_{t_{0}}^{t_{1}}\xi _{j}\right\rangle -\left\langle \xi _{j},\nabla F_{t_{0}}^{t_{1}}\xi _{i}\right\rangle }{2\epsilon _{ijk}e_{k}}},\qquad i\neq j,\end{aligned}}}
  

where 
  
    
      
        
          ϵ
          
            i
            j
            k
          
        
      
    
    {\displaystyle \epsilon _{ijk}}
  
 is the Levi-Civita symbol, 
  
    
      
        
          e
        
        =
        
          {
          
            e
            
              k
            
          
          }
        
      
    
    {\displaystyle \mathbf {e} =\left\{e_{k}\right\}}
  
 is the eigenvector corresponding to the unit eigenvector of the matrix 
  
    
      
        
          
            [
            
              K
              
                
                  t
                  
                    0
                  
                
              
              
                t
              
            
            ]
          
          
            j
            k
          
        
        =
        
          ⟨
          
            
              ξ
              
                j
              
            
            ,
            ∇
            
              F
              
                
                  t
                  
                    0
                  
                
              
              
                
                  t
                  
                    1
                  
                
              
            
            
              ξ
              
                k
              
            
          
          ⟩
        
        
          /
        
        
          
            
              λ
              
                k
              
            
          
        
      
    
    {\displaystyle \left[K_{t_{0}}^{t}\right]_{jk}=\left\langle \xi _{j},\nabla F_{t_{0}}^{t_{1}}\xi _{k}\right\rangle /{\sqrt {\lambda _{k}}}}
  
.
The time 
  
    
      
        
          t
          
            0
          
        
      
    
    {\displaystyle t_{0}}
  
 positions of elliptic LCSs are visualized as tubular level sets of the PRA distribution 
  
    
      
        
          θ
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle \theta _{t_{0}}^{t}}
  
. In two-dimensions, therefore, (polar) elliptic LCSs are simply closed level curves of the PRA, which turn out to be objective. In three dimensions, (polar) elliptic LCSs are toroidal or cylindrical level surfaces of the PRA, which are, however, not objective and hence will generally change in rotating frames. Coherent Lagrangian vortex boundaries can be visualized as outermost members of nested families of elliptic LCSs. Two- and three-dimensional examples of elliptic LCS revealed by tubular level surfaces of the PRA are shown in Fig. 10a-b.


=== Rotational coherence from the Lagrangian-averaged vorticity deviation (LAVD) ===
The level sets of the PRA are objective in two dimensions but not in three dimensions. An additional shortcoming of the polar rotation tensor is its dynamical inconsistency: polar rotations computed over adjacent sub-intervals of a total deformation do not sum up to the rotation computed for the full-time interval of the same deformation. Therefore, while 
  
    
      
        
          R
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle R_{t_{0}}^{t_{1}}}
  
 is the closest rotation tensor to 
  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle \nabla F_{t_{0}}^{t_{1}}}
  
 in the 
  
    
      
        
          L
          
            2
          
        
      
    
    {\displaystyle L^{2}}
  
 norm over a fixed time interval 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
, these piecewise best fits do not form a family of rigid-body rotations as 
  
    
      
        
          t
          
            0
          
        
      
    
    {\displaystyle t_{0}}
  
 and 
  
    
      
        
          t
          
            1
          
        
      
    
    {\displaystyle t_{1}}
  
 are varied. For this reason, rotations predicted by the polar rotation tensor over varying time intervals divert from the experimentally observed mean material rotation of fluid elements.

An alternative to the classic polar decomposition provides a resolution to both the non-objectivity and the dynamic inconsistency issue. Specifically, the Dynamic Polar Decomposition (DPD) of the deformation gradient is also of the form

  
    
      
        ∇
        
          F
          
            
              t
              
                0
              
            
          
          
            t
          
        
        =
        
          O
          
            
              t
              
                0
              
            
          
          
            t
          
        
        
          M
          
            
              t
              
                0
              
            
          
          
            t
          
        
        =
        
          N
          
            
              t
              
                0
              
            
          
          
            t
          
        
        
          O
          
            
              t
              
                0
              
            
          
          
            t
          
        
        ,
      
    
    {\displaystyle \nabla F_{t_{0}}^{t}=O_{t_{0}}^{t}M_{t_{0}}^{t}=N_{t_{0}}^{t}O_{t_{0}}^{t},}
  

where the proper orthogonal tensor 
  
    
      
        
          O
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle O_{t_{0}}^{t}}
  
 is the dynamic rotation tensor and the non-singular tensors 
  
    
      
        
          M
          
            
              t
              
                0
              
            
          
          
            t
          
        
        ,
        
          N
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle M_{t_{0}}^{t},N_{t_{0}}^{t}}
  
 are the left dynamic stretch tensor and right dynamic stretch tensor, respectively. Just as the classic polar decomposition, the DPD is valid in any finite dimension. Unlike the classic polar decomposition, however, the dynamic rotation and stretch tensors are obtained from solving linear differential equations, rather than from matrix manipulations. In particular, 
  
    
      
        
          O
          
            
              t
              
                0
              
            
          
          
            t
          
        
        =
        
          ∇
          
            
              a
              
                0
              
            
          
        
        a
        (
        t
        )
      
    
    {\displaystyle O_{t_{0}}^{t}=\nabla _{a_{0}}a(t)}
  
 is the deformation gradient of the purely rotational flow

  
    
      
        
          
            
              a
              ˙
            
          
        
        =
        W
        
          (
          
            x
            (
            t
            ;
            
              x
              
                0
              
            
            )
            ,
            t
          
          )
        
        a
        ,
      
    
    {\displaystyle {\dot {a}}=W\left(x(t;x_{0}),t\right)a,}
  

and 
  
    
      
        
          M
          
            
              t
              
                0
              
            
          
          
            t
          
        
        =
        
          ∇
          
            
              b
              
                0
              
            
          
        
        b
        (
        t
        )
      
    
    {\displaystyle M_{t_{0}}^{t}=\nabla _{b_{0}}b(t)}
  
 is the deformation gradient of the purely straining flow

  
    
      
        
          
            
              b
              ˙
            
          
        
        =
        
          O
          
            t
          
          
            
              t
              
                0
              
            
          
        
        S
        
          (
          
            x
            (
            t
            ;
            
              x
              
                0
              
            
            )
            ,
            t
          
          )
        
        
          O
          
            
              t
              
                0
              
            
          
          
            t
          
        
        b
        .
      
    
    {\displaystyle {\dot {b}}=O_{t}^{t_{0}}S\left(x(t;x_{0}),t\right)O_{t_{0}}^{t}b.}
  
.
The dynamic rotation tensor 
  
    
      
        
          O
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle O_{t_{0}}^{t}}
  
 can further be factorized into two deformation gradients: one for a spatially uniform (rigid-body) rotation, and one that deviates from this uniform rotation:

  
    
      
        
          O
          
            
              t
              
                0
              
            
          
          
            t
          
        
        =
        
          Φ
          
            
              t
              
                0
              
            
          
          
            t
          
        
        
          Θ
          
            
              t
              
                0
              
            
          
          
            t
          
        
        .
      
    
    {\displaystyle O_{t_{0}}^{t}=\Phi _{t_{0}}^{t}\Theta _{t_{0}}^{t}.}
  

As a spatially independent rigid-body rotation, the proper orthogonal relative rotation tensor 
  
    
      
        
          Φ
          
            
              t
              
                0
              
            
          
          
            t
          
        
        =
        
          ∂
          
            
              α
              
                0
              
            
          
        
        α
        (
        t
        )
      
    
    {\displaystyle \Phi _{t_{0}}^{t}=\partial _{\alpha _{0}}\alpha (t)}
  
 is dynamically consistent, serving as the deformation gradient of the relative rotation flow

  
    
      
        
          
            
              α
              ˙
            
          
        
        =
        
          [
          
            W
            
              (
              
                x
                (
                t
                ;
                
                  x
                  
                    0
                  
                
                )
                ,
                t
              
              )
            
            −
            
              
                
                  W
                  ¯
                
              
            
            
              (
              t
              )
            
          
          ]
        
        α
        .
      
    
    {\displaystyle {\dot {\alpha }}=\left[W\left(x(t;x_{0}),t\right)-{\bar {W}}\left(t\right)\right]\alpha .}
  

In contrast, the proper orthogonal mean rotation tensor 
  
    
      
        
          Θ
          
            
              t
              
                0
              
            
          
          
            t
          
        
        =
        
          D
          
            
              β
              
                0
              
            
          
        
        β
        (
        t
        )
      
    
    {\displaystyle \Theta _{t_{0}}^{t}=D_{\beta _{0}}\beta (t)}
  
 is the deformation gradient of the mean-rotation flow

  
    
      
        
          
            
              β
              ˙
            
          
        
        =
        
          Φ
          
            t
          
          
            
              t
              
                0
              
            
          
        
        
          
            
              W
              ¯
            
          
        
        
          (
          t
          )
        
        
          Φ
          
            
              t
              
                0
              
            
          
          
            t
          
        
        β
        .
      
    
    {\displaystyle {\dot {\beta }}=\Phi _{t}^{t_{0}}{\bar {W}}\left(t\right)\Phi _{t_{0}}^{t}\beta .}
  

The dynamic consistency of 
  
    
      
        
          Φ
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle \Phi _{t_{0}}^{t}}
  
 implies that the total angle swept by 
  
    
      
        
          Φ
          
            
              t
              
                0
              
            
          
          
            t
          
        
      
    
    {\displaystyle \Phi _{t_{0}}^{t}}
  
 around its own axis of rotation is dynamically consistent. This intrinsic rotation angle 
  
    
      
        
          ψ
          
            
              t
              
                0
              
            
          
          
            t
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \psi _{t_{0}}^{t}(x_{0})}
  
 is also objective, and turns out to equal to one half of the Lagrangian-averaged vorticity deviation (LAVD). The LAVD is defined as the trajectory-averaged magnitude of the deviation of the vorticity from its spatial mean. With the vorticity 
  
    
      
        ω
        (
        x
        ,
        t
        )
        =
        ∇
        ×
        v
        (
        x
        ,
        t
        )
      
    
    {\displaystyle \omega (x,t)=\nabla \times v(x,t)}
  
 and its spatial mean

  
    
      
        
          
            
              ω
              ¯
            
          
        
        (
        t
        )
        =
        
          
            
              
                ∫
                
                  U
                  (
                  t
                  )
                
              
              ω
              (
              x
              ,
              t
              )
              
              d
              V
            
            
              
                v
                o
                l
              
              
              (
              U
              (
              t
              )
              )
            
          
        
        ,
      
    
    {\displaystyle {\bar {\omega }}(t)={\frac {\int _{U(t)}\omega (x,t)\,dV}{\mathrm {vol} \,(U(t))}},}
  

the LAVD over a time interval 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
 therefore takes the form

  
    
      
        
          
            L
            A
            V
            D
          
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
        :=
        
          ∫
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        
          |
          
            ω
            (
            x
            (
            s
            ;
            
              x
              
                0
              
            
            )
            ,
            s
            )
            −
            
              
                
                  ω
                  ¯
                
              
            
            (
            s
            )
          
          |
        
        
        d
        s
        ,
      
    
    {\displaystyle \mathrm {LAVD} _{t_{0}}^{t_{1}}(x_{0}):=\int _{t_{0}}^{t_{1}}\left|\omega (x(s;x_{0}),s)-{\bar {\omega }}(s)\right|\,ds,}
  

with 
  
    
      
        U
        (
        t
        )
      
    
    {\displaystyle U(t)}
  
 denoting the (possibly time-varying) domain of definition of the velocity field 
  
    
      
        v
        (
        x
        ,
        t
        )
      
    
    {\displaystyle v(x,t)}
  
. This result applies both in two- and three dimensions, and enables the computation of a well-defined, objective and dynamically consistent material rotation angle along any trajectory.

Outermost complex tubular level curves of the LAVD define initial positions of rotationally coherent material vortex boundaries in two-dimensional unsteady flows (see Fig. 11a). By construction, these boundaries may exhibit transverse filamentation, but any developing filament keeps rotating with the boundary, without global transverse departure form the material vortex. (Exceptions are inviscid flows where such a global departure of LAVD level surfaces from a vortex is possible as fluid elements preserve their material rotation rate for all times). Remarkably, centers of rotationally coherent vortices (defined by local maxima of the LAVD field) can be proven to be the observed centers of attraction or repulsion for finite-size (inertial) particle motion in geophysical flows (see Fig. 11b). In three-dimensional flows, tubular level surfaces of the LAVD define initial positions of two-dimensional eddy boundary surfaces (see Fig. 11c) that remain rotationally coherent over a time intcenter|erval 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
 (see Fig. 11d).


=== Stretching-based coherence from a local variational approach: Shear surfaces ===
The local variational theory of elliptic LCSs targets material surfaces that locally maximize material shear over the finite time interval 
  
    
      
        [
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        ]
      
    
    {\displaystyle [t_{0},t_{1}]}
  
 of interest. This means that at initial point each point 
  
    
      
        
          x
          
            0
          
        
        ∈
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle x_{0}\in {\mathcal {M}}(t_{0})}
  
 of an elliptic LCS 
  
    
      
        
          
            M
          
        
        (
        t
        )
      
    
    {\displaystyle {\mathcal {M}}(t)}
  
, the tangent space 
  
    
      
        
          T
          
            
              x
              
                0
              
            
          
        
        
          
            M
          
        
        (
        
          t
          
            0
          
        
        )
      
    
    {\displaystyle T_{x_{0}}{\mathcal {M}}(t_{0})}
  
 is the plane along which the local Lagrangian shear 
  
    
      
        
          σ
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \sigma _{t_{0}}^{t_{1}}(x_{0})}
  
 is maximal (cf. Fig 7).
Introducing the two-dimensional shear vector field

  
    
      
        
          η
          
            ±
          
        
        (
        
          x
          
            0
          
        
        )
        :=
        
          
            
              
                
                  λ
                  
                    2
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
                −
                1
              
              
                
                  λ
                  
                    2
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
                −
                
                  λ
                  
                    1
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
            
          
        
        
          ξ
          
            1
          
        
        (
        
          x
          
            0
          
        
        )
        ±
        
          
            
              
                1
                −
                
                  λ
                  
                    1
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
              
                
                  λ
                  
                    2
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
                −
                
                  λ
                  
                    1
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
            
          
        
        
          ξ
          
            2
          
        
        (
        
          x
          
            0
          
        
        )
        ,
      
    
    {\displaystyle \eta ^{\pm }(x_{0}):={\sqrt {\frac {\lambda _{2}(x_{0})-1}{\lambda _{2}(x_{0})-\lambda _{1}(x_{0})}}}\xi _{1}(x_{0})\pm {\sqrt {\frac {1-\lambda _{1}(x_{0})}{\lambda _{2}(x_{0})-\lambda _{1}(x_{0})}}}\xi _{2}(x_{0}),}
  

and the three-dimensional shear normal vector field

  
    
      
        
          n
          
            ±
          
        
        (
        
          x
          
            0
          
        
        )
        =
        
          
            
              
                
                  λ
                  
                    1
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
              
                
                  
                    
                      λ
                      
                        1
                      
                    
                    (
                    
                      x
                      
                        0
                      
                    
                    )
                  
                
                +
                
                  
                    
                      λ
                      
                        3
                      
                    
                    (
                    
                      x
                      
                        0
                      
                    
                    )
                  
                
              
            
          
        
        
          ξ
          
            1
          
        
        (
        
          x
          
            0
          
        
        )
        ±
        
          
            
              
                
                  λ
                  
                    3
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
              
                
                  
                    
                      λ
                      
                        1
                      
                    
                    (
                    
                      x
                      
                        0
                      
                    
                    )
                  
                
                +
                
                  
                    
                      λ
                      
                        3
                      
                    
                    (
                    
                      x
                      
                        0
                      
                    
                    )
                  
                
              
            
          
        
        
          ξ
          
            3
          
        
        (
        
          x
          
            0
          
        
        )
        ,
      
    
    {\displaystyle n_{\pm }(x_{0})={\sqrt {\frac {\sqrt {\lambda _{1}(x_{0})}}{{\sqrt {\lambda _{1}(x_{0})}}+{\sqrt {\lambda _{3}(x_{0})}}}}}\xi _{1}(x_{0})\pm {\sqrt {\frac {\sqrt {\lambda _{3}(x_{0})}}{{\sqrt {\lambda _{1}(x_{0})}}+{\sqrt {\lambda _{3}(x_{0})}}}}}\xi _{3}(x_{0}),}
  

the criteria for two- and three-dimensional elliptic LCSs can be summarized as follows:

For 3D flows, as in the case of hyperbolic LCSs, solving the Frobenius PDE can be avoided. Instead, one can construct intersections of a tubular elliptic LCS with select 2D planes, and fit a surface numerically to a large number of these intersection curves. As for hyperbolic LCSs above, let us denote the unit normal of a 2D plane 
  
    
      
        Π
      
    
    {\displaystyle \Pi }
  
 by 
  
    
      
        
          n
          
            Π
          
        
      
    
    {\displaystyle n_{\Pi }}
  
. Again, the intersection curves of elliptic LCSs with the plane 
  
    
      
        Π
      
    
    {\displaystyle \Pi }
  
 are normal to both 
  
    
      
        
          n
          
            Π
          
        
      
    
    {\displaystyle n_{\Pi }}
  
 and to the unit normal 
  
    
      
        
          n
          
            ±
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle n_{\pm }(x_{0})}
  
 of the LCS. As a consequence, an intersection curve 
  
    
      
        
          x
          
            0
          
        
        (
        s
        )
      
    
    {\displaystyle x_{0}(s)}
  
 satisfies the reduced shear ODE

  
    
      
        
          x
          
            0
          
          
            ′
          
        
        =
        
          n
          
            ±
          
        
        (
        
          x
          
            0
          
        
        )
        ×
        
          n
          
            Π
          
        
        ,
      
    
    {\displaystyle x_{0}^{\prime }=n_{\pm }(x_{0})\times n_{\Pi },}
  

whose trajectories we refer to as reduced shear lines. (Strictly speaking, the reduced shear ODE is not an ordinary differential equation, given that its right-hand side is not a vector field, but a direction field, which is generally not globally orientable). Intersections of tubular elliptic LCSs with 
  
    
      
        Π
      
    
    {\displaystyle \Pi }
  
 are limit cycles of the reduced shear ODE. Determining such limit cycles in a smooth family of nearby 
  
    
      
        Π
      
    
    {\displaystyle \Pi }
  
 planes, then fitting a surface to the limit cycle family yields a numerical approximation for 2D shear surface. A three-dimensional example of this local variational computation of an elliptic LCS is shown in Fig. 11.


=== Stretching-based coherence from a global variational approach: lambda-lines ===

As noted above under hyperbolic LCSs, a global variational approach has been developed in two dimensions to capture elliptic LCSs as closed stationary curves of the material-line-averaged Lagrangian strain functional. Such curves turn out to be closed null-geodesics of the generalized Green–Lagrange strain tensor family 
  
    
      
        
          
            1
            2
          
        
        (
        
          C
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        −
        λ
        I
        )
      
    
    {\displaystyle {\frac {1}{2}}(C_{t_{0}}^{t_{1}}-\lambda I)}
  
, where 
  
    
      
        λ
        >
        0
      
    
    {\displaystyle \lambda >0}
  
 is a positive parameter (Lagrange multiplier). The closed null-geodesics can be shown to coincide with limit cycles of the family of direction fields

  
    
      
        
          η
          
            λ
          
          
            ±
          
        
        (
        
          x
          
            0
          
        
        )
        :=
        
          
            
              
                
                  λ
                  
                    2
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
                −
                
                  λ
                  
                    2
                  
                
              
              
                
                  λ
                  
                    2
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
                −
                
                  λ
                  
                    1
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
            
          
        
        
          ξ
          
            1
          
        
        (
        
          x
          
            0
          
        
        )
        ±
        
          
            
              
                
                  λ
                  
                    2
                  
                
                −
                
                  λ
                  
                    1
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
              
                
                  λ
                  
                    2
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
                −
                
                  λ
                  
                    1
                  
                
                (
                
                  x
                  
                    0
                  
                
                )
              
            
          
        
        
          ξ
          
            2
          
        
        (
        
          x
          
            0
          
        
        )
        ,
      
    
    {\displaystyle \eta _{\lambda }^{\pm }(x_{0}):={\sqrt {\frac {\lambda _{2}(x_{0})-\lambda ^{2}}{\lambda _{2}(x_{0})-\lambda _{1}(x_{0})}}}\xi _{1}(x_{0})\pm {\sqrt {\frac {\lambda ^{2}-\lambda _{1}(x_{0})}{\lambda _{2}(x_{0})-\lambda _{1}(x_{0})}}}\xi _{2}(x_{0}),}
  

Note that for 
  
    
      
        λ
        =
        1
      
    
    {\displaystyle \lambda =1}
  
, the direction field 
  
    
      
        
          η
          
            λ
          
          
            ±
          
        
        (
        
          x
          
            0
          
        
      
    
    {\displaystyle \eta _{\lambda }^{\pm }(x_{0}}
  
 coincides with the direction field 
  
    
      
        
          η
          
            ±
          
        
        (
        
          x
          
            0
          
        
      
    
    {\displaystyle \eta ^{\pm }(x_{0}}
  
 for shearlines obtained above from the local variational theory of LCSs.
Trajectories of 
  
    
      
        
          η
          
            λ
          
          
            ±
          
        
      
    
    {\displaystyle \eta _{\lambda }^{\pm }}
  
 are referred to as 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
-lines. Remarkably, they are initial positions of material lines that are infinitesimally uniformly stretching under the flow map 
  
    
      
        
          F
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle F_{t_{0}}^{t_{1}}}
  
. Specifically, any subset of a 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
-line is stretched by a factor of 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
 between the times 
  
    
      
        
          t
          
            0
          
        
      
    
    {\displaystyle t_{0}}
  
 and 
  
    
      
        
          t
          
            1
          
        
      
    
    {\displaystyle t_{1}}
  
. As an example, Fig. 13 shows elliptic LCSs identified as closed 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
-lines within the Great Red Spot of Jupiter.


== Parabolic LCSs ==
Parabolic LCSs are shearless material surfaces that delineate cores of jet-type sets of trajectories. Such LCSs are characterized by both low stretching (because they are inside a non-stretching structure), but also by low shearing (because material shearing is minimal in jet cores).


=== Diagnostic approach: Finite-time Lyapunov exponents (FTLE) trenches ===
Since both shearing and stretching are as low as possible along a parabolic LCS, one may seek initial positions of such material surfaces as trenches of the FTLE field 
  
    
      
        F
        T
        L
        
          E
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle FTLE_{t_{0}}^{t_{1}}(x_{0})}
  
. A geophysical example of a parabolic LCS (generalized jet core) revealed as a trench of the FTLE field is shown in Fig. 14a.


=== Global variational approach: Heteroclinic chains of null-geodesics ===
In two dimensions, parabolic LCSs are also solutions of the global shearless variational principle described above for hyperbolic LCSs. As such, parabolic LCSs are composed of shrink lines and stretch lines that represent geodesics of the Lorentzian metric tensor 
  
    
      
        
          D
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
      
    
    {\displaystyle D_{t_{0}}^{t_{1}}}
  
. In contrast to hyperbolic LCSs, however, parabolic LCSs satisfy more robust boundary conditions: they remain stationary curves of the material-line-averaged shear functional even under variations to their endpoints. This explains the high degree of robustness and observability that jet cores exhibit in mixing. This is to be contrasted with the highly sensitive and fading footprint of hyperbolic LCSs away from strongly hyperbolic regions in diffusive tracer patterns.
Under variable endpoint boundary conditions, initial positions of parabolic LCSs turn out to be alternating chains of shrink lines and stretch lines that connect singularities of these line fields. These singularities occur at points where 
  
    
      
        
          λ
          
            1
          
        
        (
        
          x
          
            0
          
        
        )
        =
        
          λ
          
            2
          
        
        (
        
          x
          
            0
          
        
        )
      
    
    {\displaystyle \lambda _{1}(x_{0})=\lambda _{2}(x_{0})}
  
, and hence no infinitesimal deformation takes place between the two time instances 
  
    
      
        
          t
          
            0
          
        
      
    
    {\displaystyle t_{0}}
  
 and 
  
    
      
        
          t
          
            1
          
        
      
    
    {\displaystyle t_{1}}
  
. Fig. 14b shows an example of parabolic LCSs in Jupiter's atmosphere, located using this variational theory. The chevron-type shapes forming out of circular material blobs positioned along the jet core is characteristic of tracer deformation near parabolic LCSs. 


== Software packages for LCS computations ==
Particle advection and Finite-Time Lyapunov Exponent calculation:

ManGen (source code)
LCS MATLAB Kit (source code)
FlowVC (source code)
cuda_ftle (source code)
CTRAJ
Newman (source code)
FlowTK (source code)
Jupyter notebooks that guide you through methods used to extract advective, diffusive, stochastic and active transport barriers from discrete velocity data.

TBarrier (source code)


== See also ==
Turbulence
Chaos theory
Dynamical systems theory
Spectral submanifold
Eulerian coherent structure
Coherent turbulent structure


== References ==


== Further reading ==

Salman, H.; Hesthaven, J. S.; Warburton, T.; Haller, G. (2006). "Predicting transport by Lagrangian coherent structures with a high-order method". Theoretical and Computational Fluid Dynamics. 21 (1): 39–58. Bibcode:2007ThCFD..21...39S. doi:10.1007/s00162-006-0031-0. S2CID 11159109.
Green, M. A.; Rowley, C. W.; Haller, G. (2007). "Detection of Lagrangian coherent structures in three-dimensional turbulence". Journal of Fluid Mechanics. 572: 111–120. Bibcode:2007JFM...572..111G. CiteSeerX 10.1.1.506.7756. doi:10.1017/S0022112006003648. S2CID 1074531.
