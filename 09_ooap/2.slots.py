######################################Slots#########################################
# Under normal situation, when we define a class and create an instance of a class, we can bind any attributes 
# and methods to the instance, which is the flexibility of dynamic languages. First define the class:
class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name) #Michael

# You can also try to bind a method to the instance:
def set_age(self, age):
    self.age = age
def get_age(self):
    return self.age 

from types import MethodType
s.set_age = MethodType(set_age, s) #bind a method to the instance
s.set_age(25)
print(s.age) #25


# However, a method bound to one instance has no effect on another:
s2 = Student()
# s2.set_age(25)  # try to call new method, AttributeError: 'Student' object has no attribute 'set_age'

#To bind methods to all instances, bind methods to classes:
def set_score(self, score):
    self.score = score
def get_score(self):
    return self.score 

Student.set_score = set_score  #bind a method to the class
Student.set_age = set_age #bind a method to the class
Student.get_score = get_score #bind a method to the class
Student.get_age = get_age #bind a method to the class

s2 = Student()
s2.set_age(35)  # call new method
s2.set_score(95)  # call new method

#call new method
print(s2.age) #35
print(s2.get_age()) #35
#call new method
print(s2.score) #95
print(s2.get_score()) #95

###############################__slots__######################################

# But what if we want to restrict the properties of an instance? For example, only adding nameand ageproperties to 
# the Student instance is allowed.

# For the purpose of limitation, Python allows a special variable to be defined when defining a __slots__class to 
# limit the attributes that can be added to the class instance:(※)
class Student(object):
    __slots__ = ('name', 'age') # use tuple to define properies allowed to bound  (※)

s = Student()
s.name = 'Simon' 
s.age = '50'
print(s.name) #Simon
print(s.age) #50
# s.score=98 #AttributeError: 'Student' object has no attribute 'score'
# The property cannot be bound because it is not put in , 'score' trying to bind will get the error.

# It should be __slots__noted that the __slots__ defined properties only work on the current class instance, 
# and have no effect on inherited subclasses:(※)
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 100
print(g.score) #100

# Unless it is also defined in the subclass, in __slots__this way, the attributes allowed to be defined by the subclass 
# instance are its own __slots__ and the superclass __slots__. (※)