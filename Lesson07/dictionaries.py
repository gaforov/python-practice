# Dictionaries in Python
fruits = {
    'apple': 'sweet',
    'lemon': 'sour'
}

fruits2 = dict(apple='sweet', lemon='sour')

print(fruits)
print(fruits2)
print(type(fruits))
print(len(fruits2))

# Access items in dictionary
print(fruits['apple'])  # return value of the key
print(fruits.get('lemon')) # return value of the key 2nd way

# Print all keys
print(fruits.keys())
print(fruits.values())

# list of key/value pairs as tuples
print(fruits.items())

# verify if key exits
print('banana' in fruits)
print('apple' in fruits)

# change values
fruits['lemon'] = 'yellow'
fruits.update({'Kiwi':'tropical'})

print(fruits)

# remove items
print(fruits.pop('Kiwi'))
print(fruits)