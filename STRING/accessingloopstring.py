# accessing for loop string :
print('using with for loop')
str1='akash26'
for i in str1:
    print(i)

# accessing for loop with range & len functions :
print('using loop with range & len function :')
str2='python'
for i in range(len(str2)):
    print(str2[i])  # with index : print(i,'=',str2[i])

# accessing while loop withlen function :
print('using while loop with len function :')
str3='mysql'
print(len(str3))
i=0 
while (i<len(str3)):
    print(str3[i])
    i+=1
