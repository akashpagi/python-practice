# slicing on list:
l=[ [1,2,3],
    [4,5,6],
    [7,8,9],
    [0,0,0]]
n=len(l)
print('original list :')
for i in range(n):
    print(l[i],'=',i)
print()

print('****************************************')
print()

print('s: : =',l[1: :]) #default value is 0(zero)
print()

print('s:s: =',l[1:3:])
print()

print('s:s:s=',l[0:5:2])
print()

print('last 2 lists using "-ve" index slicing :')
print('s: =',l[-2: : ])
print()

print("'-ve' index slicing :")
print('s:s: =',l[-5:-3])
print()

print('**************************************')
print()

print('nested list slicing :')
a=l[1:3]
print(a)
b=l[1:3][1]
print(b)
print('extract only one specific element :',l[1:3][0][1])
print('using for loop:')
for e_1 in b:
    print(e_1)
print()
print('****************************************')
print()

print('nested last 3 lists slicing :')
a=l[-3:]
print(a)
b=l[-3:][0]
print(b)
print('extract only one specific element :',l[-3:][0][2])
print('using for loop:')
for e_2 in b:
    print(e_2)
print()
