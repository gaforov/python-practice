# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print('Else print:', value)

fruits = ['Apple', 'Orange', 'Kiwi', 'Banana']
for i in fruits:
    print(i)

for x in 'California':
    print(x)

print('---')
for i in fruits:
    if i == 'Kiwi':
        break
    print(i)

print('---')
for i in fruits:
    if i == 'Kiwi':
        continue
    print(i)
