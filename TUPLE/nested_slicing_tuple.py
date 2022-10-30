#  nested slicing on tuple:
t=( (1,2,3),
    (4,5,6),
    (7,8,9),
    (0,0,0))
n=len(t)
print('original tuple :')
for i in range(n):
    print(t[i],'=',i)
print()

print('****************************************')
print()

print('s: : =',t[1: :]) #default value is 0(zero)
print()

print('s:s: =',t[1:3:])
print()

print('s:s:s=',t[0:4:2])
print()

print('last 2 tuples using "-ve" index nested slicing :')
print('s: =',t[-2: : ])
print()

print("'-ve' index nested slicing :")
print('s:s: =',t[-4:-3])
print()

print('**************************************')
print()

print('nested tuple slicing :')
a=t[1:3]
print(a)
b=t[1:3][1]
print(b)
print('extract only one specific element :',t[1:3][0][1])
print('using for loop:')
for t_1 in b:
    print(t_1)
print()
print('****************************************')
print()

print('nested last 3 tuples slicing :')
a=t[-3:]
print(a)
b=t[-3:][0]
print(b)
print('extract only one specific element :',t[-3:][0][2])
print('using for loop:')
for t_2 in b:
    print(t_2)
print()
