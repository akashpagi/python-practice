# passing and returning dictionary from function:

def show(d):
    print(d)
    print(type(d))
    return d
d={1:'a',2:'s',3:'p'}
new_d=show(d)
print()
print(new_d)
print(type(new_d))