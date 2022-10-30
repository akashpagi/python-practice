# globals()function : using with dictionary
A=10
def globals_fun():
    A=20
    print('local var :',A)
    a=globals()['A']
    print('globals :',a)
    a=40
    print('globals :',a)
    
globals_fun()
print('global var :',A)

