# Mohr–Mascheroni theorem

> **Query Topic**: Mohr's theorem (Rank #2 Search Result)
> **Source Queue**: train (Row ID: 55, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Mohr–Mascheroni_theorem

---

In Euclidean geometry, the Mohr–Mascheroni theorem states that any geometric construction that can be performed by a compass and straightedge can be performed by a compass alone.
This theorem refers to geometric constructions which only involve points and circles, since it is not possible to draw straight lines without a straightedge. However, a line is considered to be determined if two distinct points on that line are given or constructed, even if the line itself is not drawn.
Although the use of a straightedge can make certain constructions significantly easier, the theorem shows that these constructions are possible even without the use of it. This means the only use of a straightedge is for the aesthetics of drawing straight lines, and is functionally unnecessary for the purposes of construction.


== History ==
The result was originally published by Georg Mohr in 1672, but his proof languished in obscurity until 1928.  The theorem was independently discovered by Lorenzo Mascheroni in 1797 and it was known as Mascheroni's Theorem until Mohr's work was rediscovered.
Several proofs of the result are known. Mascheroni's proof of 1797 was generally based on the idea of using reflection in a line as the major tool. Mohr's solution was different. In 1890, August Adler published a proof using the inversion transformation.
An algebraic approach uses the isomorphism between the Euclidean plane and the real coordinate space 
  
    
      
        
          
            R
          
          
            2
          
        
      
    
    {\displaystyle \mathbb {R} ^{2}}
  
. In this way, a stronger version of the theorem was proven in 1990. It also shows the dependence of the theorem on Archimedes' axiom (which cannot be formulated in a first-order language).


== Constructive proof ==


=== Outline ===
To prove the Mohr–Mascheroni theorem, it suffices to show that each of the basic constructions of compass and straightedge is possible using a compass alone, as these are the foundations of all other constructions. All constructions can be written as a series of steps involving these five basic constructions:

Creating the line through two existing points
Creating the circle through one point with centre another point
Creating the point which is the intersection of two existing, non-parallel lines
Creating the one or two points in the intersection of a line and a circle (if they intersect)
Creating the one or two points in the intersection of two circles (if they intersect).
Constructions (2) and (5) can be done with a compass alone. For construction (1), a line is considered to be given by any two points. It is understood that the line itself cannot be drawn without a straightedge, so the proof of the theorem lies in showing that constructions (3) and (4) are possible using only a compass. Once this is done, it follows that every compass-straightedge construction can be done under the restrictions of the theorem.


=== Notation ===
The following notation will be used throughout this article. A circle whose center is located at point U and that passes through point V will be denoted by U(V). A circle with center U and radius specified by a number, r, or a line segment AB will be denoted by U(r) or U(AB), respectively.


=== Some preliminary constructions ===
To prove the above constructions (3) and (4), a few necessary intermediary constructions are also explained below since they are used and referenced frequently. These are also compass-only constructions.


==== Compass equivalence theorem (circle translation) ====

The modern compass with its fixable (non-collapsing) aperture can be used to transfer distances directly, while a  collapsing compass cannot. The compass equivalence theorem states that, while a "modern compass" appears to be a more powerful instrument, it can be simulated with a collapsing compass alone. This justifies the use of "fixed compass" moves (constructing a circle of a given radius at a different location) for the proof of this theorem.
Given points A, B, and C, construct a circle centered at A with the radius BC, using only a collapsing compass.

Draw a circle centered at A and passing through B and vice versa (the blue circles). They will intersect at points D and D'.
Draw circles through C with centers at D and D' (the red circles). Label their other intersection E.
Draw a circle (the green circle) with center A passing through E. This is the required circle.


==== Reflecting a point across a line ====

Given a line AB determined by two points A and B, and an arbitrary point C, construct the image of C upon reflection across this line:

Construct two circles: one centered at A and one centered at B, both passing through C.
The other point of intersection of the two circles, D, is the reflection of C across the line AB.
If C = D (that is, there is a unique point of intersection of the two circles), then C is its own reflection and lies on the line AB.


==== Extending the length of a line segment ====

Given a line AB determined by two points A and B, construct the point C on the line such that B is the midpoint of line segment AC.

Construct point D as the intersection of circles A(B) and B(A). (∆ABD is an equilateral triangle.)
Construct point E ≠ A as the intersection of circles D(B) and B(D). (∆DBE is an equilateral triangle.)
Finally, construct point C ≠ D as the intersection of circles B(E) and E(B). (∆EBC is an equilateral triangle, and the three angles at B show that A, B and C are collinear.)
This construction can be repeated as often as necessary to find a point Q so that the length of line segment AQ is n times the length of line segment AB for any positive integer n.


==== Inversion in a circle ====

Given a circle B(r), for some radius r (in black) and a point D (≠ B), construct the point I that is the inverse of D about the circle. Naturally there is no inversion for a point D = B.

Draw a circle D(B) (in red).
Assume that the red circle intersects the black circle at E and E'
If the circles do not intersect in two points, see below for an alternative construction.
If the circles intersect in only one point, E = E' , it is possible to invert 
  
    
      
        D
      
    
    {\displaystyle D}
  
 simply by doubling the length of EB (quadrupling the length of DB).
Reflect the circle center B across the line EE' :
Construct two new circles E(B) and E' (B) (in light blue).
The light blue circles intersect at B and at another point I ≠ B.
Point I is the desired inverse of D in the black circle.
This point I lies on line DB and satisfies DB · IB = r2.
In the event that the above construction fails (that is, the red circle and the black circle do not intersect in two points), find a point Q on the line BD so that the length of line segment BQ is a positive integral multiple, say n, of the length of BD and is greater than r/2. Find Q' the inverse of Q in circle B(r) as above (the red and black circles must now intersect in two points). The point I is now obtained by extending BQ'  so that BI = n ⋅ BQ' .
The existence of such an integer n relies on Archimedes' axiom. As a result, this construction may require an unbounded number of iterations depending on the ratio of r to BD.


==== Determining the center of a circle through three points ====

Given three non-collinear points A, B and C, construct the center O of the circle they determine.

Construct point D, the inverse of C in the circle A(B).
Reflect A in the line BD to the point X.
O is the inverse of X in the circle A(B).


=== Intersection of two non-parallel lines ===

The third basic construction concerns the intersection of two non-parallel lines.
Given non-parallel lines AB and CD determined by points A, B, C, D, construct their point of intersection, X.

Select circle O(r) of arbitrary radius whose center O does not lie on either line.
Invert points A and B in circle O(r) to points A' and B' respectively.
The line AB is inverted to the circle passing through O, A' and B'. Find the center E of this circle.
Invert points C and D in circle O(r) to points C' and D' respectively.
The line CD is inverted to the circle passing through O, C' and D'. Find the center F of this circle.
Let Y ≠ O be the intersection of circles E(O) and F(O).
X is the inverse of Y in the circle O(r).


=== Intersection of a line and a circle ===
The fourth basic construction concerns the intersection of a line and a circle. The construction below breaks into two cases depending upon whether the center of the circle is or is not collinear with the line.


==== Circle center is not collinear with the line ====
Assume that center of the circle does not lie on the line.

Given a circle C(r) (in black) and a line AB, construct the points of intersection, P and Q, between them (if they exist).

Construct the point D, which is the reflection of point C across line AB. (See above.)
Under the assumption of this case, C ≠ D.
If in fact C = D then this construction will fail, and we have verification of collinearity.
Construct a circle D(r) (in red). (See above, compass equivalence.)
The intersections of circle C(r) and the new red circle D(r) are points P and Q.
If the two circles are (externally) tangential then P = Q.
If the two circles do not intersect then neither does the circle with the line.
Points P and Q are the intersection points of circle C(r) and the line AB.
If P = Q then the line is tangential to the circle C(r).
An alternate construction, using circle inversion can also be given.

Invert points A and B in circle C(r) to points A' and B' respectively.
Under the assumption of this case, points A', B', and C are not collinear.
Find the center E of the circle passing through points C, A', and B'.
Construct circle E(C), which represents the inversion of the line AB into circle C(r).
P and Q are the intersection points of circles C(r) and E(C).
If the two circles are (internally) tangential then P = Q, and the line is also tangential.


==== Circle center is collinear with the line ====

Given the circle C(r) whose center C lies on the line AB, construct the points P and Q, the intersection points of the circle and the line.

Choose an arbitrary point D on the circle.
Construct point D'  as the reflection of D across line AB.
Construct point F as the intersection of circles C(DD' ) and D(C). (F is the fourth vertex of parallelogram CD'DF.)
Construct point F' as the intersection of circles C(DD' ) and D' (C). (F' is the fourth vertex of parallelogram CDD'F'.)
Construct point M as an intersection of circles F(D' ) and F' (D). (M lies on AB.)
Points P and Q are the intersections of circles F(CM) and C(D).


=== Conclusion ===
Since all five basic constructions have been shown to be achievable with only a compass, this proves the Mohr–Mascheroni theorem. Any compass-straightedge construction may be achieved with the compass alone by describing their constructive steps in terms of the five basic constructions.


== Validity of the theorem ==
Dono Kijne points out that the Mohr–Mascheroni theorem fundamentally relies on Archimedes' axiom. As a result, any proof of Mohr–Mascheroni theorem must inherently involve an unbounded number of steps. This raises some questions about what constitutes a valid geometric construction.
Most geometric constructions can be thought of as "straight-line programs", a list of elementary instructions with a fixed number of steps. Under this model, the Mohr–Mascheroni theorem would not qualify as a valid result because it has no a priori bound on the number of iterations required.
To address this, Erwin Engeler suggested that geometric constructions be defined as "programs with loops", a list of instructions that allow conditionals and control flow. This saves the Mohr–Mascheroni theorem, but introduces new issues:
For example, consider straightedge-only constructions within the rational plane 
  
    
      
        
          
            Q
          
          
            2
          
        
      
    
    {\displaystyle \mathbb {Q} ^{2}}
  
. If we allow an unbounded number of steps, then given any four points 
  
    
      
        A
        ,
        B
        ,
        C
        ,
        D
        ∈
        
          
            Q
          
          
            2
          
        
      
    
    {\displaystyle A,B,C,D\in \mathbb {Q} ^{2}}
  
 in general position, we can enumerate all rational points and lines in 
  
    
      
        
          
            Q
          
          
            2
          
        
      
    
    {\displaystyle \mathbb {Q} ^{2}}
  
. By simply "waiting" for a line parallel to AB to appear, that line can then be used to construct the midpoint of AB. This construction does not look like an intuitively valid construction and contradicts the belief that constructing the midpoint using a straightedge is impossible.


== Other types of restricted construction ==


=== Restrictions involving the compass ===
Renaissance mathematicians Lodovico Ferrari, Gerolamo Cardano and Niccolò Fontana Tartaglia and others were able to show in the 16th century that any ruler-and-compass construction could be accomplished with a straightedge and a fixed-width compass (i.e. a rusty compass).
The compass equivalence theorem shows that in any construction, a rigid compass, which preserves distances, may be replaced with a collapsible compass, which does not preserve distances. It is possible to translate any circle in the plane with a collapsing compass using no more than three uses of the compass than with a rigid compass. In fact, Euclid's original constructions use a collapsible compass.


=== Restrictions excluding the compass ===

Motivated by Mascheroni's result, in 1822 Jean Victor Poncelet conjectured a variation on the same theme. His work paved the way for the field of projective geometry, wherein he proposed that any construction possible by straightedge and compass could be done with straightedge alone.  However, the one stipulation is that no less than a single circle with its center identified must be provided. This statement, now known as the Poncelet–Steiner theorem, was proved by Jakob Steiner eleven years later.


== Further generalizations ==
The Mohr–Mascheroni theorem has been generalized to higher dimensions, such as, for example, a three-dimensional variation where the straightedge is replaced with a plane, and the compass is replaced with a sphere. It has been shown that n-dimensional "straightedge and compass" constructions can still be performed even with just an ordinary two-dimensional compass.
Additionally, some research is underway to generalize the Mohr–Mascheroni theorem to non-Euclidean geometries.


== See also ==
Napoleon's problem
Geometrography
Inversive geometry
Projective geometry


== Notes ==


== References ==
Eves, Howard (1963), A Survey of Geometry (Volume One), Allyn and Bacon
Hungerbühler, Norbert (1994), "A Short Elementary Proof of the Mohr–Mascheroni Theorem", The American Mathematical Monthly, 101 (8): 784–787, doi:10.1080/00029890.1994.11997027
Pedoe, Dan (1988) [1970], Geometry / A Comprehensive Course, Dover, ISBN 978-0-486-65812-4


== Further reading ==
Pedoe, Dan (1995) [1957], "1 Section 11: Compass geometry", Circles / A Mathematical View, Mathematical Association of America, pp. 23–25, ISBN 978-0-88385-518-8
Posamentier, Alfred S.; Geretschläger, Robert (2016), "8. Mascheroni constructions using only the compass", The Circle, Prometheus Books, pp. 197–216, ISBN 978-1-63388-167-9


== External links ==
Construction with the Compass Only
