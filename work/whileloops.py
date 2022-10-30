'''# while loops 
a=1
while(a<=10):
    print(a)
    a+=1 # assignment operators is evaluate a=a+


# while loops else
a=1
while(a<=5):
    print(a)
    a+=1
else:
    print('while conditoin FALSE so else part excuted')'''


#  nested while loops 
i = 1
j = 1
while i <= 3:
    while j <=5 :
        print('outer loop :',i, ",", 'inner loop :',j)
        j = j + 1
        i = i + 1