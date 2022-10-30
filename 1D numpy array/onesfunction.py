# creating array using ones function:
import numpy as n
a=n.ones(5)
b=n.ones(5,dtype=int)
c=n.ones((3,2)) 
print(a)
print(b)
print(c)

#accessing 1D numpy array using for loop:
import numpy as n
print('without index')
a=n.ones(5)
for i in a:
    print(i)
import numpy as n
print('with index')
b=n.ones(5,dtype=int)
n=len(b)
for j in range(n):
    print(j,'=',b[j])


#accessing 1D numpy array using while loop:
import numpy as n
print('using while loop')
a=n.ones(5)
n=len(a)
i=0
while (i<n):
    print(a[i])
    i+=1                    