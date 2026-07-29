# Hamiltonian simulation

> **Query Topic**: Hamiltonian H (Rank #2 Search Result)
> **Source Queue**: train (Row ID: 10, Frequency: 13)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Hamiltonian_simulation

---

Hamiltonian simulation (also referred to as quantum simulation) is a problem in quantum information science that attempts to find the computational complexity and quantum algorithms needed for simulating quantum systems. Hamiltonian simulation is a problem that demands algorithms which implement the evolution of a quantum state efficiently. The Hamiltonian simulation problem was proposed by Richard Feynman in 1982, where he proposed a quantum computer as a possible solution since the simulation of general Hamiltonians seem to grow exponentially with respect to the system size.


== Problem statement ==
In the Hamiltonian simulation problem, given a Hamiltonian 
  
    
      
        H
      
    
    {\displaystyle H}
  
 (
  
    
      
        
          2
          
            n
          
        
        ×
        
          2
          
            n
          
        
      
    
    {\displaystyle 2^{n}\times 2^{n}}
  
 hermitian matrix acting on 
  
    
      
        n
      
    
    {\displaystyle n}
  
 qubits), a time 
  
    
      
        t
      
    
    {\displaystyle t}
  
 and maximum simulation error 
  
    
      
        ϵ
      
    
    {\displaystyle \epsilon }
  
, the goal is to find an algorithm that approximates 
  
    
      
        U
      
    
    {\displaystyle U}
  
 such that 
  
    
      
        
          |
        
        
          |
        
        U
        −
        
          e
          
            −
            i
            H
            t
          
        
        
          |
        
        
          |
        
        ≤
        ϵ
      
    
    {\displaystyle ||U-e^{-iHt}||\leq \epsilon }
  
, where 
  
    
      
        
          e
          
            −
            i
            H
            t
          
        
      
    
    {\displaystyle e^{-iHt}}
  
 is the ideal evolution and 
  
    
      
        
          |
        
        
          |
        
        ⋅
        
          |
        
        
          |
        
      
    
    {\displaystyle ||\cdot ||}
  
 is the spectral norm.
A special case of the Hamiltonian simulation problem is the local Hamiltonian simulation problem. This is when 
  
    
      
        H
      
    
    {\displaystyle H}
  
 is a k-local Hamiltonian on 
  
    
      
        n
      
    
    {\displaystyle n}
  
 qubits where 
  
    
      
        H
        =
        
          ∑
          
            j
            
              =
            
            ⁡
            1
          
          
            m
          
        
        
          H
          
            j
          
        
      
    
    {\displaystyle H=\sum _{j\mathop {=} 1}^{m}H_{j}}
  
 and 
  
    
      
        
          H
          
            j
          
        
      
    
    {\displaystyle H_{j}}
  
 acts non-trivially on at most 
  
    
      
        k
      
    
    {\displaystyle k}
  
 qubits instead of 
  
    
      
        n
      
    
    {\displaystyle n}
  
 qubits. The local Hamiltonian simulation problem is important because most Hamiltonians that occur in nature are k-local.


== Techniques ==


=== Product formulas ===

Also known as Trotter formulas or Trotter–Suzuki decompositions, Product formulas simulate the sum-of-terms of a Hamiltonian by simulating each one separately for a small time slice. 
If 
  
    
      
        H
        =
        A
        +
        B
        +
        C
      
    
    {\displaystyle H=A+B+C}
  
, then 
  
    
      
        U
        =
        
          e
          
            −
            i
            (
            A
            +
            B
            +
            C
            )
            t
          
        
      
    
    {\displaystyle U=e^{-i(A+B+C)t}}
  
 is well-approximated by 
  
    
      
        (
        
          e
          
            −
            i
            A
            t
            
              /
            
            r
          
        
        
          e
          
            −
            i
            B
            t
            
              /
            
            r
          
        
        
          e
          
            −
            i
            C
            t
            
              /
            
            r
          
        
        
          )
          
            r
          
        
      
    
    {\displaystyle (e^{-iAt/r}e^{-iBt/r}e^{-iCt/r})^{r}}
  
 for a large 
  
    
      
        r
      
    
    {\displaystyle r}
  
; where 
  
    
      
        r
      
    
    {\displaystyle r}
  
 is the number of time steps to simulate for. The larger the 
  
    
      
        r
      
    
    {\displaystyle r}
  
, the more accurate the simulation. 
If the Hamiltonian is represented as a Sparse matrix, the distributed edge coloring algorithm can be used to decompose it into a sum of terms; which can then be simulated by a Trotter–Suzuki algorithm.


=== Taylor series ===

  
    
      
        
          e
          
            −
            i
            H
            t
          
        
        =
        
          ∑
          
            n
            
              =
            
            ⁡
            0
          
          
            ∞
          
        
        
          
            
              (
              −
              i
              H
              t
              
                )
                
                  n
                
              
            
            
              n
              !
            
          
        
        =
        I
        −
        i
        H
        t
        −
        
          
            
              
                H
                
                  2
                
              
              
                t
                
                  2
                
              
            
            2
          
        
        +
        
          
            
              i
              
                H
                
                  3
                
              
              
                t
                
                  3
                
              
            
            6
          
        
        +
        ⋯
      
    
    {\displaystyle e^{-iHt}=\sum _{n\mathop {=} 0}^{\infty }{\frac {(-iHt)^{n}}{n!}}=I-iHt-{\frac {H^{2}t^{2}}{2}}+{\frac {iH^{3}t^{3}}{6}}+\cdots }
  
 by the Taylor series expansion. This says that during the evolution of a quantum state, the Hamiltonian is applied over and over again to the system with a various number of repetitions. The first term is the identity matrix so the system doesn't change when it is applied, but in the second term the Hamiltonian is applied once. For practical implementations, the series has to be truncated 
  
    
      
        
          (
          
            
              ∑
              
                n
                
                  =
                
                ⁡
                0
              
              
                N
              
            
            
              
                
                  (
                  −
                  i
                  H
                  t
                  
                    )
                    
                      n
                    
                  
                
                
                  n
                  !
                
              
            
          
          )
        
      
    
    {\displaystyle \left(\sum _{n\mathop {=} 0}^{N}{\frac {(-iHt)^{n}}{n!}}\right)}
  
, where the bigger the 
  
    
      
        N
      
    
    {\displaystyle N}
  
, the more accurate the simulation. This truncated expansion is then implemented via the linear combination of unitaries (LCU) technique for Hamiltonian simulation. Namely, one decomposes the Hamiltonian 
  
    
      
        H
        =
        
          ∑
          
            ℓ
            =
            1
          
          
            L
          
        
        
          α
          
            ℓ
          
        
        
          H
          
            ℓ
          
        
      
    
    {\displaystyle H=\sum _{\ell =1}^{L}\alpha _{\ell }H_{\ell }}
  
 such that each 
  
    
      
        
          H
          
            ℓ
          
        
      
    
    {\displaystyle H_{\ell }}
  
 is unitary (for instance, the Pauli operators always provide such a basis), and so each 
  
    
      
        
          H
          
            n
          
        
        =
        
          ∑
          
            
              ℓ
              
                1
              
            
            ,
            …
            ,
            
              ℓ
              
                n
              
            
            =
            1
          
          
            L
          
        
        
          α
          
            
              ℓ
              
                1
              
            
          
        
        ⋯
        
          α
          
            
              ℓ
              
                n
              
            
          
        
        
          H
          
            
              ℓ
              
                1
              
            
          
        
        ⋯
        
          H
          
            
              ℓ
              
                n
              
            
          
        
      
    
    {\displaystyle H^{n}=\sum _{\ell _{1},\ldots ,\ell _{n}=1}^{L}\alpha _{\ell _{1}}\cdots \alpha _{\ell _{n}}H_{\ell _{1}}\cdots H_{\ell _{n}}}
  
 is also a linear combination of unitaries.


=== Quantum walk ===

In the quantum walk, a unitary operation whose spectrum is related to the Hamiltonian is implemented then the Quantum phase estimation algorithm is used to adjust the eigenvalues. This makes it unnecessary to decompose the Hamiltonian into a sum-of-terms like the Trotter-Suzuki methods.


=== Quantum signal processing ===

The quantum signal processing algorithm works by transducing the eigenvalues of the Hamiltonian into an ancilla qubit,  transforming the eigenvalues with single qubit rotations and finally projecting the ancilla. It has been proved to be optimal in query complexity when it comes to Hamiltonian simulation.


== Complexity ==
The table of the complexities of the Hamiltonian simulation algorithms mentioned above. The Hamiltonian simulation can be studied in two ways. This depends on how the Hamiltonian is given. If it is given explicitly, then gate complexity matters more than query complexity. If the Hamiltonian is described as an Oracle (black box) then the number of queries to the oracle is more important than the gate count of the circuit. The following table shows the gate and query complexity of the previously mentioned techniques.

Where 
  
    
      
        
          |
        
        
          |
        
        H
        
          |
        
        
          
            |
          
          
            
              m
              a
              x
            
          
        
      
    
    {\displaystyle ||H||_{\rm {max}}}
  
 is the largest entry of 
  
    
      
        H
      
    
    {\displaystyle H}
  
.


== See also ==
Quantum simulator


== References ==
