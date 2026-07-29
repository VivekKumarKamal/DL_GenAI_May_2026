# Nambu–Goto action

> **Query Topic**: Yoichiro Nambu (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 68, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Nambu–Goto_action

---

The Nambu–Goto action is the simplest invariant action in bosonic string theory , and is also used in other theories that investigate string-like objects (for example, cosmic strings ). It is the starting point of the analysis of zero-thickness (infinitely thin) string behaviour, using the principles of Lagrangian mechanics . Just as the action for a free point particle is proportional to its proper time – i.e. , the "length" of its world-line – a relativistic string's action is proportional to the area of the sheet which the string traces as it travels through spacetime.

It is named after Japanese physicists Yoichiro Nambu and Tetsuo Goto [ ja ] .

## Background

### Relativistic Lagrangian mechanics

The basic principle of Lagrangian mechanics, the principle of stationary action , is that an object subjected to outside influences will "choose" a path which makes a certain quantity, the action , an extremum. The action is a functional , a mathematical relationship which takes an entire path and produces a single number. The physical path , that which the object actually follows, is the path for which the action is "stationary" (or extremal): any small variation of the path from the physical one does not significantly change the action. (Often, this is equivalent to saying the physical path is the one for which the action is a minimum.) Actions are typically written using Lagrangians, formulas which depend upon the object's state at a particular point in space and/or time. In non-relativistic mechanics, for example, a point particle's Lagrangian is the difference between kinetic and potential energy: $L=K-U$ . The action, often written $S$ , is then the integral of this quantity from a starting time to an ending time:

$S=\int _{t_{\text{i}}}^{t_{\text{f}}}L\,dt.$

(Typically, when using Lagrangians, we assume we know the particle's starting and ending positions, and we concern ourselves with the path which the particle travels between those positions.)

This approach to mechanics has the advantage that it is easily extended and generalized. For example, we can write a Lagrangian for a relativistic particle, which will be valid even if the particle is traveling close to the speed of light. To preserve Lorentz invariance , the action should only depend upon quantities that are the same for all (Lorentz) observers, i.e. the action should be a Lorentz scalar . The simplest such quantity is the proper time , the time measured by a clock carried by the particle. According to special relativity, all Lorentz observers watching a particle move will compute the same value for the quantity

$-ds^{2}=-(c\,dt)^{2}+dx^{2}+dy^{2}+dz^{2},\$

and $ds/c$ is then an infinitesimal proper time. For a point particle not subject to external forces (i.e., one undergoing inertial motion), the relativistic action is

$S=-mc\int ds.$

### World-sheets

Just as a zero-dimensional point traces out a world-line on a spacetime diagram, a one-dimensional string is represented by a world-sheet . All world-sheets are two-dimensional surfaces, hence we need two parameters to specify a point on a world-sheet. String theorists use the symbols $\tau$ and $\sigma$ for these parameters. As it turns out, string theories involve higher-dimensional spaces than the 3D world with which we are familiar; bosonic string theory requires 25 spatial dimensions and one time axis. If $d$ is the number of spatial dimensions, we can represent a point by the vector

$x=(x^{0},x^{1},x^{2},\ldots ,x^{d}).$

We describe a string using functions which map a position in the parameter space ( $\tau$ , $\sigma$ ) to a point in spacetime. For each value of $\tau$ and $\sigma$ , these functions specify a unique spacetime vector:

$X(\tau ,\sigma )=(X^{0}(\tau ,\sigma ),X^{1}(\tau ,\sigma ),X^{2}(\tau ,\sigma ),\ldots ,X^{d}(\tau ,\sigma )).$

The functions $X^{\mu }(\tau ,\sigma )$ determine the shape which the world-sheet takes. Different Lorentz observers will disagree on the coordinates they assign to particular points on the world-sheet, but they must all agree on the total proper area which the world-sheet has. The Nambu–Goto action is chosen to be proportional to this total proper area.

Let $\eta _{\mu \nu }$ be the metric on the $(d+1)$ -dimensional spacetime. Then,

$g_{ab}=\eta _{\mu \nu }{\frac {\partial X^{\mu }}{\partial y^{a}}}{\frac {\partial X^{\nu }}{\partial y^{b}}}\$

is the induced metric on the world-sheet, where $a,b=0,1$ and $y^{0}=\tau ,y^{1}=\sigma$ .

For the area ${\mathcal {A}}$ of the world-sheet the following holds:

$\mathrm {d} {\mathcal {A}}=\mathrm {d} ^{2}\Sigma {\sqrt {-g}}$

where $\mathrm {d} ^{2}\Sigma =\mathrm {d} \sigma \,\mathrm {d} \tau$ and $g=\mathrm {det} \left(g_{ab}\right)\$

Using the notation that:

${\dot {X}}={\frac {\partial X}{\partial \tau }}$

and

$X'={\frac {\partial X}{\partial \sigma }},$

one can rewrite the metric $g_{ab}$ :

$g_{ab}=\left({\begin{array}{cc}{\dot {X}}^{2}&{\dot {X}}\cdot X'\\X'\cdot {\dot {X}}&X'^{2}\end{array}}\right)\$

$g={\dot {X}}^{2}X'^{2}-({\dot {X}}\cdot X')^{2}$

the Nambu–Goto action is defined as

where $X\cdot Y:=\eta _{\mu \nu }X^{\mu }Y^{\nu }$ .
The factors before the integral give the action the correct units, energy multiplied by time. $T_{0}$ is the tension in the string, and $c$ is the speed of light. Typically, string theorists work in "natural units" where $c$ is set to 1 (along with the reduced Planck constant $\hbar$ and the Newtonian constant of gravitation $G$ ). Also, partly for historical reasons, they use the "slope parameter" $\alpha '$ instead of $T_{0}$ . With these changes, the Nambu–Goto action becomes

${\mathcal {S}}=-{\frac {1}{2\pi \alpha '}}\int \mathrm {d} ^{2}\Sigma {\sqrt {({\dot {X}}\cdot X')^{2}-({\dot {X}})^{2}(X')^{2}}}.$

These two forms are, of course, entirely equivalent: choosing one over the other is a matter of convention and convenience.

Two further equivalent forms ( on shell but not off shell) are

${\mathcal {S}}=-{\frac {1}{2\pi \alpha '}}\int \mathrm {d} ^{2}\Sigma {\sqrt {{\dot {X}}^{2}-{X'}^{2}}},$

and

${\mathcal {S}}=-{\frac {1}{4\pi \alpha '}}\int \mathrm {d} ^{2}\Sigma ({\dot {X}}^{2}-{X'}^{2}).$

The conjugate momentum field

$P=-{\frac {T}{\sqrt {({\dot {X}}\cdot X')^{2}-{\dot {X}}^{2}{X'}^{2}}}}\left[X'({\dot {X}}\cdot X')-{\dot {X}}{X'}^{2}\right]$ .

Then,

$P^{2}={\frac {T^{2}}{({\dot {X}}\cdot X')^{2}-{\dot {X}}^{2}{X'}^{2}}}\left[{X'}^{2}({\dot {X}}\cdot X')^{2}-2({\dot {X}}\cdot X')^{2}X'^{2}+{\dot {X}}^{2}{X'}^{4}\right]=-T^{2}{X'}^{2}$

is a primary constraint . The secondary constraint is $P\cdot X'=0$ . These constraints generate timelike diffeomorphisms and spacelike diffeomorphisms on the worldsheet. The Hamiltonian $H=P\cdot {\dot {X}}-{\mathcal {L}}=0$ . The extended Hamiltonian is given by

$H=\int d\sigma \left[\lambda (P^{2}+T^{2}{X'}^{2})+\rho P\cdot X'\right]$

where $\lambda$ and $\rho$ are Lagrange multipliers .

The equations of motion satisfy the Virasoro constraints ${\dot {X}}^{2}+X'^{2}=0$ and ${\dot {X}}\cdot X'=0$ .

Typically, the Nambu–Goto action does not yet have the form appropriate for studying the quantum physics of strings. For this it must be modified in a similar way as the action of a point particle. That is classically equal to minus mass times the invariant length in spacetime, but must be replaced by a quadratic expression with the same classical value. For strings the analog correction is provided by the Polyakov action , which is classically equivalent to the Nambu–Goto action, but gives the 'correct' quantum theory. It is, however, possible to develop a quantum theory from the Nambu–Goto action in the light cone gauge .
