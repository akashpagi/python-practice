# syntax :  str.format(value or argument)
str='my age is {}'
print(str.format(18)) # or print('my age is {}'.format(18))

print('*********** intger *************') # or print('float') 
# do not write space between {} 
print('{}'.format(10))
print('{} {}'.format(10,20))
print('{0}'.format(10))
print('{0} {1}'.format(10,20))
print('{num1}'.format(num1=10))
print('{num1} {num2}'.format(num1=10,num2=20))
print('{num2} {num1}'.format(num1=10,num2=20))
print()

print('*********** integer and string *************')
print('hello my name is {}'.format('akash !!!'))
print('{} {}'.format('akash',26))
print('{0} {1}'.format('akash',26))
print('{1} {0}'.format('akash',26))
print('{n1} {s2}'.format(n1=26,s2='akash'))
print('{s2} {n1}'.format(n1=26,s2='akash'))
print()

#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101)) #0b101
print('{num1:d}'.format(num1=26))
print()

# [width]
print('{num:5d}'.format(num=5))
print()

# [0] means padding
print('{num:05d}'.format(num=2))
print()
 
# [sign] means +,-, space 
#Use "+" to always indicate if the number is positive or negative:
txt = "The numbers is between {:+} & {:+}."
print(txt.format(-4, 2))
print()

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temp is between {:-} & {:-} degrees celsius."
print(txt.format(-3, 7))
print()

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The space is between {: }{: } numbers."
print(txt.format(-3,-7))
print()

#[align] :<,^,>,=
#Use "<" to left-align the value:
print('left align {:*<5} '.format(26))
print()

#Use "^" to center-align the value:
print('center {:*^7} align'.format(26))
print()

#Use ">" to right-align the value:
print('right align {:>5} '.format(26))
print()

#Use ">" to equal-align the value:
print('equal {:=5} align'.format(-26))
print()

print('********* float **********') 
# do not write space between {} 
# f : floating point decimal format (default 6)
print('{}'.format(15.65))
print('{:f}'.format(15.65))     
print('{f1:f}'.format(f1=15.65))
print()
# float with [fill][align][sign][#][0][,][.presicion]type 
print('{f1:8f}'.format(f1=15.65))
print('{f1:8.3f}'.format(f1=15.65))
print('{f1:+8.2f}'.format(f1=15.65))  #  [sign][.presicion]type
print('{f1:*<8.2f}'.format(f1=15.65)) # [fill][left align][.presicion]type
print('{f1:*>8.2f}'.format(f1=15.65)) # [fill][right align][.presicion]type
print('{f1:^8.2f}'.format(f1=15.65)) # [center align][.presicion]type
print('{f1:*^8.2f}'.format(f1=15.65)) # [fill][center align][.presicion]type
print()

print('******** string *********')
# s : string (convert any python object as str()) # no [sign]
print('{:8s}'.format('akash'))
print('{:<8s}'.format('akash')) 
print('{:^8s}'.format('akash')) # [center align]
print('{:>8s}'.format('akash')) # [right align]
print('{:*^8s}'.format('akash')) # [center align]
print('{:.3s}'.format('akash')) # [.presicon]type
print('{:*^8.2s}'.format('akash')) 
print()

print('******* [,] *******')
print('my salary is {:,} .'.format(1234567890))
print()

print('******* [_] *******')
print('The universe is {:_} years old.'.format(13800000000))
print()

print('******* examples *******')
name='akash'
age=18
print('my name is {} and age {}.'.format(name,age))
print()

a=50
b=3
print('in percentage {:.2%}'.format(a/b))





 