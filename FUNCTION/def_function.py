# ex.1: with add() function 
def add():
    x=10
    y=20
    c=x+y
    print(c)
add()
print()

# ex.2 :with argument and format
def add2(y): # parametrs in ()
    x=10
    c=x+y
    print(c)
    print(f'formatted output:{c:5.1f}')
add2(34) # argument in (int,float,string,etc....)
add2(20.55) # float value
print()

# write once and use it as many time as you need :
def disp():
    city='Mumbai !!'
    print('Welcome to',city)
disp() 
disp()
print()

# divide larger task into many small task,helpful for debugging code :
def add3():
    x=10
    y=20
    c=x+y
    z=y-x
    print('add:',c)
    print('sub:',z) # subtraction inside the addition
add3()
print()

# subtraction
def sub():
    x=10
    y=20
    c=y-x
    print('subtraction :',c)
sub()
print()

# string
def my_function():
  print("Hello from a function")
my_function()