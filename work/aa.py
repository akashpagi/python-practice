'''import array 
stu_roll=array.array('i',[101,102,103,104,105])
#for element in stu_roll:
print(stu_roll[1])

#from array import* 
#stu_roll=array('i',[1,2,3,4,5])
#print(stu_roll[2])

import array
stu_roll=array.array('i',[1,2,3,4,5])
#for x in stu_roll:
    #print(x)
n=len(stu_roll)
for i in range(n):
    print(i, '=' , stu_roll[i])'''


import array
stu_roll=array.array('i',[1,2,3,4,5])

n=len(stu_roll)
i=0
while (i<n):
    print(stu_roll[i])
    i+=1
