import numpy as n 
a=n.array([[10,20,30,40],[50,60,70,80]])
print('without index')
for r in a:
    for c in r:
        print(c)
    print() 

    

import numpy as n 
a=n.array([[10,20,30,40],[50,60,70,80]])
print('with index')
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,'=',a[i][j])
    print()
