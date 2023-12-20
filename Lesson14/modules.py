# import math or
from math import pi
import random as rdm
'''In Python, Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program. In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application'''

# print(math.pi)
print(pi)

rdm.choice('123')

for item in dir(rdm):
    print(item)