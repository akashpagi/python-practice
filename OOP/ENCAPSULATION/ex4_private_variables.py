# ex4 : private variables can modified only inside the class.
# we can't modified outside the class
class Superbike:
    __MaxSpeed=0
    __Name=''
    def __init__(self):
        self.__MaxSpeed=300
        self.__Name='Hayabusa'
    def Drive(self):
        print('Driving at')
        print('MaxSpeed:',self.__MaxSpeed)
    #def setSpeed(self,Speed):
       #self.__MaxSpeed=Speed
        #print('setSpeed:',self.__MaxSpeed)
s=Superbike()
s.Drive()
#s.setSpeed(100)
s.__MaxSpeed=150
s.Drive()