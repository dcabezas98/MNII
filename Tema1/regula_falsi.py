from math import exp, cos

def f(x):
    return exp(x)-cos(x)

def regula_falsi(f, a, b, exact):
    while True:
        x = b-f(b)*(b-a)/(f(b)-f(a))
        if(abs(f(x))<exact):
            return x
        elif(f(a)*f(x)<0):
            b=x
        else:
            a=x

print(regula_falsi(f, -2, -1, 1e-7))
