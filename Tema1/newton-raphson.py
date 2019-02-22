from sympy import *
x, y, z = symbols('x y x')
init_printing(use_unicode=True)

f=Lambda(x, x**2-3)
f1=Lambda(x, diff(f(x),x))

def newton_raphson(f, x0, n, tol):
    for i in range(n):
        x1 = x0-f(x0)/f1(x0)
        if(abs(x1-x0)<tol):
            return N(x1, 18) # N(x,n): evaluacion numerica con n digitos
        else:
            x0=x1
    return N(x1, 18)

print(newton_raphson(f, 2, 10, 1e-12))
