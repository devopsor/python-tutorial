##################################Parameters of Function##############################
# Python's function definition is very simple, but it is very flexible. 
# In addition to the required parameters that are normally defined, default parameters, 
# variable parameters and keyword parameters can also be used, 
# so that the interface defined by the function can not only handle complex parameters, 
# but also simplify the caller's code.

def power(x):
    return x*x
print(power(3))

# For power(x) functions, the parameter xis a positional parameter.
def power(x ,n):
    result = 1
    while n > 0:
        result *= x
        n= n-1
    return result
print(power(3,3))

#default parameters
# Python's error message is clear: the calling function is power() missing a positional argument n.
# This is where the default parameters come in handy. Since we often calculate x 2 , 
# it is perfectly fine to set the default value of the second parameter n to 2:
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(3))
print('\n')
# In this way, when we call power(5), it is equivalent to calling power(5, 2):

#What are the benefits of using default parameters? 
# The biggest advantage is that it can reduce the difficulty of calling functions.
# For example, let's write a function for the registration of first-grade elementary school students, 
# which needs to be passed in nameand gendertwo parameters:
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
enroll('Sarah', 'F')
# name: Sarah
# gender: F  
print('\n')

# What if you want to continue to pass in information such as age, city, etc.? 
# This will greatly increase the complexity of calling functions.
# We can set age and city as default parameters:
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
# In this way, most students do not need to provide age and city when registering, only the required two parameters:
enroll('Sarah', 'F')
print('\n')
# name: Sarah  
# gender: F    
# age: 6       
# city: Beijing

# First define a function, pass in a list, add one END and return:
def add_end(L=[]):
    L.append('END')
    return L
# When you call normally, the result seems to be fine:
print(add_end([1, 2, 3])) #[1, 2, 3, 'END']
print(add_end(['x', 'y', 'z'])) #['x', 'y', 'z', 'END']
print(add_end()) #['END']
print(add_end()) #['END', 'END']  
print(add_end()) #['END', 'END', 'END'] 
print('\n')

# To modify the above example, we can do it with Nonethis immutable object:
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print(add_end([1, 2, 3])) #[1, 2, 3, 'END']
print(add_end(['x', 'y', 'z'])) #['x', 'y', 'z', 'END']
print(add_end()) #['END']
print(add_end()) #['END']
print(add_end()) #['END']
print('\n')
####################################Variable Parameter####################################
# In Python functions, it is also possible to define variadic parameters. 
# As the name implies, a variable parameter means that the number of parameters passed in is variable, 
# which can be 1, 2 to any number, or 0.

# To define this function, we must determine the input parameters. 
# Since the number of parameters is uncertain, we first thought that a, b, c... can be passed in as a list or tuple, 
# so that the function can be defined as follows:
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc((1, 3, 5, 7)))  #84
print(calc([1, 3, 5, 7]))  #84
print(calc({1, 3, 5, 7}))  #84
print('\n')

#If you use variadic parameters, the way to call the function can be simplified to this:
#So, let's change the function's parameter to a variadic parameter:
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 3, 5, 7))  #84

# Defining a variable parameter is compared to defining a list or tuple parameter by simply prefixing the parameter 
# with a *number. Inside the function, the parameter numbers received is a tuple, 
# so the function code is completely unchanged. 
# However, when calling this function, you can pass in any number of parameters, including 0 parameters:
print(calc(1,2)) #5
print(calc()) #0

# This way of writing is of course feasible, but the problem is too cumbersome, 
# so Python allows you to add a *number in front of the list or tuple, and pass the elements of the list or 
# tuple into variable parameters:
nums = [1, 2, 3]
print(calc(*nums)) #14
print('\n')

# *nums Indicates that numsall elements of this list are passed in as variable parameters. 
# This notation is quite useful and common.

#################################### Keyword Arguments###############################
# Variable parameters allow you to pass in zero or any number of parameters, 
# which are automatically assembled into a tuple when the function is called. 
# The keyword arguments allow you to pass in 0 or any number of arguments with parameter names, 
# and these keyword arguments are automatically assembled into a dict inside the function. See example:
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael',30) #name: Michael age: 30 other: {}
person('Michael',30, city='Tokyo') #name: Michael age: 30 other: {'city': 'Tokyo'}

# Of course, the complex call above can be written in a simplified form:
extra = {'city': 'Tokyo', 'job': 'Engineer'}
person('Jack', 24, **extra) #name: Jack age: 24 other: {'city': 'Tokyo', 'job': 'Engineer'}
print('\n')

#Named keyword arguments
def person(name, age, **kw):
    if 'city' in kw:
        # Has city parameter
        pass
    if 'job' in kw:
        # Has job parameter
        pass
    print('name:', name, 'age:', age, 'other:', kw)
# But the caller can still pass in unrestricted keyword arguments:
person('Jack', 24, city='Tokyo', addr='Shinjyuku', zipcode=123456)
#name: Jack age: 24 other: {'city': 'Tokyo', 'addr': 'Shinjyuku', 'zipcode': 123456}

# If you want to restrict the names of keyword arguments, 
# you can use named keyword arguments, for example, only accept cityand jobas keyword arguments. 
# The functions defined in this way are as follows:
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Tokyo', job='Engineer') #Jack 24 Tokyo Engineer
print('\n')

#Named keyword arguments can have default values ​​to simplify invocation:
def person(name, age, *, city='Tokyo', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer') #Jack 24 Tokyo Engineer
print('\n')

#################################### Parameter Combination ###############################
# To define a function in Python, you can use required parameters, default parameters, variable parameters, 
# keyword parameters, and named keyword parameters, all of which can be used in combination. 
# Note, however, that the order of parameter definitions must be: required parameters, default parameters, 
# variadic parameters, named keyword parameters, and keyword parameters.
# For example, define a function that contains several of the above parameters:
def  f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def  f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
# When the function is called, the Python interpreter automatically passes in the corresponding parameters 
# according to the parameter position and parameter name.
f1(1, 2)  #a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3) #a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b') #a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}

f1(1, 2, 3, 'a', 'b', x=99) #a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None) #a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# The most amazing thing is that with a tuple and dict, you can also call the above function:
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)  #a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw) #a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

