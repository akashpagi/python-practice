class Parent:
     def __init__(self):
        self.name='akash'
        print('Parent constructor')
     def view_1(self):
        print('Parent class ')

class Child(Parent):
    def view_2(self):
        print('Child class ')
ob = Child()
print(ob.name)
ob.view_1()
ob.view_2()