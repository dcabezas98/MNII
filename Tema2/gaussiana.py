import sympy as sp, math as m

t, x = sp.symbols('t x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))
f=sp.Lambda(x, sp.cos(x))

"""
def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.cos(x)
"""

def legendre(f, raices_legendre):

    n = len(raices_legendre)-1
    
    l = [1]*(n+1)

    result = 0
    
    for i in range(n+1):
        for j in range(n+1):
            if i != j:
                l[i]*=sp.poly((x-raices_legendre[j])/(raices_legendre[i]-raices_legendre[j]))

        result += (l[i].integrate()(1)-l[i].integrate()(-1))*f(raices_legendre[i])

    return result        


def gaussiana(f, a, b, n, raices_legendre):

    g=sp.Lambda(t, f(((b-a)*t+b+a)/2))
    
    return legendre(g, raices_legendre)*(b-a)/2


raices_legendre=[-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116]

n = len(raices_legendre)-1

result = gaussiana(f, -1, 2, n, raices_legendre)

print(result)

# Compruebo exactitud

p = sp.Poly(1,x)

for i in range(2*n+3): # Todos los errores deberian dar 0 menos el último
    #print(p)
    r = gaussiana(p, -1, 1, n, raices_legendre)
    print("Grado "+str(i)+" Error =", abs(r-p.integrate()(1)+p.integrate()(-1)))
    p*=sp.poly(x)
