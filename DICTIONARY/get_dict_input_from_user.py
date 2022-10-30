s={}
n=int(input('enter number of elements:'))
for i in range(n):
    k=input('enter key:')
    v=input('enter value:')
    s.update({k:v})
print(s)