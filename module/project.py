#project.py <----- main module
import cal as c 

print("Cal module's variable :" ,c.a)
c.name()

a=c.add(10,30)
print(a)

s=c.sub
b=s(16,30)
print(b)

print('----------------------------------')

print( 'from cal import a,name,add ')
from cal import a,name,add
print(a) 
name()
a=add(59,23)
print(a)

print('----------------------------------')

print( 'from cal import a,name,add as x ')
from cal import a,name,sub as x
print(a) 
name()
z=x(2,3) 
print(z)

print('---------------------------------')

print('from cal import *')
from cal import *
_a_=add(9,100)
print(_a_)
name()