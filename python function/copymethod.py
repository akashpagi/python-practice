import numpy as n 
a=n.array([10,20,30,40,50])
b=a.copy()
print(a)
print(b)
print('memory location is diffrent')
print('a',id(a))
print('b',id(b))

import numpy as n 
a=n.array([10,20,30,40,50])
b=a.copy()
print('modified a & b value diffent')
a[2]=80
b[3]=300
print(a)
print(b)