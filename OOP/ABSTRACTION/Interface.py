from abc import ABC,abstractmethod  #abc is module 
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass      
    # without concrete method in @abstractmethod called interface

class Child(Father):
    def disp(self):
        print('child class defining abstract method')

c=Child()
c.disp()