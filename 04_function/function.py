# Function
# Python has a lot of built-in useful functions that we can call directly.
print(abs(-100))
print(abs(-100.3))
print(abs(--+100))
print(abs(+-100))
print('\n')

print(max(1,-00))
print(max(1,2,-3,9))
print('\n')

# Data type conversion
print( int('123'))
print( int(12.34))
print( float('12.34'))
print( str(1.23))
print( str(100))
print( bool(1))
print( bool(''))
print('\n')

# Function alias
# The function name is actually a reference to a function object
#  It is completely possible to assign the function name to a variable, 
# # which is equivalent to giving the function an "alias":
b = abs
print(b(-2))

def fun_abs(x):
    if(x > 0):
        return x
    else:
        return -x
print(fun_abs(-19))
print('\n')

# Empty Function
# Pass Statements do nothing, so what's the use? In fact , it passcan be used as a placeholder. 
# For example, if you haven't figured out how to write the code of the function, 
# you can put one first passso that the code can run.
def nop():
    pass
# If it is missing pass, the code will run with syntax errors.
age = 10
if age > 10:
    pass
else:
    pass

# Parameter Check
def new_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print(new_abs('10'))  #TypeError: bad operand type
print(new_abs(10))
print(new_abs(-10))
print('\n')
#Return Multiple Values
# For example, it is often necessary to move from one point to another in the game, 
# and given the coordinates, displacement and angle, the new coordinates can be calculated:
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
(x, y)= move(100, 100, 60, math.pi / 6)
print(x, y) # 151.96152422706632, 70.0
print(x) #151.96152422706632
print(y) # 70.0
print('\n')


print(math.sqrt(2))