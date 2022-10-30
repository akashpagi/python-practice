n_d={1:{'course':'python','fees':499},
     2:{'course':'java','fees':399}}

print()

print('accessing nested dictionary:')
print(n_d[1]['course'])
print(n_d[1]['fees'])
print(n_d[2]['course'])
print(n_d[2]['fees'])
print()

print('modifying nested dictionary:')
n_d[1]['course']='swift'
n_d[2]['fees']=599
print(n_d)
print()

print('add new dict in nested dictionary:')
n_d[3]={'course':'objective-c','fees':'600'}
print(n_d)
print()

print('add new items in nested dictionary:')
n_d1={1:{'course':'python','fees':499},
      2:{'course':'java','fees':399}}
n_d1[1]['duration']='6 months'
n_d1[2]['duration']='10 months'
print(n_d1)
