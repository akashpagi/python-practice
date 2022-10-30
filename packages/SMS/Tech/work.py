#sibling
'''def tech_work():
    print('tech folder --> work module (tech_work_function)')
print()

print('Method 1 :')
from User import request

def tech_work_1():
    print('tech folder --> work module (tech_work_function)')

request.user_request()

print()


#LENOVO@LENOVO-PC MINGW64 ~/Desktop/akash pagi/PYTHON/packages/SMS/Tech (master)
#python work.py <-------calling method 2
print('Method 2 :')


import sys
sys.path.append('C:/Users/LENOVO/Desktop/akash pagi/PYTHON/packages/SMS/User')
import request
def tech_work():
    print('tech folder --> work module (tech_work_function)')

request.user_request()'''


print('Method 3 :')
from User.request import user_request

def tech_work_2():
    print('tech folder --> work module (tech_work_function)')
user_request() 


 