# Probability generating function

> **Query Topic**: probability mass function (PMF) and probability density function (PDF) (Rank #2 Search Result)  
> **Source Queue**: train (Row ID: 105, Frequency: 5)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Probability_generating_function

---

In probability theory, the probability generating function of a discrete random variable is a power series representation (the generating function) of the probability mass function of the random variable.  Probability generating functions are often employed for their succinct description of the sequence of probabilities Pr(X = i) in the probability mass function for a random variable X, and to make available the well-developed theory of power series with non-negative coefficients.


== Definition ==


=== Univariate case ===
If X is a discrete random variable taking values x in the non-negative integers {0,1, ...}, then the probability generating function of X is defined as

  
    
      
        G
        (
        z
        )
        =
        E
        ⁡
        (
        
          z
          
            X
          
        
        )
        =
        
          ∑
          
            x
            =
            0
          
          
            ∞
          
        
        p
        (
        x
        )
        
          z
          
            x
          
        
        ,
      
    
    {\displaystyle G(z)=\operatorname {E} (z^{X})=\sum _{x=0}^{\infty }p(x)z^{x},}
  

where 
  
    
      
        p
      
    
    {\displaystyle p}
  
 is the probability mass function of 
  
    
      
        X
      
    
    {\displaystyle X}
  
.  Note that the subscripted notations 
  
    
      
        
          G
          
            X
          
        
      
    
    {\displaystyle G_{X}}
  
 and 
  
    
      
        
          p
          
            X
          
        
      
    
    {\displaystyle p_{X}}
  
 are often used to emphasize that these pertain to a particular random variable 
  
    
      
        X
      
    
    {\displaystyle X}
  
, and to its distribution. The power series converges absolutely at least for all complex numbers 
  
    
      
        z
      
    
    {\displaystyle z}
  
 with 
  
    
      
        
          |
        
        z
        
          |
        
        <
        1
      
    
    {\displaystyle |z|<1}
  
; the radius of convergence being often larger.


=== Multivariate case ===
If X = (X1,...,Xd) is a discrete random variable taking values (x1, ..., xd) in the d-dimensional non-negative integer lattice {0,1, ...}d, then the probability generating function of X is defined as

  
    
      
        G
        (
        z
        )
        =
        G
        (
        
          z
          
            1
          
        
        ,
        …
        ,
        
          z
          
            d
          
        
        )
        =
        E
        ⁡
        
          
            (
          
        
        
          z
          
            1
          
          
            
              X
              
                1
              
            
          
        
        ⋯
        
          z
          
            d
          
          
            
              X
              
                d
              
            
          
        
        
          
            )
          
        
        =
        
          ∑
          
            
              x
              
                1
              
            
            ,
            …
            ,
            
              x
              
                d
              
            
            =
            0
          
          
            ∞
          
        
        p
        (
        
          x
          
            1
          
        
        ,
        …
        ,
        
          x
          
            d
          
        
        )
        
          z
          
            1
          
          
            
              x
              
                1
              
            
          
        
        ⋯
        
          z
          
            d
          
          
            
              x
              
                d
              
            
          
        
        ,
      
    
    {\displaystyle G(z)=G(z_{1},\ldots ,z_{d})=\operatorname {E} {\bigl (}z_{1}^{X_{1}}\cdots z_{d}^{X_{d}}{\bigr )}=\sum _{x_{1},\ldots ,x_{d}=0}^{\infty }p(x_{1},\ldots ,x_{d})z_{1}^{x_{1}}\cdots z_{d}^{x_{d}},}
  

where p is the probability mass function of X. The power series converges absolutely at least for all complex vectors 
  
    
      
        z
        =
        (
        
          z
          
            1
          
        
        ,
        .
        .
        .
        
          z
          
            d
          
        
        )
        ∈
        
          
            C
          
          
            d
          
        
      
    
    {\displaystyle z=(z_{1},...z_{d})\in \mathbb {C} ^{d}}
  
 with 
  
    
      
        
          max
        
        {
        
          |
        
        
          z
          
            1
          
        
        
          |
        
        ,
        .
        .
        .
        ,
        
          |
        
        
          z
          
            d
          
        
        
          |
        
        }
        ≤
        1.
      
    
    {\displaystyle {\text{max}}\{|z_{1}|,...,|z_{d}|\}\leq 1.}
  


== Properties ==


=== Power series ===
Probability generating functions obey all the rules of power series with non-negative coefficients.  In particular, 
  
    
      
        G
        (
        
          1
          
            −
          
        
        )
        =
        1
      
    
    {\displaystyle G(1^{-})=1}
  
, where 
  
    
      
        G
        (
        
          1
          
            −
          
        
        )
        =
        
          lim
          
            x
            →
            1
            ,
            x
            <
            1
          
        
        G
        (
        x
        )
      
    
    {\displaystyle G(1^{-})=\lim _{x\to 1,x<1}G(x)}
  
, x approaching 1 from below, since the probabilities must sum to one. So the radius of convergence of any probability generating function must be at least 1, by Abel's theorem for power series with non-negative coefficients.


=== Probabilities and expectations ===
The following properties allow the derivation of various basic quantities related to 
  
    
      
        X
      
    
    {\displaystyle X}
  
:

The probability mass function of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 is recovered by taking derivatives of 
  
    
      
        G
      
    
    {\displaystyle G}
  
, 
  
    
      
        p
        (
        k
        )
        =
        Pr
        ⁡
        (
        X
        =
        k
        )
        =
        
          
            
              
                G
                
                  (
                  k
                  )
                
              
              (
              0
              )
            
            
              k
              !
            
          
        
        .
      
    
    {\displaystyle p(k)=\operatorname {Pr} (X=k)={\frac {G^{(k)}(0)}{k!}}.}
  

It follows from Property 1 that if random variables 
  
    
      
        X
      
    
    {\displaystyle X}
  
 and 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 have probability generating functions that are equal, 
  
    
      
        
          G
          
            X
          
        
        =
        
          G
          
            Y
          
        
      
    
    {\displaystyle G_{X}=G_{Y}}
  
, then 
  
    
      
        
          p
          
            X
          
        
        =
        
          p
          
            Y
          
        
      
    
    {\displaystyle p_{X}=p_{Y}}
  
.  That is, if 
  
    
      
        X
      
    
    {\displaystyle X}
  
 and 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 have identical probability generating functions, then they have identical distributions.
The normalization of the probability mass function can be expressed in terms of the generating function by 
  
    
      
        E
        ⁡
        [
        1
        ]
        =
        G
        (
        
          1
          
            −
          
        
        )
        =
        
          ∑
          
            i
            =
            0
          
          
            ∞
          
        
        p
        (
        i
        )
        =
        1.
      
    
    {\displaystyle \operatorname {E} [1]=G(1^{-})=\sum _{i=0}^{\infty }p(i)=1.}
  
 The expectation of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 is given by 
  
    
      
        E
        ⁡
        [
        X
        ]
        =
        
          G
          ′
        
        (
        
          1
          
            −
          
        
        )
        .
      
    
    {\displaystyle \operatorname {E} [X]=G'(1^{-}).}
  
 More generally, the 
  
    
      
        
          k
          
            t
            h
          
        
      
    
    {\displaystyle k^{th}}
  
factorial moment, 
  
    
      
        E
        ⁡
        [
        X
        (
        X
        −
        1
        )
        ⋯
        (
        X
        −
        k
        +
        1
        )
        ]
      
    
    {\displaystyle \operatorname {E} [X(X-1)\cdots (X-k+1)]}
  
 of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 is given by 
  
    
      
        E
        ⁡
        
          [
          
            
              
                X
                !
              
              
                (
                X
                −
                k
                )
                !
              
            
          
          ]
        
        =
        
          G
          
            (
            k
            )
          
        
        (
        
          1
          
            −
          
        
        )
        ,
        
        k
        ≥
        0.
      
    
    {\displaystyle \operatorname {E} \left[{\frac {X!}{(X-k)!}}\right]=G^{(k)}(1^{-}),\quad k\geq 0.}
  
 So the variance of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 is given by 
  
    
      
        Var
        ⁡
        (
        X
        )
        =
        
          G
          ″
        
        (
        
          1
          
            −
          
        
        )
        +
        
          G
          ′
        
        (
        
          1
          
            −
          
        
        )
        −
        
          
            [
            
              
                G
                ′
              
              (
              
                1
                
                  −
                
              
              )
            
            ]
          
          
            2
          
        
        .
      
    
    {\displaystyle \operatorname {Var} (X)=G''(1^{-})+G'(1^{-})-\left[G'(1^{-})\right]^{2}.}
  
 Finally, the k-th raw moment of X is given by 
  
    
      
        E
        ⁡
        [
        
          X
          
            k
          
        
        ]
        =
        
          
            (
            
              z
              
                
                  ∂
                  
                    ∂
                    z
                  
                
              
            
            )
          
          
            k
          
        
        G
        (
        z
        )
        
          
            
              |
            
          
          
            z
            =
            
              1
              
                −
              
            
          
        
      
    
    {\displaystyle \operatorname {E} [X^{k}]=\left(z{\frac {\partial }{\partial z}}\right)^{k}G(z){\Big |}_{z=1^{-}}}
  

  
    
      
        
          G
          
            X
          
        
        (
        
          e
          
            t
          
        
        )
        =
        
          M
          
            X
          
        
        (
        t
        )
      
    
    {\displaystyle G_{X}(e^{t})=M_{X}(t)}
  
 where X is a random variable, 
  
    
      
        
          G
          
            X
          
        
        (
        t
        )
      
    
    {\displaystyle G_{X}(t)}
  
 is the probability generating function (of 
  
    
      
        X
      
    
    {\displaystyle X}
  
) and 
  
    
      
        
          M
          
            X
          
        
        (
        t
        )
      
    
    {\displaystyle M_{X}(t)}
  
 is the moment-generating function (of 
  
    
      
        X
      
    
    {\displaystyle X}
  
).


=== Functions of independent random variables ===
Probability generating functions are particularly useful for dealing with functions of independent random variables. For example:


== Examples ==
The probability generating function of an almost surely constant random variable, i.e. one with 
  
    
      
        Pr
        (
        X
        =
        c
        )
        =
        1
      
    
    {\displaystyle \Pr(X=c)=1}
  
 and 
  
    
      
        Pr
        (
        X
        ≠
        c
        )
        =
        0
      
    
    {\displaystyle \Pr(X\neq c)=0}
  
 is 
  
    
      
        G
        (
        z
        )
        =
        
          z
          
            c
          
        
        .
      
    
    {\displaystyle G(z)=z^{c}.}
  

The probability generating function of a binomial random variable, the number of successes in 
  
    
      
        n
      
    
    {\displaystyle n}
  
 trials, with probability 
  
    
      
        p
      
    
    {\displaystyle p}
  
 of success in each trial, is 
  
    
      
        G
        (
        z
        )
        =
        
          
            [
            
              (
              1
              −
              p
              )
              +
              p
              z
            
            ]
          
          
            n
          
        
        .
      
    
    {\displaystyle G(z)=\left[(1-p)+pz\right]^{n}.}
  
 Note: it is the 
  
    
      
        n
      
    
    {\displaystyle n}
  
-fold product of the probability generating function of a Bernoulli random variable with parameter 
  
    
      
        p
      
    
    {\displaystyle p}
  
.   So the probability generating function of a fair coin, is 
  
    
      
        G
        (
        z
        )
        =
        
          
            1
            2
          
        
        +
        
          
            z
            2
          
        
        .
      
    
    {\displaystyle G(z)={\frac {1}{2}}+{\frac {z}{2}}.}
  

The probability generating function of a negative binomial random variable on 
  
    
      
        {
        0
        ,
        1
        ,
        2
        ⋯
        }
      
    
    {\displaystyle \{0,1,2\cdots \}}
  
, the number of failures until the 
  
    
      
        
          r
          
            t
            h
          
        
      
    
    {\displaystyle r^{th}}
  
 success with probability of success in each trial 
  
    
      
        p
      
    
    {\displaystyle p}
  
, is 
  
    
      
        G
        (
        z
        )
        =
        
          
            (
            
              
                p
                
                  1
                  −
                  (
                  1
                  −
                  p
                  )
                  z
                
              
            
            )
          
          
            r
          
        
        ,
      
    
    {\displaystyle G(z)=\left({\frac {p}{1-(1-p)z}}\right)^{r},}
  
 which converges for 
  
    
      
        
          |
        
        z
        
          |
        
        <
        
          
            1
            
              1
              −
              p
            
          
        
      
    
    {\displaystyle |z|<{\frac {1}{1-p}}}
  
.  Note that this is the 
  
    
      
        r
      
    
    {\displaystyle r}
  
-fold product of the probability generating function of a geometric random variable with parameter 
  
    
      
        1
        −
        p
      
    
    {\displaystyle 1-p}
  
 on 
  
    
      
        {
        0
        ,
        1
        ,
        2
        ,
        ⋯
        }
      
    
    {\displaystyle \{0,1,2,\cdots \}}
  
.
The probability generating function of a Poisson random variable with rate parameter 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
 is 
  
    
      
        G
        (
        z
        )
        =
        
          e
          
            λ
            (
            z
            −
            1
            )
          
        
        .
      
    
    {\displaystyle G(z)=e^{\lambda (z-1)}.}
  


== Related concepts ==
The probability generating function is an example of a generating function of a sequence: see also formal power series. It is equivalent to, and sometimes called, the z-transform of the probability mass function.
Other generating functions of random variables include the moment-generating function, the characteristic function and the cumulant generating function. The probability generating function is also equivalent to the factorial moment generating function, which as 
  
    
      
        E
        ⁡
        
          [
          
            z
            
              X
            
          
          ]
        
      
    
    {\displaystyle \operatorname {E} \left[z^{X}\right]}
  
 can also be considered for continuous and other random variables.


== Notes ==


== References ==
