from sympy import poly, Poly, pdiv, degree, LC
from sympy.abc import x

def euclides(f0, f1):
    r = poly(x)
    while degree(r, gen=x) > 0:
        c, r = pdiv(f0,f1)
        f0, f1 = f1, -r    
    return f0

def simplify_roots(f):
    f1=Poly(f,x).diff()
    d=euclides(f,f1)
    return pdiv(f, d)[0]

c=simplify_roots(Poly(4*x**6+4*x**5+5*x**4+6*x**3-5*x**2-4*x+2, domain='QQ'))
print(c/LC(c))
