# Darcy–Weisbach equation

> **Query Topic**: relationship between the Cauchy momentum equation and the Navier-Stokes equation (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 167, Frequency: 11)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Darcy–Weisbach_equation

---

In fluid dynamics , the Darcy–Weisbach equation is an empirical equation that relates the head loss , or pressure loss, due to viscous shear forces along a given length of pipe to the average velocity of the fluid flow for an incompressible fluid. The equation is named after Henry Darcy and Julius Weisbach . Currently, there is no formula more accurate or universally applicable than the Darcy–Weisbach supplemented by the Moody diagram or Colebrook equation .

The Darcy–Weisbach equation contains a dimensionless friction factor, known as the Darcy friction factor . This is also variously called the Darcy–Weisbach friction factor, friction factor, resistance coefficient, or flow coefficient.

## Historical background

The Darcy-Weisbach equation, combined with the Moody chart for calculating head losses in pipes, is traditionally attributed to Henry Darcy , Julius Weisbach , and Lewis Ferry Moody . However, the development of these formulas and charts also involved other scientists and engineers over its historical development. Generally, the Bernoulli's equation would provide the head losses but in terms of quantities not known a priori, such as pressure. Therefore, empirical relationships were sought to correlate the head loss with quantities like pipe diameter and fluid velocity.

Julius Weisbach was certainly not the first to introduce a formula correlating the length and diameter of a pipe to the square of the fluid velocity. Antoine Chézy (1718-1798), in fact, had published a formula in 1770 that, although referring to open channels (i.e., not under pressure), was formally identical to the one Weisbach would later introduce, provided it was reformulated in terms of the hydraulic radius . However, Chézy's formula was lost until 1800, when Gaspard de Prony (a former student of his) published an account describing his results. It is likely that Weisbach was aware of Chézy's formula through Prony's publications.

Weisbach's formula was proposed in 1845 in the form we still use today:

$\Delta H=f\cdot {LV^{2} \over {2gD}}$

where:

- $\Delta H$ : head loss.

- $L$ : length of the pipe.

- $D$ : diameter of the pipe.

- $V$ : velocity of the fluid.

- $g$ : acceleration due to gravity .

However, the friction factor f was expressed by Weisbach through the following empirical formula:

$f=\alpha +{\beta \over {\sqrt {V}}}$

with $\alpha$ and $\beta$ depending on the diameter and the type of pipe wall. Weisbach's work was published in the United States in 1848 and soon became well known there. In contrast, it did not initially gain much traction in France, where Prony equation , which had a polynomial form in terms of velocity (often approximated by the square of the velocity), continued to be used. Beyond the historical developments, Weisbach's formula had the objective merit of adhering to dimensional analysis , resulting in a dimensionless friction factor f. The complexity of f, dependent on the mechanics of the boundary layer and the flow regime (laminar, transitional, or turbulent), tended to obscure its dependence on the quantities in Weisbach's formula, leading many researchers to derive irrational and dimensionally inconsistent empirical formulas. It was understood not long after Weisbach's work that the friction factor f depended on the flow regime and was independent of the Reynolds number (and thus the velocity) only in the case of rough pipes in a fully turbulent flow regime (Prandtl-von Kármán equation).

## Pressure-loss equation

In a cylindrical pipe of uniform diameter D , flowing full, the pressure loss due to viscous effects Δ p is proportional to length L and can be characterized by the Darcy–Weisbach equation:

${\frac {\Delta p}{L}}=f_{\mathrm {D} }\cdot {\frac {\rho }{2}}\cdot {\frac {{\langle v\rangle }^{2}}{D_{H}}},$

where the pressure loss per unit length ⁠ Δ p / L ⁠ (SI units: Pa / m ) is a function of:

$\rho$ , the density of the fluid (kg/m 3 );

$D_{H}$ , the hydraulic diameter of the pipe (for a pipe of circular section, this equals D ; otherwise D H = 4A/P for a pipe of cross-sectional area A and perimeter P ) (m);

$\langle v\rangle$ , the mean flow velocity , experimentally measured as the volumetric flow rate Q per unit cross-sectional wetted area (m/s);

$f_{\mathrm {D} }$ , the Darcy friction factor (also called flow coefficient λ ).

For laminar flow in a circular pipe of diameter D c , the friction factor is inversely proportional to the Reynolds number alone ( f D = ⁠ 64 / Re ⁠ ) which itself can be expressed in terms of easily measured or published physical quantities (see section below). Making this substitution the Darcy–Weisbach equation is rewritten as

${\frac {\Delta p}{L}}={\frac {128}{\pi }}\cdot {\frac {\mu Q}{D_{c}^{4}}},$

where

μ is the dynamic viscosity of the fluid (Pa·s = N·s/m 2 = kg/(m·s));

Q is the volumetric flow rate , used here to measure flow instead of mean velocity according to Q = ⁠ π / 4 ⁠ D c 2 < v > (m 3 /s).

Note that this laminar form of Darcy–Weisbach is equivalent to the Hagen–Poiseuille equation , which is analytically derived from the Navier–Stokes equations .

## Head-loss formula

The head loss Δ h (or h f ) expresses the pressure loss due to friction in terms of the equivalent height of a column of the working fluid, so the pressure drop is

$\Delta p=\rho g\,\Delta h,$

where:

Δ h = The head loss due to pipe friction over the given length of pipe (SI units: m);

g = The local acceleration due to gravity (m/s 2 ).

It is useful to present head loss per length of pipe (dimensionless):

$S={\frac {\Delta h}{L}}={\frac {1}{\rho g}}\cdot {\frac {\Delta p}{L}},$

where L is the pipe length ( m ).

Therefore, the Darcy–Weisbach equation can also be written in terms of head loss:

$S=f_{\text{D}}\cdot {\frac {1}{2g}}\cdot {\frac {{\langle v\rangle }^{2}}{D}}.$

### In terms of volumetric flow

The relationship between mean flow velocity $\langle v\rangle$ and volumetric flow rate Q is

$Q=A\cdot \langle v\rangle ,$

where:

Q = The volumetric flow (m 3 /s),

A = The cross-sectional wetted area (m 2 ).

In a full-flowing, circular pipe of diameter D c ,

$Q={\frac {\pi }{4}}D_{c}^{2}\langle v\rangle .$

Then the Darcy–Weisbach equation in terms of Q is

$S=f_{\text{D}}\cdot {\frac {8}{\pi ^{2}g}}\cdot {\frac {Q^{2}}{D_{c}^{5}}}.$

## Shear-stress form

The mean wall shear stress τ in a pipe or open channel is expressed in terms of the Darcy–Weisbach friction factor as

$\tau ={\frac {1}{8}}f_{\text{D}}\rho {\langle v\rangle }^{2}.$

The wall shear stress has the SI unit of pascals (Pa).

## Darcy friction factor

The friction factor f D is not a constant: it depends on such things as the characteristics of the pipe (diameter D and roughness height ε ), the characteristics of the fluid (its kinematic viscosity ν [nu]), and the velocity of the fluid flow ⟨ v ⟩ . It has been measured to high accuracy within certain flow regimes and may be evaluated by the use of various empirical relations, or it may be read from published charts. These charts are often referred to as Moody diagrams , after L. F. Moody , and hence the factor itself is sometimes erroneously called the Moody friction factor . It is also sometimes called the Blasius friction factor, after the approximate formula he proposed.

Figure 1 shows the value of f D as measured by experimenters for many different fluids, over a wide range of Reynolds numbers, and for pipes of various roughness heights. There are three broad regimes of fluid flow encountered in these data: laminar, critical, and turbulent.

### Laminar regime

For laminar (smooth) flows , it is a consequence of Poiseuille's law (which stems from an exact classical solution for the fluid flow) that

$f_{\mathrm {D} }={\frac {64}{\mathrm {Re} }},$

where Re is the Reynolds number

$\mathrm {Re} ={\frac {\rho }{\mu }}\langle v\rangle D={\frac {\langle v\rangle D}{\nu }},$

and where μ is the viscosity of the fluid and

$\nu ={\frac {\mu }{\rho }}$

is known as the kinematic viscosity . In this expression for Reynolds number, the characteristic length D is taken to be the hydraulic diameter of the pipe, which, for a cylindrical pipe flowing full, equals the inside diameter. In Figures 1 and 2 of friction factor versus Reynolds number, the regime Re < 2000 demonstrates laminar flow; the friction factor is well represented by the above equation.

In effect, the friction loss in the laminar regime is more accurately characterized as being proportional to flow velocity, rather than proportional to the square of that velocity: one could regard the Darcy–Weisbach equation as not truly applicable in the laminar flow regime.

In laminar flow, friction loss arises from the transfer of momentum from the fluid in the center of the flow to the pipe wall via the viscosity of the fluid; no vortices are present in the flow. Note that the friction loss is insensitive to the pipe roughness height ε : the flow velocity in the neighborhood of the pipe wall is zero.

### Critical regime

For Reynolds numbers in the range 2000 < Re < 4000 , the flow is unsteady (varies grossly with time) and varies from one section of the pipe to another (is not "fully developed"). The flow involves the incipient formation of vortices; it is not well understood.

### Turbulent regime

For Reynolds number greater than 4000, the flow is turbulent; the resistance to flow follows the Darcy–Weisbach equation: it is proportional to the square of the mean flow velocity. Over a domain of many orders of magnitude of Re ( 4000 < Re < 10 8 ), the friction factor varies less than one order of magnitude ( 0.006 < f D < 0.06 ). Within the turbulent flow regime, the nature of the flow can be further divided into a regime where the pipe wall is effectively smooth, and one where its roughness height is salient.

#### Smooth-pipe regime

When the pipe surface is smooth (the "smooth pipe" curve in Figure 2), the friction factor's variation with Re can be modeled by the Kármán–Prandtl resistance equation for turbulent flow in smooth pipes with the parameters suitably adjusted

${\frac {1}{\sqrt {f_{\mathrm {D} }}}}=1.930\log _{10}\left(\mathrm {Re} {\sqrt {f_{\mathrm {D} }}}\right)-0.537.$

The numbers 1.930 and 0.537 are phenomenological; these specific values provide a fairly good fit to the data. The product Re √ f D (called the "friction Reynolds number") can be considered, like the Reynolds number, to be a (dimensionless) parameter of the flow: at fixed values of Re √ f D , the friction factor is also fixed.

In the Kármán–Prandtl resistance equation, f D can be expressed in closed form as an analytic function of Re through the use of the Lambert W function :

${\frac {1}{\sqrt {f_{\mathrm {D} }}}}={\frac {1.930}{\ln(10)}}W\left(10^{\frac {-0.537}{1.930}}{\frac {\ln(10)}{1.930}}\mathrm {Re} \right)=0.838\ W(0.629\ \mathrm {Re} )$

In this flow regime, many small vortices are responsible for the transfer of momentum between the bulk of the fluid to the pipe wall. As the friction Reynolds number Re √ f D increases, the profile of the fluid velocity approaches the wall asymptotically, thereby transferring more momentum to the pipe wall, as modeled in Blasius boundary layer theory.

#### Rough-pipe regime

When the pipe surface's roughness height ε is significant (typically at high Reynolds number), the friction factor departs from the smooth pipe curve, ultimately approaching an asymptotic value ("rough pipe" regime). In this regime, the resistance to flow varies according to the square of the mean flow velocity and is insensitive to Reynolds number. Here, it is useful to employ yet another dimensionless parameter of the flow, the roughness Reynolds number

$R_{*}={\frac {1}{\sqrt {8}}}\left(\mathrm {Re} {\sqrt {f_{\mathrm {D} }}}\,\right){\frac {\varepsilon }{D}}$

where the roughness height ε is scaled to the pipe diameter D .

It is illustrative to plot the roughness function B :

$B(R_{*})={\frac {1}{1.930{\sqrt {f_{\mathrm {D} }}}}}+\log \left({\frac {1.90}{\sqrt {8}}}\cdot {\frac {\varepsilon }{D}}\right)$

Figure 3 shows B versus R ∗ for the rough pipe data of Nikuradse, Shockling, and Langelandsvik.

In this view, the data at different roughness ratio ⁠ ε / D ⁠ fall together when plotted against R ∗ , demonstrating scaling in the variable R ∗ . The following features are present:

- When ε = 0 , then R ∗ is identically zero: flow is always in the smooth pipe regime. The data for these points lie to the left extreme of the abscissa and are not within the frame of the graph.

- When R ∗ < 5 , the data lie on the line B ( R ∗ ) = R ∗ ; flow is in the smooth pipe regime.

- When R ∗ > 100 , the data asymptotically approach a horizontal line; they are independent of Re , f D , and ⁠ ε / D ⁠ .

- The intermediate range of 5 < R ∗ < 100 constitutes a transition from one behavior to the other. The data depart from the line B ( R ∗ ) = R ∗ very slowly, reach a maximum near R ∗ = 10 , then fall to a constant value.

Afzal's fit to these data in the transition from smooth pipe flow to rough pipe flow employs an exponential expression in R ∗ that ensures proper behavior for 1 < R ∗ < 50 (the transition from the smooth pipe regime to the rough pipe regime):

${\frac {1}{\sqrt {f_{\mathrm {D} }}}}=-2\log \left({\frac {2.51}{\mathrm {Re} {\sqrt {f_{\mathrm {D} }}}}}\left(1+0.305R_{*}\exp {\frac {-11}{R_{*}}}\right)\right),$

and

${\frac {1}{\sqrt {f_{\mathrm {D} }}}}=-1.93\log \left({\frac {1.90}{\mathrm {Re} {\sqrt {f_{\mathrm {D} }}}}}\left(1+0.34R_{*}\exp {\frac {-11}{R_{*}}}\right)\right),$

This function shares the same values for its term in common with the Kármán–Prandtl resistance equation, plus one parameter 0.305 or 0.34 to fit the asymptotic behavior for R ∗ → ∞ along with one further parameter, 11, to govern the transition from smooth to rough flow. It is exhibited in Figure 3.

The friction factor for another analogous roughness becomes

${\frac {1}{\sqrt {f_{\mathrm {D} }}}}=-2\,\log _{10}\left({\frac {2.51}{\mathrm {Re} {\sqrt {f_{\mathrm {D} }}}}}\left\{1+0.305R_{*}\;\left(1-\exp {\frac {-R_{*}}{26}}\right)\right\}\right),$

and

${\frac {1}{\sqrt {f_{\mathrm {D} }}}}=-1.93\,\log _{10}\left({\frac {1.91}{\mathrm {Re} {\sqrt {f_{\mathrm {D} }}}}}\left\{1+0.34R_{*}\;\left(1-\exp {\frac {-R_{*}}{26}}\right)\right\}\right),$

This function shares the same values for its term in common with the Kármán–Prandtl resistance equation, plus one parameter 0.305 or 0.34 to fit the asymptotic behavior for R ∗ → ∞ along with one further parameter, 26, to govern the transition from smooth to rough flow.

The Colebrook–White relation fits the friction factor with a function of the form

${\frac {1}{\sqrt {f_{\mathrm {D} }}}}=-2.00\log \left({\frac {2.51}{\mathrm {Re} {\sqrt {f_{\mathrm {D} }}}}}\left(1+{\frac {R_{*}}{3.3}}\right)\right).$

This relation has the correct behavior at extreme values of R ∗ , as shown by the labeled curve in Figure 3: when R ∗ is small, it is consistent with smooth pipe flow, when large, it is consistent with rough pipe flow. However its performance in the transitional domain overestimates the friction factor by a substantial margin. Colebrook acknowledges the discrepancy with Nikuradze's data but argues that his relation is consistent with the measurements on commercial pipes. Indeed, such pipes are very different from those carefully prepared by Nikuradse: their surfaces are characterized by many different roughness heights and random spatial distribution of roughness points, while those of Nikuradse have surfaces with uniform roughness height, with the points extremely closely packed.

### Calculating the friction factor from its parametrization

For turbulent flow , methods for finding the friction factor f D include using a diagram, such as the Moody chart , or solving equations such as the Colebrook–White equation (upon which the Moody chart is based), or the Swamee–Jain equation . While the Colebrook–White relation is, in the general case, an iterative method, the Swamee–Jain equation allows f D to be found directly for full flow in a circular pipe.

#### Direct calculation when friction loss S is known

In typical engineering applications, there will be a set of given or known quantities. The acceleration of gravity g and the kinematic viscosity of the fluid ν are known, as are the diameter of the pipe D and its roughness height ε . If as well the head loss per unit length S is a known quantity, then the friction factor f D can be calculated directly from the chosen fitting function. Solving the Darcy–Weisbach equation for √ f D ,

${\sqrt {f_{\mathrm {D} }}}={\frac {\sqrt {2gSD}}{\langle v\rangle }}$

we can now express Re √ f D :

$\mathrm {Re} {\sqrt {f_{\mathrm {D} }}}={\frac {1}{\nu }}{\sqrt {2g}}{\sqrt {S}}{\sqrt {D^{3}}}$

Expressing the roughness Reynolds number R ∗ ,

${\begin{aligned}R_{*}&={\frac {\varepsilon }{D}}\cdot \mathrm {Re} {\sqrt {f_{\mathrm {D} }}}\cdot {\frac {1}{\sqrt {8}}}\\&={\frac {1}{2}}{\frac {\sqrt {g}}{\nu }}\varepsilon {\sqrt {S}}{\sqrt {D}}\end{aligned}}$

we have the two parameters needed to substitute into the Colebrook–White relation, or any other function, for the friction factor f D , the flow velocity ⟨ v ⟩ , and the volumetric flow rate Q .

### Confusion with the Fanning friction factor

The Darcy–Weisbach friction factor f D is 4 times larger than the Fanning friction factor f , so attention must be paid to note which one of these is meant in any "friction factor" chart or equation being used. Of the two, the Darcy–Weisbach factor f D is more commonly used by civil and mechanical engineers, and the Fanning factor f by chemical engineers, but care should be taken to identify the correct factor regardless of the source of the chart or formula.

Note that

$\Delta p=f_{\mathrm {D} }\cdot {\frac {L}{D}}\cdot {\frac {\rho {\langle v\rangle }^{2}}{2}}=f\cdot {\frac {L}{D}}\cdot {2\rho {\langle v\rangle }^{2}}$

Most charts or tables indicate the type of friction factor, or at least provide the formula for the friction factor with laminar flow. If the formula for laminar flow is f = ⁠ 16 / Re ⁠ , it is the Fanning factor f , and if the formula for laminar flow is f D = ⁠ 64 / Re ⁠ , it is the Darcy–Weisbach factor f D .

Which friction factor is plotted in a Moody diagram may be determined by inspection if the publisher did not include the formula described above:

- Observe the value of the friction factor for laminar flow at a Reynolds number of 1000.

- If the value of the friction factor is 0.064, then the Darcy friction factor is plotted in the Moody diagram. Note that the nonzero digits in 0.064 are the numerator in the formula for the laminar Darcy friction factor: f D = ⁠ 64 / Re ⁠ .

- If the value of the friction factor is 0.016, then the Fanning friction factor is plotted in the Moody diagram. Note that the nonzero digits in 0.016 are the numerator in the formula for the laminar Fanning friction factor: f = ⁠ 16 / Re ⁠ .

The procedure above is similar for any available Reynolds number that is an integer power of ten. It is not necessary to remember the value 1000 for this procedure—only that an integer power of ten is of interest for this purpose.

## History

Historically this equation arose as a variant on the Prony equation ; this variant was developed by Henry Darcy of France, and further refined into the form used today by Julius Weisbach of Saxony in 1845. Initially, data on the variation of f D with velocity was lacking, so the Darcy–Weisbach equation was outperformed at first by the empirical Prony equation in many cases. In later years it was eschewed in many special-case situations in favor of a variety of empirical equations valid only for certain flow regimes, notably the Hazen–Williams equation or the Manning equation , most of which were significantly easier to use in calculations. However, since the advent of the calculator , ease of calculation is no longer a major issue, and so the Darcy–Weisbach equation's generality has made it the preferred one.

## Derivation by dimensional analysis

Away from the ends of the pipe, the characteristics of the flow are independent of the position along the pipe. The key quantities are then the pressure drop along the pipe per unit length, ⁠ Δ p / L ⁠ , and the volumetric flow rate. The flow rate can be converted to a mean flow velocity V by dividing by the wetted area of the flow (which equals the cross-sectional area of the pipe if the pipe is full of fluid).

Pressure has dimensions of energy per unit volume, therefore the pressure drop between two points must be proportional to the dynamic pressure q. We also know that pressure must be proportional to the length of the pipe between the two points L as the pressure drop per unit length is a constant. To turn the relationship into a proportionality coefficient of dimensionless quantity, we can divide by the hydraulic diameter of the pipe, D , which is also constant along the pipe. Therefore,

$\Delta p\propto {\frac {L}{D}}q={\frac {L}{D}}\cdot {\frac {\rho }{2}}\cdot {\langle v\rangle }^{2}$

The proportionality coefficient is the dimensionless " Darcy friction factor " or "flow coefficient". This dimensionless coefficient will be a combination of geometric factors such as π , the Reynolds number and (outside the laminar regime) the relative roughness of the pipe (the ratio of the roughness height to the hydraulic diameter ).

Note that the dynamic pressure is not the kinetic energy of the fluid per unit volume, [ citation needed ] for the following reasons. Even in the case of laminar flow , where all the flow lines are parallel to the length of the pipe, the velocity of the fluid on the inner surface of the pipe is zero due to viscosity, and the velocity in the center of the pipe must therefore be larger than the average velocity obtained by dividing the volumetric flow rate by the wet area. The average kinetic energy then involves the root mean-square velocity , which always exceeds the mean velocity. In the case of turbulent flow , the fluid acquires random velocity components in all directions, including perpendicular to the length of the pipe, and thus turbulence contributes to the kinetic energy per unit volume but not to the average lengthwise velocity of the fluid.

## Practical application

In a hydraulic engineering application, it is typical for the volumetric flow Q within a pipe (that is, its productivity) and the head loss per unit length S (the concomitant power consumption) to be the critical important factors. The practical consequence is that, for a fixed volumetric flow rate Q , head loss S decreases with the inverse fifth power of the pipe diameter, D . Doubling the diameter of a pipe of a given schedule (say, ANSI schedule 40) roughly doubles the amount of material required per unit length and thus its installed cost. Meanwhile, the head loss is decreased by a factor of 32 (about a 97% reduction). Thus the energy consumed in moving a given volumetric flow of the fluid is cut down dramatically for a modest increase in capital cost.

## Advantages

The Darcy-Weisbach's accuracy and universal applicability makes it the ideal formula for flow in pipes. The advantages of the equation are as follows:

- It is based on fundamentals.

- It is dimensionally consistent.

- It is useful for any fluid, including oil, gas, brine, and sludges.

- It can be derived analytically in the laminar flow region.

- It is useful in the transition region between laminar flow and fully developed turbulent flow.

- The friction factor variation is well documented.
