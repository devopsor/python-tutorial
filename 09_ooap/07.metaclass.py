#################################Type###########################

# The biggest difference between dynamic languages ​​and static languages ​​is that the definitions of functions 
# and classes are not defined at compile time, but dynamically created at runtime.

# For example, if we want to define a Hello class, we write a hello.py module:
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)
h = Hello()

h.hello() #Hello, world
h.hello('New World!') #Hello, New World!

print(type(Hello)) #<class 'type'> 
print(type(h)) #<class '__main__.Hello'>
print('\n')
# type() 
# A function can view the type of a type or variable, Hello it is a class, its type is type, 
# h 
# but an instance, its type is class Hello.

# We say that the definition of a class is created dynamically at runtime, and the way to create a class is to 
# use a type() function.

# type() Functions can both return the type of an object and create new types. For example, we can type() create 
# Hello classes through functions without passing class Hello(object)...definitions:
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello() #Hello, world.

print(type(Hello)) #<class 'type'>
print(type(h)) #<class '__main__.Hello'>


# To create a class object, the type() function passes in 3 parameters in turn:
# Hello: 
# the name of the class;
# (object,): 
# A collection of inherited parent classes. Note that Python supports multiple inheritance. 
# If there is only one parent class, don't forget the single-element writing of tuple;
# dict(hello=fn)
# The method name of the class is bound to the function, here we fn bind the function to the method name hello.

# A class created by a type()function is exactly the same as writing a class directly, because when the Python 
# interpreter encounters a class definition, it just scans the syntax of the class definition, and then calls type() 
# the function to create the class.

# Under normal situation, we all use it class Xxx...to define classes, but type() functions also allow us to 
# create classes dynamically, that is to say, dynamic languages ​​themselves support dynamic creation of classes 
# at runtime, which is very different from static languages. To create a class during language runtime, 
# you must construct a source code string and then call the compiler, or use some tools to generate bytecode 
# implementation, which is essentially dynamic compilation and will be very complicated.

#################################metaclass##########################################
# In addition to using type() dynamically created classes, to control class creation behavior, you can also use 
# metaclasses.
# metaclass, literally translated as metaclass, the simple explanation is:
# metaclass is a template of class，it must be derived from type class
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
# With ListMetaclass, we also instruct to use ListMetaclass to customize the class when defining the class, 
# and pass in keyword parameters metaclass:
class MyList(list, metaclass=ListMetaclass):
    pass

# The magic takes effect when we pass in keyword arguments metaclass, which instruct the Python interpreter to 
# create MyList it through ListMetaclass.__new__(), where we can modify the class definition, for example, 
# add new methods, and then return to modify definition after.
# __new__()
# The parameters received by the method are:

# cls: The object of the class currently ready to be created;
# name: class name;
# bases: A collection of parent classes that a class inherits;
# attrs: A collection of methods for the class.

# Test MyList to see if the method can be called add():
L = MyList()
L.add(1)
print(L) #[1]

# And ordinary list does not have add() method:
L2 = list()
# L2.add(1) #AttributeError: 'list' object has no attribute 'add'

# What is the point of dynamic modification? MyList wouldn't it be simpler to just write the method directly in the 
# definition add()? Under normal situation, it should be written directly, and modification through metaclass
# is purely perverted.
# However, there is always a need to modify the class definition through the metaclass. ORM is a typical example.

# The full name of ORM is "Object Relational Mapping", that is, object-relational mapping, which maps a row of 
# a relational database to an object, that is, a class corresponds to a table. In this way, it is easier to write code without
# directly manipulating SQL statements.

# To write an ORM framework, all classes can only be defined dynamically, because only the user can define 
# the corresponding class according to the structure of the table.

# Let's try writing an ORM framework.

# The first step in writing a low-level module is to write the calling interface first. For example, if a user uses this ORM 
# framework and wants to define a User class to operate the corresponding database table User, we expect him to 
# write the following code:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Simple ORM using metaclass '

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # Save the mapping relationship between attributes and columns
        attrs['__table__'] = name # Assuming the table name is the same as the class name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

# Among them, the parent class Model and attribute type StringField are IntegerField provided by the ORM framework, 
# and the rest of the magic methods are automatically completed save() by the parent class . Model Although the 
# writing of metaclass is more complicated, it is very simple for ORM users to use.
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# When the user defines one class User(Model), the Python interpreter first User searches in the definition of 
# the current class metaclass. 
# If it is not found, it continues to search in the parent class. 
# If it is found Model, metaclass it uses Model the one defined in ModelMetaclass to create a User class, 
# that is, metaclass can hide Inherit to subclasses, but subclasses don't feel it themselves.

# In ModelMetaclass, a total of several things have been done:
# 1. exclude Modelmodifications to the class;
# 2. Find all attributes of the defined class in the current class (for example User), if you find a Field attribute, 
# save it to a __mappings__ dict, and delete the Field attribute from the class attribute, otherwise, it is easy to 
# cause runtime errors (The property of the class will overwrite the property of the same name of the class);
# 3.Save the table name to __table__, here it is simplified as the table name defaults to the class name.
# 4. In the Model class, you can define various methods of operating the database, such as save(), delete(), find(), 
# updateand so on.
# 5. We implemented the save() method to save an instance to the database. With table names, attribute-to-field 
# mappings, and collections of attribute values, INSERT statements can be constructed.

# Try writing code:
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

# The output is as follows:
# Found model: User
# Found mapping: id ==> <IntegerField:id>
# Found mapping: name ==> <StringField:username>
# Found mapping: email ==> <StringField:email>
# Found mapping: password ==> <StringField:password>
# SQL: insert into User (id,username,email,password) values (?,?,?,?)
# ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']


