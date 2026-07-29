# Self-organized criticality

> **Query Topic**: dynamic scaling in self-similar structures (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 324, Frequency: 2)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Self-organized_criticality

---

Self-organized criticality ( SOC ) is a property of dynamical systems that have a critical point as an attractor . Their macroscopic behavior thus displays the spatial or temporal scale-invariance characteristic of the critical point of a phase transition , but without the need to tune control parameters to a precise value, because the system, effectively, tunes itself as it evolves towards criticality.

The concept was put forward by Per Bak , Chao Tang and Kurt Wiesenfeld ("BTW") in a paper following an earlier paper by Jonathan I. Katz published in 1987 in Physical Review Letters , and is considered to be one of the mechanisms by which complexity arises in nature. Its concepts have been applied across fields as diverse as geophysics , physical cosmology , evolutionary biology and ecology , bio-inspired computing and optimization (mathematics) , economics , quantum gravity , sociology , solar physics , plasma physics , neurobiology and others.

SOC is typically observed in slowly driven non-equilibrium systems with many degrees of freedom and strongly nonlinear dynamics. Many individual examples have been identified since BTW's original paper, but to date there is no known set of general characteristics that guarantee a system will display SOC.

## Overview

Self-organized criticality is one of a number of important discoveries made in statistical physics and related fields over the latter half of the 20th century, discoveries which relate particularly to the study of complexity in nature. For example, the study of cellular automata , from the early discoveries of Stanislaw Ulam and John von Neumann through to John Conway 's Game of Life and the extensive work of Stephen Wolfram , made it clear that complexity could be generated as an emergent feature of extended systems with simple local interactions. Over a similar period of time, Benoît Mandelbrot 's large body of work on fractals showed that much complexity in nature could be described by certain ubiquitous mathematical laws, while the extensive study of phase transitions carried out in the 1960s and 1970s showed how scale invariant phenomena such as fractals and power laws emerged at the critical point between phases.

The term self-organized criticality was first introduced in Bak , Tang and Wiesenfeld 's 1987 paper, which clearly linked together those factors: a simple cellular automaton was shown to produce several characteristic features observed in natural complexity ( fractal geometry, pink (1/f) noise and power laws ) in a way that could be linked to critical-point phenomena . Crucially, however, the paper emphasized that the complexity observed emerged in a robust manner that did not depend on finely tuned details of the system: variable parameters in the model could be changed widely without affecting the emergence of critical behavior: hence, self-organized criticality. Thus, the key result of BTW's paper was its discovery of a mechanism by which the emergence of complexity from simple local interactions could be spontaneous — and therefore plausible as a source of natural complexity — rather than something that was only possible in artificial situations in which control parameters are tuned to precise critical values. An alternative view is that SOC appears when the criticality is linked to a value of zero of the control parameters.

Despite the considerable interest and research output generated from the SOC hypothesis, there remains no general agreement with regards to its mechanisms in abstract mathematical form. Bak, Tang and Wiesenfeld based their hypothesis on the behavior of their sandpile model.

## Mathematical models

In chronological order of development:

- Invasion percolation

- Stick-slip model of fault failure

- Bak–Tang–Wiesenfeld sandpile

- Forest-fire model

- Manna model

- Olami–Feder–Christensen model

- Bak–Sneppen model

- Neural network

- The rice pile or Oslo model

Early theoretical work included the development of a variety of alternative SOC-generating dynamics distinct from the BTW model, attempts to prove model properties analytically (including calculating the critical exponents ), and examination of the conditions necessary for SOC to emerge. One of the important issues for the latter investigation was whether conservation of energy was required in the local dynamical exchanges of models: the answer in general is no, but with (minor) reservations, as some exchange dynamics (such as those of BTW) do require local conservation at least on average [ clarification needed ] .

It has been argued that the energy released in the BTW "sandpile" model should actually generate 1/f 2 noise rather than 1/f noise. This claim was based on untested scaling assumptions, and a more rigorous analysis showed that sandpile models 
generally produce 1/f a spectra, with a<2. However, the dynamics of the accumulated stress does exhibit the 1/f noise in the BTW model. Other simulation models were proposed later that could also produce true 1/f noise.

In addition to the nonconservative theoretical model mentioned above [ clarification needed ] , other theoretical models for SOC have been based upon information theory , mean field theory , the convergence of random variables , and cluster formation. A continuous model of self-organised criticality is proposed by using tropical geometry .

Key theoretical issues yet to be resolved include the calculation of the possible universality classes of SOC behavior and the question of whether it is possible to derive a general rule for determining if an arbitrary algorithm displays SOC.

## In nature

SOC has become established as a strong candidate for explaining a number of natural phenomena, including:

- The magnitude of earthquakes ( Gutenberg–Richter law ) and frequency of aftershocks ( Omori law )

- Fluctuations in economic systems such as financial markets (references to SOC are common in econophysics )

- The evolution of proteins

- Forest fires [ clarification needed ]

- Neuronal avalanches in the cortex

- Acoustic emission from fracturing materials

Despite the numerous applications of SOC to understanding natural phenomena, the universality of SOC theory has been questioned. For example, experiments with real piles of rice revealed their dynamics to be far more sensitive to parameters than originally predicted. Furthermore, it has been argued that 1/f scaling in EEG recordings are inconsistent with critical states, and whether SOC is a fundamental property of neural systems remains an open and controversial topic.

## Applications

### Optimization

It has been found that the avalanches from an SOC process make effective patterns in a random search for optimal solutions on graphs. An example of such an optimization problem is graph coloring . The SOC process apparently helps the optimization from getting stuck in a local optimum without the use of any annealing scheme, as suggested by previous work on extremal optimization .

### Synthetic biology

Self-organized criticality has also been explored in synthetic biology . Experimental work has shown that gene regulatory networks engineered to operate near critical states can generate heterogeneous gene expression within genetically identical cell populations. This behavior may reduce the need for precise tuning of protein production and has been proposed as a strategy to engineer functional diversity while maintaining a single genetic construct.
