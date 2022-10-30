def floop():
    print('for loop without index')
    l_1 = [10,-50,13.34,'python'] # you can use all datatype in list or one datatype also
    for element in l_1:
        print(element)
floop()
print()

def floop1():
    print('for loop with index')
    l_2 = [10,-50,13.34,'python']
    n=len(l_2)
    for i in range(n):
        print(i,'=',l_2[i])
floop1()