import numpy as np, math as m
import matplotlib.pyplot as plt

def f(t, y):  # solucion y(t)=t+exp(-t)
    return -y+t+1

y0 = 1

def runge_kutta4(f, a, b, n, y0):

    u = [y0]

    h = (b-a)/n
    
    for j in range(n):
        K1= f(a+j*h, u[j])
        K2= f(a+j*h+h/2, u[j]+h*K1/2)
        K3= f(a+j*h+h/2, u[j]+h*K2/2)
        K4= f(a+j*h+h, u[j]+h*K3)
              
        u.append(u[j]+h*(K1+2*K2+2*K3+K4)/6)

    return u



a, b = 0, 1
n = 10

h = (b-a)/n

u = runge_kutta4(f, a, b, n, y0)

r = [a+i*h for i in range(n+1)]

def result(t):
    return t+np.exp(-t)
    
    
plt.plot(r, u, 'ro') # ro = red o (puntos)
plt.plot(r, [result(t) for t in r])

plt.show()


print(u)
