# Derivation of the Navier–Stokes equations

> **Query Topic**: Navier-Stokes equations (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 230, Frequency: 13)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Derivation_of_the_Navier–Stokes_equations

---

The derivation of the Navier–Stokes equations as well as their application and formulation for different families of fluids , is an important exercise in fluid dynamics with applications in mechanical engineering , physics , chemistry , heat transfer , and electrical engineering . A proof explaining the properties and bounds of the equations, such as Navier–Stokes existence and smoothness , is one of the important unsolved problems in mathematics .

## Basic assumptions

The Navier–Stokes equations are based on the assumption that the fluid, at the scale of interest, is a continuum – a continuous substance rather than discrete particles. Another necessary assumption is that all the fields of interest including pressure , flow velocity , density , and temperature are at least weakly differentiable .

The equations are derived from the basic principles of continuity of mass , conservation of momentum , and conservation of energy . Sometimes it is necessary to consider a finite arbitrary volume, called a control volume , over which these principles can be applied. This finite volume is denoted by Ω and its bounding surface ∂Ω . The control volume can remain fixed in space or can move with the fluid.

## The material derivative

Changes in properties of a moving fluid can be measured in two different ways. One can measure a given property by either carrying out the measurement on a fixed point in space as particles of the fluid pass by, or by following a parcel of fluid along its streamline . The derivative of a field with respect to a fixed position in space is called the Eulerian derivative, while the derivative following a moving parcel is called the advective or material (or Lagrangian ) derivative.

The material derivative is defined as the linear operator :

${\frac {D}{Dt}}\ {\stackrel {\mathrm {def} }{=}}\ {\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla$

where u is the flow velocity. The first term on the right-hand side of the equation is the ordinary Eulerian derivative (the derivative on a fixed reference frame, representing changes at a point with respect to time) whereas the second term represents changes of a quantity with respect to position (see advection ). This "special" derivative is in fact the ordinary derivative of a function of many variables along a path following the fluid motion; it may be derived through application of the chain rule in which all independent variables are checked for change along the path (which is to say, the total derivative ).

For example, the measurement of changes in wind velocity in the atmosphere can be obtained with the help of an anemometer in a weather station or by observing the movement of a weather balloon. The anemometer in the first case is measuring the velocity of all the moving particles passing through a fixed point in space, whereas in the second case the instrument is measuring changes in velocity as it moves with the flow.

## Continuity equations

The Navier–Stokes equation is a special continuity equation . A continuity equation may be derived from conservation principles of:

- mass ,

- momentum ,

- energy .

A continuity equation (or conservation law ) is an integral relation stating that the rate of change of some integrated property φ defined over a control volume Ω must be equal to the rate at which it is lost or gained through the boundaries Γ of the volume plus the rate at which it is created or consumed by sources and sinks inside the volume. This is expressed by the following integral continuity equation:

${\frac {d}{dt}}\int _{\Omega }\varphi \ d\Omega =-\int _{\Gamma }\varphi \mathbf {u\cdot n} \ d\Gamma -\int _{\Omega }s\ d\Omega$

where u is the flow velocity of the fluid, n is the outward-pointing unit normal vector, and s represents the sources and sinks in the flow, taking the sinks as positive.

The divergence theorem may be applied to the surface integral , changing it into a volume integral :

${\frac {d}{dt}}\int _{\Omega }\varphi \ d\Omega =-\int _{\Omega }\nabla \cdot (\varphi \mathbf {u} )\ d\Omega -\int _{\Omega }s\ d\Omega .$

Applying the Reynolds transport theorem to the integral on the left and then combining all of the integrals:

$\int _{\Omega }{\frac {\partial \varphi }{\partial t}}\ d\Omega =-\int _{\Omega }\nabla \cdot (\varphi \mathbf {u} )\ d\Omega -\int _{\Omega }s\ d\Omega \quad \Rightarrow \quad \int _{\Omega }\left({\frac {\partial \varphi }{\partial t}}+\nabla \cdot (\varphi \mathbf {u} )+s\right)d\Omega =0.$

The integral must be zero for any control volume; this can only be true if the integrand itself is zero, so that:

${\frac {\partial \varphi }{\partial t}}+\nabla \cdot (\varphi \mathbf {u} )+s=0.$

From this valuable relation (a very generic continuity equation ), three important concepts may be concisely written: conservation of mass, conservation of momentum, and conservation of energy. Validity is retained if φ is a vector, in which case the vector-vector product in the second term will be a dyad .

### Conservation of mass

Mass may be considered also. When the intensive property φ is considered as the mass, by substitution into the general continuity equation, and taking s = 0 (no sources or sinks of mass):

${\frac {\partial \rho }{\partial t}}+\nabla \cdot (\rho \mathbf {u} )=0$

where ρ is the mass density (mass per unit volume), and u is the flow velocity. This equation is called the mass continuity equation , or simply the continuity equation. This equation generally accompanies the Navier–Stokes equation.

In the case of an incompressible fluid , ⁠ Dρ / Dt ⁠ = 0 (the density following the path of a fluid element is constant) and the equation reduces to:

$\nabla \cdot \mathbf {u} =0$

which is in fact a statement of the conservation of volume.

### Conservation of momentum

A general momentum equation is obtained when the conservation relation is applied to momentum. When the intensive property φ is considered as the mass flux (also momentum density ), that is, the product of mass density and flow velocity ρ u , by substitution into the general continuity equation:

${\frac {\partial }{\partial t}}(\rho \mathbf {u} )+\nabla \cdot (\rho \mathbf {u} \otimes \mathbf {u} )=\mathbf {s}$

where u ⊗ u is a dyad , a special case of tensor product , which results in a second rank tensor; the divergence of a second rank tensor is again a vector (a first-rank tensor).

Using the formula for the divergence of a dyad,

$\nabla \cdot (\mathbf {a} \otimes \mathbf {b} )=(\nabla \cdot \mathbf {a} )\mathbf {b} +\mathbf {a} \cdot \nabla \mathbf {b}$

we then have

$\mathbf {u} {\frac {\partial \rho }{\partial t}}+\rho {\frac {\partial \mathbf {u} }{\partial t}}+\mathbf {u} \nabla \cdot (\rho \mathbf {u} )+\rho \mathbf {u} \cdot \nabla \mathbf {u} =\mathbf {s}$

Note that the gradient of a vector is a special case of the covariant derivative , the operation results in second rank tensors; except in Cartesian coordinates, it is important to understand that this is not simply an element by element gradient. Rearranging :

$\mathbf {u} \left({\frac {\partial \rho }{\partial t}}+\nabla \cdot (\rho \mathbf {u} )\right)+\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+\mathbf {u} \cdot \nabla \mathbf {u} \right)=\mathbf {s}$

The leftmost expression enclosed in parentheses is, by mass continuity (shown before), equal to zero. Noting that what remains on the left side of the equation is the material derivative of flow velocity:

$\rho {\frac {D\mathbf {u} }{Dt}}=\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+\mathbf {u} \cdot \nabla \mathbf {u} \right)=\mathbf {s}$

This appears to simply be an expression of Newton's second law ( F = m a ) in terms of body forces instead of point forces. Each term in any case of the Navier–Stokes equations is a body force. A shorter though less rigorous way to arrive at this result would be the application of the chain rule to acceleration:

${\begin{aligned}\rho {\frac {d}{dt}}{\bigl (}\mathbf {u} (x,y,z,t){\bigr )}=\mathbf {s} \quad &\Rightarrow &\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+{\frac {\partial \mathbf {u} }{\partial x}}{\frac {dx}{dt}}+{\frac {\partial \mathbf {u} }{\partial y}}{\frac {dy}{dt}}+{\frac {\partial \mathbf {u} }{\partial z}}{\frac {dz}{dt}}\right)&=\mathbf {s} \\\quad &\Rightarrow &\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+u{\frac {\partial \mathbf {u} }{\partial x}}+v{\frac {\partial \mathbf {u} }{\partial y}}+w{\frac {\partial \mathbf {u} }{\partial z}}\right)&=\mathbf {s} \\\quad &\Rightarrow &\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+\mathbf {u} \cdot \nabla \mathbf {u} \right)&=\mathbf {s} \end{aligned}}$

where u = ( u , v , w ) . The reason why this is "less rigorous" is that we haven't shown that the choice of

$\mathbf {u} =\left({\frac {dx}{dt}},{\frac {dy}{dt}},{\frac {dz}{dt}}\right)$

is correct; however it does make sense since with that choice of path the derivative is "following" a fluid "particle", and in order for Newton's second law to work, forces must be summed following a particle. For this reason the convective derivative is also known as the particle derivative.

## Cauchy momentum equation

The generic density of the momentum source s seen previously is made specific first by breaking it up into two new terms, one to describe internal stresses and one for external forces, such as gravity. By examining the forces acting on a small cube in a fluid, it may be shown that

$\rho {\frac {D\mathbf {u} }{Dt}}=\nabla \cdot {\boldsymbol {\sigma }}+\mathbf {\rho } {f}$

where σ is the Cauchy stress tensor , and f accounts for body forces present. This equation is called the Cauchy momentum equation and describes the non-relativistic momentum conservation of any continuum that conserves mass. σ is a rank two symmetric tensor given by its covariant components. In orthogonal coordinates in three dimensions it is represented as the 3 × 3 matrix :

$\sigma _{ij}={\begin{pmatrix}\sigma _{xx}&\tau _{xy}&\tau _{xz}\\\tau _{yx}&\sigma _{yy}&\tau _{yz}\\\tau _{zx}&\tau _{zy}&\sigma _{zz}\end{pmatrix}}$

where the σ are normal stresses and τ shear stresses . This matrix is split up into two terms:

$\sigma _{ij}={\begin{pmatrix}\sigma _{xx}&\tau _{xy}&\tau _{xz}\\\tau _{yx}&\sigma _{yy}&\tau _{yz}\\\tau _{zx}&\tau _{zy}&\sigma _{zz}\end{pmatrix}}=-{\begin{pmatrix}p&0&0\\0&p&0\\0&0&p\end{pmatrix}}+{\begin{pmatrix}\sigma _{xx}+p&\tau _{xy}&\tau _{xz}\\\tau _{yx}&\sigma _{yy}+p&\tau _{yz}\\\tau _{zx}&\tau _{zy}&\sigma _{zz}+p\end{pmatrix}}=-p\mathbf {I} +{\boldsymbol {\tau }}$

where I is the 3 × 3 identity matrix and τ is the deviatoric stress tensor . Note that the mechanical pressure p is equal to the negative of the mean normal stress:

$p=-{\tfrac {1}{3}}\left(\sigma _{xx}+\sigma _{yy}+\sigma _{zz}\right).$

The motivation for doing this is that pressure is typically a variable of interest, and also this simplifies application to specific fluid families later on since the rightmost tensor τ in the equation above must be zero for a fluid at rest. Note that τ is traceless . The Cauchy equation may now be written in another more explicit form:

$\rho {\frac {D\mathbf {u} }{Dt}}=-\nabla p+\nabla \cdot {\boldsymbol {\tau }}+\mathbf {\rho } {f}$

This equation is still incomplete. For completion, one must make hypotheses on the forms of τ and p , that is, one needs a constitutive law for the stress tensor which can be obtained for specific fluid families and on the pressure. Some of these hypotheses lead to the Euler equations (fluid dynamics) , other ones lead to the Navier–Stokes equations. Additionally, if the flow is assumed compressible an equation of state will be required, which will likely further require a conservation of energy formulation.

## Application to different fluids

The general form of the equations of motion is not "ready for use", the stress tensor is still unknown so that more information is needed; this information is normally some knowledge of the viscous behavior of the fluid. For different types of fluid flow this results in specific forms of the Navier–Stokes equations.

### Newtonian fluid

#### Compressible Newtonian fluid

The formulation for Newtonian fluids stems from an observation made by Newton that, for most fluids,

$\tau \propto {\frac {\partial u}{\partial y}}$

In order to apply this to the Navier–Stokes equations, three assumptions were made by Stokes:

The stress tensor is a linear function of the strain rate tensor or equivalently the velocity gradient. The fluid is isotropic. For a fluid at rest, ∇ ⋅ τ must be zero (so that hydrostatic pressure results).

- The stress tensor is a linear function of the strain rate tensor or equivalently the velocity gradient.

- The fluid is isotropic.

- For a fluid at rest, ∇ ⋅ τ must be zero (so that hydrostatic pressure results).

The above list states the classic argument that the shear strain rate tensor (the (symmetric) shear part of the velocity gradient) is a pure shear tensor and does not include any inflow/outflow part (any compression/expansion part). This means that its trace is zero, and this is achieved by subtracting ∇ ⋅ u in a symmetric way from the diagonal elements of the tensor. The compressional contribution to viscous stress is added as a separate diagonal tensor.

Applying these assumptions will lead to :

${\boldsymbol {\tau }}=\mu \left(\nabla \mathbf {u} +\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)+\lambda \left(\nabla \cdot \mathbf {u} \right)\mathbf {I}$

or in tensor form

$\tau _{ij}=\mu \left({\frac {\partial u_{i}}{\partial x_{j}}}+{\frac {\partial u_{j}}{\partial x_{i}}}\right)+\delta _{ij}\lambda {\frac {\partial u_{k}}{\partial x_{k}}}$

That is, the deviatoric of the deformation rate tensor is identified to the deviatoric of the stress tensor, up to a factor μ .

δ ij is the Kronecker delta . μ and λ are proportionality constants associated with the assumption that stress depends on strain linearly; μ is called the first coefficient of viscosity or shear viscosity (usually just called "viscosity") and λ is the second coefficient of viscosity or volume viscosity (and it is related to bulk viscosity ). The value of λ , which produces a viscous effect associated with volume change, is very difficult to determine, not even its sign is known with absolute certainty. Even in compressible flows, the term involving λ is often negligible; however it can occasionally be important even in nearly incompressible flows and is a matter of controversy. When taken nonzero, the most common approximation is λ ≈ − ⁠ 2 / 3 ⁠ μ .

A straightforward substitution of τ ij into the momentum conservation equation will yield the Navier–Stokes equations , describing a compressible Newtonian fluid:

$\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+\mathbf {u} \cdot \nabla \mathbf {u} \right)=-\nabla p+\nabla \cdot \left[\mu \left(\nabla \mathbf {u} +\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\right]+\nabla \cdot \left[\lambda \left(\nabla \cdot \mathbf {u} \right)\mathbf {I} \right]+\rho \mathbf {g}$

The body force has been decomposed into density and external acceleration, that is, f = ρ g . The associated mass continuity equation is:

${\frac {\partial \rho }{\partial t}}+\nabla \cdot (\rho \mathbf {u} )=0$

In addition to this equation, an equation of state and an equation for the conservation of energy is needed. The equation of state to use depends on context (often the ideal gas law ), the conservation of energy will read:

$\rho {\frac {Dh}{Dt}}={\frac {Dp}{Dt}}+\nabla \cdot (k\nabla T)+\Phi$

Here, h is the specific enthalpy , T is the temperature , and Φ is a function representing the dissipation of energy due to viscous effects:

$\Phi =\mu \left(2\left({\frac {\partial u}{\partial x}}\right)^{2}+2\left({\frac {\partial v}{\partial y}}\right)^{2}+2\left({\frac {\partial w}{\partial z}}\right)^{2}+\left({\frac {\partial v}{\partial x}}+{\frac {\partial u}{\partial y}}\right)^{2}+\left({\frac {\partial w}{\partial y}}+{\frac {\partial v}{\partial z}}\right)^{2}+\left({\frac {\partial u}{\partial z}}+{\frac {\partial w}{\partial x}}\right)^{2}\right)+\lambda (\nabla \cdot \mathbf {u} )^{2}.$

With a good equation of state and good functions for the dependence of parameters (such as viscosity) on the variables, this system of equations seems to properly model the dynamics of all known gases and most liquids.

#### Incompressible Newtonian fluid

For the special (but very common) case of incompressible flow, the momentum equations simplify significantly. Using the following assumptions:

- Viscosity μ will now be a constant

- The second viscosity effect λ = 0

- The simplified mass continuity equation ∇ ⋅ u = 0

This gives incompressible Navier-Stokes equations , describing incompressible Newtonian fluid:

$\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+\mathbf {u} \cdot \nabla \mathbf {u} \right)=-\nabla p+\nabla \cdot \left[\mu \left(\nabla \mathbf {u} +\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\right]+\rho \mathbf {g}$

then looking at the viscous terms of the x momentum equation for example we have:

${\begin{aligned}&{\frac {\partial }{\partial x}}\left(2\mu {\frac {\partial u}{\partial x}}\right)+{\frac {\partial }{\partial y}}\left(\mu \left({\frac {\partial u}{\partial y}}+{\frac {\partial v}{\partial x}}\right)\right)+{\frac {\partial }{\partial z}}\left(\mu \left({\frac {\partial u}{\partial z}}+{\frac {\partial w}{\partial x}}\right)\right)\\[8px]&\qquad =2\mu {\frac {\partial ^{2}u}{\partial x^{2}}}+\mu {\frac {\partial ^{2}u}{\partial y^{2}}}+\mu {\frac {\partial ^{2}v}{\partial y\,\partial x}}+\mu {\frac {\partial ^{2}u}{\partial z^{2}}}+\mu {\frac {\partial ^{2}w}{\partial z\,\partial x}}\\[8px]&\qquad =\mu {\frac {\partial ^{2}u}{\partial x^{2}}}+\mu {\frac {\partial ^{2}u}{\partial y^{2}}}+\mu {\frac {\partial ^{2}u}{\partial z^{2}}}+\mu {\frac {\partial ^{2}u}{\partial x^{2}}}+\mu {\frac {\partial ^{2}v}{\partial y\,\partial x}}+\mu {\frac {\partial ^{2}w}{\partial z\,\partial x}}\\[8px]&\qquad =\mu \nabla ^{2}u+\mu {\frac {\partial }{\partial x}}{\cancelto {0}{\left({\frac {\partial u}{\partial x}}+{\frac {\partial v}{\partial y}}+{\frac {\partial w}{\partial z}}\right)}}\\[8px]&\qquad =\mu \nabla ^{2}u\end{aligned}}\,$

Similarly for the y and z momentum directions we have μ ∇ 2 v and μ ∇ 2 w .

The above solution is key to deriving Navier–Stokes equations from the equation of motion in fluid dynamics when density and viscosity are constant.

### Non-Newtonian fluids

A non-Newtonian fluid is a fluid whose flow properties differ in any way from those of Newtonian fluids . Most commonly the viscosity of non-Newtonian fluids is a function of shear rate or shear rate history. However, there are some non-Newtonian fluids with shear-independent viscosity, that nonetheless exhibit normal stress-differences or other non-Newtonian behaviour. Many salt solutions and molten polymers are non-Newtonian fluids, as are many commonly found substances such as ketchup , custard , toothpaste , starch suspensions, paint , blood , and shampoo . In a Newtonian fluid, the relation between the shear stress and the shear rate is linear, passing through the origin, the constant of proportionality being the coefficient of viscosity. In a non-Newtonian fluid, the relation between the shear stress and the shear rate is different, and can even be time-dependent. The study of the non-Newtonian fluids is usually called rheology . A few examples are given here.

#### Bingham fluid

In Bingham fluids, the situation is slightly different:

${\frac {\partial u}{\partial y}}={\begin{cases}0,&\tau <\tau _{0}\\[5px]{\dfrac {\tau -\tau _{0}}{\mu }},&\tau \geq \tau _{0}\end{cases}}$

These are fluids capable of bearing some stress before they start flowing. Some common examples are toothpaste and clay .

#### Power-law fluid

A power law fluid is an idealised fluid for which the shear stress , τ , is given by

$\tau =K\left({\frac {\partial u}{\partial y}}\right)^{n}$

This form is useful for approximating all sorts of general fluids, including shear thinning (such as latex paint) and shear thickening (such as corn starch water mixture).

## Stream function formulation

In the analysis of a flow, it is often desirable to reduce the number of equations and/or the number of variables. The incompressible Navier–Stokes equation with mass continuity (four equations in four unknowns) can be reduced to a single equation with a single dependent variable in 2D, or one vector equation in 3D. This is enabled by two vector calculus identities :

${\begin{aligned}\nabla \times (\nabla \phi )&=0\\\nabla \cdot (\nabla \times \mathbf {A} )&=0\end{aligned}}$

for any differentiable scalar φ and vector A . The first identity implies that any term in the Navier–Stokes equation that may be represented as the gradient of a scalar will disappear when the curl of the equation is taken. Commonly, pressure p and external acceleration g will be eliminated, resulting in (this is true in 2D as well as 3D):

$\nabla \times \left({\frac {\partial \mathbf {u} }{\partial t}}+\mathbf {u} \cdot \nabla \mathbf {u} \right)=\nu \nabla \times \left(\nabla ^{2}\mathbf {u} \right)$

where it is assumed that all body forces are describable as gradients (for example it is true for gravity), and density has been divided so that viscosity becomes kinematic viscosity .

The second vector calculus identity above states that the divergence of the curl of a vector field is zero. Since the (incompressible) mass continuity equation specifies the divergence of flow velocity being zero, we can replace the flow velocity with the curl of some vector ψ so that mass continuity is always satisfied:

$\nabla \cdot \mathbf {u} =0\quad \Rightarrow \quad \nabla \cdot (\nabla \times {\boldsymbol {\psi }})=0\quad \Rightarrow \quad 0=0$

So, as long as flow velocity is represented through u = ∇ × ψ , mass continuity is unconditionally satisfied. With this new dependent vector variable, the Navier–Stokes equation (with curl taken as above) becomes a single fourth order vector equation, no longer containing the unknown pressure variable and no longer dependent on a separate mass continuity equation:

$\nabla \times \left({\frac {\partial }{\partial t}}(\nabla \times {\boldsymbol {\psi }})+(\nabla \times {\boldsymbol {\psi }})\cdot \nabla (\nabla \times {\boldsymbol {\psi }})\right)=\nu \nabla \times \left(\nabla ^{2}(\nabla \times {\boldsymbol {\psi }})\right)$

Apart from containing fourth order derivatives, this equation is fairly complicated, and is thus uncommon. Note that if the cross differentiation is left out, the result is a third order vector equation containing an unknown vector field (the gradient of pressure) that may be determined from the same boundary conditions that one would apply to the fourth order equation above.

### 2D flow in orthogonal coordinates

The true utility of this formulation is seen when the flow is two dimensional in nature and the equation is written in a general orthogonal coordinate system , in other words a system where the basis vectors are orthogonal. Note that this by no means limits application to Cartesian coordinates , in fact most of the common coordinates systems are orthogonal, including familiar ones like cylindrical and obscure ones like toroidal .

The 3D flow velocity is expressed as (note that the discussion not used coordinates so far):

$\mathbf {u} =u_{1}\mathbf {e} _{1}+u_{2}\mathbf {e} _{2}+u_{3}\mathbf {e} _{3}$

where e i are basis vectors, not necessarily constant and not necessarily normalized, and u i are flow velocity components; let also the coordinates of space be ( x 1 , x 2 , x 3 ) .

Now suppose that the flow is 2D. This does not mean the flow is in a plane, rather it means that the component of flow velocity in one direction is zero and the remaining components are independent of the same direction. In that case (take component 3 to be zero):

$\mathbf {u} =u_{1}\mathbf {e} _{1}+u_{2}\mathbf {e} _{2};\qquad {\frac {\partial u_{1}}{\partial x_{3}}}={\frac {\partial u_{2}}{\partial x_{3}}}=0$

The vector function ψ is still defined via:

$\mathbf {u} =\nabla \times {\boldsymbol {\psi }}$

but this must simplify in some way also since the flow is assumed 2D. If orthogonal coordinates are assumed, the curl takes on a fairly simple form, and the equation above expanded becomes:

$u_{1}\mathbf {e} _{1}+u_{2}\mathbf {e} _{2}={\frac {\mathbf {e} _{1}}{h_{2}h_{3}}}\left[{\frac {\partial }{\partial x_{2}}}\left(h_{3}\psi _{3}\right)-{\frac {\partial }{\partial x_{3}}}\left(h_{2}\psi _{2}\right)\right]+$

${\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }+{\frac {\mathbf {e} _{2}}{h_{3}h_{1}}}\left[{\frac {\partial }{\partial x_{3}}}\left(h_{1}\psi _{1}\right)-{\frac {\partial }{\partial x_{1}}}\left(h_{3}\psi _{3}\right)\right]+{\frac {\mathbf {e} _{3}}{h_{1}h_{2}}}\left[{\frac {\partial }{\partial x_{1}}}\left(h_{2}\psi _{2}\right)-{\frac {\partial }{\partial x_{2}}}\left(h_{1}\psi _{1}\right)\right]$

Examining this equation shows that we can set ψ 1 = ψ 2 = 0 and retain equality with no loss of generality, so that:

$u_{1}\mathbf {e} _{1}+u_{2}\mathbf {e} _{2}={\frac {\mathbf {e} _{1}}{h_{2}h_{3}}}{\frac {\partial }{\partial x_{2}}}\left(h_{3}\psi _{3}\right)-{\frac {\mathbf {e} _{2}}{h_{3}h_{1}}}{\frac {\partial }{\partial x_{1}}}\left(h_{3}\psi _{3}\right)$

the significance here is that only one component of ψ remains, so that 2D flow becomes a problem with only one dependent variable. The cross differentiated Navier–Stokes equation becomes two 0 = 0 equations and one meaningful equation.

The remaining component ψ 3 = ψ is called the stream function . The equation for ψ can simplify since a variety of quantities will now equal zero, for example:

$\nabla \cdot {\boldsymbol {\psi }}={\frac {1}{h_{1}h_{2}h_{3}}}{\frac {\partial }{\partial x_{3}}}\left(\psi h_{1}h_{2}\right)=0$

if the scale factors h 1 and h 2 also are independent of x 3 . Also, from the definition of the vector Laplacian

$\nabla \times (\nabla \times {\boldsymbol {\psi }})=\nabla (\nabla \cdot {\boldsymbol {\psi }})-\nabla ^{2}{\boldsymbol {\psi }}=-\nabla ^{2}{\boldsymbol {\psi }}$

Manipulating the cross differentiated Navier–Stokes equation using the above two equations and a variety of identities will eventually yield the 1D scalar equation for the stream function:

${\frac {\partial }{\partial t}}\left(\nabla ^{2}\psi \right)+(\nabla \times {\boldsymbol {\psi }})\cdot \nabla \left(\nabla ^{2}\psi \right)=\nu \nabla ^{4}\psi$

where ∇ 4 is the biharmonic operator . This is very useful because it is a single self-contained scalar equation that describes both momentum and mass conservation in 2D. The only other equations that this partial differential equation needs are initial and boundary conditions.

The assumptions for the stream function equation are:

- The flow is incompressible and Newtonian.

- Coordinates are orthogonal .

- Flow is 2D: u 3 = ⁠ ∂ u 1 / ∂ x 3 ⁠ = ⁠ ∂ u 2 / ∂ x 3 ⁠ = 0

- The first two scale factors of the coordinate system are independent of the last coordinate: ⁠ ∂ h 1 / ∂ x 3 ⁠ = ⁠ ∂ h 2 / ∂ x 3 ⁠ = 0 , otherwise extra terms appear.

The stream function has some useful properties:

- Since −∇ 2 ψ = ∇ × (∇ × ψ ) = ∇ × u , the vorticity of the flow is just the negative of the Laplacian of the stream function.

- The level curves of the stream function are streamlines .

## The stress tensor

The derivation of the Navier–Stokes equation involves the consideration of forces acting on fluid elements, so that a quantity called the stress tensor appears naturally in the Cauchy momentum equation . Since the divergence of this tensor is taken, it is customary to write out the equation fully simplified, so that the original appearance of the stress tensor is lost.

However, the stress tensor still has some important uses, especially in formulating boundary conditions at fluid interfaces . Recalling that σ = − p I + τ , for a Newtonian fluid the stress tensor is:

$\sigma _{ij}=-p\delta _{ij}+\mu \left({\frac {\partial u_{i}}{\partial x_{j}}}+{\frac {\partial u_{j}}{\partial x_{i}}}\right)+\delta _{ij}\lambda \nabla \cdot \mathbf {u} .$

If the fluid is assumed to be incompressible, the tensor simplifies significantly. In 3D cartesian coordinates for example:

${\begin{aligned}{\boldsymbol {\sigma }}&=-{\begin{pmatrix}p&0&0\\0&p&0\\0&0&p\end{pmatrix}}+\mu {\begin{pmatrix}2\displaystyle {\frac {\partial u}{\partial x}}&\displaystyle {{\frac {\partial u}{\partial y}}+{\frac {\partial v}{\partial x}}}&\displaystyle {{\frac {\partial u}{\partial z}}+{\frac {\partial w}{\partial x}}}\\\displaystyle {{\frac {\partial v}{\partial x}}+{\frac {\partial u}{\partial y}}}&2\displaystyle {\frac {\partial v}{\partial y}}&\displaystyle {{\frac {\partial v}{\partial z}}+{\frac {\partial w}{\partial y}}}\\\displaystyle {{\frac {\partial w}{\partial x}}+{\frac {\partial u}{\partial z}}}&\displaystyle {{\frac {\partial w}{\partial y}}+{\frac {\partial v}{\partial z}}}&2\displaystyle {\frac {\partial w}{\partial z}}\end{pmatrix}}\\[6px]&=-p\mathbf {I} +\mu \left(\nabla \mathbf {u} +\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\\[6px]&=-p\mathbf {I} +2\mu \mathbf {e} \end{aligned}}$

e is the strain rate tensor, by definition:

$e_{ij}={\frac {1}{2}}\left({\frac {\partial u_{i}}{\partial x_{j}}}+{\frac {\partial u_{j}}{\partial x_{i}}}\right).$
