import math as m 
print('numbers and numeric representation :')
#ceil(x):it is smallest integer ,greater or equal to the number of x
print(m.ceil(25.39))
print()
#floor(x):it is laragest integer ,less or equal to the number of x
print(m.floor(26.50))
print()
#fabs(x):returns absolute value of x or positive quantity of x
print(m.fabs(-90))
print()
#factorial(x):
print(m.factorial(5))
print()
#fsaum(iterable):find the sum of element in an iterable
my_list=[1,2,30,4,5,-4,5.6]
print(m.fsum(my_list))
print()
#gcd(x,y): returns greatest common divisor x and y
print(m.gcd(60,24))
print()
#copysign(x,y):it returns the number x and copy the sign of y to x.
x=10;y=-15
print(m.copysign(x,y))
print()
#isfinte(x):
#isinf(x):
#isnan(x):
#remender(x,y):
x=11;y=2
print(m.remainder(x,y))
print()

import math as m 
print('trigonometric & angular conversion functions :')
#sin(x):return the sine of x in radians
print('degree :',m.sin(m.radians(60)),'  radian :',m.sin(60) )
print()

#cos(x):return the coine of x in radians
print('degree :',m.cos(m.radians(60)),'  radian :',m.cos(60) )
print()

#tan(x):return the tan of x in radians
print('degree :',m.tan(m.radians(45)),'  radian :',m.tan(45) )
print()

#asin(x):this is the inversine operation of the sine,there are acos,atan also.
print('asin (with degree):',m.degrees(m.asin(0.86602)))
print('acos (with degree):',m.degrees(m.acos(0.5000)))
print('atan (with degree):',m.degrees(m.atan( 0.9999)))
print()

 #degrees(rad):radian to degree
print("pi / 180 Radians is equal to Degrees : ", end ="") 
print (m.degrees(m.pi/180)) 
  
print("180 Radians is equal to Degrees : ", end ="") 
print (m.degrees(180)) 
  
print("1 Radians is equal to Degrees : ", end ="") 
print (m.degrees(1)) 
print()

#radians(deg):radian to degree
print("pi / 180 Radians is equal to Degrees : ", end ="") 
print (m.radians(m.pi / 180)) 
  
print("180 Radians is equal to Degrees : ", end ="") 
print (m.radians(180)) 

print("1 Radians is equal to Degrees : ", end ="") 
print((m.radians(1)))
print()

# power and logaritmic functions :
#pow(a,b):a to the power b value 
print(m.pow(2,2))
print()
#sqrt(a):square root of a (given value default in float)
print(m.sqrt(25))
print()
#exp(a):return the value of e raised to the power a (e**a).where natural log e=2.718281
print(m.exp(4)) #means(e**4)
print()
#log(a,base): log a with base,if base is not mentioned then base value is natural log e=2.718281
print(m.log(2,3))
print()
# log2(a):return value of a where base is 2
print(m.log2(16))
print()
#log10(a):return value of a where base is 10
print(m.log10(1000))