# Non-dimensionalization and scaling of the Navier–Stokes equations

> **Query Topic**: relationship between the Cauchy momentum equation and the Navier-Stokes equation (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 167, Frequency: 11)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Non-dimensionalization_and_scaling_of_the_Navier–Stokes_equations

---

In fluid mechanics , non-dimensionalization of the Navier–Stokes equations is the conversion of the Navier–Stokes equation to a nondimensional form . This technique can ease the analysis of the problem at hand, and reduce the number of free parameters . Small or large sizes of certain dimensionless parameters indicate the importance of certain terms in the equations for the studied flow. This may provide possibilities to neglect terms in (certain areas of) the considered flow. Further, non-dimensionalized Navier–Stokes equations can be beneficial if one is posed with similar physical situations – that is problems where the only changes are those of the basic dimensions of the system.

Scaling of Navier–Stokes equation refers to the process of selecting the proper spatial scales – for a certain type of flow – to be used in the non-dimensionalization of the equation. Since the resulting equations need to be dimensionless, a suitable combination of parameters and constants of the equations and flow (domain) characteristics have to be found. As a result of this combination, the number of parameters to be analyzed is reduced and the results may be obtained in terms of the scaled variables .

## Need for non-dimensionalization and scaling

In addition to reducing the number of parameters, non-dimensionalized equation helps to gain a greater insight into the relative size of various terms present in the equation. Following appropriate selecting of scales for the non-dimensionalization process, this leads to identification of small terms in the equation. Neglecting the smaller terms against the bigger ones allows for the simplification of the situation. For the case of flow without heat transfer , the non-dimensionalized Navier–Stokes equation depends only on the Reynolds Number and hence all physical realizations of the related experiment will have the same value of non-dimensionalized variables for the same Reynolds Number.

Scaling helps provide better understanding of the physical situation, with the variation in dimensions of the parameters involved in the equation. This allows for experiments to be conducted on smaller scale prototypes provided that any physical effects which are not included in the non-dimensionalized equation are unimportant.

## Non-dimensionalized Navier–Stokes equation

The incompressible Navier–Stokes momentum equation is written as:

${\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} =-{\frac {1}{\rho }}\nabla p+\nu \nabla ^{2}\mathbf {u} +\mathbf {g} .$

where ρ is the density , p is the pressure , ν is the kinematic viscosity , u is the flow velocity , and g is the body acceleration field.

The above equation can be non-dimensionalized through selection of appropriate scales as follows:

Substituting the scales the non-dimensionalized equation obtained is:

where $Fr$ is the Froude number and $Re$ is the Reynolds number ( $Re=UL/\nu$ ).

### Flows with large viscosity

For flows where viscous forces are dominant i.e. slow flows with large viscosity, a viscous pressure scale μ U / L is used. In the absence of a free surface, the equation obtained is

### Stokes regime

Scaling of equation ( 1 ) can be done, in a flow where inertia term is smaller than the viscous term i.e. when Re → 0 then inertia terms can be neglected, leaving the equation of a creeping motion .

$Re{\frac {\partial \mathbf {u^{*}} }{\partial t^{*}}}=-\nabla ^{*}p^{*}+\nabla ^{*2}\mathbf {u^{*}} .$

Such flows tend to have influence of viscous interaction over large distances from an object. [ citation needed ] At low Reynolds number the same equation reduces to a diffusion equation , named Stokes equation

$-\nabla ^{*}p^{*}+\nabla ^{*2}\mathbf {u^{*}} =\mathbf {0} .$

### Euler regime

Similarly if Re → ∞ i.e. when the inertia forces dominates, the viscous contribution can be neglected. The non-dimensionalized Euler equation for an inviscid flow is

${\frac {\partial \mathbf {u^{*}} }{\partial t}}+(\mathbf {u^{*}} \cdot \nabla ^{*})\mathbf {u^{*}} \ =-\nabla ^{*}p^{*}.$

### When density varies due to both concentration and temperature

Density variation due to both concentration and temperature is an important field of study in double diffusive convection . If density changes due to both temperature and salinity are taken into account, then some more terms add to the Z-Component of momentum as follows:

${\frac {\partial W}{\partial t}}+U{\frac {\partial W}{\partial X}}+W{\frac {\partial W}{\partial Z}}\ =-{\frac {1}{\rho _{o}}}{\frac {\partial p_{d}}{\partial Z}}+v\left({\frac {\partial ^{2}W}{\partial X^{2}}}+{\frac {\partial ^{2}W}{\partial Z^{2}}}\right)\ -g\left(\beta _{s}\nabla {S}-\beta _{T}\nabla {T}\right)$

Where S is the salinity of the fluid, β T is the thermal expansion coefficient at constant pressure and β S is the coefficient of saline expansion at constant pressure and temperature.

Non dimensionalizing using the scale:

$S^{*}={\frac {S-S_{B}}{S_{T}-S_{B}}}$ and $T^{*}={\frac {T-T_{B}}{T_{T}-T_{B}}}$

we get

${\frac {\partial W^{*}}{\partial t^{*}}}+U^{*}{\frac {\partial W^{*}}{\partial X^{*}}}+W^{*}{\frac {\partial W^{*}}{\partial Z^{*}}}\ =-{\frac {\partial p_{d}}{\partial Z^{*}}}+Pr\left({\frac {\partial ^{2}W^{*}}{\partial X^{*2}}}+{\frac {\partial ^{2}W^{*}}{\partial Z^{*2}}}\right)\ -{Ra_{s}Pr_{s}S}+{Ra_{T}Pr_{T}T}$

where S T , T T denote the salinity and temperature at top layer, S B , T B denote the salinity and temperature at bottom layer, Ra is the Rayleigh Number , and Pr is the Prandtl Number . The sign of Ra S and Ra T will change depending on whether it stabilizes or destabilizes the system.
