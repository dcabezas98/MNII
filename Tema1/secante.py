from math import exp, cos

def f(x):
    return x**2-3

def secante(f, a, b, n, tol):
    for i in range(n):
        x = b-f(b)*(b-a)/(f(b)-f(a))
        if(abs(x-b)<tol):
            return x
        else:
            a=b
            b=x
    return x

print(secante(f, 1, 2, 10, 1e-7))
