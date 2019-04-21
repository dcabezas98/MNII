from sympy import *

x = symbols('x')
init_printing(use_unicode=True)

#f=Lambda(x, x*cos(x)-x**2*sin(x))
f=Lambda(x, 2**x*sin(x))
g=Lambda(x, diff(f(x),x))


#f'(c)= 8(32/3f(c+h/8)-4/3f(c+h/4)-217/24f(c)-1/3f(c+h/2)+1/24f(c+h))/7h
def fdn(f, c, h):
    return 8*(32/3*f(c+h/8)-4/3*f(c+h/4)-217/24*f(c)-1/3*f(c+h/2)+1/24*f(c+h))/(7*h)

h=0.4
c=1.05

print("c=",c)

fdnc=fdn(f,c,h)
print("FDN: f'("+str(c)+")=", fdnc)
print("Error FDN:", abs(N(fdnc-g(c))))
