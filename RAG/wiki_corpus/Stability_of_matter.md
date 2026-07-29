# Stability of matter

> **Query Topic**: Earnshaw's theorem state (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 361, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Stability_of_matter

---

In physics , the stability of matter refers to the ability of a large number of charged particles , such as electrons and protons , to form macroscopic objects without collapsing or blowing apart due to electromagnetic interactions. Classical physics predicts that such systems should be inherently unstable due to attractive and repulsive electrostatic forces between charges, and thus the stability of matter was a theoretical problem that required a quantum mechanical explanation.

The first solution to this problem was provided by Freeman Dyson and Andrew Lenard in 1967–1968, but a shorter and more conceptual proof was found later by Elliott Lieb and Walter Thirring in 1975 using the Lieb–Thirring inequality . The stability of matter is partly due to the uncertainty principle and the Pauli exclusion principle .

## Description of the problem

In statistical mechanics , the existence of macroscopic objects is usually explained in terms of the behavior of the energy or the free energy with respect to the total number $N$ of particles. More precisely, the ground-state energy should be a linear function of $N$ for large values of $N$ . In fact, if the ground-state energy behaves proportional to $N^{a}$ for some $a\neq 1$ , then pouring two glasses of water would provide an energy proportional to $(2N)^{a}-2N^{a}=(2^{a}-2)N^{a}$ , which is enormous for large $N$ . A system is called stable of the second kind or thermodynamically stable when the free energy is bounded from below by a linear function of $N$ . Upper bounds are usually easy to show in applications, and this is why scientists have worked more on proving lower bounds.

Neglecting other forces, it is reasonable to assume that ordinary matter is composed of negative and positive non-relativistic charges ( electrons and ions ), interacting solely via the Coulomb's interaction . A finite number of such particles always collapses in classical mechanics , due to the infinite depth of the electron-nucleus attraction, but it can exist in quantum mechanics thanks to Heisenberg's uncertainty principle . Proving that such a system is thermodynamically stable is called the stability of matter problem and it is very difficult [ clarification needed ] due to the long range of the Coulomb potential. Stability should be a consequence of screening effects , but those are hard to quantify.

Let us denote by

$H_{N,K}=-\sum _{i=1}^{N}{\frac {\Delta _{x_{i}}}{2}}-\sum _{k=1}^{K}{\frac {\Delta _{R_{k}}}{2M_{k}}}-\sum _{i=1}^{N}\sum _{k=1}^{K}{\frac {z_{k}}{|x_{i}-R_{k}|}}+\sum _{1\leq i<j\leq N}{\frac {1}{|x_{i}-x_{j}|}}+\sum _{1\leq k<m\leq K}{\frac {z_{k}z_{m}}{|R_{k}-R_{m}|}}$

the quantum Hamiltonian of $N$ electrons and $K$ nuclei of charges $z_{1},...,z_{K}$ and masses $M_{1},...,M_{K}$ in atomic units . Here $\Delta =\nabla ^{2}=\sum _{j=1}^{3}\partial _{jj}$ denotes the Laplacian , which is the quantum kinetic energy operator. At zero temperature, the question is whether the ground state energy (the minimum of the spectrum of $H_{N,K}$ ) is bounded from below by a constant times the total number of particles:

The constant $C$ can depend on the largest number of spin states for each particle as well as the largest value of the charges $z_{k}$ . It should ideally not depend on the masses $M_{1},...,M_{K}$ so as to be able to consider the infinite mass limit, that is, classical nuclei.

## History

### 19th century physics

At the end of the 19th century it was understood that electromagnetic forces held matter together. However two problems co-existed. Earnshaw's theorem from 1842, proved that no charged body can be in a stable equilibrium under the influence of electrostatic forces alone. The second problem was that James Clerk Maxwell had shown that accelerated charge produces electromagnetic radiation , which in turn reduces its motion. In 1900, Joseph Larmor suggested the possibility of an electromagnetic system with electrons in orbits inside matter. He showed that if such system existed, it could be scaled down by scaling distances and vibrations times, however this suggested a modification to Coulomb's law at the level of molecules. Classical physics was thus unable to explain the stability of matter and could only be explained with quantum mechanics which was developed at the beginning of the 20th century.

### Dyson–Lenard solution

Freeman Dyson showed in 1967 that if all the particles are bosons , then the inequality ( 1 ) cannot be true and the system is thermodynamically unstable. It was in fact later proved that in this case the energy goes like $N^{7/5}$ instead of being linear in $N$ . It is therefore important that either the positive or negative charges are fermions . In other words, stability of matter is a consequence of the Pauli exclusion principle . In real life electrons are indeed fermions, but finding the right way to use Pauli's principle and prove stability turned out to be remarkably difficult. Michael Fisher and David Ruelle formalized the conjecture in 1966 According to Dyson, Fisher and Ruelle offered a bottle of Champagne to anybody who could prove it. Dyson and Lenard found the proof of ( 1 ) a year later and therefore got the bottle.

### Lieb–Thirring inequality

As was mentioned before, stability is a necessary condition for the existence of macroscopic objects, but it does not immediately imply the existence of thermodynamic functions. One should really show that the energy really behaves linearly in the number of particles. Based on the Dyson–Lenard result, this was solved in an ingenious way by Elliott Lieb and Joel Lebowitz in 1972.

According to Dyson himself, the Dyson–Lenard proof is "extraordinarily complicated and difficult" and relies on deep and tedious analytical bounds. The obtained constant $C$ in ( 1 ) was also very large. In 1975, Elliott Lieb and Walter Thirring found a simpler and more conceptual proof, based on a spectral inequality, now called the Lieb–Thirring inequality . They got a constant $C$ which was by several orders of magnitude smaller than the Dyson–Lenard constant and had a realistic value.
They arrived at the final inequality

where $Z=\max(z_{k})$ is the largest nuclear charge and $q$ is the number of electronic spin states which is 2. Since $N^{1/3}K^{2/3}\leq N+K$ , this yields the desired linear lower bound ( 1 ). 
The Lieb–Thirring idea was to bound the quantum energy from below in terms of the Thomas–Fermi energy. The latter is always stable due to a theorem of Edward Teller which states that atoms can never bind in Thomas–Fermi model . The Lieb–Thirring inequality was used to bound the quantum kinetic energy of the electrons in terms of the Thomas–Fermi kinetic energy $\int _{\mathbb {R} ^{3}}\rho (x)^{\frac {5}{3}}d^{3}x$ . Teller's no-binding theorem was in fact also used to bound from below the total Coulomb interaction in terms of the simpler Hartree energy appearing in Thomas–Fermi theory. Speaking about the Lieb–Thirring proof, Dyson wrote later

Lenard and I found a proof of the stability of matter in 1967. Our proof was so complicated and so unilluminating that it stimulated Lieb and Thirring to find the first decent proof. (...) Why was our proof so bad and why was theirs so good? The reason is simple. Lenard and I began with mathematical tricks and hacked our way through a forest of inequalities without any physical understanding. Lieb and Thirring began with physical understanding and went on to find the appropriate mathematical language to make their understanding rigorous. Our proof was a dead end. Theirs was a gateway to the new world of ideas.

### Further work

The Lieb–Thirring approach has generated many subsequent works and extensions. (Pseudo-)Relativistic systems, magnetic fields, quantized fields and two-dimensional fractional statistics ( anyons ) have for instance been studied since the Lieb–Thirring paper. 
The form of the bound ( 1 ) has also been improved over the years. For example, one can obtain a constant independent of the number $K$ of nuclei.
