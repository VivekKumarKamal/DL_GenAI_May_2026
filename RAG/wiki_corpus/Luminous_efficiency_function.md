# Luminous efficiency function

> **Query Topic**: variation between illuminance and luminance (Rank #3 Search Result)
> **Source Queue**: train (Row ID: 19, Frequency: 3)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Luminous_efficiency_function

---

A luminous efficiency function or luminosity function represents the average spectral sensitivity of human visual perception of light . It is based on subjective judgements of which of a pair of different-colored lights is brighter, to describe relative sensitivity to light of different wavelengths . It is not an absolute reference to any particular individual, but is a standard observer representation of visual sensitivity of a theoretical human eye . It is valuable as a baseline for experimental purposes, and in colorimetry . Different luminous efficiency functions apply under different lighting conditions, varying from photopic in brightly lit conditions through mesopic to scotopic under low lighting conditions. When not specified, the luminous efficiency function generally refers to the photopic luminous efficiency function.

The CIE photopic luminous efficiency function y (λ) or V (λ) is a standard function established by the Commission Internationale de l'Éclairage (CIE) and standardized in collaboration with the ISO , and may be used to convert radiant energy into luminous (i.e., visible) energy. It also forms the central color matching function in the CIE 1931 color space .

## Details

There are two luminous efficiency functions in common use. For everyday light levels, the photopic luminosity function best approximates the response of the human eye. For low light levels, the response of the human eye changes, and the scotopic curve applies. The photopic curve is the CIE standard curve used in the CIE 1931 color space.

The luminous flux (or visible power) in a light source is defined by the photopic luminosity function (assuming it is bright enough to activate photopic vision in the eyes). The following equation calculates the total luminous flux in a source of light:

$\Phi _{\mathrm {v} }=683.002\ (\mathrm {lm/W} )\cdot \int _{0}^{\infty }{\overline {y}}(\lambda )\Phi _{\mathrm {e} ,\lambda }(\lambda )\,\mathrm {d} \lambda ,$

where

- Φ v is the luminous flux , in lumens;

- Φ e,λ is the spectral radiant flux , in watts per nanometre;

- y ( λ ), also known as V ( λ ), is the luminosity function, dimensionless;

- λ is the wavelength, in nanometres.

Formally, the integral is the inner product of the luminosity function with the spectral power distribution . In practice, the integral is replaced by a sum over discrete wavelengths for which tabulated values of the luminous efficiency function are available. The CIE distributes standard tables with luminosity function values at 5 nm intervals from 380 nm to 780 nm .

The standard luminous efficiency function is normalized to a peak value of unity at 555 nm (see luminous coefficient ). The value of the constant in front of the integral is usually rounded off to 683 lm/W . The small excess fractional value comes from the slight mismatch between the definition of the lumen and the peak of the luminosity function. The lumen is defined to be unity for a radiant energy of 1/683 W at a frequency of 540 THz , which corresponds to a standard air wavelength of 555.016 nm rather than 555 nm , which is the peak of the luminosity curve. The value of y ( λ ) is 0.999 997 at 555.016 nm , so that a value of 683/ 0.999 997 = 683.002 is the multiplicative constant.

The number 683 is connected to the modern (1979) definition of the candela , the unit of luminous intensity . This arbitrary number made the new definition give numbers equivalent to those from the old definition of the candela.

## Improvements to the standard

The CIE 1924 photopic V ( λ ) luminosity function, which is included in the CIE 1931 color-matching functions as the y ( λ ) function, has long been acknowledged to underestimate the contribution of the blue end of the spectrum to perceived luminance. There have been numerous attempts to improve the standard function, to make it more representative of human vision. Judd in 1951, improved by Vos in 1978, resulted in a function known as CIE V M ( λ ). More recently, Sharpe, Stockman, Jagla & Jägle (2005) developed a function consistent with the Stockman & Sharpe cone fundamentals ; their curves are plotted in the figure above.

Stockman & Sharpe has subsequently produced an improved function in 2011, taking into account the effects of chromatic adaptation under daylight . Their work in 2008 has revealed that "luminous efficiency or V(l) functions change dramatically with chromatic adaptation".

### ISO standard

The ISO standard is ISO/CIE FDIS 11664–1. The standard provides an incremental table by nm of each value in the visible range for the CIE 1924 function.

## Scotopic luminosity

For very low levels of intensity ( scotopic vision ), the sensitivity of the eye is mediated by rods, not cones, and shifts toward the violet , peaking around 507 nm for young eyes; the sensitivity is equivalent to 1699 lm/W or 1700 lm/W at this peak. The standard scotopic luminous efficiency function or V ′ ( λ ) was adopted by the CIE in 1951, based on measurements by Wald (1945) and by Crawford (1949).

Luminosity for mesopic vision , a wide transitioning band between scotopic and phototic vision, is more poorly standardized. The consensus is that this luminous efficiency can be written as a weighted average of scotopic and mesopic luminosities, but different organizations provide different weighting factors.

## Human variation

### Color blindness

Color blindness changes the sensitivity of the eye as a function of wavelength. For people with protanopia , the peak of the eye's response is shifted toward the short-wave part of the spectrum (approximately 540 nm), while for people with deuteranopia , there is a slight shift in the peak of the spectrum, to about 560 nm. People with protanopia have essentially no sensitivity to light of wavelengths more than 670 nm.

### Age

For older people with normal color vision, the crystalline lens may become slightly yellow due to cataracts , which moves the maximum of sensitivity to the red part of the spectrum and narrows the range of perceived wavelengths. A method for estimating the transmittance of the human crystalline lens depending on age is standardized as CIE 203:2012, though further improvement has been proposed. For a few more lens transmission functions, see the Lucas (2014) Irradiance Toolbox.

## Other functions

### Non-vision parameters

The wavelength-dependent effect of light is seen not only with vision, but also (in humans) in the circadian rhythm via melanopsin . For reporting the effect of light on the human circadian rhythm, a value called melanopic illuminance is used, defined using a luminous efficiency function specific to the melanopsin. The unit is lux (lx) used in a non-SI-compliant fashion. With CIE S 026:2018, the system has become SI-compliant, with the melanopic equivalent daylight illuminance (M-EDI, unit lx ) being derived from melanopic irradiance (unit W/m 2 ). A human being subject to 100 lx of M-EDI of light should have the same alternation to their circadian rhythm as if they are being exposed to 100 lx of daylight.

Lucas (2014) and the later CIE S 026 also define luminous efficiency function specific to four other human opsins. Lucas uses non-SI-compliant lux while CIE uses SI-compliant EDI lux. Although the CIE standard requires payment, the associated toolbox and its user guide is available for free. Some modern sensors, such as the Roomyou1, are designed to measure melanopic equivalent daylight illuminance (M-EDI) alongside other indoor climate parameters.

### Non-human animals

Most non- primate mammals have the a similar luminous efficiency function to people with protanopia. Their insensitivity to long-wavelength red light makes it possible to use such illumination while studying the nocturnal life of animals.

Definition of melanopic illuminance and opsin-specific illuminances in the sense of Lucas (2014) are available for rodents. There is a significant difference at short wavelengths ( < 420 nm) because the rodent eye filters light differently before the retina compared to the human eye. A 2024 article by Lucas's Group and international researchers calls for better standardization of light levels used in animal experiments using these species-adjusted illuminance measurements, both to improve the reproducibility of light-related experiments and to improve animal welfare. The article includes α opic data for mice, brown rats, macaques, cats, and dogs. It links to two separate toolboxes, one for calculating the species-specific EDI from a spectral power distribution , the other for estimating the species-specific EDI for a given amount of photonic lux and a light source of known spectrum.

The wavelength-dependent attractive effect on bees and moths have been quantified with a relative arbitrary unit of "attraction". These data have been used to design white LED light sources with lower arthopod attraction at night.
