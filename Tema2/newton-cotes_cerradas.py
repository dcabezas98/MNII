import sympy as sp, math as m

x, y = sp.symbols('x y')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))
#f=sp.Lambda(x, x**4*sp.exp(-2*x**2))
#f=sp.Lambda(x, 1/(1+x**2)) # Esta no converge
f=sp.Lambda(x, sp.exp(sp.sin(x)**2-2))

"""
def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    #return m.cos(x)
    return x**4*m.exp(-2*x**2)
"""

def lagrange(nodes):
    
    l = []
    for i in range(len(nodes)):
        l.append(1)
        for j in range(len(nodes)):
            if j != i:
                l[i]*=sp.poly((x-nodes[j])/(nodes[i]-nodes[j]))

    return l


def n_c(f, a, b, n):
    
    nodes = []
    h = (b-a)/n
    
    for i in range(n+1):
        k = a+i*h
        nodes.append(k)

    l = lagrange(nodes)
        
    result = 0

    for i in range(n+1):
        result += (l[i].integrate()(b)-l[i].integrate()(a))*sp.N(f(nodes[i]))

    return result        

n=8
a,b=0, 2

result = n_c(f, a, b, n)

print(result)


# Error para n par:
"""
def k(n):

    p = sp.Poly(y,y)

    for i in range(0,n+1): # desde 1 si n impar
        p*=sp.Poly(y-i,y)

    result = p.integrate()(n)-p.integrate()(0)

    result /= m.factorial(n+2) # si n impar, n+1

    return result
"""

"""
kn = k(n)
h = (b-a)/n

#g=sp.Lambda(x, sp.diff(f(x),x,n+2))
#print(g(x))

cota_n2=80640 # Introducir a mano

print("k"+str(n)+"="+str(kn))
print("Cota error: "+str(abs(kn*h**(n+3)*cota_n2)))
"""


# Ej 14, trapecio:
"""
def fa(x):
    return x**2*m.log(x)

def fb(x):
    return x**3*m.exp(-x)

def fc(x):
    return 3*x/(x**2-4)

def fd(x):
    return m.cos(x)*m.exp(3*x)


print("a) " + str(n_c(fa, 1, 1.5, 1)))
print("b) " + str(n_c(fb, 0, 1, 1)))
print("c) " + str(n_c(fc, 1, 1.8, 1)))
print("d) " + str(n_c(fd, 0, m.pi/4, 1)))

# simpson

print("a) " + str(n_c(fa, 1, 1.5, 2)))
print("b) " + str(n_c(fb, 0, 1, 2)))
print("c) " + str(n_c(fc, 1, 1.8, 2)))
print("d) " + str(n_c(fd, 0, m.pi/4, 2)))
"""
