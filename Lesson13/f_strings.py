'''
A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}.
'''

person = 'Said'
coins = 3

# Different ways to print the same message
print('\n' + person + ' has ' + str(coins) + ' coins left.')

message = '\n%s has %s coins left.' % (person, coins)
print(message)

print('\n', person, 'has', coins, 'coins left.')

message = '\n{} has {} coins left.'.format(person, coins)
print(message)

# we flip the parameters and use index to insert values
message = '\n{1} has {0} coins left.'.format(coins, person)
print(message)

message = '\n{person} has {coins} coins left.'.format(coins=coins, person=person)
print(message)

# pulling data from the dictionary and pass to parameters
player = {'person': 'Said', 'coins': 3}

message = '\n{person} has {coins} coins left.'.format(**player)
print(message)

#################
# f-Strings! 
print('\n\n*** f-Strings! ***')

message = f'\n{person} has {coins} coins left.'
print(message)

message = f'\n{person} has {2 * 5} coins left.'
print(message)

message = f'\n{person.upper()} has {coins} coins left.'
print(message)

message = f'\n{player["person"]} has {coins} coins left.'
print(message)

