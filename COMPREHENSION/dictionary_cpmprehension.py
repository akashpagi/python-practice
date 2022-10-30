print('using for loop:')
square_dict={}
for num in range(1,6):
    square_dict[num]=num*num
print(square_dict)
print()

print('dictionary comprehension:')
new_dict={num:num*num for num in range(1,6)}
print(new_dict)
print()

print('dictionary comprehension with if statement:')
new_dict_1={num:num*num for num in range(1,6) if(num%2==0)}
print(new_dict_1)
print()

print('dictionary comprehension with double if statement:')
new_dict_2={num:num*num for num in range(1,6) if(num%2==0) if(num%3==1)}
print(new_dict_2)
print()