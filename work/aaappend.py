import array
print('without append method')
stu_roll=array.array('i',[1,2,3,4,5])
n=len(stu_roll)
i=0
while (i<n):
    print(stu_roll[i])
    i+=1
print('using append method ')
stu_roll.append(6)
stu_roll.append(7)
n=len(stu_roll)
i=0
while (i<n):
    print(stu_roll[i])
    i+=1
