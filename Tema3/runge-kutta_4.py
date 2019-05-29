import numpy as np, math as m
import matplotlib.pyplot as plt

def f(t, y):  # solucion y(t)=t+exp(-t)
    #return -y+t+1
    #return (2-2*t*y)/(1+t**2) #12
    return y**2/(1+t) #3

#y0 = 1 #12
y0 = -1/m.log(2) #3

a, b = 1, 2
n = 10

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


h = (b-a)/n

u = runge_kutta4(f, a, b, n, y0)

print(u)

r = [a+i*h for i in range(n+1)]

def result(t):
    #return (2*t+1)/(t**2+1) #12
    return -1/m.log(t+1) #3
    

print("Errores: ")
print([abs(u[j]-result(a+j*h)) for j in range(n+1)])
    
plt.plot(r, u, 'ro') # ro = red o (puntos)
plt.plot(r, [result(t) for t in r])

plt.show()
