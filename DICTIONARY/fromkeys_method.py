keys=(1,2,3)
#values=('a','s','p','d')
v=dict.fromkeys(keys)
print(v)
print()

#values='asp'
v=dict.fromkeys(keys,'asp')
print("dict with value 'asp' :",v)
print()

values=['a','b']
v=dict.fromkeys(keys,values)
print("dict with value of mutable object :",v)  