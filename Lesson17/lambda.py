def squared(num): return num * num
# lambda num : num * num


print(squared(3))


def addTwo(num): return num + 2
# lambda num : num + 2


print(addTwo(10))


def sum(a, b): return a + b
# lambda a, b : a + b


print(sum(2, 3))


# Building fucntions using lambda
def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

# The following could've been achieved using loops, but with lambda functions can be done in 1 line.
numbers = [3, 5, 7, 19, 21, 66, 50]
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

# Filters
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print("Odd numbers:", list(odd_nums))
even_nums = filter(lambda num: num % 2 == 0, numbers)
print("Even numbers:", list(even_nums))

