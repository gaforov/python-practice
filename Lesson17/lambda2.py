from functools import reduce

# acc = accumulator(subtotal), curr = current (current item)

numbers = [1, 2, 3, 4, 10, 15]

total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)

# another example: Higher order runction
names = ['John Doe', 'Sara Conner', 'Ford Henry']
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count) # it appears spaces between strings are counted as well