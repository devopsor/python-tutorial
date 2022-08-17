#################################Class and Instance#################################
# The most important concepts of object-oriented are the class (Class) and the instance (Instance). (※)
# It must be remembered that the class is an object template, such as the Student class, and the instance is 
# a specific "object" created according to the class. Each object has The same method, but the respective data 
# may be different.

# Still taking the Student class as an example, in Python, a class is defined by class keywords:
class Student(object):
    pass

# class
# The class name is followed by the class name, that is Student, the class name is usually a capitalized word, 
# followed by (object), indicating which class the class is inherited from. We will talk about the concept of 
# inheritance later. Usually, if there is no suitable inheritance class, Just use object classes, which are classes that 
# all classes will eventually inherit from.

# After defining a Student class, you can create an instance based on the Student class. Creating an Student 
# instance is achieved by the class name + ():
bart = Student()
simon = Student()
print(bart)    #<__main__.Student object at 0x000001DC54FBBB80>
print(simon) #<__main__.Student object at 0x000001DC54FBB340>
print(Student) #<class '__main__.Student'>

# It can be seen that the variable bartpoints to an Student instance, followed by 0x000001DC54FBBB80 
# the memory address. The address of each object is different, and Student itself is a class.
# You can freely bind properties to an instance variable, for example, to bart bind a name property to an instance:
bart.name = 'Bart Simpson'
print(bart.name) #Bart Simpson

# Since a class can play the role of a template, when creating an instance, we can force some attributes that 
# we think must be bound to be filled in. By defining a special __init__method, when an instance is created , 
# the properties such as name, etc. are bound:score
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
# Note: There are two underscores before and after the special method "__init__"! ! !(※)

# Note that __init__　the first parameter of the method is always self, (※)
# representing the created instance itself, 
# therefore, within the __init__method, you can bind various properties to self, because selfit points to the created 
# instance itself.

# With a __init__ method, when creating an instance, you can't pass in empty parameters, you must pass __init__ 
# in parameters that match the method, but self you don't need to pass in, the Python interpreter will pass the instance 
# variables in by itself:
bart = Student('Bart Simpson', 59)
print(bart.name) #Bart Simpson
print(bart.score) #59

# Compared with ordinary functions, functions defined in classes have only one difference, that is, 
# the first parameter is always an instance variable self, and this parameter is not passed when calling. 
# Other than that, class methods are no different from normal functions, so you can still use default arguments, 
# variadic arguments, keyword arguments, and named keyword arguments.

# Data Encapsulation

#An important feature of object-oriented programming is data encapsulation. In the above Student class, 
# each instance has its own nameand score these data. We can access this data through functions, such as printing 
# a student's grades:
def print_score(std):
    print('%s: %s'%(std.name, std.score))
print_score(bart) #Bart Simpson: 59

# However, since Student the instance itself owns the data, to access the data, there is no need to access it from 
# an external function. You can directly  define a function of Student to access the data inside the class, 
# thus encapsulating the "data". These functions that encapsulate data Studentare associated with the class itself, 
# which we call class methods:
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_grade(self):
            if self.score >= 90:
                return 'A'
            elif self.score >= 60:
                return 'B'
            else:
                return 'C'
# self To define a method, it is the same as a normal function except that the first parameter is . 
# To call a method, you only need to call it directly on the instance variable. Except that self you don't need to pass it, 
# other parameters are passed in normally:
bart = Student('james', 99)
bart.print_score() #james: 99
print(bart.get_grade()) #A

#Summary

# A class is a template for creating an instance, and an instance is a concrete object. The data owned by 
# each instance is independent of each other and does not affect each other;

# A method is a function bound to an instance. Unlike ordinary functions, a method can directly access 
# the instance's data;

# By calling a method on an instance, we are directly manipulating the data inside the object without knowing 
# the implementation details inside the method.

# Unlike static languages, Python allows binding any data to instance variables, that is, for two instance variables, 
# although they are different instances of the same class, they may have different variable names:
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age=9
print(bart.age) #9
print(lisa.age) #AttributeError: 'Student' object has no attribute 'age'

