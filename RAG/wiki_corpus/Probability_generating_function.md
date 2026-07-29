# Probability generating function

> **Query Topic**: probability mass function (PMF) and probability density function (PDF) (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 25, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Probability_generating_function

---

In probability theory , the probability generating function of a discrete random variable is a power series representation (the generating function ) of the probability mass function of the random variable . Probability generating functions are often employed for their succinct description of the sequence of probabilities Pr( X = i ) in the probability mass function for a random variable X , and to make available the well-developed theory of power series with non-negative coefficients.

## Definition

### Univariate case

If X is a discrete random variable taking values x in the non-negative integers {0,1, ...}, then the probability generating function of X is defined as

$G(z)=\operatorname {E} (z^{X})=\sum _{x=0}^{\infty }p(x)z^{x},$ where $p$ is the probability mass function of $X$ . Note that the subscripted notations $G_{X}$ and $p_{X}$ are often used to emphasize that these pertain to a particular random variable $X$ , and to its distribution . The power series converges absolutely at least for all complex numbers $z$ with $|z|<1$ ; the radius of convergence being often larger.

### Multivariate case

If X = ( X 1 ,..., X d ) is a discrete random variable taking values ( x 1 , ..., x d ) in the d -dimensional non-negative integer lattice {0,1, ...} d , then the probability generating function of X is defined as $G(z)=G(z_{1},\ldots ,z_{d})=\operatorname {E} {\bigl (}z_{1}^{X_{1}}\cdots z_{d}^{X_{d}}{\bigr )}=\sum _{x_{1},\ldots ,x_{d}=0}^{\infty }p(x_{1},\ldots ,x_{d})z_{1}^{x_{1}}\cdots z_{d}^{x_{d}},$ where p is the probability mass function of X . The power series converges absolutely at least for all complex vectors $z=(z_{1},...z_{d})\in \mathbb {C} ^{d}$ with ${\text{max}}\{|z_{1}|,...,|z_{d}|\}\leq 1.$

## Properties

### Power series

Probability generating functions obey all the rules of power series with non-negative coefficients. In particular, $G(1^{-})=1$ , where $G(1^{-})=\lim _{x\to 1,x<1}G(x)$ , x approaching 1 from below , since the probabilities must sum to one. So the radius of convergence of any probability generating function must be at least 1, by Abel's theorem for power series with non-negative coefficients.

### Probabilities and expectations

The following properties allow the derivation of various basic quantities related to $X$ :

- The probability mass function of $X$ is recovered by taking derivatives of $G$ , $p(k)=\operatorname {Pr} (X=k)={\frac {G^{(k)}(0)}{k!}}.$

- It follows from Property 1 that if random variables $X$ and $Y$ have probability generating functions that are equal, $G_{X}=G_{Y}$ , then $p_{X}=p_{Y}$ . That is, if $X$ and $Y$ have identical probability generating functions, then they have identical distributions.

- The normalization of the probability mass function can be expressed in terms of the generating function by $\operatorname {E} [1]=G(1^{-})=\sum _{i=0}^{\infty }p(i)=1.$ The expectation of $X$ is given by $\operatorname {E} [X]=G'(1^{-}).$ More generally, the $k^{th}$ factorial moment , $\operatorname {E} [X(X-1)\cdots (X-k+1)]$ of $X$ is given by $\operatorname {E} \left[{\frac {X!}{(X-k)!}}\right]=G^{(k)}(1^{-}),\quad k\geq 0.$ So the variance of $X$ is given by $\operatorname {Var} (X)=G''(1^{-})+G'(1^{-})-\left[G'(1^{-})\right]^{2}.$ Finally, the k -th raw moment of X is given by $\operatorname {E} [X^{k}]=\left(z{\frac {\partial }{\partial z}}\right)^{k}G(z){\Big |}_{z=1^{-}}$

- $G_{X}(e^{t})=M_{X}(t)$ where X is a random variable, $G_{X}(t)$ is the probability generating function (of $X$ ) and $M_{X}(t)$ is the moment-generating function (of $X$ ).

### Functions of independent random variables

Probability generating functions are particularly useful for dealing with functions of independent random variables. For example:

- If $X_{i},i=1,2,\cdots ,N$ is a sequence of independent (and not necessarily identically distributed) random variables that take on natural-number values, and $S_{N}=\sum _{i=1}^{N}a_{i}X_{i},$ where the $a_{i}$ are constant natural numbers, then the probability generating function is given by $G_{S_{N}}(z)=\operatorname {E} (z^{S_{N}})=\operatorname {E} \left(z^{\sum _{i=1}^{N}a_{i}X_{i},}\right)=G_{X_{1}}(z^{a_{1}})G_{X_{2}}(z^{a_{2}})\cdots G_{X_{N}}(z^{a_{N}}).$

- In particular, if $X$ and $Y$ are independent random variables: $G_{X+Y}(z)=G_{X}(z)\cdot G_{Y}(z)$ and $G_{X-Y}(z)=G_{X}(z)\cdot G_{Y}(1/z).$

- In the above, the number $N$ of independent random variables in the sequence is fixed. Assume $N$ is discrete random variable taking values on the non-negative integers, which is independent of the $X_{i}$ , and consider the probability generating function $G_{N}$ . If the $X_{i}$ are not only independent but also identically distributed with common probability generating function $G_{X}=G_{X_{i}}$ , then $G_{S_{N}}(z)=G_{N}(G_{X}(z)).$ This can be seen, using the law of total expectation , as follows: ${\begin{aligned}G_{S_{N}}(z)&=\operatorname {E} (z^{S_{N}})=\operatorname {E} (z^{\sum _{i=1}^{N}X_{i}})\\[4pt]&=\operatorname {E} {\big (}\operatorname {E} (z^{\sum _{i=1}^{N}X_{i}}\mid N){\big )}=\operatorname {E} {\big (}(G_{X}(z))^{N}{\big )}=G_{N}(G_{X}(z)).\end{aligned}}$ This last fact is useful in the study of Galton–Watson processes and compound Poisson processes .

- When the $X_{i}$ are not supposed identically distributed (but still independent and independent of $N$ ), we have $G_{S_{N}}(z)=\sum _{n\geq 1}f_{n}\prod _{i=1}^{n}G_{X_{i}}(z),$ where $f_{n}=\Pr(N=n).$ For identically distributed $X_{i}$ s, this simplifies to the identity stated before, but the general case is sometimes useful to obtain a decomposition of $S_{N}$ by means of generating functions.

## Examples

- The probability generating function of an almost surely constant random variable , i.e. one with $\Pr(X=c)=1$ and $\Pr(X\neq c)=0$ is $G(z)=z^{c}.$

- The probability generating function of a binomial random variable , the number of successes in $n$ trials, with probability $p$ of success in each trial, is $G(z)=\left[(1-p)+pz\right]^{n}.$ Note : it is the $n$ -fold product of the probability generating function of a Bernoulli random variable with parameter $p$ . So the probability generating function of a fair coin , is $G(z)={\frac {1}{2}}+{\frac {z}{2}}.$

- The probability generating function of a negative binomial random variable on $\{0,1,2\cdots \}$ , the number of failures until the $r^{th}$ success with probability of success in each trial $p$ , is $G(z)=\left({\frac {p}{1-(1-p)z}}\right)^{r},$ which converges for $|z|<{\frac {1}{1-p}}$ . Note that this is the $r$ -fold product of the probability generating function of a geometric random variable with parameter $1-p$ on $\{0,1,2,\cdots \}$ .

- The probability generating function of a Poisson random variable with rate parameter $\lambda$ is $G(z)=e^{\lambda (z-1)}.$

## Related concepts

The probability generating function is an example of a generating function of a sequence: see also formal power series . It is equivalent to, and sometimes called, the z-transform of the probability mass function.

Other generating functions of random variables include the moment-generating function , the characteristic function and the cumulant generating function . The probability generating function is also equivalent to the factorial moment generating function , which as $\operatorname {E} \left[z^{X}\right]$ can also be considered for continuous and other random variables.
