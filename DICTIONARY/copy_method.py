d={1:'a',2:'s',3:'p'}
print('original dict:',d)
print('id(s):',id(d))

print()

new_d=d.copy()
print('copied dict:',new_d)
print('id(d):',id(new_d))
print()

d[3]='xyz'
print('modifying original dict:',d)
print('id(d):',id(d))