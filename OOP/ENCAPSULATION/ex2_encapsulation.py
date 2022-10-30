#ex2 : access data indirectly using setter and getter methods:
class Myclass:
    __Sid="A"
    def setSid(self,Sid):
        self.__Sid= Sid
    def getSid(self):
        return self.__Sid

o=Myclass()
print(o.getSid())
#print(o.__Sid) #AttributeError: 'Myclass' object has no attribute '__Sid'
o.setSid("B")
print(o.getSid())