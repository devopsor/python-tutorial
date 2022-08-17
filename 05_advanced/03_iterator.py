##################################Iterate######################################
# In Python, iteration is done through for ... in, and in many languages, such as C, 
# iteration listis done through subscripts, such as C code:
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

# An Iterable is basically an object that any user can iterate over. 
# We can generate an iterator when we pass the object to the iter() method.
iterate = isinstance([1, 2, 3], Iterable)
print('Iterable? [1, 2, 3]:', iterate)  #Iterable? [1, 2, 3]: True

iterate = isinstance('abc', Iterable)
print('Iterable? \'abc\':', iterate) #Iterable? 'abc': True

iterate =  isinstance(123, Iterable)
print('Iterable? 123:', iterate) #Iterable? 123: False

iterate = isinstance(g(), Iterable)
print('Iterable? g():', iterate) #Iterable? g(): True


# Iterator is also an object that helps a user in iterating over another object (that is iterable※). 
# We use the __next__() method for iterating. 

iterate = isinstance([1, 2, 3], Iterator)
print('Iterator? [1, 2, 3]:', iterate) #Iterator? [1, 2, 3]: False

iterate = isinstance(iter([1, 2, 3]), Iterator)
print('Iterator? iter([1, 2, 3]):', iterate) #Iterator? iter([1, 2, 3]): True     

iterate = isinstance('abc', Iterator)
print('Iterator? \'abc\':', iterate) #Iterator? 'abc': False

iterate = isinstance(123, Iterator)
print('Iterator? 123:', iterate) #Iterator? 123: False

iterate = isinstance(g(), Iterator)
print('Iterator? g():',iterate) #Iterator? g(): True
print('\n')

# iter list:
iterate = isinstance([1, 2, 3, 4, 5], Iterable)
print(iterate)  #True
iterate = isinstance([1, 2, 3, 4, 5], Iterator)
print(iterate) #False
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

# for x in [1, 2, 3, 4, 5]:
# 1
# 2
# 3
# 4
# 5
print('\n')

iterate = isinstance(iter([1, 2, 3, 4, 5]), Iterable)
print(iterate)  #True
iterate = isinstance(iter([1, 2, 3, 4, 5]), Iterator)
print(iterate) #True
print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)
# for x in iter([1, 2, 3, 4, 5]):     
# 1
# 2
# 3
# 4
# 5

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# next():
# 1
# 2
# 3
# 4
# 5
print('\n')

d = {'a': 1, 'b': 2, 'c': 3}
iterate = isinstance(d, Iterable)
print(iterate)  #True
iterate = isinstance(d, Iterator)
print(iterate) #False

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)
#iter key: {'a': 1, 'b': 2, 'c': 3}  
# key: a
# key: b
# key: c

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter value: {'a': 1, 'b': 2, 'c': 3}
# value: 1
# value: 2
# value: 3

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)
# iter item: {'a': 1, 'b': 2, 'c': 3} 
# item: a 1
# item: b 2
# item: c 3
print('\n')

# iter list with index:
iterate = isinstance(['A', 'B', 'C'], Iterable)
print(iterate)  #True
iterate = isinstance(['A', 'B', 'C'], Iterator)
print(iterate) #False

print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# iter enumerate(['A', 'B', 'C']      
# 0 A
# 1 B
# 2 C
print('\n')

# iter complex list:
iterate = isinstance([(1, 1), (2, 4), (3, 9)], Iterable)
print(iterate)  #True
iterate = isinstance([(1, 1), (2, 4), (3, 9)], Iterator)
print(iterate) #False

print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
# iter [(1, 1), (2, 4), (3, 9)]:
# 1 1
# 2 4
# 3 9
