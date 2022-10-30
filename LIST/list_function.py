# creating empty list using list function :
print('creating empty list :')
a=list()
print(a)
print(type(a))
print()

# creating element list using list function :
print('creating element list :')
a=list('python')
print(a)
print(type(a))
print()

#creating range list using list function :
print('create range list :')
a=list(range(0,8,2))
print(a)
a[0]=34
a[2]=26
print('modifying a :',a)
print(type(a))
