# anonymous function or lambda function :
# calling lambda function using with a variable :
# ex 1 :
a=lambda x : print(x)
a(26)

# ex 2 :
b=lambda x,y : x+y
print(b(2,1))

# ex 3 :
add_sub=lambda x,y : (x+y,x-y)
a , s = add_sub(5,3)
print(a ,s)

# ex 4 : using actual argument :
# defualt argument :
l=lambda x,y=18 : x+y
print(l(2,2))
# vriable length argument :
k=lambda *num: (num[0]+num[1])
print(k(26,3))