#################################Inheritance and Polymorphism############################
# In OOP programming, when we define a class, we can inherit from an existing class, the new class is called 
# a subclass (Subclass), and the inherited class is called a base class, parent class or superclass (Base class, 
# Super class).
# For example, we've written a Animalclass called with a run() method that prints directly:
class Animal(object):
    def run(self):
        print('Animal is running...')
class Cat(Animal):
    pass
class Dog(Animal):
    pass

# For Dog, it Animalis its parent class, and for Animal, it Dog is its subclass. Cat and Dog similar.
# What are the benefits of inheritance? 
# The biggest benefit is that the subclass gets the full functionality of the parent class. Since Animialthe run() 
# method is implemented, Dog and Cat as a subclass do nothing, it automatically has the run() method:
cat = Cat()
dog = Dog()
cat.run()
dog.run()
# Animal is running...
# Animal is running...
print('\n')


######################################Polymorphism###############################################
# When the same method exists in both the subclass and the superclass run(), we say that the subclass run() 
# overrides the superclass, run() and the subclass will always be called when the code runs run(). In this way, 
# we get another benefit of inheritance: polymorphism.
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
cat = Cat()
dog = Dog()
cat.run() #Cat is running...  
dog.run() #Dog is running...
print('\n')

# To understand what polymorphism is, we first need to explain a little more about data types. When we define a class, 
# we are actually defining a data type. The data types we define are no different from the data types that come with 
# Python, such as str, list, and dict:
a = list() # a is a list type
b = Animal() # b is Animal type
c = Dog() # c is Dog type
print(isinstance(a, list)) #True
print(isinstance(b, Animal)) #True
print(isinstance(c, Animal)) #True
print(isinstance(b, Dog)) #False
print(isinstance(c, Dog)) #True

# Therefore, in the inheritance relationship, if the data type of an instance is a subclass, its data type can also be 
# regarded as a superclass. However, the reverse does not work:
a = Animal()
print(isinstance(a, Dog)) #False

# To understand the benefits of polymorphism, we need to write one more function that accepts a Animal variable 
# of type:
def run_once(animal):
    animal.run()
    
# When we pass Animalin an instance, run_once() it prints out:
run_once(Animal()) #Animal is running...
run_once(Dog()) #Dog is running...
run_once(Cat()) #Cat is running...

#Summary
# Inheritance can directly take all the functions of the parent class, so that there is no need to start from scratch. 
# The subclass only needs to add its own unique methods, or it can override the methods that the parent class
# is not suitable for.