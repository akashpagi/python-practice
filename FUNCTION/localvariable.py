# local variable :
def add(y):
    x=10 #<--- local variable 
    print(x) #<-- using local varible inside function
    print(x+y) #<-- using local varible inside function
add(20)
#prnit(x) #<--- using local varible out side function , it will show error