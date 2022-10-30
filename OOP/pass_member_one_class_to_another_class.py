class Student:
    # constructor
    def __init__(self,n,r):
        self.name= n
        self.roll= r
    # instance method
    def disp(self):
        print('name:',self.name,'roll:',self.roll)
        
class User:
    #static method
    @staticmethod
    def show(s):
        print('s_name:',s.name,'s_roll:',s.roll)
        # calling disp function
        s.disp()  

#creating object of student class with parameters
o=Student('hardik',1)
User.show(o) # 