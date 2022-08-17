################################ Regex ################################ 

# Strings are the most involved data structure in programming, and the need to operate on strings is 
# almost everywhere. 
# For example, to determine whether a string is a legal email address, although you can programmatically 
# extract @ the substrings before and after, and then determine whether it is a word or a domain name, 
# this is not only troublesome, but also difficult to reuse the code.

# Regular expressions are a powerful weapon for matching strings. Its design idea is to use a descriptive 
# language to define a rule for a string. Any string that conforms to the rule is considered to be "matched". 
# Otherwise, the string is illegal.

# So the way we judge whether a string is a valid Email is:
# 1. Create a regular expression that matches Email;
# 2. Use the regular expression to match the user's input to determine whether it is legal.

# Because regular expressions are also represented by strings, we must first understand how to describe 
# characters with characters.

# In a regular expression, if a character is given directly, it is an exact match. With \d can match a number, 
# \w can match a letter or a number, so:
# '00\d' can match '007', but cannot match '00A';
# '\d\d\d' can match '010';
# '\w\w\d' can match 'py3';
# .Can match any character, so: 'py.' Can match 'pyc', 'pyo', 'py!' etc.

# To match a variable-length character, in the regular expression, 
# use * means any number of characters  (including 0), 
# use + means at least one character, 
# use ? means 0 or 1 character, 
# use {n} means n characters, 
# use {n,m}means n to m characters :

# Let's look at a complex example: \d{3}\s+\d{3,8}.
# Let's read from left to right:
# \d{3} means match 3 numbers, for example '010';
# \s It can match a space (including blanks such as Tab), so it \s+ means that there is at least one space, 
#such as matching ' ', ' 'etc.;
# \d{3,8} Represents 3-8 numbers, eg '1234567'.

# Taken together, the above regular expression can match phone numbers with area codes separated by any 
# number of spaces.

# What if you want to match '010-12345' numbers like this? 
# Since it '-' is a special character, in the regular expression, it needs to '\'be escaped, so the above regular 
# is \d{3}\-\d{3,8}.
# However, it still doesn't match '010 - 12345' because it has spaces. So we need more complex matching methods.

#Advanced
# For a more precise match, you can use the [] representation range, for example:
# [0-9a-zA-Z\_] Can match a number, letter or underscore;

# [0-9a-zA-Z\_]+ Can match strings consisting of at least one number, letter or underscore, such as 'a100', '0_Z', 
# 'Py3000' etc.;

# [a-zA-Z\_][0-9a-zA-Z\_]* It can match a string starting with a letter or underscore, followed by any string consisting
# of a number, letter or underscore, which is a legal variable in Python;

# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19} More precisely limits the length of the variable to 1-20 characters (1 character 
# in front + up to 19 characters in back).

# A|B can match either A or B, so (P|p)ython can match 'Python' either 'python'.
# ^ Indicates the beginning of a line, ^\d indicating that it must start with a number.
# $ Indicates the end of the line, \d$ indicating that it must end with a number.

# You may have noticed that py it can also match 'python', but adding ^py$ it becomes a whole line match, 
# and it can only match 'py'.

################################ re module ################################ 

# With the preparation knowledge, we can use regular expressions in Python. Python provides re modules that 
# contain all regular expression functionality.
# Let's first see how to determine whether the regular expression matches:
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

print('Test: 010-12345')  #Test: 010-12345
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))  #010 12345

t = '19:55:30'
print('Test:', t)  #Test: 19:55:30
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())  #('19', '55', '30')

