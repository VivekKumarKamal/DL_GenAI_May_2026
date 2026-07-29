# Mathematical formulation of the Standard Model

> **Query Topic**: explanation for the effective supersymmetry in quark-diquark models (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 348, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Mathematical_formulation_of_the_Standard_Model

---

The Standard Model of particle physics is a gauge quantum field theory containing the internal symmetries of the unitary product group SU (3) × SU(2) × U(1) . The theory is commonly viewed as describing the fundamental set of particles – the leptons , quarks , gauge bosons and the Higgs boson .

The Standard Model is renormalizable and mathematically self-consistent; however, despite having huge and continued successes in providing experimental predictions, it does leave some unexplained phenomena . In particular, although the physics of special relativity is incorporated, general relativity is not, and the Standard Model will fail at energies or distances where the graviton is expected to emerge. Therefore, in a modern field theory context, it is seen as an effective field theory .

## Quantum field theory

The standard model is a quantum field theory , meaning its fundamental objects are quantum fields , which are defined at all points in spacetime. QFT treats particles as excited states (also called quanta ) of their underlying quantum fields , which are more fundamental than the particles. These fields are

- the fermion fields, ψ , which account for "matter particles";

- the electroweak boson fields $W_{1}$ , $W_{2}$ , $W_{3}$ , and B ;

- the gluon field , G a ; and

- the Higgs field , φ .

That these are quantum rather than classical fields has the mathematical consequence that they are operator -valued. In particular, values of the fields generally do not commute. As operators, they act upon a quantum state ( ket vector ).

## Alternative presentations of the fields

As is common in quantum theory, there is more than one way to look at things. At first the basic fields given above may not seem to correspond well with the "fundamental particles" in the chart above, but there are several alternative presentations that, in particular contexts, may be more appropriate than those that are given above.

### Fermions

Rather than having one fermion field ψ , it can be split up into separate components for each type of particle. This mirrors the historical evolution of quantum field theory, since the electron component ψ e (describing the electron and its antiparticle the positron ) is then the original ψ field of quantum electrodynamics , which was later accompanied by ψ μ and ψ τ fields for the muon and tauon respectively (and their antiparticles). Electroweak theory added $\psi _{\nu _{\mathrm {e} }},\psi _{\nu _{\mu }}$ , and $\psi _{\nu _{\tau }}$ for the corresponding neutrinos . The quarks add still further components. In order to be four-spinors like the electron and other lepton components, there must be one quark component for every combination of flavor and color , bringing the total to 24 (3 for charged leptons, 3 for neutrinos, and 2·3·3 = 18 for quarks). Each of these is a four component Dirac spinor , for a total of 96 complex-valued components for the fermion field.

An important definition is the barred fermion field ${\bar {\psi }}$ , which is defined to be $\psi ^{\dagger }\gamma ^{0}$ , where $\dagger$ denotes the Hermitian adjoint of ψ , and γ 0 is the zeroth gamma matrix . If ψ is thought of as an n × 1 matrix then ${\bar {\psi }}$ should be thought of as a 1 × n matrix .

#### A chiral theory

An independent decomposition of ψ is that into chirality components:

- "Left" chirality: $\psi ^{\rm {L}}={\frac {1}{2}}(1-\gamma _{5})\psi$

- "Right" chirality: $\psi ^{\rm {R}}={\frac {1}{2}}(1+\gamma _{5})\psi$

where $\gamma _{5}$ is the fifth gamma matrix . This is very important in the Standard Model because left and right chirality components are treated differently by the gauge interactions .

In particular, under weak isospin SU(2) transformations the left-handed particles are weak-isospin doublets, whereas the right-handed are singlets – i.e. the weak isospin of ψ R is zero. Put more simply, the weak interaction could rotate e.g. a left-handed electron into a left-handed neutrino (with emission of a W − ), but could not do so with the same right-handed particles. As an aside, the right-handed neutrino originally did not exist in the standard model – but the discovery of neutrino oscillation implies that neutrinos must have mass , and since chirality can change during the propagation of a massive particle, right-handed neutrinos must exist in reality. This does not however change the (experimentally demonstrated) chiral nature of the weak interaction.

Furthermore, U(1) acts differently on $\psi _{\mathrm {e} }^{\rm {L}}$ and $\psi _{\mathrm {e} }^{\rm {R}}$ (because they have different weak hypercharges ).

#### Mass and interaction eigenstates

A distinction can thus be made between, for example, the mass and interaction eigenstates of the neutrino. The former is the state that propagates in free space, whereas the latter is the different state that participates in interactions. Which is the "fundamental" particle? For the neutrino, it is conventional to define the "flavor" ( ν e , ν μ , or ν τ ) by the interaction eigenstate, whereas for the quarks we define the flavor (up, down, etc.) by the mass state. We can switch between these states using the CKM matrix for the quarks, or the PMNS matrix for the neutrinos (the charged leptons on the other hand are eigenstates of both mass and flavor).

As an aside, if a complex phase term exists within either of these matrices, it will give rise to direct CP violation , which could explain the dominance of matter over antimatter in our current universe. This has been proven for the CKM matrix, and is expected for the PMNS matrix.

#### Positive and negative energies

Finally, the quantum fields are sometimes decomposed into "positive" and "negative" energy parts: ψ = ψ + + ψ − . This is not so common when a quantum field theory has been set up, but often features prominently in the process of quantizing a field theory.

### Bosons

Due to the Higgs mechanism , the electroweak boson fields $W_{1}$ , $W_{2}$ , $W_{3}$ , and $B$ "mix" to create the states that are physically observable. To retain gauge invariance, the underlying fields must be massless, but the observable states can gain masses in the process. These states are:

The massive neutral (Z) boson : $Z=\cos \theta _{\rm {W}}W_{3}-\sin \theta _{\rm {W}}B$

The massless neutral boson: $A=\sin \theta _{\rm {W}}W_{3}+\cos \theta _{\rm {W}}B$

The massive charged W bosons : $W^{\pm }={\frac {1}{\sqrt {2}}}\left(W_{1}\mp iW_{2}\right)$ where θ W is the Weinberg angle .

The A field is the photon , which corresponds classically to the well-known electromagnetic four-potential – i.e. the electric and magnetic fields. The Z field actually contributes in every process the photon does, but due to its large mass, the contribution is usually negligible.

## Perturbative QFT and the interaction picture

Much of the qualitative descriptions of the Standard Model in terms of "particles" and "forces" comes from the perturbative quantum field theory view of the model. In this, the Lagrangian is decomposed as ${\mathcal {L}}={\mathcal {L}}_{0}+{\mathcal {L}}_{\mathrm {I} }$ into separate free field and interaction Lagrangians. The free fields care for particles in isolation, whereas processes involving several particles arise through interactions. The idea is that the state vector should only change when particles interact, meaning a free particle is one whose quantum state is constant. This corresponds to the interaction picture in quantum mechanics.

In the more common Schrödinger picture , even the states of free particles change over time: typically the phase changes at a rate that depends on their energy. In the alternative Heisenberg picture , state vectors are kept constant, at the price of having the operators (in particular the observables ) be time-dependent. The interaction picture constitutes an intermediate between the two, where some time dependence is placed in the operators (the quantum fields) and some in the state vector. In QFT, the former is called the free field part of the model, and the latter is called the interaction part. The free field model can be solved exactly, and then the solutions to the full model can be expressed as perturbations of the free field solutions, for example using the Dyson series .

It should be observed that the decomposition into free fields and interactions is in principle arbitrary. For example, renormalization in QED modifies the mass of the free field electron to match that of a physical electron (with an electromagnetic field), and will in doing so add a term to the free field Lagrangian which must be cancelled by a counterterm in the interaction Lagrangian, that then shows up as a two-line vertex in the Feynman diagrams . This is also how the Higgs field is thought to give particles mass : the part of the interaction term that corresponds to the nonzero vacuum expectation value of the Higgs field is moved from the interaction to the free field Lagrangian, where it looks just like a mass term having nothing to do with the Higgs field.

### Free fields

Under the usual free/interaction decomposition, which is suitable for low energies, the free fields obey the following equations:

- The fermion field ψ satisfies the Dirac equation ; $(i\hbar \gamma ^{\mu }\partial _{\mu }-m_{\rm {f}}c)\psi _{\rm {f}}=0$ for each type $f$ of fermion.

- The photon field A satisfies the wave equation $\partial _{\mu }\partial ^{\mu }A^{\nu }=0$ .

- The Higgs field φ satisfies the Klein–Gordon equation .

- The weak interaction fields Z , W ± satisfy the Proca equation .

These equations can be solved exactly. One usually does so by considering first solutions that are periodic with some period L along each spatial axis; later taking the limit: L → ∞ will lift this periodicity restriction.

In the periodic case, the solution for a field F (any of the above) can be expressed as a Fourier series of the form $F(x)=\beta \sum _{\mathbf {p} }\sum _{r}E_{\mathbf {p} }^{-{\frac {1}{2}}}\left(a_{r}(\mathbf {p} )u_{r}(\mathbf {p} )e^{-{\frac {ipx}{\hbar }}}+b_{r}^{\dagger }(\mathbf {p} )v_{r}(\mathbf {p} )e^{\frac {ipx}{\hbar }}\right)$ where:

- β is a normalization factor; for the fermion field $\psi _{\rm {f}}$ it is ${\textstyle {\sqrt {m_{\rm {f}}c^{2}/V}}}$ , where $V=L^{3}$ is the volume of the fundamental cell considered; for the photon field A μ it is $\hbar c/{\sqrt {2V}}$ .

- The sum over p is over all momenta consistent with the period L , i.e., over all vectors ${\frac {2\pi \hbar }{L}}(n_{1},n_{2},n_{3})$ where $n_{1},n_{2},n_{3}$ are integers.

- The sum over r covers other degrees of freedom specific for the field, such as polarization or spin; it usually comes out as a sum from 1 to 2 or from 1 to 3 .

- E p is the relativistic energy for a momentum p quantum of the field, ${\textstyle ={\sqrt {m^{2}c^{4}+c^{2}\mathbf {p} ^{2}}}}$ when the rest mass is m .

- a r ( p ) and $b_{r}^{\dagger }(\mathbf {p} )$ are annihilation and creation operators respectively for "a-particles" and "b-particles" respectively of momentum p ; "b-particles" are the antiparticles of "a-particles". Different fields have different "a-" and "b-particles". For some fields, a and b are the same.

- u r ( p ) and v r ( p ) are non-operators that carry the vector or spinor aspects of the field (where relevant).

- $p=(E_{\mathbf {p} }/c,\mathbf {p} )$ is the four-momentum for a quantum with momentum p . $px=p_{\mu }x^{\mu }$ denotes an inner product of four-vectors .

In the limit L → ∞ , the sum would turn into an integral with help from the V hidden inside β . The numeric value of β also depends on the normalization chosen for $u_{r}(\mathbf {p} )$ and $v_{r}(\mathbf {p} )$ .

Technically, $a_{r}^{\dagger }(\mathbf {p} )$ is the Hermitian adjoint of the operator a r ( p ) in the inner product space of ket vectors . The identification of $a_{r}^{\dagger }(\mathbf {p} )$ and a r ( p ) as creation and annihilation operators comes from comparing conserved quantities for a state before and after one of these have acted upon it. $a_{r}^{\dagger }(\mathbf {p} )$ can for example be seen to add one particle, because it will add 1 to the eigenvalue of the a-particle number operator , and the momentum of that particle ought to be p since the eigenvalue of the vector-valued momentum operator increases by that much. For these derivations, one starts out with expressions for the operators in terms of the quantum fields. That the operators with $\dagger$ are creation operators and the one without $\dagger$ are annihilation operators is a convention, imposed by the sign of the commutation relations postulated for them.

An important step in preparation for calculating in perturbative quantum field theory is to separate the "operator" factors a and b above from their corresponding vector or spinor factors u and v . The vertices of Feynman graphs come from the way that u and v from different factors in the interaction Lagrangian fit together, whereas the edges come from the way that the a s and b s must be moved around in order to put terms in the Dyson series on normal form.

### Interaction terms and the path integral approach

The Lagrangian can also be derived without using creation and annihilation operators (the "canonical" formalism) by using a path integral formulation , pioneered by Feynman building on the earlier work of Dirac. Feynman diagrams are pictorial representations of interaction terms. A quick derivation is indeed presented at the article on Feynman diagrams .

## Lagrangian formalism

We can now give some more detail about the aforementioned free and interaction terms appearing in the Standard Model Lagrangian density . Any such term must be both gauge and reference-frame invariant, otherwise the laws of physics would depend on an arbitrary choice or the frame of an observer. Therefore, the global Poincaré symmetry , consisting of translational symmetry , rotational symmetry and the inertial reference frame invariance central to the theory of special relativity must apply. The local SU(3) × SU(2) × U(1) gauge symmetry is the internal symmetry . The three factors of the gauge symmetry together give rise to the three fundamental interactions, after some appropriate relations have been defined, as we shall see.

### Kinetic terms

A free particle can be represented by a mass term, and a kinetic term that relates to the "motion" of the fields.

#### Fermion fields

The kinetic term for a Dirac fermion is $i{\bar {\psi }}\gamma ^{\mu }\partial _{\mu }\psi$ where the notations are carried from earlier in the article. ψ can represent any, or all, Dirac fermions in the standard model. Generally, as below, this term is included within the couplings (creating an overall "dynamical" term).

#### Gauge fields

For the spin-1 fields, first define the field strength tensor $F_{\mu \nu }^{a}=\partial _{\mu }A_{\nu }^{a}-\partial _{\nu }A_{\mu }^{a}+gf^{abc}A_{\mu }^{b}A_{\nu }^{c}$ for a given gauge field (here we use A ), with gauge coupling constant g . The quantity f abc is the structure constant of the particular gauge group, defined by the commutator $[t_{a},t_{b}]=if^{abc}t_{c},$ where t i are the generators of the group. In an abelian (commutative) group (such as the U(1) we use here) the structure constants vanish, since the generators t a all commute with each other. Of course, this is not the case in general – the standard model includes the non-Abelian SU(2) and SU(3) groups (such groups lead to what is called a Yang–Mills gauge theory ).

We need to introduce three gauge fields corresponding to each of the subgroups SU(3) × SU(2) × U(1) .

- The gluon field tensor will be denoted by $G_{\mu \nu }^{a}$ , where the index a labels elements of the 8 representation of color SU(3) . The strong coupling constant is conventionally labelled g s (or simply g where there is no ambiguity). The observations leading to the discovery of this part of the Standard Model are discussed in the article in quantum chromodynamics .

- The notation $W_{\mu \nu }^{a}$ will be used for the gauge field tensor of SU(2) where a runs over the 3 generators of this group. The coupling can be denoted g w or again simply g . The gauge field will be denoted by $W_{\mu }^{a}$ .

- The gauge field tensor for the U(1) of weak hypercharge will be denoted by B μν , the coupling by g ′ , and the gauge field by B μ .

The kinetic term can now be written as ${\mathcal {L}}_{\rm {kin}}=-{1 \over 4}B_{\mu \nu }B^{\mu \nu }-{1 \over 2}\mathrm {tr} W_{\mu \nu }W^{\mu \nu }-{1 \over 2}\mathrm {tr} G_{\mu \nu }G^{\mu \nu }$ where the traces are over the SU(2) and SU(3) indices hidden in W and G respectively. The two-index objects are the field strengths derived from W and G the vector fields. There are also two extra hidden parameters: the theta angles for SU(2) and SU(3) .

### Coupling terms

The next step is to "couple" the gauge fields to the fermions, allowing for interactions.

#### Electroweak sector

The electroweak sector interacts with the symmetry group U(1) × SU(2) L , where the subscript L indicates coupling only to left-handed fermions. ${\mathcal {L}}_{\mathrm {EW} }=\sum _{\psi }{\bar {\psi }}\gamma ^{\mu }\left(i\partial _{\mu }-g^{\prime }{1 \over 2}Y_{\mathrm {W} }B_{\mu }-g{1 \over 2}{\boldsymbol {\tau }}\cdot \mathbf {W} _{\mu }\right)\psi$ where B μ is the U(1) gauge field; Y W is the weak hypercharge (the generator of the U(1) group); W μ is the three-component SU(2) gauge field; and the components of τ are the Pauli matrices (infinitesimal generators of the SU(2) group) whose eigenvalues give the weak isospin. Note that we have to redefine a new U(1) symmetry of weak hypercharge , different from QED, in order to achieve the unification with the weak force. The electric charge Q , third component of weak isospin T 3 (also called T z , I 3 or I z ) and weak hypercharge Y W are related by $Q=T_{3}+{\tfrac {1}{2}}Y_{\rm {W}},$ (or by the alternative convention Q = T 3 + Y W ). The first convention, used in this article, is equivalent to the earlier Gell-Mann–Nishijima formula . It makes the hypercharge be twice the average charge of a given isomultiplet.

One may then define the conserved current for weak isospin as $\mathbf {j} _{\mu }={1 \over 2}{\bar {\psi }}_{\rm {L}}\gamma _{\mu }{\boldsymbol {\tau }}\psi _{\rm {L}}$ and for weak hypercharge as $j_{\mu }^{Y}=2(j_{\mu }^{\rm {em}}-j_{\mu }^{3})~,$ where $j_{\mu }^{\rm {em}}$ is the electric current and $j_{\mu }^{3}$ the third weak isospin current. As explained above , these currents mix to create the physically observed bosons, which also leads to testable relations between the coupling constants.

To explain this in a simpler way, we can see the effect of the electroweak interaction by picking out terms from the Lagrangian. We see that the SU(2) symmetry acts on each (left-handed) fermion doublet contained in ψ , for example $-{g \over 2}({\bar {\nu }}_{e}\;{\bar {e}})\tau ^{+}\gamma _{\mu }(W^{+})^{\mu }{\begin{pmatrix}{\nu _{e}}\\e\end{pmatrix}}=-{g \over 2}{\bar {\nu }}_{e}\gamma _{\mu }(W^{+})^{\mu }e$ where the particles are understood to be left-handed, and where $\tau ^{+}\equiv {1 \over 2}(\tau ^{1}{+}i\tau ^{2})={\begin{pmatrix}0&1\\0&0\end{pmatrix}}$

This is an interaction corresponding to a "rotation in weak isospin space" or in other words, a transformation between e L and ν eL via emission of a W − boson. The U(1) symmetry, on the other hand, is similar to electromagnetism, but acts on all " weak hypercharged " fermions (both left- and right-handed) via the neutral Z 0 , as well as the charged fermions via the photon.

#### Quantum chromodynamics sector

The quantum chromodynamics (QCD) sector defines the interactions between quarks and gluons , with SU(3) symmetry, generated by T a . Since leptons do not interact with gluons, they are not affected by this sector. The Dirac Lagrangian of the quarks coupled to the gluon fields is given by ${\mathcal {L}}_{\mathrm {QCD} }=i{\overline {U}}\left(\partial _{\mu }-ig_{s}G_{\mu }^{a}T^{a}\right)\gamma ^{\mu }U+i{\overline {D}}\left(\partial _{\mu }-ig_{s}G_{\mu }^{a}T^{a}\right)\gamma ^{\mu }D.$ where U and D are the Dirac spinors associated with up and down-type quarks, and other notations are continued from the previous section.

### Mass terms and the Higgs mechanism

#### Mass terms

The mass term arising from the Dirac Lagrangian (for any fermion ψ ) is $-m{\bar {\psi }}\psi$ , which is not invariant under the electroweak symmetry. This can be seen by writing ψ in terms of left and right-handed components (skipping the actual calculation): $-m{\bar {\psi }}\psi =-m({\bar {\psi }}_{\rm {L}}\psi _{\rm {R}}+{\bar {\psi }}_{\rm {R}}\psi _{\rm {L}})$ i.e. contribution from ${\bar {\psi }}_{\rm {L}}\psi _{\rm {L}}$ and ${\bar {\psi }}_{\rm {R}}\psi _{\rm {R}}$ terms do not appear. We see that the mass-generating interaction is achieved by constant flipping of particle chirality. The spin-half particles have no right/left chirality pair with the same SU(2) representations and equal and opposite weak hypercharges, so assuming these gauge charges are conserved in the vacuum, none of the spin-half particles could ever swap chirality, and must remain massless. Additionally, we know experimentally that the W and Z bosons are massive, but a boson mass term contains the combination e.g. A μ A μ , which clearly depends on the choice of gauge. Therefore, none of the standard model fermions or bosons can "begin" with mass, but must acquire it by some other mechanism.

#### Higgs mechanism

The solution to both these problems comes from the Higgs mechanism , which involves scalar fields (the number of which depend on the exact form of Higgs mechanism) which (to give the briefest possible description) are "absorbed" by the massive bosons as degrees of freedom, and which couple to the fermions via Yukawa coupling to create what looks like mass terms.

In the Standard Model, the Higgs field is a complex scalar field of the group SU(2) L : $\phi ={\frac {1}{\sqrt {2}}}{\begin{pmatrix}\phi ^{+}\\\phi ^{0}\end{pmatrix}},$ where the superscripts + and 0 indicate the electric charge ( Q ) of the components. The weak hypercharge ( Y W ) of both components is 1 .

The Higgs part of the Lagrangian is ${\mathcal {L}}_{\rm {H}}=\left[\left(\partial _{\mu }-igW_{\mu }^{a}t^{a}-ig'Y_{\phi }B_{\mu }\right)\phi \right]^{2}+\mu ^{2}\phi ^{\dagger }\phi -\lambda (\phi ^{\dagger }\phi )^{2},$ where λ > 0 and μ 2 > 0 , so that the mechanism of spontaneous symmetry breaking can be used. There is a parameter here, at first hidden within the shape of the potential, that is very important. In a unitarity gauge one can set $\phi ^{+}=0$ and make $\phi ^{0}$ real. Then $\langle \phi ^{0}\rangle =v$ is the non-vanishing vacuum expectation value of the Higgs field. $v$ has units of mass, and it is the only parameter in the Standard Model that is not dimensionless. It is also much smaller than the Planck scale and about twice the Higgs mass, setting the scale for the mass of all other particles in the Standard Model. This is the only real fine-tuning to a small nonzero value in the Standard Model. Quadratic terms in W μ and B μ arise, which give masses to the W and Z bosons: ${\begin{aligned}M_{\rm {W}}&={\tfrac {1}{2}}vg\\M_{\rm {Z}}&={\tfrac {1}{2}}v{\sqrt {g^{2}+{g'}^{2}}}\end{aligned}}$

The mass of the Higgs boson itself is given by ${\textstyle M_{\rm {H}}={\sqrt {2\mu ^{2}}}\equiv {\sqrt {2\lambda v^{2}}}.}$

#### Yukawa interaction

The Yukawa interaction terms are ${\mathcal {L}}_{\text{Yukawa}}=(Y_{\text{u}})_{mn}({\bar {q}}_{\text{L}})_{m}{\tilde {\varphi }}(u_{\text{R}})_{n}+(Y_{\text{d}})_{mn}({\bar {q}}_{\text{L}})_{m}\varphi (d_{\text{R}})_{n}+(Y_{\text{e}})_{mn}({\bar {L}}_{\text{L}})_{m}\varphi (e_{\text{R}})_{n}+\mathrm {h.c.}$ where $Y_{\text{u}}$ , $Y_{\text{d}}$ , and $Y_{\text{e}}$ are 3 × 3 matrices of Yukawa couplings, with the mn term giving the coupling of the generations m and n , and h.c. means Hermitian conjugate of preceding terms. The fields $q_{\text{L}}$ and $L_{\text{L}}$ are left-handed quark and lepton doublets. Likewise, $u_{\text{R}}$ , $d_{\text{R}}$ and $e_{\text{R}}$ are right-handed up-type quark, down-type quark, and lepton singlets. Finally $\varphi$ is the Higgs doublet and ${\tilde {\varphi }}=i\tau _{2}\varphi ^{*}$

#### Neutrino masses

As previously mentioned, evidence shows neutrinos must have mass. But within the standard model, the right-handed neutrino does not exist, so even with a Yukawa coupling neutrinos remain massless. An obvious solution is to simply add a right-handed neutrino ν R , which requires the addition of a new Dirac mass term in the Yukawa sector: ${\mathcal {L}}_{\nu }^{\text{Dir}}=(Y_{\nu })_{mn}({\bar {L}}_{L})_{m}{\tilde {\varphi }}(\nu _{R})_{n}+\mathrm {h.c.}$

This field however must be a sterile neutrino , since being right-handed it experimentally belongs to an isospin singlet ( T 3 = 0 ) and also has charge Q = 0 , implying Y W = 0 (see above ) i.e. it does not even participate in the weak interaction. The experimental evidence for sterile neutrinos is currently inconclusive.

Another possibility to consider is that the neutrino satisfies the Majorana equation , which at first seems possible due to its zero electric charge. In this case a new Majorana mass term is added to the Yukawa sector: ${\mathcal {L}}_{\nu }^{\text{Maj}}=-{\frac {1}{2}}m\left({\overline {\nu }}^{C}\nu +{\overline {\nu }}\nu ^{C}\right)$ where C denotes a charge conjugated (i.e. anti-) particle, and the $\nu$ terms are consistently all left (or all right) chirality (note that a left-chirality projection of an antiparticle is a right-handed field; care must be taken here due to different notations sometimes used). Here we are essentially flipping between left-handed neutrinos and right-handed anti-neutrinos (it is furthermore possible but not necessary that neutrinos are their own antiparticle, so these particles are the same). However, for left-chirality neutrinos, this term changes weak hypercharge by 2 units – not possible with the standard Higgs interaction, requiring the Higgs field to be extended to include an extra triplet with weak hypercharge = 2 – whereas for right-chirality neutrinos, no Higgs extensions are necessary. For both left and right chirality cases, Majorana terms violate lepton number , but possibly at a level beyond the current sensitivity of experiments to detect such violations.

It is possible to include both Dirac and Majorana mass terms in the same theory, which (in contrast to the Dirac-mass-only approach) can provide a “natural” explanation for the smallness of the observed neutrino masses, by linking the right-handed neutrinos to yet-unknown physics around the GUT scale (see seesaw mechanism ).

Since in any case new fields must be postulated to explain the experimental results, neutrinos are an obvious gateway to searching physics beyond the Standard Model .

## Detailed information

This section provides more detail on some aspects, and some reference material. Explicit Lagrangian terms are also provided here .

### Field content in detail

The Standard Model has the following fields. These describe one generation of leptons and quarks, and there are three generations, so there are three copies of each fermionic field. By CPT symmetry, there is a set of fermions and antifermions with opposite parity and charges. If a left-handed fermion spans some representation its antiparticle (right-handed antifermion) spans the dual representation (note that ${\bar {\mathbf {2} }}={\mathbf {2} }$ for SU(2), because it is pseudo-real ). The column " representation " indicates under which representations of the gauge groups that each field transforms, in the order (SU(3), SU(2), U(1)) and for the U(1) group, the value of the weak hypercharge is listed. There are twice as many left-handed lepton field components as right-handed lepton field components in each generation, but an equal number of left-handed quark and right-handed quark field components.

### Fermion content

This table is based in part on data gathered by the Particle Data Group .

### Free parameters

Upon writing the most general Lagrangian with massless neutrinos, one finds that the dynamics depend on 19 parameters, whose numerical values are established by experiment. Straightforward extensions of the Standard Model with massive neutrinos need 7 more parameters (3 masses and 4 PMNS matrix parameters) for a total of 26 parameters. The neutrino parameter values are still uncertain. The 19 certain parameters are summarized here.

The choice of free parameters is somewhat arbitrary. In the table above, gauge couplings are listed as free parameters, therefore with this choice the Weinberg angle is not a free parameter – it is defined as $\tan \theta _{\rm {W}}={g_{1}}/{g_{2}}$ . Likewise, the fine-structure constant of QED is $\alpha ={\frac {1}{4\pi }}{\frac {(g_{1}g_{2})^{2}}{g_{1}^{2}+g_{2}^{2}}}$ . Instead of fermion masses, dimensionless Yukawa couplings can be chosen as free parameters. For example, the electron mass depends on the Yukawa coupling of the electron to the Higgs field, and its value is $m_{\rm {e}}=y_{\rm {e}}v/{\sqrt {2}}$ . Instead of the Higgs mass, the Higgs self-coupling strength $\lambda ={\frac {m_{\rm {H}}^{2}}{2v^{2}}}$ , which is approximately 0.129, can be chosen as a free parameter. Instead of the Higgs vacuum expectation value, the $\mu ^{2}$ parameter directly from the Higgs self-interaction term $\mu ^{2}\phi ^{\dagger }\phi -\lambda (\phi ^{\dagger }\phi )^{2}$ can be chosen. Its value is $\mu ^{2}=\lambda v^{2}={m_{\rm {H}}^{2}}/2$ , or approximately $\mu$ = 88.45 GeV .

The value of the vacuum energy (or more precisely, the renormalization scale used to calculate this energy) may also be treated as an additional free parameter. The renormalization scale may be identified with the Planck scale or fine-tuned to match the observed cosmological constant . However, both options are problematic .

### Additional symmetries of the Standard Model

From the theoretical point of view, the Standard Model exhibits four additional global symmetries, not postulated at the outset of its construction, collectively denoted accidental symmetries , which are continuous U(1) global symmetries . The transformations leaving the Lagrangian invariant are: $\psi _{\text{q}}\to e^{i\alpha /3}\psi _{\text{q}}$ $E_{\rm {L}}\to e^{i\beta }E_{\rm {L}}{\text{ and }}(e_{\rm {R}})^{\text{c}}\to e^{i\beta }(e_{\rm {R}})^{\text{c}}$ $M_{\rm {L}}\to e^{i\beta }M_{\rm {L}}{\text{ and }}(\mu _{\rm {R}})^{\text{c}}\to e^{i\beta }(\mu _{\rm {R}})^{\text{c}}$ $T_{\rm {L}}\to e^{i\beta }T_{\rm {L}}{\text{ and }}(\tau _{\rm {R}})^{\text{c}}\to e^{i\beta }(\tau _{\rm {R}})^{\text{c}}$

The first transformation rule is shorthand meaning that all quark fields for all generations must be rotated by an identical phase simultaneously. The fields M L , T L and $(\mu _{\rm {R}})^{\text{c}},(\tau _{\rm {R}})^{\text{c}}$ are the 2nd (muon) and 3rd (tau) generation analogs of E L and $(e_{\rm {R}})^{\text{c}}$ fields.

By Noether's theorem , each symmetry above has an associated conservation law : the conservation of baryon number , electron number , muon number , and tau number . Each quark is assigned a baryon number of ⁠ 1 / 3 ⁠ , while each antiquark is assigned a baryon number of − ⁠ 1 / 3 ⁠ . Conservation of baryon number implies that the number of quarks minus the number of antiquarks is a constant. Within experimental limits, no violation of this conservation law has been found.

Similarly, each electron and its associated neutrino is assigned an electron number of +1, while the antielectron and the associated antineutrino carry a −1 electron number. Similarly, the muons and their neutrinos are assigned a muon number of +1 and the tau leptons are assigned a tau lepton number of +1. The Standard Model predicts that each of these three numbers should be conserved separately in a manner similar to the way baryon number is conserved. These numbers are collectively known as lepton family numbers (LF). (This result depends on the assumption made in Standard Model that neutrinos are massless. Experimentally, neutrino oscillations imply that individual electron, muon and tau numbers are not conserved.)

In addition to the accidental (but exact) symmetries described above, the Standard Model exhibits several approximate symmetries . These are the "SU(2) custodial symmetry " and the "SU(2) or SU(3) quark flavor symmetry".

### U(1) symmetry

For the leptons , the gauge group can be written SU(2) l × U(1) L × U(1) R . The two U(1) factors can be combined into U(1) Y × U(1) l , where l is the lepton number . Gauging of the lepton number is ruled out by experiment, leaving only the possible gauge group SU(2) L × U(1) Y . A similar argument in the quark sector also gives the same result for the electroweak theory.

### Charged and neutral current couplings and Fermi theory

The charged currents $j^{\mp }=j^{1}\pm ij^{2}$ are $j_{\mu }^{-}={\overline {U}}_{i\mathrm {L} }\gamma _{\mu }D_{i\mathrm {L} }+{\overline {\nu }}_{i\mathrm {L} }\gamma _{\mu }l_{i\mathrm {L} }.$ These charged currents are precisely those that entered the Fermi theory of beta decay . The action contains the charge current piece ${\mathcal {L}}_{\rm {CC}}={\frac {g}{\sqrt {2}}}(j_{\mu }^{+}W^{-\mu }+j_{\mu }^{-}W^{+\mu }).$ For energy much less than the mass of the W-boson, the effective theory becomes the current–current contact interaction of the Fermi theory , $2{\sqrt {2}}G_{\rm {F}}~~J_{\mu }^{+}J^{\mu ~~-}$ .

However, gauge invariance now requires that the component $W^{3}$ of the gauge field also be coupled to a current that lies in the triplet of SU(2). However, this mixes with the U(1) , and another current in that sector is needed. These currents must be uncharged in order to conserve charge. So neutral currents are also required, $j_{\mu }^{3}={\frac {1}{2}}\left({\overline {U}}_{i\mathrm {L} }\gamma _{\mu }U_{i\mathrm {L} }-{\overline {D}}_{i\mathrm {L} }\gamma _{\mu }D_{i\mathrm {L} }+{\overline {\nu }}_{i\mathrm {L} }\gamma _{\mu }\nu _{i\mathrm {L} }-{\overline {l}}_{i\mathrm {L} }\gamma _{\mu }l_{i\mathrm {L} }\right)$ $j_{\mu }^{\rm {em}}={\frac {2}{3}}{\overline {U}}_{i}\gamma _{\mu }U_{i}-{\frac {1}{3}}{\overline {D}}_{i}\gamma _{\mu }D_{i}-{\overline {l}}_{i}\gamma _{\mu }l_{i}.$ The neutral current piece in the Lagrangian is then ${\mathcal {L}}_{\rm {NC}}=ej_{\mu }^{\rm {em}}A^{\mu }+{\frac {g}{\cos \theta _{\rm {W}}}}(J_{\mu }^{3}-\sin ^{2}\theta _{\rm {W}}J_{\mu }^{\rm {em}})Z^{\mu }.$

## Physics beyond the Standard Model

Physics beyond the Standard Model (BSM) is the theoretical developments needed to explain the deficiencies of the Standard Model , such as the inability to explain the fundamental parameters of the Standard Model, the strong CP problem , neutrino oscillations , matter–antimatter asymmetry , and the nature of dark matter and dark energy . Another problem lies within the mathematical framework of the Standard Model itself: the Standard Model is inconsistent with that of general relativity , and one or both theories break down under certain conditions, such as spacetime singularities like the Big Bang and black hole event horizons .

Theories that lie beyond the Standard Model include various extensions of the standard model through supersymmetry , such as the Minimal Supersymmetric Standard Model (MSSM) and Next-to-Minimal Supersymmetric Standard Model (NMSSM), and entirely novel explanations, such as string theory , M-theory , and extra dimensions . As these theories tend to reproduce the entirety of current phenomena, the question of which theory is the right one, or at least the "best step" towards a Theory of Everything , can only be settled via experiments, and is one of the most active areas of research in both theoretical and experimental physics .
