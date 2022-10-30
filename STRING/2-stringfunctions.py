print('replase() function :')
add='H.No.51,Shanti Niwas'
old='51'
new='02'
newadd=add.replace(old,new)
print(add)
print(newadd)
print()

print('split() function :')
name='akash*sadanand*pagi'
str1=name.split('*',1)
print(name)
print(str1)
print()

print('join() function :')
name=('hello','how','are','you')
str1='_'.join(name)
print(name)
print(str1)
print()

print('startwith() function :')
str1='hello, welcome to my world.'
str2=str1.startswith('wel',7,20)
print(str1)
print(str2)
print()

print('endwith() function :')
str1='hello, welcome.'
str2=str1.endswith('welcome.')
str3= str1.endswith("me.",6,14)
print(str1)
print(str2)
print(str3)


