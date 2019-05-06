import sympy as sp, math as m

t, x = sp.symbols('t x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))
#f=sp.Lambda(x, sp.cos(x))
#f=sp.Lambda(x, 1/(1+x**2))
f=sp.Lambda(x, x**2*sp.exp(x))

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

        #print("alpha_"+str(i)+"="+str((l[i].integrate()(1)-l[i].integrate()(-1))))
        
        result += (l[i].integrate()(1)-l[i].integrate()(-1))*f(raices_legendre[i])

    return result        


def gaussiana(f, a, b, n, raices_legendre):

    g=sp.Lambda(t, f(((b-a)*t+b+a)/2))
    
    return legendre(g, raices_legendre)*(b-a)/2

raices_legendre1=[-0.5773502692, 0.5773502692]
raices_legendre2=[-0.7745966692, 0, 0.7745966692]
raices_legendre3=[-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116]
raices_legendre4=[-0.9061798459, -0.5384693101, 0, 0.5384693101, 0.9061798459]

raices_legendre=raices_legendre3

n = len(raices_legendre)-1
a, b = 0, 1/2

result = gaussiana(f, a, b, n, raices_legendre)

print(result)

# Compruebo exactitud
"""
p = sp.Poly(1,x)

for i in range(2*n+3): # Todos los errores deberian dar 0 menos el último
    #print(p)
    r = gaussiana(p, -1, 1, n, raices_legendre)
    print("Grado "+str(i)+" Error =", abs(r-p.integrate()(1)+p.integrate()(-1)))
    p*=sp.poly(x)
"""

# Ej 22
"""
fa=sp.Lambda(x, x**2*sp.log(x))
fb=sp.Lambda(x, x**3*sp.exp(-x))
fc=sp.Lambda(x, 3*x/(x**2-4))
fd=sp.Lambda(x, sp.cos(x)*sp.exp(3*x))

print("a) " + str(gaussiana(fa, 1, 1.5, 2, raices_legendre2)))
print("Error: " + str(abs(0.19225935773048122-gaussiana(fa, 1, 1.5, 2, raices_legendre2))))
print("b) " + str(sp.N(gaussiana(fb, 0, 1, 2, raices_legendre2))))
print("Error " + str(abs(0.11392894084187483-sp.N(gaussiana(fb, 0, 1, 2, raices_legendre2)))))
print("c) " + str(gaussiana(fc, 1, 1.8, 2, raices_legendre2)))
print("Error: " + str(abs(-2.059573828864272-gaussiana(fc, 1, 1.8, 2, raices_legendre2))))
print("d) " + str(gaussiana(fd, 0, m.pi/4, 2, raices_legendre2)))
print("Error " + str(abs(2.6841954140755666-gaussiana(fd, 0, m.pi/4, 2, raices_legendre2))))
"""
