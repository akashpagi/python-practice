class Cars:
    @staticmethod          #decorator
    def show_model(m,p):   # static method
        model=m
        price=p
        print('model:',model,'price:',price)
show= Cars()
Cars.show_model('bmw m2',1000000)  # calling static method
