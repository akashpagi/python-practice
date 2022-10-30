class Method_overloading:
    def sum(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            s=a+b+c
        elif (a!=None and b!=None):
            s=a*b
        else:
            s='Enter at least 2 or 3 numbers.'
        return s
o=Method_overloading()
print('three argument sum =',o.sum(10,20,30))
print('two argument condition=',o.sum(10,20))
print(o.sum())

print('---------------------------------------------------------')


class Campus:
    def area(self, x=None, y=None): # area method
        if (x!=None and y!=None ):
            return x*y
        elif (x!=None):
            return x+x
        else:
            return 0

obj = Campus()   # object
print("Area Value:", obj.area()) # zero(no) argument
print("Area Value:", obj.area(2)) # one argument
print("Area Value:", obj.area(3,5)) # two argument