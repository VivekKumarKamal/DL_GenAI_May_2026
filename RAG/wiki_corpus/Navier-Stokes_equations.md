# Navier–Stokes equations

> **Query Topic**: Navier-Stokes equations (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 230, Frequency: 13)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Navier–Stokes_equations

---

The Navier–Stokes equations ( / n æ v ˈ j eɪ ˈ s t oʊ k s / nav- YAY STOHKS ) describe the motion of viscous fluids. This system of partial differential equations was named after Claude-Louis Navier and George Gabriel Stokes , who developed them over a few decades of progressive work, from 1822 (Navier) to 1842–1850 (Stokes). Siméon Denis Poisson independently achieved the same results.

The Navier–Stokes equations mathematically express momentum balance for Newtonian fluids and make use of the conservation of mass . They are sometimes accompanied by an equation of state relating pressure , temperature and density . They arise from applying Newton's second law to fluid motion , together with the assumption that the stress in the fluid is the sum of a diffusing viscous term (proportional to the gradient of velocity) and a pressure term—hence describing viscous flow . The Navier–Stokes equations generalize the Euler equations in that the latter model only considers inviscid flow .

The Navier–Stokes equations are of great scientific and engineering interest because they may be used to model a wide variety of scenarios. In their full or simplified forms, they can assist in the design of aircraft and cars, the study of blood flow , the design of power stations , the analysis of pollution , and many other problems. Coupled with Maxwell's equations , they comprise the fundamentals of magnetohydrodynamics .

The Navier–Stokes equations are also of great interest in a purely mathematical sense. Despite their wide range of practical uses, the conjecture that they have smooth (meaning infinitely differentiable) or bounded solutions in three dimensions has not yet been proven. This is called the Navier–Stokes existence and smoothness problem. The Clay Mathematics Institute has called this one of the seven most important open problems in mathematics and has offered a $1 million prize for a solution or a counterexample.

## Flow velocity

The solution of the equations is a flow velocity . It is a vector field —to every point in a fluid , at any moment in a time interval, it gives a vector whose direction and magnitude are those of the velocity of the fluid at that point in space and at that moment in time. It is studied in three spatial dimensions and one time dimension, and higher-dimensional analogues are studied in both pure and applied mathematics. Once the velocity field is calculated, other quantities of interest, such as pressure or temperature , may be found using dynamical equations and relations. This is different from what one normally sees in classical mechanics , where solutions are typically trajectories of the position of a particle or deflection of a continuum . Studying velocity instead of position makes more sense for a fluid, although for visualization purposes, one can compute various trajectories . In particular, the streamlines of a vector field, interpreted as flow velocity, are the paths along which a massless fluid particle would travel. These paths are the integral curves whose derivative at each point is equal to the vector field, and they can represent visually the behavior of the vector field at a point in time.

## General continuum equations

The Navier–Stokes momentum equation can be derived as a particular form of the Cauchy momentum equation , whose general convective form is: ${\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}={\frac {1}{\rho }}\nabla \cdot {\boldsymbol {\sigma }}+\mathbf {a} .$ By setting the Cauchy stress tensor ${\textstyle {\boldsymbol {\sigma }}}$ to be the sum of a viscosity term ${\textstyle {\boldsymbol {\tau }}}$ (the deviatoric stress ) and a pressure term ${\textstyle -p\mathbf {I} }$ (volumetric stress), we arrive at:

$\rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=-\nabla p+\nabla \cdot {\boldsymbol {\tau }}+\rho \,\mathbf {a}$

where

- ${\textstyle {\frac {\mathrm {D} }{\mathrm {D} t}}}$ is the material derivative , defined as ${\textstyle {\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla }$ ,

- ${\textstyle \rho }$ is the (mass) density,

- ${\textstyle \mathbf {u} }$ is the flow velocity,

- ${\textstyle \nabla \cdot \,}$ is the divergence ,

- ${\textstyle p}$ is the pressure ,

- ${\textstyle t}$ is time ,

- ${\textstyle {\boldsymbol {\tau }}}$ is the deviatoric stress tensor , which has order 2,

- ${\textstyle \mathbf {a} }$ represents body accelerations acting on the continuum, for example gravity , inertial accelerations , electrostatic accelerations , and so on.

In this form, it is apparent that in the assumption of an inviscid fluid – no deviatoric stress – Cauchy equations reduce to the Euler equations .

Assuming conservation of mass , with the known properties of divergence and gradient we can use the mass continuity equation , which represents the mass per unit volume of a homogenous fluid with respect to space and time (i.e., material derivative ${\textstyle {\frac {\mathbf {D} }{\mathbf {Dt} }}}$ ) of any finite volume ( ${\textstyle \mathbf {V} }$ ) to represent the change of velocity in fluid media: ${\begin{aligned}&{\frac {\mathbf {D} m}{\mathbf {Dt} }}=\iiint \limits _{V}\left({\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )\right)\,dV\\[5pt]&{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+(\nabla \rho )\cdot \mathbf {u} +\rho (\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+\nabla \cdot (\rho \mathbf {u} )=0\end{aligned}}$ where

- ${\textstyle {\frac {\mathrm {D} m}{\mathrm {D} t}}}$ is the material derivative of mass per unit volume ( density , $\rho$ ),

- ${\textstyle \iiint \limits _{V}{\bigl (}F(x_{1},x_{2},x_{3},t){\bigr )}\,dV}$ is the mathematical operation for the integration throughout the volume ( ${\textstyle V}$ ),

- ${\textstyle {\frac {\partial }{\partial t}}}$ is the partial derivative mathematical operator,

- ${\textstyle \nabla \cdot \mathbf {u} \,}$ is the divergence of the flow velocity ( $\mathbf {u}$ ), which is a scalar field ,

- ${\textstyle \nabla \rho \,}$ is the gradient of density ( $\rho$ ), which is the vector derivative of a scalar field ,

to arrive at the conservation form of the equations of motion. This is often written:

${\frac {\partial }{\partial t}}(\rho \,\mathbf {u} )+\nabla \cdot (\rho \,\mathbf {u} \otimes \mathbf {u} )=-\nabla p+\nabla \cdot {\boldsymbol {\tau }}+\rho \,\mathbf {a}$

where ${\textstyle \otimes }$ is the outer product of the flow velocity ( ${\textstyle \mathbf {u} }$ ): $\mathbf {u} \otimes \mathbf {u} =\mathbf {u} \mathbf {u} ^{\mathsf {T}}$

The left side of the equation describes acceleration, and may be composed of time-dependent and convective components (also the effects of non-inertial coordinates if present). The right side of the equation is in effect a summation of hydrostatic effects, the divergence of deviatoric stress and body forces (such as gravity).

All non-relativistic balance equations, such as the Navier–Stokes equations, can be derived by beginning with the Cauchy equations and specifying the stress tensor through a constitutive relation . By expressing the deviatoric (shear) stress tensor in terms of viscosity and the fluid velocity gradient, and assuming constant viscosity, the above Cauchy equations will lead to the Navier–Stokes equations below.

### Convective acceleration

A significant feature of the Cauchy equation and consequently all other continuum equations (including Euler and Navier–Stokes) is the presence of convective acceleration: the effect of acceleration of a flow with respect to space. While individual fluid particles indeed experience time-dependent acceleration, the convective acceleration of the flow field is a spatial effect, one example being fluid speeding up in a nozzle.

## Compressible flow

Remark: here, the deviatoric stress tensor is denoted ${\textstyle {\boldsymbol {\tau }}}$ as it was in the general continuum equations and in the incompressible flow section .

The compressible momentum Navier–Stokes equation results from the following assumptions on the Cauchy stress tensor:

- the stress is Galilean invariant : it does not depend directly on the flow velocity, but only on spatial derivatives of the flow velocity. So the stress variable is the tensor gradient ${\textstyle \nabla \mathbf {u} }$ , or more simply the rate-of-strain tensor : ${\textstyle {\boldsymbol {\varepsilon }}\left(\nabla \mathbf {u} \right)\equiv {\frac {1}{2}}\nabla \mathbf {u} +{\frac {1}{2}}\left(\nabla \mathbf {u} \right)^{\mathsf {T}}}$

- the deviatoric stress is linear in this variable: ${\textstyle {\boldsymbol {\sigma }}({\boldsymbol {\varepsilon }})=-p\mathbf {I} +\mathbf {C} :{\boldsymbol {\varepsilon }}}$ , where ${\textstyle p}$ is independent on the strain rate tensor, ${\textstyle \mathbf {C} }$ is the fourth-order tensor representing the constant of proportionality, called the viscosity or elasticity tensor , and : is the double-dot product .

- the fluid is assumed to be isotropic , as with gases and simple liquids, and consequently ${\textstyle \mathbf {C} }$ is an isotropic tensor; furthermore, since the deviatoric stress tensor is symmetric, by Helmholtz decomposition it can be expressed in terms of two scalar Lamé parameters , the second viscosity ${\textstyle \lambda }$ and the dynamic viscosity ${\textstyle \mu }$ , as it is usual in linear elasticity : Linear stress constitutive equation (expression similar to the one for elastic solid) ${\boldsymbol {\sigma }}({\boldsymbol {\varepsilon }})=-p\mathbf {I} +\lambda \operatorname {tr} ({\boldsymbol {\varepsilon }})\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}$ where ${\textstyle \mathbf {I} }$ is the identity tensor , and ${\textstyle \operatorname {tr} ({\boldsymbol {\varepsilon }})}$ is the trace of the rate-of-strain tensor. So this decomposition can be explicitly defined as: ${\boldsymbol {\sigma }}=-p\mathbf {I} +\lambda (\nabla \cdot \mathbf {u} )\mathbf {I} +\mu \left(\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right).$

${\boldsymbol {\sigma }}({\boldsymbol {\varepsilon }})=-p\mathbf {I} +\lambda \operatorname {tr} ({\boldsymbol {\varepsilon }})\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}$

where ${\textstyle \mathbf {I} }$ is the identity tensor , and ${\textstyle \operatorname {tr} ({\boldsymbol {\varepsilon }})}$ is the trace of the rate-of-strain tensor. So this decomposition can be explicitly defined as: ${\boldsymbol {\sigma }}=-p\mathbf {I} +\lambda (\nabla \cdot \mathbf {u} )\mathbf {I} +\mu \left(\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right).$

Since the trace of the rate-of-strain tensor in three dimensions is the divergence (i.e. rate of expansion) of the flow: $\operatorname {tr} ({\boldsymbol {\varepsilon }})=\nabla \cdot \mathbf {u} .$

Given this relation, and since the trace of the identity tensor in three dimensions is three: $\operatorname {tr} ({\boldsymbol {I}})=3.$

the trace of the stress tensor in three dimensions becomes: $\operatorname {tr} ({\boldsymbol {\sigma }})=-3p+(3\lambda +2\mu )\nabla \cdot \mathbf {u} .$

So by alternatively decomposing the stress tensor into isotropic and deviatoric parts, as usual in fluid dynamics: ${\boldsymbol {\sigma }}=-\left[p-\left(\lambda +{\tfrac {2}{3}}\mu \right)\left(\nabla \cdot \mathbf {u} \right)\right]\mathbf {I} +\mu \left(\nabla \mathbf {u} +\left(\nabla \mathbf {u} \right)^{\mathsf {T}}-{\tfrac {2}{3}}\left(\nabla \cdot \mathbf {u} \right)\mathbf {I} \right)$

Introducing the bulk viscosity ${\textstyle \zeta }$ , $\zeta \equiv \lambda +{\tfrac {2}{3}}\mu ,$

we arrive at the linear constitutive equation in the form usually employed in thermal hydraulics :

${\boldsymbol {\sigma }}=-{\bigl [}p-\zeta (\nabla \cdot \mathbf {u} ){\bigr ]}\mathbf {I} +\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]$

which can also be arranged in the other usual form: ${\boldsymbol {\sigma }}=-p\mathbf {I} +\mu \left(\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right)+\left(\zeta -{\tfrac {2}{3}}\mu \right)(\nabla \cdot \mathbf {u} )\mathbf {I} .$

Note that in the compressible case the pressure is no more proportional to the isotropic stress term, since there is the additional bulk viscosity term: $p=-{\tfrac {1}{3}}\operatorname {tr} ({\boldsymbol {\sigma }})+\zeta (\nabla \cdot \mathbf {u} )$

and the deviatoric stress tensor ${\boldsymbol {\sigma }}'$ is still coincident with the shear stress tensor ${\boldsymbol {\tau }}$ (i.e. the deviatoric stress in a Newtonian fluid has no normal stress components), and it has a compressibility term in addition to the incompressible case, which is proportional to the shear viscosity:

${\boldsymbol {\sigma }}'={\boldsymbol {\tau }}=\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]$

Both bulk viscosity ${\textstyle \zeta }$ and dynamic viscosity ${\textstyle \mu }$ need not be constant – in general, they depend on two thermodynamics variables if the fluid contains a single chemical species, say for example, pressure and temperature. Any equation that makes explicit one of these transport coefficient in the conservation variables is called an equation of state .

The most general of the Navier–Stokes equations become

$\rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\nabla [\zeta (\nabla \cdot \mathbf {u} )]+\rho \mathbf {a} .$

in index notation, the equation can be written as

$\rho \left({\frac {\partial u_{i}}{\partial t}}+u_{k}{\frac {\partial u_{i}}{\partial x_{k}}}\right)=-{\frac {\partial p}{\partial x_{i}}}+{\frac {\partial }{\partial x_{k}}}\left[\mu \left({\frac {\partial u_{i}}{\partial x_{k}}}+{\frac {\partial u_{k}}{\partial x_{i}}}-{\tfrac {2}{3}}\delta _{ik}{\frac {\partial u_{l}}{\partial x_{l}}}\right)\right]+{\frac {\partial }{\partial x_{i}}}\left(\zeta {\frac {\partial u_{\ell }}{\partial x_{\ell }}}\right)+\rho a_{i}.$

The corresponding equation in conservation form can be obtained by considering that, given the mass continuity equation , the left side is equivalent to:

$\rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}={\frac {\partial }{\partial t}}(\rho \mathbf {u} )+\nabla \cdot (\rho \mathbf {u} \otimes \mathbf {u} )$

to give finally:

${\frac {\partial }{\partial t}}(\rho \mathbf {u} )+\nabla \cdot \left(\rho \mathbf {u} \otimes \mathbf {u} +[p-\zeta (\nabla \cdot \mathbf {u} )]\mathbf {I} -\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)=\rho \mathbf {a} .$

Apart from its dependence of pressure and temperature, the second viscosity coefficient also depends on the process, that is to say, the second viscosity coefficient is not just a material property. Example: in the case of a sound wave with a definitive frequency that alternatively compresses and expands a fluid element, the second viscosity coefficient depends on the frequency of the wave. This dependence is called the dispersion . In some cases, the second viscosity ${\textstyle \zeta }$ can be assumed to be constant in which case, the effect of the volume viscosity ${\textstyle \zeta }$ is that the mechanical pressure is not equivalent to the thermodynamic pressure : as demonstrated below. ${\begin{aligned}&\nabla \cdot (\nabla \cdot \mathbf {u} )\mathbf {I} =\nabla (\nabla \cdot \mathbf {u} ),\\&{\bar {p}}\equiv p-\zeta \,\nabla \cdot \mathbf {u} ,\end{aligned}}$ However, this difference is usually neglected most of the time (that is whenever we are not dealing with processes such as sound absorption and attenuation of shock waves, where second viscosity coefficient becomes important) by explicitly assuming ${\textstyle \zeta =0}$ . The assumption of setting ${\textstyle \zeta =0}$ is called as the Stokes hypothesis . The validity of Stokes hypothesis can be demonstrated for monoatomic gas both experimentally and from the kinetic theory; for other gases and liquids, Stokes hypothesis is generally incorrect. With the Stokes hypothesis, the Navier–Stokes equations become

$\rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\rho \mathbf {a} .$

If the dynamic $\mu$ and bulk $\zeta$ viscosities are assumed to be uniform in space, the equations in convective form can be simplified further. By computing the divergence of the stress tensor, since the divergence of tensor ${\textstyle \nabla \mathbf {u} }$ is ${\textstyle \nabla ^{2}\mathbf {u} }$ and the divergence of tensor ${\textstyle \left(\nabla \mathbf {u} \right)^{\mathsf {T}}}$ is ${\textstyle \nabla \left(\nabla \cdot \mathbf {u} \right)}$ , one finally arrives to the compressible Navier–Stokes momentum equation:

${\frac {D\mathbf {u} }{Dt}}=-{\frac {1}{\rho }}\nabla p+\nu \,\nabla ^{2}\mathbf {u} +\left({\tfrac {1}{3}}\nu +\xi \right)\,\nabla (\nabla \cdot \mathbf {u} )+\mathbf {a} .$

where ${\textstyle {\frac {\mathrm {D} }{\mathrm {D} t}}}$ is the material derivative . ${\textstyle \nu ={\frac {\mu }{\rho }}}$ is the shear kinematic viscosity and ${\textstyle \xi ={\frac {\zeta }{\rho }}}$ is the bulk kinematic viscosity. The left-hand side changes in the conservation form of the Navier–Stokes momentum equation.
By bringing the operator on the flow velocity on the left side, one also has:

$\left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla -\nu \,\nabla ^{2}-\left({\tfrac {1}{3}}\nu +\xi \right)\,\nabla (\nabla \cdot )\right)\mathbf {u} =-{\frac {1}{\rho }}\nabla p+\mathbf {a} .$

The convective acceleration term can also be written as $\mathbf {u} \cdot \nabla \mathbf {u} =(\nabla \times \mathbf {u} )\times \mathbf {u} +{\tfrac {1}{2}}\nabla \mathbf {u} ^{2},$ where the vector ${\textstyle (\nabla \times \mathbf {u} )\times \mathbf {u} }$ is known as the Lamb vector .

For the special case of an incompressible flow , the pressure constrains the flow so that the volume of fluid elements is constant: isochoric flow resulting in a solenoidal velocity field with ${\textstyle \nabla \cdot \mathbf {u} =0}$ .

## Incompressible flow

The incompressible momentum Navier–Stokes equation results from the following assumptions on the Cauchy stress tensor:

- the stress is Galilean invariant : it does not depend directly on the flow velocity, but only on spatial derivatives of the flow velocity. So the stress variable is the tensor gradient ${\textstyle \nabla \mathbf {u} }$ .

- the fluid is assumed to be isotropic , as with gases and simple liquids, and consequently ${\textstyle {\boldsymbol {\tau }}}$ is an isotropic tensor; furthermore, since the deviatoric stress tensor can be expressed in terms of the dynamic viscosity ${\textstyle \mu }$ : Stokes' stress constitutive equation (expression used for incompressible elastic solids) ${\boldsymbol {\tau }}=2\mu {\boldsymbol {\varepsilon }}$ where ${\boldsymbol {\varepsilon }}={\tfrac {1}{2}}\left(\mathbf {\nabla u} +\mathbf {\nabla u} ^{\mathsf {T}}\right)$ is the rate-of- strain tensor . So this decomposition can be made explicit as: Stokes's stress constitutive equation (expression used for incompressible viscous fluids) ${\boldsymbol {\tau }}=\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right]$

${\boldsymbol {\tau }}=2\mu {\boldsymbol {\varepsilon }}$

where ${\boldsymbol {\varepsilon }}={\tfrac {1}{2}}\left(\mathbf {\nabla u} +\mathbf {\nabla u} ^{\mathsf {T}}\right)$ is the rate-of- strain tensor . So this decomposition can be made explicit as:

${\boldsymbol {\tau }}=\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right]$

This is constitutive equation is also called the Newtonian law of viscosity .
Dynamic viscosity μ need not be constant – in incompressible flows it can depend on density and on pressure. Any equation that makes explicit one of these transport coefficient in the conservative variables is called an equation of state .

The divergence of the deviatoric stress in case of uniform viscosity is given by: $\nabla \cdot {\boldsymbol {\tau }}=2\mu \nabla \cdot {\boldsymbol {\varepsilon }}=\mu \nabla \cdot \left(\nabla \mathbf {u} +\nabla \mathbf {u} ^{\mathsf {T}}\right)=\mu \,\nabla ^{2}\mathbf {u}$ because ${\textstyle \nabla \cdot \mathbf {u} =0}$ for an incompressible fluid.

Incompressibility rules out density and pressure waves like sound or shock waves , so this simplification is not useful if these phenomena are of interest. The incompressible flow assumption typically holds well with all fluids at low Mach numbers (say up to about Mach 0.3), such as for modelling air winds at normal temperatures. the incompressible Navier–Stokes equations are best visualized by dividing for the density:

${\frac {D\mathbf {u} }{Dt}}={\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} =\nu \,\nabla ^{2}\mathbf {u} -{\frac {1}{\rho }}\nabla p+{\frac {1}{\rho }}\mathbf {f}$

where ${\textstyle \nu ={\frac {\mu }{\rho }}}$ is called the kinematic viscosity . 
By isolating the fluid velocity, one can also state:

$\left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla -\nu \,\nabla ^{2}\right)\mathbf {u} =-{\frac {1}{\rho }}\nabla p+{\frac {1}{\rho }}\mathbf {f} .$

If the density is constant throughout the fluid domain, or, in other words, if all fluid elements have the same density, ${\textstyle \rho }$ , then we have

${\frac {D\mathbf {u} }{Dt}}=\nu \,\nabla ^{2}\mathbf {u} -\nabla {\frac {p}{\rho }}+{\frac {1}{\rho }}\mathbf {f} ,$

where ${\textstyle {\frac {p}{\rho }}}$ is called the unit pressure head .

In incompressible flows, the pressure field satisfies the Poisson equation ,

$\nabla ^{2}p=-\rho {\frac {\partial u_{i}}{\partial x_{k}}}{\frac {\partial u_{k}}{\partial x_{i}}}=-\rho {\frac {\partial ^{2}u_{i}u_{k}}{\partial x_{k}x_{i}}},$

which is obtained by taking the divergence of the momentum equations.

Velocity profile (laminar flow): $u_{x}=u(y),\quad u_{y}=0,\quad u_{z}=0$ for the x -direction, simplify the Navier–Stokes equation: $0=-{\frac {\mathrm {d} P}{\mathrm {d} x}}+\mu \left({\frac {\mathrm {d} ^{2}u}{\mathrm {d} y^{2}}}\right)$

Integrate twice to find the velocity profile with boundary conditions $y=h,\ u=0$ ; $y=-h,\ u=0$ : $u={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}y^{2}+Ay+B$

From this equation, substitute in the two boundary conditions to get two equations: ${\begin{aligned}0&={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}+Ah+B\\0&={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}-Ah+B\end{aligned}}$

Add and solve for $B$ : $B=-{\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}$

Substitute and solve for $A$ : $A=0$

Finally this gives the velocity profile: $u={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}\left(y^{2}-h^{2}\right)$

It is well worth observing the meaning of each term (compare to the Cauchy momentum equation ):

$\overbrace {{\vphantom {\frac {}{}}}\underbrace {\frac {\partial \mathbf {u} }{\partial t}} _{\text{Variation}}+\underbrace {{\vphantom {\frac {}{}}}(\mathbf {u} \cdot \nabla )\mathbf {u} } _{\begin{smallmatrix}{\text{Convective}}\\{\text{acceleration}}\end{smallmatrix}}} ^{\text{Inertia (per volume)}}=\overbrace {{\vphantom {\frac {\partial }{\partial }}}\underbrace {{\vphantom {\frac {}{}}}-\nabla w} _{\begin{smallmatrix}{\text{Internal}}\\{\text{source}}\end{smallmatrix}}+\underbrace {{\vphantom {\frac {}{}}}\nu \nabla ^{2}\mathbf {u} } _{\text{Diffusion}}} ^{\text{Divergence of stress}}+\underbrace {{\vphantom {\frac {}{}}}\mathbf {g} } _{\begin{smallmatrix}{\text{External}}\\{\text{source}}\end{smallmatrix}}.$

The higher-order term, namely the shear stress divergence ${\textstyle \nabla \cdot {\boldsymbol {\tau }}}$ , has simply reduced to the vector Laplacian term ${\textstyle \mu \nabla ^{2}\mathbf {u} }$ . This Laplacian term can be interpreted as the difference between the velocity at a point and the mean velocity in a small surrounding volume. This implies that – for a Newtonian fluid – viscosity operates as a diffusion of momentum , in much the same way as the heat conduction . In fact neglecting the convection term, incompressible Navier–Stokes equations lead to a vector diffusion equation (namely Stokes equations ), but in general the convection term is present, so incompressible Navier–Stokes equations belong to the class of convection–diffusion equations .

In the usual case of an external field being a conservative field : $\mathbf {g} =-\nabla \varphi$ by defining the hydraulic head : $h\equiv w+\varphi$

one can finally condense the whole source in one term, arriving to the incompressible Navier–Stokes equation with conservative external field: ${\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} -\nu \,\nabla ^{2}\mathbf {u} =-\nabla h.$

The incompressible Navier–Stokes equations with uniform density and viscosity and conservative external field is the fundamental equation of hydraulics . The domain for these equations is commonly a 3 or fewer dimensional Euclidean space , for which an orthogonal coordinate reference frame is usually set to explicit the system of scalar partial differential equations to be solved. In 3-dimensional orthogonal coordinate systems are 3: Cartesian , cylindrical , and spherical . Expressing the Navier–Stokes vector equation in Cartesian coordinates is quite straightforward and not much influenced by the number of dimensions of the euclidean space employed, and this is the case also for the first-order terms (like the variation and convection ones) also in non-cartesian orthogonal coordinate systems. But for the higher order terms (the two coming from the divergence of the deviatoric stress that distinguish Navier–Stokes equations from Euler equations) some tensor calculus is required for deducing an expression in non-cartesian orthogonal coordinate systems.
A special case of the fundamental equation of hydraulics is the Bernoulli's equation .

The incompressible Navier–Stokes equation is composite, the sum of two orthogonal equations, ${\begin{aligned}{\frac {\partial \mathbf {u} }{\partial t}}&=\Pi ^{S}\left(-(\mathbf {u} \cdot \nabla )\mathbf {u} +\nu \,\nabla ^{2}\mathbf {u} \right)+\mathbf {f} ^{S}\\\rho ^{-1}\,\nabla p&=\Pi ^{I}\left(-(\mathbf {u} \cdot \nabla )\mathbf {u} +\nu \,\nabla ^{2}\mathbf {u} \right)+\mathbf {f} ^{I}\end{aligned}}$ where ${\textstyle \Pi ^{S}}$ and ${\textstyle \Pi ^{I}}$ are solenoidal and irrotational projection operators satisfying ${\textstyle \Pi ^{S}+\Pi ^{I}=1}$ , and ${\textstyle \mathbf {f} ^{S}}$ and ${\textstyle \mathbf {f} ^{I}}$ are the non-conservative and conservative parts of the body force. This result follows from the Helmholtz theorem (also known as the fundamental theorem of vector calculus). The first equation is a pressureless governing equation for the velocity, while the second equation for the pressure is a functional of the velocity and is related to the pressure Poisson equation.

The explicit functional form of the projection operator in 3D is found from the Helmholtz theorem: $\Pi ^{S}\,\mathbf {F} (\mathbf {r} )={\frac {1}{4\pi }}\nabla \times \int {\frac {\nabla ^{\prime }\times \mathbf {F} (\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}}\,\mathrm {d} V',\quad \Pi ^{I}=1-\Pi ^{S}$ with a similar structure in 2D. Thus the governing equation is an integro-differential equation similar to Coulomb's and Biot–Savart's law , not convenient for numerical computation.

An equivalent weak or variational form of the equation, proved to produce the same velocity solution as the Navier–Stokes equation, is given by, $\left(\mathbf {w} ,{\frac {\partial \mathbf {u} }{\partial t}}\right)=-{\bigl (}\mathbf {w} ,\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} {\bigr )}-\nu \left(\nabla \mathbf {w} :\nabla \mathbf {u} \right)+\left(\mathbf {w} ,\mathbf {f} ^{S}\right)$

for divergence-free test functions ${\textstyle \mathbf {w} }$ satisfying appropriate boundary conditions. Here, the projections are accomplished by the orthogonality of the solenoidal and irrotational function spaces. The discrete form of this is eminently suited to finite element computation of divergence-free flow, as we shall see in the next section. There, one will be able to address the question, "How does one specify pressure-driven (Poiseuille) problems with a pressureless governing equation?".

The absence of pressure forces from the governing velocity equation demonstrates that the equation is not a dynamic one, but rather a kinematic equation where the divergence-free condition serves the role of a conservation equation. This would seem to refute the frequent statements that the incompressible pressure enforces the divergence-free condition.

### Weak form of the incompressible Navier–Stokes equations

#### Strong form

Consider the incompressible Navier–Stokes equations for a Newtonian fluid of constant density ${\textstyle \rho }$ in a domain $\Omega \subset \mathbb {R} ^{d}\quad (d=2,3)$ with boundary $\partial \Omega =\Gamma _{D}\cup \Gamma _{N},$ being ${\textstyle \Gamma _{D}}$ and ${\textstyle \Gamma _{N}}$ portions of the boundary where respectively a Dirichlet and a Neumann boundary condition is applied ( ${\textstyle \Gamma _{D}\cap \Gamma _{N}=\emptyset }$ ): ${\begin{cases}\rho {\dfrac {\partial \mathbf {u} }{\partial t}}+\rho (\mathbf {u} \cdot \nabla )\mathbf {u} -\nabla \cdot {\boldsymbol {\sigma }}(\mathbf {u} ,p)=\mathbf {f} &{\text{ in }}\Omega \times (0,T)\\\nabla \cdot \mathbf {u} =0&{\text{ in }}\Omega \times (0,T)\\\mathbf {u} =\mathbf {g} &{\text{ on }}\Gamma _{D}\times (0,T)\\{\boldsymbol {\sigma }}(\mathbf {u} ,p){\hat {\mathbf {n} }}=\mathbf {h} &{\text{ on }}\Gamma _{N}\times (0,T)\\\mathbf {u} (0)=\mathbf {u} _{0}&{\text{ in }}\Omega \times \{0\}\end{cases}}$ ${\textstyle \mathbf {u} }$ is the fluid velocity, ${\textstyle p}$ the fluid pressure, ${\textstyle \mathbf {f} }$ a given forcing term, ${\hat {\mathbf {n} }}$ the outward directed unit normal vector to ${\textstyle \Gamma _{N}}$ , and ${\textstyle {\boldsymbol {\sigma }}(\mathbf {u} ,p)}$ the viscous stress tensor defined as: ${\boldsymbol {\sigma }}(\mathbf {u} ,p)=-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} ).$ Let ${\textstyle \mu }$ be the dynamic viscosity of the fluid, ${\textstyle \mathbf {I} }$ the second-order identity tensor and ${\textstyle {\boldsymbol {\varepsilon }}(\mathbf {u} )}$ the strain-rate tensor defined as: ${\boldsymbol {\varepsilon }}(\mathbf {u} )={\tfrac {1}{2}}\left(\left(\nabla \mathbf {u} \right)+\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right).$ The functions ${\textstyle \mathbf {g} }$ and ${\textstyle \mathbf {h} }$ are given Dirichlet and Neumann boundary data, while ${\textstyle \mathbf {u} _{0}}$ is the initial condition . The first equation is the momentum balance equation, while the second represents the mass conservation , namely the continuity equation . 
Assuming constant dynamic viscosity, using the vectorial identity $\nabla \cdot \left(\nabla \mathbf {f} \right)^{\mathsf {T}}=\nabla (\nabla \cdot \mathbf {f} )$ and exploiting mass conservation, the divergence of the total stress tensor in the momentum equation can also be expressed as: ${\begin{aligned}\nabla \cdot {\boldsymbol {\sigma }}(\mathbf {u} ,p)&=\nabla \cdot \left(-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} )\right)\\&=-\nabla p+2\mu \nabla \cdot {\boldsymbol {\varepsilon }}(\mathbf {u} )\\&=-\nabla p+2\mu \nabla \cdot \left[{\tfrac {1}{2}}\left(\left(\nabla \mathbf {u} \right)+\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\right]\\&=-\nabla p+\mu \left(\Delta \mathbf {u} +\nabla \cdot \left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\\&=-\nabla p+\mu {\bigl (}\Delta \mathbf {u} +\nabla \underbrace {(\nabla \cdot \mathbf {u} )} _{=0}{\bigr )}=-\nabla p+\mu \,\Delta \mathbf {u} .\end{aligned}}$ Moreover, note that the Neumann boundary conditions can be rearranged as: ${\boldsymbol {\sigma }}(\mathbf {u} ,p){\hat {\mathbf {n} }}={\bigl (}-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} ){\bigr )}{\hat {\mathbf {n} }}=-p{\hat {\mathbf {n} }}+\mu {\frac {\partial {\boldsymbol {u}}}{\partial {\hat {\mathbf {n} }}}}.$

#### Weak form

In order to find the weak form of the Navier–Stokes equations, firstly, consider the momentum equation $\rho {\frac {\partial \mathbf {u} }{\partial t}}-\mu \Delta \mathbf {u} +\rho (\mathbf {u} \cdot \nabla )\mathbf {u} +\nabla p=\mathbf {f}$ multiply it for a test function ${\textstyle \mathbf {v} }$ , defined in a suitable space ${\textstyle V}$ , and integrate both members with respect to the domain ${\textstyle \Omega }$ : $\int \limits _{\Omega }\rho {\frac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} -\int \limits _{\Omega }\mu \Delta \mathbf {u} \cdot \mathbf {v} +\int \limits _{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} +\int \limits _{\Omega }\nabla p\cdot \mathbf {v} =\int \limits _{\Omega }\mathbf {f} \cdot \mathbf {v}$ Counter-integrating by parts the diffusive and the pressure terms and by using Gauss's theorem: ${\begin{aligned}-\int \limits _{\Omega }\mu \Delta \mathbf {u} \cdot \mathbf {v} &=\int \limits _{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} -\int \limits _{\partial \Omega }\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}\cdot \mathbf {v} \\\int \limits _{\Omega }\nabla p\cdot \mathbf {v} &=-\int \limits _{\Omega }p\nabla \cdot \mathbf {v} +\int \limits _{\partial \Omega }p\mathbf {v} \cdot {\hat {\mathbf {n} }}\end{aligned}}$

Using these relations, one gets: $\int \limits _{\Omega }\rho {\dfrac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} +\int \limits _{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} +\int \limits _{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} -\int \limits _{\Omega }p\nabla \cdot \mathbf {v} =\int \limits _{\Omega }\mathbf {f} \cdot \mathbf {v} +\int \limits _{\partial \Omega }\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} \quad \forall \mathbf {v} \in V.$ In the same fashion, the continuity equation is multiplied for a test function ${\textstyle q}$ belonging to a space ${\textstyle Q}$ and integrated in the domain ${\textstyle \Omega }$ : $\int \limits _{\Omega }q\nabla \cdot \mathbf {u} =0.\quad \forall q\in Q.$ The space functions are chosen as follows: ${\begin{aligned}V=\left[H_{0}^{1}(\Omega )\right]^{d}&=\left\{\mathbf {v} \in \left[H^{1}(\Omega )\right]^{d}:\quad \mathbf {v} =\mathbf {0} {\text{ on }}\Gamma _{D}\right\},\\Q&=L^{2}(\Omega )\end{aligned}}$ Considering that the test function ${\textstyle \mathbf {v} }$ vanishes on the Dirichlet boundary and considering the Neumann condition, the integral on the boundary can be rearranged as: $\int \limits _{\partial \Omega }\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} =\underbrace {\int \limits _{\Gamma _{D}}\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} } _{\mathbf {v} =\mathbf {0} {\text{ on }}\Gamma _{D}\ }+\int \limits _{\Gamma _{N}}\underbrace {{\vphantom {\int \limits _{\Gamma _{N}}}}\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)} _{=\mathbf {h} {\text{ on }}\Gamma _{N}}\cdot \mathbf {v} =\int \limits _{\Gamma _{N}}\mathbf {h} \cdot \mathbf {v} .$ Having this in mind, the weak formulation of the Navier–Stokes equations is expressed as: ${\begin{aligned}&{\text{find }}\mathbf {u} \in L^{2}\left(\mathbb {R} ^{+}\;\left[H^{1}(\Omega )\right]^{d}\right)\cap C^{0}\left(\mathbb {R} ^{+}\;\left[L^{2}(\Omega )\right]^{d}\right){\text{ such that: }}\\[5pt]&\quad {\begin{cases}\displaystyle \int \limits _{\Omega }\rho {\dfrac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} +\int \limits _{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} +\int \limits _{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} -\int \limits _{\Omega }p\nabla \cdot \mathbf {v} =\int \limits _{\Omega }\mathbf {f} \cdot \mathbf {v} +\int \limits _{\Gamma _{N}}\mathbf {h} \cdot \mathbf {v} \quad \forall \mathbf {v} \in V,\\\displaystyle \int \limits _{\Omega }q\nabla \cdot \mathbf {u} =0\quad \forall q\in Q.\end{cases}}\end{aligned}}$

### Discrete velocity

With partitioning of the problem domain and defining basis functions on the partitioned domain, the discrete form of the governing equation is $\left(\mathbf {w} _{i},{\frac {\partial \mathbf {u} _{j}}{\partial t}}\right)=-{\bigl (}\mathbf {w} _{i},\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} _{j}{\bigr )}-\nu \left(\nabla \mathbf {w} _{i}:\nabla \mathbf {u} _{j}\right)+\left(\mathbf {w} _{i},\mathbf {f} ^{S}\right).$

It is desirable to choose basis functions that reflect the essential feature of incompressible flow – the elements must be divergence-free. While the velocity is the variable of interest, the existence of the stream function or vector potential is necessary by the Helmholtz theorem. Further, to determine fluid flow in the absence of a pressure gradient, one can specify the difference of stream function values across a 2D channel, or the line integral of the tangential component of the vector potential around the channel in 3D, the flow being given by Stokes' theorem . Discussion will be restricted to 2D in the following.

We further restrict discussion to continuous Hermite finite elements which have at least first-derivative degrees-of-freedom. With this, one can draw a large number of candidate triangular and rectangular elements from the plate-bending literature. These elements have derivatives as components of the gradient. In 2D, the gradient and curl of a scalar are clearly orthogonal, given by the expressions, ${\begin{aligned}\nabla \varphi &=\left({\frac {\partial \varphi }{\partial x}},\,{\frac {\partial \varphi }{\partial y}}\right)^{\mathsf {T}},\\[5pt]\nabla \times \varphi &=\left({\frac {\partial \varphi }{\partial y}},\,-{\frac {\partial \varphi }{\partial x}}\right)^{\mathsf {T}}.\end{aligned}}$

Adopting continuous plate-bending elements, interchanging the derivative degrees-of-freedom and changing the sign of the appropriate one gives many families of stream function elements.

Taking the curl of the scalar stream function elements gives divergence-free velocity elements. The requirement that the stream function elements be continuous assures that the normal component of the velocity is continuous across element interfaces, all that is necessary for vanishing divergence on these interfaces.

Boundary conditions are simple to apply. The stream function is constant on no-flow surfaces, with no-slip velocity conditions on surfaces.
Stream function differences across open channels determine the flow. No boundary conditions are necessary on open boundaries, though consistent values may be used with some problems. These are all Dirichlet conditions.

The algebraic equations to be solved are simple to set up, but of course are non-linear , requiring iteration of the linearized equations.

Similar considerations apply to three-dimensions, but extension from 2D is not immediate because of the vector nature of the potential, and there exists no simple relation between the gradient and the curl as was the case in 2D.

### Pressure recovery

Recovering pressure from the velocity field is easy. The discrete weak equation for the pressure gradient is, $(\mathbf {g} _{i},\nabla p)=-{\bigl (}\mathbf {g} _{i},\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} _{j}{\bigr )}-\nu \left(\nabla \mathbf {g} _{i}:\nabla \mathbf {u} _{j}\right)+\left(\mathbf {g} _{i},\mathbf {f} ^{I}\right)$

where the test/weight functions are irrotational. Any conforming scalar finite element may be used. However, the pressure gradient field may also be of interest. In this case, one can use scalar Hermite elements for the pressure. For the test/weight functions ${\textstyle \mathbf {g} _{i}}$ one would choose the irrotational vector elements obtained from the gradient of the pressure element.

## Non-inertial frame of reference

The rotating frame of reference introduces some interesting pseudo-forces into the equations through the material derivative term. Consider a stationary inertial frame of reference ${\textstyle K}$ , and a non-inertial frame of reference ${\textstyle K'}$ , which is translating with velocity ${\textstyle \mathbf {U} (t)}$ and rotating with angular velocity ${\textstyle \Omega (t)}$ with respect to the stationary frame. The Navier–Stokes equation observed from the non-inertial frame then becomes

${\begin{aligned}\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=&-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\nabla [\zeta (\nabla \cdot \mathbf {u} )]+\rho \mathbf {f} \\&-\rho \left[2\mathbf {\Omega } \times \mathbf {u} +\mathbf {\Omega } \times (\mathbf {\Omega } \times \mathbf {x} )+{\frac {\mathrm {d} \mathbf {U} }{\mathrm {d} t}}+{\frac {\mathrm {d} \mathbf {\Omega } }{\mathrm {d} t}}\times \mathbf {x} \right]\end{aligned}}$

Here ${\textstyle \mathbf {x} }$ and ${\textstyle \mathbf {u} }$ are measured in the non-inertial frame. The first term in the parenthesis represents Coriolis acceleration , the second term is due to centrifugal acceleration , the third is due to the linear acceleration of ${\textstyle K'}$ with respect to ${\textstyle K}$ and the fourth term is due to the angular acceleration of ${\textstyle K'}$ with respect to ${\textstyle K}$ .

## Other equations

The Navier–Stokes equations are strictly a statement of the balance of momentum. To fully describe fluid flow, more information is needed, how much depending on the assumptions made. This additional information may include boundary data ( no-slip , capillary surface , etc.), conservation of mass, balance of energy , and/or an equation of state .

### Continuity equation for incompressible fluid

Regardless of the flow assumptions, a statement of the conservation of mass is generally necessary. This is achieved through the mass continuity equation , as discussed above in the "General continuum equations" within this article, as follows: ${\begin{aligned}{\frac {\mathbf {D} m}{\mathbf {Dt} }}&={\iiint \limits _{V}}\left({{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )}\right)dV\\{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot {\mathbf {u} })&={\frac {\partial \rho }{\partial t}}+({\nabla \rho })\cdot {\mathbf {u} }+{\rho }(\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+\nabla \cdot ({\rho \mathbf {u} })=0\end{aligned}}$ A fluid media for which the density $\rho$ is constant is called incompressible . Therefore, the rate of change of $\rho$ with respect to time ${\textstyle {\frac {\partial \rho }{\partial t}}}$ and the gradient of density ${\textstyle \nabla \rho }$ are equal to zero. In this case the general equation of continuity, ${\textstyle {\frac {\partial \rho }{\partial t}}+\nabla \cdot ({\rho \mathbf {u} })=0}$ , reduces to: $\rho (\nabla {\cdot }{\mathbf {u} })=0$ Furthermore, assuming that $\rho \neq 0$ means that the right-hand side of the equation (zero) is divisible by density $\rho$ . Therefore, the continuity equation for an incompressible fluid reduces further to: $(\nabla {\cdot {\mathbf {u} }})=0$ This relationship, ${\textstyle (\nabla {\cdot {\mathbf {u} }})=0}$ , identifies that the divergence of the flow velocity vector $\mathbf {u}$ is equal to zero, which means that for an incompressible fluid the flow velocity field is a solenoidal vector field or a divergence-free vector field . Note that this relationship can be expanded upon due to its uniqueness with the vector Laplace operator $\nabla ^{2}\mathbf {u} =\nabla (\nabla \cdot \mathbf {u} )-\nabla \times (\nabla \times \mathbf {u} )$ , and vorticity ${\boldsymbol {\omega }}=\nabla \times \mathbf {u}$ which is now expressed like so, for an incompressible fluid : $\nabla ^{2}\mathbf {u} =-{\bigl (}\nabla \times (\nabla \times \mathbf {u} ){\bigr )}=-(\nabla \times {\boldsymbol {\omega }})$

## Stream function for incompressible 2D fluid

Taking the curl of the incompressible Navier–Stokes equation results in the elimination of pressure. This is especially easy to see if 2D Cartesian flow is assumed (like in the degenerate 3D case with ${\textstyle u_{z}=0}$ and no dependence of anything on ${\textstyle z}$ ), where the equations reduce to: ${\begin{aligned}\rho \left({\frac {\partial u_{x}}{\partial t}}+u_{x}{\frac {\partial u_{x}}{\partial x}}+u_{y}{\frac {\partial u_{x}}{\partial y}}\right)&=-{\frac {\partial p}{\partial x}}+\mu \left({\frac {\partial ^{2}u_{x}}{\partial x^{2}}}+{\frac {\partial ^{2}u_{x}}{\partial y^{2}}}\right)+\rho g_{x}\\\rho \left({\frac {\partial u_{y}}{\partial t}}+u_{x}{\frac {\partial u_{y}}{\partial x}}+u_{y}{\frac {\partial u_{y}}{\partial y}}\right)&=-{\frac {\partial p}{\partial y}}+\mu \left({\frac {\partial ^{2}u_{y}}{\partial x^{2}}}+{\frac {\partial ^{2}u_{y}}{\partial y^{2}}}\right)+\rho g_{y}.\end{aligned}}$

Differentiating the first with respect to ${\textstyle y}$ , the second with respect to ${\textstyle x}$ and subtracting the resulting equations will eliminate pressure and any conservative force . 
For incompressible flow, defining the stream function ${\textstyle \psi }$ through $u_{x}={\frac {\partial \psi }{\partial y}};\quad u_{y}=-{\frac {\partial \psi }{\partial x}}$ results in mass continuity being unconditionally satisfied (given the stream function is continuous), and then incompressible Newtonian 2D momentum and mass conservation condense into one equation: ${\frac {\partial }{\partial t}}\left(\nabla ^{2}\psi \right)+{\frac {\partial \psi }{\partial y}}{\frac {\partial }{\partial x}}\left(\nabla ^{2}\psi \right)-{\frac {\partial \psi }{\partial x}}{\frac {\partial }{\partial y}}\left(\nabla ^{2}\psi \right)=\nu \nabla ^{4}\psi$

where ${\textstyle \nabla ^{4}}$ is the 2D biharmonic operator and ${\textstyle \nu }$ is the kinematic viscosity , ${\textstyle \nu ={\frac {\mu }{\rho }}}$ . We can also express this compactly using the Jacobian determinant : ${\frac {\partial }{\partial t}}\left(\nabla ^{2}\psi \right)+{\frac {\partial \left(\psi ,\nabla ^{2}\psi \right)}{\partial (y,x)}}=\nu \nabla ^{4}\psi .$

This single equation together with appropriate boundary conditions describes 2D fluid flow, taking only kinematic viscosity as a parameter. Note that the equation for creeping flow results when the left side is assumed zero.

In axisymmetric flow another stream function formulation, called the Stokes stream function , can be used to describe the velocity components of an incompressible flow with one scalar function.

The incompressible Navier–Stokes equation is a differential algebraic equation , having the inconvenient feature that there is no explicit mechanism for advancing the pressure in time. Consequently, much effort has been expended to eliminate the pressure from all or part of the computational process. The stream function formulation eliminates the pressure but only in two dimensions and at the expense of introducing higher derivatives and elimination of the velocity, which is the primary variable of interest.

## Properties

### Nonlinearity

The Navier–Stokes equations are nonlinear partial differential equations in the general case and so remain in almost every real situation. In some cases, such as one-dimensional flow and Stokes flow (or creeping flow), the equations can be simplified to linear equations. The nonlinearity makes most problems difficult or impossible to solve and is the main contributor to the turbulence that the equations model.

The nonlinearity is due to convective acceleration, which is an acceleration associated with the change in velocity over position. Hence, any convective flow, whether turbulent or not, will involve nonlinearity. An example of convective but laminar (nonturbulent) flow would be the passage of a viscous fluid (for example, oil) through a small converging nozzle . Such flows, whether exactly solvable or not, can often be thoroughly studied and understood.

### Turbulence

Turbulence is the time-dependent chaotic behaviour seen in many fluid flows. It is generally believed that it is due to the inertia of the fluid as a whole: the culmination of time-dependent and convective acceleration; hence flows where inertial effects are small tend to be laminar (the Reynolds number quantifies how much the flow is affected by inertia). It is believed, though not known with certainty, that the Navier–Stokes equations describe turbulence properly.

The numerical solution of the Navier–Stokes equations for turbulent flow is extremely difficult, and due to the significantly different mixing-length scales that are involved in turbulent flow, the stable solution of this requires such a fine mesh resolution that the computational time becomes significantly infeasible for calculation or direct numerical simulation . Attempts to solve turbulent flow using a laminar solver typically result in a time-unsteady solution, which fails to converge appropriately. To counter this, time-averaged equations such as the Reynolds-averaged Navier–Stokes equations (RANS), supplemented with turbulence models, are used in practical computational fluid dynamics (CFD) applications when modeling turbulent flows. Some models include the Spalart–Allmaras , k – ω , k – ε , and SST models, which add a variety of additional equations to bring closure to the RANS equations. Large eddy simulation (LES) can also be used to solve these equations numerically. This approach is computationally more expensive—in time and in computer memory—than RANS, but produces better results because it explicitly resolves the larger turbulent scales.

### Applicability

Together with supplemental equations (for example, conservation of mass) and well-formulated boundary conditions, the Navier–Stokes equations seem to model fluid motion accurately; even turbulent flows seem (on average) to agree with real world observations.

The Navier–Stokes equations assume that the fluid being studied is a continuum (it is infinitely divisible and not composed of particles such as atoms or molecules), and is not moving at relativistic velocities . At very small scales or under extreme conditions, real fluids made out of discrete molecules will produce results different from the continuous fluids modeled by the Navier–Stokes equations. For example, capillarity of internal layers in fluids appears for flow with high gradients. For large Knudsen number of the problem, the Boltzmann equation may be a suitable replacement. Failing that, one may have to resort to molecular dynamics or various hybrid methods.

Another limitation is simply the complicated nature of the equations. Time-tested formulations exist for common fluid families, but the application of the Navier–Stokes equations to less common families tends to result in very complicated formulations and often to open research problems. For this reason, these equations are usually written for Newtonian fluids where the viscosity model is linear ; truly general models for the flow of other kinds of fluids (such as blood) do not exist.

## Application to specific problems

The Navier–Stokes equations, even when written explicitly for specific fluids, are rather generic in nature and their proper application to specific problems can be very diverse. This is partly because there is an enormous variety of problems that may be modeled, ranging from as simple as the distribution of static pressure to as complicated as multiphase flow driven by surface tension .

Generally, application to specific problems begins with some flow assumptions and initial/boundary condition formulation, this may be followed by scale analysis to further simplify the problem.

### Parallel flow

Assume steady, parallel, one-dimensional, non-convective pressure-driven flow between parallel plates, the resulting scaled (dimensionless) boundary value problem is: ${\frac {\mathrm {d} ^{2}u}{\mathrm {d} y^{2}}}=-1;\quad u(0)=u(1)=0.$

The boundary condition is the no slip condition . This problem is easily solved for the flow field: $u(y)={\frac {y-y^{2}}{2}}.$

From this point onward, more quantities of interest can be easily obtained, such as viscous drag force or net flow rate.

### Radial flow

Difficulties may arise when the problem becomes slightly more complicated. A seemingly modest twist on the parallel flow above would be the radial flow between parallel plates; this involves convection and thus non-linearity. The velocity field may be represented by a function $f(z)$ that must satisfy: ${\frac {\mathrm {d} ^{2}f}{\mathrm {d} z^{2}}}+Rf^{2}=-1;\quad f(-1)=f(1)=0.$

This ordinary differential equation is what is obtained when the Navier–Stokes equations are written and the flow assumptions applied (additionally, the pressure gradient is solved for). The nonlinear term makes this a very difficult problem to solve analytically (a lengthy implicit solution may be found which involves elliptic integrals and roots of cubic polynomials ). Issues with the actual existence of solutions arise for ${\textstyle R>1.41}$ (approximately; this is not √ 2 ), the parameter ${\textstyle R}$ being the Reynolds number with appropriately chosen scales. This is an example of flow assumptions losing their applicability, and an example of the difficulty in "high" Reynolds number flows.

### Convection

A type of natural convection that can be described by the Navier–Stokes equation is the Rayleigh–Bénard convection . It is one of the most commonly studied convection phenomena because of its analytical and experimental accessibility.

## Exact solutions of the Navier–Stokes equations

Some exact solutions to the Navier–Stokes equations exist. Examples of degenerate cases—with the non-linear terms in the Navier–Stokes equations equal to zero—are Poiseuille flow , Couette flow and the oscillatory Stokes boundary layer . But also, more interesting examples, solutions to the full non-linear equations, exist, such as Jeffery–Hamel flow , Von Kármán swirling flow , stagnation point flow , Landau–Squire jet , and Taylor–Green vortex . Time-dependent self-similar solutions of the three-dimensional non-compressible Navier–Stokes equations in Cartesian coordinate can be given with the help of the Kummer's functions with quadratic arguments. For the compressible Navier–Stokes equations the time-dependent self-similar solutions are however the Whittaker functions again with quadratic arguments when the polytropic equation of state is used as a closing condition. Note that the existence of these exact solutions does not imply they are stable: turbulence may develop at higher Reynolds numbers.

Under additional assumptions, the component parts can be separated.

For example, in the case of an unbounded planar domain with two-dimensional — incompressible and stationary — flow in polar coordinates ( r , φ ) , the velocity components ( u r , u φ ) and pressure p are: ${\begin{aligned}u_{r}&={\frac {A}{r}},\\u_{\varphi }&=B\left({\frac {1}{r}}-r^{{\frac {A}{\nu }}+1}\right),\\p&=-{\frac {A^{2}+B^{2}}{2r^{2}}}-{\frac {2B^{2}\nu r^{\frac {A}{\nu }}}{A}}+{\frac {B^{2}r^{\left({\frac {2A}{\nu }}+2\right)}}{{\frac {2A}{\nu }}+2}}\end{aligned}}$

where A and B are arbitrary constants. This solution is valid in the domain r ≥ 1 and for A < −2 ν .

In Cartesian coordinates, when the viscosity is zero ( ν = 0 ), this is: ${\begin{aligned}\mathbf {v} (x,y)&={\frac {1}{x^{2}+y^{2}}}{\begin{pmatrix}Ax+By\\Ay-Bx\end{pmatrix}},\\p(x,y)&=-{\frac {A^{2}+B^{2}}{2\left(x^{2}+y^{2}\right)}}\end{aligned}}$

For example, in the case of an unbounded Euclidean domain with three-dimensional — incompressible, stationary and with zero viscosity ( ν = 0 ) — radial flow in Cartesian coordinates ( x , y , z ) , the velocity vector v and pressure p are: [ citation needed ] ${\begin{aligned}\mathbf {v} (x,y,z)&={\frac {A}{x^{2}+y^{2}+z^{2}}}{\begin{pmatrix}x\\y\\z\end{pmatrix}},\\p(x,y,z)&=-{\frac {A^{2}}{2\left(x^{2}+y^{2}+z^{2}\right)}}.\end{aligned}}$

There is a singularity at x = y = z = 0 .

### A three-dimensional steady-state vortex solution

A steady-state example with no singularities comes from considering the flow along the lines of a Hopf fibration . Let ${\textstyle r}$ be a constant radius of the inner coil. One set of solutions is given by: ${\begin{aligned}\rho (x,y,z)&={\frac {3B}{r^{2}+x^{2}+y^{2}+z^{2}}}\\p(x,y,z)&={\frac {-A^{2}B}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{3}}}\\\mathbf {u} (x,y,z)&={\frac {A}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{2}}}{\begin{pmatrix}2(-ry+xz)\\2(rx+yz)\\r^{2}-x^{2}-y^{2}+z^{2}\end{pmatrix}}\\g&=0\\\mu &=0\end{aligned}}$

for arbitrary constants ${\textstyle A}$ and ${\textstyle B}$ . This is a solution in a non-viscous gas (compressible fluid) whose density, velocities and pressure goes to zero far from the origin. (Note this is not a solution to the Clay Millennium problem because that refers to incompressible fluids where ${\textstyle \rho }$ is a constant, and neither does it deal with the uniqueness of the Navier–Stokes equations with respect to any turbulence properties.) It is also worth pointing out that the components of the velocity vector are exactly those from the Pythagorean quadruple parametrization. Other choices of density and pressure are possible with the same velocity field:

Another choice of pressure and density with the same velocity vector above is one where the pressure and density fall to zero at the origin and are highest in the central loop at z = 0 , x 2 + y 2 = r 2 : ${\begin{aligned}\rho (x,y,z)&={\frac {20B\left(x^{2}+y^{2}\right)}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{3}}}\\p(x,y,z)&={\frac {-A^{2}B}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{4}}}+{\frac {-4A^{2}B\left(x^{2}+y^{2}\right)}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{5}}}.\end{aligned}}$

In fact in general there are simple solutions for any polynomial function f where the density is: $\rho (x,y,z)={\frac {1}{r^{2}+x^{2}+y^{2}+z^{2}}}f\left({\frac {x^{2}+y^{2}}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{2}}}\right).$

### Viscous three-dimensional periodic solutions

Two examples of periodic fully-three-dimensional viscous solutions are described in. These solutions are defined on a three-dimensional torus $\mathbb {T} ^{3}=\mathbb {R} ^{3}/{L\mathbb {Z} ^{3}}$ and are characterized by positive and negative helicity respectively.
The solution with positive helicity is given by: ${\begin{aligned}u_{x}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U_{0}\left[\,\sin \left(kx-{\frac {\pi }{3}}\right)\cos \left(ky+{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{2}}\right)-\cos \left(kz-{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\\u_{y}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U_{0}\left[\,\sin \left(ky-{\frac {\pi }{3}}\right)\cos \left(kz+{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{2}}\right)-\cos \left(kx-{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\\u_{z}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U_{0}\left[\,\sin \left(kz-{\frac {\pi }{3}}\right)\cos \left(kx+{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{2}}\right)-\cos \left(ky-{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\end{aligned}}$ where $k=2\pi /L$ is the wave number and the velocity components are normalized so that the average kinetic energy per unit of mass is $U_{0}^{2}/2$ at $t=0$ .
The pressure field is obtained from the velocity field as $p=p_{0}-\rho _{0}\|{\boldsymbol {u}}\|^{2}/2$ (where $p_{0}$ and $\rho _{0}$ are reference values for the pressure and density fields respectively).
Since both the solutions belong to the class of Beltrami flow , the vorticity field is parallel to the velocity and, for the case with positive helicity, is given by $\omega ={\sqrt {3}}\,k\,{\boldsymbol {u}}$ . 
These solutions can be regarded as a generalization in three dimensions of the classic two-dimensional Taylor–Green vortex .

## Wyld diagrams

Wyld diagrams are bookkeeping graphs that correspond to the Navier–Stokes equations via a perturbation expansion of the fundamental continuum mechanics . Similar to the Feynman diagrams in quantum field theory , these diagrams are an extension of Mstislav Keldysh 's technique for nonequilibrium processes in fluid dynamics. [ citation needed ] In other words, these diagrams assign graphs to the (often) turbulent phenomena in turbulent fluids by allowing correlated and interacting fluid particles to obey stochastic processes associated to pseudo-random functions in probability distributions .

## Representations in 3D

Note that the formulas in this section make use of the single-line notation for partial derivatives, where, e.g. ${\textstyle \partial _{x}u}$ means the partial derivative of ${\textstyle u}$ with respect to ${\textstyle x}$ , and ${\textstyle \partial _{y}^{2}f_{\theta }}$ means the second-order partial derivative of ${\textstyle f_{\theta }}$ with respect to ${\textstyle y}$ .

A 2022 paper provides a less costly, dynamical and recurrent solution of the Navier-Stokes equation for 3D turbulent fluid flows. On suitably short time scales, the dynamics of turbulence is deterministic.

### Cartesian coordinates

From the general form of the Navier–Stokes, with the velocity vector expanded as ${\textstyle \mathbf {u} =(u_{x},u_{y},u_{z})}$ , sometimes respectively named ${\textstyle u}$ , ${\textstyle v}$ , ${\textstyle w}$ , we may write the vector equation explicitly, ${\begin{aligned}x:\ &\rho \left({\partial _{t}u_{x}}+u_{x}\,{\partial _{x}u_{x}}+u_{y}\,{\partial _{y}u_{x}}+u_{z}\,{\partial _{z}u_{x}}\right)\\&\quad =-\partial _{x}p+\mu \left({\partial _{x}^{2}u_{x}}+{\partial _{y}^{2}u_{x}}+{\partial _{z}^{2}u_{x}}\right)+{\frac {1}{3}}\mu \ \partial _{x}\left({\partial _{x}u_{x}}+{\partial _{y}u_{y}}+{\partial _{z}u_{z}}\right)+\rho g_{x}\\\end{aligned}}$ ${\begin{aligned}y:\ &\rho \left({\partial _{t}u_{y}}+u_{x}{\partial _{x}u_{y}}+u_{y}{\partial _{y}u_{y}}+u_{z}{\partial _{z}u_{y}}\right)\\&\quad =-{\partial _{y}p}+\mu \left({\partial _{x}^{2}u_{y}}+{\partial _{y}^{2}u_{y}}+{\partial _{z}^{2}u_{y}}\right)+{\frac {1}{3}}\mu \ \partial _{y}\left({\partial _{x}u_{x}}+{\partial _{y}u_{y}}+{\partial _{z}u_{z}}\right)+\rho g_{y}\\\end{aligned}}$ ${\begin{aligned}z:\ &\rho \left({\partial _{t}u_{z}}+u_{x}{\partial _{x}u_{z}}+u_{y}{\partial _{y}u_{z}}+u_{z}{\partial _{z}u_{z}}\right)\\&\quad =-{\partial _{z}p}+\mu \left({\partial _{x}^{2}u_{z}}+{\partial _{y}^{2}u_{z}}+{\partial _{z}^{2}u_{z}}\right)+{\frac {1}{3}}\mu \ \partial _{z}\left({\partial _{x}u_{x}}+{\partial _{y}u_{y}}+{\partial _{z}u_{z}}\right)+\rho g_{z}.\end{aligned}}$

Note that gravity has been accounted for as a body force, and the values of ${\textstyle g_{x}}$ , ${\textstyle g_{y}}$ , ${\textstyle g_{z}}$ will depend on the orientation of gravity with respect to the chosen set of coordinates.

The continuity equation reads: $\partial _{t}\rho +\partial _{x}(\rho u_{x})+\partial _{y}(\rho u_{y})+\partial _{z}(\rho u_{z})=0.$

When the flow is incompressible, ${\textstyle \rho }$ does not change for any fluid particle, and its material derivative vanishes: ${\textstyle {\frac {\mathrm {D} \rho }{\mathrm {D} t}}=0}$ . The continuity equation is reduced to: $\partial _{x}u_{x}+\partial _{y}u_{y}+\partial _{z}u_{z}=0.$

Thus, for the incompressible version of the Navier–Stokes equation the second part of the viscous terms fall away (see Incompressible flow ).

This system of four equations comprises the most commonly used and studied form. Though comparatively more compact than other representations, this is still a nonlinear system of partial differential equations for which solutions are difficult to obtain.

### Cylindrical coordinates

A change of variables on the Cartesian equations will yield the following momentum equations for ${\textstyle r}$ , ${\textstyle \phi }$ , and ${\textstyle z}$ ${\begin{aligned}r:\ &\rho \left({\partial _{t}u_{r}}+u_{r}{\partial _{r}u_{r}}+{\frac {u_{\varphi }}{r}}{\partial _{\varphi }u_{r}}+u_{z}{\partial _{z}u_{r}}-{\frac {u_{\varphi }^{2}}{r}}\right)\\&\quad =-{\partial _{r}p}\\&\qquad +\mu \left({\frac {1}{r}}\partial _{r}\left(r{\partial _{r}u_{r}}\right)+{\frac {1}{r^{2}}}{\partial _{\varphi }^{2}u_{r}}+{\partial _{z}^{2}u_{r}}-{\frac {u_{r}}{r^{2}}}-{\frac {2}{r^{2}}}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +{\frac {1}{3}}\mu \partial _{r}\left({\frac {1}{r}}{\partial _{r}\left(ru_{r}\right)}+{\frac {1}{r}}{\partial _{\varphi }u_{\varphi }}+{\partial _{z}u_{z}}\right)\\&\qquad +\rho g_{r}\\[8px]\end{aligned}}$ ${\begin{aligned}\varphi :\ &\rho \left({\partial _{t}u_{\varphi }}+u_{r}{\partial _{r}u_{\varphi }}+{\frac {u_{\varphi }}{r}}{\partial _{\varphi }u_{\varphi }}+u_{z}{\partial _{z}u_{\varphi }}+{\frac {u_{r}u_{\varphi }}{r}}\right)\\&\quad =-{\frac {1}{r}}{\partial _{\varphi }p}\\&\qquad +\mu \left({\frac {1}{r}}\ \partial _{r}\left(r{\partial _{r}u_{\varphi }}\right)+{\frac {1}{r^{2}}}{\partial _{\varphi }^{2}u_{\varphi }}+{\partial _{z}^{2}u_{\varphi }}-{\frac {u_{\varphi }}{r^{2}}}+{\frac {2}{r^{2}}}{\partial _{\varphi }u_{r}}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r}}\partial _{\varphi }\left({\frac {1}{r}}{\partial _{r}\left(ru_{r}\right)}+{\frac {1}{r}}{\partial _{\varphi }u_{\varphi }}+{\partial _{z}u_{z}}\right)\\&\qquad +\rho g_{\varphi }\\[8px]\end{aligned}}$ ${\begin{aligned}z:\ &\rho \left({\partial _{t}u_{z}}+u_{r}{\partial _{r}u_{z}}+{\frac {u_{\varphi }}{r}}{\partial _{\varphi }u_{z}}+u_{z}{\partial _{z}u_{z}}\right)\\&\quad =-{\partial _{z}p}\\&\qquad +\mu \left({\frac {1}{r}}\partial _{r}\left(r{\partial _{r}u_{z}}\right)+{\frac {1}{r^{2}}}{\partial _{\varphi }^{2}u_{z}}+{\partial _{z}^{2}u_{z}}\right)\\&\qquad +{\frac {1}{3}}\mu \partial _{z}\left({\frac {1}{r}}{\partial _{r}\left(ru_{r}\right)}+{\frac {1}{r}}{\partial _{\varphi }u_{\varphi }}+{\partial _{z}u_{z}}\right)\\&\qquad +\rho g_{z}.\end{aligned}}$

The gravity components will generally not be constants, however for most applications either the coordinates are chosen so that the gravity components are constant or else it is assumed that gravity is counteracted by a pressure field (for example, flow in horizontal pipe is treated normally without gravity and without a vertical pressure gradient). The continuity equation is: ${\partial _{t}\rho }+{\frac {1}{r}}\partial _{r}\left(\rho ru_{r}\right)+{\frac {1}{r}}{\partial _{\varphi }\left(\rho u_{\varphi }\right)}+{\partial _{z}\left(\rho u_{z}\right)}=0.$

This cylindrical representation of the incompressible Navier–Stokes equations is the second most commonly seen (the first being Cartesian above). Cylindrical coordinates are chosen to take advantage of symmetry, so that a velocity component can disappear. A very common case is axisymmetric flow with the assumption of no tangential velocity ( ${\textstyle u_{\phi }=0}$ ), and the remaining quantities are independent of ${\textstyle \phi }$ : ${\begin{aligned}\rho \left({\partial _{t}u_{r}}+u_{r}{\partial _{r}u_{r}}+u_{z}{\partial _{z}u_{r}}\right)&=-{\partial _{r}p}+\mu \left({\frac {1}{r}}\partial _{r}\left(r{\partial _{r}u_{r}}\right)+{\partial _{z}^{2}u_{r}}-{\frac {u_{r}}{r^{2}}}\right)+\rho g_{r}\\\rho \left({\partial _{t}u_{z}}+u_{r}{\partial _{r}u_{z}}+u_{z}{\partial _{z}u_{z}}\right)&=-{\partial _{z}p}+\mu \left({\frac {1}{r}}\partial _{r}\left(r{\partial _{r}u_{z}}\right)+{\partial _{z}^{2}u_{z}}\right)+\rho g_{z}\\{\frac {1}{r}}\partial _{r}\left(ru_{r}\right)+{\partial _{z}u_{z}}&=0.\end{aligned}}$

### Spherical coordinates

In spherical coordinates , the ${\textstyle r}$ , ${\textstyle \phi }$ , and ${\textstyle \theta }$ momentum equations are (note the convention used: ${\textstyle \theta }$ is polar angle, or colatitude , ${\textstyle 0\leq \theta \leq \pi }$ ): ${\begin{aligned}r:\ &\rho \left({\partial _{t}u_{r}}+u_{r}{\partial _{r}u_{r}}+{\frac {u_{\varphi }}{r\sin \theta }}{\partial _{\varphi }u_{r}}+{\frac {u_{\theta }}{r}}{\partial _{\theta }u_{r}}-{\frac {u_{\varphi }^{2}+u_{\theta }^{2}}{r}}\right)\\&\quad =-{\partial _{r}p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}{\partial _{r}u_{r}}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial _{\varphi }^{2}u_{r}}+{\frac {1}{r^{2}\sin \theta }}\partial _{\theta }\left(\sin \theta {\partial _{\theta }u_{r}}\right)-2{\frac {u_{r}+{\partial _{\theta }u_{\theta }}+u_{\theta }\cot \theta }{r^{2}}}-{\frac {2}{r^{2}\sin \theta }}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +{\frac {1}{3}}\mu \partial _{r}\left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}u_{r}\right)+{\frac {1}{r\sin \theta }}\partial _{\theta }\left(u_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +\rho g_{r}\\[8px]\end{aligned}}$ ${\begin{aligned}\varphi :\ &\rho \left({\partial _{t}u_{\varphi }}+u_{r}{\partial _{r}u_{\varphi }}+{\frac {u_{\varphi }}{r\sin \theta }}{\partial _{\varphi }u_{\varphi }}+{\frac {u_{\theta }}{r}}{\partial _{\theta }u_{\varphi }}+{\frac {u_{r}u_{\varphi }+u_{\varphi }u_{\theta }\cot \theta }{r}}\right)\\&\quad =-{\frac {1}{r\sin \theta }}{\partial _{\varphi }p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}{\partial _{r}u_{\varphi }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial _{\varphi }^{2}u_{\varphi }}+{\frac {1}{r^{2}\sin \theta }}\partial _{\theta }\left(\sin \theta {\partial _{\theta }u_{\varphi }}\right)+{\frac {2\sin \theta {\partial _{\varphi }u_{r}}+2\cos \theta {\partial _{\varphi }u_{\theta }}-u_{\varphi }}{r^{2}\sin ^{2}\theta }}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r\sin \theta }}\partial _{\varphi }\left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}u_{r}\right)+{\frac {1}{r\sin \theta }}\partial _{\theta }\left(u_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +\rho g_{\varphi }\\[8px]\end{aligned}}$ ${\begin{aligned}\theta :\ &\rho \left({\partial _{t}u_{\theta }}+u_{r}{\partial _{r}u_{\theta }}+{\frac {u_{\varphi }}{r\sin \theta }}{\partial _{\varphi }u_{\theta }}+{\frac {u_{\theta }}{r}}{\partial _{\theta }u_{\theta }}+{\frac {u_{r}u_{\theta }-u_{\varphi }^{2}\cot \theta }{r}}\right)\\&\quad =-{\frac {1}{r}}{\partial _{\theta }p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}{\partial _{r}u_{\theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial _{\varphi }^{2}u_{\theta }}+{\frac {1}{r^{2}\sin \theta }}\partial _{\theta }\left(\sin \theta {\partial _{\theta }u_{\theta }}\right)+{\frac {2}{r^{2}}}{\partial _{\theta }u_{r}}-{\frac {u_{\theta }+2\cos \theta {\partial _{\varphi }u_{\varphi }}}{r^{2}\sin ^{2}\theta }}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r}}\partial _{\theta }\left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}u_{r}\right)+{\frac {1}{r\sin \theta }}\partial _{\theta }\left(u_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +\rho g_{\theta }.\end{aligned}}$

Mass continuity will read: ${\partial _{t}\rho }+{\frac {1}{r^{2}}}\partial _{r}\left(\rho r^{2}u_{r}\right)+{\frac {1}{r\sin \theta }}{\partial _{\varphi }(\rho u_{\varphi })}+{\frac {1}{r\sin \theta }}\partial _{\theta }\left(\sin \theta \rho u_{\theta }\right)=0.$

These equations could be (slightly) compacted by, for example, factoring ${\textstyle {\frac {1}{r^{2}}}}$ from the viscous terms. However, doing so would undesirably alter the structure of the Laplacian and other quantities.
