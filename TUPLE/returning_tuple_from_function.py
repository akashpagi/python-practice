def old_disp(t):
    print('old_disp :',t)
    print(type(t))
    return t
t=(1,2,-4,'python')
new_disp = old_disp(t)
print('new_disp :',new_disp)
print(type(new_disp))