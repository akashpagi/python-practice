# append method :
def append():
    a=[10,-73,37.47,'vivek']
    print('before append :',a)
    a.append(234)
    print('after append :',a)
append()
print()

#insert method :
def insert():
    list1=[10,30,11.33,-20]
    list1.insert(0,'raju')
    list1.insert(3,85)
    print('insert method :',list1)
insert()
print()

#pop & pop (n) method :
#list2=[10,20.32,'python',-45]
def pop():
    list2=[10,20.32,'python',-45]
    list2.pop()
    print('pop method :',list2)
    list2=[10,20.32,'python',-45]
    list2.pop(2) # pop(position_number)
    print('pop(n) method :',list2)
pop()
print()

#remove method :
def remove():
    a=[1,2,3,4,5]
    a.remove(4)
    print('remove method :',a)
  
    print('first occurrence example :')
    b=[1,2,3,4,3,5]
    print('before remove method :',b)
    b.remove(3)
    print('after remove method :',b)
remove()
print()

#index method :
a=[10,20,20,40]
num=a.index(20)
print('index method :',num)
print()

#reverse method :
def reverse():
    a=[1,2,3,4,5]
    a.reverse()
    print('reverse method :',a)
reverse()
print()

#extend method :
def extend():
    a=[1,2,3,4,5]
    b=[6,7,8]
    print('before extend a & b :',a,b)
    a.extend(b)
    print('after extend method :',a)
extend()
print()

#count method :
def count():
    a=[10,20,30,20,20,50]
    num1=a.count(20)
    num2=a.count(30)
    print('count method (same num in list):',num1)
    print('count method (single num in list):',num2)
count()
print()

# sort method :
def sort():
    a=[40,50,30,23,5]
    print('before :',a)
    a.sort()
    print('after sorting :',a)
sort()
print()

# clear method  :
def clear():
    a=[10,20,'python',30.45]
    print('befroe :',a)
    a.clear()
    print('after clear :',a)
clear()
print()





