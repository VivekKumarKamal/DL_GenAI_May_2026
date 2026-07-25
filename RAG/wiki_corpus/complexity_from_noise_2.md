# Perlin noise

> **Query Topic**: complexity from noise (Rank #2 Search Result)  
> **Source Queue**: train (Row ID: 85, Frequency: 10)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Perlin_noise

---

Perlin noise is a type of gradient noise developed by Ken Perlin in 1982. It has many uses, including but not limited to: procedurally generating terrain, applying pseudo-random changes to a variable, and assisting in the creation of image textures. It is most commonly implemented in two, three, or four dimensions, but can be defined for any number of dimensions.


== History ==
Ken Perlin developed Perlin noise in 1982 as a result of his problems with the "machine-like" look of computer-generated imagery (CGI) at the time. He formally described his findings in a SIGGRAPH paper in 1985 called "An Image Synthesizer". He developed it after working on Disney's computer animated sci-fi motion picture Tron (1982) for the animation company Mathematical Applications Group (MAGI). In 1997, Perlin was awarded an Academy Award for Technical Achievement for creating the algorithm, the citation for which read:

To Ken Perlin for the development of Perlin Noise, a technique used to produce natural appearing textures on computer generated surfaces for motion picture visual effects.
The development of Perlin Noise has allowed computer graphics artists to better represent the complexity of natural phenomena in visual effects for the motion picture industry.
Perlin did not apply for any patents on the algorithm, but in 2001 he was granted a patent for the use of 3D+ implementations of simplex noise for texture synthesis. Simplex noise has the same purpose of Perlin noise, but uses a simpler space-filling grid and produces less grid-shaped artifacts.


== Uses ==

Perlin noise is a procedural texture primitive, a type of gradient noise used by visual effects artists to increase the appearance of realism in computer graphics. The function has a pseudo-random appearance that causes all details created to stay the same size. This property allows it to be controllable; multiple scaled copies of Perlin noise can be inserted into mathematical expressions to create various procedural textures. Synthetic textures using Perlin noise are often used in CGI to make computer-generated visual elements appear more natural, by imitating the controlled random appearance of textures in nature.

It is also frequently used to generate textures when memory is limited, such as in demos.  Its successors, such as fractal noise and simplex noise, have become popular in graphics processing units both for real-time graphics and for non-real-time procedural textures in computer graphics. It is also frequently used in video games to make procedurally generated terrain that looks natural.


== Algorithm detail ==

Perlin noise is most commonly implemented as a two-, three- or four-dimensional function, but can be defined for any number of dimensions.  An implementation typically involves three steps: defining a grid of random gradient vectors, computing the dot product between the gradient vectors and their offsets, and interpolation between these values.

Define an n-dimensional grid where each grid intersection has associated with it a fixed random n-dimensional unit-length gradient vector, except in the one dimensional case where the gradients are random scalars between −1 and 1.

To work out the value of any candidate point, the unique grid cell in which the point lies is found. The 2n corners of that cell and their associated gradient vectors is identified. For each corner, an offset vector (a displacement vector from that corner to the candidate point) is calculated, and the dot product between its gradient vector and the offset vector is computed. This dot product will be zero if the candidate point is exactly at the grid corner.
For a point in a two-dimensional grid, this requires the computation of four offset vectors and dot products, while in three dimensions it requires eight offset vectors and eight dot products. In general, the algorithm has O(2n) complexity in n dimensions.

The final step is interpolation between the 2n dot products. Interpolation is performed using a function that has zero first derivative (and possibly also second derivative) at the 2n grid nodes. Therefore, at points close to the grid nodes, the output will approximate the dot product of the gradient vector of the node and the offset vector to the node. This means that the noise function will pass through 0 at every node, giving Perlin noise its characteristic look.
If n = 1, an example of a function that interpolates between value a0 at grid node 0 and value a1 at grid node 1 is

  
    
      
        f
        (
        x
        )
        =
        
          a
          
            0
          
        
        +
        smoothstep
        ⁡
        (
        x
        )
        ⋅
        (
        
          a
          
            1
          
        
        −
        
          a
          
            0
          
        
        )
        
        
          for 
        
        0
        ≤
        x
        ≤
        1
      
    
    {\displaystyle f(x)=a_{0}+\operatorname {smoothstep} (x)\cdot (a_{1}-a_{0})\quad {\text{for }}0\leq x\leq 1}
  

where the smoothstep function was used.
Noise functions for use in computer graphics typically produce values in the range [–1.0, 1.0] and can be scaled accordingly.


== Gradient permutation ==
In Ken Perlin's original implementation he used a simple hashing scheme to determine what gradient vector is associated with each grid intersection. A pre-computed permutation table is used to turn a given grid coordinate into a random number. The original implementation worked on a 256-node grid and so included the following permutation table:

This specific permutation is not absolutely required, though it does require a randomized array of the integers 0 to 255. If creating a new permutation table, care should be taken to ensure uniform distribution of the values.
To get a gradient vector using the permutation table the coordinates of a grid point are looked up sequentially in the permutation table adding the value of each coordinate to the permutation of the previous coordinate. So for example the original implementation did this in 3D as follows:

The algorithm then looks at the bottom 4 bits of the hash output to pick 1 of 12 gradient vectors for that grid point.


== Complexity ==
For each evaluation of the noise function, the dot product of the position and gradient vectors must be evaluated at each node of the containing grid cell. Perlin noise therefore scales with complexity O(2n) for n dimensions.  Alternatives to Perlin noise producing similar results with improved complexity scaling include simplex noise and OpenSimplex noise.


== References ==


== External links ==

Matt Zucker's Perlin noise math FAQ 
Jason Bevins's extensive C++ library for generating complex, coherent noise values
PHP Implementation (GitHub)
Perlin Noise Explained in Depth (with C++ source code)
The Book of Shaders by Patricio Gonzalez Vivo & Jen Lowe
Python package to create Perlin noise
Random terrain generation and perlin noise with SDL
