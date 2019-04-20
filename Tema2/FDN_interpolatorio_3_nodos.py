from sympy import *

x = symbols('x')
init_printing(use_unicode=True)

f=Lambda(x, x*cos(x)-x**2*sin(x))
g=Lambda(x, diff(f(x),x))

# Progresiva
#f'(c)= (-3f(c)+4f(c+h)-f(c+2h))/2h
def fdn1(c, h, valores):
    return (-3*valores[c]+4*valores[c+h]-valores[c+2*h])/(2*h)
    #return (-3*valores[round(c,1)]+4*valores[round(c+h,1)]-valores[round(c+2*h,1)])/(2*h)

# Central
#f'(c)= (f(c+h)-f(fc-h))/2h
def fdn2(c, h, valores):
    return (valores[c+h]-valores[c-h])/(2*h)

# Regresiva
#f'(c)= (-f(c-2h)+4f(c-h)-3f(c))/2h
def fdn3(c, h, valores):
    return (valores[c-2*h]-4*valores[c-h]+3*valores[c])/(2*h)
    #return (valores[round(c-2*h,1)]-4*valores[round(c-h,1)]+3*valores[round(c)])/(2*h)

valores=dict({(2.9,-4.827866), (3.0,-4.240058), (3.1,-3.496909), (3.2,-2.596792)})

h=0.1
a=2.9

c=a+0*h
print("c=",c)

print("Progresiva:")
fdn1c=fdn1(c, h, valores)
print("FDN1: f'(c)=", fdn1c)
print("Error FDN1:", abs(fdn1c-g(c)))

c=a+1*h
print("c=",c)

print("Progresiva:")
fdn1c=fdn1(c, h, valores)
print("FDN1: f'("+str(c)+")=", fdn1c)
print("Error FDN1:", abs(fdn1c-g(c)))

print("Central:")
fdn2c=fdn2(c, h, valores)
print("FDN2: f'("+str(c)+")=", fdn2c)
print("Error FDN2:", abs(fdn2c-g(c)))

c=a+2*h
print("c=",c)

print("Central:")
fdn2c=fdn2(c, h, valores)
print("FDN2: f'("+str(c)+")=", fdn2c)
print("Error FDN2:", abs(fdn2c-g(c)))

print("Regresiva:")
fdn3c=fdn3(c, h, valores)
print("FDN3: f'("+str(c)+")=", fdn3c)
print("Error FDN3:", abs(fdn3c-g(c)))

c=a+3*h
print("c=",c)

print("Regresiva:")
fdn3c=fdn3(c, h, valores)
print("FDN3: f'("+str(c)+")=", fdn3c)
print("Error FDN3:", abs(fdn3c-g(c)))
