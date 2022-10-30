# any function
import numpy as n
print('without any()function')
a=n.array([10,2,30,40])
b=n.array([10,20,30,40])
c=a==b
print(c)
print('with any()function')
a=n.array([10,20,30,40])
b=n.array([1,20,3,2])
c=a==b
print(any(c))

'''

# all function
import numpy as n
a=n.array([1,20,3,4])
b=n.array([10,20,30,40])
c=a==b
print(all(c))
'''
