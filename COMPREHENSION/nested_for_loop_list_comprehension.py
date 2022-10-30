# Nested list comprehension
a=[]
for i in range(4):
    for j in range(4):
        a.append(i*j)
        pass

lst= [[i*j for j in range(4)] for i in range(4)] 
print(lst) 