from sympy import *
A,B,C,R0 = 3.94*10**-3,-5.802*10**-7,-4.274*10**-12,100
x,y = symbols('x,y')
f1,f2 = R0+R0*A*x+R0*B*x**2-y,R0+R0*A*x+R0*B*x**2+R0*C*(x-100)**3-y
f3 = x-123
Temperture = solve([f2,f3],(x,y))
print(Temperture)