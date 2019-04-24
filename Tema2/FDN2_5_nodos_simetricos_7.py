from sympy import *

x = symbols('x')
init_printing(use_unicode=True)

f=Lambda(x, cos(x))
g=Lambda(x, diff(f(x),x,2))

#f''(c)= (-1/12*f(c-2h)+4/3*f(c-h)-5/2*f(c)+4/3*f(c+h)-1/12*f(c+2h))/h**2
def fdn2(f, c, h):
    return (-1/12*f(c-2*h)+4/3*f(c-h)-5/2*f(c)+4/3*f(c+h)-1/12*f(c+2*h))/h**2

h=0.001
c=0

fdn2c=fdn2(f, c, h)
print("FDN2: f''(c)=", fdn2c)
print("Error FDN2:", abs(fdn2c-g(c)))
