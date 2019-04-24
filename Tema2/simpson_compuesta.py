import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))

def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.exp(3*x)*m.sin(3*x)/(x**4+1)


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


a, b = 0,2
n = 23

result = simpson_compuesta(f, a, b, n)

print(result)

# Error

h = (b-a)/(2*n)

cota_4=2495

print("Cota error: "+str(abs((b-a)*h**4/180*cota_4)))
