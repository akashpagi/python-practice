# pass/call object reference :
# Ex.1 :
print()
print('******* INTEGER *******')
def val(x):
    print(x,id(x)) # same memory of x
    x=15 
    print(x,id(x))
x=10
val(x)
print(x,id(x)) # same memory of x
print()

# # Ex.2 :
print('******* LIST *******')
def val1(lst):
    #print('IFBA :',x,id(x)) #IFBA:Inside Function before append
    lst.append(4)
    print('IFAA :',lst,id(lst))  #IFAA:Inside Function After append
lst=[1,2,3]
print('BCF  :',lst,id(lst))  # BCF:Before Calling Function
val1(lst)
print('ACF  :',lst,id(lst))   # ACF:After Calling Function
print()


print('Ex.3 :')
print('******* integer *******')
def val2(a):
    a=15 
    print(a,id(a))
x=10
val2(x)
print(x,id(x))
print()

print('Ex.4 :')
print('******* list *******')
def val3(l):
    l.append(4)
    print(l,id(l))  #Inside Function After append
lst=[1,2,3]
print(lst,id(lst))  # Before Calling Function
val3(lst)
print(lst,id(lst))   # After Calling Function
print()

# Ex .5 : when we create a new object inside function then it will not be available outside function
print('different lst value')
def val4(lst):
    print(lst,id(lst))
    lst=[11,22,33]
    print(lst,id(lst))
lst=[1,2,3]
print(lst,id(lst))
val4(lst)
print(lst,id(lst))

