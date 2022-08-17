####################################Instance Attribute####################################
#The way to bind properties to an instance is through instance variables, or through selfvariables:

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
print(s.score) #90

# But what if class Student itself needs to bind a property? Attributes can be defined directly in the class. 
# This attribute is a class attribute and is Student classified all:
class Student(object):
    name = 'Student'
    
# When we define a class attribute, although this attribute is classified as all, all instances of the class can be 
# accessed. Let's test it out:
class Student(object):
    name = 'Student'

s = Student()
print(s.name) #Student
print(Student.name) #Student

s.name = 'Michael' 
print(s.name) #Michael
print(Student.name) #Student


del s.name
print(s.name) #Student
print(Student.name) #Student
print('\n')

del Student.name
# print(s.name) #AttributeError: 'Student' object has no attribute 'name'
# print(Student.name) #AttributeError: type object 'Student' has no attribute 'name'

# As can be seen from the above example, when writing a program, do not use the same name for instance attributes 
# and class attributes, because instance attributes with the same name will mask the class attributes, but after you 
# delete the instance attributes, use The same name, the access will be the class property.
