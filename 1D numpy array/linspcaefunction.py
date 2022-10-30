import numpy as n
a=n.linspace(1,3,5)
print(a[2]);print(a[3])

# accessing 1D numpy array using for loop:
import numpy as n
a=n.linspace(1,3,num=3)
print('with index')
n=len(a)
for i in range(n):
    print(i,'=',a[i])

import numpy as n
print('without index')
for j in a:
    print(j) 

# accessing 1D numpy array using while loop:
import numpy as np
print ('using while loop')
a=np.linspace(1,4,num=5) #or (1,4,5)
n=len(a)
i=0
while (i<n):
    print(a[i])
    i+=1