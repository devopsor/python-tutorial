# Character Encoding
# As we have already said, strings are also a data type, but strings are special in that there is an encoding problem.
# Because computers can only process numbers, if you want to process text, you must first convert the text to numbers before you can process it. 
# The earliest computers were designed with 8 bits as a byte, so the largest integer that a byte can represent is 255 (binary 11111111=decimal 255). 
# If you want to represent a larger integer, more bytes must be used. 
# For example, the largest integer that can be represented by two bytes is 65535, 
# and can be represented by 4 bytes is 4294967295.

# Since the computer was invented by Americans, only 127 characters were encoded into the computer at the earliest, 
# that are uppercase and lowercase English letters, numbers and some symbols. This encoding table is called ASCII encoding. 
# For example A, the encoding of uppercase letters is 65, lowercase letters. z is 122.
# But obviously one byte is not enough to process Chinese, at least two bytes are needed, and it cannot conflict with the ASCII encoding, 
# so China has developed an GB2312 encoding to compile Chinese into it.

# As you can imagine, there are hundreds of languages ​​in the world. Japan has Japanese compiled into Shift_JIS 
# and South Korea has compiled Korean into EUC-KR. Each country has its own standards, and conflicts will inevitably. 
# As a result, in multilingual mixed In the text, there will be garbled characters displayed.

# Therefore, the Unicode character set came into being. Unicode unifies all languages ​​into one encoding, so there will be no more garbled problems.
# The Unicode standard is constantly evolving, but the most commonly used is the UCS-16 encoding, 
# which uses two bytes to represent a character (4 bytes if you want to use very remote characters). 
# Modern operating systems and most programming languages ​​directly support Unicode.

# Now, take a look at the difference between ASCII encoding and Unicode encoding: ASCII encoding is 1 byte, while Unicode encoding is usually 2 bytes.
# Letters A are encoded in ASCII in decimal 65 and binary 01000001;
# Characters 0 are encoded in ASCII, which is decimal 48 and binary 00110000. Note that characters '0' and integers 0 are different;
# Chinese characters 中 have gone beyond the scope of ASCII encoding, and Unicode encoding is decimal 20013 and binary 01001110 00101101.

# You can guess that if you A use Unicode encoding for ASCII encoding, you only need to add 0 in front of it. 
# Therefore, A the Unicode encoding is 00000000 01000001.
# A new problem has appeared again: if it is unified into Unicode encoding, the problem of garbled characters has disappeared since then. 
# However, if the text you write is basically all in English, using Unicode encoding requires twice as much storage space as ASCII encoding, 
# which is very uneconomical in terms of storage and transmission.

# Therefore, to save space, there is an encoding that converts the Unicode encoding into a "variable-length encoding" UTF-8. 
# UTF-8 encoding encodes a Unicode character into 1-6 bytes according to different number sizes, commonly used English letters are encoded into 1 byte, 
# Chinese characters are usually 3 bytes, and only very rare characters will be encoded. Encoded into 4-6 bytes. 
# If the text you want to transfer contains a lot of English characters, encoding in UTF-8 can save space:

# It can also be found from the above table that UTF-8 encoding has an additional benefit, 
# that is, ASCII encoding can actually be regarded as a part of UTF-8 encoding, so a large number of historical legacy software 
# that only supports ASCII encoding can be used in UTF- 8 code to continue working.

# After figuring out the relationship between ASCII, Unicode and UTF-8, 
# we can summarize the working methods of character encoding commonly used in computer systems:
# In the computer memory, the Unicode encoding is uniformly used, and when it needs to be saved to the hard disk or needs to be transmitted, 
# it is converted to UTF-8 encoding.

################################Python strings###################################################################
# After figuring out the headache of character encoding, let's study Python strings.
# In the latest Python 3 version, strings are encoded in Unicode, that is, Python's strings support multiple languages, for example:
print('こんにちは')  #こんにちは

# For the encoding of a single character, Python provides a ord() function to obtain the integer representation of the character, 
# and the chr()function converts the encoding to the corresponding character:
print(ord('A'))  #65
print(ord('中')) #20013
print(chr(66)) #B
print(chr(25991)) #文
print( '\u4e2d\u6587') #中文
print('\n')
# Since Python's string type is str represented in Unicode in memory, 
# one character corresponds to several bytes. If you want to transfer it over the network, or save it to disk, 
# you need to strchange it to bytes bytes.

# Python uses prefixed single or double quotes bytes for data of types :b
print( 'ABC'.encode('ascii'))  # b'ABC'
print( '日本語'.encode('utf-8')) # b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'
# print( '中文'.encode('ascii'))   // error
print('\n')

# Pure English str can be ASCII coded as bytes, the content is the same, 
# and Chinese str can be UTF-8 coded as bytes. Codes containing Chinese str cannot be used ASCII, 
# because the range of Chinese codes exceeds the range of ASCIIcodes, and Python will report an error.
print(b'ABC'.decode('ascii'))  #ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  #中文
print('\n')
# If bytes are only a small fraction of invalid bytes , you can pass errors='ignore' in the ignoring bytes:
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))  // UnicodeDecodeError
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')) #中
print('\n')

# To count characters in a string, you can use the len()function:
print(len('abc')) #3
print(len(b'ABC')) #3
# It can be seen that 1 Chinese character usually occupies 3 bytes after UTF-8 encoding
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) #6
print(len(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))) #2
print(len('中文')) #2
print('\n')

######################################Format#############################################
print( 'Hello,%s' % 'world') #Hello, world
print( 'Hi, %s, you have $%d.' % ('Michael', 1000000)) #Hi, Michael, you have $1000000.
print('\n')
# As you might guess, % operators are used to format strings. Inside the string, 
# %s it means to replace it with a string, 
# %d it means to replace it with an integer, there are several %? placeholders, followed by several variables or values, 
# and the order should correspond well. If there is only one %?, the parentheses can be omitted.
print('%2d-%02d' % (3, 1)) # 3-01
print('%02d-%2d' % (3, 1)) #03- 1
print('%.2f' % 3.1415926) #3.14
print('\n')

print('Age: %s. Gender: %s' % (25, True)) #Age: 25. Gender: True
print( 'growth rate: %d%%' % 7) #growth rate: 7%
print( 'Hello, {0}, 成绩提升了 {1:.2f}%'.format('小李', 17.125)) #Hello, 小李, 成绩提升了 17.12%
print('\n')

###################################### f-string ######################################
# The last way to format a string is to use fa string that starts with, call it f-string, 
# it differs from a normal string in that if the string contains {xxx}, it will be replaced with the corresponding variable:
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}') #The area of a circle with radius 2.5 is 19.62
