############################### integer ################################
print(1)  # 1
print(100) #100
print(-800) #-800
print(0) #0
print(0xff) #255
print(0xff000) #1044480
#it is difficult to count the number of 0s
print(10000000000) #10000000000
#Python allows _separators between numbers
print(10_000) #10000
print(10_000_000_000) #10000000000
# Hexadecimal numbers can also be written
print(0xa1b2_c3d4) #2712847316
print('\n')
############################## floating point number #######################
print(1.23)  #1.23
print(-9.01) #-9.01
print(1.23e9) #1230000000.0
print(12.3e8) #1230000000.0
print(1.2e-5) #1.2e-05
print('\n')
################################### string ##############################
print('I\'m \"OK\"!') #I'm "OK"!
# Single quote (single quote): '
print('abc') #abc
print(type('abc')) #<class 'str'>
# Double quotes (double quotes): "
print("abc")  #abc
print(type("abc")) #<class 'str'>
# Difference between single and double quotes, both are equal in value
str_sq = 'abc'
str_dq = "abc"
print(str_sq == str_dq) #True
print('\n')
# Different treatment of quotes in strings
# Single quotes (single quotes) and double quotes (double quotes) handle quotes in strings differently.
str_sq = 'a\'b"c'
print(str_sq)  # a'b"c
str_sq = "a'b\"c"
print(str_sq)  # a'b"c
#There is no problem even if you \' write single quotes .
str_sq = "a\'b\"c"
print(str_sq)  # a'b"c


str_sq = 'a\'b"c'
str_dq = "a'b\"c"
print(str_sq == str_dq) #True
print('\n')
#Newline can be written as it is
str_sq = 'abc\nxyz';
print(str_sq)
# abc
# xyz
print('\n')
str_sq = 'abc\\nxyz';
print(str_sq) #abc\nxyz
print('\n')
str_sq = 'abc\\\nxyz';
print(str_sq)
# abc\
# xyz
print('\n')

# Line breaks can be written as they are in strings enclosed in triple quotes.
str_tq = '''abc
xyz'''
print(str_tq)
# abc
# xyz
print('\n')
str_tq = '''abc

        xyz'''
# abc
#
#        xyz
print(str_tq)
print(type(str_tq)) #<class 'str'>
print('\n')

print(r'Hello, "Bart"')
str4 = r'''Hello,
Lisa!'''
print(str4)
print('\n')


# single and double quotes
str_tq_sq = '''\'abc\'
"xyz"'''
print(str_tq_sq)
# 'abc'
# "xyz"
str_tq_dq = """'abc'
\"xyz\""""
print(str_tq_dq)
# 'abc'
# "xyz"
print(str_tq_sq == str_tq_dq)
# True
print('\n')



################################### Boolean value#############################
print(True)  #True
print(False) #False
print(3>2) #True
print(3>=2) #True
print(2<3) #True
print(2>=3) #False
print(2!=3) #True
print(3==3) #True
print('\n')

print(True and True)  #True
print(True and False) #False
print(False and False) #False
print(5>3 and 3 >2) #True
print('\n')

print(True or False)  #True
print(not False) #True
print(not 1 > 2) #True
print('\n')

# Boolean values ​​are often used in conditional judgments, such as:
age = 10
if age >= 18:
    print('adult')
else:
    print('teenager')
print('\n')

# None
print(None)
print(type(None))  #
print('\n')

data = None
if data is None:
    print("It is in fact a None")  #It is in fact a None
else:
    print("No, it is Not None")
print('\n')

# Comparing None with False or True type
data = None
print(data == False)  #False
print(data == True) #False
print('\n')
# Check the type of an object
print(type('string') is str) #True
print(type('string') is int) #False
print('\n')

# variable

__007 = 10
print(__007)  #10
print('\n')
t_007 = 'T007'
print(t_007) #T007
print('\n')
Answer = True
answer = False
print(Answer) #True

a = 123 # a is int
print(a) #123
a = 'ABC' # a changed to ABC
print(a) #ABC
print('\n')

a = 'ABC'
b = a
a = 'XYZ'
print(b)  #ABC
print('\n')

# constant
# constants are usually represented by variable names in all uppercase
PI = 3.14159265359
print(PI)  #ABC

# division
#The result of a division calculation is a floating-point number
print(10/3) #3.3333333333333335
#  There is also a division //, called floor division, where the division of two integers is still integers:
print(10//3) #3
print(10 //3*(3+1)) #12

# remainder 
print ( 3 - - - 1)  # 2
print ( 10 % 2) #0

# Python integers have no size limit, while integers in some languages ​​are limited in size according to their storage lengt
print(99999999999999999999)
print(9999999999999999999_9)
print('\n')

#############################Tips and Tricks#########################
num1 = 10000000000
num2 = 100000000
total = num1 + num2
print(total)  #10100000000

num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(total) #10100000000
print(f'{total:,}')  #10,100,000,000
print(f'{total:_}')  #10_100_000_000