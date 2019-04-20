import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))

def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.cos(x)


def trapecio_compuesta(f, a, b, n):
    
    h = (b-a)/n

    result = (f(a)+f(b))/2
    
    for i in range(1, n):
        result += f(a+i*h)

    result *= h
        
    return result        


result = trapecio_compuesta(f, -1, 1, 500)

print(result)
