a=(1,2,[4,5])
print('original list a :',a)
print('id(a) :',id(a))
print('type :',type(a))
print()

print('acessing tuple of lists using for loop :')
n=len(a)
for i in range(n):
    if type(a[i]) is list :
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,'=',a[i][j])
    else:
        print(i,'=',a[i])
print()

print('modifying list inside the tuple :')
a[2][1]=50
print('modifying a :',a)
print()

t=([10,20],[30,40])
print('original list t :',t)
print('id(t) :',id(t))
print()

print('acessing tuple of lists using for loop :')
m=len(t)
for i in range(m):
    for j in range(len(t[i])):
        print(i,j,'=',t[i][j])
print()

print('modifying list inside the tuple :')
t[0][0]=8
print('modifying a :',t)
print()