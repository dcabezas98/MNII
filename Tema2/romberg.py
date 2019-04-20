import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))

def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.cos(x)


def trapecio_compuesta(f, a, b, n):
    
    h = (b-a)/n

    result = (f(a)+f(b))/2
    
    for i in range(1, n):
        result += f(a+i*h)

    result *= h
        
    return result


def romberg(f, a, b, n):

    R=[[]]*(n+1)
    
    R[0].append(trapecio_compuesta(f, a, b, 1))

    for k in range(1,n+1):

        hk=(b-a)/2**k
        aux = 0
        for i in range(1,2**k):
            aux+=f(a+(2*i-1)*hk)
        R[k].append(R[k-1][0]/2+hk*aux)
    
    for j in range(1,n+1):
        for k in range(j, n+1):
            R[k][j]=R[k][j-1]*(1+1/(4**j-1))-1/(4**j-1)*R[k-1][j-1]

    print(R)
    return R[n][n]

    
result = romberg(f, -1, 1, 3)

print(result)
