##################################Slice######################################
# Taking part of a list or tuple is a very common operation. For example, a list as follows:
lslice = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(lslice) #['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#Python provides a slice (Slice) operator, which can greatly simplify this operation.
tslice = lslice[0:3]
print(tslice) #['Michael', 'Sarah', 'Tracy']

# L[0:3] Indicates that it is 0 taken from the index 3 up to, but not including, the index 3. 
# i.e. the indices 0, 1, 2, are exactly 3 elements.
tslice = lslice[:3]
print(tslice) #['Michael', 'Sarah', 'Tracy']


#You can also start at index 1 and take out 2 elements:
tslice = lslice[1:3]
print(tslice) #['Sarah', 'Tracy']

tslice = lslice[-1]
print(tslice) #Jack

tslice = lslice[-2:-1]
print(tslice) #['Bob']

tslice = lslice[-2:]
print(tslice) #['Bob', 'Jack']

L = list(range(10))
print(L) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Don't even write anything, just write [:]to copy a list as-is:
print(L[:])#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tuple is also a kind of list, the only difference is that tuple is immutable. 
# Therefore, tuples can also be sliced, but the result of the operation is still a tuple:
print((0, 1, 2, 3, 4, 5)[:3]) #(0, 1, 2)

# Strings 'xxx'can also be regarded as a kind of list, each element is a character. 
# Therefore, strings can also be sliced, but the result of the operation is still a string:
print('ABCDEFG'[:3]) #ABC
print('ABCDEFG'[::3]) #ADG
print('ABCDEFG'[::2]) #ACEG