from math import log, exp, cos 

def f(x):
    return log(x**2+1)-exp(x/2)*cos(3*x)
    #return 3*x**2+exp(x)-2
    #return exp(x)-cos(x)
    #return x**3-52

def regula_falsi(f, a, b, res):
    i=1
    while True:
        x=b-f(b)*(b-a)/(f(b)-f(a))
        print("Iteracion "+str(i)+": Valor de X"+str(i-1)+"="+str(x))
        i+=1
        if abs(f(x))<res:
            return x
        elif(f(a)*f(x)<0):
            b=x
        else:
            a=x

def regula_falsi_tol(f, a, b, tol):
    i=1
    x=b-f(b)*(b-a)/(f(b)-f(a))
    print("Iteracion "+str(i)+": Valor de X"+str(i-1)+"="+str(x))
    i+=1
    if(f(a)*f(x)<0):
        b=x
    else:
        a=x
        
    while True:
        y=x
        x=b-f(b)*(b-a)/(f(b)-f(a))
        print("Iteracion "+str(i)+": Valor de X"+str(i-1)+"="+str(x))
        i+=1
        if abs(x-y)<tol:
            return x
        elif(f(a)*f(x)<0):
            b=x
        else:
            a=x

x=regula_falsi(f, -1, 0, 1e-6)
#x=regula_falsi_tol(f, 0, 1, 1e-5)
print("Raíz en x="+str(x))
print("f(x)="+str(f(x)))
