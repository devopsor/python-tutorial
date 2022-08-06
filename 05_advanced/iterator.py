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

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))  #Iterable? [1, 2, 3]: True
print('Iterable? \'abc\':', isinstance('abc', Iterable)) #Iterable? 'abc': True
print('Iterable? 123:', isinstance(123, Iterable)) #Iterable? 123: False
print('Iterable? g():', isinstance(g(), Iterable)) #Iterable? g(): True

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator)) #Iterator? [1, 2, 3]: False
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator)) #Iterator? iter([1, 2, 3]): True     
print('Iterator? \'abc\':', isinstance('abc', Iterator)) #Iterator? 'abc': False
print('Iterator? 123:', isinstance(123, Iterator)) #Iterator? 123: False
print('Iterator? g():', isinstance(g(), Iterator)) #Iterator? g(): True

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

# for x in [1, 2, 3, 4, 5]:
# 1
# 2
# 3
# 4
# 5

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

d = {'a': 1, 'b': 2, 'c': 3}

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

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# iter enumerate(['A', 'B', 'C']      
# 0 A
# 1 B
# 2 C

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
# iter [(1, 1), (2, 4), (3, 9)]:
# 1 1
# 2 4
# 3 9
