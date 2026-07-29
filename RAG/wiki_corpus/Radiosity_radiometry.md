# Radiosity (radiometry)

> **Query Topic**: radiosity in radiometry (Rank #1 Search Result)
> **Source Queue**: test (Row ID: 484, Frequency: 9)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Radiosity_(radiometry)

---

In radiometry , radiosity is the radiant flux leaving (emitted, reflected and transmitted by) a surface per unit area, and spectral radiosity is the radiosity of a surface per unit frequency or wavelength , depending on whether the spectrum is taken as a function of frequency or of wavelength. The SI unit of radiosity is the watt per square metre ( W/m 2 ), while that of spectral radiosity in frequency is the watt per square metre per hertz (W·m −2 ·Hz −1 ) and that of spectral radiosity in wavelength is the watt per square metre per metre (W·m −3 )—commonly the watt per square metre per nanometre ( W·m −2 ·nm −1 ). The CGS unit erg per square centimeter per second ( erg·cm −2 ·s −1 ) is often used in astronomy . Radiosity is often called intensity in branches of physics other than radiometry, but in radiometry this usage leads to confusion with radiant intensity .

## Mathematical definitions

### Radiosity

Radiosity of a surface , denoted J e ("e" for "energetic", to avoid confusion with photometric quantities), is defined as

$J_{\mathrm {e} }={\frac {\partial \Phi _{\mathrm {e} }}{\partial A}}=J_{\mathrm {e,em} }+J_{\mathrm {e,r} }+J_{\mathrm {e,tr} },$

where

- ∂ is the partial derivative symbol

- $\Phi _{e}$ is the radiant flux leaving (emitted, reflected and transmitted)

- $A$ is the area

- $J_{e,em}=M_{e}$ is the emitted component of the radiosity of the surface, that is to say its exitance

- $J_{e,r}$ is the reflected component of the radiosity of the surface

- $J_{e,tr}$ is the transmitted component of the radiosity of the surface

For an opaque surface, the transmitted component of radiosity J e,tr vanishes and only two components remain:

$J_{\mathrm {e} }=M_{\mathrm {e} }+J_{\mathrm {e,r} }.$

In heat transfer , combining these two factors into one radiosity term helps in determining the net energy exchange between multiple surfaces.

### Spectral radiosity

Spectral radiosity in frequency of a surface , denoted J e,ν , is defined as

$J_{\mathrm {e} ,\nu }={\frac {\partial J_{\mathrm {e} }}{\partial \nu }},$

where ν is the frequency.

Spectral radiosity in wavelength of a surface , denoted J e,λ , is defined as

$J_{\mathrm {e} ,\lambda }={\frac {\partial J_{\mathrm {e} }}{\partial \lambda }},$

where λ is the wavelength.

## Radiosity method

The radiosity of an opaque , gray and diffuse surface is given by

$J_{\mathrm {e} }=M_{\mathrm {e} }+J_{\mathrm {e,r} }=\varepsilon \sigma T^{4}+(1-\varepsilon )E_{\mathrm {e} },$

where

- ε is the emissivity of that surface;

- σ is the Stefan–Boltzmann constant ;

- T is the temperature of that surface;

- E e is the irradiance of that surface.

Normally, E e is the unknown variable and will depend on the surrounding surfaces. So, if some surface i is being hit by radiation from some other surface j , then the radiation energy incident on surface i is E e, ji A i = F ji A j J e, j where F ji is the view factor or shape factor , from surface j to surface i . So, the irradiance of surface i is the sum of radiation energy from all other surfaces per unit surface of area A i :

$E_{\mathrm {e} ,i}={\frac {\sum _{j=1}^{N}F_{ji}A_{j}J_{\mathrm {e} ,j}}{A_{i}}}.$

Now, employing the reciprocity relation for view factors F ji A j = F ij A i ,

$E_{\mathrm {e} ,i}=\sum _{j=1}^{N}F_{ij}J_{\mathrm {e} ,j},$

and substituting the irradiance into the equation for radiosity, produces

$J_{\mathrm {e} ,i}=\varepsilon _{i}\sigma T_{i}^{4}+(1-\varepsilon _{i})\sum _{j=1}^{N}F_{ij}J_{\mathrm {e} ,j}.$

For an N surface enclosure, this summation for each surface will generate N linear equations with N unknown radiosities, and N unknown temperatures. For an enclosure with only a few surfaces, this can be done by hand. But, for a room with many surfaces, linear algebra and a computer are necessary.

Once the radiosities have been calculated, the net heat transfer ${\dot {Q}}_{i}$ at a surface can be determined by finding the difference between the incoming and outgoing energy:

${\dot {Q}}_{i}=A_{i}\left(J_{\mathrm {e} ,i}-E_{\mathrm {e} ,i}\right).$

Using the equation for radiosity J e, i = ε i σ T i 4 + (1 − ε i ) E e, i , the irradiance can be eliminated from the above to obtain

${\dot {Q}}_{i}={\frac {A_{i}\varepsilon _{i}}{1-\varepsilon _{i}}}\left(\sigma T_{i}^{4}-J_{\mathrm {e} ,i}\right)={\frac {A_{i}\varepsilon _{i}}{1-\varepsilon _{i}}}\left(M_{\mathrm {e} ,i}^{\circ }-J_{\mathrm {e} ,i}\right),$

where M e, i ° is the radiant exitance of a black body .

## Circuit analogy

For an enclosure consisting of only a few surfaces, it is often easier to represent the system with an analogous circuit rather than solve the set of linear radiosity equations. To do this, the heat transfer at each surface is expressed as

${\dot {Q_{i}}}={\frac {M_{\mathrm {e} ,i}^{\circ }-J_{\mathrm {e} ,i}}{R_{i}}},$

where R i = (1 − ε i )/( A i ε i ) is the resistance of the surface.

Likewise, M e, i ° − J e, i is the blackbody exitance minus the radiosity and serves as the 'potential difference'. These quantities are formulated to resemble those from an electrical circuit V = IR .

Now performing a similar analysis for the heat transfer from surface i to surface j ,

${\dot {Q}}_{ij}=A_{i}F_{ij}(J_{\mathrm {e} ,i}-J_{\mathrm {e} ,j})={\frac {J_{\mathrm {e} ,i}-J_{\mathrm {e} ,j}}{R_{ij}}},$

where R ij = 1/( A i F ij ).

Because the above is between surfaces, R ij is the resistance of the space between the surfaces and J e, i − J e, j serves as the potential difference.

Combining the surface elements and space elements, a circuit is formed. The heat transfer is found by using the appropriate potential difference and equivalent resistances , similar to the process used in analyzing electrical circuits .

## Other methods

In the radiosity method and circuit analogy, several assumptions were made to simplify the model. The most significant is that the surface is a diffuse emitter. In such a case, the radiosity does not depend on the angle of incidence of reflecting radiation and this information is lost on a diffuse surface. In reality, however, the radiosity will have a specular component from the reflected radiation . So, the heat transfer between two surfaces relies on both the view factor and the angle of reflected radiation.

It was also assumed that the surface is a gray body, that is to say its emissivity is independent of radiation frequency or wavelength. However, if the range of radiation spectrum is large, this will not be the case. In such an application, the radiosity must be calculated spectrally and then integrated over the range of radiation spectrum.

Yet another assumption is that the surface is isothermal . If it is not, then the radiosity will vary as a function of position along the surface. However, this problem is solved by simply subdividing the surface into smaller elements until the desired accuracy is obtained.

## SI radiometry units
