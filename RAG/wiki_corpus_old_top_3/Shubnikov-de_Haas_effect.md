# Shubnikov–de Haas effect

> **Query Topic**: De Haas-Van Alphen effect (Rank #2 Search Result)
> **Source Queue**: train (Row ID: 143, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Shubnikov–de_Haas_effect

---

An oscillation in the conductivity of a material that occurs at low temperatures in the presence of very intense magnetic fields, the Shubnikov–de Haas effect (SdH) is a macroscopic manifestation of the inherent quantum mechanical nature of matter. It is often used to determine the effective mass of charge carriers (electrons and electron holes), allowing investigators to distinguish among majority and minority carrier populations. 
The effect is named after Wander Johannes de Haas and Lev Shubnikov.


== Physical process ==
At sufficiently low temperatures and high magnetic fields, the free electrons in the conduction band of a metal, semimetal, or narrow band gap semiconductor will behave like simple harmonic oscillators.  When the magnetic field strength is changed, the oscillation period of the simple harmonic oscillators changes proportionally.  The resulting energy spectrum is made up of Landau levels separated by the cyclotron energy.  These Landau levels are further split by the Zeeman energy. In each Landau level the cyclotron and Zeeman energies and the number of electron states (eB/h) all increase linearly with increasing magnetic field. Thus, as the magnetic field increases, the spin-split Landau levels move to higher energy. As each energy level passes through the Fermi energy, it depopulates as the electrons become free to flow as current. This causes the material's transport and thermodynamic properties to oscillate periodically, producing a measurable oscillation in the material's conductivity.  Since the transition across the Fermi 'edge' spans a small range of energies, the waveform is square rather than sinusoidal, with the shape becoming ever more square as the temperature is lowered.


== Theory ==
Consider a two-dimensional quantum gas of electrons confined in a sample with given width and with edges. In the presence of a magnetic flux density B, the energy eigenvalues of this system are described by Landau levels. As shown in Fig 1, these levels are equidistant along the vertical axis. Each energy level is substantially flat inside a sample (see Fig 1). At the edges of a sample, the work function bends levels upwards.

Fig 1 shows the Fermi energy EF located in between two Landau levels. Electrons become mobile as their energy levels cross the Fermi energy EF. With the Fermi energy EF in between two Landau levels, scattering of electrons will occur only at the edges of a sample where the levels are bent. The corresponding electron states are commonly referred to as edge channels.
The Landauer–Büttiker approach is used to describe transport of electrons in this particular sample. The Landauer–Büttiker approach allows calculation of net currents Im flowing between a number of contacts 1 ≤ m ≤ n. In its simplified form, the net current Im of contact m with chemical potential μm reads

where e denotes the electron charge, h denotes the Planck constant, and i stands for the number of edge channels. The matrix Tml denotes the probability of transmission of a negatively charged particle (i.e. of an electron) from a contact l ≠ m to another contact m. The net current Im in relationship (1) is made up of the currents towards contact m and of the current transmitted from the contact m to all other contacts l ≠ m . That current equals the voltage μm / e of contact m multiplied with the Hall conductivity of  2e2 / h per edge channel. 

Fig 2 shows a sample with four contacts. To drive a current through the sample, a voltage is applied between the contacts 1 and 4. A voltage is measured between the contacts 2 and 3. Suppose electrons leave the 1st contact, then are transmitted from contact 1 to contact 2, then from contact 2 to contact 3, then from contact 3 to contact 4, and finally from contact 4 back to contact 1. A negative charge (i.e. an electron) transmitted from contact 1 to contact 2 will result in a current from contact 2 to contact 1. An electron transmitted from contact 2 to contact 3 will result in a current from contact 3 to contact 2 etc. Suppose also that no electrons are transmitted along any further paths. The probabilities of transmission of ideal contacts then read

  
    
      
        
          T
          
            21
          
        
        =
        
          T
          
            32
          
        
        =
        
          T
          
            43
          
        
        =
        
          T
          
            14
          
        
        =
        1
        ,
      
    
    {\displaystyle T_{21}=T_{32}=T_{43}=T_{14}=1,}
  

and

  
    
      
        
          T
          
            m
            l
          
        
        =
        0
      
    
    {\displaystyle T_{ml}=0}
  

otherwise. With these probabilities, the currents I1 ... I4 through the four contacts, and with their chemical potentials μ1 ... μ4, equation (1) can be re-written

  
    
      
        
          (
          
            
              
                
                  
                    I
                    
                      1
                    
                  
                
              
              
                
                  
                    I
                    
                      2
                    
                  
                
              
              
                
                  
                    I
                    
                      3
                    
                  
                
              
              
                
                  
                    I
                    
                      4
                    
                  
                
              
            
          
          )
        
        =
        
          
            
              2
              e
              ⋅
              i
            
            h
          
        
        
          (
          
            
              
                
                  1
                
                
                  0
                
                
                  0
                
                
                  −
                  1
                
              
              
                
                  −
                  1
                
                
                  1
                
                
                  0
                
                
                  0
                
              
              
                
                  0
                
                
                  −
                  1
                
                
                  1
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  −
                  1
                
                
                  1
                
              
            
          
          )
        
        
          (
          
            
              
                
                  
                    μ
                    
                      1
                    
                  
                
              
              
                
                  
                    μ
                    
                      2
                    
                  
                
              
              
                
                  
                    μ
                    
                      3
                    
                  
                
              
              
                
                  
                    μ
                    
                      4
                    
                  
                
              
            
          
          )
        
        .
      
    
    {\displaystyle \left({\begin{matrix}I_{1}\\I_{2}\\I_{3}\\I_{4}\end{matrix}}\right)={\frac {2e\cdot i}{h}}\left({\begin{matrix}1&0&0&-1\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{matrix}}\right)\left({\begin{matrix}\mu _{1}\\\mu _{2}\\\mu _{3}\\\mu _{4}\end{matrix}}\right).}
  

A voltage is measured between contacts 2 and 3. The voltage measurement should ideally not involve a flow of current through the meter, so I2 = I3 = 0. It follows that

  
    
      
        
          I
          
            3
          
        
        =
        0
        =
        
          
            
              2
              e
              ⋅
              i
            
            h
          
        
        
          (
          
            −
            
              μ
              
                2
              
            
            +
            
              μ
              
                3
              
            
          
          )
        
        ,
      
    
    {\displaystyle I_{3}=0={\frac {2e\cdot i}{h}}\left(-\mu _{2}+\mu _{3}\right),}
  

  
    
      
        
          μ
          
            2
          
        
        =
        
          μ
          
            3
          
        
        .
      
    
    {\displaystyle \mu _{2}=\mu _{3}.}
  

In other words, the chemical potentials μ2 and μ3 and their respective voltages μ2 / e and μ3 / e are the same. As a consequence of no drop of voltage between the contacts 2 and 3, the current I1 experiences zero resistivity RSdH in between contacts 2 and 3

  
    
      
        
          R
          
            
              S
              d
              H
            
          
        
        =
        
          
            
              
                μ
                
                  2
                
              
              −
              
                μ
                
                  3
                
              
            
            
              e
              ⋅
              
                I
                
                  1
                
              
            
          
        
        =
        0.
      
    
    {\displaystyle R_{\mathrm {SdH} }={\frac {\mu _{2}-\mu _{3}}{e\cdot I_{1}}}=0.}
  

The result of zero resistivity between the contacts 2 and 3 is a consequence of the electrons being mobile only in the edge channels of the sample. The situation would be different if a Landau level came close to the Fermi energy EF. Any electrons in that level would become mobile as their energy approaches the Fermi energy EF. Consequently, scatter would lead to  RSdH > 0. In other words, the above approach yields zero resistivity whenever the Landau levels are positioned such that the Fermi energy  EF is in between two levels.


== Applications ==
Shubnikov–De Haas oscillations can be used to determine the two-dimensional electron density of a sample. For a given magnetic flux 
  
    
      
        Φ
      
    
    {\displaystyle \Phi }
  
 the maximum number D of electrons with spin S = 1/2 per Landau level  is

Upon insertion of the expressions for the flux quantum Φ0 = h / e and for the magnetic flux Φ = BA relationship (2) reads

  
    
      
        D
        =
        2
        
          
            
              e
              B
              A
            
            h
          
        
      
    
    {\displaystyle D=2{\frac {eBA}{h}}}
  

Let N denote the maximum number of states per unit area, so D = NA and

  
    
      
        N
        =
        2
        
          
            
              e
              B
            
            h
          
        
        .
      
    
    {\displaystyle N=2{\frac {eB}{h}}.}
  

Now let each Landau level correspond to an edge channel of the above sample. For a given number i of edge channels each filled with N electrons per unit area, the overall number n of electrons per unit area will read

  
    
      
        n
        =
        i
        N
        =
        2
        i
        
          
            
              e
              B
            
            h
          
        
        .
      
    
    {\displaystyle n=iN=2i{\frac {eB}{h}}.}
  

The overall number n of electrons per unit area is commonly referred to as the electron density of a sample. No electrons disappear from the sample into the unknown, so the electron density n is constant. It follows that

  
    
      
        
          B
          
            i
          
        
        =
        
          
            
              n
              h
            
            
              2
              e
              i
            
          
        
        ,
      
    
    {\displaystyle B_{i}={\frac {nh}{2ei}},}
  

  
    
      
        
          
            1
            
              B
              
                i
              
            
          
        
        =
        
          
            
              2
              e
              i
            
            
              n
              h
            
          
        
        ,
      
    
    {\displaystyle {\frac {1}{B_{i}}}={\frac {2ei}{nh}},}
  

For a given sample, all factors including the electron density n on the right hand side of relationship (3) are constant. When plotting the index i of an edge channel versus the reciprocal of its magnetic flux density 1/Bi, one obtains a straight line with slope 2e/(nh). Since the electron charge e is known and also the Planck constant h, one can derive the electron density n of a sample from this plot.
Shubnikov–De Haas oscillations are observed in highly doped Bi2Se3. Fig 3 shows the reciprocal magnetic flux density 1/Bi of the 10th to 14th minima of a Bi2Se3 sample. The slope of 0.00618/T as obtained from a linear fit yields the electron density n

  
    
      
        n
        =
        
          
            
              2
              e
            
            
              0.00618
              
                /
              
              
                T
              
              ⋅
              h
            
          
        
        ≈
        7.82
        ×
        
          10
          
            14
          
        
        
          /
        
        
          
            m
          
          
            2
          
        
        .
      
    
    {\displaystyle n={\frac {2e}{0.00618/\mathrm {T} \cdot h}}\approx 7.82\times 10^{14}/\mathrm {m} ^{2}.}
  

Shubnikov–de Haas oscillations can be used to map the Fermi surface of electrons in a sample, by determining the periods of oscillation for various applied field directions.


== Related physical process ==
The effect is related to the De Haas–Van Alphen effect, which is the name given to the corresponding oscillations in magnetization. The signature of each effect is a periodic waveform when plotted as a function of inverse magnetic field. The "frequency" of the magnetoresistance oscillations indicate areas of extremal orbits around the Fermi surface. The area of the Fermi surface is expressed in teslas. More accurately, the period in inverse Teslas is inversely proportional to the area of the extremal orbit of the Fermi surface in inverse m/cm.


== References ==

Schubnikow, L.; De Haas, W.J. (1930). "Magnetische Widerstandsvergrösserung in Einkristallen von Wismut bei tiefen Temperaturen" [Magnetic resistance increase in single crystals of bismuth at low temperatures] (PDF). Proceedings of the Royal Netherlands Academy of Arts and Science (in German). 33: 130–133.
Schubnikow, L.; De Haas, W.J. (1930). "Neue Erscheinungen bei der Widerstandsänderung von Wismuthkristallen im Magnetfeld bei der Temperatur von flüssigem Wasserstoff (I)" [New phenomena in the change in resistance of bismuth crystals in a magnetic field at the temperature of liquid hydrogen (I)] (PDF). Proceedings of the Royal Netherlands Academy of Arts and Science. 33: 363–378.
Schubnikow, L.; De Haas, W.J. (1930). "Neue Erscheinungen bei der Widerstandsänderung von Wismuthkristallen im Magnetfeld bei der Temperatur von flüssigem Wasserstoff (II)" (PDF). Proceedings of the Royal Netherlands Academy of Arts and Science. 33: 418–432.
Schubnikow, L.; De Haas, W.J. (1930). "Die Widerstandsänderung von Wismuthkristallen im Magnetfeld bei der Temperatur von flüssigem Stickstoff" [The change in resistance of bismuth crystals in a magnetic field at the temperature of liquid nitrogen] (PDF). Proceedings of the Royal Netherlands Academy of Arts and Science. 33: 433–439.


== External links ==
The article uses text from Shubnikov effect on Lang.gov Archived 2017-09-22 at the Wayback Machine that is a Public Domain as a work of a US government agency.
Material behavior in strong magnetic fields Archived 2006-09-03 at the Wayback Machine
