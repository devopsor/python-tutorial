# Once you have mastered Python's data types, statements, and functions, 
# you can basically write many useful programs.

# For example, constructing a 1, 3, 5, 7, ..., 99list can be achieved by looping:
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 
# 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 
# 91, 93, 95, 97, 99]
# Taking the first half of the elements of the list can also be achieved by looping.

# In Python, more code is not better, but less is better. 
# The more complex the code is not the better, but the simpler the better.


# Based on this idea, let's introduce the very useful advanced features in Python, 
# the functions that can be achieved in 1 line of code, and never write 5 lines of code. 
# Always keep in mind that less code means more efficient development.
