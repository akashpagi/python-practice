class Pclass1:
    def pc1(self):
        print('parent1')
class Pclass2:
    def pc2(self):
        print('parent2')
class Cclass(Pclass1,Pclass2):
    def cc(self):
        print('childclass')
obj=Cclass()
obj.cc()
obj.pc1()
obj.pc2()

print()
# multiple inheritance with constructor and method resolution order(MRO):

class Parentclass1:
    def __init__(self):
        super().__init__()
        print('pc1 constructor')
class Parentclass2:
    def __init__(self):
        super().__init__()
        print('pc2 constructor')

class Childclass(Parentclass1,Parentclass2):
    def __init__(self):
        super().__init__()
        print('cc constructor')
o=Childclass()