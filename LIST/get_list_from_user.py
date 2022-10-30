a=[]
n=int(input('enter number of elements :'))
for i in range(n):
    a.append(int(input('enter elements :')))
print('new_list :',a) 
print()
print('new_list using for loop :')
for elements in a:
    print(elements)
