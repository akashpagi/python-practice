class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x
class B:
    def __init__(self,x):
        self.x=x
a=A(100)
b=B(200)
print(a+b)

print('-----------------------------')


class Point:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'({self.a},{self.b})'  # or f'{self.a},{self.b}'
    def __mul__(self,other):
        a = self.a*other.a
        b = self.b*other.b
        c = Point(a,b)
        return c

    def __gt__(self,other):
        r1=self.a*other.a
        r2=self.b*other.b
        if (r1>r2):
            return True
        else:
            return False   
p1_a = Point(5,3)
p2_b = Point(2,7)
c = p1_a * p2_b   # Point.__mul__(p1_a,p2_b)
print(c)
print(c.a)
print(c.b)
if (p1_a > p2_b):
    print('a wins')
else:
    print('b wins')


print('-----------------------------')

class Point_1:
    def __init__(self, a_1,b_1):
        self.a_1 = a_1
        self.b_1 = b_1
    def __str__(self):
        return f'({self.a_1},{self.b_1})'  # or f'{self.a},{self.b}'
    def __mul__(self,other):
        a_1 = self.a_1*other.a_1
        b_1 = self.b_1*other.b_1
        return Point(a_1,b_1)

   
p1 = Point_1(2,3)
p2 = Point_1(2,2)

print(p1 * p2) # Point.__mul__(p1_a,p2_b)


print('---------------------------------------')

class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f'({self.x },{self.y},{self.z})'
    def __sub__(self,other):
        return vector(self.x-other.x , self.y-other.y , self.z-other.z)
v1=vector(2,2,0)
v2=vector(1,0,1)
print(v1-v2)

   
