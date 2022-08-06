###############################Cycle#######################################
# To calculate 1+2+3, we can write the expression directly:
print(1+2+3)

# To calculate 1+2+3+...+10, I can barely write it.
# However, to calculate 1+2+3+...+10000, it is impossible to write the expression directly.
# In order for a computer to compute thousands of repetitions, we need loops.
# There are two kinds of loops in Python. One is the for...in loop, which iterates each element in the list or tuple in turn. 
# See the example:
names = ['Michael','Bob','Tracy']
for name in names:
    print(name)
# Michael
# Bob
# Tracy
print('\n')

# So the for x in ...loop is to substitute each element into the variable x and then execute the statement of the indented block.
# For another example, if we want to calculate the sum of integers from 1 to 10, we can use a sum variable to accumulate:
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum) #55
print('\n')

# If you want to calculate the sum of integers from 1-100, it is a bit difficult to write from 1 to 100. 
# Fortunately, Python provides a range() function that can generate a sequence of integers, 
# which can then list() be converted to a list through the function. 
# For example range(5), the generated sequence is an integer starting from 0 and less than 5:
print(range(5))  # range(0, 5)
print(list(range(5))) #[0, 1, 2, 3, 4]

sum = 0
for i in range(5):
    sum+=i
print(sum) #10
print('\n')

sum = 0
for i in list(range(5)):
    sum+=i
print(sum) #10
print('\n')

sum = 0
for x in range(101):
    sum = sum + x
print(sum) #5050
print('\n')

# The second kind of loop is the while loop. As long as the conditions are met, it will continue to loop, 
# and when the conditions are not met, it will exit the loop. 
# For example, if we want to calculate the sum of all odd numbers within 100, we can use a while loop to achieve:
sum = 0
count = 100
while count >0:
    sum+=count
    count-=1
print(sum)#5050
print('\n')

#######################################break########################################
# In a loop, a breakstatement can exit the loop early. For example, to print the numbers from 1 to 100 in a loop:
n = 1
while n <= 100:
    if n > 10: # when n = 11, the condition is met and the break statement is executed
        break # break statement will end the current loop
    print(n)
    n = n + 1
print('END')
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# END
# Execute the above code, you can see that after printing 1~10, it is printed immediately END, and the program ends.
# The visible break effect is to end the loop early.

#######################################continue########################################
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # If n is even, execute the continue statement
        # The continue statement will directly continue to the next cycle of the loop, 
        # and the subsequent print() statement will not be executed
        continue 
    print(n)
#Execute the above code, you can see that the print is no longer 1 to 10, but 1, 3, 5, 7, 9.
