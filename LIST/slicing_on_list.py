# slicing on list:
lst=[1,2,3,4,5,6,7]
n=len(lst)
print('original list :')
for i in range(n):
    print(i,'=',lst[i])
print()

print('start: =',lst[2: :]) #default value is 0(zero)
print()

print('start:stop: =',lst[1:6:])
print()

print('start:stop:stepsize =',lst[0:7:2])
print()

# since starting index is greater than length of lst, returns empty list
print('starting index is greater than length of lst,returns empty list :')
print('start:stop:stepsize =',lst[7:9:]) 
print()

print('last elements using "-ve" index slicing :')
print('start: =',lst[-5: : ])
print()

print("'-ve' index slicing :")
print('start:stop: =',lst[-7:-2])
print()


print("'-ve' index slicing :")
print('start:stop:stepsize =',lst[-6:-1:2])
print()


print("'-ve'& '+ve' index slicing :")
print('start:stop: =',lst[-4:6:])
print()

print("'-ve'& '+ve' index slicing :")
print('start:stop:stepsize =',lst[-7:7:3])
print()

