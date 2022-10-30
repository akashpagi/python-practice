# ex.1 :
def disp():
    def inside():
        print('inside function')
    print('disp function')
    inside()
disp()
print()

#
def disp2():
    def inside2():
        return 'inside function '
    result = inside2() + ' disp function '
    return result
disp2() # error


# nested function use with return statement & parameter :
def disp1(name):
    def inside1():
        return 'inside function'
    result = inside1() + name + 'disp function'
    return result
a=disp1('python')
print(a)