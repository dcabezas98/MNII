from math import log, log2, ceil, exp, cos # ceil: Redondeo ascendente

def f(x):
    return log(x**2+1)-exp(x/2)*cos(3*x)
    #return 3*x**2+exp(x)-2
    #return x**3-52
    #return x**5+3*x**2-5

def biseccion(f, a, b, error, res):
    n = ceil(log2((b-a)/error)-1)     # Numero de pasos
    for i in range(n):
        x = (a+b)/2
        print("Iteracion "+str(i+1)+": Valor de X"+str(i)+"="+str(x))
        if abs(f(x))<res:
            return x
        elif(f(a)*f(x)<0):
            b=x
        else:
            a=x
    return x

x=biseccion(f, -1, 0, 1e-20, 1e-6)
print("Raíz en x="+str(x))
print("f(x)="+str(f(x)))
