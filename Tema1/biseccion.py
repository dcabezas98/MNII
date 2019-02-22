from math import log2, ceil # ceil: Redondeo ascendente

def f(x):
    #return x**3+4*x**2-10
    return x**5+3*x**2-5

def biseccion(f, a, b, error, exact):
    n = ceil(log2((b-a)/error)-1)     # Número de pasos
    for i in range(n):
        x = (a+b)/2
        if(abs(f(x))<exact):
            return x
        elif(f(a)*f(x)<0):
            b=x
        else:
            a=x
    return x

print(biseccion(f, -0.5, 1.5, 1e-8, 1e-7))
