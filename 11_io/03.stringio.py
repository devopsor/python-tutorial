########################################StringIO########################################
#In many cases, data read and write is not necessarily a file, but can also be read and written in memory.
# StringIO, as the name suggests, reads and writes str in memory.
# To write str into StringIO, we need to create a StringIO first, and then write it like a file:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue()) # hello world!

# Read from StringIO:
f = StringIO('StringIO and BytesIO \nare methods for manipulating\n str and bytes in\n memory\n')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
    
# StringIO and BytesIO        
# are methods for manipulating
# str and bytes in
# memory