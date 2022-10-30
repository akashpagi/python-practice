print('classmethod without parameter/ formal argument')
class Emp:
   salary=15000
   @classmethod
   def show_salary(cls):
        print('salary:',cls.salary)
obj_1=Emp()
Emp.show_salary()

print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')

print()
print('classmethod with parameter/ formal argument')  
class Emp_1:
   name='rohit'
   @classmethod
   def show_details(cls,age):
       cls.age=age
       print('name:',cls.name)
       print('age:',cls.age)
obj_2=Emp_1()
Emp_1.show_details(28) 



print()

class D:
    multiplier = 2
    @classmethod
    def val(cls, x):
        return cls.multiplier * x
obj_3=D()
print('answer:',obj_3.val(7))
