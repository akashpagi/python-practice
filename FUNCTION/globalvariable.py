# global variable :
# ex.1:
a=50 
def show():
    x=10
    print('global variable :',a)  #<-- using global varible inside function
    print('local varible :',x)  #<-- using local varible inside function
show()
print('a :',a) 
#print('x :',x) #<--- using local varible out side function , it will show error
print()

# ex.2:
i= 3
def myfun():
    a= i+1
    print('myfun :',a)
myfun()
print('global variable :',i)
print()

# ex.3:
i= 0
def myfun1():
   i=0      # same global variable value treated in local variable
    i= i+1
    print('myfun1 :',i)
myfun1()
print('global variable : ',i)