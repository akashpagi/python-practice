print('copy method(copying_list):')
a=[10,20,30,40]
b=a.copy()
b=a[:] 
print('A:',a)
print('B:',b)
print()

print('modifying "A" :')
a[3]=50
print('A:',a)
print('id :',id(a))
print('B:',b)
print('id :',id(b))
print()

print('modifying "B" :')
b[3]=70
print('A:',a)
print('id :',id(a))
print('B:',b)
print('id :',id(b))
print()

print('colning_list:')
a=[1,2,3,4]
b=a[:] 
print('A:',a)
print('B:',b)
print()

print('modifying "A" :')
a[1]=99
print('A:',a)
print('id :',id(a))
print('B:',b)
print('id :',id(b))
print()

print('modifying "B" :')
b[1]=95
print('A:',a)
print('id :',id(a))
print('B:',b)
print('id :',id(b))