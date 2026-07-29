# Shubnikov–de Haas effect

> **Query Topic**: De Haas-Van Alphen effect (Rank #2 Search Result)
> **Source Queue**: test (Row ID: 311, Frequency: 10)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Shubnikov–de_Haas_effect

---

An oscillation in the conductivity of a material that occurs at low temperatures in the presence of very intense magnetic fields , the Shubnikov–de Haas effect ( SdH ) is a macroscopic manifestation of the inherent quantum mechanical nature of matter. It is often used to determine the effective mass of charge carriers ( electrons and electron holes ), allowing investigators to distinguish among majority and minority carrier populations. 
The effect is named after Wander Johannes de Haas and Lev Shubnikov .

## Physical process

At sufficiently low temperatures and high magnetic fields, the free electrons in the conduction band of a metal , semimetal , or narrow band gap semiconductor will behave like simple harmonic oscillators . When the magnetic field strength is changed, the oscillation period of the simple harmonic oscillators changes proportionally. The resulting energy spectrum is made up of Landau levels separated by the cyclotron energy. These Landau levels are further split by the Zeeman energy . In each Landau level the cyclotron and Zeeman energies and the number of electron states ( eB / h ) all increase linearly with increasing magnetic field. Thus, as the magnetic field increases, the spin-split Landau levels move to higher energy. As each energy level passes through the Fermi energy , it depopulates as the electrons become free to flow as current. This causes the material's transport and thermodynamic properties to oscillate periodically, producing a measurable oscillation in the material's conductivity. Since the transition across the Fermi 'edge' spans a small range of energies, the waveform is square rather than sinusoidal , with the shape becoming ever more square as the temperature is lowered. [ citation needed ]

## Theory

Consider a two-dimensional quantum gas of electrons confined in a sample with given width and with edges. In the presence of a magnetic flux density B , the energy eigenvalues of this system are described by Landau levels . As shown in Fig 1, these levels are equidistant along the vertical axis. Each energy level is substantially flat inside a sample (see Fig 1). At the edges of a sample, the work function bends levels upwards.

Fig 1 shows the Fermi energy E F located in between two Landau levels . Electrons become mobile as their energy levels cross the Fermi energy E F . With the Fermi energy E F in between two Landau levels , scattering of electrons will occur only at the edges of a sample where the levels are bent. The corresponding electron states are commonly referred to as edge channels.

The Landauer–Büttiker approach is used to describe transport of electrons in this particular sample. The Landauer–Büttiker approach allows calculation of net currents I m flowing between a number of contacts 1 ≤ m ≤ n . In its simplified form, the net current I m of contact m with chemical potential μ m reads

where e denotes the electron charge , h denotes the Planck constant , and i stands for the number of edge channels. The matrix T ml denotes the probability of transmission of a negatively charged particle (i.e. of an electron) from a contact l ≠ m to another contact m . The net current I m in relationship ( 1 ) is made up of the currents towards contact m and of the current transmitted from the contact m to all other contacts l ≠ m . That current equals the voltage μ m / e of contact m multiplied with the Hall conductivity of 2 e 2 / h per edge channel.

Fig 2 shows a sample with four contacts. To drive a current through the sample, a voltage is applied between the contacts 1 and 4. A voltage is measured between the contacts 2 and 3. Suppose electrons leave the 1st contact, then are transmitted from contact 1 to contact 2, then from contact 2 to contact 3, then from contact 3 to contact 4, and finally from contact 4 back to contact 1. A negative charge (i.e. an electron) transmitted from contact 1 to contact 2 will result in a current from contact 2 to contact 1. An electron transmitted from contact 2 to contact 3 will result in a current from contact 3 to contact 2 etc. Suppose also that no electrons are transmitted along any further paths. The probabilities of transmission of ideal contacts then read

$T_{21}=T_{32}=T_{43}=T_{14}=1,$

and

$T_{ml}=0$

otherwise. With these probabilities, the currents I 1 ... I 4 through the four contacts, and with their chemical potentials μ 1 ... μ 4 , equation ( 1 ) can be re-written

$\left({\begin{matrix}I_{1}\\I_{2}\\I_{3}\\I_{4}\end{matrix}}\right)={\frac {2e\cdot i}{h}}\left({\begin{matrix}1&0&0&-1\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{matrix}}\right)\left({\begin{matrix}\mu _{1}\\\mu _{2}\\\mu _{3}\\\mu _{4}\end{matrix}}\right).$

A voltage is measured between contacts 2 and 3. The voltage measurement should ideally not involve a flow of current through the meter, so I 2 = I 3 = 0. It follows that

$I_{3}=0={\frac {2e\cdot i}{h}}\left(-\mu _{2}+\mu _{3}\right),$

$\mu _{2}=\mu _{3}.$

In other words, the chemical potentials μ 2 and μ 3 and their respective voltages μ 2 / e and μ 3 / e are the same. As a consequence of no drop of voltage between the contacts 2 and 3, the current I 1 experiences zero resistivity R SdH in between contacts 2 and 3

$R_{\mathrm {SdH} }={\frac {\mu _{2}-\mu _{3}}{e\cdot I_{1}}}=0.$

The result of zero resistivity between the contacts 2 and 3 is a consequence of the electrons being mobile only in the edge channels of the sample. The situation would be different if a Landau level came close to the Fermi energy E F . Any electrons in that level would become mobile as their energy approaches the Fermi energy E F . Consequently, scatter would lead to R SdH > 0. In other words, the above approach yields zero resistivity whenever the Landau levels are positioned such that the Fermi energy E F is in between two levels.

## Applications

Shubnikov–De Haas oscillations can be used to determine the two-dimensional electron density of a sample. For a given magnetic flux $\Phi$ the maximum number D of electrons with spin S = 1/2 per Landau level is

Upon insertion of the expressions for the flux quantum Φ 0 = h / e and for the magnetic flux Φ = BA relationship ( 2 ) reads

$D=2{\frac {eBA}{h}}$

Let N denote the maximum number of states per unit area, so D = NA and

$N=2{\frac {eB}{h}}.$

Now let each Landau level correspond to an edge channel of the above sample. For a given number i of edge channels each filled with N electrons per unit area, the overall number n of electrons per unit area will read

$n=iN=2i{\frac {eB}{h}}.$

The overall number n of electrons per unit area is commonly referred to as the electron density of a sample. No electrons disappear from the sample into the unknown, so the electron density n is constant. It follows that

$B_{i}={\frac {nh}{2ei}},$

${\frac {1}{B_{i}}}={\frac {2ei}{nh}},$

For a given sample, all factors including the electron density n on the right hand side of relationship ( 3 ) are constant. When plotting the index i of an edge channel versus the reciprocal of its magnetic flux density 1/ B i , one obtains a straight line with slope 2 e /( nh ). Since the electron charge e is known and also the Planck constant h , one can derive the electron density n of a sample from this plot. Shubnikov–De Haas oscillations are observed in highly doped Bi 2 Se 3 . Fig 3 shows the reciprocal magnetic flux density 1/ B i of the 10th to 14th minima of a Bi 2 Se 3 sample. The slope of 0.00618/T as obtained from a linear fit yields the electron density n

$n={\frac {2e}{0.00618/\mathrm {T} \cdot h}}\approx 7.82\times 10^{14}/\mathrm {m} ^{2}.$

Shubnikov–de Haas oscillations can be used to map the Fermi surface of electrons in a sample, by determining the periods of oscillation for various applied field directions.

## Related physical process

The effect is related to the De Haas–Van Alphen effect , which is the name given to the corresponding oscillations in magnetization. The signature of each effect is a periodic waveform when plotted as a function of inverse magnetic field. The " frequency " of the magnetoresistance oscillations indicate areas of extremal orbits around the Fermi surface . The area of the Fermi surface is expressed in teslas . More accurately, the period in inverse Teslas is inversely proportional to the area of the extremal orbit of the Fermi surface in inverse m/cm.
