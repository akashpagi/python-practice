from abc import ABC,abstractmethod  #abc is module 
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
class Child(Father):
    def disp(self):
        print('Child class')
        print('Defining Abstract Method')

Ob=Child()
Ob.disp()
 