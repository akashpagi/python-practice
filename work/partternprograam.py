#num=int(input('enter the number of row : '))
#for row in range(1,num+1):
  #  print(' * '* row)
    
num=int(input('enter the number of row : '))
for row in range(1, num+1):
    for column in range(1, row+1):
        print("{0}{1}".format(row,column),end='__  $__  __ __ $ __   __')# other print(row,column,symbols,numbers ,end=' ')
    print()
# reverse :'''
'''num=int(input('enter the number of row : '))
for row in range(num,0,-1): # u can also use num (num-1)
    for column in range(1, row+1):
        print(' * ',end=' ')# other print(row,column,symbols,numbers ,end=' ')
    print()
num=int(input('enter the number of row : '))
for row in range(1, num+1):
    for column in range(1, row+1):
        print('  + ',end=' ')# other print(row,column,symbols,numbers ,end=' ')
    print()'''



