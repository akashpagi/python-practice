#ex1 :private methods : we can access only within means own class
 
class Myclass():
    def __disp1(self):
        print('private methods')

    def disp2(self):
        print('this is disp2 calling disp1')
        self.__disp1()

o=Myclass()
o.disp2()
o.__disp2() #AttributeError: 'Myclass' object has no attribute '__disp2'