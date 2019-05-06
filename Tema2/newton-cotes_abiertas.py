import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))

def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    #return m.cos(x)
    return x**3*m.cos(x**2+3)

    
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
    h = (b-a)/(n+2)
    
    for i in range(n+1):
        k = a+(i+1)*h
        nodes.append(k)

    if n == 0:
        return (b-a)*f(a+h)
        
    l = lagrange(nodes)
        
    result = 0

    for i in range(n+1):
        result += (l[i].integrate()(b)-l[i].integrate()(a))*f(nodes[i])

    return result        

n = 0
a, b = 1, 1.5

result = n_c(f, a, b, n)

print(result)


# Ej 14, punto medio:
"""
def fa(x):
    return x**2*m.log(x)

def fb(x):
    return x**3*m.exp(-x)

def fc(x):
    return 3*x/(x**2-4)

def fd(x):
    return m.cos(x)*m.exp(3*x)


print("a) " + str(n_c(fa, 1, 1.5, 0)))
print("b) " + str(n_c(fb, 0, 1, 0)))
print("c) " + str(n_c(fc, 1, 1.8, 0)))
print("d) " + str(n_c(fd, 0, m.pi/4, 0)))
"""
