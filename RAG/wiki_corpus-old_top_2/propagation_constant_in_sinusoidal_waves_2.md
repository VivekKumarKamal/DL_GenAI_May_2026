# Sine wave

> **Query Topic**: propagation constant in sinusoidal waves (Rank #2 Search Result)  
> **Source Queue**: train (Row ID: 192, Frequency: 12)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Sine_wave

---

A sine wave, sinusoidal wave, or sinusoid (symbol: ∿) is a periodic wave whose waveform (shape) is the trigonometric sine function. In mechanics, as a linear motion over time, this is simple harmonic motion; as rotation, it corresponds to uniform circular motion. Sine waves occur often in physics, including wind waves, sound waves, and light waves, such as monochromatic radiation. In engineering, signal processing, and mathematics, Fourier analysis decomposes general functions into a sum of sine waves of various frequencies, relative phases, and magnitudes.
When any two sine waves of the same frequency (but arbitrary phase) are linearly combined, the result is another sine wave of the same frequency; this property is unique among periodic waves. Conversely, if some phase is chosen as a zero reference, a sine wave of arbitrary phase can be written as the linear combination of two sine waves with phases of zero and a quarter cycle, the sine and cosine components, respectively.


== Audio example ==

A sine wave represents a single frequency with no harmonics and is considered an acoustically pure tone. Adding sine waves of different frequencies results in a different waveform. Presence of higher harmonics in addition to the fundamental causes variation in the timbre, which is the reason why the same musical pitch played on different instruments sounds different.


== Sinusoid form ==
Sine waves of arbitrary phase and amplitude are called sinusoids and have the general form:

  
    
      
        y
        (
        t
        )
        =
        A
        sin
        ⁡
        (
        ω
        t
        +
        φ
        )
        =
        A
        sin
        ⁡
        (
        2
        π
        f
        t
        +
        φ
        )
      
    
    {\displaystyle y(t)=A\sin(\omega t+\varphi )=A\sin(2\pi ft+\varphi )}
  

where:

  
    
      
        A
      
    
    {\displaystyle A}
  
, amplitude, the peak deviation of the function from zero.

  
    
      
        t
      
    
    {\displaystyle t}
  
, the real independent variable, usually representing time in seconds.

  
    
      
        ω
      
    
    {\displaystyle \omega }
  
, angular frequency, the rate of change of the function argument in units of radians per second.

  
    
      
        f
      
    
    {\displaystyle f}
  
, ordinary frequency, the number of oscillations (cycles) that occur each second of time.

  
    
      
        φ
      
    
    {\displaystyle \varphi }
  
, phase, specifies (in radians) where in its cycle the oscillation is at t = 0.
When 
  
    
      
        φ
      
    
    {\displaystyle \varphi }
  
 is non-zero, the entire waveform appears to be shifted backwards in time by the amount 
  
    
      
        
          
            
              φ
              ω
            
          
        
      
    
    {\displaystyle {\tfrac {\varphi }{\omega }}}
  
 seconds. A negative value represents a delay, and a positive value represents an advance.
Adding or subtracting 
  
    
      
        2
        π
      
    
    {\displaystyle 2\pi }
  
 (one cycle) to the phase results in an equivalent wave.


== As a function of both position and time ==

Sinusoids that exist in both position and time also have:

a spatial variable 
  
    
      
        x
      
    
    {\displaystyle x}
  
 that represents the position on the dimension on which the wave propagates.
a wave number (or angular wave number) 
  
    
      
        k
      
    
    {\displaystyle k}
  
, which represents the proportionality between the angular frequency 
  
    
      
        ω
      
    
    {\displaystyle \omega }
  
 and the linear speed (speed of propagation) 
  
    
      
        v
      
    
    {\displaystyle v}
  
:
wavenumber is related to the angular frequency by 
  
    
      
        k
        
          =
        
        
          
            ω
            v
          
        
        
          =
        
        
          
            
              2
              π
              f
            
            v
          
        
        
          =
        
        
          
            
              2
              π
            
            λ
          
        
      
    
    {\textstyle k{=}{\frac {\omega }{v}}{=}{\frac {2\pi f}{v}}{=}{\frac {2\pi }{\lambda }}}
  
 where 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
 (lambda) is the wavelength.
Depending on their direction of travel, they can take the form:

  
    
      
        y
        (
        x
        ,
        t
        )
        =
        A
        sin
        ⁡
        (
        k
        x
        −
        ω
        t
        +
        φ
        )
      
    
    {\displaystyle y(x,t)=A\sin(kx-\omega t+\varphi )}
  
, if the wave is moving to the right, or

  
    
      
        y
        (
        x
        ,
        t
        )
        =
        A
        sin
        ⁡
        (
        k
        x
        +
        ω
        t
        +
        φ
        )
      
    
    {\displaystyle y(x,t)=A\sin(kx+\omega t+\varphi )}
  
, if the wave is moving to the left.
Since sine waves propagate without changing form in distributed linear systems, they are often used to analyze wave propagation.


=== Standing waves ===

When two waves with the same amplitude and frequency traveling in opposite directions superpose each other, then a standing wave pattern is created.
On a plucked string, the superimposing waves are the waves reflected from the fixed endpoints of the string. The string's resonant frequencies are the string's only possible standing waves, which only occur for wavelengths that are twice the string's length (corresponding to the fundamental frequency) and integer divisions of that (corresponding to higher harmonics).


=== Multiple spatial dimensions ===
The earlier equation gives the displacement 
  
    
      
        y
      
    
    {\displaystyle y}
  
 of the wave at a position 
  
    
      
        x
      
    
    {\displaystyle x}
  
 at time 
  
    
      
        t
      
    
    {\displaystyle t}
  
 along a single line. This could, for example, be considered the value of a wave along a wire.
In two or three spatial dimensions, the same equation describes a travelling plane wave if position 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and wavenumber 
  
    
      
        k
      
    
    {\displaystyle k}
  
 are interpreted as vectors, and their product as a dot product. For more complex waves such as the height of a water wave in a pond after a stone has been dropped in, more complex equations are needed.


==== Sinusoidal plane wave ====


== Fourier analysis ==

French mathematician Joseph Fourier discovered that sinusoidal waves can be summed as simple building blocks to approximate any periodic waveform, including square waves. These Fourier series are frequently used in signal processing and the statistical analysis of time series. The Fourier transform then extended Fourier series to handle general functions, and birthed the field of Fourier analysis.


== Differentiation and integration ==


=== Differentiation ===
Differentiating any sinusoid with respect to time can be viewed as multiplying its amplitude by its angular frequency and advancing it by a quarter cycle:

  
    
      
        
          
            
              
                
                  
                    d
                    
                      d
                      t
                    
                  
                
                [
                A
                sin
                ⁡
                (
                ω
                t
                +
                φ
                )
                ]
              
              
                
                =
                A
                ω
                cos
                ⁡
                (
                ω
                t
                +
                φ
                )
              
            
            
              
              
                
                =
                A
                ω
                sin
                ⁡
                (
                ω
                t
                +
                φ
                +
                
                  
                    
                      π
                      2
                    
                  
                
                )
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\frac {d}{dt}}[A\sin(\omega t+\varphi )]&=A\omega \cos(\omega t+\varphi )\\&=A\omega \sin(\omega t+\varphi +{\tfrac {\pi }{2}})\,.\end{aligned}}}
  

A differentiator has a zero at the origin of the complex frequency plane. The gain of its frequency response increases at a rate of +20 dB per decade of frequency (for root-power quantities), the same positive slope as a 1st order high-pass filter's stopband, although a differentiator does not have a cutoff frequency or a flat passband. A nth-order high-pass filter approximately applies the nth time derivative of signals whose frequency band is significantly lower than the filter's cutoff frequency.


=== Integration ===
Integrating any sinusoid with respect to time can be viewed as dividing its amplitude by its angular frequency and delaying it a quarter cycle:

  
    
      
        
          
            
              
                ∫
                A
                sin
                ⁡
                (
                ω
                t
                +
                φ
                )
                d
                t
              
              
                
                =
                −
                
                  
                    A
                    ω
                  
                
                cos
                ⁡
                (
                ω
                t
                +
                φ
                )
                +
                C
              
            
            
              
              
                
                =
                −
                
                  
                    A
                    ω
                  
                
                sin
                ⁡
                (
                ω
                t
                +
                φ
                +
                
                  
                    
                      π
                      2
                    
                  
                
                )
                +
                C
              
            
            
              
              
                
                =
                
                  
                    A
                    ω
                  
                
                sin
                ⁡
                (
                ω
                t
                +
                φ
                −
                
                  
                    
                      π
                      2
                    
                  
                
                )
                +
                C
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\int A\sin(\omega t+\varphi )dt&=-{\frac {A}{\omega }}\cos(\omega t+\varphi )+C\\&=-{\frac {A}{\omega }}\sin(\omega t+\varphi +{\tfrac {\pi }{2}})+C\\&={\frac {A}{\omega }}\sin(\omega t+\varphi -{\tfrac {\pi }{2}})+C\,.\end{aligned}}}
  

The constant of integration 
  
    
      
        C
      
    
    {\displaystyle C}
  
 will be zero if the bounds of integration is an integer multiple of the sinusoid's period.
An integrator has a pole at the origin of the complex frequency plane. The gain of its frequency response falls off at a rate of -20 dB per decade of frequency (for root-power quantities), the same negative slope as a 1st order low-pass filter's stopband, although an integrator does not have a cutoff frequency or a flat passband. A nth-order low-pass filter approximately performs the nth time integral of signals whose frequency band is significantly higher than the filter's cutoff frequency.


== See also ==


== References ==


== External links ==
"Sine Wave". Mathematical Mysteries. 2021-11-17. Retrieved 2022-09-30.
