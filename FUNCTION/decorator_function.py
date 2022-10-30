'''
def decorator_fun(any_function):
    def wrapper_fun():
        print('this is extra decorator function')
        any_function()
    return wrapper_fun
    
# @ symbol use for as a shortcut key :
@decorator_fun #shortcut
def fun1():
    print('this is function 1')
fun1()

print()

@decorator_fun #shortcut
def fun2():
    print('this is function 2')
fun2()

#print()
#var=decorator_fun(fun1)
#var()
print() 


# ex 2 :
def decor_fun(num):
    def inner():
        a=num()
        add=a+20
        return add
    return inner
@decor_fun    
def num():
    return 10 
#=decor_fun(num)
print(num()) # () calling inner fuinction '''
 
 # multi decorators function :
def decor1(num):
     def inner():
         b=num()
         multi=b*5
         return multi
     return inner
def decor(num):
     def inner():
         a=num()
         add=a+5
         return add 
     return inner
@decor
@decor1
def num():
     return 10
#num=decor(decor1(num))
print(num())

