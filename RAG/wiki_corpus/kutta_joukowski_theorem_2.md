# Circulation (physics)

> **Query Topic**: Kutta-Joukowski theorem (Rank #2 Search Result)  
> **Source Queue**: train (Row ID: 87, Frequency: 16)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Circulation_(physics)

---

In physics, circulation is the line integral of a vector field around a closed curve embedded in the field. In fluid dynamics, the field is the fluid velocity field. In electrodynamics, it can be the electric or the magnetic field. 
The term circulation was introduced by William Thomson (later Lord Kelvin) in 1869 to denote the line integral of velocity around a closed curve as a kinematic measure of rotational motion in a fluid, independent of any particular application.
In aerodynamics, circulation appears in a more specialised context in relation to the calculation of lift, where it is evaluated on contours enclosing a body under additional flow assumptions. In this context, circulation was first used independently by Frederick Lanchester, Ludwig Prandtl, Martin Kutta and Nikolay Zhukovsky. It is usually denoted by Γ (uppercase gamma).


== Definition and properties ==
If V is a vector field and dl is a vector representing the differential length of a small element of a defined curve, the contribution of that differential length to circulation is dΓ:

  
    
      
        
          d
        
        Γ
        =
        
          V
        
        ⋅
        
          d
        
        
          l
        
        =
        
          |
          
            V
          
          |
        
        
          |
          
            
              d
            
            
              l
            
          
          |
        
        cos
        ⁡
        θ
        .
      
    
    {\displaystyle \mathrm {d} \Gamma =\mathbf {V} \cdot \mathrm {d} \mathbf {l} =\left|\mathbf {V} \right|\left|\mathrm {d} \mathbf {l} \right|\cos \theta .}
  

Here, θ is the angle between the vectors V and dl.
The circulation Γ of a vector field V around a closed curve C is the line integral:

  
    
      
        Γ
        =
        
          ∮
          
            C
          
        
        
          V
        
        ⋅
        
          d
        
        
          l
        
        .
      
    
    {\displaystyle \Gamma =\oint _{C}\mathbf {V} \cdot \mathrm {d} \mathbf {l} .}
  

In a conservative vector field this integral evaluates to zero for every closed curve. That means that a line integral between any two points in the field is independent of the path taken. It also implies that the vector field can be expressed as the gradient of a scalar function, which is called a potential.


== Relation to vorticity and curl ==
Circulation can be related to curl of a vector field V and, more specifically, to vorticity if the field is a fluid velocity field,

  
    
      
        
          ω
        
        =
        ∇
        ×
        
          V
        
        .
      
    
    {\displaystyle {\boldsymbol {\omega }}=\nabla \times \mathbf {V} .}
  

By Stokes' theorem, the flux of curl or vorticity vectors through a surface S is equal to the circulation around its perimeter,

  
    
      
        Γ
        =
        
          ∮
          
            ∂
            S
          
        
        
          V
        
        ⋅
        
          d
        
        
          l
        
        =
        
          ∬
          
            S
          
        
        ∇
        ×
        
          V
        
        ⋅
        
          d
        
        
          S
        
        =
        
          ∬
          
            S
          
        
        
          ω
        
        ⋅
        
          d
        
        
          S
        
      
    
    {\displaystyle \Gamma =\oint _{\partial S}\mathbf {V} \cdot \mathrm {d} \mathbf {l} =\iint _{S}\nabla \times \mathbf {V} \cdot \mathrm {d} \mathbf {S} =\iint _{S}{\boldsymbol {\omega }}\cdot \mathrm {d} \mathbf {S} }
  

Here, the closed integration path ∂S is the boundary or perimeter of an open surface S, whose infinitesimal element normal dS = ndS is oriented according to the right-hand rule. Thus curl and vorticity are the circulation per unit area, taken around a local infinitesimal loop.
In potential flow of a fluid with a region of vorticity, all closed curves that enclose the vorticity have the same value for circulation.


== Uses ==


=== Kutta–Joukowski theorem in fluid dynamics ===

In fluid dynamics, the lift per unit span (L') acting on a body in a two-dimensional flow field is directly proportional to the circulation. Lift per unit span can be expressed as the product of the circulation Γ about the body, the fluid density 
  
    
      
        ρ
      
    
    {\displaystyle \rho }
  
, and the speed of the body relative to the free-stream 
  
    
      
        
          v
          
            ∞
          
        
      
    
    {\displaystyle v_{\infty }}
  
:

  
    
      
        
          L
          ′
        
        =
        ρ
        
          v
          
            ∞
          
        
        Γ
      
    
    {\displaystyle L'=\rho v_{\infty }\Gamma }
  

This is known as the Kutta–Joukowski theorem.
This equation applies around airfoils, where the circulation is generated by airfoil action; and around spinning objects experiencing the Magnus effect where the circulation is induced mechanically. In airfoil action, the magnitude of the circulation is determined by the Kutta condition.
The circulation on every closed curve around the airfoil has the same value, and is related to the lift generated by each unit length of span. Provided the closed curve encloses the airfoil, the choice of curve is arbitrary.
Circulation is often used in computational fluid dynamics as an intermediate variable to calculate forces on an airfoil or other body.


=== Fundamental equations of electromagnetism ===
In electrodynamics, the Maxwell-Faraday law of induction can be stated in two equivalent forms: that the curl of the electric field is equal to the negative rate of change of the magnetic field,

  
    
      
        ∇
        ×
        
          E
        
        =
        −
        
          
            
              ∂
              
                B
              
            
            
              ∂
              t
            
          
        
      
    
    {\displaystyle \nabla \times \mathbf {E} =-{\frac {\partial \mathbf {B} }{\partial t}}}
  

or that the circulation of the electric field around a loop is equal to the negative rate of change of the magnetic field flux through any surface spanned by the loop, by Stokes' theorem

  
    
      
        
          ∮
          
            ∂
            S
          
        
        
          E
        
        ⋅
        
          d
        
        
          l
        
        =
        
          ∬
          
            S
          
        
        ∇
        ×
        
          E
        
        ⋅
        
          d
        
        
          S
        
        =
        −
        
          
            
              d
            
            
              
                d
              
              t
            
          
        
        
          ∫
          
            S
          
        
        
          B
        
        ⋅
        
          d
        
        
          S
        
        .
      
    
    {\displaystyle \oint _{\partial S}\mathbf {E} \cdot \mathrm {d} \mathbf {l} =\iint _{S}\nabla \times \mathbf {E} \cdot \mathrm {d} \mathbf {S} =-{\frac {\mathrm {d} }{\mathrm {d} t}}\int _{S}\mathbf {B} \cdot \mathrm {d} \mathbf {S} .}
  

Circulation of a static magnetic field is, by Ampère's law, proportional to the total current enclosed by the loop

  
    
      
        
          ∮
          
            ∂
            S
          
        
        
          B
        
        ⋅
        
          d
        
        
          l
        
        =
        
          μ
          
            0
          
        
        
          ∬
          
            S
          
        
        
          J
        
        ⋅
        
          d
        
        
          S
        
        =
        
          μ
          
            0
          
        
        
          I
          
            enc
          
        
        .
      
    
    {\displaystyle \oint _{\partial S}\mathbf {B} \cdot \mathrm {d} \mathbf {l} =\mu _{0}\iint _{S}\mathbf {J} \cdot \mathrm {d} \mathbf {S} =\mu _{0}I_{\text{enc}}.}
  

For systems with electric fields that change over time, the law must be modified to include a term known as Maxwell's correction.


== See also ==

Maxwell's equations
Biot–Savart law in aerodynamics
Kelvin's circulation theorem


== References ==
