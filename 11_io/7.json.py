########################################JSON########################################

# Python dictobjects can be directly serialized to JSON {}, but, in many cases, we prefer to classrepresent objects, 
# such as defining Studentclasses, and then serializing:
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

#Running the code, mercilessly got one TypeError:
# print(json.dumps(s)) #TypeError: Object of type Student is not JSON serializable


# The reason for the error is that the Studentobject is not an object serializable to JSON.
# If even class the instance object can't be serialized to JSON, it certainly doesn't make sense!
# Don't worry, let's take a closer look at dumps() the parameter list of the method. We can find that in addition to 
# the first required obj parameter, the dumps() method also provides a lot of optional parameters:

# These optional parameters allow us to customize JSON serialization. The reason why the preceding code can't 
# Student serialize the class instance to JSON is because by default, the dumps() method doesn't know how to 
# turn the Student instance into a JSON {} object.

# The optional parameter default is to turn any object into an object that can be serialized as JSON. 
# We only need to Student write a conversion function for it, and then pass the function in:
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
# the Student instance is first student2dict() converted by the function dictand then serialized to JSON smoothly:
print(json.dumps(s, default=student2dict))  #"name": "Bob", "age": 20, "score": 88}

# However, the next time you encounter an Teacher instance of a class, it still cannot be serialized to JSON. 
# We can be lazy and turn any classinstance into dict:
print(json.dumps(s, default=lambda obj: obj.__dict__)) #{"name": "Bob", "age": 20, "score": 88}

# Because usually class an instance has a __dict__property, which is one dict, to store the instance variable. 
# There are a few exceptions, such as defined __slots__classes.

# In the same way, if we want to deserialize JSON to an Studentobject instance, the loads() method first converts 
# an dictobject, and then the function we pass in object_hook is responsible for dictconverting it to an Student instance:
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

# The results are as follows:
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student)) #<__main__.Student object at 0x000001FF03B04D00>
print('\n')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)  #JSON Data is a str: {"name": "Bob", "age": 20, "score": 88}
reborn = json.loads(data)
print(reborn) #{'name': 'Bob', 'age': 20, 'score': 88}

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data) #Dump Student: {"name": "Bob", "age": 20, "score": 88}
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild) #Student object (Bob, 20, 88)


#######################################Summary##########################################
# The Python language-specific serialization module is pickle, 
# but if you want to make serialization more general and web standards-compliant, you can use json modules.

# json Modules dumps() and loads() functions are examples of very well-defined interfaces. 
# When we use it, we only need to pass in a required parameter. 
# However, when the default serialization or deserialization mechanism does not meet our requirements, 
# we can pass in more parameters to customize the serialization or deserialization rules, 
# which not only makes the interface simple and easy to use, but also fully scalability and flexibility.

