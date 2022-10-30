# upper() function :
str1='akash'
str2=str1.upper()
print(str1.upper())
print(str2)
print()

# lower() function :
str1='AKASH'
str2=str1.lower()
print(str1.lower())
print(str2)
print()

# swapcase() function :
str1='JAVA ''java ' 'javaSCRIPT ' 'JaVaScRpT '
print(str1.swapcase())
print()

# title() function 
str1='how are you ? ' 'hEllO akAsH !!'
print(str1.title())
print()

# isupper() function :
name1='AKASH'
name2='Akash'
#print(name.isupper()) 
str1=name1.isupper()
print(name1)  
print(str1)
print(name2.isupper())
print()

# islower() function :
str1='Akash'
str2='akash'
print(str1.islower())
print(str2.islower())
print()

# istitle() function :
str1='Hello Akash !! How Are You ?'
str2='hello Akash'
print(str1.istitle())
print(str2.istitle())
print()

print('isdigit() function :')
digit1='8495'
digit2='akash26'
print(digit1.isdigit())
print(digit2.isdigit())
print()


print('isalpha() function :')
alpha1='Python' # (letter should be between A to Z and a to z)
alpha2='akash24'
alpha3='z'
print(alpha1.isalpha())
print(alpha2.isalpha())
print(alpha3.isalpha())
print()


print('isalnum() function :')
alnum1='akash26' # (letter should be between A to Z ,a to z and numbers 0 to 9)
alnum2='Akash'
alnum3='z'
print(alnum1.isalnum())
print(alnum2.isalnum())
print(alnum3.isalnum())
print()

print('isspace() function :')
space1='   '
space2='   akash26'
print(space1.isspace())
print(space2.isspace())
print()

print('lstrip() finction :')
strip1='    python'
s1=strip1.lstrip()
print(strip1)
print(s1)
print()

print('rstrip() finction :')
strip1='python    '
s1=strip1.rstrip()
print(strip1)
print(s1)
print()

print('strip() finction :')
s1='    java    '
print(s1.strip())
print()

print('capitalize() function :')
s1="this Is A 'String'."
s2=s1.capitalize()
print(s1)
print(s2)
print()

print('casefold() function :')
#The casefold() method returns a string where all the characters are lower case.
#This method is similar to the lower() method, but the casefold() method is stronger, more aggressive,
# meaning that it will convert more characters into lower case,and 
# will find more matches when comparing two strings and both are converted using the casefold() method.
s1="CASEfold MethoD."
s2=s1.casefold()
print(s1)
print(s2)
print()

print('isdecimal() function :')
#The isdecimal() method returns True if all the characters are decimals (0-9).
#This method is used on unicode objects.
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())
print()

print('isidentifier() function :')
#The isidentifier() method returns True if the string is a valid identifier, otherwise False.
#A string is considered a valid identifier if it only contains alphanumeric letters (A-Z)or(a-z)  and (0-9), or underscores (_).
#A valid identifier cannot start with a number, or contain any spaces.
a ='MyFolder'
b ='demo2'
c ='my_Functions'
d ='334path'
e ='akash 34'
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print(e.isidentifier())
print()

print('isnumeric()function :')
#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
#Exponents, like ² and ¾ are also considered to be numeric values.
a = '0'       #unicode for 0 (\u0030)
b = '\u00B2'  #unicode for & sup2;
c = '10km2'
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print()

print('isprintable() function :')
str1='2bee_or_not_to_bee'
str2=str1.isprintable()
print(str1)
print(str2)
str3='Hello!\nare you #1?'
str4=str3.isprintable()
print(str3)
print(str4)










