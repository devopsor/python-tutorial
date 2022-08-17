###############################Conditional Judgment#######################################

#The reason why a computer can do many automated tasks is because it can make conditional judgments on its own.
#For example, enter the user's age, and print different content according to the age. 
# In the Python program, use the ifstatement to achieve:
age = 20
if age >= 18:
    print('your age is', age) #your age is 20
    print('adult') #adult

# According to Python's indentation rules, if the 'if' statement is judged to be true, 
# the indented two-line print statement is executed, otherwise, nothing is done.
# You can also 'if' add a 'else' statement, which means that if 'if' the judgment is yes False, 
# do not execute 'if' the content, and else execute it:
age = 3
if age >= 18:
    print('your age is', age) #
    print('adult')
else:
    print('your age is', age) #your age is 3
    print('teenager') #tennager

# Be careful not to omit the colon :, Of course, the above judgement is very rough, and it can use elif statement
age = 7
if age >= 18:
    print('adult')
elif age >=6:
    print('teenager') #teenager
else:
    print('kid')

# if judgment conditions can also be abbreviated, such as writing:
# As long as it x is a non-zero value, a non-empty string, a non-empty list, etc., 
# it is judged as True, otherwise it is False.
x = 7
if x:
    print('True') #True

##################################revisit input#########################################
# Finally, look at a problematic conditional judgment. Many students will use to input()read the user's input, 
# so that they can enter their own input, and the program runs more interestingly:
birth = input('birth: ')
birth = int(birth)
if birth < 2000:
    print('born before 2000') # born before 2000
else:
    print('born after 2000') # born after 2000


