
# passing  and returning numpy array from function :
import numpy as n
na=n.array([10,20,30,40,50])
def show(na):
    print('n :',na)
    print(type(na))
    for i in na:
        print(i)
    return na
y=show(na)
print('y :',y)
print(type(y))
for i in y:
    print(i)


  