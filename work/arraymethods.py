# append() method:
import array as a
my_array = a.array('i', [1,2,3,4,5])
my_array.append(6)
print(my_array)

# insert() method:
my_array=a.array('i',[1,2,3,4,5])
print('using insert method ')
my_array.insert(0,26)
my_array.insert(3,2001)
print(my_array)

# pop() method:

print('using pop method')
my_array = a.array('i', [1,2,3,4,5])
my_array.pop(3)
print(my_array)

# remove() method :
print('using remove method')
num = a.array('i', [1,2,1,3,4,5])
num.remove(1)
print(num)

#index() method :
print('using index method')
num = a.array('i', [1,4,2,3,4,5])
print(num.index(4))

# reverse() method:
print('using reverse method')
num = a.array('i', [1,2,3,4,5])
num.reverse()
print(num)

# extend() method:
#print('using extend method')
num = a.array('i', [1,2,3,4,5])
print('using extend method')
extend_num=a.array('i',[6,7,8])
num.extend(extend_num)
print(num)

# fromlist() method:
print('using fromlist method')
num = a.array('i', [1,2,3,4,5])
list_num =[11,22,33]
num.fromlist(list_num)
print(num)

# count() method:
print('using count method')
num = a.array('i', [1,2,2,2,3,4,5])
print(num.count(2))


# tolist() method:
print('using list method')
my_array = a.array('i', [1,2,3,4,5])
#c = my_array.tolist()
print(my_array.tolist())


'''# fromstring() method:
print('using fromstring method')
my_char_array =a.array('c', ['g','e','e','k'])
my_char_array.fromstring()
print(my_char_array)'''

# buffer_info() method:
print('using buffer_info method')
num = a.array('i', [1,2,3,4,5])
print(num.buffer_info())

 









