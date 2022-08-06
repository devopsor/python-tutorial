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
