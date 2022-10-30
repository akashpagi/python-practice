# return statement :
# ex.1 :
def add(y):
    x=10
    c=x+y
    return c # you can use also (c)
sum=add(20)
print(sum)
print()

# ex.2 :
def add1(y):
    x=20
    return (x+y)
sum=add1(20)
print(sum)
print()

# ex.3 :
def add_sub(y):
    x=10
    c=x+y
    d=y-x
    return (c,d)
sum,sub=add_sub(20)
print(sum,sub)