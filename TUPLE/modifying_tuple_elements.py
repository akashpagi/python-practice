#a=(1,2,3)
#b=(10,20,30,)
#t=a+b
#a[1]=6
#print(a)

a=(1,-20,35.8,'python')
b=(10,20,30)
t_1=a+b
print('a:',a)
print('t:',t_1)
print('id(a):',id(a))
print('id(t_1):',id(t_1))
print()

print('modify using slicing:')
a1=(1,2,3,4,5)
c=('java','ios')
s1=a1[0:2]
s2=a1[3:]
t2=s1 + c + s2
print(t2)



