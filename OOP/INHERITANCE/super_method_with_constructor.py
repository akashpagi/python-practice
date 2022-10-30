class Computer:
    def __init__(self,computer,ram):
        self.computer=computer
        self.ram=ram 

class Laptop(Computer):
    def __init__(self,computer,ram,model):
        super(). __init__(computer,ram) # calling parent class constructor
        self.model= model
    
l=Laptop('lenovo',2,'l420')
print('computer:',l.computer)
print('ram:',l.ram)
print('model:',l.model)
