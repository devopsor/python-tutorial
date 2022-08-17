########################################Read/Write Files########################################
#Reading and writing files is the most common IO operation. Python has built-in functions for reading and writing files, 
# and its usage is compatible with C.

# Before reading and writing files, we must first understand that the functions of reading and writing files 
# on the disk are provided by the operating system. 
# Modern operating systems do not allow ordinary programs to directly operate the disk. Therefore, 
# reading and writing files is to request the operating system to open a file. A file object (usually called a file descriptor), 
# and then, through the interface provided by the operating system, data is read from this file object (read file), 
# or data is written to this file object (write file).


###################################### Read File ##########################################


# To open a file object in file-reading mode, use Python's built-in open() functions, passing in the file name and 
# identifier:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# Writing a file is the same as reading a file, the only difference is that open() when calling the function, 
# an identifier is passed in 'w' either 'wb' to write a text file or a binary file:
with open('test.txt', 'w') as f:
    f.write('Today is  ')
    f.write(datetime.now().strftime('%Y-%m-%d'))
    f.close()

# To open a file object in file-reading mode, use Python's built-in open() functions, 
# passing in the file name and identifier:
with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)
# The identifier 'r' means read, so we have successfully opened a file.

#To read binary files, such as pictures, videos, etc., 'rb' open the file with mode:
with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('今日は')
    f.write(datetime.now().strftime('%Y-%m-%dです'))
    f.close()
with open('test.txt', 'r',encoding='utf-8') as f:
    s = f.read()
    print('読み込み中...')
    print(s)
# The outputs are as follows:

# $ python 2.readwrite.py
# open for read...
# Today is  2022-08-11      
# open as binary for read...
# b'Today is  2022-08-11'   
# 読み込み中...
# 今日は2022-08-11です 
