# Regular 4-polytope

> **Query Topic**: regular polytope (Rank #2 Search Result)
> **Source Queue**: train (Row ID: 321, Frequency: 14)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Regular_4-polytope

---

In mathematics, a regular 4-polytope or regular polychoron is a regular four-dimensional polytope. They are the four-dimensional analogues of the regular polyhedra in three dimensions and the regular polygons in two dimensions.
There are six convex and ten star regular 4-polytopes, giving a total of sixteen.


== History ==
The convex regular 4-polytopes were first described by the Swiss mathematician Ludwig Schläfli in the mid-19th century. He discovered that there are precisely six such figures.
Schläfli also found four of the regular star 4-polytopes: the grand 120-cell, great stellated 120-cell, grand 600-cell, and great grand stellated 120-cell. He skipped the remaining six because he would not allow forms that failed the Euler characteristic on cells or vertex figures (for zero-hole tori: F − E + V = 2). That excludes cells and vertex figures such as the great dodecahedron {5,⁠5/2⁠} and small stellated dodecahedron {⁠5/2⁠,5}.
Edmund Hess (1843–1903) published the complete list in his 1883 German book Einleitung in die Lehre von der Kugelteilung mit besonderer Berücksichtigung ihrer Anwendung auf die Theorie der Gleichflächigen und der gleicheckigen Polyeder.


== Construction ==
The existence of a regular 4-polytope 
  
    
      
        {
        p
        ,
        q
        ,
        r
        }
      
    
    {\displaystyle \{p,q,r\}}
  
 is constrained by the existence of the regular polyhedra 
  
    
      
        {
        p
        ,
        q
        }
        ,
        {
        q
        ,
        r
        }
      
    
    {\displaystyle \{p,q\},\{q,r\}}
  
 which form its cells and a dihedral angle constraint

  
    
      
        sin
        ⁡
        
          
            π
            p
          
        
        sin
        ⁡
        
          
            π
            r
          
        
        >
        cos
        ⁡
        
          
            π
            q
          
        
      
    
    {\displaystyle \sin {\frac {\pi }{p}}\sin {\frac {\pi }{r}}>\cos {\frac {\pi }{q}}}
  

to ensure that the cells meet to form a closed 3-surface.
The six convex and ten star polytopes described are the only solutions to these constraints.
There are four nonconvex Schläfli symbols {p,q,r} that have valid cells {p,q} and vertex figures {q,r}, and pass the dihedral test, but fail to produce finite figures: {3,⁠5/2⁠,3}, {4,3,⁠5/2⁠}, {⁠5/2⁠,3,4}, {⁠5/2⁠,3,⁠5/2⁠}.


== Regular convex 4-polytopes ==
The regular convex 4-polytopes are the four-dimensional analogues of the Platonic solids in three dimensions and the convex regular polygons in two dimensions.
Each convex regular 4-polytope is bounded by a set of 3-dimensional cells which are all Platonic solids of the same type and size. These are fitted together along their respective faces (face-to-face) in a regular fashion, forming the surface of the 4-polytope which is a closed, curved 3-dimensional space (analogous to the way the surface of the earth is a closed, curved 2-dimensional space).


=== Properties ===
Like their 3-dimensional analogues, the convex regular 4-polytopes can be naturally ordered by size as a measure of 4-dimensional content (hypervolume) for the same radius. Each greater polytope in the sequence is rounder than its predecessor, enclosing more content within the same radius. The 4-simplex (5-cell) has the smallest content, and the 120-cell has the largest.

The following table lists some properties of the six convex regular 4-polytopes. The symmetry groups of these 4-polytopes are all Coxeter groups and given in the notation described in that article. The number following the name of the group is the order of the group.

John Conway advocated the names simplex, orthoplex, tesseract, octaplex or polyoctahedron (pO), tetraplex or polytetrahedron (pT), and dodecaplex or polydodecahedron (pD).
Norman Johnson advocated the names n-cell, or pentachoron, hexadecachoron, tesseract or octachoron, icositetrachoron, hexacosichoron, and hecatonicosachoron (or dodecacontachoron), coining the term polychoron being a 4D analogy to the 3D polyhedron, and 2D polygon, expressed from the Greek roots poly ("many") and choros ("room" or "space").
The Euler characteristic for all 4-polytopes is zero, we have the 4-dimensional analogue of Euler's polyhedral formula:

  
    
      
        
          N
          
            0
          
        
        −
        
          N
          
            1
          
        
        +
        
          N
          
            2
          
        
        −
        
          N
          
            3
          
        
        =
        0
        
      
    
    {\displaystyle N_{0}-N_{1}+N_{2}-N_{3}=0\,}
  

where Nk denotes the number of k-faces in the polytope (a vertex is a 0-face, an edge is a 1-face, etc.).
The topology of any given 4-polytope is defined by its Betti numbers and torsion coefficients.


=== As configurations ===
A regular 4-polytope can be completely described as a configuration matrix containing counts of its component elements. The rows and columns correspond to vertices, edges, faces, and cells. The diagonal numbers (upper left to lower right) say how many of each element occur in the whole 4-polytope. The non-diagonal numbers say how many of the column's element occur in or at the row's element. For example, there are 2 vertices in each edge (each edge has 2 vertices), and 2 cells meet at each face (each face belongs to 2 cells), in any regular 4-polytope. The configuration for the dual polytope can be obtained by rotating the matrix by 180 degrees.


=== Visualization ===
The following table shows some 2-dimensional projections of these 4-polytopes. Various other visualizations can be found in the external links below. The Coxeter-Dynkin diagram graphs are also given below the Schläfli symbol.


== Regular star (Schläfli–Hess) 4-polytopes ==
 
 
The Schläfli–Hess 4-polytopes are the complete set of 10 regular self-intersecting star polychora (four-dimensional polytopes). They are named in honor of their discoverers: Ludwig Schläfli and Edmund Hess. Each is represented by a Schläfli symbol {p,q,r} in which one of the numbers is ⁠5/2⁠. They are thus analogous to the regular nonconvex Kepler–Poinsot polyhedra, which are in turn analogous to the pentagram.


=== Names ===
Their names given here were given by John Conway, extending Cayley's names for the Kepler–Poinsot polyhedra: along with stellated and great, he adds a grand modifier.  Conway offered these operational definitions:

stellation – replaces edges with longer edges in same lines. (Example: a pentagon stellates into a pentagram)
greatening – replaces the faces with large ones in same planes. (Example: an icosahedron greatens into a great icosahedron)
aggrandizement – replaces the cells with large ones in same 3-spaces. (Example: a 600-cell aggrandizes into a grand 600-cell)
John Conway names the 10 forms from 3 regular celled 4-polytopes: pT=polytetrahedron {3,3,5} (a tetrahedral 600-cell), pI=polyicosahedron {3,5,⁠5/2⁠} (an icosahedral 120-cell), and pD=polydodecahedron {5,3,3} (a dodecahedral 120-cell), with prefix modifiers: g, a, and s for great, (ag)grand, and stellated. The final stellation, the great grand stellated polydodecahedron contains them all as gaspD.


=== Symmetry ===
All ten polychora have [3,3,5] (H4) hexacosichoric symmetry. They are generated from 6 related Goursat tetrahedra rational-order symmetry groups: [3,5,5/2], [5,5/2,5], [5,3,5/2], [5/2,5,5/2], [5,5/2,3], and [3,3,5/2].
Each group has 2 regular star-polychora, except for two groups which are self-dual, having only one. So there are 4 dual-pairs and 2 self-dual forms among the ten regular star polychora.


=== Properties ===
Note:

There are 2 unique vertex arrangements, matching those of the 120-cell and 600-cell.
There are 4 unique edge arrangements, which are shown as wireframes orthographic projections.
There are 7 unique face arrangements, shown as solids (face-colored) orthographic projections. (However, the icosahedral 120-cell has the same face arrangement as the convex 600-cell.)
The cells (polyhedra), their faces (polygons), the polygonal edge figures and polyhedral vertex figures are identified by their Schläfli symbols.


== See also ==
Regular polytope
List of regular polytopes
Infinite regular 4-polytopes:
One regular Euclidean honeycomb:  {4,3,4}
Four compact regular hyperbolic honeycombs: {3,5,3}, {4,3,5}, {5,3,4}, {5,3,5}
Eleven paracompact regular hyperbolic honeycombs: {3,3,6}, {6,3,3}, {3,4,4}, {4,4,3}, {3,6,3}, {4,3,6}, {6,3,4}, {4,4,4}, {5,3,6}, {6,3,5}, and {6,3,6}.
Abstract regular 4-polytopes:
11-cell {3,5,3}
57-cell {5,3,5}
Uniform 4-polytope uniform 4-polytope families constructed from these 6 regular forms.
Platonic solid
Kepler-Poinsot polyhedra — regular star polyhedron
Star polygon — regular star polygons
4-polytope
5-polytope
6-polytope


== Notes ==


== References ==


=== Citations ===


=== Bibliography ===


== External links ==
Weisstein, Eric W. "Regular polychoron". MathWorld.
Jonathan Bowers, 16 regular 4-polytopes
Regular 4D Polytope Foldouts Archived 2011-07-17 at the Wayback Machine
Catalog of Polytope Images A collection of stereographic projections of 4-polytopes.
A Catalog of Uniform Polytopes
Dimensions 2 hour film about the fourth dimension (contains stereographic projections of all regular 4-polytopes)
Reguläre Polytope
The Regular Star Polychora
Hypersolids
