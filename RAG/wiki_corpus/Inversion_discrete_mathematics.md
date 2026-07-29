# Inversion (discrete mathematics)

> **Query Topic**: permutation-inversion groups (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 360, Frequency: 17)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)

---

In computer science and discrete mathematics , an inversion in a sequence is a pair of elements that are out of their natural order .

## Definitions

### Inversion

Let $\pi$ be a permutation . 
There is an inversion of $\pi$ between $i$ and $j$ if $i<j$ and $\pi (i)>\pi (j)$ . The inversion is indicated by an ordered pair containing either the places $(i,j)$ or the elements ${\bigl (}\pi (i),\pi (j){\bigr )}$ .

The inversion set is the set of all inversions. A permutation's inversion set using place-based notation is the same as the inverse permutation's inversion set using element-based notation with the two components of each ordered pair exchanged. Likewise, a permutation's inversion set using element-based notation is the same as the inverse permutation's inversion set using place-based notation with the two components of each ordered pair exchanged.

Inversions are usually defined for permutations, but may also be defined for sequences: Let $S$ be a sequence (or multiset permutation ). If $i<j$ and $S(i)>S(j)$ , either the pair of places $(i,j)$ or the pair of elements ${\bigl (}S(i),S(j){\bigr )}$ is called an inversion of $S$ .

For sequences, inversions according to the element-based definition are not unique, because different pairs of places may have the same pair of values.

### Inversion number

The inversion number ${\mathtt {inv}}(X)$ of a sequence $X=\langle x_{1},\dots ,x_{n}\rangle$ , is the cardinality of the inversion set. It is a common measure of sortedness (sometimes called presortedness) of a permutation or sequence. The inversion number is between 0 and ${\frac {n(n-1)}{2}}$ inclusive. A permutation and its inverse have the same inversion number.

For example ${\mathtt {inv}}(\langle 1,2,\dots ,n\rangle )=0$ since the sequence is ordered. Also, when $n=2m$ is even, ${\mathtt {inv}}(\langle m+1,m+2,\dots ,2m,1,2,\dots ,m\rangle )=m^{2}$ (because each pair $(1\leq i\leq m<j\leq 2m)$ is an inversion). This last example shows that a set that is intuitively "nearly sorted" can still have a quadratic number of inversions.

The inversion number is the number of crossings in the arrow diagram of the permutation, the permutation's Kendall tau distance from the identity permutation, and the sum of each of the inversion related vectors defined below.

Other measures of sortedness include the minimum number of elements that can be deleted from the sequence to yield a fully sorted sequence, the number and lengths of sorted "runs" within the sequence, the Spearman footrule (sum of distances of each element from its sorted position), and the smallest number of exchanges needed to sort the sequence. Standard comparison sorting algorithms can be adapted to compute the inversion number in time O( n log n ) .

### Inversion related vectors

Three similar vectors are in use that condense the inversions of a permutation into a vector that uniquely determines it. They are often called inversion vector or Lehmer code . (A list of sources is found here .)

This article uses the term inversion vector ( $v$ ) like Wolfram . The remaining two vectors are sometimes called left and right inversion vector , but to avoid confusion with the inversion vector this article calls them left inversion count ( $l$ ) and right inversion count ( $r$ ). Interpreted as a factorial number the left inversion count gives the permutations reverse colexicographic, and the right inversion count gives the lexicographic index.

Inversion vector $v$ : With the element-based definition $v(i)$ is the number of inversions whose smaller (right) component is $i$ .

$v(i)$ is the number of elements in $\pi$ greater than $i$ before $i$ .

$v(i)~~=~~\#\{k\mid k>i~\land ~\pi ^{-1}(k)<\pi ^{-1}(i)\}$

Left inversion count $l$ : With the place-based definition $l(i)$ is the number of inversions whose bigger (right) component is $i$ .

$l(i)$ is the number of elements in $\pi$ greater than $\pi (i)$ before $\pi (i)$ .

$l(i)~~=~~\#\left\{k\mid k<i~\land ~\pi (k)>\pi (i)\right\}$

Right inversion count $r$ , often called Lehmer code : With the place-based definition $r(i)$ is the number of inversions whose smaller (left) component is $i$ .

$r(i)$ is the number of elements in $\pi$ smaller than $\pi (i)$ after $\pi (i)$ .

$r(i)~~=~~\#\{k\mid k>i~\land ~\pi (k)<\pi (i)\}$

Both $v$ and $r$ can be found with the help of a Rothe diagram , which is a permutation matrix with the 1s represented by dots, and an inversion (often represented by a cross) in every position that has a dot to the right and below it. $r(i)$ is the sum of inversions in row $i$ of the Rothe diagram, while $v(i)$ is the sum of inversions in column $i$ . The permutation matrix of the inverse is the transpose , therefore $v$ of a permutation is $r$ of its inverse, and vice versa.

## Example: All permutations of four elements

The following sortable table shows the 24 permutations of four elements (in the $\pi$ column) with their place-based inversion sets (in the p-b column), inversion related vectors (in the $v$ , $l$ , and $r$ columns), and inversion numbers (in the # column). (The columns with smaller print and no heading are reflections of the columns next to them, and can be used to sort them in colexicographic order .)

It can be seen that $v$ and $l$ always have the same digits, and that $l$ and $r$ are both related to the place-based inversion set. The nontrivial elements of $l$ are the sums of the descending diagonals of the shown triangle, and those of $r$ are the sums of the ascending diagonals. (Pairs in descending diagonals have the right components 2, 3, 4 in common, while pairs in ascending diagonals have the left components 1, 2, 3 in common.)

The default order of the table is reverse colex order by $\pi$ , which is the same as colex order by $l$ . Lex order by $\pi$ is the same as lex order by $r$ .

## Weak order of permutations

The set of permutations on n items can be given the structure of a partial order , called the weak order of permutations , which forms a lattice .

The Hasse diagram of the inversion sets ordered by the subset relation forms the skeleton of a permutohedron .

If a permutation is assigned to each inversion set using the place-based definition, the resulting order of permutations is that of the permutohedron, where an edge corresponds to the swapping of two elements with consecutive values. This is the weak order of permutations. The identity is its minimum, and the permutation formed by reversing the identity is its maximum.

If a permutation were assigned to each inversion set using the element-based definition, the resulting order of permutations would be that of a Cayley graph , where an edge corresponds to the swapping of two elements on consecutive places. This Cayley graph of the symmetric group is similar to its permutohedron, but with each permutation replaced by its inverse.
