# Taylor's law

> **Query Topic**: mathematical function is commonly used to characterize linear time-invariant mechanisms (Rank #2 Search Result)
> **Source Queue**: train (Row ID: 421, Frequency: 2)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Taylor's_law

---

Taylor's power law is an empirical law in ecology that relates the variance of the number of individuals of a species per unit area of habitat to the corresponding mean by a power law relationship. It is named after the ecologist who first proposed it in 1961, Lionel Roy Taylor (1924–2007). Taylor's original name for this relationship was the law of the mean. The name Taylor's law was coined by Southwood in 1966.

## Definition

This law was originally defined for ecological systems, specifically to assess the spatial clustering of organisms. For a population count $Y$ with mean $\mu$ and variance $\operatorname {var} (Y)$ , Taylor's law is written

$\operatorname {var} (Y)=a\mu ^{b},$

where a and b are both positive constants. Taylor proposed this relationship in 1961, suggesting that the exponent b be considered a species specific index of aggregation. This power law has subsequently been confirmed for many hundreds of species.

Taylor's law has also been applied to assess the time dependent changes of population distributions. Related variance to mean power laws have also been demonstrated in several non-ecological systems:

- cancer metastasis

- the numbers of houses built over the Tonami plain in Japan.

- measles epidemiology

- HIV epidemiology,

- the geographic clustering of childhood leukemia

- blood flow heterogeneity

- the genomic distributions of single-nucleotide polymorphisms (SNPs)

- gene structures

- in number theory with sequential values of the Mertens function and also with the distribution of prime numbers

- from the eigenvalue deviations of Gaussian orthogonal and unitary ensembles of random matrix theory

## History

The first use of a double log-log plot was by Reynolds in 1879 on thermal aerodynamics. Pareto used a similar plot to study the proportion of a population and their income.

The term variance was coined by Fisher in 1918.

### Biology

Pearson in 1921 proposed the equation (also studied by Neyman )

$s^{2}=am+bm^{2}$

Smith in 1938 while studying crop yields proposed a relationship similar to Taylor's. This relationship was

$\log V_{x}=\log V_{1}+b\log x\,$

where V x is the variance of yield for plots of x units, V 1 is the variance of yield per unit area and x is the size of plots. The slope ( b ) is the index of heterogeneity. The value of b in this relationship lies between 0 and 1. Where the yield are highly correlated b tends to 0; when they are uncorrelated b tends to 1.

Bliss in 1941, Fracker and Brischle in 1941 and Hayman & Lowe in 1961 also described what is now known as Taylor's law, but in the context of data from single species.

Taylor's 1961 paper used data from 24 papers, published between 1936 and 1960, that considered a variety of biological settings: virus lesions, macro-zooplankton , worms and symphylids in soil , insects in soil, on plants and in the air, mites on leaves , ticks on sheep and fish in the sea .; the b value lay between 1 and 3. Taylor proposed the power law as a general feature of the spatial distribution of these species. He also proposed a mechanistic hypothesis to explain this law.

Initial attempts to explain the spatial distribution of animals had been based on approaches like Bartlett's stochastic population models and the negative binomial distribution that could result from birth–death processes . Taylor's explanation was based the assumption of a balanced migratory and congregatory behavior of animals. His hypothesis was initially qualitative, but as it evolved it became semi-quantitative and was supported by simulations.

Many alternative hypotheses for the power law have been advanced. Hanski proposed a random walk model, modulated by the presumed multiplicative effect of reproduction. Hanski's model predicted that the power law exponent would be constrained to range closely about the value of 2, which seemed inconsistent with many reported values.

Anderson et al formulated a simple stochastic birth, death, immigration and emigration model that yielded a quadratic variance function. As a response to this model Taylor argued that such a Markov process would predict that the power law exponent would vary considerably between replicate observations, and that such variability had not been observed.

Adrienne W. Kemp reviewed a number of discrete stochastic models based on the negative binomial, Neyman type A , and Polya–Aeppli distributions that with suitable adjustment of parameters could produce a variance to mean power law. Kemp, however, did not explain the parameterizations of her models in mechanistic terms. Other relatively abstract models for Taylor's law followed.

Statistical concerns were raised regarding Taylor's law, based on the difficulty with real data in distinguishing between Taylor's law and other variance to mean functions, as well the inaccuracy of standard regression methods.

Taylor's law has been applied to time series data, and Perry showed, using simulations, that chaos theory could yield Taylor's law.

Taylor's law has been applied to the spatial distribution of plants and bacterial populations As with the observations of Tobacco necrosis virus mentioned earlier, these observations were not consistent with Taylor's animal behavioral model.

A variance to mean power function had been applied to non-ecological systems, under the rubric of Taylor's law. A more general explanation for the range of manifestations of the power law a hypothesis has been proposed based on the Tweedie distributions , a family of probabilistic models that express an inherent power function relationship between the variance and the mean.

Several alternative hypotheses for the power law have been proposed. Hanski proposed a random walk model, modulated by the presumed multiplicative effect of reproduction. Hanski's model predicted that the power law exponent would be constrained to range closely about the value of 2, which seemed inconsistent with many reported values. Anderson et al formulated a simple stochastic birth, death, immigration and emigration model that yielded a quadratic variance function. The Lewontin Cohen growth model . is another proposed explanation. The possibility that observations of a power law might reflect more mathematical artifact than a mechanistic process was raised. Variation in the exponents of Taylor's Law applied to ecological populations cannot be explained or predicted based solely on statistical grounds however. Research has shown that variation within the Taylor's law exponents for the North Sea fish community varies with the external environment, suggesting ecological processes at least partially determine the form of Taylor's law.

### Physics

In the physics literature Taylor's law has been referred to as fluctuation scaling . Eisler et al , in a further attempt to find a general explanation for fluctuation scaling, proposed a process they called impact inhomogeneity in which frequent events are associated with larger impacts. In appendix B of the Eisler article, however, the authors noted that the equations for impact inhomogeneity yielded the same mathematical relationships as found with the Tweedie distributions.

Another group of physicists, Fronczak and Fronczak, derived Taylor's power law for fluctuation scaling from principles of equilibrium and non-equilibrium statistical physics . Their derivation was based on assumptions of physical quantities like free energy and an external field that caused the clustering of biological organisms. Direct experimental demonstration of these postulated physical quantities in relationship to animal or plant aggregation has yet to be achieved, though. Shortly thereafter, an analysis of Fronczak and Fronczak's model was presented that showed their equations directly lead to the Tweedie distributions, a finding that suggested that Fronczak and Fronczak had possibly provided a maximum entropy derivation of these distributions.

### Mathematics

Taylor's law has been shown to hold for prime numbers not exceeding a given real number. This result has been shown to hold for the first 11 million primes. If the Hardy–Littlewood twin primes conjecture is true then this law also holds for twin primes.

## The Tweedie hypothesis

About the time that Taylor was substantiating his ecological observations, MCK Tweedie , a British statistician and medical physicist, was investigating a family of probabilistic models that are now known as the Tweedie distributions . As mentioned above, these distributions are all characterized by a variance to mean power law mathematically identical to Taylor's law.

The Tweedie distribution most applicable to ecological observations is the compound Poisson-gamma distribution , which represents the sum of N independent and identically distributed random variables with a gamma distribution where N is a random variable distributed in accordance with a Poisson distribution. In the additive form its cumulant generating function (CGF) is:

$K_{b}^{*}(s;\theta ,\lambda )=\lambda \kappa _{b}(\theta )\left[\left(1+{s \over \theta }\right)^{\alpha }-1\right],$

where κ b ( θ ) is the cumulant function,

$\kappa _{b}(\theta )={\frac {\alpha -1}{\alpha }}\left({\frac {\theta }{\alpha -1}}\right)^{\alpha },$

the Tweedie exponent

$\alpha ={\frac {b-2}{b-1}},$

s is the generating function variable, and θ and λ are the canonical and index parameters, respectively.

These last two parameters are analogous to the scale and shape parameters used in probability theory . The cumulants of this distribution can be determined by successive differentiations of the CGF and then substituting s=0 into the resultant equations. The first and second cumulants are the mean and variance, respectively, and thus the compound Poisson-gamma CGF yields Taylor's law with the proportionality constant

$a=\lambda ^{1/(\alpha -1)}.$

The compound Poisson-gamma cumulative distribution function has been verified for limited ecological data through the comparison of the theoretical distribution function with the empirical distribution function . A number of other systems, demonstrating variance to mean power laws related to Taylor's law, have been similarly tested for the compound Poisson-gamma distribution.

The main justification for the Tweedie hypothesis rests with the mathematical convergence [ disambiguation needed ] properties of the Tweedie distributions. The Tweedie convergence theorem requires the Tweedie distributions to act as foci of convergence for a wide range of statistical processes. As a consequence of this convergence theorem, processes based on the sum of multiple independent small jumps will tend to express Taylor's law and obey a Tweedie distribution. A limit theorem for independent and identically distributed variables, as with the Tweedie convergence theorem, might then be considered as being fundamental relative to the ad hoc population models, or models proposed on the basis of simulation or approximation.

This hypothesis remains controversial; more conventional population dynamic approaches seem preferred amongst ecologists, despite the fact that the Tweedie compound Poisson distribution can be directly applied to population dynamic mechanisms.

One difficulty with the Tweedie hypothesis is that the value of b does not range between 0 and 1. Values of b < 1 are rare but have been reported.

## Mathematical formulation

In symbols

$s_{i}^{2}=am_{i}^{b},$

where s i 2 is the variance of the density of the i th sample, m i is the mean density of the i th sample and a and b are constants.

In logarithmic form

$\log s_{i}^{2}=\log a+b\log m_{i}$

### Scale invariance

The exponent in Taylor's law is scale invariant: If the unit of measurement is changed by a constant factor $c$ , the exponent ( $b$ ) remains unchanged.

To see this let y = cx . Then

$\mu _{1}=\operatorname {E} (x)$

$\mu _{2}=\operatorname {E} (y)=\operatorname {E} (cx)=c\operatorname {E} (x)=c\mu _{1}$

$\sigma _{1}^{2}=\operatorname {E} ((x-\mu _{1})^{2})$

$\sigma _{2}^{2}=\operatorname {E} ((y-\mu _{2})^{2})=\operatorname {E} ((cx-c\mu _{1})^{2})=c^{2}\operatorname {E} ((x-\mu _{1})^{2})=c^{2}\sigma _{1}^{2}$

Taylor's law expressed in the original variable ( x ) is

$\sigma _{1}^{2}=a\mu _{1}^{b}$

and in the rescaled variable ( y ) it is

$\sigma _{2}^{2}=c^{2}\sigma _{1}^{2}=c^{2}a\mu _{1}^{b}=c^{2-b}a(c\mu _{1})^{b}=c^{2-b}a\mu _{2}^{b}$

Thus, $\sigma _{2}^{2}$ is still proportional to $\mu _{2}^{b}$ (even though the proportionality constant has changed).

It has been shown that Taylor's law is the only relationship between the mean and variance that is scale invariant.

### Extensions and refinements

A refinement in the estimation of the slope b has been proposed by Rayner.

$b={\frac {f-\varphi +{\sqrt {(f-\varphi )^{2}-4r^{2}f\varphi }}}{2r{\sqrt {f}}}}$

where $r$ is the Pearson moment correlation coefficient between $\log(s^{2})$ and $\log m$ , $f$ is the ratio of sample variances in $\log(s^{2})$ and $\log m$ and $\varphi$ is the ratio of the errors in $\log(s^{2})$ and $\log m$ .

Ordinary least squares regression assumes that φ = ∞. This tends to underestimate the value of b because the estimates of both $\log(s^{2})$ and $\log m$ are subject to error.

An extension of Taylor's law has been proposed by Ferris et al when multiple samples are taken

$s^{2}=cn^{d}m^{b},$

where s 2 and m are the variance and mean respectively, b , c and d are constants and n is the number of samples taken. To date, this proposed extension has not been verified to be as applicable as the original version of Taylor's law.

### Small samples

An extension to this law for small samples has been proposed by Hanski. For small samples the Poisson variation ( P ) - the variation that can be ascribed to sampling variation - may be significant. Let S be the total variance and let V be the biological (real) variance. Then

$S=V+P$

Assuming the validity of Taylor's law, we have

$V=am^{b}$

Because in the Poisson distribution the mean equals the variance, we have

$P=m$

This gives us

$S=V+P=am^{b}+m$

This closely resembles Barlett's original suggestion.

### Interpretation

Slope values ( b ) significantly > 1 indicate clumping of the organisms.

In Poisson-distributed data, b = 1. If the population follows a lognormal or gamma distribution , then b = 2.

For populations that are experiencing constant per capita environmental variability, the regression of log( variance ) versus log( mean abundance ) should have a line with b = 2.

Most populations that have been studied have b < 2 (usually 1.5–1.6) but values of 2 have been reported. Occasionally cases with b > 2 have been reported. b values below 1 are uncommon but have also been reported ( b = 0.93 ).

It has been suggested that the exponent of the law ( b ) is proportional to the skewness of the underlying distribution. This proposal has criticised: additional work seems to be indicated.

### Notes

The origin of the slope ( b ) in this regression remains unclear. Two hypotheses have been proposed to explain it. One suggests that b arises from the species behavior and is a constant for that species. The alternative suggests that it is dependent on the sampled population. Despite the considerable number of studies carried out on this law (over 1000), this question remains open.

It is known that both a and b are subject to change due to age-specific dispersal, mortality and sample unit size.

This law may be a poor fit if the values are small. For this reason an extension to Taylor's law has been proposed by Hanski which improves the fit of Taylor's law at low densities.

### Extension to cluster sampling of binary data

A form of Taylor's law applicable to binary data in clusters (e.q., quadrats) has been proposed. In a binomial distribution, the theoretical variance is

${\text{var}}_{\text{bin}}=np(1-p),$

where (var bin ) is the binomial variance, n is the sample size per cluster, and p is the proportion of individuals with a trait (such as disease), an estimate of the probability of an individual having that trait.

One difficulty with binary data is that the mean and variance, in general, have a particular relationship: as the mean proportion of individuals infected increases above 0.5, the variance deceases.

It is now known that the observed variance (var obs ) changes as a power function of (var bin ).

Hughes and Madden noted that if the distribution is Poisson, the mean and variance are equal. As this is clearly not the case in many observed proportion samples, they instead assumed a binomial distribution. They replaced the mean in Taylor's law with the binomial variance and then compared this theoretical variance with the observed variance. For binomial data, they showed that var obs = var bin with overdispersion, var obs > var bin .

In symbols, Hughes and Madden's modification to Tyalor's law was

${\text{var}}_{\text{obs}}=a({\text{var}}_{\text{bin}})^{b}.$

In logarithmic form this relationship is

$\log({\text{var}}_{\text{obs}})=\log a+b\log({\text{var}}_{\text{bin}}).$

This latter version is known as the binary power law.

A key step in the derivation of the binary power law by Hughes and Madden was the observation made by Patil and Stiteler that the variance-to-mean ratio used for assessing over-dispersion of unbounded counts in a single sample is actually the ratio of two variances: the observed variance and the theoretical variance for a random distribution. For unbounded counts, the random distribution is the Poisson. Thus, the Taylor power law for a collection of samples can be considered as a relationship between the observed variance and the Poisson variance.

More broadly, Madden and Hughes considered the power law as the relationship between two variances, the observed variance and the theoretical variance for a random distribution. With binary data, the random distribution is the binomial (not the Poisson). Thus the Taylor power law and the binary power law are two special cases of a general power-law relationships for heterogeneity.

When both a and b are equal to 1, then a small-scale random spatial pattern is suggested and is best described by the binomial distribution. When b = 1 and a > 1, there is over-dispersion (small-scale aggregation). When b is > 1, the degree of aggregation varies with p . Turechek et al. have shown that the binary power law describes numerous data sets in plant pathology. In general, b is greater than 1 and less than 2.

The fit of this law has been tested by simulations. These results suggest that rather than a single regression line for the data set, a segmental regression may be a better model for genuinely random distributions. However, this segmentation only occurs for very short-range dispersal distances and large quadrat sizes. The break in the line occurs only at p very close to 0.

An extension to this law has been proposed. The original form of this law is symmetrical but it can be extended to an asymmetrical form. Using simulations the symmetrical form fits the data when there is positive correlation of disease status of neighbors. Where there is a negative correlation between the likelihood of neighbours being infected, the asymmetrical version is a better fit to the data.

## Applications

Because of the ubiquitous occurrence of Taylor's law in biology it has found a variety of uses some of which are listed here.

### Recommendations as to use

It has been recommended based on simulation studies in applications testing the validity of Taylor's law to a data sample that:

(1) the total number of organisms studied be > 15 (2) the minimum number of groups of organisms studied be > 5 (3) the density of the organisms should vary by at least 2 orders of magnitude within the sample

### Randomly distributed populations

It is commonly assumed (at least initially) that a population is randomly distributed in the environment. If a population is randomly distributed then the mean ( m ) and variance ( s 2 ) of the population are equal and the proportion of samples that contain at least one individual ( p ) is

$p=1-e^{-m}$

When a species with a clumped pattern is compared with one that is randomly distributed with equal overall densities, p will be less for the species having the clumped distribution pattern. Conversely when comparing a uniformly and a randomly distributed species but at equal overall densities, p will be greater for the randomly distributed population. This can be graphically tested by plotting p against m .

Wilson and Room developed a binomial model that incorporates Taylor's law. The basic relationship is

$p=1-e^{-m\log(s^{2}/m)(s^{2}/m-1)^{-1}}$

where the log is taken to the base e .

Incorporating Taylor's law this relationship becomes

$p=1-e^{-m\log(am^{b-1})(am^{b-1}-1)^{-1}}$

### Dispersion parameter estimator

The common dispersion parameter ( k ) of the negative binomial distribution is

$k={\frac {m^{2}}{s^{2}-m}}$

where $m$ is the sample mean and $s^{2}$ is the variance. If 1 / k is > 0 the population is considered to be aggregated; 1 / k = 0 ( s 2 = m ) the population is considered to be randomly (Poisson) distributed and if 1 / k is < 0 the population is considered to be uniformly distributed. No comment on the distribution can be made if k = 0.

Wilson and Room assuming that Taylor's law applied to the population gave an alternative estimator for k :

$k={\frac {m}{am^{b-1}-1}}$

where a and b are the constants from Taylor's law.

Jones using the estimate for k above along with the relationship Wilson and Room developed for the probability of finding a sample having at least one individual

$p=1-e^{-m\log(am^{b-1})(am^{b-1}-1)^{-1}}$

derived an estimator for the probability of a sample containing x individuals per sampling unit. Jones's formula is

$P(x)=P(x-1){\frac {k+x-1}{x}}{\frac {mk^{-1}}{mk^{-1}-1}}$

where P ( x ) is the probability of finding x individuals per sampling unit, k is estimated from the Wilson and Room equation and m is the sample mean. The probability of finding zero individuals P ( 0 ) is estimated with the negative binomial distribution

$P(0)=\left(1+{\frac {m}{k}}\right)^{-k}$

Jones also gives confidence intervals for these probabilities.

$\mathrm {CI} =t\left({\frac {P(x)(1-P(x))}{N}}\right)^{1/2}$

where CI is the confidence interval, t is the critical value taken from the t distribution and N is the total sample size.

### Katz family of distributions

Katz proposed a family of distributions (the Katz family ) with 2 parameters ( w 1 , w 2 ). This family of distributions includes the Bernoulli , Geometric , Pascal and Poisson distributions as special cases. The mean and variance of a Katz distribution are

$m={\frac {w_{1}}{1-w_{2}}}$

$s^{2}={\frac {w_{1}}{(1-w_{2})^{2}}}$

where m is the mean and s 2 is the variance of the sample. The parameters can be estimated by the method of moments from which we have

${\frac {w_{1}}{1-w_{2}}}=m$

${\frac {w_{2}}{1-w_{2}}}={\frac {s^{2}-m}{m}}$

For a Poisson distribution w 2 = 0 and w 1 = λ the parameter of the Possion distribution. This family of distributions is also sometimes known as the Panjer family of distributions.

The Katz family is related to the Sundt-Jewel family of distributions:

$p_{n}=\left(a+{\frac {b}{n}}\right)p_{n-1}$

The only members of the Sundt-Jewel family are the Poisson, binomial, negative binomial (Pascal), extended truncated negative binomial and logarithmic series distributions .

If the population obeys a Katz distribution then the coefficients of Taylor's law are

$a=-\log(1-w_{2})$

$b=1$

Katz also introduced a statistical test

$J_{n}={\sqrt {\frac {n}{2}}}{\frac {s^{2}-m}{m}}$

where J n is the test statistic, s 2 is the variance of the sample, m is the mean of the sample and n is the sample size. J n is asymptotically normally distributed with a zero mean and unit variance. If the sample is Poisson distributed J n = 0; values of J n < 0 and > 0 indicate under and over dispersion respectively. Overdispersion is often caused by latent heterogeneity - the presence of multiple sub populations within the population the sample is drawn from.

This statistic is related to the Neyman–Scott statistic

$NS={\sqrt {\frac {n-1}{2}}}\left({\frac {s^{2}}{m}}-1\right)$

which is known to be asymptotically normal and the conditional chi-squared statistic (Poisson dispersion test)

$T={\frac {(n-1)s^{2}}{m}}$

which is known to have an asymptotic chi squared distribution with n − 1 degrees of freedom when the population is Poisson distributed.

If the population obeys Taylor's law then

$J_{n}={\sqrt {\frac {n}{2}}}(am^{b-1}-1)$

### Time to extinction

If Taylor's law is assumed to apply it is possible to determine the mean time to local extinction. This model assumes a simple random walk in time and the absence of density dependent population regulation.

Let $N_{t+1}=rN_{t}$ where N t +1 and N t are the population sizes at time t + 1 and t respectively and r is parameter equal to the annual increase (decrease in population). Then

$\operatorname {var} (r)=s^{2}\log r$

where ${\text{var}}(r)$ is the variance of $r$ .

Let $K$ be a measure of the species abundance (organisms per unit area). Then

$T_{E}={\frac {2\log N}{\operatorname {Var} (r)}}\left(\log K-{\frac {\log N}{2}}\right)$

where T E is the mean time to local extinction.

The probability of extinction by time t is

$P(t)=1-e^{t/T_{E}}$

### Minimum population size required to avoid extinction

If a population is lognormally distributed then the harmonic mean of the population size ( H ) is related to the arithmetic mean ( m )

$H=m-am^{b-1}$

Given that H must be > 0 for the population to persist then rearranging we have

$m>a^{1/(2-b)}$

is the minimum size of population for the species to persist.

The assumption of a lognormal distribution appears to apply to about half of a sample of 544 species. suggesting that it is at least a plausible assumption.

### Sampling size estimators

The degree of precision ( D ) is defined to be s / m where s is the standard deviation and m is the mean. The degree of precision is known as the coefficient of variation in other contexts. In ecology research it is recommended that D be in the range 10–25%. The desired degree of precision is important in estimating the required sample size where an investigator wishes to test if Taylor's law applies to the data. The required sample size has been estimated for a number of simple distributions but where the population distribution is not known or cannot be assumed more complex formulae may needed to determine the required sample size.

Where the population is Poisson distributed the sample size ( n ) needed is

$n={\frac {(t/D)^{2}}{m}}$

where t is critical level of the t distribution for the type 1 error with the degrees of freedom that the mean ( m ) was calculated with.

If the population is distributed as a negative binomial distribution then the required sample size is

$n={\frac {(t/D)^{2}(m+k)}{mk}}$

where k is the parameter of the negative binomial distribution.

A more general sample size estimator has also been proposed

$n=\left({\frac {t}{D}}\right)^{2}am^{b-2}$

where a and b are derived from Taylor's law.

An alternative has been proposed by Southwood

$n=a{\frac {m^{b}}{D^{2}}}\,$

where n is the required sample size, a and b are the Taylor's law coefficients and D is the desired degree of precision.

Karandinos proposed two similar estimators for n . The first was modified by Ruesink to incorporate Taylor's law.

$n=\left({\frac {t}{d_{m}}}\right)^{2}am^{b-2}$

where d is the ratio of half the desired confidence interval ( CI ) to the mean. In symbols

$d_{m}={\frac {CI}{2m}}$

The second estimator is used in binomial (presence-absence) sampling. The desired sample size ( n ) is

$n=\left(td_{p}\right)^{2}p^{-1}q$

where the d p is ratio of half the desired confidence interval to the proportion of sample units with individuals, p is proportion of samples containing individuals and q = 1 − p . In symbols

$d_{p}={\frac {CI}{2p}}$

For binary (presence/absence) sampling, Schulthess et al modified Karandinos' equation

$N=\left({\frac {t}{D_{pi}}}\right)^{2}{\frac {1-p}{p}}$

where N is the required sample size, p is the proportion of units containing the organisms of interest, t is the chosen level of significance and D ip is a parameter derived from Taylor's law.

### Sequential sampling

Sequential analysis is a method of statistical analysis where the sample size is not fixed in advance. Instead samples are taken in accordance with a predefined stopping rule . Taylor's law has been used to derive a number of stopping rules.

A formula for fixed precision in serial sampling to test Taylor's law was derived by Green in 1970.

$\log T={\frac {\log(D^{2})-a}{b-2}}+(\log n){\frac {b-1}{b-2}}$

where T is the cumulative sample total, D is the level of precision, n is the sample size and a and b are obtained from Taylor's law.

As an aid to pest control Wilson et al developed a test that incorporated a threshold level where action should be taken. The required sample size is

$n=t|m-T|^{-2}am^{b}$

where a and b are the Taylor coefficients, || is the absolute value , m is the sample mean, T is the threshold level and t is the critical level of the t distribution. The authors also provided a similar test for binomial (presence-absence) sampling

$n=t|m-T|^{-2}pq$

where p is the probability of finding a sample with pests present and q = 1 − p .

Green derived another sampling formula for sequential sampling based on Taylor's law

$D=(an^{1-b}T^{b-2})^{1/2}$

where D is the degree of precision, a and b are the Taylor's law coefficients, n is the sample size and T is the total number of individuals sampled.

Serra et al have proposed a stopping rule based on Taylor's law.

$T_{n}\geq \left({\frac {an^{1-b}}{D^{2}}}\right)^{1/(2-b)}$

where a and b are the parameters from Taylor's law, D is the desired level of precision and T n is the total sample size.

Serra et al also proposed a second stopping rule based on Iwoa's regression

$T_{n}\geq {\frac {\alpha -1}{D^{2}-{\frac {\beta -1}{n}}}}$

where α and β are the parameters of the regression line, D is the desired level of precision and T n is the total sample size.

The authors recommended that D be set at 0.1 for studies of population dynamics and D = 0.25 for pest control.

## Related analyses

It is considered to be good practice to estimate at least one additional analysis of aggregation (other than Taylor's law) because the use of only a single index may be misleading. Although a number of other methods for detecting relationships between the variance and mean in biological samples have been proposed, to date none have achieved the popularity of Taylor's law. The most popular analysis used in conjunction with Taylor's law is probably Iwao's Patchiness regression test but all the methods listed here have been used in the literature.

### Barlett–Iwao model

Barlett in 1936 and later Iwao independently in 1968 both proposed an alternative relationship between the variance and the mean. In symbols

$s_{i}^{2}=am_{i}+bm_{i}^{2}\,$

where s is the variance in the i th sample and m i is the mean of the i th sample

When the population follows a negative binomial distribution , a = 1 and b = k (the exponent of the negative binomial distribution).

This alternative formulation has not been found to be as good a fit as Taylor's law in most studies.

### Nachman model

Nachman proposed a relationship between the mean density and the proportion of samples with zero counts:

$p_{0}=\exp(-am^{b})$

where p 0 is the proportion of the sample with zero counts, m is the mean density, a is a scale parameter and b is a dispersion parameter. If a = b = 1 the distribution is random. This relationship is usually tested in its logarithmic form

$\log m=c+d\log p_{0}$

Allsop used this relationship along with Taylor's law to derive an expression for the proportion of infested units in a sample

$P_{1}=1-\exp \left(-\exp \left({\frac {{\frac {\log _{e}\left({\frac {A^{2}}{a}}\right)}{b-2}}+\log _{e}(n)\left({\frac {b-1}{b-2}}-1\right)-c}{d}}\right)\right)$

$N=nP_{1}$

where

$A^{2}={\frac {D^{2}}{z_{\alpha /2}^{2}}}$

where D 2 is the degree of precision desired, z α/2 is the upper α/2 of the normal distribution, a and b are the Taylor's law coefficients, c and d are the Nachman coefficients, n is the sample size and N is the number of infested units.

### Kono–Sugino equation

Binary sampling is not uncommonly used in ecology. In 1958 Kono and Sugino derived an equation that relates the proportion of samples without individuals to the mean density of the samples.

$\log(m)=\log(a)+b\log(-\log(p_{0}))$

where p 0 is the proportion of the sample with no individuals, m is the mean sample density, a and b are constants. Like Taylor's law this equation has been found to fit a variety of populations including ones that obey Taylor's law. Unlike the negative binomial distribution this model is independent of the mean density.

The derivation of this equation is straightforward. Let the proportion of empty units be p 0 and assume that these are distributed exponentially. Then

$p_{0}=\exp(-Am^{B})$

Taking logs twice and rearranging, we obtain the equation above. This model is the same as that proposed by Nachman.

The advantage of this model is that it does not require counting the individuals but rather their presence or absence. Counting individuals may not be possible in many cases particularly where insects are the matter of study.

The equation was derived while examining the relationship between the proportion P of a series of rice hills infested and the mean severity of infestation m . The model studied was

$P=1-ae^{bm}$

where a and b are empirical constants. Based on this model the constants a and b were derived and a table prepared relating the values of P and m

The predicted estimates of m from this equation are subject to bias and it is recommended that the adjusted mean ( m a ) be used instead

$m_{a}=m\left(1-{\frac {\operatorname {var} (\log(m_{i}))}{2}}\right)$

where var is the variance of the sample unit means m i and m is the overall mean.

An alternative adjustment to the mean estimates is

$m_{a}=me^{({\text{MSE}}/2)}$

where MSE is the mean square error of the regression.

This model may also be used to estimate stop lines for enumerative (sequential) sampling. The variance of the estimated means is

$\operatorname {var} (m)=m^{2}(c_{1}+c_{2}-c_{3}+{\text{MSE}})$

where

$c_{1}={\frac {\beta ^{2}(1-p_{0})}{np_{0}\log _{e}(p_{0})^{2}}}$

$c_{2}={\frac {\text{MSE}}{N}}+s_{\beta }^{2}(\log _{e}(\log _{e}(p_{0}))-p^{2})$

$c_{3}={\frac {\exp(a+(b-2)[\alpha -\beta \log _{e}(p_{0})])}{n}}$

where MSE is the mean square error of the regression, α and β are the constant and slope of the regression respectively, s β 2 is the variance of the slope of the regression, N is the number of points in the regression, n is the number of sample units and p is the mean value of p 0 in the regression. The parameters a and b are estimated from Taylor's law:

$s^{2}=a+b\log _{e}(m)$

### Hughes–Madden equation

Hughes and Madden have proposed testing a similar relationship applicable to binary observations in cluster, where each cluster contains from 0 to n individuals.

$var_{\text{obs}}=ap^{b}(1-p)^{c}$

where a , b and c are constants, var obs is the observed variance, and p is the proportion of individuals with a trait (such as disease), an estimate of the probability of an individual with a trait. In logarithmic form, this relationship is

$\log(\operatorname {var} _{\text{obs}})=\log(a)+b\log(p)+c\log(1-p).$

In most cases, it is assumed that b = c , leading to a simple model

$\operatorname {var} _{\text{obs}}=a(p(1-p))^{b}$

This relationship has been subjected to less extensive testing than Taylor's law. However, it has accurately described over 100 data sets, and there are no published examples reporting that it does not works.

A variant of this equation was proposed by Shiyomi et al. ( ) who suggested testing the regression

$\log(\operatorname {var} _{\text{obs}}/n^{2})=a+b\log {\frac {p(1-p)}{n}}$

where var obs is the variance, a and b are the constants of the regression, n here is the sample size (not sample per cluster) and p is the probability of a sample containing at least one individual.

### Negative binomial distribution model

A negative binomial model has also been proposed. The dispersion parameter ( k ) using the method of moments is m 2 / ( s 2 – m ) and p i is the proportion of samples with counts > 0. The s 2 used in the calculation of k are the values predicted by Taylor's law. p i is plotted against 1 − ( k ( k + m ) −1 ) k and the fit of the data is visually inspected.

Perry and Taylor have proposed an alternative estimator of k based on Taylor's law.

${\frac {1}{k}}={\frac {am^{b-2}-1}{m}}$

A better estimate of the dispersion parameter can be made with the method of maximum likelihood . For the negative binomial it can be estimated from the equation

$\sum {\frac {A_{x}}{k+x}}=N\log \left(1+{\frac {m}{k}}\right)$

where A x is the total number of samples with more than x individuals, N is the total number of individuals, x is the number of individuals in a sample, m is the mean number of individuals per sample and k is the exponent. The value of k has to be estimated numerically.

Goodness of fit of this model can be tested in a number of ways including using the chi square test. As these may be biased by small samples an alternative is the U statistic – the difference between the variance expected under the negative binomial distribution and that of the sample. The expected variance of this distribution is m + m 2 / k and

$U=s^{2}-m+{\frac {m^{2}}{k}}$

where s 2 is the sample variance, m is the sample mean and k is the negative binomial parameter.

The variance of U is

$\operatorname {var} (U)=2mp^{2}q\left({\frac {1-R^{2}}{-\log(1-R)-R}}\right)+p^{4}{\frac {(1-R)^{-k}-1-kR}{N(-\log(1-R)-R)^{2}}}$

where p = m / k , q = 1 + p , R = p / q and N is the total number of individuals in the sample. The expected value of U is 0. For large sample sizes U is distributed normally.

Note: The negative binomial is actually a family of distributions defined by the relation of the mean to the variance

$\sigma ^{2}=\mu +a\mu ^{p}$

where a and p are constants. When a = 0 this defines the Poisson distribution. With p = 1 and p = 2, the distribution is known as the NB1 and NB2 distribution respectively.

This model is a version of that proposed earlier by Barlett.

### Tests for a common dispersion parameter

The dispersion parameter ( k ) is

$k={\frac {m^{2}}{s^{2}-m}}$

where m is the sample mean and s 2 is the variance. If k −1 is > 0 the population is considered to be aggregated; k −1 = 0 the population is considered to be random; and if k −1 is < 0 the population is considered to be uniformly distributed.

Southwood has recommended regressing k against the mean and a constant

$k_{i}=a+bm_{i}$

where k i and m i are the dispersion parameter and the mean of the ith sample respectively to test for the existence of a common dispersion parameter ( k c ). A slope ( b ) value significantly > 0 indicates the dependence of k on the mean density.

An alternative method was proposed by Elliot who suggested plotting ( s 2 − m ) against ( m 2 − s 2 / n ). k c is equal to 1/slope of this regression.

### Charlier coefficient

This coefficient ( C ) is defined as

$C={\frac {100(s^{2}-m)^{0.5}}{m}}$

If the population can be assumed to be distributed in a negative binomial fashion, then C = 100 (1/ k ) 0.5 where k is the dispersion parameter of the distribution.

### Cole's index of dispersion

This index ( I c ) is defined as

$I_{c}={\frac {\sum x^{2}}{(\sum x)^{2}}}$

The usual interpretation of this index is as follows: values of I c < 1, = 1, > 1 are taken to mean a uniform distribution, a random distribution or an aggregated distribution.

Because s 2 = Σ x 2 − (Σx) 2 , the index can also be written

$I_{c}={\frac {s^{2}+(nm)^{2}}{(nm)^{2}}}={\frac {1}{n^{2}}}{\frac {s^{2}}{m^{2}}}+1$

If Taylor's law can be assumed to hold, then

$I_{c}={\frac {am^{b-2}}{n^{2}}}+1$

### Lloyd's indexes

Lloyd's index of mean crowding ( IMC ) is the average number of other points contained in the sample unit that contains a randomly chosen point.

$\mathrm {IMC} =m+{\frac {s^{2}}{m-1}}$

where m is the sample mean and s 2 is the variance.

Lloyd's index of patchiness ( IP ) is

$\mathrm {IP} ={\text{IMC}}/m$

It is a measure of pattern intensity that is unaffected by thinning (random removal of points). This index was also proposed by Pielou in 1988 and is sometimes known by this name also.

Because an estimate of the variance of IP is extremely difficult to estimate from the formula itself, LLoyd suggested fitting a negative binomial distribution to the data. This method gives a parameter k

$s^{2}=m+{\frac {m^{2}}{k}}$

Then

$SE(IP)={\frac {1}{k^{2}}}\left[\operatorname {var} (k)+{\frac {k(k+1)(k+m)}{mq}}\right]$

where $SE(IP)$ is the standard error of the index of patchiness, ${\text{var}}(k)$ is the variance of the parameter k and q is the number of quadrats sampled.

If the population obeys Taylor's law then

$\mathrm {IMC} =m+a^{-1}m^{1-b}-1$

$\mathrm {IP} =1+a^{-1}m^{-b}-{\frac {1}{m}}$

### Patchiness regression test

Iwao proposed a patchiness regression to test for clumping

Let

$y_{i}=m_{i}+{\frac {s^{2}}{m_{i}}}-1$

y i here is Lloyd's index of mean crowding. Perform an ordinary least squares regression of m i against y .

In this regression the value of the slope ( b ) is an indicator of clumping: the slope = 1 if the data is Poisson-distributed. The constant ( a ) is the number of individuals that share a unit of habitat at infinitesimal density and may be < 0, 0 or > 0. These values represent regularity, randomness and aggregation of populations in spatial patterns respectively. A value of a < 1 is taken to mean that the basic unit of the distribution is a single individual.

Where the statistic s 2 / m is not constant it has been recommended to use instead to regress Lloyd's index against am + bm 2 where a and b are constants.

The sample size ( n ) for a given degree of precision ( D ) for this regression is given by

$n=\left({\frac {t}{D}}\right)^{2}\left({\frac {a+1}{m}}+b-1\right)$

where a is the constant in this regression, b is the slope, m is the mean and t is the critical value of the t distribution.

Iwao has proposed a sequential sampling test based on this regression. The upper and lower limits of this test are based on critical densities m c where control of a pest requires action to be taken.

$N_{u}=im_{c}+t(i(a+1)m_{c}+(b-1)m_{c}^{2})^{1/2}$

$N_{l}=im_{c}-t(i(a+1)m_{c}+(b-1)m_{c}^{2})^{1/2}$

where N u and N l are the upper and lower bounds respectively, a is the constant from the regression, b is the slope and i is the number of samples.

Kuno has proposed an alternative sequential stopping test also based on this regression.

$T_{n}={\frac {a+1}{D^{2}-{\frac {b-1}{n}}}}$

where T n is the total sample size, D is the degree of precision, n is the number of samples units, a is the constant and b is the slope from the regression respectively.

Kuno's test is subject to the condition that n ≥ ( b − 1) / D 2

Parrella and Jones have proposed an alternative but related stop line

$T_{n}=\left(1-{\frac {n}{N}}\right){\frac {a+1}{D^{2}-\left(1-{\frac {n}{N}}\right){\frac {b-1}{n}}}}$

where a and b are the parameters from the regression, N is the maximum number of sampled units and n is the individual sample size.

### Morisita's index of dispersion

Masaaki Morisita 's index of dispersion ( I m ) is the scaled probability that two points chosen at random from the whole population are in the same sample. Higher values indicate a more clumped distribution.

$I_{m}={\frac {\sum x(x-1)}{nm(m-1)}}$

An alternative formulation is

$I_{m}=n{\frac {\sum x^{2}-\sum x}{(\sum x)^{2}-\sum x}}$

where n is the total sample size, m is the sample mean and x are the individual values with the sum taken over the whole sample.
It is also equal to

$I_{m}={\frac {n\operatorname {IMC} }{nm-1}}$

where IMC is Lloyd's index of crowding.

This index is relatively independent of the population density but is affected by the sample size. Values > 1 indicate clumping; values < 1 indicate a uniformity of distribution and a value of 1 indicates a random sample.

Morisita showed that the statistic

$I_{m}\left(\sum x-1\right)+n-\sum x$

is distributed as a chi squared variable with n − 1 degrees of freedom.

An alternative significance test for this index has been developed for large samples.

$z={\frac {I_{m}-1}{2/(nm^{2})}}$

where m is the overall sample mean, n is the number of sample units and z is the normal distribution abscissa . Significance is tested by comparing the value of z against the values of the normal distribution .

A function for its calculation is available in the statistical R language in the vegan package .

Note, not to be confused with Morisita's overlap index .

### Standardised Morisita's index

Smith-Gill developed a statistic based on Morisita's index which is independent of both sample size and population density and bounded by −1 and +1. This statistic is calculated as follows

First determine Morisita's index ( I d ) in the usual fashion. Then let k be the number of units the population was sampled from. Calculate the two critical values

$M_{u}={\frac {\chi _{0.975}^{2}-k+\sum x}{\sum x-1}}$

$M_{c}={\frac {\chi _{0.025}^{2}-k+\sum x}{\sum x-1}}$

where χ 2 is the chi square value for n − 1 degrees of freedom at the 97.5% and 2.5% levels of confidence.

The standardised index ( I p ) is then calculated from one of the formulae below.

When I d ≥ M c > 1

$I_{p}=0.5+0.5\left({\frac {I_{d}-M_{c}}{k-M_{c}}}\right)$

When M c > I d ≥ 1

$I_{p}=0.5\left({\frac {I_{d}-1}{M_{u}-1}}\right)$

When 1 > I d ≥ M u

$I_{p}=-0.5\left({\frac {I_{d}-1}{M_{u}-1}}\right)$

When 1 > M u > I d

$I_{p}=-0.5+0.5\left({\frac {I_{d}-M_{u}}{M_{u}}}\right)$

I p ranges between +1 and −1 with 95% confidence intervals of ±0.5. I p has the value of 0 if the pattern is random; if the pattern is uniform, I p < 0 and if the pattern shows aggregation, I p > 0.

### Southwood's index of spatial aggregation

Southwood's index of spatial aggregation ( k ) is defined as

${\frac {1}{k}}={\frac {m^{*}}{m}}-1$

where m is the mean of the sample and m * is Lloyd's index of crowding.

### Fisher's index of dispersion

Fisher's index of dispersion is

$\mathrm {ID} ={\frac {(n-1)s^{2}}{m}}$

This index may be used to test for over dispersion of the population. It is recommended that in applications n > 5 and that the sample total divided by the number of samples is > 3. In symbols

${\frac {\sum x}{n}}>3$

where x is an individual sample value. The expectation of the index is equal to n and it is distributed as the chi-square distribution with n − 1 degrees of freedom when the population is Poisson distributed. It is equal to the scale parameter when the population obeys the gamma distribution .

It can be applied both to the overall population and to the individual areas sampled individually. The use of this test on the individual sample areas should also include the use of a Bonferroni correction factor.

If the population obeys Taylor's law then

$\mathrm {ID} =(n-1)am^{b-1}$

### Index of cluster size

The index of cluster size ( ICS ) was created by David and Moore. Under a random (Poisson) distribution ICS is expected to equal 0. Positive values indicate a clumped distribution; negative values indicate a uniform distribution.

$\mathrm {ICS} ={\frac {s^{2}}{m-1}}$

where s 2 is the variance and m is the mean.

If the population obeys Taylor's law

$\mathrm {ICS} =am^{b-1}-1$

The ICS is also equal to Katz's test statistic divided by ( n / 2 ) 1/2 where n is the sample size. It is also related to Clapham's test statistic. It is also sometimes referred to as the clumping index.

### Green's index

Green's index ( GI ) is a modification of the index of cluster size that is independent of n the number of sample units.

$C_{x}={\frac {s^{2}/m-1}{nm-1}}$

This index equals 0 if the distribution is random, 1 if it is maximally aggregated and −1 / ( nm − 1 ) if it is uniform.

The distribution of Green's index is not currently known so statistical tests have been difficult to devise for it.

If the population obeys Taylor's law

$C_{x}={\frac {am^{b-1}-1}{nm-1}}$

### Binary dispersal index

Binary sampling (presence/absence) is frequently used where it is difficult to obtain accurate counts. The dispersal index ( D ) is used when the study population is divided into a series of equal samples ( number of units = N : number of units per sample = n : total population size = n x N ). The theoretical variance of a sample from a population with a binomial distribution is

$s^{2}=np(1-p)$

where s 2 is the variance, n is the number of units sampled and p is the mean proportion of sampling units with at least one individual present. The dispersal index ( D ) is defined as the ratio of observed variance to the expected variance. In symbols

$D={\frac {{\text{var}}_{\text{obs}}}{{\text{var}}_{\text{bin}}}}={\frac {s^{2}}{np(1-p)}}$

where var obs is the observed variance and var bin is the expected variance. The expected variance is calculated with the overall mean of the population. Values of D > 1 are considered to suggest aggregation. D ( n − 1 ) is distributed as the chi squared variable with n − 1 degrees of freedom where n is the number of units sampled.

An alternative test is the C test.

$C={\frac {D(nN-1)-nN}{(2N(n^{2}-n))^{1/2}}}$

where D is the dispersal index, n is the number of units per sample and N is the number of samples. C is distributed normally. A statistically significant value of C indicates overdispersion of the population.

D is also related to intraclass correlation ( ρ ) which is defined as

$\rho =1-{\frac {\sum x_{i}(T-x_{i})}{p(1-p)NT(T-1)}}$

where T is the number of organisms per sample, p is the likelihood of the organism having the sought after property (diseased, pest free, etc ), and x i is the number of organism in the i th unit with this property. T must be the same for all sampled units. In this case with n constant

$\rho ={\frac {D-1}{n-1}}$

If the data can be fitted with a beta-binomial distribution then

$D=1+{\frac {(n-1)\theta }{1+\theta }}$

where θ is the parameter of the distribution.

### Ma's population aggregation critical density

Ma has proposed a parameter ( m 0 ) − the population aggregation critical density - to relate population density to Taylor's law.

$m_{0}=\exp \left({\frac {\log a}{1-b}}\right)$

## Related statistics

A number of statistical tests are known that may be of use in applications.

### de Oliveria's statistic

A related statistic suggested by de Oliveria is the difference of the variance and the mean. If the population is Poisson distributed then

$var(s^{2}-m)={\frac {2t^{2}}{n-1}}$

where t is the Poisson parameter, s 2 is the variance, m is the mean and n is the sample size. The expected value of s 2 - m is zero. This statistic is distributed normally.

If the Poisson parameter in this equation is estimated by putting t = m , after a little manipulation this statistic can be written

$O_{T}={\sqrt {\frac {n-1}{2}}}{\frac {s^{2}-m}{m}}$

This is almost identical to Katz's statistic with ( n - 1 ) replacing n . Again O T is normally distributed with mean 0 and unit variance for large n . This statistic is the same as the Neyman-Scott statistic.

de Oliveria actually suggested that the variance of s 2 - m was ( 1 - 2 t 1/2 + 3 t ) / n where t is the Poisson parameter. He suggested that t could be estimated by putting it equal to the mean ( m ) of the sample. Further investigation by Bohning showed that this estimate of the variance was incorrect. Bohning's correction is given in the equations above.

### Clapham's test

In 1936 Clapham proposed using the ratio of the variance to the mean as a test statistic (the relative variance). In symbols

$\theta ={\frac {s^{2}}{m}}$

For a Possion distribution this ratio equals 1. To test for deviations from this value he proposed testing its value against the chi square distribution with n degrees of freedom where n is the number of sample units. The distribution of this statistic was studied further by Blackman who noted that it was approximately normally distributed with a mean of 1 and a variance ( V θ ) of

$V_{\theta }={\frac {2n}{(n-1)^{2}}}$

The derivation of the variance was re analysed by Bartlett who considered it to be

$V_{\theta }={\frac {2}{n-1}}$

For large samples these two formulae are in approximate agreement. This test is related to the later Katz's J n statistic.

If the population obeys Taylor's law then

$\theta =am^{b-1}$

A refinement on this test has also been published These authors noted that the original test tends to detect overdispersion at higher scales even when this was not present in the data. They noted that the use of the multinomial distribution may be more appropriate than the use of a Poisson distribution for such data. The statistic θ is distributed

$\theta ={\frac {s^{2}}{m}}={\frac {1}{n}}\sum \left(x_{i}-{\frac {n}{N}}\right)^{2}$

where N is the number of sample units, n is the total number of samples examined and x i are the individual data values.

The expectation and variance of θ are

$\operatorname {E} (\theta )={\frac {N}{N-1}}$

$\operatorname {Var} (\theta )={\frac {(N-1)^{2}}{N^{3}}}-{\frac {2N-3}{nN^{2}}}$

For large N , E( θ ) is approximately 1 and

$\operatorname {Var} (\theta )\sim \ {\frac {2}{N}}\left(1-{\frac {1}{n}}\right)$

If the number of individuals sampled ( n ) is large this estimate of the variance is in agreement with those derived earlier. However, for smaller samples these latter estimates are more precise and should be used.
