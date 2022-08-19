# Elements in NumPy arrays can be accessed by indexing. 
# Indexing is an operation that pulls out a select set of values from an array. 
# The index of a value in an array is that value's location within the array

import numpy as np
my_array = np.array([2,4,6])
print(my_array) #[2 4 6]

# Individual values stored in an array can be accessed with indexing.
my_array = np.array([2,4,6])
print(my_array) ##[2 4 6]
value = my_array[2]
print(value) #6

#Multi-dimensional Array Indexing
my_array =np.array([[2,3,4],[6,7,8]])
print(my_array) 
# [[2 3 4]
#  [6 7 8]]

#Assigning Values with Indexing
my_array =np.array([2,4,6])
my_array[2] = 10
print(my_array)  #[ 2  4 10]

#Values can also be assigned to a particular location in a 2-D arrays using the form:
my_array = np.array([[2,3,4],[6,7,8]])
print(my_array)
# [[2 3 4]
#  [6 7 8]]
my_array[1,2]=20
print(my_array)
# [[ 2  3  4]
#  [ 6  7 20]]