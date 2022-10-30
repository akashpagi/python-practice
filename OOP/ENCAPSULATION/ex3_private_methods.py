# ex3 :private methods : we can access only within means own class

class Car:
    def __init__(self):
        self.__UpdateSoftware()
    #def __init__(self): # Line 16
        #self.__UpdateSoftware() # Line 16
    def Drive(self): #public method
        print('Driving')
    def __UpdateSoftware(self): #private method
        print('Updating Software')
c=Car()
c.Drive() 
# you can't access private methods outside the class (means you will get error)
#AttributeError: 'Car' object has no attribute '__UpdateSoftware'
#c.__UpdateSoftware() 