n_d={'course':'python','fees':499,1:{'course':'java','fees':399}}
print(n_d)
print()
for i in n_d:
    print(i)

print()

print('using for loop:')
for i in n_d :
    if type(n_d[i]) is dict:
        for k in n_d[i]:
            print(k,'=',n_d[i][k])
    else:
        print(i,'=',n_d[i])