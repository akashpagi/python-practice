print('using for loop:')
dict1 = {}
for n in range(1,6):
    if(n%2==0):
        dict1[n] = n*n
    else:
        dict1[n]='invaild'
print(dict1)

print()

print('dict_comprehension with if else statement:')
new_dict1={n:(n*n if(n%2==0) else'invaild') for n in range(1,6)}
print(new_dict1)
print()


print('convert list to dictionary:')
lst=[(1,'akash'),(2,'python')] 
d={k:v for (k,v) in lst}
print(d)