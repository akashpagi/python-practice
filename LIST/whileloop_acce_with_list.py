def wloop():
    print('while loop with index')
    list_1=['mumbai','pune','delhi','jaipur']
    n=len(list_1)
    i=0
    while(i<n):
        print(i,'=',list_1[i])
        i=i+1 # or i+=1
wloop()