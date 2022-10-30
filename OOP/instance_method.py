print('instance method without parameter/formal argument:')
class Myclass:
    def __init__(self):
        self.model='iphone x'    # instance variable 
    def show_model(self):         # instance method
        # accessing instance variable inside instance method
        print(self.model) 
# create object p        
p=Myclass()                  
# calling instance method without argument 
# syntax:object_name.method_name()
p.show_model() 


print()
print('instance method with parameter/formal argument:')
class Mobile_price:
    def __init__(self):
        self.model='OnePlus 7'               # instance variable 
    def model_price(self,p):         # instance method with parameter
        self.price=p
        print('model:',self.model,'price:',self.price) 
# create object p        
p=Mobile_price()
p.model_price(35000)




