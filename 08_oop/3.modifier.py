#################################Modifiers#################################
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

dart = Student('simon', 99)
print(dart.name) #simon
print(dart.score) #99

# Inside the Class, there can be properties and methods, and the external code can manipulate the data by 
# directly calling the method of the instance variable, thus hiding the complex internal logic.

# However, from the previous definition of the Student class, external code can still freely modify the properties of 
# an name instance score:
dart.name = 'James'
print(dart.name) #James
print('\n')

# If you want to prevent internal attributes from being accessed externally, you can add two underscores before 
# the name of the attribute __. In Python, if the variable name of an instance __starts with a variable name, 
# it becomes a private variable (private), which can only be accessed internally. It is not accessible from the outside, 
# so let's change the Student class:
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def set_score(self, score):
        self.__score = score
    def get_score(self):
        return self.__score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
dart = Student('Dylan', 97)
dart.__name = 'Diel' # the e
print(dart.__name) #Diel
print('\n')

print(dart.get_name()) #Dylan
print(dart.get_score()) #97
dart.set_name('John') 
dart.set_score(100) 
print(dart.get_name()) #John
print(dart.get_score()) #100
dart.print_score() #John: 100


