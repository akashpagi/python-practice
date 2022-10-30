#a=(1,2,3,4,5)
#del a
#print(a)
a=(1,2,3,4,5)
print('a:',a)
t=a[0:3]
print('t:',t)
print('id(a):',id(a))
print('id(t):',id(t))
print()


print('delete spefific element:')
s1=a[0:2]
s2=a[3:]
t1=s1+s2
print('t1:',t1)