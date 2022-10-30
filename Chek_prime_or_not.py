e_n=4
f_n=0
start=1
while start<=e_n:
    if e_n%start==0:
        f_n+=1  #factor_n=factor_n+1
    start+=1
if f_n==2:
    print(e_n,"is a prime number.")
else:            
    print(e_n,"is not a prime number.")

 

