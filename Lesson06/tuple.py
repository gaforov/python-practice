my_tuple = tuple(('Said', 45, True)) # tuple with constructor ?
tuple2 = (1, 4, 56, 10, 4, 4)

print(my_tuple)
print(tuple2)
print(type(my_tuple))

new_list = list(my_tuple) # creates a new list out of my_tuple
new_list.append('Orange') # we can modify lists but not tuples
new_tuple = tuple(new_list) # we are adding new_list to new_tuple and then printing it. 
print(new_tuple)

(one, two, *hey) = tuple2
print(one)
print(two)
print(hey)

print(tuple2.count(4))