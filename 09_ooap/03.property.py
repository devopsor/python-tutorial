###############################@property###################################

#When binding properties, if we directly expose the properties, although it is very simple to write, there is no way to 
# check the parameters, so the results can be changed casually:
class Student(object):
    pass
s = Student()
s.score = 9999
print(s.score) #9999

# This is obviously illogical. In order to limit the scope of the score, you can set_score() set the score through 
# one method, and get_score() get the score through another, so that in the set_score() method, you can check 
# the parameters:
class Student(object):
    def get_score(self):
         return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# Now, operating on an arbitrary Student instance, you can't set the score arbitrarily:
s = Student()
s.set_score(60) # ok!
print(s.get_score()) #60
# s.set_score(9999) #ValueError: score must between 0 ~ 100!

# However, the above calling method is a little more complicated, and it is not as straightforward and simple as 
# using properties directly.

# Is there a way to both inspect parameters and access class variables in an easy way like properties? 
# For the perfect Python programmer, this is a must!

# Remember that decorators can dynamically add functionality to a function? For class methods, decorators work 
# just as well. Python's built-in @property decorator is responsible for turning a method into an attribute call:
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 90 # OK!  Actually converted to s.set_score(90)
print(s.score) # 90 Actually converted to s.get_score(90)

# Noticing this magic @property, when we operate on instance properties, we know that the properties are probably 
# not directly exposed, but implemented through getter and setter methods.
# You can also define read-only properties, only define the getter method, and not define the setter method is a 
# read-only property:
class Student(object):
    @property
    def birth(self):
        return self._birth  #Note: the method name of the attribute should not be the same as the instance variable name. 

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2022 - self._birth
# The above birth is a read-write property, but age a read-only property, because it can be calculated age based 
# on the current time.birth
s = Student()
s.birth = 1990 # OK!  Actually converted to s.set_brith(1990)
print(s.birth) # 1990 Actually converted to s.get_birth()
print(s.age) # 32 Actually converted to s.get_age()
print('\n')


# Pay special attention: the method name of the attribute should not be the same as the instance variable name. 
# For example, the following code is wrong:
class Student(object):
    @property
    def birth(self):
        return self.birth

# This is because s.birth when the call is made, it is first converted into a method call, and when it is executed 
# return self.birth, it is regarded as an accessed self attribute, so it is converted into a method call, resulting in infinite
# recursion, which eventually leads to a stack overflow error RecursionError.

#Summary
# @propertyWidely used in class definitions, it allows the caller to write short code while ensuring the necessary 
# checks for parameters, thus reducing the possibility of errors when the program is running.