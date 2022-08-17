#################################Customize Class###########################
# Be careful when you see variable or function names like __slots__this __xxx__, these have special uses in Python.

# __slots__ We already know how to use it, and __len__() we also know that the method is to make the class act 
# on the len()function.
# In addition, there are many such special-purpose functions in Python classes that can help us customize classes.

#__str__

# We first define a Studentclass and print an instance:
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael')) #<__main__.Student object at 0x000002338752BB80>

# How can I print beautifully? Just define a __str__()method that returns a nice-looking string:
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('Michael')) #Student object (name: Michael)

##################################__iter__########################################
# If a class wants to be used for for ... in looping, like list or tuple, it must implement a __iter__() method that 
# returns an iterable object, and then Python's for loop will keep calling the iterable object's __next__() method to 
# get the next value of the loop , until an Stop Iteration error is encountered to exit the loop.
# Let's take the Fibonacci number sequence as an example and write a Fib class that can act on the for loop:

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # initialize two counters: a，b
    def __iter__(self):
        return self # The instance itself is an iterative object, so return itself
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # calculate the next value
        if self.a > 500: # condition to exit the loop
            raise StopIteration()
        return self.a # return next value

for n in Fib():
    print(n)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377

##################################__getitem__########################################

# Although the Fib instance can act on the for loop, it looks a bit like a list, but it is still not enough to use 
# it as a list, for example, take the fifth element:
# Fib()[5] #TypeError: 'Fib' object is not subscriptable

# To behave like a list to take out elements by subscript, you need to implement a __getitem__() method:
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

# Now, you can access any item of the sequence by subscript:
f = Fib()
print(f[10]) #89
print(f[20]) #10946

# But list has a magic slicing method:
print(list(range(100))[5:10])  #[5, 6, 7, 8, 9]

# For Fib, it reports an error. The reason is that the __getitem__() incoming parameter may be an int or 
# a slice object slice, so make a judgment:
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n is index
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n is slice
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# Now try Fib's slice:
f = Fib()
print(f[0:5]) #[1, 1, 2, 3, 5]
print(f[:10]) #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# But the step parameter is not processed:
print(f[:10:2]) #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# There is also no handling of negative numbers, so there __getitem__() is still a lot of work to do to implement 
# one correctly.

# Corresponding to it is the __setitem__() method, which treats the object as a list or dict to assign a value to 
# a collection. Finally, there is a __delitem__() method for removing an element.

# In short, through the above method, our own defined classes behave no differently from Python's own list, 
# tuple, and dict. This is entirely due to the "duck typing" of dynamic languages, and there is no need to force 
# an interface to inherit.

##################################__getattr__########################################

# Under normal circumstances, when we call a method or property of a class, if it does not exist, an error will 
# be reported. For example, define Studenta class:
class Student(object):
    def __init__(self):
        self.name = 'Michael'

# Calling a name property, no problem, but calling a non-existing scoreproperty, there is a problem:
s = Student()
print(s.name) #Michael
# print(s.score) #AttributeError: 'Student' object has no attribute 'score'
# The error message clearly tells us that the attribute score in Student was not found.

# To avoid this error, in addition to adding an score attribute, Python has another mechanism, which is to write 
# a __getattr__() method that returns an attribute dynamically. amend as below:
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
s = Student()
print(s.name) #Michael
# When calling an attribute that doesn't exist, for example score, the Python interpreter will try to 
# call __getattr__(self, 'score') to try to get the attribute, so we have a chance to return scorethe value:
print(s.score) #99


# Note that it will only be called if the property is not found __getattr__, existing properties, for example name, 
# will not __getattr__ be looked up in.

# Also, notice that any invocation s.abc will return None, because the __getattr__ default return we defined is 
# just that None. To make the class respond to only a few specific properties, we have to throw AttributeError 
# an error according to the convention:
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student()
print(s.age()) #25
# print(s.score) #AttributeError: 'Student' object has no attribute 'score'

# This can actually process all the properties and method calls of a class dynamically without any special means.

# What does this fully dynamic invocation feature actually do? The effect is that it can be called for a completely 
# dynamic situation.

# If you want to write an SDK and write a method for the API corresponding to each URL, it will be exhausting, 
# and once the API is changed, the SDK will also need to be changed.
# With fully dynamic __getattr__, we can write a chained call:
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

# In this way, no matter how the API changes, the SDK can implement fully dynamic calls according to the URL, 
# and it does not change with the increase of APIs! It is very convenient to call the API.

####################################__call__####################################
# An object instance can have its own properties and methods that we instance.method() use to . 
# Can it be called directly on the instance itself? In Python, the answer is yes.
# Any class, just need to define a __call__() method, you can directly call the instance. See example:
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
        
# The calling method is as follows:
s = Student('Michael')
s() #My name is Michael.

# __call__() Parameters can also be defined. A direct call to an instance is like a call to a function, 
# so you can think of an object as a function and a function as an object, because there is no fundamental difference 
# between the two.

# If you think of objects as functions, then the functions themselves can actually be dynamically created at runtime, 
# because instances of classes are created at runtime, so we blur the line between objects and functions.

####################################callable####################################

# So, how to tell if a variable is an object or a function? In fact, more often, we need to judge whether an object 
# can be called. The object that can be called is an Callable object, such as a function and __call__() the class 
# instance we defined above:
s = Student('Simon')
s()#My name is Simon.
print(callable(s)) #True

m = max([1,2,3])
print(m) #3
print(callable(max)) #True

print(callable(None)) #False
print(callable('str')) #False

# Through callable()functions, we can determine whether an object is a "callable" object.

#Summary
# Python's class allows the definition of many custom methods, allowing us to generate specific classes very easily.
