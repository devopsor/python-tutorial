# Multiple values stored within an array can be accessed simultaneously with array slicing. 
# To pull out a section or slice of an array, the colon operator : is used when calling the index. 
# The general form is:
# <slice> = <array>[start:stop]

import numpy as np

my_array = np.array([2, 4, 6])
my_slice = my_array[0:2]
print(my_slice) #[2 4]


# On either sides of the colon, a blank stands for "default".
# [:2] corresponds to [start=default:stop=2]
# [1:] corresponds to [start=1:stop=default]
my_array = np.array([2, 4, 6, 8])
print(my_array)  # [2 4 6 8]
my_slice = my_array[1:]
print(my_slice)  # [4 6 8]


my_slice = my_array[:3]
print(my_slice)  #[2 4 6]

#The following indexing operations output the same array.
a = np.array([2, 4, 6, 8])
b = a[0:]
print(b)
c = a[:4]
print(c)
d = a[0:]
print(d)
e = a[:]
print(e)

# Slicing 2D Arrays
# 2D NumPy arrays can be sliced with the general form:
a = np.array([[2, 4, 6, 8], [10, 20, 30, 40]])
print(a)
# [[ 2  4  6  8]
#  [10 20 30 40]]
b = a[0:2, 0:3]
print(b)
# [[ 2  4  6]
#  [10 20 30]]

# Again, a blank represents defaults the first index or the last index. 
# The colon operator all by itself also represents "all" (default start: default stop).
a = np.array([[2, 4, 6, 8], [10, 20, 30, 40]])
b = a[:,:]  #[all rows, all columns]
print(b)
# [[ 2  4  6  8]
#  [10 20 30 40]]