from sympy import poly, Poly, degree, Lambda, diff, symbols
from sympy.abc import x

r, s = symbols('r s')

def bairstow(f, r0, s0):
    n=degree(f,x)
    b=[Lambda((r,s), 0), Lambda((r,s), 0)]
    
    for i in range(n, -1, -1):
        b.append(Lambda((r,s), f.nth(i)+r*b[n-i+1](r,s)+s*b[n-i](r,s))) # nth(i), coeficiente de grado i
        
        """
    b[0]=Lambda((r,s), b[0](r0,s0)+diff(b[0](r,s),r).subs([(r,r0),(s,s0)])*(r-r0)+diff(b[0](r,s),s).subs([(r,r0),(s,s0)])*(s-s0))
    b[1]=Lambda((r,s), b[1](r0,s0)+diff(b[1](r,s),r).subs([(r,r0),(s,s0)])*(r-r0)+diff(b[1](r,s),s).subs([(r,r0),(s,s0)])*(s-s0))
        """

    c1=Lambda((r,s), 0)
    c2=Lambda((r,s), 0)
    for i in range(n, 0, -1):
        c=Lambda((r,s), b[n-i]+r*c1(r,s)+s*c2(r,s))
        c3, c2, c1 = c2, c1, c
        
    D=

print(bairstow(poly(x**4+x**3/2+3*x**2/2+x-1),1,1))
