# ex.1 :
def disp():
    def show():
        return 'show function'
    print('disp function')
    return show
re_show= disp()
print(re_show())
print()

# ex.2 : wiyh parameter 
def disp1(show1):
        print('disp1 function')
        return show1
def show1():
        return 'show1 function'
re_show1= disp1(show1)
print(re_show1())