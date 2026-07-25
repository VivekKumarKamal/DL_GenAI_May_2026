# Contact resistance

> **Query Topic**: resistance-switching processes  
> **Source Queue**: train (Row ID: 51, Frequency: 14)  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Contact_resistance

---

Electrical contact resistance (ECR, or simply contact resistance) is resistance to the flow of electric current caused by incomplete contact of the surfaces through which the current is flowing, and by films or oxide layers on the contacting surfaces. It occurs at electrical connections such as switches, connectors, breakers, contacts, and measurement probes. Contact resistance values are typically small (in the microohm to milliohm range).
Contact resistance can cause significant voltage drops and heating in circuits with high current. Because contact resistance adds to the intrinsic resistance of the conductors, it can cause significant measurement errors when exact resistance values are needed.
Contact resistance may vary with temperature. It may also vary with time (most often decreasing) in a process known as resistance creep.
Electrical contact resistance is also called interface resistance, transitional resistance, or the correction term. Parasitic resistance is a more general term, of which it is usually assumed that contact resistance is a major component.
William Shockley introduced the idea of a potential drop on an injection electrode to explain the difference between experimental results and the model of gradual channel approximation.


== Measurement methods ==
Because contact resistance is usually comparatively small, it can be difficult to measure, and four-terminal measurement gives better results than a simple two-terminal measurement made with an ohmmeter.

In a two-terminal measurement (as with a typical ohmmeter), the current used to make the measurement is injected through the measurement leads, which causes a potential drop not just across the contact area to be measured but also across the probe contacts and the leads. That means that the contact resistance of the probes and their leads is inseparable from the resistance of the contact area to be measured, with which they are in series.
In a four-terminal measurement, the current used to make the measurement is injected using a second, separate pair of leads, so the contact resistance of the measurement probes and their leads is not included in the measurement.
Specific contact resistance can be obtained by multiplying by contact area.


== Experimental characterization ==
For experimental characterization, a distinction must be made between contact resistance evaluation in two-electrode systems (for example, diodes) and three-electrode systems (for example, transistors).
In two-electrode systems, specific contact resistivity is experimentally defined as the slope of the I–V curve at V = 0:

  
    
      
        
          r
          
            c
          
        
        =
        
          
            {
            
              
                
                  ∂
                  V
                
                
                  ∂
                  J
                
              
            
            }
          
          
            V
            =
            0
          
        
      
    
    {\displaystyle r_{\text{c}}=\left\{{\frac {\partial V}{\partial J}}\right\}_{V=0}}
  

where 
  
    
      
        J
      
    
    {\displaystyle J}
  
 is the current density, or current per area. The units of specific contact resistivity are typically therefore in ohm-square metre, or Ω⋅m2. When the current is a linear function of the voltage, the device is said to have ohmic contacts.
Inductive and capacitive methods could be used in principle to measure an intrinsic impedance without the complication of contact resistance. In practice, direct current methods are more typically used to determine resistance.
The three electrode systems such as transistors require more complicated methods for the contact resistance approximation. The most common approach is the transmission line model (TLM). Here, the total device resistance 
  
    
      
        
          R
          
            tot
          
        
      
    
    {\displaystyle R_{\text{tot}}}
  
 is plotted as a function of the channel length:

  
    
      
        
          R
          
            tot
          
        
        =
        
          R
          
            c
          
        
        +
        
          R
          
            ch
          
        
        =
        
          R
          
            c
          
        
        +
        
          
            L
            
              W
              C
              μ
              
                (
                
                  
                    V
                    
                      gs
                    
                  
                  −
                  
                    V
                    
                      ds
                    
                  
                
                )
              
            
          
        
      
    
    {\displaystyle R_{\text{tot}}=R_{\text{c}}+R_{\text{ch}}=R_{\text{c}}+{\frac {L}{WC\mu \left(V_{\text{gs}}-V_{\text{ds}}\right)}}}
  

where 
  
    
      
        
          R
          
            c
          
        
      
    
    {\displaystyle R_{\text{c}}}
  
 and 
  
    
      
        
          R
          
            ch
          
        
      
    
    {\displaystyle R_{\text{ch}}}
  
 are contact and channel resistances, respectively, 
  
    
      
        L
        
          /
        
        W
      
    
    {\displaystyle L/W}
  
 is the channel length/width, 
  
    
      
        C
      
    
    {\displaystyle C}
  
 is gate insulator capacitance (per unit of area), 
  
    
      
        μ
      
    
    {\displaystyle \mu }
  
 is carrier mobility, and 
  
    
      
        
          V
          
            gs
          
        
      
    
    {\displaystyle V_{\text{gs}}}
  
 and 
  
    
      
        
          V
          
            ds
          
        
      
    
    {\displaystyle V_{\text{ds}}}
  
 are gate-source and drain-source voltages. Therefore, the linear extrapolation of total resistance to the zero channel length provides the contact resistance. The slope of the linear function is related to the channel transconductance and can be used for estimation of the ”contact resistance-free” carrier mobility. The approximations used here (linear potential drop across the channel region, constant contact resistance, ...) lead sometimes to the channel dependent contact resistance.
Beside the TLM it was proposed the gated four-probe measurement and the modified time-of-flight method (TOF). The direct methods able to measure potential drop on the injection electrode directly are the Kelvin probe force microscopy (KFM) and the electric-field induced second harmonic generation.
In the semiconductor industry, Cross-Bridge Kelvin Resistor(CBKR) structures are the mostly used test structures to characterize metal-semiconductor contacts in the Planar devices of VLSI technology. During the measurement process, force the current (
  
    
      
        I
      
    
    {\displaystyle I}
  
) between contacts 1 and 2 and measure the potential deference between contacts 3 and 4. The contact resistance 
  
    
      
        
          R
          
            k
          
        
      
    
    {\displaystyle R_{\text{k}}}
  
 can be then calculated as 
  
    
      
        
          R
          
            k
          
        
        =
        
          V
          
            34
          
        
        
          /
        
        I
      
    
    {\displaystyle R_{\text{k}}=V_{34}/I}
  
 .


== Mechanisms ==
For given physical and mechanical material properties, parameters that govern the magnitude of electrical contact resistance (ECR) and its variation at an interface relate primarily to surface structure and applied load (Contact mechanics). Surfaces of metallic contacts generally exhibit an external layer of oxide material and adsorbed water molecules, which lead to capacitor-type junctions at weakly contacting asperities and resistor type contacts at strongly contacting asperities, where sufficient pressure is applied for asperities to penetrate the oxide layer, forming metal-to-metal contact patches. If a contact patch is sufficiently small, with dimensions comparable or smaller than the mean free path of electrons resistance at the patch can be described by the Sharvin mechanism, whereby electron transport can be described by ballistic conduction. Generally, over time, contact patches expand and the contact resistance at an interface relaxes, particularly at weakly contacting surfaces, through current induced welding and dielectric breakdown. This process is known also as resistance creep. The coupling of surface chemistry, contact mechanics and charge transport mechanisms needs to be considered in the mechanistic evaluation of ECR phenomena.


== Quantum limit ==
When a conductor has spatial dimensions close to 
  
    
      
        2
        π
        
          /
        
        
          k
          
            F
          
        
      
    
    {\displaystyle 2\pi /k_{\text{F}}}
  
, where 
  
    
      
        
          k
          
            F
          
        
      
    
    {\displaystyle k_{\text{F}}}
  
 is Fermi wavevector of the conducting material, Ohm's law does not hold anymore. These small devices are called quantum point contacts. Their conductance must be an integer multiple of the value 
  
    
      
        2
        
          e
          
            2
          
        
        
          /
        
        h
      
    
    {\displaystyle 2e^{2}/h}
  
, where 
  
    
      
        e
      
    
    {\displaystyle e}
  
 is the elementary charge and 
  
    
      
        h
      
    
    {\displaystyle h}
  
 is the Planck constant. Quantum point contacts behave more like waveguides than the classical wires of everyday life and may be described by the Landauer scattering formalism. Point-contact tunneling is an important technique for characterizing superconductors.


== Other forms of contact resistance ==
Measurements of thermal conductivity are also subject to contact resistance, with particular significance in heat transport through granular media. Similarly, a drop in hydrostatic pressure (analogous to electrical voltage) occurs when fluid flow transitions from one channel to another.


== Significance ==
Bad contacts are the cause of failure or poor performance in a wide variety of electrical devices. For example, corroded jumper cable clamps can frustrate attempts to start a vehicle that has a low battery. Dirty or corroded contacts on a fuse or its holder can give the false impression that the fuse is blown. A sufficiently high contact resistance can cause substantial heating in a high current device. Unpredictable or noisy contacts are a major cause of the failure of electrical equipment.


== See also ==
Contact cleaner
Wetting current


== References ==


== Further reading ==
Pitney, Kenneth E. (2014) [1973]. Ney Contact Manual - Electrical Contacts for Low Energy Uses (reprint of 1st ed.). Deringer-Ney, originally JM Ney Co. ASIN B0006CB8BC. (NB. Free download after registration.)
Slade, Paul G. (February 12, 2014) [1999]. Electrical Contacts: Principles and Applications. Electrical engineering and electronics. Vol. 105 (2 ed.). CRC Press, Taylor & Francis, Inc. ISBN 978-1-43988130-9. {{cite book}}: |work= ignored (help)
Holm, Ragnar; Holm, Else (June 29, 2013) [1967]. Williamson, J. B. P. (ed.). Electric Contacts: Theory and Application (reprint of 4th revised ed.). Springer Science & Business Media. ISBN 978-3-540-03875-7. (NB. A rewrite of the earlier "Electric Contacts Handbook".)
Holm, Ragnar; Holm, Else (1958). Electric Contacts Handbook (3rd completely rewritten ed.). Berlin / Göttingen / Heidelberg, Germany: Springer-Verlag. ISBN 978-3-66223790-8. {{cite book}}: ISBN / Date incompatibility (help) [1] (NB. A rewrite and translation of the earlier "Die technische Physik der elektrischen Kontakte" (1941) in German language, which is available as reprint under ISBN 978-3-662-42222-9.)
Huck, Manfred; Walczuk, Eugeniucz; Buresch, Isabell; et al. (2016) [1984]. Vinaricky, Eduard; Schröder, Karl-Heinz; Weiser, Josef; Keil, Albert; Merl, Wilhelm A.; Meyer, Carl-Ludwig (eds.). Elektrische Kontakte, Werkstoffe und Anwendungen: Grundlagen, Technologien, Prüfverfahren (in German) (3 ed.). Berlin / Heidelberg / New York / Tokyo: Springer-Verlag. ISBN 978-3-642-45426-4.
