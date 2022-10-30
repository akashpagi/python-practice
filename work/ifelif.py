'''# 1 to 10 (free)
# 11 to 30 (30)
# 31 to 70 (20)

# if elif statement
age = int(input('enter your age:'))
if age==1 or age<1:
   print ("sorry !! you have entered wrong age")
elif 1<age<=10:
   print ("1.ticket price : free")
 
elif 10<age<=30:
   print ("2.ticket price : 30rupees")

elif  30<age<=70:
   print ("3.ticket price : 20rupees")
elif 70<age:
    print("good bye !!")'''

day=input('enter day :')
if (day == 'sunday'):
   print ('market')
elif (day =='monday'):
   print ('today is monday')
elif (day=='tuseday'):
   print ('my birthday')
elif(day=='wednesday') :
   print ('makr sankratri')
else :
    print('today is holiday')

