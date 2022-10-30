print('using for loop :')
a=(10,-20,34.45,'python')

for i in a:
    print(i)

print()

print('for loop using range function & with index :')
n=len(a)
for j in range(n):
    print(j,'=',a[j])
