class Parentclass:
    def __init__(self):
        print('pc constructor')
    def show_pc(self):
        print('parent class')

class Childclass(Parentclass):
    def __init__(self):
        super().__init__()
        print('cc constructor')
    def show_cc(self):
        print('child class')

class Grandchildclass(Childclass):
    def __init__(self):
        super().__init__()
        print('gcc constructor')
    def show_gcc(self):
        print('grand child class')

o=Grandchildclass()
#o.show_pc()

#o.show_cc()

#o.show_gcc()
