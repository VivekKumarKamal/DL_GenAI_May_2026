# Parity of a permutation

> **Query Topic**: permutation-inversion groups (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 360, Frequency: 17)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Parity_of_a_permutation

---

In mathematics , when X is a finite set with at least two elements, the permutations of X (i.e. the bijective functions from X to X ) fall into two classes of equal size: the even permutations and the odd permutations . If any total ordering of X is fixed, the parity ( oddness or evenness ) of a permutation $\sigma$ of X can be defined as the parity of the number of inversions for σ , i.e., of pairs of elements x , y of X such that x < y and σ ( x ) > σ ( y ) .

The sign , signature , or signum of a permutation σ is denoted sgn( σ ) and defined as +1 if σ is even and − 1 if σ is odd. The signature defines the alternating character of the symmetric group S n . Another notation for the sign of a permutation is given by the more general Levi-Civita symbol ( ε σ ), which is defined for all maps from X to X , and has value zero for non-bijective maps .

The sign of a permutation can be explicitly expressed as

sgn( σ ) = (−1) N ( σ )

where N ( σ ) is the number of inversions in σ .

Alternatively, the sign of a permutation σ can be defined from its decomposition into the product of transpositions as

sgn( σ ) = (−1) m

where m is the number of transpositions in the decomposition. Although such a decomposition is not unique, the parity of the number of transpositions in all decompositions is the same, implying that the sign of a permutation is well-defined .

## Example

Consider the permutation σ of the set {1, 2, 3, 4, 5} defined by $\sigma (1)=3,$ $\sigma (2)=4,$ $\sigma (3)=5,$ $\sigma (4)=2,$ and $\sigma (5)=1.$ In one-line notation , this permutation is denoted 34521. It can be obtained from the identity permutation 12345 by three transpositions: first exchange the numbers 2 and 4, then exchange 3 and 5, and finally exchange 1 and 3. This shows that the given permutation σ is odd. Following the method of the cycle notation article, this could be written, composing from right to left, as

$\sigma ={\begin{pmatrix}1&2&3&4&5\\3&4&5&2&1\end{pmatrix}}={\begin{pmatrix}1&3&5\end{pmatrix}}{\begin{pmatrix}2&4\end{pmatrix}}={\begin{pmatrix}1&3\end{pmatrix}}{\begin{pmatrix}3&5\end{pmatrix}}{\begin{pmatrix}2&4\end{pmatrix}}.$

There are many other ways of writing σ as a composition of transpositions, for instance

σ = (1 5)(3 4)(2 4)(1 2)(2 3) ,

but it is impossible to write it as a product of an even number of transpositions.

## Properties

The identity permutation is an even permutation. An even permutation can be obtained as the composition of an even number (and only an even number) of exchanges (called transpositions ) of two elements, while an odd permutation can be obtained by (only) an odd number of transpositions.

The following rules follow directly from the corresponding rules about addition of integers:

- the composition of two even permutations is even

- the composition of two odd permutations is even

- the composition of an odd and an even permutation is odd

From these it follows that

- the inverse of every even permutation is even

- the inverse of every odd permutation is odd

Considering the symmetric group S n of all permutations of the set {1, ..., n }, we can conclude that the map

sgn: S n → {−1, 1}

that assigns to every permutation its signature is a group homomorphism .

Furthermore, we see that the even permutations form a subgroup of S n . This is the alternating group on n letters, denoted by A n . It is the kernel of the homomorphism sgn. The odd permutations cannot form a subgroup, since the composite of two odd permutations is even, but they form a coset of A n (in S n ).

If n > 1 , then there are just as many even permutations in S n as there are odd ones; consequently, A n contains n ! /2 permutations. (The reason is that if σ is even then (1  2) σ is odd, and if σ is odd then (1  2) σ is even, and these two maps are inverse to each other.)

A cycle is even if and only if its length is odd. This follows from formulas like

$(a\ b\ c\ d\ e)=(d\ e)(c\ e)(b\ e)(a\ e){\text{ or }}(a\ b)(b\ c)(c\ d)(d\ e).$

In practice, in order to determine whether a given permutation is even or odd, one writes the permutation as a product of disjoint cycles. The permutation is odd if and only if this factorization contains an odd number of even-length cycles.

Another method for determining whether a given permutation is even or odd is to construct the corresponding permutation matrix and compute its determinant . The value of the determinant is the same as the parity of the permutation.

Every permutation of odd order must be even. The permutation (1 2)(3 4) in A 4 shows that the converse is not true in general.

## Equivalence of the two definitions

This section presents proofs that the parity of a permutation σ can be defined in two equivalent ways:

- as the parity of the number of inversions in σ (under any ordering); or

- as the parity of the number of transpositions that σ can be decomposed to (however we choose to decompose it).

Let σ be a permutation on a ranked domain S . Every permutation can be produced by a sequence of transpositions (2-element exchanges). Let the following be one such decomposition

σ = T 1 T 2 ... T k

We want to show that the parity of k is equal to the parity of the number of inversions of σ .

Every transposition can be written as a product of an odd number of transpositions of adjacent elements, e.g.

(2 5) = (2 3) (3 4) (4 5) (4 3) (3 2).

Generally, we can write the transposition ( i i+d ) on the set {1,..., i ,..., i+d ,...} as the composition of 2 d −1 adjacent transpositions by recursion on d :

- The base case d=1 is trivial.

- In the recursive case, first rewrite ( i , i+d ) as ( i , i +1) ( i +1, i+d ) ( i , i +1). Then recursively rewrite ( i +1, i+d ) as adjacent transpositions.

If we decompose in this way each of the transpositions T 1 ... T k above, we get the new decomposition:

σ = A 1 A 2 ... A m

where all of the A 1 ... A m are adjacent. Also, the parity of m is the same as that of k .

This is a fact: for all permutation τ and adjacent transposition a, aτ either has one less or one more inversion than τ . In other words, the parity of the number of inversions of a permutation is switched when composed with an adjacent transposition.

Therefore, the parity of the number of inversions of σ is precisely the parity of m , which is also the parity of k . This is what we set out to prove.

An alternative proof uses the Vandermonde polynomial

$P(x_{1},\ldots ,x_{n})=\prod _{i<j}(x_{i}-x_{j}).$

So for instance in the case n = 3 , we have

$P(x_{1},x_{2},x_{3})=(x_{1}-x_{2})(x_{2}-x_{3})(x_{1}-x_{3}).$

Now for a given permutation σ of the numbers {1, ..., n }, we define

$\operatorname {sgn}(\sigma )={\frac {P(x_{\sigma (1)},\ldots ,x_{\sigma (n)})}{P(x_{1},\ldots ,x_{n})}}.$

Since the polynomial $P(x_{\sigma (1)},\dots ,x_{\sigma (n)})$ has the same factors as $P(x_{1},\dots ,x_{n})$ except for their signs, it follows that sgn( σ ) is either +1 or − 1. Furthermore, if σ and τ are two permutations, we see that

${\begin{aligned}\operatorname {sgn}(\sigma \tau )&={\frac {P(x_{\sigma (\tau (1))},\ldots ,x_{\sigma (\tau (n))})}{P(x_{1},\ldots ,x_{n})}}\\[4pt]&={\frac {P(x_{\tau (1)},\ldots ,x_{\tau (n)})}{P(x_{1},\ldots ,x_{n})}}\cdot {\frac {P(x_{\sigma (\tau (1))},\ldots ,x_{\sigma (\tau (n))})}{P(x_{\tau (1)},\ldots ,x_{\tau (n)})}}\\[4pt]&=\operatorname {sgn}(\sigma )\cdot \operatorname {sgn}(\tau ).\end{aligned}}$

A third approach uses the presentation of the group S n in terms of generators τ 1 , ..., τ n − 1 and relations

- $\tau _{i}^{2}=1$ for all i

- $\tau _{i}^{}\tau _{i+1}\tau _{i}=\tau _{i+1}\tau _{i}\tau _{i+1}$ for all i < n − 1

- $\tau _{i}^{}\tau _{j}=\tau _{j}\tau _{i}$ if $|i-j|\geq 2.$

Recall that a pair x , y such that x < y and σ ( x ) > σ ( y ) is called an inversion. We want to show that the count of inversions has the same parity as the count of 2-element swaps. To do that, we can show that every swap changes the parity of the count of inversions, no matter which two elements are being swapped and what permutation has already been applied. 
Suppose we want to swap the i th and the j th element. Clearly, inversions formed by i or j with an element outside of [ i , j ] will not be affected. 
For the n = j − i − 1 elements within the interval ( i , j ) , assume v i of them form inversions with i and v j of them form inversions with j . If i and j are swapped, those v i inversions with i are gone, but n − v i inversions are formed. The count of inversions i gained is thus n − 2 v i , which has the same parity as n .

Similarly, the count of inversions j gained also has the same parity as n . Therefore, the count of inversions gained by both combined has the same parity as 2 n or 0. Now if we count the inversions gained (or lost) by swapping the i th and the j th element, we can see that this swap changes the parity of the count of inversions, since we also add (or subtract) 1 to the number of inversions gained (or lost) for the pair (i,j) .

Consider the elements that are sandwiched by the two elements of a transposition. Each one lies completely above, completely below, or in between the two transposition elements.

An element that is either completely above or completely below contributes nothing to the inversion count when the transposition is applied. Elements in-between contribute $\pm 2$ .

## Other definitions and proofs

The parity of a permutation of $n$ points is also encoded in its cycle structure .

Let σ = ( i 1 i 2 ... i r +1 )( j 1 j 2 ... j s +1 )...( ℓ 1 ℓ 2 ... ℓ u +1 ) be the unique decomposition of σ into disjoint cycles , which can be composed in any order because they commute. A cycle ( a b c ... x y z ) involving k + 1 points can always be obtained by composing k transpositions (2-cycles):

$(a\ b\ c\dots x\ y\ z)=(a\ b)(b\ c)\dots (x\ y)(y\ z),$

so call k the size of the cycle, and observe that, under this definition, transpositions are cycles of size 1. From a decomposition into m disjoint cycles we can obtain a decomposition of σ into k 1 + k 2 + ... + k m transpositions, where k i is the size of the i th cycle. The number N ( σ ) = k 1 + k 2 + ... + k m is called the discriminant of σ , and can also be computed as

$n{\text{ minus the number of disjoint cycles in the decomposition of }}\sigma$

if we take care to include the fixed points of σ as 1-cycles.

Suppose a transposition ( a b ) is applied after a permutation σ . When a and b are in different cycles of σ then

$(a\ b)(a\ c_{1}\ c_{2}\dots c_{r})(b\ d_{1}\ d_{2}\dots d_{s})=(a\ c_{1}\ c_{2}\dots c_{r}\ b\ d_{1}\ d_{2}\dots d_{s})$ ,

and if a and b are in the same cycle of σ then

$(a\ b)(ac_{1}c_{2}\dots c_{r}\ b\ d_{1}\ d_{2}\dots d_{s})=(a\ c_{1}\ c_{2}\dots c_{r})(b\ d_{1}\ d_{2}\dots d_{s})$ .

In either case, it can be seen that N (( a b ) σ ) = N ( σ ) ± 1 , so the parity of N (( a b ) σ ) will be different from the parity of N ( σ ).

If σ = t 1 t 2 ... t r is an arbitrary decomposition of a permutation σ into transpositions, by applying the r transpositions $t_{1}$ after t 2 after ... after t r after the identity (whose N is zero) observe that N ( σ ) and r have the same parity. By defining the parity of σ as the parity of N ( σ ), a permutation that has an even length decomposition is an even permutation and a permutation that has one odd length decomposition is an odd permutation.

- A careful examination of the above argument shows that r ≥ N ( σ ) , and since any decomposition of σ into cycles whose sizes sum to r can be expressed as a composition of r transpositions, the number N ( σ ) is the minimum possible sum of the sizes of the cycles in a decomposition of σ , including the cases in which all cycles are transpositions.

- This proof does not introduce a (possibly arbitrary) order into the set of points on which σ acts.

## Generalizations

Parity can be generalized to Coxeter groups : one defines a length function ℓ( v ), which depends on a choice of generators (for the symmetric group, adjacent transpositions ), and then the function v ↦ ( − 1) ℓ( v ) gives a generalized sign map.
