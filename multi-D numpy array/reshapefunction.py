# convert 1D array to 2D arrray using reshape function :
print('convert 1D array to 2D arrray')
import numpy as n 
a=n.array([1,2,3,4,5,6])
b=n.reshape(a,(2,3))
print(b)
print()

# convert 1D array to 3D arrray using reshape function :
print('convert 1D array to 3D arrray')
import numpy as n 
a=n.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=n.reshape(a,(2,3,2))
print(b)
print()


# convert 2D array to 1D arrray using reshape function :
print('convert 2D array to 1D arrray')
import numpy as n 
a=n.array([[1,2,3],[4,5,6]])
b=n.reshape(a,(6))
print(b)
print()

# convert 3D array to 1D arrray using reshape function :
print('convert 3D array to 1D arrray')
import numpy as n 
a=n.array([[[1,2,3],[4,5,6],[7,8,9]]])
b=n.reshape(a,(9))
print(b)
print()


print('flatten method : convert 2D or 3D array to 1D array:')
import numpy as n 
a= a=n.array([[1,2,3],[4,5,6]])
b=a.flatten()
print(b)