class father:
    def fun1(self):
        print("Parent class::")
    @classmethod
    def fun2(self):
        print("Class method::")
    @staticmethod
    def fun3():
        a=10
        print("Static method")
        print("Value of a= ",a)
class child(father):
    def show(self):
        self.a=10
        self.b=30
        self.c=self.a+self.b
        print("Result=",self.c)
        print("This is child classs")
obj=child()
obj.show()
obj.fun1()
obj.fun2()
obj.fun3()

