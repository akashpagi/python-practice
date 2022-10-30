# def display isgeneraator function :
# yield returns a,b value
print('using generator function & yield statement :')
def display(a,b): 
    yield a 
    yield b
result=display(10,20)
print(result)
print(type(result))
print()

print('using list function :')
lst=list(result)
print(lst)
print()

print('using for loop:')
for i in lst:
    print(i)

print()
# next()_function :
print('using next function :')
def show(a,b):
    while(a<=b):
        yield a
        a+=1
result=show(1,5)
print(result)
print(type(result))
print()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))