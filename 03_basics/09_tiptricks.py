#############################Tips and Tricks1#########################
condition = False
if condition:
    x = 1
else:
    x=0
print(x) #0
###############################################OR
x = 1 if condition else 0
print(x) #0
condition = True
x = 1 if condition else 0
print(x) #1
print('\n')
#############################Tips and Tricks2#########################
num1 = 10000000000
num2 = 100000000
total = num1 + num2
print(total)  #10100000000
###############################################OR
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(total) #10100000000
print(f'{total:,}')  #10,100,000,000
print(f'{total:_}')  #10_100_000_000
print('\n')
#############################Tips and Tricks3#########################
f = open('input.txt','r')
file_contents = f.read()
f.close()
wrods = file_contents.split(' ')
word_count = len(wrods)
print(word_count) #3
###############################################OR
with open('input.txt', 'r') as f:
    file_contents = f.read()
words = file_contents.split(' ')
word_count = len(wrods)
print(word_count) #3
print('\n')

#############################Tips and Tricks4#########################
names = ['Corey','Chris','Dave','Travis']
index = 0
for name in names:
    print(index,name)
    index+=1
# 0 Corey
# 1 Chris
# 2 Dave
# 3 Travis
###############################################OR
for index, name in enumerate(names):
    print(index,name)
# 0 Corey
# 1 Chris
# 2 Dave
# 3 Travis
for index, name in enumerate(names, start=1):
    print(index,name)
# 1 Corey
# 2 Chris
# 3 Dave
# 4 Travis
print('\n')
#############################Tips and Tricks5#########################
names = ['Peter Parker','Clark Kent','Wade Wilson','Bruce Wayne']
heros = ['Spiderman','Superman','Deadpool','Batman']
for index, name in enumerate(names):
    hero = heros[index]
    print(f'{name} is actually {hero}')

# Peter Parker is actually Spiderman
# Clark Kent is actually Superman   
# Wade Wilson is actually Deadpool  
# Bruce Wayne is actually Batman    
###############################################OR
for name, hero in zip(names, heros):
    print(f'{name} is actually {hero}')

# Peter Parker is actually Spiderman
# Clark Kent is actually Superman   
# Wade Wilson is actually Deadpool  
# Bruce Wayne is actually Batman    
universes = ['Marvel','DC','Marvel','DC']
for name, hero, universe in zip(names, heros, universes):
    print(f'{name} is actually {hero} from {universe}')

# Peter Parker is actually Spiderman from Marvel
# Clark Kent is actually Superman from DC
# Wade Wilson is actually Deadpool from Marvel
# Bruce Wayne is actually Batman from DC

for value in zip(names, heros, universes):
    print(value)
# ('Peter Parker', 'Spiderman', 'Marvel')
# ('Clark Kent', 'Superman', 'DC')
# ('Wade Wilson', 'Deadpool', 'Marvel')
# ('Bruce Wayne', 'Batman', 'DC')
print('\n')
#############################Tips and Tricks6#########################
#unpacking
a,b = 1,2
print(a) #1
print(b)  #2
print(a, b) #1 2

a,b,*c = 1,2,3,4,5,6
print(a) #1
print(b) #2
print(c) #[3, 4, 5, 6]

a,b,*c,d= 1,2,3,4,5,6
print(a) #1
print(b) #2
print(c) #[3, 4, 5]
print(d) #6

a,b,*_,d= 1,2,3,4,5,6
print(a) #1
print(b) #2
print(d) #6
print('\n')
#############################Tips and Tricks7#########################
class Person:
    pass
person =  Person()
person.first = 'Corey'
person.last = 'Schafer'
print(person.first) #Corey
print(person.last) #Schafer
###############################################OR

first_key =  'first'
first_val = 'Corey'
first_key =  'last'
first_val = 'Schafer'
print(person.first) #Corey
print(person.last) #Schafer
print('\n')
###############################################OR
person_info = {'first':'Corey', 'last':'Schafer'}
for key,value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))
# Corey
# Schafer
print('\n')
#############################Tips and Tricks8#########################
username = input('username:')
password = input('password:')
print('Logging In ...')

###############################################OR
#Dont't show password in terminal
from getpass import getpass
username = input('username:')
password = getpass('password:') 
print('Logging In ...')


#############################Tips and Tricks9#########################
#Get the documentary information of imported library

# $ python
# Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import smtpd
# >>> help(smtpd)
# Help on module smtpd:

# NAME
#     smtpd - An RFC 5321 smtp proxy with optional RFC 1870 and RFC 6531 extensions.

# MODULE REFERENCE
#     https://docs.python.org/3.9/library/smtpd

#     The following documentation is automatically generated from the Python
#     source files.  It may be incomplete, incorrect or include features that
#     are considered implementation detail and may vary between Python
#     implementations.  When in doubt, consult the module reference at the
#     location listed above.

# DESCRIPTION
#     Usage: %(program)s [options] [localhost:localport [remotehost:remoteport]]





#############################Tips and Tricks10#########################
#Get the method information of imported library
# $ python
# Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from datetime import datetime
# >>> dir(datetime)    #※
# ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__',
# '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', 
# '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 
# 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 
# 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 
# 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 
# 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
