#write a file
f1=open('asp1.txt','w')
f1.write('My asp1.txt file !!!!')
#f1.close()
print('asp1.txt :Successfully Writtren')
#f1=open('asp1.txt','r')
#print(f1.read())
print()

print('Closed or not:',f1.closed)
print('Accessing mode:',f1.mode)
print('Name of the file:',f1.name)


#f1.close()

print()

f=open('asp.txt','r')
r=f.read()
print(r)
f.close()


