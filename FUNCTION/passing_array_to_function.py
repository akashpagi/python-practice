# passing array to function :
# passing array and returning array from function :
import array as a 
ar=a.array('i',[10,20,30,40,50])
def show(ar):
    print('a :',ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar
y=show(ar)
print('y :',y)
print(type(y))
for i in y:
    print(i)


  