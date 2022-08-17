###################################tuple########################################
# Another type of ordered list is called a tuple.
# Tuple and list are very similar, but once tuple is initialized, it cannot be modified. (※)
# For example, it also lists the names of classmates:
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates[1]) #Bob
print(classmates) #('Michael', 'Bob', 'Tracy')

# Now, the tuple of classmates cannot be changed, 
# nor does it have methods such as append() and insert(). 
# Other methods of getting elements are the same as list, 
# you can use it normally classmates[0], classmates[-1] but you cannot assign it to another element.

# What's the point of an immutable tuple? Because tuples are immutable, the code is safer. 
# If possible, use tuple instead of list.

# The trap of tuple: When you define a tuple, the elements of the tuple must be determined 
# at the time of definition, such as:
t = (1, 2)
print(t) #(1, 2)
# If you want to define an empty tuple, you can write ():
t = ()
print(t) #()

# However, to define a tuple with only 1 element, if you define it like this:
t = (1)
print(t) #1

# The definition is not tuple, but 1, the number! 
# This is because parentheses () can represent both tuple and parentheses in mathematical formulas, 
# which creates ambiguity. Therefore, Python stipulates that the calculation results are naturally obtained 
# according to the parentheses 1.
# Therefore, a tuple with only one element must be defined with a comma ,to disambiguate like the following:
t=(1,)
print(t) #(1,)

# When Python displays a tuple with only one element, it will also add a comma ,, 
# so as not to be misunderstood as parentheses in the sense of mathematical calculations.
t = ('a', 'b', ['A', 'B'])
# t[1]=2  #TypeError: 'tuple' object does not support item assignment
t[2][0] = 'X'
t[2][1] = 'Y'
print(t[2][0]) #X
print(t[2][1]) #Y
print(t) #('a', 'b', ['X', 'Y'])
print(*t) #'a', 'b', ['X', 'Y']
print(*t[1]) #b

