# getting array input from user using for loop:

import array as a
s_roll=a.array('i' ,[])
n=int(input('How many number?:'))


for i in range(n):
    s_roll.append(int(input('Enter number :')))

#for i in range(len(s_roll)): 
  #  print(s_roll[i])
print(s_roll) 

y=int(input('enter the search number for index :'))
x=0
for i in s_roll:
    if i==y:
        print(x)
        break
    x+=1