# creating array using arange function:
import numpy as n
a=n.arange(5)
b=n.arange(5.0)
c=n.arange(1,6)
d=n.arange(1,10,2)
print(a)
print(b)
print(c)
print(d)

#accessing 1D numpy array using for loop:
import numpy as n
print('without index')
a=n.arange(2,6)
for i in a:
    print(i)
import numpy as n
print('with index')
b=n.arange(1,5)
n=len(b)
for j in range(n):
    print(j,'=',b[j])


#accessing 1D numpy array using while loop:
import numpy as n
print('using while loop')
a=n.arange(0,10,2)
n=len(a)
i=0
while (i<n):
    print(a[i])
    i+=1