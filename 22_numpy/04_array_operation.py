# Mathematical operations can be completed using NumPy arrays.

import numpy as np

array_a = np.array([1, 2, 3])
array_b = array_a + 2
print(array_b) #[3 4 5]


array_a = np.array([1, 2, 3])
array_b = np.array([2, 4, 6])
array_c = array_a + array_b
print(array_c) #[3 6 9]



array_a = np.array([1,2,3])
array_b = 3*array_a
print(array_b) #[3 6 9]


array_a = np.array([10,20,30])
array_b = array_a/2
print(array_b) #[ 5. 10. 15.]

#Array Multiplication
#NumPy array can be multiplied by each other using matrix multiplication.
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
array_c = array_a * array_b
print(array_c) #[ 4 10 18]


array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
array_c =np.dot(array_a,array_b)
print(array_c) #32

#Exponents and Logarithms
array_a = np.array([1, 2, 3])
array_b =np.exp(array_a)
print(array_b) #[ 2.71828183  7.3890561  20.08553692]

#Logarithms
#NumPy has three logarithmic functions.
#natural logarithm (log base)
# np.log2() - logarithm base 2
# np.log10() - logarithm base 10

my_result =np.log(np.e)
print(my_result) #1.0

my_result =np.log2(16)
print(my_result) #4.0

my_result =np.log10(1000)
print(my_result) #3.0

#NumPy also contains all of the standard trigonometry functions which operate on arrays.
np.set_printoptions(4)
a = np.array([0, np.pi/4, np.pi/3, np.pi/2])
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))

# [0.     0.7071 0.866  1.    ]
# [1.0000e+00 7.0711e-01 5.0000e-01 6.1232e-17]
# [0.0000e+00 1.0000e+00 1.7321e+00 1.6331e+16]


# NumPy contains functions to convert arrays of angles between degrees and radians.
#deg2rad() - convert from degrees to radians
a = np.array([np.pi,2*np.pi])
print(np.rad2deg(a)) #[180. 360.]

#rad2deg() - convert from radians to degrees
a = np.array([0,90, 180, 270])
print(np.deg2rad(a)) #[0.     1.5708 3.1416 4.7124]

