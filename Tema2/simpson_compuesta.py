import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))
#f=sp.Lambda(x, sp.log(x+2)/(x**2+1))
#f=sp.Lambda(x, x**2*sp.exp(x))

f=sp.Lambda(x, sp.exp(sp.sin(x)**2-2))

"""
def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    #return m.exp(3*x)*m.sin(3*x)/(x**4+1)
    return x**3*m.cos(x**2+3)
"""

def simpson_compuesta(f, a, b, n):

    m = 2*n
    
    h = (b-a)/m

    result = sp.N(f(a)+f(b))
    
    for i in range(1, n+1):
        result += sp.N(4*f(a+(2*i-1)*h))

    for i in range(2, n+1):
        result += sp.N(2*f(a+(2*i-2)*h))

    result *= h/3
        
    return result   


a, b = 0, 2
n = 54

result = simpson_compuesta(f, a, b, n)

print(result)

# Error

h = (b-a)/(2*n)

cota_4=7.3576

print("Cota error: "+str(abs((b-a)*h**4/180*cota_4)))

print("Error: "+str(abs(result-simpson_compuesta(f,a,b,500))))


# Ej 14
"""
def fa(x):
    return x**2*m.log(x)

def fb(x):
    return x**3*m.exp(-x)

def fc(x):
    return 3*x/(x**2-4)

def fd(x):
    return m.cos(x)*m.exp(3*x)


print("a) " + str(simpson_compuesta(fa, 1, 1.5, 50)))
print("b) " + str(simpson_compuesta(fb, 0, 1, 50)))
print("c) " + str(simpson_compuesta(fc, 1, 1.8, 50)))
print("d) " + str(simpson_compuesta(fd, 0, m.pi/4, 50)))
"""
