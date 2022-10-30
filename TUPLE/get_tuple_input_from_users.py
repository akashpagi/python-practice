a=[]
n=int(input("enter number of elements :"))

for i in range(n):
    a.append(input('enter elements :'))
    
print()

print(type(a))
print('list:',a)

print()

a=tuple(a) # a convert  into tuple

print(type(a))
print('tuple:',a)





