import numpy as n 
a=n.array([[10,20,30,40],[50,60,70,80]])
n=len(a)
i=0                            #outer loop
while(i<n):                    #outer loop
    j=0                        #inner loop
    while(j<len(a[i])):        #inner loop
        print(a[i][j])         #inner loop
        j+=1                   #inner loop
    i+=1                       #outer loop
    print()                    #outer loop