class Mobile:
    def __init__(self): 
        self.model='nokia' # instance variable
    def s_model(self): # accessing instance variable 
        print(self.model)
m=Mobile()
print(m.model) #or m.s_model() 
print()
m=Mobile()
n=Mobile()
o=Mobile()
print(m.model)
print(n.model)
print(o.model)

print()
print('modify')
o.model='iphone x'
print(o.model)

