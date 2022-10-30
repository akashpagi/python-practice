#creatting 2D array using array ones function :
import numpy as n 
a=n.ones((3,2),dtype=int)
print(a)
print()

# accesing 2D array using while loop:
import numpy as n 
print('with index')
a=n.ones((3,2),dtype=int)
n=len(a)
i=0
while(i<n):
    j=0
    while(j<len(a[i])):
        print(i,j,'=',a[i][j])
        j+=1
    i+=1
    print()

#accessing & modifying 2D array elements:
import numpy as n 
a=n.ones((3,4),dtype=int)
a[0][0]=26
a[2][0]=2001
a[1][0]=7
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1]) 
print()

# accesing 2D array using for loop:
import numpy as n 
a=n.ones((3,2),dtype=int)
print('without index')
for i in a:
    for j in i:
        print(j)
print()

import numpy as n 
a=n.ones((3,2),dtype=int)
print('with index')
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,'=',a[i][j])
print()
