for i in range(4):
    print(i)

print('---')
for i in range(2, 4):
    print(i)

print('---')
for i in range(0, 31, 5):
    print(i)
print('Print at the very end')

names = ['John', 'Mike', 'Tom']
actions = ['eats', 'sleeps', 'codes']

print('------')
for name in names:
    for action in actions:
        print(name + " " + action)

print('------')
for action in actions:
    for name in names:
        print(name + " " + action)


