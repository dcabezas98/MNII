from sympy import *

x = symbols('x')
init_printing(use_unicode=True)

#f=Lambda(x, x**2-3)
#f=Lambda(x, 3*x-2-x**2+math.e**x) #f funcion que a x le asigna 3*x....
#f=Lambda(x, x**2+10*cos(x)+x)
#f=Lambda(x, 3*x**2+exp(x)-2)
f=Lambda(x, x**3-3*x**2*2**(-x)+3*x*4**(-x)-8**(-x))

f1=Lambda(x, diff(f(x),x))

def newton_raphson(f, x0, n, tol):
    for i in range(n):
        x1 = x0-N(f(x0),32)/N(f1(x0),32)
        print("Iteracion "+str(i+1)+": Valor de X"+str(i+1)+"="+str(x1))
        if abs(x1-x0)<tol:
        #if abs(N(f(x1),32))<tol:    # Residuo
            return N(x1, 18) # N(x,n): evaluacion numerica con n digitos
        else:
            x0=x1
    return N(x1, 18)

y=newton_raphson(f, 1, 99999, 1e-7)
print("Raíz en x="+str(y))
print("f(x)="+str(f(y)))

# Estudio orden convergencia
"""
n=36
x0=1
for i in range(n-1):
    x1 = x0-N(f(x0),32)/N(f1(x0),32)
    print(abs(x1-y)/abs(x0-y)**2)
    x0=x1

f2=Lambda(x, diff(f1(x),x))
print("f''(x)="+str(N(f2(y))))
"""
