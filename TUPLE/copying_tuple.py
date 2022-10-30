a=(1,2,3,4,5)
b=a
print('a:',a)
print('b:',b)
print()



b=a[0:5]
print('a:',a)
print('id(a):',id(a))
print('b:',b)
print('id(b):',id(b))
print()

a=a[1:4] # copy
print('a:',a)
print('id(a):',id(a))
print('b:',b)
print('id(b):',id(b))