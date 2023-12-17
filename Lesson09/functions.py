def hello():
    print('\nHello world!')


hello()


def sum(num1, num2):
    print(num1 + num2)


sum(2, 4)
sum(10, 20)

# using 'return' with functions, returning funcitons


def sum(num1, num2=10):
    if (type(num1) is not int or type(num2) is not int):
        # just return works too, or return 0
        return 'both num1 and num2 must be integer data types'
    return num1 + num2


print(sum(10, 5))
# if you miss an argument, default value from the definition will be used
print(sum(10))
print(sum(10, 5.3))
print(sum(10, 'A'))


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items('Said', 'Tom', 35, True)


def multiple_items2(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_items2(first='John', last='Doe')
