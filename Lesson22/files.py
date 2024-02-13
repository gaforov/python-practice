import os
#  R = Read
#  A = Append
#  W = Write
#  X = Create
#  Similar to CRUD (Create, Read, Update, Delete)

# Read - error if it doesn't exist
# f = open("names.txt", "r") <-- By default it is "r" (read), no need to specify unless different name given
f = open("names.txt")
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())
for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Adam\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("Delete all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# X - Create new file(s)
# (1) - Opens a file for writing, creates the file if ir does not exist.
f = open("name_list.txt", "w")
f.close()

# (2) - Create the specified file, but returns an error if the file exists.
if not os.path.exists("sample.txt"):
    f = open("sample.txt", "x")
    f.close()

# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("sample.txt"): 
    os.remove("sample.txt")
else:
    print("The file you wish to delete does not exist.")

# Copy and paste content from 'more_names' to 'names' file. Replaces data. 
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)