#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y) #Point: 1 2

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q) #deque(['y', 'a', 'b', 'c', 'x'])

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])  #dd['key1'] = abc
print('dd[\'key2\'] =', dd['key2'])  #dd['key2'] = N/A

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)  #Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

