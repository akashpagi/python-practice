class Mobile:
    def __init__(self):
        self.model='iphone x'    # 
    def set_model(self):    
        self.model='iphone 11'
obj=Mobile()                  
print('before setting:',obj.model)
obj.set_model()
print('after setting:',obj.model)
print()

class Phone:
    def set_model(self,n):
        self.model=n
    
m=Phone()
m.set_model('OnePlus 7')
print('model:',m.model)