a={1,4,5,6}
b={1,2,3,4,5}
print('intersection method :')
c=a.intersection(b)
print(c)

print()
print('union method :')
c=a.union(b)
print(c)
print()

x={'apple','mango','cherry'}
y={'cherry','car','bike'}
print('difference method :')
z=x.difference(y)
print(z)
w=y.difference(x)
print(w)

print()
a1={1,2,3,4}
b1={3,4,5,7,2,1}
print('issubset method :')
c1=a1.issubset(b1)
print(c1)

print()
y1={1,2,3,4}
x1={3,4,5,7,2,1}
print('issuperset method :')
w1=x1.issuperset(y1)
print(w1)
w2=y1.issuperset(x1)
print(w2)


print()
x_1={1,2,3,4}
y_1={8,6,5,7}
print('isdisjoint method :')
z_1=x_1.isdisjoint(y_1)
print(z_1)

print()
print('difference_update method :')
a_1={1,2,3,4}
a_2={3,5,2,4}
a_1.difference_update(a_2)
print(a_1)


print()
print('intersection_update method :')
b_1={1,2,3,4}
b_2={3,5,2,4}
b_1.intersection_update(b_2)
print(b_1)


print()
print('symmetric_diffrernce method :')
c_1={1,2,3,4}
c_2={3,5,2,4}
re=c_1.symmetric_difference(c_2)
print(re)

print()
print('symmetric_diffrernce_update method :')
s_1={1,8,3,4}
s_2={3,5,2,0}
s_1.symmetric_difference_update(s_2)
print(s_1)



