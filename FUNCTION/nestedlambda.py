# nested lambda functioin :
# ex 1 :
add=lambda x=10 : (lambda y :x+y)
a=add()
print(a(20))