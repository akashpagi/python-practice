# creatting and accessing 2D array in array function :
import numpy as n 
a=n.array([[10,20,30,40],
           [50,60,70,80]])
print(a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[1][1])
print(a[1][2])
print(a[1][3])

 # modifying 2D array in array function :
import numpy as n 
a=n.array([[10,20,30,40],[50,60,70,80]])
a[0][3]=852
a[1][1]=123
print(a)
