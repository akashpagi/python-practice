class Parent:
    money=1000

    def fun1(self):
        print('this is function 1')

    @classmethod
    def show_money(cls):
        print('@classmethod ''money:',cls.money)

    @staticmethod
    def static():
        a=10
        print('@staticmethod ''a:',a)
        

class child(Parent):
    def fun2(self):
        print('this is function 2')
obj=child()
obj.fun1()
obj.show_money()
obj.static()
obj.fun2()