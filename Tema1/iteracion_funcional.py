import math

# Ejercicio 11: convergencia cúbica
"""
k = 7

alpha, beta = 3/4, 1/4

def g1(x):
    return (x**2+k)/(2*x)

def g2(x):
    return x*(3*k-x**2)/(2*k)

def g(x):
    return alpha*g1(x)+beta*g2(x)
"""
###################################

# Ejercicio 12:

def g1(x):
    return (x+5/x)/2

def g2(x):
    return x-(x**2-5)/10

###################################

def iteracion_funcional(g, x0, n, tol):
    x1=x0
    for i in range(n):
        x0=x1
        x1=g(x0)
        print("Iteracion "+str(i+1)+": Valor de X"+str(i+1)+"="+str(x1))
        if abs(x0-x1) < tol:
            return x1
    return x1

y = iteracion_funcional(g1, 1.5, 200, 1e-15)

print("Punto fijo en x="+str(y))
print("g("+str(y)+")="+str(g1(y)))
