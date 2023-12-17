numbers = [4, 45, 78, 1, 10]
numbers.reverse()
print(numbers) # reverse print

numbers.sort()
print(numbers)

numbers.sort(reverse=True) # reverse sort, larger to smaller. 
print(numbers) 

print(sorted(numbers, reverse=True)) # will print the same as above except original list not modified(sorted). Global sorted() function used. 

print('Cpying list different ways: ')
numbers2 = numbers.copy()
numbers3 = list(numbers)
numbers4 = numbers[:]

print(numbers)
print(numbers2)
numbers3.sort()
print(numbers3)
print(numbers4)
print(type(numbers))