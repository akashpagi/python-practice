# adding single and multiple set :
print('adding one element :')
a={1,2,'python'}
print('before a :',a)
a.add('java')
print('after adding one element :',a)

print()

print('adding multiple elements :')
s=set()
x=(1,2,3,4)
s.update(x)
print(s)

print()

b={34,'java',5}
print('before updating :',b)
b.update((1,26,44))
print('after updating :',b)