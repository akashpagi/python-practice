class Robot:

    def __init__(self):        
        self.a=111
        self._b=222
        self.__c=333

o=Robot()

print(o.a)
print(o._b)
#print(o.__c) # private variables : we can access only within the class
    