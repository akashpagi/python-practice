# recurision :
i=0
def recurision():
    #i=0
    global i
    i=i+1
    print('recurision :',i)
    recurision()
recurision()

import sys 
sys.setrecursionlimit(50)
print(sys.getrecursionlimit())

