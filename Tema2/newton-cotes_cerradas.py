import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))

def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.cos(x)

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


result = n_c(f, -1, 2, 6)

print(result)
