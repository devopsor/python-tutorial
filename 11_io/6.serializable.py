########################################Pickle########################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In the process of running the program, all variables are in memory, for example, define a dict:
d = dict(name='Bob', age=20, score=88)
# Variables can be modified at any time, such as changing name to 'Bill', but once the program ends, the memory 
# occupied by the variables will be completely reclaimed by the operating system. If the modified version is not 'Bill' 
# stored on disk, the next time the program is re-run, the variable is initialized to 'Bob'.

# The process of changing variables from memory to storable or transferable is called serialization, 
# which is called pickling in Python, and is also called serialization, marshalling, flattening, etc. 
# in other languages, all of which mean the same thing.

# After serialization, the serialized content can be written to disk or transmitted to other machines over the network.
# Conversely, re-reading the variable contents from the serialized object into memory is called deserialization, 
# or unpickling.

# Python provides pickle modules to implement serialization.
import pickle

d = dict(name='Bob', age=20, score=88)

# pickle.dumps() 
# The method serializes any object into one bytes, which can then be byteswritten to a file. 
# Or use another method pickle.dump() to directly serialize the object and write it to a file-like Object:
    
data = pickle.dumps(d)
print(data)
# b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x03age\x94K\x14\x8c\x05score\x94KXu.'

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
#Take a look at the dump.txtfile that was written, a bunch of jumbled stuff, that's all about the internals of objects that 
# Python saves.
 
# When we want to read an object from disk to memory, we can read the content into one first bytes, and then use 
# the pickle.loads() method to deserialize the object, or we can directly use the pickle.load() method to deserialize 
# the object directly from one file-like Object. We open another Python command line to deserialize the object 
# we just saved:
reborn = pickle.loads(data)
print(reborn) # {'name': 'Bob', 'age': 20, 'score': 88}

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

print(d)  #{'name': 'Bob', 'age': 20, 'score': 88}
#The content of the variable is back!

# The problem with Pickle, like all other programming language-specific serialization problems, 
# is that it can only be used with Python, and possibly different versions of Python are not compatible with each other, 
# so pickle can only be used to save data that is not important, and cannot be successfully used. 
# Deserialization doesn't matter.
