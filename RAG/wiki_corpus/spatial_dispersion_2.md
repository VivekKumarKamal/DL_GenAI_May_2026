# Spatial dispersion

> **Query Topic**: spatial dispersion (Rank #2 Search Result)  
> **Source Queue**: train (Row ID: 146, Frequency: 9)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Spatial_dispersion

---

In the physics of continuous media, spatial dispersion is a phenomenon where material parameters such as the permittivity or conductivity have dependence on wavevector. Normally such a dependence is assumed to be absent for simplicity, however spatial dispersion exists to varying degrees in all materials.
The underlying physical reason for the wavevector dependence is often that the material has some spatial structure smaller than the wavelength of any signals (such as light or sound) being considered. Since these small spatial structures cannot be resolved by the waves, only indirect effects (e.g. wavevector dependence) remain detectable. In such a case, although the light cannot resolve the individual atoms, they nevertheless can as an aggregate affect how the light propagates. Another common mechanism is that the (e.g.) light is coupled to an excitation of the material, such as a plasmon.
Spatial dispersion can be compared to temporal dispersion, the latter often just called dispersion. Temporal dispersion represents memory effects in systems, commonly seen in optics and electronics. Spatial dispersion on the other hand represents spreading effects and is usually significant only at microscopic length scales. Spatial dispersion contributes relatively small perturbations to optics, providing weak effects such as optical activity. Spatial dispersion and temporal dispersion may occur in the same system.
Spatial dispersion is also distinct from anisotropic effects like birefringence. In such phenomena, the effective material parameters felt by a wave depend on direction of the wavevector, but that can be entirely captured as a tensorial material parameter where the tensor components are independent of wavevector. By contrast, spatial dispersion means that the tensor parameter itself depends on the wavevector — its magnitude and (often) direction too.


== Origin: nonlocal response ==
The origin of spatial dispersion can be modelled as a nonlocal response, where response to a force field appears at many locations, and can appear even in locations where the force is zero. This usually arises due to a spreading of effects by the hidden microscopic degrees of freedom.
As an example, consider the current 
  
    
      
        J
        (
        x
        ,
        t
        )
      
    
    {\displaystyle J(x,t)}
  
 that is driven in response to an electric field 
  
    
      
        E
        (
        x
        ,
        t
        )
      
    
    {\displaystyle E(x,t)}
  
, which is varying in space (x) and time (t). Simplified laws such as Ohm's law would say that these are directly proportional to each other, 
  
    
      
        J
        =
        σ
        E
      
    
    {\displaystyle J=\sigma E}
  
, but this breaks down if the system has memory (temporal dispersion) or spreading (spatial dispersion). The most general linear response is given by:

  
    
      
        J
        (
        x
        ,
        t
        )
        =
        
          ∫
          
            −
            ∞
          
          
            −
            ∞
          
        
        d
        
          x
          ′
        
        
          ∫
          
            −
            ∞
          
          
            −
            ∞
          
        
        d
        
          t
          ′
        
        
        σ
        (
        x
        ,
        
          x
          ′
        
        ,
        t
        ,
        
          t
          ′
        
        )
        E
        (
        
          x
          ′
        
        ,
        
          t
          ′
        
        )
        ,
      
    
    {\displaystyle J(x,t)=\int _{-\infty }^{-\infty }dx'\int _{-\infty }^{-\infty }dt'\,\sigma (x,x',t,t')E(x',t'),}
  

where 
  
    
      
        σ
        (
        x
        ,
        
          x
          ′
        
        ,
        t
        ,
        
          t
          ′
        
        )
        d
        
          x
          ′
        
        
        d
        
          t
          ′
        
      
    
    {\displaystyle \sigma (x,x',t,t')dx'\,dt'}
  
 is the nonlocal conductivity function.
If the system is invariant in time (time translation symmetry) and invariant in space (space translation symmetry), then we can simplify because 
  
    
      
        σ
        (
        x
        ,
        
          x
          ′
        
        ,
        t
        ,
        
          t
          ′
        
        )
        =
        
          σ
          
            
              s
              y
              m
            
          
        
        (
        x
        −
        
          x
          ′
        
        ,
        t
        −
        
          t
          ′
        
        )
      
    
    {\displaystyle \sigma (x,x',t,t')=\sigma _{\rm {sym}}(x-x',t-t')}
  
 for some convolution kernel 
  
    
      
        
          σ
          
            
              s
              y
              m
            
          
        
      
    
    {\displaystyle \sigma _{\rm {sym}}}
  
. We can also consider plane wave solutions for 
  
    
      
        E
      
    
    {\displaystyle E}
  
 and 
  
    
      
        J
      
    
    {\displaystyle J}
  
 like so:

  
    
      
        J
        (
        x
        ,
        t
        )
        =
        Re
        ⁡
        (
        
          J
          
            0
          
        
        
          e
          
            i
            k
            x
            −
            i
            ω
            t
          
        
        )
      
    
    {\displaystyle J(x,t)=\operatorname {Re} (J_{0}e^{ikx-i\omega t})}
  

  
    
      
        E
        (
        x
        ,
        t
        )
        =
        Re
        ⁡
        (
        
          E
          
            0
          
        
        
          e
          
            i
            k
            x
            −
            i
            ω
            t
          
        
        )
      
    
    {\displaystyle E(x,t)=\operatorname {Re} (E_{0}e^{ikx-i\omega t})}
  

which yields a remarkably simple relationship between the two plane waves' complex amplitudes:

  
    
      
        
          J
          
            0
          
        
        =
        
          
            
              σ
              ~
            
          
        
        (
        k
        ,
        ω
        )
        
          E
          
            0
          
        
        .
      
    
    {\displaystyle J_{0}={\tilde {\sigma }}(k,\omega )E_{0}.}
  

where the function 
  
    
      
        
          
            
              σ
              ~
            
          
        
        (
        k
        ,
        ω
        )
      
    
    {\displaystyle {\tilde {\sigma }}(k,\omega )}
  
 is given by a Fourier transform of the space-time response function:

  
    
      
        
          
            
              σ
              ~
            
          
        
        (
        k
        ,
        ω
        )
        =
        
          ∫
          
            −
            ∞
          
          
            −
            ∞
          
        
        d
        
          x
          ″
        
        
          ∫
          
            −
            ∞
          
          
            −
            ∞
          
        
        d
        
          t
          ″
        
        
        
          e
          
            −
            i
            k
            
              x
              ″
            
            +
            i
            ω
            
              t
              ″
            
          
        
        
          σ
          
            
              s
              y
              m
            
          
        
        (
        
          x
          ″
        
        ,
        
          t
          ″
        
        )
        .
      
    
    {\displaystyle {\tilde {\sigma }}(k,\omega )=\int _{-\infty }^{-\infty }dx''\int _{-\infty }^{-\infty }dt''\,e^{-ikx''+i\omega t''}\sigma _{\rm {sym}}(x'',t'').}
  

The conductivity function 
  
    
      
        
          
            
              σ
              ~
            
          
        
        (
        k
        ,
        ω
        )
      
    
    {\displaystyle {\tilde {\sigma }}(k,\omega )}
  
 has spatial dispersion if it is dependent on the wavevector k. This occurs if the spatial function 
  
    
      
        
          σ
          
            
              s
              y
              m
            
          
        
        (
        x
        −
        
          x
          ′
        
        ,
        t
        −
        
          t
          ′
        
        )
      
    
    {\displaystyle \sigma _{\rm {sym}}(x-x',t-t')}
  
 is not pointlike (delta function) response in x-x' .


== Spatial dispersion in electromagnetism ==
In electromagnetism, spatial dispersion plays a role in a few material effects such as optical activity and doppler broadening. Spatial dispersion also plays an important role in the understanding of electromagnetic metamaterials. Most commonly, the spatial dispersion in permittivity ε is of interest.


=== Crystal optics ===
Inside crystals there may be a combination of spatial dispersion, temporal dispersion, and anisotropy. The constitutive relation for the polarization vector can be written as:

  
    
      
        
          P
          
            i
          
        
        (
        
          
            
              k
              →
            
          
        
        ,
        ω
        )
        =
        
          ∑
          
            j
          
        
        (
        
          ϵ
          
            i
            j
          
        
        (
        
          
            
              k
              →
            
          
        
        ,
        ω
        )
        −
        
          ϵ
          
            0
          
        
        
          δ
          
            i
            j
          
        
        )
        
          E
          
            j
          
        
        (
        
          
            
              k
              →
            
          
        
        ,
        ω
        )
        ,
      
    
    {\displaystyle P_{i}({\vec {k}},\omega )=\sum _{j}(\epsilon _{ij}({\vec {k}},\omega )-\epsilon _{0}\delta _{ij})E_{j}({\vec {k}},\omega ),}
  

i.e., the permittivity is a wavevector- and frequency-dependent tensor.
Considering Maxwell's equations, one can find the plane wave normal modes inside such crystals. These occur when the following relationship is satisfied for a nonzero electric field vector 
  
    
      
        
          
            
              E
              →
            
          
        
      
    
    {\displaystyle {\vec {E}}}
  
:

  
    
      
        
          ω
          
            2
          
        
        
          μ
          
            0
          
        
        ϵ
        (
        
          
            
              k
              →
            
          
        
        ,
        ω
        )
        
          
            
              E
              →
            
          
        
        −
        (
        
          
            
              k
              →
            
          
        
        ⋅
        
          
            
              k
              →
            
          
        
        )
        
          
            
              E
              →
            
          
        
        +
        (
        
          
            
              k
              →
            
          
        
        ⋅
        
          
            
              E
              →
            
          
        
        )
        
          
            
              k
              →
            
          
        
        =
        0.
      
    
    {\displaystyle \omega ^{2}\mu _{0}\epsilon ({\vec {k}},\omega ){\vec {E}}-({\vec {k}}\cdot {\vec {k}}){\vec {E}}+({\vec {k}}\cdot {\vec {E}}){\vec {k}}=0.}
  

Spatial dispersion in 
  
    
      
        ϵ
        (
        
          
            
              k
              →
            
          
        
        ,
        ω
        )
      
    
    {\displaystyle \epsilon ({\vec {k}},\omega )}
  
 can lead to strange phenomena, such as the existence of multiple modes at the same frequency and wavevector direction, but with different wavevector magnitudes.
Nearby crystal surfaces and boundaries, it is no longer valid to describe system response in terms of wavevectors. For a full description it is necessary to return to a full nonlocal response function (without translational symmetry), however the end effect can sometimes be described by "additional boundary conditions" (ABC's).


=== In isotropic media ===

In materials that have no relevant crystalline structure, spatial dispersion can be important.
Although symmetry demands that the permittivity is isotropic for zero wavevector, this restriction does not apply for nonzero wavevector. The non-isotropic permittivity for nonzero wavevector leads to effects such as optical activity in solutions of chiral molecules. In isotropic materials without optical activity, the permittivity tensor can be broken down to transverse and longitudinal components, referring to the response to electric fields either perpendicular or parallel to the wavevector.
For frequencies nearby an absorption line (e.g., an exciton), spatial dispersion can play an important role.


=== Landau damping ===

In plasma physics, a wave can be collisionlessly damped by particles in the plasma whose velocity matches the wave's phase velocity. This is typically represented as a spatially dispersive loss in the plasma's permittivity.


=== Permittivity–permeability ambiguity at nonzero frequency ===

At nonzero frequencies, it is possible to represent all magnetizations as time-varying polarizations. Moreover, since the electric and magnetic fields are directly related by 
  
    
      
        ∇
        ×
        E
        =
        −
        ∂
        B
        
          /
        
        ∂
        t
      
    
    {\displaystyle \nabla \times E=-\partial B/\partial t}
  
, the magnetization induced by a magnetic field can be represented instead as a polarization induced by the electric field, though with a highly dispersive relationship.
What this means is that at nonzero frequency, any contribution to permeability μ can instead be alternatively represented by a spatially dispersive contribution to permittivity ε. The values of the permeability and permittivity are different in this alternative representation, however this leads to no observable differences in real quantities such as electric field, magnetic flux density, magnetic moments, and current.
As a result, it is most common at optical frequencies to set μ to the vacuum permeability μ0 and only consider a dispersive permittivity ε. There is some discussion over whether this is appropriate in metamaterials where effective medium approximations for μ are used, and debate over the reality of "negative permeability" seen in negative index metamaterials.


=== Static spatial dispersion ===
Even at zero frequency, a charge disturbance in one location will cause a delocalized cloud that screens its effect. This delocalization can be described as spatial dispersion in the static permittivity. In a metal this takes the form of Friedel oscillations, wherein in the permittivity function 
  
    
      
        ϵ
        (
        k
        )
      
    
    {\displaystyle \epsilon (k)}
  
 can be understood as a hard cutoff for wavevectors exceeding twice the Fermi wavevector, and this hard cutoff causing a form of ringing artifact.


== Spatial dispersion in acoustics ==
In acoustics, especially in solids,  spatial dispersion can be significant for wavelengths comparable to the lattice spacing, which typically occurs at very high frequencies (gigahertz and above).
In solids, the difference in propagation for transverse acoustic modes and longitudinal acoustic modes of sound is due to a spatial dispersion in the elasticity tensor which relates stress and strain. For polar vibrations (optical phonons), the distinction between longitudinal and transverse modes can be seen as a spatial dispersion in the restoring forces, from the "hidden" non-mechanical degree of freedom that is the electromagnetic field.
Many electromagnetic wave effects from spatial dispersion find an analogue in acoustic waves. For example, there is acoustical activity — the rotation of the polarization plane of transverse sound waves — in chiral materials, analogous to optical activity.


== References ==
