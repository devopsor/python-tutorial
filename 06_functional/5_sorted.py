############################Sorting Algorithm#################################

# Sorting is also an algorithm that is often used in programs. 
# Whether using bubble sort or quicksort, the core of sorting is to compare the size of two elements. 
# If it's a number, we can compare it directly, but what if it's a string or two dicts? 
# It doesn't make sense to compare sizes directly, so the process of comparison must be abstracted 
# through functions.

# Python's built-in sorted() function can sort a list:
print(sorted([36, 5, -12, 9, -21])) #[-21, -12, 5, 9, 36]
print('\n')

_list = sorted([36, 5, -12, 9, -21])
print(_list)#[-21, -12, 5, 9, 36]

# In addition, the sorted() function is also a higher-order function, 
# it can also receive a key function to implement custom sorting, (※)
# such as sorting by absolute value size:
print(sorted([36, 5, -12, 9, -21], key=abs)) #[5, 9, -12, -21, 36]
print('\n')
# the function specified by key will act on each element of the list and 　(※)
# sort according to the result returned by the key function. 　(※)
# Compare the original list with the key=abs processed list:

# Let's look at another example of string sorting:
_list = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(_list) #['Credit', 'Zoo', 'about', 'bob']

# By default, strings are sorted by ASCII size comparison, since 'Z' < 'a', 
# as a result, uppercase letters Zare sorted before lowercase letters a.
_list = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(_list) #['about', 'bob', 'Credit', 'Zoo']

# To reverse sort, without changing the key function, you can pass in the third parameter reverse=True:
_list =  sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(_list) #['Zoo', 'Credit', 'bob', 'about']

