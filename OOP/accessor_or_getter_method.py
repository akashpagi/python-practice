class Myclass:
    def __init__(self):
        self.fname='akash'
    def get_fname(self):
        return f'first_name : {self.fname}'
obj=Myclass()
x=obj.get_fname()
print(x)