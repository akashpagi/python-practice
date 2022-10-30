import first as f
import second as s

print(f.a)
f.name()
print()
print(s.a)
s.name()

print('-------------------------------')

from first import name,a
#print(a)
#name()
from second import name,a # here first module is replace by second module
print(a)
name()

print('--------------------------------')

from first import *
from second import *  # here first module is replace by second module
print(a)
print(t)  
name() 


''' 
# first.py <----- firat module
a='first module'
t=(1,2,3,4)
def name():
    print('name function from first module')



 # second.py <----- second module
a='second module'

def name():
    print('name function from second module')
    


'''