# Wallpaper group

> **Query Topic**: How many crystallographic point groups are there in three-dimensional space (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 270, Frequency: 18)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Wallpaper_group

---

A wallpaper group (or plane symmetry group or plane crystallographic group ) is a mathematical classification of a two-dimensional repetitive pattern, based on the symmetries in the pattern. Such patterns occur frequently in architecture and decorative art , especially in textiles , tiles , and wallpaper .

The simplest wallpaper group, Group p 1, applies when there is no symmetry beyond simple translation of a pattern in two dimensions. The following patterns have more forms of symmetry, including some rotational and reflectional symmetries:

- Example A : Cloth, Tahiti

- Example B : Ornamental painting, Nineveh , Assyria

- Example C : Painted porcelain , China

Examples A and B have the same wallpaper group; it is called p 4 m in the IUCr notation and *442 in the orbifold notation . Example C has a different wallpaper group, called p 4 g or 4*2 . The fact that A and B have the same wallpaper group means that they have the same symmetries, regardless of the designs' superficial details; whereas C has a different set of symmetries.

The number of symmetry groups depends on the number of dimensions in the patterns. Wallpaper groups apply to the two-dimensional case, intermediate in complexity between the simpler frieze groups and the three-dimensional space groups .

A proof that there are only 17 distinct groups of such planar symmetries was first carried out by Evgraf Fedorov in 1891 and then derived independently by George Pólya in 1924. The proof that the list of wallpaper groups is complete came only after the much harder case of space groups had been done. The seventeen wallpaper groups are listed below; see § The seventeen groups .

## Symmetries of patterns

A symmetry of a pattern is, loosely speaking, a way of transforming the pattern so that it looks exactly the same after the transformation. For example, translational symmetry is present when the pattern can be translated (in other words, shifted) some finite distance and appear unchanged. Think of shifting a set of vertical stripes horizontally by one stripe. The pattern is unchanged. Strictly speaking, a true symmetry only exists in patterns that repeat exactly and continue indefinitely. A set of only, say, five stripes does not have translational symmetry—when shifted, the stripe on one end "disappears" and a new stripe is "added" at the other end. In practice, however, classification is applied to finite patterns, and small imperfections may be ignored.

The types of transformations that are relevant here are called Euclidean plane isometries . For example:

- If one shifts example B one unit to the right, so that each square covers the square that was originally adjacent to it, then the resulting pattern is exactly the same as the starting pattern. This type of symmetry is called a translation . Examples A and C are similar, except that the smallest possible shifts are in diagonal directions.

- If one turns example B clockwise by 90°, around the centre of one of the squares, again one obtains exactly the same pattern. This is called a rotation . Examples A and C also have 90° rotations, although it requires a little more ingenuity to find the correct centre of rotation for C .

- One can also flip example B across a horizontal axis that runs across the middle of the image. This is called a reflection . Example B also has reflections across a vertical axis, and across two diagonal axes. The same can be said for A .

However, example C is different . It only has reflections in horizontal and vertical directions, not across diagonal axes. If one flips across a diagonal line, one does not get the same pattern back, but the original pattern shifted across by a certain distance. This is part of the reason that the wallpaper group of A and B is different from the wallpaper group of C .

Another transformation is a glide reflection , a combination of reflection and translation parallel to the line of reflection.

## Formal definition and discussion

Mathematically, a wallpaper group or plane crystallographic group is a type of topologically discrete group of isometries of the Euclidean plane that contains two linearly independent translations .

Two such isometry groups are of the same type (of the same wallpaper group) if they are the same up to an affine transformation of the plane . Thus e.g. a translation of the plane (hence a translation of the mirrors and centres of rotation) does not affect the wallpaper group. The same applies for a change of angle between translation vectors, provided that it does not add or remove any symmetry (this is only the case if there are no mirrors and no glide reflections , and rotational symmetry is at most of order 2).

Unlike in the three-dimensional case , one can equivalently restrict the affine transformations to those that preserve orientation .

It follows from Bieberbach's theorems on crystallographic groups that all wallpaper groups are different even as abstract groups (as opposed to e.g. frieze groups , of which two are isomorphic with Z ).

2D patterns with double translational symmetry can be categorized according to their symmetry group type.

### Isometries of the Euclidean plane

Isometries of the Euclidean plane fall into four categories (see the article Euclidean plane isometry for more information).

- Translations , denoted by T v , where v is a vector in R 2 . This has the effect of shifting the plane applying displacement vector v .

- Rotations , denoted by R c , θ , where c is a point in the plane (the centre of rotation), and θ is the angle of rotation.

- Reflections , or mirror isometries , denoted by F L , where L is a line in R 2 . ( F is for "flip"). This has the effect of reflecting the plane in the line L , called the reflection axis or the associated mirror .

- Glide reflections , denoted by G L , d , where L is a line in R 2 and d is a distance. This is a combination of a reflection in the line L and a translation along L by a distance d .

### The independent translations condition

The condition on linearly independent translations means that there exist linearly independent vectors v and w (in R 2 ) such that the group contains both T v and T w .

The purpose of this condition is to distinguish wallpaper groups from frieze groups , which possess a translation but not two linearly independent ones, and from two-dimensional discrete point groups , which have no translations at all. In other words, wallpaper groups represent patterns that repeat themselves in two distinct directions, in contrast to frieze groups, which only repeat along a single axis.

(It is possible to generalise this situation. One could for example study discrete groups of isometries of R n with m linearly independent translations, where m is any integer in the range 0 ≤ m ≤ n .)

### The discreteness condition

The discreteness condition means that there is some positive real number ε, such that for every translation T v in the group, the vector v has length at least ε (except of course in the case that v is the zero vector, but the independent translations condition prevents this, since any set that contains the zero vector is linearly dependent by definition and thus disallowed).

The purpose of this condition is to ensure that the group has a compact fundamental domain, or in other words, a "cell" of nonzero, finite area, which is repeated through the plane. Without this condition, one might have for example a group containing the translation T x for every rational number x , which would not correspond to any reasonable wallpaper pattern.

One important and nontrivial consequence of the discreteness condition in combination with the independent translations condition is that the group can only contain rotations of order 2, 3, 4, or 6; that is, every rotation in the group must be a rotation by 180°, 120°, 90°, or 60°. This fact is known as the crystallographic restriction theorem , and can be generalised to higher-dimensional cases.

### Notations for wallpaper groups

#### Crystallographic notation

Crystallography has 230 space groups to distinguish, far more than the 17 wallpaper groups, but many of the symmetries in the groups are the same. Thus one can use a similar notation for both kinds of groups, that of Carl Hermann and Charles-Victor Mauguin . An example of a full wallpaper name in Hermann-Mauguin style (also called IUCr notation ) is p 31 m , with four letters or digits; more usual is a shortened name like cmm or pg .

For wallpaper groups the full notation begins with either p or c , for a primitive cell or a face-centred cell ; these are explained below. This is followed by a digit, n , indicating the highest order of rotational symmetry: 1-fold (none), 2-fold, 3-fold, 4-fold, or 6-fold. The next two symbols indicate symmetries relative to one translation axis of the pattern, referred to as the "main" one; if there is a mirror perpendicular to a translation axis that is the main one (or if there are two, one of them). The symbols are either m , g , or 1 , for mirror, glide reflection, or none. The axis of the mirror or glide reflection is perpendicular to the main axis for the first letter, and either parallel or tilted 180°/ n (when n > 2) for the second letter. Many groups include other symmetries implied by the given ones. The short notation drops digits or an m that can be deduced, so long as that leaves no confusion with another group.

A primitive cell is a minimal region repeated by lattice translations. All but two wallpaper symmetry groups are described with respect to primitive cell axes, a coordinate basis using the translation vectors of the lattice. In the remaining two cases symmetry description is with respect to centred cells that are larger than the primitive cell, and hence have internal repetition; the directions of their sides is different from those of the translation vectors spanning a primitive cell. Hermann-Mauguin notation for crystal space groups uses additional cell types.

- p 2 ( p 2 ): Primitive cell, 2-fold rotation symmetry, no mirrors or glide reflections.

- p 4 gm ( p 4 gm ): Primitive cell, 4-fold rotation, glide reflection perpendicular to main axis, mirror axis at 45°.

- c 2 mm ( c 2 mm ): Centred cell, 2-fold rotation, mirror axes both perpendicular and parallel to main axis.

- p 31 m ( p 31 m ): Primitive cell, 3-fold rotation, mirror axis at 60°.

Here are all the names that differ in short and full notation.

The remaining names are p 1 , p 2 , p 3 , p 3 m 1 , p 31 m , p 4 , and p 6 .

#### Orbifold notation

Orbifold notation for wallpaper groups, advocated by John Conway (Conway, 1992) (Conway 2008), is based not on crystallography, but on topology. One can fold the infinite periodic tiling of the plane into its essence, an orbifold , then describe that with a few symbols.

- A digit, n , indicates a centre of n -fold rotation corresponding to a cone point on the orbifold. By the crystallographic restriction theorem, n must be 2, 3, 4, or 6.

- An asterisk, * , indicates a mirror symmetry corresponding to a boundary of the orbifold. It interacts with the digits as follows: Digits before * denote centres of pure rotation ( cyclic ). Digits after * denote centres of rotation with mirrors through them, corresponding to "corners" on the boundary of the orbifold ( dihedral ).

- Digits before * denote centres of pure rotation ( cyclic ).

- Digits after * denote centres of rotation with mirrors through them, corresponding to "corners" on the boundary of the orbifold ( dihedral ).

- A cross, × , occurs when a glide reflection is present and indicates a crosscap on the orbifold. Pure mirrors combine with lattice translation to produce glides, but those are already accounted for so need no notation.

- The "no symmetry" symbol, o , stands alone, and indicates there are only lattice translations with no other symmetry. The orbifold with this symbol is a torus; in general the symbol o denotes a handle on the orbifold.

The group denoted in crystallographic notation by cmm will, in Conway's notation, be 2*22 . The 2 before the * says there is a 2-fold rotation centre with no mirror through it. The * itself says there is a mirror. The first 2 after the * says there is a 2-fold rotation centre on a mirror. The final 2 says there is an independent second 2-fold rotation centre on a mirror, one that is not a duplicate of the first one under symmetries.

The group denoted by pgg will be 22× . There are two pure 2-fold rotation centres, and a glide reflection axis. Contrast this with pmg , Conway 22* , where crystallographic notation mentions a glide, but one that is implicit in the other symmetries of the orbifold.

Coxeter 's bracket notation is also included, based on reflectional Coxeter groups , and modified with plus superscripts accounting for rotations, improper rotations and translations.

### Why there are exactly seventeen groups

An orbifold can be viewed as a polygon with face, edges, and vertices which can be unfolded to form a possibly infinite set of polygons which tile either the sphere , the plane or the hyperbolic plane . When it tiles the plane it will give a wallpaper group and when it tiles the sphere or hyperbolic plane it gives either a spherical symmetry group or hyperbolic symmetry group . The type of space the polygons tile can be found by calculating the Euler characteristic , χ = V − E + F , where V is the number of corners (vertices), E is the number of edges and F is the number of faces. If the Euler characteristic is positive then the orbifold has an elliptic (spherical) structure; if it is zero then it has a parabolic structure, i.e. a wallpaper group; and if it is negative it will have a hyperbolic structure. When the full set of possible orbifolds is enumerated it is found that only 17 have Euler characteristic 0.

When an orbifold replicates by symmetry to fill the plane, its features create a structure of vertices, edges, and polygon faces, which must be consistent with the Euler characteristic. Reversing the process, one can assign numbers to the features of the orbifold, but fractions, rather than whole numbers. Because the orbifold itself is a quotient of the full surface by the symmetry group, the orbifold Euler characteristic is a quotient of the surface Euler characteristic by the order of the symmetry group.

The orbifold Euler characteristic is 2 minus the sum of the feature values, assigned as follows:

- A digit n without or before a * counts as ⁠ n − 1 / n ⁠ .

- A digit n after a * counts as ⁠ n − 1 / 2 n ⁠ .

- Both * and × count as 1.

- The "no symmetry" o counts as 2.

For a wallpaper group, the sum for the characteristic must be zero; thus the feature sum must be 2.

- 632: ⁠ 5 / 6 ⁠ + ⁠ 2 / 3 ⁠ + ⁠ 1 / 2 ⁠ = 2

- 3*3: ⁠ 2 / 3 ⁠ + 1 + ⁠ 2 / 6 ⁠ = 2

- 4*2: ⁠ 3 / 4 ⁠ + 1 + ⁠ 1 / 4 ⁠ = 2

- 22×: ⁠ 1 / 2 ⁠ + ⁠ 1 / 2 ⁠ + 1 = 2

Now enumeration of all wallpaper groups becomes a matter of arithmetic, of listing all feature strings with values summing to 2.

Feature strings with other sums are not nonsense; they imply non-planar tilings, not discussed here. (When the orbifold Euler characteristic is negative, the tiling is hyperbolic ; when positive, spherical or bad ).

## Guide to recognizing wallpaper groups

To work out which wallpaper group corresponds to a given design, one may use the following table.

See also this overview with diagrams .

## The seventeen groups

Each of the groups in this section has two cell structure diagrams, which are to be interpreted as follows (it is the shape that is significant, not the colour):

On the right-hand side diagrams, different equivalence classes of symmetry elements are colored (and rotated) differently.

The brown or yellow area indicates a fundamental domain , i.e. the smallest part of the pattern that is repeated.

The diagrams on the right show the cell of the lattice corresponding to the smallest translations; those on the left sometimes show a larger area.

Each symmetry element of a wallpaper group is either an element of a certain point group or a combination of such an element and a translation. This point group is given in the descriptions below. There is not necessarily a point having the said point-group symmetry. For example the Group pg is associated with the point group D 1 , which includes a reflexion, but there is no reflexion and no point having any symmetry. The Group pm on the other hand, associated with the same point group, does have reflexion lines.

### Group p 1 (o)

- Orbifold signature: o

- Coxeter notation (rectangular): [∞ + ,2,∞ + ] or [∞] + ×[∞] +

- Lattice: oblique

- Point group: C 1

- The group p 1 contains only translations; there are no rotations, reflections, or glide reflections.

- Computer generated

- Medieval wall diapering

- 21 co-uniform tiling

The two translations (cell sides) can each have different lengths, and can form any angle.

### Group p 2 (2222)

- Orbifold signature: 2222

- Coxeter notation (rectangular): [∞,2,∞] +

- Lattice: oblique

- Point group: C 2

- The group p 2 contains four rotation centres of order two (180°), but no reflections or glide reflections.

- Computer generated

- Cloth, Sandwich Islands ( Hawaii )

- Ceiling of an Egyptian tomb

- Wire fence , U.S.

- Mat on which an Egyptian king stood

- Egyptian mat (detail)

- 15 co-uniform tiling

### Group pm (**)

- Orbifold signature: **

- Coxeter notation: [∞,2,∞ + ] or [∞ + ,2,∞]

- Lattice: rectangular

- Point group: D 1

- The group pm has no rotations. It has reflection axes, they are all parallel.

(The first four have a vertical symmetry axis, and the last two each have a different diagonal one.)

- Computer generated

- Dress of a figure in a tomb at Biban el Moluk , Egypt

- Egyptian tomb , Thebes

- 6 co-uniform tiling (slab)

- Ceiling of a tomb at Gourna, Egypt . Reflection axis is diagonal

- Indian metalwork at the Great Exhibition in 1851. This is almost pm (ignoring short diagonal lines between ovals motifs, which make it p 1 )

### Group pg (××)

- Orbifold signature: ××

- Coxeter notation: [(∞,2) + ,∞ + ] or [∞ + ,(2,∞) + ]

- Lattice: rectangular

- Point group: D 1

- The group pg contains glide reflections only, and their axes are all parallel. There are no rotations or reflections.

- Computer generated

- Mat with herringbone pattern on which Egyptian king stood. Zooming in shows that there it does not have bilateral symmetry (see next image).

- Egyptian mat (detail)

- Pavement with herringbone pattern in Salzburg . Glide reflection axis runs northeast–southwest

- One of the colorings of the snub square tiling ; the glide reflection lines are in the direction upper left / lower right; ignoring colors there is much more symmetry than just pg , then it is p 4 g (see there for this image with equally colored triangles)

- 6 co-uniform tiling made only of pentagons

Without the details inside the zigzag bands the mat is pmg ; with the details but without the distinction between brown and black it is pgg .

Ignoring the wavy borders of the tiles, the pavement is pgg .

### Group cm (*×)

- Orbifold signature: *×

- Coxeter notation: [∞ + ,2 + ,∞] or [∞,2 + ,∞ + ]

- Lattice: rhombic

- Point group: D 1

- The group cm contains no rotations. It has reflection axes, all parallel. There is at least one glide reflection whose axis is not a reflection axis; it is halfway between two adjacent parallel reflection axes.

- This group applies for symmetrically staggered rows (i.e. there is a shift per row of half the translation distance inside the rows) of identical objects, which have a symmetry axis perpendicular to the rows.

- Computer generated

- Dress of Amun , from Abu Simbel , Egypt

- Dado from Biban el Moluk , Egypt

- Bronze vessel in Nimroud , Assyria

- Spandrels of arches , the Alhambra , Spain

- Soffit of arch, the Alhambra , Spain

- Persian tapestry

- Indian metalwork at the Great Exhibition in 1851

- Detail of a floor tile. Manises Ceramics Museum, Spain

- Dress of a figure in a tomb at Biban el Moluk , Egypt

- 6 co-uniform tiling with hexagonal cells

- Textile pattern: houndstooth

### Group pmm (*2222)

- Orbifold signature: *2222

- Coxeter notation (rectangular): [∞,2,∞] or [∞]×[∞]

- Coxeter notation (square): [4,1 + ,4] or [1 + ,4,4,1 + ]

- Lattice: rectangular

- Point group: D 2

- The group pmm has reflections in two perpendicular directions, and four rotation centres of order two (180°) located at the intersections of the reflection axes.

- 2D image of lattice fence , U.S. (in 3D there is additional symmetry)

- Mummy case stored in The Louvre

- Mummy case stored in The Louvre . Would be type p 4 m except for the mismatched coloring

- 8 co-uniform tiling with all non-slab planigons

- Color filter array layout used in Fujifilm X-Trans sensors

### Group pmg (22*)

- Orbifold signature: 22 *

- Coxeter notation: [(∞,2) + ,∞] or [∞,(2,∞) + ]

- Lattice: rectangular

- Point group: D 2

- The group pmg has two rotation centres of order two (180°), and reflections in only one direction. It has glide reflections whose axes are perpendicular to the reflection axes. The centres of rotation all lie on glide reflection axes.

- Computer generated

- Cloth, Sandwich Islands ( Hawaii )

- Ceiling of Egyptian tomb

- Floor tiling in Prague , the Czech Republic

- Bowl from Kerma

- Pentagon packing

- 4 co-uniform tiling

### Group pgg (22×)

- Orbifold signature: 22 ×

- Coxeter notation (rectangular): [((∞,2) + ,(∞,2) + )]

- Coxeter notation (square): [4 + ,4 + ]

- Lattice: rectangular

- Point group: D 2

- The group pgg contains two rotation centres of order two (180°), and glide reflections in two perpendicular directions. The centres of rotation are not located on the glide reflection axes. There are no reflections.

- Computer generated

- Bronze vessel in Nimroud , Assyria

- Pavement in Budapest , Hungary

- 4 co-uniform tiling (strictly trihexagonal)

### Group cmm (2*22)

- Orbifold signature: 2 *22

- Coxeter notation (rhombic): [∞,2 + ,∞]

- Coxeter notation (square): [(4,4,2 + )]

- Lattice: rhombic

- Point group: D 2

- The group cmm has reflections in two perpendicular directions, and a rotation of order two (180°) whose centre is not on a reflection axis. It also has two rotations whose centres are on a reflection axis.

- This group is frequently seen in everyday life, since the most common arrangement of bricks in a brick building ( running bond ) utilises this group (see example below).

The rotational symmetry of order 2 with centres of rotation at the centres of the sides of the rhombus is a consequence of the other properties.

The pattern corresponds to each of the following:

- symmetrically staggered rows of identical doubly symmetric objects

- a checkerboard pattern of two alternating rectangular tiles, of which each, by itself, is doubly symmetric

- a checkerboard pattern of alternatingly a 2-fold rotationally symmetric rectangular tile and its mirror image

- Computer generated

- Elongated triangular tiling

- Suburban brick wall using running bond arrangement, U.S.

- Ceiling of Egyptian tomb . Ignoring colors, this would be p 4 g

- Egyptian

- Persian tapestry

- Egyptian tomb

- Turkish dish

- A compact packing of two sizes of circle

- Another compact packing of two sizes of circle

- Another compact packing of two sizes of circle

- 3 co-uniform tiling (Krötenheerdt)

### Group p 4 (442)

- Orbifold signature: 442

- Coxeter notation: [4,4] +

- Lattice: square

- Point group: C 4

- The group p 4 has two rotation centres of order four (90°), and one rotation centre of order two (180°). It has no reflections or glide reflections.

A p 4 pattern can be looked upon as a repetition in rows and columns of equal square tiles with 4-fold rotational symmetry. Also it can be looked upon as a checkerboard pattern of two such tiles, a factor √ 2 smaller and rotated 45°.

- Computer generated

- Ceiling of Egyptian tomb ; ignoring colors this is p 4 , otherwise p 2

- Ceiling of Egyptian tomb

- Overlaid patterns

- Frieze, the Alhambra , Spain . Requires close inspection to see why there are no reflections

- Viennese cane

- Renaissance earthenware

- Pythagorean tiling

- Generated from a photograph

- 4 co-uniform tiling

### Group p 4 m (*442)

- Orbifold signature: *442

- Coxeter notation: [4,4]

- Lattice: square

- Point group: D 4

- The group p 4 m has two rotation centres of order four (90°), and reflections in four distinct directions (horizontal, vertical, and diagonals). It has additional glide reflections whose axes are not reflection axes; rotations of order two (180°) are centred at the intersection of the glide reflection axes. All rotation centres lie on reflection axes.

This corresponds to a straightforward grid of rows and columns of equal squares with the four reflection axes. Also it corresponds to a checkerboard pattern of two of such squares.

Examples displayed with the smallest translations horizontal and vertical (like in the diagram):

- Computer generated

- Square tiling

- Tetrakis square tiling ; ignoring colors, this is p 4 m , otherwise cmm

- Truncated square tiling (ignoring color also, with smaller translations)

- Ornamental painting, Nineveh , Assyria

- Storm drain , U.S.

- Egyptian mummy case

- Persian glazed tile

- Compact packing of two sizes of circle

- 4 co-uniform tiling (Krötenheerdt)

Examples displayed with the smallest translations diagonal:

- checkerboard

- Cloth, Otaheite ( Tahiti )

- Egyptian tomb

- Cathedral of Bourges

- Dish from Turkey , Ottoman period

### Group p 4 g (4*2)

- Orbifold signature: 4 *2

- Coxeter notation: [4 + ,4]

- Lattice: square

- Point group: D 4

- The group p 4 g has two centres of rotation of order four (90°), which are each other's mirror image, but it has reflections in only two directions, which are perpendicular. There are rotations of order two (180°) whose centres are located at the intersections of reflection axes. It has glide reflections axes parallel to the reflection axes, in between them, and also at an angle of 45° with these.

A p 4 g pattern can be looked upon as a checkerboard pattern of copies of a square tile with 4-fold rotational symmetry, and its mirror image. Alternatively it can be looked upon (by shifting half a tile) as a checkerboard pattern of copies of a horizontally and vertically symmetric tile and its 90° rotated version. Note that neither applies for a plain checkerboard pattern of black and white tiles, this is group p 4 m (with diagonal translation cells).

- Bathroom linoleum , U.S.

- Painted porcelain , China

- Fly screen, U.S.

- Painting, China

- one of the colorings of the snub square tiling (see also at pg )

- 4 co-uniform tiling ( fractalization of snub square tiling)

### Group p 3 (333)

- Orbifold signature: 333

- Coxeter notation: [(3,3,3)] + or [3 [3] ] +

- Lattice: hexagonal

- Point group: C 3

- The group p 3 has three different rotation centres of order three (120°), but no reflections or glide reflections.

Imagine a tessellation of the plane with equilateral triangles of equal size, with the sides corresponding to the smallest translations. Then half of the triangles are in one orientation, and the other half upside down. This wallpaper group corresponds to the case that all triangles of the same orientation are equal, while both types have rotational symmetry of order three, but the two are not equal, not each other's mirror image, and not both symmetric (if the two are equal it is p 6 , if they are each other's mirror image it is p 31 m , if they are both symmetric it is p 3 m 1 ; if two of the three apply then the third also, and it is p 6 m ). For a given image, three of these tessellations are possible, each with rotation centres as vertices, i.e. for any tessellation two shifts are possible. In terms of the image: the vertices can be the red, the blue or the green triangles.

Equivalently, imagine a tessellation of the plane with regular hexagons, with sides equal to the smallest translation distance divided by √ 3 . Then this wallpaper group corresponds to the case that all hexagons are equal (and in the same orientation) and have rotational symmetry of order three, while they have no mirror image symmetry (if they have rotational symmetry of order six it is p 6 , if they are symmetric with respect to the main diagonals it is p 31 m , if they are symmetric with respect to lines perpendicular to the sides it is p 3 m 1 ; if two of the three apply then the third also, it is p 6 m ). For a given image, three of these tessellations are possible, each with one third of the rotation centres as centres of the hexagons. In terms of the image: the centres of the hexagons can be the red, the blue or the green triangles.

- Computer generated

- Snub trihexagonal tiling (ignoring the colors: p 6 ); the translation vectors are rotated a little to the right compared with the directions in the underlying hexagonal lattice of the image

- Street pavement in Zakopane , Poland

- Tiling based on similar tiling in the Alhambra , Spain

- 6 co-uniform tiling, each rotation point surrounded by a 3-fold cluster

### Group p 3 m 1 (*333)

- Orbifold signature: *333

- Coxeter notation: [(3,3,3)] or [3 [3] ]

- Lattice: hexagonal

- Point group: D 3

- The group p 3 m 1 has three different rotation centres of order three (120°). It has reflections in the three sides of an equilateral triangle. The centre of every rotation lies on a reflection axis. There are additional glide reflections in three distinct directions, whose axes are located halfway between adjacent parallel reflection axes.

Like for p 3 , imagine a tessellation of the plane with equilateral triangles of equal size, with the sides corresponding to the smallest translations. Then half of the triangles are in one orientation, and the other half upside down. This wallpaper group corresponds to the case that all triangles of the same orientation are equal, while both types have rotational symmetry of order three, and both are symmetric, but the two are not equal, and not each other's mirror image. For a given image, three of these tessellations are possible, each with rotation centres as vertices. In terms of the image: the vertices can be the red, the blue or the green triangles.

- Triangular tiling (ignoring colors: p 6 m )

- Hexagonal tiling (ignoring colors: p 6 m )

- Truncated hexagonal tiling (ignoring colors: p 6 m )

- Persian glazed tile (ignoring colors: p 6 m )

- Persian ornament

- Painting, China (see detailed image)

- 6 co-uniform tiling (smallest one containing 3 different 3-clusters)

### Group p 31 m (3*3)

- Orbifold signature: 3 *3

- Coxeter notation: [6,3 + ]

- Lattice: hexagonal

- Point group: D 3

- The group p 31 m has three different rotation centres of order three (120°), of which two are each other's mirror image. It has reflections in three distinct directions. It has at least one rotation whose centre does not lie on a reflection axis. There are additional glide reflections in three distinct directions, whose axes are located halfway between adjacent parallel reflection axes.

Like for p 3 and p 3 m 1 , imagine a tessellation of the plane with equilateral triangles of equal size, with the sides corresponding to the smallest translations. Then half of the triangles are in one orientation, and the other half upside down. This wallpaper group corresponds to the case that all triangles of the same orientation are equal, while both types have rotational symmetry of order three and are each other's mirror image, but not symmetric themselves, and not equal. For a given image, only one such tessellation is possible. In terms of the image: the vertices must be the red triangles, not the blue triangles.

- Persian glazed tile

- Painted porcelain , China

- Painting, China

- Geometric design on a folding camping table

- Compact packing of two sizes of circle

- 4 co-uniform tiling

### Group p 6 (632)

- Orbifold signature: 632

- Coxeter notation: [6,3] +

- Lattice: hexagonal

- Point group: C 6

- The group p 6 has one rotation centre of order six (60°); two rotation centres of order three (120°), which are each other's images under a rotation of 60°; and three rotation centres of order two (180°) which are also each other's images under a rotation of 60°. It has no reflections or glide reflections.

A pattern with this symmetry can be looked upon as a tessellation of the plane with equal triangular tiles with C 3 symmetry, or equivalently, a tessellation of the plane with equal hexagonal tiles with C 6 symmetry (with the edges of the tiles not necessarily part of the pattern).

- Computer generated

- Regular polygons

- Wall panelling, the Alhambra , Spain

- Persian ornament

- Floret pentagonal tiling

- 7 co-uniform tiling with horizontal and 60° translations

### Group p 6 m (*632)

- Orbifold signature: *632

- Coxeter notation: [6,3]

- Lattice: hexagonal

- Point group: D 6

- The group p 6 m has one rotation centre of order six (60°); it has two rotation centres of order three, which only differ by a rotation of 60° (or, equivalently, 180°), and three of order two, which only differ by a rotation of 60°. It has also reflections in six distinct directions. There are additional glide reflections in six distinct directions, whose axes are located halfway between adjacent parallel reflection axes.

A pattern with this symmetry can be looked upon as a tessellation of the plane with equal triangular tiles with D 3 symmetry, or equivalently, a tessellation of the plane with equal hexagonal tiles with D 6 symmetry (with the edges of the tiles not necessarily part of the pattern). Thus the simplest examples are a triangular lattice with or without connecting lines, and a hexagonal tiling with one color for outlining the hexagons and one for the background.

- Computer generated

- Trihexagonal tiling

- Small rhombitrihexagonal tiling

- Great rhombitrihexagonal tiling

- Persian glazed tile

- Bronze vessel in Nimroud , Assyria

- Byzantine marble pavement, Rome

- Painted porcelain , China

- Painted porcelain , China

- Compact packing of two sizes of circle

- Another compact packing of two sizes of circle

- 7 co-uniform tiling

- King's dress, Khorsabad , Assyria ; this is almost p 6 m (ignoring inner parts of flowers, which make it cmm )

## Lattice types

There are five lattice types or Bravais lattices , corresponding to the five possible wallpaper groups of the lattice itself. The wallpaper group of a pattern with this lattice of translational symmetry cannot have more, but may have less symmetry than the lattice itself.

- In the 5 cases of rotational symmetry of order 3 or 6, the unit cell consists of two equilateral triangles (hexagonal lattice, itself p 6 m ). They form a rhombus with angles 60° and 120°.

- In the 3 cases of rotational symmetry of order 4, the cell is a square (square lattice, itself p 4 m ).

- In the 5 cases of reflection or glide reflection, but not both, the cell is a rectangle (rectangular lattice, itself pmm ). It may also be interpreted as a centered rhombic lattice. Special cases: square.

- In the 2 cases of reflection combined with glide reflection, the cell is a rhombus (rhombic lattice, itself cmm ). It may also be interpreted as a centered rectangular lattice. Special cases: square, hexagonal unit cell.

- In the case of only rotational symmetry of order 2, and the case of no other symmetry than translational, the cell is in general a parallelogram (parallelogrammatic or oblique lattice, itself p 2 ). Special cases: rectangle, square, rhombus, hexagonal unit cell.

## Symmetry groups

The actual symmetry group should be distinguished from the wallpaper group. Wallpaper groups are collections of symmetry groups. There are 17 of these collections, but for each collection there are infinitely many symmetry groups, in the sense of actual groups of isometries. These depend, apart from the wallpaper group, on a number of parameters for the translation vectors, the orientation and position of the reflection axes and rotation centers.

The numbers of degrees of freedom are:

- 6 for p 2

- 5 for pmm , pmg , pgg , and cmm

- 4 for the rest.

However, within each wallpaper group, all symmetry groups are algebraically isomorphic.

Some symmetry group isomorphisms:

- p 1 : Z 2

- pm : Z × D ∞

- pmm : D ∞ × D ∞ .

## Dependence of wallpaper groups on transformations

- The wallpaper group of a pattern is invariant under isometries and uniform scaling ( similarity transformations ).

- Translational symmetry is preserved under arbitrary bijective affine transformations .

- Rotational symmetry of order two ditto; this means also that 4- and 6-fold rotation centres at least keep 2-fold rotational symmetry.

- Reflection in a line and glide reflection are preserved on expansion/contraction along, or perpendicular to, the axis of reflection and glide reflection. It changes p 6 m , p 4 g , and p 3 m 1 into cmm , p 3 m 1 into cm , and p 4 m , depending on direction of expansion/contraction, into pmm or cmm . A pattern of symmetrically staggered rows of points is special in that it can convert by expansion/contraction from p 6 m to p 4 m .

Note that when a transformation decreases symmetry, a transformation of the same kind (the inverse) obviously for some patterns increases the symmetry. Such a special property of a pattern (e.g. expansion in one direction produces a pattern with 4-fold symmetry) is not counted as a form of extra symmetry.

Change of colors does not affect the wallpaper group if any two points that have the same color before the change, also have the same color after the change, and any two points that have different colors before the change, also have different colors after the change.

If the former applies, but not the latter, such as when converting a color image to one in black and white, then symmetries are preserved, but they may increase, so that the wallpaper group can change.

## Web demo and software

Several software graphic tools will let you create 2D patterns using wallpaper symmetry groups. Usually you can edit the original tile and its copies in the entire pattern are updated automatically.

- MadPattern , a free set of Adobe Illustrator templates that support the 17 wallpaper groups

- Tess , a shareware tessellation program for multiple platforms, supports all wallpaper, frieze, and rosette groups, as well as Heesch tilings.

- Wallpaper Symmetry is a free online JavaScript drawing tool supporting the 17 groups. The main page has an explanation of the wallpaper groups, as well as drawing tools and explanations for the other planar symmetry groups as well.

- TALES GAME , a free software designed for educational purposes which includes the tessellation function.

- Kali Archived 2018-12-16 at the Wayback Machine , online graphical symmetry editor Java applet (not supported by default in browsers).

- Kali Archived 2020-11-21 at the Wayback Machine , free downloadable Kali for Windows and Mac Classic.

- Inkscape , a free vector graphics editor , supports all 17 groups plus arbitrary scales, shifts, rotates, and color changes per row or per column, optionally randomized to a given degree. (See )

- SymmetryWorks is a commercial plugin for Adobe Illustrator , supports all 17 groups.

- EscherSketch is a free online JavaScript drawing tool supporting the 17 groups.

- Repper is a commercial online drawing tool supporting the 17 groups plus a number of non-periodic tilings
