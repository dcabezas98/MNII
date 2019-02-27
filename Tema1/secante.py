from math import exp, cos

def f(x):
   # return x**2-3
    return 3*x**2+exp(x)-2

def secante(f, a, b, n, tol):
    for i in range(n):
        x = b-f(b)*(b-a)/(f(b)-f(a))
        print("Iteracion "+str(i+1)+": Valor de X"+str(i)+"="+str(x))
        if(abs(x-b)<tol):
            return x
        else:
            a=b
            b=x
    return x

x=secante(f, 0, 1, 50, 1e-5)
print("Raíz en x="+str(x))
print("f(x)="+str(f(x)))
