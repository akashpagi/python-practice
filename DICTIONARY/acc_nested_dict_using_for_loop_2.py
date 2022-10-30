n_d={1:{'course':'python','fees':499},
     2:{'course':'java','fees':399}}
print('dict keys:')
for d_k in n_d:
    print(d_k)

print()

print('dict_keys & values:')
for d_k in n_d:
    for kv in n_d[d_k]:
        print(kv,'=',n_d[d_k][kv])