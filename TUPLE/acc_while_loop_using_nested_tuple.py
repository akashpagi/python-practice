a=(1,2,3,(50,60))
n=len(a)
i=0
while(i<n):
    if type(a[i]) is tuple:
        if (len(a[i])>1):
            j=0
            m=len(a[i])
            while (j<m):
                print(i,j,'=',a[i][j])
                j+=1
            i+=1 
    else:
        print(i,'=',a[i])
        i+=1 

print()

t=((1,2,3),(4,5,6))
n=len(t)
i=0
while (i<n):
    j=0
    while (j<(len(t[i]))):
        print(i,j,'=',t[i][j])
        j+=1
    i+=1