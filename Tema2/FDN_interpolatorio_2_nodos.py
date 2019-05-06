import sympy as sp, math as m

x, y = sp.symbols('x y')
sp.init_printing(use_unicode=True)

f=sp.Lambda(x, sp.exp(x))
r=sp.Lambda(y, sp.log(sp.cos(sp.exp(y)+y**2)))
g=sp.Lambda(x, sp.diff(r(x),x))

# Central
#f'(c)= (f(c+h)-f(c-h))/2h
def fdn(c, h, f):
    return (f(c+h)-f(c-h))/(2*h)

h=0.1
c=0

for i in range(5):
    print("h=",h)
    fdnc=fdn(c, h, r)
    print("f'(0)=", sp.N(fdnc))
    print("Error FDN:", abs(sp.N(fdnc-g(c))))
    h/=10
