# with class mthod :
class Person:
    age='24'                     # class variable
    def __init__(self,n): 
        self.name=n
    def show_name(self):
        print('name:',self.name)
    @classmethod                 # class method
    def is_age(cls):
        print('age:',cls.age)

p1=Person('rohit')
p1.show_name()
Person.is_age()                  #Accessing class varible inside class method


print()

#Outside class:
class Emp:
    salary='12000'           #class varible
    @classmethod             # class method
    def show_salary(cls):
        cls.salary           #Accessing class varible inside class method
m=Emp()
print('salary:',Emp.salary)  #Accessing class varible outside class 


print()
# modify:
print('modify:')
n=Emp()
o=Emp()
Emp.salary='10000'
print('m_salary:',Emp.salary)
print('n_salary:',Emp.salary)
print('o_salary:',Emp.salary)


