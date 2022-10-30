print('positional argument :')
# ex 1 :
def pw(x,y):
    c=x**y
    print(c)
pw(5,2)
# ex 2 :
def pw1(x,y):
    c=x**y
    print(c)
pw1(2,5)
# ex 1 : 
# the number of arguments and their positions in the function defination 
# should be equal to the numder and position of the argument in the function call .
def pw2(x,y):
    c=x**y
    print(c)
#pw2(5,2,3)
pw2(3,4)
print()

print('keyword argument:')
# ex.1 :
def ka(name,age):
    print(name,age)
ka(name='akash',age=18)
# ex2 : keyword argument using with f-string :
def ka1(name,age):
    print(f'my name is {name} and age {age}.')
ka1(age=18,name='akash')
# ex.3 :
def ka2(name,age):
    print(name,age)
#ka2(name='akash',age=18,roll=101)
ka2(age=18,name='akash')
print()

print('default argument :')
# ex.1: defualt age is 20
def da(name,age=20):
    print(name,age)
da(name='python')
# ex.2: defualt age is 20 using with f-string :
def da1(name,age=20):
    print(f'my name is {name} and age {age} .')
da1(name='python',age=18)
print()

print('variable length argument:')
# ex 1 :
def vla(*num):
    z=num[0]+num[1]+num[2]
    print('addition :',z)
vla(5,2,4)
# ex 2 :
def vla1(x,*num):
    z=num[0]+num[1]
    print(x,'addition :',z)
vla1(5,2,4)
print()

print('keyword variable length argument:')
# ex 1 :
def kvla(**num):
    z=num['a']+num['b']+num['c']
    print('addition :',z)
kvla(a=5,b=3,c=2)
# ex 2 :
def kvla1(x,**num):
    z=num['a']+num['b']
    print(x,'addition :',z)
kvla1(2,a=5,b=3)