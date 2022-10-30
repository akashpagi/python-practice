# ex1 :
def disp(show):
    print('disp function'  + show())
def show():
    return ' show function'
disp(show)
print()

# ex2 :
def disp1(show1):
    return 'disp function'  + show1()
def show1():
    return ' show function'
result = disp1(show1)
print(result)