# nested_list for loop :
# for loop using  : len(),for loop ,type(),if else statement,
a=[1,2,3,[50,60]]
n=len(a)
for i in range(n):
    if type(a[i]) is list:
        if (len(a[i])>1): #a[3]>1 =3-1=2 get 2>1
            m=len(a[i]) # 2
            for j in range(m): # range(0,1)
                print(i,j,'=',a[i][j])
    else:
        print(i,'=',a[i])
print()

# nested list without index :
print('without index :')
a1=[[10,20,30],[40,50,60]]
for r in a1 :
    for c in r :
        print(c)
    print()
print() 


print('with index :')
a=[[10,20,30],[40,50,60]]
n=len(a) # length of a n=2
for i in range(n) : # 2=(0,1)
    for j in range(len(a[i])) : #a[0]=1(length is 3(0,1,2)),a[1]=2 (length is 3(0,1,2))
        print(i,j,'=',a[i][j])
    print()