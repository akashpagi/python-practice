class Mobile:
    fp='Yes'               # class variable
@classmethod            # class method
def is_fp(cls):
    print('fingure print :',cls)

m=Mobile()
n=Mobile()
o=Mobile()

print('m:',Mobile.fp)
print('n:',Mobile.fp)
print('o:',Mobile.fp)
print()

print('modify class:')
Mobile.fp='No'
print('m:',Mobile.fp)
print('n:',Mobile.fp)
print('o:',Mobile.fp)
print()

print('modify object :')
n.fp= 'No fp'
print('n:',n.fp)
