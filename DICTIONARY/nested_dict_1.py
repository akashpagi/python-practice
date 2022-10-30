print('nested empty dictionary:')
d={1:{},
     2:{},
     3:{}}
print(d)
print()

print('creating nested dictionary:')
n_d={'course':'python','fees':499,1:{'course':'java','fees':399}}
print(n_d)
print()
print('accessing nested dictionary:')
print(n_d['course'])
print(n_d['fees'])
print(n_d[1]['course'])
print(n_d[1]['fees'])
print()

print('modifying nested dictionary:')
n_d['course']='ML'
n_d['fees']=1000
n_d[1]['course']='swift'
n_d[1]['fees']=1200
print(n_d)

print('add new items in nested dictionary:')
n_d['duration']='6 months'
n_d[1]['duration']='10 months'
n_d[1][2]={'course':'objective-c','fees':'600'}
print(n_d)

