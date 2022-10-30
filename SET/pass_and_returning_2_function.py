def old_s(s):
  
    print(type(s))
    print(s)
    print()
    print('using for loop:')
    for i in s:
        print(i)
    return s
s={2,5,3,'java'}
new_s=old_s(s)
print()
print(type(new_s))
print(new_s)
