from abc import ABC,abstractmethod  #abc is module 
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):              
        print('Concrete Method')

class Child(Father):
    def disp(self):
        print('Defining Abstract Method')

Ob=Child()
Ob.disp()
Ob.show()