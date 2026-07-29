# Dynamic scaling

> **Query Topic**: dynamic scaling in self-similar systems (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 421, Frequency: 2)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Dynamic_scaling

---

Dynamic scaling (sometimes known as Family–Vicsek scaling ) is a litmus test that shows whether an evolving system exhibits self-similarity . In general a function is said to exhibit dynamic scaling if it satisfies:

$f(x,t)\sim t^{\theta }\varphi \left({\frac {x}{t^{z}}}\right).$

Here the exponent $\theta$ is fixed by the dimensional requirement $[f]=[t^{\theta }]$ . The numerical value of $f/t^{\theta }$ should remain invariant despite the unit of measurement of $t$ is changed by some factor since $\varphi$ is a dimensionless quantity.

Many of these systems evolve in a self-similar fashion in the sense that data obtained from the snapshot at any fixed time is similar to the respective data taken from the snapshot of any earlier or later time. That is, the system is similar to itself at different times. The litmus test of such self-similarity is provided by the dynamic scaling.

## History

The term "dynamic scaling" as one of the essential concepts to describe the dynamics of critical phenomena seems to originate in the seminal paper of Pierre Hohenberg and Bertrand Halperin (1977), namely they suggested "[...] that the wave vector- and frequency dependent susceptibility of a ferromagnet near its Curie point may be expressed as a function independent of $|T-T_{C}|$ provided that the length and frequency scales, as well as the magnetization and magnetic field, are rescaled by appropriate powers of $|T-T_{C}|$ .

Later Tamás Vicsek and Fereydoon Family proposed the idea of dynamic scaling in the context of diffusion-limited aggregation ( DLA ) of clusters in two dimensions. The form of their proposal for dynamic scaling was:

$f(x,t)\sim t^{-w}x^{-\tau }\varphi \left({\frac {x}{t^{z}}}\right),$

where the exponents satisfy the following relation:

$w=(2-\tau )z.$

## Test

In such systems we can define a certain time-dependent stochastic variable $x$ . We are interested in computing the probability distribution of $x$ at various instants of time i.e. $f(x,t)$ . The numerical value of $f$ and the typical or mean value of $x$ generally changes over time. The question is: what happens to the corresponding dimensionless variables? If the numerical values of the dimensional quantities change, but corresponding dimensionless quantities remain invariant then we can argue that snapshots of the system at different times are similar. When this happens we say that the system is self-similar.

One way of verifying dynamic scaling is to plot dimensionless variables $f/t^{\theta }$ as a function of $x/t^{z}$ of the data extracted at various different time. Then if all the plots of $f$ vs $x$ obtained at different times collapse onto a single universal curve then it is said that the systems at different time are similar and it obeys dynamic scaling. The idea of data collapse is deeply rooted to the Buckingham Pi theorem . Essentially such systems can be termed as temporal self-similarity since the same system is similar at different times.

## Examples

Many phenomena investigated by physicists are not static but evolve probabilistically with time (i.e. Stochastic process ). The universe itself is perhaps one of the best examples. It has been expanding ever since the Big Bang . Similarly, growth of networks like the Internet are also ever growing systems. Another example is polymer degradation where degradation does not occur in a blink of an eye but rather over quite a long time. Spread of biological and computer viruses too does not happen over night.

Many other seemingly disparate systems which are found to exhibit dynamic scaling. For example:

- kinetics of aggregation described by Smoluchowski coagulation equation ,

- the growth model within the Kardar–Parisi–Zhang (KPZ) universality class; one find that the width of the surface $W(L,t)$ exhibits dynamic scaling.

- the marginal probabilities of fractional Poisson processes exhibits dynamic scaling.
