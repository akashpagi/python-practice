a=(1,2,3,(50,60))
n=len(a)
print('using for loop :')
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,'=',a[i][j])
    else:
        print(i,'=',a[i])
print()

t=((10,20,30),(40,50,60))
print(t[0])
print(t[1])
for r in t:
    for c in r :
        print(c,end=' ')
    print()

print()
t1=((10,20,30),(40,50,60))
print('with index:')
n=len(t1)
for i in range(n):
    for j in range(len(t1[i])):
        print(i,j,'=',t1[i][j])

              