from abc import ABC ,abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print('Child class disp 1 abstract method')

class GrandChild(Child):
    def disp2(self):
        print('GrandChild class disp 2 abstract method')

gc=GrandChild()
gc.disp1()
gc.disp2()
  