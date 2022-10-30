# method overriding similar like constructor overriding:

class Add:
    def result(self,a,b):
        print('addition:',a+b)

        
class Multi(Add):
    def result(self,a,b):
        super().result(16,12) # or super().result(a,b) # 30 
        print('multiplication:',a*b)
    
m=Multi()
m.result(10,20)