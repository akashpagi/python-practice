
# Constructor overriding:
class Parent:
    def __init__(self):
        self.name='akash'
        print('Parent class constructor')
        
class Child:
    def __init__(self,a):
        self.age=a
        print('age:',self.age)

c=Child(18)  # calling child class constructor
print()
p=Parent()
print(p.name)



