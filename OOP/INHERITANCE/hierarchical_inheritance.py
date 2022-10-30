class Parentclass():
    def fun1(self):
        print('parent class')
class Childclass1(Parentclass):
    def fun2(self):
        print('child class 1')
class Childclass2(Parentclass):
    def fun3(self):
        print('child class 2')

o_1=Childclass1()
o_2=Childclass2()
o_1.fun2() #callling child class 1 
o_2.fun3()  #callling child class 2 
print()

o_1.fun1() #callling parent class 
o_2.fun1()  #callling parent class 

