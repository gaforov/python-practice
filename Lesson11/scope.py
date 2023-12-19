name = 'John'

def greeting1():
    print(name)

def greeting2(name):
    print(name)

def greeting3():
    greeting2('Marry')


greeting1() # name is coming from the global variable, outside definition. 
greeting2('Said') # no longer accessing global varibale, name is retrieved from local definition/function. 
greeting3() # We are calling greeting2 inside greeting3, it is accessible because greeting2() is called in a global scope.
