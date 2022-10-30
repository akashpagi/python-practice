
# slicing on tuple:
t=(1,2,3,4,5,6,7)
n=len(t)
print('original tuple 1 :')
for i in range(n):
    print(i,'=',t[i])
print()

print('s: : =',t[2: :]) #default value is 0(zero)
print()

print('s:s: =',t[1:6:])
print()

print('s:s:s =',t[0:7:2])
print()

# since starting index is greater than length of t, returns empty tuple
print('starting index is greater than length of t,returns empty tuple :')
print('s:s:s =',t[7:9:2]) 
print()

print('original tuple 2:')
t1=tuple('HELLO_JI')
m=len(t1)
for j in range(m):
    print(j,'=',t1[j])

print()

print('last elements using "-ve" index slicing :')
print('s: =',t1[-5: : ])
print()

print("'-ve' index slicing :")
print('s:s: =',t1[-7:-2])
print()


print("'-ve' index slicing :")
print('s:s:s =',t1[-6:-1:2])
print()


print("'-ve'& '+ve' index slicing :")
print('s:s: =',t1[-4:6:])
print()

print("'-ve'& '+ve' index slicing :")
print('s:s:s =',t1[-7:7:3])
print()

