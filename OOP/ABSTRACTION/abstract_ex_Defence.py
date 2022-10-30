from abc import ABC ,abstractmethod

class DefenceForce(ABC):
    def __init__(self):
        self.cadate_id=101
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print('Gun ="AK47"' ,self.cadate_id)

class Army(DefenceForce):
    def area(self):
        print('ArmyArea = Land')
class AirForce(DefenceForce):
    def area(self):
        print('AirforceArea = Sky')
        
class Navy(DefenceForce):
    def area(self):
        print('NavyArea = Sea')

a=Army()
af=AirForce()
n=Navy()

a.gun()
a.area()
print()
af.gun()
af.area()
print()
n.gun()
n.area()