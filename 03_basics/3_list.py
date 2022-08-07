###################################list########################################

#A list is an ordered collection from which elements can be added and removed at any time.
# For example, to list the names of all the students in the class, you can use a list to represent:
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates) #['Michael', 'Bob', 'Tracy']

#A variable classmatesis a list. Use the len()function to get the number of list elements:
print(len(classmates)) #3

# Use the index to access the element at each position in the list, remember that the index is from the 0 beginning:
print(classmates[0]) #Michael
print(classmates[1]) #Bob
print(classmates[2]) #Tracy
# print(classmates[3])  #IndexError: list index out of range


# When the index is out of range, Python will report an IndexError error, 
# so, to make sure the index is not out of bounds, remember that the index of the last element is len(classmates) - 1
print(classmates[len(classmates)-1])  #Tracy

# If you want to get the last element, in addition to calculating the index position, 
# you can also use -1 as an index to get the last element directly:
print(classmates[-1]) #Tracy

# and so on, you can get the second from last and third from last:
print(classmates[-1]) #Tracy
print(classmates[-2]) #Bob
print(classmates[-3]) #Michael
# print(classmates[-4]) #IndexError: list index out of range

#A list is a mutable ordered list, so you can append elements to the end of the list:
classmates.append('Adam')
print(classmates)  #['Michael', 'Bob', 'Tracy', 'Adam']

#You can also insert an element at a specified position, such as the position with the index number 1:
classmates.insert(1, 'Jack')
print(classmates) #['Michael', 'Jack', 'Bob', 'Tracy', ]

#To remove elements at the end of a list, use the pop() method:
print(classmates.pop()) #'Adam'
print(classmates) #['Michael', 'Jack', 'Bob', 'Tracy']

# To delete an element at a specified position, use the pop(i) method, where it is the index position:
print(classmates.pop(1)) #Jack
print(classmates)  #['Michael', 'Bob', 'Tracy']

# To replace an element with another element, you can directly assign it to the corresponding index position:
classmates[1] = 'Sarah'
print(classmates) #['Michael', 'Sarah', 'Tracy']

#The data types of the elements in the list can also be different, for example:
list = ['Apple', 123, True]
print(list) #['Apple', 123, True]

#The list element can also be another list, for example:
str = ['python', 'java', ['asp', 'php'], 'scheme']
print(str) #['python', 'java', ['asp', 'php'], 'scheme']
print(str[2][1]) #php
print(len(str)) #4
