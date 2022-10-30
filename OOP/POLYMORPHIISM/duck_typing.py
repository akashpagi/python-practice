class Duck:
    def sound(self):
        print("Duck sound like 'quack quack'")
class Cat:
    def sound(self):
        print("Cat sound like 'meow meow'")

class Dog:
    def talk(self):
        print("Dog talk like 'bark bark'")


def Myfunction(o):
    o.sound()

d=Duck()
Myfunction(d)

c=Cat()
Myfunction(c)

D=Dog()
Myfunction(D)