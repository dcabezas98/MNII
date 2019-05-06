import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))
#f=sp.Lambda(x, sp.exp(sp.sin(x)**2-2))

"""
def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.exp(3*x)*m.sin(3*x)/(x**4+1)
"""

def trapecio_compuesta(f, a, b, n):
    
    h = (b-a)/n

    result = sp.N(f(a)+f(b))/2
    
    for i in range(1, n):
        result += sp.N(f(a+i*h))

    result *= h
        
    return result        

"""
a, b = 0,2
n = 8

result = trapecio_compuesta(f, a, b, n)

print(result)

# Error

h = (b-a)/n

cota_2 = 0.73576

print("Cota error: "+str(abs((b-a)*h**2/12*cota_2)))
"""

# 2 Examen

f=sp.Lambda(x, (sp.cos(sp.pi*x)+1)**(10/3))
a, b = 0, 1
solution = 3.000492123714049

n = 2

for _ in range(6):
    result = trapecio_compuesta(f, a, b, n)
    print(str(n)+ " subintervalos:")
    print("\t"+str(result))
    print("\tError:" + str(abs(result-solution)))
    #print("\tError/4:" + str(abs(result-solution)/4))
    n*=2
