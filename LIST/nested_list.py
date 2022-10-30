# nested list :
# ex. 1: nested list & indexing :
a=[1,2,3,[50,60]]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
print()

# modifying nested list :
a=[1,2,3,[50,60]]
print('modifying nested list :')
print('before :',a)
a[1]=200
a[3][0]=500
print('after modifying :',a)
