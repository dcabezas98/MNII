from sympy import *

x = symbols('x')
init_printing(use_unicode=True)

f=Lambda(x, exp(x))
g=Lambda(x, diff(f(x),x))

# Central
#f'(c)= (f(c+h)-f(c-h))/2h
def fdn(c, h, f):
    return (f(c+h)-f(c-h))/(2*h)

h=0.1
c=0

for i in range(5):
    print("h=",h)
    fdnc=fdn(c, h, f)
    print("f'(0)=", fdnc)
    print("Error FDN:", abs(fdnc-g(c)))
    h/=10
