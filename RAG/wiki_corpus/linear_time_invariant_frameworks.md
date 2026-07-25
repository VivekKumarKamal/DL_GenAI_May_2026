# Invariant extended Kalman filter

> **Query Topic**: linear time-invariant frameworks (Rank #1 Search Result)  
> **Source Queue**: train (Row ID: 15, Frequency: 6)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Invariant_extended_Kalman_filter

---

The invariant extended Kalman filter (IEKF) (not to be confused with the iterated extended Kalman filter) was first introduced as a version of the extended Kalman filter (EKF) for nonlinear systems possessing symmetries (or invariances), then generalized and recast as an adaptation to Lie groups of the linear Kalman filtering theory. Instead of using a linear correction term based on a linear output error, the IEKF uses a geometrically adapted correction term based on an invariant output error; in the same way the gain matrix is not updated from a linear state error, but from an invariant state error. The main benefit is that the gain and covariance equations have reduced dependence on the estimated value of the state. In some cases they converge to constant values on a much bigger set of trajectories than is the case for the EKF, which results in a better convergence of the estimation.


== Filter derivation ==


=== Discrete-time framework ===
Consider a system whose state is encoded at time step 
  
    
      
        n
      
    
    {\displaystyle n}
  
 by an element 
  
    
      
        
          x
          
            n
          
        
      
    
    {\displaystyle x_{n}}
  
 of a Lie group 
  
    
      
        G
      
    
    {\displaystyle G}
  
 and dynamics has the following shape:

  
    
      
        
          x
          
            n
          
        
        =
        
          ϕ
          
            n
          
        
        (
        
          x
          
            n
            −
            1
          
        
        )
        ⋅
        
          u
          
            n
          
        
      
    
    {\displaystyle x_{n}=\phi _{n}(x_{n-1})\cdot u_{n}}
  

where 
  
    
      
        
          ϕ
          
            n
          
        
      
    
    {\displaystyle \phi _{n}}
  
 is a group automorphism of 
  
    
      
        G
      
    
    {\displaystyle G}
  
, 
  
    
      
        ⋅
      
    
    {\displaystyle \cdot }
  
 is the group operation and  
  
    
      
        
          u
          
            n
          
        
      
    
    {\displaystyle u_{n}}
  
 an element of  
  
    
      
        G
      
    
    {\displaystyle G}
  
. The system is supposed to be observed through a measurement  
  
    
      
        
          y
          
            n
          
        
      
    
    {\displaystyle y_{n}}
  
 having the following shape:

  
    
      
        
          y
          
            n
          
        
        =
        
          x
          
            n
          
        
        ∗
        
          b
          
            n
          
        
      
    
    {\displaystyle y_{n}=x_{n}*b_{n}}
  

where  
  
    
      
        
          b
          
            n
          
        
      
    
    {\displaystyle b_{n}}
  
 belongs to a vector space 
  
    
      
        
          
            Y
          
        
      
    
    {\displaystyle {\mathcal {Y}}}
  
 endowed with a left action of the elements of  
  
    
      
        G
      
    
    {\displaystyle G}
  
 denoted again by  
  
    
      
        ∗
      
    
    {\displaystyle *}
  
 (which cannot create confusion with the group operation as the second member of the operation is an element of 
  
    
      
        
          
            Y
          
        
      
    
    {\displaystyle {\mathcal {Y}}}
  
, not 
  
    
      
        G
      
    
    {\displaystyle G}
  
). Alternatively, the same theory applies to a measurement defined by a right action:

  
    
      
        
          y
          
            n
          
        
        =
        
          b
          
            n
          
        
        ∗
        
          x
          
            n
          
        
      
    
    {\displaystyle y_{n}=b_{n}*x_{n}}
  


=== Filter equations ===
The invariant extended Kalman filter is an observer 
  
    
      
        
          
            
              
                x
                ^
              
            
          
          
            n
          
        
      
    
    {\displaystyle {\hat {x}}_{n}}
  
 defined by the following equations if the measurement function is a left action:

  
    
      
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
            −
            1
          
        
        =
        
          ϕ
          
            n
          
        
        (
        
          
            
              
                x
                ^
              
            
          
          
            n
            −
            1
            
              |
            
            n
            −
            1
          
        
        )
        ⋅
        
          u
          
            n
          
        
      
    
    {\displaystyle {\hat {x}}_{n|n-1}=\phi _{n}({\hat {x}}_{n-1|n-1})\cdot u_{n}}
  

  
    
      
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
          
        
        =
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
            −
            1
          
        
        ⋅
        exp
        ⁡
        (
        
          K
          
            n
          
        
        (
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
            −
            1
          
          
            −
            1
          
        
        ∗
        
          y
          
            n
          
        
        −
        
          b
          
            n
          
        
        )
        )
      
    
    {\displaystyle {\hat {x}}_{n|n}={\hat {x}}_{n|n-1}\cdot \exp(K_{n}({\hat {x}}_{n|n-1}^{-1}*y_{n}-b_{n}))}
  

where 
  
    
      
        exp
        ⁡
        (
        )
      
    
    {\displaystyle \exp()}
  
 is the exponential map of 
  
    
      
        G
      
    
    {\displaystyle G}
  
 and 
  
    
      
        
          K
          
            n
          
        
      
    
    {\displaystyle K_{n}}
  
 is a gain matrix to be tuned through a Riccati equation.
If measurement function is a right action then the update state is defined as:

  
    
      
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
          
        
        =
        exp
        ⁡
        (
        
          K
          
            n
          
        
        (
        
          y
          
            n
          
        
        ∗
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
            −
            1
          
          
            −
            1
          
        
        −
        
          b
          
            n
          
        
        )
        )
        ⋅
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
            −
            1
          
        
      
    
    {\displaystyle {\hat {x}}_{n|n}=\exp(K_{n}(y_{n}*{\hat {x}}_{n|n-1}^{-1}-b_{n}))\cdot {\hat {x}}_{n|n-1}}
  


=== Continuous-time framework ===
The discrete-time framework above was first introduced for continuous-time dynamics of the shape:

  
    
      
        
          
            d
            
              d
              t
            
          
        
        
          x
          
            t
          
        
        =
        
          f
          
            t
          
        
        (
        
          x
          
            t
          
        
        )
        ,
      
    
    {\displaystyle {\frac {d}{dt}}x_{t}=f_{t}(x_{t}),}
  

where the vector field 
  
    
      
        
          f
          
            t
          
        
      
    
    {\displaystyle f_{t}}
  
 verifies at any time 
  
    
      
        t
      
    
    {\displaystyle t}
  
 the relation:

  
    
      
        ∀
        a
        ,
        b
        ∈
        G
        ,
        
          f
          
            t
          
        
        (
        a
        ⋅
        b
        )
        =
        
          f
          
            t
          
        
        (
        a
        )
        b
        +
        a
        
          f
          
            t
          
        
        (
        b
        )
        −
        a
        f
        (
        I
        d
        )
        b
      
    
    {\displaystyle \forall a,b\in G,f_{t}(a\cdot b)=f_{t}(a)b+af_{t}(b)-af(Id)b}
  

where the identity element of the group is denoted by 
  
    
      
        I
        d
      
    
    {\displaystyle Id}
  
 and is used the short-hand notation 
  
    
      
        g
        u
        =
        
          L
          
            g
          
        
        (
        u
        )
      
    
    {\displaystyle gu=L_{g}(u)}
  
 (resp. 
  
    
      
        u
        g
        =
        
          R
          
            g
          
        
        (
        u
        )
      
    
    {\displaystyle ug=R_{g}(u)}
  
) for the left translation 
  
    
      
        
          L
          
            g
          
        
        :
        T
        
          G
          
            x
          
        
        →
        T
        
          G
          
            g
            x
          
        
      
    
    {\displaystyle L_{g}:TG_{x}\rightarrow TG_{gx}}
  
 (resp. the right translation 
  
    
      
        
          R
          
            g
          
        
        :
        T
        
          G
          
            x
          
        
        →
        T
        
          G
          
            x
            g
          
        
      
    
    {\displaystyle R_{g}:TG_{x}\rightarrow TG_{xg}}
  
) where 
  
    
      
        T
        
          G
          
            x
          
        
      
    
    {\displaystyle TG_{x}}
  
 denotes the tangent space to 
  
    
      
        G
      
    
    {\displaystyle G}
  
 at 
  
    
      
        x
      
    
    {\displaystyle x}
  
. It leads to more involved computations than the discrete-time framework, but properties are similar.


== Main properties ==
The main benefit of invariant extended Kalman filtering is the behavior of the invariant error variable, whose definition depends on the type of measurement. For left actions we define a left-invariant error variable as:

  
    
      
        
          e
          
            n
            
              |
            
            n
            −
            1
          
          
            L
          
        
        =
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
            −
            1
          
          
            −
            1
          
        
        
          x
          
            n
          
        
      
    
    {\displaystyle e_{n|n-1}^{L}={\hat {x}}_{n|n-1}^{-1}x_{n}}
  
,

  
    
      
        
          e
          
            n
            
              |
            
            n
          
          
            L
          
        
        =
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
          
          
            −
            1
          
        
        
          x
          
            n
          
        
      
    
    {\displaystyle e_{n|n}^{L}={\hat {x}}_{n|n}^{-1}x_{n}}
  
,
while for right actions we define a right-invariant error variable as:

  
    
      
        
          e
          
            n
            
              |
            
            n
            −
            1
          
          
            R
          
        
        =
        
          x
          
            n
          
        
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
            −
            1
          
          
            −
            1
          
        
      
    
    {\displaystyle e_{n|n-1}^{R}=x_{n}{\hat {x}}_{n|n-1}^{-1}}
  
,

  
    
      
        
          e
          
            n
            
              |
            
            n
          
          
            R
          
        
        =
        
          x
          
            n
          
        
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
          
          
            −
            1
          
        
      
    
    {\displaystyle e_{n|n}^{R}=x_{n}{\hat {x}}_{n|n}^{-1}}
  
,
Indeed, replacing 
  
    
      
        
          x
          
            n
          
        
      
    
    {\displaystyle x_{n}}
  
, 
  
    
      
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
            −
            1
          
        
      
    
    {\displaystyle {\hat {x}}_{n|n-1}}
  
, 
  
    
      
        
          
            
              
                x
                ^
              
            
          
          
            n
            
              |
            
            n
          
        
      
    
    {\displaystyle {\hat {x}}_{n|n}}
  
 by their values we obtain for left actions, after some algebra:

  
    
      
        
          e
          
            n
            
              |
            
            n
            −
            1
          
          
            L
          
        
        =
        
          u
          
            n
          
          
            −
            1
          
        
        ⋅
        
          ϕ
          
            n
          
        
        (
        
          e
          
            n
            −
            1
            
              |
            
            n
            −
            1
          
          
            L
          
        
        )
        ⋅
        
          u
          
            n
          
        
      
    
    {\displaystyle e_{n|n-1}^{L}=u_{n}^{-1}\cdot \phi _{n}(e_{n-1|n-1}^{L})\cdot u_{n}}
  
,

  
    
      
        
          e
          
            n
            
              |
            
            n
          
          
            L
          
        
        =
        exp
        ⁡
        (
        −
        
          K
          
            n
          
        
        (
        
          e
          
            n
            
              |
            
            n
            −
            1
          
          
            L
          
        
        ∗
        
          b
          
            n
          
        
        −
        
          b
          
            n
          
        
        )
        )
        ⋅
        
          e
          
            n
            
              |
            
            n
            −
            1
          
          
            L
          
        
      
    
    {\displaystyle e_{n|n}^{L}=\exp(-K_{n}(e_{n|n-1}^{L}*b_{n}-b_{n}))\cdot e_{n|n-1}^{L}}
  
,
and for right actions:

  
    
      
        
          e
          
            n
            
              |
            
            n
            −
            1
          
          
            R
          
        
        =
        
          ϕ
          
            n
          
        
        (
        
          e
          
            n
            −
            1
            
              |
            
            n
            −
            1
          
          
            R
          
        
        )
      
    
    {\displaystyle e_{n|n-1}^{R}=\phi _{n}(e_{n-1|n-1}^{R})}
  
,

  
    
      
        
          e
          
            n
            
              |
            
            n
          
          
            R
          
        
        =
        
          e
          
            n
            
              |
            
            n
            −
            1
          
          
            R
          
        
        exp
        ⁡
        (
        −
        
          K
          
            n
          
        
        (
        
          b
          
            n
          
        
        ∗
        
          e
          
            n
            
              |
            
            n
            −
            1
          
          
            R
          
        
        −
        
          b
          
            n
          
        
        )
        )
      
    
    {\displaystyle e_{n|n}^{R}=e_{n|n-1}^{R}\exp(-K_{n}(b_{n}*e_{n|n-1}^{R}-b_{n}))}
  
,
We see the estimated value of the state is not involved in the equation followed by the error variable, a property of linear Kalman filtering the classical extended Kalman filter does not share, but the similarity with the linear case actually goes much further. Let 
  
    
      
        
          ξ
          
            n
            
              |
            
            n
            −
            1
          
        
        ,
        
          ξ
          
            n
            
              |
            
            n
          
        
      
    
    {\displaystyle \xi _{n|n-1},\xi _{n|n}}
  
 be a linear version of the error variable defined by the identity:

  
    
      
        
          e
          
            n
            
              |
            
            n
            −
            1
          
        
        =
        exp
        ⁡
        (
        
          ξ
          
            n
            
              |
            
            n
            −
            1
          
        
        )
        ,
      
    
    {\displaystyle e_{n|n-1}=\exp(\xi _{n|n-1}),}
  

  
    
      
        
          e
          
            n
            
              |
            
            n
          
        
        =
        exp
        ⁡
        (
        
          ξ
          
            n
            
              |
            
            n
          
        
        )
        .
      
    
    {\displaystyle e_{n|n}=\exp(\xi _{n|n}).}
  

Then, with 
  
    
      
        
          F
          
            n
          
        
      
    
    {\displaystyle F_{n}}
  
 defined by the Taylor expansion 
  
    
      
        
          ξ
          
            n
            
              |
            
            n
          
        
        =
        
          F
          
            n
          
        
        
          ξ
          
            n
            
              |
            
            n
            −
            1
          
        
        +
        ∘
        (
        
          |
        
        
          |
        
        
          ξ
          
            n
            
              |
            
            n
            −
            1
          
        
        
          |
        
        
          |
        
        )
      
    
    {\displaystyle \xi _{n|n}=F_{n}\xi _{n|n-1}+\circ (||\xi _{n|n-1}||)}
  
 we actually have: 

  
    
      
        
          ξ
          
            n
            
              |
            
            n
          
        
        =
        
          F
          
            n
          
        
        
          ξ
          
            n
            
              |
            
            n
            −
            1
          
        
        .
      
    
    {\displaystyle \xi _{n|n}=F_{n}\xi _{n|n-1}.}
  

In other words, there are no higher-order terms: the dynamics is linear for the error variable 
  
    
      
        
          ξ
          
            n
            
              |
            
            n
          
        
        ,
        
          ξ
          
            n
            
              |
            
            n
            −
            1
          
        
      
    
    {\displaystyle \xi _{n|n},\xi _{n|n-1}}
  
. This result and error dynamics independence are at the core of theoretical properties and practical performance of IEKF.


== Relation to symmetry-preserving observers ==
Most physical systems possess natural symmetries (or invariance), i.e. there exist transformations (e.g. rotations, translations, scalings) that leave the system unchanged. From mathematical and engineering viewpoint, it makes sense that a filter well-designed for the considered system should preserve the same invariance properties. The idea for the IEKF is a modification of the EKF equations to take advantage of the symmetries of the system.


=== Definition ===
Consider the system

  
    
      
        
          
            
              x
              ˙
            
          
        
        
          =
        
        f
        (
        x
        ,
        u
        )
        +
        M
        (
        x
        )
        w
      
    
    {\displaystyle {\dot {x}}{=}f(x,u)+M(x)w}
  

  
    
      
        y
        
          =
        
        h
        (
        x
        ,
        u
        )
        +
        N
        (
        x
        )
        v
      
    
    {\displaystyle y{=}h(x,u)+N(x)v}
  

where  
  
    
      
        w
        ,
        v
      
    
    {\displaystyle w,v}
  
 are independent white Gaussian noises.
Consider 
  
    
      
        G
      
    
    {\displaystyle G}
  
 a Lie group with identity 
  
    
      
        e
      
    
    {\displaystyle e}
  
, and
(local) transformation groups 
  
    
      
        
          φ
          
            g
          
        
        ,
        
          ψ
          
            g
          
        
        ,
        
          ρ
          
            g
          
        
      
    
    {\displaystyle \varphi _{g},\psi _{g},\rho _{g}}
  
  (
  
    
      
        g
        ∈
        G
      
    
    {\displaystyle g\in G}
  
) such that 
  
    
      
        (
        X
        ,
        U
        ,
        Y
        )
        =
        (
        
          φ
          
            g
          
        
        (
        x
        )
        ,
        
          ψ
          
            g
          
        
        (
        u
        )
        ,
        
          ρ
          
            g
          
        
        (
        y
        )
        )
      
    
    {\displaystyle (X,U,Y)=(\varphi _{g}(x),\psi _{g}(u),\rho _{g}(y))}
  
. The previous system with noise is said to be invariant if it is left unchanged by the action the transformations groups 
  
    
      
        
          φ
          
            g
          
        
        ,
        
          ψ
          
            g
          
        
        ,
        
          ρ
          
            g
          
        
      
    
    {\displaystyle \varphi _{g},\psi _{g},\rho _{g}}
  
; that is, if

  
    
      
        
          
            
              X
              ˙
            
          
        
        
          =
        
        f
        (
        X
        ,
        U
        )
        +
        M
        (
        X
        )
        w
      
    
    {\displaystyle {\dot {X}}{=}f(X,U)+M(X)w}
  
.

  
    
      
        Y
        
          =
        
        h
        (
        X
        ,
        U
        )
        +
        N
        (
        X
        )
        v
      
    
    {\displaystyle Y{=}h(X,U)+N(X)v}
  


=== Filter equations and main result ===
Since it is a symmetry-preserving filter, the general form of an IEKF reads

  
    
      
        
          
            
              
                
                  x
                  ^
                
              
              ˙
            
          
        
        =
        f
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        )
        +
        W
        (
        
          
            
              x
              ^
            
          
        
        )
        L
        
          
            (
          
        
        I
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        )
        ,
        E
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        ,
        y
        )
        
          
            )
          
        
        E
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        ,
        y
        )
      
    
    {\displaystyle {\dot {\hat {x}}}=f({\hat {x}},u)+W({\hat {x}})L{\Bigl (}I({\hat {x}},u),E({\hat {x}},u,y){\Bigr )}E({\hat {x}},u,y)}
  

where

  
    
      
        E
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        ,
        y
        )
      
    
    {\displaystyle E({\hat {x}},u,y)}
  
 is an invariant output error, which is different from the usual output error 
  
    
      
        
          
            
              y
              ^
            
          
        
        −
        y
      
    
    {\displaystyle {\hat {y}}-y}
  

  
    
      
        W
        (
        
          
            
              x
              ^
            
          
        
        )
        =
        
          
            (
          
        
        
          w
          
            1
          
        
        (
        
          
            
              x
              ^
            
          
        
        )
        ,
        .
        .
        ,
        
          w
          
            n
          
        
        (
        
          
            
              x
              ^
            
          
        
        )
        
          
            )
          
        
      
    
    {\displaystyle W({\hat {x}})={\bigl (}w_{1}({\hat {x}}),..,w_{n}({\hat {x}}){\bigr )}}
  
 is an invariant frame

  
    
      
        I
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        )
      
    
    {\displaystyle I({\hat {x}},u)}
  
 is an invariant vector

  
    
      
        L
        (
        I
        ,
        E
        )
      
    
    {\displaystyle L(I,E)}
  
 is a freely chosen gain matrix.
To analyze the error convergence, an invariant state error 
  
    
      
        η
        (
        
          
            
              x
              ^
            
          
        
        ,
        x
        )
      
    
    {\displaystyle \eta ({\hat {x}},x)}
  
 is defined, which is different from the standard output error 
  
    
      
        
          
            
              x
              ^
            
          
        
        −
        x
      
    
    {\displaystyle {\hat {x}}-x}
  
, since the standard output error usually does not preserve the symmetries of the system.
Given the considered system and associated transformation group, there exists a constructive method  to determine 
  
    
      
        E
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        ,
        y
        )
        ,
        W
        (
        
          
            
              x
              ^
            
          
        
        )
        ,
        I
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        )
        ,
        η
        (
        
          
            
              x
              ^
            
          
        
        ,
        x
        )
      
    
    {\displaystyle E({\hat {x}},u,y),W({\hat {x}}),I({\hat {x}},u),\eta ({\hat {x}},x)}
  
, based on the moving frame method.
Similarly to the EKF, the gain matrix 
  
    
      
        L
        (
        I
        ,
        E
        )
      
    
    {\displaystyle L(I,E)}
  
 is determined from the equations

  
    
      
        L
        
          =
        
        P
        
          C
          
            T
          
        
        
          
            (
          
        
        N
        (
        e
        )
        
          N
          
            T
          
        
        (
        e
        )
        
          
            
              )
            
          
          
            −
            1
          
        
      
    
    {\displaystyle L{=}PC^{T}{\bigl (}N(e)N^{T}(e){\bigr )}^{-1}}
  
,

  
    
      
        
          
            
              P
              ˙
            
          
        
        
          =
        
        A
        P
        +
        P
        
          A
          
            T
          
        
        +
        M
        (
        e
        )
        
          M
          
            T
          
        
        (
        e
        )
        −
        P
        
          C
          
            T
          
        
        
          
            (
          
        
        N
        (
        e
        )
        
          N
          
            T
          
        
        (
        e
        )
        
          
            
              )
            
          
          
            −
            1
          
        
        C
        P
      
    
    {\displaystyle {\dot {P}}{=}AP+PA^{T}+M(e)M^{T}(e)-PC^{T}{\bigl (}N(e)N^{T}(e){\bigr )}^{-1}CP}
  
,
where the matrices 
  
    
      
        A
        ,
        C
      
    
    {\displaystyle A,C}
  
 depend here only on the known invariant vector 
  
    
      
        I
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        )
      
    
    {\displaystyle I({\hat {x}},u)}
  
, rather than on 
  
    
      
        (
        
          
            
              x
              ^
            
          
        
        ,
        u
        )
      
    
    {\displaystyle ({\hat {x}},u)}
  
 as in the standard EKF. This much simpler dependence and its consequences are the main interests of the IEKF. Indeed, the matrices 
  
    
      
        A
        ,
        C
      
    
    {\displaystyle A,C}
  
 are then constant on a much bigger set of trajectories (so-called permanent trajectories) than equilibrium points as it is the case for the EKF. Near such trajectories, we are back to the "true", i.e. linear, Kalman filter where convergence is guaranteed. Informally, this means the IEKF converges in general at least around any slowly varying permanent trajectory, rather than just around any slowly varying equilibrium point for the EKF.


== Application examples ==


=== Attitude and heading reference systems ===
Invariant extended Kalman filters are for instance used in attitude and heading reference systems. In such systems the orientation, velocity and/or position of a moving rigid body,
e.g. an aircraft, are estimated from different embedded sensors, such as inertial sensors, magnetometers, GPS or sonars. The use of an IEKF naturally leads to consider the quaternion error 
  
    
      
        
          
            
              q
              ^
            
          
        
        
          q
          
            −
            1
          
        
      
    
    {\displaystyle {\hat {q}}q^{-1}}
  
, which is often used as an ad hoc trick to preserve the constraints of the quaternion group. The benefits of the IEKF compared to the EKF are experimentally shown for a large set of trajectories.


=== Inertial navigation ===
A major application of the Invariant extended Kalman filter is inertial navigation, which fits the framework after embedding of the state (consisting of attitude matrix 
  
    
      
        R
      
    
    {\displaystyle R}
  
, velocity vector 
  
    
      
        v
      
    
    {\displaystyle v}
  
 and position vector 
  
    
      
        x
      
    
    {\displaystyle x}
  
) into the Lie group 
  
    
      
        S
        
          E
          
            2
          
        
        (
        3
        )
      
    
    {\displaystyle SE_{2}(3)}
  
 defined by the group operation:

  
    
      
        (
        
          R
          
            1
          
        
        ,
        
          v
          
            1
          
        
        ,
        
          x
          
            1
          
        
        )
        ⋅
        (
        
          R
          
            2
          
        
        ,
        
          v
          
            2
          
        
        ,
        
          x
          
            2
          
        
        )
        =
        (
        
          R
          
            1
          
        
        
          R
          
            2
          
        
        ,
        
          x
          
            1
          
        
        +
        
          R
          
            1
          
        
        
          x
          
            2
          
        
        ,
        
          v
          
            1
          
        
        +
        
          R
          
            1
          
        
        
          v
          
            2
          
        
        )
      
    
    {\displaystyle (R_{1},v_{1},x_{1})\cdot (R_{2},v_{2},x_{2})=(R_{1}R_{2},x_{1}+R_{1}x_{2},v_{1}+R_{1}v_{2})}
  


=== Simultaneous localization and mapping ===
The problem of simultaneous localization and mapping also fits the framework of invariant extended Kalman filtering after embedding of the state (consisting of attitude matrix 
  
    
      
        R
      
    
    {\displaystyle R}
  
, position vector 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and a sequence of static feature points 
  
    
      
        
          p
          
            1
          
        
        ,
        …
        ,
        
          p
          
            K
          
        
      
    
    {\displaystyle p^{1},\dots ,p^{K}}
  
) into the Lie group 
  
    
      
        S
        
          E
          
            K
            +
            1
          
        
        (
        3
        )
      
    
    {\displaystyle SE_{K+1}(3)}
  
 (or 
  
    
      
        S
        
          E
          
            K
            +
            1
          
        
        (
        2
        )
      
    
    {\displaystyle SE_{K+1}(2)}
  
 for planar systems) defined by the group operation:

  
    
      
        (
        
          R
          
            1
          
        
        ,
        
          x
          
            1
          
        
        ,
        
          p
          
            1
          
          
            1
          
        
        ,
        …
        ,
        
          p
          
            1
          
          
            K
          
        
        )
        ⋅
        (
        
          R
          
            2
          
        
        ,
        
          x
          
            2
          
        
        ,
        
          p
          
            2
          
          
            2
          
        
        ,
        …
        ,
        
          p
          
            2
          
          
            K
          
        
        )
        =
        (
        
          R
          
            1
          
        
        
          R
          
            2
          
        
        ,
        
          x
          
            1
          
        
        +
        
          R
          
            1
          
        
        
          x
          
            2
          
        
        ,
        
          p
          
            1
          
          
            1
          
        
        +
        
          R
          
            1
          
        
        
          p
          
            2
          
          
            1
          
        
        ,
        …
        ,
        
          p
          
            1
          
          
            K
          
        
        +
        
          R
          
            1
          
        
        
          p
          
            2
          
          
            K
          
        
        )
      
    
    {\displaystyle (R_{1},x_{1},p_{1}^{1},\dots ,p_{1}^{K})\cdot (R_{2},x_{2},p_{2}^{2},\dots ,p_{2}^{K})=(R_{1}R_{2},x_{1}+R_{1}x_{2},p_{1}^{1}+R_{1}p_{2}^{1},\dots ,p_{1}^{K}+R_{1}p_{2}^{K})}
  

The main benefit of the Invariant extended Kalman filter in this case is solving the problem of false observability.


== References ==
