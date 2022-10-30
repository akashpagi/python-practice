class Parent:
    def fun1(self):
        print('this is function 1')
class Child1(Parent):
    def fun2(self):
        print('this is function 2')
class Child2(Parent):
    def fun3(self):
        print('this is function 3')
class Grandchild(Child1,Child2):
    
    def fun4(self):
        print('this is function 4')

o=Grandchild()
o.fun1()
o.fun2()
o.fun3()
o.fun4()