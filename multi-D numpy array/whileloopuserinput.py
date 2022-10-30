import numpy as np
m  = int(input('enter the rows no.:'))
n = int(input('enter the columns no.:'))
a = np.zeros((m,n),dtype=int)
print(a)


u = len(a)
i = 0
while (i<u):
    j = 0
    while j < len(a[i]):
        x = int(input('enter elements:'))
        a[i][j] = x
        j+=1
    i+=1
print(a)

print()
print('with index')
i = 0
while (i<u):
    j = 0
    while j < len(a[i]):
        print(i,j,'=',a[i][j])
        j+=1
    i+=1
print(a)

 