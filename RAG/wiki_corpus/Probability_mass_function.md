# Probability mass function

> **Query Topic**: probability mass function (PMF) and probability density function (PDF) (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 25, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Probability_mass_function

---

In probability and statistics , a probability mass function (sometimes called probability function or frequency function ) is a function that gives the probability that a discrete random variable is exactly equal to some value. Sometimes it is also known as the discrete probability density function . The probability mass function is often the primary means of defining a discrete probability distribution , and such functions exist for either scalar or multivariate random variables whose domain is discrete.

A probability mass function differs from a continuous probability density function (PDF) in that the latter is associated with continuous rather than discrete random variables. A continuous PDF must be integrated over an interval to yield a probability.

The value of the random variable having the largest probability mass is called the mode .

## Formal definition

Probability mass function is the probability distribution of a discrete random variable , and provides the possible values and their associated probabilities. It is the function $p:\mathbb {R} \to [0,1]$ defined by

$p_{X}(x)=P(X=x)$

for $-\infty <x<\infty$ , where $P$ is a probability measure . $p_{X}(x)$ can also be simplified as $p(x)$ .

The probabilities associated with all (hypothetical) values must be non-negative and sum up to 1,

$\sum _{x}p_{X}(x)=1$ and $p_{X}(x)\geq 0.$

Thinking of probability as mass helps to avoid mistakes since the physical mass is conserved as is the total probability for all hypothetical outcomes $x$ .

## Measure theoretic formulation

A probability mass function of a discrete random variable $X$ can be seen as a special case of two more general measure theoretic constructions: 
the distribution of $X$ and the probability density function of $X$ with respect to the counting measure . We make this more precise below.

Suppose that $(A,{\mathcal {A}},P)$ is a probability space and that $(B,{\mathcal {B}})$ is a measurable space whose underlying σ-algebra is discrete, so in particular contains singleton sets of $B$ . In this setting, a random variable $X\colon A\to B$ is discrete provided its image is countable.
The pushforward measure $X_{*}(P)$ —called the distribution of $X$ in this context—is a probability measure on $B$ whose restriction to singleton sets induces the probability mass function (as mentioned in the previous section) $f_{X}\colon B\to \mathbb {R}$ since $f_{X}(b)=P(X^{-1}(b))=P(X=b)$ for each $b\in B$ .

Now suppose that $(B,{\mathcal {B}},\mu )$ is a measure space equipped with the counting measure $\mu$ . The probability density function $f$ of $X$ with respect to the counting measure, if it exists, is the Radon–Nikodym derivative of the pushforward measure of $X$ (with respect to the counting measure), so $f=dX_{*}P/d\mu$ and $f$ is a function from $B$ to the non-negative reals. As a consequence, for any $b\in B$ we have $P(X=b)=P(X^{-1}(b))=X_{*}(P)(b)=\int _{b}fd\mu =f(b),$

demonstrating that $f$ is in fact a probability mass function.

When there is a natural order among the potential outcomes $x$ , it may be convenient to assign numerical values to them (or n -tuples in case of a discrete multivariate random variable ) and to consider also values not in the image of $X$ . That is, $f_{X}$ may be defined for all real numbers and $f_{X}(x)=0$ for all $x\notin X(S)$ as shown in the figure.

The image of $X$ has a countable subset on which the probability mass function $f_{X}(x)$ is one. Consequently, the probability mass function is zero for all but a countable number of values of $x$ .

The discontinuity of probability mass functions is related to the fact that the cumulative distribution function of a discrete random variable is also discontinuous. If $X$ is a discrete random variable, then $P(X=x)=1$ means that the casual event $(X=x)$ is certain (it is true in 100% of the occurrences); on the contrary, $P(X=x)=0$ means that the casual event $(X=x)$ is always impossible. This statement isn't true for a continuous random variable $X$ , for which $P(X=x)=0$ for any possible $x$ . Discretization is the process of converting a continuous random variable into a discrete one.

## Examples

### Finite

There are three major distributions associated, the Bernoulli distribution , the binomial distribution and the geometric distribution .

- Bernoulli distribution: ber(p) , is used to model an experiment with only two possible outcomes. The two outcomes are often encoded as 1 and 0. $p_{X}(x)={\begin{cases}p,&{\text{if }}x{\text{ is 1}}\\1-p,&{\text{if }}x{\text{ is 0}}\end{cases}}$ An example of the Bernoulli distribution is tossing a coin. Suppose that $S$ is the sample space of all outcomes of a single toss of a fair coin , and $X$ is the random variable defined on $S$ assigning 0 to the category "tails" and 1 to the category "heads". Since the coin is fair, the probability mass function is $p_{X}(x)={\begin{cases}{\frac {1}{2}},&x=0,\\{\frac {1}{2}},&x=1,\\0,&x\notin \{0,1\}.\end{cases}}$

- Binomial distribution, models the number of successes when someone draws n times with replacement. Each draw or experiment is independent, with two possible outcomes. The associated probability mass function is ${\textstyle {\binom {n}{k}}p^{k}(1-p)^{n-k}}$ . An example of the binomial distribution is the probability of getting exactly one 6 when someone rolls a fair die three times.

- Geometric distribution describes the number of trials needed to get one success. Its probability mass function is ${\textstyle p_{X}(k)=(1-p)^{k-1}p}$ . An example is tossing a coin until the first "heads" appears. $p$ denotes the probability of the outcome "heads", and $k$ denotes the number of necessary coin tosses. Other distributions that can be modeled using a probability mass function are the categorical distribution (also known as the generalized Bernoulli distribution) and the multinomial distribution .

- If the discrete distribution has two or more categories one of which may occur, whether or not these categories have a natural ordering, when there is only a single trial (draw) this is a categorical distribution.

- An example of a multivariate discrete distribution , and of its probability mass function, is provided by the multinomial distribution . Here the multiple random variables are the numbers of successes in each of the categories after a given number of trials, and each non-zero probability mass gives the probability of a certain combination of numbers of successes in the various categories.

### Infinite

The following exponentially declining distribution is an example of a distribution with an infinite number of possible outcomes—all the positive integers: ${\text{Pr}}(X=i)={\frac {1}{2^{i}}}\qquad {\text{for }}i=1,2,3,\dots$ Despite the infinite number of possible outcomes, the total probability mass is 1/2 + 1/4 + 1/8 + ⋯ = 1, satisfying the unit total probability requirement for a probability distribution.

## Multivariate case

Two or more discrete random variables have a joint probability mass function, which gives the probability of each possible combination of realizations for the random variables.
