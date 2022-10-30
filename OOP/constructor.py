class Phone_market:
    def __init__(self,m,realvalue=11000): #constructor (__int__())
        self.model=m 
        self.realvalue=realvalue 
    def show_model(self,p):
        self.price=p 
        print('model:',self.model,'price:',self.price)
        print('realvalue:',self.realvalue)
# passsing argument(m) to constructor
o_1=Phone_market('redmi_note_8')
# accessing method from outside class
o_1.show_model(15000)
print()
o_2=Phone_market('oppo_f1',9000)
o_2.show_model(12000)
