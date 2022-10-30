#list comprehension :
print('using for loop :')
lst=[]
for i in range(6):
    lst.append(i+2)
print(lst)

print('list comprehension :')
new_list=[i+2 for i in range(6)]
print(new_list)
print()

