# Parity of a permutation

> **Query Topic**: permutation-inversion groups (Rank #2 Search Result)  
> **Source Queue**: train (Row ID: 43, Frequency: 17)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Parity_of_a_permutation

---

In mathematics, when X is a finite set with at least two elements, the permutations of X (i.e. the bijective functions from X to X) fall into two classes of equal size: the even permutations and the odd permutations. If any total ordering of X is fixed, the parity (oddness or evenness) of a permutation 
  
    
      
        σ
      
    
    {\displaystyle \sigma }
  
 of X can be defined as the parity of the number of inversions for σ, i.e., of pairs of elements x, y of X such that x < y and σ(x) > σ(y).
The sign, signature, or signum of a permutation σ is denoted sgn(σ) and defined as +1 if σ is even and −1 if σ is odd. The signature defines the alternating character of the symmetric group Sn. Another notation for the sign of a permutation is given by the more general Levi-Civita symbol (εσ), which is defined for all maps from X to X, and has value zero for  non-bijective maps.
The sign of a permutation can be explicitly expressed as

sgn(σ) = (−1)N(σ)
where N(σ) is the number of inversions in σ.
Alternatively, the sign of a permutation σ can be defined from its decomposition into the product of transpositions as

sgn(σ) = (−1)m
where m is the number of transpositions in the decomposition. Although such a decomposition is not unique, the parity of the number of transpositions in all decompositions is the same, implying that the sign of a permutation is well-defined.


== Example ==
Consider the permutation σ of the set {1, 2, 3, 4, 5} defined by 
  
    
      
        σ
        (
        1
        )
        =
        3
        ,
      
    
    {\displaystyle \sigma (1)=3,}
  
 
  
    
      
        σ
        (
        2
        )
        =
        4
        ,
      
    
    {\displaystyle \sigma (2)=4,}
  
 
  
    
      
        σ
        (
        3
        )
        =
        5
        ,
      
    
    {\displaystyle \sigma (3)=5,}
  
 
  
    
      
        σ
        (
        4
        )
        =
        2
        ,
      
    
    {\displaystyle \sigma (4)=2,}
  
 and 
  
    
      
        σ
        (
        5
        )
        =
        1.
      
    
    {\displaystyle \sigma (5)=1.}
  
  In one-line notation, this permutation is denoted 34521.  It can be obtained from the identity permutation 12345 by three transpositions: first exchange the numbers 2 and 4, then exchange 3 and 5, and finally exchange 1 and 3. This shows that the given permutation σ is odd. Following the method of the cycle notation article, this could be written, composing from right to left, as

  
    
      
        σ
        =
        
          
            (
            
              
                
                  1
                
                
                  2
                
                
                  3
                
                
                  4
                
                
                  5
                
              
              
                
                  3
                
                
                  4
                
                
                  5
                
                
                  2
                
                
                  1
                
              
            
            )
          
        
        =
        
          
            (
            
              
                
                  1
                
                
                  3
                
                
                  5
                
              
            
            )
          
        
        
          
            (
            
              
                
                  2
                
                
                  4
                
              
            
            )
          
        
        =
        
          
            (
            
              
                
                  1
                
                
                  3
                
              
            
            )
          
        
        
          
            (
            
              
                
                  3
                
                
                  5
                
              
            
            )
          
        
        
          
            (
            
              
                
                  2
                
                
                  4
                
              
            
            )
          
        
        .
      
    
    {\displaystyle \sigma ={\begin{pmatrix}1&2&3&4&5\\3&4&5&2&1\end{pmatrix}}={\begin{pmatrix}1&3&5\end{pmatrix}}{\begin{pmatrix}2&4\end{pmatrix}}={\begin{pmatrix}1&3\end{pmatrix}}{\begin{pmatrix}3&5\end{pmatrix}}{\begin{pmatrix}2&4\end{pmatrix}}.}
  

There are many other ways of writing σ as a composition of transpositions, for instance

σ = (1 5)(3 4)(2 4)(1 2)(2 3),
but it is impossible to write it as a product of an even number of transpositions.


== Properties ==
The identity permutation is an even permutation. An even permutation can be obtained as the composition of an even number (and only an even number) of exchanges (called transpositions) of two elements, while an odd permutation can be obtained by (only) an odd number of transpositions.
The following rules follow directly from the corresponding rules about addition of integers:

the composition of two even permutations is even
the composition of two odd permutations is even
the composition of an odd and an even permutation is odd
From these it follows that

the inverse of every even permutation is even
the inverse of every odd permutation is odd
Considering the symmetric group Sn of all permutations of the set {1, ..., n}, we can conclude that the map

sgn: Sn → {−1, 1} 
that assigns to every permutation its signature is a group homomorphism.
Furthermore, we see that the even permutations form a subgroup of Sn. This is the alternating group on n letters, denoted by An. It is the kernel of the homomorphism sgn. The odd permutations cannot form a subgroup, since the composite of two odd permutations is even, but they form a coset of An (in Sn).
If n > 1, then there are just as many even permutations in Sn as there are odd ones; consequently, An contains n!/2 permutations. (The reason is that if σ is even then (1  2)σ is odd, and if σ is odd then (1  2)σ is even, and these two maps are inverse to each other.)
A cycle is even if and only if its length is odd. This follows from formulas like

  
    
      
        (
        a
         
        b
         
        c
         
        d
         
        e
        )
        =
        (
        d
         
        e
        )
        (
        c
         
        e
        )
        (
        b
         
        e
        )
        (
        a
         
        e
        )
        
           or 
        
        (
        a
         
        b
        )
        (
        b
         
        c
        )
        (
        c
         
        d
        )
        (
        d
         
        e
        )
        .
      
    
    {\displaystyle (a\ b\ c\ d\ e)=(d\ e)(c\ e)(b\ e)(a\ e){\text{ or }}(a\ b)(b\ c)(c\ d)(d\ e).}
  

In practice, in order to determine whether a given permutation is even or odd, one writes the permutation as a product of disjoint cycles. The permutation is odd if and only if this factorization contains an odd number of even-length cycles.
Another method for determining whether a given permutation is even or odd is to construct the corresponding permutation matrix and compute its determinant. The value of the determinant is the same as the parity of the permutation.
Every permutation of odd order must be even. The permutation (1 2)(3 4) in A4 shows that the converse is not true in general.


== Equivalence of the two definitions ==
This section presents proofs that the parity of a permutation σ can be defined in two equivalent ways:

as the parity of the number of inversions in σ (under any ordering); or
as the parity of the number of transpositions that σ can be decomposed to (however we choose to decompose it).


== Other definitions and proofs ==
The parity of a permutation of 
  
    
      
        n
      
    
    {\displaystyle n}
  
 points is also encoded in its cycle structure.
Let σ = (i1 i2 ... ir+1)(j1 j2 ... js+1)...(ℓ1 ℓ2 ... ℓu+1) be the unique decomposition of σ into disjoint cycles, which can be composed in any order because they commute. A cycle (a b c ... x y z) involving k + 1 points can always be obtained by composing k transpositions (2-cycles):

  
    
      
        (
        a
         
        b
         
        c
        …
        x
         
        y
         
        z
        )
        =
        (
        a
         
        b
        )
        (
        b
         
        c
        )
        …
        (
        x
         
        y
        )
        (
        y
         
        z
        )
        ,
      
    
    {\displaystyle (a\ b\ c\dots x\ y\ z)=(a\ b)(b\ c)\dots (x\ y)(y\ z),}
  

so call k the size of the cycle, and observe that, under this definition, transpositions are cycles of size 1. From a decomposition into m disjoint cycles we can obtain a decomposition of σ into k1 + k2 + ... + km transpositions, where ki is the size of the ith cycle. The number N(σ) = k1 + k2 + ... + km is called the discriminant of σ, and can also be computed as

  
    
      
        n
        
           minus the number of disjoint cycles in the decomposition of 
        
        σ
      
    
    {\displaystyle n{\text{ minus the number of disjoint cycles in the decomposition of }}\sigma }
  

if we take care to include the fixed points of σ as 1-cycles.
Suppose a transposition (a b) is applied after a permutation σ. When a and b are in different cycles of σ then

  
    
      
        (
        a
         
        b
        )
        (
        a
         
        
          c
          
            1
          
        
         
        
          c
          
            2
          
        
        …
        
          c
          
            r
          
        
        )
        (
        b
         
        
          d
          
            1
          
        
         
        
          d
          
            2
          
        
        …
        
          d
          
            s
          
        
        )
        =
        (
        a
         
        
          c
          
            1
          
        
         
        
          c
          
            2
          
        
        …
        
          c
          
            r
          
        
         
        b
         
        
          d
          
            1
          
        
         
        
          d
          
            2
          
        
        …
        
          d
          
            s
          
        
        )
      
    
    {\displaystyle (a\ b)(a\ c_{1}\ c_{2}\dots c_{r})(b\ d_{1}\ d_{2}\dots d_{s})=(a\ c_{1}\ c_{2}\dots c_{r}\ b\ d_{1}\ d_{2}\dots d_{s})}
  
,
and if a and b are in the same cycle of σ then

  
    
      
        (
        a
         
        b
        )
        (
        a
        
          c
          
            1
          
        
        
          c
          
            2
          
        
        …
        
          c
          
            r
          
        
         
        b
         
        
          d
          
            1
          
        
         
        
          d
          
            2
          
        
        …
        
          d
          
            s
          
        
        )
        =
        (
        a
         
        
          c
          
            1
          
        
         
        
          c
          
            2
          
        
        …
        
          c
          
            r
          
        
        )
        (
        b
         
        
          d
          
            1
          
        
         
        
          d
          
            2
          
        
        …
        
          d
          
            s
          
        
        )
      
    
    {\displaystyle (a\ b)(ac_{1}c_{2}\dots c_{r}\ b\ d_{1}\ d_{2}\dots d_{s})=(a\ c_{1}\ c_{2}\dots c_{r})(b\ d_{1}\ d_{2}\dots d_{s})}
  
.
In either case, it can be seen that N((a b)σ) = N(σ) ± 1, so the parity of N((a b)σ) will be different from the parity of N(σ).
If σ = t1t2 ... tr is an arbitrary decomposition of a permutation σ into transpositions, by applying the r transpositions 
  
    
      
        
          t
          
            1
          
        
      
    
    {\displaystyle t_{1}}
  
 after t2 after ... after tr after the identity (whose N is zero) observe that N(σ) and r have the same parity. By defining the parity of σ as the parity of N(σ), a permutation that has an even length decomposition is an even permutation and a permutation that has one odd length decomposition is an odd permutation.

Remarks

A careful examination of the above argument shows that r ≥ N(σ), and since any decomposition of σ into cycles whose sizes sum to r can be expressed as a composition of r transpositions, the number N(σ) is the minimum possible sum of the sizes of the cycles in a decomposition of σ, including the cases in which all cycles are transpositions.
This proof does not introduce a (possibly arbitrary) order into the set of points on which σ acts.


== Generalizations ==
Parity can be generalized to Coxeter groups: one defines a length function ℓ(v), which depends on a choice of generators (for the symmetric group, adjacent transpositions), and then the function v ↦ (−1)ℓ(v) gives a generalized sign map.


== See also ==
The fifteen puzzle is a classic application
Zolotarev's lemma


== Notes ==


== References ==
Weisstein, Eric W. "Even Permutation". MathWorld.
Jacobson, Nathan (2009). Basic algebra. Vol. 1 (2nd ed.). Dover. ISBN 978-0-486-47189-1.
Rotman, J.J. (1995). An introduction to the theory of groups. Graduate texts in mathematics. Springer-Verlag. ISBN 978-0-387-94285-8.
Goodman, Frederick M. Algebra: Abstract and Concrete. ISBN 978-0-9799142-0-1.
Meijer, Paul Herman Ernst; Bauer, Edmond (2004). Group theory: the application to quantum mechanics. Dover classics of science and mathematics. Dover Publications. ISBN 978-0-486-43798-9.
