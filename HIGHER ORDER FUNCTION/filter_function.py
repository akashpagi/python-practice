# higher order function :
print('filter()_function :')
a=[30,87,25,50,35,32,60]
def high_marks(n):
    if(n>=35):
        return True 


print('using list function :')
result=list(filter(high_marks,a))
print('list:',result)
print('using for loop :')
for i in result:
    print(i)
print()


print('********************************************')


print()
b=[30,87,25,50,35,32,60]
print('using list & lambda function :')
result_1=list(filter(lambda n:(n<=34),b))

print('list:',result_1)
print(type(result_1))
print('using while loop :')
m=len(result_1)
i=0
while (i<m):
    print(result_1[i])
    i+=1



