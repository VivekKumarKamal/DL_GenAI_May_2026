# Rigged Hilbert space

> **Query Topic**: Hilbert space in quantum mechanics (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 65, Frequency: 11)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Rigged_Hilbert_space

---

In mathematics and physics , a rigged Hilbert space ( Gelfand triple , nested Hilbert space , equipped Hilbert space ) is a construction which can enlarge a Hilbert space to a bigger space containing additional objects which are not in the Hilbert space but which one would like to think of alongside the Hilbert space. For example, in the quantum mechanical description of a non-relativistic particle using the Hilbert space of square-integrable functions on the real line, eigenstates of the position and momentum operators are not in the Hilbert space, but are in a suitably defined rigged Hilbert space. Informally, the term "rigged" means that the Hilbert space has been equipped to do more than it otherwise could, in analogy with rigging a boat.

This construction is designed to link the distribution and square-integrable aspects of functional analysis . Such spaces were introduced to study spectral theory . They bring together the ' bound state ' ( eigenvector ) and ' continuous spectrum ', in one place.

Using this notion, a version of the spectral theorem for unbounded operators on Hilbert space can be formulated. "Rigged Hilbert spaces are well known as the structure which provides a proper mathematical meaning to the Dirac formulation of quantum mechanics ."

## Motivation

A function such as $x\mapsto e^{ix},$ is an eigenfunction of the differential operator $-i{\frac {d}{dx}}$ on the real line R , but isn't square-integrable for the usual ( Lebesgue ) measure on R . To properly consider this function as an eigenfunction requires some way of stepping outside the strict confines of the Hilbert space theory. This was supplied by the apparatus of distributions , and a generalized eigenfunction theory was developed in the years after 1950.

## Definition

A rigged Hilbert space is a pair ( H , Φ) with H a Hilbert space, Φ a dense subspace, such that Φ is given a topological vector space structure for which the inclusion map $i:\Phi \to H,$ is continuous. Identifying H with its dual space H * , the adjoint to i is the map $i^{*}:H=H^{*}\to \Phi ^{*}.$

The duality pairing between Φ and Φ * is then compatible with the inner product on H , in the sense that: $\langle u,v\rangle _{\Phi \times \Phi ^{*}}=(u,v)_{H}$ whenever $u\in \Phi \subset H$ and $v\in H=H^{*}\subset \Phi ^{*}$ . In the case of complex Hilbert spaces, we use a Hermitian inner product; it will be complex linear in u (math convention) or v (physics convention), and conjugate-linear (complex anti-linear) in the other variable.

The triple $(\Phi ,\,\,H,\,\,\Phi ^{*})$ is often named the Gelfand triple (after Israel Gelfand ). $H$ is referred to as a pivot space.

Note that even though Φ is isomorphic to Φ * (via Riesz representation ) if it happens that Φ is a Hilbert space in its own right, this isomorphism is not the same as the composition of the inclusion i with its adjoint i * $i^{*}i:\Phi \subset H=H^{*}\to \Phi ^{*}.$

### Functional analysis approach

The concept of rigged Hilbert space places this idea in an abstract functional-analytic framework. Formally, a rigged Hilbert space consists of a Hilbert space H , together with a subspace Φ which carries a finer topology , that is one for which the natural inclusion $\Phi \subseteq H$ is continuous. It is no loss to assume that Φ is dense in H for the Hilbert norm. We consider the inclusion of dual spaces H * in Φ * . The latter, dual to Φ in its 'test function' topology, is realised as a space of distributions or generalised functions of some sort, and the linear functionals on the subspace Φ of type $\phi \mapsto \langle v,\phi \rangle$ for v in H are faithfully represented as distributions (because we assume Φ dense).

Now by applying the Riesz representation theorem we can identify H * with H . Therefore, the definition of rigged Hilbert space is in terms of a sandwich: $\Phi \subseteq H\subseteq \Phi ^{*}.$

The most significant examples are those for which Φ is a nuclear space ; this comment is an abstract expression of the idea that Φ consists of test functions and Φ* of the corresponding distributions .

An example of a nuclear countably Hilbert space $\Phi$ and its dual $\Phi ^{*}$ is the Schwartz space ${\mathcal {S}}(\mathbb {R} )$ and the space of tempered distributions ${\mathcal {S}}'(\mathbb {R} )$ , respectively, rigging the Hilbert space of square-integrable functions . As such, the rigged Hilbert space is given by ${\mathcal {S}}(\mathbb {R} )\subset L^{2}(\mathbb {R} )\subset {\mathcal {S}}'(\mathbb {R} ).$ Another example is given by Sobolev spaces : Here (in the simplest case of Sobolev spaces on $\mathbb {R} ^{n}$ ) $H=L^{2}(\mathbb {R} ^{n}),\ \Phi =H^{s}(\mathbb {R} ^{n}),\ \Phi ^{*}=H^{-s}(\mathbb {R} ^{n}),$ where $s>0$ .
