a=(1,2,3,4,5)
b=a
print('a:',a)
print('id(a):',id(a))
print('b:',b)
print('id(b):',id(b))
print()

print('using aliasing :')
a=a[:3] # creating new object 
print('a:',a)
print('id(a):',id(a))
print('b:',b)
print('id(b):',id(b))