import numpy as n 
a=n.array([1,2,3,4,5,6])
b=n.array([[10,20,30],[40,50,60],[70,80,90]])
c=n.array([[[1,2,3],[4,5,6],[7,8,9]]])
print()
 
# ndim attribute :
print('1D array ndim :',a.ndim)
print('2D array ndim :',b.ndim)
print('3D array ndim :',c.ndim)
print()

# shape attribute :
# for 1D array shape elements in the row 
# for 2D array shape specifies number of row and colum in each row 
print('1D shape :',a.shape)
print('2D shape :',b.shape)
print('3D shape :',c.shape)
print()

# size attribute :
print('1D size :',a.size)
print('2D size :',b.size)
print('3D size :',c.size)
print()

# itemsize attribute :
print('1D itemsize :',a.itemsize)
print('2D itemsize :',b.itemsize)
print('3D itemsize :',c.itemsize)
print()

# dtype attribute :
print('1D dtype :',a.dtype)
print('2D dtype :',b.dtype)
print('3D dtype :',c.dtype)
print()

# nbytes attribute :
print('1D nbytes :',a.nbytes)
print('2D nbytes :',b.nbytes)
print('3D nbytes :',c.nbytes)
print()



