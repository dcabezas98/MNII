import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))

def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.cos(x)


def simpson_compuesta(f, a, b, n):

    m = 2*n
    
    h = (b-a)/m

    result = f(a)+f(b)
    
    for i in range(1, n+1):
        result += 4*f(a+(2*i-1)*h)

    for i in range(2, n+1):
        result += 2*f(a+(2*i-2)*h)

    result *= h/3
        
    return result        


result = simpson_compuesta(f, -1, 1, 500)

print(result)
