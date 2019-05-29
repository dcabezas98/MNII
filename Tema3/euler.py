import numpy as np, math as m
import matplotlib.pyplot as plt

def f(t, y):  # solucion y(t)=t+exp(-t)
    return m.sqrt(y)

y0 = 1e-5

a, b = 0, 1
n = 10

def euler(f, a, b, n, y0):

    u = [y0]

    h = (b-a)/n
    
    for j in range(n):              
        u.append(u[j]+h*f(a+h*j, u[j]))

    return u


h = (b-a)/n

u = euler(f, a, b, n, y0)

print(u)

r = [a+i*h for i in range(n+1)]

def result(t):
    return t**2/4
    
    
plt.plot(r, u, 'ro') # ro = red o (puntos)
plt.plot(r, [result(t) for t in r])

plt.show()
