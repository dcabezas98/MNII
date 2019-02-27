from math import log2, ceil, exp # ceil: Redondeo ascendente

def f(x):
    return 3*x**2+exp(x)-2
    #return x**3-52
    #return x**5+3*x**2-5

def biseccion(f, a, b, error, exact):
    n = ceil(log2((b-a)/error)-1)     # Numero de pasos
    for i in range(n):
        x = (a+b)/2
        print("Iteracion "+str(i+1)+": Valor de X"+str(i)+"="+str(x))
        if abs(f(x))<exact:
        #if abs(x-a)<exact:    # exact=Tolerancia
            return x
        elif(f(a)*f(x)<0):
            b=x
        else:
            a=x
    return x

x=biseccion(f, 0, 1, 1e-25, 1e-5)
print("Raíz en x="+str(x))
print("f(x)="+str(f(x)))
