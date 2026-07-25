# Bernoulli's principle

> **Query Topic**: Bernoulli's principle  
> **Source Queue**: train (Row ID: 95, Frequency: 15)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Bernoulli's_principle

---

Bernoulli's principle is a  concept in fluid dynamics that relates pressure, speed and height. For example, for a fluid flowing horizontally, Bernoulli's principle states that an increase in the speed  occurs simultaneously with a decrease in pressure. The principle is named after the Swiss mathematician and physicist Daniel Bernoulli, who published it in his book Hydrodynamica in 1738. Although Bernoulli deduced that pressure decreases when the flow speed increases, it was Leonhard Euler in 1752 who derived Bernoulli's equation in its usual form.
Bernoulli's principle can be derived directly from Isaac Newton's second law of motion. When a small volume of fluid is flowing horizontally from a region of high pressure to a region of low pressure, there is more pressure from behind than in front. This gives a net force on the volume, accelerating it along the streamline.  Fluid is accelerated in the direction of the velocity if the pressure goes down. Thus the decrease of pressure is the cause of a higher velocity.
Bernoulli's principle can also be derived from the principle of conservation of energy which states that in a steady fluid flow the sum of all forms of energy the same throughout the flow. This requires that the sum of kinetic energy, potential energy and internal energy remains constant. Thus an increase in the speed of the fluid occurs with a simultaneous decrease in its potential energy and internal energy. 
Fluid particles are subject only to pressure and their own weight. If a fluid is flowing horizontally and along a section of a streamline, where the speed increases it can only be because the fluid on that section has moved from a region of higher pressure to a region of lower pressure; and if its speed decreases, it can only be because it has moved from a region of lower pressure to a region of higher pressure. Consequently, within a fluid flowing horizontally, the highest speed occurs where the pressure is lowest, and the lowest speed occurs where the pressure is highest.

Bernoulli's principle is only applicable for isentropic flows: when the effects of irreversible processes (like turbulence) and non-adiabatic processes (e.g. thermal radiation) are small and can be neglected. The simple form of Bernoulli's equation is valid for incompressible flows (e.g. most liquid flows and gases moving at low Mach number). More advanced forms may be applied to compressible flows at higher Mach numbers.


== Incompressible flow equation ==
In most flows of liquids, and of gases at low Mach number, the density of a fluid parcel can be considered to be constant, regardless of pressure variations in the flow. Therefore, the fluid can be considered to be incompressible, and these flows are called incompressible flows. Bernoulli performed his experiments on liquids, so his equation in its original form is valid only for incompressible flow.
A common form of Bernoulli's equation is:

where:

  
    
      
        v
      
    
    {\displaystyle v}
  
 is the fluid flow speed at a point,

  
    
      
        g
      
    
    {\displaystyle g}
  
 is the acceleration due to gravity,

  
    
      
        z
      
    
    {\displaystyle z}
  
 is the elevation of the point above a reference plane, with the positive 
  
    
      
        z
      
    
    {\displaystyle z}
  
-direction pointing upward—so in the direction opposite to the gravitational acceleration,

  
    
      
        p
      
    
    {\displaystyle p}
  
 is the static pressure at the chosen point, and

  
    
      
        ρ
      
    
    {\displaystyle \rho }
  
 is the density of the fluid at all points in the fluid.
Bernoulli's equation and the Bernoulli constant are applicable throughout any region of flow where the energy per unit mass is uniform. Because the energy per unit mass of liquid in a well-mixed reservoir is uniform throughout, Bernoulli's equation can be used to analyze the fluid flow everywhere in that reservoir (including pipes or flow fields that the reservoir feeds) except where viscous forces dominate and erode the energy per unit mass.
The following assumptions must be met for this Bernoulli equation to apply:

the flow must be steady, that is, the flow parameters (velocity, density, etc.) at any point cannot change with time,
the flow must be incompressible—even though pressure varies, the density must remain constant along a streamline;
friction by viscous forces must be negligible.
For conservative force fields (not limited to the gravitational field), Bernoulli's equation can be generalized as:

  
    
      
        
          
            
              v
              
                2
              
            
            2
          
        
        +
        Ψ
        +
        
          
            p
            ρ
          
        
        =
        
          constant
        
      
    
    {\displaystyle {\frac {v^{2}}{2}}+\Psi +{\frac {p}{\rho }}={\text{constant}}}
  

where Ψ is the force potential at the point considered. For example, for the Earth's gravity Ψ = gz.
By multiplying with the fluid density ρ, equation (A) can be rewritten as:

  
    
      
        
          
            
              1
              2
            
          
        
        ρ
        
          v
          
            2
          
        
        +
        ρ
        g
        z
        +
        p
        =
        
          constant
        
      
    
    {\displaystyle {\tfrac {1}{2}}\rho v^{2}+\rho gz+p={\text{constant}}}
  

or:

  
    
      
        q
        +
        ρ
        g
        h
        =
        
          p
          
            0
          
        
        +
        ρ
        g
        z
        =
        
          constant
        
      
    
    {\displaystyle q+\rho gh=p_{0}+\rho gz={\text{constant}}}
  

where

q = ⁠1/2⁠ρv2 is dynamic pressure,
h = z + ⁠p/ρg⁠ is the piezometric head or hydraulic head (the sum of the elevation z and the pressure head) and
p0 = p + q is the stagnation pressure (the sum of the static pressure p and dynamic pressure q).
The constant in the Bernoulli equation can be normalized. A common approach is in terms of total head or energy head H:

  
    
      
        H
        =
        z
        +
        
          
            p
            
              ρ
              g
            
          
        
        +
        
          
            
              v
              
                2
              
            
            
              2
              g
            
          
        
        =
        h
        +
        
          
            
              v
              
                2
              
            
            
              2
              g
            
          
        
        ,
      
    
    {\displaystyle H=z+{\frac {p}{\rho g}}+{\frac {v^{2}}{2g}}=h+{\frac {v^{2}}{2g}},}
  

The above equations suggest there is a flow speed at which pressure is zero, and at even higher speeds the pressure is negative. Most often, gases and liquids are not capable of negative absolute pressure, or even zero pressure, so clearly Bernoulli's equation ceases to be valid before zero pressure is reached. In liquids—when the pressure becomes too low—cavitation occurs. The above equations use a linear relationship between flow speed squared and pressure. At higher flow speeds in gases, or for sound waves in liquid, the changes in mass density become significant so that the assumption of constant density is invalid.


=== Simplified form ===
In many applications of Bernoulli's equation, the change in the ρgz term is so small compared with the other terms that it can be ignored. For example, in the case of aircraft in flight, the change in height z is so small the ρgz term can be omitted. This allows the above equation to be presented in the following simplified form:

  
    
      
        p
        +
        q
        =
        
          p
          
            0
          
        
      
    
    {\displaystyle p+q=p_{0}}
  

where p0 is called total pressure, and q is  dynamic pressure. Many authors refer to the pressure p as static pressure to distinguish it from total pressure p0 and dynamic pressure q. In Aerodynamics, L.J. Clancy writes: "To distinguish it from the total and dynamic pressures, the actual pressure of the fluid, which is associated not with its motion but with its state, is often referred to as the static pressure, but where the term pressure alone is used it refers to this static pressure."
The simplified form of Bernoulli's equation can be summarized in the following memorable word equation:

Every point in a steadily flowing fluid, regardless of the fluid speed at that point, has its own unique static pressure p and dynamic pressure q. Their sum p + q is defined to be the total pressure p0. The significance of Bernoulli's principle can now be summarized as "total pressure is constant in any region free of viscous forces". If the fluid flow is brought to rest at some point, this point is called a stagnation point, and at this point the static pressure is equal to the stagnation pressure.
If the fluid flow is irrotational, the total pressure is uniform and Bernoulli's principle can be summarized as "total pressure is constant everywhere in the fluid flow". It is reasonable to assume that irrotational flow exists in any situation where a large body of fluid is flowing past a solid body. Examples are aircraft in flight and ships moving in open bodies of water. However, Bernoulli's principle importantly does not apply in the boundary layer such as in flow through long pipes.


=== Unsteady potential flow ===
The Bernoulli equation for unsteady potential flow is used in the theory of ocean surface waves and acoustics. For an irrotational flow, the flow velocity can be described as the gradient ∇φ of a velocity potential φ. In that case, and for a constant density ρ, the momentum equations of the Euler equations can be integrated to:
  
    
      
        
          
            
              ∂
              φ
            
            
              ∂
              t
            
          
        
        +
        
          
            
              1
              2
            
          
        
        
          v
          
            2
          
        
        +
        
          
            p
            ρ
          
        
        +
        g
        z
        =
        f
        (
        t
        )
        ,
      
    
    {\displaystyle {\frac {\partial \varphi }{\partial t}}+{\tfrac {1}{2}}v^{2}+{\frac {p}{\rho }}+gz=f(t),}
  

which is a Bernoulli equation valid also for unsteady—or time dependent—flows. Here ⁠∂φ/∂t⁠ denotes the partial derivative of the velocity potential φ with respect to time t, and v = |∇φ| is the flow speed. The function f(t) depends only on time and not on position in the fluid. As a result, the Bernoulli equation at some moment t applies in the whole fluid domain. This is also true for the special case of a steady irrotational flow, in which case f and ⁠∂φ/∂t⁠ are constants so equation (A) can be applied in every point of the fluid domain. Further f(t) can be made equal to zero by incorporating it into the velocity potential using the transformation:
  
    
      
        Φ
        =
        φ
        −
        
          ∫
          
            
              t
              
                0
              
            
          
          
            t
          
        
        f
        (
        τ
        )
        
        
          d
        
        τ
        ,
      
    
    {\displaystyle \Phi =\varphi -\int _{t_{0}}^{t}f(\tau )\,\mathrm {d} \tau ,}
  

resulting in:

  
    
      
        
          
            
              ∂
              Φ
            
            
              ∂
              t
            
          
        
        +
        
          
            
              1
              2
            
          
        
        
          v
          
            2
          
        
        +
        
          
            p
            ρ
          
        
        +
        g
        z
        =
        0.
      
    
    {\displaystyle {\frac {\partial \Phi }{\partial t}}+{\tfrac {1}{2}}v^{2}+{\frac {p}{\rho }}+gz=0.}
  

Note that the relation of the potential to the flow velocity is unaffected by this transformation: ∇Φ = ∇φ.
The Bernoulli equation for unsteady potential flow also appears to play a central role in Luke's variational principle, a variational description of free-surface flows using the Lagrangian mechanics.


== Compressible flow equation ==
Bernoulli developed his principle from observations on liquids, and Bernoulli's equation is valid for ideal fluids: those that are inviscid, incompressible and subjected only to conservative forces. It is sometimes valid for the flow of gases as well, provided that there is no transfer of kinetic or potential energy from the gas flow to the compression or expansion of the gas. If both the gas pressure and volume change simultaneously, then work will be done on or by the gas. In this case, Bernoulli's equation in its incompressible flow form cannot be assumed to be valid. However, if the gas process is entirely isobaric, or isochoric, then no work is done on or by the gas (so the simple energy balance is not upset). According to the gas law, an isobaric or isochoric process is ordinarily the only way to ensure constant density in a gas. Also the gas density will be proportional to the ratio of pressure and absolute temperature; however, this ratio will vary upon compression or expansion, no matter what non-zero quantity of heat is added or removed. The only exception is if the net heat transfer is zero, as in a complete thermodynamic cycle or in an individual isentropic (frictionless adiabatic) process, and even then this reversible process must be reversed, to restore the gas to the original pressure and specific volume, and thus density. Only then is the original, unmodified Bernoulli equation applicable. In this case the equation can be used if the flow speed of the gas is sufficiently below the speed of sound, such that the variation in density of the gas (due to this effect) along each streamline can be ignored. Adiabatic flow at less than Mach 0.3 is generally considered to be slow enough.
It is possible to use the fundamental principles of physics to develop similar equations applicable to compressible fluids. There are numerous equations, each tailored for a particular application, but all are analogous to Bernoulli's equation and all rely on nothing more than the fundamental principles of physics such as Newton's laws of motion or the first law of thermodynamics.


=== Compressible flow in fluid dynamics ===
For a compressible fluid, with a barotropic equation of state, and under the action of conservative forces,

  
    
      
        
          
            
              v
              
                2
              
            
            2
          
        
        +
        
          ∫
          
            
              p
              
                1
              
            
          
          
            p
          
        
        
          
            
              
                d
              
              
                
                  
                    p
                    ~
                  
                
              
            
            
              ρ
              
                (
                
                  
                    
                      p
                      ~
                    
                  
                
                )
              
            
          
        
        +
        Ψ
        =
        
          constant (along a streamline)
        
      
    
    {\displaystyle {\frac {v^{2}}{2}}+\int _{p_{1}}^{p}{\frac {\mathrm {d} {\tilde {p}}}{\rho \left({\tilde {p}}\right)}}+\Psi ={\text{constant (along a streamline)}}}
  

where:

p is the pressure
ρ is the density and ρ(p) indicates that it is a function of pressure
v is the flow speed
Ψ is the potential associated with the conservative force field, often the gravitational potential
In engineering situations, elevations are generally small compared to the size of the Earth, and the time scales of fluid flow are small enough to consider the equation of state as adiabatic. In this case, the above equation for an ideal gas becomes:

  
    
      
        
          
            
              v
              
                2
              
            
            2
          
        
        +
        g
        z
        +
        
          (
          
            
              γ
              
                γ
                −
                1
              
            
          
          )
        
        
          
            p
            ρ
          
        
        =
        
          constant (along a streamline)
        
      
    
    {\displaystyle {\frac {v^{2}}{2}}+gz+\left({\frac {\gamma }{\gamma -1}}\right){\frac {p}{\rho }}={\text{constant (along a streamline)}}}
  

where, in addition to the terms listed above:

γ is the ratio of the specific heats of the fluid
g is the acceleration due to gravity
z is the elevation of the point above a reference plane
In many applications of compressible flow, changes in elevation are negligible compared to the other terms, so the term gz can be omitted. A very useful form of the equation is then:

  
    
      
        
          
            
              v
              
                2
              
            
            2
          
        
        +
        
          (
          
            
              γ
              
                γ
                −
                1
              
            
          
          )
        
        
          
            p
            ρ
          
        
        =
        
          (
          
            
              γ
              
                γ
                −
                1
              
            
          
          )
        
        
          
            
              p
              
                0
              
            
            
              ρ
              
                0
              
            
          
        
      
    
    {\displaystyle {\frac {v^{2}}{2}}+\left({\frac {\gamma }{\gamma -1}}\right){\frac {p}{\rho }}=\left({\frac {\gamma }{\gamma -1}}\right){\frac {p_{0}}{\rho _{0}}}}
  

where:

p0 is the total pressure
ρ0 is the total density


=== Compressible flow in thermodynamics ===
The most general form of the equation, suitable for use in thermodynamics in case of (quasi) steady flow, is:

  
    
      
        
          
            
              v
              
                2
              
            
            2
          
        
        +
        Ψ
        +
        w
        =
        
          constant
        
        .
      
    
    {\displaystyle {\frac {v^{2}}{2}}+\Psi +w={\text{constant}}.}
  

Here w is the enthalpy per unit mass (also known as specific enthalpy), which is also often written as h (not to be confused with "head" or "height").
Note that

  
    
      
        w
        =
        e
        +
        
          
            p
            ρ
          
        
         
         
         
        
          (
          
            =
            
              
                γ
                
                  γ
                  −
                  1
                
              
            
            
              
                p
                ρ
              
            
          
          )
        
      
    
    {\displaystyle w=e+{\frac {p}{\rho }}~~~\left(={\frac {\gamma }{\gamma -1}}{\frac {p}{\rho }}\right)}
  

where e is the thermodynamic energy per unit mass, also known as the specific internal energy. So, for constant internal energy 
  
    
      
        e
      
    
    {\displaystyle e}
  
 the equation reduces to the incompressible-flow form.
The constant on the right-hand side is often called the Bernoulli constant and denoted b. For steady inviscid adiabatic flow with no additional sources or sinks of energy, b is constant along any given streamline. More generally, when b may vary along streamlines, it still proves a useful parameter, related to the "head" of the fluid (see below).
When the change in Ψ can be ignored, a very useful form of this equation is:

  
    
      
        
          
            
              v
              
                2
              
            
            2
          
        
        +
        w
        =
        
          w
          
            0
          
        
      
    
    {\displaystyle {\frac {v^{2}}{2}}+w=w_{0}}
  

where w0 is total enthalpy. For a calorically perfect gas such as an ideal gas, the enthalpy is directly proportional to the temperature, and this leads to the concept of the total (or stagnation) temperature.
When shock waves are present, in a reference frame in which the shock is stationary and the flow is steady, many of the parameters in the Bernoulli equation suffer abrupt changes in passing through the shock. The Bernoulli parameter remains unaffected. An exception to this rule is radiative shocks, which violate the assumptions leading to the Bernoulli equation, namely the lack of additional sinks or sources of energy.


=== Unsteady potential flow ===
For a compressible fluid, with a barotropic equation of state, the unsteady momentum conservation equation

  
    
      
        
          
            
              ∂
              
                
                  
                    v
                    →
                  
                
              
            
            
              ∂
              t
            
          
        
        +
        
          (
          
            
              
                
                  v
                  →
                
              
            
            ⋅
            ∇
          
          )
        
        
          
            
              v
              →
            
          
        
        =
        −
        
          
            
              g
              →
            
          
        
        −
        
          
            
              ∇
              p
            
            ρ
          
        
      
    
    {\displaystyle {\frac {\partial {\vec {v}}}{\partial t}}+\left({\vec {v}}\cdot \nabla \right){\vec {v}}=-{\vec {g}}-{\frac {\nabla p}{\rho }}}
  

With the irrotational assumption, namely, the flow velocity can be described as the gradient ∇φ of a velocity potential φ. The unsteady momentum conservation equation becomes

  
    
      
        
          
            
              ∂
              ∇
              ϕ
            
            
              ∂
              t
            
          
        
        +
        ∇
        
          (
          
            
              
                ∇
                ϕ
                ⋅
                ∇
                ϕ
              
              2
            
          
          )
        
        =
        −
        ∇
        Ψ
        −
        ∇
        
          ∫
          
            
              p
              
                1
              
            
          
          
            p
          
        
        
          
            
              d
              
                
                  
                    p
                    ~
                  
                
              
            
            
              ρ
              (
              
                
                  
                    p
                    ~
                  
                
              
              )
            
          
        
      
    
    {\displaystyle {\frac {\partial \nabla \phi }{\partial t}}+\nabla \left({\frac {\nabla \phi \cdot \nabla \phi }{2}}\right)=-\nabla \Psi -\nabla \int _{p_{1}}^{p}{\frac {d{\tilde {p}}}{\rho ({\tilde {p}})}}}
  

which leads to

  
    
      
        
          
            
              ∂
              ϕ
            
            
              ∂
              t
            
          
        
        +
        
          
            
              ∇
              ϕ
              ⋅
              ∇
              ϕ
            
            2
          
        
        +
        Ψ
        +
        
          ∫
          
            
              p
              
                1
              
            
          
          
            p
          
        
        
          
            
              d
              
                
                  
                    p
                    ~
                  
                
              
            
            
              ρ
              (
              
                
                  
                    p
                    ~
                  
                
              
              )
            
          
        
        =
        
          constant
        
      
    
    {\displaystyle {\frac {\partial \phi }{\partial t}}+{\frac {\nabla \phi \cdot \nabla \phi }{2}}+\Psi +\int _{p_{1}}^{p}{\frac {d{\tilde {p}}}{\rho ({\tilde {p}})}}={\text{constant}}}
  

In this case, the above equation for isentropic flow becomes:

  
    
      
        
          
            
              ∂
              ϕ
            
            
              ∂
              t
            
          
        
        +
        
          
            
              ∇
              ϕ
              ⋅
              ∇
              ϕ
            
            2
          
        
        +
        Ψ
        +
        
          
            γ
            
              γ
              −
              1
            
          
        
        
          
            p
            ρ
          
        
        =
        
          constant
        
      
    
    {\displaystyle {\frac {\partial \phi }{\partial t}}+{\frac {\nabla \phi \cdot \nabla \phi }{2}}+\Psi +{\frac {\gamma }{\gamma -1}}{\frac {p}{\rho }}={\text{constant}}}
  


== Derivations ==


== Applications ==

In modern everyday life there are many observations that can be successfully explained by application of Bernoulli's principle, even though no real fluid is entirely inviscid, and a small viscosity often has a large effect on the flow.

Bernoulli's principle can be used to calculate the lift force on an airfoil, if the behaviour of the fluid flow in the vicinity of the foil is known. For example, if the air flowing past the top surface of an aircraft wing is moving faster than the air flowing past the bottom surface, then Bernoulli's principle implies that the pressure on the surfaces of the wing will be lower above than below. This pressure difference results in an upwards lifting force. Whenever the distribution of speed past the top and bottom surfaces of a wing is known, the lift forces can be calculated (to a good approximation) using Bernoulli's equations, which were established by Bernoulli over a century before the first man-made wings were used for the purpose of flight.
The basis of a carburetor used in many reciprocating engines is a throat in the air flow to create a region of low pressure to draw fuel into the carburetor and mix it thoroughly with the incoming air. The low pressure in the throat can be explained by Bernoulli's principle, where air in the throat is moving at its fastest speed and therefore it is at its lowest pressure. The carburetor may or may not use the difference between the two static pressures which result from the Venturi effect on the air flow in order to force the fuel to flow, and as a basis a carburetor may use the difference in pressure between the throat and local air pressure in the float bowl, or between the throat and a Pitot tube at the air entry.
An injector on a steam locomotive or a static boiler.
The pitot tube and static port on an aircraft are used to determine the airspeed of the aircraft. These two devices are connected to the airspeed indicator, which determines the dynamic pressure of the airflow past the aircraft. Bernoulli's principle is used to calibrate the airspeed indicator so that it displays the indicated airspeed appropriate to the dynamic pressure.
A De Laval nozzle utilizes Bernoulli's principle to create a force by turning pressure energy generated by the combustion of propellants into velocity. This then generates thrust by way of Newton's third law of motion.
The flow speed of a fluid can be measured using a device such as a Venturi meter or an orifice plate, which can be placed into a pipeline to reduce the diameter of the flow. For a horizontal device, the continuity equation shows that for an incompressible fluid, the reduction in diameter will cause an increase in the fluid flow speed. Subsequently, Bernoulli's principle then shows that there must be a decrease in the pressure in the reduced diameter region. This phenomenon is known as the Venturi effect.
The maximum possible drain rate for a tank with a hole or tap at the base can be calculated directly from Bernoulli's equation and is found to be proportional to the square root of the height of the fluid in the tank. This is Torricelli's law, which is compatible with Bernoulli's principle. Increased viscosity lowers this drain rate; this is reflected in the discharge coefficient, which is a function of the Reynolds number and the shape of the orifice.
The Bernoulli grip relies on this principle to create a non-contact adhesive force between a surface and the gripper.


== Misconceptions ==


=== Airfoil lift ===

One of the most common erroneous explanations of aerodynamic lift asserts that the air must traverse the upper and lower surfaces of a wing in the same amount of time, implying that since the upper surface presents a longer path the air must be moving over the top of the wing faster than over the bottom. Bernoulli's principle is then cited to conclude that the pressure on top of the wing must be lower than on the bottom.
Equal transit time applies to the flow around a body generating no lift, but there is no physical principle that requires equal transit time in cases of bodies generating lift. In fact, theory predicts – and experiments confirm – that the air traverses the top surface of a body experiencing lift in a shorter time than it traverses the bottom surface; the explanation based on equal transit time is false. While the equal-time explanation is false, it is not the Bernoulli principle that is false, because this principle is well established; Bernoulli's equation is used correctly in common mathematical treatments of aerodynamic lift.


=== Common classroom demonstrations ===
There are several common classroom demonstrations that are sometimes incorrectly explained using Bernoulli's principle.
One involves holding a piece of paper horizontally so that it droops downward and then blowing over the top of it. As the demonstrator blows over the paper, the paper rises. It is then asserted that this is because "faster moving air has lower pressure".
One problem with this explanation can be seen by blowing along the bottom of the paper: if the deflection was caused by faster moving air, then the paper should deflect downward; but the paper deflects upward regardless of whether the faster moving air is on the top or the bottom. Another problem is that when the air leaves the demonstrator's mouth it has the same pressure as the surrounding air; the air does not have lower pressure just because it is moving; in the demonstration, the static pressure of the air leaving the demonstrator's mouth is equal to the pressure of the surrounding air. A third problem is that it is false to make a connection between the flow on the two sides of the paper using Bernoulli's equation since the air above and below are different flow fields and Bernoulli's principle only applies within a flow field.
As the wording of the principle can change its implications, stating the principle correctly is important. What Bernoulli's principle actually says is that within a flow of constant energy, when fluid flows through a region of lower pressure it speeds up and vice versa. Thus, Bernoulli's principle concerns itself with changes in speed and changes in pressure within a flow field. It cannot be used to compare different flow fields.
A correct explanation of why the paper rises would observe that the plume follows the curve of the paper and that a curved streamline will develop a pressure gradient perpendicular to the direction of flow, with the lower pressure on the inside of the curve. Bernoulli's principle predicts that the decrease in pressure is associated with an increase in speed; in other words, as the air passes over the paper, it speeds up and moves faster than it was moving when it left the demonstrator's mouth. But this is not apparent from the demonstration.
Other common classroom demonstrations, such as blowing between two suspended spheres, inflating a large bag, or suspending a ball in an airstream are sometimes explained in a similarly misleading manner by saying "faster moving air has lower pressure".


== See also ==
Torricelli's law
Coandă effect
Euler equations – for the flow of an inviscid fluid
Hydraulics – applied fluid mechanics for liquids
Navier–Stokes equations – for the flow of a viscous fluid
Teapot effect
Terminology in fluid dynamics


== Notes ==


== References ==


== External links ==

The Flow of Dry Water - The Feynman Lectures on Physics
Science 101 Q: Is It Really Caused by the Bernoulli Effect?
Millersville University – Applications of Euler's equation
NASA – Beginner's guide to aerodynamics Archived 2012-07-15 at the Wayback Machine
Misinterpretations of Bernoulli's equation – Weltner and Ingelman-Sundberg Archived 2012-02-08 at the Wayback Machine
