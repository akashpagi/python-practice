
'''print('create a calss and class with argument')
class Computer:
    def config(self):
        print('i5,16gb,1TB')
    def add(self,x,y):# function with argument
        return x+y
c=Computer()
c.config()
print(type(c))
print()  
print(c.add(5,24))
print()

print('class with constructor __init__ method')
class Mobile:
    def __init__(self):
        self.model='realme X'
    def show_model(self):
        self.price= 14999
        print('model:',self.model,'  price:',self.price)
m=Mobile()
m.show_model()
 
print()'''

print('class with argument')
print()
class Phone:
    def __init__(self,m):
        self.model=m
    def show_model(self,n):
        self.price=n
        print('model:',self.model,'price:',self.price)

a=Phone('iphone x')
a.show_model(50000)
print('id:',id(a))
print()

b=Phone('htc')
b.show_model(25000)
print('id:',id(b))
print()

c=Phone('oneplus 7 pro')
c.show_model(35000)
print('id:',id(c))


