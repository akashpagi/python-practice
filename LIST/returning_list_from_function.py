def lst(a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    return a
a=[10,20,30,'python']
new_a=lst(a)
print('new_a :',new_a)
print(type(new_a))
