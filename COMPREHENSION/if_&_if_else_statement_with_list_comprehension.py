# list comprehension with if statement :
print()
print('using for loop with if statement(condition):')
lst=[]
for i in range(11,21):
    if (i%2==0):
        lst.append(i)
print(lst)

print('list comprehension with condition:')
lst_1=[i for i in range(11,21) if (i%2==0)]
print(lst_1)
print()


# list comprehension with if statement :
print('using for loop with double if statement(condition):')
e_lst=[]
for x in range(16):
    if (x%2==0):
        if (x%3==0):
            e_lst.append(x)
print(e_lst)

print('list comprehension with double condition:')
if_lst=[x for x in range(16) if(x%2==0) if(x%3==0)]
print(if_lst)
print()

print('using for loop with if else statement:')
if_else_lst1=[]
for i in range(7):
    if (i%2==0):
        if_else_lst1.append(i)
    else:
        if_else_lst1.append('invaild')
print(if_else_lst1)

print('list comprehension with if else statement :')
#new_list=[expression if_statement else expression for item in iterable_object]
if_else_lst=[i if (i%2==0) else 'invaild' for i in range(7)]
print(if_else_lst)


