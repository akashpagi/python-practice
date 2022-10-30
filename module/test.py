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

print('-------------------------------')

