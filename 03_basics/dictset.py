###############################dictionary #######################################

# Python has a built-in dictionary: the support of dict, the full name of dict is dictionary, 
# also called map in other languages, uses key-value (key-value) storage, and has extremely fast search speed.
# For example, suppose you want to find the corresponding grades based on the names of your classmates. 
# If you use a list to implement it, you need two lists:
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
for name in names:
    if name == 'Bob':
        print(scores[1]) #75
        break
print('\n')
# Given a name, to find the corresponding score, you must first find the corresponding position in the names, 
# and then extract the corresponding score from the scores. The longer the list, the longer the time.

# In Python, it is implemented with dict, only a "name"-"grade" comparison table is needed, 
# and the results are directly searched according to the name. No matter how large the table is, 
# the search speed will not slow down. Write a dict in Python as follows:

dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict['Bob']) #75

# Why is dict lookup so fast? Because the implementation principle of dict is the same as that of looking up a dictionary. 
# Suppose the dictionary contains 10,000 Chinese characters, and we want to look up a certain word. 
# One way is to turn the dictionary back from the first page until we find the word we want. 
# This method is to find the element in the list. The larger the list, the slower the search.

# In this key-value storage method, when you put it in, you must calculate the storage location of the value according to the key, 
# so that you can get the value directly according to the key when you take it.

# The method of putting data into dict, in addition to specifying it during initialization, can also be put in by key:
dict = {}
dict['Adam'] = 67
print(dict['Adam']) #67
# To avoid the error that the key does not exist, there are two ways, one is by injudging whether the key exists:
print('Adam' in dict)
print('Bob' in dict)
print('\n')

# The second is through the method provided by dict get(). If the key does not exist, it can be returned None, 
# or the value specified by itself:
print(dict.get('Bob'))  #None
print(dict.get('Bob', -1)) #-1

dict['Bob'] = -1
print(dict.get('Bob')) # -1
print(dict.get('Bob', -1)) #-1, apparently, dict.get('Bob', -1) can not check whether item exist in list or not
# Note: None Python's interactive environment does not display results when returning.
print('\n')

print(dict) #{'Adam': 67, 'Bob': -1}
print(dict.pop('Bob')) #-1
print(dict) #{'Adam': 67}
print('\n')

# Note that the incoming parameter [1, 2, 3] is a list, and the display {1, 2, 3} only tells you that there are 3 elements 1, 2, and 3 
# inside the set, and the order of display does not mean that the set is ordered.
# Duplicate elements are automatically filtered in the set:
number = set([1, 1, 2, 2, 3, 3])
print(number) #{1, 2, 3}
number.add('4')
print(number) #{'4', 1, 2, 3}
print('\n')

number.remove('4')
print(number) #{1, 2, 3}
print('\n')

# add(key) Elements can be added to the set through methods, which can be added repeatedly, but have no effect:
number.add(4)
print(number) #{1, 2, 3, 4}
print('\n')

# remove(key) Elements can be removed by methods:
number.remove(4)
print(number) #{1, 2, 3}
print('\n')

# A set can be regarded as a collection of unordered and non-repetitive elements in a mathematical sense. 
# Therefore, two sets can perform operations such as intersection and union in a mathematical sense:
s1 =set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2) #{2, 3}
print(s1|s2) #{1, 2, 3, 4}

# The only difference between set and dict is that the corresponding value is not stored. 
# However, the principle of set is the same as that of dict. Therefore, mutable objects cannot be placed, 
# because it is impossible to judge whether two mutable objects are equal, and there is no guarantee of set. 
# Inside "there will be no repeating elements". Try putting the list into the set and see if an error will be reported.

###############################Revisiting Immutable Objects####################################
# As we said above, str is an immutable object, and list is a mutable object.
# For a mutable object, such as a list, when you operate on the list, the content inside the list will change, such as:
a = ['c', 'b', 'a']
print(a) #['c', 'b', 'a']
a.sort()
print(a) #['a', 'b', 'c']

# And for immutable objects, such as str, what about str:
a = 'abc'
b = a.replace('a', 'A')
print(a) #abc
print(b) #Abc

