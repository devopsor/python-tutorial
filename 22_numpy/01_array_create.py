# NumPy is a library for the Python programming language, adding support for large, 
# multi-dimensional arrays and matrices, along with a large collection of high-level mathematical 
# functions to operate on these arrays

import numpy as np


# To verify NumPy is installed, invoke NumPy's version using the Python REPL. Import NumPy and 
# call the .__version__ attribute common to most Python packages
print(np.__version__)  #1.23.2
# Outputting a version number indicates a successful NumPy installation

#####################################NumPy Arrays###########################
for value in np.array([1.0, 3.1, 5e-04, 0.007]):
    print(value)
# 1.0
# 3.1
# 0.0005
# 0.007
print('\n')

for value in np.array([1.0, 3.1, 5e-04, 0.007]):
    print(type(value))
# <class 'numpy.float64'>
# <class 'numpy.float64'>
# <class 'numpy.float64'>
# <class 'numpy.float64'>
print('\n')

for value in np.array([1, -0.038, 'gear', True]):
    print(value)
# 1
# -0.038
# gear
# True
print('\n')

for value in np.array([1, -0.038, 'gear', True]):
    print(type(value))
# <class 'numpy.str_'>
# <class 'numpy.str_'>
# <class 'numpy.str_'>
# <class 'numpy.str_'>
print('\n')

#####################################Array Multiplication###########################
# An entire NumPy array can be multiplied by a scalar in one step. The scalar multiplication operation below 
# produces an array with each element multiplied by the scalar 2
nparray = np.array([1,2,3,4])
print(2*nparray) #[2 4 6 8]

#####################################Array Creation###########################
# NumPy arrays are created with the np.array() function. 
# The arguments provided to np.array() needs to be a list or iterable
result = np.array([1,2,3])
print(result) #[1 2 3]

result = np.array([1,2,3], dtype='float')
print(result) #[1. 2. 3.]

my_array = np.array([1,2,3], dtype='float')
print(my_array.dtype)  #float64

#np.arange()
#NumPy's np.arange() function creates a NumPy array according the arguments start, stop,step
my_array = np.arange(0,10+2,2)
print(my_array) #[ 0  2  4  6  8 10]

#np.linspace()
# NumPy's np.linspace() function creates a NumPy array according the arguments start, stop,number of elements
#my_array = np.linspace(start, stop, number of elements)
my_array =np.linspace(0,2*np.pi,10)
print(my_array) #
# [0.         0.6981317  1.3962634  2.0943951  2.7925268  
#  3.4906585 4.1887902  4.88692191 5.58505361 6.28318531]

#np.zeros()
# NumPy's np.zeros() function creates a NumPy array containing all zeros of a specific size
#my_array = np.zeros((rows,cols))
my_array =np.zeros((5,4))
print(my_array) #
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# np.ones()
# NumPy's np.ones() function creates a NumPy array containing all 1's of a specific size
my_array =np.ones((5,4))
print(my_array) #
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

#####################################Arrays of Random Numbers###########################
# NumPy has functions to create arrays of many different types of random numbers in the np.random module

# np.random.randint(lower limit, upper limit, number of values)
my_array =np.random.randint(0,10,5)
print(my_array) #[8 5 6 8 1] random numbers

my_array =np.random.randint(0,10,[3,5])
print(my_array) 
# [[1 4 8 4 3]
#  [7 0 1 1 8]
#  [8 8 7 2 4]]

#Array of Random Floats
# Arrays of random floating point numbers can be created with NumPy's np.random.rand() function
# np.random.rand(number of values)
# To create an array of 5 random floats between 0 and 1:
my_array =np.random.rand(5)
print(my_array) 
#[0.45924568 0.86406766 0.88902137 0.04356328 0.04023839]

# To expand the range of random floats to between 0 and 10, multiply the result by 10
my_array =np.random.rand(5)*10
print(my_array) 
#[0.20452507 0.31338168 2.84297991 6.77407907 9.78631133]

# To change the range to between 11 and 13, we multiply the range by 2 (range 0-2), then add 11 to the result
my_array =np.random.rand(5)*2+11
print(my_array) 
#[11.49794965 12.71306683 12.80804545 12.38729468 12.01874006]

#Random Array Choice from a List
# np.random.choice(list of choices, number of choices)
lst = [1,5,9,11]
my_array =np.random.choice(lst,3)
print(my_array)  #[ 1  5 11]



