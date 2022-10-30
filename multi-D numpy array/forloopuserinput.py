import numpy as n 
r = int(input('enter the rows number:'))
c = int(input('enter the columns number:'))
a = n.zeros((r,c),dtype=int)
n = len(a)
print(a)
for i in range(n):
    for j in range(len(a[i])):
        x = int(input('enter elements:'))
        a[i][j] = x

for m in a:
    for p in m:
        print(p)
print(a)

    