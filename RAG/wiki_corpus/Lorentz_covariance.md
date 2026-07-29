# Lorentz covariance

> **Query Topic**: Lorentz symmetry or Lorentz invariance in relativistic physics (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 7, Frequency: 15)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Lorentz_covariance

---

In relativistic physics , Lorentz symmetry or Lorentz invariance , named after the Dutch physicist Hendrik Lorentz , is an equivalence of observation or observational symmetry due to special relativity implying that the laws of physics stay the same for all observers that are moving with respect to one another within an inertial frame . It has also been described as "the feature of nature that says experimental results are independent of the orientation or the boost velocity of the laboratory through space".

Lorentz covariance , a related concept, is a property of the underlying spacetime manifold. Lorentz covariance has two distinct, but closely related meanings:

- A physical quantity is said to be Lorentz covariant if it transforms under a given representation of the Lorentz group . According to the representation theory of the Lorentz group , these quantities are built out of scalars , four-vectors , four-tensors , and spinors . In particular, a Lorentz covariant scalar (e.g., the space-time interval ) remains the same under Lorentz transformations and is said to be a Lorentz invariant (i.e., they transform under the trivial representation ).

- An equation is said to be Lorentz covariant if it can be written in terms of Lorentz covariant quantities (confusingly, some use the term invariant here). The key property of such equations is that if they hold in one inertial frame, then they hold in any inertial frame; this follows from the result that if all the components of a tensor vanish in one frame, they vanish in every frame. This condition is a requirement according to the principle of relativity ; i.e., all non- gravitational laws must make the same predictions for identical experiments taking place at the same spacetime event in two different inertial frames of reference .

On manifolds , the words covariant and contravariant refer to how objects transform under general coordinate transformations. Both covariant and contravariant four-vectors can be Lorentz covariant quantities.

Local Lorentz covariance , which follows from general relativity , refers to Lorentz covariance applying only locally in an infinitesimal region of spacetime at every point. There is a generalization of this concept to cover Poincaré covariance and Poincaré invariance.

## Examples

In general, the (transformational) nature of a Lorentz tensor [ clarification needed ] can be identified by its tensor order , which is the number of free indices it has. No indices implies it is a scalar, one implies that it is a vector, etc. Some tensors with a physical interpretation are listed below.

The sign convention of the Minkowski metric η = diag (1, −1, −1, −1) is used throughout the article.

### Scalars

$\Delta s^{2}=\Delta x^{a}\Delta x^{b}\eta _{ab}=c^{2}\Delta t^{2}-\Delta x^{2}-\Delta y^{2}-\Delta z^{2}$

$\Delta \tau ={\sqrt {\frac {\Delta s^{2}}{c^{2}}}},\,\Delta s^{2}>0$

$L={\sqrt {-\Delta s^{2}}},\,\Delta s^{2}<0$

$m_{0}^{2}c^{2}=P^{a}P^{b}\eta _{ab}={\frac {E^{2}}{c^{2}}}-p_{x}^{2}-p_{y}^{2}-p_{z}^{2}$

${\begin{aligned}F_{ab}F^{ab}&=\ 2\left(B^{2}-{\frac {E^{2}}{c^{2}}}\right)\\G_{cd}F^{cd}&={\frac {1}{2}}\epsilon _{abcd}F^{ab}F^{cd}=-{\frac {4}{c}}\left({\vec {B}}\cdot {\vec {E}}\right)\end{aligned}}$

$\Box =\eta ^{\mu \nu }\partial _{\mu }\partial _{\nu }={\frac {1}{c^{2}}}{\frac {\partial ^{2}}{\partial t^{2}}}-{\frac {\partial ^{2}}{\partial x^{2}}}-{\frac {\partial ^{2}}{\partial y^{2}}}-{\frac {\partial ^{2}}{\partial z^{2}}}$

### Four-vectors

$\Delta X^{a}=\left(c\Delta t,\Delta {\vec {x}}\right)=(c\Delta t,\Delta x,\Delta y,\Delta z)$

$X^{a}=\left(ct,{\vec {x}}\right)=(ct,x,y,z)$

which is the 4D partial derivative : $\partial ^{a}=\left({\frac {\partial _{t}}{c}},-{\vec {\nabla }}\right)=\left({\frac {1}{c}}{\frac {\partial }{\partial t}},-{\frac {\partial }{\partial x}},-{\frac {\partial }{\partial y}},-{\frac {\partial }{\partial z}}\right)$

$U^{a}=\gamma \left(c,{\vec {u}}\right)=\gamma \left(c,{\frac {dx}{dt}},{\frac {dy}{dt}},{\frac {dz}{dt}}\right)$ where $U^{a}={\frac {dX^{a}}{d\tau }}$

$P^{a}=\left(\gamma mc,\gamma m{\vec {v}}\right)=\left({\frac {E}{c}},{\vec {p}}\right)=\left({\frac {E}{c}},p_{x},p_{y},p_{z}\right)$ where $P^{a}=mU^{a}$ and $m$ is the rest mass .

$J^{a}=\left(c\rho ,{\vec {j}}\right)=\left(c\rho ,j_{x},j_{y},j_{z}\right)$ where $J^{a}=\rho _{o}U^{a}$

$A^{a}=\left({\frac {\phi }{c}},{\vec {A}}\right)=\left({\frac {\phi }{c}},A_{x},A_{y},A_{z}\right)$

### Four-tensors

$\delta _{b}^{a}={\begin{cases}1&{\mbox{if }}a=b,\\0&{\mbox{if }}a\neq b.\end{cases}}$

$\eta _{ab}=\eta ^{ab}={\begin{cases}1&{\mbox{if }}a=b=0,\\-1&{\mbox{if }}a=b=1,2,3,\\0&{\mbox{if }}a\neq b.\end{cases}}$

$F_{ab}={\begin{bmatrix}0&{\frac {1}{c}}E_{x}&{\frac {1}{c}}E_{y}&{\frac {1}{c}}E_{z}\\-{\frac {1}{c}}E_{x}&0&-B_{z}&B_{y}\\-{\frac {1}{c}}E_{y}&B_{z}&0&-B_{x}\\-{\frac {1}{c}}E_{z}&-B_{y}&B_{x}&0\end{bmatrix}}$

$G_{cd}={\frac {1}{2}}\epsilon _{abcd}F^{ab}={\begin{bmatrix}0&B_{x}&B_{y}&B_{z}\\-B_{x}&0&{\frac {1}{c}}E_{z}&-{\frac {1}{c}}E_{y}\\-B_{y}&-{\frac {1}{c}}E_{z}&0&{\frac {1}{c}}E_{x}\\-B_{z}&{\frac {1}{c}}E_{y}&-{\frac {1}{c}}E_{x}&0\end{bmatrix}}$

## Lorentz violating models

In standard field theory, there are very strict and severe constraints on marginal and relevant Lorentz violating operators within both QED and the Standard Model . Irrelevant Lorentz violating operators may be suppressed by a high cutoff scale, but they typically induce marginal and relevant Lorentz violating operators via radiative corrections. So, we also have very strict and severe constraints on irrelevant Lorentz violating operators.

Since some approaches to quantum gravity lead to violations of Lorentz invariance, these studies are part of phenomenological quantum gravity . Lorentz violations are allowed in string theory , supersymmetry and Hořava–Lifshitz gravity .

Lorentz violating models typically fall into four classes: [ citation needed ]

- The laws of physics are exactly Lorentz covariant but this symmetry is spontaneously broken . In special relativistic theories, this leads to phonons , which are the Goldstone bosons . The phonons travel at less than the speed of light .

- Similar to the approximate Lorentz symmetry of phonons in a lattice (where the speed of sound plays the role of the critical speed), the Lorentz symmetry of special relativity (with the speed of light as the critical speed in vacuum) is only a low-energy limit of the laws of physics, which involve new phenomena at some fundamental scale. Bare conventional "elementary" particles are not point-like field-theoretical objects at very small distance scales, and a nonzero fundamental length must be taken into account. Lorentz symmetry violation is governed by an energy-dependent parameter which tends to zero as momentum decreases. Such patterns require the existence of a privileged local inertial frame (the "vacuum rest frame"). They can be tested, at least partially, by ultra-high energy cosmic ray experiments like the Pierre Auger Observatory .

- The laws of physics are symmetric under a deformation of the Lorentz or more generally, the Poincaré group , and this deformed symmetry is exact and unbroken. This deformed symmetry is also typically a quantum group symmetry, which is a generalization of a group symmetry. Deformed special relativity is an example of this class of models. The deformation is scale dependent, meaning that at length scales much larger than the Planck scale, the symmetry looks pretty much like the Poincaré group. Ultra-high energy cosmic ray experiments cannot test such models.

- Very special relativity forms a class of its own; if charge-parity (CP) is an exact symmetry, a subgroup of the Lorentz group is sufficient to give us all the standard predictions. This is, however, not the case.

Models belonging to the first two classes can be consistent with experiment if Lorentz breaking happens at Planck scale or beyond it, or even before it in suitable preonic models, and if Lorentz symmetry violation is governed by a suitable energy-dependent parameter. One then has a class of models which deviate from Poincaré symmetry near the Planck scale but still flows towards an exact Poincaré group at very large length scales. This is also true for the third class, which is furthermore protected from radiative corrections as one still has an exact (quantum) symmetry.

Even though there is no evidence of the violation of Lorentz invariance, several experimental searches for such violations have been performed during recent years. A detailed summary of the results of these searches is given in the Data Tables for Lorentz and CPT Violation.

Lorentz invariance is also violated in QFT assuming non-zero temperature.

There is also growing evidence of Lorentz violation in Weyl semimetals and Dirac semimetals .
