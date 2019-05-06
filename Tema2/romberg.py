import sympy as sp, math as m

x = sp.symbols('x')
sp.init_printing(use_unicode=True)

#f=sp.Lambda(x, x*sp.cos(x)-x**2*sp.sin(x))
#f=sp.Lambda(x, sp.exp(x)*sp.cos(x))
#f=sp.Lambda(x, sp.sqrt(x))


"""
def f(x):
    #return x*m.cos(x)-x**2*m.sin(x)
    return m.cos(x)
"""


def trapecio_compuesta(f, a, b, n):
    
    h = (b-a)/n

    result = (f(a)+f(b))/2
    
    for i in range(1, n):
        result += f(a+i*h)

    result *= h
        
    return result


def romberg(f, a, b, n):

    R=[[0 for _ in range(n+1)] for _ in range(n+1)]
    
    R[0][0]=trapecio_compuesta(f,a,b,1)
        
    for k in range(1,n+1):

        hk=(b-a)/2**k
        aux = 0
        for i in range(1,2**(k-1)+1):
            aux+=sp.N(f(a+(2*i-1)*hk))
        R[k][0]=R[k-1][0]/2+hk*aux
    
    for j in range(1,n+1):
        for k in range(j, n+1):
            R[k][j]=R[k][j-1]*(1+1/(4**j-1))-1/(4**j-1)*R[k-1][j-1]

    #return R[n][n], R[n][0]
    return R

"""
a, b = 0, m.pi
n = 12
"""

"""
result = romberg(f, a, b, n)
print(result)
"""

# solution = romberg(f, a, b, 12)[0]
# solution = 2/3

"""
for k in range(n+1):
    r = romberg(f, a, b, k)
    print("R[{0}][0]={1}, error={3}\tR[{0}][{0}]={2}, error={4}".format(k, r[1], r[0], abs(r[1]-solution), abs(r[0]-solution)))

"""

# Estimación Ek=4/3(Rk,0-Rk+1,0)
"""
R = romberg(f, a, b, n)

for k in range(n):
    print("R[{0}][0]={1}, error={2}, estimacion={3}".format(k, sp.N(R[k][0]), sp.N(abs(R[k][0]-R[n][n])),  sp.N(4/3*abs(R[k][0]-R[k+1][0]))))
"""

# 2 Examen

f=sp.Lambda(x, (sp.cos(sp.pi*x)+1)**(10/3))
a, b = 0, 1
solution = 3.000492123714049

n = 10
R = romberg(f, a, b, n)

print('Romberg')

for j in range(1, n+1):
    print("R[{0}][{0}]={1}".format(j, R[j][j]))
    print("\tError:" + str(abs(R[j][j]-solution)))

for j in range(1, n):
    print(abs(R[j][j]-solution)/abs(R[j+1][j+1]-solution))
    
print('\nTrapecio Compuesta')

for j in range(1, n+1):
    print("R[{0}][0]={1}".format(j, R[j][0]))
    print("\tError:" + str(abs(R[j][0]-solution)))

for j in range(1, n):
    print(abs(R[j][0]-solution)/abs(R[j+1][0]-solution))
