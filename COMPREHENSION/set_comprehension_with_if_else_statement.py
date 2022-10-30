set_1=set()
for i in range(7):
    if (i%2==0):
        set_1.add(i)
    else:
        set_1.add(i*100)
        pass
#print(set_1)

print('set comprehension with if else statement:')
else_set={i if (i%2==0) else (i*100) for i in range(7)}
print(else_set)