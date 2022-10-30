class Duck:
    def sound(self):
        print('Duck:quack quack')
class Cat:
    def sound(self):
        print('Cat:meow meow')

class Dog:
    def talk(self):
        print('Dog:bark bark')


def Myfunction(o):
    if hasattr(o,'sound'):
        o.sound()
    if hasattr(o,'talk'):
        o.talk()

d=Duck()
Myfunction(d)

c=Cat()
Myfunction(c)
print()
D=Dog()
Myfunction(D)