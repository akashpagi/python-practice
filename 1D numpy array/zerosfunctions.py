# creating array using zeros function:
import numpy as n
a=n.zeros(5)
b=n.zeros(5,dtype=int)
c=n.zeros((3,2)) # 2D numpy array
print(a,b)
print('2D numpy array') # 2D numpy array
print(c)

#accessing 1D numpy array using for loop:
import numpy as n
print('without index')
a=n.zeros(6)
for i in a:
    print(i)
import numpy as n
print('with index')
b=n.zeros(5,dtype=int)
n=len(b)
for j in range(n):
    print(j,'=',b[j])


#accessing 1D numpy array using while loop:
import numpy as n
print('using while loop')
a=n.zeros(5)
n=len(a)
i=0
while (i<n):
    print(a[i])
    i+=1