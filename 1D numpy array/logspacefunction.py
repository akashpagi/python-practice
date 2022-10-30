# creating array using logspace function:
import numpy as n
a=n.logspace(1,3,num=5,base=10)
print(a)

#accessing 1D array elements:
import numpy as n
a=n.logspace(1,3,num=5,base=10)
print(a[0]);print(a[3]);print(a[2])

#accessing 1D numpy array using for loop:
import numpy as n
print('without index')
a=n.logspace(1,3,num=3,base=10)
for i in a:
    print(i)
import numpy as n
print('with index')
a=n.logspace(1,3,num=3,base=2)
n=len(a)
for j in range(n):
    print(j,'=',a[j])

#accessing 1D numpy array using while loop:
import numpy as n
print('using while loop')
a=n.logspace(1,3,num=3,base=10)
n=len(a)
i=0
while (i<n):
    print(a[i])
    i+=1



