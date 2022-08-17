########################################BytesIO########################################
#StringIO can only operate on str. If you want to operate binary data, you need to use BytesIO.
#BytesIO implements reading and writing bytes in memory, we create a BytesIO, and then write some bytes:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue()) #b'hello world!'

# read from BytesIO:
data = 'StringIO and BytesIO \nare methods for manipulating\n str and bytes in\n memory\n'.encode('utf-8')
f = BytesIO(data)
print(f.read()) #b'StringIO and BytesIO \nare methods for manipulating\n str and bytes in\n memory\n'

