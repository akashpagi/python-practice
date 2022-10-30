print('map()_function :')
a=[1,2,3,4,5]
def inc(n):
    return n+2
result=map(inc,a)
print('increment list :',list(result))

print()
print('**********************************')
print()

print('using lambda function :')
num=[10,20,30,40]
result_1=list(map(lambda n:(n*2),num))
print(result_1)
print('using while loop :')
m=len(result_1)
i=0
while(i<m):
    print(result_1[i])
    i+=1
print()
print('**********************************')
print()

print('add two lists using map & lambda function :')
lst_1=[10,20,30,40]
lst_2=[2,4,6,8]
result_2=list(map(lambda n,m: (n+m),lst_1,lst_2))
print(result_2)