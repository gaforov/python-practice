'''
A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}.
'''
# f-Strings! You can pass formatting options

num = 10
print(f'\n2.25 times {num} is {2.25 * num:.2f}')  # 2 decimals fixed.

for num in range(1, 11):
    print(f'\n2.25 times {num} is {2.25 * num:.2f}')

for num in range(1, 11):
    print(f'{num} divided by 4.0 is {num / 4:.2%}')
