a = 5
try:
    if not type(a) is str:
        raise TypeError('Only strings are allowed.')
except Exception as e:
    print(e)