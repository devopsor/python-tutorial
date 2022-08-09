################################################Type###################################
#When we get a reference to an object, how do we know what type the object is and what methods are there?

#First, let's judge the object type and use the type() function:
# Basic types can be type() judged by:
print(type(123)) #<class 'int'>
print(type('str')) #<class 'str'>
print(type(None)) #<class 'NoneType'>
print('\n')

# If a variable points to a function or class, you can also use the type() judgment:
print(type(abs)) #<class 'builtin_function_or_method'>


# But type() what type does the function return? It returns the corresponding Class type. If we want to if 
# judge in the statement, we need to compare whether the types of the two variables are the same:
print(type(123) == type(345))#True
print(type(123)==int) #True
print('\n')

print(type('abc')==type('123'))#True
print(type('abc') == str)#True
print(type('abc')==type(123)) #False
print('\n')

# Judging basic data types can be written directly int, stretc., but what if you want to judge whether an object is 
# a function? You can use types constants defined in modules:

import types
def fn():
    pass
print(type(fn)==types.FunctionType) #True
print(type(abs)==types.BuiltinFunctionType) #True
print(type(lambda x: x)==types.LambdaType) #True
print(type((x for x in range(10)))==types.GeneratorType) #True
print('\n')

# type() The basic types that can use judgment can also use judgment isinstance():
print(isinstance('a', str)) #True
print(isinstance(123, int)) #True
print(isinstance(b'a', bytes)) #True
print('\n')

# And you can also judge whether a variable is one of some types, for example, the following code can judge 
# whether it is a list or a tuple:
print(isinstance([1, 2, 3], (list, tuple))) #True
print(isinstance((1, 2, 3), (list, tuple))) #True

# Always use isinstance() to judge the type first, and you can "catch all" the specified type and its subclasses.

# use dir()

# If you want to get all the properties and methods of an object, you can use a dir()function that returns a list of strings,
# for example, to get all the properties and methods of a str object:
print(dir('ABC'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
# '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
# 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
# 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Similarly __xxx__ attributes and methods are used for special purposes in Python, (※)
# such as __len__methods returning length. 
# In Python, if you call a len() function to try to get the length of an object, in fact, inside the len() function, 
# it automatically calls the object's __len__() methods, so the following code is equivalent:
print(len('ABC')) #3
print('ABC'.__len__()) #3

# If we want to use the class we wrote ourselves len(myObj), we can write a __len__()method ourselves:
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog)) #100

#The rest are normal properties or methods, like lower() returning lowercase strings:
print('ABC'.lower()) #abc
print('\n')

# It's not enough to just list the properties and methods getattr(), setattr() as well hasattr(), we can directly manipulate 
# the state of an object:
class MyObject(object):
    def __init__(self):
         self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

# Next, you can test the object's properties:
print(hasattr(obj, 'x')) #True
print(obj.x) #9
print(hasattr(obj, 'y')) #False
setattr(obj, 'y', 19) 
print(hasattr(obj, 'y')) #True
print(getattr(obj, 'y')) #19
print(obj.y) #19

#If you try to get an attribute that doesn't exist, an AttributeError will be thrown:
# getattr(obj, 'z') #AttributeError: 'MyObject' object has no attribute 'z'

# A default parameter can be passed in, and if the property does not exist, the default value is returned:
print(getattr(obj, 'z', 404)) #404

#You can also get the methods of an object:
print(hasattr(obj, 'power')) #True
# print(getattr(obj, 'power')) 
# #<bound method MyObject.power of <__main__.MyObject object at 0x000001D661BC74F0>>

#Summary
# Through a series of built-in functions, we can analyze any Python object and get its internal data. It should be 
# noted that only when we do not know the object information, we will get the object information. If you can 
# write directly:

# sum = obj.x + obj.y

# Just don't write:

# sum = getattr(obj, 'x') + getattr(obj, 'y')

# An example of correct usage is as follows:
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

# Suppose we want to read an image from the file stream fp, we first need to determine whether the fp object has 
# a read method. If it exists, the object is a stream, and if it does not exist, it cannot be read. hasattr() came in handy.

# Please note that in dynamic languages ​​such as Python, according to duck types, there are read() methods, 
# which does not mean that the fp object is a file stream, it may also be a network stream, or a byte stream in memory, 
# but as long as the read()method returns is valid image data, it does not affect the function of reading the image.
