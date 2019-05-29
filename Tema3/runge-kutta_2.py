import numpy as np, math as m
import matplotlib.pyplot as plt

def f(t, y):  # solucion y(t)=t+exp(-t)
    return -y+t+1

y0 = 1

def runge_kutta2(f, a, b, n, y0, b1, b2, c2):

    u = [y0]

    h = (b-a)/n
    
    for j in range(0, n):
        K1= f(a+j*h, u[j])
        K2= f(a+j*h+c2*h, u[j]+c2*h*K1)
        u.append(u[j]+h*(b1*K1+b2*K2))

    return u


# Euler mejorado
b1 = 0
b2 = 1
c2 = 1/2

# Heun
"""
b1 = 1/2
b2 = 1/2
c2 = 1
"""

a, b = 0, 1
n = 10

h = (b-a)/n

u = runge_kutta2(f, a, b, n, y0, b1, b2, c2)

r = [a+i*h for i in range(n+1)]

def result(t):
    return t+np.exp(-t)
    
    
plt.plot(r, u, 'ro') # ro = red o (puntos)
plt.plot(r, [result(t) for t in r])

plt.show()
