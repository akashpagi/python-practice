# A view object that displays a list of a given dictionary’s (key, value) tuple pair.
d={1:'a',2:'b',3:'c'}
print(d)
print()

new_d=d.items()
print('new_d :',new_d)
print(type(new_d))
print()

print('convert tuple to list:')
lst=list(new_d)
print(lst)
print(type(lst))