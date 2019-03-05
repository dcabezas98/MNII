import math

def g(x):
    return x-(x**2-5)/10

###################################

def iteracion_funcional(g, x0, n, tol):
    x1=x0
    for i in range(n):
        x0=x1
        x11=g(x0)
        x21=g(x11)
        x1=x0-(x11-x0)**2/(x21-2*x11+x0)
        print("Iteracion "+str(i+1)+": Valor de X"+str(i+1)+"="+str(x1))
        #if abs(x1-x0) < tol:
        if abs(x1-math.sqrt(5))<tol:
            return x1
    return x1

y = iteracion_funcional(g, 1.5, 200, 1e-15)

print("Punto fijo en x="+str(y))
print("g("+str(y)+")="+str(g(y)))
