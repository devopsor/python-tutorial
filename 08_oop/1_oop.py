###########################Object Oriented Programming#################################

# Object Oriented Programming
# Briefly speaking, OOP is a kind of programming idea. OOP regards the object as the basic unit of  the program, 
# an object contains data and functions to manipulate the data.

# Process-oriented programming treats a computer program as a series of commands, that is,
# the sequential execution of a set of functions. In order to simplify the program design, 
# the process-oriented function is further divided into sub-functions, that is, the large function is divided 
# into small functions to reduce the complexity of the system.

# In object-oriented programming, a computer program is regarded as a collection of objects, 
# and each object can receive messages from other objects and process these messages. 
# The execution of a computer program is a series of messages passed between objects.

# In Python, all data types can be treated as objects, and of course custom objects are also possible. 
# The custom object data type is the concept of class in object-oriented.

# We use an example to illustrate the difference between procedure-oriented and object-oriented program flow.
# Suppose we want to deal with student grade sheets. To represent a student's grades, a procedure-oriented 
# program can be represented by a dict:
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
print(std1) #{'name': 'Michael', 'score': 98} 
print(std2) #{'name': 'Bob', 'score': 81}

# And processing student grades can be implemented through functions, such as printing student grades:
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
print_score(std1) # Michael:98
print_score(std2) # Bob:81
print('\n')
# If we adopt the idea of ​​object-oriented programming, we prefer not to think about the execution flow of the program, 
# but the data type of student should be regarded as an object, which has name and score these two properties.
# If you want to print a student's grades, you must first create an object corresponding to the student, and then 
# send a print_score message to the object to let the object print out its own data.
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# Sending a message to an object is actually calling the associated function corresponding to the object, 
# which we call the method of the object. Object-oriented programs are written like this:
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score() #Bart Simpson: 59
lisa.print_score() #Lisa Simpson: 87
 

# Object-oriented design ideas come from nature, because in nature, the concepts of classes and instances are 
# natural. Class is an abstract concept, such as the Class we define—Student, which refers to the concept of students, 
# and the instance (Instance) is a specific Student, for example, Bart Simpson and Lisa Simpson are two specific 
# Students.

# Therefore, the object-oriented design idea is to abstract the Class and create the Instance according to the Class.
# Object-oriented abstraction is higher than functions, because a Class contains both data and methods for 
# manipulating data.

#Summary
# Data encapsulation, inheritance and polymorphism are the three major characteristics of object-oriented, 
# which we will explain in detail later.