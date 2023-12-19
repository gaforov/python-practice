name = 'John'
fruit = 'Pear'
count = 1


def greeting2(name):
    def greeting1(): # variables of inner function will not print at its current form/syntax. 
        fruit = 'orange'
        print(fruit)
    print(name)

def greeting3():
    # fruit = 'apple' # local variable is preferred, if I comment out this, variable fruit value from global will be used. 
    print(fruit)
    global count  # not good practice, not recommended
    count += 2
    print(count)
    greeting2('Marry')

print('-----')
# greeting1() # greeting1 is no longer accessible because it is called inside another function, its local now. 
greeting2('Said') # name is accessible because of indentation. belongs to outer function, not inner. 
greeting3() # We are calling greeting2 inside greeting3, it is accessible because greeting2() is called in a global scope.

def greeting4(name):
    fruit = 'Banana'
    color = 'Red'
    def greeting1(): 
        nonlocal color # reference variable from the upper scope. comment this out, upper scope 'color' will gray out. 
        color = 'Blue' # this is reference (re-assigning value) from line 27. 
        print(color)
        print(fruit)
        print(name)
    greeting1() # we need to call the inner function inside outer function.

print('\n------')
greeting4('Tester')