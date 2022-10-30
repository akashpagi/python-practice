# immediatly invoked function expression (IIFE) :

# ex 1 :
sum=lambda x : x+1
print(sum(5))
# new 
(lambda x : print(x+1))(5)
print()

# ex 2 :
add=lambda x,y : x+y
print(add(5,2))
#new
(lambda x,y : print(x+y))(5,2)
