class Army:
    def __init__(self):
        self.name='Rhaul'
        #self.inner=self.Gun()  # Inner object Name
    def show(self):
        
        print('OuterClass:')
        print('name:',self.name)

    class Gun:
        def __init__(self):
            self.name='AK47'
            self.capacity='75 Rounds'
            self.length='32.3 in'
        def disp(self):
            print()
            print('InnerClass:')
            print('gun_name:',self.name)
            print('gun_capacity:',self.capacity)
            print('gun_length:',self.length)

o=Army()

o.show()


#OuterClassName.InnerClassObjectName.InnerClassFunctionName



Ic=Army().Gun()
print()

Ic.disp()

print()
print(Ic.name)
print(Ic.capacity)
print(Ic.length)


