import numpy as n 
a=n.array([10,20,30,40,50])
b=n.array([5,40,60,40,60])
#(a>b,a,b)
c=n.where(a>=b,a,b)
print(c)