'''a=5;b=2.2
value=a+b
print(value)
print(type(value))

a='akash';b='pagi'
s= a + b
print(s)
print(type(s))

a=20;b='10'
q= a + b
print(q)
print(type(q))'''

# explicit type conversion :

a=5;b=2
value=a/b
print('original value = ',value)
print(type(value))
int_value=int(value)
print('conversion value = ',int_value)
print(type(int_value))  

q=20;u='akash'
print(type(u))
value=q+len(u)
print(value)

# int to complex :
n='10' 
s=list(n)
print(s)
print(type(s))

# list to tuple , :
n=['a', 'k', 'a', 's', 'h']
s=tuple(n)
print(s)
print(type(s))


# bin to int
a=int('0b1010',2)
print(a)
print(type(a))


# oct to int
a=int('0o100',8)
print(a)
print(type(a))

# hex to int 
a=int(0x8e)
print(a)
print(type(a))

# int to oct 
a=oct(64)
print(a)
print(type(a))

# int to hex
a=hex(142)
print(a)
print(type(a))

