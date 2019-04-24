import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))

def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.exp(3*x)*m.sin(3*x)/(x**4+1)


def trapecio_compuesta(f, a, b, n):
    
    h = (b-a)/n

    result = (f(a)+f(b))/2
    
    for i in range(1, n):
        result += f(a+i*h)

    result *= h
        
    return result        


a, b = 0,2
n = 1155

result = trapecio_compuesta(f, a, b, n)

print(result)

# Error

h = (b-a)/n

cota_2 = 200

print("Cota error: "+str(abs((b-a)*h**2/12*cota_2)))
