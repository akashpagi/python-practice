import array as a
s_roll=a.array('i' ,[])
n=int(input('enter number of element?:'))


i=0
while (i<n):
    x=int(input('enter number :'))
    s_roll.append(x)
    i+=1 

j=0
while (j<len(s_roll)):
    print(s_roll[j])
    j+=1

