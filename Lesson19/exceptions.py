# print(a) # <-- NameError exception raised(throws)

# Catching the exception
try:
    print(b)
except:
    print('\nThere is an error')


print('---------------\n')

# Catching the exception in more specific way
try:
    print(c)
except NameError as e: # 'as e' part is optional if you want to print default message. 
    print('NameError means something probably is not defined OR Name is not defined inside paranthesis')
    print(e)


print('\n---------------\n')
# Zero devision error, exception when dividing any number by zero
x = 10
try:
    print(x/0)
except ZeroDivisionError as exception:
    print('Cannot divide by zero')
    print(exception) # prints default message
except Exception:
    print("Catch errors other than 'divede by zero'")
else:
    print('No errors!')
finally:
    print('Finally block (always) prints whether error occurs or not.\n')

