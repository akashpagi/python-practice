# ex.1
import array as a
print('before slicing')
num = a.array('i',[1,2,3,4,5,6,7])
n =len(num)
for i in range(n):
    print(i,'=',num[i])
print('after slicing')
a = num[0: ]  
for i in a:
    print(i) 


'''# ex.2
import array as a
num = a.array('i',[1,2,3,4,5])
for i in num[-4:4]:
    print(i)'''