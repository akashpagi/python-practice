# set comprehension :
#print()
#print('using for loop:')
set_1=set()
for x in range(4):
    set_1.add(x+2)
    pass
#print(set_1)

print()
print('set comprehension :')
new_set={(x+2) for x in range(4)}
print(new_set) 


#print('using for loop with if statement:')
set_2=set()
for i in range(11):
    if (i%2==0):
        set_2.add(i)
        pass
#print(set_2)

print()
print('set comprehension with if statement:')
new_set_1={i for i in range(11) if (i%2==0)}
print(new_set_1)