a=[1,2,(4,5)]
print('original list a :',a)
print('id(a) :',id(a))
print('type :',type(a))
print()

print('acessing list of tuple using for loop :')
n=len(a)
for i in range(n):
    if type(a[i]) is tuple :
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,'=',a[i][j])
    else:
        print(i,'=',a[i])
print()

a.append((6,7))
print('after appending list a :',a)
print('id(a) :',id(a))
print('type :',type(a))

print()
l=[(10,20),(30,40)]
print('original list l :',l)
print('id(l) :',id(l))
print()

print('acessing list of tuple using for loop :')
m=len(l)
for i in range(m):
    for j in range(len(l[i])):
        print(i,j,'=',l[i][j])
    