# Multiplicative inverse

> **Query Topic**: reciprocal length or inverse length (Rank #3 Search Result)
> **Source Queue**: test (Row ID: 24, Frequency: 18)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Multiplicative_inverse

---

In mathematics , a multiplicative inverse or reciprocal for a number x , denoted by ${\tfrac {1}{x}}$ or x − 1 , is a number which when multiplied by x yields the multiplicative identity , 1. The multiplicative inverse of a fraction ${\tfrac {a}{b}}$ is ${\tfrac {b}{a}}.$ Dividing 1 by a real number yields its multiplicative inverse. For example, the reciprocal of 5 is one fifth (1/5 or 0.2), and the reciprocal of 0.25 is 1 divided by 0.25, or 4. The reciprocal function , the function f ( x ) that maps x to ${\tfrac {1}{x}},$ is one of the simplest examples of a function which is its own inverse (an involution ).

Multiplying by a number is the same as dividing by its reciprocal and vice versa. For example, multiplication by 4/5 (or 0.8) will give the same result as division by 5/4 (or 1.25). Therefore, multiplication by a number followed by multiplication by its reciprocal yields the original number (since the product of the number and its reciprocal is 1).

The term reciprocal was in common use at least as far back as the third edition of Encyclopædia Britannica (1797) to describe two numbers whose product is 1; geometrical quantities in inverse proportion are described as reciprocall in a 1570 translation of Euclid 's Elements .

In the phrase multiplicative inverse , the qualifier multiplicative is often omitted and then tacitly understood (in contrast to the additive inverse ). Multiplicative inverses can be defined over many mathematical domains as well as numbers. In these cases it can happen that ab ≠ ba ; then "inverse" typically implies that an element is both a left and right inverse .

The notation f −1 is sometimes also used for the inverse function of the function f , which is for most functions not equal to the multiplicative inverse. For example, the multiplicative inverse ${\tfrac {1}{\sin x}}=(\sin x)^{-1}$ is the cosecant of x , and not the inverse sine of x denoted by sin −1 x or arcsin x . The terminology difference reciprocal versus inverse is not sufficient to make this distinction, since many authors prefer the opposite naming convention, probably for historical reasons (for example in French , the inverse function is preferably called the bijection réciproque ).

## Examples and counterexamples

In the real numbers, zero does not have a reciprocal ( division by zero is undefined ) because no real number multiplied by 0 produces 1 (the product of any number with zero is zero). With the exception of zero, reciprocals of every real number are real, reciprocals of every rational number are rational, and reciprocals of every complex number are complex. The property that every element other than zero has a multiplicative inverse is part of the definition of a field , of which these are all examples. On the other hand, no integer other than 1 and −1 has an integer reciprocal, and so the integers are not a field.

In modular arithmetic , the modular multiplicative inverse of a is also defined: it is the number x such that ax ≡ 1 (mod n ) . This multiplicative inverse exists if and only if a and n are coprime . For example, the inverse of 3 mod 11 is four because 4 ⋅ 3 ≡ 1 (mod 11) . The extended Euclidean algorithm may be used to compute it.

The sedenions are an algebra in which every nonzero element has a multiplicative inverse, but which nonetheless has divisors of zero, that is, nonzero elements x , y such that xy = 0 .

A square matrix has an inverse if and only if its determinant has an inverse in the coefficient ring . The linear map that has the matrix A −1 with respect to some base is then the inverse function of the map having A as matrix in the same base. Thus, the two distinct notions of the inverse of a function are strongly related in this case, but they still do not coincide, since the multiplicative inverse of Ax would be ( Ax ) −1 , not A −1 x .

These two notions of an inverse function do sometimes coincide, for example for the function $f(x)=x^{i}=e^{i\ln(x)}$ where ln is the principal branch of the complex logarithm and $e^{-\pi }<|x|<e^{\pi }$ : $\left({\tfrac {1}{f}}\circ f\right)(x)={\frac {1}{f}}(f(x))={\frac {1}{f(f(x))}}={\frac {1}{e^{i\ln(e^{i\ln(x)})}}}={\frac {1}{e^{ii\ln(x)}}}={\frac {1}{e^{-\ln(x)}}}=x.$

The trigonometric functions are related by the reciprocal identity: the cotangent is the reciprocal of the tangent; the secant is the reciprocal of the cosine; the cosecant is the reciprocal of the sine.

A ring in which every nonzero element has a multiplicative inverse is a division ring ; likewise an algebra in which this holds is a division algebra .

## Complex numbers

As mentioned above, the reciprocal of every nonzero complex number z = a + bi is complex. It can be found by multiplying both top and bottom of ${\tfrac {1}{z}}$ by its complex conjugate ${\bar {z}}=a-bi$ and using the property that $z{\bar {z}}=\|z\|^{2}$ , the absolute value of z squared, which is the real number a 2 + b 2 :

${\begin{aligned}{\frac {1}{z}}&={\frac {\bar {z}}{z{\bar {z}}}}\\[2pt]&={\frac {\bar {z}}{\|z\|^{2}}}\\[2pt]&={\frac {a-bi}{a^{2}+b^{2}}}\\[2pt]&={\frac {a}{a^{2}+b^{2}}}-{\frac {b}{a^{2}+b^{2}}}i.\end{aligned}}$

The intuition is that ${\tfrac {\bar {z}}{\|z\|}}$ gives us the complex conjugate with a magnitude reduced to a value of 1, so dividing again by | z | ensures that the magnitude is now equal to the reciprocal of the original magnitude as well, hence: ${\frac {1}{z}}={\frac {\bar {z}}{\|z\|^{2}}}$ In particular, if || z || = 1 ( z has unit magnitude), then ${\tfrac {1}{z}}={\bar {z}}.$ Consequently, the imaginary units , ± i , have additive inverse equal to multiplicative inverse, and are the only complex numbers with this property. For example, additive and multiplicative inverses of i are −( i ) = − i and ( i ) −1 = − i , respectively.

For a complex number in polar form z = r (cos φ + i sin φ ) , the reciprocal simply takes the reciprocal of the magnitude and the negative of the angle:

${\frac {1}{z}}={\frac {1}{r}}{\bigl (}\cos(-\varphi )+i\sin(-\varphi ){\bigr )}.$

Geometrically in the complex plane the inverse of a complex number can be found by performing an inversion in the unit circle followed by a reflection over the real axis (see drawing).

## Calculus

In real calculus , the derivative of ${\tfrac {1}{x}}=x^{-1}$ is given by the power rule with the power −1: ${\frac {d}{dx}}x^{-1}=(-1)x^{(-1)-1}=-x^{-2}=-{\frac {1}{x^{2}}}.$

The power rule for integrals ( Cavalieri's quadrature formula ) cannot be used to compute the integral of ${\tfrac {1}{x}},$ because doing so would result in division by zero : $\int {\frac {dx}{x}}={\frac {x^{0}}{0}}+C$ Instead the integral is given by: $\int _{1}^{a}{\frac {dx}{x}}=\ln a,\qquad \int {\frac {dx}{x}}=\ln x+C.$ where ln is the natural logarithm . To show this, note that ${\textstyle {\frac {d}{dy}}e^{y}=e^{y}}$ , so if $x=e^{y}$ and $y=\ln x$ , we have: ${\begin{aligned}&{\frac {dx}{dy}}=x\\[2pt]\Rightarrow \quad &{\frac {dx}{x}}=dy\\[2pt]\Rightarrow \quad &\int {\frac {dx}{x}}=\int dy=y+C=\ln x+C.\end{aligned}}$

## Algorithms

The reciprocal may be computed by hand with the use of long division .

Computing the reciprocal is important in many division algorithms , since the quotient ${\tfrac {a}{b}}$ can be computed by first computing ${\tfrac {1}{b}}$ and then multiplying it by a . Noting that $f(x)={\tfrac {1}{x}}-b$ has a zero at $x={\tfrac {1}{b}},$ Newton's method can find that zero, starting with a guess x 0 and iterating using the rule:

$x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}-{\frac {{\frac {1}{x_{n}}}-b}{\frac {-1}{x_{n}^{2}}}}=2x_{n}-bx_{n}^{2}=x_{n}(2-bx_{n}).$

This continues until the desired precision is reached. For example, suppose we wish to compute 1/17 ≈ 0.0588 with three digits of precision. Taking x 0 = 0.1 , the following sequence is produced:

${\begin{aligned}x_{1}&=0.1(2-17\times 0.1)&&=0.03\\x_{2}&=0.03(2-17\times 0.03)&&=0.0447\\x_{3}&=0.0447(2-17\times 0.0447)&&\approx 0.0554\\x_{4}&=0.0554(2-17\times 0.0554)&&\approx 0.0586\\x_{5}&=0.0586(2-17\times 0.0586)&&\approx 0.0588\end{aligned}}$

A typical initial guess can be found by rounding b to a nearby power of 2, then using bit shifts to compute its reciprocal.

In constructive mathematics , for a real number x to have a reciprocal, it is not sufficient that x ≠ 0 . There must instead be given a rational number r such that 0 < r < | x | . In terms of the approximation algorithm described above, this is needed to prove that the change in y will eventually become arbitrarily small.

This iteration can also be generalized to a wider sort of inverses; for example, matrix inverses .

## Reciprocals of irrational numbers

Every real or complex number excluding zero has a reciprocal, and reciprocals of certain irrational numbers can have important special properties. Examples include the reciprocal of e (≈ 0.367879) and the golden ratio 's reciprocal (≈ 0.618034). The first reciprocal is special because no other positive number can produce a lower number when put to the power of itself; $f{\bigl (}{\tfrac {1}{e}}{\bigr )}$ is the global minimum of f ( x ) = x x . The second number is the only positive number that is equal to its reciprocal plus one: $\varphi ={\frac {1}{\varphi }}+1.$ Its additive inverse is the only negative number that is equal to its reciprocal minus one: $-\varphi =-{\frac {1}{\varphi }}-1.$

The function

$f(n)={\tfrac {1}{2}}n+{\sqrt {\left({\tfrac {1}{2}}n\right)^{\!2}+1}}$

can be used to find the irrational number which differs from its reciprocal by an integer n , because in general f ( n ) – f ( n ) – 1 = n . For example:

${\begin{aligned}&f(4)=2+{\sqrt {5}};\qquad f^{-1}(4)={\frac {1}{2+{\sqrt {5}}}}=-2+{\sqrt {5}};\\&\therefore \,f(4)-f^{-1}(4)=4.\end{aligned}}$

Such irrational numbers share an evident property: they have the same fractional part as their reciprocal, since these numbers differ by an integer.

The reciprocal function plays an important role in simple continued fractions , which have a number of remarkable properties relating to the representation of (both rational and) irrational numbers.

## Further remarks

If the multiplication is associative, an element x with a multiplicative inverse cannot be a zero divisor ( x is a zero divisor if some nonzero y , xy = 0 ). To see this, it is sufficient to multiply the equation xy = 0 by the inverse of x (on the left), and then simplify using associativity. In the absence of associativity, the sedenions provide a counterexample.

The converse does not hold: an element which is not a zero divisor is not guaranteed to have a multiplicative inverse.
Within ⁠ $\mathbb {Z} ,$ ⁠ all integers except −1, 0, 1 provide examples; they are not zero divisors nor do they have inverses in ⁠ $\mathbb {Z} .$ ⁠ If the ring or algebra is finite , however, then all elements a which are not zero divisors do have a (left and right) inverse. For, first observe that the map f ( x ) = ax must be injective : f ( x ) = f ( y ) implies x = y : ${\begin{aligned}ax=ay&&\Rightarrow &\quad ax-ay=0\\&&\Rightarrow &\quad a(x-y)=0\\&&\Rightarrow &\quad x-y=0\\&&\Rightarrow &\quad x=y.\end{aligned}}$ Distinct elements map to distinct elements, so the image consists of the same finite number of elements, and the map is necessarily surjective . Specifically, f (namely multiplication by a ) must map some element x to 1 , ax = 1 , so that x is an inverse for a .

## Applications

The expansion of the reciprocal ${\tfrac {1}{q}}$ in any base can also act as a source of pseudo-random numbers , if q is a "suitable" safe prime , a prime of the form 2 p + 1 where p is also a prime. A sequence of pseudo-random numbers of length q − 1 will be produced by the expansion.
