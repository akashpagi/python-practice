import numpy as n
print( 'with index')
num=n.array([1,2,3,4,5])
n=len(num)
for i in range(n):
    print(i,'=',num[i])


print('without index')
for element in num:
    print(element)

