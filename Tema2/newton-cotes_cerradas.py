import sympy as sp, math as m

x, y = sp.symbols('x y')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))
#f=sp.Lambda(x, x**4*sp.exp(-2*x**2))
f=sp.Lambda(x, 1/(1+x**2))

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
        result += (l[i].integrate()(b)-l[i].integrate()(a))*f(nodes[i])

    return result        

n=50
a,b=-4, 4

result = n_c(f, a, b, n)

print(result)


# Error:

def k(n):

    p = sp.Poly(y,y)

    for i in range(n+1):
        p*=sp.Poly(y-i,y)

    result = p.integrate()(n)-p.integrate()(0)

    result /= m.factorial(n+2)

    return result

"""
kn = k(n)
h = (b-a)/n

#g=sp.Lambda(x, sp.diff(f(x),x,n+2))
#print(g(x))

cota_n2=80640 # Introducir a mano

print("k"+str(n)+"="+str(kn))
print("Cota error: "+str(abs(kn*h**(n+3)*cota_n2)))
"""
