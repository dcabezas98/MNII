from sympy import poly, Poly, degree, N, sqrt
from sympy.abc import x

def bairstow(f, r, s, k):

    n=degree(f,x)
    
    for _ in range(k):
   
        b0, b1 = 0, 0
        c0, c1, c2 = 0, 0, 0
        for i in range(n, -1, -1):
            b=f.nth(i)+r*b0+s*b1 # nth(i), coeficiente de grado i
            b0, b1 = b, b0
            c=b+r*c0+s*c1
            c3, c2, c1, c0 = c2, c1, c0, c
        
        D=c1*c3-c2**2
        
        r+=N((b1*c2-b0*c3)/D)
        s+=N((c2*b0-c1*b1)/D)

    return poly(x**2-r*x-s)

f=poly(x**4+x**3/2+3*x**2/2+x-1)

p=bairstow(f, 1, 1, 10)

a=p.nth(2)
b=p.nth(1)
c=p.nth(0)

x1=(-b+sqrt(b**2-4*a*c))/(2*a)
x2=(-b-sqrt(b**2-4*a*c))/(2*a)

print(p)
print('X1='+str(x1), ' X2='+str(x2))
print('f(X1)='+str(f(x1)), ' f(X2)='+str(f(x2)))
