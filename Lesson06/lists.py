users = ['Said', 'John', 'Anne', 'Michael', 'Tom']
data = ['Johnson', 43, True]
empty_list = []

print('Said' in users)
print(users[0])
print(users[-1]) # last in the list, -2 will print 2nd last and so on...
print(users[0:3]) # first three in the list. 0, 1, 2 (until 3, 3 being exclusive)
print(users[2:]) # start priting with index of 2 and after
print(users[-3:-1]) #Anne is -3 (counting backwards, last index being -1) and Michael is -2 in above list. Thus, Anne & Michael gets printed. 

print('data list length:', len(data))
users.append('Joseph')

users += ['Tester']
print(users)

data.extend(['50', 'Apple'])
print(data)

data.insert(0, 'Kiwi')
print(data)

data.remove(43)
print(data)

data.pop()
print(data)

del data[1]
print(data)

data.clear()
print(data)

# del data
# print(data)  #Error because list 'data' does not exist at this line. 

# Replacing a specific index with new list item. When you sort, lowercase Stings go to very end. 
print(users)
users[1:2] = ['said']
print(users)
users.sort()
print(users)

users.sort(key=str.lower) # by using this syntax, we include lower case into sorting. Use same data types when sorting. This wouldn't work on mixed data types. 
print(users)