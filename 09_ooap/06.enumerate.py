#################################Enumerate###########################
# When we need to define constants, one way is to use uppercase variables to define integers, such as months:

# A better approach is to define a class type for such an enumeration type, and then each constant is a unique 
# instance of the class. Python provides Enum classes to implement this functionality:
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# This gives us Monthan enumeration class of type that can be used directly Month.Janto refer to a constant, 
# or to enumerate all of its members:
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# Jan => Month.Jan , 1 
# Feb => Month.Feb , 2 
# Mar => Month.Mar , 3 
# Apr => Month.Apr , 4 
# May => Month.May , 5 
# Jun => Month.Jun , 6 
# Jul => Month.Jul , 7 
# Aug => Month.Aug , 8 
# Sep => Month.Sep , 9 
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12

# value 
# Attributes are int constants that are automatically assigned to members and are 1 counted from the beginning 
# by default.

# If you need more precise control over the enumeration type, you can Enum derive a custom class from:
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun =0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu =4
    Fri = 5
    Sat = 6

# @unique Decorators can help us check to ensure that there are no duplicate values.
# There are several ways to access these enum types:
day1 = Weekday.Mon
print(day1) #Weekday.Mon
print(Weekday.Tue) #Weekday.Tue
print(Weekday.Tue.value) #2

print(day1 ==Weekday.Mon) #True
print(day1 ==Weekday.Tue) #False
print(Weekday(1)) #Weekday.Mon
print(day1 == Weekday(1)) #True

# print(Weekday(7)) #ValueError: 7 is not a valid Weekday

# It can be seen that enumeration constants can be referenced by member names, and enumeration constants 
# can be obtained directly according to the value of value.