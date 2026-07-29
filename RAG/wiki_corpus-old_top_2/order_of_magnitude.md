# Order of magnitude

> **Query Topic**: order of magnitude (Rank #1 Search Result)  
> **Source Queue**: train (Row ID: 225, Frequency: 15)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Order_of_magnitude

---

In a ratio scale based on powers of ten, the order of magnitude is a measure of the nearness of two figures. Two numbers are "within an order of magnitude" of each other if the ratio of the greater to the lesser is between 1 and 10. In other words, the two numbers are within about a factor of 10 of each other.
For example, 1 and 1.02 are within an order of magnitude, as well as 1 and 2, 1 and 9, and 1 and 0.2. However, 1 and 15 are not within an order of magnitude, since their ratio is 15/1 = 15 > 10. The reciprocal ratio, 1/15, is less than 0.1, so the same result is obtained.
Differences in order of magnitude can be measured on a base-10 logarithmic scale in "decades" (i.e., factors of ten). For example, there is one order of magnitude between 2 and 20, and two orders of magnitude between 2 and 200.  Each division or multiplication by 10 is called an order of magnitude. 
This phrasing helps quickly express the difference in scale between 2 and 2,000,000: they differ by 6 orders of magnitude.
Examples of numbers of different magnitudes can be found at Orders of magnitude (numbers).
Below are examples of different methods of partitioning the real numbers into specific "orders of magnitude" for various purposes. There is not one single accepted way of doing this, and different partitions may be easier to compute but less useful for approximation, or better for approximation but more difficult to compute.


== Calculating the order of magnitude ==
Generally, the order of magnitude of a number is the smallest power of 10 used to represent that number. To work out the order of magnitude of a number 
  
    
      
        n
      
    
    {\displaystyle n}
  
, the number is first expressed in the following form:

  
    
      
        n
        =
        a
        ×
        
          10
          
            b
          
        
      
    
    {\displaystyle n=a\times 10^{b}}
  

where 
  
    
      
        
          
            1
            
              10
            
          
        
        ≤
        a
        <
        
          
            10
          
        
      
    
    {\displaystyle {\frac {1}{\sqrt {10}}}\leq a<{\sqrt {10}}}
  
, or approximately 
  
    
      
        0.316
        ≲
        a
        ≲
        3.16
      
    
    {\displaystyle 0.316\lesssim a\lesssim 3.16}
  
. Then, 
  
    
      
        b
      
    
    {\displaystyle b}
  
 represents the order of magnitude of the number. The order of magnitude can be any integer. The table below enumerates the order of magnitude of some numbers using this definition:

The geometric mean of 
  
    
      
        
          10
          
            b
            −
            1
            
              /
            
            2
          
        
      
    
    {\displaystyle 10^{b-1/2}}
  
 and 
  
    
      
        
          10
          
            b
            +
            1
            
              /
            
            2
          
        
      
    
    {\displaystyle 10^{b+1/2}}
  
 is 
  
    
      
        
          10
          
            b
          
        
      
    
    {\displaystyle 10^{b}}
  
, meaning that a value of exactly 
  
    
      
        
          10
          
            b
          
        
      
    
    {\displaystyle 10^{b}}
  
 (i.e., 
  
    
      
        a
        =
        1
      
    
    {\displaystyle a=1}
  
) represents a geometric halfway point within the range of possible values of 
  
    
      
        a
      
    
    {\displaystyle a}
  
.
Some use a simpler definition where 
  
    
      
        0.5
        ≤
        a
        <
        5
      
    
    {\displaystyle 0.5\leq a<5}
  
. This definition has the effect of lowering the values of 
  
    
      
        b
      
    
    {\displaystyle b}
  
 slightly:


== Uses ==
Orders of magnitude are used to make approximate comparisons.  If numbers differ by one order of magnitude, one number is about 10 times larger than the other.  If values differ by two orders of magnitude, they differ by a factor of about 100. Two numbers of the same order of magnitude have roughly the same scale: the larger value is less than ten times the smaller value. The growing amounts of Internet data have led to addition of new SI prefixes over time, most recently in 2022.


=== Calculating the order of magnitude by truncation ===
The order of magnitude of a number is, intuitively speaking, the number of digits in it which are above the ones place.  More precisely, the order of magnitude of a number can be defined in terms of the common logarithm, usually as the integer part of the logarithm, obtained by truncation. For example, the number 4000000 has a logarithm (in base 10) of 6.602; its order of magnitude is 6.  When truncating, a number of this order of magnitude is between 106 and 107. In a similar example, with the phrase "seven-figure income", the order of magnitude is the number of figures minus one, so it is very easily determined without a calculator to be 6. An order of magnitude is an approximate position on a logarithmic scale.


=== Order-of-magnitude estimate ===
An order-of-magnitude estimate of a variable, whose precise value is unknown, is an estimate rounded to the nearest power of ten.  For example, an order-of-magnitude estimate for a variable between about 3 billion and 30 billion (such as the human population of the Earth) is 10 billion. To round a number to its nearest order of magnitude, one rounds its logarithm to the nearest integer.  Thus 4000000, which has a logarithm (in base 10) of 6.602, has 7 as its nearest order of magnitude, because "nearest" implies rounding rather than truncation.  For a number written in scientific notation, this logarithmic rounding scale requires rounding up to the next power of ten when the multiplier is greater than the square root of ten (about 3.162). For example, the nearest order of magnitude for 1.7×108 is 8, whereas the nearest order of magnitude for 3.7×108 is 9. An order-of-magnitude estimate is sometimes also called a zeroth order approximation.


=== Orders of magnitude lists ===
Orders of magnitude (acceleration)
Orders of magnitude (area)
Orders of magnitude (bit rate)
Orders of magnitude (current)
Orders of magnitude (data)
Orders of magnitude (energy)
Orders of magnitude (force)
Orders of magnitude (frequency)
Orders of magnitude (illuminance)
Orders of magnitude (length)
Orders of magnitude (mass)
Orders of magnitude (numbers)
Orders of magnitude (power)
Orders of magnitude (pressure)
Orders of magnitude (radiation)
Orders of magnitude (speed)
Orders of magnitude (temperature)
Orders of magnitude (time)
Orders of magnitude (voltage)
Orders of magnitude (volume)


== Non-decimal orders of magnitude ==

An order of magnitude is an approximation of the logarithm of a value relative to some contextually understood reference value, usually 10, interpreted as the base of the logarithm and the representative of values of magnitude one. Logarithmic distributions are common in nature and considering the order of magnitude of values sampled from such a distribution can be more intuitive. When the reference value is 10, the order of magnitude can be understood as the number of digits minus one in the base-10 representation of the value. Similarly, if the reference value is one of some powers of 2 since computers store data in a binary format, the magnitude can be understood in terms of the amount of computer memory needed to store that value.


=== Irrational orders of magnitude ===
Other orders of magnitude may be calculated using bases other than integers. In the field of astronomy, the nighttime brightnesses of celestial bodies are ranked by "magnitudes" in which each increasing level is brighter by a factor of 
  
    
      
        
          
            100
            
              5
            
          
        
        ≈
        2.512
      
    
    {\displaystyle {\sqrt[{5}]{100}}\approx 2.512}
  
 greater than the previous level. Thus, a level being 5 magnitudes brighter than another indicates that it is a factor of 
  
    
      
        (
        
          
            100
            
              5
            
          
        
        
          )
          
            5
          
        
        =
        100
      
    
    {\displaystyle ({\sqrt[{5}]{100}})^{5}=100}
  
 times brighter: that is, two base 10 orders of magnitude. 
This series of magnitudes forms a logarithmic scale with a base of 
  
    
      
        
          
            100
            
              5
            
          
        
      
    
    {\displaystyle {\sqrt[{5}]{100}}}
  
.


=== Base 1,000,000 orders of magnitude ===
The different decimal numeral systems of the world use a larger base to better envision the size of the number, and have created names for the powers of this larger base. The table shows  what number the order of magnitude aim at for base 10 and for base 1000000. It can be seen that the order of magnitude is included in the number name in this example, because bi- means 2, tri- means 3, etc. (these make sense in the long scale only), and the suffix -illion tells that the base is 1000000. But the number names billion, trillion themselves (here with other meaning than in the first chapter) are not names of the orders of magnitudes, they are names of "magnitudes", that is the numbers 1000000000000 etc.

SI units in the table at right are used together with SI prefixes, which were devised with mainly base 1000 magnitudes in mind. The IEC standard prefixes with base 1024 were invented for use in electronic technology.


== See also ==
Big O notation
Decibel
Mathematical operators and symbols in Unicode
Names of large numbers
Names of small numbers
Number sense
Powers of Ten
Scientific notation
Unicode symbols for CJK Compatibility includes SI Unit symbols
Valuation (algebra), an algebraic generalization of "order of magnitude"
Scale (analytical tool)


== References ==


== Further reading ==
Asimov, Isaac, The Measure of the Universe (1983).


== External links ==
The Scale of the Universe 2  Interactive tool from Planck length 10−35 meters to universe size 1027
Cosmos – an Illustrated Dimensional Journey from microcosmos to macrocosmos – from Digital Nature Agency
Powers of 10, a graphic animated illustration that starts with a view of the Milky Way at 1023 meters and ends with subatomic particles at 10−16 meters.
What is Order of Magnitude?
