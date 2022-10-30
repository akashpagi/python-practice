# global keyword :
i= 2
def myfun():
    global i    
    i= i+1
    print('local var :',i)
myfun()
print('global var : ',i)
print()

# ex.2 :
i=0
def myfun1():
    global i
    while(i<3):
        i=i+1
        print(i)
myfun1()