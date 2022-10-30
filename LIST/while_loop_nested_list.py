#nested +list_while loop :
print('ex.1 :')
lst=[1,2,3,[50,60]]
n=len(lst)
i=0
while (i<n): 
    if type(lst[i]) is list:
        if(len(lst[i])>1): #a[3]>1 =3-1=2 get 2>1
            j=0
            m=len(lst[i]) # 2
            while j<m: #m=2=(0,1)
                print(i,j,'=',lst[i][j])
                j+=1
            i+=1
    else:
        print(i,'=',lst[i])
        i+=1
print()

#ex.2 :
print('ex.2 :')
a=[[10,20,30],[40,50,60]]
n=len(a)
i=0
while (i<n):
    j=0
    m=len(a[i])
    while (j<m):
        print(i,j,'=',a[i][j])
        j+=1
    i+=1